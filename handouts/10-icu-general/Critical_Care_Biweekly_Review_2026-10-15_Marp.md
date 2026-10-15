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
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-10-15'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧

## 2026-10-02 ～ 2026-10-15（過去 14 天）

**整理：謝慕揚 MD, PhD, FESC**

涵蓋：Resuscitation · Critical Care · CCM · Chest · ICM · Shock

---

<!-- _class: abbr -->

# 縮寫對照 (1/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| RCT | Randomized Controlled Trial | 隨機對照試驗 |
| RR / HR / OR | Risk / Hazard / Odds Ratio | 風險比／風險比／勝算比 |
| aOR / aHR | adjusted OR / HR | 校正勝算比／風險比 |
| CI / CrI | Confidence / Credible Interval | 信賴區間／後驗信賴區間 |
| LCA | Latent Class Analysis | 潛在類別分析 |
| CPR | Cardiopulmonary Resuscitation | 心肺復甦術 |
| OHCA | Out-of-Hospital Cardiac Arrest | 院外心臟驟停 |
| ROSC | Return of Spontaneous Circulation | 自發循環恢復 |
| ECPR | Extracorporeal CPR | 體外心肺復甦 |
| PEA | Pulseless Electrical Activity | 無脈搏電氣活動 |
| MV / BV | Mechanical Ventilation / Bag-Valve | 機械通氣／徒手甦醒球 |

---

<!-- _class: abbr -->

# 縮寫對照 (2/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| ARF | Acute Respiratory Failure | 急性呼吸衰竭 |
| NIRS / NIV | Noninvasive Respiratory Support / Ventilation | 非侵襲呼吸支持／通氣 |
| HFNC / COT | High-Flow Nasal Cannula / Conventional O₂ | 高流量鼻管／傳統氧療 |
| HFCWO | High-Frequency Chest Wall Oscillation | 高頻胸壁震盪 |
| PPC / VATS | Postop Pulmonary Complication / VA Thoracoscopy | 術後肺併發症／胸腔鏡手術 |
| NPi / QPi | Neurological / Quantitative Pupil Index | 神經／量化瞳孔指數 |
| AKI / CKD | Acute Kidney Injury / Chronic Kidney Disease | 急性腎損傷／慢性腎臟病 |
| LMD | Lowest Mean Diuresis | 最低平均尿量 |
| CS / VA ECMO | Cardiogenic Shock / Venoarterial ECMO | 心因性休克／靜脈-動脈體外膜氧合 |
| PICS(-F) | Post-Intensive Care Syndrome (-Family) | 重症後症候群（家屬型） |
| ITD / ACD | Impedance Threshold Device / Active Compression-Decompression | 阻抗閾值裝置／主動壓胸-減壓 |

---

<!-- _class: small-text -->

# 本期 10 大重點 (Key Pearls) — 1/2

1. **CPR 用機械式呼吸 vs 徒手 bag-valve**：Bayesian MA（6,847 人）ROSC RR **1.20**，益處機率 99%；存活/神經學仍不精確。
2. **OHCA 不可電擊→可電擊後給 amiodarone**：德國登錄配對，出院存活 **6.5% vs 4.2%（OR 1.58）**；神經學預後未顯著。
3. **ECPR 節律惡化成 asystole**：良好神經學預後 **RR 0.20**；節律改善 RR 3.12。
4. **Post-ROSC 實驗室表型（LCA）**：MOD / HOM / IMD 三型，HOM、IMD 死亡與不良預後較 MOD 低。
5. **肺切除術後預防性 HFNC**：中-重度 PPC **23.1% vs 39.6%**（OR 0.50）；不建議全面常規化。

---

<!-- _class: small-text -->

# 本期 10 大重點 (Key Pearls) — 2/2

6. **ARF 痰液滯留的 HFCWO**：支氣管鏡需求校正後 **OR 0.336（p=0.055，不顯著）**；住院縮短屬探索性。
7. **ABI 自動瞳孔量測**：NPi 與 QPi 相關 r=0.717，但 **QPi 對 propofol 敏感**，鎮靜病人兩者不可互換。
8. **少尿閾值**：死亡/CKD 的風險在 **比 0.5 mL/kg/hr 更低**的尿量即上升。
9. **VA ECMO 累積 inotrope 暴露越高**：脫機失敗、30 天死亡、心律不整皆增加（HR ~1.04）。
10. **敗血症存活者家屬 PICS-F**：12 個月仍 42% 不退，與病人「心理」PICS 最相關（aOR 3.71）。

---

<!-- _class: divider -->

# 1. 心臟驟停與復甦
## Resuscitation

---

# CPR：機械式呼吸 vs 徒手 bag-valve（Bayesian MA）

## Chu YQ, et al. *Resuscitation* 2026 — [doi.org/10.1016/j.resuscitation.2026.111345](https://doi.org/10.1016/j.resuscitation.2026.111345) · PMID 42863592

- 8 篇研究、**6,847 人**；CPR 期間任一時間用機械通氣 (MV) vs 徒手 bag-valve (BV)

| 終點 | 結果 | 後驗機率 |
|------|------|----------|
| ROSC | **RR 1.20（95% CrI 1.04–1.42）** | 99% |
| 存活入院 | 方向有利 MV | 92.3% |
| 出院存活 | 方向有利 MV | 93.6% |
| 良好神經學 | 方向有利 MV | 92.2% |
| 氣胸 | 兩組相當 | — |

> 皆為觀察性資料統合，殘餘干擾無法排除；指引仍未建議以 MV 取代 BV。重點：避免過度通氣。

---

# OHCA：不可電擊→可電擊後給 amiodarone

## Knapp J, et al. *Resuscitation* 2026 — [doi.org/10.1016/j.resuscitation.2026.111349](https://doi.org/10.1016/j.resuscitation.2026.111349) · PMID 42838501

- German Resuscitation Registry；初始不可電擊、之後≥2 次去顫；傾向分數配對（各 1,843）

| 終點 | amiodarone | 無 | OR |
|------|-----------|----|----|
| 帶 ROSC 入院 | 26.7% | 23.0% | 1.22 |
| 24h 存活 | 21.4% | 14.7% | 1.58 |
| **出院存活** | **6.5%** | **4.2%** | **1.58** |
| 良好神經學 | 3.7% | 2.9% | 1.31 (NS) |

> 短期與出院存活較高，但神經學預後未達顯著；觀察性資料，給藥時機待前瞻驗證。

---

# ECPR：節律動態的預後意義（統合分析）

## Marabotti A, et al. *Resuscitation* 2026 — [doi.org/10.1016/j.resuscitation.2026.111348](https://doi.org/10.1016/j.resuscitation.2026.111348) · PMID 42838500

- 10 篇觀察研究、**5,183 人**；OHCA 接受 ECPR

| 節律變化 | 良好神經學預後 | GRADE |
|----------|----------------|-------|
| 改善（不可電擊→可電擊） | **RR 3.12（1.26–7.74）** | Low |
| 惡化（可電擊→不可電擊） | **RR 0.41（0.21–0.80）** | Moderate |
| 惡化成 **asystole** | **RR 0.20（0.09–0.45）** | Moderate |
| 惡化成 PEA | RR 0.62（0.31–1.25，NS） | Low |

> 初始節律以外，CPR 過程「往 asystole 走」是強烈不良訊號，可納入上機決策。

---

# Post-ROSC 早期實驗室表型（LCA）

## Liu X, et al. *Resuscitation* 2026 — [doi.org/10.1016/j.resuscitation.2026.111351](https://doi.org/10.1016/j.resuscitation.2026.111351) · PMID 42855036

- 新加坡全國世代（2011–2022），n=**1,514**；ROSC 後 6h 內 14 項實驗室變項做潛在類別分析

| 表型 | n | vs MOD 不良神經學 | 30 天死亡 |
|------|---|-------------------|-----------|
| MOD（多器官障礙） | 286 | 參考 | 參考 |
| HOM（恆定） | 967 | aOR 0.50 | aHR 0.71 |
| IMD（免疫失調） | 261 | aOR 0.46 | aHR 0.78 |

> 最具鑑別力：creatinine、eosinophil、lymphocyte。探索性，待外部驗證與表型導向治療研究。

---

<!-- _class: divider -->

# 2. Mechanical Ventilation
## 與呼吸支持

---

# 肺切除術後預防性 HFNC（RCT）

## Lin R, et al. *Crit Care* 2026;30(1) — [doi.org/10.1186/s13054-026-06205-4](https://doi.org/10.1186/s13054-026-06205-4) · PMID 42864673

- 單中心、開放標籤 RCT；VATS 肺葉／肺節切除之老年 NSCLC；n=**210**
- 介入：拔管後預防性 **HFNC** vs 傳統氧療 (COT)

| 終點 | 結果 |
|------|------|
| PPC 嚴重度 | **ordinal OR 0.50（0.28–0.91，p=0.022）** |
| 中-重度 PPC | **23.1% vs 39.6%（差 −15.6%，p=0.010）** |
| 住院天數 | 無差異 |

> 作者強調**不支持對「所有」肺切除病人常規使用**；宜用於較年長／高風險者。

---

# ARF 痰液滯留：高頻胸壁震盪（HFCWO）

## Ielo S, et al. *Chest* 2026 — [doi.org/10.1016/j.chest.2026.10.007](https://doi.org/10.1016/j.chest.2026.10.007) · PMID 42874912

- 單中心 RCT；ARF 需 NIRS、痰多且咳嗽無效（peak cough flow <270 L/min）；n=**88**

| 終點 | 結果 |
|------|------|
| 治療性支氣管鏡（未校正） | 13.6% vs 31.8%（p=0.042） |
| 支氣管鏡（**校正後**） | **OR 0.336（p=0.055）→ 不顯著** |
| 住院日 / RICU 日 / HFNC 天數 | 縮短（探索性） |
| 插管 / 死亡 | 無差異 |

> 主要終點校正後**未達顯著**；次要益處為 hypothesis-generating，勿據單一小型試驗改變常規。

---

<!-- _class: divider -->

# 3. 神經重症
## Neurocritical Care

---

# LYNX：NPi 與 QPi 不可互換

## Bouzat P, et al. *Crit Care* 2026;30(1) — [doi.org/10.1186/s13054-026-06360-8](https://doi.org/10.1186/s13054-026-06360-8) · PMID 42839269

- 三家歐洲 ICU 前瞻世代；ABI（TBI／出血／缺血性中風）通氣 >12h；n=**108**，7,089 對量測

- NPi 與 QPi **中-強相關 r=0.717**；兩者皆預測 6 個月不良預後（NPi OR 1.49；QPi OR 1.76）
- **QPi 與顱內高壓相關（OR 1.38），NPi 則否**
- **propofol 使 QPi 中位降至 1（NPi 僅降至 4.0）** → QPi 對麻醉藥遠較敏感

> 鎮靜病人兩指標不可互換；QPi 異常未必代表顱內壓升高，須結合臨床與 multimodal 監測。

---

<!-- _class: divider -->

# 4. AKI / Renal

---

# 少尿的最佳閾值 — 重新檢視 0.5 mL/kg/hr

## Mossberg R, et al. *Crit Care Med* 2026 — [doi.org/10.1097/CCM.0000000000007370](https://doi.org/10.1097/CCM.0000000000007370) · PMID 42872921

- 瑞典單中心回顧（2017–2024），無既存 CKD 之成人 ICU；n=**4,999**
- 計算 3/6/12/24h 最低平均尿量 (LMD)

| 對應結局 | LMD 閾值範圍 (mL/kg/hr) |
|----------|-------------------------|
| AKI | 0.41 – 0.53 |
| incident CKD | 0.21 – 0.43 |
| 90 天死亡 | 0.16 – 0.39 |

> 死亡與持續性腎損傷的風險在**比現行 AKI 定義更低的尿量**即上升；支持重新檢視 AKI 定義（單中心、回顧性）。

---

<!-- _class: divider -->

# 5. 血流動力學與循環支持
## Hemodynamics

---

# VA ECMO：累積 inotrope 暴露與脫機失敗

## van Steenwijk MPJ, et al. *Crit Care Med* 2026 — [doi.org/10.1097/CCM.0000000000007338](https://doi.org/10.1097/CCM.0000000000007338) · PMID 42809661

- 荷蘭 6 中心（2018–2024），嚴重 CS 接受 VA ECMO；n=**440**；joint modeling

| 終點（累積 inotrope 每單位） | HR |
|------------------------------|----|
| ECMO 脫機失敗 | 1.04（1.00–1.07） |
| 30 天死亡 | 1.04（1.01–1.08） |
| 心律不整 | 1.05（1.01–1.08） |
| 乳酸清除較慢 | 0.96（0.92–0.99） |

> VA ECMO 下器官灌流已由機器提供，持續高劑量 inotrope 效益可能不敵心肌氧耗與心律不整；許可下應考慮積極減量（觀察性）。

---

# 以保險申報資料定義心因性休克

## Choi KH, et al. *Crit Care Med* 2026 — [doi.org/10.1097/CCM.0000000000007380](https://doi.org/10.1097/CCM.0000000000007380) · PMID 42831735

- 兩臨床世代對照韓國全國健保；演算法 = ICD-10 R57.0／心臟碼 + 治療條件（機械循環支持或血管活性藥）
- CICU 世代 **sensitivity 0.89、specificity 0.90**；RESCUE sensitivity 0.95
- 全國辨識 207,419 人；累積死亡 12 個月 37.9%、5 年 49.9%、10 年 61.7%

> 「診斷碼 + 治療條件」演算法可用既有行政資料做系統層級 CS 照護品質評估與長期追蹤。

---

<!-- _class: divider -->

# 6. ICU 存活與家屬
## Survivorship & Family

---

# 敗血症存活者家屬的長期 PICS-F

## Shirasaki K, et al. *Crit Care Med* 2026 — [doi.org/10.1097/CCM.0000000000007378](https://doi.org/10.1097/CCM.0000000000007378) · PMID 42872916

- 日本 21 ICU 前瞻多中心；94 對照顧者-病人；3/6/12 個月追蹤

| 指標 | 3 個月 | 12 個月 |
|------|--------|---------|
| 家屬 **PICS-F** | 43% | 42%（不退） |
| 病人 PICS 症狀 | 82% | 62%（下降） |

- 病人有 PICS → 家屬 PICS-F **aOR 3.00**；僅病人「**心理** PICS」相關（aOR 3.71）

> ICU 後追蹤不應只顧病人；敗血症存活者家屬的心理後遺症長期不退，應納入支持。

---

# 種族／族裔與 ICU 存活者身體功能障礙

## Watson MA, et al. *Crit Care Med* 2026 — [doi.org/10.1097/CCM.0000000000007373](https://doi.org/10.1097/CCM.0000000000007373) · PMID 42841714

- 單一學術中心回顧；休克／呼吸衰竭／ECMO 之 ICU 存活者；n=**4,370**；31% 出院時有身體障礙

| 族群 | 結果 | aOR |
|------|------|-----|
| 非西班牙裔黑人 | 任何功能障礙 | 1.34（1.04–1.72） |
| 西班牙裔 | 新發功能障礙 | 1.42（1.05–1.91） |

> 有障礙者 1 年內醫療利用風險皆較高；提醒關注 post-ICU 復健的公平性（單中心、回顧性）。

---

<!-- _class: divider -->

# 7. 其他值得關注
## Honorable Mentions

---

<!-- _class: small-text -->

# 其他焦點 (1/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| **Tigris 十問**（PMX 血液吸附） | 研究者自評 Bayesian 設計、先驗、族群富集之優缺；謹慎外推 | [doi](https://doi.org/10.1186/s13054-026-06219-y) · PMID 42839288 |
| **敗血症微循環監測**（Review） | 大循環達標 ≠ 微循環一致；量測高度異質，僅為補充框架 | [doi](https://doi.org/10.1186/s13054-026-06353-7) · PMID 42839239 |
| **OHCA 阻抗閾值裝置 (ITD)** | ROSC 較高（aOR 1.09）但**出院存活反而較低（aOR 0.68）**；選擇偏差 | [doi](https://doi.org/10.1016/j.resuscitation.2026.111340) · PMID 42849561 |
| **鴉片類相關 OHCA** | 整體與預後無關聯（OR 1.02）；Utstein 變項關係兩群不同 | [doi](https://doi.org/10.1016/j.resuscitation.2026.111352) · PMID 42855034 |

---

<!-- _class: small-text -->

# 其他焦點 (2/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| **院前優先後送選擇偏差**（AIPW） | 風險差呈 U 形、受現場時間調節；因果推論的方法學提醒 | [doi](https://doi.org/10.1186/s13054-026-06196-2) · PMID 42850620 |
| **戰場安寧／臨終照護**（Scoping） | 疼痛處置文獻最多（ketamine、經黏膜 fentanyl）；安寧準則缺口 | [doi](https://doi.org/10.1186/s13054-026-06359-1) · PMID 42844637 |
| **sTNFR1 × 糖尿病/ASCVD** | 共病削弱 sTNFR1 與敗血症死亡的關聯（交互作用 p<0.001） | [doi](https://doi.org/10.1097/CCM.0000000000007374) · PMID 42813914 |

---

<!-- _class: ref -->

# 參考文獻 (1/2)

1. Chu YQ, et al. Mechanical vs manual bag-valve ventilation during CPR: Bayesian meta-analysis. [*Resuscitation*. 2026;111345.](https://doi.org/10.1016/j.resuscitation.2026.111345) PMID 42863592.
2. Knapp J, et al. Amiodarone after conversion from non-shockable to shockable rhythm in OHCA. [*Resuscitation*. 2026;111349.](https://doi.org/10.1016/j.resuscitation.2026.111349) PMID 42838501.
3. Marabotti A, et al. Cardiac rhythm dynamics during CPR and outcomes in ECPR. [*Resuscitation*. 2026;111348.](https://doi.org/10.1016/j.resuscitation.2026.111348) PMID 42838500.
4. Liu X, et al. Early post-ROSC laboratory phenotypes after OHCA. [*Resuscitation*. 2026;111351.](https://doi.org/10.1016/j.resuscitation.2026.111351) PMID 42855036.
5. Lin R, et al. Prophylactic HFNC vs conventional oxygen for postoperative respiratory complications. [*Crit Care*. 2026;30(1).](https://doi.org/10.1186/s13054-026-06205-4) PMID 42864673.
6. Ielo S, et al. High-frequency chest wall oscillation in ARF with bronchial hypersecretion: RCT. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.10.007) PMID 42874912.
7. Bouzat P, et al. NPi vs QPi automated pupillometry in acute brain injury (LYNX). [*Crit Care*. 2026;30(1).](https://doi.org/10.1186/s13054-026-06360-8) PMID 42839269.
8. Mossberg R, et al. Oliguria thresholds for AKI, CKD, and mortality. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007370) PMID 42872921.
9. van Steenwijk MPJ, et al. Inotropic exposure during VA ECMO and weaning failure. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007338) PMID 42809661.
10. Choi KH, et al. Claims-based operational definition of cardiogenic shock. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007380) PMID 42831735.

---

<!-- _class: ref -->

# 參考文獻 (2/2)

11. Shirasaki K, et al. Long-lasting mental disorders in caregivers of ICU sepsis survivors (PICS-F). [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007378) PMID 42872916.
12. Watson MA, et al. Race and ethnicity and physical impairment among ICU survivors. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007373) PMID 42841714.
13. Legrand M, et al. Polymyxin B hemoadsorption in endotoxic septic shock: ten questions on Tigris. [*Crit Care*. 2026;30(1).](https://doi.org/10.1186/s13054-026-06219-y) PMID 42839288.
14. Yin X, et al. Multimodal microcirculatory and organ perfusion monitoring in sepsis. [*Crit Care*. 2026;30(1).](https://doi.org/10.1186/s13054-026-06353-7) PMID 42839239.
15. Weidman AC, et al. Impedance threshold device use during OHCA. [*Resuscitation*. 2026;111340.](https://doi.org/10.1016/j.resuscitation.2026.111340) PMID 42849561.
16. Mok V, et al. Opioid-associated vs undifferentiated OHCA. [*Resuscitation*. 2026;111352.](https://doi.org/10.1016/j.resuscitation.2026.111352) PMID 42855034.
17. Kubo A, et al. Prehospital transport prioritization and time-varying selection bias. [*Crit Care*. 2026;30(1).](https://doi.org/10.1186/s13054-026-06196-2) PMID 42850620.
18. Matray C, et al. Palliative and end-of-life care on the battlefield: scoping review. [*Crit Care*. 2026;30(1).](https://doi.org/10.1186/s13054-026-06359-1) PMID 42844637.
19. Gaulton TG, et al. Diabetes/ASCVD modify sTNFR1–sepsis mortality association. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007374) PMID 42813914.

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**整理：謝慕揚 MD, PhD, FESC**

Critical Care 雙週期刊回顧 · 2026-10-15
