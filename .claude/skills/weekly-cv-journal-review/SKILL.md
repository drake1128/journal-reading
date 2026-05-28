---
name: weekly-cv-journal-review
description: Generate the dedicated Weekly Cardiology Journal Review handout (markdown), Marp slide deck, and PDF for the past 7 days across 6 core journals (NEJM, Lancet, EHJ, JACC family, Circulation family, EuroIntervention). Use when Drake (謝慕揚醫師) says "每週期刊文獻回顧", "weekly CV review", "weekly cardiology journal review", "journal review (cardiology)", or "期刊文獻回顧". Output goes to handouts/91-podcast-journal-review/. CRITICAL: every "其他焦點/Other highlights" table in Marp slides MUST include a 連結 column with clickable DOI hyperlinks so colleagues can jump to the source article.
---

# Weekly Cardiology Journal Review Skill

Produce a comprehensive weekly review covering the **past 7 days** of cardiology literature from **6 core journals**, with one handout + one Marp deck + one PDF.

## Trigger phrases

- "每週期刊文獻回顧"
- "weekly CV review"
- "weekly cardiology journal review"
- "journal review (cardiology)"
- "期刊文獻回顧"
- "幫我整理最近這一週心臟科的期刊"

## Journals (6 total)

| Group | Journals to search |
|-------|-------------------|
| **General medicine** | NEJM, Lancet (CV-related original articles + editorials) |
| **European Heart Journal** | All original articles + editorials |
| **JACC family** | J Am Coll Cardiol, JACC Cardiovasc Interv, JACC Heart Fail, JACC Cardiovasc Imaging, JACC Clin Electrophysiol |
| **Circulation family** | Circulation, Circ Cardiovasc Interv, Circ Heart Fail, Circ Cardiovasc Imaging, Circ Arrhythm Electrophysiol, Circ Genom Precis Med |
| **EuroIntervention** | All articles |

## Output specification

Always produce **3 files** named with the run date (today, YYYY-MM-DD):

| File | Purpose |
|------|---------|
| `Weekly_CV_Journal_Review_YYYY-MM-DD 教學講義.md` | Long-form handout |
| `Weekly_CV_Journal_Review_YYYY-MM-DD_Marp.md` | Marp slide source |
| `Weekly_CV_Journal_Review_YYYY-MM-DD.pdf` | Compiled slide deck |

**No PPTX, no LaTeX**, no any other format. Move all 3 files to `handouts/91-podcast-journal-review/`.

## Workflow (numbered, follow in order)

### 1. Confirm date window
- Today is the run date
- Date range = past **7 days** (today minus 7 → today)
- Express as `YYYY/MM/DD` for PubMed `dateRange` filter

### 2. Search PubMed for each journal in parallel

Use `mcp__pubmed__pubmed_search_articles` with `dateType: "pdat"` and request `summaryCount` so you get titles + DOIs in one call. Five queries, run in **parallel** (single message, multiple tool calls):

```text
Query 1 (NEJM):
  "N Engl J Med"[Journal] AND (cardiovascular OR cardiology OR coronary OR heart OR aortic OR atrial OR ventricular OR stroke OR hypertension)

Query 2 (Lancet):
  "Lancet"[Journal] AND (cardiovascular OR cardiology OR coronary OR heart OR aortic OR atrial OR ventricular OR stroke OR hypertension)

Query 3 (EHJ):
  "Eur Heart J"[Journal]

Query 4 (JACC family):
  ("J Am Coll Cardiol"[Journal] OR "JACC Cardiovasc Interv"[Journal] OR "JACC Heart Fail"[Journal] OR "JACC Cardiovasc Imaging"[Journal] OR "JACC Clin Electrophysiol"[Journal])

Query 5 (Circulation family):
  ("Circulation"[Journal] OR "Circ Cardiovasc Interv"[Journal] OR "Circ Heart Fail"[Journal] OR "Circ Cardiovasc Imaging"[Journal] OR "Circ Arrhythm Electrophysiol"[Journal] OR "Circ Genom Precis Med"[Journal])

Query 6 (EuroIntervention):
  "EuroIntervention"[Journal]
```

Set `maxResults: 30-50`, `sort: "pub_date"`, `summaryCount: 30-50`.

If a journal returns 0 hits, note explicitly in the handout (e.g., "本週 Lancet **無心血管原始研究**").

### 3. Fetch full abstracts for top picks

After scanning titles, identify ~5-10 top picks (priority: original RCTs > major observational > editorials > reviews). Use `mcp__pubmed__pubmed_fetch_articles` with `pmids: [...]`.

If the result file exceeds the token limit, the harness will save it to disk — use Python (`pypdf` or `json`) to parse and extract the abstracts.

### 4. **VERIFY trial results via WebSearch** (CRITICAL)

For every major trial in the top picks, **do NOT trust the abstract alone**. Use `WebSearch` to confirm:
- Primary endpoint result (HR/RR/win ratio + 95% CI + P-value)
- Whether the trial was POSITIVE / NEGATIVE / NEUTRAL
- Cross-check against tctmd.com, ACC.org, Cardiology Today, Medscape

**Why this matters**: Negative/neutral trials are easy to misread as positive from abstract phrasing. Past example: CHIP-BCIS3 (Perera et al., NEJM 2026, ehae784-era timeframe) was clearly NEGATIVE (win ratio 0.85, P=0.30) with a HARM signal (CV death 26.7% vs 14.5%) — but a careless abstract read could miss this.

### 5. Write the handout markdown

Structure:

```markdown
# 每週心血管期刊文獻回顧 — YYYY-MM-DD ~ YYYY-MM-DD

**整理：謝慕揚 MD, PhD, FESC**
**日期：YYYY-MM-DD**
**涵蓋期刊**：NEJM、Lancet、European Heart Journal、JACC family、Circulation family、EuroIntervention

---

## 目錄
1. [本週重點摘要 (Top 5 Picks)](#1-本週重點摘要-top-5-picks)
2. [NEJM](#2-nejm)
3. [European Heart Journal](#3-european-heart-journal)
4. [JACC Family](#4-jacc-family)
5. [Circulation Family](#5-circulation-family)
6. [EuroIntervention](#6-eurointervention)
7. [Lancet](#7-lancet)
8. [縮寫對照](#8-縮寫對照)
9. [參考文獻](#9-參考文獻)

---

## 1. 本週重點摘要 (Top 5 Picks)

| # | 試驗 / 主題 | 期刊 | 結果方向 | One-line summary |
|---|------------|------|---------|-----------------|
| 1 | ... | ... | ✅ Positive / ❌ Negative / 💡 Concept-shift | ... |

> **Pearl of the Week**：[一句話總結本週主題]

---

[Per-journal sections with detail tables for top picks + "其他焦點" tables for the rest]

---

## 9. 參考文獻

[Vancouver style with DOI hyperlinks]
```

**Per top pick**: dedicate a subsection with a 2-column table (項目 / 內容) covering 設計, 族群, primary endpoint, 結果, 安全性, take home.

**Per "其他焦點" table**: 3 columns: `主題 | 摘要 | 連結`. The 連結 cell uses PubMed (`[PMID xxxxx](https://pubmed.ncbi.nlm.nih.gov/xxxxx/)`) or DOI (`[DOI](https://doi.org/...)`) — **never leave it empty**.

### 6. Write the Marp slide deck

Use the standard project Marp YAML front-matter (see `.claude/SKILL.md` for the full CSS block). Footer: `'謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | YYYY-MM-DD'`.

Slide order:
1. Title slide (`<!-- _class: lead -->`)
2. **本週主題** — one-line characterization of the week
3. **Top 5 Picks 一覽** — single-table overview with key numbers
4. NEJM divider + per-paper detail slides
5. EHJ divider + per-paper detail slides + **其他焦點 (1/2)** + **其他焦點 (2/2)**
6. JACC divider + per-paper detail slides + **JACC — 高敏 Troponin & 演算法** + **JACC — 其他**
7. Circulation divider + per-paper detail slides + **Circulation 其他焦點**
8. EuroIntervention divider + per-paper detail slides + **EuroIntervention 其他焦點**
9. **整合 Take Home** divider
10. **本週 5 大臨床啟示** (Pearls 1-5)
11. **縮寫對照** (`<!-- _class: small-text -->`)
12. **參考文獻** (`<!-- _class: ref -->`, may need 2-3 slides)
13. **謝謝聆聽 / Q&A** (`<!-- _class: lead -->`)

### 7. ⚠️ CRITICAL — Every "其他焦點/Other highlights" Marp table MUST have a 連結 column

This is the **most important** rule of this skill. Slide tables that list multiple secondary articles MUST be 3 columns:

```markdown
| 主題 | 重點 | 連結 |
|------|------|------|
| **CARDIO-TTRansform Phase 3** | Eplontersen 治療 ATTR-CM design paper | [DOI](https://doi.org/10.1161/CIRCHEARTFAILURE.126.014205) |
| **Stellate ganglion 光療治 VT** | 非侵入性神經調節 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.125.078175) |
```

**Why**: The slide PDF is shared with colleagues. Without a clickable link, they cannot jump to the source article. **NEVER ship a Marp table with the 主題 + 重點 columns alone — always include 連結 with a working DOI hyperlink.**

For per-paper detail slides (single-paper, 2-column 項目/內容 tables), the link goes in the slide's H2 subtitle: `## [Author, et al. Journal YYYY](https://doi.org/...)`.

### 8. Compile PDF and move files

```bash
marp --no-stdin "Weekly_CV_Journal_Review_YYYY-MM-DD_Marp.md" \
     --pdf -o "Weekly_CV_Journal_Review_YYYY-MM-DD.pdf" \
     --allow-local-files

mv "Weekly_CV_Journal_Review_YYYY-MM-DD 教學講義.md" handouts/91-podcast-journal-review/
mv "Weekly_CV_Journal_Review_YYYY-MM-DD_Marp.md"     handouts/91-podcast-journal-review/
mv "Weekly_CV_Journal_Review_YYYY-MM-DD.pdf"         handouts/91-podcast-journal-review/
```

Always pass `--no-stdin` (Marp will hang on stdin otherwise).

## Top 5 Picks selection criteria

In priority order:
1. **Original RCTs** (positive AND negative — both deserve coverage)
2. **Pivotal observational studies** changing practice
3. **Major guideline updates / consensus documents**
4. **Editorials** that frame multiple papers
5. **Concept-shifting reviews / first-in-human** studies

Mix 結果方向 markers in the Top 5 table:
- ✅ Positive
- ❌ Negative (with `+ harm signal` if mortality/safety worse)
- 💡 Concept-shift / observation
- ➰ Early feasibility / design paper

Always include at least one negative trial if available — drawing attention to "what didn't work" is one of the highest-value functions of the review.

## Reference list (參考文獻)

Group by journal in this order: NEJM, EHJ, JACC, Circulation, EuroIntervention, plus 「補充（外部報導）」for tctmd.com / ACC.org links used during verification.

Vancouver format with DOI link in the citation:

```markdown
1. Author1, Author2, et al. Title. [*Journal*. Year;Vol(Issue):Pages.](https://doi.org/DOI)
```

If only PMID is available:
```markdown
1. Author1, et al. Title. [*Journal*. Year.](https://pubmed.ncbi.nlm.nih.gov/PMID/)
```

## Author attribution and framing

- Always: `謝慕揚 MD, PhD, FESC`
- For Gmail draft (separate skill / subsequent step): Drake is **讀書會共筆整理人** (reading-group note-taker), NOT 精選專家. Include a disclaimer footer.

## Quality checklist before delivery

- [ ] Date window confirmed (past 7 days as of run date)
- [ ] All 6 journals searched (or "no results" noted explicitly)
- [ ] Top 5 Picks table populated with 結果方向 markers
- [ ] **Every Marp 「其他焦點」 table has a 連結 column with DOI hyperlinks** ⚠️
- [ ] Per-paper detail slides have DOI/PubMed link in H2 subtitle
- [ ] Major trials verified via WebSearch (not just abstract)
- [ ] Negative/neutral trials labeled with ❌ or NS clearly
- [ ] Drug names in English (never translate)
- [ ] Reference list grouped by journal with hyperlinks
- [ ] Marp CSS: no Google Fonts import, no gradients, no custom divs
- [ ] PDF compiled with `--no-stdin --allow-local-files`
- [ ] All 3 files moved to `handouts/91-podcast-journal-review/`
- [ ] Original abstract sources discarded after parsing (no leftover .pdf in repo root)

## Cross-references

- General journal-reading conventions: `.claude/SKILL.md`
- Marp template: `.claude/assets/marp-template.md`
- Handout template: `.claude/assets/handout-template.md`
- DOI verification patterns: `.claude/references/doi-verification.md`
- Table examples (incl. 連結 column): `.claude/references/table-examples.md`
- Project workflow specs: `CLAUDE.md` → 「每週心血管期刊文獻回顧」section
