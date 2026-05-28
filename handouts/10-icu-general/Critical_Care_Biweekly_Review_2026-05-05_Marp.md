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
  section.lead p, section.lead strong, section.lead a { color: #dfe6e9; }
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
  h2 { color: #0072bc; font-size: 0.85em; }
  h3 { color: #555555; }
  table { font-size: 0.7em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.85em;
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
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.78em; }
  section.ref { font-size: 0.6em; }
  section.ref h1 { font-size: 1.4em; }
  section.abbr { font-size: 0.55em; }
  section.abbr h1 { font-size: 1.3em; }
  section.abbr table { font-size: 1em; }
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-05-05'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧

## 2026-04-08 ～ 2026-05-05（4 週補回顧）

**謝慕揚 MD, PhD, FESC** | 2026-05-05

涵蓋：ICM (Intensive Care Medicine)、Critical Care、CCM (Critical Care Medicine)、Lancet Respir Med

---

<!-- _class: abbr -->

# 常用縮寫對照（一）

| 縮寫 | 全名 |
|------|------|
| RCT | Randomized Controlled Trial 隨機對照試驗 |
| OR / aOR | (Adjusted) Odds Ratio 校正勝算比 |
| HR | Hazard Ratio 風險比 |
| CI / CrI | Confidence / Credible Interval 信賴區間 |
| IPD-MA | Individual Participant Data Meta-Analysis |
| NMA | Network Meta-Analysis 網絡統合分析 |
| ICU / PICU | Intensive Care Unit / Pediatric ICU |
| ED / NHS | Emergency Department / National Health Service |
| ARDS / AHRF / ARF | Acute Resp Distress Synd / Acute Hypoxaemic / Acute Resp Failure |
| NIV / IMV | Non-Invasive / Invasive Mechanical Ventilation |
| CPAP / HFNC / NIPPV | Continuous Positive Airway Pressure / High-Flow Nasal Cannula / Non-Invasive Positive Pressure Ventilation |
| SOT | Standard Oxygen Therapy（呼吸文獻）／Solid Organ Transplant（移植） |
| PaCO₂ / PaO₂ / FiO₂ | Arterial CO₂ / O₂ partial pressure / Fraction of inspired O₂ |

---

<!-- _class: abbr -->

# 常用縮寫對照（二）

| 縮寫 | 全名 |
|------|------|
| AKI / AKD / CKD | Acute Kidney Injury / Disease, Chronic Kidney Disease |
| RRT / CKRT / UF | Renal Replacement Therapy / Continuous Kidney Replacement / Ultrafiltration |
| KDIGO | Kidney Disease: Improving Global Outcomes |
| MP / VILI | Mechanical Power / Ventilator-Induced Lung Injury |
| ECCO₂R / miECCO₂R | (Minimally Invasive) Extracorporeal CO₂ Removal |
| TBI / ICP / ICH | Traumatic Brain Injury / Intracranial Pressure / Hypertension |
| TCD / ONSD / EEG / MRI | Transcranial Doppler / Optic Nerve Sheath Diameter / EEG / MRI |
| PCT / NEWS2 | Procalcitonin / National Early Warning Score 2 |
| SOFA / APACHE-II | Sequential Organ Failure Assessment / Acute Physiology And Chronic Health Eval II |
| EAA / PMX | Endotoxin Activity Assay / Polymyxin B haemoadsorption |
| SSC / SOC | Surviving Sepsis Campaign / Standard of Care |
| PE / PA | Pulmonary Embolism / Pulmonary Artery |
| FDA / PMA | Food and Drug Administration / Premarket Approval |
| WGS / RR-TB / AI | Whole Genome Sequencing / Rifampicin-Resistant TB / Artificial Intelligence |
| GMR / AUC / aRD | Geometric Mean Ratio / Area Under Curve / Adjusted Risk Difference |

---

# 重點摘要 (Top Pearls)

> 1. **Tigris** — Polymyxin B (PMX) 在 endotoxic septic shock 後驗益處 95.3%（28d）/ 99.4%（90d）— 但僅 157 人、open-label
> 2. **PRONTO** — Procalcitonin (PCT) + NEWS2 主要終點 negative，mortality 卻 −3.12%（機制未明）
> 3. **AHRF NMA** — CPAP（OR 0.45）/ HFNC（OR 0.61）皆減插管；CPAP 也減死亡
> 4. **Thille NIV** — 高風險、無 hypercapnia 病人，NIV+HFNC 7d 再插管 11.8% vs 17.6%
> 5. **MP score** — 拋棄單一閾值；compliance + duration 共同決定 VILI（ventilator-induced lung injury）風險

---

# 重點摘要（續）

> 6. **AKI biomarker bundle** — KDIGO bundle + biomarker enrichment：AKI 17.7% vs 27.1%（OR 0.55）
> 7. **NUTRIREA-3 post hoc** — 低熱量低蛋白餵食對腎臟安全
> 8. **Brain temperature** — 從強制低溫轉向「fever 偵測 + normothermia」
> 9. **BESS** — 嬰兒 bronchiolitis 用 surfactant **無效**
> 10. **Immunocompromised ARF** — 30 天死亡 47.3%；HFNC 為保護因子

---

<!-- _class: divider -->

# 1. Sepsis 與血液淨化

---

# Tigris：PMX 在 endotoxic septic shock — Phase 3 RCT
## [Neyra JA, et al. Lancet Respir Med 2026;14(5)](https://doi.org/10.1016/S2213-2600(26)00047-0) | [PMID 41887242](https://pubmed.ncbi.nlm.nih.gov/41887242/)

- **設計**：19 個美國醫院、open-label、Bayesian phase 3、2:1 randomization
- **族群**：成人 septic shock + multiorgan failure + **Endotoxin Activity Assay (EAA) 0.60-0.89**
- **介入**：PMX (Polymyxin B haemoadsorption) 兩次 (90-120 min, 22h apart) vs Standard of Care (SOC)
- **N**：157（106 / 51） — 篩選 14,890 人才入選
- **主要終點**：28-day mortality

---

# Tigris：結果
## [Neyra JA, et al. Lancet Respir Med 2026](https://doi.org/10.1016/S2213-2600(26)00047-0)

| 終點 | PMX | Control | OR (95% CrI) | Posterior P(benefit) |
|------|-----|---------|--------------|---------------------|
| **28-day death** | **39%** | **45%** | **0.67 (0.39-1.08)** | **95.3%** |
| 90-day death | — | — | 0.54 (0.32-0.87) | 99.4% |
| Serious AE (Adverse Event) | 30% | 22% | diff −8% | — |

> **解讀重點**：Bayesian 先驗來自 EUPHRATES 次族群分析；族群高度 enriched（EAA 0.60-0.89）— **不可外推到無 EAA 測量的一般 sepsis**

---

# PRONTO：PCT + NEWS2 在 ED Sepsis
## [Todd S, et al. Lancet Respir Med 2026;14(5)](https://doi.org/10.1016/S2213-2600(25)00433-3) | [PMID 41881047](https://pubmed.ncbi.nlm.nih.gov/41881047/)

- 英國 NHS（National Health Service）17 Trust、20 Emergency Department (ED)
- **n=7,667** randomised
- 比較：PCT (Procalcitonin) + NEWS2 (National Early Warning Score 2) algorithm vs 標準 NEWS2
- **共同主要終點**：3h IV (intravenous) ABX (antibiotics)（superiority）+ 28d mortality（NI margin 2.5%）

| 終點 | PCT 組 | 標準組 | 結果 |
|------|--------|--------|------|
| **3h IV ABX** | 48.4% | 48.2% | **無差異 (p=0.95)** |
| **28d 死亡** | **13.6%** | **16.6%** | **aRD −3.12%, p=0.0009** |

> **mortality 益處的機制無解** — 作者明示「further research needed」；PCT 僅在 64.7% 病人實際納入決策

---

<!-- _class: divider -->

# 2. Mechanical Ventilation

---

# AHRF 非侵襲呼吸支持 NMA
## [Lee KG, et al. Lancet Respir Med 2026](https://doi.org/10.1016/S2213-2600(26)00039-1) | [PMID 42034114](https://pubmed.ncbi.nlm.nih.gov/42034114/)

44 RCT，9,704 人；vs Standard Oxygen Therapy (SOT)：

| 介入 | Intubation OR | Mortality OR | GRADE |
|------|--------------|--------------|-------|
| **CPAP** (Continuous Positive Airway Pressure) | **0.45 (0.27-0.72)** ↓ | **0.73 (0.55-0.95)** ↓ | Mod / Low |
| **HFNC** (High-Flow Nasal Cannula) | 0.61 (0.42-0.86) ↓ | 0.83 (0.66-0.98) ↓ | Mod / Low |
| **Bilevel NIPPV** (Non-Invasive Positive Pressure Vent) | 0.60 (0.39-0.89) ↓ | 0.93 (0.71-1.17) — | Mod / Low |

> **CPAP 在減插管最強**；CPAP 與 HFNC 為 mortality 兩個最有依據選項

---

# Extubation 後預防性 NIV — 非 hypercapnia 也有用
## [Thille AW, et al. ICM 2026](https://doi.org/10.1007/s00134-026-08396-4) | [PMID 41973108](https://pubmed.ncbi.nlm.nih.gov/41973108/)

- 兩 RCT post hoc；n=829（高風險、PaCO₂ ≤45 mmHg）
- **NIV (Non-Invasive Ventilation) + HFNC vs HFNC alone**

| 終點 | NIV+HFNC | HFNC only | Δ |
|------|----------|-----------|---|
| **7d 再插管** | **11.8%** | **17.6%** | **−5.8% (p=0.021)** |

> 高齡 (>65) 或心肺合併症病人即使無 hypercapnia 仍可受益於 NIV

---

# Risk-Adjusted Mechanical Power Score
## [Lijović L, et al. Crit Care Med 2026](https://doi.org/10.1097/CCM.0000000000007129) | [PMID 41945715](https://pubmed.ncbi.nlm.nih.gov/41945715/)

- n=2,150 中-重度 ARDS（Acute Respiratory Distress Syndrome；NL + US 兩大資料集）
- **High-compliance lung**：dose-response，10 J/min 起 hazard ↑，**累積有害**
- **Low-compliance lung**：風險集中 11-20 J/min 窄帶、**無累積效應**
- AUC (Area Under Curve) **0.863**（XGBoost / eXtreme Gradient Boosting）

> 「單一 MP (Mechanical Power) 閾值」已不足夠 — 需 power × duration × compliance 三維度評估

---

<!-- _class: divider -->

# 3. AKI / Renal / Nutrition

---

# 高風險術後 AKI：KDIGO Bundle + Biomarker
## [von Groote T, et al. ICM 2026](https://doi.org/10.1007/s00134-026-08399-1) | [PMID 42007986](https://pubmed.ncbi.nlm.nih.gov/42007986/)

- 4 RCT IPD-MA（Individual Participant Data Meta-Analysis）；**n=1,851**
- 介入：KDIGO (Kidney Disease: Improving Global Outcomes) bundle + biomarker enrichment

| 終點 | Intervention | Control | OR (95% CI) |
|------|-------------|---------|-------------|
| **中-重度 AKI (KDIGO≥2) 72h** | **17.7%** | **27.1%** | **0.55 (0.44-0.70)** |

I² = 0%（完全一致）；p<0.0001

> 高風險術後病人若有 enrichment biomarker，KDIGO bundle 應為標準

---

# NUTRIREA-3 Post Hoc：低熱量低蛋白不傷腎
## [Schleef M, et al. ICM 2026](https://doi.org/10.1007/s00134-026-08369-7) | [PMID 41989569](https://pubmed.ncbi.nlm.nih.gov/41989569/)

- 3,036 機械通氣 + shock；前 7 天
- 低（6 kcal/kg + 0.2-0.4g protein/kg/d）vs 標準（25 kcal/kg + 1.0-1.3g/kg/d）

| 終點 | 低熱量 | 標準 | HR (Hazard Ratio, 95% CI) |
|------|--------|------|---------------------------|
| **AKD (Acute Kidney Disease) during ICU** | 44.6% | 46.1% | 0.97 (0.88-1.07) |
| Peak urea | ↓ | ↑ | p=0.002 |

> 休克急性期低熱量低蛋白餵食策略**對腎臟安全**

---

<!-- _class: divider -->

# 4. 神經重症

---

# 急性腦損傷溫度管理：觀念演進
## [Lavinio A, et al. ICM 2026](https://doi.org/10.1007/s00134-026-08367-9) | [PMID 42007984](https://pubmed.ncbi.nlm.nih.gov/42007984/)

| 情境 | 過去 | 現在 |
|------|------|------|
| **TBI** (Traumatic Brain Injury) | 預防性低溫 | 僅 refractory ICH 才用 |
| **Acute vascular brain injury** | 強制低溫 | 早期 fever 偵測 + normothermia |
| **Post-cardiac arrest** | 強制 33℃ | 32-37.5℃ 任選 + 預防 fever |

> 神經 ICU 溫度管理 = **預防發燒 + maintained normothermia**
> ICH = Intracranial Hypertension（顱內高壓）

---

# Non-Invasive ICP（Intracranial Pressure）工具
## [Picetti E, et al. ICM 2026](https://doi.org/10.1007/s00134-026-08420-7) | [PMID 42043555](https://pubmed.ncbi.nlm.nih.gov/42043555/)

- **工具**：
  - TCD (Transcranial Doppler，經顱都卜勒)
  - ONSD (Optic Nerve Sheath Diameter，視神經鞘直徑)
  - Pupillometry（自動瞳孔測量）、skull compliance、time-of-flight US
- **限制**：calibration / zeroing — 絕對準確度受限
  - TCD ±7-15 mmHg；ONSD ±7-10 mmHg
- **適用**：選 invasive monitor 時機；cardiac arrest、liver failure、sepsis 後評估；**低資源地區**

---

<!-- _class: divider -->

# 5. ICU 復健與其他

---

# 重症復健標準化建議
## [Hodgson CL, et al. ICM 2026](https://doi.org/10.1007/s00134-026-08427-0) | [PMID 42059920](https://pubmed.ncbi.nlm.nih.gov/42059920/)

- **核心**：早期 awakening + mobilisation、安全（low AE rate）
- **三面向**：身體、認知、心理 — 跨 ICU、病房、社區
- **未來方向**：詳細記錄 dose（time、intensity、duration）、實作策略

> 將復健視為與抗生素、ventilation 同等的核心治療，從入院 day 1 啟動

---

# Honorable Mentions

| 試驗 / 主題 | 結論 | 連結 |
|------------|------|------|
| **BESS** infant bronchiolitis surfactant | **NEGATIVE** (n=232; IMV 64.9 vs 62.0h, GMR 1.02) | [PMID 41875912](https://pubmed.ncbi.nlm.nih.gov/41875912/) |
| Intermediate-risk PE (Pulmonary Embolism) thrombectomy timing | mortality 無差，PA 壓力較低 | [PMID 42023946](https://pubmed.ncbi.nlm.nih.gov/42023946/) |
| Immunocompromised ARF (n=9,854) | 30d mortality **47.3%**；HFNC 保護 | [PMID 41856149](https://pubmed.ncbi.nlm.nih.gov/41856149/) |
| **SOFA-2** (Sequential Organ Failure Assessment 2) | 優於 SOFA-1（兩 cohort） | [PMID 42036712](https://pubmed.ncbi.nlm.nih.gov/42036712/) |
| **SMARTT** WGS (Whole Genome Sequencing)-guided RR-TB | unfavourable outcomes ↓ | [PMID 42026006](https://pubmed.ncbi.nlm.nih.gov/42026006/) |
| miECCO₂R (minimally invasive Extracorporeal CO₂ Removal) via RRT (Renal Replacement Therapy) | feasible，PaCO₂ 71→52 in 24h | [PMID 42057044](https://pubmed.ncbi.nlm.nih.gov/42057044/) |

---

# Take Home Messages

> 1. **Sepsis**：Tigris 顯示 PMX 在高 EAA 族群可能有效，但族群極窄；PRONTO 提醒 PCT 不能取代臨床判斷

> 2. **Ventilation**：CPAP 與 HFNC 為 AHRF 兩大首選；MP 風險需考量 compliance；高風險 extubation 用 NIV+HFNC

> 3. **AKI**：KDIGO bundle + biomarker enrichment 可減半中-重度 AKI；低熱量低蛋白不傷腎

> 4. **Neurocritical**：normothermia 取代強制低溫；non-invasive ICP 為輔助工具

> 5. **Whole-ICU mindset**：復健為核心治療而非附加項目

---

<!-- _class: ref -->

# 主要參考文獻

1. [Neyra JA, et al. Tigris. *Lancet Respir Med* 2026;14(5)](https://doi.org/10.1016/S2213-2600(26)00047-0) PMID 41887242
2. [Todd S, et al. PRONTO. *Lancet Respir Med* 2026;14(5)](https://doi.org/10.1016/S2213-2600(25)00433-3) PMID 41881047
3. [Lee KG, et al. AHRF NMA. *Lancet Respir Med* 2026](https://doi.org/10.1016/S2213-2600(26)00039-1) PMID 42034114
4. [Thille AW, et al. NIV after extubation. *ICM* 2026](https://doi.org/10.1007/s00134-026-08396-4) PMID 41973108
5. [Lijović L, et al. MP score. *Crit Care Med* 2026](https://doi.org/10.1097/CCM.0000000000007129) PMID 41945715
6. [Kryvenko V, et al. miECCO₂R. *Crit Care* 2026;30(1)](https://doi.org/10.1186/s13054-026-06062-1) PMID 42057044
7. [von Groote T, et al. AKI bundle IPD-MA. *ICM* 2026](https://doi.org/10.1007/s00134-026-08399-1) PMID 42007986
8. [Murugan R, et al. UF rate trial. *Crit Care* 2026;30(1)](https://doi.org/10.1186/s13054-026-06040-7) PMID 42021350
9. [Schleef M, et al. NUTRIREA-3 post hoc. *ICM* 2026](https://doi.org/10.1007/s00134-026-08369-7) PMID 41989569
10. [Lavinio A, et al. Brain temperature. *ICM* 2026](https://doi.org/10.1007/s00134-026-08367-9) PMID 42007984

---

<!-- _class: ref -->

# 主要參考文獻（續）

11. [Picetti E, et al. Non-invasive ICP. *ICM* 2026](https://doi.org/10.1007/s00134-026-08420-7) PMID 42043555
12. [Silva S, et al. Coma stepwise. *ICM* 2026](https://doi.org/10.1007/s00134-026-08418-1) PMID 42059919
13. [Hodgson CL, et al. ICU rehabilitation. *ICM* 2026](https://doi.org/10.1007/s00134-026-08427-0) PMID 42059920
14. [Semple MG, et al. BESS. *Lancet Respir Med* 2026;14(5)](https://doi.org/10.1016/S2213-2600(26)00008-1) PMID 41875912
15. [Chiang CJ, et al. PE thrombectomy timing. *Crit Care Med* 2026](https://doi.org/10.1097/CCM.0000000000007130) PMID 42023946
16. [Azoulay E, et al. Immunocompromised ARF. *Lancet Respir Med* 2026;14(5)](https://doi.org/10.1016/S2213-2600(26)00046-9) PMID 41856149
17. [Liufu R, et al. SOFA-2. *Crit Care* 2026](https://doi.org/10.1186/s13054-026-05981-3) PMID 42036712
18. [Wei S, et al. SOFA-2 pneumonia. *Crit Care* 2026](https://doi.org/10.1186/s13054-026-06027-4) PMID 42045961
19. [Van Rie A, et al. SMARTT. *Lancet Respir Med* 2026](https://doi.org/10.1016/S2213-2600(26)00095-0) PMID 42026006
20. [Mallmann C, et al. Vasopressor weaning. *ICM* 2026](https://pubmed.ncbi.nlm.nih.gov/41973110/) PMID 41973110

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

下次回顧：2026-05-15 (排程已建立)
