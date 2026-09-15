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
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-09-15'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧

## 2026-09-01 ～ 2026-09-15（過去 14 天）

**整理：謝慕揚 MD, PhD, FESC**

涵蓋：ICM · Critical Care · CCM · Shock · Resuscitation · Lancet Respir Med · AJRCCM · Chest

---

<!-- _class: abbr -->

# 縮寫對照 (1/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| RCT | Randomized Controlled Trial | 隨機對照試驗 |
| RR | Risk Ratio | 風險比（相對危險） |
| OR / aOR | (Adjusted) Odds Ratio | （校正）勝算比 |
| HR | Hazard Ratio | 風險比 |
| CI | Confidence Interval | 信賴區間 |
| CrI | Credible Interval | 後驗信賴區間（Bayesian） |
| MICU | Mobile ICU | 移動式加護（院前） |
| ABX | Antibiotics | 抗生素 |
| MBP | Mean Blood Pressure | 平均血壓 |
| SOFA | Sequential Organ Failure Assessment | 連續器官衰竭評估 |
| HP-PMX | Polymyxin B Haemoadsorption | 多黏菌素 B 血液吸附 |
| EAA | Endotoxin Activity Assay | 內毒素活性測量 |
| ΔpH | Change in arterial pH | 動脈 pH 變化 |
| TEE / TELUS | Transesophageal Echocardiography / Lung Ultrasound | 經食道超音波（心／肺） |

---

<!-- _class: abbr -->

# 縮寫對照 (2/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| ARDS | Acute Respiratory Distress Syndrome | 急性呼吸窘迫症候群 |
| IMV / NIV | (Non-)Invasive Mechanical Ventilation | （非）侵襲性機械通氣 |
| ECCO₂R | Extracorporeal CO₂ Removal | 體外二氧化碳移除 |
| ECMO | Extracorporeal Membrane Oxygenation | 體外膜氧合 |
| AE-COPD | Acute Exacerbation of COPD | 慢性阻塞性肺病急性惡化 |
| WEAN SAFE | WorldwidE AssessmeNt of Separation From ventilatory assistancE | 全球脫離呼吸器評估世代 |
| WLST | Withdrawal/Withhold Life-Sustaining Therapy | 撤除／不予維生治療 |
| AKI / KDIGO | Acute Kidney Injury / Kidney Disease: Improving Global Outcomes | 急性腎損傷 / 腎臟病全球預後 |
| RRT / SQP / RRI | Renal Replacement Therapy / Semi-Quantitative Perfusion / Renal Resistive Index | 腎替代療法 / 半定量灌流 / 腎阻力指數 |
| OHCA / ROSC | Out-of-Hospital Cardiac Arrest / Return of Spontaneous Circulation | 院外心臟驟停 / 自發循環恢復 |
| CPRIC | CPR-Induced Consciousness | CPR 誘發意識 |
| FBAO | Foreign Body Airway Obstruction | 異物呼吸道阻塞 |
| PICS / PICS-F | Post-Intensive Care Syndrome (-Family) | 加護後症候群（家屬型） |
| HCPS / AT / DIC | Hantavirus Cardiopulmonary Syndrome / Antithrombin / Disseminated Intravascular Coagulation | 漢他心肺症候群 / 抗凝血酶 / 瀰漫性血管內凝血 |

---

<!-- _class: small-text -->

# 本期重點摘要 (Key Pearls) 1/2

1. **SAMU Save Sepsis**：院前 1 小時復甦 bundle **無法降低** septic shock 死亡率（RR 0.81，p=0.16，NEGATIVE）。
2. **Ketamine 輔助鎮靜 RCT**：省 opioid 但 95% CrI **跨越 0**（Bayesian 訊號、非確定療效）。
3. **WEAN SAFE**：脫離失敗者 ICU 死亡率 **78%**（成功脫離者僅 2%）；三種失敗表型。
4. **X-COPD**：ECCO₂R 促 COPD 早期拔管、縮短 IMV，但**提前中止 (n=18)**，僅假說生成。
5. **敗血症 ΔpH**：ED→ICU 期 pH 下滑為強力死亡預測（整體 HR 2.80；基準 pH 正常者 HR 4.43）。

---

<!-- _class: small-text -->

# 本期重點摘要 (Key Pearls) 2/2

6. **HP-PMX**：應「表型導向」（EAA 0.60-0.89 + SOFA 7-13 + 腹腔源 + 早期），非全面使用。
7. **CPRIC**：CPR 誘發意識與存活出院正相關（OR 2.71），是良好生理訊號、勿視為單純干擾。
8. **FBAO-OHCA**：存活出院僅 3.6%，>65 歲無一存活；Magill forceps／插管最有效。
9. **腎灌流表型 (SQP)**：持續高灌流→較少持續性 AKI（OR 0.56）；RRI 軌跡無鑑別力。
10. **ICU 後恢復**：79% 有能力開車、僅 45% 已恢復；PICS-F 影響 20-60% 家屬。

---

<!-- _class: divider -->

# 1. Sepsis 與血流動力學

---

# SAMU Save Sepsis：院前 1 小時復甦 bundle（NEGATIVE）

## Jouffroy R, et al. Crit Care Med 2026 — https://doi.org/10.1097/CCM.0000000000007283 (PMID 42573415)

- **設計**：法國多中心、open-label、cluster RCT（院前 MICU 為叢集）
- **介入**：1h bundle = 早期 ABX + ≤35 mL/kg 生理食鹽水 + norepinephrine + hydrocortisone
- **N=381**（398 收案）

| 終點 | Bundle | Usual care | 效果 |
|------|--------|-----------|------|
| **28 天死亡** | **22%** | **27%** | RR 0.81 (0.61-1.08)；**p=0.16** |
| ICU / 出院 / 90 天死亡 | — | — | 皆無差異 |

> **「更早」≠「更好」**：院前把 bundle 前移、與對照差異小；品質與到院整合更關鍵（同期社論 PMID 42725825）。

---

# HP-PMX：表型導向的多黏菌素 B 血液吸附

## Shock 2026（2015-2026 綜整）— https://doi.org/10.1097/SHK.0000000000002940 (PMID 42726100)

- **責任表型四要素**：EAA 0.60-0.89｜SOFA 7-13｜腹腔感染源｜早期啟動
- Tigris：90 天死亡絕對下降 **15.5% (95% CrI 3.6-27.1)**；posterior probability 99.4%
- 腹腔感染族群獲益最集中（Tanaka adjusted HR 0.485，p=0.031）
- **EAA 不可得時 → SOFA 7-13 作為臨床替代指標**（五步驟演算法）

> HP-PMX 不是萬用療法，而是「表型導向治療」的範例；仍待正式外部驗證。

---

# 敗血症早期動脈 pH 變化 (ΔpH) 預測死亡

## Shock 2026（多中心 cohort, n=3,512）— https://doi.org/10.1097/SHK.0000000000002932 (PMID 42704020)

- ΔpH = ED pH − 入 ICU 24h 內最低 pH；與 28 天死亡呈**非線性**（負向風險最高）

| 基準 pH | adjusted HR（低於閾值者） |
|---------|--------------------------|
| 整體 | **2.80 (2.13-3.69)** |
| Acidosis (<7.35) | 2.71 |
| **Normal (7.35-7.45)** | **4.43（最高）** |
| Alkalosis (>7.45) | 1.90 |

> ED→ICU 的 pH「動態下滑」比單一 pH 值更能揪出「看似穩定卻惡化」者。

---

# TELUS 併入復甦性 TEE 評估休克

## Crit Care Med 2026（rTEECoRe registry, 多中心）— https://doi.org/10.1097/CCM.0000000000007337 (PMID 42695753)

- 379 次休克 TEE，其中 96 次（25.3%）加做經食道肺超音波 (TELUS)
- **休克病因辨識率：86.5% vs 75.3%（OR 1.95，95% CI 1.02-3.72，p=0.04）**
- 處置改變較多但未顯著（78.1% vs 71.7%，p=0.22）；時間僅 +2.5 分鐘；併發症罕見

> 復甦性 TEE 加做 TELUS 可提高病因辨識、成本低；待標準化與 outcome 驗證。

---

<!-- _class: divider -->

# 2. Mechanical Ventilation 與呼吸支持

---

# WEAN SAFE 次分析：脫離失敗的表型與預後

## Caldecott R, et al. Intensive Care Med 2026 — https://doi.org/10.1007/s00134-026-08592-2 (PMID 42714473)

- N=5,664；77.6% 曾嘗試分離，其中 **15.1% 於 day 90 仍脫離失敗**
- Failed-Wean 者 IMV／ICU 停留最久，較多 reintubation 與 tracheostomy

| 族群 | ICU 死亡率 |
|------|-----------|
| **Failed-Wean** | **78%** |
| Successful-Wean | 2% |

- 三種失敗表型（A：單次+WLST｜B：單次無 WLST｜C：>1 次）；首次分離失敗與 WLST／死亡強相關

> 脫離失敗非單一實體；「首次分離嘗試失敗」是預後與 WLST 決策的關鍵節點。

---

# X-COPD：ECCO₂R 促 COPD 惡化早期拔管（提前中止）

## Karagiannidis C, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06300-6 (PMID 42693471)

- RCT 因贊助方財務中止：**實收 18 人（計畫 192）**
- 複合主要終點（day 60 死亡/重度失能）：0/8 vs 3/9；RR −33%（95% CI −65% to 6%，**p=0.21**）
- **IMV 時間顯著較短：7.1 vs 24.3 天（p=0.043）**；day 29 device-free days 17 vs 8（p=0.011）
- VAP 0 vs 3；1 例 ECCO₂R 嚴重出血

> 樣本極小 + 提前中止 → **僅假說生成**，不足以改變臨床；期待足夠檢力試驗。

---

# 低劑量 ketamine 輔助鎮痛鎮靜 — 雙盲 RCT

## Crit Care Med 2026（墨爾本 2 中心, n=120）— https://doi.org/10.1097/CCM.0000000000007341 (PMID 42704275)

- ketamine **0.15 mg/kg/hr** vs placebo（皆已用 opioid 輸注）
- 主要終點：每小時 opioid（fentanyl equivalent）
  - 中位數 **64 vs 77 µg/hr**；median difference −13.0（**95% CrI −26.6 to 2.4，含 0**）；probability of benefit 95.1%
- 譫妄、ventilator/ICU/hospital-free days、嚴重不良事件**無差異**

> **CrI 跨越 0** → Bayesian「可能有益」訊號，非確定療效；尚不足以作為常規 opioid-sparing 推薦。

---

# ARDS 之類固醇：情境依賴療法（Review）

## Daoud T, Villar J, Annane D. Intensive Care Med 2026 — https://doi.org/10.1007/s00134-026-08567-3 (PMID 42593538)

- 支持用於中-重度 ARDS，特別是 **COVID-19 ARDS 與嚴重社區型肺炎**（降死亡、縮短 IMV）
- **異質性**：hyperinflammatory 表型與 septic ARDS 較可能獲益；influenza-associated／non-septic 證據有限或矛盾
- 未來：biomarker + adaptive platform trial + 表型導向；肺標靶遞送、選擇性 GR modulator

> 類固醇非「用或不用」二分；應依病因、發炎表型、疾病階段與時機個別化。

---

<!-- _class: divider -->

# 3. AKI / Renal

---

# 重症 AKI 生物標記的證據地圖

## Kane-Gill SL, et al. Crit Care Med 2026 — https://doi.org/10.1097/CCM.0000000000007362 (PMID 42725835)

- 篩 6,805 筆、納入 **1,116 篇**（成人 78.6%，93.3% cohort design）
- 用途分佈：預測 AKI (944)｜預後 (647)｜診斷病因 (109)｜**enrichment (僅 6)**｜管理 (僅 12)
- **落差**：預測準確度證據豐富，但「改變處置」的 management／enrichment 試驗稀少

> AKI 生物標記「能預測」已有大量證據，但「能否改變處置」仍待管理型試驗補足。

---

# 早期腎灌流表型 (SQP) 與腎恢復

## Shock 2026（中國 6 ICU 前瞻, n=456, NCT05866250）— https://doi.org/10.1097/SHK.0000000000002936 (PMID 42704056)

- Doppler 半定量灌流 (SQP) 分兩表型：sustained-high (49.1%) vs sustained-low (50.9%)
- 高灌流表型：
  - 持續性 AKI 較少（adjusted OR **0.56**，95% CI 0.35-0.89）
  - 腎恢復較快、day 3/7 RRT 較少
- **RRI 軌跡無鑑別力**

> 床邊 Doppler 半定量腎灌流（非 RRI）或可補足 KDIGO，提供早期腎恢復生理資訊；待外部驗證。

---

<!-- _class: divider -->

# 4. 心臟驟停與復甦

---

# CPR 誘發意識 (CPRIC)：良好預後訊號

## Resuscitation 2026（Victoria VACAR 2008-2024, n=43,402）— https://doi.org/10.1016/j.resuscitation.2026.111287 (PMID 42697466)

- CPRIC 發生率 3.3%，逐年上升（IRR 1.083）
- 相關因子：年輕、cardiac aetiology、公共場所、目擊、可電擊心律、mechanical CPR
- **與存活出院獨立正相關：OR 2.71 (2.38-3.09)**；non-interfering 表型 OR 4.09

> CPRIC 反映較佳灌流生理；應辨識並妥善鎮靜／鎮痛，而非中斷高品質 CPR。

---

# 異物阻塞 (FBAO) 造成之 OHCA：存活極差

## Resuscitation 2026（Victoria VACAR 2020-2024, population-based）— https://doi.org/10.1016/j.resuscitation.2026.111309 (PMID 42735815)

- 29,684 OHCA 中 223（0.8%）因 FBAO；中位年齡 77 歲，住家 56%／長照 30%
- **有效技術**：Magill forceps 與插管各 **73%** 成功；laryngeal mask 常用（35%）少有效（7%）
- 移除異物 74%、ROSC 48%，**存活出院僅 3.6%**；**>65 歲（165 人）無一存活**

> 重點在旁觀者立即施救 + EMS 直接喉鏡/Magill forceps；並理性面對高齡病人無效醫療。

---

<!-- _class: divider -->

# 5. ICU 後恢復與 PICS

---

# PICS 與復健 + ICU 存活者「重新開車」

## ICM 2026 (PMID 42714474, https://doi.org/10.1007/s00134-026-08600-5) · CCM 2026 (PMID 42725819, https://doi.org/10.1097/CCM.0000000000007316)

- **PICS 敘事回顧**：ABCDEF bundle、早期 mobilisation、家屬照護；**PICS-family 影響 20-60% 家屬**
- **ICU 存活者駕駛世代（英國, n=40/33 完成評估）**：

| 指標 | 結果 |
|------|------|
| 評估為有能力駕駛 | **79%** |
| 實際已恢復駕駛（~3 個月） | **45%** |
| 自陳恢復駕駛（3/6/12 月） | 62% / 82% / 91% |

> ICU 後恢復（含開車此日常功能）應納入常規追蹤；多數駕駛障礙可經介入後恢復。

---

<!-- _class: divider -->

# 6. 其他值得關注

---

<!-- _class: small-text -->

# 其他值得關注 (Honorable Mentions)

| 主題 | 重點 | 連結 |
|------|------|------|
| **流感住院/死亡風險因子** 兩篇 meta-analysis（支援 WHO 指引） | 量化風險因子與全球 case fatality 基準 | [DOI-1](https://doi.org/10.1016/S2213-2600(26)00195-5) · [DOI-2](https://doi.org/10.1016/S2213-2600(26)00200-6) |
| **Andes 病毒 HCPS**（智利全國, n=215） | 需 ECMO 占 49.3%；大流行期死亡上升 (aOR 2.73) | [DOI](https://doi.org/10.1007/s00134-026-08599-9) |
| **創傷早期 AT 耗損**（Shock, n=100） | 32% AT<80%；與 shock (OR 9.42)、DIC (OR 12.20)、內皮損傷相關 | [DOI](https://doi.org/10.1097/SHK.0000000000002935) |
| **重新開車路線圖**（CCM 社論） | ICU 後駕駛決策框架，搭配前瞻世代 | [DOI](https://doi.org/10.1097/CCM.0000000000007348) |

---

<!-- _class: ref -->

# 參考文獻 (1/2)

1. Jouffroy R, et al. A 1-Hour Resuscitation Bundle for Prehospital Management of Septic Shock. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007283 (PMID 42573415)
2. Peake SL, Delaney A. How Early Is Early? Prehospital Management of Septic Shock. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007346 (PMID 42725825)
3. Phenotype-guided polymyxin B haemoadsorption in abdominal septic shock. *Shock* 2026. https://doi.org/10.1097/SHK.0000000000002940 (PMID 42726100)
4. Early Arterial pH Changes as Strong Predictors of Mortality in Sepsis. *Shock* 2026. https://doi.org/10.1097/SHK.0000000000002932 (PMID 42704020)
5. TELUS as Adjunct to Resuscitative TEE in Evaluation of Shock. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007337 (PMID 42695753)
6. Caldecott R, et al. Distinct weaning phenotypes (WEAN SAFE secondary analysis). *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08592-2 (PMID 42714473)
7. Karagiannidis C, et al. ECCO₂R for AE-COPD requiring IMV (X-COPD trial). *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06300-6 (PMID 42693471)
8. Ketamine for Analgosedation in Mechanically Ventilated Adults: RCT. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007341 (PMID 42704275)
9. Daoud T, et al. Corticosteroids in ARDS. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08567-3 (PMID 42593538)
10. Kane-Gill SL, et al. Systematic Evidence Map of AKI Biomarkers. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007362 (PMID 42725835)

---

<!-- _class: ref -->

# 參考文獻 (2/2)

11. Early renal perfusion phenotypes and renal recovery. *Shock* 2026. https://doi.org/10.1097/SHK.0000000000002936 (PMID 42704056)
12. Trends in CPR-induced consciousness in OHCA. *Resuscitation* 2026. https://doi.org/10.1016/j.resuscitation.2026.111287 (PMID 42697466)
13. OHCA from Foreign Body Airway Obstruction (Victoria). *Resuscitation* 2026. https://doi.org/10.1016/j.resuscitation.2026.111309 (PMID 42735815)
14. Schaller SJ, et al. Rehabilitation and PICS across the recovery continuum. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08600-5 (PMID 42714474)
15. Apps C, et al. Comprehensive Driving Assessment After Critical Illness. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007316 (PMID 42725819)
16. Danesh V, Mikkelsen ME. Returning to Driving: A Roadmap. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007348 (PMID 42725840)
17. Risk factors for hospital admission/mortality in influenza (meta-analysis). *Lancet Respir Med* 2026. https://doi.org/10.1016/S2213-2600(26)00195-5 (PMID 42710513)
18. Global hospital admission & case fatality in influenza (meta-analysis). *Lancet Respir Med* 2026. https://doi.org/10.1016/S2213-2600(26)00200-6 (PMID 42710510)
19. Meza-Fuentes G, et al. Andes virus HCPS (national Chilean cohort). *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08599-9 (PMID 42684407)
20. Early antithrombin depletion after trauma. *Shock* 2026. https://doi.org/10.1097/SHK.0000000000002935 (PMID 42713784)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

本文件為讀書會內部共筆，僅供醫療專業人員教學討論參考
