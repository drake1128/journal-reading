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
footer: '謝慕揚 MD, PhD, FESC | LV Unloading in HR-PCI | ACC 2026'
---

<!-- _class: lead -->

# CHIP-BCIS3 Trial
## LV Unloading in High-Risk PCI — Microaxial Flow Pump vs. Standard Care

**謝慕揚 MD, PhD, FESC**
資料來源：*N Engl J Med* 2026 | Perera D, Ryan M, et al.
[原文連結](https://doi.org/10.1056/NEJMoa2515704)

---

# 大綱

1. 研究背景與 "Protected PCI" 概念
2. 試驗設計與納入條件
3. 基線特徵
4. 主要終點結果 (Win Ratio)
5. 次要終點 — 死亡與安全性
6. Periprocedural Myocardial Injury 分析
7. 不良事件與血管併發症
8. 亞組分析
9. 與既往試驗比較
10. 臨床意義與結論

---

<!-- _class: divider -->

# 第一部分：研究背景

---

# "Protected PCI" 的概念與爭議

- 嚴重 LV dysfunction + 複雜冠狀動脈疾病 = **高風險 PCI**
- Microaxial flow pump (Impella) 可提供 **continuous nonpulsatile LV unloading**
- 2015 年 FDA 核准用於 severe LV dysfunction 之 PCI
- "Protected PCI" 使用量快速成長，但**缺乏 RCT 證據**

### 既往試驗均為陰性

| 試驗 | 年份 | 比較 | 結果 |
|------|------|------|------|
| BCIS-1 | 2010 | IABP vs. no MCS | 無益 |
| PROTECT II | 2012 | Impella 2.5 vs. IABP | Futility 終止 |

---

# CHIP-BCIS3 試驗設計

- **前瞻性、多中心、open-label RCT**
- 英國 21 家醫院，2021-2024 年收案
- **N = 300**，1:1 隨機分配
- 追蹤中位數 **22 個月** (IQR 16-30)

### 介入策略

| Pump 組 (n=148) | Standard Care 組 (n=152) |
|-----------------|------------------------|
| Impella CP elective 置入 | 無計劃性 MCS |
| 術前 CT 血管規劃建議 | 同前 |
| 不允許 crossover | Bailout IABP/VA-ECMO 允許 |

---

# 納入條件 — 真正 High-Risk Population

### 核心條件
- **LVEF ≤35%** (或 ≤45% 合併 severe MR)
- **BCIS Jeopardy Score ≥8** (0-12 scale)
- 計劃接受 **complex PCI**

### Complex PCI 定義 (至少符合一項)
1. **Unprotected left main PCI** + occluded RCA / left dominant / entire bifurcation
2. **多血管 calcium modification** / left main / final patent conduit / SYNTAX ≥32
3. **CTO retrograde approach**

### 排除條件
- Cardiogenic shock、急性 STEMI、已使用 MCS

---

# 主要終點設計 — Hierarchical Win Ratio

```text
Tier 1: Death from any cause (全因死亡)
    ↓ tie
Tier 2: Disabling stroke (失能性中風)
    ↓ tie
Tier 3: Spontaneous MI (自發性心肌梗塞)
    ↓ tie
Tier 4: CV hospitalization (心血管住院)
    ↓ tie
Tier 5: Periprocedural myocardial injury
```

- Win ratio > 1 = pump 組較佳
- Win ratio < 1 = standard care 較佳
- Power: 85% to detect win ratio ≥1.6

---

<!-- _class: divider -->

# 第二部分：結果

---

# 基線特徵 — 高風險族群

| 特徵 | Pump (n=148) | Standard Care (n=152) |
|------|-------------|----------------------|
| 年齡 (歲) | 72.2 ± 10.1 | 73.3 ± 9.3 |
| 男性 | 84.5% | 80.9% |
| 糖尿病 | **56.1%** | 48.0% |
| Median LVEF | **26% (20-31)** | **28% (20-32)** |
| Median BCIS-JS | 12 (10-12) | 12 (10-12) |
| Median SYNTAX | 38 (28-47) | 38 (31-49) |
| NYHA III-IV | 45.4% | 46.6% |

> **Pearl**：整體 LVEF 27%、SYNTAX 38 — 確認為真正 high-risk cohort

---

# 主要終點 — Win Ratio 結果

| 階層 | Win for Pump | Win for SC | Difference |
|------|-------------|-----------|------------|
| Death | 16.4% | 23.4% | **-7.0** |
| Disabling stroke | 0.8% | 0.6% | +0.2 |
| Spontaneous MI | 4.6% | 1.9% | +2.6 |
| CV hospitalization | 8.2% | 6.5% | +1.7 |
| Periprocedural injury | 6.6% | 10.5% | -3.9 |
| **Overall** | **36.6%** | **43.0%** | **-6.4** |

### Win Ratio = 0.85 (95% CI, 0.63-1.15; P = 0.30)

> **結果：Pump 無益，數值偏向 standard care**

---

# 次要終點 — 死亡風險令人擔憂

| 終點 | Pump 組 | Standard Care | HR (95% CI) |
|------|---------|--------------|-------------|
| **全因死亡** | 32.6% | 23.4% | **1.54 (0.99-2.41)** |
| **心血管死亡** | 26.7% | 14.5% | **1.91 (1.11-3.30)** |
| Disabling stroke | 3.5% | 4.5% | 0.53 (0.13-2.11) |
| Spontaneous MI | 6.8% | 12.4% | 0.64 (0.28-1.47) |
| CV 住院 | 24.5% | 21.0% | 1.20 (0.72-1.98) |

> **Pearl**：心血管死亡 HR 1.91 為**統計顯著有害訊號**
> 24 個月心血管死亡絕對風險差 = +12.2%

---

# Periprocedural Myocardial Injury

- Pump 組：**61.7%** vs. Standard Care 組：**50.0%**
- Risk Ratio = 1.23 (95% CI, 0.99-1.54)

### 矛盾發現

- 理論上 LV unloading 應**減少** ischemia 和 myocardial damage
- 實際結果：pump 組心肌損傷**更多**

### 可能解釋

1. 裝置本身造成心肌損傷 (機械性)
2. 一次性完成所有血管重建 vs. staged approach
3. 較長手術時間的影響
4. Pump 給予「安全感」導致更積極操作

---

# 血管重建完整度 — 兩組相似

| 指標 | Pump 組 | Standard Care |
|------|---------|--------------|
| Revascularization index | 67% (50-80) | 67% (50-80) |
| Residual SYNTAX score | 14 (8-22) | 13 (7-26) |
| Staged PCI | 10 patients | **27 patients** |

> **Pearl**：Standard care 組透過 **staged strategy** 達到與 pump 組相同的血管重建程度，但不需承擔大口徑血管通路風險

---

# 不良事件

| 事件 | Pump 組 | Standard Care | RR (95% CI) |
|------|---------|--------------|-------------|
| Major bleeding | 10.8% | 7.3% | 1.48 (0.71-3.09) |
| Minor vascular complications | 15.5% | 9.9% | 1.56 (0.85-2.88) |
| Major vascular complications | 1.4% | 0.7% | — |

### 裝置置入成功率
- 成功率：**97.3%** (144/148)
- 失敗原因：周邊血管疾病 (2)、major vascular complication (1)、急性下肢缺血 (1)

### Standard care 組 bailout MCS
- 9/152 (6.0%)：8 例 IABP，1 例 microaxial flow pump

---

# 亞組分析 — 所有亞組一致

| 亞組 | Win Ratio (95% CI) |
|------|-------------------|
| Overall | 0.85 (0.63-1.15) |
| Age < 74.6 yr | 0.91 (0.58-1.42) |
| Age ≥ 74.6 yr | 0.80 (0.53-1.21) |
| BCIS-JS < 12 | 1.07 (0.61-1.90) |
| BCIS-JS = 12 | 0.73 (0.51-1.06) |
| LVEF < 27% | 0.94 (0.61-1.45) |
| LVEF ≥ 27% | 0.78 (0.51-1.19) |
| Left main PCI: Yes | 0.93 (0.65-1.32) |
| Left main PCI: No | 0.62 (0.33-1.15) |

> 無任何亞組顯示 pump 有顯著獲益

---

<!-- _class: divider -->

# 第三部分：討論與結論

---

# 與其他 MCS 試驗的整合分析

| 試驗 | 情境 | 裝置 | 結果 |
|------|------|------|------|
| **BCIS-1** (2010) | Elective HR-PCI | IABP | 無益 |
| **PROTECT II** (2012) | Elective HR-PCI | Impella 2.5 vs. IABP | Futility |
| **CHIP-BCIS3** (2026) | Elective HR-PCI | Impella CP vs. no MCS | **無益，可能有害** |
| **DANGER-SHOCK** (2024) | STEMI + shock | Impella CP vs. SC | **有益 (NNT~7)** |

> **Pearl**：Impella 在 elective HR-PCI 始終無益，但在 cardiogenic shock 有益。臨床適應症需明確區分。

---

# 臨床啟示

### 不應做的
- 在 elective high-risk PCI 中**常規使用** Impella
- 僅因 "high SYNTAX score" 或 "low LVEF" 就啟動 Protected PCI

### 應該做的
- 優先考慮 **staged PCI strategy** — 可達相同血管重建效果
- 嚴格評估大口徑血管通路之 **出血/血管併發症** 風險
- Cardiogenic shock 患者仍可考慮 Impella (DANGER-SHOCK 證據)
- 多專科 Heart Team 討論最佳血管重建策略

> **Bottom line**："Protected PCI" 這個名詞本身具有誤導性 — pump 並未提供保護，反而可能造成傷害。

---

<!-- _class: small-text -->

# 參考文獻

1. Perera D, et al. LV Unloading in HR-PCI. [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2515704)
2. Perera D, et al. BCIS-1: Elective IABP in HR-PCI. [*JAMA*. 2010;304:867-74.](https://doi.org/10.1001/jama.2010.1190)
3. O'Neill WW, et al. PROTECT II. [*Circulation*. 2012;126:1717-27.](https://doi.org/10.1161/CIRCULATIONAHA.112.098194)
4. Moller JE, et al. DANGER-SHOCK. [*N Engl J Med*. 2024;390:1382-93.](https://doi.org/10.1056/NEJMoa2312572)
5. Ryan M, et al. CHIP-BCIS3 Design. [*Circ Cardiovasc Interv*. 2024;17(3):e013367.](https://doi.org/10.1161/CIRCINTERVENTIONS.123.013367)
6. Amin AP, et al. Impella Use in US PCI. [*Circulation*. 2020;141:273-84.](https://doi.org/10.1161/CIRCULATIONAHA.119.044007)
7. Lawton JS, et al. 2021 ACC/AHA/SCAI Revascularization Guideline. [*Circulation*. 2022;145(3):e18-e114.](https://doi.org/10.1161/CIR.0000000000001038)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
