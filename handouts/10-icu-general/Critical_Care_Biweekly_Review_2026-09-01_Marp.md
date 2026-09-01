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
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-09-01'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧

## 2026-08-18 ～ 2026-09-01（過去 14 天）

**整理：謝慕揚 MD, PhD, FESC**

涵蓋：ICM · Critical Care · CCM · Chest · Lancet Respir Med · AJRCCM · Resuscitation · Shock

---

<!-- _class: abbr -->

# 縮寫對照 (1/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| RCT | Randomized Controlled Trial | 隨機對照試驗 |
| SR / MA | Systematic Review / Meta-Analysis | 系統性回顧 / 統合分析 |
| NMA | Network Meta-Analysis | 網絡統合分析 |
| OR / RR / HR | Odds / Relative Risk / Hazard Ratio | 勝算比 / 相對風險 / 風險比 |
| CI | Confidence Interval | 信賴區間 |
| AUC | Area Under the Curve | 曲線下面積 |
| ICU / ED | Intensive Care Unit / Emergency Department | 加護病房 / 急診 |
| RBC / Hb | Red Blood Cell / Hemoglobin | 紅血球 / 血紅素 |
| allo-HSCT | Allogeneic Hematopoietic Stem-Cell Transplantation | 異體造血幹細胞移植 |
| ECMO | Extracorporeal Membrane Oxygenation | 體外膜氧合 |
| VV / VA | Venovenous / Venoarterial (ECMO) | 靜脈-靜脈 / 靜脈-動脈 |
| ECPR | Extracorporeal Cardiopulmonary Resuscitation | 體外心肺復甦 |
| IABP | Intra-Aortic Balloon Pump | 主動脈內氣球幫浦 |

---

<!-- _class: abbr -->

# 縮寫對照 (2/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| RAP | Right Atrial Pressure | 右心房壓 |
| VExUS | Venous Excess Ultrasound Score | 靜脈鬱血超音波分數 |
| PH | Pulmonary Hypertension | 肺高壓 |
| ARDS | Acute Respiratory Distress Syndrome | 急性呼吸窘迫症候群 |
| ABI | Acute Brain Injury | 急性腦損傷 |
| V_T / ΔP / PEEP | Tidal Volume / Driving Pressure / Positive End-Expiratory Pressure | 潮氣容積 / 驅動壓 / 呼氣末正壓 |
| SBT / HFO | Spontaneous Breathing Trial / High-Flow Oxygen | 自主呼吸試驗 / 高流量氧療 |
| VAP / vHAP | Ventilator- / Ventilated Hospital-Acquired Pneumonia | 呼吸器 / 需機械通氣院內肺炎 |
| FAPP / AMT | FilmArray Pneumonia Panel / Antimicrobial Therapy | 多重 PCR 肺炎套組 / 抗微生物治療 |
| OHCA / NSE | Out-of-Hospital Cardiac Arrest / Neuron-Specific Enolase | 院外心臟驟停 / 神經元烯醇化酶 |
| cStO₂ / NIRS | Cerebral Tissue Oxygen Saturation / Near-Infrared Spectroscopy | 腦組織氧飽和 / 近紅外光譜 |
| AKI / FSS-ICU | Acute Kidney Injury / Functional Status Score-ICU | 急性腎損傷 / ICU 功能評分 |

---

<!-- _class: small-text -->

# 重點摘要 Key Pearls (1/2)

- **TRANSPORT**：癌症敗血性休克 liberal（Hb 9）vs restrictive（Hb 7）輸血，12h 乳酸下降 **52% vs 50%（p=0.82）無差異**；因安全性提早中止；liberal 血栓 13% vs 1%（p=0.001）。
- **EVER**：結構化早期活動，主要終點 FSS-ICU **23.6 vs 22.2（p=0.44）無差異**；12 個月亦無差異；達 Step≥4 者較佳。
- **Multiplex PCR（FAPP）VAP**：24h 標靶抗生素 35.1% vs 23.6%（**p=0.13 未達顯著**），僅培養確診者顯著。
- **插管誘導劑 NMA**：ketamine 血流動力學不穩多於 etomidate（RR 1.31）；etomidate 有腎上腺抑制；ketamine-propofol 可能最穩（證據弱）。
- **VA-ECMO + LV unloading**：60 天死亡無差異（p=0.84），併發症更多。

---

<!-- _class: small-text -->

# 重點摘要 Key Pearls (2/2)

- **ECMO 長期死亡（1 年）**：VV 37% · VA 55% · ECPR 74%；功能預後資料嚴重不足。
- **VExUS**：對右心導管 RAP 驗證，判別 RAP>12 mmHg 的 **AUC 0.97**。
- **ABI 通氣**：呼吸系統彈性（elastance）調節 V_T／呼吸速率對預後的影響 — 要同時看 ΔP。
- **ASSESS-SHOCK**：cStO₂ 與譫妄無關，但偏低與 90 天死亡相關（p<0.001）。
- **AKI = 全身性症候群**：與肺腦心肝及免疫遠端交互作用；試驗終點需納入遠端器官。

---

<!-- _class: divider -->

# 1. Sepsis 與敗血性休克

---

# TRANSPORT：癌症敗血性休克輸血策略 RCT

## Intensive Care Med 2026 · https://doi.org/10.1007/s00134-026-08582-4 · PMID 42616082

- 法國 18 中心 superiority RCT；癌症 + septic shock + lactate>2.0 + Hb<9.0 g/dL
- liberal（Hb 9.0）vs restrictive（Hb 7.0）RBC 輸血，前 48h
- **原計畫 260 人 → 因安全性提早中止，最終 187 人**

| 終點 | Liberal | Restrictive | 統計 |
|------|---------|-------------|------|
| 12h 乳酸下降（主要） | 52% | 50% | OR 1.07；p=0.82 |
| 動/靜脈血栓 | 13% | 1% | p=0.001 |
| 28 天死亡 | 46% | 53% | p=0.34 |

> 中性主要終點 + 血栓警訊 → 不支持常規 liberal 輸血；restrictive（Hb 7）仍為合理預設。

---

# Sepsis 焦點：兩則

## Chest 2026 · https://doi.org/10.1016/j.chest.2026.06.075 · PMID 42665126 ｜ ICM 2026 · https://doi.org/10.1007/s00134-026-08574-4 · PMID 42645558

- **allo-HSCT 後敗血性休克（Chest）**：多中心 ICU 世代，1,164 位受贈者中 **38% 因 septic shock 入 ICU**；預後差，需早期辨識與治療目標討論。
- **危重病 β-blockade（ICM state-of-the-art）**：過度持續交感刺激有害（心律不整、心肌損傷、免疫/代謝失調）；現有證據異質，**尚不支持常規使用**，僅特定情境個別化考量。

---

<!-- _class: divider -->

# 2. 機械通氣、肺炎與呼吸支持

---

# Multiplex PCR（FAPP）用於 VAP / vHAP — RCT

## Intensive Care Med 2026 · https://doi.org/10.1007/s00134-026-08591-3 · PMID 42622675

- 多中心 open-label RCT；免疫正常成人，suspected VAP/vHAP
- FilmArray Pneumonia Panel (FAPP) + 常規微生物 vs 常規微生物
- 主要終點：24h 內 targeted AMT 比例；n=146

| 族群 | 介入 | 對照 | 統計 |
|------|------|------|------|
| 全體（主要） | 35.1% | 23.6% | 差 11.5%；95% CI −0.03~26.2；p=0.13 |
| 培養確診肺炎 | 55.3% | 31.0% | 差 24.2%；p=0.048 |

> 整體 negative；效益集中於培養陽性者。單靠 PCR 陽性不宜過度縮窄或啟動抗生素。

---

# 危重病插管誘導劑 — NMA

## Chest 2026 · https://doi.org/10.1016/j.chest.2026.07.5239 · PMID 42612901

- 21 RCT、6,031 人 network meta-analysis

| 比較（vs etomidate） | 效應 | 確定性 |
|------|------|--------|
| ketamine：插管中血流動力學不穩 | RR 1.31（1.15–1.48） | moderate |
| ketamine-propofol：血流動力學不穩 | RR 0.44（0.27–0.72） | low |
| ketamine：插管後升壓劑啟動 | RR 0.80（0.50–1.28） | low |
| etomidate | ↑ 腎上腺抑制（adrenal suppression） | — |

> etomidate 血流較穩但有腎上腺抑制與後續升壓劑代價；ketamine-propofol 具潛力惟證據有限。

---

# ABI 通氣 + SBT 生理

## VENTIBRAIN 事後分析 ICM 2026 https://doi.org/10.1007/s00134-026-08562-8 (PMID 42618770) ｜ Crit Care 2026 https://doi.org/10.1186/s13054-026-06266-5 (PMID 42618951)

- **急性腦損傷（ABI）通氣（VENTIBRAIN, n=1,158）**：相同 V_T 下高彈性肺 ΔP 更高（各三分位 ΔP 中位 5/9/12 cmH₂O）；**V_T、呼吸速率對預後的影響受呼吸系統彈性調節** → 要同時看 driving pressure。
- **SBT：經氣管內管 HFO vs T-piece（隨機交叉, n=20）**：HFO-6.9mm@60L/min 產生 PEEP ~6 cmH₂O、減少肺容積流失、降低動態跨肺 ΔP、改善氧合；為生理上獨特之 SBT 策略，臨床預後待驗證。

---

# 焦點回顧：ARDS（三篇 ICM 綜述）

## ICM 2026 · PMID 42658259 / 42645559 / 42611192

- **ARDS + 急性腦損傷**：肺保護與腦生理保護目標可能衝突（如 permissive hypercapnia vs 顱內壓），須權衡個別化。（https://doi.org/10.1007/s00134-026-08595-z）
- **創傷 ARDS**：以 multi-hit 模型理解；嚴重胸部創傷者發生率高。（https://doi.org/10.1007/s00134-026-08581-5）
- **超越指引的個別化 ARDS**：肺保護為基石，但需回答起始設定、ΔP 未達標、recruitability 與 PEEP 設定等床邊實務。（https://doi.org/10.1007/s00134-026-08563-7）

---

<!-- _class: divider -->

# 3. ECMO、循環與血流動力學

---

# VA-ECMO + 左心室減壓（LV unloading）

## Crit Care 2026 · https://doi.org/10.1186/s13054-026-06213-4 · PMID 42661221

- 2 中心回溯、target trial emulation + propensity overlap weighting，n=264
- refractory cardiogenic shock 需 VA-ECMO ≥48h；unloading = Impella 或 IABP（24h 內）
- **主要終點 60 天死亡：加權風險差 1.4%（95% CI −11.8~14.6；p=0.84）無差異**
- ECMO 脫離率無差異；**器材相關併發症在 unloading 組較多**

> 假說產生性資料，不支持常規 LV unloading；需 phenotype 導向精選病人。

---

# ECMO 後長期死亡與功能預後 — SR/MA

## Crit Care Med 2026 · https://doi.org/10.1097/CCM.0000000000007318 · PMID 42671261

- 163 研究、78,053 成人

| 模式 | 1 年死亡率（95% CI） |
|------|---------------------|
| VV-ECMO | 37.2%（30.0–45.1） |
| VA-ECMO | 55.2%（50.2–60.1） |
| ECPR | 74.4%（71.4–77.2） |

- 僅 23% 研究報告功能預後（工具異質，多用 CPC）

> 長期死亡率依模式差異巨大；功能恢復資料嚴重不足，需標準化報告以利病人選擇與溝通。

---

# VExUS 分數侵入性驗證（對 RAP）

## Chest 2026 · https://doi.org/10.1016/j.chest.2026.08.031 · PMID 42668061

- 義大利 7 中心；VExUS 與右心導管 RAP 1 小時內對照；n=187（含 145 pre-capillary PH）

| VExUS grade | 0 | 1 | 2 | 3 |
|-------------|---|---|---|---|
| 平均 RAP (mmHg) | 3.9 | 8.4 | 13.5 | 15.8 |

- 判別 RAP >12 mmHg：**AUC 0.97（95% CI 0.94–0.99）**，優於單一超音波指標

> VExUS 對右心房壓/體循環鬱血具良好效度（本族群為 PH，ICU 外推仍需個別判斷）。

---

<!-- _class: divider -->

# 4. AKI、營養與代謝

---

# AKI 是全身性症候群 ｜ 蛋白質的統計陷阱

## Crit Care 2026 https://doi.org/10.1186/s13054-026-06252-x (PMID 42632888) ｜ https://doi.org/10.1186/s13054-026-06273-6 (PMID 42642764)

- **AKI = systemic syndrome**：ICU 近半數發生；經發炎與代謝物累積與肺、腦、心、肝、免疫遠端交互作用；未來試驗終點需超越 MAKE、納入遠端器官與替代終點。
- **蛋白質補充的證據分歧**：舊觀察性研究稱高蛋白降低死亡，但 EFFORT Protein(2023)、PRECISe(2024)、TARGET Protein(2025) 三大 RCT **均無益處**；差異源自 immortal time bias、confounding by indication、collider bias 等 → 急性期勿盲目追高蛋白。

---

<!-- _class: divider -->

# 5. 神經重症與心臟驟停後

---

# ASSESS-SHOCK：cStO₂（NIRS）與譫妄、死亡

## Shock 2026 · https://doi.org/10.1097/SHK.0000000000002925 · PMID 42627201

- 前瞻多中心觀察（NCT03814564），circulatory shock，n=256；INVOS™ NIRS 連續 48h
- delirium 發生率 34%（day 1–7）

| 結果 | 有 vs 無譫妄 / 存活 | 統計 |
|------|--------------------|------|
| 48h 平均 cStO₂（譫妄） | 61.6% vs 63.1% | p=0.72（無關） |
| 48h 平均 cStO₂（死亡） | 非存活 60.0% vs 存活 63.9% | p<0.001 |

> cStO₂ 不是譫妄預測工具，但持續偏低標記整體不良預後（含死亡）。

---

# OHCA：NSE 與神經預後（含焦點兩則）

## Resuscitation 2026 · PMID 42442598 / 42492621 / 42486429

- **NSE 與預後「不一致」者（n=646）**：peak NSE ≥60 μg/L 對不良神經預後特異度 98.5%；但正常 NSE 仍預後不良者（26%）與年齡、non-shockable、非心因、乳酸相關 → 需多模態整合。（https://doi.org/10.1016/j.resuscitation.2026.111205）
- **胸外按壓位置（US, n=152）**：指引位置多落在 LVOT 上方而非理想最大按壓區（較外側），提示生理位置錯配。（https://doi.org/10.1016/j.resuscitation.2026.111220）
- **極端氣溫與 OHCA（31 研究 SR）**：U/J 型關係，冷暴露佔比高且預後差。（https://doi.org/10.1016/j.resuscitation.2026.111221）

---

<!-- _class: divider -->

# 6. ICU 一般照護、復健與長期預後

---

# EVER：早期活動 RCT（12 個月）

## Intensive Care Med 2026 · https://doi.org/10.1007/s00134-026-08598-w · PMID 42645557

- 韓國 5 中心 open-label RCT，n=169；六步驟結構化 early mobilization vs usual care
- **主要終點 FSS-ICU（ICU 出院）：23.6 vs 22.2（p=0.44）無差異**
- 介入組更早（30 vs 46h）、次數多（11 vs 4）、時間長（330 vs 120 min）
- 達 Step≥4（坐到站）者 FSS-ICU 較高（30.6 vs 23.3；p<0.01）
- 12 個月 EQ-5D、SF-36、IES-R、MoCA、PICS 兩組皆改善、無差異

> 協議化早期活動未改善功能預後；「達到較高活動階梯（劑量/強度）」可能才是關鍵。

---

# 其他焦點（Honorable Mentions）

## Crit Care Med / Crit Care 2026

| 主題 | 重點 | 連結 |
|------|------|------|
| Microbiome in critical illness（CCM, PMID 42644690） | 危重病 microbiome 失衡、治療影響與恢復策略框架 | https://doi.org/10.1097/CCM.0000000000007327 |
| ICU 房間特性與預後（CCM, PMID 42611642） | 單/多人房、可視度與死亡無關；單人房 LOS 稍長 | https://doi.org/10.1097/CCM.0000000000007305 |
| ICU 譫妄心理社會因應（Crit Care, PMID 42629591） | 病人與家屬的 coping 策略；支持以家庭為中心介入 | https://doi.org/10.1186/s13054-026-06232-1 |

---

<!-- _class: ref -->

# 參考文獻 (1/2)

1. Pène F, et al. TRANSPORT RCT: early RBC transfusion in septic shock with cancer. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08582-4 (PMID 42616082)
2. Septic shock after allo-HSCT: multicenter ICU cohort. *Chest* 2026. https://doi.org/10.1016/j.chest.2026.06.075 (PMID 42665126)
3. β-blockade in critical illness (state-of-the-art). *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08574-4 (PMID 42645558)
4. Millot G, et al. Multiplex PCR (FAPP) for VAP/vHAP RCT. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08591-3 (PMID 42622675)
5. Respiratory mechanics & ventilator settings in ABI (VENTIBRAIN). *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08562-8 (PMID 42618770)
6. McDougall G, et al. Induction agents for intubation: NMA. *Chest* 2026. https://doi.org/10.1016/j.chest.2026.07.5239 (PMID 42612901)
7. Xu SS, et al. HFO via ETT vs T-piece during SBT (crossover). *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06266-5 (PMID 42618951)
8. ARDS in acute brain injury (review). *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08595-z (PMID 42658259)
9. ARDS management in trauma (review). *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08581-5 (PMID 42645559)
10. ARDS beyond the guidelines (review). *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08563-7 (PMID 42611192)
11. Dettling A, et al. LV unloading during VA-ECMO. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06213-4 (PMID 42661221)

---

<!-- _class: ref -->

# 參考文獻 (2/2)

12. Stebbins KT, et al. Long-term mortality/functional outcomes after ECMO: SR/MA. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007318 (PMID 42671261)
13. D'Alto M, et al. VExUS invasive validation in PH. *Chest* 2026. https://doi.org/10.1016/j.chest.2026.08.031 (PMID 42668061)
14. Manca B, et al. AKI as a systemic syndrome. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06252-x (PMID 42632888)
15. Neuberger M, Hartl WH. Protein in critical illness: statistical shortcomings. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06273-6 (PMID 42642764)
16. Heliste M, et al. ASSESS-SHOCK: cStO₂ & delirium/mortality. *Shock* 2026. https://doi.org/10.1097/SHK.0000000000002925 (PMID 42627201)
17. Lee DH, et al. Discordant NSE & neurologic outcomes in OHCA. *Resuscitation* 2026;226:111205. https://doi.org/10.1016/j.resuscitation.2026.111205 (PMID 42442598)
18. Martinez L, et al. US identification of ideal compression area. *Resuscitation* 2026;226:111220. https://doi.org/10.1016/j.resuscitation.2026.111220 (PMID 42492621)
19. Nunes AR, et al. Extreme temperatures & OHCA (SR). *Resuscitation* 2026;226:111221. https://doi.org/10.1016/j.resuscitation.2026.111221 (PMID 42486429)
20. Chung CR, et al. EVER: early mobilization RCT (12-month). *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08598-w (PMID 42645557)
21. Klingensmith NJ, et al. The Microbiome in Critical Illness. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007327 (PMID 42644690)
22. Lindner S, et al. ICU room characteristics & outcomes. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007305 (PMID 42611642)
23. Oh E, et al. Psychosocial coping with ICU delirium (MMSR). *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06232-1 (PMID 42629591)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

本文件為讀書會內部共筆，僅供醫療專業人員教學討論參考
