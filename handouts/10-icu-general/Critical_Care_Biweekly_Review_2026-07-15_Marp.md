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
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-07-15'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧

## 2026-07-01 ～ 2026-07-15

**謝慕揚 MD, PhD, FESC** | 2026-07-15

涵蓋：ICM、Critical Care、CCM、Ann Intensive Care、Resuscitation、Chest、Lancet Respir Med、AJRCCM、Shock

---

<!-- _class: abbr -->

# 縮寫對照 (1/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| RCT | Randomized Controlled Trial | 隨機對照試驗 |
| NMA | Network Meta-Analysis | 網絡統合分析 |
| RR | Relative Risk / Risk Ratio | 相對風險 |
| OR / aOR | (Adjusted) Odds Ratio | （校正）勝算比 |
| HR / sHR | Hazard / Subhazard Ratio | 風險比／次分布風險比 |
| CI | Confidence Interval | 信賴區間 |
| GRADE | Grading of Recommendations Assessment, Development and Evaluation | 證據等級系統 |
| AUROC | Area Under the ROC Curve | ROC 曲線下面積 |
| ICU | Intensive Care Unit | 加護病房 |
| ARDS | Acute Respiratory Distress Syndrome | 急性呼吸窘迫症候群 |
| IMV / NIV | Invasive / Non-Invasive Ventilation | 侵襲性／非侵襲性通氣 |
| HFNC | High-Flow Nasal Cannula | 高流量鼻管氧療 |
| VT / PBW | Tidal Volume / Predicted Body Weight | 潮氣量／理想預測體重 |
| ULTV / LTV | Ultra-Low / Low Tidal Volume Ventilation | 超低／低潮氣量通氣 |
| PEEP | Positive End-Expiratory Pressure | 吐氣末正壓 |

---

<!-- _class: abbr -->

# 縮寫對照 (2/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| LDP | Lung- and Diaphragm-Protective ventilation | 肺與橫膈同步保護通氣 |
| P-SILI | Patient Self-Inflicted Lung Injury | 病人自傷性肺損傷 |
| P0.1 | Airway Occlusion Pressure at 100 ms | 氣道阻斷壓（100 毫秒） |
| ΔP_L | (Calculated) Transpulmonary Driving Pressure | 跨肺驅動壓 |
| VFD | Ventilator-Free Days | 脫離呼吸器天數 |
| ECMO / ECCO₂R | Extracorporeal Membrane Oxygenation / CO₂ Removal | 體外膜氧合／二氧化碳移除 |
| VAP | Ventilator-Associated Pneumonia | 呼吸器相關肺炎 |
| CAP | Community-Acquired Pneumonia | 社區型肺炎 |
| CRT / TP-GT | Capillary Refill Time / Tissue-Perfusion-Guided Therapy | 微血管再充填時間／組織灌流導向治療 |
| CS / tMCS | Cardiogenic Shock / Temporary Mechanical Circulatory Support | 心因性休克／暫時性機械循環支持 |
| mAFP | Micro-Axial Flow Pump (Impella) | 微軸流泵 |
| LVEF / GLS / MAPSE | Ejection Fraction / Global Longitudinal Strain / Mitral Annular Plane Systolic Excursion | 射血分率／整體縱向應變／二尖瓣環收縮位移 |
| OHCA / ROSC / PEA | Out-of-Hospital Cardiac Arrest / Return of Spontaneous Circulation / Pulseless Electrical Activity | 到院前心跳停止／自發循環恢復／無脈搏電氣活動 |
| SOFA-2 | Sequential Organ Failure Assessment 2 | 連續器官衰竭評估（第 2 版） |

---

# 本期重點摘要 (Key Pearls) — 1/2

- **Albumin 在 septic shock**：meta-analysis RR **0.90 (0.83-0.99)**，但 GRADE low、間接證據 → 尚不改 first-line
- **Tissue-perfusion-guided 復甦**：30 天死亡 **RR 0.96 (NS)**，價值在減少早期輸液（省 ~467 mL）
- **Corticosteroid 在 CAP**：高劑量 **不優於** 低劑量（RR 0.98）；低劑量即足夠
- **ULTV（4 mL/kg）在 COVID ARDS**：1 年死亡不降（HR 1.19），**認知反而較差**（MoCA −2 分）
- **LDP 通氣新框架**：ΔP_L >20 cmH₂O → 死亡 **HR 6.57**（Effort-I）

---

# 本期重點摘要 (Key Pearls) — 2/2

- **拔管後 NIV 空檔用 HFNC**：再插管 13.7% vs 18.5%（p=0.036），但校正後 NS → 可考慮
- **Naloxone 在 PEA 型 OHCA**：存活至出院 **OR 1.46 (1.11-1.92)**；shockable/asystole 無關
- **年齡 × Impella（CS）**：每增 1 歲 30 天死亡 +3.2%；LVEF 恢復由 74.5% → 41.9%
- **重症心臟超音波**：**MAPSE ≤10 mm aOR 2.48**，MAPSE/GLS 優於 LVEF
- **Obesity 機械通氣**：個體化 PEEP、食道壓/EIT 監測、prone 安全

---

<!-- _class: divider -->

# 1. 呼吸治療與機械通氣

---

# Lung- and Diaphragm-Protective (LDP) Ventilation

## Plens GM, et al. Intensive Care Med 2026 — https://doi.org/10.1007/s00134-026-08535-x

- 從只保護肺 → **同時保護肺與橫膈**，重點在 **assisted ventilation（輔助通氣期）**
- 過強吸氣努力 → P-SILI + 橫膈 myotrauma；努力不足 → 橫膈萎縮
- 整合通氣 + 鎮靜；新興工具：diaphragm neurostimulation、partial neuromuscular blockade

> 呼應 **Effort-I**（Ann Intensive Care 2026, n=206）：ΔP_L >20 cmH₂O → 28 天死亡 **HR 6.57 (2.29-18.86)**；P0.1 過低或過高皆與死亡相關。

---

# ULTV vs LTV：VT4COVID 1 年追蹤

## Richard JC, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06195-3

- COVID-19 ARDS、10 法國 ICU、n=215；ULTV **4 mL/kg PBW** vs LTV **6 mL/kg PBW**
- **1 年死亡 46% vs 42%，HR 1.19 (0.79-1.80) — 無差異**
- **ULTV 組 MoCA 較低（中位差 −2 分，p<0.05）**；與 PaCO₂ 暴露相關，與最低 PaO₂ 無關

> 臨床啟示：超低潮氣量伴 permissive hypercapnia 可能有**認知代價**；除非有 driving pressure/mechanical power 理由，不建議常規壓到 4 mL/kg。

---

# 拔管後 NIV 空檔期：HFNC vs 標準氧氣

## Thille AW, et al. Intensive Care Med 2026 — https://doi.org/10.1007/s00134-026-08544-w

- 高風險（>65 歲或心肺疾病）拔管後預防性 NIV，空檔用 HFNC (n=655) vs 標準氧氣 (n=422)
- **7 天 extubation failure 13.7% vs 18.5%（差 −4.7%，p=0.036）**
- **但 G-computation 校正後 −3.9%（NS）**；僅 48h 內再插管顯著較低

> 定位：訊號正向、待 RCT 確認 → **可考慮、非強制**。延續上期「高風險無 hypercapnia 者 NIV 仍有價值」討論。

---

# 60 年 ARDS：ECMO → ECCO₂R ｜ Obesity 通氣力學

## Fernando SM, et al. ICM 2026 — https://doi.org/10.1007/s00134-026-08533-z ｜ Nova A, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06181-9

**ECLS 演進（Review）**
- 回顧 VV-ECMO 與 ECCO₂R 在 ARDS 的療效、預後、併發症與長期預後；標示不確定領域

**Obesity 機械通氣（Review）**
- 肥胖降 FRC → airway closure、atelectasis；建議個體化 PEEP、食道壓/EIT 監測
- 中重度 ARDS prone 安全；拔管後早期 NIV 有助

---

<!-- _class: divider -->

# 2. Sepsis 與血流動力學

---

# Albumin 復甦在 septic shock

## Mendes H, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06172-w

- 7 RCT、n=3,273，白蛋白 vs 晶體液復甦
- **最長追蹤全因死亡 RR 0.90 (0.83-0.99)；p=0.02；I²=0%**
- Bayesian 後驗死亡下降機率 **94.7%**

> 但多為次族群資料、屬**間接**、不精確 → **GRADE low certainty**。尚不足以改為 first-line；待專門設計 RCT。

---

# Tissue-Perfusion-Guided 復甦｜Corticosteroid 在 CAP

## Tóth T, et al. Ann Intensive Care 2026 — https://doi.org/10.1016/j.aicoj.2026.100106 ｜ Ouyang Y, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06185-5

**TP-GT（8 RCT, n=2,394）**
- 30 天死亡 **RR 0.96 (NS)**；90 天 RR 0.94 (NS)
- 前 6-8h 輸液 **−467 mL**；價值 = fluid stewardship

**Corticosteroid CAP（NMA, 32 RCT, n=9,746）**
- 高/低劑量 vs placebo：RR 0.83 / 0.84（皆降死亡）
- **高 vs 低劑量：RR 0.98（無差異）** → **低劑量即足夠**

---

<!-- _class: divider -->

# 3. 心臟循環支持與重症心臟超音波

---

# 年齡 × microaxial flow pump（Impella）在 CS

## Ughetto A, et al. Ann Intensive Care 2026 — https://doi.org/10.1016/j.aicoj.2026.100104

- 歐洲 11 中心登錄，n=1,043（Impella CP/5.0/5.5）
- **每增 1 歲 30 天死亡 adjusted sHR 1.032**
- 最高兩四分位 30 天死亡 sHR 1.66、1.87；1 年 1.78、2.08（Ptrend <0.01）
- 主要 LVEF 恢復：最年輕 **74.5% → 最年長 41.9%**

> 高齡 CS 病人 tMCS 存活與心肌恢復顯著較差 → 決策納入年齡與恢復潛力。

---

# 重症心臟超音波：MAPSE / GLS 優於 LVEF

## Cavefors O, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06193-5

- 前瞻觀察 n=377，入院 24h 內超音波
- **可行性**：MAPSE 90% > S' 83% > LVEF 71% > GLS 65%
- 校正後與 90 天死亡相關：**GLS (OR 1.08/1%)、MAPSE (OR 1.17/mm)**；LVEF、S' 則否
- **MAPSE ≤10 mm：aOR 2.48 (1.31-4.71)**

> LVEF 在 ICU 預後價值有限；納入 MAPSE（最易取得）與 GLS 提升左心功能不全偵測。

---

<!-- _class: divider -->

# 4. 心跳停止與復甦後照護

---

# Naloxone 與 PEA 型 OHCA 存活

## Niederberger SM, et al. Resuscitation 2026;225:111139 — https://doi.org/10.1016/j.resuscitation.2026.111139

- 美國 40,333 例 OHCA，依 presenting rhythm 分層，propensity-matched
- **PEA 病人 naloxone → 存活至出院 OR 1.46 (1.11-1.92)**；ROSC OR 1.09 (NS)
- shockable rhythm 與 asystole：naloxone 與結果**無關聯**

> opioid-associated OHCA 上升；non-shockable（尤其 PEA）rhythm 可能提示鴉片相關 → 積極給 naloxone（待 RCT 確認因果）。

---

# 心跳停止後「延遲甦醒」

## Sandroni C, Grippo A. Resuscitation 2026;225:111156 — https://doi.org/10.1016/j.resuscitation.2026.111156

- Post-cardiac arrest 病人可能在數日至數週後才恢復意識（late awakening）
- 強調**避免過早悲觀 prognostication**
- 以多模態工具（EEG、影像、生物標記）提升「恢復預測」而非僅「不良預測」

---

<!-- _class: divider -->

# 5. 感染預防、精準醫療與 ICU 實務

---

# VAP 精準管理｜動脈導管感染預防

## Rouzé A, et al. ICM 2026 — https://doi.org/10.1007/s00134-026-08548-6 ｜ Donner V, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06153-z

**VAP（Editorial）**：病生理 → 精準診斷/治療（快速微生物、biomarker 導向療程）

**動脈導管相關血流感染 AC-CRBSI（Review）**
- 長期被低估，證據多外推自中心靜脈導管
- 預防 bundle：catheter stewardship、2% chlorhexidine、chlorhexidine 敷料、每 7 天更換、手部衛生
- 爭議：插入部位、超音波導引風險、定期換管

---

# 精準重症｜到院前呼吸道管理

## Van Nynatten LR, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06169-5 ｜ Vieux T, et al. ICM 2026 — https://doi.org/10.1007/s00134-026-08532-0

**The Molecular ICU（Review）**
- 眾多 neutral RCT 源於生物學不一致族群 → 提出 **pathway-level biomarker** + predictive enrichment

**Prehospital airway（Review）**
- OHCA：supraglottic airway 為合理首選（存活相當、置放快）
- 急性心因性肺水腫/COPD：NIV（CPAP/BiPAP）證據明確；prehospital HFNC 資料仍有限

---

<!-- _class: divider -->

# 6. 其他值得關注

---

# Honorable Mentions

| 主題 | 重點 | 連結 |
|------|------|------|
| SOFA-2 外部驗證（n=118,542） | AUROC **80.9% vs 76.7%**（優於 SOFA-1） | https://doi.org/10.1016/j.aicoj.2026.100107 |
| HDI × 高齡重症（n=9,920） | HDI ≥0.90 國家 30 天死亡較低（aOR 0.49）；較少 IMV 部分中介 | https://doi.org/10.1016/j.aicoj.2026.100101 |
| APS Consortium（Chest） | ARDS/Pneumonia/Sepsis 表型化國家平台設計 | https://doi.org/10.1016/j.chest.2026 |
| MM 病人 ICU 存活改善（n=428） | 近期世代 1 年死亡下降（aOR 0.68）→ 應積極收治 | https://doi.org/10.1016/j.aicoj.2026.100100 |

---

<!-- _class: ref -->

# 參考文獻 (1/2)

1. Plens GM, et al. Lung- and diaphragm-protective mechanical ventilation in ARDS. *Intensive Care Med*. 2026. https://doi.org/10.1007/s00134-026-08535-x (PMID 42412219)
2. Soipetkasem P, et al. Effort-I: respiratory effort parameters and outcomes. *Ann Intensive Care*. 2026;16:100103. https://doi.org/10.1016/j.aicoj.2026.100103 (PMID 42388558)
3. Richard JC, et al. Ultra-low tidal volume and 1-year outcome in COVID-19 ARDS (VT4COVID). *Crit Care*. 2026;30(1). https://doi.org/10.1186/s13054-026-06195-3 (PMID 42449426)
4. Thille AW, et al. HFNC during breaks from NIV after extubation. *Intensive Care Med*. 2026. https://doi.org/10.1007/s00134-026-08544-w (PMID 42440109)
5. Fernando SM, et al. 60 years of ARDS: ECMO to ECCO₂R. *Intensive Care Med*. 2026. https://doi.org/10.1007/s00134-026-08533-z (PMID 42412218)
6. Nova A, et al. Obesity: biomechanical implications for mechanical ventilation. *Crit Care*. 2026. https://doi.org/10.1186/s13054-026-06181-9 (PMID 42415102)
7. Mendes H, et al. Albumin fluid resuscitation in septic shock: meta-analysis. *Crit Care*. 2026. https://doi.org/10.1186/s13054-026-06172-w (PMID 42410446)
8. Tóth T, et al. Tissue-perfusion-guided resuscitation in shock: meta-analysis. *Ann Intensive Care*. 2026;16:100106. https://doi.org/10.1016/j.aicoj.2026.100106 (PMID 42434600)
9. Ouyang Y, et al. Higher vs lower dose corticosteroids in CAP: NMA. *Crit Care*. 2026. https://doi.org/10.1186/s13054-026-06185-5 (PMID 42402602)
10. Hunsicker O, et al. Pathophysiology of distributive shock beyond vasoplegia. *Intensive Care Med*. 2026. https://doi.org/10.1007/s00134-026-08555-7 (PMID 42440111)

---

<!-- _class: ref -->

# 參考文獻 (2/2)

11. Ughetto A, et al. Age and microaxial flow pump outcomes in cardiogenic shock. *Ann Intensive Care*. 2026;16:100104. https://doi.org/10.1016/j.aicoj.2026.100104 (PMID 42403523)
12. Cavefors O, et al. Echocardiographic LV longitudinal function in the ICU. *Crit Care*. 2026;30(1). https://doi.org/10.1186/s13054-026-06193-5 (PMID 42432793)
13. Niederberger SM, et al. Naloxone and survival in PEA OHCA. *Resuscitation*. 2026;225:111139. https://doi.org/10.1016/j.resuscitation.2026.111139 (PMID 42176972)
14. Sandroni C, Grippo A. Late awakening after cardiac arrest. *Resuscitation*. 2026;225:111156. https://doi.org/10.1016/j.resuscitation.2026.111156 (PMID 42242458)
15. Rouzé A, et al. Advances in VAP: pathophysiology to precision management. *Intensive Care Med*. 2026. https://doi.org/10.1007/s00134-026-08548-6 (PMID 42417825)
16. Donner V, et al. Prevention of arterial catheter-related bloodstream infections. *Crit Care*. 2026. https://doi.org/10.1186/s13054-026-06153-z (PMID 42410430)
17. Van Nynatten LR, et al. The molecular ICU: omics and precision critical care. *Crit Care*. 2026;30(1). https://doi.org/10.1186/s13054-026-06169-5 (PMID 42410654)
18. Vieux T, et al. Prehospital airway and ventilatory management. *Intensive Care Med*. 2026. https://doi.org/10.1007/s00134-026-08532-0 (PMID 42390593)
19. Liufu R, et al. External validation of SOFA-2 score. *Ann Intensive Care*. 2026;16:100107. https://doi.org/10.1016/j.aicoj.2026.100107 (PMID 42434601)
20. Dankl D, et al. HDI and outcomes in older critically ill patients. *Ann Intensive Care*. 2026;16:100101. https://doi.org/10.1016/j.aicoj.2026.100101 (PMID 42388557)
21. Nakaa S, et al. Improved ICU survival in multiple myeloma. *Ann Intensive Care*. 2026;16:100100. https://doi.org/10.1016/j.aicoj.2026.100100 (PMID 42403522)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

讀書會共筆整理人 ｜ 2026-07-15

本文件為讀書會內部共筆，僅供醫療專業人員教學討論參考
