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
footer: '謝慕揚 MD, PhD, FESC | Leveraging AI for Literature Review — ACS / Efient | 2026'
---

<!-- _class: lead -->

# 在 AI 時代運用人工智慧進行文獻回顧

## 以 ACS 與 Efient (Prasugrel) 為主軸的實戰工作坊

### Leveraging Artificial Intelligence for Literature Review in the Age of AI:
### A Practical Workflow Demonstrated through ACS / Prasugrel Evidence

**謝慕揚 MD, PhD, FESC**
新竹臺大分院 心血管中心
2026-06-07

---

# 本講座的設計 / How This Talk is Organised

## 三個交織的主軸

- **臨床主軸**：ACS 與 **Efient (prasugrel)** 的證據地圖
  → 三個 worked examples：ISAR-REACT 5、de-escalation、special populations
- **工具主軸**：Claude Code + MCP + **Scientific Skills**
  → 把 Claude 當作系統性的研究助理，而不只是聊天機器人
- **方法主軸**：**Prompt Engineering** — 寫好提示詞，把投影片磨亮
  → 從一句模糊問題，迭代到可以上台的講義

> **目標聽眾**：年輕心臟科醫師、住院醫師、想用 AI 跟上文獻的同仁

---

# Outline

1. **Why** — 年輕醫師面對的閱讀困境
2. **Journey** — ChatGPT → Claude.ai → Claude Code
3. **Claude Code & MCP** — 兩個核心引擎
4. **Scientific Skills** — Claude 內建的「科研工具箱」
5. **Prompt Engineering** — 寫好提示詞，把投影片磨亮
6. **Three Worked Examples** — 全部以 **ACS / Efient** 為核心
   - Example 1：**ISAR-REACT 5** — Prasugrel vs Ticagrelor
   - Example 2：**De-escalation** — TROPICAL-ACS / TOPIC / HOST-REDUCE
   - Example 3：**Special Populations** — 老年、低體重、亞洲族群
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
- 單就 **ACS / antiplatelet** 主題，過去 5 年 PubMed 收錄 **逾 12,000 篇**

> **核心矛盾**：文獻產出速度 ≫ 人類閱讀速度

---

# 以 Efient (Prasugrel) 為例：文獻量壓力

### 為什麼選這個藥當主軸？

- **臨床高度相關**：所有 cath lab 的 ACS / PCI 病人都會接觸
- **文獻爭議多**：vs ticagrelor、de-escalation、elderly、Asian dose
- **指引快速演進**：2023 ESC ACS guideline 已修改 default P2Y12 推薦
- **典型「讀不完」的代表**：每年新增 ~600 篇 prasugrel 相關 paper

### 我會用這三個切片來示範

1. **頭對頭比較**：ISAR-REACT 5
2. **降階治療**：TROPICAL-ACS、TOPIC、HOST-REDUCE-POLYTECH-ACS
3. **特殊族群**：ELDERLY-ACS 2、POPular AGE、亞洲低體重

> **沒有 AI 幫忙，要把這三條線串起來，至少需要兩個週末**

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
  我 → 花 3 小時讀一篇 ISAR-REACT 5 → 勉強弄懂 → 沒時間做筆記

After AI:
  我 → 提出 clinical question (例如 "Prasugrel vs Ticagrelor in ACS")
     → Claude 搜尋 PubMed、retrieve full text、提取關鍵 endpoints
     → 我 review、challenge、驗證 HR / CI / p-value
     → 產出教學講義 + 投影片 + 郵件
     → 時間：約 90 分鐘完成完整 workflow
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
- 請它用中文解釋某個統計方法 (如 hierarchical composite endpoint)
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
- **Projects** 功能 → 可以上傳多份 PDF (例如把 ISAR-REACT 5 + bRIGHT subgroup 一次餵進去)
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
- MCP 讓它能直接查 PubMed、Semantic Scholar、bioRxiv、ClinicalTrials.gov、ClinPGx

### 對我的意義

- 每週一個完整 workflow：**搜尋 → 閱讀 → 整理 → 投影片 → 郵件** 全自動
- 每個 handout 都存在 git repo 裡，版本管理、可追溯

---

<!-- _class: divider -->

# Part 3
## Claude Code & MCP
### 兩個核心引擎

---

# Claude Code 三句話說明

- **Anthropic 官方 CLI**，把 Claude 模型直接放進你的終端機
- 不是「聊天框」，而是**可以執行操作的 AI agent**
- 你給它一個 `CLAUDE.md` 檔案 → 它會**自動遵循**你的工作流程

### 為什麼這對醫師很重要

- 你**不需要會寫 code**，可以直接用中文/英文描述
- 所有產出**可重複、可追蹤、可分享**（檔案、Git、Markdown、PDF）
- 一次定義 workflow → 之後每次自動執行

> **下一節我們會看到**：Scientific Skills 把這個 agent 變成「研究助理」

---

# 什麼是 MCP (Model Context Protocol)？

### 比喻

- Claude = 一位聰明的研究助理
- MCP = 這位助理的 **USB 接口**
- 每個 MCP server = 一個外接裝置（PubMed、Semantic Scholar、Gmail、Git、ClinicalTrials.gov…）

### 技術定義

- **Anthropic 於 2024 年 11 月發布**的開放標準
- 標準化 AI 與外部工具（API、DB、file system）的溝通協議
- 任何人都可以寫 MCP server → 生態系快速膨脹

> **意義**：Claude 不再被困在對話框裡，可以直接**操作真實世界**的醫學資料庫

---

# 我每天在用的 MCP Servers

| MCP Server | 功能 | 在 ACS / Efient 範例的角色 |
|-----------|------|---------------------------|
| **PubMed** | 查 3,600 萬筆生醫文獻 | ISAR-REACT 5、TROPICAL-ACS 全文檢索 |
| **Semantic Scholar** | 2 億篇論文 + citation graph | 找 prasugrel 領域 key papers / h-index |
| **bioRxiv / medRxiv** | 預印本 | 抓最新 ACS guideline 與 mechanistic 研究 |
| **ClinicalTrials.gov** | 註冊試驗資料 | 確認 NCT、追進行中的 trials |
| **ClinPGx** (PharmGKB 後繼) | CYP2C19 / 藥物基因 | 解讀 prasugrel vs clopidogrel 在 LOF 病人 |
| **Zotero** | 書目管理 | 匯出 BibTeX、整理 citation |
| **Gmail / Calendar / GitHub** | 工作流自動化 | 草稿 email、行事曆、版本控管 |

---

<!-- _class: divider -->

# Part 4
## Scientific Skills
### Claude 內建的「科研工具箱」

---

# 什麼是 Scientific Skills？

### 簡單說

- **Skills** = 一組打包好的、可重用的「研究流程」
- 每一個 skill 是一份**有結構的 prompt + 工具組合**
- 你只要呼叫名字（如 `literature-review`, `clinical-reports`），Claude 就會自動套用該 skill 的方法論
- 由 Anthropic 與 Claude Scientific Computing 團隊維護

### 為什麼比直接寫 prompt 好

- **可重複**：每次的「文獻回顧」都遵循同一套流程
- **內含領域知識**：例如 `literature-review` 知道要用 PRISMA / PICO 框架
- **與 MCP 自動串接**：skill 自帶該領域常用的資料庫 (PubMed, ClinicalTrials, FDA…)

> **比喻**：MCP 是工具，Skills 是 SOP；Skills 教 Claude 怎麼把工具用得對

---

# Skills vs MCP — 兩者的差別

| 維度 | MCP | Skills |
|------|-----|--------|
| 本質 | 工具（資料來源、API） | 流程（方法論、SOP） |
| 比喻 | USB 接口 | SOP 手冊 |
| 範例 | PubMed MCP、Gmail MCP | `literature-review`、`citation-management` |
| 誰寫 | Anthropic + 社群 + 自己 | Anthropic + 領域專家 |
| 何時呼叫 | 需要外部資料時 | 進入特定 workflow 時 |
| 對醫師意義 | 拓展 AI 能接觸的資料 | 確保 AI 用對的方法做事 |

> **實務上**：Skill 內部會主動呼叫 MCP；你只要呼叫 skill，剩下就交給它

---

# 我在 ACS / Efient workflow 用到的核心 Skills

| Skill | 我用它做什麼 | Efient 範例對應 |
|-------|------------|----------------|
| `literature-review` | PRISMA 式系統性文獻搜尋 | 搜全 ISAR-REACT 系列 + de-escalation 試驗 |
| `citation-management` | Vancouver / DOI / PubMed link 整理 | 產生 30 篇參考文獻清單 |
| `scientific-writing` | 段落式醫學寫作（不只 bullet） | 寫教學講義主文 |
| `clinical-decision-support` | CDS-style 病人分層建議 | Prasugrel vs Ticagrelor 選藥流程 |
| `clinical-reports` | Trial / case report 結構化整理 | TRITON-TIMI 38 結果摘要 |
| `statistical-analysis` | 解讀 HR / CI / NNT / non-inferiority | 解 ISAR-REACT 5 的 win ratio |
| `scientific-visualization` | 出版級圖表 (KM, forest plot) | 三試驗 forest plot |
| `pubmed-database` | 進階 PubMed 查詢 | MeSH 重寫 query |
| `clinicaltrials-database` | 註冊試驗追蹤 | 追 ongoing prasugrel 試驗 |
| `clinpgx-database` | PGx 解讀 | CYP2C19 LOF 對 clopidogrel 的影響 |

---

# `literature-review` Skill — 進入 PRISMA 模式

### 它強迫 Claude 做這幾件事

1. **明確界定 PICO**（Population, Intervention, Comparator, Outcome）
2. **同時查多個資料庫** (PubMed, Semantic Scholar, bioRxiv, ClinicalTrials.gov)
3. **Boolean / MeSH 重寫** query → 提升精準度
4. **去重 + 評分**（相關性、研究設計階層、發表年）
5. **結構化抽取**：study design、N、primary endpoint、result、bleeding
6. **產出 PRISMA flow + 證據表 + 缺口分析**

### 我給它的觸發語

```text
請用 literature-review skill，做一份「prasugrel 在 ACS 的 head-to-head trials」
PRISMA-style 回顧；時間範圍 2007-2026；產出 evidence table + gap analysis。
```

---

# `citation-management` Skill — 一次解決引用格式

### 解決什麼痛點

- 醫師最大的煩惱：**Vancouver 格式手動排很痛**
- AI 容易**幻覺 PMID** → 放進去前要驗證
- DOI / PMID / PMC link 三者要一致

### Skill 自動做的事

- 從 PubMed / Crossref 抓回真實 metadata
- 驗證 DOI 是否可解析（避免 hallucinated DOI）
- 統一格式（Vancouver / AMA / APA）
- 產出 BibTeX、RIS（可直接匯入 Zotero / EndNote）

### 我用的指令

```text
把以下 PMIDs 用 citation-management skill 整理成 Vancouver
含 DOI hyperlink，並驗證每個 link 都能打開。
```

---

# `scientific-writing` Skill — 段落式醫學寫作

### 為什麼重要

- Bullet points 適合投影片，**講義主文需要連貫敘事**
- AI 預設會寫 bullet → 不適合期刊或教科書風格
- 這個 skill 強制段落結構（topic sentence → evidence → implication）

### 兩階段寫作策略

```text
Stage 1: 先請 Claude 列出每段的 outline (3-5 句)
Stage 2: 我審核 outline → 再請 Claude 展開為完整段落
```

> **對 ACS 講義特別有用**：避免 AI 把 ISAR-REACT 5 寫成五個 bullet
> 而是寫成「背景 → 設計 → 結果 → 限制 → 臨床意義」連貫敘事

---

# `clinical-decision-support` Skill — 把證據變決策樹

### 應用場景

- 把「ISAR-REACT 5 顯示 prasugrel 優於 ticagrelor」這個結論
- **轉化為實際 cath lab 的選藥流程**
- 兼顧 contraindication（prior stroke）、特殊族群（age ≥75, BW <60kg）

### Skill 自動產出

- **病人分層表** (risk stratification)
- **決策流程圖** (decision tree, mermaid syntax)
- **禁忌與警示清單** (red flags)
- **替代方案** (alternative regimens)

### 我會把這個 skill 接到 `scientific-writing` 後面

→ 產出「文獻摘要 + 臨床建議」雙層次教學講義

---

# `statistical-analysis` Skill — 解讀 trial 統計

### Efient 三大例子的統計概念

| Trial | 關鍵統計概念 | Skill 做什麼 |
|-------|------------|-------------|
| ISAR-REACT 5 | HR 1.36 (1.09-1.70) | 解釋 ITT vs PP；計算 NNT |
| TROPICAL-ACS | Non-inferiority margin 30% | 解非劣性檢定的閾值意義 |
| HOST-REDUCE-POLYTECH-ACS | 2x2 factorial | 解 factorial design |

### 我請 skill 做的事

```text
請用 statistical-analysis skill，解釋 ISAR-REACT 5 為什麼用 HR 而非 OR；
計算治療 1 年後的 absolute risk reduction 與 NNT；
評估 1.09-1.70 的 CI 是否包含臨床有意義差異。
```

---

# `scientific-visualization` Skill — 自動產生出版級圖

### 對 Efient 範例的應用

- **Forest plot**：ISAR-REACT 5 + TRITON-TIMI 38 + meta-analysis
- **Kaplan-Meier**：模擬重繪 ISAR-REACT 5 primary endpoint 曲線
- **Subgroup forest**：ELDERLY-ACS 2 在 age, sex, DM 各亞群的 HR

### 工具鏈

- skill 會自動選 `matplotlib` / `seaborn` / `plotly`
- 出版級規格：300 DPI、色盲友善、字級足夠
- 直接存成 PNG / SVG → 投影片可用

> **典型 prompt**：「請用 scientific-visualization skill 畫一張 forest plot，
> 比較 prasugrel vs ticagrelor 在 ACS 的 ischemic 與 bleeding endpoint」

---

# `clinpgx-database` — 藥物基因組學的關鍵

### 與 Efient 高度相關

- Clopidogrel 是 prodrug → 需 **CYP2C19** 活化
- **CYP2C19 LOF carrier**（亞洲人約 50-60%）→ clopidogrel 失效
- Prasugrel 與 ticagrelor **不依賴 CYP2C19**
- 在 LOF 病人 → 強適應症使用 prasugrel/ticagrelor

### Skill 自動做的事

- 查 ClinPGx 的 **CPIC guideline**（基因型 → 用藥建議）
- 查特定 SNP（rs4244285, rs4986893）→ 對應 metabolizer 表現型
- 產出「基因檢測 → 用藥決策」對照表

> **臨床啟示**：在 ISAR-REACT 5 的次族群中，prasugrel 的優勢在亞洲族群可能放大

---

# 把 Skills 串起來：我的 ACS / Efient 完整 pipeline

```text
Step 1: literature-review
  → 抓 ISAR-REACT 5、TRITON-TIMI 38、TROPICAL-ACS、TOPIC、
    HOST-REDUCE-POLYTECH-ACS、ELDERLY-ACS 2、POPular AGE

Step 2: citation-management
  → 驗證每個 PMID/DOI；輸出 Vancouver 清單與 BibTeX

Step 3: statistical-analysis
  → 解讀每個試驗的 HR / CI / NNT / non-inferiority margin

Step 4: scientific-writing
  → 段落式講義主文（不要 bullet 海）

Step 5: clinical-decision-support
  → 「Prasugrel 選藥流程」CDS 圖

Step 6: scientific-visualization
  → 三試驗 forest plot + ISAR-REACT 5 KM 曲線

Step 7: pptx + Marp
  → 自動產出投影片 + 教學講義 PDF
```

---

<!-- _class: divider -->

# Part 5
## Prompt Engineering for Slides
### 寫好提示詞，把投影片磨亮

---

# 為什麼提示詞 (Prompt) 重要？

### 同一個 Claude，產出可以差 10 倍

- **壞 prompt**：「幫我做 ISAR-REACT 5 的投影片」
  → 得到模糊、缺數據、沒有引用的 5 張投影片
- **好 prompt**：明確 PICO、輸出格式、字數限制、引用要求
  → 得到可直接上台的 8 張投影片

### 三個原則

1. **明確** (Specific)：少用「好的」「漂亮的」這類抽象詞
2. **結構化** (Structured)：把 prompt 切成 Goal / Context / Format / Constraint
3. **可迭代** (Iterative)：第一次不完美沒關係，下一輪改 1 個面向

---

# 好 Prompt 的四段結構 (GCFC)

```text
[Goal] 我要做什麼
[Context] 給 AI 的背景：聽眾、場合、深度
[Format] 輸出格式：Marp、Markdown、表格、字數
[Constraint] 限制：禁止幻覺、要附 PubMed link、保留英文藥名
```

### Efient 投影片實例

```text
[Goal]    幫我做一張投影片，總結 ISAR-REACT 5 的主要結果
[Context] 對象是新進的 fellow，他們已知 dual antiplatelet 概念，
          但沒讀過原文；報告場合是 cath conference 5 分鐘
[Format]  Marp，1 張 slide，包含：N、design、primary endpoint、
          結果(HR + 95% CI + p)、bleeding、結論一句話
[Constraint] 所有數字對照原文；引用要附 PubMed link；中英對照
```

---

# 用 PICO 寫文獻回顧 prompt

### PICO 框架

| 元素 | ISAR-REACT 5 例 |
|------|----------------|
| **P** Population | ACS 病人，計畫 invasive evaluation |
| **I** Intervention | Prasugrel (60 mg LD → 10 mg QD) |
| **C** Comparator | Ticagrelor (180 mg LD → 90 mg BID) |
| **O** Outcome | Composite of death, MI, stroke at 12 months |

### 寫成 prompt

```text
請用 literature-review skill 找 RCT：
- Population: ACS 病人 (STEMI/NSTEMI/UA)
- Intervention: Prasugrel
- Comparator: Ticagrelor
- Outcome: 12-month MACE (CV death/MI/stroke)
時間：2015-2026；只要 RCT 與 meta-analysis；附 PMID 與 DOI
```

---

# Iterative Prompting — 五輪精修一張投影片

### 第 1 輪 (起手)

> 「做 ISAR-REACT 5 的結果投影片」

→ 得到通用、缺細節的版本

### 第 2 輪 (補數據)

> 「加上 N、HR、95% CI、p value，與 BARC 3-5 bleeding」

### 第 3 輪 (補表格)

> 「把 primary 拆成 death/MI/stroke 各別數字，做成表格」

### 第 4 輪 (補引用)

> 「在投影片底部加上 PubMed link 31475799」

### 第 5 輪 (調風格)

> 「縮成 6 個 bullet 以內；中英對照；強調 stroke 沒有差異」

> **每一輪只改一個維度** — 這樣才能看出哪一輪改壞了

---

# 用 Prompt 修「投影片本身」的技巧

### 我常用的修改類提示詞

```text
1. 簡化 — 「請把這張投影片簡化，每個 bullet 不超過 12 字」
2. 拆分 — 「請把這張投影片分成兩張，避免文字溢出」
3. 補表 — 「請新增一張對比表格：prasugrel vs ticagrelor 的 PK/PD」
4. 補圖 — 「請補上 KM 曲線示意圖（用 mermaid 或 ASCII）」
5. 加引用 — 「在每張 slide 的 H2 副標題加上 PubMed link」
6. 換風格 — 「把這張改成 quote-slide 風格（class: quote-slide）」
7. 中英 — 「把英文術語保留原文，前面加中文翻譯（中文 (English)）」
8. 對齊 CLAUDE.md — 「請依 CLAUDE.md 的 Marp 規範調整 colour scheme」
```

> **訣竅**：把這些 prompt **存成模板**，下次直接複製貼上

---

# 壞 Prompt vs 好 Prompt — 對照範例

| 場景 | ❌ 壞 Prompt | ✅ 好 Prompt |
|------|------------|-------------|
| 找文獻 | 「找 prasugrel 的論文」 | 「用 literature-review skill 找 2019-2026 ACS prasugrel RCT，PRISMA flow，含 PMID」 |
| 做表格 | 「做個比較表」 | 「Marp 表格，欄位：Trial、N、Design、1° Endpoint、HR (CI)、Bleeding；4 列：ISAR-REACT 5、TRITON、TROPICAL、HOST-REDUCE」 |
| 改投影片 | 「這張不好看，改一下」 | 「文字太多，請拆成兩張；第一張只放數據，第二張放臨床啟示，每張 ≤ 6 行」 |
| 寫結論 | 「下個結論」 | 「以一位 cardiology fellow 角度，寫 2 句臨床啟示；不要超出原文」 |

---

# 把 Prompt 存進 CLAUDE.md → 變成 Workflow

### 一次寫好，之後一句話觸發

`CLAUDE.md` 加入 Recurring Tasks：

```markdown
### ACS Antiplatelet 文獻雙週回顧

Trigger: "Antiplatelet 文獻回顧"

Workflow:
1. literature-review skill 搜過去 14 天 PubMed:
   - "P2Y12 inhibitor" OR "prasugrel" OR "ticagrelor" OR "clopidogrel"
   - AND ("acute coronary syndrome" OR "PCI")
2. 分類：head-to-head / de-escalation / special populations
3. citation-management 整理 Vancouver
4. scientific-writing 產出段落式講義
5. Marp 投影片 + PDF
6. 移至 handouts/01-ischemic-heart-disease/
```

> 之後我只要打 **「Antiplatelet 文獻回顧」** → 整個流程自動跑

---

<!-- _class: divider -->

# Part 6
## Three Worked Examples
### 全部以 ACS / Efient 為核心

---

# 三個範例的設計邏輯

| Example | 主題 | 核心試驗 | 學習目標 |
|---------|------|---------|---------|
| **1** | Head-to-head | ISAR-REACT 5 (NEJM 2019) | 體驗一篇 RCT 的完整 AI 拆解 |
| **2** | De-escalation | TROPICAL-ACS (Lancet 2017)、TOPIC (EHJ 2017)、HOST-REDUCE-POLYTECH-ACS (Lancet 2020) | 跨試驗 synthesize；non-inferiority 概念 |
| **3** | Special Populations | ELDERLY-ACS 2 (Circulation 2018)、POPular AGE (Lancet 2020) | 把證據轉成 CDS 流程；亞洲族群延伸 |

> **三個範例使用同一個 toolkit**：
> `literature-review` + `citation-management` + `scientific-writing` + `clinical-decision-support`

---

<!-- _class: divider -->

# Example 1
## ISAR-REACT 5 — Prasugrel vs Ticagrelor
### 一篇 NEJM RCT 的完整 AI 拆解

---

# Example 1 ─ Step 1：定義 Clinical Question

### 我給 Claude Code 的觸發 prompt

```text
請用 literature-review + clinical-reports skill：

[Goal] 我要在下週的 cath conference 報 ISAR-REACT 5 的 15 分鐘
[Context] 聽眾是新進 fellow + senior CV staff
[Format] Marp 投影片 12-15 張 + 中英對照講義
[Constraint] 所有 HR/CI/p 對照原文；附 NCT01944800、PMID 31475799、DOI
            包含一張 evidence table、一張 Asian sub-analysis 後續資料
            (e.g., bleeding patterns)
            最後一張：cath lab 選藥決策建議
```

> **重點**：一個 prompt 同時觸發 **2 個 skills**，並指定**輸出格式 + 限制**

---

# Example 1 ─ Step 2：Claude 自動展開的 PubMed Query

```text
("ISAR-REACT 5"[All Fields])
OR
( ("prasugrel"[MeSH Terms] OR "prasugrel"[Title/Abstract])
  AND ("ticagrelor"[MeSH Terms] OR "ticagrelor"[Title/Abstract])
  AND ("acute coronary syndrome"[MeSH Terms]
       OR "myocardial infarction"[MeSH Terms]
       OR "ACS"[Title/Abstract])
  AND ("randomized controlled trial"[Publication Type]
       OR "randomized"[Title/Abstract])
)
AND ("2018"[PDAT] : "2026"[PDAT])
```

### Claude 同時告訴我

- **主篇**：Schüpke S, et al. NEJM. 2019;381(16):1524-1534
- **重要 sub-analysis**：bleeding subgroup (Heart 2021)、long-term FU (Eur Heart J 2022)、Asia-related secondary analyses

> **價值**：你不用記 PubMed 語法 — 但你看得懂 query 邏輯，可以挑戰它

---

# Example 1 ─ Step 3：Full-text 抽取 (Verified)

### Claude 用 `mcp__pubmed__pubmed_fetch_articles` 抓回完整 abstract

| 欄位 | 數值 / 內容 |
|------|------------|
| **N** | 4,018 (Prasugrel 2,006; Ticagrelor 2,012) |
| **Population** | ACS (STEMI / NSTEMI / UA), invasive evaluation planned |
| **Design** | Multicenter, RCT, **open-label** |
| **Primary** | Death, MI, or stroke at 1 year |
| **Result** | Ticagrelor **9.3%** vs Prasugrel **6.9%** |
| **HR** | 1.36 (95% CI 1.09–1.70), **p = 0.006** |
| **MI** | 4.8% vs 3.0% |
| **Stroke** | 1.1% vs 1.0% (no difference) |
| **BARC 3-5 Bleeding** | 5.4% vs 4.8% (HR 1.12, p = 0.46, **NS**) |
| **Stent thrombosis** | Definite/probable 1.3% vs 1.0% |

> ★ 所有數字都已用 PubMed MCP **驗證過原文**（PMID 31475799）

---

# Example 1 ─ Step 4：Claude 自動產出的 Evidence Table

| Trial | N | Comparator | 1° Endpoint | Result | Bleeding |
|-------|---|------------|-------------|--------|----------|
| **ISAR-REACT 5** (NEJM 2019) | 4,018 | Prasugrel vs Ticagrelor | CV death/MI/stroke 1y | 6.9% vs 9.3% (HR 1.36, p=0.006) | BARC 3-5 NS |
| **TRITON-TIMI 38** (NEJM 2007) | 13,608 | Prasugrel vs Clopidogrel | CV death/MI/stroke ~14m | 9.9% vs 12.1% (HR 0.81, p<0.001) | TIMI major ↑ (2.4% vs 1.8%, p=0.03) |

### 關鍵對照

- **TRITON**：Prasugrel **優於** clopidogrel，但 bleeding 增加
- **ISAR-REACT 5**：Prasugrel **優於** ticagrelor，bleeding 沒差

> **臨床訊息**：在 ACS + invasive 病人，prasugrel 是合理的 first-line 選擇
> （只要排除禁忌：prior stroke、age ≥75、BW <60 kg）

---

# Example 1 ─ Step 5：clinical-decision-support 流程圖

```text
ACS 病人，計畫 invasive evaluation
        |
        ├── 有 prior stroke / TIA?
        │      └── Yes → Avoid prasugrel → Ticagrelor or Clopidogrel
        |
        ├── Age ≥ 75?
        │      └── Yes → 慎用 prasugrel (考慮 5 mg) 或 ticagrelor
        |
        ├── BW < 60 kg?
        │      └── Yes → Prasugrel 5 mg 維持劑量
        |
        └── 無上述條件 → Prasugrel 60/10 mg (ISAR-REACT 5: 1° better than ticagrelor)
```

> **這張圖由 Claude 自動產出**（mermaid syntax → 投影片可用）
> 我只需要 review 是否符合本院 ACS pathway

---

# Example 1 ─ Step 6：Claude 修投影片的對話實錄

### 第 2 輪修改

> **我**：「這張投影片文字太多，請拆成兩張；第一張只放數據，第二張放臨床啟示」

→ Claude 拆成兩張，並自動加上 `<!-- _class: divider -->` 給臨床啟示

### 第 3 輪修改

> **我**：「請把 stroke 那一行用 `**bold**` 強調沒有差異」

→ Claude 改為 **Stroke: 1.1% vs 1.0% (NS)** 並在底下補一句解讀

### 第 4 輪修改

> **我**：「把 KM 曲線換成 mermaid 流程圖（我們沒授權重畫圖）」

→ Claude 換成決策樹 + 註明「KM 詳見原文 Figure 1」

> **每一輪只動一個維度** — 這樣才能精準收斂

---

<!-- _class: divider -->

# Example 2
## De-escalation Strategies
### TROPICAL-ACS / TOPIC / HOST-REDUCE-POLYTECH-ACS

---

# Example 2 ─ 為什麼這個主題重要

### 臨床矛盾

- 強效 P2Y12 (prasugrel/ticagrelor) **降低 ischemic events**
- 但 **bleeding** 累積在 chronic phase
- 想法：早期用強效 → 1 個月後降階為 clopidogrel 或低劑量 prasugrel

### 三個關鍵試驗 (Claude 自動找到)

| 試驗 | 策略 | 引用 |
|------|------|------|
| **TROPICAL-ACS** (Lancet 2017) | Platelet function-guided de-escalation | PMID 28855078 |
| **TOPIC** (EHJ 2017) | 1m 後固定切換到 clopidogrel | Cuisset T et al. |
| **HOST-REDUCE-POLYTECH-ACS** (Lancet 2020) | Prasugrel 10→5 mg 降劑量 | PMID 32882163 |

---

# Example 2 ─ Step 1：跨試驗 PRISMA 搜尋 prompt

```text
請用 literature-review skill：
[Goal] 整理 ACS 病人 antiplatelet de-escalation 的證據
[PICO]
  P: ACS post-PCI 病人，已使用 prasugrel/ticagrelor
  I: 任何 de-escalation 策略 (drug switch / dose reduction / PFT-guided)
  C: 持續 standard 強效 P2Y12
  O: Net clinical benefit (MACE + bleeding) at 1 year
[Format] PRISMA flow + evidence table + 比較圖
[Constraint] 至少要包含 TROPICAL-ACS、TOPIC、HOST-REDUCE-POLYTECH-ACS
            (PMID 28855078, 32882163)；non-inferiority margin 各別交代
```

---

# Example 2 ─ Step 2：Evidence Table（已驗證）

| Trial | N | De-escalation 策略 | 1° Endpoint | Result | 結論 |
|-------|---|-------------------|-------------|--------|------|
| **TROPICAL-ACS** | 2,610 | PFT-guided: 1w prasugrel → 1w clopidogrel → guided | NCB at 1y | 7% vs 9% (HR 0.81, 95% CI 0.62-1.06) | Non-inferior (p_NI = 0.0004) |
| **TOPIC** | 646 | 1m 後固定切到 clopidogrel | BARC ≥2 bleeding | 4.0% vs 14.9% (HR 0.30, p<0.01) | Bleeding ↓; ischemic 不變 |
| **HOST-REDUCE-POLYTECH-ACS** | 2,338 | Prasugrel 10→5 mg @ 1m | NCB at 1y | 7.2% vs 10.1% (HR 0.70, 95% CI 0.52-0.92, p=0.012) | Superior |

> 全部以 PubMed/Lancet/EHJ 原文驗證
> **重要**：HOST-REDUCE 是**亞洲（韓國）人群**的 dose-reduction 試驗

---

# Example 2 ─ Step 3：statistical-analysis 解 non-inferiority

### TROPICAL-ACS 的 30% margin 怎麼讀

```text
Non-inferiority margin = 30%
意思：de-escalation 即使比 standard 差 30%（HR ≤ 1.30 上限），
     仍視為「不劣於」。
原始結果：HR 0.81 (95% CI 0.62-1.06)
- CI 上限 1.06 < 1.30 → 達到 non-inferiority (p_NI = 0.0004)
- CI 上限 < 1.0? 否 → 未達 superiority (p_superiority = 0.12)
```

### Claude 自動補上

- **NNT for bleeding reduction (TOPIC)** ≈ 9 (10.9 個百分點差距)
- **NNT for NCB (HOST-REDUCE)** ≈ 35

> **看 trial 不只看 HR — 看 margin、看 CI 上下限的臨床意義**

---

# Example 2 ─ Step 4：跨試驗綜合啟示

### Claude 自動產出的 synthesis

> 三個試驗從不同角度支持「de-escalation 是可行的」：
> **TROPICAL-ACS** 用 PFT 引導切藥；
> **TOPIC** 證明 1 個月後切到 clopidogrel 不增加缺血；
> **HOST-REDUCE-POLYTECH-ACS** 證明亞洲人 prasugrel 10→5 mg 還能更安全。

### 我加上的臨床經驗

- 本院 cath lab 對 **ACS + 出血高風險** 病人，1 個月後降階是合理選擇
- **PFT 引導**在台灣不普及 → TOPIC / HOST-REDUCE 模式更實用
- **Asian 病人**特別適用 dose reduction (HOST-REDUCE 直接證據)

> **AI 提供 synthesis，醫師補上「本院實況」**

---

<!-- _class: divider -->

# Example 3
## Special Populations
### Elderly / Low BW / Asian

---

# Example 3 ─ 場景與 prompt

### Clinical Question

> *「我下週要對 elderly ACS 病人用 prasugrel — 有什麼證據？亞洲人是否要減量？」*

### 我給 Claude 的 prompt

```text
請用 literature-review + clinpgx-database + clinical-decision-support skill：

[Goal] Special populations 證據彙整 (≥75y, BW<60kg, Asian)
[Trials must include]
  - ELDERLY-ACS 2 (Savonitto S et al., Circulation 2018, PMID 29459361)
  - POPular AGE (Gimbel M et al., Lancet 2020, PMID 32334703)
  - Asian-PrasFit / KOMAR / 日本 prasugrel 3.75 mg 註冊試驗
[Format] Evidence table + CDS 決策圖 + Asian dose 建議
[Constraint] 區分 ≥75y、BW<60kg、Asian 三條線；NCT 號碼必附
```

---

# Example 3 ─ ELDERLY-ACS 2 (Verified via PubMed)

### 設計

- N ~1,400 (early stop)；ACS ≥75y；早期 invasive
- **Prasugrel 5 mg** vs **Clopidogrel 75 mg**
- Primary: composite (mortality, MI, stroke, rehosp for CV event) at 1y

### 結果（Savonitto S, et al. Circulation 2018; PMID 29459361）

| Endpoint | Prasugrel 5mg | Clopidogrel | HR / Δ |
|----------|---------------|-------------|--------|
| Primary composite | ~17.0% | ~16.6% | HR 1.007 (NS) |
| BARC ≥2 bleeding | 4.1% | 2.7% | numerically ↑ |

### 結論

- **Reduced-dose prasugrel 在 elderly 並未顯著優於 clopidogrel**
- 反而 **bleeding 數值偏高**

---

# Example 3 ─ POPular AGE (Verified)

### 設計

- N = 1,002；NSTE-ACS ≥70y
- **Clopidogrel** vs **Ticagrelor (or Prasugrel)** — 1:1 隨機
- 大多數 (95%) 對照組接受 ticagrelor
- Co-primary: PLATO bleeding；NCB (death, MI, stroke, bleeding)

### 結果（Gimbel M, et al. Lancet 2020; PMID 32334703）

| Endpoint | Clopidogrel | Potent (mainly ticagrelor) | HR |
|----------|-------------|---------------------------|----|
| PLATO major/minor bleeding | 18% | 24% | 0.71 (0.54-0.94, p=0.02) |
| NCB | 28% | 32% | non-inferior (Δ -4%, p=0.03 NI) |

### 啟示

- ≥70y NSTE-ACS：**clopidogrel 出血少、總體 NCB 不劣於強效藥**
- Bleeding-driven discontinuation 是大問題（discontinuation 47% vs 22%）

---

# Example 3 ─ 亞洲族群與 Prasugrel 3.75 mg

### 為什麼要降劑量？

- 亞洲人 (尤其日本) **prasugrel 暴露量較高、出血風險較高**
- 日本 PMDA 核准 **prasugrel 3.75 mg/day** 維持劑量（loading 20 mg）
- 韓國 HOST-REDUCE-POLYTECH-ACS：直接驗證 **10→5 mg** 降階優於 10 mg

### Claude 自動補上的 evidence

- **PRASFIT-ACS** (Saito et al., Circ J 2014)：日本人 3.75 mg vs clopidogrel
- **HOST-REDUCE-POLYTECH-ACS** (PMID 32882163)：韓國人 5 mg de-escalation

### 結論

- **亞洲 ACS 病人使用 prasugrel 5 mg 維持劑量是合理選擇**
- 高度建議在 BW <60 kg、age ≥75 同時存在時降階

---

# Example 3 ─ 整合 CDS：Special Populations 選藥

```text
ACS post-PCI 需要 P2Y12 inhibitor
   |
   ├── Prior stroke/TIA?  → Yes → Clopidogrel or Ticagrelor (避免 prasugrel)
   |
   ├── Age ≥ 75? ─────────────────────────┐
   |       └── Yes → POPular AGE: Clopidogrel = ticagrelor in NCB; bleeding ↓
   |              ELDERLY-ACS 2: Prasugrel 5mg ≠ better than clopidogrel
   |              ⇒ 默認 Clopidogrel；若 high ischemic risk, consider Prasugrel 5 mg
   |
   ├── BW < 60 kg? → Prasugrel 5 mg 維持劑量
   |
   └── Asian + 標準 ACS:
           ├── HOST-REDUCE 證據 → 1 個月後 10→5 mg 降階
           └── 高出血風險 → 直接從 5 mg 開始
```

> **這張圖由 `clinical-decision-support` skill 自動產出**

---

# Example 3 ─ 真正的價值在 synthesis

### 三個範例匯流出來的訊息

1. **沒有 high stroke/age/BW 風險** → ISAR-REACT 5 支持 prasugrel
2. **>70y 想避免 bleeding** → POPular AGE 支持 clopidogrel
3. **>75y / BW<60 / Asian** → 降階 (5 mg or 1m de-escalation)
4. **強效 + bleeding 累積** → 1m 後切藥可考慮 (TROPICAL-ACS / TOPIC / HOST-REDUCE)

> **AI 把 7 個試驗的訊息「壓縮」成一張流程圖**
> **而我用 5 分鐘 review 它的邏輯**，補上本院 pathway

---

<!-- _class: divider -->

# Part 7
## Tips & Pitfalls
### 驗證、幻覺、版權

---

# Do's — 讓 AI 更有效的技巧

- **Be specific**：用 PICO + GCFC 結構描述問題
- **Iterate**：第一次結果不滿意 → 要求 Claude 調整策略
- **Cross-reference**：**同時** 用 PubMed 與 Semantic Scholar → 發現盲點
- **Date filters**：指定時間範圍，避免舊資料淹沒新證據
- **MeSH terms**：請 Claude 用 MeSH 重寫 query → 精準度大增
- **Verify**：重要數據（HR、p-value、N）**一律對照原文**
- **Save the prompt**：好用的 prompt 存進 `CLAUDE.md` → 下次直接觸發
- **善用 Skills**：`literature-review` 比手寫 prompt 更穩定

---

# Don'ts (1) — 內容與驗證

### 不要直接相信 AI 的 citation

- Claude 偶爾會 **hallucinate 一個不存在的 PMID/DOI**
- 解法：所有 citation 連結**自己點一次**確認；用 `citation-management` skill

### 不要用 abstract 就下結論

- **Neutral trial 常被誤判成 positive** — POPular AGE 的 NCB **non-inferiority**容易被當成「clopidogrel 比較好」
- 解法：WebSearch 實際的 HR/CI/p-value；讀 full text；看 NI margin

---

# Don'ts (2) — 判斷與隱私

### 不要讓 AI 寫你沒讀過的段落

- Claude 可以產出「看起來像專家」的文字
- 但臨床解讀必須是 **你自己的判斷**

### 不要把病人資料丟進公開 AI

- HIPAA / 個資法 → 使用 Claude for Work 或地端部署
- 原則：**病人 identifier 絕不進入公開 AI**

### 不要把 ISAR-REACT 5 的結論直接套到 medically-managed ACS

- TRILOGY-ACS 顯示 prasugrel 在 medically managed ACS **無顯著優勢**
- AI 不會替你做 trial-to-population 對應；你要

---

# 幻覺 (Hallucination) 最常見的形式

| 類型 | 具體例子 (Efient 相關) | 防範方法 |
|------|----------------------|---------|
| 假 citation | 編出一個 PMID，文章不存在 | 點開 PubMed link 驗證 |
| 錯 N 或百分比 | 把 ISAR-REACT 5 N=4,018 寫成 4,800 | 對照原文 abstract |
| 誤判顯著性 | 把 BARC bleeding p=0.46 寫成「ticagrelor 更易出血」 | 讀 full text 的 primary result |
| 誤植作者 | Schüpke 寫成 Schunkert | 核對第一作者與通訊作者 |
| 過度推論 | 從 ISAR-REACT 5 推到 medically-managed ACS | 自己判斷 study population |

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
- 永遠強調「**讀書會共筆整理人**」而非「精選專家」

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
> 例如：「每週把當期 Circulation 的 ACS 文章整理成中文」

> **3.** **學 Skills 比學 prompt 重要**
> `literature-review` + `citation-management` 兩個就夠你撐很久

---

# 給年輕醫師的 5 個建議 (4–5)

> **4.** **從一個藥、一個主題開始**
> 例如本講座：先把 prasugrel 的 7 個試驗串起來
> 之後再延伸到 ticagrelor、cangrelor、warfarin/DOAC

> **5.** 進階時學 **Claude Code + MCP + Git**
> → 解鎖完整 agent workflow，把 prompt 寫進 `CLAUDE.md`

### 核心理念

- **不要追求完美**，追求**可重複**
- **不要取代自己的判斷**，而是**放大自己的產出**

---

# 我過去一年的實際產出

### 使用 Claude Code 建立的 handouts

| 資料夾 | 主題 | 產出數量 |
|--------|------|---------|
| `01-ischemic-heart-disease/` | ACS, STEMI, PCI, Antiplatelet | 25+ |
| `04-valvular-disease/` | TEER, TAVI | 15+ |
| `10-icu-general/` | ICU biweekly | 30+ |
| `91-podcast-journal-review/` | 每週期刊回顧 | 50+ |

### 累積效益

- **Git repo** 成為我的第二大腦
- 所有教學材料**可搜尋、可版本控管**
- 新加入的住院醫師可以直接讀 repo 學習 prasugrel / ACS pathway

---

# 未來展望 — 短期與中期

### 短期 (2026)

- **Multimodal MCP** → 直接分析 ECG、Echo、Angiogram 影像
- **Long-context models** (1M+ tokens) → 一次讀完整份 ESC ACS guideline
- **Local LLM** → 病人資料可以地端處理

### 中期 (2027–2028)

- **AI-assisted CDS** → 即時 prasugrel/ticagrelor 選藥（整合 CYP2C19、age、BW）
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

# References & Resources (1/2) — Trials

1. Schüpke S, et al. Ticagrelor or Prasugrel in Patients with Acute Coronary Syndromes (**ISAR-REACT 5**). [*N Engl J Med*. 2019;381(16):1524-1534.](https://doi.org/10.1056/NEJMoa1908973) — [PubMed](https://pubmed.ncbi.nlm.nih.gov/31475799/)
2. Wiviott SD, et al. Prasugrel versus Clopidogrel in Patients with Acute Coronary Syndromes (**TRITON-TIMI 38**). [*N Engl J Med*. 2007;357(20):2001-2015.](https://doi.org/10.1056/NEJMoa0706482) — [PubMed](https://pubmed.ncbi.nlm.nih.gov/17982182/)
3. Sibbing D, et al. Guided de-escalation of antiplatelet treatment in patients with ACS undergoing PCI (**TROPICAL-ACS**). [*Lancet*. 2017;390(10104):1747-1757.](https://doi.org/10.1016/S0140-6736(17)32155-4) — [PubMed](https://pubmed.ncbi.nlm.nih.gov/28855078/)
4. Kim HS, et al. Prasugrel-based de-escalation of dual antiplatelet therapy after PCI in ACS (**HOST-REDUCE-POLYTECH-ACS**). [*Lancet*. 2020;396(10257):1079-1089.](https://doi.org/10.1016/S0140-6736(20)31791-8) — [PubMed](https://pubmed.ncbi.nlm.nih.gov/32882163/)
5. Cuisset T, et al. Benefit of switching DAPT after ACS (**TOPIC**). [*Eur Heart J*. 2017;38(41):3070-3078.](https://doi.org/10.1093/eurheartj/ehx175)
6. Savonitto S, et al. Comparison of Reduced-Dose Prasugrel and Standard-Dose Clopidogrel in Elderly Patients with ACS (**ELDERLY-ACS 2**). [*Circulation*. 2018;137(23):2435-2445.](https://doi.org/10.1161/CIRCULATIONAHA.117.032180) — [PubMed](https://pubmed.ncbi.nlm.nih.gov/29459361/)
7. Gimbel M, et al. Clopidogrel versus ticagrelor or prasugrel in patients ≥70y with NSTE-ACS (**POPular AGE**). [*Lancet*. 2020;395(10233):1374-1381.](https://doi.org/10.1016/S0140-6736(20)30325-1) — [PubMed](https://pubmed.ncbi.nlm.nih.gov/32334703/)
8. Saito S, et al. Efficacy and safety of adjusted-dose prasugrel in Japanese patients with ACS (**PRASFIT-ACS**). [*Circ J*. 2014;78(7):1684-92.](https://doi.org/10.1253/circj.CJ-13-1482)

---

<!-- _class: small-text -->

# References & Resources (2/2) — AI / Tools

9. Anthropic. Introducing the Model Context Protocol. [anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol)
10. Anthropic. How scientists are using Claude to accelerate research. [anthropic.com/news/accelerating-scientific-research](https://www.anthropic.com/news/accelerating-scientific-research)
11. Anthropic. Claude for Life Sciences. [anthropic.com/news/claude-for-life-sciences](https://www.anthropic.com/news/claude-for-life-sciences)
12. Anthropic. Claude Code Documentation. [docs.claude.com/en/docs/claude-code](https://docs.claude.com/en/docs/claude-code)
13. Anthropic. Skills (Scientific Skills). [docs.claude.com/en/docs/skills](https://docs.claude.com/en/docs/skills)
14. Tay A. MCP Servers and Academic Search. [aarontay.substack.com](https://aarontay.substack.com/p/mcp-servers-and-academic-search-the)
15. Tay A. The Agentic Researcher. [aarontay.substack.com](https://aarontay.substack.com/p/creating-your-own-research-assistant)
16. NCBI E-utilities Documentation. [ncbi.nlm.nih.gov/books/NBK25501](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
17. Semantic Scholar API. [api.semanticscholar.org](https://api.semanticscholar.org/)
18. ClinPGx (formerly PharmGKB). [clinpgx.org](https://www.clinpgx.org/)
19. Marp — Markdown Presentation Ecosystem. [marp.app](https://marp.app/)
20. Model Context Protocol — Official Specification. [modelcontextprotocol.io](https://modelcontextprotocol.io/)

---

<!-- _class: lead -->

# 謝謝聆聽

## Questions & Discussion

**謝慕揚 MD, PhD, FESC**
新竹臺大分院 心血管中心

*本投影片由 Claude Code + MCP + Scientific Skills 協助製作*
*All slides built with Claude Code — an AI agent for medical education*

*2026-06-07 · 主軸：ACS / Efient (Prasugrel)*
