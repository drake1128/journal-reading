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
footer: '謝慕揚 MD, PhD, FESC | Biweekly CV Journal Review | 2026-04-11'
---

<!-- _class: lead -->

# Biweekly CV Journal Review
## 雙週心血管期刊文獻回顧

**謝慕揚 MD, PhD, FESC**
2026-03-28 至 2026-04-11
NEJM · Lancet · EHJ · Circulation · EuroIntervention · JACC

---

# 大綱

1. **NEJM 介入心臟學特輯** — IVUS trials (2 neutral + 1 positive), Angio-FFR × 2
2. **NEJM 其他** — Beta-Blocker 停藥、LAA Closure、LDL 目標、Mavacamten
3. **Lancet** — NOBLE 10-yr、HOST-EXAM 10-yr、PRO-TAVI
4. **EHJ** — Finerenone、ATTRv Screening、Lp(a) + Aspirin
5. **Circulation** — AMEND System、HFpEF Exercise、AVC Sex Differences
6. **EuroIntervention** — HIR Criteria、Complex PCI Meta-Analysis

---

<!-- _class: divider -->

# NEJM 冠脈介入專題

---

# OPTIMAL: IVUS vs Angio PCI in Left Main — Neutral
## [N Engl J Med 2026](https://doi.org/10.1056/NEJMoa2600440)

- International, multicenter, open-label RCT (Italy, Spain, UK)
- 806 patients, unprotected left main disease

| 終點 | IVUS (n=401) | Angio (n=405) | HR | P |
|------|:------------:|:-------------:|:--:|:-:|
| **Primary Composite** | **33.7%** | **30.9%** | **1.11** | **0.40** |

- IVUS 組手術時間較長 (89 vs 66 min)

> **Take Home**: IVUS 在 left main PCI **未優於** angiography — 社論：「Is IVUS Always Necessary?」

---

# IVUS-CHIP: IVUS vs Angio Complex PCI — Neutral
## [N Engl J Med 2026](https://doi.org/10.1056/NEJMoa2601521)

- 7 European countries, 2,020 patients, complex high-risk lesions

| 終點 | IVUS | Angio | HR (95% CI) |
|------|:----:|:-----:|:-----------:|
| **Target-Vessel Failure** | **13.9%** | **11.1%** | **1.25 (0.97-1.60)** |

- 唯一 positive: **DKCRUSH VIII** — bifurcation crush stenting: HR **0.40** (0.23-0.71)

> **Pearl**: 3 篇 IVUS trials: **2 neutral, 1 positive** — IVUS 效益取決於是否改變手術策略

---

# Angiography-Derived FFR × 2 篇
## [N Engl J Med 2026](https://doi.org/10.1056/NEJMoa2600949) & [(vFFR)](https://doi.org/10.1056/NEJMoa2601841)

| 試驗 | 技術 | 設計 | 結果 |
|------|------|------|------|
| Angio-FFR | Image-based FFR | Multicenter RCT | Noninferior to wire-FFR |
| vFFR | 3D QCA-based vFFR | 37 sites, 8 countries | Noninferior to wire-FFR |

- **兩種不同演算法均達 noninferiority**
- 無需 pressure wire 或 hyperemic agent
- 可望打破 FFR 使用率低的障礙

> **Pearl**: Physiology-guided PCI 即將進入**無導絲時代**

---

# Discontinuation of Beta-Blocker After MI
## [N Engl J Med 2026;394(13):1302-12](https://doi.org/10.1056/NEJMoa2601005)

- Open-label, randomized, **noninferiority** trial (25 centers, Korea)
- MI 後穩定患者，**LVEF ≥ 40%**，無 heart failure
- Beta-blocker 停藥 **noninferior to** 持續使用

> **Pearl**: 呼應 ABYSS & REDUCE-AMI — MI 後 LVEF 正常且無 HF 者**可安全停藥**

> 「MI 後一定要吃 beta-blocker 一輩子」的時代正式終結

---

# LAA Closure or Medical Therapy in AF
## [N Engl J Med 2026;394(13):1270-80](https://doi.org/10.1056/NEJMoa2513310)

- Multicenter RCT (Germany)
- AF + **高中風 & 高出血風險**
- LAA closure vs physician-directed best medical care
- 療效**不確定** — 同期社論：「Another Overused Method?」

> **Take Home**: LAA closure 需要**更嚴格 patient selection**，不宜過度推廣

---

# Intensive LDL Targeting in ASCVD
## [N Engl J Med 2026;394(14):1365-75](https://doi.org/10.1056/NEJMoa2600283)

- Open-label superiority trial (South Korea)
- **LDL < 55 mg/dL** (intensive) vs **55-70 mg/dL** (standard)
- ASCVD secondary prevention 族群
- **首個直接比較這兩個 LDL 目標的 RCT**

> **Pearl**: 為 ESC guideline 推薦的 **LDL < 55 mg/dL** 目標提供 RCT 證據

---

# Mavacamten in Adolescents with Obstructive HCM
## [N Engl J Med 2026](https://doi.org/10.1056/NEJMoa2601103)

- Phase 3, double-blind, placebo-controlled RCT
- Symptomatic adolescents (12-17 y/o), NYHA II-III
- **首個兒科 HCM 的 cardiac myosin inhibitor RCT**
- Mavacamten 在青少年 HCM 中展現療效與安全性

> **Take Home**: 填補兒科 obstructive HCM 藥物治療的空白

---

<!-- _class: divider -->

# Lancet — Left Main & Antiplatelet

---

# NOBLE 10-Year: PCI vs CABG for Left Main
## [Lancet 2026;407:1374-82](https://doi.org/10.1016/S0140-6736(26)00205-9)

| 終點 | PCI (n=592) | CABG (n=592) | HR | P |
|------|:-----------:|:-----------:|:--:|:-:|
| **10-yr Mortality** | 23% | 25% | 0.93 | 0.56 |

- 36 hospitals, 9 countries, 1201 patients
- **10 年全因死亡率無差異** — 不同 SYNTAX score 亦然
- Left main PCI 在適當患者中是安全的長期選擇

> **Pearl**: NOBLE vs EXCEL — Left main 的 PCI/CABG 辯論轉向 **patient-tailored** 策略

---

# HOST-EXAM 10-Year: Clopidogrel vs Aspirin
## [Lancet 2026](https://doi.org/10.1016/S0140-6736(26)00422-8)

| 終點 | Clopidogrel | Aspirin | HR | P |
|------|:-----------:|:-------:|:--:|:-:|
| **Primary Composite** | 25.4% | 28.5% | 0.86 | 0.005 |
| Thrombotic | 17.3% | 20.0% | — | 0.002 |
| Bleeding | 9.1% | 10.8% | — | 0.020 |
| All-Cause Death | — | — | — | NS |

- 5438 patients, median 10.5-yr follow-up (92.8% completion)
- **Clopidogrel 優於 aspirin**: 降低 ischaemic + bleeding events

> **Pearl**: 10 年追蹤確認 — PCI 後 chronic maintenance **clopidogrel > aspirin**

---

# PRO-TAVI: Deferral of PCI in TAVI Patients
## [Lancet 2026](https://doi.org/10.1016/S0140-6736(26)00308-9)

- 12 hospitals, Netherlands, 466 patients (median age 81)
- Deferral of PCI vs PCI before TAVI

| 終點 | Deferral | PCI before TAVI | P (noninf) |
|------|:--------:|:---------------:|:----------:|
| **1-yr Composite** | 24% | 26% | **0.0008** |

- HR 0.89 (0.62-1.28) — **Noninferiority confirmed**
- TAVI 前 defer PCI 是合理的保守策略

---

<!-- _class: divider -->

# European Heart Journal

---

# Finerenone: Lifetime Cardiorenal Benefits
## [Eur Heart J 2026](https://doi.org/10.1093/eurheartj/ehag126)

- **FIDELIO-DKD + FIGARO-DKD** pooled analysis
- CKD + T2DM 患者的 finerenone 終生心腎效益
- Ostrominski, Vaduganathan, Solomon, Anker et al.
- 強化 finerenone 在 **cardio-kidney-metabolic disease** 的角色

> **Pearl**: CKD + T2DM 患者的治療「四柱」: RAAS-i + SGLT2i + GLP-1 RA + **Finerenone**

---

# Cascade Genetic Screening in ATTRv Amyloidosis
## [Eur Heart J 2026](https://doi.org/10.1093/eurheartj/ehag222)

- 967 individuals, 431 families, 15 Italian centres (2004-2024)
- 461 asymptomatic carriers → **16.7% converted** to symptomatic
- 部分 carriers 比預期 **提早 >10 年** 發病
- Disease-modifying therapy: **HR 0.11** (95% CI 0.01-0.17) for mortality

> **Pearl**: Cascade screening → 早期診斷 → 早期治療 → **改善存活**

---

# EHJ 精選快覽

| 主題 | DOI |
|------|-----|
| Aspirin for elevated **Lp(a)** — evidence mounting | [ehag161](https://doi.org/10.1093/eurheartj/ehag161) |
| **GLP-1 RA** and atherosclerosis | [ehag075](https://doi.org/10.1093/eurheartj/ehag075) |
| **MAD** and VA after MV surgery — true, longer, inferolateral | [ehag243](https://doi.org/10.1093/eurheartj/ehag243) |
| Breast cancer → fibrotic signalling → **AF** | [ehag185](https://doi.org/10.1093/eurheartj/ehag185) |
| **ATTR-CM** non-biopsy dx: eGFR-adjusted FLC cut-offs | [ehag250](https://doi.org/10.1093/eurheartj/ehag250) |
| AI missed opportunities in **albuminuria testing** | [qcag054](https://doi.org/10.1093/ehjqcco/qcag054) |
| First European **remote robotic** heart surgery | [ehag002](https://doi.org/10.1093/eurheartj/ehag002) |

---

<!-- _class: divider -->

# Circulation & 子刊

---

# AMEND System: Transeptal Mitral Annuloplasty FIM
## [Circ Cardiovasc Interv 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.125.015977)

- Semi-rigid closed **D-shaped annuloplasty ring**
- **Transvenous transeptal approach**
- 13 patients, grade 3-4 functional MR
- Selective AP dimensional reduction → improve coaptation → reduce MR
- **6-month results encouraging**

> **Pearl**: AMEND = TEER 之外的 transcatheter MV 治療新選擇

---

# Circulation 精選快覽

| 主題 | 期刊 | DOI |
|------|------|-----|
| Multi-organ exercise deficits in **HFpEF** | Circulation | [077579](https://doi.org/10.1161/CIRCULATIONAHA.125.077579) |
| **Sex-specific AVC** and AS risk (MESA) | Circ CV Imaging | [018849](https://doi.org/10.1161/CIRCIMAGING.125.018849) |
| THV expansion in degenerated **mitral bioprostheses** | Circ CV Interv | [016270](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016270) |
| HF **GDMT scoring systems** scoping review | Circ Heart Fail | [013881](https://doi.org/10.1161/CIRCHEARTFAILURE.125.013881) |
| **LBBAP** delivery system prevents entanglement | Circ Arrhythm | [014355](https://doi.org/10.1161/CIRCEP.125.014355) |
| **Gene therapy** cardiac immunotoxicity | Circ Heart Fail | [013771](https://doi.org/10.1161/CIRCHEARTFAILURE.125.013771) |

---

<!-- _class: divider -->

# EuroIntervention

---

# HIR Criteria After PCI: Too Broad?
## [EuroIntervention 2026;22(7):e392-e401](https://doi.org/10.4244/EIJ-D-25-01174)

- 15,336 CCS patients, Mount Sinai (2012-2022)
- **71.4%** met ≥1 ESC 2024 HIR criterion
- HIR criteria predict MACCE (p for trend < 0.001)
- 但 **>70% 都是「高風險」→ 分層精確度有限**

> **Pearl**: 當 >70% 患者都是「高風險」時，我們需要**更精準的工具**

---

# Complex vs Non-Complex PCI: Meta-Analysis
## [EuroIntervention 2026;22(7):e402-e414](https://doi.org/10.4244/EIJ-D-25-01204)

290,039 patients — Bayesian random-effects model

| Endpoint | Adjusted HR (95% CrI) |
|----------|:---------------------:|
| **MI** | **1.71** (1.49-1.96) |
| Major Bleeding | **1.24** (1.14-1.35) |
| All-Cause Death | **1.21** (1.12-1.32) |
| Stent Thrombosis | **1.76** (1.49-2.14) |
| TLR/TVR | **1.99** (1.58-2.50) |

- Posterior probability **>99%** for all endpoints
- Complex PCI 同時增加 ischaemic **and** bleeding risk

---

# Stent Retriever-Assisted Coronary Thrombectomy
## [EuroIntervention 2026;22(7):e415-e416](https://doi.org/10.4244/EIJ-D-25-01014) — Geneva University Hospitals

- 57 y/o male, inferior **STEMI**, RCA thrombotic occlusion
- Day 1: Aspiration → TIMI 3, 但遠端 large thrombus → deferred stenting
- Day 3: **Organized thrombus** → stent retriever + aspiration strategy
- 結果：**Complete thrombus clearance** (OCT confirmed) → **免 stenting**

| 器材 | 規格 | 廠商 |
|------|------|------|
| Guiding catheter | JR4 **7 Fr** | — |
| Guidewire | **SION blue × 2** (0.014", 180 cm) | Asahi Intecc |
| Microcatheter | **Rebar 18** (ID 0.021", 130 cm) | Medtronic |
| Stent Retriever | **enVast 4.5 × 46 mm** | Vesalio |
| Aspiration | **CAT RX** (5.3 Fr, 140 cm) + ENGINE | Penumbra |

---

# Stent Retriever: Size 選擇與操作關鍵

- **enVast** = 首個 FDA cleared coronary-specific stent retriever (2025-12)
- 適用血管：**≥ 2 mm 且 ≤ 6 mm** diameter
- **直徑選擇**：至少 **oversized 50%** vs vessel diameter
  - RCA ~3 mm → **4.5 mm** device (50% oversizing)
- **長度選擇**：涵蓋 thrombus + 兩端留餘量 → 本案選 **46 mm**
- FIM 系列最常用：**4.5 × 37 mm** (60% of cases)

```text
Rebar microcatheter → 送入 enVast → 回收 microcatheter (展開)
    → Telescope guide extension 推進 → CAT RX aspiration ON
    → 回收 stent retriever (under continuous aspiration)
```

> **Pearl**: 7 Fr guide 必要 — CAT RX (5.3 Fr) 佔滿 6 Fr lumen，需 7 Fr 容納 retriever 回收

---

# Antiplatelet Pretreatment in Coronary Revascularisation
## [EuroIntervention 2026;22(7):e378-e391](https://doi.org/10.4244/EIJ-D-25-00896) — Bhatt DL, Mehran R et al.

- 從 **routine pretreatment** → **cath-lab-based loading** 的趨勢
- **Cangrelor** 的角色日益重要（parenteral, rapid onset/offset）
- 涵蓋 NSTE-ACS、STEMI、stable CAD 各場景

---

<!-- _class: divider -->

# JACC & 子刊

---

# ★ 2026 AHA/ACC Acute PE Guideline
## [J Am Coll Cardiol 2026;87(13):1626-1710](https://doi.org/10.1016/j.jacc.2025.11.005)

- **10 個學會聯合制定**，85 頁完整指引
- **重大創新**：引入 **AHA/ACC PE Clinical Categories** — 取代 massive/submassive 分類
- 首次明確定位 **catheter-based therapy** 的適應症
- 定義 **Post-PE Syndrome** 的診斷與處理
- 同期刊出 ~15 篇配套專家評論（JACC 幾乎整期獻給 PE）

> **Pearl**: 近 15 年來首次 PE 指引全面更新 — 對急診、重症、心臟科均有重大影響

---

# JACC 主刊精選

| 文獻 | 重點發現 |
|------|---------|
| **CTO PCI vs Medical**: EUROCTO/DECISION-CTO | PCI 改善 **QoL** (p<0.001)，但 MACE 無差異 |
| **BP Trajectories**: STEP Trial (n=7,296) | 每延遲 1 月達標 → CV risk **↑3%** |
| **Radiomic Epicardial Fat** for HF (n=72,751) | Highest decile: HF risk **↑20 倍** |
| **PE Thrombectomy Trends**: PERT (n=2,958) | MT 使用**每年 ↑18%**，2021 年超越 CDT |

---

# JACC 子刊精選

| 文獻 | 期刊 | 重點 |
|------|------|------|
| **YELLOW-III**: Evolocumab plaque changes | CV Imaging | Fibrous cap ↑38%, Lipid core ↓31% |
| **xFFR**: On-site DL CT-FFR | CV Imaging | Accuracy 88%, **8 min** analysis |
| **Severe TR**: ESC/EACTS in real-world | CV Interv | 13.1% 被排除者仍有 symptom benefit |
| **HM3 vs HTx** in young (18-49y) | Heart Fail | 2-yr survival: 88.7% vs 90.2% (similar) |
| **PROACTIVE-HF**: Remote PA monitoring | Heart Fail | Cordella system improves HF care |

---

<!-- _class: divider -->

# Take Home Messages

---

# 本雙週 Top 5 Take Home Messages

1. **IVUS-guided PCI** 在 left main (OPTIMAL) 及 complex PCI (IVUS-CHIP) 均為 **neutral** — 挑戰既有觀念
2. **Angio-derived FFR** (兩種演算法) 均 noninferior to wire-based FFR — physiology-guided PCI 將更普及
3. **MI 後 beta-blocker** 在 LVEF 正常且無 HF 者可安全停藥
4. **Clopidogrel > Aspirin** 作為 PCI 後 long-term monotherapy（10 年追蹤）
5. **NOBLE 10-yr**: Left main PCI vs CABG 在全因死亡率上無差異

---

<!-- _class: small-text -->

# 本雙週 Clinical Practice Changes

| 領域 | 舊觀念 | 新證據 |
|------|--------|--------|
| Left Main PCI | IVUS 建議使用 | OPTIMAL: IVUS **未優於** angio (neutral) |
| FFR Assessment | 需要 pressure wire | **Angio-derived FFR** 可替代 (NEJM ×2) |
| MI 後 Beta-Blocker | 終生使用 | LVEF ≥40%, 無 HF: **可停藥** |
| PCI 後 Monotherapy | Aspirin 為標準 | **Clopidogrel 優於 aspirin** (10-yr) |
| Left Main: PCI vs CABG | CABG 較佳 | **10 年死亡率無差異** (NOBLE) |
| TAVI + CAD | Routine PCI before TAVI | **Deferral is noninferior** (PRO-TAVI) |

---

<!-- _class: ref -->

# 參考文獻 (1/2)

1. IVUS-Guided PCI in Left Main. [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2600440)
2. IVUS-Guided Complex High-Risk PCI. [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2601521)
3. Angiography-Derived FFR to Guide PCI. [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2600949)
4. Angiography-Based Physiology (vFFR). [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2601841)
5. Beta-Blocker Discontinuation After MI. [*N Engl J Med*. 2026;394:1302-12.](https://doi.org/10.1056/NEJMoa2601005)
6. LAA Closure or Medical Therapy in AF. [*N Engl J Med*. 2026;394:1270-80.](https://doi.org/10.1056/NEJMoa2513310)
7. Mavacamten in Adolescent HCM. [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2601103)
8. Intensive LDL Targeting in ASCVD. [*N Engl J Med*. 2026;394:1365-75.](https://doi.org/10.1056/NEJMoa2600283)
9. Hypertension Control Strategies. [*N Engl J Med*. 2026;394:1376-87.](https://doi.org/10.1056/NEJMoa2504068)
10. NOBLE 10-Year. [*Lancet*. 2026;407:1374-82.](https://doi.org/10.1016/S0140-6736(26)00205-9)

---

<!-- _class: ref -->

# 參考文獻 (2/2)

11. HOST-EXAM 10-Year. [*Lancet*. 2026.](https://doi.org/10.1016/S0140-6736(26)00422-8)
12. PRO-TAVI. [*Lancet*. 2026.](https://doi.org/10.1016/S0140-6736(26)00308-9)
13. Finerenone Lifetime Benefits. [*Eur Heart J*. 2026.](https://doi.org/10.1093/eurheartj/ehag126)
14. ATTRv Cascade Screening. [*Eur Heart J*. 2026.](https://doi.org/10.1093/eurheartj/ehag222)
15. AMEND System FIM. [*Circ Cardiovasc Interv*. 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.125.015977)
16. HIR Criteria in CCS. [*EuroIntervention*. 2026;22:e392-e401.](https://doi.org/10.4244/EIJ-D-25-01174)
17. Complex PCI Meta-Analysis. [*EuroIntervention*. 2026;22:e402-e414.](https://doi.org/10.4244/EIJ-D-25-01204)
18. Antiplatelet Pretreatment Review. [*EuroIntervention*. 2026;22:e378-e391.](https://doi.org/10.4244/EIJ-D-25-00896)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
*Based on articles retrieved from PubMed*
