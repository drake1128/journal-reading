# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository creates bilingual (Traditional Chinese with English medical terminology) educational documents from medical literature. Documents are prepared for 謝慕揚醫師 (Drake) MD, PhD, FESC.

**Primary format: Markdown** (`.md`) — can be converted to PDF via Marp, Pandoc/Quarto, or LaTeX as needed.

## Output Format Strategy

```
Markdown (.md)  ← PRIMARY source format
    ├── Marp    → PDF (.pdf)            投影片簡報
    ├── Pandoc  → PDF (.pdf)           列印講義
    ├── Quarto  → Website (.html)      線上教材
    └── Pandoc  → LaTeX (.tex)         需要時才轉換
```

### Why Markdown First
- Single source, multiple outputs
- Easy to edit and version control
- Marp for presentations, Pandoc/Quarto for PDF/web
- LaTeX is available as a downstream conversion when needed

## Output Requirements

For each handout, generate the following files:
1. **Handout `.md`** — Complete teaching document (long-form Markdown)
2. **Marp `.md`** — Presentation slides (Marp-formatted Markdown), filename ends with `_Marp.md`
3. **`.pdf`** — Compiled PDF via Marp CLI
4. **Delete original PDF** — Remove the source article PDF after processing

### Build Commands

```bash
# Generate PDF from Marp Markdown
marp --no-stdin "Filename_Marp.md" --pdf -o "Filename.pdf" --allow-local-files
```

**Note:** Always use `--no-stdin` flag to prevent Marp from hanging on stdin.
**Note:** Do NOT generate PPTX — PDF is the only compiled output format.

### Legacy LaTeX (when explicitly requested)

```bash
xelatex -interaction=nonstopmode document.tex
xelatex -interaction=nonstopmode document.tex
rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz
```

## Document Generation Rules

### Language
- Main text: Traditional Chinese (繁體中文)
- Keep English for: drug names (NEVER translate), medical terminology, lab tests, procedures, clinical trial names, statistics (HR, CI, p-values), anatomical terms
- Format: `中文說明 (English term)`

### Author Attribution
Always use: `謝慕揚 MD, PhD, FESC`

---

## Handout Markdown Format (.md)

### Structure Template

```markdown
# Article Title / 中文標題

**整理：謝慕揚 MD, PhD, FESC**
**日期：YYYY-MM-DD**
**原文連結：[Journal Name — Article Title](https://doi.org/DOI)**

---

## 目錄
(use Markdown heading links)

---

## 1. Section Name

Content here...

### Subsection

- Bullet points
- **Bold for emphasis**

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |

> Blockquote for key points or clinical pearls

---

## 參考文獻

1. Author1, Author2, et al. Title. [*Journal*. Year;Vol(Issue):Pages.](https://doi.org/DOI)
2. ...
```

### Heading Hierarchy
- `# H1` — Document title (once only)
- `## H2` — Major sections
- `### H3` — Subsections
- `---` — Section dividers (horizontal rule)

### Tables
Standard Markdown pipe tables. Keep it simple:
```markdown
| Column A | Column B | Column C |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| **Bold** | Normal   | Normal   |
```

### Key Points / Clinical Pearls
Use blockquotes:
```markdown
> **Pearl 1**: Important clinical point here
```

### Code Blocks (for dosing protocols, algorithms)
Use fenced code blocks with `text` language:
````markdown
```text
Step 1: Loading dose 500 mcg/kg IV over 1 min
    |
Step 2: Start infusion 50 mcg/kg/min
    |
Step 3: Evaluate at 4-5 min
```
````

### Citation Format (Vancouver Style, Markdown)
```markdown
1. Author1, Author2, et al. Article Title. [*Journal*. Year;Vol(Issue):Pages.](https://doi.org/DOI)
```

If DOI unavailable:
```markdown
1. Author1, et al. Article Title. *Journal*. Year;Vol:Pages.
```

---

## Marp Slide Format (_Marp.md)

### YAML Front Matter (Required)

```yaml
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Microsoft JhengHei', 'PingFang TC', sans-serif;
    background-color: #ffffff;
    color: #2d3436;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 2.2em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: white;
    border-bottom: none;
    font-size: 2.5em;
    text-align: center;
  }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.72em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.88em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 0.68em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
footer: '謝慕揚 MD, PhD, FESC | Topic Name | Year'
---
```

### Marp Slide Rules (CRITICAL)

1. **Slide separator**: `---` on its own line
2. **Title slide**: Use `<!-- _class: lead -->`
3. **Section divider**: Use `<!-- _class: divider -->`
4. **Small text (references)**: Use `<!-- _class: small-text -->`

### Marp CSS Rules (CRITICAL — avoid black blocks)

1. **NO Google Fonts `@import`** — use local system fonts only
2. **NO CSS `linear-gradient()`** — use flat `background-color` only
3. **NO custom HTML `<div>` elements** — use pure Markdown only
4. **NO dark `pre` backgrounds** — use light `background-color: #f5f6fa`
5. **Use `background-color`** not `background` for solid colors
6. All styling must work offline without external resources

### Marp Color Scheme (matches LaTeX legacy)

```
emergency_red:  #ba181b  → h1, strong, blockquote border
emergency_blue: #0072bc  → h2, th background, links, divider slides
emergency_gray: #555555  → h3
lead slide bg:  #1a2740  → dark blue title/end slides
```

### Marp Slide Structure

```markdown
<!-- _class: lead -->
# Title
## Subtitle
**Author** | Date
[Original Article Link](https://doi.org/DOI)

---

# Content Slide Title

- Bullet point
- Another point

| Col 1 | Col 2 |
|-------|-------|
| Data  | Data  |

---

<!-- _class: divider -->
# Section Title

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
```

---

## Hyperlink Requirements (Critical — Mandatory for ALL Documents)

### Original Article Link (原文連結)
Every handout and Marp slide deck **MUST** include a hyperlink to the original source article:
- **Handout**: Add `**原文連結：[Journal — Title](URL)**` immediately after the date line
- **Marp title slide**: Include a clickable link to the original article on the lead slide
- Use DOI link (`https://doi.org/...`) as the canonical URL when available
- For podcast transcripts, use the podcast page URL (e.g., AHA Journals podcast page)
- For journal issue summaries, link to the issue page

### Reference Hyperlinks (參考文獻連結)
Every reference in the 參考文獻 section **MUST** include a clickable hyperlink:
1. **Primary**: Use PubMed link — `https://pubmed.ncbi.nlm.nih.gov/PMID/`
2. **If no PMID available**: Use DOI link — `https://doi.org/10.xxxx/xxxxxx`
3. **If neither available**: Use the journal article URL directly
4. **NEVER leave a reference without a hyperlink** — at minimum, link to a DOI or journal page
5. For references with both PMID and DOI, prefer the DOI link in the citation text

### DOI Verification
All DOI links must be verified before inclusion:
1. Search: `"article title" + journal + year + DOI`
2. Use `https://doi.org/` prefix (not http, not dx.doi.org)
3. **NEVER fabricate or guess DOIs** — if unverifiable, cite without hyperlink but with journal URL
4. For journal issue summaries without individual DOIs, link to the issue page

### Reference Format with Hyperlinks
```markdown
1. Author1, Author2, et al. Article Title. [*Journal*. Year;Vol(Issue):Pages.](https://doi.org/DOI)
```

If DOI unavailable but PMID known:
```markdown
1. Author1, et al. Article Title. [*Journal*. Year;Vol:Pages.](https://pubmed.ncbi.nlm.nih.gov/PMID/)
```

---

## Key Assets

### Templates
- `.claude/assets/marp-template.md` — Marp slide template (use for presentations)
- `.claude/assets/handout-template.md` — Markdown handout template (use for long-form documents)

### Legacy LaTeX (for reference)
- `.claude/assets/template.tex` — LaTeX document template
- `.claude/assets/Drake_preamble.tex` — LaTeX preamble
- `.claude/assets/Tufte-book example.tex` — Tufte book style reference

### References
- `.claude/references/doi-verification.md` — DOI patterns for major journals
- `.claude/references/table-examples.md` — Table formatting examples (Markdown + Marp)

### Scripts
- `.claude/scripts/` — Utility scripts (PDF processing, audio transcription, YouTube SRT)

## Folder Structure

Handouts are organized by **clinical topic** under `handouts/`:

```
handouts/
├── 01_缺血性心臟病/      # Ischemic Heart Disease (ACS, STEMI, PCI complications)
├── 02_心衰竭/            # Heart Failure (HFrEF, HFpEF, devices)
├── 03_心律不整/          # Arrhythmia (AF, ablation, anticoagulation)
├── 04_瓣膜疾病/          # Valvular Heart Disease (TAVR, SAVR, tricuspid)
├── 05_心臟影像/          # Cardiac Imaging (CMR, ECG, Echo, AI-ECG)
├── 06_介入心臟學/        # Interventional Cardiology (PCI, structural)
├── 07_周邊血管/          # Peripheral Vascular (carotid, PAD)
├── 10_ICU_一般照護/      # General ICU Care (antibiotics, stress ulcer, governance)
├── 11_ICU_呼吸系統/      # ICU Respiratory (ventilation, diaphragm, weaning)
├── 12_ICU_血液動力學/    # ICU Hemodynamics (CO monitoring, ECMO)
├── 13_ICU_腎臟/          # ICU Renal (AKI, RRT)
├── 20_肺栓塞/            # Pulmonary Embolism
├── 21_肺高壓/            # Pulmonary Hypertension
├── 22_COPD_氣喘/         # COPD & Asthma
├── 90_AI_科技/           # AI & Technology
├── 91_Podcast_期刊回顧/  # Podcast & Journal Snapshots
└── 99_其他/              # Miscellaneous
```

### Numbering Convention
- `01-09`: Cardiology subspecialties
- `10-19`: Critical Care / ICU
- `20-29`: Pulmonology
- `90-99`: Non-clinical topics

## Post-Completion Workflow

After successfully creating handout files:

1. **Delete original PDF** — Remove the source article PDF from the repository root
2. **Generate PDF** — Run Marp to create `.pdf`
3. **Move to topic folder** — Place all files in appropriate `handouts/` subfolder

### File Naming Convention
- Handout: `Topic Name 教學講義.md` (e.g., `Esmolol 在重症加護的應用 教學講義.md`)
- Marp slides: `Topic_Name_Marp.md` (e.g., `Esmolol_ICU_Teaching_Marp.md`)
- PDF output: `Topic_Name.pdf` (e.g., `Esmolol_ICU_Teaching.pdf`)

### Example Workflow
```bash
# Delete original PDF
rm "NEJMoa_original.pdf"

# Generate PDF
marp --no-stdin "Esmolol_ICU_Teaching_Marp.md" --pdf -o "Esmolol_ICU_Teaching.pdf" --allow-local-files

# Move to topic folder
mv "Esmolol 在重症加護的應用 教學講義.md" "handouts/10_ICU_一般照護/"
mv "Esmolol_ICU_Teaching_Marp.md" "handouts/10_ICU_一般照護/"
mv "Esmolol_ICU_Teaching.pdf" "handouts/10_ICU_一般照護/"
```

---

## Gmail HTML Email Draft

When creating email drafts for sharing handouts, use the `gmail_createDraft` MCP tool with HTML formatting.

### Critical: Gmail Strips `<style>` Tags

**Gmail (and most email clients) will remove any `<style>` blocks in `<head>`**. All styles must be written as **inline styles** directly on each element using the `style="..."` attribute.

```html
<!-- ❌ WRONG - Gmail will strip this -->
<head>
  <style>
    .header { background-color: #1a2740; }
  </style>
</head>
<div class="header">...</div>

<!-- ✓ CORRECT - Use inline styles -->
<div style="background-color: #1a2740; color: white; padding: 25px;">...</div>
```

### Color Scheme (matches Marp)

| Element | Color | Usage |
|---------|-------|-------|
| `#1a2740` | Dark blue | Header/Footer background |
| `#b0c4de` | Light steel blue | Header subtitle text |
| `#ba181b` | Emergency red | Key points, highlights, `<strong>` |
| `#0072bc` | Emergency blue | Section headers, table headers, links |
| `#f8f9fa` | Light gray | Content area background |
| `#fff5f5` | Light red | Key points box background |
| `#e3f2fd` | Light blue | Take home message background |
| `#dcdde1` | Border gray | Table/box borders |

### HTML Email Template Structure

```html
<html>
<body style="font-family: Arial, 'Microsoft JhengHei', sans-serif; line-height: 1.6; color: #2d3436; margin: 0; padding: 0;">

<!-- Header -->
<div style="background-color: #1a2740; color: white; padding: 25px; border-radius: 8px 8px 0 0;">
  <h1 style="margin: 0; font-size: 1.5em; color: white;">English Title</h1>
  <h2 style="margin: 8px 0 0 0; font-size: 1.1em; color: #b0c4de; font-weight: normal;">中文標題</h2>
</div>

<!-- Content Area -->
<div style="padding: 25px; background-color: #f8f9fa;">

  <!-- Key Points Box (red accent) -->
  <div style="background-color: #fff5f5; border-left: 5px solid #ba181b; padding: 15px 20px; margin: 20px 0; border-radius: 0 8px 8px 0;">
    <h3 style="color: #ba181b; margin: 0 0 10px 0;">核心概念</h3>
    <p style="margin: 0;">Content with <strong style="color: #ba181b;">highlighted text</strong></p>
  </div>

  <!-- Section Box -->
  <div style="background-color: white; padding: 20px; margin: 20px 0; border-radius: 8px; border: 1px solid #dcdde1;">
    <h3 style="color: #0072bc; margin: 0 0 15px 0; border-bottom: 3px solid #0072bc; padding-bottom: 8px;">Section Title</h3>
    <!-- Content here -->
  </div>

  <!-- Table -->
  <table style="width: 100%; border-collapse: collapse; margin: 0;">
    <tr>
      <th style="background-color: #0072bc; color: white; padding: 12px 10px; text-align: left; border: 1px solid #0072bc;">Header</th>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 12px 10px; border: 1px solid #dcdde1;">Data</td>
    </tr>
    <tr style="background-color: #f0f4f8;">
      <td style="padding: 12px 10px; border: 1px solid #dcdde1;">Alternating row</td>
    </tr>
  </table>

  <!-- Take Home Message (blue accent) -->
  <div style="background-color: #e3f2fd; border-left: 5px solid #0072bc; padding: 15px 20px; margin: 20px 0; border-radius: 0 8px 8px 0;">
    <h3 style="color: #0072bc; margin: 0 0 10px 0;">Take Home Message</h3>
    <p style="margin: 0;">Summary content here.</p>
  </div>

</div>

<!-- Footer -->
<div style="background-color: #1a2740; padding: 20px; text-align: center; color: #b0c4de; border-radius: 0 0 8px 8px;">
  <p style="margin: 0 0 5px 0; color: white;"><strong>謝慕揚 MD, PhD, FESC</strong></p>
  <p style="margin: 0; font-size: 0.9em;">本文件僅供醫療專業人員教學參考</p>
</div>

</body>
</html>
```

### Special Elements

**Comparison Table (red/green contrast):**
```html
<table style="width: 100%; border-collapse: collapse;">
  <tr>
    <td style="padding: 10px; border: 1px solid #dcdde1; background-color: #ffebee; width: 50%;">
      <strong style="color: #c62828;">❌ Wrong approach</strong><br>
      Description
    </td>
    <td style="padding: 10px; border: 1px solid #dcdde1; background-color: #e8f5e9; width: 50%;">
      <strong style="color: #2e7d32;">✓ Correct approach</strong><br>
      Description
    </td>
  </tr>
</table>
```

**Tip/Note Box (yellow):**
```html
<p style="margin: 10px 0; background-color: #fff8e1; padding: 10px; border-radius: 5px;">
  💡 Important tip or note here
</p>
```

**Code/Formula Box:**
```html
<div style="background-color: #f5f6fa; padding: 12px 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1em;">
  SV ≈ VTI × π ≈ VTI × 3.14
</div>
```

### MCP Tool Usage

```javascript
gmail_createDraft({
  to: "recipient@example.com",
  subject: "[教學講義] Title — Subtitle",
  body: "<html>...</html>",  // Full HTML with inline styles
  isHtml: true  // CRITICAL: Must be true for HTML rendering
})
```

---

## Trigger Keywords

This skill activates on: "整理", "請幫我整理", "markdown", "marp", "期刊講義", "journal reading", "教學", "每週期刊回顧", "weekly journal review", or references to medical literature from NEJM, JACC, Circulation, EuroIntervention, European Heart Journal.

## Recurring Tasks

### TEER 文獻雙週回顧

**Trigger**: User says "TEER 文獻回顧" or "TEER review"

**Workflow**:
1. Search PubMed and Semantic Scholar for publications from the last 14 days using queries:
   - "transcatheter edge-to-edge repair" OR "TEER"
   - "MitraClip" OR "PASCAL" OR "edge-to-edge repair"
   - "TriClip" OR "tricuspid TEER"
2. Compile all unique articles, remove duplicates
3. Generate a structured Markdown review document with:
   - 重點摘要 (Key Pearls)
   - Categorized by: Mitral TEER, Tricuspid TEER, PASCAL, Imaging/Technique, Guidelines
   - Case reports of interest
   - Complete reference list with DOI/PubMed hyperlinks
4. Save as `TEER_Biweekly_Review_YYYY-MM-DD 教學講義.md`
5. Move to `handouts/04_瓣膜疾病/`

**Goal**: Drake is developing expertise in TEER (14 cases performed). These reviews support his goal of becoming a TEER expert specializing in MitraClip and Pascal devices.

### TAVI 文獻雙週回顧

**Trigger**: User says "TAVI 文獻回顧" or "TAVI review"

**Workflow**:
1. Search PubMed and Semantic Scholar for publications from the last 14 days using queries:
   - "transcatheter aortic valve implantation" OR "TAVI" OR "TAVR"
   - "balloon-expandable" OR "self-expanding" OR "aortic stenosis transcatheter"
   - "SAPIEN" OR "Evolut" OR "ACURATE" OR "Navitor" OR "JenaValve"
2. Compile all unique articles, remove duplicates
3. Generate a structured Markdown review document with:
   - 重點摘要 (Key Pearls)
   - Categorized by: Clinical Outcomes, Device Comparison, Imaging/Planning, Complications, Conduction Disturbance/Pacemaker, Durability, Bicuspid/Low-Risk, Guidelines
   - Case reports of interest
   - Complete reference list with DOI/PubMed hyperlinks
4. Generate Marp slides with:
   - Every slide must have PubMed/DOI hyperlinks in H2 subtitle
   - Reference pages at the end (use `section.ref` CSS class)
5. Generate PDF from Marp
6. Save as `TAVI_Biweekly_Review_YYYY-MM-DD 教學講義.md`
7. Move to `handouts/04_瓣膜疾病/`

**Output**: 教學講義 `.md` + Marp `_Marp.md` + PDF `.pdf` (no PPTX)

### 每週心臟科期刊 Podcast 回顧

**Trigger**: User says "每週期刊回顧" or "weekly journal review"

**Journals covered** (4 core cardiology journals):

| 期刊 | 出刊頻率 | 出刊日 | Podcast 名稱 | Podcast 頻率 |
|------|---------|--------|-------------|-------------|
| **JACC** | 每週 | Tuesday | JACC This Week (Krumholz & Lam) | 每週 |
| **Circulation** | 每週 | Tuesday | Circulation on the Run (Hundley & Myhre) | 每週 |
| **European Heart Journal** | 雙週 | 隔週 | EHJ Podcast / Issue @ a Glance | 雙週 |
| **EuroIntervention** | ~雙週 (24 issues/yr) | 不固定 | Turning Point (訪談式，非 issue summary) | 不定期 |

**Workflow**:
1. 確認日期範圍（本週六往回 7 天）
2. 依序處理 4 本期刊：
   a. **JACC** — WebFetch podcast show notes + PubMed 本週 JACC 文章
   b. **Circulation** — WebFetch Circulation on the Run + PubMed 本週 Circulation 文章
   c. **EHJ** — 確認是否有新 biweekly issue，有則整理 Issue @ a Glance
   d. **EuroIntervention** — 確認是否有新 issue 或 Turning Point episode
3. 背景同時用 yt-dlp + Whisper 轉錄 podcast YouTube 音訊為 SRT（存入 `handouts/91_Podcast_期刊回顧/`）
4. 各期刊產出：教學講義 `.md` + Marp `_Marp.md` + PDF `.pdf`
5. 額外產出「本週心臟科文獻總覽」整合版（top 3-5 articles across all journals）
6. 所有檔案移至 `handouts/91_Podcast_期刊回顧/`

**Podcast 來源**：
| 期刊 | Podcast 頁面 | YouTube |
|------|-------------|---------|
| JACC | jaccaudio.acc.org | JACC Journals YouTube |
| Circulation | ahajournals.org/circ/podcast | AHA Journals YouTube |
| EHJ | academic.oup.com/eurheartj/pages/podcasts | ESC YouTube |
| EuroIntervention | eurointervention.pcronline.com/pages/turning-point | — |

**Transcript 取得策略**：
- **即時**：WebFetch podcast show notes + PubMed abstracts → 快速產出講義
- **背景**：yt-dlp + Whisper → SRT 存檔備查（`Journal_Podcast_YYYY-MM-DD.srt`）

**EuroIntervention 特殊處理**：
- 有新 issue 時：整理 TOC + 重要 abstracts
- Turning Point 有新 episode 時：同步整理訪談內容
- 無更新時：跳過，在總覽中註明「本週無新 issue」

**檔案命名**：
- `JACC This Week YYYY-MM-DD 期刊回顧 教學講義.md`
- `JACC_This_Week_YYYY-MM-DD_Marp.md`
- `JACC_This_Week_YYYY-MM-DD.pdf`
- `Weekly_Cardiology_Review_YYYY-MM-DD 教學講義.md`（總覽）
- （Circulation、EHJ、EuroIntervention 同理）

**Output**: 每期刊一份講義 + 一份總覽，共 ~5 份文件（PDF only, no PPTX）
