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
footer: '謝慕揚 MD, PhD, FESC | ACC 2026 Angio-Based Physiology | 2026'
---

<!-- _class: lead -->

# ACC 2026: Angiography-Based Coronary Physiology

## ALL-RISE & FAST III — 血管攝影衍生生理學指引 PCI

**謝慕揚 MD, PhD, FESC**
資料來源：*N Engl J Med* 2026 | 2026-03-31
[ALL-RISE: DOI 10.1056/NEJMoa2600949](https://doi.org/10.1056/NEJMoa2600949) | [FAST III: DOI 10.1056/NEJMoa2601841](https://doi.org/10.1056/NEJMoa2601841)

---

# 大綱

1. Pressure-wire FFR 的限制與 angiography-based physiology 的概念
2. ALL-RISE Trial — FFRangio vs Pressure Wire
3. FAST III Trial — vFFR vs FFR
4. 兩大試驗交叉比較
5. 臨床意義與未來方向

---

<!-- _class: divider -->

# 第一部分：背景與概念

---

# 為何需要 Angiography-Based Physiology?

## Pressure-Wire FFR 的限制

- FFR/iFR 有 **Class I** 建議用於 intermediate lesion 評估
- 臨床使用率仍然 **< 20%**
- 障礙因素：
  - 需要 **guide catheter** 與專用 **pressure wire**
  - 常需 **adenosine** 誘發 maximal hyperemia
  - 增加 **手術時間、radiation、contrast** 用量
  - 增加手術 **成本** 與 **複雜度**

> **關鍵問題**：能否不用 pressure wire，僅以血管攝影影像估算 FFR？

---

# Angiography-Derived FFR 的原理

## 不同系統使用不同演算法，但概念相同

| 系統 | 廠商 | 特色 |
|------|------|------|
| **FFRangio** | CathWorks | 3D reconstruction + resistance model |
| **vFFR** | Pie Medical | 3D-QCA + Gould-Kirkeeide model |
| **QFR** | Medis | 3D-QCA + computational fluid dynamics |
| **FlashAngio** | RainMed | AI-based computation |

- **共同優勢**：不需 pressure wire、不需 adenosine、計算快速（~5-6 min）
- 多項 validation study 證實與 wire-based FFR 良好相關

---

# 先前證據：QFR 的故事

- **FAVOR III China** (2021)：QFR-guided **優於** angiography-guided → Class IB
- **FAVOR III Europe** (2024)：QFR-guided **未能** noninferiority vs FFR-guided

> **教訓**：不同 angiography-based physiology 系統不可互換，需個別臨床驗證

- ACC 2026 同時發表兩項試驗驗證另外兩個系統

---

<!-- _class: divider -->

# 第二部分：ALL-RISE Trial

---

# ALL-RISE：研究設計

## FFRangio (CathWorks) vs Pressure Wire

| 項目 | 內容 |
|------|------|
| 設計 | International, randomized, noninferiority |
| 中心數 | **59 sites**（全球） |
| 樣本數 | **1930** (965 vs 965) |
| 族群 | Intermediate stenosis 50-90% |
| 主要終點 | Death, MI, unplanned revascularization (1 yr) |
| NI margin | **3.5 pp** |
| 贊助 | CathWorks |

- 對照組可用 FFR (55.5%) 或 NHPR/iFR (44.5%)
- 註冊：[NCT05893498](https://clinicaltrials.gov/study/NCT05893498)

---

# ALL-RISE：基線特徵

| 特徵 | FFRangio (n=965) | Pressure Wire (n=965) |
|------|-------------------|----------------------|
| 年齡 | 68.4 ± 10.1 yr | 68.4 ± 10.3 yr |
| 女性 | 24.5% | 25.5% |
| 糖尿病 | 39.5% | 36.3% |
| 高血壓 | 78.5% | 79.9% |
| Prior PCI | 38.9% | 39.0% |
| NSTE-ACS | 9.9% | 8.8% |
| LAD as study vessel | 49.3% | 50.0% |

- 兩組基線特徵 **均衡**
- **穩定型冠心症**為主（~90%）

---

# ALL-RISE：手術特徵

## FFRangio 減少手術時間與資源使用

| 項目 | FFRangio | Pressure Wire | 差異 |
|------|----------|---------------|------|
| Assessment 時間 | 6 min | 8 min | **-2 min** |
| 手術時間 | 39 min | 42 min | **-5 min** |
| Fluoroscopy | 9 min | 12 min | **-3 min** |
| Contrast | 100 mL | 105 mL | **-14 mL** |
| Abnormal ≤0.80 | **43.0%** | 37.0% | — |
| PCI performed | **44.3%** | 35.4% | OR 1.45 |

> FFRangio 偵測到更多 abnormal values → 更多 PCI（+9 pp）

---

# ALL-RISE：主要結果

## Noninferiority 成功達標

| 終點 | FFRangio | Pressure Wire | HR (95% CI) |
|------|----------|---------------|-------------|
| **Primary composite** | **6.9%** | **7.1%** | **0.98 (0.70-1.39)** |
| Death | 2.3% | 2.1% | 1.16 (0.63-2.14) |
| MI | 1.6% | 2.5% | 0.65 (0.34-1.25) |
| Revascularization | 4.1% | 4.6% | 0.90 (0.58-1.40) |
| BARC 3-5 bleeding | 0.7% | 1.5% | 0.50 (0.20-1.23) |

- Risk difference = **-0.2 pp**
- Upper bound 97.5% CI = **2.1 pp** < 3.5 pp margin
- **P < 0.001 for noninferiority**

---

<!-- _class: divider -->

# 第三部分：FAST III Trial

---

# FAST III：研究設計

## vFFR (Pie Medical) vs Wire-Based FFR

| 項目 | 內容 |
|------|------|
| 設計 | International, open-label, randomized, noninferiority |
| 中心數 | **37 sites**（7 歐洲國家） |
| 樣本數 | **2211** (1116 vs 1095, full analysis set) |
| 族群 | Intermediate stenosis 30-80%, chronic or acute |
| 主要終點 | Death, any MI, any revascularization (1 yr) |
| NI margin | **3.0 pp** |
| 贊助 | Pie Medical + Siemens (unrestricted grants) |

- 對照組僅用 FFR（需 adenosine）
- 註冊：[NCT04931771](https://clinicaltrials.gov/study/NCT04931771)

---

# FAST III：手術特徵

## vFFR 同樣偵測到更多功能性顯著病灶

| 項目 | vFFR | FFR |
|------|------|-----|
| Complete assessment | 96.7% | 99.1% |
| Median value | 0.83 (0.74-0.89) | 0.85 (0.79-0.91) |
| Functional significance ≤0.80 | **40.9%** | **31.3%** |
| Revascularization | **45.0%** | **36.0%** |
| PCI procedure time | 55.8 min | 60.9 min |
| Procedure time difference | **-5.13 min** (p < 0.05) | — |

> 與 ALL-RISE 一致：angiography-based 系統偵測更多 abnormal lesions

---

# FAST III：主要結果

## Noninferiority 成功達標

| 終點 | vFFR | FFR | Risk Difference |
|------|------|-----|-----------------|
| **Primary composite** | **7.5%** | **7.5%** | **-0.02 pp** |
| Study-vessel failure | 4.0% | 4.6% | -0.62 pp |
| Death | 2.2% | 2.3% | — |
| Any MI | 2.9% | 2.4% | — |
| Any revascularization | 4.2% | 4.2% | — |

- 95% CI for difference: **-2.25 to 2.21 pp**
- Upper bound = **2.21 pp** < 3.0 pp margin
- **P = 0.004 for noninferiority**

---

<!-- _class: divider -->

# 第四部分：兩大試驗交叉比較

---

# 試驗設計比較

| 項目 | ALL-RISE | FAST III |
|------|----------|----------|
| Angio-based 系統 | FFRangio (CathWorks) | vFFR (Pie Medical) |
| 對照組 | FFR + NHPR | FFR only |
| 樣本數 | 1930 | 2211 |
| 地理分佈 | 全球 59 sites | 歐洲 37 sites |
| NI margin | 3.5 pp | 3.0 pp |
| ACS 比例 | ~9.4% | 18.7% |
| 糖尿病 | ~37.8% | ~26.6% |
| Investigator-initiated | 否 (industry) | 是 (unrestricted grants) |

---

# 關鍵結果比較

| 結果 | ALL-RISE | FAST III |
|------|----------|----------|
| **Primary endpoint (intervention)** | **6.9%** | **7.5%** |
| **Primary endpoint (control)** | **7.1%** | **7.5%** |
| Risk difference | -0.2 pp | -0.02 pp |
| Upper bound CI | 2.1 pp | 2.21 pp |
| **Noninferiority** | **P < 0.001** | **P = 0.004** |
| Abnormal rate (intervention) | 43.0% | 40.9% |
| Abnormal rate (control) | 37.0% | 31.3% |
| PCI rate (intervention) | 44.3% | 45.0% |
| PCI rate (control) | 35.4% | 36.0% |
| **PCI rate difference** | **~9 pp** | **~9 pp** |

---

# 三大共同發現

> **Pearl 1**：兩個 angiography-based 系統（FFRangio, vFFR）均成功達標 noninferiority，結果高度一致

> **Pearl 2**：兩個試驗中 angiography-based 組的 PCI rate 均較 pressure wire 組高約 **9 percentage points**（~44% vs ~35%），但 **未增加不良事件**

> **Pearl 3**：Angiography-based assessment 減少手術時間（-5 min）、fluoroscopy（-3 min）與 contrast 用量（-14 mL），流程顯著簡化

---

<!-- _class: divider -->

# 第五部分：臨床意義

---

# 臨床實務影響

## 預期改變心導管室的工作流程

1. **提升 physiology-guided revascularization 採用率**
   - 目前 <20% → 有望大幅增加
   - 去除 pressure wire 與 adenosine 障礙

2. **簡化手術流程**
   - 不需 guide catheter（若僅 diagnostic）
   - 減少 procedure time、radiation、contrast

3. **降低成本**
   - 省去 pressure wire 耗材 + adenosine
   - 需考慮軟體授權費用

4. **適用更廣泛族群**
   - Adenosine 禁忌症患者可受益
   - 腎功能不全患者（減少 contrast）

---

# 需注意事項

> **注意 1**：Angiography-based 系統偵測到更多功能性顯著病灶（~40-43% vs ~31-37%），導致更多 PCI。是「更精準偵測」還是「過度治療」仍需釐清。

> **注意 2**：不同系統結果不可互換 — QFR 在 FAVOR III Europe 未達標，而 FFRangio 與 vFFR 成功。技術差異影響臨床結果。

> **注意 3**：目前僅有 1 年 follow-up，長期安全性與效果仍需追蹤。

> **注意 4**：多數患者為 stable coronary disease。在 STEMI 非 culprit vessel 的應用正由 AIR-STEMI trial 驗證中。

---

<!-- _class: small-text -->

# 參考文獻

1. Fearon WF, et al. Angiography-Derived FFR to Guide PCI. [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2600949)
2. Daemen J, et al. Angiography-Based Physiology to Guide Coronary Revascularization. [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2601841)
3. Tonino PAL, et al. FFR vs Angiography for Guiding PCI (FAME). [*N Engl J Med*. 2009;360:213-24.](https://doi.org/10.1056/NEJMoa0807611)
4. De Bruyne B, et al. FFR-Guided PCI for Stable CAD (FAME 2). [*N Engl J Med*. 2014;371:1208-17.](https://doi.org/10.1056/NEJMoa1408758)
5. Xu B, et al. QFR-Guided Intervention (FAVOR III China). [*Lancet*. 2021;398:2149-59.](https://doi.org/10.1016/S0140-6736(21)02248-0)
6. Andersen BK, et al. QFR vs FFR (FAVOR III Europe). [*Lancet*. 2024;404:1835-46.](https://doi.org/10.1016/S0140-6736(24)01881-9)
7. Vrints C, et al. 2024 ESC Guidelines for CCS. [*Eur Heart J*. 2024;45:3415-537.](https://doi.org/10.1093/eurheartj/ehae177)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
