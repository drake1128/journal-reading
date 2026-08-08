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
  section.lead a { color: #b0c4de; }
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
footer: '謝慕揚 MD, PhD, FESC | JVP & S3 預後價值 (Drazner SOLVD) | 2001'
---

<!-- _class: lead -->

# Elevated JVP & Third Heart Sound in Heart Failure

## 頸靜脈壓升高與第三心音的預後價值 (SOLVD)

**謝慕揚 MD, PhD, FESC**
Drazner MH, et al. *N Engl J Med*. 2001;345(8):574-581
[原文連結：https://doi.org/10.1056/NEJMoa010641](https://doi.org/10.1056/NEJMoa010641)

---

# 大綱

1. 研究背景：床邊理學檢查為何重要
2. 研究方法：SOLVD 回溯分析
3. 事件發生率與存活曲線
4. 單變項與多變項分析（核心結果）
5. 分層分析（NYHA、治療分派）
6. 臨床意義與 Pearls
7. 研究限制與結論

---

<!-- _class: divider -->

# 第一部分：背景與方法

---

# 研究背景

- 憂心醫師**理學檢查 (physical examination)** 能力下滑，尤其住院醫師的心臟聽診技巧不佳。
- 過去 JVP、S3 的預後資料多來自**小樣本觀察研究**，且**多未校正**其他嚴重度指標（如 LVEF）。
- 在實證醫學年代，若能證明理學檢查有用，可重新激勵醫師精進 bedside 技巧。

> **假說**：心衰竭病人若有 **JVP 升高**或 **S3 (third heart sound / S3 gallop)**，可提供**重要且獨立**的預後資訊。

---

# 研究方法

- **設計**：SOLVD treatment trial 之回溯分析（enalapril vs. placebo 隨機試驗）。
- **族群**：症狀性心衰竭、**LVEF ≤ 0.35**；收案 1986–1989。
- **理學檢查**：入組時以常規檢查，於表單上「yes/no」記錄 JVP 與 S3。
- **追蹤**：平均 32 ± 15 個月。
- **分析族群**：排除資料不全後 **2479 人**。
- **統計**：Cox proportional-hazard model；校正 age、LVEF、NYHA、治療、性別、病因、race、AF、Na、Cr、DM/HTN、beta-blocker/digoxin/diuretic。

---

# 終點定義

| 終點 | 定義 |
|------|------|
| 全因死亡 | 原試驗主要終點 |
| Pump-failure death | 幫浦衰竭死亡（含有惡化前兆之疑似心律不整死亡） |
| 心律不整死亡 | 無惡化前兆之疑似心律不整死亡 |
| 心衰竭進展 | 預先指定 = pump-failure death + 「死亡或心衰竭住院」複合終點 |

- 族群分布：JVP 升高 **280 人**、S3 **597 人**；706 人具其一或兩者，1773 人皆無。

---

<!-- _class: divider -->

# 第二部分：結果

---

# 事件發生率 (Table 2)

每 100 人年發生率；有徵象者各終點（除心律不整死亡外）皆顯著升高。

| 終點 | JVP+ (280) | JVP− (2199) | S3+ (597) | S3− (1882) |
|------|-----------|-------------|-----------|------------|
| 全因死亡 | 20.3 | 13.3 | 17.5 | 13.0 |
| 心衰竭住院 | 23.8 | 13.0 | 20.9 | 12.1 |
| 死亡或HF住院 | 38.1 | 22.0 | 30.9 | 21.4 |
| Pump-failure death | 12.4 | 6.3 | 10.4 | 5.9 |
| 心律不整死亡 | 3.6 | 3.2 | 3.8 | 3.1 |

> Kaplan–Meier：JVP+ 與 S3+ 達複合終點機率皆顯著較高（log-rank **P < 0.001**）。

---

# 單變項分析 (Univariate)

| 終點 | JVP RR (95% CI) | S3 RR (95% CI) |
|------|-----------------|----------------|
| 全因死亡 | 1.52 (1.27–1.82) | 1.35 (1.17–1.55) |
| 心衰竭住院 | 1.78 (1.47–2.17) | 1.70 (1.46–1.97) |
| 死亡或HF住院 | 1.69 (1.45–1.97) | 1.42 (1.26–1.60) |
| Pump-failure death | 1.99 (1.57–2.52) | 1.77 (1.46–2.15) |
| 心律不整死亡 | 1.10 (0.72–1.68)* | 1.22 (0.90–1.65)* |

*除心律不整死亡（P=0.66 / P=0.20）外，其餘 **P < 0.001**。*

---

# 多變項分析 (Table 3) — 核心

校正所有共變項後，JVP 與 S3 對 HF 住院、死亡或HF住院、pump-failure death 仍**各自獨立顯著**。

| 終點 | JVP (280) | S3 (597) | 任一或兩者 (706) |
|------|-----------|----------|------------------|
| 全因死亡 | 1.15 (0.95–1.38) | 1.15 (0.99–1.33) | **1.17 (1.02–1.35)** |
| 心衰竭住院 | **1.32 (1.08–1.62)** | **1.42 (1.21–1.66)** | **1.43 (1.23–1.66)** |
| 死亡或HF住院 | **1.30 (1.11–1.53)** | **1.22 (1.08–1.38)** | **1.28 (1.14–1.45)** |
| Pump-failure death | **1.37 (1.07–1.75)** | **1.40 (1.14–1.71)** | **1.47 (1.21–1.79)** |
| 心律不整死亡 | 0.96 (0.62–1.49) | 1.13 (0.82–1.54) | 1.08 (0.80–1.46) |

---

# 補充與分層分析

- **兩者 vs. 單一**：同時具 JVP + S3（171 人）與僅具其一（535 人）風險相近，如死亡或HF住院 RR 1.05 (0.84–1.30, P=0.69)。
- **依 NYHA 分層 (I/II vs. III/IV)**：兩層結果與主分析一致，RR 多 > 1.00。
- **依治療分層 (placebo vs. enalapril)**：風險相近；治療與 JVP/S3 **無顯著交互作用**（所有 P > 0.1）。

> ACE inhibitor 治療**不改變** JVP／S3 的預後價值。

---

<!-- _class: divider -->

# 第三部分：臨床意義

---

# 病生理連結

- **JVP 升高** → 反映右心房壓上升 → 與慢性心衰竭的**左側充盈壓升高**相關。
- **S3** → 反映低心室順應性、充盈壓升高或早期舒張快速充盈。
- 左側充盈壓升高與不良預後相關，可能經由**心肌牽張誘發 apoptosis** 或**交感神經活化**。
- 呼應為何兩徵象關聯的是**幫浦衰竭路徑**（pump-failure death、HF 住院），而**非心律不整死亡**。

---

# 臨床 Pearls

> **Pearl 1**：床邊發現 JVP 升高或 S3，是心衰竭病人**未來 HF 住院／幫浦衰竭死亡**風險升高的獨立警訊。

> **Pearl 2**：此預後價值**獨立於 LVEF、NYHA、血鈉**之外，也**不因是否使用 ACE inhibitor 而改變**。

> **Pearl 3**：JVP 升高盛行率低但特異度高（univariate pump-failure death RR 1.99）；S3 較常見但觀察者間一致性有限，判讀需審慎。

---

# 研究限制

- **回溯性設計**：可能存在殘餘干擾 (residual confounding)。
- **理學檢查未標準化**：無 phonocardiography 確認；隨機錯分類會使結果**偏向虛無**（低估效果）。
- **S3 觀察者間一致性**：即使有經驗醫師亦僅中至低。
- **beta-blocker 使用率低**：無法評估其對徵象預後價值的影響。
- 入組即限 LVEF ≤ 0.35 → 無法評估作為 LVSD 診斷指標之效能。

---

# 結論

1. 心衰竭病人的 **JVP 升高**與 **S3**，各自**獨立**與不良預後（含心衰竭進展）相關，校正其他嚴重度指標後仍成立。
2. 強化「**聚焦式床邊評估具臨床意義**」的信念，為訓練醫師提供精進理學檢查的實證動力。

> 一項零成本、床邊即可完成的檢查，提供獨立於影像與生物標記之外的預後資訊。

---

<!-- _class: small-text -->

# 參考文獻

1. Drazner MH, Rame JE, Stevenson LW, Dries DL. Prognostic importance of elevated jugular venous pressure and a third heart sound in patients with heart failure. *N Engl J Med*. 2001;345(8):574-581. https://doi.org/10.1056/NEJMoa010641
2. The SOLVD Investigators. Effect of enalapril on survival in patients with reduced LVEF and congestive heart failure. *N Engl J Med*. 1991;325(5):293-302.
3. Dries DL, et al. Racial differences in the outcome of left ventricular dysfunction. *N Engl J Med*. 1999;340(8):609-616.
4. Stevenson LW, Perloff JK. The limited reliability of physical signs for estimating hemodynamics in chronic heart failure. *JAMA*. 1989;261(6):884-888.

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
