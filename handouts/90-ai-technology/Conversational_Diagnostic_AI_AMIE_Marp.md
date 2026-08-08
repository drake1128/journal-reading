---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: 'Microsoft JhengHei', 'PingFang TC', sans-serif; background-color: #ffffff; color: #2d3436; }
  section.lead { background-color: #1a2740; color: #ffffff; }
  section.lead h1 { color: #ffffff; font-size: 2.2em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.divider { background-color: #0072bc; color: white; display: flex; justify-content: center; align-items: center; }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.5em; text-align: center; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.72em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote { border-left: 4px solid #ba181b; background-color: #fff5f5; padding: 0.5em 1em; font-size: 0.88em; }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.68em; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
footer: '謝慕揚 MD, PhD, FESC | 對話式診斷 AI (AMIE) | 2026'
---

<!-- _class: lead -->
# 邁向對話式診斷人工智慧
## Towards Conversational Diagnostic AI — AMIE (Nature 2025)

**謝慕揚 MD, PhD, FESC** | 2026-08-02

[Nature 2025 — Towards conversational diagnostic artificial intelligence (doi:10.1038/s41586-025-08866-7)](https://doi.org/10.1038/s41586-025-08866-7)

---

# 臨床背景：為何要對話式診斷 AI

- 醫病對話是有效且富同理心照護的核心；醫療會談 (medical interview) 被稱為醫師「最強大的工具」。
- 某些情境下，**60–80% 的診斷單靠病史詢問 (history-taking alone)** 即可完成。
- 良好問診人力**全球稀缺、僅能間歇取得**。

> 大型語言模型 (large language model, LLM) 已能規劃、推理並維持自然對話 → 有機會發展能**在不確定性下主動蒐集資訊、進行具診斷價值對話**的醫療 AI，改善可近性、品質與健康公平 (health equity)。

---

# AMIE 是什麼

**AMIE = Articulate Medical Intelligence Explorer**（Google Research / Google DeepMind）

- 專為**診斷對話 (diagnostic dialogue)** 最佳化的 LLM-based AI 系統。
- 基礎模型建於 **PaLM 2**，再經 instruction fine-tuning。
- 訓練混合：醫學推理、醫學問答、長文問答、電子病歷 (EHR) 摘要 + 真實與模擬對話。
- 核心創新：**self-play 模擬對話 + 自動回饋**（規模化到 5,000+ 疾病）＋ 推論階段 **chain-of-reasoning**。

> 目標非取代醫師，而是探索「主動問診 → 形成鑑別診斷 (DDx) → 同理溝通」整條診斷對話鏈。

---

<!-- _class: divider -->
# 訓練方法：self-play 與 chain-of-reasoning

---

# self-play：inner + outer 雙迴圈

**所有代理都由 AMIE 自己扮演**：vignette generator、patient agent、doctor agent、moderator、critic（知道正解）。

```text
Inner loop：Doctor ⇄ Patient 產生對話
      → Critic（知正解）給 in-context 回饋
      → Doctor 依回饋重做（每次迭代重複 2 次）
Outer loop：精修對話 → 併入下一輪 fine-tuning
      → 新版 AMIE 再回 inner loop（持續學習循環）
```

- 每次迭代產 **11,686 段對話**，源自 **5,230 種疾病**（常見 + 少見）。
- 模擬對話平均約 **21 輪**（刻意模擬文字聊天式聚焦問診）。

---

# 推論階段：chain-of-reasoning（三步驟）

「推理鏈」= 一連串**後步依賴前步輸出**的模型呼叫，每一輪回覆前執行：

| 步驟 | 內容 |
|------|------|
| **1. 分析病人資訊** | 整理正／負向症狀與病史、產生當前 DDx、指出缺漏資訊、評估信心與急迫性 |
| **2. 形成回應與行動** | 生成回覆並追問缺漏；必要時建議立即行動（如急診）；有把握則提出鑑別 |
| **3. 精修回應** | 依事實正確性與格式修訂：避免事實錯誤、避免重複、展現同理、清楚呈現 |

---

<!-- _class: divider -->
# 評估設計與結果

---

# 研究設計摘要

| 項目 | 內容 |
|------|------|
| 設計 | Randomized, double-blind crossover；remote OSCE 風格 |
| 介面 | 線上**同步文字聊天**（非語音、非視訊） |
| 情境數 | **159**（India 75、Canada 70、UK 14）|
| 專科 | 心血管 31、呼吸 32、腸胃 33、神經 32、泌尿／婦產 15、內科 16 |
| 對照 | **20 位全科醫師 (PCP)**，年資 3–25 年（中位 7）|
| 病人 | **20 位 validated patient-actor**（India／Canada 各 10）|
| 評分 | **33 位專科醫師**，每情境 3 人盲化評分（多數決／中位數）|

> OSCE agent = PCP 或 AMIE；兩者皆被要求不得透露身分。每次問診限時 ≤ 20 分鐘。

---

# 主要結果：鑑別診斷準確度 (DDx)

- AMIE 的 **top-k 準確度在所有 k 值 (1–10) 皆顯著高於 PCP**（P < 0.05，FDR 校正）。
- PCP 並非每次列滿 10 診斷（**min = 3、mean = 5.36**）；AMIE 較完整。
- **關鍵**：相同資訊下，AMIE 產生的 DDx 較完整 → **AMIE 蒐集資訊與 PCP 相當，但解讀成 DDx 更佳**。
- 兩者多在**前 10 輪**即取得足以正確鑑別的資訊。

> 非疾病狀態情境僅 10/159；AMIE 趨勢一致但因 n 小未達顯著。

---

# 主要結果：32／26 評分軸

| 評分觀點 | 優於 PCP | 未達顯著的軸（AMIE 仍非劣）|
|----------|:---:|------|
| **專科醫師** | **30 / 32** | 「轉診升級建議適當」、「無虛構 (confabulation) 內容」|
| **病人 (patient-actor)** | **25 / 26** | 「承認錯誤」（適用情境少、排除多）|

- **沒有任何一軸 PCP 顯著優於 AMIE**。
- 評分涵蓋 GMCPQ／PACES／PCCBP：問診結構、診斷處置、同理溝通。

---

# 同理心與 verbosity 的解讀

- patient-actor 與 specialist **一致**認為 AMIE 在**同理心與溝通 (empathy & communication)** 優於 PCP，且這類病人中心軸佔多數維度。
- 但 AMIE 回應**顯著較長、較有結構 (verbose)**。

> **務實提醒**：部分「同理心」優勢**可能源自回應較長、較有結構**，讓評分者感覺花了較多時間準備——不宜直接等同於真正的臨床同理。缺少語音／非語言線索也可能對醫師不利。

---

# 對醫學教育與臨床的意涵

- **問診教學**：chain-of-reasoning「分析→追問→精修」可作為住院醫師／NP 的結構化問診框架。
- **標準化病人 (SP) 模擬**：self-play 的 patient agent／critic 示範**可規模化、可回饋**的問診練習。
- **診斷推理訓練**：AI 於相同資訊下 DDx 更完整 → 教學應強化「從已知資訊推出完整鑑別」。
- **可近性／公平**：願景是把世界級問診品質規模化到資源不足地區。
- **人機互補**：結合醫師對非語言線索的判讀 + LLM 的結構與完整鑑別。

---

# 限制（務必謹慎解讀）

> **1. 介面不符真實臨床**：同步文字聊天對 PCP 不熟悉，**不代表一般（遠距）醫療實務**。

> **2. 模擬病人非真實病人**：無法涵蓋真實背景全貌；AMIE 對**低英語識讀**病人表現明顯下降。

> **3. 情境偏疾病狀態**：僅 10/159 為無疾病，不符基層「多在排除疾病」的現實。

> **4. 公平／偏誤未充分評估；5. 尚非真實部署** — 需不確定性估計、**轉交人類醫師**、合格醫師在環把關。作者：應以**謙遜與謹慎**詮釋。

---

<!-- _class: lead -->
# Take-home messages

**AMIE** 是對話式診斷 AI 的重要**里程碑**，但成果來自**受限模擬情境 + 文字聊天 + 模擬病人**。

- 優勢在「**把資訊解讀成完整 DDx**」，非「問到更多」。
- 30/32、25/26 軸優於 PCP，但**介面對醫師不熟悉**是關鍵前提。
- 「同理心」高分部分可能只是**回應較長較有結構**。
- 對醫學教育：重點是**結構化診斷推理**與**可規模化問診模擬**，不是取代醫師。

---

<!-- _class: small-text -->
# 參考文獻

1. Tu T, Schaekermann M, Palepu A, et al. Towards conversational diagnostic artificial intelligence. *Nature*. 2025;642(8067):442-450.
   https://doi.org/10.1038/s41586-025-08866-7

2. McDuff D, Schaekermann M, Tu T, et al. Towards accurate differential diagnosis with large language models. *Nature*. 2025.
   https://doi.org/10.1038/s41586-025-08869-4

**縮寫**：LLM 大型語言模型；DDx 鑑別診斷；OSCE 客觀結構式臨床測驗；PCP 全科醫師；EHR 電子病歷；SP 標準化病人；NP 專科護理師；FDR 偽發現率；patient-actor 扮演病人的受訓演員。

*本投影片為讀書會共筆整理，僅供教學參考；數據均引自原文。*
