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
    font-size: 22px;
    padding: 40px 50px;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 1.8em; }
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
    font-size: 2.2em;
    text-align: center;
  }
  section.divider h2 {
    color: #ffffff;
    font-size: 1.1em;
    text-align: center;
  }
  section.divider h3 {
    color: #ffe066;
    font-size: 0.95em;
    text-align: center;
  }
  h1 { color: #ba181b; border-bottom: 2px solid #ba181b; padding-bottom: 0.15em; font-size: 1.35em; margin-bottom: 0.3em; margin-top: 0; }
  h2 { color: #0072bc; font-size: 0.85em; margin: 0.25em 0; font-weight: normal; }
  h3 { color: #555555; font-size: 0.95em; margin: 0.4em 0 0.3em 0; }
  p { margin: 0.35em 0; }
  table { font-size: 0.78em; width: 100%; margin: 0.4em 0; border-collapse: collapse; }
  th { background-color: #0072bc; color: white; padding: 4px 7px; }
  td { padding: 3px 7px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.4em 0.9em;
    font-size: 0.85em;
    margin: 0.4em 0;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 6px;
    padding: 0.5em;
    font-size: 0.7em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 1px 5px; border-radius: 4px; font-size: 0.88em; }
  strong { color: #ba181b; }
  a { color: #0072bc; text-decoration: underline; }
  footer { color: #787878; font-size: 0.5em; }
  ul, ol { font-size: 0.92em; margin: 0.3em 0; padding-left: 1.4em; }
  li { margin: 0.15em 0; }
  section.small-text { font-size: 19px; }
  section.small-text table { font-size: 0.72em; }
  section.ref { font-size: 17px; }
  section.ref ol { font-size: 1em; }
  section.ref li { margin: 0.2em 0; }
  section.abbr { font-size: 18px; }
  section.abbr table { font-size: 0.82em; }
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review 2026-06-01 | 讀書會共筆'
---

<!-- _class: lead -->

# Critical Care 雙週期刊回顧
## Biweekly Critical Care Literature Review

**2026-05-18 ～ 2026-06-01**

讀書會共筆整理人：謝慕揚 MD, PhD, FESC

涵蓋：ICM ｜ Critical Care ｜ CCM ｜ AJRCCM ｜ Lancet Respir Med ｜ Chest ｜ Ann Intensive Care

[👉 完整講義連結 (GitHub)](https://github.com/drake1128/journal-reading/blob/master/handouts/10-icu-general/Critical_Care_Biweekly_Review_2026-06-01%20%E6%95%99%E5%AD%B8%E8%AC%9B%E7%BE%A9.md)

---

<!-- _class: small-text -->

# 本期十大重點 (Top 10 Pearls)

1. **ARDS 表型 × 驅動壓** — Hypoinflammatory 型對高 ΔP 更脆弱（aHR 2.01 vs 1.46）
2. **坐椅位 RCT** — 自主呼吸 ICU 病人，P/F 改善 +13 mmHg（臥位 −13）
3. **限制性液體 × AKI 分期** — Stage 1 獲益；Stage 2-3 有害（RR 1.20）
4. **POMPAE 陰性** — 目標鎂 1.5-2.0 mmol/L 無法預防 POAF（RR 1.29）
5. **TLR4 磷酸化 Sepsis Endotype** — 高活化亞群 Day 4 HR 2.77
6. **NaHCO₃ Meta-Analysis** — 確定性降低 RRT（RR 0.69）；死亡率 Bayesian 90.4%
7. **VV-ECMO 升級** — 4.7% 需升級；院內死亡 47.9%；VA 升級 OR 3.44 存活佳
8. **MINT 亞分析** — AMI + 重症：限制性輸血趨勢較差（RR 1.24）
9. **俯臥位回落** — 疫情中 51.9% → 疫情後 25.6%（疫情前 11.0%）
10. **長期重症代謝** — Day 10 能量峰值後下降；三種代謝軌跡亞型

---

<!-- _class: abbr -->

# 常用縮寫對照（一）

| 縮寫 | 全名 | 中文 |
|------|------|------|
| ARDS | Acute Respiratory Distress Syndrome | 急性呼吸窘迫症候群 |
| ΔP | Driving Pressure | 驅動壓 |
| PLDyn | Dynamic Transpulmonary Driving Pressure | 動態跨肺驅動壓 |
| PEEP | Positive End-Expiratory Pressure | 呼氣末正壓 |
| PSV | Pressure Support Ventilation | 壓力支持通氣 |
| SBT | Spontaneous Breathing Trial | 自主呼吸測試 |
| EIT | Electrical Impedance Tomography | 電阻抗層析成像 |
| EFI | EIT-derived Flow Index | 電阻抗衍生流量指數 |
| P/F ratio | PaO₂/FiO₂ ratio | 氧合指數 |
| HFNC | High-Flow Nasal Cannula | 高流量鼻管氧療 |
| NIV | Non-Invasive Ventilation | 非侵襲性通氣 |
| Pmus | Inspiratory Muscle Pressure | 吸氣肌壓 |
| EE | Energy Expenditure | 能量消耗 |
| RQ | Respiratory Quotient | 呼吸商 |

---

<!-- _class: abbr -->

# 常用縮寫對照（二）

| 縮寫 | 全名 | 中文 |
|------|------|------|
| TLR4 | Toll-like Receptor 4 | 類鐸受體 4 |
| SOFA | Sequential Organ Failure Assessment | 連續器官衰竭評估 |
| TTE | Transthoracic Echocardiography | 經胸超音波心動圖 |
| MAP | Mean Arterial Pressure | 平均動脈壓 |
| NEE | Norepinephrine Equivalent | 正腎上腺素等效劑量 |
| HSI | Hyperspectral Imaging | 高光譜成像 |
| AKI | Acute Kidney Injury | 急性腎損傷 |
| RRT | Renal Replacement Therapy | 腎臟替代療法 |
| NaHCO₃ | Sodium Bicarbonate | 碳酸氫鈉 |
| TSA | Trial Sequential Analysis | 試驗序列分析 |
| POAF | Post-Operative Atrial Fibrillation | 術後心房顫動 |
| AMI | Acute Myocardial Infarction | 急性心肌梗塞 |
| VV-ECMO | Veno-Venous Extracorporeal Membrane Oxygenation | 靜脈-靜脈體外膜氧合 |
| ICP | Intracranial Pressure | 顱內壓 |

---

<!-- _class: divider -->

# ARDS 與機械通氣
## Acute Respiratory Distress Syndrome & Mechanical Ventilation

---

# ARDS 炎症表型決定 Lung-Protective Ventilation 的獲益
## [Pensier J et al. *Lancet Respir Med* 2026-05-19](https://doi.org/10.1016/S2213-2600(26)00045-7) | [PMID 42155495](https://pubmed.ncbi.nlm.nih.gov/42155495/)

- **設計**：EPVent-2 + BIDMC retrospective cohort；n=890（hyperinflammatory 424 / hypoinflammatory 466）
- **分型**：Latent Class Analysis (LCA) — IL-6/IL-8/CRP/IL-10/protein C 等 6 biomarkers
- **60 天死亡率**：hyperinflammatory **55%** vs hypoinflammatory **29%**（p<0.0001）

| 指標 | Hypoinflammatory | Hyperinflammatory | Interaction p |
|------|------------------|-------------------|---------------|
| High ΔP ≥15 cmH₂O | aHR **2.01** (1.39-2.91) | aHR **1.46** (1.11-1.94) | **0.033** |
| High PLDyn ≥12 cmH₂O | aHR **2.36** (1.64-3.39) | aHR **1.18** (0.84-1.60) | **0.001** |

> Hyperinflammatory 超額死亡：**46% 由 extrapulmonary organ failure 中介**，呼吸衰竭 0% → 靶向多器官支持比單純護肺更重要

---

# 坐椅位 (Armchair Position) 改善自主呼吸 ICU 病人氧合 — RCT
## [Fossat G et al. *Intensive Care Med* 2026-05-18](https://doi.org/10.1007/s00134-026-08453-y) | [PMID 42149248](https://pubmed.ncbi.nlm.nih.gov/42149248/)

- **設計**：單中心 RCT（法國）；PSV / HFNC / NIV 自主呼吸病人；n=284
- **介入**：坐椅 (armchair) vs 半臥位 (semi-recumbent) 3 小時

| 組別 | 3 小時後 P/F 變化 | 邊際平均值 |
|------|------------------|-----------|
| 坐椅組 | **+13 mmHg** (95% CI 1-24) | 241 mmHg |
| 臥位組 | **−13 mmHg** (95% CI −25 to −1) | 206 mmHg |
| Interaction p | **0.002** | 組間 p=0.004 |

- **安全性**：無嚴重不良事件
- **限制**：單中心、3 小時短期觀察、無插管率等長期終點

> 「讓病人坐起來」= 即時呼吸治療，而非僅復健。**應成為每日 ICU 常規**。

---

<!-- _class: small-text -->

# Technology-Enhanced PEEP 最佳化 — SR/MA
## [Boulton AJ et al. *Crit Care Med* 2026-05-29](https://doi.org/10.1097/CCM.0000000000007144) | [PMID 42207935](https://pubmed.ncbi.nlm.nih.gov/42207935/)

- **設計**：SR/MA，34 RCTs，n=2,951；7 種技術（食道氣球、EIT、P-V curve、閉環通氣等）
- **死亡率（10 studies, n=1,719）**：**RR 0.69（0.52-0.93）** — 但證據確定性 **very low**

| 終點 | 結果 | Certainty |
|------|------|-----------|
| 機械通氣持續時間 | 無差異（MD −0.06 d） | Very low |
| **28 天死亡率** | **RR 0.69（0.52-0.93）↓** | **Very low** |
| 其他臨床效果 | 無顯著差異 | — |

> 食道氣球 / EIT 導向 PEEP「可能」降低死亡率，但 **very low certainty** — 尚不足以改變常規實踐。目前限於有設備與專業的中心使用。

---

# 俯臥位通氣在北美疫情後大幅衰退
## [Barker AK et al. *Crit Care Med* 2026-05-22](https://doi.org/10.1097/CCM.0000000000007148) | [PMID 42171428](https://pubmed.ncbi.nlm.nih.gov/42171428/)

- **設計**：37 家北美醫院 retrospective cohort；n=5,944（PaO₂/FiO₂ ≤150，eligible for proning）

| 時期 | 俯臥位使用率 | adjusted OR vs 疫情前 |
|------|-------------|----------------------|
| 疫情前（2018-2020/02） | 11.0% | — |
| 疫情中（2020/03-2022/02） | **51.9%** | **7.6** (5.5-10.4) |
| 疫情後（2022/03-2024/12） | **25.6%** | 2.7 (1.8-3.9) vs 疫情中 |

- 疫情中 SARS-CoV-2 陽性 vs 陰性：OR 5.1（4.1-5.6）
- 醫院間差異仍持續（median OR 2.3 for similar patients）

> 俯臥位在疫情後滑落近 1/2。**對合乎適應症的 ARDS（P/F ≤150）應維持每日 ≥12-16 小時俯臥位** — 指引早已推薦，執行率不佳需系統性介入。

---

<!-- _class: divider -->

# Sepsis / 血流動力學
## Sepsis / Hemodynamics

---

# TLR4 磷酸化定義高風險 Sepsis Endotype
## [Mühlhaus M et al. *Crit Care* 2026-05-30](https://doi.org/10.1186/s13054-026-06115-5) | [PMID 42218524](https://pubmed.ncbi.nlm.nih.gov/42218524/)

- **設計**：前瞻性觀察，n=100 sepsis（SepsisDataNet.NRW cohort）
- **方法**：TLR4（Toll-like Receptor 4）磷酸化以 **proximity ligation assay** 定量；Day 1 + Day 4

| 時間點 | HR（高活化亞群） | 95% CI | p |
|--------|-----------------|--------|---|
| Day 1 | **2.03** | 1.01-4.07 | 0.048 |
| Day 4 | **2.77** | 1.14-6.73 | 0.025 |
| 多變量（SOFA/年齡/感染部位） | — | — | **0.006** |

- 整體 TLR4 活化偏低（median <1 signal/cell），但**高活化亞群**死亡率顯著增加
- 解釋為何 TLR4 拮抗劑（eritoran）在全 sepsis 族群試驗失敗

> **先分型、後治療** — 未來「biomarker-guided 免疫調控」比盲目全族群投藥更有前景。目前仍 hypothesis-generating（n=100）。

---

<!-- _class: small-text -->

# Sepsis 心血管亞表型：四種類別，死亡率 20-58%
## [Chotalia M et al. *Crit Care Med* 2026-05-25](https://doi.org/10.1097/CCM.0000000000007159) | [PMID 42187539](https://pubmed.ncbi.nlm.nih.gov/42187539/)

- **設計**：retrospective cohort；UK Birmingham；衍生 n=995 / 驗證 n=804；TTE 聚類分析

| Class | 特徵 | 比例（衍生） | 90 天死亡 |
|-------|------|------------|----------|
| 1 | 正常 LV + RV 功能 | 51% | **20%** |
| 2 | 高 cardiac index，hyperdynamic LV EF | 30% | **46%** |
| 3 | 擴大 RV，RV 收縮受損 | 10% | **47%** |
| 4 | 低 cardiac output，低 LV EF | 9% | **41%** |

- 3 變量模型（TTE + 血流動力學）可高準確辨別各亞型
- Class 2-4 與死亡率獨立相關；各 class 對 vasoactive / 液體反應不同

> 「Treatable traits」概念：**Class 3（右心衰）避免過度液體；Class 4（低輸出）考慮強心劑**。仍需前瞻性研究確認依亞型治療能改善結局。

---

# 高劑量升壓劑損傷微循環 — Hyperspectral Imaging (HSI) 研究
## [Rehn P et al. *Crit Care* 2026-05-29](https://doi.org/10.1186/s13054-026-06110-w) | [PMID 42216197](https://pubmed.ncbi.nlm.nih.gov/42216197/)

- **設計**：前瞻性 cohort 二次分析（HySpec-ICU），n=502 外科 ICU 病人
- **方法**：HSI 量測手部 tissue oxygen saturation (StO₂)；NEE（norepinephrine equivalent）量化升壓劑

**主要結果**：
- 高 NEE 獨立相關低 StO₂（B=**−0.093**；β=−0.193；**p=0.001**）
- MAP 與 StO₂ **無相關**
- 最高 NEE quartile（>0.28）：最低 StO₂ + 30 天死亡率 **41.8%**
- 休克恢復後 StO₂ +5.8%

> **Macrohemodynamic targets 正常 ≠ Microcirculation 正常** — 高劑量升壓劑即使 MAP 達標，仍可能損傷微循環。HSI 作為非侵入性床邊工具有前景，但尚未普及。

---

<!-- _class: divider -->

# AKI / 腎臟 / 液體管理
## Acute Kidney Injury / Renal / Fluid

---

# 限制性液體策略在 AKI：Stage 決定效果方向
## [White KC et al. *Crit Care* 2026-05-30](https://doi.org/10.1186/s13054-026-06094-7) | [PMID 42218546](https://pubmed.ncbi.nlm.nih.gov/42218546/)

- **設計**：Target trial emulation；澳洲 Queensland 12 ICU；n=8,685 成人 AKI
- **限制性策略**：72 小時液體平衡減少 **−2,304 mL**（95% CI −2,465 to −2,144）

| AKI Stage | AKI Rank 平均差（Day 7） | 30 天死亡率 |
|-----------|------------------------|------------|
| Stage 1（早期） | **−3.1**（−3.8 to −2.5）✅ 改善 | — |
| Stage 2 | **+4.5**（3.8 to 5.1）⚠️ 惡化 | RR **1.20**（1.09-1.33）↑ |
| Stage 3 | **+6.3**（4.7 to 7.9）⚠️ 最惡化 | — |

> **不可用單一液體限制策略套用所有 AKI 分期**：Stage 1 可積極限制；**Stage 2-3 應保守評估，優先確保腎灌注**。

---

# 碳酸氫鈉 Meta-Analysis：確定性降低 RRT 使用
## [Chen JJ et al. *Crit Care Med* 2026-05-22](https://doi.org/10.1097/CCM.0000000000007179) | [PMID 42171427](https://pubmed.ncbi.nlm.nih.gov/42171427/)

- **設計**：SR/MA；4 RCTs（含 **BICARICU-1 + BICARICU-2**）；n=1,111

| 終點 | RR (95% CI) | TSA / Bayesian |
|------|-------------|----------------|
| **RRT 使用** | **0.69（0.61-0.78）** ✅ | TSA 支持確定性獲益 |
| 28 天死亡率 | 0.84（0.55-1.30）NS | Bayesian P(benefit) **90.4%** |
| RRT 降低後驗機率 | — | **94.6%** |

- NS = Not Statistically Significant
- BICARICU-2：n=627，43 法國 ICU，IV NaHCO₃ vs usual care，嚴重酸血症 + moderate-to-severe AKI

> 對 pH <7.20 + AKI 病人：**NaHCO₃ 顯著降低 RRT 需求** — clinically meaningful。死亡率效益尚待大型 RCT；Bayesian 益處後驗機率達 90%。

---

<!-- _class: divider -->

# 心臟重症 / 術後照護
## Cardiac Critical Care / Post-operative Care

---

# POMPAE 試驗：目標鎂 1.5-2.0 mmol/L 無法預防 POAF — 陰性 RCT
## [Meerman M et al. *Crit Care Med* 2026-05-28](https://doi.org/10.1097/CCM.0000000000007162) | [PMID 42206948](https://pubmed.ncbi.nlm.nih.gov/42206948/)

- **設計**：雙盲 RCT，placebo-controlled；CABG / 瓣膜手術；n=265（因 futility **提前終止**）
- **介入**：IV Magnesium Sulfate（目標血清鎂 **1.5-2.0 mmol/L**，麻醉誘導至 ICU 離院）
- **血清鎂已確認達到目標濃度** → failure of target engagement 非原因

| 組別 | POAF 發生率 |
|------|------------|
| Magnesium | **37.9%** |
| Placebo | **28.6%** |
| RR | **1.29**（95% CI 0.92-1.80）|

- 任何亞族群無獲益；鎂組血壓支持需求更多（非顯著）

> **以 1.5-2.0 mmol/L 為目標的 perioperative 鎂輸注不應常規預防 POAF**。「鎂有益 POAF」的傳統觀念應被此嚴謹 RCT 動搖。低鎂血症（<0.8）補至正常值仍合理，但刻意超生理濃度無支持依據。

---

# MINT 亞分析：AMI + 重症病人的限制性輸血趨勢較差
## [Cooper HA et al. *Crit Care Med* 2026-05-25](https://doi.org/10.1097/CCM.0000000000007211) | [PMID 42188994](https://pubmed.ncbi.nlm.nih.gov/42188994/)

- **設計**：MINT（Myocardial Ischemia and Transfusion）trial 亞分析；n=3,504；144 中心
- **族群**：AMI + anemia；重症（ICU）n=1,679 vs 非重症 n=1,825
- **介入**：限制性（Hb <7-8 g/dL）vs 寬鬆性（Hb <10 g/dL）

| 族群 | 30 天死亡 RR | 死亡+MI RR |
|------|-------------|-----------|
| **重症（ICU）** | **1.24**（0.95-1.61）⚠️ | **1.21**（0.99-1.47）⚠️ |
| 非重症 | 1.09（0.77-1.54）| 1.09（0.85-1.38）|
| Interaction p | 0.55 | 0.52 |

> ICU 中合併 AMI 的病人：**Hb <10 g/dL 作為輸血觸發點比 Hb <7-8 更合理** — 不應以「重症用限制性輸血」的一般原則低輸血此特殊族群。

---

<!-- _class: divider -->

# ECMO / 神經重症
## ECMO / Neurocritical Care

---

# VV-ECMO 升級 (Escalation) 在 ARDS：4.7%，院內死亡率 47.9%
## [Ma S et al. *Crit Care Med* 2026-05-22](https://doi.org/10.1097/CCM.0000000000007177) | [PMID 42171409](https://pubmed.ncbi.nlm.nih.gov/42171409/)

- **設計**：Chinese ECLS Registry 多中心 cohort；112 中心；n=3,333 VV-ECMO ARDS（2017-2023）

| | 數量 | 比例 |
|---|------|------|
| 需要 ECMO escalation | 157 | **4.7%** |
| → VA-ECMO | 41 | 26.1% |
| → VAV-ECMO（veno-arterial-venous） | 68 | 43.3% |
| → VVA-ECMO（veno-veno-arterial） | 48 | 30.6% |
| 整體院內死亡率 | — | **47.9%** |

- **VA vs VVA 升級**：OR **3.44**（95% CI 1.05-11.34）— VA 存活更佳
- **高容量中心（>15 cases/year）** 升級率較低（OR 0.60；0.38-0.93）

> VV-ECMO 升級是高風險但有時必要的決策；VA 升級可能優於 VAV/VVA；**高容量中心降低升級需求 → 低容量中心應考慮適時轉診**。

---

# NEURO-CONDA Pilot：神經重症 Isoflurane 吸入性鎮靜 — 可行性試驗
## [Murcia-Gubianas C et al. *Crit Care* 2026-05-28](https://doi.org/10.1186/s13054-026-06101-x) | [PMID 42210338](https://pubmed.ncbi.nlm.nih.gov/42210338/)

- **設計**：Phase IV RCT，open-label，pilot；n=30（各 15 人）；76% TBI（traumatic brain injury）
- **條件**：有 ICP（intracranial pressure）監測，**無顱內高壓（ICP 正常）**
- **主要終點**：sedation 有效性（RASS / BIS™）+ 安全性（sustained ICP elevation / CPP <60）

**結果**：
- Sedation 有效性 100%（兩組相當）
- **無嚴重 ADR**；ICP / CPP 全程穩定
- 無需提高升壓劑

**重要限制**：n=30、開放標籤、無 ICH 病人、無長期神經學結局

> 在「無 ICP 升高」的神經重症病人，isoflurane 吸入性鎮靜顯示 feasibility。**目前不應改變常規神經重症鎮靜實踐** — 需大型 RCT 確認效益。

---

<!-- _class: divider -->

# 營養 / 長期重症
## Nutrition / Persistent Critical Illness

---

# 長期重症代謝軌跡：Day 10 達峰，三種亞型
## [Oosterveld T et al. *Crit Care* 2026-05-27](https://doi.org/10.1186/s13054-026-06102-w) | [PMID 42204563](https://pubmed.ncbi.nlm.nih.gov/42204563/)

- **設計**：前瞻性多中心；5 歐洲 + 2 澳洲 ICU；n=433，1,194 次 indirect calorimetry（ICU ≥10 天）

**主要結果**：
- EE（energy expenditure）：初期上升，**Day 10 達峰**後顯著下降（p<0.001）
- Urea:creatinine ratio（蛋白質異化指標）Day 10 前持續上升（p<0.001）

**三種代謝軌跡（latent class analysis）**：

| 軌跡 | 特徵 |
|------|------|
| **Hypometabolism** | 低 EE；最常見 |
| **Normometabolism** | 中等 EE |
| **Hypermetabolism** | 持續高 EE |

> **Day 10 後維持高熱量目標可能 overfeeding**。對長期重症病人應定期重新評估 EE；無 calorimetry 時，**Day 10 後考慮調低熱量 10-20%** 作為經驗法則。

---

<!-- _class: divider -->

# 其他焦點
## Other Highlights

---

<!-- _class: small-text -->

# 其他焦點 (Other Highlights)

| 文獻 | 主題 | 重點 |
|------|------|------|
| [Plens GM et al. *CCM* 2026-05-21](https://doi.org/10.1097/CCM.0000000000007145) PMID 42165647 | AI 即時估算 Pmus | Bias 0.9 cmH₂O；dyssynchrony 敏感度 86.5%、特異度 77.4% |
| [Boers LS et al. *Ann Int Care* 2026-05-21](https://doi.org/10.1016/j.aicoj.2026.100085) PMID 42212006 | 肺泡 host response 失調 | HSV/CMV 再活化 + alveolar immune paralysis；Compartment profiling 前景 |
| [Zhang R et al. *Crit Care* 2026-05-31](https://doi.org/10.1186/s13054-026-06098-3) PMID 42219497 | EIT EFI 預測再插管 | n=150；AUC **0.980**；EFI <1.333 → 48h 再插管率↑ |
| [Perez J et al. *AJRCCM* 2026-05-24](https://doi.org/10.1093/ajrccm/aamag246) PMID 42178817 | EIT tidal R/D in ARDS PSV | 主要決定因素：PLEnd-Exp；EIT-PEEP 顯著降低 R/D（11.3% vs 21.9%） |
| [Wechsler ME et al. *Lancet Respir Med* 2026-05-18](https://doi.org/10.1016/S2213-2600(26)00076-7) PMID 42150582 | SUNRISE 試驗 tezepelumab | OCS-sparing OR **2.93**（1.43-6.03）；exacerbations 30% vs 59% |
| [Sulica R et al. *Chest* 2026-05-22](https://doi.org/10.1016/j.chest.2026.05.018) PMID 42176848 | 危重 PAH ICU 管理 | RV preload/afterload/contractility 三角；ECLS as bridge to recovery/transplant |

---

<!-- _class: ref -->

# 參考文獻（一）

1. Pensier J, et al. [*Lancet Respir Med* 2026.](https://doi.org/10.1016/S2213-2600(26)00045-7) PMID 42155495
2. Fossat G, et al. [*Intensive Care Med* 2026.](https://doi.org/10.1007/s00134-026-08453-y) PMID 42149248
3. Boulton AJ, et al. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007144) PMID 42207935
4. Barker AK, et al. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007148) PMID 42171428
5. Perez J, et al. [*Am J Respir Crit Care Med* 2026.](https://doi.org/10.1093/ajrccm/aamag246) PMID 42178817
6. Mühlhaus M, et al. [*Crit Care* 2026;30(1).](https://doi.org/10.1186/s13054-026-06115-5) PMID 42218524
7. Chotalia M, et al. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007159) PMID 42187539
8. Rehn P, et al. [*Crit Care* 2026;30(1).](https://doi.org/10.1186/s13054-026-06110-w) PMID 42216197
9. White KC, et al. [*Crit Care* 2026;30(1).](https://doi.org/10.1186/s13054-026-06094-7) PMID 42218546
10. Chen JJ, et al. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007179) PMID 42171427

---

<!-- _class: ref -->

# 參考文獻（二）

11. Meerman M, et al. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007162) PMID 42206948
12. Cooper HA, et al. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007211) PMID 42188994
13. Ma S, et al. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007177) PMID 42171409
14. Murcia-Gubianas C, et al. [*Crit Care* 2026;30(1).](https://doi.org/10.1186/s13054-026-06101-x) PMID 42210338
15. Oosterveld T, et al. [*Crit Care* 2026;30(1).](https://doi.org/10.1186/s13054-026-06102-w) PMID 42204563
16. Plens GM, et al. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007145) PMID 42165647
17. Boers LS, et al. [*Ann Intensive Care* 2026;16:100085.](https://doi.org/10.1016/j.aicoj.2026.100085) PMID 42212006
18. Zhang R, et al. [*Crit Care* 2026;30(1).](https://doi.org/10.1186/s13054-026-06098-3) PMID 42219497
19. Wechsler ME, et al. [*Lancet Respir Med* 2026.](https://doi.org/10.1016/S2213-2600(26)00076-7) PMID 42150582
20. Sulica R, et al. [*Chest* 2026.](https://doi.org/10.1016/j.chest.2026.05.018) PMID 42176848

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

Critical Care Biweekly Review 2026-06-01

本文件僅供醫療專業人員教學參考
