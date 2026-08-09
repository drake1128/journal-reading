"""Convert fetched PMC full-text XML -> readable Markdown, and pull PubMed
structured abstracts for the references whose full text is paywalled.

Outputs one .md per reference plus INDEX.md.
"""
from __future__ import annotations

import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

OUT = Path(__file__).parent
UA = {"User-Agent": "journal-reading/1.0 (mailto:drake1128@gmail.com)"}

# no, slug, DOI, PMID, citation
REFS = [
    (1,  "Baron_1988_OutcomeBias_JPSP", "10.1037/0022-3514.54.4.569", "3367280",
     "Baron J, Hershey JC. Outcome bias in decision evaluation. J Pers Soc Psychol. 1988;54(4):569-579."),
    (2,  "Caplan_1991_OutcomeEffect_JAMA", "10.1001/jama.1991.03460150061024", "2008024",
     "Caplan RA, Posner KL, Cheney FW. Effect of outcome on physician judgments of appropriateness of care. JAMA. 1991;265(15):1957-1960."),
    (3,  "Resnic_2009_PublicHealthHazards_JACC", "10.1016/j.jacc.2008.11.034", "19264236",
     "Resnic FS, Welt FGP. The public health hazards of risk avoidance associated with public reporting of risk-adjusted outcomes in coronary intervention. J Am Coll Cardiol. 2009;53(10):825-830."),
    (4,  "Joynt_2012_PublicReportingPCI_JAMA", "10.1001/jama.2012.12922", "23047360",
     "Joynt KE, Blumenthal DM, Orav EJ, Resnic FS, Jha AK. Association of public reporting for PCI with utilization and outcomes among Medicare beneficiaries with AMI. JAMA. 2012;308(14):1460-1468."),
    (5,  "Waldo_2015_PublicReportingAMI_JACC", "10.1016/j.jacc.2015.01.008", "25790884",
     "Waldo SW, McCabe JM, O'Brien C, Kennedy KF, Joynt KE, Yeh RW. Association between public reporting of outcomes with procedural management and mortality for patients with AMI. J Am Coll Cardiol. 2015;65(11):1119-1126."),
    (6,  "Gupta_2016_ImplicationsPublicReporting_JACCIntv", "10.1016/j.jcin.2016.08.012", "27765301",
     "Gupta A, Yeh RW, Tamis-Holland JE, et al. Implications of public reporting of risk-adjusted mortality following PCI. JACC Cardiovasc Interv. 2016;9(20):2077-2085."),
    (7,  "Wadhera_2018_PublicReportingPCI_JAMACardio", "10.1001/jamacardio.2018.0947", "29800962",
     "Wadhera RK, Joynt Maddox KE, Yeh RW, Bhatt DL. Public reporting of PCI outcomes. JAMA Cardiol. 2018;3(7):635-640."),
    (8,  "Riley_2020_SCAI_ComplexPCI_CCI", "10.1002/ccd.28994", "32406991",
     "Riley RF, Henry TD, Mahmud E, et al. SCAI position statement on optimal PCI therapy for complex coronary artery disease. Catheter Cardiovasc Interv. 2020;96(2):346-362."),
    (9,  "Naidu_2021_SCAI_CathLabBestPractices_CCI", "10.1002/ccd.29744", "33909349",
     "Naidu SS, Abbott JD, Bagai J, et al. SCAI expert consensus update on best practices in the cardiac catheterization laboratory. Catheter Cardiovasc Interv. 2021;98(2):255-276."),
    (10, "Haynes_2009_SurgicalSafetyChecklist_NEJM", "10.1056/NEJMsa0810119", "19144931",
     "Haynes AB, Weiser TG, Berry WR, et al. A surgical safety checklist to reduce morbidity and mortality in a global population. N Engl J Med. 2009;360(5):491-499."),
    (11, "Taylor_2017_BestCaseWorstCase_JAMASurg", "10.1001/jamasurg.2016.5674", "28146230",
     "Taylor LJ, Nabozny MJ, Steffens NM, et al. A framework to improve surgeon communication in high-stakes surgical decisions: Best Case/Worst Case. JAMA Surg. 2017;152(6):531-538."),
    (12, "Schwarze_2010_SurgicalBuyIn_CCM", "10.1097/CCM.0b013e3181cc466b", "20048678",
     "Schwarze ML, Bradley CT, Brasel KJ. Surgical 'buy-in': the contractual relationship between surgeons and patients that influences decisions regarding life-supporting therapy. Crit Care Med. 2010;38(3):843-848."),
    (13, "Schillinger_2003_ClosingTheLoop_ArchIntMed", "10.1001/archinte.163.1.83", "12523921",
     "Schillinger D, Piette J, Grumbach K, et al. Closing the loop: physician communication with diabetic patients who have low health literacy. Arch Intern Med. 2003;163(1):83-90."),
    (14, "Glaser_2020_InformedConsentComprehension_MDM", "10.1177/0272989X19896348", "31948345",
     "Glaser J, Nouri S, Fernandez A, et al. Interventions to improve patient comprehension in informed consent for medical and surgical procedures: an updated systematic review. Med Decis Making. 2020;40(2):119-143."),
    (15, "Schenker_2011_InformedConsentComprehension_MDM", "10.1177/0272989X10364247", "20357225",
     "Schenker Y, Fernandez A, Sudore R, Schillinger D. Interventions to improve patient comprehension in informed consent for medical and surgical procedures: a systematic review. Med Decis Making. 2011;31(1):151-173."),
    (16, "Levinson_1997_CommunicationMalpractice_JAMA", "10.1001/jama.1997.03540310051034", "9032162",
     "Levinson W, Roter DL, Mullooly JP, Dull VT, Frankel RM. Physician-patient communication: the relationship with malpractice claims among primary care physicians and surgeons. JAMA. 1997;277(7):553-559."),
    (17, "Gallagher_2003_DisclosureMedicalErrors_JAMA", "10.1001/jama.289.8.1001", "12597752",
     "Gallagher TH, Waterman AD, Ebers AG, Fraser VJ, Levinson W. Patients' and physicians' attitudes regarding the disclosure of medical errors. JAMA. 2003;289(8):1001-1007."),
    (18, "Wu_2000_SecondVictim_BMJ", "10.1136/bmj.320.7237.726", "10720336",
     "Wu AW. Medical error: the second victim. BMJ. 2000;320(7237):726-727."),
]

# Hand-written stand-ins for references that have no abstract anywhere
# (society position statements typically don't carry one).
NOTES = {
    8: """_SCAI position statement 沒有結構式 abstract（PubMed 與 Crossref 皆無）。_

官方摘要與相關資源：
- SCAI 文件頁：https://www.scai.org/publications/clinical-documents/scai-position-statement-optimal-interventional-therapy-complex

文件涵蓋：complex CAD 的術前解剖與臨床複雜度評估（含 higher-risk clinical
features）、hemodynamic support 的使用時機、CTO／calcified lesion／left main 的
操作策略，以及達成 optimal outcome 所需的流程規劃 —— 即本 review 中「術前風險
分層」與「bail-out 規劃」兩項能力的主要文獻依據。

> 需要逐段引用時請從 Wiley 下載全文 PDF（見上方 DOI 連結）。""",
}

GROUPS = {
    "結果偏誤 (Outcome Bias)": [1, 2],
    "公開績效報告與風險趨避的個案選擇": [3, 4, 5, 6, 7],
    "高風險個案的流程、退場條件與治理": [8, 9, 10],
    "高風險決策溝通與知情理解": [11, 12, 13, 14, 15, 16],
    "併發症後的揭露與術者本身的承擔": [17, 18],
}


# ---------- PMC XML -> Markdown ----------

def node_text(el) -> str:
    parts = []
    if el.text:
        parts.append(el.text)
    for c in el:
        tag = c.tag
        inner = node_text(c)
        if tag in ("italic", "underline"):
            parts.append(f"*{inner}*" if inner else "")
        elif tag == "bold":
            parts.append(f"**{inner}**" if inner else "")
        elif tag == "xref":
            parts.append(f"[{inner}]")
        elif tag in ("sup",):
            parts.append(f"^{inner}")
        elif tag in ("sub",):
            parts.append(f"_{inner}")
        else:
            parts.append(inner)
        if c.tail:
            parts.append(c.tail)
    return "".join(parts)


def clean(s: str) -> str:
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\s+([,.;:)])", r"\1", s)
    return s.strip()


def render_table(tw) -> list[str]:
    lines = []
    cap = tw.find(".//caption")
    if cap is not None:
        lines.append(f"**Table.** {clean(node_text(cap))}")
        lines.append("")
    for tbl in tw.findall(".//table"):
        rows = tbl.findall(".//tr")
        if not rows:
            continue
        grid = [[clean(node_text(c)).replace("|", "/") for c in r.findall("./th") + r.findall("./td")]
                for r in rows]
        width = max(len(r) for r in grid)
        for i, r in enumerate(grid):
            r += [""] * (width - len(r))
            lines.append("| " + " | ".join(r) + " |")
            if i == 0:
                lines.append("|" + "---|" * width)
        lines.append("")
    return lines


def walk(el, depth: int, out: list[str]):
    for child in el:
        t = child.tag
        if t == "sec":
            title = child.find("./title")
            if title is not None:
                out.append("")
                out.append("#" * min(depth + 1, 6) + " " + clean(node_text(title)))
                out.append("")
            walk(child, depth + 1, out)
        elif t == "title":
            continue
        elif t == "p":
            txt = clean(node_text(child))
            if txt:
                out.append(txt)
                out.append("")
        elif t == "list":
            for li in child.findall("./list-item"):
                out.append("- " + clean(node_text(li)))
            out.append("")
        elif t == "table-wrap":
            out.extend(render_table(child))
        elif t == "fig":
            cap = child.find(".//caption")
            lab = child.find("./label")
            out.append(f"> **{clean(node_text(lab)) if lab is not None else 'Figure'}.** "
                       f"{clean(node_text(cap)) if cap is not None else ''}")
            out.append("")
        else:
            walk(child, depth, out)


def xml_to_md(path: Path) -> tuple[str, str]:
    root = ET.parse(path).getroot()
    art = root.find(".//article") or root
    abs_parts: list[str] = []
    for ab in art.findall(".//front//abstract"):
        walk(ab, 2, abs_parts)
    body_parts: list[str] = []
    body = art.find(".//body")
    if body is not None:
        walk(body, 1, body_parts)
    return "\n".join(abs_parts).strip(), "\n".join(body_parts).strip()


# ---------- PubMed abstract ----------

def pubmed_abstract(pmid: str) -> str:
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=" + pmid)
    try:
        raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
    except Exception as e:
        return f"_(PubMed fetch failed: {e})_"
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        return f"_(PubMed parse failed: {e})_"
    out = []
    for ab in root.findall(".//Abstract/AbstractText"):
        label = ab.get("Label")
        txt = clean(node_text(ab))
        if not txt:
            continue
        out.append(f"**{label}.** {txt}" if label else txt)
        out.append("")
    if not out:
        return "_(No abstract in PubMed.)_"
    return "\n".join(out).strip()


def main():
    index_rows = {}
    for no, slug, doi, pmid, cite in REFS:
        xml = OUT / f"{no:02d}_{slug}.fulltext.xml"
        pdf = OUT / f"{no:02d}_{slug}.pdf"
        md = OUT / f"{no:02d}_{slug}.md"

        abstract, body = "", ""
        if xml.exists():
            try:
                abstract, body = xml_to_md(xml)
            except Exception as e:
                print(f"  {no:02d} XML parse error: {e}")
        if not abstract:
            abstract = pubmed_abstract(pmid)
            time.sleep(0.4)
        if abstract.startswith("_(No abstract") and no in NOTES:
            abstract = NOTES[no]

        if body:
            status, note = "FULLTEXT", "PMC full text (XML → Markdown)"
        elif pdf.exists():
            status, note = "PDF", f"PDF on disk ({pdf.stat().st_size // 1024} KB)"
        else:
            status, note = "ABSTRACT", "abstract only — full text behind paywall"

        parts = [
            f"# [{no}] {cite}", "",
            f"- **DOI**: https://doi.org/{doi}",
            f"- **PubMed**: https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            f"- **狀態**: {status} — {note}", "",
            "---", "", "## Abstract", "", abstract, "",
        ]
        if body:
            parts += ["---", "", "## Full text", "", body, ""]
        md.write_text("\n".join(parts), encoding="utf-8")
        index_rows[no] = (slug, doi, pmid, cite, status, note, pdf.exists())
        print(f"{no:02d} {status:9s} {slug[:48]:48s} {len(body.split()):5d} body words")

    # INDEX.md
    lines = [
        "# High-Risk Intervention — Communication & Ownership：文獻全文庫", "",
        "為「高風險介入的溝通與承擔」詳細 review 所蒐集的 18 篇文獻。", "",
        "| 狀態 | 意義 |",
        "|------|------|",
        "| `FULLTEXT` | 有完整全文（PMC XML → Markdown），可直接引用內文細節 |",
        "| `PDF` | 有正式排版 PDF 檔 |",
        "| `ABSTRACT` | 只有摘要，全文在付費牆後，需院內訂閱下載 |", "",
        "---", "",
    ]
    for group, nos in GROUPS.items():
        lines += [f"## {group}", "",
                  "| # | 文獻 | 狀態 | 檔案 | 連結 |",
                  "|---|------|------|------|------|"]
        for no in nos:
            slug, doi, pmid, cite, status, note, has_pdf = index_rows[no]
            files = [f"`{no:02d}_{slug}.md`"]
            if has_pdf:
                files.append(f"`{no:02d}_{slug}.pdf`")
            for supp in sorted(OUT.glob(f"{no:02d}[a-z]_*.pdf")):
                files.append(f"`{supp.name}` (官方投影片組)")
            lines.append(
                f"| {no} | {cite} | `{status}` | {'<br>'.join(files)} | "
                f"[DOI](https://doi.org/{doi}) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/{pmid}/) |")
        lines.append("")

    missing = [n for n, v in index_rows.items() if v[4] == "ABSTRACT"]
    if missing:
        lines += ["---", "", "## 需要院內訂閱補下載", "",
                  "以下文獻的出版社擋掉了程式化下載（Cloudflare / 付費牆）。"
                  "在院內網路或用機構帳號從下列連結手動下載後，"
                  f"把檔案放進本資料夾並命名為 `NN_Slug.pdf` 即可：", ""]
        for no in missing:
            slug, doi, pmid, cite, *_ = index_rows[no]
            lines.append(f"{no}. {cite}")
            lines.append(f"   - https://doi.org/{doi}　→ 存成 `{no:02d}_{slug}.pdf`")
        lines.append("")
    (OUT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nINDEX.md written. ABSTRACT-only: {missing}")


if __name__ == "__main__":
    main()
