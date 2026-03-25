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
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
footer: '謝慕揚 MD, PhD, FESC | AI 數位科技應用於醫學教育 | 2026'
---

<!-- _class: lead -->

# AI 數位科技應用於醫學教育
## AI and Digital Technology in Medical Education

**謝慕揚 MD, PhD, FESC**
多篇文獻綜合整理 | 2026-03-03
[BEME Guide No. 84](https://doi.org/10.1080/0142159X.2024.2314198) | [Macy Foundation Report](https://doi.org/10.1097/ACM.0000000000006107)

---

# 大綱

1. 為什麼現在要談 AI 與醫學教育？
2. LLM 在醫學考試的驚人表現
3. AI 作為教學工具：虛擬病人與導學
4. AI 在評量與回饋
5. VR/AR/XR 沉浸式學習
6. 倫理、學術誠信與政策
7. 國際指引：AAMC、WHO、AMEE
8. 台灣現況與未來展望

---

<!-- _class: divider -->

# 第一部分：AI 爆發的時代

---

# 為什麼現在要談 AI？

### 關鍵時間軸

| 年份 | 里程碑 |
|------|--------|
| 2022.11 | ChatGPT 發布 |
| 2023.03 | GPT-4 通過 USMLE (~86%) |
| 2023.07 | Med-PaLM 2 達 86.5% (Nature) |
| 2024.01 | WHO AI Ethics 指引發布 |
| 2024.03 | BEME Guide No. 84 (278 篇文獻) |
| 2025.01 | AAMC AI Principles v1.0 |
| 2025.07 | AAMC AI Principles v2.0 |
| 2025.08 | MEDINFO 2025 台北 |
| 2025.09 | Macy Foundation 報告 |

---

# AI 在醫學教育的應用地圖

```text
AI 在醫學教育
  |
  ├── 教學 (Teaching)
  |   ├── LLM 個人化導學
  |   ├── 虛擬病人 (Virtual Patients)
  |   └── 適性學習平台
  |
  ├── 評量 (Assessment)
  |   ├── 自動化評分
  |   ├── 隱匿式評量 (Stealth Assessment)
  |   └── 學習軌跡預測
  |
  ├── 臨床技能
  |   ├── VR/AR 手術訓練
  |   ├── AI-ECG 判讀
  |   └── 遊戲化學習
  |
  └── 行政
      ├── 入學審查 NLP
      └── 課程優化
```

---

<!-- _class: divider -->

# 第二部分：LLM 的醫學考試表現

---

# LLM 在 USMLE 的進化

| 模型 | 年份 | USMLE 正確率 | 備註 |
|------|------|-------------|------|
| ChatGPT (GPT-3.5) | 2023 | **~60%** | 及格邊緣 |
| GPT-4 | 2023 | **~86%** | 大幅超越及格線 |
| Med-PaLM 2 | 2023 | **86.5%** | Google, Nature |
| GPT-4o | 2024 | **~89%** | 持續進步 |
| **GPT-o1** | **2025** | **95.4%** | 接近滿分 |

- Network meta-analysis (2025)：120 evaluations, 16 models, 9 languages
- **13/16 models 超過 60% 及格線**

> **3 年內從及格邊緣到 95%！**

---

# 但 LLM 不是萬能的

### ChatGPT 醫學回應品質 (Wei et al. 2024)

- Systematic review: 60 studies
- **整體準確率：56%** (95% CI: 51-60%)

### 重要區別

| 情境 | LLM 表現 |
|------|---------|
| **結構化考試** (MCQ) | 優秀 (86-95%) |
| **開放式臨床問題** | 中等 (~56%) |
| **軟技能** (溝通、倫理) | GPT-4: 90% |
| **即時臨床決策** | 仍不可靠 |

> **Pearl**：LLM 適合作為學習工具，不適合作為臨床決策的唯一依據

---

<!-- _class: divider -->

# 第三部分：AI 教學工具

---

# AI 虛擬病人：爆發成長

### Zeng et al. (2025) — Scoping Review

- 28 studies (2023-2025)
- **92.9%** 發表於近 2 年
- 應用：問診訓練、臨床推理、病史詢問

### GPT-4 模擬病人 (Holderried et al. 2024)

- 106 conversations, 1,894 Q&A pairs
- Medically plausible: **> 99%**
- Interrater reliability (Cohen κ): **0.832** (almost perfect)
- 能提供結構化 history-taking feedback

> **Pearl**：AI 虛擬病人已經可以達到「幾乎完美」的臨床合理性

---

# GAI 教學 vs 傳統教學

### Li et al. (2025) — Meta-analysis of 11 RCTs, 786 Students

| 結果 | SMD | P 值 | 結論 |
|------|-----|------|------|
| 知識獲得 | 0.27 | 0.36 | 無差異 |
| **實作技能** | **0.63** | **0.02** | **GAI 較好** |
| 學生滿意度 | 較高 | — | GAI 較滿意 |

- 81.8% 使用 ChatGPT
- 72.7% 來自亞洲機構

> **GAI 在知識傳遞與傳統相當，但實作技能有優勢**

---

# 多平台 LLM 教學比較

### Mavrych et al. (2025)

| LLM | 解剖學 | 神經科學 | 特色 |
|-----|--------|---------|------|
| **ChatGPT** | 優 | 優 | 最廣泛使用 |
| **Claude** | 優 | 優 | 長文脈絡能力強 |
| **Copilot** | 中 | 中 | 搜尋整合佳 |
| **Gemini** | 優 | 良 | 多模態能力 |

- 各 LLM **均超越學生平均**
- 不同模型各有擅長領域

---

<!-- _class: divider -->

# 第四部分：AI 評量與回饋

---

# AI 在評量的四大應用

### 1. 自動化模擬評量
- Deep learning model: **71% accuracy** (F1 = 0.68)
- 自動 pass/fail 判定 anaphylaxis simulation

### 2. 手術技能自動評量
- CNN/RNN 用於 robotic surgery assessment
- 客觀、即時的技術評分

### 3. 隱匿式評量 (Stealth Assessment)
- 嵌入學習活動中，**不知不覺地**評估能力
- CBME 的未來關鍵技術

### 4. 溝通技巧 AI 回饋
- 自動偵測 eye contact、body language
- 生成 actionable feedback

---

# AMEE Guide No. 178：AI 評量指引

### 涵蓋範圍 (2025)

| 面向 | 內容 |
|------|------|
| 文字評量 | 自動化 written response 評分 |
| 影像判讀 | AI feedback on interpretation |
| AI as Tutor | AI 扮演教師角色 |
| AI as Learner | AI 模擬學生理解 |
| 所需能力 | 教師與學生的 AI competencies |
| 倫理議題 | Bias, fairness, transparency |

> **目前最全面的 AI 評量指引**

---

<!-- _class: divider -->

# 第五部分：VR/AR/XR 沉浸式學習

---

# 延展實境在醫學教育

| 技術 | 應用 | 優勢 |
|------|------|------|
| **VR** | 手術模擬、解剖 | 沉浸式、可重複 |
| **AR** | 床邊教學、超音波 | 真實環境疊加 |
| **Mixed Reality** | 複雜手術規劃 | 結合虛實 |

### COVID-19 加速了 XR 採用
- VR/AR **維持或提升**了疫情期間教育品質 (Sadek 2023)

### 外科 Trainee 接受度高
- Umbrella review (Toni 2024)
- **Perceived usefulness** + **ease of use** → 預測 adoption

### 遊戲化學習 (Gamification)
- 53 studies, 20 countries → 提升 clinical reasoning engagement

---

<!-- _class: divider -->

# 第六部分：倫理與政策

---

# 學術誠信的新挑戰

### 問題

- GenAI 可生成**難以偵測**的 AI-written assignments
- AI detector 的 false positive/negative 率仍高
- 傳統 plagiarism detection 效果有限

### 美國醫學院 AI 政策現況 (Rush et al. 2026)

- 146 所醫學院審查
- 平均僅涵蓋 **32.3%** 的 framework subthemes

| 最常涵蓋 | 最少涵蓋 |
|----------|----------|
| Academic Honesty (**81.5%**) | Technical Infrastructure (6.2%) |
| Appropriate Use (~70%) | Environmental Stewardship (**1.4%**) |

> **多數政策只聚焦「禁止作弊」，缺乏整體 AI 策略**

---

# AMEE 倫理指引重點

### AMEE Guide No. 158：八大面向

1. **Data gathering** — 資料收集倫理
2. **Privacy** — 隱私保護
3. **Consent** — 知情同意
4. **Data ownership** — 資料所有權
5. **Security** — 資安
6. **Bias** — AI 偏差
7. **Transparency** — 透明度
8. **Responsibility** — 責任歸屬

### AMEE Guide No. 192：學術出版 AI 揭露
- GenAI 使用的透明報告框架
- Authorship, verification, plagiarism, bias

---

<!-- _class: divider -->

# 第七部分：國際指引

---

# 三大國際組織的 AI 教育立場

| 組織 | 文件 | 年份 | 重點 |
|------|------|------|------|
| **AAMC** | Principles v2.0 | 2025 | 七大原則 + AI Competencies |
| **WHO** | AI Ethics Guidance | 2024 | 40+ 建議，不應取代臨床判斷 |
| **UNESCO** | AI Competency Frameworks | 2024 | 教師 + 學生 AI 能力框架 |

### AAMC 七大原則 (v2.0, 2025)
- 與 AMEE, IAMSE, APMEN, AAHCI 國際合作
- 涵蓋 AI 整合、learner support、教育流程

### WHO 關鍵訊息
- **不應以 AI 取代臨床判斷**
- 從 AI 開發早期即納入 stakeholder engagement

---

# AMEE Guides 總覽 (2023-2025)

| Guide | 主題 | 適用對象 |
|-------|------|---------|
| **No. 156** | AI in MedEd Research 基礎 | 研究者 |
| **No. 158** | AI 倫理使用 | 所有教育者 |
| **No. 172** | 為 AGI 做準備 | 機構決策者 |
| **No. 178** | AI 在 Assessment | 評量設計者 |
| **No. 190** | AI in Co-Creation | 課程設計者 |
| **No. 192** | 學術出版 AI 揭露 | 研究者/作者 |

> **6 份 AMEE Guides（2023-2025）— AI 在醫學教育最完整的指引體系**

---

<!-- _class: divider -->

# 第八部分：台灣與未來

---

# 台灣 AI 醫療教育現況

| 項目 | 現況 |
|------|------|
| AI 醫療論文全球排名 | **第 10** (1,331 篇, 2024) |
| 國家政策 | AI Taiwan Action Plan 2.0 |
| 國際會議 | **MEDINFO 2025 台北** |
| 學術機構 | 台北醫學大學 AI in Medicine 碩士班 |
| 健保署合作 | Google Health 五年 AI 計畫 |
| 醫院認證 | 多家 HIMSS Stage 7 |

### 亞太趨勢
- GAI 教學研究 **72.7%** 來自亞洲
- LLM 在中文考試表現較低 → 語言是挑戰

---

# 現在就可以做的事

| 應用 | 工具 | 場景 |
|------|------|------|
| LLM 輔助自學 | ChatGPT, Claude | 問答、案例討論 |
| AI 產生練習題 | GPT-4, Claude | Formative assessment |
| AI 虛擬病人 | GPT-4 role-play | History-taking |
| AI 文獻整理 | Claude, Perplexity | Journal reading |
| AI 簡報製作 | Marp + Claude | 教學投影片 |

> **Pearl**：你現在看到的這份投影片，就是用 Claude + Marp 製作的

---

# 對教育者的四個建議

> **1. 不要問「要不要用 AI」，要問「怎麼負責任地用 AI」**

> **2. 從 assessment redesign 開始** — AI 能輕易完成的作業，需要重新設計

> **3. 培養 AI literacy** — 不只使用 AI，更要批判性地評估 AI 輸出

> **4. 教師自己先學會用 AI** — faculty development 是成功的關鍵

---

<!-- _class: small-text -->

# 參考文獻 (1/2)

1. Gordon M, et al. BEME Guide No. 84. [*Med Teach.* 2024;46(4):446-470.](https://doi.org/10.1080/0142159X.2024.2314198)
2. Boscardin CK, et al. Macy Foundation Part I. [*Acad Med.* 2025;100(9S):S15-S21.](https://doi.org/10.1097/ACM.0000000000006107)
3. Lee P, et al. GPT-4 for Medicine. [*NEJM.* 2023;388:1233-1239.](https://doi.org/10.1056/NEJMsr2214184)
4. Singhal K, et al. Med-PaLM. [*Nature.* 2023;620:172-180.](https://doi.org/10.1038/s41586-023-06291-2)
5. Kasagga A, et al. LLMs on Medical Exams. [*Cureus.* 2025;17(10):e94300.](https://doi.org/10.7759/cureus.94300)
6. Li J, et al. GAI vs Traditional Teaching. [*BMC Med Educ.* 2025;25:1087.](https://doi.org/10.1186/s12909-025-07750-2)
7. Zeng J, et al. LLM Virtual Patients. [*JMIR.* 2025;27:e79091.](https://doi.org/10.2196/79091)

---

<!-- _class: small-text -->

# 參考文獻 (2/2)

8. Masters K. AMEE Guide No. 158. [*Med Teach.* 2023;45(6):574-584.](https://doi.org/10.1080/0142159X.2023.2186203)
9. Masters K, et al. AMEE Guide No. 178. [*Med Teach.* 2025;47(9):1215-1230.](https://doi.org/10.1080/0142159X.2024.2445037)
10. Rush E, et al. AI Policies Across U.S. Medical Schools. [*Med Teach.* 2026;48(3).](https://doi.org/10.1080/0142159X.2025.2564869)
11. WHO. AI Ethics for Health. [Geneva: WHO; 2024.](https://www.who.int/publications/i/item/9789240084759)
12. AAMC. AI Principles v2.0. [2025.](https://www.aamc.org/about-us/mission-areas/medical-education/principles-ai-use)
13. Wei Q, et al. ChatGPT Medical Responses. [*J Biomed Inform.* 2024;151:104620.](https://doi.org/10.1016/j.jbi.2024.104620)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
*本投影片由 Claude + Marp 協助製作*
