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
    font-size: 22px;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 1.9em; }
  section.lead h2 { color: #b0c4de; font-size: 1.1em; }
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
    font-size: 2.2em;
    text-align: center;
  }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.5em; }
  h2 { color: #0072bc; font-size: 1.2em; }
  h3 { color: #555555; font-size: 1.05em; }
  table { font-size: 0.72em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 4px 8px; }
  td { padding: 3px 8px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.4em 0.8em;
    font-size: 0.88em;
  }
  ul, ol { margin: 0.2em 0; }
  li { margin: 0.1em 0; }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.6em;
    font-size: 0.68em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.55em; }
  section.small-text { font-size: 18px; }
footer: '謝慕揚 MD, PhD, FESC | Weekly Critical Care Review | 2026-04-17'
---

<!-- _class: lead -->

# Weekly Critical Care Journal Review
## 每週重症醫學期刊文獻回顧

**謝慕揚 MD, PhD, FESC**
2026-04-10 至 2026-04-17
資料來源：NEJM, ICM, Critical Care, CCM, Resuscitation, Chest, AJRCCM

---

# 核心發現摘要

- **SuDDICU Trial (NEJM)**：最大型 SDD 國際 RCT — 90-day mortality OR 0.91 (0.82-1.02), **未達統計顯著**；但 32 篇 RCT meta-analysis 顯示 **99.3% 機率有益**
- **NUTRIREA-3 Post Hoc (ICM)**：Low calorie/protein 對腎功能的影響分析
- **Prophylactic NIV (ICM)**：High-risk non-hypercapnic 患者拔管後 NIV 策略
- **SOFA-2 外部驗證 (Crit Care)**：AUROC 與 SOFA-1 相當 (0.646 vs 0.641)
- **TEE-Guided CPR (Resuscitation)**：49% 患者標準按壓位置壓到 aortic valve
- **Impella Volume-Outcome (Crit Care)**：高手術量中心結果較佳

> **趨勢**：SDD 爭議再起；MCS volume-outcome 持續累積；CPR physiology-guided 個人化方向明確

---

# Top Picks 精選文獻

| # | 期刊 | 文獻標題 | 主題 |
|---|------|---------|------|
| 1 | NEJM | SuDDICU: Selective Decontamination of Digestive Tract | SDD 與 ICU 死亡率 |
| 2 | ICM | Prophylactic NIV After Extubation (Non-Hypercapnic) | 拔管後 NIV |
| 3 | ICM | NUTRIREA-3 Post Hoc: Calorie/Protein & Renal | ICU 營養與腎功能 |
| 4 | Crit Care | ARDS: Measuring & Managing Pulmonary Edema | ARDS 肺水腫 |
| 5 | Crit Care | SOFA-2 vs SOFA: External Validation | SOFA-2 驗證 |
| 6 | Crit Care | Impella Volume and Outcomes | Impella volume-outcome |
| 7 | Resuscitation | TEE-Guided CPR: Compression Location | TEE 引導 CPR |
| 8 | Resuscitation | IV vs IO in OHCA: Long-Term RCT | IO vs IV 長期結果 |

---

<!-- _class: divider -->

# SuDDICU Trial — NEJM

---

# SuDDICU: Selective Digestive Decontamination

## Crossover Cluster RCT — SDD n=2791, Control n=3191

| 終點 | SDD | Control | 效果量 |
|------|-----|---------|--------|
| **90-Day Mortality** | **27.0%** | **29.1%** | **OR 0.91 (0.82-1.02) — NS** |
| MRO Acquisition | 20.9% | 32.5% | 顯著降低 |
| Antibiotic Resistance | — | — | 未增加 |

- 主要終點 **negative** — 90-day mortality 未達統計顯著
- 次要終點：SDD 組 multi-resistant organism 獲取率 **顯著較低**
- **未發現 SDD 增加抗藥性** — 回應長期 AMR 顧慮

> **Pearl**：單一試驗 negative，但別急著下結論 — 看累積 meta-analysis

---

# SuDDICU: Meta-Analysis 累積證據

## 32 篇 RCT Bayesian Meta-Analysis

- Pooled RR **0.91** (credible interval 0.82-0.99)
- **99.3% posterior probability of benefit**
- 同期社論：「Finding the Way Forward」([DOI: 10.1056/NEJMe2602823](https://doi.org/10.1056/NEJMe2602823))

> **Pearl**：SuDDICU 是 SDD 最大型 RCT，primary endpoint negative，但 Bayesian meta-analysis 顯示 99.3% 機率有益。關鍵問題不再是「有沒有效」，而是「**在什麼環境下值得實施**」— ICU endemic resistance patterns 不同

- **臨床決策**：應基於 totality of evidence，而非單一 RCT
- AMR 疑慮未獲證實 — 此為重要發現

---

<!-- _class: divider -->

# 感染與 Sepsis / ARDS 與呼吸

---

# Infection & Sepsis 重點摘要

## Sepsis/ARDS Heterogeneity & Sepsis Outcomes

- **Sepsis/ARDS Phenotyping Review** (Crit Care)
  - Phenotype（臨床表現型）→ Subphenotype（hypo-/hyper-inflammatory）→ Endotype（分子機制型）
  - Precision medicine 在重症醫學的應用方向
  - Biomarker-driven 治療選擇改善 RCT 設計
- **Sepsis Outcomes & Cultural/Linguistic Diversity** (CCM)
  - 語言障礙影響 sepsis 早期識別與溝通
- **Vasopressor Weaning in Septic Shock** (ICM Commentary)
  - 2026 Surviving Sepsis Campaign **缺乏** vasopressor weaning 具體建議
  - 何時、如何減量缺乏實證共識

---

# ARDS 與呼吸治療

## Pulmonary Edema, ARDS Resolution, Prophylactic NIV

- **ARDS Pulmonary Edema Review** (Crit Care)
  - 評估：imaging, EVLW measurement, biomarkers, lung ultrasound B-lines
  - 管理：fluid restriction, diuretics, albumin, PEEP optimization
  - 個人化 fluid management 是未來方向

- **Defining ARDS Resolution** (CCM Commentary)
  - Berlin definition 定義了 ARDS 診斷，但何時算「**已解決**」缺乏標準化
  - 影響臨床試驗終點設計與日常判斷

- **Prophylactic NIV After Extubation** (ICM)
  - High-risk reintubation 但 **non-hypercapnic** 患者
  - Post-extubation NIV 在 hypercapnic 已有定論，non-hypercapnic 是知識缺口

---

<!-- _class: divider -->

# 血流動力學與休克 / 機械循環支持

---

# 血流動力學與休克

## Norepinephrine Dosing & Vasopressor Weaning

- **Weight-Normalized NE Dosing & BMI-Dependent Vasopressin Response** (Crit Care)
  - NE weight-based dosing 在不同 BMI 患者的影響
  - Obese 患者 vasopressor dosing 策略可能需調整
  - 是否應使用 ideal body weight 計算劑量？

- **Vasopressor Weaning** (ICM Commentary)
  - 起始劑量有詳盡指引，但減量缺乏實證共識
  - 2026 SSC guidelines 的重要缺口

> **Pearl**：Vasopressor dosing 的個人化 — 不只是「開多少」，還包括「何時減、如何減」

---

# 機械循環支持 (MCS)

## Impella Volume-Outcome, VA-ECMO, Complications

| 文獻 | 期刊 | 重點發現 |
|------|------|---------|
| Impella Volume & Outcomes | Crit Care | 高手術量中心結果較佳，支持 **regionalization** |
| Impella Bleeding/Thrombosis | Crit Care | 歐洲多中心真實世界出血/血栓事件分析 |
| VA-ECMO Decannulation | Crit Care | MANTA vs Femoseal — percutaneous 可避免外科 |
| Prehospital ECPR | Crit Care | 院前 ECPR 可行性，logistics 為主要瓶頸 |

> **Pearl**：Impella 在 cardiogenic shock 的證據仍在演進。Volume-outcome relationship 提示：**不是每個中心都適合執行 Impella** — 經驗量是決定結果的重要因素

- Impella anticoagulation protocol 標準化是臨床重要挑戰
- Percutaneous VA-ECMO decannulation 需適當 vascular closure device 選擇

---

<!-- _class: divider -->

# 心臟停止與復甦醫學

---

# TEE-Guided CPR

## Hemodynamic Effects of Adjusting Compression Location
### Chen CC et al. (Taiwan) — Resuscitation

- **設計**：Prospective observational, 76 patients
- **關鍵發現**：37/76 (**49%**) 標準按壓位置壓到 aortic valve

| 分組 | N | 結果 |
|------|---|------|
| 有 Aortic Valve Compression on TEE | 37 | 較差預後 |
| 無 Aortic Valve Compression | 39 | **較佳預後** |

- 調整按壓位置避免 AV compression → 血流動力學效果較佳
- 支持 **physiology-guided, personalized CPR** 概念

> **Pearl**：近半數患者在標準 CPR 位置下壓到 aortic valve — 可能抵消胸部按壓產生的前向血流。TEE-guided CPR 是未來重要方向

---

# IV vs IO & Immunomodulation & Post-Arrest QoL

## Cardiac Arrest 其他重要研究

- **IV vs IO Vascular Access in OHCA — Long-Term RCT** (Resuscitation)
  - 1,479 patients — IO 比 IV 更快建立、更快給藥
  - 30-day survival: IO 12% vs IV 10% — **NS**
  - 30-day favorable neuro: IO 9% vs IV 8% — RR 1.16 (0.83-1.62) — **NS**
  - IO 速度優勢 **未轉化為存活優勢**

- **Immunomodulation Post-Arrest Brain Injury** (Resuscitation — SR & MA)
  - Steroids, IL-1 blockade 等免疫調節策略
  - 目前證據 **不足以推薦常規使用**

- **Quality of Life After OHCA: Age Matters** (Resuscitation)
  - 年齡影響 OHCA 存活者生活品質

- **Temperature Management After IHCA** (CCM Commentary)
  - TTM3 後策略持續演變，IHCA 最佳溫度目標仍不確定

---

# Cardiac Arrest：其他發現

## EEG, PICS, Hospital Variability

- **Self-Adhesive EEG vs Conventional EEG** (Resuscitation)
  - Postanoxic coma 監測 — 簡化流程的可能
- **Physical Impairment as Dominant PICS After IHCA** (Resuscitation)
  - Physical impairment 是 PICS 主要成分
- **Between-Hospital Variability in Cardiac Arrest Outcomes** (Resuscitation)
  - 醫院間結果變異性大，支持品質改善標準化
- **Early Colonoscopy After ECPR** (ICM)
  - ECPR 後腸道缺血是重要併發症，早期偵測可改善預後
- **MI-Related OHCA Phenotypes** (Resuscitation)
  - 不同 phenotype 需不同風險分層

---

<!-- _class: divider -->

# 營養 / SOFA-2 / 神經重症 / ICU 超音波

---

# NUTRIREA-3 Post Hoc & SOFA-2 驗證

## ICU 營養與器官衰竭評估

- **NUTRIREA-3 Post Hoc: Low vs Standard Calorie/Protein & Renal** (ICM)
  - 原始試驗：61 French ICUs, ventilated + shock
  - Low (6 kcal/kg, 0.2-0.4 g/kg) vs Standard (25 kcal/kg, 1.0-1.3 g/kg)
  - Post hoc 聚焦 renal dysfunction outcomes

> **Pearl**：ICU 早期營養趨勢「less is more」— 急性期過度餵食可能抑制 autophagy、造成高血糖與 azotemia

- **SOFA-2 External Validation** (Crit Care — Iwasaki Y et al., Japan)

| 指標 | SOFA-2 | SOFA-1 |
|------|--------|--------|
| **AUROC for Mortality** | **0.646** | **0.641** |
| Resp/CV/Liver Domain | 較低 | — |
| Kidney Domain | **較高** | — |

- SOFA-2 可替代 SOFA-1，但分數 **不可直接互換**

---

# 神經重症 / Delirium / ICU 超音波

## Neuromonitoring, Circadian Rhythm, Ultrasound

- **Cerebral Microdialysis: Delphi Consensus** (Crit Care)
  - 標準化 lactate/pyruvate ratio, glucose, glutamate 監測
  - Advanced neuromonitoring 的重要工具

- **Circadian Melatonin Rhythms & Delirium** (Crit Care)
  - ICU 環境干擾 circadian rhythm → 增加 delirium 風險
  - 支持 light-dark cycle optimization 策略

- **Delirium Disparities in Critically Ill Latinos** (CCM)
  - 語言/文化因素影響 delirium 篩檢與診斷正確性

- **The Ultrasound of Silence** (ICM — Slama M, Vignon P, Balik M)
  - 何時 **不做** 超音波也是一種智慧
  - POCUS 普及帶來過度檢查風險，需 clinical judgment 平衡

---

# Take-Home Messages

1. **SuDDICU**：單一 RCT negative，但 Bayesian meta-analysis 99.3% probability of benefit — 決策應基於 **totality of evidence**
2. **ARDS**：Pulmonary edema 量化（LUS, EVLW）是個人化 fluid management 關鍵；ARDS resolution 定義仍待建立
3. **TEE-Guided CPR**：49% 患者標準按壓壓到 aortic valve — physiology-guided resuscitation 是未來方向
4. **IO vs IV**：IO 速度優勢未轉化為存活優勢，兩者均為合理選擇
5. **Impella**：Volume-outcome relationship 支持 regionalization
6. **NUTRIREA-3**：ICU 早期「less is more」— 低熱量/低蛋白策略持續受關注
7. **SOFA-2**：外部驗證與 SOFA-1 相當，但分數不可直接互換
8. **輸血**：「Treat the patient, not the number」— Hb threshold 需結合生理指標

---

<!-- _class: small-text -->

# 參考文獻 (1/2)

1. SuDDICU Investigators. Selective Decontamination of the Digestive Tract in Intensive Care. [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2506398)
2. Editorial. Selective Digestive Decontamination — Finding the Way Forward. [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMe2602823)
3. Thille AW, et al. Prophylactic NIV After Extubation in High-Risk Non-Hypercapnic Patients. [*Intensive Care Med*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41973108/)
4. Schleef M, et al. NUTRIREA-3 Post Hoc: Low vs Standard Calorie/Protein and Renal Dysfunction. [*Intensive Care Med*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41989569/)
5. Schippers JR, et al. ARDS: Measuring and Managing Pulmonary Edema. [*Crit Care*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41968319/)
6. Iwasaki Y, et al. SOFA-2 vs SOFA: External Validation. [*Crit Care*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41968305/)
7. Nishimoto Y, et al. Impella Procedural Volume and Outcomes. [*Crit Care*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41964018/)
8. Chen CC, et al. TEE-Guided CPR: Adjusting Compression Location. [*Resuscitation*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41985614/)
9. Vallentin MF, et al. IV vs IO Vascular Access in OHCA: Long-Term RCT. [*Resuscitation*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41967754/)
10. Chiumello D, Rocco PRM. Defining ARDS Resolution. [*Crit Care Med*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41989175/)

---

<!-- _class: small-text -->

# 參考文獻 (2/2)

11. Zhao L, et al. Sepsis/ARDS: Phenotype, Subphenotype, and Endotype. [*Crit Care*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41964051/)
12. Wendel-Garcia PD, et al. Weight-Normalized NE Dosing and BMI-Dependent Vasopressin Response. [*Crit Care*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41981631/)
13. Ughetto A, et al. Impella Bleeding/Thrombotic Events: European Multicenter. [*Crit Care*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41975435/)
14. Berg E, et al. VA-ECMO Percutaneous Decannulation: MANTA & Femoseal. [*Crit Care*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41968311/)
15. Dhingra SJ, et al. Immunomodulation Post-Cardiac Arrest Brain Injury: SR & MA. [*Resuscitation*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41974223/)
16. Helmy A, et al. Cerebral Microdialysis: Delphi Consensus. [*Crit Care*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41975464/)
17. Hunziker D, et al. Circadian Melatonin Rhythms and Delirium. [*Crit Care*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41963961/)
18. Slama M, Vignon P, Balik M, et al. The Ultrasound of Silence. [*Intensive Care Med*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41989568/)
19. Fogagnolo A, Spadaro S. Transfusion: Hemoglobin or Patients? [*Intensive Care Med*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41984148/)
20. Mallmann C, et al. Vasopressor Weaning in Septic Shock. [*Intensive Care Med*. 2026.](https://pubmed.ncbi.nlm.nih.gov/41973110/)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
