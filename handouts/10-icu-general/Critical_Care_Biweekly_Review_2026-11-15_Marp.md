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
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-11-15'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧

## 2026-11-01 ～ 2026-11-15

**謝慕揚 MD, PhD, FESC** | 2026-11-15

涵蓋：ICM、Critical Care、CCM、AJRCCM、Resuscitation、Shock

---

<!-- _class: abbr -->

# 常用縮寫對照（一）

| 縮寫 | 全名 |
|------|------|
| RCT | Randomized Controlled Trial 隨機對照試驗 |
| OR / aOR | (Adjusted) Odds Ratio 校正勝算比 |
| HR / RR / aRR | Hazard Ratio / (Adjusted) Risk Ratio 風險比 |
| IRR | Incidence Rate Ratio 發生率比 |
| CI / CrI | Confidence / Credible Interval 信賴區間 |
| AUROC | Area Under the ROC Curve 曲線下面積 |
| GRADE | 證據等級評估系統 |
| TTR | Time in Target analgesic Range 在目標鎮痛範圍內時間 |
| ICER / QALY | Incremental Cost-Effectiveness Ratio / Quality-Adjusted Life Year |
| COS / ITE | Core Outcome Set / Individualized Treatment Effect |
| ICU / HDU / ED | Intensive Care / High-Dependency Unit / Emergency Department |
| SOFA / GCS / NEWS-2 | Organ Failure / Glasgow Coma Scale / National Early Warning Score 2 |

---

<!-- _class: abbr -->

# 常用縮寫對照（二）

| 縮寫 | 全名 |
|------|------|
| SSC / SEP-1 | Surviving Sepsis Campaign / Severe Sepsis Bundle |
| VAP / NLR | Ventilator-Associated Pneumonia / Neutrophil:Lymphocyte Ratio |
| ARDS / ARF | Acute Resp Distress Syndrome / Acute Resp Failure |
| IMV / HFNO | Invasive Mechanical Ventilation / High-Flow Nasal Oxygen |
| Paco₂ | Arterial CO₂ partial pressure 動脈二氧化碳分壓 |
| AKI / CKRT / RRT | Acute Kidney Injury / (Continuous) Kidney Replacement Therapy |
| aBW / ESPEN | Adjusted Body Weight / Euro Soc Clinical Nutrition & Metabolism |
| OHCA / ROSC / CPR | Out-of-Hospital Cardiac Arrest / Return of Spontaneous Circ / CPR |
| PEA / EtCO₂ | Pulseless Electrical Activity / End-Tidal CO₂ |
| ILCOR / CoSTR | Int'l Liaison Committee on Resuscitation / Consensus Science Treatment Rec |
| TTM / NOAF | Targeted Temperature Management / New-Onset Atrial Fibrillation |
| ECMO / ECPR / ELSO | Extracorporeal Membrane Oxygenation / Extracorporeal CPR / ELSO Registry |
| ABI / SOT / ETC | Acute Brain Injury / Solid Organ Transplant / Electron Transport Chain |

---

# 本期重點摘要 (Key Pearls, 1–5)

> **1. CO-ROAM**：Oliceridine 鎮痛**不劣於** remifentanil（TTR 96.0% vs 92.3%），呼吸抑制 0% vs 4.6%（p=0.015），成本更低。

> **2. ARDS**：Normocapnia（提高呼吸速率）vs mild hypercapnia，90 天死亡 **28.8% = 28.8%**（p=0.84）。

> **3. NEWS-1 TRIPS**：NEWS2 觸發 Hour-1 Bundle 可行，遵從率升；死亡率 9.2% vs 3.9%（**無顯著差異**，試點）。

> **4. Sepsis time zero**：抗生素延遲只在**低血壓**或 **lactate ≥4** 時與死亡相關（aRR 1.07 / 1.10）。

> **5. antiVAP**：創傷病人常規抗生素預防**無法減少**早發性 VAP（wOR 0.87，p=0.48）。

---

# 本期重點摘要 (Key Pearls, 6–10)

> **6. 2026 ILCOR CoSTR**：年度復甦共識發布，涵蓋 BLS/ALS/PLS/NLS/EIT/First Aid。

> **7. TTM/TTM2**：以機器學習找「誰該降溫」——**無可偵測異質益處**（33°C vs 正常體溫，死亡 49.4% vs 47.9%）。

> **8. 重症 NOAF**：發生率 10.6%，出院後血栓栓塞風險 **×1.94–2.01**，但抗凝僅 33–36%。

> **9. ECMO**：量能越大死亡越低；但分散到 **≥4 個 ICU** 執行反而較差（OR 1.18）。

> **10. 肥胖營養**：蛋白 **<0.45 g/kg 調整體重/天**與 ICU 死亡上升相關（hazard 1.41）。

---

<!-- _class: divider -->

# 1. Sepsis 與感染

---

# NEWS-1 TRIPS：NEWS2 觸發 Sepsis Hour-1 Bundle

## 試點 stepped-wedge RCT｜Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007447](https://doi.org/10.1097/CCM.0000000000007447)｜PMID 43018426

- 香港 4 家急診，NEWS-2 ≥5 觸發 SSC Hour-1 Bundle，n=200
- Lactate、血液培養、抗生素遵從率**顯著上升**；整體 bundle 遵從率僅 **56.1%**
- 30 天死亡率 **3.9%（標準）vs 9.2%（NEWS-1）**，絕對差 +5.3%（95% CI −1.6 ～ +12.1，**無差異**）
- 14 項進展指標除 bundle 遵從率外全達標

> **啟示**：可作客觀觸發工具、提升流程遵從；臨床效益未定，勿過度解讀死亡率方向（試點、樣本小）。

---

# Sepsis「Time Zero」：哪種器官失能對抗生素延遲最敏感？

## Rhee/Klompas｜Am J Respir Crit Care Med 2026｜[doi.org/10.1093/ajrccm/aamag610](https://doi.org/10.1093/ajrccm/aamag610)｜PMID 43016314

- 145 家美國醫院、1,849,729 人次疑似感染；IPW 校正時變混淆

| Time zero 定義 | 抗生素 1–3h vs 0–1h | 判讀 |
|------|:---:|------|
| 低血壓 | aRR **1.07** (1.03–1.10) | 延遲有害 |
| Lactate ≥4.0 | aRR **1.10** (1.05–1.15) | 延遲有害 |
| 其他器官失能（單獨/組合） | 不顯著 | 時窗較寬 |
| 急性呼吸衰竭（3–6h vs 0–3h） | aRR 1.11 (1.05–1.18) | 稍寬時窗 |

> **啟示**：抗生素緊迫度依生理嚴重度分層——休克/高 lactate 分秒必爭。

---

# 社區型 sepsis（無初始器官支持）：ICU/HDU 划算嗎？

## 日本 140 院世代｜Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007435](https://doi.org/10.1097/CCM.0000000000007435)｜PMID 43024934

- n=28,211（GW 18,349 / HDU 8,706 / ICU 1,156），overlap 傾向加權
- 整體 ICU/HDU **未**降死亡（HDU RR 0.99、ICU RR 1.06），整體不符成本效益
- **次族群有益**：HDU 且 SOFA ≥6（RR 0.86）或 GCS ≤12（RR 0.81）
- 成本效益：HDU 且 GCS ≤12（ICER 47,738 USD/QALY）、SOFA ≥6（55,319）

> **啟示**：疾病較重（高 SOFA、意識差）者升級 HDU 可兼具存活與成本效益。

---

# 出院後 NLR 預測 sepsis 存活者長期風險

## Ontario 人口世代｜Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007375](https://doi.org/10.1097/CCM.0000000000007375)｜PMID 43002070

- n=37,250 sepsis 存活者，出院 15–90 天門診 NLR（中位 2.7）
- 1 年再住院或死亡 47.6%；隨 NLR 四分位上升：34.2% → 41.5% → 50.3% → **64.4%**
- vs 最低四分位：adjusted HR **1.24 / 1.54 / 2.25**

> **啟示**：post-sepsis 門診一張 CBC 即可算 NLR 做長期風險分層；目前為關聯性。

---

<!-- _class: divider -->

# 2. 鎮痛、Mechanical Ventilation 與呼吸支持

---

# CO-ROAM：Oliceridine vs Remifentanil（機械通氣鎮痛）

## 非劣性 RCT｜Intensive Care Med 2026｜[doi.org/10.1007/s00134-026-08643-8](https://doi.org/10.1007/s00134-026-08643-8)｜PMID 43007421

- 中國 19 家 ICU、評估者盲性、n=304；主要終點 TTR，非劣性界值 −10%
- TTR **96.0% vs 92.3%**（絕對差 +3.7%，95% CI −0.3 ～ +5.7）→ **達非劣性**
- 輕-中度不良反應 IRR 0.72（p=0.049）
- 呼吸抑制 **0% vs 4.6%（p=0.015）**；拔管後 **0% vs 7.9%（p=0.005）**；成本較低
- IMV 時間、ICU 住院、28 天死亡**無差異**

> **啟示**：有呼吸抑制顧慮者，oliceridine 是合理替代；定位在安全性與成本，非改善硬終點。

---

# ARDS：Normocapnia 未優於 Mild Hypercapnia

## 目標試驗模擬（ARDSNet/PETAL）｜Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007434](https://doi.org/10.1097/CCM.0000000000007434)｜PMID 43012617

- 每組 292 人；Paco₂ 35–45（靠提高呼吸速率）vs 50–55 mmHg，4 天
- 呼吸速率 **33 vs 28 次/分（p<0.001）**；pH 皆 ≥7.33
- 90 天院內死亡 **28.8% vs 28.8%（log-rank p=0.842）**；高齡、肥胖次族群一致

> **啟示**：ARDS 下允許 mild hypercapnia 安全；不須為 normocapnia 而拉高呼吸速率（增加 mechanical power）。為模擬研究，解讀保守。

---

# 免疫低下病人 HFNO：整體無益，機器學習找受益者

## HIGH trial causal forest｜Intensive Care Med 2026｜[doi.org/10.1007/s00134-026-08635-8](https://doi.org/10.1007/s00134-026-08635-8)｜PMID 42970133

- 以 HIGH trial（n=776）衍生 causal forest，預測第 28 天 IMV
- 整體平均效果**不顯著**，但治療反應**異質性大**
- **最受益者**：較年長、實體器官移植、較少嗜中性球低下、低氧較重但非呼吸器官 SOFA 較低
- 觀察世代（n=818）排序表現保留、絕對校準較差

> **啟示**：免疫低下 ARF 不宜「全有或全無」看 HFNO；特定表型可能受益，需前瞻驗證。

---

# antiVAP：創傷病人抗生素預防早發性 VAP — 無益

## 法國 15 中心、IPTW｜Crit Care 2026｜[doi.org/10.1186/s13054-026-06408-9](https://doi.org/10.1186/s13054-026-06408-9)｜PMID 43026563

- n=1,321 重傷、機械通氣 ≥48h；746 人（56%）接受預防（>90% amox-clav）
- 早發性 VAP 32% vs 34%；IPTW 後 **weighted OR 0.87（95% CI 0.66–1.22；p=0.48）**
- 競爭風險 csHR 0.87（p=0.19）；晚發 VAP、肺外感染、通氣/住院、30 天死亡皆**無改善**

> **啟示**：重症創傷不應常規抗生素預防早發性 VAP；重點在非抗生素 bundle（床頭抬高、口腔照護、及早脫機）。

---

<!-- _class: divider -->

# 3. AKI / Renal / Nutrition

---

# CKRT 早期白蛋白變化預測長期腎衰竭與死亡

## 韓國 8 院 LINK-AKI｜Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007408](https://doi.org/10.1097/CCM.0000000000007408)｜PMID 43023826

- n=1,087 AKI 接受 CKRT 且存活 ≥90 天；依第 0/7 天白蛋白分 4 組
- 1 年複合終點（ESKD 或死亡）發生率 33.4%

| 白蛋白軌跡 | adjusted OR (95% CI) |
|------|:---:|
| 持續低白蛋白 | **2.64 (1.73–4.04)** |
| 已改善 | 2.27 (1.38–3.75) |
| 新發 | 1.68 (1.06–2.68) |

> **啟示**：追蹤第 7 天白蛋白軌跡；持續/新發低白蛋白者為高風險（關聯性，補白蛋白能否改善未證實）。

---

# 肥胖重症病人蛋白質：太低有害

## 國際盛行率調查｜Crit Care 2026｜[doi.org/10.1186/s13054-026-06449-0](https://doi.org/10.1186/s13054-026-06449-0)｜PMID 43021385

- 785 家 ICU、n=9,068（BMI ≥25），競爭風險；以調整體重 (aBW) 標準化
- 早期蛋白攝取與「活著出 ICU 的時間」**無關**
- **極低攝取（< 約 0.45 g/kg aBW/天）**與 ICU 死亡 hazard 上升；0 g/kg 時 **hazard 1.41（1.17–1.69）**
- 超過門檻後無進一步關聯

> **啟示**：以 aBW 計算蛋白需求，避免急性期掉到 ~0.45 g/kg aBW/天以下；但不必盲目衝高。

---

<!-- _class: divider -->

# 4. Resuscitation 與心臟驟停

---

# 2026 ILCOR CoSTR 年度共識

## Resuscitation 2026｜[doi.org/10.1016/j.resuscitation.2026.111328](https://doi.org/10.1016/j.resuscitation.2026.111328)｜PMID 42988037

- 國際復甦聯盟 (ILCOR) 年度科學與治療建議共識 (CoSTR)
- 涵蓋六大工作小組：**BLS、ALS、PLS、NLS、EIT、First Aid**
- 以 GRADE 評估證據確定性、提出共識治療建議、列優先研究缺口
- 多數屬 good practice statement；強建議與高確定性證據仍少

> **啟示**：各 ICU/急診與急救團隊對照 2026 CoSTR 檢視 BLS/ALS 流程、教育訓練與品質指標；逐項建議以原文為準。

---

# 降溫 vs 正常體溫：以機器學習找「誰該降溫」

## TTM/TTM2 次分析｜Crit Care 2026｜[doi.org/10.1186/s13054-026-06414-x](https://doi.org/10.1186/s13054-026-06414-x)｜PMID 42972430

- n=2,789 OHCA；causal forest + BART 依缺血負荷、到院神經學找異質效果
- 6 個月死亡 33°C vs 正常體溫（36.0–37.7°C）：**49.4% vs 47.9%**
- 個體化效果變異極小，**無可偵測異質性**（條件平均風險差 −1.2% ～ +2.1%，p=0.99）
- hypothermia 有益後驗機率僅 42–53%

> **啟示**：目標體溫管理重點在**預防發燒、維持正常體溫**；無證據依缺血負荷挑特定病人做 33°C。

---

# 初始非可電擊 OHCA：節律轉變的預後意義

## 韓國全國世代｜Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007449](https://doi.org/10.1097/CCM.0000000000007449)｜PMID 43018417

- 初始非可電擊節律，依 CPR 中變化分 A-A / A-P / P-A / P-P；IPTW 校正
- 良好神經預後（CPC 1–2）率：A-A 0.101% → A-P 0.231% → P-A 0.384% → **P-P 0.874%**
- vs A-A：A-P OR 2.28、P-A OR 3.80、P-P OR **8.70**

> **啟示**：asystole 轉 PEA 比持續 asystole 預後好；節律動態提供額外脈絡（整體良好預後率仍極低）。

---

# 以 ETCO₂ 動態「逐週期」預測 ROSC

## NTUH-HYCARD LSTM｜Resuscitation 2026｜[doi.org/10.1016/j.resuscitation.2026.111387](https://doi.org/10.1016/j.resuscitation.2026.111387)｜PMID 43020455

- 多中心（2016–2023），每 2 分鐘 EtCO₂ 序列輸入 LSTM，預測下一週期 ROSC
- 1,651 事件序列 / 1,480 病人；583 事件以 ROSC 結束
- **事件層級** AUROC **0.876**；**週期層級** AUROC 0.685 且**系統性高估** ROSC 機率

> **啟示**：ETCO₂「趨勢」比單一數值有資訊；AI 即時預測可行，但須 recalibration，尚不能單獨用於床邊決策。

---

<!-- _class: divider -->

# 5. Hemodynamics、ECMO 與 ICU 組織

---

# ECMO 醫院量能與跨 ICU 分散

## ELSO registry｜Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007442](https://doi.org/10.1097/CCM.0000000000007442)｜PMID 43018409

- n=115,849 成人 ECMO、495 家醫院（2012–2023），hierarchical 校正
- 較高年案例量（每 10 例 OR 0.98）與 ECMO 時數（每 1000h OR 0.99）→ 較低死亡
- **≥4 個 ICU 執行 ECMO 的醫院死亡高於單一 ICU 者（OR 1.18，1.06–1.31）**，推測病人較複雜、由總量抵銷

> **啟示**：ECMO 宜追求足夠案例量並適度集中於專責單位，而非廣泛分散；最佳中心設計待研究。

---

# 重症新發心房顫動 (NOAF)：出院後風險與抗凝缺口

## Bayesian 統合分析｜Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007412](https://doi.org/10.1097/CCM.0000000000007412)｜PMID 43018413

- 54 篇、367,896 人；一般 ICU/HDU 無 AF 病史而新發 AF
- NOAF 發生率 **10.6%**（CrI 8.6–12.9%）
- 出院後系統性血栓栓塞絕對風險 7.1%；vs 無 NOAF **RR 1.94–2.01**
- 抗凝使用率低：院內 32.9%、出院後 35.9%；23.9% 之後診斷 AF

> **啟示**：ICU 的 NOAF 非一過性，出院時應納入血栓栓塞風險評估與心律追蹤；抗凝需個別化權衡出血。

---

<!-- _class: divider -->

# 6. 神經重症、復健與機轉

---

# 急性腦損傷通氣試驗核心結果集 (COS)

## 國際 Delphi｜Intensive Care Med 2026｜[doi.org/10.1007/s00134-026-08659-0](https://doi.org/10.1007/s00134-026-08659-0)｜PMID 42986439

- 31 國多專業、4 輪 Delphi、GRADE 9 分制；54 結果達共識
- 最終 COS **13 個結果**、5 領域（呼吸功能、存活、併發症、功能狀態、生活品質）
- 階層式複合終點：ICU 存活 → 72h 內不再插管 → days alive without mechanical ventilation

> **啟示**：ABI 脫離呼吸器研究宜採此 13 項與階層式複合終點；臨床亦提示脫機須兼顧呼吸、存活與功能。

---

# Guanfacine 治療外科/創傷 ICU 譫妄（試點）

## 單中心雙盲 RCT｜Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007448](https://doi.org/10.1097/CCM.0000000000007448)｜PMID 43012620

- n=100 CAM-ICU 確診譫妄；每晚 guanfacine 2 mg vs 安慰劑，最多 14 天
- 可行性達標（adherence/retention/資料完整度 100%）
- delirium/coma-free days 未校正下較高（2 vs 1，p=0.02），**校正後不顯著**
- 住院/通氣天數無差異；無安全疑慮

> **啟示**：安全、初步訊號值得追，但**證據不足以常規使用**；待多中心確認。

---

# 重症早期骨骼肌粒線體動態（機轉）

## 連續肌肉切片｜Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007433](https://doi.org/10.1097/CCM.0000000000007433)｜PMID 43023821

- n=33 機械通氣、SOFA ≥9；ICU 第 5、15 天 vastus lateralis 切片 vs 健康對照
- 完整粒線體輪廓減少、受損增加（第 5、15 天皆顯著）
- Complex III/IV 活性持續下降（citrate synthase 正規化後仍降）

> **啟示**：重症肌肉流失有早期、持續的粒線體功能障礙；呼應及早復健、營養與未來粒線體標的介入（機轉研究，暫不改變處置）。

---

<!-- _class: divider -->

# 7. 其他值得關注 (Honorable Mentions)

---

# Honorable Mentions

- **ECPR 長期存活（Resuscitation，PMID 42971311｜[doi](https://doi.org/10.1016/j.resuscitation.2026.111379)）**：refractory VT/VF OHCA、兩中心、728 人；存活出院者 5 年存活 67.2%、CPC 1–2 >90%，年輕與出院返家者預後最佳。

- **Guytonian 靜脈回流圖譜（Crit Care Med，PMID 43024946｜[doi](https://doi.org/10.1097/CCM.0000000000007446)）**：重構 150 筆 septic shock 血行動力，識別四種循環表型；VRdP 與 cardiac output 強相關（β 1.03），CVP 與 CO 負相關。

- **VIMUD-ICU（ICM，letter）**：振動聲波音樂治療於術後 ICU 譫妄的探索性 RCT（輔助性非藥物介入，證據初步）。

- **ICU recovery 教育課程（ICM，Delphi）**：訂出 ICU 復原教育核心課程（早期活動、PICS、譫妄預防、ABCDEF bundle）。

---

<!-- _class: lead -->

# 本期提醒

**陰性 / 中性訊號，勿過度詮釋：**

- NEWS-1 TRIPS：死亡率方向不利但**不顯著**（可行性試點）
- ARDS normocapnia vs mild hypercapnia：**死亡率完全相同**
- antiVAP：抗生素預防**無效**
- TTM/TTM2 降溫異質性：**無可偵測次族群益處**

2026 ILCOR CoSTR 逐項建議請以原文全文為準。

---

<!-- _class: ref -->

# 參考文獻（一）

1. NEWS-1 TRIPS. NEWS2-Guided Sepsis Hour-1 Bundle Care. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007447) PMID 43018426.
2. Rhee C, Pak TR, Klompas M, et al. Optimizing Sepsis Time Zero Definitions. [*Am J Respir Crit Care Med*. 2026.](https://doi.org/10.1093/ajrccm/aamag610) PMID 43016314.
3. Care Intensity With Survival in Sepsis Without Initial Organ Support (Japan). [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007435) PMID 43024934.
4. Neutrophil:Lymphocyte Ratio After Sepsis and Long-Term Outcomes. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007375) PMID 43002070.
5. Lu S, et al. Oliceridine vs Remifentanil (CO-ROAM). [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08643-8) PMID 43007421.
6. Normocapnia vs Mild Hypercapnia in ARDS: Target Trial Emulation. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007434) PMID 43012617.
7. Maillard A, et al. Individualized Effects of HFNO in Immunocompromised. [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08635-8) PMID 42970133.
8. antiVAP: Antibiotic Prophylaxis & Early-Onset VAP in Trauma. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-06408-9) PMID 43026563.

---

<!-- _class: ref -->

# 參考文獻（二）

9. Early Albumin Changes & Outcomes in AKI on CKRT. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007408) PMID 43023826.
10. Protein Prescriptions Based on Adjusted Body Weight. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-06449-0) PMID 43021385.
11. 2026 ILCOR CoSTR Summary. [*Resuscitation*. 2026.](https://doi.org/10.1016/j.resuscitation.2026.111328) PMID 42988037.
12. Hypothermia vs Normothermia by Neurological Status (TTM/TTM2). [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-06414-x) PMID 42972430.
13. Rhythm Transitions in Nonshockable OHCA. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007449) PMID 43018417.
14. Cycle-to-Cycle ROSC Prediction Using EtCO₂. [*Resuscitation*. 2026.](https://doi.org/10.1016/j.resuscitation.2026.111387) PMID 43020455.
15. Long-Term Survival Following ECPR. [*Resuscitation*. 2026.](https://doi.org/10.1016/j.resuscitation.2026.111379) PMID 42971311.
16. Hospital ECMO Volume & Distribution Across ICUs (ELSO). [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007442) PMID 43018409.

---

<!-- _class: ref -->

# 參考文獻（三）

17. New-Onset Atrial Fibrillation in Critically Ill Patients. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007412) PMID 43018413.
18. A Guytonian Atlas of Venous Return in Septic Shock. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007446) PMID 43024946.
19. Fong N, et al. Core Outcome Set for Ventilation Trials in Acute Brain Injury. [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08659-0) PMID 42986439.
20. Guanfacine on Delirium in Surgical/Trauma ICU (Pilot RCT). [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007448) PMID 43012620.
21. Mitochondrial Structure & Function in Skeletal Muscle of Critically Ill. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007433) PMID 43023821.

---

<!-- _class: lead -->

# 謝謝聆聽

## Critical Care 雙週期刊回顧｜2026-11-15

**謝慕揚 MD, PhD, FESC**

讀書會共筆 · 僅供醫療專業人員教學討論參考
