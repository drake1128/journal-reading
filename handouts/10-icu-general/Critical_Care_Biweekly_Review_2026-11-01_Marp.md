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
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-11-01'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧

## 2026-10-18 ～ 2026-11-01

**謝慕揚 MD, PhD, FESC** | 2026-11-01

涵蓋：ICM、Critical Care、CCM、Chest、Resuscitation、Shock

---

<!-- _class: abbr -->

# 常用縮寫對照（一）

| 縮寫 | 全名 |
|------|------|
| RCT / cRCT | (Cluster) Randomized Controlled Trial 隨機對照試驗 |
| OR / aOR | (Adjusted) Odds Ratio 校正勝算比 |
| HR / sHR | (Subdistribution) Hazard Ratio 風險比 |
| RR / MD | Risk Ratio 風險比 / Mean Difference 平均差 |
| CI | Confidence Interval 信賴區間 |
| AUC / AUROC | Area Under the (ROC) Curve 曲線下面積 |
| GRADE | 證據等級評估系統 |
| ICU / EMS | Intensive Care Unit 加護病房 / Emergency Medical Services |
| SOFA / APACHE | 連續器官衰竭評估 / 急性生理與慢性健康評估 |
| VAP | Ventilator-Associated Pneumonia 呼吸器相關肺炎 |

---

<!-- _class: abbr -->

# 常用縮寫對照（二）

| 縮寫 | 全名 |
|------|------|
| PAA | Pathogen-Appropriate Antifungal 對應病原的抗黴菌藥 |
| CHX | Chlorhexidine 氯己定 |
| SOT / SIC | Solid Organ Transplant 實體器官移植 / Sepsis-Induced Coagulopathy |
| NIV / IMV | Non-Invasive / Invasive Mechanical Ventilation 非侵襲 / 侵襲性通氣 |
| Vt / PBW | Tidal Volume 潮氣量 / Predicted Body Weight 預測體重 |
| P-SILI | Patient Self-Inflicted Lung Injury 病人自發性肺損傷 |
| AKI / KRT | Acute Kidney Injury 急性腎損傷 / Kidney Replacement Therapy |
| FST | Furosemide Stress Test 呋塞米壓力試驗 |
| OHCA / ROSC | Out-of-Hospital Cardiac Arrest / Return of Spontaneous Circulation |
| ACS / ECG | Acute Coronary Syndrome 急性冠心症 / Electrocardiogram 心電圖 |
| MAP / ETCO₂ | Mean Arterial Pressure 平均動脈壓 / End-Tidal CO₂ |

---

<!-- _class: small-text -->

# 重點摘要 Key Pearls（一）

1. **念珠菌敗血性休克**：延遲給對的抗黴菌藥，死亡 aOR **1.045/小時**；2h 內投藥存活 86%，但中位延遲 32.3h、僅 16.9% 在 6h 內投藥 —— **問題是「想不到」**
2. **Chlorhexidine 口腔照護加成防 VAP：negative**（IRR 1.08, p=0.56），死亡率無差異、ICU 反而多住 0.89 天
3. **音樂治療脫機：主要終點陰性**（脫機時間 p=0.97），但躁動／鎮靜改善、**氣切率↓14%（p=0.025）**
4. **NIV 高 Vt/PBW** 與失敗及死亡相關（OR **9.11**）；反映高 respiratory drive 與 P-SILI
5. **FST** 預測 AKI 惡化 (AUC 0.89)、KRT 脫離佳；但 **FST 引導提早 KRT 不降死亡**（RR 1.00）

---

<!-- _class: small-text -->

# 重點摘要 Key Pearls（二）

6. **免疫低下 ICU 內感染**：血液腫瘤 (sHR 1.64)、其他免疫抑制 (sHR 1.61) 風險高；**實體癌不然** (sHR 0.88)
7. **升壓劑下橈動脈壓被低估**：~1/5 病人 brachial-radial 壓差 >11 mmHg，死亡率 48% vs 30%
8. **AI-ECG** 在 post-ROSC 排除 ACS：約半數判為「ACS 不太可能」且零漏判，集中在 non-shockable (AUROC 0.824)
9. **心臟驟停給氣**：即時回饋 (Real BVM Help®) 讓速率＋潮氣量同時達標 7.5%→**39%**；只用 ETCO₂ 常給氣不足 (58.2%)
10. **ESICM 以人為本 ICU 共識**：43 條 —— 彈性探視、結構化溝通、睡眠／譫妄環境、數位科技

---

<!-- _class: divider -->

# 1. Sepsis 與感染

---

# 念珠菌敗血性休克：延遲投藥是最強預後因子

## Abhishek A, et al. Crit Care Med 2026 — https://doi.org/10.1097/CCM.0000000000007395 (PMID 42904906)

- 32 家醫院、**850** 位培養陽性 Candida septic shock（1989–2018 回溯）
- 延遲給 PAA 每多 1 小時：死亡 **aOR 1.045（95% CI 1.035–1.056；p<0.0001）**
- 2 小時內投藥存活 **86%**，之後每小時約掉 5%
- 多變項中「投藥時間」是**最強單一預後預測因子**
- 現實：中位延遲 **32.3 小時**，僅 **16.9%** 在 6h 內拿到對的藥

> 核心訊息不是「要更快」，而是「**要先想到**」——對高風險病人及早考慮經驗性抗黴菌＋source control。

---

# 免疫低下病人 ICU 內感染：依類別分層

## Daltro-Oliveira R, et al. Crit Care Med 2026 — https://doi.org/10.1097/CCM.0000000000007388 (PMID 42895439)

- 巴西 50 家 ICU、**38,126** 人，競爭風險 (Fine-Gray) 分析首次 ICU-acquired infection

| 免疫抑制類別 | sHR (95% CI) |
|------|:---:|
| 血液惡性腫瘤 | **1.64 (1.01–2.65)** ↑ |
| 其他免疫抑制 | **1.61 (1.02–2.54)** ↑ |
| 實體癌 | 0.88 (0.68–1.14) — |

> 感控強度應針對**血液腫瘤與使用免疫抑制劑者**加強；實體癌與非免疫低下無異，不需過度升級。

---

# Sepsis 臨床表型：跨六國 62,458 人

## Shen YY, et al. Shock 2026 — https://doi.org/10.1097/SHK.0000000000002954 (PMID 42954722)

- MIMIC-IV 發現世代 + 5 個外部世代；24 個常規變項、共識分群 → **3 個 profile**

| Profile | 佔比 | 院內死亡 | 特徵 |
|------|:---:|:---:|------|
| 1 | 32.6% | **30.3%** | 多重器官衰竭最重 |
| 2 | 20.0% | 13.8% | 血行動力相對穩定 |
| 3 | 47.4% | 9.3% | 以呼吸支持為主 |

- 校正年齡、SOFA 後 Profile 3 vs 1 的 1 年死亡 HR **0.62（0.57–0.67）**

> 可解釋、跨國可重現的 sepsis 表型；目前為研究工具，尚不改變床邊治療。

---

<!-- _class: divider -->

# 2. Mechanical Ventilation 與呼吸支持

---

# Chlorhexidine 加成防 VAP — Negative 試驗

## Anushapreethi S, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06217-0 (PMID 42958418)

- 印度 6 家內科 ICU、cluster-randomized crossover，**n=1,035**，10,024 ventilator-days
- 標準口腔照護 bundle ± 0.12% chlorhexidine

| 終點 | No CHX | CHX | 效果 |
|------|:---:|:---:|------|
| VAP /1,000 vent-days | 16.9 | 18.8 | IRR **1.08 (0.84–1.38), p=0.56** |
| 28 天死亡 | 28.7% | 26.4% | aOR 0.87, p=0.33 |
| ICU 天數 | — | +0.89 天 | p=0.013（CHX 反而長） |

> 完整 bundle 之上再加 CHX **無額外防 VAP 效益**；重點在口腔照護的落實，而非 CHX 本身。

---

# NIV 的高潮氣量是失敗與死亡警訊

## Santa Cruz R, et al. Crit Care Med 2026 — https://doi.org/10.1097/CCM.0000000000007387 (PMID 42900697)

- 統合分析 11 篇、1,136 位急性呼吸衰竭成人
- NIV 失敗組 **Vt/PBW 較高**（MD +1.02 mL/kg）；**絕對 Vt 無差異** → 必須看 Vt/PBW
- 高 Vt/PBW 與死亡相關 **OR 9.11（3.88–21.37）**、呼吸速率高、PaCO₂ 低、與 PS 無關
- 機轉指向**高 respiratory drive / P-SILI**

> NIV 不是「設好壓力就好」——盯住 Vt/PBW（約 ≤8–9 mL/kg）；若壓力合理但 Vt/PBW 仍高、呼吸快，應考慮及早插管。屬關聯非因果。

---

# 音樂治療脫機：主要陰性、次要正向

## Pereiro S, et al. Crit Care Med 2026 — https://doi.org/10.1097/CCM.0000000000007372 (PMID 42904879)

- 單中心 RCT，**n=100**，每日個別化音樂治療（平均 25 分鐘）vs 標準照護
- **主要終點「脫離呼吸器時間」無差異（p=0.97）**
- 次要：RASS 躁動／鎮靜改善（p=0.048 / 0.005 / 0.024）、propofol 使用↓（p=0.028）
- **氣切率顯著↓ 14%（p=0.025）**；總插管與 ICU 天數較短但未顯著

> 不是縮短脫機的工具，而是減少躁動、鎮靜與人性化照護的**低成本輔助**。勿過度詮釋次要終點。

---

# 機器學習「ARDS 影像分數」獨立預測預後

## Zhong Y, et al. Crit Care Med 2026 — https://doi.org/10.1097/CCM.0000000000007384 (PMID 42919460)

- 單中心、**6,591** 位 IMV 病人；深度學習辨識雙側肺泡浸潤 → ARDS-CXR 分數
- 分數陽性 (17%) 28 天死亡 **35.1% vs 13.5%**；閾值以下仍可分層（−2→0：12.8%→27.5%）
- 預測死亡 AUROC **0.68** > PaO₂/FiO₂ 0.64
- 校正 PaO₂/FiO₂ 或 APACHE-IV 後，分數每 +1 仍與死亡↑、拔管時間↑相關

> 胸片的 ARDS 嚴重度可量化，提供**超越低氧與疾病嚴重度**的預後資訊；單中心回溯，待外部驗證。

---

<!-- _class: divider -->

# 3. AKI / Renal

---

# Furosemide Stress Test：好的分層工具，不是治療

## Tran PNT, et al. Crit Care Med 2026 — https://doi.org/10.1097/CCM.0000000000007392 (PMID 42904937)

- 統合分析 20 篇、1,979 人

| 用途 | Sens | Spec | AUC | GRADE |
|------|:---:|:---:|:---:|:---:|
| 預測 AKI 進展 stage 3 | 0.69 | 0.88 | **0.89** | low |
| 預測需 KRT | 0.81 | 0.75 | 0.79 | very low |
| 成功脫離 KRT | 0.81 | 0.87 | **0.89** | low |

- **FST 引導提早啟動 KRT 對死亡率無效**（RR 1.00；0.79–1.27；2 RCT, n=212）

> 定位：拿不到新型生物標記時的便宜 bedside 分層工具；別當成「提早洗腎能救命」的依據。

---

# 重新思考少尿：從閾值到軌跡

## Tenhunen AB, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06436-5 (PMID 42958591)

- 將 AKI 尿量判準**重新校準**，使各 stage 尿量閾值對應 creatinine-stage 推導的死亡率
- 現行 KDIGO 尿量判準（<0.5 mL/kg/h × 6–12h）為歷史沿用、非預後校準
- 評論（Honoré PM, et al. *Crit Care Med* 2026, PMID 42904903）：少尿的意義在**趨勢與對 fluid challenge 的反應**

> 解讀少尿看趨勢與治療反應，而非死守單一切點；尿量判準未來可能依 stage 重新校準。

---

<!-- _class: divider -->

# 4. Resuscitation 與心臟驟停

---

# AI-ECG 決策樹：post-ROSC 排除 ACS

## Choi A, et al. Resuscitation 2026 — https://doi.org/10.1016/j.resuscitation.2026.111373 (PMID 42956925)

- 單中心，OHCA 成人；發展 (n=329)＋驗證 (n=71)；深度學習 ECG 生物標記建規則式決策樹，**零偽陰性約束**
- 將 **52.0% / 45.1%** 判為「ACS 不太可能」，**無任何經判定 ACS 漏判**
- 效益集中在 **non-shockable**：排除 64.8% 非 ACS（AUROC 0.824）
- shockable（高前測機率）：95.0% 仍保留為「未排除 ACS」

> 或可安全排除約半數 post-ROSC 病人的 ACS 病因、減少不必要緊急冠狀動脈攝影；待前瞻多中心驗證。

---

# 心臟驟停給氣：即時回饋 > 只看 ETCO₂

## Aufderheide TP, et al. Resuscitation 2026 — https://doi.org/10.1016/j.resuscitation.2026.111372 (PMID 42956924)

- 威斯康辛州 EMS 成人 OHCA、before/after，**n=278**；Real BVM Help® 即時回饋

| 達標比例 | Before (ETCO₂) | After (回饋) | p |
|------|:---:|:---:|:---:|
| 速率 | 47.7% | **74.4%** | <0.0001 |
| 潮氣量 | 15.3% | **45.4%** | <0.0001 |
| 速率＋潮氣量 | 7.5% | **39.0%** | <0.0001 |

- 只用 ETCO₂（22,037 次給氣）：最常見錯誤是**給氣量不足（58.2% 偏低）**

> CPR 徒手給氣極難達標；應導入**速率＋潮氣量的即時回饋**。

---

<!-- _class: divider -->

# 5. Hemodynamics 與監測

---

# 升壓劑下 Brachial-to-Radial 壓力差

## Putowski Z, et al. Crit Care Med 2026 — https://doi.org/10.1097/CCM.0000000000007391 (PMID 42919451)

- 波蘭 13 家 ICU、前瞻觀察，**303** 位用 vasoactive 藥物成人
- 中位 brachial-radial 壓差 4.5 mmHg；**18.4% >11 mmHg**（臨床顯著）
- 顯著壓差者：升壓劑劑量↑（0.23 vs 0.10 µg/kg/min）、lactate↑（2.7 vs 1.3）、SOFA↑
- 多變項中僅**升壓劑劑量**獨立相關（OR 1.68；1.12–2.52）
- **ICU 死亡率 48.0% vs 30.1%**

> 高劑量升壓劑下，約 1/5 病人橈動脈 MAP 低於上臂；別據橈動脈讀值一味加壓，必要時用上臂交叉比對或更中央監測。

---

<!-- _class: divider -->

# 6. ICU 復健、組織與藥學

---

# 重症康復者肌肉「合成能力」其實保留

## Fischer-Hammerschmied A, et al. Crit Care 2026 — https://doi.org/10.1186/s13054-026-06418-7 (PMID 42934773)

- 前瞻機轉研究，20 位 ICU 出院 3–6 個月康復者 vs 20 配對對照；阻力運動＋24g 蛋白後測肌肉蛋白合成率
- 康復者肌肉較薄、握力較低；**基礎合成率反而較高**（0.041 vs 0.030 %/hr）
- 介入後合成率**兩組相當**（0.071 vs 0.070 %/hr）；兩組皆提升合成訊號、降低 autophagy

> 康復者對「阻力運動＋蛋白質」仍有良好合成反應——支持結構化**運動-營養復健**促進肌肉恢復的首個機轉證據。

---

# ESICM「以人為本 ICU 夥伴關係」共識 ＋ 肥胖用藥

## Latour JM, et al. ICM 2026 (PMID 42931902) ／ Barletta JF, et al. ICM 2026 (PMID 42911397)

**ESICM 共識（43 條）** — https://doi.org/10.1007/s00134-026-08626-9
- 六領域：以人為本照護、溝通透明、情緒福祉、公平共融、ICU 環境、科技創新
- 彈性探視、結構化跨團隊溝通、同理心訓練、病人與醫護心理支持、睡眠／譫妄環境、數位科技

**肥胖重症用藥原則** — https://doi.org/10.1007/s00134-026-08628-7
- 仿單劑量多未納入肥胖 PK/PD 變異；**選對計算體重**是達標關鍵；個別化、善用臨床藥師

---

<!-- _class: divider -->

# 7. 其他值得關注

---

<!-- _class: small-text -->

# Honorable Mentions

- **Cluster vs Individual 隨機化**（Lønstrup S, et al. *Crit Care Med* 2026, PMID 42904944）：65 篇統合分析、315,276 人。死亡率無系統差異，但住院天數類終點 cRCT 效果量較小；<半數統合分析標明隨機化型態。
- **SIC 扭曲 HALP 分數**（Dong X, et al. *Shock* 2026, PMID 42954754）：MIMIC-IV 6,218 人；HALP 在無 SIC 者獨立預測死亡，SIC 者被削弱（interaction p=0.006）；建議先評估凝血狀態，或改用 m-HALP。
- **Sepsis 粒線體功能障礙驅動血小板活化**（Greco E, et al. *Crit Care Med* 2026, PMID 42925135）：體外研究；MitoTEMPO 可逆轉，為「以粒線體為標的」預防器官損傷提供假說。

---

<!-- _class: ref -->

# 參考文獻（一）

1. Abhishek A, et al. Delay to Appropriate Antifungal in Candida Septic Shock. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007395 (PMID 42904906)
2. Gupta S, Rhee C, Klompas M. Candida Septic Shock: Who Requires Empiric Therapy? *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007411 (PMID 42951887)
3. Daltro-Oliveira R, et al. ICU-Acquired Infections in Immunosuppressed Patients. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007388 (PMID 42895439)
4. Shen YY, et al. Consensus-derived Clinical Sepsis Profiles. *Shock* 2026. https://doi.org/10.1097/SHK.0000000000002954 (PMID 42954722)
5. Witowski A, et al. Immunological Signatures of Sepsis in Abdominal SOT. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08612-1 (PMID 42955323)
6. Anushapreethi S, et al. Chlorhexidine Oral-Care Bundle for VAP. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06217-0 (PMID 42958418)
7. Santa Cruz R, et al. Tidal Volume During NIV: Meta-Analysis. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007387 (PMID 42900697)
8. Mavignier N, Mauri T. Excessive Tidal Volume During NIV. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007410 (PMID 42957594)
9. Pereiro S, et al. Music Therapy During Weaning: RCT. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007372 (PMID 42904879)
10. Zhong Y, et al. ML ARDS Radiographic Findings & Outcomes. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007384 (PMID 42919460)
11. Tran PNT, et al. Furosemide Stress Test in AKI: Meta-Analysis. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007392 (PMID 42904937)

---

<!-- _class: ref -->

# 參考文獻（二）

12. Tenhunen AB, et al. Recalibrating Urine Output Criteria for AKI. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06436-5 (PMID 42958591)
13. Honoré PM, et al. Rethinking Oliguria: From Threshold to Trajectory. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007399 (PMID 42904903)
14. Choi A, et al. AI-ECG Decision Tree to Exclude ACS After OHCA. *Resuscitation* 2026. https://doi.org/10.1016/j.resuscitation.2026.111373 (PMID 42956925)
15. Aufderheide TP, et al. Ventilation Monitoring in OHCA. *Resuscitation* 2026. https://doi.org/10.1016/j.resuscitation.2026.111372 (PMID 42956924)
16. Putowski Z, et al. Brachial-to-Radial Pressure Gradient on Vasoactives. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007391 (PMID 42919451)
17. Fischer-Hammerschmied A, et al. Anabolic Muscle Capacity After Critical Illness. *Crit Care* 2026. https://doi.org/10.1186/s13054-026-06418-7 (PMID 42934773)
18. Latour JM, et al. ESICM Consensus: Human-Centred Partnership in the ICU. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08626-9 (PMID 42931902)
19. Barletta JF, Erstad BL. Drug Dosing for Obese ICU Patients. *Intensive Care Med* 2026. https://doi.org/10.1007/s00134-026-08628-7 (PMID 42911397)
20. Lønstrup S, et al. Cluster vs Individual Randomization. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007386 (PMID 42904944)
21. Dong X, et al. SIC Attenuates HALP Score in Sepsis. *Shock* 2026. https://doi.org/10.1097/SHK.0000000000002956 (PMID 42954754)
22. Greco E, et al. Mitochondrial Impairment in Sepsis-Induced Platelet Activation. *Crit Care Med* 2026. https://doi.org/10.1097/CCM.0000000000007407 (PMID 42925135)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

Critical Care 雙週期刊回顧 | 2026-11-01
