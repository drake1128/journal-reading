"""Download PDFs for TAVI complication case reports.

Strategy:
1. Articles with PMC ID -> Try Europe PMC first (works for older articles)
2. Try Unpaywall url_for_pdf (rare for Elsevier OA)
3. Save abstract metadata as fallback for articles that can't be downloaded
"""
from __future__ import annotations

import csv
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

UNPAYWALL_EMAIL = "drake1128@gmail.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}
DOWNLOAD_DIR = Path(__file__).parent
META_FILE = DOWNLOAD_DIR / "_metadata_all.tsv"
STATUS_FILE = DOWNLOAD_DIR / "_download_status.tsv"


def safe_filename(s: str, max_len: int = 80) -> str:
    s = re.sub(r"[^A-Za-z0-9_\-]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s[:max_len]


def try_download(url: str, dest: Path, referer: str | None = None) -> tuple[bool, str]:
    headers = dict(HEADERS)
    if referer:
        headers["Referer"] = referer
    try:
        with requests.get(url, headers=headers, timeout=60, stream=True, allow_redirects=True) as r:
            if r.status_code != 200:
                return False, f"HTTP {r.status_code}"
            chunks = []
            total = 0
            for chunk in r.iter_content(8192):
                chunks.append(chunk)
                total += len(chunk)
                if total > 50 * 1024 * 1024:
                    return False, "too large"
            data = b"".join(chunks)
            if not data.startswith(b"%PDF"):
                ct = r.headers.get("Content-Type", "")[:30]
                return False, f"not PDF ({ct})"
            dest.write_bytes(data)
            return True, f"{len(data)//1024} KB"
    except Exception as e:
        return False, f"err {type(e).__name__}: {str(e)[:50]}"


def europe_pmc_pdf(pmc: str, dest: Path) -> tuple[bool, str]:
    pmc_num = pmc.replace("PMC", "")
    url = f"https://europepmc.org/articles/PMC{pmc_num}?pdf=render"
    return try_download(url, dest)


def unpaywall_pdf(doi: str, dest: Path) -> tuple[bool, str]:
    if not doi:
        return False, "no DOI"
    try:
        r = requests.get(
            f"https://api.unpaywall.org/v2/{doi}",
            params={"email": UNPAYWALL_EMAIL},
            timeout=30,
            headers=HEADERS,
        )
        if r.status_code != 200:
            return False, f"Unpaywall HTTP {r.status_code}"
        data = r.json()
        # Try all locations with url_for_pdf
        urls = []
        best = data.get("best_oa_location") or {}
        if best.get("url_for_pdf"):
            urls.append(best["url_for_pdf"])
        for loc in (data.get("oa_locations") or []):
            u = loc.get("url_for_pdf")
            if u and u not in urls:
                urls.append(u)
        if not urls:
            return False, "Unpaywall: no PDF URL"
        for u in urls:
            ok, detail = try_download(u, dest)
            if ok:
                return True, f"Unpaywall {detail}"
        return False, f"Unpaywall: tried {len(urls)} URLs, all failed"
    except Exception as e:
        return False, f"Unpaywall err: {type(e).__name__}"


def process_one(row: dict) -> dict:
    pmid = row["pmid"]
    pmc = row["pmc"]
    doi = row["doi"]
    year = row["year"]
    author = row["author"]

    fname = f"{pmid}_{safe_filename(author)}_{year}.pdf"
    dest = DOWNLOAD_DIR / fname

    result = {"pmid": pmid, "filename": fname}

    if dest.exists() and dest.stat().st_size > 1000:
        return {**result, "status": "exists", "method": "-", "detail": f"{dest.stat().st_size//1024} KB"}

    # Step 1: Europe PMC if PMC ID
    if pmc:
        ok, detail = europe_pmc_pdf(pmc, dest)
        if ok:
            return {**result, "status": "ok", "method": "EuropePMC", "detail": detail}
        epmc_detail = detail
    else:
        epmc_detail = "no PMC"

    # Step 2: Unpaywall
    ok, detail = unpaywall_pdf(doi, dest)
    if ok:
        return {**result, "status": "ok", "method": "Unpaywall", "detail": detail}

    return {**result, "status": "no_pdf", "method": "-", "filename": "",
            "detail": f"EPMC: {epmc_detail} | UPW: {detail}"}


def main():
    rows = []
    with open(META_FILE, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for r in reader:
            if len(r) < 7:
                continue
            rows.append({
                "pmid": r[0], "pmc": r[1], "doi": r[2],
                "journal": r[3], "year": r[4], "author": r[5], "title": r[6],
            })

    print(f"Processing {len(rows)} articles…", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(process_one, row): row for row in rows}
        done = 0
        for fut in as_completed(futures):
            res = fut.result()
            row = futures[fut]
            res["journal"] = row["journal"]
            res["year"] = row["year"]
            res["author"] = row["author"]
            res["doi"] = row["doi"]
            res["title"] = row["title"]
            results.append(res)
            done += 1
            if done % 10 == 0 or res["status"] == "ok":
                print(f"[{done}/{len(rows)}] {res['pmid']} {row['year']}: {res['status']} ({res['method']}) - {res['detail']}",
                      flush=True)

    results.sort(key=lambda x: (x["status"] != "ok", x["status"], int(x["year"]), x["pmid"]))
    with open(STATUS_FILE, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["pmid", "status", "method", "filename", "journal", "year", "author", "doi", "title", "detail"])
        for r in results:
            w.writerow([r["pmid"], r["status"], r["method"], r["filename"],
                        r["journal"], r["year"], r["author"], r["doi"], r["title"], r["detail"]])

    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print("\n=== Summary ===")
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
