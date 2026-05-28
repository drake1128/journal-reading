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
  section.ref { font-size: 0.62em; }
footer: '謝慕揚 MD, PhD, FESC | 2026 AHA/ACC PE Guideline | 2026-04-11'
---

<!-- _class: lead -->

# 2026 AHA/ACC Acute PE Guideline
## 急性肺栓塞指引概覽

**謝慕揚 MD, PhD, FESC**
[*J Am Coll Cardiol*. 2026;87(13):1626-1710](https://doi.org/10.1016/j.jacc.2025.11.005)
10 學會聯合制定 | AHA/ACC 首部 PE 指引

---

# 大綱

1. 為什麼需要新指引？
2. **Clinical Categories A-E** — 取代 massive/submassive
3. 診斷策略
4. 抗凝血治療
5. 進階治療（Thrombolysis, CDT, MT, Surgery）
6. PERT 與追蹤

---

<!-- _class: divider -->

# 為什麼需要新指引？

---

# 舊分類的問題

- AHA/ACC **從未**發布過 PE 專屬指引
- **「Submassive」**涵蓋太廣 — 從穩定到瀕臨休克，全歸同一類

```text
「Submassive PE」= ?

Patient A: Troponin 輕微升高，臨床穩定，自覺良好
Patient B: RV failure，lactate 升高，即將休克

→ 同樣被稱為「submassive」→ 治療決策完全不同！
```

- Catheter-based therapy 使用量每年 ↑18% — 需要明確定位
- **本指引的目標**：以 physiopathological severity 精準分層

---

<!-- _class: divider -->

# Clinical Categories A-E

---

# Category A & B — 低風險

| Category | 定義 | 處置 |
|:--------:|------|------|
| **A** | **Subclinical** — 影像意外發現，無症狀 | 可從急診**直接出院** |
| **B** | **Low Severity** — 有症狀，PESI I-II / sPESI 0 / Hestia 0 | **早期出院** (24-48h) |

> **Pearl**: Category A = 過去被忽略的「incidental PE」，首次有明確處置建議

---

# Category C — Intermediate Severity（最關鍵的分層）

有症狀 + PESI III-V / sPESI ≥ 1 / Hestia ≥ 1 → **住院**

| Subcategory | RV Function | Troponin | 風險 |
|:-----------:|:----------:|:--------:|:----:|
| **C1** | Normal | Normal | Intermediate-low |
| **C2** | **Abnormal OR** | **elevated** (一項異常) | Intermediate |
| **C3** | **Abnormal AND** | **elevated** (兩項皆異常) | **Intermediate-high** |

- C3 = 過去的「submassive + RV dysfunction + troponin 升高」
- **C3 需密切監測**，可能進展至 Category D

> **Pearl**: 過去的「submassive」被精細分為 **C1, C2, C3, D1, D2** — 五個不同等級

---

# Category D — Incipient Failure

**血壓仍正常**，但出現心肺衰竭前兆

| Subcategory | 定義 |
|:-----------:|------|
| **D1** | **暫時性低血壓** — 短暫發作，對 volume 有反應，**無器官損傷** |
| **D2** | **暫時性低血壓 + 器官損傷** (AKI, elevated lactate) |

- Advanced therapy **may be considered** (Class 2b)
- 這些患者是「即將 crash」的族群 — 需要密切監測

---

# Category E — Cardiopulmonary Failure

| Subcategory | 定義 | SCAI Shock |
|:-----------:|------|:----------:|
| **E1** | **Persistent hypotension + cardiogenic shock** | Stage C |
| **E2** | **Refractory shock or cardiac arrest** | Stage D-E |

- Advanced therapy **reasonable** for E1 (**Class 2a**)
- E2 = emergent intervention + cardiopulmonary support

---

# Respiratory Modifier (R)

可附加於**任何 subcategory** — 例如 C2**R**, D1**R**

- **Hypoxia**
- **Tachypnea**
- **Escalating O₂ requirements**

> **Pearl**: R modifier 識別**呼吸惡化趨勢** — 提示可能進展至更高 category

---

# 新舊分類對照

| 舊分類 | 新分類 | 改善 |
|--------|--------|------|
| Low-risk | **A** (subclinical) + **B** (low severity) | 區分有/無症狀 |
| **Submassive** (涵蓋過廣) | **C1, C2, C3, D1, D2** | 五級精細分層 |
| Massive | **E1, E2** | 對應 SCAI Shock staging |
| — | **R modifier** | 識別呼吸惡化趨勢 |

---

<!-- _class: divider -->

# 診斷與抗凝血治療

---

# 診斷策略建議

| 建議 | COR |
|------|:---:|
| 使用 validated decision rules (Wells, Geneva) | **1** |
| 低機率 + D-dimer negative → 排除 PE | **1** |
| Age-adjusted D-dimer (>50 歲) | **2a** |
| **CTPA** 為首選確診影像 | **1** |
| 血行動力學不穩 → **bedside echo** 評估 RV | **1** |

---

# 抗凝血治療

| 階段 | 建議 | COR |
|------|------|:---:|
| **初始 parenteral** | **LMWH 優於 UFH** | **1** |
| **口服長期** | **DOAC 優於 VKA** | **1** |
| DOAC 禁忌 | Pregnancy, APS, severe renal/hepatic failure | 3 |
| 有 reversible risk factor | 3-6 個月 | 1 |
| **首次 PE 無 reversible RF** | **延長 > 3-6 個月** | **1** |
| 持續性 RF (cancer) | **長期/終生** | 1 |

> **Pearl**: LMWH > UFH, DOAC > VKA — 兩個「大於」要記住

---

<!-- _class: divider -->

# 進階治療

---

# Advanced Therapy by Category

| Category | Thrombolysis | CDT | MT | Surgery |
|:--------:|:----------:|:---:|:--:|:-------:|
| A-C1 | Class 3 | Class 3 | Class 3 | Class 3 |
| C2-C3 | — | — | — | — |
| **D1-D2** | 2b | **2b** | **2b** | 2b |
| **E1** | **2a** | **2a** | **2a** | **2a** |
| E2 | 個案 | 個案 | 個案 | Emergent |

- **E1**: All advanced therapies = **Class 2a** (Reasonable)
- **D1-D2**: All advanced therapies = **Class 2b** (May be considered)
- **A-C1**: **Class 3** (No Benefit) — 不建議

---

# Catheter-Based Therapy 重點

- **CDT** (Catheter-Directed Thrombolysis):
  - E1: Class 2a — prevent deterioration + early mortality
  - D1-D2: Class 2b — progressive deterioration 時考慮

- **Mechanical Thrombectomy (MT)**:
  - E1: Class 2a
  - D1-D2: Class 2b
  - **高出血風險時可考慮 over systemic thrombolysis**
  - 但 superiority 尚未被證實

> **Pearl**: Catheter-based therapy = 高出血風險時的**替代**選擇，而非 systemic thrombolysis 的**取代**

---

<!-- _class: divider -->

# PERT 與追蹤

---

# PERT (PE Response Team) — Class 1

### 組成

Vascular medicine · Interventional cardiology/radiology · Cardiac surgery · Emergency medicine · Hematology · Pharmacy · Nursing

### 功能

- 即時 risk stratification → 決定 Category
- Advanced therapy selection & implementation
- 證據缺口的臨床判斷
- Follow-up coordination

---

# Post-PE 追蹤框架

| 時間點 | 內容 |
|--------|------|
| **出院 1 週內** | Communication or clinic visit |
| **3 個月** | 重新評估 anticoagulation duration |
| **每次回診 (≥ 1 年)** | 篩檢 **CTEPD/CTEPH** |

### Post-PE Syndrome（首次被正式定義）

- Persistent dyspnea
- Exercise intolerance
- Reduced quality of life
- Psychological impact (anxiety, PTSD)

> **Pearl**: PE 不只是急性期疾病 — Post-PE Syndrome 需要長期追蹤

---

<!-- _class: divider -->

# Take Home Messages

---

# 5 大 Take Home Messages

1. **告別 massive/submassive** — 新 Clinical Categories **A-E** 更精準地指導治療
2. **Category C 是最關鍵的分層** — C1/C2/C3 區分了過去被 submassive 混為一談的不同風險等級
3. **LMWH > UFH, DOAC > VKA** — 抗凝血治療的兩個「大於」
4. **Catheter-based therapy** 在 E1 獲得 Class 2a，D1-D2 獲得 Class 2b — 不是取代 thrombolysis，是高出血風險時的替代
5. **Post-PE Syndrome** 首次被正式定義 — PE 需要至少 1 年的結構化追蹤

---

<!-- _class: ref -->

# 參考文獻

1. Creager MA, et al. 2026 AHA/ACC PE Guideline. [*JACC*. 2026;87(13):1626-1710.](https://doi.org/10.1016/j.jacc.2025.11.005)
2. Creager MA, et al. Same guideline. [*Circulation*. 2026.](https://doi.org/10.1161/CIR.0000000000001415)
3. Dudzinski DM, et al. Guideline-at-a-Glance. [*JACC*. 2026;87(13):1620-1625.](https://doi.org/10.1016/j.jacc.2025.12.042)
4. Kim JM, et al. MT & CDT in PE: PERT. [*JACC*. 2026;87(13):1574-1590.](https://doi.org/10.1016/j.jacc.2025.12.073)
5. [AHA Professional Heart Daily — Top Things to Know](https://professional.heart.org/en/science-news/2026-guideline-for-the-evaluation-and-management-of-acute-pulmonary-embolism-in-adults)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
