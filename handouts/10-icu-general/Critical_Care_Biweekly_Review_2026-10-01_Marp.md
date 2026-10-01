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
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-10-01'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧

## 2026-09-17 ～ 2026-10-01（過去 14 天）

**整理：謝慕揚 MD, PhD, FESC**

涵蓋：ICM · Critical Care · Chest · Resuscitation · Shock · CCM

---

<!-- _class: abbr -->

# 縮寫對照 (1/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| RCT | Randomized Controlled Trial | 隨機對照試驗 |
| RR / HR / OR | Risk / Hazard / Odds Ratio | 風險比／風險比／勝算比 |
| CI | Confidence Interval | 信賴區間 |
| AUC | Area Under the Curve | 曲線下面積 |
| MOR | Median Odds Ratio | 中位勝算比（群集變異） |
| ICU | Intensive Care Unit | 加護病房 |
| EMS | Emergency Medical Service | 緊急醫療服務 |
| CMM | Comprehensive Medication Management | 完整藥物管理（藥師） |
| ARDS | Acute Respiratory Distress Syndrome | 急性呼吸窘迫症候群 |
| V_T / PBW | Tidal Volume / Predicted Body Weight | 潮氣容積／預測體重 |
| ΔP / E | Driving Pressure / Elastance | 驅動壓／呼吸系統彈性 |
| PEEP | Positive End-Expiratory Pressure | 吐氣末正壓 |
| VFD | Ventilator-Free Days | 無呼吸器天數 |
| sRAGE | Soluble Receptor for Advanced Glycation End-products | 肺泡上皮損傷標記 |

---

<!-- _class: abbr -->

# 縮寫對照 (2/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| PTP | Pressure-Time Product | 壓力–時間乘積 |
| P-SILI | Patient Self-Inflicted Lung Injury | 病人自發性肺損傷 |
| NEE | Norepinephrine Equivalent | 正腎上腺素等效劑量 |
| CRT | Capillary Refill Time | 微血管再充填時間 |
| AKI / eGFR / sCr | Acute Kidney Injury / est. GFR / serum Creatinine | 急性腎損傷／腎絲球過濾率／血清肌酸酐 |
| MAKE60 | Major Adverse Kidney Events to day 60 | 60 天重大腎臟不良事件 |
| ICP / nICP | (non-invasive) Intracranial Pressure | （非侵襲性）顱內壓 |
| OHCA / ROSC | Out-of-Hospital Cardiac Arrest / Return of Spontaneous Circulation | 院外心臟驟停／自發循環恢復 |
| CPR / RB-CPR / CO-CPR | (Rescue-Breathing / Compression-Only) CPR | 心肺復甦（含人工呼吸／僅壓胸） |
| TOR | Termination of Resuscitation | 終止復甦 |
| OMI / NST-OMI | (Non-ST-Elevation) Occlusive MI | （無 ST 上升之）阻塞性心梗 |
| PE / CTPA | Pulmonary Embolism / CT Pulmonary Angiography | 肺栓塞／電腦斷層肺動脈攝影 |
| ECMO / VV ECMO | (Venovenous) Extracorporeal Membrane Oxygenation | （靜脈–靜脈）體外膜氧合 |
| PJP / LDH | Pneumocystis jirovecii Pneumonia / Lactate Dehydrogenase | 肺囊蟲肺炎／乳酸脫氫酶 |

---

# 本期重點 (Key Pearls) — 1/2

- **Ilofotase alfa** 無法預防開心手術後 AKI（phase 2 RCT，NEGATIVE）
- **Sevoflurane 吸入鎮靜**在中-重度 ARDS 造成傷害（SESAR：90 天存活 47% vs 56%）
- 急性腦損傷通氣：用**呼吸系統彈性 (E)** 而非固定 V_T（VENTIBRAIN）
- **sRAGE** 可指引 ARDS 個人化肺復張（LIVE trial 次分析）
- **Ondansetron** 可降低 ARDS 病人呼吸驅動（概念驗證）

---

# 本期重點 (Key Pearls) — 2/2

- 難治型敗血性休克：加入**組織低灌流 (CRT + lactate)** 比單看升壓劑劑量更能分辨高風險
- 非心因性 OHCA：**人工呼吸 (RB-CPR)** 仍有益，尤其兒童／溺水／窒息
- **Post-ROSC ECG**：NST-OMI 常被漏做冠脈攝影、死亡率最高
- 重症**藥師每日完整藥物管理 (CMM)** 與較低院內死亡相關
- **適應性 D-dimer 閾值** rule-out PE 安全（失誤率 0.12%）

---

<!-- _class: divider -->

# 1. Sepsis 與血流動力學

---

# 難治型敗血性休克：組織低灌流改善風險分層

## ANDROMEDA-SHOCK-2 secondary analysis｜[DOI](https://doi.org/10.1007/s00134-026-08551-x)｜PMID 42467247

- 6h protocolised 復甦後評估難治性；n=1,363
- **雙低灌流條件** = NEE >0.5 µg/kg/min **且** CRT >3 秒 **且** lactate 未下降
- 雙低灌流者（3.9%）：28 天死亡 **73.6% vs 23.7%（aHR 4.68, 95% CI 3.31-6.64）**
- 預後富集優於單看升壓劑劑量（LR+ 8.12 vs 2.71）

> **啟示**：定義「難治型休克」不應只看升壓劑劑量；併入 CRT 與 lactate 動態能抓出死亡率逾 70% 的極高風險族群。

---

<!-- _class: divider -->

# 2. Mechanical Ventilation 與呼吸支持

---

# 揮發性吸入鎮靜在 ARDS：從期待到傷害

## ICM Review（含 SESAR 解讀）｜[DOI](https://doi.org/10.1007/s00134-026-08613-0)｜PMID 42803955

- SESAR RCT（JAMA 2025，n=687，中-重度 ARDS）：sevoflurane vs propofol
  - **day 28 VFD 較少（median difference −2.1 天）**
  - **90 天存活較低：47.1% vs 55.7%（HR 1.31, 95% CI 1.05-1.62）**
  - 7 天死亡較高（19.4% vs 13.5%，RR 1.44）

> **啟示**：ARDS 不建議於臨床試驗外常規使用揮發性吸入鎮靜；「生理上合理」≠「臨床有益」。

---

# 急性腦損傷通氣：用彈性 (E) 而非固定 V_T

## VENTIBRAIN post hoc｜[DOI](https://doi.org/10.1007/s00134-026-08562-8)｜PMID 42618770

- n=1,158；E = ΔP ÷（V_T/PBW）
- 高 V_T：**低 E 者降 ICU 死亡（OR 0.52）**；高 E 者無益（OR 1.16），交互作用 p<0.001
- 最適 V_T/PBW 隨 E 上升而下降：**11.4 → 4.4 mL/kg**；最適呼吸次數 15 → 19 次/分
- **ΔP 每增 1 cmH₂O ≈ 呼吸次數每增 3 次/分** 的預後衝擊

> **啟示**：腦損傷設定 V_T 應參考 E／ΔP 與維持 isocapnia 所需呼吸次數，而非盲目套用 6 mL/kg。

---

# sRAGE 指引 ARDS 個人化肺復張

## LIVE trial secondary analysis｜[DOI](https://doi.org/10.1016/j.chest.2026.08.054)｜PMID 42777910

- n=259；以血漿 sRAGE 2,440 pg/mL 分高/低
- 治療效果隨 baseline sRAGE 而異（p-for-interaction=0.006）：
  - **高 sRAGE**：肺復張降 90 天死亡（HR 0.41, 95% CI 0.18-0.93）
  - **低 sRAGE**：肺復張反而升死亡（HR 3.27, 95% CI 1.06-10.1）
- 發炎表型只具預後價值、不預測治療反應

> **啟示**：肺復張非「全有或全無」；高 sRAGE（偏瀰漫性）者或可獲益，低 sRAGE 者可能受害。

---

# Ondansetron 降低 ARDS 呼吸驅動

## Chest 概念驗證 crossover｜[DOI](https://doi.org/10.1016/j.chest.2026.09.086)｜PMID 42810428

- n=9（ARDS，pressure-support，通氣 >48h）；IV ondansetron 0.15 mg/kg
- 吸氣 PTP：108 → 85 cmH₂O·s/min（**mean difference −23, p<0.001**）
- 呼吸次數 −1.7、minute ventilation −1.0 L/min、E_di 峰值 −2.4 µV；V_T 不變
- PaCO₂ +3.2 mmHg；**PaO₂/FiO₂ 改善 +23（p=0.009）**

> **啟示**：血清素–5-HT₃ 途徑是調控過高呼吸驅動的新標的；樣本極小、須大型 RCT 驗證。

---

# 機械通氣期間的咳嗽功能（Review）

## Chest narrative review｜[DOI](https://doi.org/10.1016/j.chest.2026.09.023)｜PMID 42790625

- ICU 病人常因呼吸肌功能障礙 + 氣管內管阻礙聲門閉合而**咳嗽無效**
- 無效咳嗽是 **extubation failure 的獨立危險因子**，亦與 post-extubation pneumonia、ICU 停留延長相關
- 現行指引已列為脫離關鍵評估項，但臨床量測缺乏標準化

> **啟示**：脫離評估不應只看氧合與呼吸力學；客觀量化咳嗽能力（如 peak cough flow）有助辨識高拔管失敗風險者。

---

<!-- _class: divider -->

# 3. 神經重症 Neurocritical Care

---

# 顱內壓 (ICP)：生理、監測與個人化管理（Review）

## ICM Review｜[DOI](https://doi.org/10.1007/s00134-026-08558-4)｜PMID 42525086

- 挑戰傳統固定閾值（ICP >22 mmHg 統一階梯）：病人耐受度因人、因病因、因情境而異
- 新概念：**ICP burden、波形型態、cerebral autoregulation、功能性腦監測**
- nICP 在無法/禁忌侵襲性監測時互補；整合入 multimodal neuromonitoring
- 未來：AI 分析神經監測資料、預測繼發損傷

> **啟示**：ICP 管理從「單一閾值」轉向「生理導向、個人化」；判讀應結合波形、自我調節與 multimodal 監測。

---

<!-- _class: divider -->

# 4. AKI / Renal

---

# Ilofotase alfa 預防開心手術後 AKI（phase 2 RCT，NEGATIVE）

## ICM phase 2 RCT｜[DOI](https://doi.org/10.1007/s00134-026-08596-y)｜PMID 42766022

- 重組人類 alkaline phosphatase；術前 eGFR 25-65、複雜 on-pump 心臟手術
- 兩劑 IV 128 mg vs placebo；n=204 分析（109 vs 95）
- 主要終點 sCrRatio **1.21 vs 1.27（p=0.31）**
- **MAKE60 15.9% vs 15.4%（p=0.87）**；無安全疑慮

> **啟示**：目前沒有藥物能常規預防心臟手術後 AKI；仍以 KDIGO bundle 為核心。不應用於此適應症。

---

<!-- _class: divider -->

# 5. 心臟驟停與復甦 Resuscitation

---

# 非心因性 OHCA：人工呼吸 vs 僅壓胸

## 全日本 Utstein 世代｜[DOI](https://doi.org/10.1016/j.resuscitation.2026.111332)｜PMID 42790858

- n=154,137 非心因性 OHCA；RB-CPR 13.1% vs CO-CPR 86.9%
- 30 天死亡 **adjusted RR 0.98（95% CI 0.98-0.99）**；不良神經預後 RR 0.99
- 益處集中於**兒童、溺水、窒息**；成人/高齡無明顯差異

> **啟示**：一般（多心因性）OHCA 仍以 CO-CPR 為旁觀者首選；兒童／溺水／窒息等非心因性情境，加入人工呼吸可能額外有益。

---

# Post-ROSC ECG：NST-OMI 型態與預後

## Resuscitation 單中心｜[DOI](https://doi.org/10.1016/j.resuscitation.2026.111334)｜PMID 42790861

- n=214（CAG 確診 OMI 101）
- NST-OMI 以 **left-main equivalent、Smith-modified Sgarbossa（各 8%）** 最常見
- NST-OMI **較少接受 CAG（78% vs 98%）**；**未做 CAG 的 NST-OMI 30 天死亡 75%**
- **PR-segment 延長**獨立預測死亡（aOR 0.977, p=0.032）

> **啟示**：post-ROSC ECG 不應只看 ST 上升；熟悉 NST-OMI 型態避免漏掉需緊急冠脈介入者。

---

# EMS 機構間「救/不救、何時停」差異巨大

## ESO Data Collaborative｜[DOI](https://doi.org/10.1016/j.resuscitation.2026.111333)｜PMID 42790860

- n=560,240；不啟動復甦 13.7%；符合 Universal TOR rule 者 56.9% 執行 TOR
- 校正病人因素後仍有巨大機構間差異：
  - 不啟動復甦 **MOR 2.30**
  - **TOR MOR 4.13**（兩家隨機機構對相似病人之 TOR 勝算中位差距達 4 倍）

> **啟示**：院前決策差異非病人因素造成；需標準化流程與教育以提升一致性、公平性與品質。

---

<!-- _class: divider -->

# 6. 肺栓塞 Pulmonary Embolism

---

# 適應性 D-dimer 閾值排除 PE 的安全性

## 系統性回顧與統合分析｜[DOI](https://doi.org/10.1016/j.chest.2026.09.030)｜PMID 42790624

- 6 研究、12,194 人（PE 盛行率 7.0-19.2%）
- 以適應性策略排除 PE（未做 CTPA）：整體 3 個月診斷失誤率 **0.12%（I²=0%）**
- adaptive window 內失誤率 **0.50%**；可省 **60.8%** 的 CTPA

> **啟示**：年齡／臨床機率調整之 D-dimer 閾值安全可行，可減少不必要 CTPA、降低輻射與顯影劑暴露。

---

# 2026 AHA/ACC vs 2019 ESC 肺栓塞分類

## Chest 兩院區世代｜[DOI](https://doi.org/10.1016/j.chest.2026.09.028)｜PMID 42810427

- n=2,251；30 天死亡 5.6%
- 30 天死亡 AUC：**AHA/ACC 0.885 vs ESC 0.763（差 0.122, p<0.001）**
- AHA/ACC D-E 但 ESC 中風險的 37 人中，**75.7% 於 30 天死亡**
- 差異具「光譜依賴性」（去除 AHA/ACC 極端類別後縮小）

> **啟示**：AHA/ACC 全光譜分層能辨識被 ESC 低估的高風險族群；分流時值得參考其更細緻分層。

---

<!-- _class: divider -->

# 7. 其他值得關注 Honorable Mentions

---

# 其他值得關注 (1/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| 重症藥師與死亡 (Chest) | 任一天缺乏藥師 CMM → 院內死亡勝算 **+20%**（OR 1.20）；n=28,795 | [DOI](https://doi.org/10.1016/j.chest.2026.09.027) |
| 續用 ECMO 的倫理 (Chest) | 無復原/移植/裝置出路時可否單方撤除？批判四項倫理論據 | [DOI](https://doi.org/10.1016/j.chest.2026.09.022) |
| 非 HIV PJP 表型 (Chest) | LDH≥400 + 淋巴球<700 分型；F4 死亡 subdistribution HR **6.15** | [DOI](https://doi.org/10.1016/j.chest.2026.09.011) |

---

# 其他值得關注 (2/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| 數十年 ICM RCT 回顧 (ICM) | 持久進步常來自支持性照護最佳化與避免醫源性傷害 | [DOI](https://doi.org/10.1007/s00134-026-08579-z) |
| TPE 期間抗感染藥劑量 (Crit Care) | 低 Vd、高蛋白結合藥（aminoglycosides、glycopeptides）受影響最大 | [DOI](https://doi.org/10.1186/s13054-026-06306-0) |
| NLRP3 發炎體 (Crit Care) | 敗血症免疫調控雙面性；過度活化 vs 耗竭皆有害 | [DOI](https://doi.org/10.1186/s13054-026-06315-z) |
| VV ECMO 細胞激素圖譜 (Shock) | ECMO 前高 TNF-β、RANTES 與較低存活相關；n=35 | [DOI](https://doi.org/10.1097/SHK.0000000000002943) |

---

<!-- _class: ref -->

# 參考文獻 (1/2)

1. Kattan E, et al. Persistent tissue hypoperfusion in refractory septic shock: ANDROMEDA-SHOCK-2 secondary analysis. [*Intensive Care Med*. 2026;52(10):2058-70.](https://doi.org/10.1007/s00134-026-08551-x) PMID: 42467247.
2. The NLRP3 inflammasome in sepsis and critical illness: a narrative review. [*Crit Care*. 2026;30(1).](https://doi.org/10.1186/s13054-026-06315-z) PMID: 42778957.
3. Volatile anesthetic sedation in ARDS. [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08613-0) PMID: 42803955.
4. Grieco DL, et al. Respiratory mechanics modifies ventilator settings–outcome in acute brain injury (VENTIBRAIN). [*Intensive Care Med*. 2026;52(10):2071-84.](https://doi.org/10.1007/s00134-026-08562-8) PMID: 42618770.
5. Epithelial injury & inflammatory phenotypes for personalized ventilation in ARDS: LIVE trial secondary analysis. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.08.054) PMID: 42777910.
6. Effect of ondansetron on respiratory drive in ARDS. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.09.086) PMID: 42810428.
7. Cough function during mechanical ventilation. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.09.023) PMID: 42790625.
8. Taccone FS, et al. Intracranial pressure physiology, monitoring and individualized management. [*Intensive Care Med*. 2026;52(10):2108-28.](https://doi.org/10.1007/s00134-026-08558-4) PMID: 42525086.
9. Phase 2 RCT of ilofotase alfa for kidney injury after open heart surgery. [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08596-y) PMID: 42766022.
10. Iida Y, et al. Rescue-breathing vs compression-only bystander CPR in non-cardiac OHCA. [*Resuscitation*. 2026.](https://doi.org/10.1016/j.resuscitation.2026.111332) PMID: 42790858.

---

<!-- _class: ref -->

# 參考文獻 (2/2)

11. The post-ROSC ECG: NST-elevation occlusion morphology & prognosis. [*Resuscitation*. 2026.](https://doi.org/10.1016/j.resuscitation.2026.111334) PMID: 42790861.
12. EMS agency-level variation in non-initiation and termination of resuscitation in OHCA. [*Resuscitation*. 2026.](https://doi.org/10.1016/j.resuscitation.2026.111333) PMID: 42790860.
13. Safety of age-adjusted & clinical probability-adjusted D-dimer cut-offs in suspected PE: systematic review & meta-analysis. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.09.030) PMID: 42790624.
14. 2026 AHA/ACC vs 2019 ESC risk classification in hospitalized acute PE. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.09.028) PMID: 42810427.
15. Optimization of pharmacist medication management and mortality in the ICU. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.09.027) PMID: 42810430.
16. Continuing ECMO without potential recovery, transplant, or device. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.09.022) PMID: 42785423.
17. Biological phenotypes in non-HIV Pneumocystis jirovecii pneumonia. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.09.011) PMID: 42805328.
18. Martin-Loeches I, et al. Decades of intensive care medicine trials. [*Intensive Care Med*. 2026;52(10):2178-93.](https://doi.org/10.1007/s00134-026-08579-z) PMID: 42593537.
19. Dosing of anti-infective drugs during therapeutic plasma exchange: narrative review. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-06306-0) PMID: 42786518.
20. Hagiwara J, et al. Longitudinal cytokine profiling in venovenous ECMO. [*Shock*. 2026.](https://doi.org/10.1097/SHK.0000000000002943) PMID: 42752598.
21. Jabaudon M, et al. Inhaled sedation in ARDS: the SESAR RCT. [*JAMA*. 2025;333(17):1488-99.](https://doi.org/10.1001/jama.2025.3169) PMID: 40111326.

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

本回顧為讀書會內部共筆，僅供醫療專業人員教學討論參考
