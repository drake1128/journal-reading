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
    font-size: 2.5em;
    text-align: center;
  }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.5em; }
  h2 { color: #0072bc; font-size: 1.0em; }
  h3 { color: #555555; }
  table { font-size: 0.62em; width: 100%; }
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
  section.ref { font-size: 0.55em; }
  section.ref h1 { font-size: 1.2em; }
  section.ref ol { line-height: 1.4; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-05-17'
---

<!-- _class: lead -->

# 每週心血管期刊文獻回顧
## 2026-05-10 ~ 2026-05-17

**整理：謝慕揚 MD, PhD, FESC**
**讀書會共筆 · 醫療專業教學參考**

涵蓋：NEJM · Lancet · EHJ · JACC family · Circulation family · EuroIntervention

---

# 本週主題

> **「重新檢視老藥、嚴格看待新藥」**

- **老藥回歸**：DIGIT-HF AF subgroup + DECISION 兩篇 EHJ 文章重新確立 **digitoxin/digoxin** 在 HFrEF 的地位
- **新藥落地**：tonlamarsen (RAAS antisense)、XXB750 (NPR-1 agonist) 兩項 phase 2 BP 試驗 **target engagement 達標卻無臨床效益**
- **結構介入**：DOUBLE-CHOICE 證實 ACURATE neo2 在選定解剖優於 Evolut（PPM 11.2% vs 26.5%）——但 valve 已下市
- **新概念**：sotatercept 跨界 HFpEF-CpcPH 首例 phase 2 positive (CADENCE)

---

# Top 5 Picks 一覽

| # | 試驗 | 期刊 | 結果 | 關鍵數字 |
|---|------|------|------|---------|
| 1 | **DOUBLE-CHOICE** | EuroIntervention | ✅ | 30d composite 15.4% vs 30.4% (p<0.001)；PPM 11.2% vs 26.5% |
| 2 | **DIGIT-HF AF subgroup** | EHJ | ✅ | 主試驗 HR 0.82 (95% CI 0.69-0.98)；AF 與 sinus 一致 |
| 3 | **CADENCE** (sotatercept) | Circulation | 💡 | PVR −1.02 WU (p=0.004) in HFpEF + CpcPH |
| 4 | **TAPIS** (DAPT+IVT) | Lancet | ✅ | 90d mRS 0-1: 68.7% vs 62.0%, RR 1.11 (p=0.0089) |
| 5 | **KARDINAL** (tonlamarsen) | JACC | ❌ | ΔSBP −0.1 mmHg (p=0.97) 雖再壓 angiotensinogen −44% |

---

<!-- _class: divider -->

# NEJM

---

# ORIENTAL-MeVO — Thrombectomy for Medium-Vessel Stroke

## [Hu W, et al. *N Engl J Med* 2026;394(19):1894-1904.](https://doi.org/10.1056/NEJMoa2514120)

| 項目 | 內容 |
|------|------|
| 設計 | 中國 48 中心 open-label RCT，blinded outcome |
| 族群 | n=563；急性 MeVO 缺血性中風，NIHSS ≥6，發病 24h 內 |
| 介入 | Thrombectomy + medical mgmt vs medical mgmt alone |
| Primary | 90d mRS 0-2：**58.6% vs 46.6%**, adjusted RR **1.24 (1.07-1.44), p=0.004** ✅ |
| 安全 | Symptomatic ICH **4.7% vs 2.2%**；90d mortality 11.1% vs 10.2% (NS) |

> Thrombectomy 適應症由 LVO 延伸至 MeVO，但症狀性 ICH **雙倍**——須謹慎挑選 NIHSS ≥6 患者

---

<!-- _class: divider -->

# Lancet

---

# TAPIS — DAPT + IV Thrombolysis 改善中度中風預後

## [Wang A, et al. *Lancet* 2026;407(10542):1919-1928.](https://doi.org/10.1016/S0140-6736(26)00757-9)

| 項目 | 內容 |
|------|------|
| 設計 | 中國 60 中心 double-blind, placebo-controlled RCT |
| 族群 | n=1,382；IVT-treated stroke，NIHSS 4-10 |
| 介入 | 發病 6h 內加 ticagrelor + aspirin × 7d vs placebo（後續 aspirin × 83d） |
| Primary | 90d mRS 0-1：**68.7% vs 62.0%**, RR **1.11 (1.03-1.20), p=0.0089** ✅ |
| 安全 | 36h symptomatic ICH **0.9% vs 0.7%**, RR 1.20 (0.37-3.93, NS) |

> IVT 後 6 小時內加上 7 天 DAPT 是新策略——對中等嚴重度 stroke 額外功能效益顯著

---

# SURMOUNT-MAINTAIN — Tirzepatide 維持減重

## [Horn DB, et al. *Lancet* 2026 (online).](https://doi.org/10.1016/S0140-6736(26)00656-2)

| 項目 | 內容 |
|------|------|
| 設計 | Phase 3b RCT；60w open-label 減重 + 52w double-blind 維持 |
| 族群 | n=378（達 MTD 後 3:3:2 分組）；BMI ≥30 或 ≥27+共病 |
| 比較 | 繼續 MTD vs 降至 5 mg vs 換 placebo × 52 週 |
| 112 週體重變化 | MTD **−21.9%** vs 5 mg **−16.6%** vs placebo **−9.9%** (p<0.0001) ✅ |

> 減重後停藥必回升；繼續 tirzepatide MTD 維持最佳，降至 5 mg 仍優於 placebo——**obesity 是慢性病**

---

<!-- _class: divider -->

# European Heart Journal

---

# DIGIT-HF AF subgroup — Digitoxin 在 HFrEF（AF 與否皆有效）

## [Bavendiek U, et al. *Eur Heart J* 2026 (online).](https://doi.org/10.1093/eurheartj/ehag379)

| 項目 | 內容 |
|------|------|
| 背景 | 主試驗 (NEJM 2025, n=1,240)：digitoxin vs placebo |
| 主試驗 primary | All-cause death + HF 住院 **HR 0.82 (0.69-0.98), p=0.03** ✅ |
| 本次分析 | Prespecified subgroup：依基線 AF 狀態 |
| 主要訊息 | Digitoxin 效益 **不受 AF 狀態影響**——sinus 與 AF 皆有一致改善 |

> 強心劑回到 HFrEF 武器庫；台灣 digoxin 仍可使用但須監測 narrow therapeutic window

---

# DECISION — 停 digoxin 反惡化（**Don't stop!**）

## [van der Meer P, et al. *Eur Heart J* 2026 (online).](https://doi.org/10.1093/eurheartj/ehag385)

| 項目 | 內容 |
|------|------|
| 設計 | DECISION trial 子分析：blinded withdrawal at end-of-study |
| 族群 | n=587 已治療中位 36.5 個月 |
| 結果 | 撤 digoxin 後 CV death/worsening HF 由 5.7 → **42.8 events/100 PY**；撤 placebo 維持 5.9 |
| Risk | 撤 digoxin **RR 7.37 (1.56-34.88), p=0.012** ❌ (harm signal) |
| 生理 | HR ↑、SBP ↓、NT-proBNP ↑ |

> 已使用 digoxin 的 HF 病人**不要隨意停藥**；deprescribing 需謹慎

---

# SPRINT/ACCORD pooled — BP Variability 預測 CV 事件

## [Zhao W, et al. *Eur Heart J* 2026 (online).](https://doi.org/10.1093/eurheartj/ehag330)

| 項目 | 內容 |
|------|------|
| 族群 | n=18,415（IPD），中位 12 次 BP 量測，追蹤 3.6 年 |
| 結果 | SBP-VIM 最高 vs 最低 tertile **HR 1.15 (1.00-1.32)** |
| 形狀 | BPV 與 MCE 呈 **J-shape**（過低或過高 BPV 均有害） |
| Prognostic | BPV 預測力 ≈ mean SBP |

> 未來 HTN 管理應同時關注「平均」與「變異性」

---

# EAPCI/EBC Consensus — LM PCI 必須用 Intracoronary Imaging

## [Johnson TW, et al. *Eur Heart J* 2026 (online).](https://doi.org/10.1093/eurheartj/ehag353)

- **核心建議**：所有 LM bifurcation PCI（ACS 與 CCS）皆應使用 **IVUS or OCT**
- 美國與歐洲 guidelines 已將 LM imaging 列為高等級建議
- 本 consensus 提供 planning、guidance、optimization 操作層面指南
- 與本週 EuroIntervention 的 **OCTOBER LM substudy** 相互呼應（OCT vs angio: MACE 14.4% vs 18.4%, HR 0.78, NS）

> LM bifurcation 不再「能 image 就 image」，而是「**必須 image**」

---

# EHJ — 其他焦點 (1/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| **MOMENTUM-3 RAASi 分析** | RAASi 與 LVAD 較低 HRAE 相關 (aRR 0.83) | [DOI](https://doi.org/10.1093/eurheartj/ehag386) |
| **ACHD 首次 AMI** | 預後與一般族群相似 (Holmgren et al.) | [DOI](https://doi.org/10.1093/eurheartj/ehag216) |
| **AMI 機械併發症 SOTA** | Free-wall rupture / pseudoaneurysm / PMR | [DOI](https://doi.org/10.1093/eurheartj/ehag164) |
| **HF 盛行率 ≈ 6 億?** | Cleland 評論：從推估到證據 | [DOI](https://doi.org/10.1093/eurheartj/ehag331) |

---

# EHJ — 其他焦點 (2/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| **CAD 分子機轉** | Atherosclerosis biological insights (von Scheidt & Kovacic) | [DOI](https://doi.org/10.1093/eurheartj/ehag221) |
| **AI in CV Medicine** | Crea editorial：「nothing will be as it was」 | [DOI](https://doi.org/10.1093/eurheartj/ehag361) |
| **MTMR4 與 LQT 風險** | LQT1 vs LQT2 gene-specific 影響 | [DOI](https://doi.org/10.1093/eurheartj/ehag294) |
| **FINEARTS-HF 子分析** | 病毒呼吸道感染與 HFpEF 預後 | [DOI](https://doi.org/10.1093/eurheartj/ehag384) |
| **AF burden vs density** | 量化 AF 新指標 | [DOI](https://doi.org/10.1093/eurheartj/ehag298) |

---

<!-- _class: divider -->

# JACC Family

---

# KARDINAL — Tonlamarsen 在 uncontrolled HTN ❌

## [Laffin LJ, et al. *J Am Coll Cardiol* 2026;87(18):2508-2520.](https://doi.org/10.1016/j.jacc.2026.03.034)

| 項目 | 內容 |
|------|------|
| 設計 | Phase 2 RCT，n=198 randomized after single-dose run-in |
| 介入 | Tonlamarsen 90 mg monthly × 4 doses vs placebo |
| Δangiotensinogen | Monthly **−67.2%** vs single-dose+placebo **−23.0%** (diff **−44.1%**, p<0.0001) ✅ |
| ΔOffice SBP | Monthly **−6.7 mmHg** vs single-dose+placebo **−6.7 mmHg** (diff **−0.1 mmHg**, p=0.97) ❌ |

> **Target engagement ≠ BP benefit**——RAAS 上游 antisense 在已用多種藥物族群達 ceiling effect

---

# HM-APOLLO 301/302 — Single-Pill Low-Dose Triple ✅

## [Sung KC, et al. *J Am Coll Cardiol* 2026;87(18):2392-2411.](https://doi.org/10.1016/j.jacc.2025.12.028)

| 項目 | 內容 |
|------|------|
| 設計 | 韓國 Phase 3 RCT，n>1,000；輕中度 HTN |
| 介入 | LDC-ALC (amlodipine 1.67 + losartan 16.67 + chlorthalidone 4.17 mg) vs amlodipine 5 mg / losartan 50 mg |
| Study 301 | LDC-ALC vs amlodipine ΔSBP −19.1 vs −19.9 (non-inferior, p=0.495) |
| Study 302 | LDC-ALC vs losartan ΔSBP −19.9 vs −16.4 (**superior**, p=0.037) ✅ |

> **超低劑量三合一單顆**作為 initial therapy 安全有效，比 losartan 單藥更佳

---

# XXB750 — NPR-1 Agonist 在 resistant HTN ❌

## [White WB, et al. *J Am Coll Cardiol* 2026;87(18):2373-2387.](https://doi.org/10.1016/j.jacc.2025.11.045)

| 項目 | 內容 |
|------|------|
| 設計 | Phase 2 RCT，n=189，4 dose levels (30/60/120/240 mg monthly SC) × 12 週 |
| 族群 | Resistant HTN，24h SBP ≥135 mmHg 已用 3-4 種藥 |
| 藥理 | XXB750 顯著增加 cGMP（dose-dependent），target engagement 達標 |
| Primary | 24h SBP 變化：**所有劑量與 placebo 無差異** ❌ |
| 安全 | 不良事件略增 |

> NPR-1 agonist 路徑暫時失敗；resistant HTN 仍以 RDN 與 spironolactone 為主流

---

# JACC — POTS Ivabradine vs Propranolol ✅

## [Uppal J, et al. *J Am Coll Cardiol* 2026 (online).](https://doi.org/10.1016/j.jacc.2026.03.167)

| 項目 | 內容 |
|------|------|
| 設計 | Crossover RCT，28 名女性 POTS (平均 33 歲) |
| 介入 | Ivabradine 5 mg BID vs propranolol 10 mg QID vs placebo，各 4 週 |
| 主要結果 | 10 分鐘 head-up tilt ΔHR peak：ivabradine **24**, propranolol **25**, placebo **33** beats/min (p_drug<0.001) |
| 比較 | 兩活性藥物效果相當，皆降至 POTS 診斷閾值（ΔHR <30）以下 |

> Ivabradine 與 propranolol 都有效；ivabradine 副作用較少（無 fatigue/depression），可為 first-line

---

# EAST-AFNET 4 CKD subgroup — ERC 也適用 CKD ✅

## [Schenker N, et al. *J Am Coll Cardiol* 2026 (online).](https://doi.org/10.1016/j.jacc.2026.03.087)

| 項目 | 內容 |
|------|------|
| 設計 | EAST-AFNET 4 prespecified secondary；n=2,742；23% CKD (GFR <60) |
| 族群 | Recently diagnosed AF + stroke risk factors |
| ERC effect | No CKD HR **0.84** (p<0.001)；CKD HR **0.67** (p<0.001) |
| Interaction | P_interaction = 0.133（一致效果） ✅ |
| 安全 | CKD 增加安全事件但與 ERC 無交互作用 |

> CKD 不應成為延後 early rhythm control 的理由——CKD + AF 患者更應積極考慮

---

# LIFE-BTK 3-Year — DRS 在 CLTI 持久優勢 ✅

## [Parikh SA, et al. *J Am Coll Cardiol* 2026 (online).](https://doi.org/10.1016/j.jacc.2026.04.008)

| 項目 | 內容 |
|------|------|
| 設計 | n=261，DRS (Esprit BTK) vs PTA (2:1)；CLTI + infrapopliteal |
| 3-yr Primary efficacy | KM **59.5% vs 44.8%, p=0.0025** ✅ |
| Restenosis | 38.0% vs 49.0% |
| CD-TLR | 10.2% vs 18.4%（adjusted HR 0.46, 95% CI 0.22-0.97） |
| 安全 | Limb salvage 93.8% vs 95.7%（comparable） |

> DRS 在 BTK CLTI 提供持久的 patency 與較少 re-intervention——3 年成熟證據支持取代 PTA

---

# JACC — Multiarterial Grafting IV Analysis ❌

## [Schaffer JM, et al. *J Am Coll Cardiol* 2026 (online).](https://doi.org/10.1016/j.jacc.2026.03.044)

| 項目 | 內容 |
|------|------|
| 設計 | Medicare 1.29M CABG (2001-2019)；surgeon MAG rate 為 IV |
| 傳統 risk-adjust | MAG **10.74 yrs** vs SAG **10.33 yrs** (+0.41 yr) |
| IV model | MAG **10.38 yrs** vs SAG **10.38 yrs** (Δ 0.01 yr) ❌ |
| 結論 | 觀察性研究高估 MAG 效益——unmeasured confounding 主導 |

> MAG 在 selected patients 合理，但**不應 routine 推行於所有 CABG**——與 ROMA/ART 等 RCT 一致

---

# JACC — 高血壓主題刊：其他焦點

| 主題 | 重點 | 連結 |
|------|------|------|
| **AHA Workshop BP 量測** | 跨年齡 BP 評估更新報告 | [DOI](https://doi.org/10.1016/j.jacc.2026.02.5124) |
| **Global Hypertension 2000-2020** | 知曉率、治療率、控制率 disparities | [DOI](https://doi.org/10.1016/j.jacc.2025.12.091) |
| **BETTER-BP** | Behavioral economics 改善 adherence | [DOI](https://doi.org/10.1016/j.jacc.2025.10.062) |
| **STEP trial BP trajectory** | 老年高風險患者 BP 軌跡與預後 | [DOI](https://doi.org/10.1016/j.jacc.2026.01.090) |
| **PM 與 HTN 死亡** | 中國 2.1M 案例 case-crossover | [DOI](https://doi.org/10.1016/j.jacc.2026.01.006) |

---

# JACC — 其他焦點

| 主題 | 重點 | 連結 |
|------|------|------|
| **Istaroxime SEISMiC pooled** | 心因性休克 hemodynamic + arrhythmia 改善 | [DOI](https://doi.org/10.1016/j.jchf.2026.103103) |
| **Door-to-Lactate Clearance** | Lactate clearance 為休克復甦關鍵 surrogate | [DOI](https://doi.org/10.1016/j.jchf.2026.103104) |
| **CPVT LCSD** | 左心交感切除降低 CPVT 患者 ICD 需求 | [DOI](https://doi.org/10.1016/j.jacep.2026.03.027) |
| **HDP in US 2016-2024** | 妊娠高血壓盛行率持續上升 | [DOI](https://doi.org/10.1016/j.jacc.2026.03.154) |
| **CD36 LOF 與 DCM** | All of Us：CD36 LOF 與 dilated cardiomyopathy | [DOI](https://doi.org/10.1016/j.jchf.2026.103099) |

---

<!-- _class: divider -->

# Circulation Family

---

# CADENCE — Sotatercept 在 CpcPH-HFpEF 💡

## [Gomberg-Maitland M, et al. *Circulation* 2026;153(19):1446-1459.](https://doi.org/10.1161/CIRCULATIONAHA.126.079918)

| 項目 | 內容 |
|------|------|
| 設計 | Phase 2 RCT；n=164；sotatercept 0.3 vs 0.7 mg/kg vs placebo q3w × 24w |
| 族群 | HFpEF + combined post+precapillary PH（mPAP ↑, PAWP ↑, PVR ↑） |
| Primary ΔPVR | 0.3 mg/kg **−1.02 WU (p=0.004)** ✅；0.7 mg/kg **−0.75 WU (p=0.024)** ✅ |
| 次要 | mPAP **−9.2 mmHg**；PAWP −2.5~−3.0；6MWD +20 m (0.3 mg/kg) |
| 安全 | Hgb ↑、腹瀉 |

> **PAH 之活素訊號抑制劑跨界進入 HFpEF-CpcPH**——首個 phase 2 positive proof-of-concept；Merck 規劃 phase 3

---

# AGENT 上市後 — DCB 在美國快速擴張

## [Lalani C, et al. *Circ Cardiovasc Interv* 2026 (online).](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016625)

| 項目 | 內容 |
|------|------|
| 期間 | 2024 年 4 月 FDA 核准 ~ 2025 年 6 月 |
| 數量 | n=14,946 DCB，12,337 患者，704 中心 |
| ISR PCI DCB 使用 | **<1% → 17.5%/月** 快速擴張 |
| 特徵 | DCB 群 imaging 使用 **54.5%**（vs DES 35%），atherectomy 14.9% |
| 安全 | 院內不良事件率與 DES 相當（SMD <10%） |

> DCB 已成為 US ISR 主流；non-ISR off-label 使用亦增長

---

# RESTORE FIH — Laser/Optics IVL for Calcified Coronary 💡

## [Price MJ, et al. *Circ Cardiovasc Interv* 2026 (online).](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016874)

- 首次人體研究
- 機制：**雷射 + 光學介導**衝擊波（vs 現行電液壓 IVL，如 Shockwave Coronary IVL）
- 適應症：嚴重鈣化冠脈病灶
- 安全性與初步成效獲確認
- 須後續大型試驗驗證

> 鈣化病灶介入工具持續擴展——除了現行 IVL/Atherectomy 之外的新選項

---

# AD-HOC Registry — PPM after TAVR in Sievers BAV

## [Fabris T, et al. *Circ Cardiovasc Interv* 2026 (online).](https://doi.org/10.1161/CIRCINTERVENTIONS.125.015994)

| 項目 | 內容 |
|------|------|
| 設計 | Retrospective multicenter (24 centers), n=781 |
| 族群 | 嚴重 AS + Sievers type 1 BAV 接受 TAVR (2016-2023) |
| mPPM vs pPPM | **22% vs 8%** (p<0.001)；mPPM 多於 pPPM |
| 風險因子 | Balloon-expandable valve 與 mPPM 及 pPPM 皆獨立相關 |
| Small annulus (≤430 mm²) | pPPM 與 all-cause mortality 相關（但與 CV mortality 無關） |

> BAV TAVR 在 small annulus 須更謹慎的 sizing 計畫

---

# Circulation 其他焦點

| 主題 | 重點 | 連結 |
|------|------|------|
| **AHA 2026 — 二級預防 after CABG** | 更新 GDMT、LDL、cardiac rehab 重點 | [DOI](https://doi.org/10.1161/CIR.0000000000001434) |
| **Laroprovstat (AZD0780)** | 首個口服小分子 PCSK9i，phase 1 LDL-C 降 80% | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.125.075973) |
| **FOURIER + FOURIER-OLE** | Evolocumab 早期 vs 晚期啟動與動脈瘤事件 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.125.077140) |
| **Pediatric HCM Massive LVH** | 兒童 HCM 預後分析 multi-registry | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.078843) |
| **AHA — Pediatric ADHF** | 兒童急性失代償性 HF 評估管理 | [DOI](https://doi.org/10.1161/CIR.0000000000001428) |
| **AHA — RV Failure 評估** | RV failure 分子、代謝、影像方法 | [DOI](https://doi.org/10.1161/CIR.0000000000001422) |

---

<!-- _class: divider -->

# EuroIntervention<br>(Mainz 2026 Issue)

---

# DOUBLE-CHOICE — ACURATE neo2 vs Evolut TAVI ✅

## [Feistritzer HJ, et al. *EuroIntervention* 2026;22(10):555-565.](https://doi.org/10.4244/EIJ-D-26-00001)

| 項目 | 內容 |
|------|------|
| 設計 | 德國 10 中心 open-label, 2×2 factorial, non-inferiority RCT；n=835 |
| 族群 | 嚴重 AS，**selected anatomies**（解剖適合 ACURATE neo2） |
| Primary | 30d composite (死亡+stroke+modPVR+PPM)：**15.4% vs 30.4%**, p_non-inf<0.001, p_diff<0.001 ✅ |
| 主要差異 | **PPM 11.2% vs 26.5%** (p<0.001) |
| Mod/Severe PVR | 1.3% vs 1.7%（兩者皆低） |
| ⚠️ 重要背景 | ACURATE neo2 已於 **2026/05 由 BSC 自市場下架** |

> 「**ACURATE 平台設計理念**」（supra-annular、low radial force）仍是未來 TAV 設計重要參考

---

# GLUCO-TAVI — Glucocorticoids 預防 TAVI 後 PPM ❌

## [Fuertes-Kenneally L, et al. *EuroIntervention* 2026;22(10):545-554.](https://doi.org/10.4244/EIJ-D-26-00032)

| 項目 | 內容 |
|------|------|
| 設計 | Pilot PROBE RCT；n=100；西班牙單中心 |
| 介入 | Methylprednisolone 7 mg/kg + prednisone 5d vs 標準照護 |
| 1m PPM | **8% vs 16%**, RR **0.50 (0.16-1.55), p=0.23** (NS but trend) |
| 1y PPM | RR 0.67 (0.26-1.73, NS) |
| 安全 | 無安全性問題 |

> 數值朝預期方向但 sample 不足——須大型 RCT 確認；anti-inflammatory 預防 TAVI conduction disturbance 仍合理假設

---

# SPYRAL 36-Month — RDN 長期 BP 效益 ✅

## [Kandzari DE, et al. *EuroIntervention* 2026;22(10):585-593.](https://doi.org/10.4244/EIJ-D-26-00161)

| 項目 | 內容 |
|------|------|
| 族群 | n=2,137 SPYRAL programme pooled |
| 基線 | OSBP 163, ASBP 152, 藥物 3.8 種 |
| 36 個月 | ΔOSBP **−18.1 mmHg**, ΔASBP **−13.3 mmHg** (p<0.0001) |
| 藥物 | 由 3.8 → 3.5 種（NS but trend ↓） |
| Clinical responder | **88%** 達 ≥10 mmHg OSBP 或 ≥5 mmHg ASBP 或 ≥1 種藥物減量 |

> RF-RDN 效益**耐用 3 年**——支持作為 uncontrolled HTN guideline-recommended therapy

---

# OCTOBER LM substudy — OCT vs Angio in True LM Bifurcation

## [Holck EN, et al. *EuroIntervention* 2026;22(10):566-574.](https://doi.org/10.4244/EIJ-D-25-01337)

| 項目 | 內容 |
|------|------|
| 設計 | OCTOBER trial true LM bifurcation 病灶 n=227 |
| 可行性 | 98% pre-stenting + 96% final pullback 完成 |
| 限制 | 近段 LM ostium 顯影率 43%（受 guide catheter shadowing 影響） |
| MACE | OCT 14.4% vs Angio 18.4%，HR **0.78 (0.39-1.51)**, NS |

> 與主試驗方向一致；LM ostium 仍是 OCT 限制——與 EAPCI/EBC consensus 互相參照

---

# Emilsson — Ticagrelor vs Clopidogrel in DOAC + ACS PCI

## [Emilsson OL, et al. *EuroIntervention* 2026;22(10):575-584.](https://doi.org/10.4244/EIJ-D-25-01373)

| 項目 | 內容 |
|------|------|
| 設計 | SWEDEHEART registry cohort, n=3,708, 2014-2022 |
| 族群 | DOAC + ACS PCI，dual antithrombotic（無 aspirin） |
| MACE | 16.7% vs 16.6%, aHR **1.02** (NS) |
| Bleeding | 4.9% vs 3.7%, aHR **1.53 (1.06-2.22)** ❌ |
| Mortality | 6.6% vs 6.2% (NS) |

> **Clopidogrel 優於 ticagrelor**——無 ischemic 好處但出血明顯增加，與 ESC 2024 ACS guideline 一致

---

# EuroIntervention 其他焦點

| 主題 | 重點 | 連結 |
|------|------|------|
| **TAVI timing in AS 回顧** | 早期介入 vs symptomatic 介入（Craig et al.） | [DOI](https://doi.org/10.4244/EIJ-D-25-00754) |
| **TAVI 後發炎 editorial** | Inflammation as therapeutic target post-TAVI | [DOI](https://doi.org/10.4244/EIJ-D-26-00452) |
| **Prasugrel vs ticagrelor 辯論** | ACS 中應該優先選擇哪一個？pros and cons | [DOI](https://doi.org/10.4244/EIJ-E-26-00004) |
| **DOUBLE-CHOICE editorial** | 「不必要的告別」——對 ACURATE neo2 下市反思 | [DOI](https://doi.org/10.4244/EIJ-E-26-00008) |
| **Anticoag + ACS antithrombotic** | "Sledgehammer or scalpel" editorial | [DOI](https://doi.org/10.4244/EIJ-D-26-00417) |

---

<!-- _class: divider -->

# 整合 Take Home

---

# 本週 5 大臨床啟示

> **Pearl 1 — 老藥重生**：DIGIT-HF + DECISION 共同強調 **digitoxin/digoxin 在已優化 GDMT 之上仍有 incremental 效益**；既已開始的患者**不要隨意停藥**

> **Pearl 2 — 新藥當心**：tonlamarsen (RAAS antisense)、XXB750 (NPR-1 agonist) phase 2 皆 **target engagement 達標但 BP 終點失敗**——「surrogate ≠ outcome」

> **Pearl 3 — 結構介入**：DOUBLE-CHOICE 證實 ACURATE neo2 的低 PPM 優勢；雖然 valve 下市，但**設計理念**（supra-annular、low radial force）值得繼承

> **Pearl 4 — 急性中風新策略**：TAPIS 顯示 IVT 後 6 小時內加 7 天 DAPT 可提升功能恢復（無顯著 ICH）；ORIENTAL-MeVO 將 thrombectomy 適應症延伸至 MeVO

> **Pearl 5 — RAAS 與 HFpEF**：CADENCE 顯示 sotatercept 跨界 HFpEF-CpcPH；MOMENTUM-3 RAASi 分析顯示 LVAD 患者 RAASi 與低 bleeding 相關——RAAS 在 HF 仍有可挖掘的應用

---

<!-- _class: small-text -->

# 縮寫對照

| 縮寫 | 全稱 |
|------|------|
| ACHD | Adult Congenital Heart Disease |
| AS / BAV | Aortic Stenosis / Bicuspid Aortic Valve |
| BPV | Blood Pressure Variability |
| CABG / MAG / SAG | Coronary Artery Bypass Grafting / Multi / Single Arterial Grafting |
| CKD | Chronic Kidney Disease |
| CLTI | Chronic Limb-Threatening Ischemia |
| CpcPH | Combined Post- and Precapillary Pulmonary Hypertension |
| DAPT / DOAC | Dual Antiplatelet Therapy / Direct Oral Anticoagulant |
| DCB / DRS | Drug-Coated Balloon / Drug-eluting Resorbable Scaffold |
| ERC | Early Rhythm Control |
| GDMT | Guideline-Directed Medical Therapy |
| HFrEF / HFpEF | HF with Reduced / Preserved Ejection Fraction |
| HRAE | Hemocompatibility-Related Adverse Event |
| IVT / IVL | Intravenous Thrombolysis / Intravascular Lithotripsy |
| LDC | Low-Dose Combination |
| LM | Left Main coronary |
| LVAD | Left Ventricular Assist Device |
| MeVO | Medium Vessel Occlusion |
| NPR-1 | Natriuretic Peptide Receptor-1 |
| OCT / IVUS | Optical Coherence Tomography / Intravascular Ultrasound |
| POTS | Postural Orthostatic Tachycardia Syndrome |
| PPM | Permanent Pacemaker / Prosthesis-Patient Mismatch |
| PVR / mPAP / PAWP | Pulmonary Vascular Resistance / mean PA / PA Wedge Pressure |
| RAAS(i) / RDN | Renin-Angiotensin-Aldosterone System (inhibitor) / Renal Denervation |
| TAVI/TAVR | Transcatheter Aortic Valve Implantation/Replacement |

---

<!-- _class: ref -->

# 參考文獻 (1/3)

**NEJM**
1. Hu W, et al. ORIENTAL-MeVO. [*N Engl J Med* 2026;394(19):1894-1904.](https://doi.org/10.1056/NEJMoa2514120)
2. Ospel JM, Hill MD. Editorial. [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMe2601852)

**Lancet**
3. Wang A, et al. TAPIS. [*Lancet* 2026;407(10542):1919-1928.](https://doi.org/10.1016/S0140-6736(26)00757-9)
4. Horn DB, et al. SURMOUNT-MAINTAIN. [*Lancet* 2026.](https://doi.org/10.1016/S0140-6736(26)00656-2)

**European Heart Journal**
5. Bavendiek U, et al. DIGIT-HF AF subgroup. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag379)
6. van der Meer P, et al. DECISION. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag385)
7. Zhao W, et al. SPRINT/ACCORD BPV. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag330)
8. Johnson TW, et al. EAPCI/EBC LM imaging consensus. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag353)
9. Isath A, et al. MOMENTUM-3 RAASi. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag386)
10. Holmgren L, et al. ACHD + AMI. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag216)
11. Lorusso R, et al. AMI mechanical complications SOTA. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag164)
12. Cleland JGF, et al. HF prevalence. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag331)

---

<!-- _class: ref -->

# 參考文獻 (2/3)

**JACC Family**
13. Laffin LJ, et al. KARDINAL. [*J Am Coll Cardiol* 2026;87(18):2508-2520.](https://doi.org/10.1016/j.jacc.2026.03.034)
14. Sung KC, et al. HM-APOLLO. [*J Am Coll Cardiol* 2026;87(18):2392-2411.](https://doi.org/10.1016/j.jacc.2025.12.028)
15. White WB, et al. XXB750. [*J Am Coll Cardiol* 2026;87(18):2373-2387.](https://doi.org/10.1016/j.jacc.2025.11.045)
16. Uppal J, et al. POTS Ivabradine. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.03.167)
17. Schenker N, et al. EAST-AFNET 4 CKD. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.03.087)
18. Parikh SA, et al. LIFE-BTK 3-yr. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.04.008)
19. Schaffer JM, et al. MAG IV analysis. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.03.044)
20. Biegus J, et al. Istaroxime SEISMiC pooled. [*JACC Heart Fail* 2026.](https://doi.org/10.1016/j.jchf.2026.103103)
21. Bos JM, et al. CPVT LCSD. [*JACC Clin Electrophysiol* 2026.](https://doi.org/10.1016/j.jacep.2026.03.027)
22. Lam EL, et al. HDP US 2016-2024. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.03.154)

**Circulation Family**
23. Gomberg-Maitland M, et al. CADENCE. [*Circulation* 2026;153(19):1446-1459.](https://doi.org/10.1161/CIRCULATIONAHA.126.079918)
24. Lalani C, et al. AGENT post-approval. [*Circ Cardiovasc Interv* 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016625)
25. Price MJ, et al. RESTORE FIH. [*Circ Cardiovasc Interv* 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016874)
26. Fabris T, et al. AD-HOC Registry. [*Circ Cardiovasc Interv* 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.125.015994)
27. Ruel M, et al. AHA Secondary Prevention CABG 2026. [*Circulation* 2026.](https://doi.org/10.1161/CIR.0000000000001434)

---

<!-- _class: ref -->

# 參考文獻 (3/3)

28. Vega RB, et al. Laroprovstat phase 1. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.125.075973)
29. Zimerman A, et al. FOURIER aneurysm. [*Circulation* 2026;153(19):1516-1519.](https://doi.org/10.1161/CIRCULATIONAHA.125.077140)
30. Przybylski R, et al. Pediatric HCM massive LVH. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.078843)

**EuroIntervention (Mainz 2026 Issue)**
31. Feistritzer HJ, et al. DOUBLE-CHOICE. [*EuroIntervention* 2026;22(10):555-565.](https://doi.org/10.4244/EIJ-D-26-00001)
32. Fuertes-Kenneally L, et al. GLUCO-TAVI. [*EuroIntervention* 2026;22(10):545-554.](https://doi.org/10.4244/EIJ-D-26-00032)
33. Kandzari DE, et al. SPYRAL 36-mo. [*EuroIntervention* 2026;22(10):585-593.](https://doi.org/10.4244/EIJ-D-26-00161)
34. Holck EN, et al. OCTOBER LM substudy. [*EuroIntervention* 2026;22(10):566-574.](https://doi.org/10.4244/EIJ-D-25-01337)
35. Emilsson OL, et al. SWEDEHEART DOAC+ACS. [*EuroIntervention* 2026;22(10):575-584.](https://doi.org/10.4244/EIJ-D-25-01373)
36. Craig NJ, et al. TAVI timing review. [*EuroIntervention* 2026;22(10):530-544.](https://doi.org/10.4244/EIJ-D-25-00754)
37. Pilgrim T, Cozzi O. Inflammation post-TAVI editorial. [*EuroIntervention* 2026.](https://doi.org/10.4244/EIJ-D-26-00452)
38. Angiolillo DJ, et al. Prasugrel vs ticagrelor debate. [*EuroIntervention* 2026.](https://doi.org/10.4244/EIJ-E-26-00004)
39. Blankenberg S, Ludwig S. DOUBLE-CHOICE editorial. [*EuroIntervention* 2026.](https://doi.org/10.4244/EIJ-E-26-00008)

**外部報導**
40. ESC Press Office. [DIGIT-HF main trial release.](https://www.escardio.org/The-ESC/Press-Office/Press-releases/Digitoxin-improves-outcomes-in-advanced-heart-failure)
41. ACC. [CADENCE: Sotatercept in CpcPH-HFpEF.](https://www.acc.org/latest-in-cardiology/articles/2026/03/25/21/27/sun-1045am-cadence-acc-2026)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**讀書會共筆整理人**
**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考，不構成臨床治療建議。*
