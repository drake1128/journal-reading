"""Fetch full-text PDFs for the "High-Risk Intervention: Communication & Ownership" review.

Strategy per DOI:
  1. NCBI ID Converter  -> PMID / PMCID
  2. Europe PMC render  -> PDF (works for anything in PMC OA/author-manuscript)
  3. Unpaywall          -> any OA location with url_for_pdf
  4. Hard-coded known-free publisher URLs (BMJ, author-hosted preprints, etc.)

Anything still missing is reported so it can be pulled through institutional access.
"""
from __future__ import annotations

import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

UNPAYWALL_EMAIL = "drake1128@gmail.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
}
OUT = Path(__file__).parent

# ref_no, slug, DOI, extra direct-URL candidates (tried last)
REFS = [
    (1,  "Baron_1988_OutcomeBias_JPSP", "10.1037/0022-3514.54.4.569",
     ["https://www.sas.upenn.edu/~baron/papers/outcome.pdf"]),
    (2,  "Caplan_1991_OutcomeEffect_JAMA", "10.1001/jama.1991.03460150061024", []),
    (3,  "Resnic_2009_PublicHealthHazards_JACC", "10.1016/j.jacc.2008.11.034",
     ["https://www.jacc.org/doi/pdf/10.1016/j.jacc.2008.11.034"]),
    (4,  "Joynt_2012_PublicReportingPCI_JAMA", "10.1001/jama.2012.12922", []),
    (5,  "Waldo_2015_PublicReportingAMI_JACC", "10.1016/j.jacc.2015.01.008", []),
    (6,  "Gupta_2016_ImplicationsPublicReporting_JACCIntv", "10.1016/j.jcin.2016.08.012", []),
    (7,  "Wadhera_2018_PublicReportingPCI_JAMACardio", "10.1001/jamacardio.2018.0947", []),
    (8,  "Riley_2020_SCAI_ComplexPCI_CCI", "10.1002/ccd.28994",
     ["https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/ccd.28994"]),
    (9,  "Naidu_2021_SCAI_CathLabBestPractices_CCI", "10.1002/ccd.29744",
     ["https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/ccd.29744"]),
    (10, "Haynes_2009_SurgicalSafetyChecklist_NEJM", "10.1056/NEJMsa0810119",
     ["https://www.nejm.org/doi/pdf/10.1056/NEJMsa0810119"]),
    (11, "Taylor_2017_BestCaseWorstCase_JAMASurg", "10.1001/jamasurg.2016.5674", []),
    (12, "Schwarze_2010_SurgicalBuyIn_CCM", "10.1097/CCM.0b013e3181cc466b", []),
    (13, "Schillinger_2003_ClosingTheLoop_ArchIntMed", "10.1001/archinte.163.1.83", []),
    (14, "Glaser_2020_InformedConsentComprehension_MDM", "10.1177/0272989X19896348", []),
    (15, "Schenker_2011_InformedConsentComprehension_MDM", "10.1177/0272989X10364247", []),
    (16, "Levinson_1997_CommunicationMalpractice_JAMA", "10.1001/jama.1997.03540310051034", []),
    (17, "Gallagher_2003_DisclosureMedicalErrors_JAMA", "10.1001/jama.289.8.1001", []),
    (18, "Wu_2000_SecondVictim_BMJ", "10.1136/bmj.320.7237.726",
     ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1117748/pdf/726.pdf",
      "https://www.bmj.com/content/bmj/320/7237/726.full.pdf"]),
]


def get(url, **kw):
    kw.setdefault("timeout", 60)
    kw.setdefault("headers", HEADERS)
    kw.setdefault("allow_redirects", True)
    return requests.get(url, **kw)


def try_download(url: str, dest: Path) -> tuple[bool, str]:
    try:
        with get(url, stream=True) as r:
            if r.status_code != 200:
                return False, f"HTTP {r.status_code}"
            data = b""
            for chunk in r.iter_content(16384):
                data += chunk
                if len(data) > 60 * 1024 * 1024:
                    return False, "too large"
            if not data.startswith(b"%PDF"):
                return False, f"not PDF ({r.headers.get('Content-Type','?')[:28]})"
            dest.write_bytes(data)
            return True, f"{len(data)//1024} KB"
    except Exception as e:
        return False, f"{type(e).__name__}: {str(e)[:60]}"


def id_convert(dois: list[str]) -> dict[str, dict]:
    """DOI -> {pmid, pmcid} via NCBI ID Converter (batches of 200)."""
    out: dict[str, dict] = {}
    url = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
    for i in range(0, len(dois), 50):
        batch = dois[i:i + 50]
        try:
            r = get(url, params={"ids": ",".join(batch), "format": "json",
                                 "tool": "journal-reading", "email": UNPAYWALL_EMAIL})
            for rec in r.json().get("records", []):
                key = (rec.get("doi") or "").lower()
                out[key] = {"pmid": rec.get("pmid", ""), "pmcid": rec.get("pmcid", "")}
        except Exception as e:
            print(f"  idconv batch failed: {e}")
        time.sleep(0.4)
    return out


def pmid_from_esearch(doi: str) -> str:
    try:
        r = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
                params={"db": "pubmed", "term": f"{doi}[DOI]", "retmode": "json"})
        ids = r.json().get("esearchresult", {}).get("idlist", [])
        return ids[0] if ids else ""
    except Exception:
        return ""


def unpaywall_urls(doi: str) -> list[str]:
    try:
        r = get(f"https://api.unpaywall.org/v2/{doi}", params={"email": UNPAYWALL_EMAIL}, timeout=30)
        if r.status_code != 200:
            return []
        d = r.json()
        urls: list[str] = []
        for loc in ([d.get("best_oa_location")] + (d.get("oa_locations") or [])):
            if not loc:
                continue
            for k in ("url_for_pdf", "url"):
                u = loc.get(k)
                if u and u not in urls:
                    urls.append(u)
        return urls
    except Exception:
        return []


def process(ref) -> dict:
    no, slug, doi, extra = ref
    dest = OUT / f"{no:02d}_{slug}.pdf"
    res = {"no": no, "slug": slug, "doi": doi, "file": dest.name,
           "pmid": "", "pmcid": "", "status": "MISSING", "method": "", "detail": ""}

    if dest.exists() and dest.stat().st_size > 20000:
        res.update(status="OK", method="cached", detail=f"{dest.stat().st_size//1024} KB")
        return res

    ids = IDS.get(doi.lower(), {})
    res["pmid"] = ids.get("pmid", "") or pmid_from_esearch(doi)
    res["pmcid"] = ids.get("pmcid", "") or ""

    tried = []

    # 1) Europe PMC
    if res["pmcid"]:
        for u in (f"https://europepmc.org/articles/{res['pmcid']}?pdf=render",
                  f"https://www.ncbi.nlm.nih.gov/pmc/articles/{res['pmcid']}/pdf/"):
            ok, d = try_download(u, dest)
            if ok:
                res.update(status="OK", method="EuropePMC/PMC", detail=d)
                return res
            tried.append(f"PMC:{d}")

    # 2) Unpaywall
    for u in unpaywall_urls(doi):
        ok, d = try_download(u, dest)
        if ok:
            res.update(status="OK", method="Unpaywall", detail=d)
            return res
        tried.append(f"UPW:{d}")

    # 3) hand-picked direct URLs
    for u in extra:
        ok, d = try_download(u, dest)
        if ok:
            res.update(status="OK", method="direct", detail=d)
            return res
        tried.append(f"direct:{d}")

    res["detail"] = " | ".join(tried[:4]) or "no candidate URL"
    return res


if __name__ == "__main__":
    dois = [r[2] for r in REFS]
    print("Resolving DOI -> PMID/PMCID …", flush=True)
    IDS = id_convert(dois)
    print(f"  resolved {sum(1 for v in IDS.values() if v.get('pmcid'))} PMCIDs "
          f"/ {len(IDS)} records\n", flush=True)

    results = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        futs = {pool.submit(process, r): r for r in REFS}
        for f in as_completed(futs):
            r = f.result()
            results.append(r)
            flag = "OK  " if r["status"] == "OK" else "MISS"
            print(f"[{flag}] {r['no']:02d} {r['slug'][:52]:52s} {r['method']:14s} {r['detail'][:70]}",
                  flush=True)

    results.sort(key=lambda x: x["no"])
    (OUT / "_status.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    ok = [r for r in results if r["status"] == "OK"]
    print(f"\n=== {len(ok)}/{len(results)} downloaded ===")
    for r in results:
        if r["status"] != "OK":
            print(f"  MISSING {r['no']:02d} {r['slug']}  PMID={r['pmid'] or '-'} PMCID={r['pmcid'] or '-'}")
