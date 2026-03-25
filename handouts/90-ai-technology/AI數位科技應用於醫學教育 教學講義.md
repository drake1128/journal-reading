# AI and Digital Technology in Medical Education
# AI 數位科技應用於醫學教育之相關分享

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-03-03**
**原文連結：本講義為多篇文獻之綜合整理，以 [BEME Guide No. 84 (*Med Teach* 2024)](https://doi.org/10.1080/0142159X.2024.2314198) 及 [Macy Foundation Report (*Acad Med* 2025)](https://doi.org/10.1097/ACM.0000000000006107) 為核心架構**

---

## 目錄

1. [前言與概述](#1-前言與概述)
2. [LLM 在醫學考試的表現](#2-llm-在醫學考試的表現)
3. [AI 作為教學工具](#3-ai-作為教學工具)
4. [AI 在評量與回饋的應用](#4-ai-在評量與回饋的應用)
5. [VR/AR/XR 在醫學教育的應用](#5-vrarxr-在醫學教育的應用)
6. [倫理、學術誠信與機構政策](#6-倫理學術誠信與機構政策)
7. [國際指引與共識聲明](#7-國際指引與共識聲明)
8. [台灣與亞太現況](#8-台灣與亞太現況)
9. [未來展望與建議](#9-未來展望與建議)
10. [參考文獻](#參考文獻)

---

## 核心發現摘要

> **現況**：AI 在醫學教育的應用正處於爆發期 — BEME Guide No. 84 統整了 278 篇文獻，Macy Foundation 審閱了 455 篇，AMEE 已發布 6 份相關指引（2023-2025）。
>
> **關鍵數據**：GPT-4 系列在 USMLE 達 86-95% 正確率；GAI-based 教學在實作技能優於傳統教學（SMD 0.63, p = 0.02）；92.9% 的 LLM 虛擬病人研究發表於近 2 年。
>
> **挑戰**：學術誠信、AI 偏差、過度依賴、教師數位素養不足、制度政策落差。

---

## 1. 前言與概述

### 為什麼現在要談 AI 與醫學教育？

- 2022 年 11 月 ChatGPT 發布後，AI 在醫學教育的研究文獻**呈指數增長**
- LLM（Large Language Model）首次在 USMLE 達到及格標準（2023）
- WHO（2024）、AAMC（2025）、AMEE（2023-2025）相繼發布 AI 教育指引
- **台灣**：MEDINFO 2025 在台北舉辦；台灣 AI 醫療論文全球排名第 10

### AI 在醫學教育的應用地圖

```text
AI 在醫學教育的應用
    |
    ├── 教學 (Teaching)
    |   ├── LLM 個人化導學 (AI Tutoring)
    |   ├── 虛擬病人 (Virtual Patients)
    |   ├── 臨床推理訓練 (Clinical Reasoning)
    |   └── 適性學習平台 (Adaptive Learning)
    |
    ├── 評量 (Assessment)
    |   ├── 自動化評分 (Automated Grading)
    |   ├── 隱匿式評量 (Stealth Assessment)
    |   ├── OSCE 自動評估
    |   └── 學習軌跡預測 (Learning Analytics)
    |
    ├── 臨床技能 (Clinical Skills)
    |   ├── VR/AR 手術訓練
    |   ├── AI-ECG 判讀訓練
    |   ├── 影像判讀 AI 輔助
    |   └── 遊戲化學習 (Gamification)
    |
    └── 行政與研究 (Administration)
        ├── 入學審查 NLP 分析
        ├── 課程設計與優化
        └── 學術出版 AI 使用規範
```

---

## 2. LLM 在醫學考試的表現

### 2.1 里程碑研究

| 研究 | 模型 | 考試 | 正確率 | 年份 |
|------|------|------|--------|------|
| Kung et al. | ChatGPT (GPT-3.5) | USMLE Step 1-3 | **~60%** (及格邊緣) | 2023 |
| Nori et al. | GPT-4 | USMLE | **~86%** | 2023 |
| Singhal et al. | Med-PaLM 2 | MedQA | **86.5%** | 2023 |
| Bicknell et al. | GPT-4o | USMLE | 顯著提升 | 2024 |
| Kasagga et al. | GPT-o1 | 全球 10 考試系統 | **95.4%** | 2025 |

### 2.2 Network Meta-Analysis：全球醫學執照考試 (2025)

- **120 evaluations，16 models，9 languages，10 exam systems**
- **13/16 models 超過 60% 及格線**
- Top performers：GPT-o1 (95.4%) > DeepSeek-R1 (92.0%) > GPT-4o (89.4%)
- 中文/日文考試表現較低 → 語言影響顯著
- Model type、exam system、language 解釋了 **89% 的異質性**

### 2.3 GPT-4 的「軟技能」表現

- Brin et al. (2023)：80 題 USMLE 軟技能（溝通、倫理、同理心）
- **GPT-4：90%** vs ChatGPT：62.5%
- GPT-4 展現 empathy 能力，超越 AMBOSS 用戶平均

### 2.4 ChatGPT 醫學回應品質的系統性回顧

- Wei et al. (2024)：60 studies（17 in meta-analysis）
- 整體準確率：**56%** (95% CI: 51-60%)
- → LLM 作為教學輔助 ≠ 直接取代臨床判斷

> **Pearl**：LLM 在結構化考試表現優異（高達 95%），但在開放式臨床情境的準確率仍有限（~56%）。適合作為學習工具，不適合作為臨床決策的唯一依據。

---

## 3. AI 作為教學工具

### 3.1 LLM-Based 虛擬病人

**Zeng et al. (2025) — Scoping Review**
- PRISMA-ScR，28 studies（2023-2025），5 databases
- **92.9%** 研究發表於近 2 年（早期發展階段）
- 應用：問診訓練、臨床推理、病史詢問
- 進階技術：social robots、VR、mixed reality 增加真實感
- 僅 **13%** 使用 validated tools；僅 **21.7%** 客觀測量 learning outcomes

**Holderried et al. (2024) — GPT-4 模擬病人**
- 106 conversations，1,894 Q&A pairs
- GPT-4 role-play 在 **> 99%** 案例中「medically plausible」
- 與 human rater 的 interrater reliability：**Cohen κ = 0.832**（almost perfect）
- 能提供結構化 history-taking feedback

### 3.2 GAI-Based 教學 vs 傳統教學

**Li et al. (2025) — Meta-Analysis of 11 RCTs, 786 Students**

| 結果 | SMD (95% CI) | P 值 | 解讀 |
|------|-------------|------|------|
| 知識獲得 (Knowledge) | 0.27 (-0.31 to 0.85) | 0.36 | **無顯著差異** |
| **實作技能 (Practical skills)** | **0.63** (0.10-1.16) | **0.02** | **GAI 較好** |
| 學生滿意度 | 較高 | — | GAI 組較滿意 |

- 81.8% 使用 ChatGPT；72.7% 來自亞洲機構
- → GAI 在知識傳遞與傳統教學相當，但在**實作技能**上有優勢

### 3.3 多平台 LLM 比較

| LLM | 解剖學 | 神經科學 | 特色 |
|-----|--------|---------|------|
| ChatGPT (GPT-4) | 優 | 優 | 最廣泛使用 |
| Claude | 優 | 優 | 長文脈絡能力強 |
| Copilot | 中 | 中 | 搜尋整合佳 |
| Gemini | 優 | 良 | 多模態能力 |

- 各 LLM 均超越學生平均分數（Mavrych et al., 2025）

> **Pearl**：AI 虛擬病人與 LLM 導學是目前最有潛力的應用，但大部分研究仍在早期階段，缺乏 validated outcomes 與長期追蹤。

---

## 4. AI 在評量與回饋的應用

### 4.1 自動化模擬評量

**Siddiqui et al. (2023) — Deep Learning for Simulation Assessment**
- 52 anaphylaxis simulation videos
- Bidirectional transformer encoder model
- 最佳模型 accuracy：**71%** (F1 = 0.68)
- → 證實 deep learning 自動化模擬評量的可行性

### 4.2 AI 在手術技能評量

**Boal et al. (2024) — Systematic Review**
- AI 系統（CNN, RNN）用於 robotic surgery 技能自動評量
- 可提供客觀、即時的技術評分
- 挑戰：assessment criteria 標準化

### 4.3 隱匿式評量 (Stealth Assessment)

- AI-powered 嵌入式評量：在學習活動中不知不覺地評估能力
- 持續性 competency evaluation，不干擾學習流程
- 未來 competency-based medical education (CBME) 的關鍵技術

### 4.4 AI 對溝通技巧的回饋

**Bedmutha et al. (2024)**
- AI 生成 social signals 回饋（眼神接觸、肢體語言）
- 在 patient-provider communication 中的技術可行性已驗證

### 4.5 AMEE Guide No. 178：AI 在 HPE Assessment

- 涵蓋：自動化文字評量、影像判讀回饋、AI as tutor/learner
- 所需能力、倫理議題、教師發展
- **最全面的 AI 評量指引**

---

## 5. VR/AR/XR 在醫學教育的應用

### 5.1 應用領域

| 技術 | 應用場景 | 優勢 |
|------|---------|------|
| **VR (Virtual Reality)** | 手術模擬、解剖教學 | 沉浸式、可重複練習 |
| **AR (Augmented Reality)** | 床邊教學、超音波導引 | 真實環境疊加資訊 |
| **Mixed Reality** | 複雜手術規劃 | 結合虛實 |

### 5.2 COVID-19 加速了 VR/AR 的採用

**Sadek et al. (2023) — Systematic Review**
- VR/AR 在疫情期間**維持或提升**了醫學教育品質
- 特別適用：anatomy、surgical training、procedural skills

### 5.3 XR 在外科訓練的接受度

**Toni et al. (2024) — Umbrella Review**
- 外科 trainee 對 XR 的接受度**高**
- Technology Acceptance Model (TAM) 的兩大因子：
  - **Perceived usefulness**（感知有用性）
  - **Ease of use**（易用性）
- → 兩者均強烈預測 VR/AR adoption

### 5.4 遊戲化學習 (Gamification) 在臨床推理

- Scoping review (2025)：53 studies，20 countries
- 美國 28.3%、德國 9.4%、法國 7.6%
- Game-design elements 提升 engagement 與 interaction
- 適用於 clinical reasoning 訓練

---

## 6. 倫理、學術誠信與機構政策

### 6.1 學術誠信的挑戰

- GenAI 可生成難以偵測的 AI-written assignments
- 傳統 plagiarism detection 工具效果有限
- AI detector 的 false positive/negative 率仍高
- 需要更新 honor codes 與 assessment methods

### 6.2 美國醫學院 AI 政策審查

**Rush et al. (2026) — 146 U.S. Medical Schools**
- 平均覆蓋 24 項 framework subthemes 中的 **8 項 (32.3%)**

| 最常涵蓋 | 比例 | 最少涵蓋 | 比例 |
|----------|------|----------|------|
| Academic Honesty/Plagiarism | **81.5%** | Audit/Compliance | 6.8% |
| Appropriate Use | ~70% | Technical Infrastructure | 6.2% |
| Citation/Attribution | ~60% | Environmental Stewardship | **1.4%** |

- → **策略規劃有重大缺口**：多數政策僅聚焦「禁止作弊」，缺乏整體 AI 整合策略

### 6.3 AMEE Guide No. 158：AI 倫理指引

涵蓋八大面向：

1. **Data gathering** — 資料收集的倫理
2. **Anonymity & Privacy** — 匿名與隱私保護
3. **Consent** — 知情同意
4. **Data ownership** — 資料所有權
5. **Security** — 資安
6. **Bias** — AI 偏差
7. **Transparency** — 透明度
8. **Responsibility & Autonomy** — 責任與自主

### 6.4 AMEE Guide No. 192：學術出版中的 AI 使用揭露

- 2025 年發布，提供 GenAI 使用透明報告的框架
- 涵蓋：authorship、verification、plagiarism、bias、data privacy
- 包括 internal 與 external disclosure 的標準

---

## 7. 國際指引與共識聲明

### 7.1 AAMC Principles for Responsible AI Use (2025)

- **Version 1.0**：2025 年 1 月完成
- **Version 2.0**：2025 年 7 月完成
- 七大基本原則用於 AI 整合至醫學教育
- 與 AMEE、IAMSE、APMEN、AAHCI 合作制定
- 另外發布 **AI Competencies for Medical Educators**

### 7.2 WHO Guidance on AI Ethics for Health (2024)

- 超過 **40 項建議**，針對政府、科技公司與醫療提供者
- 涉及 AI 在醫護教育的應用（simulated patients、dynamic educational texts）
- **警告不應以 AI 取代臨床判斷**
- 強調從 AI 開發早期即納入 stakeholder engagement

### 7.3 UNESCO AI and Education (2024-2025)

- 2024 年 9 月：發布 **AI Competency Frameworks for Teachers and Students**
- 2025 年：發布 AI 對教育 access、equity、quality、governance 的影響報告
- 定義理解、應用、批判性評估 AI 技術的能力

### 7.4 AMEE Guides 總覽

| Guide | Year | 主題 |
|-------|------|------|
| **No. 156** | 2023 | AI in Medical Education Research 基礎 |
| **No. 158** | 2023 | AI 倫理使用 |
| **No. 172** | 2024 | 為 AGI 做準備 |
| **No. 178** | 2025 | AI 在 HPE Assessment |
| **No. 190** | 2025 | AI 在 Co-Creation of HPE |
| **No. 192** | 2025 | 學術出版中的 AI 使用揭露 |

### 7.5 Macy Foundation Conference (2025)

- 2024 年 11 月於 Atlanta 舉辦，3 天會議
- Part I (Boscardin et al.)：審閱 **455 篇文獻**，mapping AI across 5 domains
- Part II (Gin et al.)：訪談 **25 位 AI 教育創新者**
- 啟動 grants program，支持 3 個 2-year demonstration projects

---

## 8. 台灣與亞太現況

### 8.1 台灣 AI 醫療教育生態

| 項目 | 現況 |
|------|------|
| AI 醫療論文全球排名 | **第 10 名** (2024, 1,331 篇) |
| 國家政策 | **AI Taiwan Action Plan 2.0** (2023) |
| 重要活動 | **MEDINFO 2025**（第 20 屆世界醫學資訊大會）台北 |
| 學術機構 | 台北醫學大學 AI in Medicine 碩士班 |
| 醫院認證 | 多家醫院獲 HIMSS Stage 7 認證 |
| 健保署 | 與 Google Health 合作五年 AI 計畫 |

### 8.2 亞太區域趨勢

- GAI-based teaching meta-analysis 中 **72.7%** RCT 來自亞洲
- Asia Pacific Journal of Education (2024) 專文：亞太 GenAI 教育研究議程
- 部分東南亞國家 AI 教育應用仍「limited and fragmented」
- 語言障礙：LLM 在中文/日文醫學考試表現較低

---

## 9. 未來展望與建議

### 9.1 短期可行的應用（現在就可以做）

| 應用 | 工具 | 適用場景 |
|------|------|---------|
| **LLM 輔助自主學習** | ChatGPT, Claude, Gemini | 問答、解釋、案例討論 |
| **AI 產生練習題** | GPT-4, Claude | Formative assessment |
| **AI 虛擬病人** | GPT-4 role-play | History-taking 練習 |
| **AI 文獻整理** | Claude, Perplexity | Journal reading |
| **AI 簡報製作** | Marp + Claude | 教學投影片 |

### 9.2 中期發展（1-3 年）

- AI-powered adaptive learning platforms（個人化學習路徑）
- VR/AR 與 AI 結合的沉浸式手術訓練
- Stealth assessment 嵌入式能力評量
- AI-ECG/影像 training modules

### 9.3 長期願景

- AGI (Artificial General Intelligence) in HPE（AMEE Guide No. 172）
- Virtual PCI planning 作為教學工具（回顧本系列 CTA 講義）
- AI-driven precision education：個人化學習路徑 + 即時能力評估 + 智慧回饋

### 9.4 對教育者的建議

> **Pearl 1**：不要問「要不要用 AI」，要問「怎麼負責任地用 AI」
>
> **Pearl 2**：從 assessment redesign 開始 — 如果 AI 可以輕易完成的作業，可能需要重新設計
>
> **Pearl 3**：培養學生的 AI literacy，不只是使用 AI，更要批判性地評估 AI 的輸出
>
> **Pearl 4**：教師自己要先學會使用 AI — faculty development 是成功的關鍵

---

## 參考文獻

1. Gordon M, Daniel M, Ajiboye A, et al. A scoping review of artificial intelligence in medical education: BEME Guide No. 84. [*Med Teach.* 2024;46(4):446-470.](https://doi.org/10.1080/0142159X.2024.2314198)

2. Boscardin CK, Abdulnour RE, Gin BC. Macy Foundation Innovation Report Part I: Current Landscape of AI in Medical Education. [*Acad Med.* 2025;100(9S):S15-S21.](https://doi.org/10.1097/ACM.0000000000006107)

3. Gin BC, LaForge K, Burk-Rafel J, Boscardin CK. Macy Foundation Innovation Report Part II: From Hype to Reality. [*Acad Med.* 2025;100(9S):S22-S29.](https://doi.org/10.1097/ACM.0000000000006117)

4. Lee P, Bubeck S, Petro J. Benefits, Limits, and Risks of GPT-4 as an AI Chatbot for Medicine. [*N Engl J Med.* 2023;388:1233-1239.](https://doi.org/10.1056/NEJMsr2214184)

5. Singhal K, Azizi S, Tu T, et al. Large language models encode clinical knowledge. [*Nature.* 2023;620:172-180.](https://doi.org/10.1038/s41586-023-06291-2)

6. Kung TH, Cheatham M, Medenilla A, et al. Performance of ChatGPT on USMLE. [*PLOS Digit Health.* 2023;2(2):e0000198.](https://doi.org/10.1371/journal.pdig.0000198)

7. Kasagga A, Sapkota A, et al. Performance of LLMs on Medical Licensing Exams Worldwide: Network Meta-Analysis. [*Cureus.* 2025;17(10):e94300.](https://doi.org/10.7759/cureus.94300)

8. Li J, Yin K, Wang Y, et al. Effectiveness of GAI-based teaching vs traditional methods: meta-analysis of RCTs. [*BMC Med Educ.* 2025;25:1087.](https://doi.org/10.1186/s12909-025-07750-2)

9. Zeng J, Qi W, Shen S, et al. LLM-Based Virtual Patients: Scoping Review. [*J Med Internet Res.* 2025;27:e79091.](https://doi.org/10.2196/79091)

10. Holderried F, et al. Language Model-Powered Simulated Patient With Automated Feedback. [*JMIR Med Educ.* 2024;10:e59213.](https://doi.org/10.2196/59213)

11. Tolsgaard MG, et al. Fundamentals of AI in Medical Education Research: AMEE Guide No. 156. [*Med Teach.* 2023;45(6):565-573.](https://doi.org/10.1080/0142159X.2023.2180340)

12. Masters K. Ethical Use of AI in HPE: AMEE Guide No. 158. [*Med Teach.* 2023;45(6):574-584.](https://doi.org/10.1080/0142159X.2023.2186203)

13. Masters K, et al. AI in HPE Assessment: AMEE Guide No. 178. [*Med Teach.* 2025;47(9):1215-1230.](https://doi.org/10.1080/0142159X.2024.2445037)

14. Rush E, et al. An audit of AI-related documents across U.S. medical schools. [*Med Teach.* 2026;48(3).](https://doi.org/10.1080/0142159X.2025.2564869)

15. WHO. Ethics and governance of AI for health: Guidance on large multi-modal models. [Geneva: WHO; 2024.](https://www.who.int/publications/i/item/9789240084759)

16. AAMC. Principles for Responsible AI Use in Medical Education v2.0. [2025.](https://www.aamc.org/about-us/mission-areas/medical-education/principles-ai-use)

17. Wei Q, Yao Z, et al. Evaluation of ChatGPT-generated medical responses: systematic review and meta-analysis. [*J Biomed Inform.* 2024;151:104620.](https://doi.org/10.1016/j.jbi.2024.104620)

18. Iqbal U, et al. Impact of LLM (ChatGPT) in healthcare: umbrella review. [*J Biomed Sci.* 2025;32:44.](https://doi.org/10.1186/s12929-025-01131-z)

---

*本文件僅供醫療專業人員教學參考。*
