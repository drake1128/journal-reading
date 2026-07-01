---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Microsoft JhengHei', 'PingFang TC', 'Noto Sans TC', sans-serif;
    background-color: #ffffff;
    color: #2d3436;
    font-size: 0.95em;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 2.0em; border-bottom: none; }
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
    font-size: 2.5em;
    text-align: center;
  }
  section.divider h2 { color: #dfe6e9; font-size: 1.1em; text-align: center; }
  section.divider h3 { color: #dfe6e9; font-size: 0.9em; text-align: center; }
  section.abbr table { font-size: 0.72em; width: 100%; }
  section.abbr th { background-color: #555555; color: white; padding: 5px 8px; }
  section.abbr td { padding: 3px 8px; }
  section.abbr tr:nth-child(even) { background-color: #f0f4f8; }
  section.abbr h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.4em; }
  section.ref { font-size: 0.62em; }
  section.ref h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.4em; }
  section.ref ol { padding-left: 1.2em; }
  section.ref li { margin-bottom: 0.3em; }
  section.small-text { font-size: 0.82em; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; font-size: 1.0em; }
  h3 { color: #555555; font-size: 0.9em; }
  table { font-size: 0.72em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.85em;
    color: #2d3436;
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
  ul li { margin-bottom: 0.25em; }
  ol li { margin-bottom: 0.25em; }
footer: '謝慕揚 MD, PhD, FESC | Critical Care 雙週期刊回顧 | 2026-07-01'
---

<!-- _class: lead -->
# Critical Care 雙週期刊回顧
## Biweekly Critical Care Literature Review
## 2026-06-17 ～ 2026-07-01

**整理：謝慕揚 MD, PhD, FESC**

ICM · Critical Care · CCM · AJRCCM · Chest · Resuscitation · Shock

---

<!-- _class: abbr -->
# 縮寫對照 (1/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| RCT | Randomized Controlled Trial | 隨機對照試驗 |
| RR / OR / HR | Risk Ratio / Odds Ratio / Hazard Ratio | 風險比 / 勝算比 / 風險比 |
| sHR | Subdistribution Hazard Ratio | 次分布風險比（競爭風險）|
| CI | Confidence Interval | 信賴區間 |
| AUROC | Area Under the ROC Curve | ROC 曲線下面積 |
| MAP | Mean Arterial Pressure | 平均動脈壓 |
| AKI | Acute Kidney Injury | 急性腎損傷 |
| KDIGO / KPS | Kidney Disease: Improving Global Outcomes / Kidney Protection Strategy | 腎臟指引 / 腎臟保護策略 |
| PEEP | Positive End-Expiratory Pressure | 吐氣末正壓 |
| EIT | Electrical Impedance Tomography | 電阻抗斷層掃描 |
| ARDS | Acute Respiratory Distress Syndrome | 急性呼吸窘迫症候群 |

---

<!-- _class: abbr -->
# 縮寫對照 (2/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| mNGS | Metagenomic Next-Generation Sequencing | 總體基因體次世代定序 |
| DOOR/RADAR | Desirability of Outcome Ranking / Risk-Adjusted | 抗生素風險調整預後排序 |
| EI / CI / IB | Extended / Continuous Infusion / Intermittent Bolus | 延長 / 連續輸注 / 間歇 bolus |
| OSA / AHI / PAP | Obstructive Sleep Apnea / Apnea-Hypopnea Index / Positive Airway Pressure | 睡眠呼吸中止 / 指數 / 正壓呼吸器 |
| OHCA / ROSC | Out-of-Hospital Cardiac Arrest / Return of Spontaneous Circulation | 院外心跳停止 / 恢復自主循環 |
| ECPR / ECMO | Extracorporeal CPR / Membrane Oxygenation | 體外心肺復甦 / 體外膜氧合 |
| IO / DBP / EtCO₂ | Intraosseous / Diastolic BP / End-Tidal CO₂ | 骨內針 / 舒張壓 / 呼氣末 CO₂ |
| MEL / POAF | Melatonin / Postoperative Atrial Fibrillation | 褪黑激素 / 術後心房顫動 |
| SGLT2 / AMI / CS | SGLT2 inhibitor / Acute MI / Cardiogenic Shock | SGLT2 抑制劑 / 急性心梗 / 心因性休克 |

---

# 重點摘要 Key Pearls (1/2)

> **1. HISTAP RCT**：高風險腹腔手術術中 MAP ≥80 vs ≥65 mmHg → 主要複合終點 38.1% vs 48.9%（RR 0.78，p=0.006），AKI 減少（23.5% vs 33.7%）

> **2. DigiSep RCT**：mNGS 未改善敗血症主要終點（DOOR/RADAR，NS）；次要終點探索性改善

> **3. 科技輔助 PEEP MA**：機械通氣天數無差異，28 天死亡率 RR 0.69（證據 very low）

> **4. 敗血症氧合 RCT（單中心）**：hyperoxia 28 天死亡 ↓（18.7% vs 40.7%），但 90 天無差異——與現行證據相左，審慎

> **5. β-lactam 延長輸注 MA**：治癒率優於間歇 bolus（OR 1.58），死亡率無差異

---

# 重點摘要 Key Pearls (2/2)

> **6. KDIGO 腎臟保護策略**：真實世界僅 31% 完整執行；完整執行與腎功能恢復相關（sHR 6.29）

> **7. Melatonin 預防譫妄 MA**：RR 0.77，外科 ICU / 療程 ≥7 天 / 累積 22 mg 最佳

> **8. 硫酸鎂預防 POAF RCT**：無效提前中止（37.9% vs 28.6%，RR 1.29）

> **9. OHCA 骨內針**：肱骨 IO 優於脛骨 IO（ROSC 校正 OR 2.55）

> **10. 護理師主導家屬參與（NFPS）**：譫妄 ↓（26.85% vs 34.25%），縮短通氣/住院天數

---

<!-- _class: divider -->
# 1. 呼吸支持與機械通氣
## Respiratory Support & Mechanical Ventilation

---

# HISTAP：術中 MAP ≥80 vs ≥65 mmHg — Phase 3 RCT
## Cecconi et al. *Intensive Care Med* 2026 — [DOI 10.1007/s00134-026-08501-7](https://doi.org/10.1007/s00134-026-08501-7) | PMID 42370999

- 18 個義大利中心、n=630、≥60 歲慢性高血壓、選擇性大型腹腔手術、高風險
- 術中 Mean Arterial Pressure (MAP) 目標 ≥80（治療）vs ≥65 mmHg（對照）

| 終點 | ≥80 | ≥65 | 統計 |
|------|-----|-----|------|
| **主要複合（死亡 + ≥1 器官障礙）** | **38.1%** | 48.9% | RR 0.78 (0.65-0.93)，p=0.006 |
| Acute Kidney Injury (AKI) | 23.5% | 33.7% | p=0.005 |

> 已建立連續血流動力學監測 + 協議化輸液的高風險腹腔手術長者，較高 MAP 目標具器官保護（主要來自輕-中度 AKI 減少）

---

# 科技輔助 PEEP 最佳化 — 系統性回顧 + Meta-analysis
## Boulton et al. *Crit Care Med* 2026;54(7):1767 — [DOI 10.1097/CCM.0000000000007144](https://doi.org/10.1097/CCM.0000000000007144) | PMID 42207935

- 34 篇 RCT、n=2,951；食道壓、Electrical Impedance Tomography (EIT)、閉環通氣等 7 技術

| 終點 | 效應 | 證據 |
|------|------|------|
| 機械通氣時間（主要） | 無差異（MD −0.06 天）| very low |
| **28 天死亡率** | **RR 0.69 (0.52-0.93)** | very low |

> 個別化 PEEP 未縮短通氣時間，但可能降低死亡率；證據等級偏低，需大型 RCT 確認——研究熱點而非常規

---

# SynAIRgy：AD109 治療 OSA — Phase 3 RCT
## Strollo et al. *AJRCCM* 2026;212(7):1569 — [DOI 10.1093/ajrccm/aamag215](https://doi.org/10.1093/ajrccm/aamag215) | PMID 42148495

- n=646、無法耐受 Positive Airway Pressure (PAP) 的 Obstructive Sleep Apnea (OSA)；AD109 = aroxybutynin/atomoxetine 口服；26 週

| 終點 | 結果 |
|------|------|
| **Apnea-Hypopnea Index (AHI) 治療差** | **−4.0 事件/小時（p=0.001）** |
| AHI 相對下降 | 44.1% vs 17.6% |
| PROMIS-Fatigue（疲勞）| 無顯著差異 |
| 因不良事件停藥 | 21.2% vs 3.1% |

> 首個具規模的 OSA 藥物 Phase 3 陽性結果；效應中等、症狀改善有限、耐受性議題仍需關注

---

<!-- _class: divider -->
# 2. Sepsis 與感染管控
## Sepsis & Infection Control

---

# DigiSep：Metagenomic NGS 於敗血症 — RCT
## Brenner et al. *Intensive Care Med* 2026 — [DOI 10.1007/s00134-026-08521-3](https://doi.org/10.1007/s00134-026-08521-3) | PMID 42377463

- 24 個德國 ICU、n=389；mNGS + 標準微生物 vs 僅標準微生物

| 終點 | 介入 | 對照 | 統計 |
|------|------|------|------|
| **DOOR/RADAR（主要）** | 3.21 | 3.49 | 95% CI −0.58~0.03（**NS**）|
| 機械通氣天數 | 6.6 | 9.3 天 | 差異顯著（次要）|
| 90 天 EQ-5D-5L | 0.312 | 0.208 | p=0.047 |

> **主要終點陰性**——mNGS 常規使用尚無 RCT 實證支持；保留給培養無解、高度懷疑非典型病原之個案

---

# β-lactam 延長 vs 連續輸注 — 網絡 Meta-analysis
## Zhou et al. *Crit Care* 2026;30(1) — [DOI 10.1186/s13054-026-06142-2](https://doi.org/10.1186/s13054-026-06142-2) | PMID 42323608

- 35 篇 RCT、n=10,627；Extended (EI) / Continuous (CI) / Intermittent Bolus (IB)

| 終點 | EI vs IB | CI vs IB |
|------|---------|---------|
| 全死因死亡率 | OR 0.80（NS）| OR 0.86（NS）|
| **臨床治癒率** | **OR 1.58 (1.13-2.23)** | OR 1.35 (1.05-1.85) |
| 住院天數 | −3.49 天（邊界）| 無顯著 |

> 延長 / 連續輸注治癒率優於間歇 bolus，死亡率無差異；考量可行性，**延長輸注（EI）為務實首選**

---

# SHAMROC：限制 vs 自由輸液長期結果（CLOVERS 追蹤）
## Jorda et al. *AJRCCM* 2026;212(7):1510 — [DOI 10.1093/ajrccm/aamag154](https://doi.org/10.1093/ajrccm/aamag154) | PMID 42093058

- CLOVERS 預設長期追蹤、n=898、6 與 12 個月評估

| 領域（6 個月）| 差異（限制 vs 自由）| 結論 |
|------|------|------|
| 認知（MoCA-Blind）| 0.11 | 無差異 |
| 失能（ADL）| 0.03 | 無差異 |
| 生活品質（EQ-5D-5L）| −0.01 | 無差異 |

> 敗血症低血壓的早期限制或自由輸液策略，**6 與 12 個月認知、身體功能、生活品質皆無差異**；可依個別血流動力學彈性選擇

---

<!-- _class: divider -->
# 3. AKI / 血液動力學 / 休克
## AKI / Hemodynamics / Shock

---

# KDIGO 腎臟保護策略（KPS）真實世界執行
## Sadjadi et al. *Crit Care* 2026;30(1) — [DOI 10.1186/s13054-026-06144-0](https://doi.org/10.1186/s13054-026-06144-0) | PMID 42321935

- 5 個歐洲中心、n=258（KDIGO 2-3 期 Acute Kidney Injury）

| 指標 | 結果 |
|------|------|
| 完整 KPS 執行率 | **31%** |
| MAP 最佳化（最低）| 33% |
| 住院時腎功能恢復（校正 sHR）| **6.29 (3.08-12.85)** |
| 30 天內需 RRT | sHR 0.12 (0.02-0.91) |

> 腎臟保護策略真實世界僅 1/3 完整執行，MAP 最佳化落差最大；可透過 AKI 警示 + bundle 查核立即改善照護

---

# 敗血症氧合目標 — 單中心 RCT（審慎解讀）
## Chen et al. *Shock* 2026;66(1):90 — [DOI 10.1097/SHK.0000000000002865](https://doi.org/10.1097/SHK.0000000000002865) | PMID 42337386

- 單中心、n=270、三組氧合目標（保守 / 常規 / 高氧 PaO₂ 100-150）

| 終點 | 保守 | 常規 | 高氧 |
|------|------|------|------|
| **28 天死亡率** | 40.7% | 34.4% | **18.7%**（p=0.005）|
| 90 天死亡率 | 50.0% | 41.9% | 36.3%（NS）|

> ⚠️ **與 ICU-ROX / HYPERS2S 等相左，單中心小樣本、90 天無差異**——不改變「避免高氧、SpO₂ 92-96%」實踐，僅供假說生成

---

<!-- _class: divider -->
# 4. 急救與心肺復甦
## Cardiac Arrest & Resuscitation

---

# ECPR 用於難治性 OHCA — 成本效益模型
## Nazeha et al. *Crit Care Med* 2026;54(7):1721 — [DOI 10.1097/CCM.0000000000007153](https://doi.org/10.1097/CCM.0000000000007153) | PMID 42378681

- 新加坡體系、決策樹 + Markov 模型、n=1,462（可電擊、無到院前 ROSC）

| 情境 | ICER（門檻 S$45,000/QALY）| 結論 |
|------|------|------|
| 基準 | $34,320/QALY | 具成本效益 |
| 年齡 <65 歲 | $33,469/QALY | 具成本效益 |
| 轉送 +10 分鐘 | $47,158/QALY | 略超門檻 |

> Extracorporeal CPR (ECPR) 對難治性 OHCA 多數情境具成本效益，但**對轉送時間高度敏感**——縮短到 ECMO 中心時間是關鍵

---

# OHCA 骨內針位置 + ICU CPR 生理指標
## Resuscitation 2026 — [IO DOI](https://doi.org/10.1016/j.resuscitation.2026.111179) PMID 42314896 ｜ [DBP/EtCO₂ DOI](https://doi.org/10.1016/j.resuscitation.2026.111177) PMID 42331277

- **肱骨 vs 脛骨 Intraosseous (IO)**（n=1,920）：ROSC 校正 OR **2.55 (1.54-4.22)**；存活出院 OR 2.04
- **ICU CPR 生理指標**（68 事件）：ROSC 組 Diastolic BP (DBP) 39 vs 24 mmHg（p<0.001）、End-Tidal CO₂ (EtCO₂) 19 vs 15 mmHg（p=0.010）

> 肱骨 IO 可能較脛骨帶來更高 ROSC / 存活（回溯，需 RCT）；ICU 心跳停止若有動脈導管 + capnography，DBP 與 EtCO₂ 為互補的 CPR 品質指標

---

# Pre-MIRACLEscore：到院前 OHCA 神經預後
## Razak et al. *Resuscitation* 2026 — [DOI 10.1016/j.resuscitation.2026.111176](https://doi.org/10.1016/j.resuscitation.2026.111176) | PMID 42379417

- EUCAR（n=1,402）+ GLOBAL-MIRACLE（前瞻 n=747）；ROSC 後仍昏迷者
- 自 MIRACLEscore 移除 pH（適用無法測 pH 的到院前環境）

| 驗證 | AUROC |
|------|-------|
| 整體 | 0.85 (0.83-0.87) |
| 前瞻驗證 | 0.85 (校正斜率 1.11) |

> 到院前 / 無法測 pH 環境的 OHCA 神經預後分層工具（AUROC 0.85）；**預後工具不應單獨用於早期撤除維生決策**

---

<!-- _class: divider -->
# 5. 神經重症 / 譫妄 / ICU 照護品質
## Neurocritical Care / Delirium / ICU Quality

---

# Melatonin 類藥物預防 ICU 譫妄 — 劑量-反應 MA
## Chaves-Filho et al. *Crit Care* 2026;30(1) — [DOI 10.1186/s13054-026-06047-0](https://doi.org/10.1186/s13054-026-06047-0) | PMID 42310686

- 24 篇 RCT、n=3,680；GRADE + trial sequential analysis

| 終點 | 效應 |
|------|------|
| **譫妄發生率** | **RR 0.77 (0.62-0.94)** |
| 外科型 ICU | RR 0.64 (0.48-0.87) |
| 療程 ≥7 天 | RR 0.73 (0.60-0.90) |
| 最佳累積劑量 | 約 22 mg Melatonin (MEL) |

> MEL / ramelteon 可能降低譫妄，外科 ICU、療程 ≥7 天、22 mg 最佳；安全但效應中等、低確定性——作為 ABCDEF bundle 輔助，不取代非藥物核心

---

# POC EEG AI 癲癇負荷 + 護理師主導家屬參與
## CCM 2026 — [EEG-AI DOI](https://doi.org/10.1097/CCM.0000000000007158) PMID 42223304 ｜ Crit Care — [NFPS DOI](https://doi.org/10.1186/s13054-026-06145-z) PMID 42316318

- **POC EEG + AI 癲癇負荷（SzB）**（n=359）：每多 1 h 癲癇活動 → 不良預後校正 OR 1.98；SzB ≥90% → OR 增 3.4 倍（劑量-反應）
- **NFPS 護理師主導家屬參與**（配對每組 365）：譫妄 26.85% vs 34.25%（p=0.03），縮短通氣 / ICU / 住院天數，長期死亡率無差異

> AI 輔助床邊 EEG 助早期偵測非驚厥性癲癇；NFPS 是低成本安全的非藥物譫妄策略

---

<!-- _class: divider -->
# 6. 其他值得關注
## Honorable Mentions

---

# 其他焦點 (Honorable Mentions)

| 主題 | 重點 | 連結 |
|------|------|------|
| **硫酸鎂預防 POAF（RCT，CCM）** | 無效提前中止：37.9% vs 28.6%（RR 1.29）；不支持常規補鎂 | [DOI](https://doi.org/10.1097/CCM.0000000000007162) |
| **SGLT2i 於 AMI-CS（Shock）** | 出院處方 SGLT2i：1 年心死亡 sHR 0.749（NS），趨勢良好待 RCT | [DOI](https://doi.org/10.1097/SHK.0000000000002904) |
| **重症神經併發症（ICM 綜述）** | 譫妄 / ICU-AW / 腦病變是死亡與失能主因，需系統性偵測 | [DOI](https://doi.org/10.1007/s00134-026-08490-7) |
| **治療限制的性別差異（Crit Care）** | 差異主要在入院時（女性 aOR 1.26），住院期間無差異 | [DOI](https://doi.org/10.1186/s13054-026-06139-x) |
| **蛋白質劑量指引（Crit Care）** | 急性期高蛋白未改善結果、AKI 可能有害；身體組成導向研究 | [DOI](https://doi.org/10.1186/s13054-026-06116-4) |

---

<!-- _class: ref -->
# 參考文獻 (1/2)

1. Cecconi M, et al. HISTAP: high vs standard blood pressure target in major abdominal surgery. *Intensive Care Med*. 2026. [DOI](https://doi.org/10.1007/s00134-026-08501-7) PMID 42370999
2. Boulton AJ, et al. Technology-enhanced PEEP optimization: systematic review and meta-analysis. *Crit Care Med*. 2026;54(7):1767. [DOI](https://doi.org/10.1097/CCM.0000000000007144) PMID 42207935
3. Strollo PJ, et al. AD109 for OSA: phase 3 trial (SynAIRgy). *AJRCCM*. 2026;212(7):1569. [DOI](https://doi.org/10.1093/ajrccm/aamag215) PMID 42148495
4. Brenner T, et al. Clinical metagenomics in sepsis: the DigiSep trial. *Intensive Care Med*. 2026. [DOI](https://doi.org/10.1007/s00134-026-08521-3) PMID 42377463
5. Zhou L, et al. Extended vs continuous infusion of beta-lactams: network meta-analysis. *Crit Care*. 2026;30(1). [DOI](https://doi.org/10.1186/s13054-026-06142-2) PMID 42323608
6. Jorda A, et al. Restrictive vs liberal fluid, long-term outcomes (SHAMROC). *AJRCCM*. 2026;212(7):1510. [DOI](https://doi.org/10.1093/ajrccm/aamag154) PMID 42093058
7. Sadjadi M, et al. Kidney protection strategy implementation in AKI. *Crit Care*. 2026;30(1). [DOI](https://doi.org/10.1186/s13054-026-06144-0) PMID 42321935
8. Chen X, et al. Impact of oxygen targets on sepsis outcome: RCT. *Shock*. 2026;66(1):90. [DOI](https://doi.org/10.1097/SHK.0000000000002865) PMID 42337386
9. Decoding candidemia phenotypes in critically ill patients. *Crit Care*. 2026. [DOI](https://doi.org/10.1186/s13054-026-05964-4) PMID 42365321

---

<!-- _class: ref -->
# 參考文獻 (2/2)

10. Nazeha N, et al. Cost-effectiveness of ECPR in OHCA. *Crit Care Med*. 2026;54(7):1721. [DOI](https://doi.org/10.1097/CCM.0000000000007153) PMID 42378681
11. Razak MA, et al. Pre-MIRACLEscore for OHCA neurological risk. *Resuscitation*. 2026. [DOI](https://doi.org/10.1016/j.resuscitation.2026.111176) PMID 42379417
12. Witherell A, et al. Intraosseous line location and OHCA outcomes. *Resuscitation*. 2026;226:111179. [DOI](https://doi.org/10.1016/j.resuscitation.2026.111179) PMID 42314896
13. Singh A, et al. DBP and EtCO₂ during ICU CPR and ROSC. *Resuscitation*. 2026. [DOI](https://doi.org/10.1016/j.resuscitation.2026.111177) PMID 42331277
14. Chaves-Filho A, et al. Melatoninergic agonists for ICU delirium: dose–response meta-analysis. *Crit Care*. 2026;30(1). [DOI](https://doi.org/10.1186/s13054-026-06047-0) PMID 42310686
15. Parvizi J, et al. POC EEG AI seizure burden and outcome. *Crit Care Med*. 2026;54(7):1710. [DOI](https://doi.org/10.1097/CCM.0000000000007158) PMID 42223304
16. Wu Y, et al. Nurse-led family participatory support in ICU. *Crit Care*. 2026;30(1). [DOI](https://doi.org/10.1186/s13054-026-06145-z) PMID 42316318
17. Meerman M, et al. Magnesium sulfate to prevent POAF: RCT. *Crit Care Med*. 2026;54(7):1635. [DOI](https://doi.org/10.1097/CCM.0000000000007162) PMID 42206948
18. Burden of neurological complications in critical illness. *Intensive Care Med*. 2026. [DOI](https://doi.org/10.1007/s00134-026-08490-7) PMID 42377460
19. Amacher SA, et al. Sex differences in treatment limitation decisions. *Crit Care*. 2026;30(1). [DOI](https://doi.org/10.1186/s13054-026-06139-x) PMID 42316265

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**整理：謝慕揚 MD, PhD, FESC**

本回顧涵蓋 2026-06-17 ～ 2026-07-01
資料來源：PubMed（ICM · Critical Care · CCM · AJRCCM · Chest · Resuscitation · Shock）
