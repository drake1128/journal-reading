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
    padding: 40px 50px;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 1.8em; }
  section.lead h2 { color: #b0c4de; font-size: 1.1em; }
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
    font-size: 2.2em;
    text-align: center;
  }
  h1 { color: #ba181b; border-bottom: 2px solid #ba181b; padding-bottom: 0.15em; font-size: 1.35em; margin-bottom: 0.3em; margin-top: 0; }
  h2 { color: #0072bc; font-size: 0.85em; margin: 0.25em 0; font-weight: normal; }
  h3 { color: #555555; font-size: 0.95em; margin: 0.4em 0 0.3em 0; }
  p { margin: 0.35em 0; }
  table { font-size: 0.78em; width: 100%; margin: 0.4em 0; border-collapse: collapse; }
  th { background-color: #0072bc; color: white; padding: 4px 7px; }
  td { padding: 3px 7px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.4em 0.9em;
    font-size: 0.85em;
    margin: 0.4em 0;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 6px;
    padding: 0.5em;
    font-size: 0.7em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 1px 5px; border-radius: 4px; font-size: 0.88em; }
  strong { color: #ba181b; }
  a { color: #0072bc; text-decoration: underline; }
  footer { color: #787878; font-size: 0.5em; }
  ul, ol { font-size: 0.92em; margin: 0.3em 0; padding-left: 1.4em; }
  li { margin: 0.15em 0; }
  section.small-text { font-size: 19px; }
  section.small-text table { font-size: 0.72em; }
  section.ref { font-size: 17px; }
  section.ref ol { font-size: 1em; }
  section.ref li { margin: 0.2em 0; }
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review 2026-05-15 | 讀書會共筆'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧
## Biweekly Critical Care Literature Review

**2026-05-06 ～ 2026-05-15**

讀書會共筆整理人：謝慕揚 MD, PhD, FESC

涵蓋：ICM ｜ Critical Care ｜ CCM ｜ AJRCCM ｜ Lancet Respir Med ｜ Chest ｜ Resuscitation

[👉 完整講義 MD 連結 (GitHub)](https://github.com/drake1128/journal-reading/blob/master/handouts/10-icu-general/Critical_Care_Biweekly_Review_2026-05-15%20%E6%95%99%E5%AD%B8%E8%AC%9B%E7%BE%A9.md)

---

<!-- _class: small-text -->

# 本期八大重點 (Top 8 Pearls)

1. **Female PBW 過度估計** — 同 Vt/PBW，女性 ΔP 風險 ↑26%（n=30,516）
2. **誘導劑 NMA** — Ketamine 比 etomidate 多 hemodynamic collapse，mortality 相當
3. **TOL/TAZ vs CAZ/AVI 肺穿透**（皆 CI）— ELF ratio 0.66 vs 0.41；建議 TDM
4. **REMAP-CAP Ivermectin** — 重症 + 非重症 COVID-19 皆無效，提前終止
5. **ARDS Global 2023 定義驗證** — SFR 可替代 PFR，比 Berlin 早 3 小時診斷
6. **EBV + Immunoparalysis** — Sepsis 死亡 HR 7.23 之最高風險免疫 endotype
7. **RCA 用於 CRRT — Delphi 共識** — Liver dysfunction / shock / hyperlactatemia 可用
8. **ECMO + AKI + CRRT — ADQI/ELSO 共識** — 約半數 ECMO 需 CRRT

---

<!-- _class: divider -->

# 1. Mechanical Ventilation & ARDS

---

<!-- _class: small-text -->

# Pearl 1｜Female PBW 過度估計女性肺容積

## von Wedel D, et al. ICM 2026-05-07 ｜ [PubMed 42096093](https://pubmed.ncbi.nlm.nih.gov/42096093/) ｜ [DOI](https://doi.org/10.1007/s00134-026-08442-1)

- **設計**：10 RCT + 2 real-world cohort 整合分析
- **N**：30,516（39.4% 女性）
- **重點結果**：

| Outcome（同 Vt/kg PBW 下）| 女性差異 | OR / 中介 |
|---|---|---|
| High driving pressure (ΔP ≥15 cmH₂O) | 絕對 +4.2% (3.2-5.3) | **aOR 1.26 (1.19-1.33), p<0.001** |
| 28 天死亡率 | 8.4% 由 ΔP 中介 | p<0.001 |
| 解剖肺容積 | −343 mL (−449 ~ −237) | p<0.001 |
| Aerated 肺容積 | −188 mL (−282 ~ −94) | p<0.001 |

> **臨床啟示**：對女性病人應以 **ΔP / Pplat** 為主要 target，而非僅依 Vt/PBW；建議 ΔP <14 cmH₂O。

---

<!-- _class: small-text -->

# Pearl 5｜ARDS Global 2023 定義：SFR 可替代 PFR

## Bennett RM, et al. Crit Care 2026-05-08 ｜ [PubMed 42104520](https://pubmed.ncbi.nlm.nih.gov/42104520/) ｜ [DOI](https://doi.org/10.1186/s13054-026-06043-4)

- **設計**：prospective sepsis cohort，n=950
- **比較**：Berlin (2012) vs Global (2023)

| 指標 | Berlin | Global |
|---|---|---|
| 符合 ARDS | 427 (45%) | **466 (49%)** |
| 中位 qualifying time | 基準 | **早 3 小時** |
| 30 天死亡 prognostic value | 良好 | 良好（SFR ≈ PFR） |

- **SFR (SpO₂/FiO₂)** 對 30 天死亡有 prognostic validity；與 PFR 中度相關
- Global 多納入者整體預後較佳 → 嚴重度分層仍需個別化

> **臨床啟示**：無 ABG 時 SFR 是合理替代；Global 定義能早 qualify。

---

<!-- _class: divider -->

# 2. Airway / 緊急插管

---

<!-- _class: small-text -->

# Pearl 2｜Etomidate vs Ketamine NMA — 9 RCT, n=4,672

## Zampieri FG, et al. Crit Care 2026-05-12 ｜ [PubMed 42121165](https://pubmed.ncbi.nlm.nih.gov/42121165/) ｜ [DOI](https://doi.org/10.1186/s13054-026-06067-w)

| 比較（Ketamine vs Etomidate） | OR (95% CI) | Certainty |
|---|---|---|
| Mortality | 0.96 (0.80-1.16) | Moderate |
| **Cardiovascular collapse** | **1.44 (1.20-1.71)** | Moderate |
| Post-induction hypotension | **1.34 (1.07-1.68)** | Low |
| Peri-intubation vasopressor | **1.45 (1.21-1.74)** | Low |
| First-pass success | 無差 | Moderate |
| Peri-intubation cardiac arrest | 無差 | Moderate |

> **重要修正**：「Ketamine 心臟最穩定」前見受挑戰。重症族群中 catecholamine 已 depleted，ketamine 反而引發更多 hemodynamic 不穩。Etomidate 仍是 hemodynamic 高風險者的首選。

---

<!-- _class: divider -->

# 3. Sepsis / Immunology

---

<!-- _class: small-text -->

# Pearl 6｜EBV + Immunoparalysis：最高死亡風險的免疫 endotype

## Rosiewicz KS, et al. Crit Care 2026-05-07 ｜ [PubMed 42098862](https://pubmed.ncbi.nlm.nih.gov/42098862/) ｜ [DOI](https://doi.org/10.1186/s13054-026-05966-2)

- **N**：124 位 ICU sepsis；IP+ 定義為 mHLA-DR <5,000/monocyte

| 組別 (vs EBV− IP−) | Mortality HR (95% CI) |
|---|---|
| EBV+ IP− | 3.30 (1.24-8.81) |
| EBV− IP+ | 2.14 (0.93-4.90) ns |
| **EBV+ IP+** | **7.23 (2.24-23.3), p=0.0009** |

- EBV+ IP+ 同時呈現「最高 cytokine 活化（IL-6/8/10/17A/18/MCP-1）+ 最低 mHLA-DR」
- **Hyperinflammation 與 immunosuppression 並存** 之 endotype

> **臨床啟示**：目前 hypothesis-generating；未來「EBV DNA + mHLA-DR 動態監測」或可指引 immunomodulatory / antiviral 介入。

---

<!-- _class: small-text -->

# Pearl 4｜REMAP-CAP Ivermectin — 重症 + 非重症 COVID-19 皆無效

## Hashmi M, et al. CCM 2026-05-08 ｜ [PubMed 42101205](https://pubmed.ncbi.nlm.nih.gov/42101205/) ｜ [DOI](https://doi.org/10.1097/CCM.0000000000007134)

- **設計**：international Bayesian platform RCT；Pakistan、India、Ireland（2021-06 ~ 2022-09）
- **族群**：住院 COVID-19；critically ill n=61、non-critically ill n=89

| Outcome | Critically ill | Non-critically ill |
|---|---|---|
| OSFD（primary）median | −1 vs −1 | 22 vs 22 |
| Adjusted proportional OR | **0.94 (0.40-2.07)** | 1.04 (0.48-2.34) |
| **PP superiority** | **44.2%** | 53.7% |
| 醫院存活 | 35.1% vs 37.5% | 84.1% vs 77.8% |

> **臨床啟示**：與 ACTIV-6 / TOGETHER / COVID-OUT 一致。試驗因 operational futility（外部證據成熟）提前終止 — Bayesian platform 「learn and adapt」典範。

---

<!-- _class: divider -->

# 4. 感染與 HAP/VAP 藥動學

---

<!-- _class: small-text -->

# Pearl 3｜TOL/TAZ vs CAZ/AVI 在 HAP/VAP 之 ELF 穿透（皆 CI）

## Benítez-Cano A, et al. Crit Care 2026-05-13 ｜ [PubMed 42129898](https://pubmed.ncbi.nlm.nih.gov/42129898/) ｜ [DOI](https://doi.org/10.1186/s13054-026-06075-w)

- **設計**：單中心、open-label、randomized PK trial；n=30 critically ill nosocomial pneumonia
- **介入**：TOL/TAZ 6g/3g CI vs CAZ/AVI 6g/1.5g CI（**兩組皆 CI**）

| 藥物 | ELF/plasma 穿透率 (中位 [IQR]) |
|---|---|
| **Ceftolozane** | **0.66 [0.32]** |
| **Ceftazidime** | **0.41 [0.30]** |
| Tazobactam | 0.44 [0.05] |
| Avibactam | 0.44 [0.46] |

> **常見誤讀修正**：本研究**未比較 CI vs intermittent infusion**，是兩種「皆採 CI」之藥物 PK 比較。標準劑量 CI 即可達 ELF PK/PD 目標；高 MIC 或 plasma 過度暴露風險高者建議 **TDM**。

---

<!-- _class: divider -->

# 5. Renal / CRRT / ECMO

---

<!-- _class: small-text -->

# Pearl 7｜RCA 用於 CRRT — Delphi 共識（CREDES）

## Jacobs R, et al. Crit Care 2026-05-13 ｜ [PubMed 42129846](https://pubmed.ncbi.nlm.nih.gov/42129846/) ｜ [DOI](https://doi.org/10.1186/s13054-026-06066-x)

- **設計**：modified Delphi（CREDES）；29→23 位 EU/US/Canada 專家、3 輪
- **產出**：22 條共識聲明

**重點訊息**

- **以下族群仍可用 RCA**（需密切監測 + dosing 調整）：
  - Liver dysfunction
  - Severe shock
  - Hyperlactatemia
- **Citrate 累積管理**：階梯式 — 降低 citrate delivery → 必要時停 RCA
- **常見併發症**：metabolic alkalosis、電解質紊亂 — 可處置

> **與既有指引銜接**：KDIGO 2025 仍以 RCA 為 CRRT 首選 anticoagulant；本共識補上「邊緣族群」操作面建議。

---

<!-- _class: small-text -->

# Pearl 8｜ECMO + AKI + CRRT — ADQI/ELSO 聯合共識

## Gist KM, et al. ICM 2026-05-06 ｜ [PubMed 42113209](https://pubmed.ncbi.nlm.nih.gov/42113209/) ｜ [DOI](https://doi.org/10.1007/s00134-026-08440-3)

- **產出**：36th ADQI Meeting（June 2025）多學科共識
- **5 個工作組**：
  1. AKI / CRRT 流行病學、risk factor、outcomes
  2. Fluid management 與 outcomes
  3. ECMO 期間 CRRT 啟動 + fluid removal indications
  4. ECMO 期間 CRRT 操作最佳實務
  5. Biomarkers、extracorporeal blood purification、drug PK/PD

**關鍵數字**：約 **半數** ECMO 病人需 CRRT；AKI / fluid balance 同時影響短期與長期 outcomes

> **臨床啟示**：可作為各院 ECMO + CRRT bundle / pathway 之 reference 文件。

---

<!-- _class: small-text -->

# Awake / Extubated ECMO for ARDS — 國際 cohort

## Roncon-Albuquerque R Jr, et al. AJRCCM 2026-05-06 ｜ [PubMed 42092985](https://pubmed.ncbi.nlm.nih.gov/42092985/) ｜ [DOI](https://doi.org/10.1093/ajrccm/aamag219)

- **設計**：8 國、14 中心、retrospective（2015-2024）；n=307

| 策略 | N | 90 天死亡率 | Strategy failure |
|---|---|---|---|
| Primary awake ECMO | 113 | **30.1%** | 40.7% (46/113) |
| Extubated on ECMO | 194 | **14.9%** | 24.2% (47/194) |

- Strategy failure 與 90 天死亡強相關（HR ~6-8）；多在前 10 天
- 失敗主因：呼吸惡化；primary awake 組為 agitation/delirium；extubated 組為痰液清除困難

> **臨床啟示**：兩組 baseline 不同（selection bias）。Extubated 策略 outcome 較佳；primary awake 需肺以外器官功能尚佳、配合度高之選擇族群。

---

<!-- _class: divider -->

# 6. Hemodynamics / Fluid

---

<!-- _class: small-text -->

# SHAMROC — CLOVERS 長期 patient-centered outcomes

## Jorda A, et al. AJRCCM 2026-05-06 ｜ [PubMed 42093058](https://pubmed.ncbi.nlm.nih.gov/42093058/) ｜ [DOI](https://doi.org/10.1093/ajrccm/aamag154)

- **設計**：CLOVERS (NCT03434028) 預設長期 follow-up
- **N**：702（431 survivor + 271 死亡）入 6 個月分析
- **介入**：早期 restrictive vs liberal fluid

**6 個月結果（皆無差異）**

| Outcome | 差異 (Restrictive − Liberal) | 95% CI |
|---|---|---|
| MoCA-Blind（認知） | 0.11 | −1.44 ~ 1.70 |
| Hayling（執行功能） | 0.38 | −0.97 ~ 1.76 |
| ADL（功能） | 0.03 | −0.84 ~ 0.90 |
| PROMIS Mobility | 0.72 | −2.20 ~ 3.64 |
| EQ-5D-5L（HRQoL） | −0.01 | −0.07 ~ 0.06 |

> **臨床啟示**：restrictive 長期 safe（與 CLASSIC 一致），但**未顯示優勢** — 個別化策略仍為王道。

---

<!-- _class: divider -->

# 7. 其他焦點 (Other Highlights)

---

<!-- _class: small-text -->

# 其他焦點 (一)

| 主題 | 文獻 | 連結 |
|---|---|---|
| Refractory Septic Shock 定義（SCCM/ESICM Delphi）| Leone M, CCM 2026-05 | [PMID 41873857](https://pubmed.ncbi.nlm.nih.gov/41873857/) |
| SCCM 老年 ICU 指引 | Ferrante LE, CCM 2026-05 | [PMID 41860327](https://pubmed.ncbi.nlm.nih.gov/41860327/) |
| Olanzapine vs low-dose Dexmed 譫妄 (RCT) | Liu J, AJRCCM 2026-05-12 | [PMID 42118124](https://pubmed.ncbi.nlm.nih.gov/42118124/) |
| ECMO weaning 之 V̇E/V̇CO₂ slope | Giosa L, AJRCCM 2026-05-06 | [PMID 42093063](https://pubmed.ncbi.nlm.nih.gov/42093063/) |
| Immunocompromised ARF（103 ICU/26 國，n=9,854）| Azoulay E, Lancet Respir Med 2026-05 | [PMID 41856149](https://pubmed.ncbi.nlm.nih.gov/41856149/) |
| OxyKids 兒童 ARDS SpO₂ 目標 RCT | Louman S, Lancet Respir Med 2026-05-12 | [PMID 42119581](https://pubmed.ncbi.nlm.nih.gov/42119581/) |

---

<!-- _class: small-text -->

# 其他焦點 (二) — Resuscitation

| 主題 | 文獻 | 重點 | 連結 |
|---|---|---|---|
| **REBOARREST** | Brede JR, Crit Care 2026-05-05 | 非外傷 OHCA prehospital REBOA；n=179；sustained ROSC 28% vs 26%（p=0.78）— **negative** | [PMID 42087223](https://pubmed.ncbi.nlm.nih.gov/42087223/) |
| **MPA 除顫 RCT** | Nehme Z, Resuscitation 2026-05-04 | n=560；transthoracic impedance ↓ 8.5Ω 但 survival 無差（39.8% vs 39.9%）；提前終止 | [PMID 42092447](https://pubmed.ncbi.nlm.nih.gov/42092447/) |
| **DOSE VF 二次分析** | Cheskes S, Resuscitation 2026-05 | n=342；**AP positioning** 獨立關聯 ROSC（aOR 2.01, 1.12-3.59）— current 並非主因 | [PMID 41856454](https://pubmed.ncbi.nlm.nih.gov/41856454/) |

---

<!-- _class: divider -->

# Take Home Messages

---

# 三個即刻可應用的臨床重點

1. **女性病人接 ventilator 時，每次設定都應同步看 ΔP**
   - 不要只信 Vt/PBW；ΔP ≥15 cmH₂O 即需降 Vt 或允許 permissive hypercapnia
   - 文獻：von Wedel D, ICM 2026-05-07

2. **緊急插管在 hemodynamic 不穩重症族群，etomidate 仍是首選**
   - Ketamine 之心血管不穩定性顯著高於 etomidate（OR 1.44）
   - 文獻：Zampieri FG, Crit Care 2026-05-12

3. **嚴重 HAP/VAP 用 TOL/TAZ 或 CAZ/AVI 時，建議 CI + TDM**
   - 標準 CI 即達 ELF 目標；但 plasma 過度暴露 / 高 MIC 需 TDM
   - 文獻：Benítez-Cano A, Crit Care 2026-05-13

---

<!-- _class: ref -->

# 主要參考文獻 (1/2)

1. von Wedel D, et al. *Intensive Care Med.* 2026 May 7. [10.1007/s00134-026-08442-1](https://doi.org/10.1007/s00134-026-08442-1) — PMID 42096093
2. Zampieri FG, et al. *Crit Care.* 2026 May 12. [10.1186/s13054-026-06067-w](https://doi.org/10.1186/s13054-026-06067-w) — PMID 42121165
3. Benítez-Cano A, et al. *Crit Care.* 2026 May 13. [10.1186/s13054-026-06075-w](https://doi.org/10.1186/s13054-026-06075-w) — PMID 42129898
4. Hashmi M, et al. *Crit Care Med.* 2026 May 8. [10.1097/CCM.0000000000007134](https://doi.org/10.1097/CCM.0000000000007134) — PMID 42101205
5. Bennett RM, et al. *Crit Care.* 2026 May 8. [10.1186/s13054-026-06043-4](https://doi.org/10.1186/s13054-026-06043-4) — PMID 42104520
6. Rosiewicz KS, et al. *Crit Care.* 2026 May 7. [10.1186/s13054-026-05966-2](https://doi.org/10.1186/s13054-026-05966-2) — PMID 42098862
7. Jacobs R, et al. *Crit Care.* 2026 May 13. [10.1186/s13054-026-06066-x](https://doi.org/10.1186/s13054-026-06066-x) — PMID 42129846
8. Gist KM, et al. *Intensive Care Med.* 2026 May 6. [10.1007/s00134-026-08440-3](https://doi.org/10.1007/s00134-026-08440-3) — PMID 42113209

---

<!-- _class: ref -->

# 主要參考文獻 (2/2)

9. Roncon-Albuquerque R Jr, et al. *Am J Respir Crit Care Med.* 2026 May 6. [10.1093/ajrccm/aamag219](https://doi.org/10.1093/ajrccm/aamag219) — PMID 42092985
10. Jorda A, et al. *Am J Respir Crit Care Med.* 2026 May 6. [10.1093/ajrccm/aamag154](https://doi.org/10.1093/ajrccm/aamag154) — PMID 42093058
11. Giosa L, et al. *Am J Respir Crit Care Med.* 2026 May 6. [10.1093/ajrccm/aamag145](https://doi.org/10.1093/ajrccm/aamag145) — PMID 42093063
12. Liu J, et al. *Am J Respir Crit Care Med.* 2026 May 12. [10.1093/ajrccm/aamag235](https://doi.org/10.1093/ajrccm/aamag235) — PMID 42118124
13. Leone M, et al. *Crit Care Med.* 2026 May. [10.1097/CCM.0000000000007124](https://doi.org/10.1097/CCM.0000000000007124) — PMID 41873857
14. Ferrante LE, et al. *Crit Care Med.* 2026 May. [10.1097/CCM.0000000000007084](https://doi.org/10.1097/CCM.0000000000007084) — PMID 41860327
15. Brede JR, et al. *Crit Care.* 2026 May 5. [10.1186/s13054-026-06057-y](https://doi.org/10.1186/s13054-026-06057-y) — PMID 42087223
16. Nehme Z, et al. *Resuscitation.* 2026 May 4. [10.1016/j.resuscitation.2026.111121](https://doi.org/10.1016/j.resuscitation.2026.111121) — PMID 42092447
17. Cheskes S, et al. *Resuscitation.* 2026 May. [10.1016/j.resuscitation.2026.111061](https://doi.org/10.1016/j.resuscitation.2026.111061) — PMID 41856454

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考，不代表任何醫療機構立場*
