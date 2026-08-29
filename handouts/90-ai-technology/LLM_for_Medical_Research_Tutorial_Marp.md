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
  section.lead h1 { color: #ffffff; font-size: 2.0em; border-bottom: none; }
  section.lead h2 { color: #b0c4de; }
  section.lead h3 { color: #dfe6e9; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #8ab4f8; }
  section.lead blockquote {
    background-color: #f5f6fa;
    color: #2d3436;
    border-left: 4px solid #ba181b;
  }
  section.lead blockquote strong { color: #ba181b; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: white;
    border-bottom: none;
    font-size: 2.4em;
    text-align: center;
  }
  section.divider h2 { color: #ffe066; text-align: center; }
  section.divider h3 { color: #ffffff; text-align: center; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.55em; }
  h2 { color: #0072bc; font-size: 1.1em; }
  h3 { color: #555555; }
  table { font-size: 0.66em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.85em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 0.6em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.8em; }
  section.mid-text { font-size: 0.9em; }
  section.ref { font-size: 0.66em; }
footer: '謝慕揚 MD, PhD, FESC | 醫學研究使用 LLM 的實務指引 (Nat Protoc 2026) | 2026'
---

<!-- _class: lead -->

# 醫學研究使用大型語言模型的實務指引

## Tutorial: Guidance on the Use of Large Language Models for Medical Research

### Jin Q, et al. *Nat Protoc.* 2026 — NIH / National Library of Medicine

**謝慕揚 MD, PhD, FESC** | 2026-08-29

[原文連結 — https://doi.org/10.1038/s41596-026-01408-z](https://doi.org/10.1038/s41596-026-01408-z)

> **作者群主體來自維護 PubMed 的 NLM，不含模型廠商，聲明無利益衝突**

---

# 一句話總結

> **這是 NIH／NLM 寫給臨床與研究人員的「LLM 落地作業指引」，不是綜述、也不是評論。**

核心主張很直白：

**現在大多數人使用 LLM 的方式 — 打開 ChatGPT 隨手問一問 (ad hoc prompting) — 對醫療任務而言遠遠不夠。**

這種落差會同時造成 **低度利用 (underutilization)** 與 **誤用 (misapplication)**。

**解方**：一條有紀律的流水線 + 10 條最佳實務

---

# 對臨床端最關鍵的三條

> **1. 先收集約 100 個測試案例再開始**
> 沒有測試集就沒有品質可言

> **2. 不要把可識別的病人資料放進非 HIPAA 合規的服務**
> 透過 API 的專有模型**通常不符合 HIPAA**

> **3. 不要用選擇題成績挑模型**
> MCQ 表現與真實臨床效用**不相關**

---

# 為什麼這篇值得讀

1. **來源權威且中立**
   NLM（PubMed）＋ Columbia、Yale、UIUC、UVA、Weill Cornell、FSU、NIH Clinical Center
   **沒有模型廠商**；聲明無利益衝突

2. **把「怎麼做」寫成可執行步驟**
   附公開教學程式碼 repo：`ncbi-nlp/LLM-Medicine-Primer`

3. **明確指出醫界最常見的兩個錯誤**
   用 web app 處理病人資料、用考試分數挑模型 — 這兩點天天發生

> **一句話**：把這篇當成 LLM 版的 CONSORT／STROBE —
> **它規範的不是結果，而是流程的可信度。**

---

<!-- _class: divider -->

# 整體框架

## 五個階段

---

# 五階段流水線

```text
1. 任務形成 Task formulation
   抽象需求 → 具體任務；辨識屬於五大能力的哪一種
   ★ 收集約 100 個測試案例 (input + output)
                    ↓
2. 模型選擇 LLM selection
   三個考量：任務與資料 / 效能要求 / 存取介面
   硬限制：資料型態 (modality)、context window
                    ↓
3. 提示工程 Prompt engineering
   FSL → CoT → RAG → Tool learning；temperature = 0
                    ↓
4. 微調 Fine-tuning（只有三種情況才需要）
   全量微調 vs PEFT / LoRA
                    ↓
5. 部署 Deployment
   法規遵循 / 系統穩健性(公平性) / 成本 / 上線後監測
```

> **關鍵順序**：提示工程**排在微調前面** — 多數醫療任務**不需要微調**

---

<!-- _class: divider -->

# 階段一

## 任務形成 Task Formulation

---

# 先問：這件事屬於 LLM 的哪一種能力？

| 能力 | 醫療應用範例 | 評估方式 |
|------|-------------|---------|
| **知識與推理** | 醫學問答、臨床決策支援、**病人與試驗配對** | 先比對短答案，滿意後再看解釋 |
| **摘要** | 長病歷→出院病摘；文獻→系統性回顧 | BLEU / ROUGE / BERTScore ⚠️ |
| **轉譯** | 跨語言、醫學教育、**醫病溝通**（換語氣寫給不同對象） | 同摘要 |
| **結構化** | 自由文字→結構化欄位；DRG 分類；概念關係抽取 | **precision / recall / F1** |
| **多模態** | 放射報告生成；整合 EHR 病史 + 當次影像 | 同推理 |

> 💡 **Translation 不只是中英翻譯** — 也包括**寫作風格轉換**
> （把技術性說明改寫成病人聽得懂的話）→ 這是衛教最實際的用途

---

# ⚠️ 一個反直覺的重點

> **在「結構化」這類較簡單的任務上，
> LLM 常常打不贏經過微調的 BERT 類模型。**

**LLM 的主場是需要醫學知識與臨床推理的任務，不是所有 NLP 任務。**

---

# 最重要的一步：先建測試集

> **Best practice 1：收集約 100 個測試實例，每個都要有 input 與 output。**

依據數個 LLM 醫學評估研究的經驗，建議 **~100 個實例**，要求**多樣 (diverse)**

**為什麼這是整條流水線的地基？**

- 沒有測試集，**無法比較兩個 prompt 誰比較好**
- 沒有測試集，**無法知道換模型之後有沒有變差**
- 沒有測試集，**無法在部署後偵測退化**

> 🔑 **這是本文對臨床端最重要、也最常被跳過的一條。**
> 大多數人的做法是「試幾個例子看起來不錯就上線」—
> **那不是評估，那是印象。**

---

<!-- _class: divider -->

# 階段二

## 模型選擇 LLM Selection

---

# 隱私與法規 — 臨床端的第一道關卡

> ⚠️ **作者的明確陳述**
>
> 透過 API 存取的專有模型（如 OpenAI 的 GPT-5）**通常不符合 HIPAA**，
> **因此不應用於病人資料**。
>
> **Azure** 與 **Anthropic** 提供**符合 HIPAA 的 LLM 存取**。
> **或者**使用**本地端模型**（Llama、Mistral）以獲得更強的隱私控制。

| 做法 | 評價 |
|------|------|
| 醫院在**安全本地伺服器**用**完全去識別化**病歷微調，限授權內部人員 | ✅ 朝向合規 |
| 把**可識別的病歷**上傳到**公開 LLM API** | ❌ 很可能違法，**尤其當該 API 會用輸入去訓練模型** |

**準則**：使用前**先讀完供應商使用者條款**

---

# 資料模態 (Modality) — 硬限制

| 資料型態 | 需求 |
|---------|------|
| 放射／病理 2D 或 3D 影像 | 需要**超越純文字**的模型（o3-mini、Llama 3 不行） |
| 醫療對話（音訊） | 可先轉錄成文字，再用文字模型 |
| 基因體（DNA 序列、RNA 表現） | 需要 omics 判讀知識 |
| 時序（生命徵象監測） | 需能分析結構化 EHR 的長時間模式 |

> ⚠️ 基因體與時序資料**雖可表示成純文字**，但
> **一般 LLM 能否在不經額外訓練下有效處理，仍不清楚**

> **Best practice 3：確認任務必需的模態，選擇支援該模態的 LLM**

---

# Context Window — 另一個硬限制

```text
1 個 token ≈ 0.8 個英文字
一篇 PubMed title + abstract ≈ 250 字 ≈ 300–400 tokens
```

| 模型 | Context window | 約可容納摘要數 |
|------|---------------|--------------|
| Llama 3.0 | 8,000 tokens | ~20 篇 |
| Claude 4.5 Opus | 200k tokens | ~800 篇 |
| GPT-5 | 400k tokens | ~1,600 篇 |
| Gemini 3.0 | 1M tokens | ~2,500 篇 |

> ⚠️ **長 context 不是萬靈丹**：作者點名 **lost-in-the-middle** —
> **模型會用不到放在提示中間的資訊**，這問題**在長 context 模型上同樣存在**
>
> **實務啟示：重要的東西放頭尾，不要埋在中間。**

---

# 效能評估：兩種路線

| | 自動評估 | 臨床評估 |
|---|---|---|
| 方法 | MedQA-USMLE、PubMedQA、MedMCQA 等**選擇題** | 真實情境測試，如 **RCT** |
| 優點 | 可規模化、可作為起點 | **黃金標準**，與病人照護相關 |
| 缺點 | ⚠️ **分數高不等於臨床效用好** | 耗費大量人力，常拿不到 |

> ⚠️ **本文最重要的警告之一**
>
> **在多選題 benchmark 上分數更高，不必然轉換為更好的臨床效用。**
> 因為真實應用中**根本沒有選項可選**；多項研究顯示
> **MCQ 表現與真實任務效用不相關**。
>
> 較有前景的方向：**HealthBench**（評分表）、**Chatbot Arena**（偏好）

**Best practice 4**：優先依臨床評估選模型；拿不到才用自動評估**篩選**候選

---

# 存取介面：三選一

| 介面 | 優點 | 缺點 |
|------|------|------|
| **Web 應用**（ChatGPT） | 便宜、易用 | ❌ 無法控制模型行為、無法規模化評估；**多數不具明確 HIPAA 合規**；**通常連 temperature 都設不了** |
| **模型 API** | 比自架容易；**部分提供 HIPAA 合規**；可控參數 | 專有模型客製化受限 |
| **本地部署** | **最大控制權與隱私**；可取得**下一個 token 的原始機率分布** | 硬體與技術門檻高 |

> ⚠️ **作者明確不建議在開發階段使用 web 應用**

**總結權衡**：尖端專有 LLM 一般任務表現較好，但**客製化、隱私、安全掌控較少**；
開源 LLM 客製化與安全性較佳，但**開發與部署兩端門檻都更高**

---

<!-- _class: divider -->

# 階段三

## 提示工程 Prompt Engineering

---

# 核心方法論

**定義**：設計與最佳化提示，以有效引導 LLM 產生準確、連貫回應的過程

**核心觀念**：**不修改模型參數**就能引導多樣行為；任務越複雜，提示越需精緻

**自動化**：可用 **DSPy**、**TextGrad** 讓 LLM 依效能回饋自動調整提示

> 🔑 **作者給的方法論主軸**
>
> **先分析錯誤 (error analysis)，再依錯誤型態選技術。**
>
> 例：錯誤肇因於**缺乏醫學知識** → 用 **RAG** 把相關資訊餵給模型

---

<!-- _class: small-text -->

# 四項核心技術（1／2）

**① FSL — Few-Shot Learning**
- 提示中放入**少數範例**，每個都要**同時含輸入與期望輸出**
- 範例應**有代表性且多樣**；分類任務應**展示所有可能標籤**
- 進階：依待預測實例的**語意相似度動態生成範例**
- **Best practice 5：從 zero-shot 開始**，逐步加範例以提升效能或處理邊緣案例

**② CoT — Chain-of-Thought**
- 最簡單做法：輸入末尾加上 **"Let's think step-by-step"**
- 在複雜醫療決策中特別有用：**推理說明可提升效能，也幫助醫師理解與驗證**
- **Best practice 6：把 CoT 當成預設值**

> 💡 一個只給答案的 AI **無法被查核**；給出推理的 AI 才可能被醫師**驗證與否決**
> 這是**安全性議題**，不只是效能議題

---

# 四項核心技術（2／2）

**③ RAG — Retrieval-Augmented Generation**

解決兩個醫療上特別危險的問題：

| 問題 | 說明 |
|------|------|
| **幻覺 (hallucination)** | 生成不正確的內容**或不存在的參考文獻** |
| **知識過期** | 參數中的知識停留在訓練時點 |

- 建議語料：**系統性回顧、醫學教科書、臨床指引**
- 常用資源：**PubMed**（>3,900 萬篇摘要）、**PubMed Central**（>700 萬篇開放全文）

**④ Tool learning（function calling）**
- 資料庫工具、**醫學計算機**；例：給 LLM「讀取原始 EHR」的工具

> 💡 與其要求 LLM「心算」CHA₂DS₂-VASc 或 eGFR，**不如給它一個計算器工具**
> **演算法該交給演算法。**

---

# Temperature 與輸出格式

> **Best practice 8**
>
> **temperature 從 0 開始** — 取得**確定性結果以確保可重現性**
> 只有需要多樣回應（如 ensembling）時才調高
>
> **指示 LLM 產生結構化輸出，例如 JSON 字典** —
> 主要考量是**自動解析回應的難易度**

⚠️ Temperature 通常**可透過 API 或本地端設定，但 web app 通常不行**

→ 這是**不建議用 web app 做開發的另一個具體理由**

---

# 提示工程的其他細節

**多模態資料轉成文字提示**

- 單細胞 RNA 定序可轉成含**基因標記與表現量**的文字提示
- 生物感測器訊號可轉成文字，生成**個人健康洞察與運動建議**

**早期迭代階段可探索的經驗性調整**

- 聚焦的範例 (focused examples)
- **上下文擺放與包裝的位置**
- 多樣本 (multishot) 範例的組織方式

> 這些屬於原文所稱「較為經驗性 (anecdotal) 的提示微調」，
> 特別適用於**早期迭代開發階段**。

---

<!-- _class: divider -->

# 階段四

## 微調 Fine-Tuning

---

# 什麼時候才需要微調？

> **只有三種情況才考慮 (Best practice 9)**
>
> 1. **提示工程技術（FSL、RAG）已無法充分改善結果**
> 2. **有大規模、現成的高品質訓練資料**
> 3. **可用的提示長到成本上不可行**

> 🔑 **反過來說：這三條都不成立，就不要微調。**
> 這是本文對想「訓練自己的醫療 AI」的團隊最務實的提醒。

---

# 全量微調 vs PEFT

| | Full fine-tuning | **PEFT（如 LoRA）** |
|---|---|---|
| 更新範圍 | **全部參數** | **遠少於全模型的參數** |
| 適合資料 | **較大、較多樣** | **較小、較專一**（避免 overfitting） |
| 硬體需求 | 高 | **大幅降低** |
| 效能 | — | **常與全量相當，低資料量時甚至更好** |

**具體案例**：用 **quantized LoRA (QLoRA)** 微調 LLM 做臨床文本摘要，
**僅用數千筆訓練實例 + 一張 NVIDIA Quadro RTX 8000 GPU** 即達成有效結果

⚠️ **與提示工程一樣，微調後模型必須在「獨立測試集」上評估**，驗證確實提升

---

<!-- _class: divider -->

# 階段五

## 部署 Deployment

---

# 法規遵循

- 須遵守 **HIPAA** 與 **GDPR**
- 使用專有 LLM 時**必須確認平台符合 HIPAA**
- 作者具體點名：
  - **OpenAI API 目前不符合 HIPAA**
  - **Azure** 提供符合 HIPAA 的 OpenAI 模型存取
  - **Anthropic** 為 Claude 模型提供 **HIPAA 認證的 API 託管**

> ⚠️ **LLM 這類 AI 演算法有可能被視為醫療器材而受管制** —
> 尤其在**臨床場域使用或用於決策支援**時，
> 需符合 **FDA** 或其他主管機關對**醫材軟體**的規範

**Best practice 10**：謹慎選擇符合法規與臨床標準的協定，並**持續監測**

---

# 系統穩健性與公平性

> ⚠️ **作者的明確警告**
>
> **即使是最成功的專有模型也可能展現種族偏誤。**
>
> 研究顯示，當提供**僅在種族上不同、其餘完全相同的病人描述**時，
> **LLM 可能對治療、費用或預後給出不同的預測**。
>
> 這種差異**在正式運作時會造成醫療不平等 (healthcare disparities)**。

**因此**：部署前**必須評估模型公平性**

若無法檢視資料或演算法（許多專有模型即是如此），
仍可**使用既有 benchmark 資料集評估**，了解是否存在偏誤及其程度

---

# 成本

**專有模型**（作者實例，截至 2025 年 12 月）

```text
Google Gemini 3.0
  input  : US$2  / 1M tokens（提示 < 200k tokens 時）
  output : US$12 / 1M tokens

實例：處理 1,000 份典型 MIMIC-III 出院病摘
      ≈ 400 萬 tokens ≈ US$8（僅計提示 token；輸出另計）
```

**開源模型**：前期硬體（GPU）＋ 持續維運

| 模型規模 | 硬體需求 |
|---------|---------|
| **7–8B** 參數 instruction-tuned | 常可用**單張高記憶體 GPU**（如 A100 40GB）；**容忍延遲甚至可用 CPU** |
| **70B** 參數 | 通常需**多 GPU 或 tensor-parallel serving** |

**節省技巧**：新模型（如 Qwen3）提供 **FP8 變體**，**GPU 記憶體用量約減半**（vs FP16）

---

# 上線後 (Post-deployment)

**持續監測是必要的。作者強調四件事：**

1. **定位** — 確保 LLM 輸出被**負責任地當作輔助工具，而非取代醫療專業人員的判斷**
2. **訓練** — 協助醫療人員理解**如何解讀與運用輸出、並管理潛在風險**
3. **社群參與** — 透過**社群諮詢委員會**與**病人小組**收集回饋，貼近真實世界多樣性
4. **模型生命週期管理** ⚠️
   **模型的淘汰或替換，可能需要重新實作提示、重新驗證效能、重新認證安全與合規**

> 🔑 **第 4 點最容易被忽略**：你依賴的模型版本**會被下架**。
>
> 要問的不是「這個 prompt 現在好不好用」，
> 而是「**換模型的那一天，我們要花多久重跑驗證？**」
>
> → 這就是為什麼 **Best practice 1（先建 100 個測試案例）是整條流水線的地基**

---

<!-- _class: divider -->

# 評估

## 為什麼「考試考很高」不等於「好用」

---

# 論證結構

```text
常見的推論（錯誤）
  「這個模型 USMLE 考 90 分 → 它可以看門診」

作者的反駁
  ① 真實臨床「沒有選項可選」
     MCQ 提供 5 個選項，其中必有 1 個正確
     真實情境是開放式的，且可能沒有正確答案
  ② 多項研究顯示 MCQ 表現與真實任務效用「不相關」

正確的做法
  自動評估 → 只用來「篩選」候選模型（可規模化、便宜）
       ↓
  臨床評估 → 才是黃金標準（如 RCT），但耗費人力
       ↓
  開放式評估是有前景的中間路線
     · HealthBench（以評分表 rubric 為基礎）
     · Chatbot Arena（以偏好 preference 為基礎）
```

> 💡 **對醫學教育的延伸**：這和「**筆試成績能不能預測臨床表現**」是同一個問題。
> 作者的立場等同 Miller 金字塔 — **knows ≠ knows how ≠ shows how ≠ does**。
> **用 MCQ 挑 LLM，就像用筆試挑住院醫師。**

---

<!-- _class: divider -->

# 十條最佳實務

---

<!-- _class: small-text -->

# 最佳實務彙整

| # | 最佳實務 | 階段 |
|---|---------|------|
| **1** | 收集約 **100 個測試實例**（含 input 與 output） | 任務形成 |
| **3** | 確認必需的**資料模態**，選擇支援該模態且 **context window 足夠**的 LLM | 模型選擇 |
| **4** | 優先依**臨床評估**選模型；無法取得時才以**自動評估**篩選候選 | 模型選擇 |
| **5** | 從 **zero-shot 開始**，逐步加範例以提升效能或處理邊緣案例 | 提示工程 |
| **6** | 把 **CoT 當作預設**，提升可解釋性與效能 | 提示工程 |
| **7** | 善用 **RAG** 與**工具呼叫 (function calling)** | 提示工程 |
| **8** | **temperature 從 0 開始**；輸出**結構化格式（如 JSON）** | 提示工程 |
| **9** | 只在**三種情況**下才微調 | 微調 |
| **10** | 選擇符合**法規與臨床標準**的協定，並**持續監測**（公平性、偏誤、生命週期） | 部署 |

> 註：原文 Box 2 共列 10 條；第 2 條於內文未被直接引用，完整內容請參閱原文 Box 2。

---

<!-- _class: divider -->

# 接到我們自己的工作流

---

<!-- _class: small-text -->

# 實務對照表

> ⚠️ 本頁為**講義整理者的延伸應用建議**，非原文內容

| 我們的既有工作 | 對應段落 | 具體做法 |
|--------------|---------|---------|
| 每週期刊文獻回顧 | **Summarization + RAG** | 用 PubMed／PMC 當檢索語料；要求 **JSON 結構化輸出**（title / journal / DOI / 結論方向）以便自動核對 |
| 「不要根據 abstract 猜結論」的紀律 | **幻覺與知識過期** | 這正是 RAG 存在的理由；但 RAG **不保證正確** — 交叉查證不可省 |
| 衛教單張、醫病溝通改寫 | **Translation**（風格轉換） | 明確指定對象（病人／家屬／住院醫師）與閱讀程度 |
| 病歷結構化、資料擷取 | **Structurization** | ⚠️ 注意：這類任務**微調過的 BERT 可能更好也更便宜** |
| 任何碰到病人資料的事 | **法規遵循** | ❌ 不要放進未聲明合規／未經院方核可的服務 |
| 想評估「這個 AI 好不好用」 | **BP 1 + 評估章節** | 先建 ~100 題自己的測試集；**不要用它考 USMLE 來決定** |

---

<!-- _class: mid-text -->

# 限制與該注意的地方

1. **這是 Tutorial，不是系統性回顧或實證指引**
   提供的是**專家共識性質的操作框架**；「~100 個測試實例」是**經驗法則**，非檢定過的閾值

2. **技術細節會快速過期**
   模型名稱、context window、價格（明確標註 "as of December 2025"）都會變
   → **框架會存活，數字不會**

3. **合規陳述有時效與地域性**

4. **沒有提供醫療機構層級的治理範本**（採購、稽核、事故通報）

5. **公平性章節指出問題，但未給出可操作的檢測流程**

> ⚠️ **給台灣讀者**：文中所有 HIPAA 建議，應轉譯為
> 「**符合個資法、通過院內資安與 IRB 審查的路徑**」。
> **不要因為某服務標示 HIPAA 合規，就認定在台灣可直接用於病人資料。**

---

<!-- _class: divider -->

# Take Home

---

<!-- _class: small-text -->

# Take Home（1／3）

> **Pearl 1**：這是 **NIH／NLM（PubMed 的維護者）** 寫的操作指引，作者群**不含模型廠商**、聲明無利益衝突。定位是**方法論工具書**，不是綜述。

> **Pearl 2**：框架五階段 — **任務形成 → 模型選擇 → 提示工程 → 微調 → 部署**。注意**提示工程排在微調之前**：多數醫療任務**不需要微調**。

> **Pearl 3（最常被跳過）**：**先收集約 100 個測試實例再開始。** 沒有測試集就無法比較 prompt、無法察覺換模型後的退化、無法在上線後偵測劣化。

> **Pearl 4（臨床紅線）**：**透過 API 的專有模型通常不符合 HIPAA，不應用於病人資料。** Azure 與 Anthropic 提供 HIPAA 合規存取；或改用本地模型。**把可識別病歷丟進公開 API 很可能違法**，尤其當該 API 會用輸入去訓練模型時。

---

<!-- _class: small-text -->

# Take Home（2／3）

> **Pearl 5（挑模型的紅線）**：**不要用 MCQ 成績挑模型。** 真實情境沒有選項可選；多項研究顯示 MCQ 表現**與真實任務效用不相關**。自動評估只能用來**篩選**，臨床評估才是黃金標準。

> **Pearl 6（四件武器）**：**FSL**（從 zero-shot 開始加）、**CoT**（設為預設，因為可被醫師驗證）、**RAG**（對抗幻覺與知識過期，用系統性回顧／教科書／指引當語料）、**Tool learning**（計算交給計算器）。**temperature = 0** 以求可重現。**輸出 JSON** 以便解析。

> **Pearl 7**：**Web app 不適合開發** — 無法控制參數（連 temperature 都設不了）、無法規模化評估、多數不具明確 HIPAA 合規。

> **Pearl 8**：**LLM 不是所有 NLP 任務的答案。** 在**結構化**這類簡單任務上，**微調過的 BERT 常常更好**。LLM 的主場是**需要醫學知識與臨床推理**的任務。

---

<!-- _class: small-text -->

# Take Home（3／3）

> **Pearl 9（公平性）**：**僅改變種族、其餘完全相同的病人描述，LLM 可能給出不同的治療、費用或預後預測。** 部署前必須評估公平性。

> **Pearl 10（生命週期）**：**你依賴的模型會被下架。** 淘汰或替換需要**重新實作提示、重新驗證效能、重新認證合規** — 這正是 Pearl 3 的測試集真正發揮價值的時刻。

> **Pearl 11（台灣在地化）**：所有 HIPAA 建議須轉譯為**個資法 + 院內資安 + IRB** 的路徑。
> **HIPAA 合規 ≠ 台灣可用。**

---

<!-- _class: ref -->

# 參考文獻

1. Jin Q, Wan N, Leaman R, Tian S, Wang Z, Yang Y, Wang Z, Xiong G, Lai P-T, Zhu Q, Hou B, Sarfo-Gyamfi M, Zhang G, Gilson A, Bhasuran B, He Z, Zhang A, Sun J, Weng C, Summers RM, Chen Q, Peng Y, Lu Z. Tutorial: guidance on the use of large language models for medical research. [*Nat Protoc*. 2026.](https://doi.org/10.1038/s41596-026-01408-z) PMID: [42498804](https://pubmed.ncbi.nlm.nih.gov/42498804/) · PMC13454964

2. 教學程式碼（NCBI／NLM 官方 repository）：[ncbi-nlp/LLM-Medicine-Primer](https://github.com/ncbi-nlp/LLM-Medicine-Primer)

3. PubMed 檢索入口：<https://pubmed.ncbi.nlm.nih.gov/>（超過 3,900 萬篇摘要）

4. PubMed Central：<https://www.ncbi.nlm.nih.gov/pmc/>（超過 700 萬篇開放取用全文）

> 原文內文引用之次級文獻（GPT-5、Claude 4.5、Gemini 3、Llama 4、DeepSeek-R1、MedQA-USMLE、PubMedQA、MedMCQA、HealthBench、Chatbot Arena、DSPy、TextGrad、LoRA、MIMIC-III 等）請逕參閱原文 References 章節。
>
> 文獻資訊經 **PubMed** 查證取得。

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

> 本內容為讀書會共筆整理，僅供醫療專業人員教學參考。
> 文中 HIPAA／GDPR／FDA 相關陳述為原文對美國與歐盟情境之描述，
> **在台灣應依個資法、院內資安規範與 IRB 審查辦理，不可直接套用。**
