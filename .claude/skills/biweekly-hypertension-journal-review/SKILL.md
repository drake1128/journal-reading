---
name: biweekly-hypertension-journal-review
description: Generate the dedicated Biweekly Hypertension Journal Review handout (markdown), Marp slide deck, and PDF for the past 14 days across the major general-medicine journals (NEJM, Lancet, BMJ, JAMA family) plus the hypertension-specialty journals (Hypertension, J Hypertens, Hypertension Research, Am J Hypertens, J Clin Hypertens) and the cardiology majors that carry large HTN trials (Circulation, EHJ, JACC, JAMA Cardiology). Use when Drake (謝慕揚醫師) says "高血壓期刊回顧", "高血壓雙週期刊", "hypertension journal review", "HTN journal review", "每雙週高血壓期刊", or "高血壓期刊文獻回顧". Two modes: Mode A (default) = full handout + Marp + PDF to handouts/09-hypertension/biweekly-review/; Mode B (checklist) = tick-box article list over the 7 journals NEJM/Lancet/JAMA/BMJ/Circulation/EHJ/JACC saved to handouts/09-hypertension/monthly-checklist/ plus a Gmail DRAFT (never send) addressed to 吳志成 副院長 chihchengwumd@gmail.com — triggered by "高血壓文章清單", "勾選清單", "寄給吳副院長". Tailored for a Taiwan physician audience (residents, NPs, cardiology/nephrology/IM). CRITICAL: every "其他焦點/Other highlights" table in Marp slides MUST include a 連結 column with clickable DOI hyperlinks.
---

# Biweekly Hypertension Journal Review Skill

Produce a comprehensive **biweekly** review covering the **past 14 days** of hypertension literature, with one handout + one Marp deck + one PDF. Modeled on the `weekly-cv-journal-review` skill but scoped to hypertension and running every two weeks. Audience: **Taiwan physicians** (心臟科、腎臟科、一般內科住院醫師、NP)。

## Trigger phrases

- "高血壓期刊回顧"
- "高血壓雙週期刊"
- "hypertension journal review"
- "HTN journal review"
- "每雙週高血壓期刊"
- "高血壓期刊文獻回顧"
- "幫我整理最近兩週的高血壓期刊"

**Mode B（勾選清單）觸發語**：

- "高血壓文章清單"
- "勾選清單"
- "寄給吳副院長" / "吳志成副院長的清單"
- "四大期刊高血壓清單"
- "整理〇月份的高血壓文章"

## Cadence

- **Every 2 weeks**, covering the **past 14 days** (run date minus 14 → run date).
- A cloud routine (see CLAUDE.md → 「每雙週高血壓期刊回顧」) may trigger this autonomously; it can also be run manually via any trigger phrase.

## 兩種輸出模式 (Modes) — 開工前先判斷

| Mode | 觸發語 | 產出 | 對象 |
|------|--------|------|------|
| **A. 完整講義（預設）** | 「高血壓期刊回顧」「hypertension journal review」等 | 教學講義 `.md` + Marp `_Marp.md` + PDF | 院內教學（住院醫師／NP） |
| **B. 勾選清單 (Checklist)** | 「高血壓文章清單」「勾選清單」「寄給吳副院長」「四大期刊高血壓清單」 | 勾選用 `.md` + **Gmail HTML 草稿** | **吳志成 副院長** (chihchengwumd@gmail.com) |

兩種模式的檢索邏輯共用，差別只在**收錄範圍、輸出格式與收件人**。以下 §Mode B 專章規範 Mode B；其餘章節（§Journals 起）為 Mode A 規範。

---

## Mode B — 勾選清單專章

### B1. 期刊範圍（**只有 7 本**，不要擴充）

四大期刊 **NEJM · Lancet · JAMA · BMJ** ＋ 三大心臟科 **Circulation · European Heart Journal · JACC**。
不含高血壓專科刊、不含 JAMA 子刊、不含腎臟科刊 —— 那是 Mode A 的範圍。

### B2. 時間區間

- 預設：過去 **14 天**（每兩週跑一次）。
- 使用者指定月份（如「七月份」「上個月」）→ 改為該月 **1 日至月底**，檔名用 `YYYY-MM`。

### B3. 三重檢索（缺一不可，去重後人工篩選）

```text
J = ("N Engl J Med"[Journal] OR "Lancet"[Journal] OR "JAMA"[Journal] OR "BMJ"[Journal]
     OR "Circulation"[Journal] OR "Eur Heart J"[Journal] OR "J Am Coll Cardiol"[Journal])

Q1 (TIAB, pdat) : J AND (hypertension[TIAB] OR "blood pressure"[TIAB] OR antihypertensive[TIAB] OR hypertensive[TIAB])
Q2 (MeSH, pdat) : J AND ("hypertension"[MeSH] OR "blood pressure"[MeSH] OR "antihypertensive agents"[MeSH] OR "hypertension, pregnancy-induced"[MeSH])
Q3 (Title, edat): J AND (hypertension[Title] OR "blood pressure"[Title] OR antihypertensive[Title] OR hypertensive[Title] OR "renal denervation"[TIAB] OR aldosterone[TIAB])
```

Q3 用 `datetype: "edat"`，專門補抓「該月入庫、但線上刊期掛前一個月」的文章（例如社論、research letter）。
反向注意：Q3 也會抓到**下個月號**的文章（entry date 落在本月），這些要剔除並在說明段落註明「將併入下月清單」。

### B4. 清單分區（固定 6 區，空的區塊直接省略）

- **A. 系統性高血壓 — 原始研究與重要分析**（最重要，放最前）
- **B. 綜述 · 指引 · 科學聲明**
- **C. 社論 · 通訊 · 新聞短訊**（同主題的多則通訊合併成一條）
- **D. 基礎／轉譯（高血壓機轉）**
- **E. 肺高壓 (PAH / PH)** — 標明「若副院長也想涵蓋」
- **F. 血壓為次要終點（相關但非主軸）**

### B5. 條目格式（**每條都要能打勾**）

```markdown
- [ ] **期刊** — 英文原標題
  一到兩句繁中結論（有數字就寫數字：Δ mmHg、HR、95% CI、P）。
  [DOI: 10.xxxx/xxxx](https://doi.org/10.xxxx/xxxx) · PMID 12345678
```

- 每條**必附 DOI 超連結 + PMID**，DOI 一律取自 PubMed 回傳值，**絕不自行拼湊**。
- 摘要缺漏（`[Abstract not available]`）就照實寫「PubMed 未附摘要，需取原文」，不要編故事。
- 值得優先讀的加 ⭐ 並說明理由。

### B6. 結尾必附「檢索與篩選說明」

列出三個檢索式各自命中筆數、去重後總數、**被人工剔除的文章（含 PMID 與剔除理由）**，以及被延到下期的文章。副院長要能複核你篩掉了什麼。

### B7. 輸出與寄送

- 檔案：`handouts/09-hypertension/monthly-checklist/Hypertension_Checklist_YYYY-MM 勾選清單.md`
  （雙週版用 `Hypertension_Checklist_YYYY-MM-DD 勾選清單.md`）
- **Gmail：一律只建草稿，絕不直接寄出。**
  - `mcp__claude_ai_Gmail__create_draft`，`to: ["chihchengwumd@gmail.com"]`
  - 主旨：`[高血壓文獻清單] YYYY 年 M 月 — 四大期刊 + Circulation / EHJ / JACC`
  - 內文用 CLAUDE.md 的 Gmail HTML inline-style 規範；每條文章標題做成 DOI 超連結
  - 信末署名 `謝慕揚 MD, PhD, FESC` + 「本清單僅供醫療專業人員教學參考」
  - **不 CC 任何人**，草稿建立後回報草稿連結給 Drake 自行確認送出
- Mode B **不產 Marp、不產 PDF**（除非 Drake 另外要求）。

---

## Journals

| Group | Journals to search |
|-------|-------------------|
| **General medicine (fixed)** | NEJM, Lancet, BMJ, JAMA — HTN/BP/cardiovascular/renal-related original articles + editorials |
| **Hypertension specialty (fixed)** | Hypertension (AHA), J Hypertens (ESH), Hypertension Research (JSH/Nature), Am J Hypertens, J Clin Hypertens |
| **Cardiology majors** | Circulation, Eur Heart J, J Am Coll Cardiol, JAMA Cardiology — filter to HTN/BP topics |
| **JAMA family (real-world/population)** | JAMA Intern Med, JAMA Network Open — filter to HTN/BP topics |
| **Renal / secondary HTN (as relevant)** | JASN, CJASN, Kidney Int — secondary HTN, CKD–HTN interface (include only HTN-relevant hits) |

If a journal returns 0 HTN-relevant hits in the window, note it explicitly (e.g., "本期 BMJ **無高血壓相關原始研究**").

## Output specification

Always produce **3 files** named with the run date (today, YYYY-MM-DD):

| File | Purpose |
|------|---------|
| `Hypertension_Biweekly_Review_YYYY-MM-DD 教學講義.md` | Long-form handout |
| `Hypertension_Biweekly_Review_YYYY-MM-DD_Marp.md` | Marp slide source |
| `Hypertension_Biweekly_Review_YYYY-MM-DD.pdf` | Compiled slide deck |

**No PPTX, no LaTeX.** Move all 3 files to `handouts/09-hypertension/biweekly-review/`.

(If Drake asks for the 4th deliverable — a **Gmail HTML draft** — build it per CLAUDE.md's Gmail HTML rules, attributing him as 讀書會共筆整理人 with the disclaimer footer, and using `mcp__gmail__draft_email` / `mcp__claude_ai_Gmail__create_draft`.)

## Fixed sections (缺一不可 — HTN-tailored)

Mirror the CV review's fixed-column philosophy, adapted to hypertension:

1. **Top 5 Picks** — cross-journal, with 結果方向 markers
2. **🎯 頑固型 & 次發性高血壓 (Resistant & Secondary HTN)** — Drake's clinical focus (aldosterone/PA, RDN candidacy, adherence, endocrine HTN)
3. **💊 藥物治療 & 新藥 (Pharmacotherapy)** — e.g., aldosterone synthase inhibitors (baxdrostat, lorundrostat), zilebesiran (siRNA), ARNI, SGLT2i-BP, combination/SPC
4. **🔧 器械 / 介入治療 (Devices)** — renal denervation (RDN), baroreflex activation, endovascular approaches
5. **👥 特殊族群 & 亞洲/台灣資料** — CKD, diabetes, pregnancy/pre-eclampsia, elderly, Asian/Taiwanese cohorts, NHI-based studies
6. **📚 其他焦點 (Honorable Mentions)** — everything else worth a look (each with a 連結)
7. **🔬 Case Reports** — 2–3 instructive cases (secondary HTN, hypertensive emergency, rare causes)
8. **指引與共識更新 (Guidelines)** — include only when a new/updated guideline appeared in the window
9. **縮寫對照** — first occurrence uses 「中文 (Full English Name, Abbr)」
10. **參考文獻** — Vancouver + DOI/PMID hyperlinks

## Workflow (numbered, follow in order)

### 1. Confirm date window
- Today = run date. Window = past **14 days** (run date − 14 → run date).
- Express as `YYYY/MM/DD` for the PubMed `date_from` / `date_to` filter (`datetype: "pdat"`).

### 2. Search PubMed for each journal group in parallel

Use the available PubMed MCP — `mcp__claude_ai_PubMed__search_articles` (primary in this session) or `mcp__pubmed__pubmed_search_articles` (fallback). Run the queries in **parallel** (single message, multiple tool calls). Use `date_from`/`date_to` = the 14-day window, `sort: "pub_date"`, `max_results: 30-40`.

```text
Q1 (NEJM):   "N Engl J Med"[Journal] AND (hypertension OR "blood pressure" OR antihypertensive OR aldosterone OR renal denervation)
Q2 (Lancet): "Lancet"[Journal] AND (hypertension OR "blood pressure" OR antihypertensive OR aldosterone)
Q3 (BMJ):    "BMJ"[Journal] AND (hypertension OR "blood pressure" OR antihypertensive)
Q4 (JAMA family): ("JAMA"[Journal] OR "JAMA Cardiol"[Journal] OR "JAMA Intern Med"[Journal] OR "JAMA Netw Open"[Journal]) AND (hypertension OR "blood pressure" OR antihypertensive)
Q5 (Hypertension specialty): ("Hypertension"[Journal] OR "J Hypertens"[Journal] OR "Hypertens Res"[Journal] OR "Am J Hypertens"[Journal] OR "J Clin Hypertens (Greenwich)"[Journal])
Q6 (Cardiology majors, HTN-filtered): ("Circulation"[Journal] OR "Eur Heart J"[Journal] OR "J Am Coll Cardiol"[Journal]) AND (hypertension OR "blood pressure" OR antihypertensive OR "renal denervation")
Q7 (Renal, HTN-filtered): ("J Am Soc Nephrol"[Journal] OR "Clin J Am Soc Nephrol"[Journal] OR "Kidney Int"[Journal]) AND (hypertension OR "blood pressure" OR aldosterone OR "secondary hypertension")
```

Note: `"Hypertension"[Journal]` also matches the specialty journal name inside titles; scan results and keep only true HTN-topic articles.

### 3. Fetch full abstracts for top picks

After scanning titles, pick ~6–12 candidates (priority: original RCTs > pivotal observational > guidelines > editorials > reviews). Fetch metadata/abstracts with `mcp__claude_ai_PubMed__get_article_metadata` (pmids: [...]). **Always keep the DOI returned by PubMed** — never fabricate one.

### 4. ⚠️ VERIFY trial results via WebSearch (CRITICAL)

For every major trial, **do NOT trust the abstract alone**. Use `WebSearch` to confirm the primary endpoint (Δ SBP/DBP + 95% CI + P-value) and whether it was POSITIVE / NEGATIVE / NEUTRAL. Cross-check tctmd.com, ACC.org, Cardiology Today, Medscape, or the journal press release.

**Why this matters** (HTN-specific pitfalls):
- BP-lowering trials often report office **and** ambulatory BP with different effect sizes — state which.
- Device/RDN trials (SPYRAL, RADIANCE) hinge on sham-control and med-adherence — read carefully.
- Novel agents (baxdrostat/BaxHTN, lorundrostat, zilebesiran/KARDIA) — confirm the actual mmHg and safety (hyperkalemia, hyponatremia).
- Follow `feedback_verify_trial_results` and `feedback_verify_secondary_articles`: batch-verify **every** DOI (search "[AID]" in PubMed) and author name before delivery.

### 5. Write the handout markdown

Structure (see the fixed sections above). Header block:

```markdown
# 每雙週高血壓期刊文獻回顧 — YYYY-MM-DD ~ YYYY-MM-DD

**整理：謝慕揚 MD, PhD, FESC**
**日期：YYYY-MM-DD**
**涵蓋期刊**：NEJM、Lancet、BMJ、JAMA family、Hypertension、J Hypertens、Hypertension Research、Am J Hypertens、J Clin Hypertens、Circulation、EHJ、JACC（＋ 腎臟科次專科）
```

- **Per top pick**: a 2-column table (項目 / 內容) — 設計 / 族群 / primary endpoint / 結果 (mmHg, CI, P) / 安全性 / take-home.
- **Per 「其他焦點」 table**: 3 columns `主題 | 摘要 | 連結` — the 連結 cell always has a PubMed or DOI hyperlink, **never empty**.
- **Pearl of the Fortnight**: one-line synthesis of the two-week theme.

### 6. Write the Marp slide deck

**⚠️ THEME IS EXCLUSIVE TO THIS ROUTINE.** This deck uses the **台灣高血壓學會 (Taiwan Hypertension Society) coral/rose identity**, NOT the project-default red/blue theme. This custom palette applies **only to the Hypertension Biweekly Review** — do NOT copy it into any other routine (weekly CV review, TAVI, TEER, podcast, etc. keep their own default themes). Paste the **exact** `style:` block below verbatim into the Marp front-matter. Footer: `'謝慕揚 MD, PhD, FESC | 高血壓期刊回顧 Hypertension Biweekly Review | YYYY-MM-DD'`.

```yaml
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  /* ===== 台灣高血壓學會 Taiwan Hypertension Society — coral/rose identity ===== */
  section {
    font-family: 'Microsoft JhengHei', 'PingFang TC', sans-serif;
    background-color: #fff9fa;
    color: #3d2d30;
    border-top: 10px solid #c4304a;
    padding-top: 44px;
  }
  /* ---- Lead / title (coral hero) ---- */
  section.lead {
    background-color: #c4304a;
    color: #ffffff;
    border-top: 10px solid #7f1d30;
  }
  section.lead h1 { color: #ffffff; font-size: 2.0em; border-bottom: none; }
  section.lead h2 { color: #ffdbe2; }
  section.lead p, section.lead strong { color: #ffeef1; }
  section.lead a { color: #ffd9df; text-decoration: underline; }
  section.lead blockquote,
  section.lead blockquote p,
  section.lead blockquote strong {
    color: #3d2d30; background-color: #ffffff; border-left-color: #f0a9b5;
  }
  /* ---- Section dividers (coral) ---- */
  section.divider {
    background-color: #c4304a;
    color: #ffffff;
    border-top: 10px solid #7f1d30;
    display: flex; justify-content: center; align-items: center;
  }
  section.divider h1 { color: #ffffff; border-bottom: none; font-size: 2.3em; text-align: center; }
  section.divider h2 { color: #ffe08a; }
  section.divider h3 { color: #ffffff; }
  /* ---- Headings ---- */
  h1 { color: #c4304a; border-bottom: 3px solid #e6828f; padding-bottom: 0.18em; font-size: 1.45em; }
  h2 { color: #d23c50; font-size: 1.02em; }
  h3 { color: #9a5560; }
  /* ---- Tables ---- */
  table { font-size: 0.62em; width: 100%; border-collapse: collapse; }
  th { background-color: #c4304a; color: #ffffff; padding: 6px 9px; }
  td { padding: 4px 8px; border-bottom: 1px solid #f3d6dc; }
  tr:nth-child(even) { background-color: #fbe9ec; }
  /* ---- Blockquote (soft pink card) ---- */
  blockquote {
    border-left: 5px solid #c4304a;
    background-color: #fdeef0;
    padding: 0.45em 0.95em; font-size: 0.82em; border-radius: 0 10px 10px 0;
  }
  /* ---- Code ---- */
  pre { background-color: #fdf3f5; color: #3d2d30; border: 1px solid #f0cdd4; border-radius: 10px; padding: 0.6em; font-size: 0.6em; }
  pre code { background-color: transparent; color: #3d2d30; }
  code { background-color: #fbe4e8; color: #c4304a; padding: 2px 6px; border-radius: 4px; }
  strong { color: #c4304a; }
  a { color: #c4304a; }
  footer { color: #b07b83; font-size: 0.55em; }
  section.small-text { font-size: 0.8em; }
  section.ref { font-size: 0.68em; }
  img[alt~="qr"] { border: 3px solid #ffffff; box-shadow: 0 0 0 1px #f0cdd4; border-radius: 8px; }
footer: '謝慕揚 MD, PhD, FESC | 高血壓期刊回顧 Hypertension Biweekly Review | YYYY-MM-DD'
---
```

Palette reference (all **flat** colors — no `linear-gradient`, so no PDF black-block risk):

| Token | Hex | Use |
|-------|-----|-----|
| Deep coral (學會紅) | `#c4304a` | lead/divider bg, top band, H1, th, strong, links |
| Coral border | `#e6828f` / `#f0a9b5` | H1 underline, lead blockquote accent |
| Rose H2 | `#d23c50` | section H2 |
| Pink surface | `#fbe9ec` / `#fdeef0` | even table rows, blockquote card |
| Pale page | `#fff9fa` | content slide bg |
| Warm dark text | `#3d2d30` | body text |
| Divider H2 accent | `#ffe08a` | bright yellow on coral divider |

Title slide: prefix the H1 with 🫀 (Taiwan Hypertension Society heart motif), e.g. `# 🫀 每雙週高血壓期刊文獻回顧`.

Slide order:
1. Title (`<!-- _class: lead -->`)
2. **本期主題** — one-line characterization
3. **Top 5 Picks 一覽** — single overview table with key mmHg numbers
4. 各固定欄目 divider + per-paper detail slides + 「其他焦點」 tables (🎯 Resistant/Secondary → 💊 Pharmacotherapy → 🔧 Devices → 👥 特殊族群 → 📚 Honorable → 🔬 Cases → 指引)
5. **整合 Take Home** divider
6. **本期 5 大臨床啟示** (Pearls 1–5)
7. **縮寫對照** (`<!-- _class: small-text -->`)
8. **參考文獻** (`<!-- _class: ref -->`, may be 2–3 slides)
9. **謝謝聆聽 / Q&A** (`<!-- _class: lead -->`)

Optional QR codes on result/design slides: generate `size=200x200`, then embed base64 (see §7b-a).

### 7. ⚠️ CRITICAL — Every "其他焦點/Other highlights" Marp table MUST have a 連結 column

Slide tables listing multiple secondary articles MUST be 3 columns (`主題 | 重點 | 連結`) with a working DOI/PubMed hyperlink in every 連結 cell. For single-paper detail slides, the link goes in the H2 subtitle: `## [Author, et al. Journal YYYY](https://doi.org/...)`.

### 7b. ⚠️ Render-safety rules — DO NOT repeat known bugs

**(a) QR codes MUST be embedded as base64 data URIs** — never left as remote `https://api.qrserver.com/...`. Headless-Chromium PDF export often fails to load remote images → blank QR. As the step right before compiling, fetch each PNG and inline as base64; **0** `api.qrserver.com` refs may remain. (Same pattern used successfully in the TSOC Adherence deck.)

**(a2) Emoji MUST render as native text, not remote Twemoji `<img>`.** The repo-root `.marprc.yml` (`options.emoji.unicode: false`) fixes this, but **Marp only auto-loads `.marprc.yml` from the current working directory** → **compile from the repo root**, then `mv` into the handout folder.

**(b) Any light-background box on the coral `lead`/`divider` slides MUST set explicit dark text** — the theme block already does this (`section.lead blockquote { color:#3d2d30; background-color:#ffffff; }`); keep it, otherwise light-on-coral or light-on-light = invisible.

**(b2) `section.divider` H1/H2/H3 must be explicitly bright** (white H1/H3, `#ffe08a` yellow H2) — the theme block sets these; else they fall to default colors on the **coral** divider background (low contrast).

**(c) Spot-check the compiled PDF** — rasterise a QR slide, the last/disclaimer slide, and an emoji slide; eyeball them (no broken-image thumbnails). Delete the temp PNGs afterward.

### 8. Compile PDF and move files

```bash
# Run from the REPO ROOT so repo-root .marprc.yml auto-loads (emoji fix).
marp --no-stdin "Hypertension_Biweekly_Review_YYYY-MM-DD_Marp.md" \
     --pdf -o "Hypertension_Biweekly_Review_YYYY-MM-DD.pdf" --allow-local-files

mv "Hypertension_Biweekly_Review_YYYY-MM-DD 教學講義.md" handouts/09-hypertension/biweekly-review/
mv "Hypertension_Biweekly_Review_YYYY-MM-DD_Marp.md"     handouts/09-hypertension/biweekly-review/
mv "Hypertension_Biweekly_Review_YYYY-MM-DD.pdf"         handouts/09-hypertension/biweekly-review/
```

Always pass `--no-stdin`.

## Top 5 Picks — selection & markers

Priority: (1) original RCTs (positive AND negative), (2) pivotal observational, (3) guideline/consensus, (4) framing editorials, (5) concept-shifting reviews / first-in-human. Always include ≥1 negative/neutral trial if available.

結果方向 markers: ✅ Positive · ❌ Negative (`+ harm signal` if safety worse) · 💡 Concept-shift · ➰ Early feasibility/design.

## Author attribution and framing

- Always: `謝慕揚 MD, PhD, FESC`
- Gmail draft (if requested): Drake is **讀書會共筆整理人**, NOT 精選專家; include disclaimer footer (see `feedback_email_disclaimer`).

## Quality checklist before delivery

- [ ] Date window confirmed (past 14 days as of run date)
- [ ] All journal groups searched (or "no results" noted explicitly)
- [ ] Top 5 Picks table populated with 結果方向 markers; ≥1 negative if available
- [ ] **Every Marp 「其他焦點」 table has a 連結 column with DOI hyperlinks** ⚠️
- [ ] Per-paper detail slides have DOI/PubMed link in H2 subtitle
- [ ] Major trials verified via WebSearch (not just abstract); mmHg + CI + P stated
- [ ] **Every DOI + author name verified** (no hallucinated secondary citations) ⚠️
- [ ] Drug names in English (never translate); abbreviations expanded on first use + 縮寫對照 section
- [ ] Reference list grouped by journal with hyperlinks
- [ ] Marp CSS: no Google Fonts import, no gradients, no custom divs (QR div + disclaimer blockquote are the only exceptions)
- [ ] **QR codes embedded as base64 — 0 remaining `api.qrserver.com` refs** ⚠️
- [ ] **Lead/divider light boxes have explicit dark text; divider H2/H3 bright** ⚠️
- [ ] PDF compiled **from the repo root** with `--no-stdin --allow-local-files`; spot-checked
- [ ] All 3 files moved to `handouts/09-hypertension/biweekly-review/`

## Cross-references

- Sibling skill (weekly, cardiology): `.claude/skills/weekly-cv-journal-review/SKILL.md`
- General journal-reading conventions: `.claude/SKILL.md`
- Marp template: `.claude/assets/marp-template.md`
- Handout template: `.claude/assets/handout-template.md`
- Project workflow specs: `CLAUDE.md` → 「每雙週高血壓期刊回顧」section
