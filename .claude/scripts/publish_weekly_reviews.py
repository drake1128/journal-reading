#!/usr/bin/env python3
"""Publish the CV weekly / Critical Care biweekly reviews to the Quarto site.

For every `<Series>_YYYY-MM-DD 教學講義.md` it builds
    <slug-dir>/index.qmd  =  YAML front matter
                             + (optional) <slug-dir>/_letter.md   ← Gmail 導讀信 (Markdown)
                             + the handout body
The Quarto listing pages (`weekly-cv-review.qmd`, `critical-care-biweekly-review.qmd`)
pick the pages up automatically — no `_quarto.yml` edit needed per week.

Usage:
    python3 .claude/scripts/publish_weekly_reviews.py            # all series
    python3 .claude/scripts/publish_weekly_reviews.py cv         # one series
    python3 .claude/scripts/publish_weekly_reviews.py cc 2026-09-01

Letters: convert a saved Gmail htmlBody with gmail_letter_to_md.py and drop it
in the slug dir as _letter.md (done once per week; the file is committed).
"""
import re, sys, glob, os, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SERIES = {
    "cv": dict(
        dir=ROOT / "handouts/91-podcast-journal-review",
        glob="*CV_Journal_Review_*教學講義.md",
        slug="weekly-cv-review-{date}",
        category="每週心血管期刊文獻回顧",
        subtitle_default="Weekly Cardiovascular Journal Review",
    ),
    "cc": dict(
        dir=ROOT / "handouts/10-icu-general",
        glob="Critical_Care_Biweekly_Review_*教學講義.md",
        slug="critical-care-biweekly-review-{date}",
        category="Critical Care 雙週期刊回顧",
        subtitle_default="Biweekly Critical Care Literature Review",
    ),
}

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def yaml_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def split_handout(md: str):
    """Return (title, subtitle, body) with the leading H1 and the 目錄 block removed."""
    lines = md.splitlines()
    title = subtitle = None
    out = []
    i = 0
    # leading H1
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        title = lines[i][2:].strip()
        i += 1
    # optional "## Weekly ... ｜ range" subtitle right after the H1
    j = i
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j < len(lines) and lines[j].startswith("## ") and (
        "Review" in lines[j] or "｜" in lines[j] or "|" in lines[j]
    ) and not lines[j].startswith("## 目錄"):
        subtitle = lines[j][3:].strip()
        i = j + 1
    body = lines[i:]
    # drop the "## 目錄" section (Quarto renders its own TOC; hand-written anchors won't match)
    cleaned, skipping = [], False
    for ln in body:
        if ln.startswith("## 目錄") or ln.startswith("## 📑 目錄") or ln.strip() in ("## 目錄 Contents",):
            skipping = True
            continue
        if skipping and ln.startswith("## "):
            skipping = False
        if skipping:
            continue
        cleaned.append(ln)
    # collapse leading/trailing rules
    text = "\n".join(cleaned).strip()
    text = re.sub(r"^(---\s*\n)+", "", text)
    return title, subtitle, text


BORING = re.compile(r"僅供|共筆整理人|交叉去重|不重覆|不重複|資料來源|git push|檔案位置|本文件|本講義為")


def _clean(c: str) -> str:
    c = re.sub(r"\*\*|__|`|\[|\]\([^)]*\)|\\$", "", c).strip().rstrip("\\").strip()
    c = re.sub(r"^[>\s]*[🔥🎯📌🔍⭐💡📋]*\s*", "", c)
    return (c[:150] + "…") if len(c) > 150 else c


def pick_description(letter: str | None, body: str) -> str:
    """One-line teaser. Order: letter 本週主題 paragraph → handout 🔍/📌 blockquote →
    first Pearl / Top-5 pick. Disclaimers and de-duplication notes are skipped."""
    cands: list[str] = []
    src = letter or ""
    for m in re.finditer(r"(?:本週主題|本週主軸|本期主題|本週定位)[：:]?\s*([^\n]{12,})", src):
        cands.append(m.group(1))
    for m in re.finditer(r"(?:本週主題|本週主軸|本期主題)[^\n]*\n+([^\n#|>][^\n]{20,})", src):
        cands.append(m.group(1))
    for m in re.finditer(r"^>\s*(?:🔍|📌|\*\*)?\s*([^\n]{20,})", body, flags=re.M):
        cands.append(m.group(1))
    for m in re.finditer(r"(?:Pearl 1|Pearl of the Week|\*\*1\.)\s*[—–:：-]?\s*([^\n]{20,})", src + "\n" + body):
        cands.append(m.group(1))
    m = re.search(r"^\|\s*1\s*\|\s*\*\*([^|]+?)\*\*", body, flags=re.M)
    if m:
        cands.append("Top pick：" + m.group(1))
    for c in cands:
        c = _clean(c)
        if len(c) >= 12 and not BORING.search(c):
            return c
    return ""


def build(series: str, only_date: str | None = None) -> list[str]:
    cfg = SERIES[series]
    made = []
    for src in sorted(cfg["dir"].glob(cfg["glob"])):
        m = DATE_RE.search(src.name)
        if not m:
            continue
        date = m.group(1)
        if only_date and date != only_date:
            continue
        slug_dir = cfg["dir"] / cfg["slug"].format(date=date)
        slug_dir.mkdir(exist_ok=True)
        md = src.read_text(encoding="utf-8")
        title, subtitle, body = split_handout(md)
        title = title or src.stem.replace(" 教學講義", "")
        letter_path = slug_dir / "_letter.md"
        letter = letter_path.read_text(encoding="utf-8").strip() if letter_path.exists() else None
        desc = pick_description(letter, body)
        page_title = f"{title.split(' / ')[0].strip()} — {date}"
        fm = [
            "---",
            f"title: {yaml_str(page_title)}",
        ]
        if subtitle:
            fm.append(f"subtitle: {yaml_str(subtitle)}")
        fm += [
            f"date: {date}",
            "author: \"謝慕揚 MD, PhD, FESC（讀書會共筆整理人）\"",
            f"description: {yaml_str(desc)}",
            f"categories: [{yaml_str(cfg['category'])}]",
            "lang: zh-TW",
            "toc: true",
            "toc-depth: 3",
            "toc-expand: 2",
            "number-sections: false",
            "format:",
            "  html:",
            "    page-layout: article",
            "---",
            "",
        ]
        parts = ["\n".join(fm)]
        parts.append(
            f"::: {{.callout-note appearance=\"minimal\" icon=false}}\n"
            f"**原始講義**：[`{src.name}`](../{src.name.replace(' ', '%20')})　｜　"
            f"整理：謝慕揚 MD, PhD, FESC　｜　本頁由 `publish_weekly_reviews.py` 自動產生\n:::\n"
        )
        if letter:
            parts.append("## 📬 本週導讀信\n")
            parts.append("::: {.letter}\n" + letter + "\n:::\n")
        parts.append("## 📖 完整教學講義\n")
        parts.append(body + "\n")
        (slug_dir / "index.qmd").write_text("\n".join(parts), encoding="utf-8")
        made.append(str(slug_dir.relative_to(ROOT)))
    return made


if __name__ == "__main__":
    args = sys.argv[1:]
    which = [args[0]] if args else list(SERIES)
    only = args[1] if len(args) > 1 else None
    for s in which:
        for p in build(s, only):
            print("wrote", p + "/index.qmd")
