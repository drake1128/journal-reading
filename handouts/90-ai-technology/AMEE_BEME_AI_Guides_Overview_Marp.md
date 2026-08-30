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
  section.lead h3 { color: #b0c4de; }
  section.lead p, section.lead strong, section.lead li { color: #dfe6e9; }
  section.lead a { color: #9ec5fe; }
  /* 淺底框內一律強制深色字：p/strong/a/li 的淺色規則不得覆蓋 */
  section.lead blockquote,
  section.lead blockquote p,
  section.lead blockquote li,
  section.lead blockquote strong,
  section.lead blockquote em {
    color: #1a2740;
    background-color: #eef2f7;
    border-left: 4px solid #0072bc;
  }
  section.lead blockquote a { color: #0a4a8f; }
  section.lead code { background-color: #eef2f7; color: #1a2740; }
  section.lead footer, section.divider footer { color: #c3d3e8; }
  section.lead::after, section.divider::after { color: #c3d3e8; }
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
    font-size: 2.1em;
    text-align: center;
  }
  section.divider h2 { color: #ffe066; text-align: center; border-bottom: none; }
  section.divider h3 { color: #ffffff; text-align: center; }
  section.divider p, section.divider strong, section.divider li { color: #ffffff; }
  section.divider blockquote,
  section.divider blockquote p,
  section.divider blockquote strong {
    color: #1a2740;
    background-color: #eef2f7;
    border-left: 4px solid #1a2740;
  }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.45em; }
  h2 { color: #0072bc; font-size: 1.05em; }
  h3 { color: #555555; }
  table { font-size: 0.62em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 5px 8px; }
  td { padding: 4px 8px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.4em 0.9em;
    font-size: 0.82em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.7em;
    font-size: 0.58em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.8em; }
  section.small-text table { font-size: 0.55em; }
  ul, ol { font-size: 0.92em; }
footer: '謝慕揚 MD, PhD, FESC | AMEE / BEME AI 指引全景 | 2026'
---

<!-- _class: lead -->
# AMEE / BEME 的 AI 指引
## 七份官方指引全景導讀 2023–2026

**謝慕揚 MD, PhD, FESC** | 2026-08-23

從研究方法 → 倫理 → 評量 → AGI → 共創 → 發表揭露

> 所有內容摘自各指引之 PubMed 摘要，經整理與詮釋
> 完整論述請閱讀原文（每頁均附 DOI 連結）

---

# 為什麼要一次看完這七份？

**它們不是七篇零散的論文，而是一套逐步展開的體系。**

AMEE（歐洲醫學教育學會）與 BEME（實證醫學教育合作組織）
在 2023–2026 三年間，針對 AI 連續發布七份官方指引 ——

從「**怎麼做研究**」開始，到「**怎麼守倫理**」，
再到「**怎麼評量**」「**怎麼面對 AGI**」「**怎麼共創**」，
最後回到「**怎麼誠實揭露**」。

> 讀完這七份，等於掌握了目前國際上對「AI 與醫學教育」
> **最具權威性的完整立場**。

---

# 七份指引一覽

| 指引 | 年份 | 主題 | 第一作者 |
|------|------|------|---------|
| **AMEE 156** | 2023 | AI 於醫學教育**研究**的基礎 | Tolsgaard MG |
| **AMEE 158** | 2023 | AI 在健康專業教育的**倫理使用** | Masters K |
| **BEME 84** | 2024 | AI 於醫學教育的**實證地圖**（scoping review） | Gordon M |
| **AMEE 172** | 2024 | 為 **AGI**（通用人工智慧）做準備 | Masters K |
| **AMEE 178** | 2025 | AI 於健康專業教育**評量** | Masters K |
| **AMEE 190** | 2026 | AI 於教育**共創**（co-creation） | Suliman S |
| **AMEE 192** | 2026 | 學術發表中**何時、如何揭露** AI 使用 | Cleland J |

> Ken Masters 一人主導其中三份（158、172、178）—— 他是這個系列的核心人物。

---

# 三條主軸

```text
【研究方法軸】              【倫理治理軸】              【教與評軸】
AMEE 156 研究基礎            AMEE 158 倫理原則            AMEE 178 評量
BEME 84  實證地圖            AMEE 192 發表揭露            AMEE 190 共創
                            AMEE 172 AGI 前瞻
      ↓                          ↓                          ↓
 「怎麼做 AI 研究」        「什麼可以做、要交代什麼」    「課堂與考場怎麼變」
```

**閱讀順序建議**

先讀 **BEME 84**（知道全局有什麼）
→ 再讀 **AMEE 178**（最貼近日常教學）
→ 再讀 **AMEE 158**（倫理底線）
→ 其餘依需求選讀

---

<!-- _class: divider -->
# AMEE Guide No. 156
## AI 於醫學教育研究的基礎（2023）

---

# AMEE 156｜填補方法學的空白

**問題意識**：AI 在學習、教學、評量的應用快速成長，
但**幾乎沒有概念性或方法學的指引**給想投入 AI 研究的醫學教育者。

**這份指引的三個明確目標**

1. 說明**閱讀與執行** AI 醫學教育研究的實務考量
2. 定義**基本術語**
3. 指出**哪些醫學教育問題與資料**適合用 AI 處理

**舉出的應用範例**
- 自動化評分書面回答（written responses）
- 對醫學影像判讀提供回饋，且可達良好信度

> Tolsgaard MG, et al. *Med Teach*. 2023;45(6):565-573.
> [10.1080/0142159X.2023.2180340](https://doi.org/10.1080/0142159X.2023.2180340)

---

<!-- _class: divider -->
# AMEE Guide No. 158
## AI 的倫理使用（2023）

---

# AMEE 158｜刻意不談技術，只談倫理

**這份指引的定位很特別**：焦點**不在 AI 技術**，
而在教師與行政主管在教學環境中遇到 AI 系統時，
會實際面臨的**倫理問題**。

**涵蓋的 11 項倫理議題**

| | | |
|---|---|---|
| 資料蒐集 (data gathering) | 匿名性 (anonymity) | 隱私 (privacy) |
| 知情同意 (consent) | 資料所有權 (data ownership) | 資安 (security) |
| 偏誤 (bias) | 透明性 (transparency) | 責任 (responsibility) |
| 自主性 (autonomy) | 行善 (beneficence) | |

每個主題都說明**概念、為何重要、如何應對其複雜性**，並附延伸閱讀。

---

# AMEE 158｜核心訴求

> **目標是讓各層級的教師與決策者對這些議題保持警覺，
> 並採取「主動」作為 —— 而非等問題發生才反應。**

**為什麼這份很重要**

- 許多倫理原則在其他脈絡中並不陌生，
  但**放在 AI 的脈絡下會呈現不同樣貌**
- 指引也引入了一些**過去不熟悉的新議題**

**與 BEME 84 的呼應**
BEME 84 在檢視 278 篇文獻後，同樣強調
**AI 應用於醫學教育「急需」倫理指引**。

> Masters K. *Med Teach*. 2023;45(6):574-584.
> [10.1080/0142159X.2023.2186203](https://doi.org/10.1080/0142159X.2023.2186203)

---

<!-- _class: divider -->
# BEME Guide No. 84
## AI 於醫學教育的實證地圖（2024）

---

# BEME 84｜目前最完整的文獻地圖

**方法**（值得注意的是它的嚴謹度）

- **Rapid scoping review**，16 週完成
- 採 **Arksey & O'Malley** 架構
- 遵循 **STORIES** 與 **BEME** 報告指引
- 檢索 PubMed/MEDLINE、EMBASE、MedEdPublish
- **無日期與語言限制**
- 涵蓋 UME、GME、繼續教育；含原始研究與觀點文章
- 資料由**多組作者配對**進行圖表化

**成果規模**

## 納入 **278 篇**publication

---

# BEME 84｜三個關鍵發現

**1. 地域極度不均**

> **68% 來自北美與歐洲** —— 亞洲、非洲、南美的聲音嚴重不足。
> 對台灣而言，這既是限制，也是**投稿與貢獻的機會**。

**2. 應用範圍比想像的廣**

涵蓋 AI 於 **招生（admissions）**、教學、評量、**臨床推理** 等面向；
角色從「強化傳統教學方法」到「引入全新實踐」都有。

**3. 提出 FACETS 框架**

為未來研究的**高效用報告（high utility reporting）**提出的框架，
目的是讓後續研究更容易被比較與整合。

> Gordon M, et al. *Med Teach*. 2024;46(4):446-470.
> [10.1080/0142159X.2024.2314198](https://doi.org/10.1080/0142159X.2024.2314198)

---

<!-- _class: divider -->
# AMEE Guide No. 172
## 為 AGI 做準備（2024）

---

# AMEE 172｜開場白很直白

> **「生成式 AI 讓健康專業教育機構措手不及，
> 它們目前仍在調適這個已經改變的教育環境。
> 然而地平線上還有更大的一躍 —— AGI。」**

**AGI（Artificial General Intelligence，通用人工智慧）的五項特徵**

| 特徵 | 英文 |
|------|------|
| 多模態 | multi-modality |
| 通用性 | generality |
| 適應性 | adaptability |
| 自主性 | autonomy |
| 學習能力 | learning ability |

---

# AMEE 172｜影響與待解問題

**對學生的影響**
- 個人化學習（personalised learning）
- **電子導師（electronic tutors）**

**對機構的影響** + 醫療場域中 AGI 提供的脈絡

**指引明確點出的待解問題**

- 對**就業**的衝擊
- **社會風險**
- 學生的**適應力**
- **成本**
- **品質**

指引最後給出可能的**時間軸**，以及機構與教師可以採取的**第一步**。

> Masters K, et al. *Med Teach*. 2024. [10.1080/0142159X.2024.2387802](https://doi.org/10.1080/0142159X.2024.2387802)

---

<!-- _class: divider -->
# AMEE Guide No. 178
## AI 於健康專業教育評量（2025）

---

# AMEE 178｜最貼近日常教學的一份

**問題意識**：機構、教師、學習者都在跟 AI
**不斷演變的複雜性、危險與潛力**角力。

**這份指引刻意的立論方式**

> 雖然驅動力是 AI，但這份指引**把路徑扎根在教學理論（pedagogical theory）**，
> 而不是從技術出發。

**涵蓋的七個面向**

1. 人類反應的光譜（range of human responses）
2. 評量類型
3. 挑戰
4. **AI 作為 tutor 與 learner 的雙重角色**
5. 所需能力（required competencies）
6. 困難與倫理議題
7. **師資培育** + 評量中 AI 致謝（acknowledgment）的技術細節

---

# AMEE 178｜它想達成什麼

> **「在變局面前緩解恐懼，
> 並展示能讓教師與學習者充分發揮 AI 潛能的可能性。」**

**兩個值得注意的觀念**

**AI 同時是 tutor 也是 learner**
不只是把 AI 當工具用 —— 它既能教學生，也在從互動中學習。
這對評量的效度與公平性提出全新問題。

**評量中的 AI 致謝需要技術規範**
不只是「有沒有用 AI」，而是**如何具體標示** ——
這與 AMEE 192 的發表揭露形成呼應。

> Masters K, et al. *Med Teach*. 2025. [10.1080/0142159X.2024.2445037](https://doi.org/10.1080/0142159X.2024.2445037)

---

<!-- _class: divider -->
# AMEE Guide No. 190
## AI 於教育共創（2026）

---

# AMEE 190｜把 AI 用在「共創」的全流程

**Co-creation** = 學生、教師與其他關鍵利害關係人的實質協作，
目標是整合多元觀點、培養參與感、動機與**擁有感（ownership）**。

**問題**：共創在實務上會遇到**人際、實務、機構**三層挑戰，
需要可行的**逐步計畫**。

**AI 可介入的三個階段與七項任務**

```text
準備 (preparation)   → 招募多元參與者、設計與規劃共創活動
執行 (conduction)    → 腦力激盪、共享決策
後續 (follow-up)     → 過程評估、成果傳播、整合入課程
```

---

# AMEE 190｜兩個理論框架

這份指引最有價值的地方在於它**不只給操作步驟，還給了分析工具**：

| 框架 | 全稱 | 用途 |
|------|------|------|
| **SAMR** | Substitution, Augmentation, Modification, Redefinition | 檢視 AI 是「取代」既有做法，還是**根本重塑**它 |
| **TOE** | Technology-Organization-Environment | 從技術、組織、環境三層面分析導入條件 |

> **關鍵提醒**：指引特別強調要
> **「保留共創的關係本質（relational essence）」** ——
> AI 用來促進協作，不是取代人與人之間的關係。

> Suliman S, et al. *Med Teach*. 2026. [10.1080/0142159X.2025.2581163](https://doi.org/10.1080/0142159X.2025.2581163)

---

<!-- _class: divider -->
# AMEE Guide No. 192
## 學術發表中的 AI 揭露（2026）

---

# AMEE 192｜這份跟你投稿直接相關

**問題意識**：GenAI 已廣泛整合進研究與學術寫作，
但**未揭露的 GenAI 使用已被大量記錄**，可能損害研究誠信。

**負責任使用的五個面向**

| 面向 | 內容 |
|------|------|
| **Authorship** | AI 能不能掛名？（答案是不能） |
| **Verification and responsibility** | 誰負責查證 AI 產出的正確性 |
| **Plagiarism and bias** | 抄襲與偏誤風險 |
| **Data privacy and confidentiality** | 把未發表資料貼進 AI 的風險 |
| **Journal requirements** | 各期刊規定不一，必須逐一確認 |

---

# AMEE 192｜揭露的兩個層次

**內部揭露（internal disclosure）**
在**研究團隊內部**說清楚誰用了什麼 AI、用在哪一步。

**外部揭露（external disclosure）**
對**期刊與讀者**揭露。指引強調要留意**各期刊的個別規定**。

**核心原則**

> **坦誠描述 GenAI 是如何被使用的（candid description）**，
> 讓讀者能夠理解：**這個模型如何形塑了研究與寫作的過程**。

指引也簡短討論了**同儕審查（peer review）中使用 GenAI** 的問題。

> ⚠️ 作者自陳：撰寫時間為 **2025 年 11 月**，
> AI 揭露仍有許多未解問題，指引以未來展望作結。

> Cleland J, et al. *Med Teach*. 2026. [10.1080/0142159X.2025.2607513](https://doi.org/10.1080/0142159X.2025.2607513)

---

<!-- _class: divider -->
# 綜合與應用

---

# 七份指引的共同訊息

**1. 全部都把「倫理」放在核心位置**
不是附錄，而是主軸 —— 158 專章、178 有倫理節、192 全篇談誠信、BEME 84 明白呼籲。

**2. 全部強調「以教學理論為本」而非技術驅動**
AMEE 178 講得最直接：impetus 是 AI，但路徑扎根在 pedagogy。

**3. 全部指向「師資培育」是瓶頸**
教師若不懂 AI，指引寫得再好也落不了地。

**4. 實證基礎仍然薄弱**
BEME 84 檢視 278 篇後的結論是「需要持續研究以探索未知領域」。

> **對讀者最實用的一句話**：
> 這七份指引提供的是**框架與提問**，不是現成答案。

---

# 延伸：同系列的鄰近指引

雖然不以 AI 為主題，但關係密切：

| 指引 | 年份 | 主題 | 連結 |
|------|------|------|------|
| AMEE 134 | 2020 | 醫學教育數位學術的倫理 | [10.1080/0142159X.2019.1695043](https://doi.org/10.1080/0142159X.2019.1695043) |
| AMEE 161 | 2023 | 線上學習（一）：線上環境的教與學 | [10.1080/0142159X.2023.2197135](https://doi.org/10.1080/0142159X.2023.2197135) |
| AMEE 163 | 2024 | 線上學習（二）：工具與實務應用 | [10.1080/0142159X.2023.2259069](https://doi.org/10.1080/0142159X.2023.2259069) |
| AMEE 154 | 2023 | 行動科技支援 WBA 的委任決策 | [10.1080/0142159X.2023.2168527](https://doi.org/10.1080/0142159X.2023.2168527) |
| AMEE 174 | 2025 | Programmatic assessment for learning | [10.1080/0142159X.2024.2409936](https://doi.org/10.1080/0142159X.2024.2409936) |
| AMEE 189 | 2026 | 形成性評量與回饋實務指引 | [10.1080/0142159X.2025.2569623](https://doi.org/10.1080/0142159X.2025.2569623) |

> AMEE 134（2020）是 Masters 在 AI 系列之前就寫的數位倫理指引 —— 這條線索其實從六年前就開始了。

---

# 對台灣醫學教育的三個機會

**1. 地域代表性的缺口就是投稿機會**

> BEME 84：**68% 文獻來自北美與歐洲**。
> 亞洲的實證嚴重不足 —— 台灣的資料有國際價值。

**2. 用 FACETS 框架設計研究，提高被引用機率**
BEME 84 提出 FACETS 就是為了讓研究可比較、可整合。
從一開始就照框架報告，比事後補強有效。

**3. 評量改革有現成的官方依據**
要在院內推動 AI 相關的評量調整時，
**AMEE Guide 178 是可以直接引用的權威依據** —— 這在說服層級時很有用。

---

# 若只讀一份 / 三份 / 全部

**只讀一份** → **AMEE 178**（評量）
最貼近日常教學，且以教學理論為本，不會過時。

**讀三份** → **BEME 84** + **AMEE 178** + **AMEE 158**
= 全局地圖 + 教學實務 + 倫理底線

**要做研究** → 加 **AMEE 156**（方法）+ **AMEE 192**（揭露）

**要看長線** → 加 **AMEE 172**（AGI）+ **AMEE 190**（共創）

> 七份合計約 100 頁，但**彼此重疊不多**，
> 因為它們是刻意分工的系列，不是各自為政的論文。

---

<!-- _class: small-text -->
# 參考文獻

1. Tolsgaard MG, et al. The fundamentals of Artificial Intelligence in medical education research: AMEE Guide No. 156. [*Med Teach*. 2023;45(6):565-573.](https://doi.org/10.1080/0142159X.2023.2180340) PMID 36862064
2. Masters K. Ethical use of Artificial Intelligence in Health Professions Education: AMEE Guide No. 158. [*Med Teach*. 2023;45(6):574-584.](https://doi.org/10.1080/0142159X.2023.2186203) PMID 36912253
3. Gordon M, et al. A scoping review of artificial intelligence in medical education: BEME Guide No. 84. [*Med Teach*. 2024;46(4):446-470.](https://doi.org/10.1080/0142159X.2024.2314198) PMID 38423127
4. Masters K, et al. Preparing for Artificial General Intelligence (AGI) in Health Professions Education: AMEE Guide No. 172. [*Med Teach*. 2024.](https://doi.org/10.1080/0142159X.2024.2387802) PMID 39115700
5. Masters K, et al. Artificial Intelligence in Health Professions Education assessment: AMEE Guide No. 178. [*Med Teach*. 2025.](https://doi.org/10.1080/0142159X.2024.2445037) PMID 39787028
6. Suliman S, et al. The role of artificial intelligence in co-creation of health professions education: AMEE Guide No. 190. [*Med Teach*. 2026.](https://doi.org/10.1080/0142159X.2025.2581163) PMID 41241925
7. Cleland J, et al. When and how to disclose AI use in academic publishing: AMEE Guide No. 192. [*Med Teach*. 2026.](https://doi.org/10.1080/0142159X.2025.2607513) PMID 41467560

**延伸指引**

8. Masters K. Ethics in medical education digital scholarship: AMEE Guide No. 134. [*Med Teach*. 2020.](https://doi.org/10.1080/0142159X.2019.1695043) PMID 31835957
9. MacNeill H, et al. Online learning in HPE Part 1: AMEE Guide No. 161. [*Med Teach*. 2024.](https://doi.org/10.1080/0142159X.2023.2197135) PMID 37094079
10. Masters K, et al. Online learning in HPE Part 2: AMEE Guide No. 163. [*Med Teach*. 2024.](https://doi.org/10.1080/0142159X.2023.2259069) PMID 37740948
11. Marty AP, et al. Mobile technologies to support workplace-based assessment for entrustment decisions: AMEE Guide No. 154. [*Med Teach*. 2023.](https://doi.org/10.1080/0142159X.2023.2168527) PMID 36706225
12. Torre D, et al. Programmatic assessment for learning: AMEE Guide No. 174. [*Med Teach*. 2025.](https://doi.org/10.1080/0142159X.2024.2409936) PMID 39368061

---

<!-- _class: small-text -->
# 縮寫對照表與資料來源

| 縮寫 | 全名 | 中文 |
|------|------|------|
| AGI | Artificial General Intelligence | 通用人工智慧 |
| AMEE | Association for Medical Education in Europe | 歐洲醫學教育學會 |
| BEME | Best Evidence Medical Education | 實證醫學教育（合作組織） |
| FACETS | （BEME 84 提出之報告框架） | 高效用報告框架 |
| GenAI | Generative Artificial Intelligence | 生成式人工智慧 |
| GME | Graduate Medical Education | 畢業後醫學教育 |
| HPE | Health Professions Education | 健康專業教育 |
| SAMR | Substitution, Augmentation, Modification, Redefinition | 科技融入四層次模型 |
| STORIES | Structured approach to the Reporting of systematic reviews | 系統性回顧報告標準 |
| TOE | Technology-Organization-Environment | 技術–組織–環境框架 |
| UME | Undergraduate Medical Education | 大學部醫學教育 |
| WBA | Workplace-Based Assessment | 工作場域評量 |

**資料來源**：本簡報所有內容整理自各指引之 PubMed 摘要（檢索日 2026-08-23），
經翻譯、歸納與詮釋；**未閱讀各指引全文**。完整論述請參閱原文。

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

七份 AMEE / BEME 官方 AI 指引導讀

> 本簡報內容整理自各指引之 PubMed 摘要，未閱讀全文
> 僅供醫療專業人員教學與研究參考
