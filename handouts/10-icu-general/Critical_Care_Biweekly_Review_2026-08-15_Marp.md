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
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-08-15'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧

## 2026-08-01 ～ 2026-08-15

**謝慕揚 MD, PhD, FESC** | 2026-08-15

涵蓋：ICM、Critical Care、CCM、Lancet Respir Med、AJRCCM、Chest、Resuscitation、Shock

> 讀書會內部共筆，僅供醫療專業人員教學討論參考

---

<!-- _class: abbr -->

# 縮寫對照 (1/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| RCT | Randomized Controlled Trial | 隨機對照試驗 |
| HTE | Heterogeneous Treatment Effect | 異質治療效應 |
| RR / OR / HR | Relative Risk / Odds Ratio / Hazard Ratio | 相對風險／勝算比／風險比 |
| aOR / aHR | Adjusted OR / Adjusted HR | 校正勝算比／校正風險比 |
| CI | Confidence Interval | 信賴區間 |
| ICU / MICU | (Mobile) Intensive Care Unit | （行動）加護病房／團隊 |
| EMS | Emergency Medical Services | 緊急醫療服務 |
| SOFA | Sequential Organ Failure Assessment | 連續器官衰竭評估 |
| CFS | Clinical Frailty Scale | 臨床衰弱量表 |
| PM | Psychoactive Medication | 精神作用藥物 |
| NEWS2 | National Early Warning Score 2 | 國家早期預警評分 2 |

---

<!-- _class: abbr -->

# 縮寫對照 (2/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| ARDS | Acute Respiratory Distress Syndrome | 急性呼吸窘迫症候群 |
| AHRF | Acute Hypoxaemic Respiratory Failure | 急性低氧呼吸衰竭 |
| IMV | Invasive Mechanical Ventilation | 侵襲性機械通氣 |
| SBT | Spontaneous Breathing Trial | 自主呼吸試驗 |
| AECOPD | Acute Exacerbation of COPD | 慢性阻塞性肺病急性惡化 |
| DE / DTF | Diaphragmatic Excursion / Diaphragm Thickening Fraction | 橫膈位移／增厚分率 |
| LABA | Long-Acting β-Agonist | 長效乙型受體促效劑 |
| ROSC / OHCA | Return of Spontaneous Circulation / Out-of-Hospital Cardiac Arrest | 自發性循環恢復／到院前心跳停止 |
| RRT / CRRT | (Continuous) Renal Replacement Therapy | （連續）腎臟替代治療 |
| NUF | Net Ultrafiltration | 淨超過濾 |
| IHD / CVD | Ischemic Heart Disease / Cardiovascular Disease | 缺血性心臟病／心血管疾病 |

---

<!-- _class: small-text -->

# 本期 10 大重點 (Key Pearls)

1. **到院前 1 小時復甦 bundle** 在 septic shock：主要終點**陰性**（RR 0.81，p=0.16）
2. **超早期 vasopressin**（norepinephrine 升壓後 0–3 h）與較低死亡相關（HR 0.82，觀察性）
3. 抗生素急迫性：**NEWS2 ≥7 比休克與否更能鎖定會因延遲而死亡者**
4. CRRT：**體液平衡**才是關鍵，NUF 率本身與死亡無獨立關聯
5. RRT 整體有害（RD +6.1%），但 creatinine 高/尿少/BUN 高者可能獲益
6. AECOPD 脫離：橫膈超音波（DE AUC 0.92）具參考，但只能當輔助
7. ICU 遠距醫療：不提高脫離成功率，但增 SBT、縮短成功者通氣天數
8. **AHRF 佔 ICU 病人 50%**，severe + IMV 死亡達 47%
9. 老年 septic shock 加護後衰弱：病前衰弱、SOFA、**corticosteroid** 為預測因子
10. COPD+CVD 的 beta-blocker：僅心衰竭/IHD 降死亡，LABA 併用削弱效益

---

<!-- _class: divider -->

# 一、呼吸治療與機械通氣

---

# 脫離呼吸器：3S 架構 (3S Framework)

## Baptistella AR, et al. Chest 2026｜https://doi.org/10.1016/j.chest.2026.08.001 (PMID 42580515)

- **Screening（篩選）**：鎮靜管理、維持呼吸/肢體肌力與心功能、由控制轉部分支持
- **Separating（分離）**：SBT 準備度、執行 SBT、拔管風險評估與決策
- **Securing（穩固）**：拔管後管理、預防呼吸衰竭
- 七個 hallmark、三階段連續銜接；強調脫離是**動態、整合性**流程而非孤立參數

> **啟示**：以「篩選→分離→穩固」作為病房脫離協定與教學骨架

---

# 橫膈超音波預測 AECOPD 脫離 (Meta-analysis)

## Zhou X, et al. Crit Care 2026｜https://doi.org/10.1186/s13054-026-06240-1 (PMID 42576250)

23 篇、2,000 人；4 參數可量化合成

| 參數 | Sensitivity | Specificity | AUC |
|------|:-----------:|:-----------:|:---:|
| **DE（橫膈位移）** | 0.85 | 0.85 | **0.92** |
| DTF（增厚分率） | 0.84 | 0.77 | 0.88 |
| D-RSBI | 0.74 | 0.88 | 0.85 |
| DCV（收縮速度） | — | — | 0.70 |

> **啟示**：DE 表現最佳、D-RSBI 抓高失敗風險；多為單中心、閾值後驗、異質性高 → **僅為輔助，不可單獨決定拔管**

---

# ICU 遠距醫療與脫離：ERIC 試驗次分析

## Adam MF, et al. Crit Care 2026｜https://doi.org/10.1186/s13054-026-06234-z (PMID 42568095)

- 柏林 10 ICU cluster stepped-wedge RCT 次分析，n=308
- **SBT 執行比例：51% vs 27%（p<0.001）** — 顯著較多
- 脫離成功率無差異（28% vs 36%；p=0.32）
- **成功脫離者 IMV 天數縮短：7 [4–10] vs 9 [6–20] 天（p=0.031）**

> **啟示**：遠距醫療未提高脫離成功率，但透過確保更頻繁 SBT，**落實既有脫離潛力**、縮短通氣天數

---

# Corticosteroids 於 ARDS：老爭議、新洞見

## Daoud T, Villar J, Annane D. Intensive Care Med 2026｜https://doi.org/10.1007/s00134-026-08567-3 (PMID 42593538)

- 臨床證據支持**中重度 ARDS**（COVID-19 ARDS、severe CAP）使用，可降死亡、縮短通氣
- **Hyperinflammatory 表型與 septic ARDS 較可能獲益**；influenza/non-septic 證據有限或矛盾
- 副作用（代謝、ICU-acquired weakness）仍未充分描述
- 未來：biomarker、adaptive platform trial、肺靶向給藥、selective GR modulator

> **啟示**：類固醇為**情境依賴**療法 — 效益受病因、病程、發炎表型與時機影響，勿一體適用

---

# AHRF 流行病學：極常見且死亡率高

## von Düring S, et al. Crit Care Med 2026｜https://doi.org/10.1097/CCM.0000000000007284 (PMID 42584185)

- 多倫多 9 ICU、21,714 人 registry（2014–2023）
- **50% 病人於入 ICU 24 h 內符合 AHRF**（Pao₂/Fio₂ ≤300 或 SpO₂/Fio₂ ≤315）
- 其中 **76% 需 IMV**，多採 lung-protective ventilation
- **ICU 死亡：整體 23%；severe AHRF + IMV 達 47%**

> **啟示**：AHRF 常見且多沿用 ARDS 策略；務實、標準化定義有助辨識與研究

---

<!-- _class: divider -->

# 二、Sepsis 與血流動力學

---

# ⭐ 到院前 1 小時復甦 bundle：主要終點陰性

## Jouffroy R, Annane D, et al. Crit Care Med 2026｜https://doi.org/10.1097/CCM.0000000000007283 (PMID 42573415)

- 法國多中心、open-label、**cluster RCT**，n=381；MICU 救護車執行早期抗生素 + ≤35 mL/kg 輸液 + 必要時 norepinephrine/hydrocortisone
- **28 天全因死亡：22% vs 27%；RR 0.81（95% CI 0.61–1.08；p=0.16）— 無顯著差異**
- 次要終點兩組相似；收案中心不均、兩組實際照護差異小

> **⚠️ 這是「方向看似有利、主要終點失敗」的 negative trial**，不可誤讀為 positive。到院前包裹式復甦**未能**降低死亡

---

# 超早期 vs 早期 vasopressin (Target Trial Emulation)

## Nakashima T, et al. Intensive Care Med 2026｜https://doi.org/10.1007/s00134-026-08575-3 (PMID 42578996)

- MIMIC-IV + eICU 資料仿真，n=3,810；norepinephrine ≥0.25 μg/kg/min 後 0–3 h vs >3–6 h 加 vasopressin
- **28 天死亡：48.1% vs 53.0%**（RD −5.0 個百分點；**HR 0.82，95% CI 0.78–0.85**）
- 較低 RRT（HR 0.68）、continuous RRT（HR 0.61）；與 AKI 發生無關

> **啟示**：較早加 vasopressin 或有利，但為**觀察性仿真、非 RCT**，僅 hypothesis-generating，尚不改變 SSC 流程

---

# 抗生素急迫性：NEWS2 vs 休克狀態

## Rhee C, Singer M, et al. Lancet Respir Med 2026｜https://doi.org/10.1016/S2213-2600(26)00187-6 (PMID 42556377)

- 美國 9 院回溯，99,667 人次
- 休克者：每延遲 1 h 抗生素→死亡上升（**aOR 1.15**）；**非休克者無關聯（aOR 1.03）**
- **NEWS2+ ≥7（含 86% 無休克者）：每延遲 1 h 死亡仍上升（aOR 1.05–1.07）**；NEWS2+ <7 無關聯

> **啟示**：NEWS2 ≥7 能鎖定「延遲抗生素會增加死亡」者，涵蓋許多無休克者 → 比單靠休克更好地導向緊急抗生素（評論 PMID 42556378）

---

<!-- _class: divider -->

# 三、腎臟與腎臟替代治療

---

# ⭐ CRRT：NUF 率 vs 體液平衡

## Monai NC, et al. Crit Care Med 2026｜https://doi.org/10.1097/CCM.0000000000007289 (PMID 42584203)

- Bern + Amsterdam 雙中心，973 人、6,914 CRRT 天
- 校正體液平衡後，**NUF 率與 28 天死亡無獨立關聯**
- 中介分析：高 NUF 的表面存活優勢**透過達成更負體液平衡**而來
- **更正的體液平衡 → 死亡等不良結局上升**

> **啟示**：勿孤立設定 NUF 率；把 NUF 當成達到病人個體化 **fluid balance 目標**的手段

---

# RRT 的異質治療效應 (Causal Forest)

## Nakamura S, et al. Crit Care Med 2026｜https://doi.org/10.1097/CCM.0000000000007282 (PMID 42573413)

- 日本全國 registry；PS matching 後 18,794 人
- **整體：RRT 與較高院內死亡相關（RD +6.1 個百分點）**
- **Causal forest 顯示顯著 HTE**：creatinine 高、尿量少、BUN 高者**可能獲益**；腎功能相對保留者更可能受害

> **啟示**：RRT 整體有害但特定次族群獲益 → 支持以資料驅動、個體化界定最佳 RRT 適應症，避免過度使用

---

<!-- _class: divider -->

# 四、心跳停止與復甦

---

# 急診醫師重症訓練與 OHCA 結局

## Kreutz J, et al. Resuscitation 2026｜https://doi.org/10.1016/j.resuscitation.2026.111264 (PMID 42600766)

- 德國 EMS 區回溯，非外傷 OHCA，n=1,426
- ROSC 各組無顯著差異（39.9/42.5/45.7%）
- **有重症訓練者：血管通路更快、更早升壓；出院存活 18.0% vs 12.2%（p=0.047）**
- 校正後：ROSC 下入院 OR 1.42、**出院存活 OR 1.59（1.05–2.40）**

> **啟示**：院前重症技能（快速通路、及早升壓）或與較佳存活相關（觀察性、假說生成）

---

# 心因性休克的地理可近性與死亡

## Choi KH, et al. Crit Care Med 2026｜https://doi.org/10.1097/CCM.0000000000007287 (PMID 42565652)

- 南韓 NHIS，80,263 人（2017–2022），依到院時間分層
- **院內死亡：29.6%（<10 分）→ 38.8%（>60 分）**；>60 分 aOR **1.51**
- 1 年死亡 >60 分 aHR 1.31；de novo 與 acute-on-chronic 一致

> **啟示**：到院越慢，心因性休克院內與長期死亡越高 → 需**區域協調 shock network 與早期到院前分流**

---

<!-- _class: divider -->

# 五、ICU 結局、復健與長期照護

---

# 重症肌肉流失：降解上升為主軸 (Meta-analysis)

## González-Seguel F, et al. Crit Care Med 2026｜https://doi.org/10.1097/CCM.0000000000007288 (PMID 42565658)

- 75 篇、2,023 病人 / 642 對照
- **type II 肌纖維萎縮**為主，伴壞死、粒線體/發炎/纖維化、泛素-蛋白酶體/自噬上調
- **肌纖維橫斷面積較對照低 22%**（ICU 出院前後皆顯著）
- **蛋白質合成無差異；蛋白質降解標記一致較高**

> **啟示**：ICU 肌無力以「降解上升」而非「合成下降」為主 → 抑制過度降解 + 早期復健可能比單增蛋白攝取更關鍵

---

# 老年 septic shock 的加護後衰弱

## Yamamoto R, et al. Crit Care Med 2026｜https://doi.org/10.1097/CCM.0000000000007304 (PMID 42584186)

- 日本血壓目標 RCT post hoc，≥65 歲，339 存活者
- 90 天 CFS：**severe（≥7）36.0%**
- 獨立預測：**病前 CFS aOR 2.03/分**、SOFA aOR 1.16/分、**corticosteroid aOR 1.72**
- 類固醇關聯在有基礎衰弱者最明顯

> **啟示**：病前衰弱、器官衰竭嚴重度、**類固醇使用**預測嚴重長期衰弱 → 類固醇與長期衰弱的關聯值得警覺

---

# ICU 存活者精神藥物：近半缺乏支持診斷

## Wu TT, et al. Crit Care Med 2026｜https://doi.org/10.1097/CCM.0000000000007310 (PMID 42593167)

- 美國 claims，需 IMV、入 ICU 前一年未用 PM，n=7,898
- 出院 30 天內 **5.3% 新開 PM**（anxiolytics/antidepressants/antipsychotics/sleep aids）
- **42.8% 無支持診斷碼**（antipsychotics 52.4% 最高）；延續達 2 年

> **啟示**：出院用藥審視與追蹤應納入 post-ICU 照護，避免不必要的長期精神藥物暴露

---

<!-- _class: divider -->

# 六、其他值得關注

---

<!-- _class: small-text -->

# 其他焦點 (Honorable Mentions)

| 主題 | 重點 | 連結 |
|------|------|------|
| **數十年 ICU RCT 回顧**（Martin-Loeches, ICM） | 許多有生理理由的介入未改善結局；進步多來自優化支持、避免醫源傷害、去實作 | https://doi.org/10.1007/s00134-026-08579-z |
| **COPD+CVD beta-blocker**（Suissa, Chest） | 全因死亡 HR 0.88；**僅心衰竭(0.77)/IHD(0.84)**，AF/HTN 無效；LABA 併用削弱 | https://doi.org/10.1016/j.chest.2026.06.074 |
| **Pragmatic RCT 在 ICU**（Blot, Crit Care） | 多數大型 ICU 試驗本質偏 pragmatic；族群異質、對比不足使「看不到差異」 | https://pubmed.ncbi.nlm.nih.gov/42587308/ |

> **啟示**：解讀 ICU 大型「中性」試驗時，需考量 pragmatic 設計本身對「無差異」的貢獻，避免直接等同「介入無效」

---

<!-- _class: divider -->

# 綜合啟示

---

<!-- _class: small-text -->

# 本期臨床帶回訊息 (Take-Home)

- **Sepsis 復甦**：到院前包裹式 bundle 失敗（negative）；vasopressin 較早加入或有利（觀察性）；抗生素急迫性以 **NEWS2 ≥7** 分層比單看休克更好
- **腎臟替代**：CRRT 決策核心是**體液平衡**而非 NUF 率；RRT 整體有害但重度腎障礙指標者可能獲益 → 個體化
- **呼吸**：AHRF 佔 ICU 一半、死亡率高；脫離用 3S 架構 + 橫膈超音波（輔助）；遠距醫療落實 SBT
- **長期結局**：肌肉流失以降解為主；老年 sepsis 存活者長期衰弱與**類固醇**相關；ICU 後精神藥物近半無診斷支持

> 所有數據請以原文為準；neutral/negative trial 勿誤讀為 positive

---

<!-- _class: ref -->

# 參考文獻 (1/2)

1. Baptistella AR, et al. 3S Framework for Ventilator Liberation. *Chest* 2026. https://doi.org/10.1016/j.chest.2026.08.001 (PMID 42580515)
2. Zhou X, et al. Diaphragmatic ultrasound for weaning in AECOPD: meta-analysis. *Crit Care* 2026;30(1). https://doi.org/10.1186/s13054-026-06240-1 (PMID 42576250)
3. Adam MF, et al. ICU telemedicine and weaning: ERIC secondary analysis. *Crit Care* 2026;30(1). https://doi.org/10.1186/s13054-026-06234-z (PMID 42568095)
4. Daoud T, Villar J, Annane D. Corticosteroids in ARDS. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08567-3 (PMID 42593538)
5. von Düring S, et al. Epidemiology of AHRF: registry cohort. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007284 (PMID 42584185)
6. Jouffroy R, Annane D, et al. 1-Hour prehospital bundle in septic shock (cluster RCT). *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007283 (PMID 42573415)
7. Nakashima T, et al. Ultra-early vs early vasopressin: target trial emulation. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08575-3 (PMID 42578996)
8. Rhee C, Singer M, et al. NEWS2 vs shock for antibiotic urgency. *Lancet Respir Med* 2026. https://doi.org/10.1016/S2213-2600(26)00187-6 (PMID 42556377)
9. Martín-Rodríguez F. NEWS2 and timing of antibiotics (comment). *Lancet Respir Med* 2026. https://doi.org/10.1016/S2213-2600(26)00202-X (PMID 42556378)

---

<!-- _class: ref -->

# 參考文獻 (2/2)

10. Monai NC, et al. Net ultrafiltration rate and mortality in CRRT. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007289 (PMID 42584203)
11. Nakamura S, et al. Heterogeneous treatment effects of RRT (Japanese registry). *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007282 (PMID 42573413)
12. Kreutz J, et al. EM critical care training and OHCA outcomes. *Resuscitation* 2026. https://doi.org/10.1016/j.resuscitation.2026.111264 (PMID 42600766)
13. Choi KH, et al. Geographic access and mortality in cardiogenic shock. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007287 (PMID 42565652)
14. González-Seguel F, et al. Muscle wasting in critical illness: meta-analysis. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007288 (PMID 42565658)
15. Yamamoto R, et al. Postintensive care frailty in older septic shock. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007304 (PMID 42584186)
16. Wu TT, et al. Psychoactive medication prescribing after critical illness. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007310 (PMID 42593167)
17. Martin-Loeches I, et al. Decades of ICM trials. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08579-z (PMID 42593537)
18. Suissa S, et al. Beta-blockers in COPD and CVD. *Chest* 2026. https://doi.org/10.1016/j.chest.2026.06.074 (PMID 42580516)
19. Blot S, et al. What place for pragmatic RCTs in intensive care? *Crit Care* 2026. https://pubmed.ncbi.nlm.nih.gov/42587308/ (PMID 42587308)

---

<!-- _class: lead -->

# 謝謝聆聽

## Critical Care 雙週期刊回顧 2026-08-15

**謝慕揚 MD, PhD, FESC**

讀書會內部共筆｜僅供醫療專業人員教學討論參考

資料來源：PubMed
