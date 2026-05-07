"""Generate a comprehensive index report (Markdown) from download status TSV."""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

DOWNLOAD_DIR = Path(__file__).parent
STATUS_FILE = DOWNLOAD_DIR / "_download_status.tsv"
INDEX_FILE = DOWNLOAD_DIR / "INDEX.md"


def load_status():
    rows = []
    with open(STATUS_FILE, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for r in reader:
            rows.append(r)
    return rows


def main():
    rows = load_status()
    by_journal = defaultdict(list)
    for r in rows:
        by_journal[r["journal"]].append(r)

    total = len(rows)
    downloaded = sum(1 for r in rows if r["status"] in ("ok", "exists"))
    failed = total - downloaded

    lines = []
    lines.append("# TAVI 併發症 Case Reports — 下載索引")
    lines.append("")
    lines.append("**搜尋來源**：JACC Case Reports、JACC Cardiovascular Interventions、")
    lines.append("Circulation Cardiovascular Interventions、Circulation Cardiovascular Imaging")
    lines.append("")
    lines.append("**搜尋詞**：`(TAVR OR TAVI OR \"transcatheter aortic valve\") AND (complication OR complications)`，限定為 `Case Reports`")
    lines.append("")
    lines.append(f"**總計**：{total} 篇 — **成功下載 {downloaded} 篇 PDF** ({downloaded*100/total:.1f}%)，**未下載 {failed} 篇** (付費牆或 Europe PMC 尚未索引的最新文章)")
    lines.append("")
    lines.append("**檔名格式**：`PMID_FirstAuthor_Year.pdf`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-journal summary
    lines.append("## 各期刊統計")
    lines.append("")
    lines.append("| 期刊 | 總計 | 成功下載 | 未下載 |")
    lines.append("|------|------|---------|--------|")
    for journal in sorted(by_journal.keys()):
        items = by_journal[journal]
        ok_count = sum(1 for x in items if x["status"] in ("ok", "exists"))
        no_count = len(items) - ok_count
        lines.append(f"| {journal} | {len(items)} | {ok_count} | {no_count} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed listing per journal
    for journal in sorted(by_journal.keys()):
        lines.append(f"## {journal}")
        lines.append("")
        items = by_journal[journal]
        # Sort by year desc, then by author
        items.sort(key=lambda x: (-int(x["year"] or 0), x["author"], x["pmid"]))

        # Downloaded first
        ok_items = [x for x in items if x["status"] in ("ok", "exists")]
        no_items = [x for x in items if x["status"] not in ("ok", "exists")]

        if ok_items:
            lines.append(f"### ✓ 已下載 ({len(ok_items)})")
            lines.append("")
            lines.append("| 年 | First Author | 標題 | PDF | DOI |")
            lines.append("|----|-------------|------|-----|-----|")
            for r in ok_items:
                doi_link = f"[{r['doi']}](https://doi.org/{r['doi']})" if r["doi"] else "-"
                title = r["title"].replace("|", "\\|")[:120]
                lines.append(f"| {r['year']} | {r['author']} | {title} | `{r['filename']}` | {doi_link} |")
            lines.append("")

        if no_items:
            lines.append(f"### ✗ 未下載 ({len(no_items)}) — 請至 DOI 連結手動下載")
            lines.append("")
            lines.append("| 年 | First Author | 標題 | DOI / PubMed |")
            lines.append("|----|-------------|------|--------------|")
            for r in no_items:
                doi_link = f"[{r['doi']}](https://doi.org/{r['doi']})" if r["doi"] else f"[PMID {r['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{r['pmid']}/)"
                title = r["title"].replace("|", "\\|")[:120]
                lines.append(f"| {r['year']} | {r['author']} | {title} | {doi_link} |")
            lines.append("")

        lines.append("---")
        lines.append("")

    INDEX_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Index written: {INDEX_FILE}")
    print(f"Total: {total}, Downloaded: {downloaded}, Failed: {failed}")


if __name__ == "__main__":
    main()
