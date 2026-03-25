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
  section.lead h1 { color: #ffffff; font-size: 2.2em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
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
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.72em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.88em;
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
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
  section.smaller-text { font-size: 0.78em; }
  section.smallest-text { font-size: 0.70em; }
footer: '謝慕揚 MD, PhD, FESC | COBRRA Trial — Apixaban vs. Rivaroxaban | 2026'
---

<!-- _class: lead -->

# Bleeding Risk with Apixaban vs. Rivaroxaban in Acute VTE

## COBRRA Trial — Apixaban 與 Rivaroxaban 出血風險比較

**謝慕揚 MD, PhD, FESC**
資料來源：[*N Engl J Med*. 2026;394:1051-60.](https://doi.org/10.1056/NEJMoa2510703) | 2026-03-12

---

# 大綱

1. 研究背景 Background
2. 研究單位與主持人 Investigators
3. 研究設計 Study Design
4. 病人特徵 Patient Characteristics
5. 主要結果 Primary Outcome
6. 次要結果 Secondary Outcomes
7. 討論與臨床意義 Clinical Implications
8. 研究限制 Limitations

---

<!-- _class: divider -->

# 研究背景 Background

---

# VTE 的疾病負擔

- **Venous thromboembolism (VTE)** 是全球第三常見急性心血管事件
- 一般人口發生率 **1-2 / 1000 人年**，隨年齡顯著增加
- 包括 **deep-vein thrombosis (DVT)** 與 **pulmonary embolism (PE)**
- 急性期死亡率：PE 約 **2-10%**（massive PE 更高）
- 抗凝治療至少需 **3 個月** 以預防復發

> VTE 是可預防且可治療的疾病，但抗凝治療的**出血風險**始終是臨床最大顧慮

---

# DOACs 時代的來臨

- 2010 年代起，**direct oral anticoagulants (DOACs)** 取代 vitamin K antagonists (VKA) 成為一線治療
- 主要 DOACs 用於 VTE 治療：

| 藥物 | 機轉 | Pivotal Trial | 年份 |
|------|------|--------------|------|
| **Rivaroxaban** | Factor Xa inhibitor | EINSTEIN-DVT/PE | 2010 |
| **Apixaban** | Factor Xa inhibitor | AMPLIFY | 2013 |
| **Edoxaban** | Factor Xa inhibitor | Hokusai-VTE | 2013 |
| **Dabigatran** | Direct thrombin inhibitor | RE-COVER | 2009 |

- DOACs 相較 VKA：**不需監測 INR**、藥物交互作用較少、固定劑量
- 各大指引 (ESC 2019, ASH 2020, CHEST 2021) 推薦 DOACs 為一線治療

---

# 為什麼需要 Head-to-Head 比較？

- Apixaban 與 rivaroxaban 各自 vs. VKA 的 pivotal trials 顯示**不同出血率**：

| 試驗 | DOAC | Clinically Relevant Bleeding | vs. VKA |
|------|------|------------------------------|---------|
| **AMPLIFY** | Apixaban | **4.3%** | 9.7% |
| **EINSTEIN** | Rivaroxaban | **8.1%** | 8.1% |

- Apixaban 似乎出血較少，但可能的解釋包括：
  - 病人族群不同（AMPLIFY 較多 provoked VTE）
  - 試驗設計差異（VKA 控制組的 TTR 不同）
  - 劑量策略差異（apixaban leading dose 7 天 vs. rivaroxaban 21 天）
- **缺乏 head-to-head RCT** → 指引無法推薦優先使用哪一種
- **COBRRA trial** 就是為了回答這個關鍵問題而設計

---

<!-- _class: divider -->

# 研究單位與主持人 Investigators

---

<!-- _class: small-text -->

# Ottawa VTE 研究團隊 — 全球 VTE 研究重鎮

**Ottawa Hospital Research Institute (OHRI)** 是全球最具影響力的 VTE 臨床研究中心之一，核心成員及其里程碑貢獻：

| 研究者 | 里程碑貢獻 | 期刊 / 年份 |
|--------|----------|-----------|
| **Philip S. Wells** | Wells DVT Score / Wells PE Score | *Lancet* 1997 / *Ann Intern Med* 2001 |
| **Philip S. Wells** | Wells DVT + D-dimer 驗證 RCT | *N Engl J Med* 2003 |
| **Gregoire Le Gal** | Revised Geneva Score (PE) | *Ann Intern Med* 2006 |
| **Gregoire Le Gal** | Age-adjusted D-dimer (ADJUST-PE) | *JAMA* 2014 |
| **Marc Rodger** | HERDOO2 Rule（VTE 停藥預測） | *J Thromb Haemost* 2009 |
| **Marc Carrier** | SOME Trial（occult cancer screening） | *N Engl J Med* 2015 |
| **Marc Carrier** | API-CAT Trial（cancer VTE reduced-dose apixaban） | *N Engl J Med* 2025 |
| **Lana Castellucci** | **COBRRA Trial（本研究）** | ***N Engl J Med* 2026** |

> Ottawa 團隊創造了全球急診每天都在使用的 **Wells Score**，並持續引領 VTE 研究

---

<!-- _class: small-text -->

# Ottawa 團隊的 VTE 研究脈絡

### 診斷工具 (Diagnostic Tools)
- **1995-2003**: Wells Score 系列 — 改變了全球 DVT/PE 的診斷流程
- **2006**: Revised Geneva Score — Le Gal 建立 PE 臨床預測規則
- **2014**: ADJUST-PE — 年齡校正 D-dimer，改變老年人 PE 排除策略

### 治療決策 (Treatment Decisions)
- **2009**: HERDOO2 Rule — Rodger 建立女性 VTE 停藥預測模型
- **2015**: SOME Trial — Carrier 證明大規模 occult cancer 篩檢無額外益處
- **2022**: CHAP Model — Wells 建立延長抗凝出血預測模型

### DOAC 時代的比較研究
- **2025**: API-CAT Trial — Carrier 證明 reduced-dose apixaban 可用於 cancer VTE 延長治療
- **2026**: **COBRRA Trial** — Castellucci 完成首個 DOAC head-to-head 出血比較

### 研究基礎建設
- **CanVECTOR Network**: 加拿大靜脈血栓研究網絡，由 OHRI 主導建立

---

<!-- _class: small-text -->

# Principal Investigator — Lana Castellucci, MD, MSc

**現職**：Associate Professor, University of Ottawa; Scientist, OHRI
**專長**：VTE 抗凝治療出血風險、臨床試驗設計

### 重要發表

| 年份 | 研究 | 期刊 |
|------|------|------|
| 2026 | **COBRRA Trial** — Apixaban vs. rivaroxaban bleeding risk | ***N Engl J Med*** |
| 2026 | **2026 AHA/ACC PE Guideline** — Writing committee member | *JACC / Circulation* |
| 2022 | **CHAP bleeding prediction model** (with Wells PS) | *Blood Adv* |
| 2021 | **ATTACC/REMAP-CAP** COVID-19 anticoagulation trials (co-investigator) | *N Engl J Med* (x2) |
| 2020 | Pulmonary embolism: update on management and controversies | *BMJ* |
| 2019 | It's time for head-to-head trials with DOACs (with Tritschler T) | *Thromb Res* |
| 2013 | Efficacy and safety of oral anticoagulants in secondary VTE prevention | *BMJ* |

- Semantic Scholar：**85 papers, 3320 citations, h-index 23**
- 2019 年即呼籲進行 DOAC head-to-head 試驗，7 年後以 COBRRA trial 實現此目標

---

<!-- _class: divider -->

# 研究設計 Study Design

---

<!-- _class: small-text -->

# COBRRA Trial 設計

- **設計**：Pragmatic, PROBE design (prospective, randomized, open-label, blinded endpoint)
- **收案**：32 centers — Canada (92.5%), Australia (7.3%), Ireland (0.2%)
- **收案期間**：2017 年 12 月 – 2025 年 1 月（歷時 7 年）
- **樣本**：2760 patients, 1:1 randomization
- **Power**：80% power 偵測 33% 相對風險下降（alpha 0.05, two-sided）
- **贊助**：Canadian Institutes of Health Research (CIHR) 等學術基金，無藥廠贊助

### 治療方案

| 藥物 | Leading Dose | 天數 | Maintenance Dose | 每日總劑量 |
|------|-------------|------|-----------------|----------|
| **Apixaban** | 10 mg BID | 7 天 | 5 mg BID | 10 mg/day |
| **Rivaroxaban** | 15 mg BID | 21 天 | 20 mg QD | 20 mg/day |

- 治療期間：**3 個月**
- Primary outcome：**Clinically relevant bleeding** (ISTH major + CRNM bleeding)
- 獨立 adjudication committee（blinded to treatment assignment）

---

<!-- _class: small-text -->

# 納入與排除條件

### 納入條件
- 年齡 ≥18 歲
- 有症狀之急性 proximal lower-limb DVT
- 或 segmental (含) 以上之 pulmonary embolism
- 能提供 informed consent（含 integrated consent）

### 主要排除條件
- 已接受 therapeutic anticoagulation >72 小時
- CrCl <30 ml/min (Cockcroft-Gault)
- Active bleeding
- Active cancer（當時 LMWH 仍為 cancer VTE 標準治療）
- 體重 >120 kg（依 ISTH 2016 guidance）
- 已知肝病 (Child-Pugh B/C)
- 禁忌交互作用藥物
- 懷孕或哺乳
- 其他長期抗凝適應症（如 atrial fibrillation）

### 分層因子 (Stratification)
- 腎功能 (CrCl <50 vs. ≥50 ml/min)、抗血小板藥物使用、收案中心

---

<!-- _class: divider -->

# 病人特徵 Patient Characteristics

---

<!-- _class: small-text -->

# 收案流程

- 評估 **9,753** 名患者
- 排除 6,993 人（683 人拒絕參加、6,310 人不符條件）
- **2,760 人隨機分配**：Apixaban 1,370 / Rivaroxaban 1,390
- 排除 60 人後進入 ITT 分析：**Apixaban 1,345 / Rivaroxaban 1,355**

### 基線特徵 — 兩組平衡良好

| 特徵 | Apixaban (n=1345) | Rivaroxaban (n=1355) |
|------|-------------------|----------------------|
| 年齡 (歲) | 58.0 ± 16.3 | 58.5 ± 15.8 |
| 女性 | 597 (44.4%) | 578 (42.7%) |
| BMI (kg/m²) | 29.1 ± 5.2 | 28.9 ± 5.1 |
| CrCl <50 ml/min | 60 (4.5%) | 63 (4.6%) |
| DVT alone | 691 (51.4%) | 718 (53.0%) |
| PE ± DVT | 654 (48.6%) | 637 (47.0%) |
| Unprovoked VTE | 1022 (76.0%) | 1065 (78.6%) |
| VTE 病史 | 210 (15.6%) | 219 (16.2%) |

---

<!-- _class: divider -->

# 主要結果 Primary Outcome

---

# Primary Outcome — Apixaban 大幅勝出

| 終點 | Apixaban | Rivaroxaban | RR (95% CI) |
|------|----------|-------------|-------------|
| **Clinically relevant bleeding** | **44 (3.3%)** | **96 (7.1%)** | **0.46 (0.33–0.65)** |
| Major bleeding | 5 (0.4%) | 32 (2.4%) | 0.16 (0.06–0.40) |
| CRNM bleeding | 39 (2.9%) | 67 (4.9%) | 0.59 (0.40–0.86) |

- **P < 0.001** for primary outcome
- Adjusted RR = **0.45** (95% CI 0.32–0.64)
- 各 subgroup 分析結果一致

> **Apixaban 降低 54% clinically relevant bleeding，Major bleeding 降低 84%**

---

# Kaplan-Meier 曲線 — 出血差異集中在前 3 週

- 大部分出血差異發生在 **前 21 天**
- 此期間 rivaroxaban 使用 **高劑量 15 mg BID**（比維持劑量高 50%）
- Apixaban 高劑量期僅 **7 天**，且每日總劑量較低（20 mg vs. 30 mg）
- 21 天後兩組曲線趨勢逐漸平行

> **提示**：Rivaroxaban 的 leading dose regimen（更高劑量、更長期間）可能是出血差異的主因

---

# 出血類型分析

| 出血類型 | Apixaban | Rivaroxaban |
|---------|----------|-------------|
| **Vaginal bleeding** | 2.7% | 3.8% |
| **GI bleeding** | 0.6% | 1.0% |
| **Hematuria** | — | 1.3% |

- Major bleeding in apixaban：5 例，全部為 Hb 下降/需輸血
- Major bleeding in rivaroxaban：32 例，28 例 Hb 下降/需輸血 + **4 例 critical organ bleeding**
- **兩組均無因出血導致之死亡**

> Vaginal bleeding 是兩組最常見的出血類型，但均低於先前 AMPLIFY (5.4%) 及 EINSTEIN (9.5%) 試驗

---

<!-- _class: divider -->

# 次要結果 Secondary Outcomes

---

# Recurrent VTE 與死亡率 — 兩組相似

| 終點 | Apixaban | Rivaroxaban | RR (95% CI) |
|------|----------|-------------|-------------|
| Recurrent VTE | 15 (1.1%) | 14 (1.0%) | 1.08 (0.52–2.23) |
| Death from any cause | 1 (0.1%) | 4 (0.3%) | 0.25 (0.03–2.26) |
| Death from bleeding | 0 | 0 | — |
| Death from recurrent VTE | 0 | 0 | — |

- Recurrent VTE 兩組幾乎完全相同 — **出血風險較低，但未犧牲抗栓效果**

### 藥物依從性
- Apixaban：**65.7%** complete adherence（BID 服藥）
- Rivaroxaban：**75.1%** complete adherence（QD 服藥）
- 儘管 apixaban 依從性較差，recurrent VTE 率仍未增加

---

<!-- _class: divider -->

# 討論與臨床意義

---

# 關鍵臨床訊息

> **Pearl 1**：Apixaban 在急性 VTE 治療中的出血風險顯著低於 rivaroxaban，且療效相當 — 首個 head-to-head RCT 證據

> **Pearl 2**：出血差異主要發生在前 3 週 leading dose 期間 — rivaroxaban 的高劑量期更長（21 天 vs. 7 天）且每日總劑量更高（30 mg vs. 20 mg）

> **Pearl 3**：儘管 apixaban 依從性較差（BID vs. QD），recurrent VTE 率仍相似 — 臨床需權衡安全性與方便性

---

# 選擇 DOAC 的實務考量

| 考量因素 | 偏好 Apixaban | 偏好 Rivaroxaban |
|---------|-------------|----------------|
| 出血風險高 | ✓ | |
| 年長患者 | ✓ | |
| CrCl 30-50 ml/min | ✓ | |
| 需較佳依從性 | | ✓ |
| 服藥方便性 | | ✓（QD） |
| 每日一次偏好 | | ✓ |

> **注意**：本試驗排除 active cancer、體重 >120 kg、AF 患者，結論不可直接外推。AF 的 head-to-head 試驗 (NCT04642430) 正在進行中。

---

<!-- _class: divider -->

# 研究限制 Limitations

---

# 主要限制

1. **Open-label 設計** — 但 endpoint blinded adjudication，且出血為 overt events
2. **僅追蹤 3 個月** — 長期抗凝的出血差異未知
3. **排除體重 >120 kg** — 肥胖患者資料不足
4. **排除 cancer-associated VTE** — 不適用於癌症患者
5. **種族多樣性有限** — 約 90% 白人，收案集中在 Canada
6. **未 powered for recurrent VTE** — 無法確認療效等同
7. **學術基金贊助** — 無藥廠贊助，但也代表結果較無商業偏見

### 不可外推的族群
- Extended secondary prevention（reduced dose DOAC）
- Cancer-associated VTE
- Atrial fibrillation（NCT04642430 進行中）

---

<!-- _class: smallest-text -->

# 參考文獻 (1/2)

1. Castellucci LA, et al. Bleeding Risk with Apixaban vs. Rivaroxaban in Acute VTE. [*N Engl J Med*. 2026;394:1051-60.](https://doi.org/10.1056/NEJMoa2510703)
2. Konstantinides SV, et al. 2019 ESC guidelines for acute PE. [*Eur Heart J*. 2020;41:543-603.](https://doi.org/10.1093/eurheartj/ehz405)
3. The EINSTEIN Investigators. Oral rivaroxaban for symptomatic VTE. [*N Engl J Med*. 2010;363:2499-510.](https://doi.org/10.1056/NEJMoa1007903)
4. Agnelli G, et al. Oral apixaban for acute VTE (AMPLIFY). [*N Engl J Med*. 2013;369:799-808.](https://doi.org/10.1056/NEJMoa1302507)
5. Stevens SM, et al. CHEST guideline for VTE. [*Chest*. 2021;160(6):e545-e608.](https://doi.org/10.1016/j.chest.2021.07.055)
6. Ortel TL, et al. ASH 2020 guidelines for VTE. [*Blood Adv*. 2020;4:4693-738.](https://doi.org/10.1182/bloodadvances.2020001830)
7. Wells PS, et al. Evaluation of D-dimer in the diagnosis of suspected DVT. [*N Engl J Med*. 2003;349:1227-35.](https://doi.org/10.1056/NEJMoa023153)
8. Le Gal G, et al. Revised Geneva Score for PE. [*Ann Intern Med*. 2006;144:165-71.](https://doi.org/10.7326/0003-4819-144-3-200602070-00004)
9. Righini M, Le Gal G, et al. Age-adjusted D-dimer (ADJUST-PE). [*JAMA*. 2014;311:1117-24.](https://doi.org/10.1001/jama.2014.2135)
10. Carrier M, et al. Screening for Occult Cancer in Unprovoked VTE (SOME). [*N Engl J Med*. 2015;373:697-704.](https://doi.org/10.1056/NEJMoa1506623)

---

<!-- _class: smallest-text -->

# 參考文獻 (2/2)

11. Mahe I, Carrier M, et al. Extended Reduced-Dose Apixaban for Cancer VTE (API-CAT). [*N Engl J Med*. 2025;392:1363-73.](https://doi.org/10.1056/NEJMoa2416112)
12. Tritschler T, Castellucci LA. It's time for head-to-head trials with DOACs. [*Thromb Res*. 2019;180:64-9.](https://doi.org/10.1016/j.thromres.2019.06.007)
13. Khan F, et al. Venous thromboembolism (Lancet Seminar). [*Lancet*. 2021;398:64-77.](https://doi.org/10.1016/S0140-6736(20)32658-1)
14. Creager MA, Castellucci LA, et al. 2026 AHA/ACC PE Guideline. [*JACC*. 2026.](https://doi.org/10.1016/j.jacc.2025.11.005)
15. Duffett L, Castellucci LA, Forgie MA. PE: update on management. [*BMJ*. 2020;370:m2177.](https://doi.org/10.1136/bmj.m2177)
16. Wells PS, et al. CHAP bleeding prediction model. [*Blood Adv*. 2022;6:4605-16.](https://doi.org/10.1182/bloodadvances.2022007027)
17. REMAP-CAP/ACTIV-4a/ATTACC. Therapeutic Anticoagulation in Critically Ill COVID-19. [*N Engl J Med*. 2021;385:777-89.](https://doi.org/10.1056/NEJMoa2103417)
18. ATTACC/ACTIV-4a/REMAP-CAP. Therapeutic Anticoagulation in Noncritically Ill COVID-19. [*N Engl J Med*. 2021;385:790-802.](https://doi.org/10.1056/NEJMoa2105911)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
