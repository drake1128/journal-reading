# Entresto Journey at 10 — AI 協作下的醫學資料正確性檢核反思

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-05-13**
**主題**：以 LLM 協作製作 TSOC 演講投影片過程中的兩輪 Novartis Medical Affairs 校稿
**檔案性質**：自我反思 + 工作流程改進記錄，作為未來 AI 協作醫學內容時的教訓檔案

---

## 目錄

1. [專案脈絡 (Project Context)](#1-專案脈絡)
2. [Round 1 — Novartis 第一輪校稿的錯誤型態](#2-round-1)
3. [根因分析 — LLM 為什麼會產生「貌似合理但實際錯誤」的醫學數據](#3-根因分析)
4. [工作流程改變 — 來源優先 (Source-First) 原則](#4-工作流程改變)
5. [Round 2 — 新流程的第一次實戰應用](#5-round-2)
6. [前置查證檢查清單 (Pre-draft Verification Checklist)](#6-前置查證檢查清單)
7. [Memory 規則 — 長期記憶寫入](#7-memory-規則)
8. [可驗證的參考文獻](#8-可驗證的參考文獻)
9. [Take-home messages](#9-take-home-messages)

---

## 1. 專案脈絡

- **演講場合**：TSOC 2026 年會，Entresto (sacubitril/valsartan) 在台上市十週年特別演講
- **投影片產出**：34 張 HTML deck（navy/gold editorial 風格，1920×1080，每張一頁），最終以 Chrome `--headless --print-to-pdf` 轉成 PDF
- **協作模式**：講者提供大綱與重點 → AI 起草投影片內容（含試驗數據、HR、p-value、CI、引用文獻）→ Novartis Medical Affairs (Huang Irene CT) 學術校稿 → 修正回稿
- **時程**：2026-05-10 初稿 → 2026-05-12 兩輪修正 → 2026-05-16/17 演講
- **檔案位置**：
  - HTML: `G:\我的雲端硬碟\Speech Entresto at 10 years\Entresto_Journey_at_10_2026-05-10 no-cases version.html`
  - PDF (corrected): `G:\我的雲端硬碟\Speech Entresto at 10 years\Entresto_Journey_at_10_2026-05-12_corrected.pdf`

---

## 2. Round 1 — Novartis 第一輪校稿的錯誤型態

Novartis 校稿在 2026-05-12 上午回稿，指出多處數據誤植。對應修正涵蓋第 3, 11, 17, 22, 24, 25, 26, 27, 28, 29, 30, 31 頁。

### 2.1 五大失誤類別

| # | 失誤類別 | 具體案例 | 嚴重度 |
|---|---------|---------|--------|
| 1 | **無中生有的合理數值** | Slide 25 KDIGO tier HR：Low 0.79 / Moderate 0.81 / High 0.78 / Very High 0.82 / Overall 0.80 — Damman 2024 *JACC* 原文**並沒有**這樣的 KDIGO 四層 stratification | ★★★★★ |
| 2 | **捏造相對風險表述** | Slide 24 & 31「21% slower eGFR decline」 — 原文是 +0.43 mL/min/yr vs. enalapril，**不是**相對百分比 | ★★★★ |
| 3 | **發表年份錯誤** | Slide 3 timeline 把 PIONEER-HF 標 2017、UK-HARP-III 標 2023；兩篇都是 2018 出版 | ★★ |
| 4 | **單字母 author 錯誤擴散** | Vietnam 透析 SRMA 第一作者寫成 Nguyen DT，正確為 **Nguyen DV** — 因為複製貼上錯誤擴散到 4 張投影片 | ★★ |
| 5 | **主題相近但實際無關的 miscitation** | Slide 30 把 **ASIAN-HF** 列為 ARNI evidence — 該 paper 是 Asia-Pacific HF registry，**不研究** ARNI | ★★★ |
| 6 | **重複未合併** | Slide 27 把同一份 Le D 2024 美國透析 cohort 拆成兩列（mortality、hyperkalemia 各一列）而非合併 | ★ |

### 2.2 為什麼我自己也沒抓到？

> **臨床判讀的危險之處**：這些 HR 都落在 0.78–0.82 區間，正好是一個有效 HF 治療在 CKD 各分層應該預期的效果量級。它們在「美感上」與「臨床直覺上」都是對的，所以即便仔細讀一遍也很難發現問題 — 必須打開原文 paper 對比 Table 2 才會穿幫。

這是 LLM 產生醫學內容時最危險的一種錯誤：**aesthetically correct, epistemically wrong**（美學上正確，知識上錯誤）。

---

## 3. 根因分析

### 3.1 為什麼 LLM 會「捏造合理數值」？

LLM 不是查資料庫，是從訓練語料的統計分布中取出最可能的下一個 token。當 prompt 要求：

> 「Fill in a KDIGO tier breakdown table for PARADIGM-HF subgroup analysis」

模型沒有開 paper、沒有讀 Table 2，它做的是：
1. 從訓練語料的「PARADIGM-HF KDIGO subgroup」相關上下文中，取出常見的 HR 量級分布（多落在 0.70–0.90）
2. 為了視覺一致性，產生四個彼此接近、跨越 CV death 與 renal endpoint 兩欄的數字
3. 加上一個 weighted average 「Overall」row 讓表格看起來更完整

結果：每個數字都「臨床合理」，但**沒有一個是從原文擷取的**。

### 3.2 訓練資料的時效與召回偏差

- LLM 對 trial publication year 的記憶常與「conference presentation year」或「first ePub」混淆
- 例如 PIONEER-HF 是 2018 年 AHA Late-Breaker 首次公布，2019 年 NEJM 完整文章發表，2018 年也有 abstract — 任何一年都可能在訓練語料中與 PIONEER-HF 共同出現
- 結果：模型回應「PIONEER-HF 是哪一年」可能會給出三種答案之一

### 3.3 主題相近 ≠ 證據相關

ASIAN-HF 被誤列為 ARNI evidence 是典型的 **topic-similarity drift**：
- 兩者都涉及「Asian HF population」
- 在語意空間中距離接近
- 模型在 prompt「list ARNI evidence in Asians」時容易把 ASIAN-HF 誤抓進來，**儘管該 paper 並未研究 ARNI**

### 3.4 Citation 是最容易捏造的元素

「Pierce JB et al. *JAMA Cardiol* 2023;8(7):652-60」這個 citation 在第二輪查證時發現 **PubMed 搜不到** — 用作者 + 期刊 + 年份 + 主題各種組合都沒結果。這是 LLM 最常見的 ghost citation 模式：
- 作者名是合理的姓氏 + 縮寫
- 期刊是真實期刊
- 年份合理
- volume / issue / page 也是合理範圍
- **但這篇 paper 不存在**

---

## 4. 工作流程改變 — Source-First 原則

### 4.1 新規則

> **下筆前先抓 paper。** 任何 HR、% reduction、p-value、CI、發表年份、作者縮寫、樣本數，都不可以從 LLM 訓練記憶寫出，必須先用 PubMed / Semantic Scholar / Zotero MCP 工具 fetch 原文（至少 abstract），並標註數值來源（Table N, page N）。

### 4.2 工具選擇

| 用途 | 首選工具 | 備援 |
|------|---------|------|
| Fetch paper metadata + abstract | `mcp__pubmed__pubmed_fetch_articles` (by PMID) | `mcp__semantic-scholar__get_paper_details` |
| 找尋特定主題的 paper | `mcp__pubmed__pubmed_search_articles` (with author / journal / dateRange filter) | `mcp__semantic-scholar__search_papers` |
| 拉取我的圖書館 | `mcp__zotero__search_items` + `mcp__zotero__get_item` | — |
| 查證 DOI 是否存在 | WebFetch `https://doi.org/<DOI>` | — |

### 4.3 找不到時的處理

- **絕對不要**填一個「合理的猜測數字」當佔位
- 在草稿中標 `[verify: 需要核對 <paper>, <table>]`
- 等查證完成才取代

---

## 5. Round 2 — 新流程的第一次實戰應用

2026-05-12 下午 Novartis 第二輪校稿回來，針對新增的兩頁（slide 12 forest plot + slide 23 CKD prescribing gap）提出問題。**這次在動 slide 23 之前，先依新規則 fetch paper 核對。**

### 5.1 Slide 12 — Forest plot 數據（4 處修正，全部依 Novartis 提供的精確數值）

| Trial | n | 新 HR (95% CI) | 額外修正 |
|-------|---|---------------|---------|
| PARAGLIDE-HF | 466 | 0.85 (0.73 – 0.999) | CI 不跨 1，圖示由金色改藍色（significant） |
| PREMIER (JP) | 400 | 0.69 (0.55 – 0.86) | 加註 LVEF < 40 |
| Danish RWE | 7,338 | 0.85 (0.74 – 0.98) | 原 slide 標 0.78 — 移動 box + CI bar 位置 |
| Optum De Novo | **9,870** | 0.70 (0.62 – 0.79) | n 由 9,176 修正 |

> **Pearl**：Forest plot 圖示顏色編碼 — 藍色 = CI 不跨 1（statistically significant），金色 = CI 跨 1（primary endpoint missed, biomarker/subgroup signal only）。PARAGLIDE-HF 上 CI 0.999 雖然極接近 1，但**形式上不跨 1**，所以視覺呈現應為藍色。

### 5.2 Slide 23 — CKD prescribing gap 表格的關鍵發現

Novartis 提問：「下表 % on ARNI 是指 ≥100% Target Dose 那組嗎？」 — 我先抓 CHAMP-HF 原文驗證。

#### PubMed 查證結果

1. **CHAMP-HF (Greene SJ et al. *JACC* 2018, PMID 30025570)**
   - Abstract 真實報告：
     - 總體 ARNI 處方率：eligible 病人中 27% 沒拿到 ACE/ARB/ARNI 任一種
     - **ARNI target-dose attainment：14%**（不是 45%）
     - ACE/ARB target-dose：17%；beta-blocker target-dose：28%；MRA target-dose：77%
     - 同時三類都達標：1%
   - **沒有** eGFR ≥60 / 30–59 / <30 / dialysis 分層的 ARNI 處方率表格
   - 原文只在 adjusted model 中提到「renal insufficiency 與較低處方率相關」

2. **「Pierce JB et al. *JAMA Cardiol* 2023;8(7):652-60」 — 找不到**
   - 用 PubMed `Pierce JB[Author]` + 各種主題詞 → 0 results
   - 用 author + journal + year 寬鬆搜尋 → 0 results
   - **這是一個 ghost citation**，是 Round 1 我為了支撐 prescribing gap 表格而捏造出來的

3. **最接近的真實 paper：Zahir Anjum D et al. *Clin Epidemiol* 2023, PMID 37489222**
   - Danish nationwide HF cohort 2014–2021
   - 按 eGFR ≥60 / 30–59 / <30 三層比較 HF therapy initiation
   - 但報的是 **HR (initiation rate)**，不是絕對 %
   - 適合作為「CKD 越嚴重，HF therapy 啟用率越低」這個敘事方向的 reference，但不能直接生出 45/25/8/3 這四個 %

#### 處理方案（與講者確認後採用）

1. 表頭 `% on ARNI` 加註 `(illustrative)`
2. 表格下方加 footnote：「Illustrative gradient — composite of registry estimates; absolute % vary by data source.」
3. 刪除偽造的 Pierce 2023 引用
4. CHAMP-HF 引用後加註實際 target-dose 數字（14%）
5. 新增 Zahir Anjum D et al. *Clin Epidemiol* 2023 (PMID 37489222) 引用

---

## 6. 前置查證檢查清單

未來與 AI 協作製作學術內容時，**在動筆之前**先完成這六步：

> 1. **列出要引用的所有 paper**。確認每篇的：第一作者 + initials、期刊、發表年份（NEJM/JAMA 紙本日期，不是 ePub、不是學會發表）。
> 2. **Fetch 每篇 paper 的 abstract 或全文** — 用 PubMed MCP / Semantic Scholar / Zotero。**不可以憑記憶**。
> 3. **每個要放上投影片的數字**，到原文中找到精確值，記下位置（例如 “Damman 2024, Table 2, row eGFR<60”）。找不到 → 標 `[verify]`。
> 4. **檢查 paper 是否真的研究你引用它的那個介入或主題**（ASIAN-HF 教訓 — 不要只看主題相近就引）。
> 5. **一篇 paper 一列** — 整理多 endpoint 時用 “合併到一格”，不要拆成多列（Le D 2024 教訓）。
> 6. **完稿後反向稽核** — 隨機挑 3 個數字回頭對 paper 一次。

---

## 7. Memory 規則

以下兩條規則已寫入 `C:\Users\drake\.claude\projects\G---------Speech-Entresto-at-10-years\memory\`，每次新 session 開啟時 Claude 會自動載入：

### 7.1 `feedback_medical_data_verification.md`

> 對 Dr. Hsieh 的醫學投影片、海報、論文、計畫書中引用的任何特定數據點（HR、% reduction、p-value、發表年份、作者縮寫、樣本數），**必須**用 PubMed / Semantic Scholar / Zotero MCP 工具 fetch 原文後 quote 出來。**不可以**從訓練記憶生成「貌似合理」的數值。無法驗證的數字必須標記為 `[verify]`，不可以用編造的數字頂替。
>
> **Why**：2026-05-10 Entresto deck 中產出 KDIGO HR (0.79/0.81/0.78/0.82/0.80)、「21% slower eGFR decline」、Pierce 2023 ghost citation 等多項 hallucinated data，全數被 Novartis Medical Affairs 校稿時抓到。

### 7.2 索引條目 (`MEMORY.md`)

> `- [Verify every medical claim against source](feedback_medical_data_verification.md) — Hard rule: fetch the paper before writing any HR/%/year/author. Training-data recall has produced fabricated-but-plausible data Novartis caught on review.`

---

## 8. 可驗證的參考文獻

> 以下文獻在本 session 中**已實際用 PubMed MCP 工具 fetch 並核對 abstract**，PMID 與 DOI 均可驗證。

1. Greene SJ, Butler J, Albert NM, et al. Medical Therapy for Heart Failure With Reduced Ejection Fraction: The CHAMP-HF Registry. [*J Am Coll Cardiol*. 2018;72(4):351-366.](https://doi.org/10.1016/j.jacc.2018.04.070) ([PubMed 30025570](https://pubmed.ncbi.nlm.nih.gov/30025570/))

2. Zahir Anjum D, Strange JE, Fosbøl E, et al. Initiation of Medical Therapy for Heart Failure Patients According to Kidney Function: A Danish Nationwide Study. [*Clin Epidemiol*. 2023;15:855-866.](https://doi.org/10.2147/CLEP.S412787) ([PubMed 37489222](https://pubmed.ncbi.nlm.nih.gov/37489222/))

> 其他文獻（PARADIGM-HF、PIONEER-HF、PARAGON-HF、PREMIER、PARAGLIDE-HF、UK-HARP-III、Damman PARADIGM-HF by KDIGO、Nguyen DV SRMA、Le D 2024、Chen FY 2025 等）在本 session 內**尚未獨立用 MCP 工具完整驗證**，僅依 Novartis Medical Affairs 第一手回稿提供的數值修正。下次更新時建議補做完整查證。

---

## 9. Take-home messages

> **Pearl 1**：LLM 產生的醫學數值「aesthetically correct, epistemically wrong」是最危險的錯誤型態 — HR 落在合理區間、視覺呈現一致、不靠原文比對抓不出來。

> **Pearl 2**：Ghost citation 比錯誤數據更難察覺 — 作者、期刊、年份、page 都看似合理，但 paper 根本不存在。**驗證 citation 是否存在**比驗證內容對錯更應該優先做。

> **Pearl 3**：Topic-similarity miscitation（例如 ASIAN-HF 被當 ARNI evidence）是另一種陷阱 — 不能只看主題相近，必須確認該 paper 真的研究了你要引用的介入。

> **Pearl 4**：「Source-first」工作流程的最大價值不是消除錯誤，而是把錯誤**改到容易被抓到**：標 `[verify]` 的數字不會混進完稿，做反向稽核時也容易發現。

> **Pearl 5**：跨機構同儕審查（這次 Novartis Medical Affairs）是 AI 協作製作學術內容**不可或缺**的最後一道防線 — 即使加上 source-first 流程，仍應假設 AI 草稿有錯誤，並安排專家校稿才能對外發表。

---

**Acknowledgements**

- **Huang, Irene CT** (Novartis Medical Affairs, Taiwan) — 兩輪細緻校稿，抓出 KDIGO HR 捏造、Pierce 2023 ghost citation 等多處關鍵錯誤
- **Damman K et al.** 2024 *JACC* PARADIGM-HF by KDIGO tiers paper — 提供本次校稿黃金標準資料來源

---

*Document version: 1.0 · 2026-05-13*
