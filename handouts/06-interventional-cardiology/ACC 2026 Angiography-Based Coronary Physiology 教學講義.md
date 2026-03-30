# ACC 2026: Angiography-Based Coronary Physiology — ALL-RISE & FAST III Trials 血管攝影衍生冠狀動脈生理學指引

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-03-31**
**來源：ACC 2026 Late-Breaking Clinical Trials / *New England Journal of Medicine* 2026**
**原文連結：**
- **ALL-RISE**: [*N Engl J Med*. 2026. DOI: 10.1056/NEJMoa2600949](https://doi.org/10.1056/NEJMoa2600949)
- **FAST III**: [*N Engl J Med*. 2026. DOI: 10.1056/NEJMoa2601841](https://doi.org/10.1056/NEJMoa2601841)

---

## 目錄

1. [前言：Angiography-Derived Coronary Physiology 的概念](#1-前言angiography-derived-coronary-physiology-的概念)
2. [ALL-RISE Trial — FFRangio vs Pressure Wire](#2-all-rise-trial--ffrangio-vs-pressure-wire)
3. [FAST III Trial — vFFR vs FFR](#3-fast-iii-trial--vffr-vs-ffr)
4. [兩大試驗交叉比較](#4-兩大試驗交叉比較)
5. [臨床意義與未來方向](#5-臨床意義與未來方向)
6. [結論](#6-結論)
7. [參考文獻](#參考文獻)

---

## 核心發現摘要

> **重大發現**：兩項大型 randomized noninferiority trial（ALL-RISE 與 FAST III）同時在 ACC 2026 發表並刊登於 *NEJM*，均證實 angiography-derived FFR（不需 pressure wire 或 hyperemic agent）指引 PCI 決策的臨床結果**不劣於**傳統 pressure-wire-based FFR。
>
> **臨床意義**：這些結果支持 angiography-based physiology 技術在心導管室的常規應用，有望大幅提升 physiology-guided revascularization 的採用率（目前 <20%），簡化工作流程，減少手術時間、radiation exposure 與 contrast 用量。

---

## 1. 前言：Angiography-Derived Coronary Physiology 的概念

### 傳統 Pressure-Wire-Based FFR 的限制

- **FFR (fractional flow reserve)** 是在最大充血 (maximal hyperemia) 狀態下，量測狹窄遠端與近端的平均動脈壓比值
- 多項 landmark trial（FAME、FAME 2、DEFINE-FLAIR、iFR-SWEDEHEART）已確立 FFR/iFR 在 intermediate lesion 評估中的 Class I 建議
- 然而，臨床上 pressure-wire-based physiological assessment 使用率仍 **<20%**
- 原因包括：需要 guide catheter、專用 pressure-wire system、可能需使用 adenosine 誘發 hyperemia、延長手術時間

### Angiography-Derived FFR 的原理

不同系統使用不同名稱與演算法，但核心概念相同：

| 系統名稱 | 廠商 | 演算法特色 |
|----------|------|-----------|
| **FFRangio** | CathWorks | 3D reconstruction + resistance model，由血管輪廓推算壓力梯度 |
| **vFFR** (vessel FFR) | Pie Medical Imaging | 3D-QCA + 物理定律（viscous resistance, separation loss），基於 Gould-Kirkeeide 模型 |
| **QFR** (quantitative flow ratio) | Medis / Pulse Medical | 3D-QCA + computational fluid dynamics |
| **FlashAngio** | RainMed | AI-based FFR computation |

### 共同特點

- **不需 pressure wire**：僅以常規血管攝影影像即可計算
- **不需 hyperemic agent**：多數系統不需 adenosine
- **快速計算**：中位數約 5-6 分鐘
- **高診斷準確度**：與 wire-based FFR 有良好相關性（多項 validation study 支持）

### 先前證據

- **FAVOR III China** (2021, *Lancet*)：QFR-guided revascularization 改善 1 年預後（vs angiography-guided）→ QFR 獲 Class IB 建議
- **FAVOR III Europe** (2024, *Lancet*)：QFR-guided revascularization **未能**證實 noninferiority（vs FFR-guided），事件率較高
- 不同 angiography-based physiology 系統之間存在差異，不能一概而論

---

## 2. ALL-RISE Trial — FFRangio vs Pressure Wire

### 研究資訊

- **全名**：Advancing Cath Lab Results with FFRangio Coronary Physiology Assessment (ALL-RISE)
- **作者**：Fearon WF, Jeremias A, et al.
- **DOI**：[10.1056/NEJMoa2600949](https://doi.org/10.1056/NEJMoa2600949)
- **註冊**：ClinicalTrials.gov [NCT05893498](https://clinicaltrials.gov/study/NCT05893498)
- **贊助**：CathWorks

### 研究設計

| 項目 | 內容 |
|------|------|
| **設計** | International, randomized, noninferiority trial |
| **中心數** | 59 sites（北美、歐洲、亞洲、中東） |
| **收案期間** | 2023 年 6 月至 2025 年 1 月 |
| **隨機分派** | 1:1 FFRangio vs pressure wire |
| **分層** | Clinical presentation（stable angina vs NSTE-ACS）+ 預定使用 FFR 或 NHPR |
| **主要終點** | Death, MI, or unplanned clinically indicated revascularization at 1 year |
| **Noninferiority margin** | **3.5 percentage points** |
| **Power** | >80%（one-sided P < 0.025） |

### 納入與排除條件

| 類型 | 標準 |
|------|------|
| **納入** | 年齡 ≥18 歲；invasive coronary angiography；至少一處 50-90% stenosis 需 physiological assessment |
| **排除** | Recent STEMI；NSTE-ACS culprit vessel；CABG candidate；prior CABG to study vessel；severe valvular disease；severe LV dysfunction |

### FFRangio 操作流程

1. 取得三個角度的血管攝影影像（至少相隔 30 度）
2. 系統自動 trace lumen borders，操作者可手動修正
3. 建立 3D coronary tree reconstruction
4. 計算各血管的 FFR 值
5. FFRangio ≤0.80 → 建議 PCI；>0.80 → 藥物治療

### Pressure Wire 組

- 可使用 FFR 或 nonhyperemic pressure ratio (NHPR, 即 iFR)
- FFR ≤0.80 或 NHPR ≤0.89 → PCI
- FFR 佔 55.5%，NHPR 佔 44.5%

### 基線特徵

| 特徵 | FFRangio (n=965) | Pressure Wire (n=965) |
|------|-------------------|----------------------|
| 年齡 (歲) | 68.4 ± 10.1 | 68.4 ± 10.3 |
| 女性 | 24.5% | 25.5% |
| 糖尿病 | 39.5% | 36.3% |
| 高血壓 | 78.5% | 79.9% |
| Prior PCI | 38.9% | 39.0% |
| NSTE-ACS | 9.9% | 8.8% |

### 手術特徵

| 項目 | FFRangio | Pressure Wire | 差異 |
|------|----------|---------------|------|
| Physiological assessment 成功率 | 98.5% | 98.6% | — |
| 中位 assessment 時間 | 6 min (IQR 4-10) | 8 min (IQR 5-15) | **-2 min** |
| 中位手術時間 | 39 min (IQR 21-62) | 42 min (IQR 29-60) | **-5 min** |
| 中位 fluoroscopy 時間 | 9 min (IQR 5-17) | 12 min (IQR 8-20) | **-3 min** |
| Contrast 用量 | 100 mL (IQR 52-145) | 105 mL (IQR 72-150) | **-14 mL** |
| Abnormal value (≤0.80) | 43.0% | 37.0% | — |
| PCI performed | **44.3%** | **35.4%** | OR 1.45 |

### 主要結果

| 終點 | FFRangio | Pressure Wire | HR (95% CI) |
|------|----------|---------------|-------------|
| **主要複合終點** (death, MI, unplanned revascularization) | **6.9%** | **7.1%** | **0.98 (0.70-1.39)** |
| Death from any cause | 2.3% | 2.1% | 1.16 (0.63-2.14) |
| Death from cardiac causes | 1.0% | 0.7% | 1.29 (0.48-3.46) |
| Myocardial infarction | 1.6% | 2.5% | 0.65 (0.34-1.25) |
| Spontaneous MI | 1.3% | 2.2% | 0.60 (0.29-1.22) |
| Unplanned revascularization | 4.1% | 4.6% | 0.90 (0.58-1.40) |
| Stent thrombosis | 0.2% | 0.5% | 0.50 (0.09-2.72) |
| BARC 3-5 bleeding | 0.7% | 1.5% | 0.50 (0.20-1.23) |
| Acute kidney injury | 0 | 0.1% | NA |

> **Noninferiority 達標**：Risk difference = -0.2 percentage points；upper bound of one-sided 97.5% CI = **2.1 pp** < margin 3.5 pp；**P < 0.001 for noninferiority**

### 重要次分析

- 大多數 subgroup 結果一致
- 可能例外：LAD lesion（FFRangio 較優）vs non-LAD（pressure wire 較優），可能因 statistical power 不足
- FFR vs NHPR 比較組可能有差異（需謹慎解讀）

---

## 3. FAST III Trial — vFFR vs FFR

### 研究資訊

- **全名**：Fractional Flow Reserve or 3D-Quantitative-Coronary-Angiography-Based Vessel-FFR-Guided Revascularization (FAST III)
- **作者**：Daemen J, van der Eijk JA, et al.
- **DOI**：[10.1056/NEJMoa2601841](https://doi.org/10.1056/NEJMoa2601841)
- **註冊**：ClinicalTrials.gov [NCT04931771](https://clinicaltrials.gov/study/NCT04931771)
- **贊助**：Pie Medical Imaging + Siemens Healthineers（unrestricted grants）

### 研究設計

| 項目 | 內容 |
|------|------|
| **設計** | International, open-label, randomized, noninferiority trial |
| **中心數** | 37 sites（7 個歐洲國家） |
| **收案期間** | 2021 年 11 月至 2024 年 5 月 |
| **隨機分派** | 1:1 vFFR-guided vs FFR-guided |
| **分層** | 依 participating center |
| **主要終點** | Death from any cause, any MI, or any revascularization at 1 year |
| **Noninferiority margin** | **3.0 percentage points** |
| **Power** | 80%（one-sided alpha 0.025） |
| **分析方法** | Modified intention-to-treat（full analysis set） |

### 納入與排除條件

| 類型 | 標準 |
|------|------|
| **納入** | ≥18 歲；chronic coronary syndrome、unstable angina 或 NSTE-ACS；≥1 intermediate lesion（diameter stenosis 30-80%）；native vessel ≥2.5 mm；TIMI flow grade 3 |
| **排除** | STEMI ≤72 hours；cardiogenic shock；left main disease；severe valvular disease；life expectancy <1 year；aorto-ostial lesions >50%；severe tortuosity；contraindication to adenosine；bypass graft lesions |

### vFFR 操作流程

1. 靜脈給予 intracoronary nitrates
2. 取得兩個角度的血管攝影（≥30 度間隔）
3. 以 guiding catheter tip 量測 aortic-root pressure
4. 經訓練認證的分析師在現場計算 vFFR
5. vFFR ≤0.80 → revascularization；>0.80 → defer

### 基線特徵

| 特徵 | vFFR (n=1116) | FFR (n=1095) |
|------|---------------|--------------|
| 年齡 (歲) | 67.6 ± 9.9 | 67.1 ± 9.7 |
| 女性 | 23.8% | 24.8% |
| 糖尿病 | 27.6% | 25.7% |
| 高血壓 | 72.4% | 72.5% |
| Chronic coronary syndrome | 81.6% | 80.9% |
| NSTE-ACS (unstable angina + non-STEMI) | 18.4% | 19.0% |
| Prior PCI | 35.0% | 34.7% |
| LVEF (%) | 54.1 ± 9.9 | 54.6 ± 10.2 |
| SYNTAX Score | 11.8 ± 8.2 | 11.5 ± 7.7 |
| Study lesions/patient | 1.27 ± 0.55 | 1.28 ± 0.55 |

### 手術特徵

| 項目 | vFFR | FFR |
|------|------|-----|
| Complete physiological assessment | 96.7% | 99.1% |
| Median vFFR/FFR value | 0.83 (IQR 0.74-0.89) | 0.85 (IQR 0.79-0.91) |
| Functional significance (≤0.80) | **40.9%** | **31.3%** |
| Revascularization of study lesions | **45.0%** | **36.0%** |
| Mean PCI procedure time | 55.8 ± 26.8 min | 60.9 ± 28.5 min |
| PCI procedure time difference | **-5.13 min** (95% CI: -8.55 to -1.71) | — |
| Intravascular imaging use | 10.8% | 9.0% |

### 主要結果

| 終點 | vFFR | FFR | Risk Difference (95% CI) |
|------|------|-----|--------------------------|
| **主要複合終點** (death, MI, revascularization) | **7.5%** | **7.5%** | **-0.02 pp (-2.25 to 2.21)** |
| Study-vessel failure | 4.0% | 4.6% | -0.62 pp (-2.35 to 1.10) |
| Death from any cause | 2.2% | 2.3% | — |
| Any myocardial infarction | 2.9% | 2.4% | — |
| Any revascularization | 4.2% | 4.2% | — |

> **Noninferiority 達標**：Risk difference = -0.02 pp；upper bound of 95% CI = **2.21 pp** < margin 3.0 pp；**P = 0.004 for noninferiority**

### 安全性

- 兩組 serious adverse events 發生率相似
- Intraprocedural complications：vFFR 3.7% vs FFR 6.0%（FFR 組略高，可能與 wire manipulation 相關）
- Seattle Angina Questionnaire 評分：兩組在 30 天與 1 年均相似

### 研究限制

1. Open-label design 可能影響後續臨床決策
2. ACS 患者比例較低（18.7%），限制 generalizability
3. 操作者對 pressure-wire FFR 經驗較 vFFR 豐富
4. 僅限於歐洲高流量中心
5. 追蹤僅 1 年

---

## 4. 兩大試驗交叉比較

### 試驗設計比較

| 項目 | ALL-RISE | FAST III |
|------|----------|----------|
| **Angiography-based 系統** | FFRangio (CathWorks) | vFFR (Pie Medical) |
| **對照組** | Pressure wire (FFR + NHPR) | Pressure wire (FFR only) |
| **樣本數** | 1930 | 2211 (full analysis set) |
| **地理分佈** | 全球（59 sites） | 歐洲（37 sites） |
| **Noninferiority margin** | 3.5 pp | 3.0 pp |
| **ACS 患者比例** | ~9.4% (NSTE-ACS) | 18.7% |
| **糖尿病比例** | ~37.8% | ~26.6% |
| **分析方法** | ITT | Modified ITT |

### 關鍵結果比較

| 項目 | ALL-RISE (FFRangio) | FAST III (vFFR) |
|------|---------------------|-----------------|
| **Primary endpoint (intervention)** | 6.9% | 7.5% |
| **Primary endpoint (control)** | 7.1% | 7.5% |
| **Risk difference** | -0.2 pp | -0.02 pp |
| **Upper bound CI** | 2.1 pp (< 3.5 margin) | 2.21 pp (< 3.0 margin) |
| **Noninferiority P value** | P < 0.001 | P = 0.004 |
| **Noninferiority 結果** | **達標** | **達標** |
| **Abnormal rate (intervention)** | 43.0% | 40.9% |
| **Abnormal rate (control)** | 37.0% | 31.3% |
| **PCI rate (intervention)** | 44.3% | 45.0% |
| **PCI rate (control)** | 35.4% | 36.0% |
| **PCI rate difference** | ~9 pp | ~9 pp |

### 共同發現

> **Pearl 1**：兩個試驗均成功達標 noninferiority，使用不同的 angiography-based physiology 系統，結果一致。

> **Pearl 2**：兩個試驗都觀察到 angiography-based physiology 組有較高的 abnormal value rate 與 PCI rate（差約 9 percentage points），但未導致更多不良事件。

> **Pearl 3**：Angiography-based assessment 減少了手術時間（ALL-RISE: -5 min procedure, -3 min fluoroscopy）與 contrast 用量（ALL-RISE: -14 mL），流程更為簡化。

### 與 FAVOR III Europe 的差異

- FAVOR III Europe（2024, *Lancet*）使用 **QFR** (quantitative flow ratio)，未能達到 noninferiority
- ALL-RISE 作者指出：QFR 計算需要更多操作者互動與手動調整，site-to-core lab 間變異較大
- FFRangio 在不同中心間的一致性較高
- 結論：**不同 angiography-based physiology 系統不可互換**，需個別驗證

---

## 5. 臨床意義與未來方向

### 臨床實務影響

1. **提升 physiology-guided revascularization 採用率**：去除 pressure wire 與 adenosine 的障礙，預期可大幅提升使用率（目前 <20%）
2. **簡化工作流程**：不需要 guide catheter（若僅做 diagnostic catheterization）、不需專用 wire、不需藥物誘發 hyperemia
3. **減少手術風險**：減少 procedure time、fluoroscopy time、contrast 用量 → 對腎功能不全患者尤為重要
4. **降低成本**：省去 pressure wire 耗材與 adenosine 藥費（但需考慮軟體授權費用）

### 需注意事項

> **Pearl 4**：Angiography-based systems 傾向於偵測到更多「功能性顯著」病灶（~40-43% vs ~31-37%），導致更多 PCI。是否代表「過度治療」或「更精準偵測」仍需進一步研究。

> **Pearl 5**：目前證據支持 FFRangio 與 vFFR，但 **不能** 將結果推論到所有 angiography-based systems（尤其 FAVOR III Europe 中 QFR 未能達標）。

### 未來研究方向

1. **更長追蹤**：目前均為 1 年結果，需要 3-5 年 follow-up
2. **ACS 患者**：ALL-RISE 的 AIR-STEMI trial 正在進行 STEMI 非 culprit vessel 評估
3. **Cost-effectiveness analysis**：FAST III 已規劃 prespecified 分析
4. **Head-to-head comparison**：不同 angiography-based systems 之間的直接比較
5. **AI integration**：未來可能結合 deep learning 進一步提升準確度與自動化程度
6. **Guideline update**：預期 ESC 與 ACC/AHA guidelines 將更新 angiography-based physiology 建議等級

---

## 6. 結論

1. **ALL-RISE**：在 intermediate coronary lesion 的 physiological assessment 中，FFRangio (CathWorks) 指引 PCI 決策 **不劣於** pressure-wire-based strategy，1 年 composite endpoint 為 6.9% vs 7.1%（P < 0.001 for noninferiority）。
2. **FAST III**：vFFR (Pie Medical) 指引的 revascularization strategy **不劣於** FFR-guided strategy，1 年 composite endpoint 為 7.5% vs 7.5%（P = 0.004 for noninferiority）。
3. 兩項試驗一致支持 angiography-derived physiology 可替代 pressure wire，有望成為心導管室 physiological assessment 的新標準工具。

---

## 參考文獻

1. Fearon WF, Jeremias A, Witberg G, et al. Angiography-Derived Fractional Flow Reserve to Guide PCI. [*N Engl J Med*. 2026. DOI: 10.1056/NEJMoa2600949.](https://doi.org/10.1056/NEJMoa2600949)

2. Daemen J, van der Eijk JA, Barbierato M, et al. Angiography-Based Physiology to Guide Coronary Revascularization. [*N Engl J Med*. 2026. DOI: 10.1056/NEJMoa2601841.](https://doi.org/10.1056/NEJMoa2601841)

3. Tonino PAL, De Bruyne B, Pijls NHJ, et al. Fractional Flow Reserve versus Angiography for Guiding Percutaneous Coronary Intervention. [*N Engl J Med*. 2009;360:213-24.](https://doi.org/10.1056/NEJMoa0807611)

4. De Bruyne B, Fearon WF, Pijls NHJ, et al. Fractional Flow Reserve-Guided PCI for Stable Coronary Artery Disease. [*N Engl J Med*. 2014;371:1208-17.](https://doi.org/10.1056/NEJMoa1408758)

5. Davies JE, Sen S, Dehbi H-M, et al. Use of the Instantaneous Wave-Free Ratio or Fractional Flow Reserve in PCI. [*N Engl J Med*. 2017;376:1824-34.](https://doi.org/10.1056/NEJMoa1700445)

6. Gotberg M, Christiansen EH, Gudmundsdottir IJ, et al. Instantaneous Wave-Free Ratio versus Fractional Flow Reserve to Guide PCI. [*N Engl J Med*. 2017;376:1813-23.](https://doi.org/10.1056/NEJMoa1616540)

7. Xu B, Tu S, Song L, et al. Angiographic Quantitative Flow Ratio-Guided Coronary Intervention (FAVOR III China): A Multicentre, Randomised, Sham-Controlled Trial. [*Lancet*. 2021;398:2149-59.](https://doi.org/10.1016/S0140-6736(21)02248-0)

8. Andersen BK, Sejr-Hansen M, Maillard L, et al. Quantitative Flow Ratio versus Fractional Flow Reserve for Coronary Revascularisation Guidance (FAVOR III Europe): A Multicentre, Randomised, Non-Inferiority Trial. [*Lancet*. 2024;404:1835-46.](https://doi.org/10.1016/S0140-6736(24)01881-9)

9. Fearon WF, Achenbach S, Engstrom T, et al. Accuracy of Fractional Flow Reserve Derived from Coronary Angiography. [*Circulation*. 2019;139:477-84.](https://doi.org/10.1161/CIRCULATIONAHA.118.037350)

10. Masdjedi K, van Zandvoort LJC, Balbi MM, et al. Validation of a Three-Dimensional Quantitative Coronary Angiography-Based Software to Calculate Fractional Flow Reserve: The FAST Study. [*EuroIntervention*. 2020;16:591-9.](https://doi.org/10.4244/EIJ-D-19-00466)

11. Masdjedi K, Tanaka N, Van Belle E, et al. Vessel Fractional Flow Reserve (vFFR) for the Assessment of Stenosis Severity: The FAST II Study. [*EuroIntervention*. 2022;17:1498-505.](https://doi.org/10.4244/EIJ-D-21-00471)

12. Vrints C, Andreotti F, Koskinas KC, et al. 2024 ESC Guidelines for the Management of Chronic Coronary Syndromes. [*Eur Heart J*. 2024;45:3415-537.](https://doi.org/10.1093/eurheartj/ehae177)

13. Koo B-K, Hu X, Kang J, et al. Fractional Flow Reserve or Intravascular Ultrasonography to Guide PCI. [*N Engl J Med*. 2022;387:779-89.](https://doi.org/10.1056/NEJMoa2201546)

14. Smits PC, Abdel-Wahab M, Neumann F-J, et al. Fractional Flow Reserve-Guided Multivessel Angioplasty in Myocardial Infarction. [*N Engl J Med*. 2017;376:1234-44.](https://doi.org/10.1056/NEJMoa1701067)

---

*本文件僅供醫療專業人員教學參考，臨床決策請結合個案情況。*
