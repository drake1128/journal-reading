# AI for Scientific Research: Anthropic Case Study — 科學家如何運用 Claude 加速研究與發現

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-01-18**
**原文連結：[Anthropic Blog — How Scientists Are Using Claude to Accelerate Research and Discovery](https://www.anthropic.com/research/claude-for-science)**

---

## 核心重點摘要

> **主要訊息**：Claude 已從基礎的文獻回顧與程式撰寫工具，進化為能參與研究全流程的 AI 協作夥伴，包括實驗設計、數據分析與假說生成。

**效率提升**：
- Genome-wide association study (GWAS) 分析：數月 → 20 分鐘
- 穿戴式裝置數據分析（450 檔案）：3 週 → 35 分鐘
- CRISPR knockout 實驗解讀：數百小時人工作業 → 自動化完成

---

## 1. 背景介紹

### 1.1 Claude for Life Sciences

Anthropic 於 2025 年 10 月推出 Claude for Life Sciences，這是一套專為科學研究設計的連接器與技能套件。最新的 Opus 4.5 模型在以下領域展現顯著進步：

- Figure interpretation（圖表解讀）
- Computational biology（計算生物學）
- Protein understanding benchmarks（蛋白質理解基準測試）

### 1.2 AI for Science Program

Anthropic 透過 AI for Science program 提供免費 API credits 給全球從事高影響力科學研究的學者。這些研究團隊開發的系統已超越傳統的文獻回顧或程式輔助功能。

**Claude 作為研究協作者的三大角色**：

1. **實驗規劃**：協助判斷應執行哪些實驗，提高成本效益
2. **時間壓縮**：將原本需要數月的專案壓縮至數小時內完成
3. **模式識別**：在大規模數據集中發現人類可能遺漏的 patterns

---

## 2. 案例一：Biomni（Stanford University）

### 2.1 系統概述

Biomni 是由 Stanford University 開發的通用型生物醫學 AI agent 平台，整合數百種工具、軟體套件與資料庫於單一系統中。

| 特性 | 說明 |
|------|------|
| 核心架構 | Claude-powered agent 可在系統中自動導航 |
| 輸入方式 | 研究者以 plain English 提出需求 |
| 自動化功能 | 自動選擇適當資源、形成假說、設計實驗 protocol、執行分析 |
| 覆蓋範圍 | 超過 25 個生物學子領域 |

### 2.2 GWAS 分析案例

Genome-wide association study (GWAS) 是尋找與特定性狀或疾病相關之遺傳變異的研究方法。傳統 GWAS 分析流程繁瑣：

- Genomic data 格式混亂，需大量 data cleaning
- 需控制 confounding factors 並處理 missing data
- 識別 hits 後需進一步確認相關基因、細胞類型、生物途徑
- 每個步驟涉及不同工具與檔案格式

> **效率比較**：傳統方法單一 GWAS 分析需時數月，Biomni 僅需 20 分鐘完成。

### 2.3 驗證案例

Biomni 團隊透過多項案例驗證系統準確性：

| 案例類型 | 任務內容 | 結果 |
|----------|----------|------|
| Molecular cloning experiment | 設計 cloning protocol | Blind evaluation 顯示品質與 5 年經驗 postdoc 相當 |
| Wearable data analysis | 分析 30 人、450 檔案（glucose monitoring、體溫、活動量） | 35 分鐘完成（人工估計需 3 週） |
| Single-cell RNA analysis | 分析 336,000 個 human embryonic cells | 確認已知 regulatory relationships 並發現新的 transcription factors |

### 2.4 Expert Skill Encoding

當 Biomni 的預設方法不足以應對特定領域時，專家可將其方法論編碼為 skill：

- 與 Undiagnosed Diseases Network 合作診斷罕見疾病時
- 發現 Claude 的預設診斷方法與臨床醫師差異甚大
- 透過訪談專家、記錄診斷流程、教導 Claude
- 導入 tacit knowledge 後，agent 表現大幅改善

---

## 3. 案例二：Cheeseman Lab（MIT/Whitehead Institute）

### 3.1 研究背景

Iain Cheeseman 實驗室運用 CRISPR 技術進行大規模 gene knockout 實驗：

- 在數千萬個人類細胞中 knockout 數千個不同基因
- 拍攝每個細胞觀察變化
- 功能相似的基因被 knockout 後會產生相似的表型
- 實驗室開發了名為 Brieflow 的 pipeline 自動分群基因

### 3.2 瓶頸：數據解讀

雖然基因分群可自動化，但解讀這些分群的生物學意義仍需人工：

- 需逐一查閱科學文獻確認基因功能
- 單一 screen 可產生數百個 clusters
- 大多數 clusters 因人力不足而從未被深入研究
- Dr. Cheeseman 雖能記住約 5,000 個基因功能，分析仍需數百小時

### 3.3 MozzareLLM 系統

PhD student Matteo Di Bernardo 與 Cheeseman 合作，將其專家方法編碼為 Claude-powered 系統 MozzareLLM：

| 功能 | 說明 |
|------|------|
| 生物程序識別 | 辨識基因 cluster 可能共享的 biological process |
| 基因分類 | 標記哪些基因已被充分研究、哪些研究較少 |
| 優先排序 | 建議哪些基因值得進一步研究 |
| 信心程度評估 | 提供 confidence levels 協助決定是否投入更多資源 |

> **Cheeseman 的評價**："Every time I go through I'm like, I didn't notice that one! And in each case, these are discoveries that we can understand and verify." — 每次審視結果時，我都會發現：「這個我沒注意到！」而且每一個案例都是我們能理解並驗證的發現。

### 3.4 模型比較

Di Bernardo 測試了多個 AI 模型，Claude 表現最佳：

- 在某案例中，Claude 正確識別出一條 RNA modification pathway
- 其他模型將此訊號誤判為 random noise

### 3.5 未來願景

團隊計畫將 Claude-annotated datasets 公開，讓其他領域專家能追蹤他們無暇研究的 clusters：

- Mitochondrial biologist 可深入研究 mitochondrial clusters
- 其他實驗室可採用 MozzareLLM 分析自己的 CRISPR 實驗
- 有望加速多年來功能未被釐清之基因的研究

---

## 4. 案例三：Lundberg Lab（Stanford University）

### 4.1 不同的瓶頸

與 Cheeseman Lab 不同，Lundberg Lab 的瓶頸在研究流程更早期：

| 比較項目 | Cheeseman Lab | Lundberg Lab |
|----------|---------------|--------------|
| 實驗類型 | Optical pooled screening | Focused screens |
| 規模 | 同時 knockout 數千基因 | 針對性選擇數百基因 |
| 主要瓶頸 | 數據解讀 | 決定研究哪些基因 |
| 成本考量 | 可大規模篩選 | 單一 screen 成本 >$20,000 |

### 4.2 傳統基因選擇方法

傳統方法依賴人工判斷：

- 研究生與 postdocs 圍著 Google spreadsheet 討論
- 逐一加入候選基因並附上簡短理由或文獻連結
- 受限於文獻記載內容與研究者記憶
- 本質上是 educated guessing game

### 4.3 AI 驅動的新方法

Lundberg Lab 運用 Claude 翻轉傳統思維：

- **傳統問題**：「根據已發表的研究，我們能做出什麼猜測？」
- **新問題**：「根據分子特性，應該研究什麼？」

### 4.4 分子關係圖譜

團隊建立了細胞內所有已知分子的關係圖譜：

- 涵蓋 proteins、RNA、DNA
- 記錄哪些蛋白質會結合
- 記錄哪些基因編碼哪些產物
- 記錄哪些分子結構相似

Claude 可在此圖譜中導航，根據 biological properties 和 relationships 識別候選基因。

### 4.5 驗證實驗設計

為驗證此方法，團隊選擇研究 primary cilia（初級纖毛）：

- 細胞上的天線狀突起，功能了解有限
- 與多種 developmental 和 neurological disorders 相關
- 選擇此主題因為研究較少，Claude 不太可能已「知道」答案

**驗證流程**：

1. 人類專家使用傳統 spreadsheet 方法預測基因
2. Claude 使用分子關係圖譜生成預測
3. 執行 whole genome screen 建立 ground truth
4. 比較兩種方法的準確率

> 若成功，此方法可望成為 focused perturbation screening 的標準第一步。

---

## 5. 總結與展望

### 5.1 關鍵洞察

1. **能力持續進化**：每次模型更新都帶來顯著改進。兩年前 AI 僅能撰寫程式碼或摘要文獻，現在已能複製論文所描述的實際研究工作。
2. **消除瓶頸**：AI 正在消除需要深度知識且過去無法規模化的任務瓶頸。
3. **啟用新方法**：AI 使研究者能採用過去不可能實現的研究方法。

### 5.2 系統特性比較

| 特性 | Biomni | MozzareLLM | Lundberg System |
|------|--------|------------|-----------------|
| 機構 | Stanford | MIT/Whitehead | Stanford |
| 定位 | 通用型 | 專用型 | 專用型 |
| 解決瓶頸 | 工具碎片化 | CRISPR 數據解讀 | 基因選擇 |
| 核心功能 | 整合數百種工具與資料庫 | 自動化基因 cluster 解讀 | AI 驅動假說生成 |

> **結語**：這些系統都尚未完美，但它們展示了科學家如何在短短數年內將 AI 從基礎工具轉變為能加速甚至取代許多研究流程的協作夥伴，並指向新穎的科學洞見與發現。

---

## 參考文獻

1. Anthropic. How scientists are using Claude to accelerate research and discovery. [*Anthropic Blog*. 2026-01-16.](https://www.anthropic.com/research/claude-for-science)
2. Anthropic. Claude for Life Sciences. [*Anthropic Solutions*.](https://www.anthropic.com/solutions/life-sciences)
3. Anthropic. AI for Science Program. [*Anthropic Programs*.](https://www.anthropic.com/programs/ai-for-science)

---

## 縮寫對照表

| 縮寫 | 全名 |
|------|------|
| AI | Artificial Intelligence（人工智慧） |
| API | Application Programming Interface（應用程式介面） |
| CRISPR | Clustered Regularly Interspaced Short Palindromic Repeats |
| GWAS | Genome-Wide Association Study（全基因組關聯研究） |
| LLM | Large Language Model（大型語言模型） |
| RNA | Ribonucleic Acid（核糖核酸） |
| DNA | Deoxyribonucleic Acid（去氧核糖核酸） |
