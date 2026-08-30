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
  /* 深底投影片的 footer 與頁碼必須夠亮 */
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
    font-size: 2.3em;
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
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.5em; }
  h2 { color: #0072bc; font-size: 1.1em; }
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
    font-size: 0.6em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.78em; }
  section.small-text table { font-size: 0.55em; }
  ul, ol { font-size: 0.92em; }
footer: '謝慕揚 MD, PhD, FESC | AMEE 2026 會前工作坊文獻回顧 | 2026'
---

<!-- _class: lead -->
# AMEE 2026 會前工作坊
## 主題文獻回顧 2021–2026

**謝慕揚 MD, PhD, FESC** | 2026-08-23

九場工作坊 · 95 篇文獻 · 全數經 PubMed 查證

> 檢索資料庫：PubMed（NCBI E-utilities），檢索日 2026-08-23
> 本文為敘述性回顧（narrative review），非系統性回顧

---

# 九場工作坊總覽

| 場次 | 主題 | 地點 |
|------|------|------|
| PCW 22 | Making Learning Visible：SSETT UP / POWER | Room 0.49-50, L0 |
| PCW 21 | Find Your Momentum：Kegan 框架職涯教練 | Room 0.11-12, L0 |
| PCW 19 | AI Chatbots 與臨床同理心（成大團隊） | Room 2.15, L2 |
| PCW 20 | Professional Identity Formation 與 belonging | Room 2.31, L2 |
| PCW 23 | Longitudinal Qualitative Research 方法學 | Room 2.17, L2 |
| PCW 24 | Future Literacy：與模糊性共處 | Room 2.95, L2 |
| AMEE AI | Beyond Cheating：AI 與評量（€135） | Hall F, L0 |
| ESME | Mixed Methods Research 入門（€135） | Room 2.44, L2 |
| 行事曆 | How Students Use AI（09:30–12:30） | R2.15 |

---

# 核心觀察：九場其實是三個群集

```text
【可視化群集】          【AI 群集】            【方法學群集】
PCW 22 督導可視化        PCW 19 AI 與同理心      PCW 23 縱貫質性研究
PCW 20 認同與歸屬        AMEE AI 評量重構        ESME 混合方法
PCW 21 教練與轉換        R2.15 學生 AI 使用
      ↓                     ↓                      ↓
 把隱性變可見          把工具變教學設計       把「變化」變可研究
```

> **PCW 24（模糊性）是貫穿三者的底層能力** —— 無論督導、用 AI 還是做質性研究，核心都是與不確定性共處。

---

# 文獻成熟度盤點

| 主題 | 文獻成熟度 | 說明 |
|------|-----------|------|
| 臨床督導 / WBA | **高** | 成熟且持續產出 |
| PIF 與 belonging | **高** | 已進入概念整合期 |
| AI 與評量 | **高** | 已有 AMEE Guide 178 / 156、BEME 84 |
| 混合方法 | **高** | 教學型文獻齊備 |
| Uncertainty tolerance | **高** | 理論辯論正激烈 |
| AI 與同理心 | **中高** | 2023 後爆發，RCT 開始出現 |
| LQR 方法學 | **中** | 近兩年快速建制化 |
| 學生 AI 使用 | **中** | 多為橫斷面問卷 |
| Kegan 框架 / Futures Literacy | **低** | PubMed 幾乎查無實證 |

---

<!-- _class: divider -->
# PCW 22
## 臨床督導與工作場域學習可視化

---

# PCW 22｜主題定位與誠實聲明

**核心問題**：臨床工作中大量學習是隱性的 —— 學習者做了什麼、成長到哪裡，督導者往往說不清楚。

> ⚠️ **`SSETT UP` 與 `POWER` 在 PubMed 檢索不到同名文獻**
> 很可能是講者自行發展、尚未正式發表，或發表於 PubMed 未索引的來源。
> 以下回顧的是其**所屬的研究傳統**，而非這兩個框架本身。
> 建議會前直接向講者索取原始出處。

---

# PCW 22｜近五年五條主軸

1. **從「評量學習」轉向「評量促進學習」**
   WBA 設計初衷是引導學習，實務上常淪為打勾作業

2. **回饋是「過程」而非「事件」**
   需要刻意設計的 feedback process，而非單次對話

3. **督導中的自主性張力**
   監督過度會壓抑自主性（self-determination theory 視角）

4. **Failure to fail 的持續困境**
   評分者「不敢當人」是可視化最大的敵人

5. **可視化的實作嘗試**
   ICU 訓練結合協作 + 進度可視化 + 教練

---

# PCW 22｜代表文獻

| 年份 | 期刊 | 核心貢獻 | 連結 |
|------|------|---------|------|
| 2023 | *Med Educ* | WBA 如何引導研究所階段學習 | [10.1111/medu.14960](https://doi.org/10.1111/medu.14960) |
| 2024 | *BMC Med Educ* | 工作場域學習的回饋流程設計 | [10.1186/s12909-024-05439-6](https://doi.org/10.1186/s12909-024-05439-6) |
| 2022 | *Med Educ* | 用自我決定理論重構督導與自主性 | [10.1111/medu.14580](https://doi.org/10.1111/medu.14580) |
| 2024 | *BMC Med Educ* | ICU 訓練的進度可視化與教練式評量 | [10.1186/s12909-023-04980-0](https://doi.org/10.1186/s12909-023-04980-0) |
| 2023 | *BMC Med Educ* | 臨床督導中的微管理 | [10.1186/s12909-023-04543-3](https://doi.org/10.1186/s12909-023-04543-3) |
| 2023 | *BMC Med Educ* | 評分者不適感與 failure to fail | [10.1186/s12909-023-04688-1](https://doi.org/10.1186/s12909-023-04688-1) |
| 2025 | *Pediatrics* | 住院醫師畢業時的獨立執業準備度 | [10.1542/peds.2024-070307](https://doi.org/10.1542/peds.2024-070307) |

---

<!-- _class: divider -->
# PCW 21
## 職涯教練與角色轉換

---

# PCW 21｜主題定位與誠實聲明

以 Robert Kegan 的**成人發展理論**（constructive-developmental theory；主體–客體轉換、self-authorship）處理角色轉換困境。

> ⚠️ **以 `Kegan` 檢索在醫學教育核心期刊幾乎查無實證研究**
> Kegan 理論在醫學教育多以**理論借用**形式出現（常見於 transformative learning 文獻），而非獨立研究主題。
> 下列為其鄰近領域文獻。

---

# PCW 21｜近五年五條主軸

1. **Coaching 已從概念走向操作化**
   定義基礎（2021）→ clinician educator（2023）→ coaching mindset（2026）

2. **Transformative learning 是 Kegan 最接近的實證出口**
   Vipler 的 scoping review 是理解 Kegan 框架的入口

3. **轉換期研究焦點在「支持結構」**
   困難不是能力不足，而是**身份與期待的重組**

4. **Precision education 提供系統層次想像**
   資料驅動、個別化的終身學習路徑

5. **教練對「教練者」本身也有發展效果**
   指導住院醫師反過來形塑主治醫師的專業認同 → 連到 PCW 20

---

# PCW 21｜代表文獻

| 年份 | 期刊 | 核心貢獻 | 連結 |
|------|------|---------|------|
| 2021 | *Acad Med* | 醫學教育中「教練」的定義與框架 | [10.1097/ACM.0000000000004168](https://doi.org/10.1097/ACM.0000000000004168) |
| 2021 | *J Grad Med Educ* | GME 中的轉化學習：scoping review | [10.4300/JGME-D-21-00065.1](https://doi.org/10.4300/JGME-D-21-00065.1) |
| 2023 | *J Grad Med Educ* | 臨床教師的教練技能 | [10.4300/JGME-D-23-00071.1](https://doi.org/10.4300/JGME-D-23-00071.1) |
| 2024 | *Acad Med* | Precision Education：終身學習的未來 | [10.1097/ACM.0000000000005601](https://doi.org/10.1097/ACM.0000000000005601) |
| 2023 | *Acad Med* | 教練經驗如何形塑教練者自身認同 | [10.1097/ACM.0000000000005011](https://doi.org/10.1097/ACM.0000000000005011) |
| 2025 | *Med Educ* | 縱貫式學生回饋與教練整合於實習 | [10.1111/medu.15666](https://doi.org/10.1111/medu.15666) |
| 2026 | *Med Educ* | When I say … a coaching mindset | [10.1111/medu.70048](https://doi.org/10.1111/medu.70048) |

---

<!-- _class: divider -->
# PCW 19
## AI Chatbots 與臨床同理心

---

# PCW 19｜觸發整個領域的關鍵發現

**Ayers JW, et al. *JAMA Intern Med*. 2023;183(6):589-596.**

比較醫師與 chatbot 回覆病人提問 —— 評審者認為 **chatbot 回覆的品質與同理心評分較高**。

> ⚠️ **必須注意其設計限制**
> 社群論壇文字、非真實臨床關係、盲評者非病人本人。
> 這篇是後續所有討論的起點，但不等於「AI 比醫師有同理心」。

⚠️ 另：本次檢索未能在 PubMed 明確定位**成大團隊**在此主題的代表著作，建議取得講者名單後以作者檢索補齊。

---

# PCW 19｜研究焦點已經轉向

**從「AI 有沒有同理心」→「AI 能不能訓練人的同理心」**

主流已轉為把 LLM 當作**可規模化的模擬病人**：

- **Holderried 2024** — LLM 模擬病人 + 自動回饋用於問診訓練
- **Yamamoto 2024** — 非隨機對照試驗，AI 模擬病人提升問診技巧
- **Wang 2025** — **隨機對照試驗**驗證 GPT 問診訓練可行性
- **Luo 2025**（*npj Digit Med*）— 眼科數位病人系統

**Cook 2025 的關鍵論點**：用 LLM 建虛擬病人「scalable, global, and low cost」
→ 成本結構改變了，這對資源有限地區最重要

---

# PCW 19｜代表文獻

| 年份 | 期刊 | 核心貢獻 | 連結 |
|------|------|---------|------|
| 2023 | *JAMA Intern Med* | Chatbot vs 醫師回覆的品質與同理心 | [10.1001/jamainternmed.2023.1838](https://doi.org/10.1001/jamainternmed.2023.1838) |
| 2024 | *JMIR Med Educ* | LLM 模擬病人 + 自動回饋 | [10.2196/59213](https://doi.org/10.2196/59213) |
| 2024 | *JMIR Med Educ* | AI 模擬病人提升問診技巧（非隨機） | [10.2196/58753](https://doi.org/10.2196/58753) |
| 2025 | *BMC Med Educ* | GPT 問診訓練**隨機對照試驗** | [10.1186/s12909-025-07614-9](https://doi.org/10.1186/s12909-025-07614-9) |
| 2025 | *npj Digit Med* | LLM 數位病人提升眼科問診技巧 | [10.1038/s41746-025-01841-6](https://doi.org/10.1038/s41746-025-01841-6) |
| 2023 | *J Med Internet Res* | AI 支援溝通技巧訓練：scoping review | [10.2196/43311](https://doi.org/10.2196/43311) |
| 2025 | *Med Teach* | LLM 虛擬病人：可規模化、低成本 | [10.1080/0142159X.2024.2376879](https://doi.org/10.1080/0142159X.2024.2376879) |

---

# PCW 19｜風險文獻不可略過

教學設計必須把風險討論納入：

| 年份 | 期刊 | 風險議題 | 連結 |
|------|------|---------|------|
| 2025 | *JMIR Ment Health* | Chatbot 互動引發妄想經驗（"AI psychosis"） | [10.2196/85799](https://doi.org/10.2196/85799) |
| 2023 | *J Med Internet Res* | ChatGPT 於醫療的倫理考量 | [10.2196/48009](https://doi.org/10.2196/48009) |
| 2025 | *Nature* | 對話式診斷 AI（AMIE）的能力與邊界 | [10.1038/s41586-025-08866-7](https://doi.org/10.1038/s41586-025-08866-7) |

> 同理心的「表現」與「存在」是兩件事。
> LLM 能產出被評為有同理心的文字，不代表臨床關係中的同理心可被取代。

---

<!-- _class: divider -->
# PCW 20
## Professional Identity Formation 與 Belonging

---

# PCW 20｜近五年五條主軸

1. **概念整合期已到來**
   Sarraf-Yazdi（2024）整合框架 + Cornett（2023）跨專業 scoping review
   → 從百家爭鳴走向共識

2. **批判轉向（critical turn）**
   系譜學挑戰「認同」預設：**誰的認同？誰被排除在外？**

3. **縱貫關係是 PIF 的載體**
   LIC 與長期師徒關係特別有利於 PIF → 直通 PCW 23

4. **教師的自我揭露與脆弱性**
   歸屬感往往來自「看見對方也是人」

5. **認同的延伸場域**
   從基礎醫學 → 跨專業教育 → allied health

---

# PCW 20｜代表文獻

| 年份 | 期刊 | 核心貢獻 | 連結 |
|------|------|---------|------|
| 2024 | *Acad Med* | PIF 的概念化整合框架 | [10.1097/ACM.0000000000005559](https://doi.org/10.1097/ACM.0000000000005559) |
| 2023 | *Adv Health Sci Educ* | 健康專業的專業認同：scoping review | [10.1007/s10459-022-10171-1](https://doi.org/10.1007/s10459-022-10171-1) |
| 2022 | *Adv Health Sci Educ* | 重思「認同」：系譜學視角 | [10.1007/s10459-022-10095-w](https://doi.org/10.1007/s10459-022-10095-w) |
| 2021 | *Med Educ* | 縱貫整合式實習中的 PIF | [10.1111/medu.14461](https://doi.org/10.1111/medu.14461) |
| 2024 | *Acad Med* | 臨床教師自我揭露疾病經驗 | [10.1097/ACM.0000000000005583](https://doi.org/10.1097/ACM.0000000000005583) |
| 2024 | *BMC Med Educ* | 長期師徒關係與新手教師認同 | [10.1186/s12909-024-06206-3](https://doi.org/10.1186/s12909-024-06206-3) |
| 2024 | *BMC Med Educ* | 冒牌者現象的教育介入 | [10.1186/s12909-023-04984-w](https://doi.org/10.1186/s12909-023-04984-w) |

---

<!-- _class: divider -->
# PCW 23
## Longitudinal Qualitative Research 方法學

---

# PCW 23｜為什麼現在才被系統化？

**LQR** = 在多個時間點反覆收集同一群人的質性資料，
捕捉「**變化如何發生**」而非「某時點的樣貌」。

> **Balmer 2021《Time to conceptualise time》是分水嶺**
> 主張醫學教育研究長期把「時間」當成背景變項，而非分析對象。

**2025 年出現實作指引雙篇**（Gordon 等人，*Clin Teach*）：
- 一篇談 LQR 的**獨特可能性**
- 一篇是**如何實際操作**的入門指引

→ 這兩篇是工作坊前最該先讀的

---

# PCW 23｜代表文獻

| 年份 | 期刊 | 核心貢獻 | 連結 |
|------|------|---------|------|
| 2021 | *Med Educ* | LQR 在醫學教育：把「時間」概念化 | [10.1111/medu.14542](https://doi.org/10.1111/medu.14542) |
| 2025 | *Clin Teach* | LQR 在健康專業教育的獨特可能性 | [10.1111/tct.70126](https://doi.org/10.1111/tct.70126) |
| 2025 | *Clin Teach* | 如何實際執行 LQR：操作指引 | [10.1111/tct.70211](https://doi.org/10.1111/tct.70211) |
| 2022 | *BMC Med Res Methodol* | 健康研究中的 LQR：method study | [10.1186/s12874-022-01732-4](https://doi.org/10.1186/s12874-022-01732-4) |
| 2024 | *Meth Psychol* | 用 LQR 理解被邊緣化族群的經驗 | [10.1016/j.metip.2023.100130](https://doi.org/10.1016/j.metip.2023.100130) |
| 2022 | *Int J Nurs Stud* | 中風照顧者出院轉銜（LQR 範例） | [10.1016/j.ijnurstu.2022.104213](https://doi.org/10.1016/j.ijnurstu.2022.104213) |

> **與 PCW 20 直接串接**：LQR 特別適合理解少數族群的經驗變化 → belonging 議題

---

<!-- _class: divider -->
# PCW 24
## Future Literacy 與模糊性共處

---

# PCW 24｜主題定位與誠實聲明

Future Literacy 是 **UNESCO 推廣的概念**（有能力想像多重未來、避免被單一預設綁架）。

> ⚠️ **Futures Literacy 在 PubMed 幾乎沒有醫學教育實證文獻**
> 屬 UNESCO／教育學／未來學傳統，PubMed 覆蓋極差。
> 相對地 **uncertainty tolerance (UT) 文獻極為成熟**。
> 本節以 UT 為主軸，並補充醫學教育中少數的情境規劃研究。

---

# PCW 24｜這是近五年最有張力的理論辯論

**三方交鋒：**

- **Ilgen 等人**：UT 是不是一個「**附帶現象**（epiphenomenon）」？
- **Haas 與 Hancock**：「房間裡的大象」—— 概念定義根本混亂
- **Richmond**：UT 與臨床推理，孰因孰果？

**測量工具受到嚴格檢驗（重要警訊）：**

- Stephens 2023 系統性回顧 → 現有 UT 量表**效度證據普遍不足**
- Patel 2023「Weighing up the research」延續批判
- Lazarus 2025 提出量表發展新取徑

**迷思被推翻**：Wegwarth 2025 檢驗「UT 高低決定專科選擇」→ **是迷思**

---

# PCW 24｜代表文獻

| 年份 | 期刊 | 核心貢獻 | 連結 |
|------|------|---------|------|
| 2022 | *Med Educ* | UT 是附帶現象嗎？（理論挑戰） | [10.1111/medu.14938](https://doi.org/10.1111/medu.14938) |
| 2022 | *Med Educ* | 對 UT 的不確定：房間裡的大象 | [10.1111/medu.14926](https://doi.org/10.1111/medu.14926) |
| 2023 | *Med Educ* | UT 量表效度證據的系統性回顧 | [10.1111/medu.15014](https://doi.org/10.1111/medu.15014) |
| 2022 | *Med Educ* | 提升醫學生 UT 的介入：scoping review | [10.1111/medu.14873](https://doi.org/10.1111/medu.14873) |
| 2024 | *Med Teach* | 培養學習者 UT 的十二個要訣 | [10.1080/0142159X.2024.2307500](https://doi.org/10.1080/0142159X.2024.2307500) |
| 2025 | *Med Educ* | UT 與專科選擇：迷思再檢驗 | [10.1111/medu.15610](https://doi.org/10.1111/medu.15610) |
| 2023 | *JMIR Med Educ* | AI 醫學教育的**四種未來世界**（情境規劃） | [10.2196/50373](https://doi.org/10.2196/50373) |

---

<!-- _class: divider -->
# AMEE AI
## Beyond Cheating：AI 與評量

---

# AMEE AI｜官方指引已到位，這是必讀起點

| 指引 | 年份 | 內容 | 連結 |
|------|------|------|------|
| **AMEE Guide No. 178** | 2025 | AI 在健康專業教育**評量**的應用 —— 與本工作坊完全對應 | [10.1080/0142159X.2024.2445037](https://doi.org/10.1080/0142159X.2024.2445037) |
| **AMEE Guide No. 156** | 2023 | AI 於醫學教育**研究**的基礎 | [10.1080/0142159X.2023.2180340](https://doi.org/10.1080/0142159X.2023.2180340) |
| **BEME Guide No. 84** | 2024 | AI 在醫學教育的 scoping review | [10.1080/0142159X.2024.2314198](https://doi.org/10.1080/0142159X.2024.2314198) |

**起點事件**：Gilson 等人證實 ChatGPT 通過 USMLE
→ 直接動搖以知識回憶為主的評量效度

---

# AMEE AI｜「作弊」的定義本身在鬆動

**Kazley AS, et al. *Med Teach*. 2025** — 直接問學生「用 ChatGPT 算不算作弊」

→ **學生的認知與教師存在明顯落差**。這正是 "Beyond Cheating" 的核心。

**系統性證據開始收斂，但結論並不樂觀：**

> Pham 2025（*Med Educ*）與 Feigerlova 2025 的系統性回顧共同指出：
> **對學習成效的實證仍薄弱** —— 多數研究為短期、單中心、自評結果。

**仍存在的缺口**：Weidener 的 scoping review 指出
**AI 倫理教學在課程中嚴重不足**

---

# AMEE AI｜代表文獻

| 年份 | 期刊 | 核心貢獻 | 連結 |
|------|------|---------|------|
| 2023 | *JMIR Med Educ* | ChatGPT 在 USMLE 的表現與評量意涵 | [10.2196/45312](https://doi.org/10.2196/45312) |
| 2024 | *Acad Med* | 生成式 AI 的潛在衝擊與機會 | [10.1097/ACM.0000000000005439](https://doi.org/10.1097/ACM.0000000000005439) |
| 2025 | *Acad Med* | Macy 基金會報告：AI 於醫學教育全景 | [10.1097/ACM.0000000000006107](https://doi.org/10.1097/ACM.0000000000006107) |
| 2025 | *Med Educ* | 生成式 AI 對學生學習影響：系統性回顧 | [10.1111/medu.15746](https://doi.org/10.1111/medu.15746) |
| 2025 | *BMC Med Educ* | AI 對教育成效影響：系統性回顧 | [10.1186/s12909-025-06719-5](https://doi.org/10.1186/s12909-025-06719-5) |
| 2025 | *Med Teach* | 用 ChatGPT 算作弊嗎？學生的認知 | [10.1080/0142159X.2024.2385667](https://doi.org/10.1080/0142159X.2024.2385667) |
| 2023 | *Perspect Med Educ* | 醫學教育中的 AI 倫理教學 | [10.5334/pme.954](https://doi.org/10.5334/pme.954) |

---

<!-- _class: divider -->
# ESME
## Mixed Methods Research

---

# ESME｜MMR 的罩門就是「整合」

**混合方法不是「同時做問卷和訪談」**，
而是刻意設計質量整合，回答單一方法無法回答的問題。

> **O'Sullivan 2024《Avoiding common pitfalls》直指最常見的失敗：**
> 質量兩部分各做各的，**從未真正整合（缺乏 integration）**。
> 這是審稿最常退件的理由。

**後設研究揭露實作品質不佳**：
Alhassan 2024 分析發現，許多研究自稱 mixed methods 但未達方法學標準。

**MMR 正被用於最新議題**：
Kassab 2025 用 MMR 研究「AI 時代醫學生如何學習」
→ 同時橫跨 ESME 與 R2.15 兩場工作坊，優先閱讀

---

# ESME｜代表文獻

| 年份 | 期刊 | 核心貢獻 | 連結 |
|------|------|---------|------|
| 2023 | *Med Teach* | 混合方法研究設計（入門教學） | [10.1080/0142159X.2023.2200118](https://doi.org/10.1080/0142159X.2023.2200118) |
| 2024 | *Adv Health Sci Educ* | **避開混合方法的常見陷阱** | [10.1007/s10459-024-10362-y](https://doi.org/10.1007/s10459-024-10362-y) |
| 2024 | *Med Teach* | 混合方法在醫學教育研究的重要性 | [10.1080/0142159X.2024.2373877](https://doi.org/10.1080/0142159X.2024.2373877) |
| 2024 | *BMC Med Educ* | 醫學教育中 MMR 應用的質性分析 | [10.1186/s12909-024-05242-3](https://doi.org/10.1186/s12909-024-05242-3) |
| 2025 | *BMC Med Educ* | AI 時代醫學生如何學習（MMR 範例） | [10.1186/s12909-025-08145-z](https://doi.org/10.1186/s12909-025-08145-z) |
| 2024 | *BMC Med Educ* | 弱勢族群在骨科訓練的歸屬感 | [10.1186/s12909-024-05568-y](https://doi.org/10.1186/s12909-024-05568-y) |

---

<!-- _class: divider -->
# R2.15
## 學生如何使用 AI

---

# R2.15｜視角翻轉

前八場關注「**教師怎麼用 AI**」，這場問：
**學生實際上在怎麼用？教育者能不能順勢引導？**

**2023–2026 累積大量跨國調查**（阿聯、泰國、中國、波蘭、巴勒斯坦、牙醫多國）

共同發現：
- 使用率高、態度正向
- **但對侷限性的認識不足**
- **幾乎沒有正式訓練**

> **Hack 等人 2026（*Clin Teach*）的標題就是結論：**
> **"Students Are Ready for AI—But Is Medical Education?"**

---

# R2.15｜研究焦點正在轉移

**從「態度調查」→「學習歷程研究」**

- **Kassab 2025** — 混合方法探討 AI 如何改變學習方式
- **Thomae 2024** — 把 ChatGPT 整合進正式課程並觀察使用情境

**依賴性（dependency）成為新焦點**

- **Alhur 2025**（*JMIR Med Educ*）— AI 依賴的悖論（質性研究）
- 延伸至**認知卸載（cognitive offloading）**的疑慮

**護理與牙醫走得比醫學系快**
Khlaif、Tseng、Kavadella 的研究顯示這兩個領域在 AI 素養課程化上進度領先

---

# R2.15｜代表文獻

| 年份 | 期刊 | 核心貢獻 | 連結 |
|------|------|---------|------|
| 2026 | *Clin Teach* | **學生準備好了，但醫學教育呢？** | [10.1111/tct.70313](https://doi.org/10.1111/tct.70313) |
| 2023 | *JMIR Med Educ* | 醫學生對 ChatGPT 與 AI 的經驗與認知 | [10.2196/51302](https://doi.org/10.2196/51302) |
| 2023 | *JMIR Med Educ* | 醫學生與醫師對 ChatGPT 的認知比較 | [10.2196/50658](https://doi.org/10.2196/50658) |
| 2024 | *JMIR Med Educ* | 將 ChatGPT 整合入課程 | [10.2196/50545](https://doi.org/10.2196/50545) |
| 2025 | *JMIR Med Educ* | AI 依賴的悖論：教育者質性研究 | [10.2196/74947](https://doi.org/10.2196/74947) |
| 2025 | *BMC Med Educ* | AI 於大學部醫學教育：更新版回顧 | [10.1186/s12909-025-08188-2](https://doi.org/10.1186/s12909-025-08188-2) |
| 2026 | *BMC Med Educ* | 牙醫學生 AI 知識與教育需求（多國） | [10.1186/s12909-026-08699-6](https://doi.org/10.1186/s12909-026-08699-6) |

---

<!-- _class: divider -->
# 綜合觀察

---

# 四個反覆出現的警訊

| 警訊 | 出處 | 對你的意義 |
|------|------|-----------|
| **測量工具效度不足** | UT 量表系統性回顧（Stephens 2023、Patel 2023） | 要做問卷研究，先查該量表的效度證據 |
| **AI 研究多為短期單中心自評** | Pham 2025、Feigerlova 2025 | 投稿最易被批評之處，也是研究缺口 |
| **混合方法缺乏真正整合** | O'Sullivan 2024、Alhassan 2024 | 設計階段就要寫清楚 integration 在哪 |
| **Failure to fail 依然普遍** | Dixon 2022、Scarff 2023 | 可視化工具若不解決評分者心理，效果有限 |

---

# 會前若只讀五篇

1. **Masters K, et al. AMEE Guide No. 178.** *Med Teach*. 2025
   AI 評量的官方立場 · [連結](https://doi.org/10.1080/0142159X.2024.2445037)

2. **Balmer DF, et al. Time to conceptualise time.** *Med Educ*. 2021
   LQR 的思想起點 · [連結](https://doi.org/10.1111/medu.14542)

3. **Sarraf-Yazdi S, et al. Conceptualizing PIF in Medicine.** *Acad Med*. 2024
   PIF 整合框架 · [連結](https://doi.org/10.1097/ACM.0000000000005559)

4. **Ilgen JS, et al. Is uncertainty tolerance an epiphenomenon?** *Med Educ*. 2022
   最有張力的理論辯論 · [連結](https://doi.org/10.1111/medu.14938)

5. **O'Sullivan P, et al. Avoiding common pitfalls in mixed methods.**
   *Adv Health Sci Educ*. 2024 · 直指設計罩門 · [連結](https://doi.org/10.1007/s10459-024-10362-y)

---

# 對心臟科臨床教學的可應用性

| 工作坊主題 | 可立即應用之處 |
|-----------|---------------|
| **PCW 22** 可視化 | 導管室 operator 訓練的 entrustment 分級與進度可視化 |
| **PCW 24** 模糊性 | 影像判讀與介入決策的不確定性教學（TEER/TAVI 適應症灰帶） |
| **PCW 20** 歸屬感 | 跨團隊（心臟科＋外科＋影像）成員的認同與歸屬 |
| **PCW 23** LQR | 追蹤 fellow 三年成長歷程的縱貫質性研究設計 |
| **ESME** MMR | 品質改善計畫（如急性腸缺血 QI）的質量整合評估 |

> 這五條都可以直接轉成研究題目 —— 而且都有現成的方法學指引可循。

---

# 檢索方法

**資料庫與範圍**

- PubMed（NCBI E-utilities API）｜檢索日 **2026-08-23**
- 時間範圍 **2021–2026**（AI 相關主題縮限為 2023–2026）
- 排序：relevance

**期刊限定（部分檢索）**

*Med Teach*、*Acad Med*、*Med Educ*、*Adv Health Sci Educ*、*Perspect Med Educ*、
*Teach Learn Med*、*BMC Med Educ*、*J Grad Med Educ*、*JMIR Med Educ*、*Clin Teach*

**引用查證**

> 所有 DOI 與 PMID 均取自 PubMed esummary 回傳值，**未經人工推測或補完**。
> 95 個 DOI 逐一測試解析：**0 個失效**。

---

# 六項明確限制（必讀）

1. **`SSETT UP` 與 `POWER` 在 PubMed 查無同名文獻**
   涵蓋的是其所屬研究傳統，非框架本身

2. **Kegan 的 constructive-developmental theory 在醫學教育缺乏實證研究**

3. **未能定位「成大團隊」在 AI 同理心主題的代表著作**

4. **Futures Literacy 屬 UNESCO／未來學傳統，PubMed 覆蓋極差**

5. **僅檢索 PubMed**
   醫學教育有相當比例發表於 ERIC、Scopus、Web of Science 收錄但 PubMed 未收之期刊

6. **本文為敘述性回顧（narrative review）**
   未做雙人篩選、未評讀偏差風險、未做 PRISMA 流程

---

<!-- _class: small-text -->
# 縮寫對照表

| 縮寫 | 全名 | 中文 |
|------|------|------|
| AMEE | Association for Medical Education in Europe | 歐洲醫學教育學會 |
| BEME | Best Evidence Medical Education | 實證醫學教育 |
| EPA | Entrustable Professional Activity | 可信賴專業活動 |
| ESME | Essential Skills in Medical Education | 醫學教育核心技能 |
| GME | Graduate Medical Education | 畢業後醫學教育 |
| HPE | Health Professions Education | 健康專業教育 |
| LIC | Longitudinal Integrated Clerkship | 縱貫整合式臨床實習 |
| LLM | Large Language Model | 大型語言模型 |
| LQR | Longitudinal Qualitative Research | 縱貫質性研究 |
| MMR | Mixed Methods Research | 混合方法研究 |
| PCW | Pre-Conference Workshop | 會前工作坊 |
| PIF | Professional Identity Formation | 專業認同形成 |
| SDT | Self-Determination Theory | 自我決定理論 |
| UT | Uncertainty Tolerance | 不確定性耐受度 |
| WBA | Workplace-Based Assessment | 工作場域評量 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

完整講義（95 篇文獻）：
`handouts/99-misc/AMEE_2026_Preconference_Workshops_Literature_Review 教學講義.md`

> 本簡報為敘述性文獻回顧，僅供醫療專業人員教學與研究參考
