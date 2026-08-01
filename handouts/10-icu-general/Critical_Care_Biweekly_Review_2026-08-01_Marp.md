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
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-08-01'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧

## 2026-07-18 ～ 2026-08-01

**謝慕揚 MD, PhD, FESC** | 2026-08-01

涵蓋：ICM、Critical Care、CCM、Ann Intensive Care、Resuscitation、Chest、Lancet Respir Med、AJRCCM、Shock

---

<!-- _class: abbr -->

# 縮寫對照 (1/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| RCT / IPD | Randomized Controlled Trial / Individual Patient Data | 隨機對照試驗／個別病人資料 |
| TSA | Trial Sequential Analysis | 試驗序列分析 |
| GRADE | Grading of Recommendations Assessment, Development and Evaluation | 證據等級評估 |
| RR / OR / IRR | Relative Risk / Odds Ratio / Incidence Rate Ratio | 相對風險／勝算比／發生率比 |
| CI / NNT | Confidence Interval / Number Needed to Treat | 信賴區間／需治療人數 |
| AUC | Area Under the Curve | 曲線下面積 |
| QALY / mRS | Quality-Adjusted Life-Year / modified Rankin Scale | 品質調整生命年／改良 Rankin 量表 |
| ARDS | Acute Respiratory Distress Syndrome | 急性呼吸窘迫症候群 |
| VILI / APP | Ventilator-Induced Lung Injury / Awake Prone Position | 呼吸器誘發肺損傷／清醒俯臥 |
| ECMO (VA/VV) | (Venoarterial/Venovenous) Extracorporeal Membrane Oxygenation | （動脈-靜脈／靜脈-靜脈）體外膜氧合 |
| tDNS | Transvenous Diaphragm Neurostimulation | 經靜脈橫膈神經刺激 |
| PaO₂/FiO₂ / SvO₂ | Arterial O₂ / Inspired O₂ fraction / Mixed venous O₂ sat | 動脈氧分壓／吸入氧濃度／混合靜脈氧飽和 |

---

<!-- _class: abbr -->

# 縮寫對照 (2/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| EGDT / CRT | Early Goal-Directed Therapy / Capillary Refill Time | 早期目標導向治療／微血管再充填時間 |
| PE / RV / PA | Pulmonary Embolism / Right Ventricle / Pulmonary Artery | 肺栓塞／右心室／肺動脈 |
| HP | Hemoperfusion | 血液灌流 |
| AKI / CSA-AKI | Acute Kidney Injury / Cardiac Surgery-Associated AKI | 急性腎損傷／心臟手術相關 AKI |
| RRT / CPB | Renal Replacement Therapy / Cardiopulmonary Bypass | 腎臟替代治療／體外循環 |
| STARD / DTA | Standards for Reporting Diagnostic Accuracy / Diagnostic Test Accuracy | 診斷準確度報告標準／診斷準確度 |
| ABI / ICP / nICP | Acute Brain Injury / (non-invasive) Intracranial Pressure | 急性腦損傷／（非侵襲性）顱內壓 |
| ICH / TCD | Intracerebral Hemorrhage / Transcranial Doppler | 腦內出血／穿顱都卜勒 |
| CA / OHCA | Cardiac Arrest / Out-of-Hospital Cardiac Arrest | 心跳停止／到院前心跳停止 |
| WLST / CRS-R | Withdrawal of Life-Sustaining Therapy / Coma Recovery Scale-Revised | 撤除維生治療／昏迷恢復量表 |
| NSE / SEP / EEG | Neuron-Specific Enolase / Somatosensory Evoked Potentials / EEG | 神經元烯醇酶／體感覺誘發電位／腦電圖 |
| bCPR / LVOT / iAMC | Bystander CPR / LV Outflow Tract / ideal Area of Maximal Compression | 旁觀者 CPR／左心室流出道／理想最大按壓區 |

---

<!-- _class: divider -->
# 本期 10 大重點

---

<!-- _class: small-text -->

# 重點摘要 Pearls (1/2)

1. **Sodium bicarbonate（嚴重代謝性酸血症）**：不降整體 90 天死亡（RR 0.96），但**↓RRT（RR 0.69，NNT 6.3）**；pH ≤7.10 死亡 RR 0.80。
2. **Hemoperfusion + ECMO**：整體無效益（OR 0.98），**RCT 中死亡上升（OR 4.96）**→ 不建議常規使用。
3. **術中 Hemoadsorption 預防 CSA-AKI**：陰性（RR 0.80，NS，GRADE very low）。
4. **心跳停止預後判定（排除 WLST）**：≥2 不利指標 FPR 0、OR 34.7；CRS-R 提升鑑別（AUC 0.925 vs 0.888）。
5. **ICH 積極 vs 保守降壓**：功能/死亡無差異，**積極組不良事件較少（RR 0.87）**。

---

<!-- _class: small-text -->

# 重點摘要 Pearls (2/2)

6. **tDNS 脫離呼吸器**：RESCUE-3，↓2.8 天通氣、脫離成功↑10.5%，省 ~US$12k。
7. **急性 PE「normotensive shock」**：2026 AHA/ACC 新概念；CRT／花斑／lactate ＋ echo（RV-PA coupling）早辨識。
8. **25 年 septic shock 復甦**：EGDT → 表型導向（ANDROMEDA-SHOCK-2）。
9. **Prone positioning ARDS**：早期俯臥為標準；awake prone 待非 COVID 確認。
10. **CPR 按壓位置**：指引點常壓在 LVOT 而非 iAMC（偏胸骨旁 4 cm）。

---

<!-- _class: divider -->
# 1. 呼吸治療與機械通氣

---

# Prone Positioning in ARDS — 50 年演進

## Ehrmann S, et al. Intensive Care Med 2026（Review）｜[doi.org/10.1007/s00134-026-08543-x](https://doi.org/10.1007/s00134-026-08543-x)

- 從救援療法 → **早期、標準的 lung-protective ventilation 組成**（插管、PaO₂/FiO₂ <150 mmHg 早期俯臥）。
- COVID-19 擴展至非插管的 **awake prone position (APP)**；非 COVID 族群與常規實務仍待確認。
- 機轉：改善氧合 + **減少 lung stress/strain → 減輕 VILI**，可能有利血流動力學。

> 中重度 ARDS 早期俯臥應視為標準；APP 於合適病人可嘗試，需嚴密監測。

---

# tDNS 於脫離呼吸器：健康經濟價值

## RESCUE-3 建模 · Crit Care Med 2026｜[doi.org/10.1097/CCM.0000000000007262](https://doi.org/10.1097/CCM.0000000000007262)

- Transvenous diaphragm neurostimulation (tDNS) 已證實提升脫離成功、縮短通氣。
- Base case：**↓2.8 天機械通氣、脫離成功率高 10.5%**。
- 節省：急性期 **US$12,102**、長期照護院 **US$11,999**（未計 tDNS 成本）；終生 **0.10-0.68 QALY** 增益。

> 對困難脫離者，tDNS 可能兼具臨床與成本效益；呼應 lung- and diaphragm-protective (LDP) 框架。

---

<!-- _class: divider -->
# 2. Sepsis 與血流動力學

---

# 25 年 Septic Shock 復甦試驗 — 概念回顧

## Contreras R, et al. Crit Care 2026;30(1)（Perspective）｜[doi.org/10.1186/s13054-026-06201-8](https://doi.org/10.1186/s13054-026-06201-8)

- 固定、孤立生理目標（如 EGDT 的 oxygen delivery）反覆**無法複製**。
- 進展：peripheral perfusion (CRT)、fluid responsiveness、critical care echo、hemodynamic phenotyping。
- **ANDROMEDA-SHOCK** 以 CRT 為快速灌流訊號；**ANDROMEDA-SHOCK-2** 操作化「表型化 + 可逆測試 + 短週期再評估」。

> 復甦由「硬性演算法」轉向「生理導向、表型驅動、以可逆測試微調」。

---

# 急性 PE 的 Normotensive Shock

## Crit Care 2026（Review；對應 2026 AHA/ACC PE 指引）｜[doi.org/10.1186/s13054-026-06214-3](https://doi.org/10.1186/s13054-026-06214-3)

- **normotensive shock**：血壓正常但已組織低灌流，屬 pre-cardiopulmonary failure，死亡風險高。
- 多重指標並用：prolonged CRT、skin mottling 補足 lactate。
- Critical care echo：確認急性 RV 壓力負荷、排除其他休克、評估 **RV-PA coupling**。

> 血壓「還正常」的次大面積 PE，若見低灌流 + echo RV 負荷 → 視為 normotensive shock，早考慮 reperfusion 升階。

---

<!-- _class: divider -->
# 3. 腎臟、酸鹼與血液淨化

---

# Sodium Bicarbonate 於嚴重代謝性酸血症 ⭐

## BICAR-ICU + BICAR-ICU2 IPD MA · Crit Care 2026;30(1)｜[doi.org/10.1186/s13054-026-06206-3](https://doi.org/10.1186/s13054-026-06206-3)

| 終點 | 結果 |
|------|------|
| 90 天死亡（整體） | 58.3% vs 60.6%；**RR 0.96（0.86-1.07）NS** |
| RRT 啟動 | 34.8% vs 50.7%；**RR 0.69（0.60-0.79）；NNT 6.3** |
| pH ≤7.10 死亡 | **RR 0.80（0.68-0.93）p=0.004**（p-interaction 0.006） |
| pH >7.10 死亡 | RR 1.05（NS） |

> 不改善整體死亡，但**顯著減少洗腎**；對**最深酸血症（pH ≤7.10）**有存活效益 → 及時矯正。

---

# 血液淨化雙陰性：Hemoadsorption & Hemoperfusion

## Crit Care 2026｜[Hemoadsorption/CSA-AKI](https://doi.org/10.1186/s13054-026-06099-2) ｜ [Hemoperfusion/ECMO](https://doi.org/10.1186/s13054-026-06203-6)

- **術中 Hemoadsorption 預防 CSA-AKI**（15 RCT；n=947）：RR **0.80（0.63-1.03）NS**，GRADE very low，TSA information size 未達。
- **Hemoperfusion + ECMO**（13 studies，n=8,151）：整體 OR **0.98（NS）**；**RCT 次群 OR 4.96（1.67-14.77）— 死亡上升**；VA/VV、CS/CA 皆無效益。

> 兩者**皆不支持常規使用**；ECMO + HP 在高品質 RCT 甚至提示可能有害。

---

# STARDaki — AKI 生物標記報告標準

## Yu H, … Kellum JA, Peng Z, et al. Intensive Care Med 2026｜[doi.org/10.1007/s00134-026-08549-5](https://doi.org/10.1007/s00134-026-08549-5)

- 現有 AKI 生物標記研究異質矛盾：122 篇 DTA 研究僅 19 篇報告 48h 內診斷、16 篇高品質；STARD 遵循度過低而無法 meta-analysis。
- 17 位國際專家 modified Delphi → **STARDaki**（病人選擇、參考標準、test-retest reliability）。

> 未來 AKI 生物標記研究應遵循 STARDaki，提升可比較性與臨床可轉譯性。

---

<!-- _class: divider -->
# 4. 神經重症照護

---

# 顱內壓（ICP）生理、監測與個體化管理

## Taccone FS, Robba C, Meyfroidt G, et al. Intensive Care Med 2026｜[doi.org/10.1007/s00134-026-08558-4](https://doi.org/10.1007/s00134-026-08558-4)

- 預後不僅取決原發損傷，更受**次發性腦損傷（含顱內高壓）**驅動。
- 傳統固定閾值（ICP >22 mmHg）→ 個體耐受度差異大。
- 新概念：**ICP burden、waveform、autoregulation、functional monitoring**；整合 nICP 與 multimodal neuromonitoring；AI 預測次發損傷。

> ICP 管理由「單一閾值」走向「生理導向、個體化」；nICP 於無法侵入監測時有互補價值。

---

# ICH：積極 vs 保守降血壓 — Meta-analysis

## Crit Care Med 2026（8 RCT，n=12,669）｜[doi.org/10.1097/CCM.0000000000007240](https://doi.org/10.1097/CCM.0000000000007240)

| 終點 | RR（積極 vs 保守） |
|------|------|
| 優良功能 | 1.07（0.99-1.16）NS |
| 90 天死亡 | 0.90（0.77-1.05）NS |
| 血腫擴大 | 0.85（0.66-1.10）NS |
| **不良事件** | **0.87（0.76-0.99）p=0.03** |

> 積極降壓**安全**（不良事件更少）但不改善主要功能/死亡；重點在平順降壓、避免波動。

---

<!-- _class: divider -->
# 5. 心跳停止與復甦

---

# 心跳停止後預後判定（排除 WLST 族群）⭐

## Crit Care 2026;30(1)（前瞻多中心，n=101；NCT02231060）｜[doi.org/10.1186/s13054-026-06209-0](https://doi.org/10.1186/s13054-026-06209-0)

- 德國 8 中心，CA 後 72h 仍昏迷、**排除前 4 週 WLST**（避免 self-fulfilling prophecy），追蹤 12 個月 mRS 4-6。
- 指標：PLR+CR、EEG、SEP、NSE、best CRS-R。
- 單一指標高特異度、低敏感度；**≥2 不利指標 → FPR 0、adjusted OR 34.7**。
- **加入 best CRS-R → AUC 0.925 vs 0.888。**

> 避免依賴單一指標；強調重複與組合評估；CRS-R 對「不確定預後」特別有幫助。

---

# 復甦相關短訊（Resuscitation 2026）

## 血流動力學監測 · 按壓位置 · bCPR 差異

- **OHCA 後進階血流動力學監測（scoping review，28 studies）**：CO/MAP 為主；**低 SvO₂、高 PA 壓**與較差預後相關；無單一變數穩定預測。[doi](https://doi.org/10.1016/j.resuscitation.2026.111218)
- **CPR 按壓位置（n=152，TTE）**：指引點與 LVOT 重疊 50%、與 iAMC 僅 2.7% → 生理錯位。[doi](https://doi.org/10.1016/j.resuscitation.2026.111220)
- **鴉片相關 OHCA bCPR 差異（NEMSIS，n=19,612）**：黑人 AOR 0.70、西語裔 0.81、女性 0.89 較少獲 bCPR。[doi](https://doi.org/10.1016/j.resuscitation.2026.111216)

---

<!-- _class: divider -->
# 6. ICU 實務與倫理

---

# ICU 實務與倫理 — Honorable Mentions

## CAVE 護理暴力 · Starting ECMO 倫理 · Bronchiectasis 指引

- **CAVE（ICU 護理攻擊/暴力，Basel 單中心）**：14% 班次發生、75% 為暴力、97% 加害者為病人；復發 27%（首次 aggression OR 6.9、verbal violence OR 4.3）；60% 事件伴病人併發症。[CCM doi](https://doi.org/10.1097/CCM.0000000000007264)
- **Starting ECMO 倫理（Chest review）**：區分 offer vs initiate；知情同意應反覆迭代；不提供時記錄溝通；機構設爭議論壇。[Chest doi](https://doi.org/10.1016/j.chest.2026.07.5210)
- **成人 Bronchiectasis ACCP 指引**：13 條建議，**皆 conditional／low-certainty**；強調 phenotyping 與 shared decision-making。[Chest doi](https://doi.org/10.1016/j.chest.2026.06.057)

---

<!-- _class: ref -->

# 參考文獻 (1/2)

1. Ehrmann S, et al. Prone positioning in ARDS. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08543-x ｜ PMID 42474726
2. Health-economic value of transvenous diaphragm neurostimulation in ventilator weaning. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007262 ｜ PMID 42479503
3. Bünger V, et al. Re-evaluation of oxygenation and oxygen exposure in ARDS and VV-ECMO. *Crit Care* 2026;30(1). https://doi.org/10.1186/s13054-026-06218-z ｜ PMID 42533343
4. Contreras R, et al. Twenty-five years of septic shock hemodynamic resuscitation trials. *Crit Care* 2026;30(1). https://doi.org/10.1186/s13054-026-06201-8 ｜ PMID 42482139
5. Sepsis-related immunosuppression: a comprehensive review. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06168-6 ｜ PMID 42498933
6. Acute PE: clinical and echocardiographic recognition of normotensive shock. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06214-3 ｜ PMID 42502164
7. Jaber S, et al. Sodium bicarbonate in severe metabolic acidemia: IPD meta-analysis (BICAR-ICU + BICAR-ICU2). *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06206-3 ｜ PMID 42472834
8. Intraoperative hemoadsorption and CSA-AKI: updated meta-analysis with TSA. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06099-2 ｜ PMID 42498964
9. Hemoperfusion during ECMO: meta-analysis of 8,151 patients. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06203-6 ｜ PMID 42472846
10. Yu H, et al. STARDaki: STARD extension for AKI diagnostic accuracy. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08549-5 ｜ PMID 42517928

---

<!-- _class: ref -->

# 參考文獻 (2/2)

11. Taccone FS, et al. Intracranial pressure physiology, monitoring and individualized management. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08558-4 ｜ PMID 42525086
12. Aggressive vs conservative BP reduction in acute ICH: systematic review and meta-analysis. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007240 ｜ PMID 42484370
13. Pressure-targeted neurocritical care at the bedside: transcranial Doppler. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06167-7 ｜ PMID 42493813
14. Neuroprognostication after cardiac arrest in patients without WLST. *Crit Care* 2026;30(1). https://doi.org/10.1186/s13054-026-06209-0 ｜ PMID 42509572
15. Advanced hemodynamic monitoring after OHCA: a scoping review. *Resuscitation* 2026. https://doi.org/10.1016/j.resuscitation.2026.111218 ｜ PMID 42492620
16. Where should we compress? Ultrasound identification of iAMC for CPR. *Resuscitation* 2026. https://doi.org/10.1016/j.resuscitation.2026.111220 ｜ PMID 42492621
17. Racial and ethnic differences in bystander CPR for opioid-associated OHCA. *Resuscitation* 2026. https://doi.org/10.1016/j.resuscitation.2026.111216 ｜ PMID 42492622
18. CAVE against nurses in the ICU: epidemiology and risk factors for recurrence. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007264 ｜ PMID 42496194
19. Starting ECMO: ethical issues and recommended approach. *Chest* 2026. https://doi.org/10.1016/j.chest.2026.07.5210 ｜ PMID 42501939
20. Management of adult bronchiectasis: ACCP clinical practice guideline. *Chest* 2026. https://doi.org/10.1016/j.chest.2026.06.057 ｜ PMID 42480819

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

本回顧涵蓋 2026-07-18 ～ 2026-08-01｜資料來源：PubMed
