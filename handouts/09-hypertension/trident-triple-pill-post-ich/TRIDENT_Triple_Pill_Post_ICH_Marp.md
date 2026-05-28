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
  section.lead h1 { color: #ffffff; font-size: 2.0em; }
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
    font-size: 2.4em;
    text-align: center;
  }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.68em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.86em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 0.65em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.78em; }
footer: '謝慕揚 MD, PhD, FESC | TRIDENT Trial — Triple Pill Post-ICH | 2026'
---

<!-- _class: lead -->

# Three Low-Dose Antihypertensive Agents in a Single Pill after Intracerebral Hemorrhage

## TRIDENT 試驗：腦出血後三合一低劑量降壓藥

**謝慕揚 MD, PhD, FESC**
資料來源：[N Engl J Med 2026;394:1571-82](https://doi.org/10.1056/NEJMoa2515043) | 2026-04-23

---

# 大綱

1. 研究背景與臨床問題
2. 試驗設計 (TRIDENT)
3. 病人特徵與血壓控制
4. 主要與次要結果
5. 安全性分析
6. 臨床意義與 Take Home Message

---

<!-- _class: divider -->

# 第一部分：研究背景

---

# 為何要做 TRIDENT？

- **自發性腦出血 (spontaneous ICH)** 致死率、致殘率極高
- **唯一被證實能預防初次與再發性 ICH 的療法 = 有效降壓**
- 實務問題：ICH 後病人長期血壓控制率低
  - 藥物順從性差
  - 治療惰性 (therapeutic inertia)
  - Guideline 建議不一致
- **假說**：一顆含 3 種低劑量降壓藥的單一藥丸（triple pill）可改善血壓控制並減少再發中風

---

# Triple Pill 配方

| 成分 | 劑量 | 機轉 |
|------|------|------|
| **Telmisartan** | 20 mg | ARB |
| **Amlodipine** | 2.5 mg | CCB |
| **Indapamide** | 1.25 mg | Thiazide-like diuretic |

> **核心概念**：每種藥物僅用 **次最大劑量以下**，利用三種不同機轉達到協同降壓，並降低單藥高劑量副作用

---

<!-- _class: divider -->

# 第二部分：試驗設計

---

# 研究設計

- **類型**：多國雙盲、隨機分派、placebo-controlled RCT
- **地點**：12 國、61 中心（含台灣 Linkou Chang Gung）
- **收案期**：2017-09-28 至 2024-11-30
- **追蹤**：中位數 2.5 年（IQR 1.6–4.4）
- **分析**：Intention-to-treat
- **登錄**：NCT02699645

---

# 納入與排除條件

| 類型 | 標準 |
|------|------|
| **納入** | 成人；曾發生自發性 ICH；臨床穩定；坐姿 SBP 130–160 mm Hg |
| **排除** | ACEI 無法替換；肝腎功能異常；對任一成分禁忌 |

### Run-in Phase（關鍵！）
- 所有人先服 2–4 週 triple pill
- 確認 ≥80% 順從性 + 無顯著 creatinine 上升
- **規管機關要求**：creatinine ↑≥20% 即排除

---

# 試驗流程

```text
2206 位篩選入 run-in phase (2–4 wk)
         ↓
  24.3% 因 creatinine↑ 或不耐受被排除
         ↓
1670 位隨機分派（1:1）
         ↓
  ┌──────────────┬──────────────┐
  Triple pill      Placebo
  (n=833)         (n=837)
         ↓
  追蹤中位數 2.5 年
  Primary endpoint: First recurrent stroke
```

---

# 研究終點

| 類型 | 終點 |
|------|------|
| **Primary** | First recurrent stroke (time-to-event) |
| **Key Secondary** | ①SBP <130 mm Hg at 6 mo；②Major CV event；③CV death |
| **Other** | Recurrent ICH、ischemic stroke、MI、all-cause death |
| **Safety** | SAE、AE of special interest（低血壓、AKI 等） |

---

<!-- _class: divider -->

# 第三部分：主要結果

---

# 病人基線特徵

| 特徵 | Triple Pill | Placebo |
|------|:----------:|:-------:|
| 年齡（歲） | 57.5±11.2 | 58.0±11.5 |
| 女性 | 33.0% | 34.4% |
| **亞裔** | **73.2%** | **72.0%** |
| 高血壓病史 | 80.1% | 81.2% |
| 糖尿病 | 21.7% | 22.5% |
| 深部 ICH | 78.4% | 75.9% |
| Hematoma 中位體積 (mL) | 12 | 11 |
| 基線 SBP (mm Hg) | 143±10 | 143±10 |
| 使用 ≥2 降壓藥 | 58.6% | 57.1% |

> **注意**：66.7% 病人來自 **斯里蘭卡 (Sri Lanka)**

---

# 血壓控制成效

| 時間點 | Triple Pill | Placebo | 差值 |
|--------|:----------:|:-------:|:----:|
| **追蹤期平均 SBP** | **127 mm Hg** | **138 mm Hg** | **−9 mm Hg** |
| 追蹤期平均 DBP | 82 mm Hg | 86 mm Hg | −4 mm Hg |
| **6 mo 時 SBP <130 mm Hg** | **49.9%** | **26.4%** | **OR 3.15** |

> **Pearl**：Placebo 組後期平均用 2.0 顆降壓藥（triple pill 組 1.2 顆），使兩組血壓差距逐漸縮小——triple pill 的獨立效應可能被低估

---

# 主要終點：再發中風

<!-- _class: small-text -->

| 終點 | Triple Pill | Placebo | HR (95% CI) | P |
|------|:----------:|:-------:|:-----------:|:-:|
| **Recurrent stroke**（主要） | 38 (4.6%) | 62 (7.4%) | **0.61 (0.41–0.92)** | **0.02** |
| Major CV event | 55 (6.6%) | 82 (9.8%) | 0.67 (0.47–0.94) | 0.04 |
| CV death | 17 (2.0%) | 25 (3.0%) | 0.67 (0.36–1.25) | 0.21 |
| **Recurrent ICH** | 15 (1.8%) | 37 (4.4%) | **0.40 (0.22–0.73)** | — |
| Ischemic stroke | 25 (3.0%) | 28 (3.3%) | 0.90 (0.52–1.54) | — |
| Fatal stroke | 3 (0.4%) | 12 (1.4%) | 0.25 (0.07–0.89) | — |
| All-cause death | 54 (6.5%) | 72 (8.6%) | 0.75 (0.53–1.07) | — |

> **NNT = 35** 位病人治療可預防一次再發中風

---

# 主要效益來自 ICH 預防

> **Pearl**：Triple pill 的效益 **主要由 recurrent ICH 大幅下降所驅動**（HR 0.40 vs. ischemic stroke HR 0.90）

### 為何特別有效？

- 血壓對 ICH 的致病角色比對 ischemic stroke 更直接
- 每降 10 mm Hg SBP → 約 40% ICH 風險下降（流行病學 & Mendelian randomization 證據）
- 3 種機轉互補 → 平穩且持久的血壓控制

---

# Subgroup 分析（Primary Outcome）

<!-- _class: small-text -->

| Subgroup | Triple Pill | Placebo | HR (95% CI) |
|----------|:----------:|:-------:|:-----------:|
| Sri Lanka | 4.1% | 7.4% | 0.55 (0.33–0.91) |
| Other | 5.5% | 7.4% | 0.72 (0.37–1.40) |
| <60 yr | 4.7% | 6.2% | 0.76 (0.44–1.33) |
| ≥60 yr | 4.4% | 8.9% | 0.48 (0.26–0.87) |
| Male | 5.0% | 7.1% | 0.71 (0.43–1.15) |
| Female | 3.6% | 8.0% | 0.44 (0.21–0.94) |
| **BP <140/90** | 5.3% | 4.6% | **1.16 (0.55–2.45)** |
| **BP ≥140/90** | 4.2% | 8.9% | **0.47 (0.28–0.76)** |

> **異質性**：僅基線 BP 分層有差異——**BP ≥140/90 的病人獲益最大**

---

<!-- _class: divider -->

# 第四部分：安全性

---

# 安全性結果

| 指標 | Triple Pill | Placebo |
|------|:----------:|:-------:|
| Serious adverse event | 23.2% | 26.0% |
| AE of special interest (前 6 wk) | 6.7% | 6.6% |
| **因 AE 提早停藥** | **13.6%** | **6.0%** |
| &nbsp;&nbsp;Creatinine ↑ ≥20% | 7.1% | 2.5% |
| &nbsp;&nbsp;Hypotension | 3.0% | 0.6% |
| &nbsp;&nbsp;其他 | 3.5% | 2.9% |

> **Pearl**：特殊關注 AE（低血鈉、高鉀、暈厥、跌倒、AKI）兩組相似

---

# Creatinine 上升怎麼看？

> **臨床洞察**：Triple pill 初期 eGFR 短暫下降多為 **血行動力學反應 (hemodynamic response)**，**不等於腎臟實質損傷**

### 研究觀察
- 第 6 週後未見 CKD 進一步惡化
- 未見透析需求增加
- 長期 eGFR trajectory 與 placebo 組相似

### 臨床建議
- **Creatinine ↑<20%**：多為血行動力學，可繼續觀察
- **Creatinine ↑≥30%**：合理的減藥或停藥警示閾值
- 研究採 **≥20%** 是規管機關規定，可能過嚴

---

<!-- _class: divider -->

# 第五部分：臨床意義

---

# 大局觀：與歷史 RCT 的一致性

<!-- _class: small-text -->

| 試驗 | 族群 | 介入 vs. 對照 | 結果 |
|------|------|-----------|------|
| **PROGRESS** (2001) | 中風/TIA | Perindopril±indapamide | Stroke 相對 ↓28%；ICH ↓49% |
| **RESPECT** (2019) | 中風 | Intensive vs. standard BP | Recurrent stroke ↓ |
| **INTERACT3** (2023) | Acute ICH | Care bundle (含快速降壓) | 功能預後改善 |
| **ESPRIT** (2025) | 中風後 | Intensive BP control | Stroke ↓ |
| **TRIDENT** (2026) | Prior ICH | Triple pill vs. placebo | **Stroke ↓39%；ICH ↓60%** |

> **TRIDENT 的貢獻**：首度以 **雙盲 RCT 設計** 證實 triple pill 在 ICH 後的療效與安全性

---

# 與 Guideline 的對應

- **2022 AHA/ASA ICH Guideline**：ICH 後 SBP 目標 **<130 mm Hg**
- **2025 AHA/ACC BP Guideline**：強調積極降壓
- **2024 ESC BP Guideline**：SBP 目標 120–130 mm Hg
- **2025 ESO ICH Guideline**：強調長期血壓管理

> **TRIDENT 證據**：Triple pill 是 **實現 guideline 目標** 的有效工具

---

# Take Home Messages

> **Pearl 1**：ICH 後 SBP 130–160 mm Hg 病人，triple pill (telmisartan 20 + amlodipine 2.5 + indapamide 1.25 mg) 可降低再發中風風險 39% (NNT=35)

> **Pearl 2**：**目標 SBP <130 mm Hg** 在 ICH 後是安全且有益的

> **Pearl 3**：**基線 BP ≥140/90 mm Hg 的病人獲益最大**，應優先考慮

> **Pearl 4**：啟動 triple pill 後 4–6 週監測 creatinine；**↑<20% 為血行動力學反應，≥30% 才需減藥**

> **Pearl 5**：低劑量多機轉組合 = 兼顧療效、順從性、安全性的務實策略

---

# 研究限制

1. **族群代表性**：66.7% 病人來自斯里蘭卡
2. **Run-in phase 排除 24.3%**：結果適用於能耐受 triple pill 的族群
3. **Creatinine ≥20% 排除標準過嚴**
4. **Placebo 組後期加藥多**，可能低估 triple pill 效益
5. **樣本數下調** 使部分次要終點檢定力不足（如 CV death）

---

<!-- _class: small-text -->

# 參考文獻

1. Anderson CS, Chow CK, de Silva HA, et al. Three Low-Dose Antihypertensive Agents in a Single Pill after Intracerebral Hemorrhage (TRIDENT). [*N Engl J Med*. 2026;394(16):1571-82.](https://doi.org/10.1056/NEJMoa2515043)
2. Greenberg SM, et al. 2022 AHA/ASA ICH Guideline. [*Stroke*. 2022;53(7):e282-e361.](https://doi.org/10.1161/STR.0000000000000407)
3. Jones DW, et al. 2025 AHA/ACC BP Guideline. [*Circulation*. 2025;152(11):e114-e218.](https://doi.org/10.1161/CIR.0000000000001301)
4. McEvoy JW, et al. 2024 ESC BP Guideline. [*Eur Heart J*. 2024;45:3912-4018.](https://doi.org/10.1093/eurheartj/ehae178)
5. Chow CK, et al. QUARTET Trial. [*Lancet*. 2021;398:1043-52.](https://doi.org/10.1016/S0140-6736(21)01922-X)
6. PROGRESS Collaborative Group. [*Lancet*. 2001;358:1033-41.](https://doi.org/10.1016/S0140-6736(01)06178-5)
7. Kitagawa K, et al. RESPECT Trial. [*JAMA Neurol*. 2019;76:1309-18.](https://doi.org/10.1001/jamaneurol.2019.2167)
8. Ma L, et al. INTERACT3 Trial. [*Lancet*. 2023;402:27-40.](https://doi.org/10.1016/S0140-6736(23)00806-1)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
