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
    font-size: 24px;
    padding: 50px 60px 70px 60px;
    line-height: 1.45;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
    padding-top: 80px;
  }
  section.lead h1 {
    color: #ffffff;
    font-size: 1.8em;
    border-bottom: none;
    margin: 0 0 0.3em 0;
  }
  section.lead h2 {
    color: #b0c4de;
    font-size: 1.05em;
    font-weight: normal;
    margin: 0.2em 0;
    border-bottom: none;
  }
  section.lead h3 {
    color: #ffffff;
    font-size: 0.72em;
    font-weight: normal;
    margin: 0.3em 0 1em 0;
    opacity: 0.9;
    line-height: 1.4;
  }
  section.lead p {
    color: #dfe6e9;
    margin: 0.3em 0;
  }
  section.lead strong {
    color: #ffffff;
  }
  section.lead em {
    color: #b0c4de;
  }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 0 80px;
  }
  section.divider h1 {
    color: #ffffff;
    border-bottom: none;
    font-size: 2.0em;
    text-align: center;
    margin: 0 0 0.2em 0;
  }
  section.divider h2 {
    color: #ffffff;
    border-bottom: none;
    text-align: center;
    font-weight: 600;
    font-size: 1.25em;
    margin: 0.1em 0;
  }
  section.divider h3 {
    color: #e3f2fd;
    text-align: center;
    font-weight: normal;
    font-size: 1.0em;
    margin: 0.3em 0;
  }
  h1 {
    color: #ba181b;
    border-bottom: 3px solid #ba181b;
    padding-bottom: 0.15em;
    font-size: 1.35em;
    margin: 0 0 0.5em 0;
  }
  h2 {
    color: #0072bc;
    font-size: 1.02em;
    margin: 0.5em 0 0.2em 0;
  }
  h3 {
    color: #444444;
    font-size: 0.95em;
    margin: 0.4em 0 0.15em 0;
  }
  p { margin: 0.25em 0; }
  ul, ol { margin: 0.25em 0; padding-left: 1.4em; }
  li { margin: 0.1em 0; }
  table { font-size: 0.68em; width: 100%; margin: 0.3em 0; border-collapse: collapse; }
  th {
    background-color: #0072bc;
    color: white;
    padding: 6px 10px;
    text-align: left;
  }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.4em 0.9em;
    margin: 0.35em 0;
    font-size: 0.85em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 6px;
    padding: 0.6em 0.8em;
    font-size: 0.58em;
    margin: 0.3em 0;
    line-height: 1.35;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code {
    background-color: #f1f2f6;
    color: #c7254e;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.82em;
  }
  strong { color: #ba181b; font-weight: 700; }
  em { color: #0072bc; }
  a { color: #0072bc; }
  footer {
    color: #787878;
    font-size: 0.55em;
  }
  section::after {
    color: #999;
    font-size: 0.65em;
  }
  section.small-text { font-size: 0.72em; }
  section.small-text li { margin: 0.05em 0; }
  section.small-text ol { padding-left: 1.5em; }
  section.quote-slide {
    background-color: #f8f9fa;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  section.quote-slide h1 {
    color: #0072bc;
    border-bottom: 3px solid #0072bc;
    font-size: 1.2em;
  }
  section.quote-slide blockquote {
    font-size: 1.2em;
    border-left: 6px solid #0072bc;
    background-color: #e3f2fd;
    color: #1a2740;
    padding: 0.8em 1.2em;
    line-height: 1.6;
  }
  section.quote-slide blockquote strong {
    color: #ba181b;
  }
footer: '謝慕揚 MD, PhD, FESC | Leveraging AI for Literature Review | 2026'
---

<!-- _class: lead -->

# 在 AI 時代運用人工智慧進行文獻回顧

## 實務與流程 — 以 Claude Code 為主軸

### Leveraging Artificial Intelligence for Literature Review in the Age of AI: Practical Approaches and Workflows

**謝慕揚 MD, PhD, FESC**
新竹臺大分院 心血管中心
2026-04-24

---

# 今天的主軸 / The Axis of This Talk

## Claude Code × AI — 給年輕醫師的文獻回顧旅程

- **不是** AI 技術介紹，也不是工程師講座
- 而是一位心臟科醫師如何用 AI 改寫自己的閱讀習慣
- 從 **「看不完」** 到 **「看得完、整理得起來、教得出來」**
- 以真實的每週期刊回顧、TEER/TAVI 雙週更新、ICU 文獻整理為例

> **給年輕醫師的訊息**：不需要會寫程式，也可以讓 AI 幫你進行高品質文獻回顧

---

# Outline

1. **Why** — 年輕醫師面對的閱讀困境
2. **Journey** — 我的 AI 工具演進：ChatGPT → Claude.ai → Claude Code
3. **What is Claude Code** — 為什麼是它
4. **MCP** — 讓 AI 與學術資料庫直接對話
5. **Workflows** — 我每週實際在跑的 4 個流程
6. **Live Walkthrough** — 從一個問題到一份教學講義
7. **Tips & Pitfalls** — 驗證、幻覺、版權
8. **Key Takeaways** — 你明天就能開始

---

<!-- _class: divider -->

# Part 1
## Why AI for Literature Review?
### 為什麼年輕醫師需要 AI 幫忙讀文獻

---

# 年輕醫師的真實處境

### 一週的時間配置

- 查房、門診、值班、會議、教學 → **80+ hours/week**
- 剩下讀文獻的時間 → 通勤、睡前、週末
- 想跟上 cardiology 的文獻 → **完全不可能**

### 文獻供給端的膨脹

- PubMed 已索引 **3,600 萬+** 篇生醫文獻
- 每年新增 **150 萬篇**
- 光是 NEJM + Lancet + JACC + Circulation + EHJ + EuroIntervention **每週就有 50+ 篇原著論文**

> **核心矛盾**：文獻產出速度 ≫ 人類閱讀速度

---

# 傳統 vs AI 時代的文獻回顧

| 面向 | 傳統做法 | AI 時代做法 |
|------|---------|------------|
| 搜尋 | 手動 Boolean query，反覆試 | 用自然語言描述問題，AI 迭代優化 |
| 篩選 | 一篇篇看標題與摘要 | 批次相關性評分 + 關鍵句擷取 |
| 閱讀 | 單篇深讀，耗時數小時 | 跨篇 synthesize，保留 citation |
| 整理 | 手動做表格、手寫 summary | 結構化表格 + 自動 citation export |
| 教學 | 做 slides → 另一輪工作 | 同一 workflow 自動產出講義 + 投影片 |

---

# 關鍵的 mindset shift

```text
Before AI:
  我 → 花 3 小時讀一篇 NEJM → 勉強弄懂 → 沒時間做筆記

After AI:
  我 → 提出 clinical question
     → Claude 搜尋、retrieve full text、提取關鍵資訊
     → 我 review、challenge、驗證
     → 產出教學講義 + 投影片 + 郵件
     → 時間：2 小時完成完整 workflow
```

> **角色轉變**：醫師從 **「搜尋者」** 變成 **「策略師 + 驗證者」**
> AI 處理 mechanical work，人類處理 clinical judgement

---

<!-- _class: divider -->

# Part 2
## The Journey
### 我的 AI 工具演進史

---

# Stage 1: ChatGPT 時代 (2023)

### 我最初的用法

- 把 NEJM abstract 貼進去 → 請它翻譯 + 整理
- 請它用中文解釋某個統計方法
- 詢問某個疾病的 differential diagnosis

### 問題

- **幻覺 (hallucination)** 嚴重：會編造不存在的 citation
- 無法存取真實 PubMed → 只能用訓練資料
- 只能 copy-paste，**無法處理檔案**
- 產出無法直接用於教學（格式、排版要手動重做）

> **結論**：對短問答有用，對系統性文獻回顧**完全不夠**

---

# Stage 2: Claude.ai 網頁版時代 (2024)

### 進步的地方

- Claude 的臨床推理能力更強
- **Projects** 功能 → 可以上傳多份 PDF
- Artifacts → 可以直接產出 Markdown 表格、HTML

### 仍然的限制

- 無法真正「搜尋」PubMed，只能處理使用者上傳的 PDF
- 每次對話有 context 限制
- 產出仍然需要手動整理、存檔、排版
- 無法執行 code、無法 run shell command

> **關鍵轉捩點**：2024 年 11 月 Anthropic 推出 **MCP (Model Context Protocol)**

---

# Stage 3: Claude Code 時代 (2025–現在)

### 典範轉移 (Paradigm Shift)

- Claude 從「聊天機器人」變成「**AI agent**」
- 可以：**讀寫檔案、執行指令、搜尋網路、呼叫 MCP servers**
- 直接在我的電腦上操作 → 產出可以直接存成檔案、推上 Git
- MCP 讓它能直接查 PubMed、Semantic Scholar、bioRxiv、ClinicalTrials.gov

### 對我的意義

- 每週一個完整 workflow：**搜尋 → 閱讀 → 整理 → 投影片 → 郵件** 全自動
- 每個 handout 都存在 git repo 裡，版本管理、可追溯

---

# 我這個 repo 的實際樣貌

```text
journal-reading/
├── CLAUDE.md                    # 專案指示 (給 Claude Code 的 instructions)
├── handouts/
│   ├── 01-ischemic-heart-disease/
│   ├── 02-heart-failure/
│   ├── 03-arrhythmia/
│   ├── 04-valvular-disease/    # TEER, TAVI biweekly reviews
│   ├── 10-icu-general/          # ICU 文獻
│   ├── 11-icu-respiratory/
│   ├── 20-pulmonary-embolism/
│   ├── 90-ai-technology/        # ← 這份投影片所在
│   └── 91-podcast-journal-review/  # 每週期刊 podcast 回顧
```

> **每一個資料夾都是 AI agent 協助產出的教學講義**

---

<!-- _class: divider -->

# Part 3
## What is Claude Code?
### 為什麼選擇它作為文獻回顧的主工具

---

# Claude Code 三句話說明

- **Anthropic 官方 CLI**，把 Claude 模型直接放進你的終端機
- 不是「聊天框」，而是**可以執行操作的 AI agent**
- 你給它一個 `CLAUDE.md` 檔案 → 它會**自動遵循**你的工作流程

### 傳統 IDE vs Claude Code

| 面向 | 傳統工具 (Cursor/Copilot) | Claude Code |
|------|--------------------------|-------------|
| 主要使用場景 | 寫 code | 完成任務 |
| 工具使用 | 限定編輯器內 | 檔案、shell、web、MCP 全開放 |
| 任務複雜度 | 單點補全 | 多步驟 agent workflow |
| 對非工程師 | 學習曲線陡 | **可以直接用自然語言** |

---

# 為什麼這對醫師很重要

### 你不需要會寫 code

- 用中文或英文描述你要做什麼
- Claude Code 自己知道：怎麼讀檔案、怎麼呼叫 MCP、怎麼產出 PDF
- 你 review 結果、指出錯誤、它自己修正

### 你得到的是**可重複、可追蹤、可分享**的 workflow

- 所有產出都存成檔案（Markdown、PDF、投影片）
- 所有對話邏輯記錄在 `CLAUDE.md` → 下次自動執行
- Git 版本管理 → 今天做的整理，三個月後還找得到

---

# Claude Code 能做什麼：以我的使用為例

| 任務 | 傳統做法 | Claude Code 做法 |
|------|---------|-----------------|
| 搜尋 PubMed 本週 TEER 文章 | 開瀏覽器、寫 query、一篇篇開 | 一句話 → 列出所有文章 + abstract |
| 下載 NEJM full text | 手動 login、存 PDF | `mcp__pubmed__get_full_text_article` 直接取 |
| 整理成中英對照講義 | 複製、貼上、翻譯、排版 | 自動依 `CLAUDE.md` 模板產出 |
| 做成投影片 | PowerPoint 手動畫 | Marp Markdown → CLI 轉 PDF |
| 寄給同事的 email | 另外排版 HTML | `gmail_createDraft` MCP tool 直接產生 draft |
| 版本管理 | 不存在 | Git commit + push |

---

<!-- _class: divider -->

# Part 4
## MCP — Model Context Protocol
### 讓 AI 與學術資料庫直接對話

---

# 什麼是 MCP？

### 用一個比喻

- Claude = 一位聰明的研究助理
- MCP = 這位助理的 **USB 接口**
- 每個 MCP server = 一個外接裝置（PubMed、Semantic Scholar、Gmail、Git…）

### 技術定義

- **Anthropic 於 2024 年 11 月發布**的開放標準
- 標準化 AI 與外部工具（API、DB、file system）的溝通協議
- 任何人都可以寫 MCP server → 生態系快速膨脹

> **意義**：Claude 不再被困在對話框裡，可以直接**操作真實世界**

---

# 我每天在用的 MCP Servers

| MCP Server | 功能 | 我的使用場景 |
|-----------|------|------------|
| **PubMed** | 查詢 3,600 萬筆生醫文獻 | 每週期刊回顧、TEER biweekly |
| **Semantic Scholar** | 2 億篇論文、citation graph | 找領域 key papers、作者 h-index |
| **bioRxiv / medRxiv** | 預印本搜尋 | 搜尋尚未出版的前沿研究 |
| **Zotero** | 書目管理 | 匯出 BibTeX、整理 citation |
| **Gmail** | 郵件 draft | 自動產出教學講義分享信 |
| **Google Calendar** | 會議行程 | Meeting Reply、晨會確認 |
| **Filesystem / GitHub** | 檔案操作、版本控管 | 所有 handout 存檔與同步 |

---

# 設定 MCP：比你想的簡單

### Claude Desktop / Claude.ai 網頁版

1. 打開 Settings → Connectors
2. 點選要的 MCP (PubMed, Semantic Scholar…)
3. 按 Connect → 完成

### Claude Code CLI

```bash
# 在 .claude.json 加入
{
  "mcpServers": {
    "pubmed": { "command": "npx", "args": ["-y", "@modelcontextprotocol/pubmed"] },
    "semantic-scholar": { ... }
  }
}
```

> **大多數 MCP 不需要 API key**（PubMed 使用公開的 NCBI E-utilities）

---

<!-- _class: divider -->

# Part 5
## Core Workflows
### 我每週實際在跑的 4 個流程

---

# Workflow A: 每週心臟科期刊回顧

### Trigger
我只需要輸入：**「每週期刊文獻回顧」**

### Claude Code 自動執行

```text
1. 確定日期範圍（過去 7 天）
2. 用 PubMed MCP 搜尋 6 本期刊：
   NEJM、Lancet、EHJ、JACC、Circulation、EuroIntervention
3. 取得 metadata + abstracts
4. 用 WebSearch 驗證重要試驗結果 (HR, CI, p-value)
5. 依期刊分類、挑選 top picks
6. 產出教學講義 + Marp 投影片 + PDF
```

**時間**：從原本的**一個週末** → 現在**約 1 小時**

---

# Workflow B: TEER / TAVI 雙週文獻回顧

### 場景
我負責 **MitraClip / Pascal / TriClip TEER** 手術；TAVI 是例行工作

### Claude Code 流程

```text
1. Trigger: "TEER 文獻回顧"
2. PubMed + Semantic Scholar 搜尋過去 14 天
3. 分類：
   - Mitral TEER (MitraClip, PASCAL)
   - Tricuspid TEER (TriClip)
   - Imaging / Technique / Complications
4. 產出 biweekly review handout + Marp slides
5. 所有引用附 DOI / PubMed link
```

> **需求**：保持對**最新文獻**的即時掌握 → 影響病人選擇、手術策略

---

# Workflow C: Podcast 講義化

### 來源
JACC This Week、Circulation on the Run、EHJ Podcast、Turning Point

### 流程

```text
1. 擷取 YouTube 音訊 (yt-dlp)
2. Whisper 轉成 SRT 字幕
3. Claude Code 讀 SRT + WebFetch podcast show notes
   + PubMed 查 full text
4. 產出完整中英對照講義
5. Marp 投影片 → PDF
6. HTML email draft → 分享給同仁
```

> **意義**：把 40 分鐘的英文 podcast 變成 15 頁中英對照的可讀講義

---

# Workflow D: ICU 重症文獻雙週回顧

### 為什麼重要
ICU 文獻橫跨多學科：pulmonology、nephrology、hemodynamics、neurology…

### 我的做法

```text
1. Trigger: "Critical Care biweekly"
2. 同時搜尋：
   - Intensive Care Medicine、Critical Care Medicine、AJRCCM
   - NEJM / JAMA / Lancet critical care 相關文章
3. 依主題分類（vent, hemodynamics, sepsis, AKI...）
4. 重點：Claude 標記最新文獻與現行 guideline 的差異
5. 產出講義 → 帶到每雙週 ICU case conference 討論
```

---

# 我的 CLAUDE.md 是核心「食譜」

### 這個檔案告訴 Claude Code

- **身份**：謝慕揚醫師，心臟科、ICU
- **語言**：Traditional Chinese 為主，藥名/trial name 保留英文
- **格式規範**：Markdown 為主，Marp 投影片附 YAML front matter
- **Workflow triggers**：「每週期刊回顧」對應什麼流程
- **檔案命名規範**：`Topic 教學講義.md`、`Topic_Marp.md`
- **後處理**：產完 PDF 後自動刪掉原始 article PDF

> **一次寫好 CLAUDE.md → 之後每次都自動遵循**
> 這就是「agent workflow」的威力

---

<!-- _class: divider -->

# Part 6
## Live Walkthrough
### 從一個問題 → 一份教學講義

---

# 今天我們要跑的例子

### Clinical Question

> *「TriClip 在 severe tricuspid regurgitation 的最新證據是什麼？
> 我要在下週三的 case conference 報 15 分鐘。」*

### 我給 Claude Code 的 prompt

```text
請幫我整理 TriClip 在 severe TR 的文獻回顧：
- 搜尋 PubMed 過去 2 年的 RCT、registry、meta-analysis
- 補充 Semantic Scholar 的 early feasibility 和 imaging paper
- 重點放在 TRILUMINATE Pivotal 2-year data
- 產出 15 頁的 Marp 投影片 + 教學講義
```

---

# Step 1: PubMed 搜尋

Claude 自動構建 Boolean query：

```text
("TriClip" OR "tricuspid edge-to-edge" OR "tricuspid TEER"
 OR "transcatheter tricuspid repair")
AND (randomized[Publication Type] OR "meta-analysis"[Publication Type]
     OR "multicenter study"[Publication Type])
AND ("2024"[PDAT] : "2026"[PDAT])
```

回傳：
- TRILUMINATE Pivotal 2-year follow-up (NEJM 2025)
- bRIGHT registry (JACC 2024)
- Sorajja et al. meta-analysis (Circulation 2025)
- 另外 18 篇 observational

---

# Step 2: Semantic Scholar 補強

```text
問題：PubMed 可能錯過哪些？
- 會議 abstract (ESC, TCT, EuroPCR)
- 影像方面的 AI/ML paper
- 工程設計的 bench study
```

Claude 用 Semantic Scholar MCP 找到：
- 3 篇 TCT 2025 late-breaking
- 1 篇 intraprocedural AI imaging paper
- 2 篇 device iteration study

> **價值**：PubMed + Semantic Scholar **覆蓋率互補**

---

# Step 3: Full Text 深入

### Claude Code 的動作

```text
mcp__pubmed__get_full_text_article(PMID="39XXXXXX")
  → 取得 TRILUMINATE 2-year full text from PMC
```

### 自動提取

- **納入/排除條件**、**Primary endpoint** (KCCQ、TR reduction)
- **Secondary endpoints** (mortality、HF hospitalization)
- **Safety** (bleeding、SLDA、device-related)
- **Subgroup analyses** (TR severity、RV function)

> **提醒**：AI 提取的數據 **一律要對照原文驗證** 後才使用

---

# Step 4: Synthesize → Evidence Table

Claude 產出：

| Study | N | Device | Design | 1° Endpoint | Result |
|-------|---|--------|--------|-------------|--------|
| TRILUMINATE Pivotal 2y | 350 | TriClip | RCT | Hierarchical composite | Win ratio 1.48, p=0.002 |
| bRIGHT 1y | 511 | TriClip | Registry | TR ≤ moderate | 78% |
| Sorajja meta-analysis | 2,100 | All TEER | MA | 30-day mortality | 1.8% (pooled) |

### 同時產出
- **中英對照 handout** (依 `CLAUDE.md` 格式)
- **Marp 投影片** (15 張，含所有 DOI link)
- **BibTeX** (for Zotero import)

---

# Step 5: 檢查、修改、輸出

### 我 (人類) 的角色

1. **Review handout** — 檢查臨床解讀是否正確
2. **驗證關鍵數據** — 對照原文 table
3. **補上 teaching pearls** — 我個人的臨床經驗
4. **調整 emphasis** — 哪些是聽眾需要知道的

### Claude Code 的角色

5. **生成最終 PDF** — `marp --no-stdin --pdf`
6. **Git commit** — 版本化
7. **創建分享 email** — Gmail draft

**總時間：約 90 分鐘**（傳統做法：整個週末）

---

<!-- _class: divider -->

# Part 7
## Tips & Pitfalls
### 驗證、幻覺、版權

---

# Do's — 讓 AI 更有效的技巧

- **Be specific**：PICO 框架 (Population, Intervention, Comparator, Outcome) 描述問題
- **Iterate**：第一次結果不滿意 → 要求 Claude 調整策略
- **Cross-reference**：**同時** 用 PubMed 與 Semantic Scholar → 發現盲點
- **Date filters**：指定時間範圍，避免舊資料淹沒新證據
- **MeSH terms**：請 Claude 用 MeSH 重寫 query → 精準度大增
- **Verify**：重要數據（HR、p-value、N）**一律對照原文**
- **Save the prompt**：好用的 prompt 存進 `CLAUDE.md` → 下次直接觸發

---

# Don'ts (Part 1) — 內容與驗證

### 不要直接相信 AI 的 citation

- Claude 偶爾會 **hallucinate 一個不存在的 PMID/DOI**
- 解法：所有 citation 連結**自己點一次**確認

### 不要用 abstract 就下結論

- **Neutral trial 常被誤判成 positive**
- 解法：WebSearch 實際的 HR/CI/p-value；讀 full text

---

# Don'ts (Part 2) — 判斷與隱私

### 不要讓 AI 寫你沒讀過的段落

- Claude 可以產出「看起來像專家」的文字
- 但臨床解讀必須是 **你自己的判斷**

### 不要把病人資料丟進公開 AI

- HIPAA / 個資法 → 使用 Claude for Work 或地端部署
- 原則：**病人 identifier 絕不進入公開 AI**

---

# 幻覺 (Hallucination) 最常見的形式

| 類型 | 具體例子 | 防範方法 |
|------|---------|---------|
| 假 citation | 編出一個 PMID，文章不存在 | 點開 PubMed link 驗證 |
| 錯 N 或百分比 | 把 350 寫成 500 | 對照原文 table |
| 誤判顯著性 | p=0.08 寫成 "significant" | 讀 full text 的 primary result |
| 誤植作者 | Stone 寫成 Cohen | 核對第一作者與通訊作者 |
| 過度推論 | 從 observational 推 causality | 自己判斷 study design |

> **黃金法則**：AI 提出的每一個臨床結論，都需要你親眼看到原文 confirm

---

# 版權與倫理

### Full text 的取得

- **PubMed Central (PMC)** 的 open-access 文章可自由下載
- **非 open-access** 需要機構 subscription → Claude 無法跳過 paywall

### AI 產出的文件使用

- **教學自用** → 完全沒問題
- **對外分享** → 註明「由 AI 協助整理，僅供教學參考」
- **論文投稿** → 依期刊 AI 使用政策揭露

### 我的做法

- 每份 handout 底部：**「謝慕揚 MD, PhD, FESC — 讀書會共筆整理」**

---

<!-- _class: divider -->

# Part 8
## Key Takeaways
### 你明天就能開始

---

# 給年輕醫師的 5 個建議 (1–3)

> **1.** 先從 **Claude.ai 網頁版 + PubMed connector** 開始
> 不需要學 CLI，瀏覽器就能用

> **2.** 找一個**你每週會做的重複任務**試水溫
> 例如：「每週把 JACC 當期目錄整理成中文」

> **3.** 把 prompt 寫成**模板**，存進 Notes 或 txt
> 下次直接複製 → 一致性是關鍵

---

# 給年輕醫師的 5 個建議 (4–5)

> **4.** **從一份 handout 開始**，別一開始就做系統回顧
> 小成功會帶來下一步動力

> **5.** 進階時再學 **Claude Code + MCP + Git**
> → 解鎖完整 agent workflow

### 核心理念

- **不要追求完美**，追求**可重複**
- **不要取代自己的判斷**，而是**放大自己的產出**

---

# 我過去一年的實際產出

### 使用 Claude Code 建立的 handouts

| 資料夾 | 主題 | 產出數量 |
|--------|------|---------|
| `01-ischemic-heart-disease/` | ACS, STEMI, PCI | 20+ |
| `04-valvular-disease/` | TEER, TAVI | 15+ |
| `10-icu-general/` | ICU biweekly | 30+ |
| `91-podcast-journal-review/` | 每週期刊回顧 | 50+ |

### 累積效益

- **Git repo** 成為我的第二大腦
- 所有教學材料**可搜尋、可版本控管**
- 新加入的住院醫師可以直接讀 repo 學習

---

# 未來展望 — 短期與中期

### 短期 (2026)

- **Multimodal MCP** → 直接分析 ECG、Echo、Angiogram 影像
- **Long-context models** (1M+ tokens) → 一次讀完整份 guideline
- **Local LLM** → 病人資料可以地端處理

### 中期 (2027-2028)

- **AI-assisted clinical decision support** → 即時文獻 + 病人 chart 整合
- **Peer review 自動化** → 上傳原稿，AI 先做結構化 review
- **虛擬研究助理** → 從 literature review 到 grant writing 全流程

---

# 未來展望 — 長期願景

### 我們要追求的方向

- AI 處理**可自動化的認知勞動**（搜尋、閱讀、整理、分類）
- 醫師專注於**高價值的人類判斷**（臨床決策、病人溝通、教學）
- 年輕醫師**不需要犧牲睡眠**來跟上文獻

> **AI 讓年輕醫師可以專注於「臨床判斷」與「病人關係」**
> 而把文獻追蹤、整理、分享的**認知負擔**交給 AI agent

---

<!-- _class: quote-slide -->

# 最後一句話

> **AI 不會取代醫師，
> 但懂得使用 AI 的醫師，
> 會領先不懂得使用 AI 的醫師。**

**— 給下一個十年的年輕心臟科醫師**

---

<!-- _class: small-text -->

# References & Resources

1. Anthropic. Introducing the Model Context Protocol. [anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol)
2. Anthropic. How scientists are using Claude to accelerate research. [anthropic.com/news/accelerating-scientific-research](https://www.anthropic.com/news/accelerating-scientific-research)
3. Anthropic. Claude for Life Sciences. [anthropic.com/news/claude-for-life-sciences](https://www.anthropic.com/news/claude-for-life-sciences)
4. Anthropic. Claude Code Documentation. [docs.claude.com/en/docs/claude-code](https://docs.claude.com/en/docs/claude-code)
5. Tay A. MCP Servers and Academic Search. [aarontay.substack.com](https://aarontay.substack.com/p/mcp-servers-and-academic-search-the)
6. Tay A. The Agentic Researcher. [aarontay.substack.com](https://aarontay.substack.com/p/creating-your-own-research-assistant)
7. NCBI E-utilities Documentation. [ncbi.nlm.nih.gov/books/NBK25501](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
8. Semantic Scholar API. [api.semanticscholar.org](https://api.semanticscholar.org/)
9. Marp — Markdown Presentation Ecosystem. [marp.app](https://marp.app/)
10. Model Context Protocol — Official Specification. [modelcontextprotocol.io](https://modelcontextprotocol.io/)

---

<!-- _class: lead -->

# 謝謝聆聽
## Questions & Discussion

**謝慕揚 MD, PhD, FESC**
新竹臺大分院 心血管中心

*本投影片由 Claude Code 與 MCP 整合協助製作*
*All slides were built with Claude Code — an AI agent for medical education*
