# Post-PCI FFR：血管別目標值與症狀改善的文獻依據

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-05-18**
**主要參考：[Collet C, et al. Impact of Post-PCI FFR Stratified by Coronary Artery. *JACC Cardiovasc Interv.* 2023;16(19):2396-2408.](https://doi.org/10.1016/j.jcin.2023.08.018)**

> 本講義整理朕緯醫師演講中提到的 post-PCI FFR 血管別目標值（LAD 0.86 / RCA 0.91 / LCX 0.93）以及 ΔFFR ≈ 0.18-0.19 與症狀改善之間的關係。整理人為讀書會共筆 (study group note-taker)，內容供醫療專業人員教學參考。

---

## 目錄

1. [背景：為什麼要做 post-PCI FFR？](#1-背景為什麼要做-post-pci-ffr)
2. [單一 cutoff 的局限：為何 LAD 與 non-LAD 不同？](#2-單一-cutoff-的局限為何-lad-與-non-lad-不同)
3. [Vessel-specific post-PCI FFR (Collet 2023 meta-analysis)](#3-vessel-specific-post-pci-ffr-collet-2023-meta-analysis)
4. [ΔFFR 與症狀改善：TARGET-FFR substudy](#4-δffr-與症狀改善target-ffr-substudy)
5. [Pullback Pressure Gradient (PPG)：focal vs diffuse](#5-pullback-pressure-gradient-ppgfocal-vs-diffuse)
6. [臨床應用：cath lab 如何使用](#6-臨床應用cath-lab-如何使用)
7. [限制與未來方向](#7-限制與未來方向)
8. [Take Home Messages](#8-take-home-messages)
9. [縮寫對照](#9-縮寫對照)
10. [參考文獻](#10-參考文獻)

---

## 1. 背景：為什麼要做 post-PCI FFR？

血管造影 (coronary angiography) 完成支架置放後，看起來「漂亮」的結果並不一定代表血流動力學最佳化。多個觀察性研究與隨機試驗顯示，PCI 後仍有相當比例的患者存在殘餘缺血 (residual ischemia)，而這些患者後續的目標血管失敗 (Target Vessel Failure, TVF) 與殘餘 angina 風險顯著較高。

### 關鍵觀察

- **TARGET-FFR (Collison 2021, EHJ)**：260 名患者 angiographically successful PCI 後，**仍有 68.1% 的 post-PCI FFR < 0.90**。即使在隨機分派到 physiology-guided incremental optimization strategy (PIOS) 組，仍有相當比例的患者無法達到 FFR ≥ 0.90 ([PMID 34279606](https://pubmed.ncbi.nlm.nih.gov/34279606/))。
- **Hwang 2022 meta-analysis (JAMA Network Open)**：5,277 名患者、5,869 條血管的 individual patient-level data；post-PCI FFR ≤ 0.80 出現於 11.8% 的血管，且每降低 0.01 FFR，TVF 風險增加 4% (adjusted HR 1.04, 95% CI 1.02-1.05, p < 0.001) ([PMID 36136329](https://pubmed.ncbi.nlm.nih.gov/36136329/))。

### 為何造影正常但 FFR 不理想？

可能原因包括：
- **支架膨脹不足 (under-expansion)**
- **支架貼壁不良 (malapposition)**
- **邊緣狹窄 (edge dissection / residual stenosis)**
- **彌漫性病變 (diffuse disease)**：支架治療僅針對局部狹窄，無法改善整條血管的彌漫性壓力下降

> **核心訊息**：造影視覺判斷無法取代生理學評估。Post-PCI FFR 是 PCI 品質的重要 quality metric。

---

## 2. 單一 cutoff 的局限：為何 LAD 與 non-LAD 不同？

### 解剖與生理基礎

**左前降支 (Left Anterior Descending, LAD)** 灌流的心肌量遠大於 LCX 或 RCA，因此 hyperemic flow demand（充血狀態下的血流需求）也最大。當血流增加時，沿著血管的壓力下降也越明顯，即使在沒有顯著狹窄的「正常」LAD，其 FFR 值通常也低於 LCX 與 RCA。

簡化來說：
- **流量需求大** → **沿途壓力下降大** → **FFR 數值偏低**
- 因此 LAD 在 PCI 後即使完美，FFR 也比較難達到 ≥ 0.90

### 早期實證 — Hwang 2019 (EuroIntervention)

[Hwang D, Lee JM, Koo BK, et al.](https://doi.org/10.4244/EIJ-D-18-00913) 在 835 名第二代 drug-eluting stent (DES) 置放患者中分析 post-PCI FFR 對 TVF 的預測能力：

| 血管 | 病人數 (n) | 最佳 cutoff 預測 TVF |
|------|-----------|---------------------|
| LAD | 603 (72.2%) | **≤ 0.82** |
| Non-LAD | 232 (27.8%) | **≤ 0.88** |

- LAD 組：低於 0.82 者 TVF 累積發生率 10.9% vs 2.5%（HR 4.08, 95% CI 2.63-6.34, p < 0.001）
- Non-LAD 組：低於 0.88 者 TVF 累積發生率 8.0% vs 1.9%（HR 6.00, 95% CI 1.78-20.26, p = 0.004）

> **Hwang 2019 已指出：post-PCI FFR 必須依照目標血管不同採用不同的 cutoff，才能合理解讀預後意義。**

---

## 3. Vessel-specific post-PCI FFR (Collet 2023 meta-analysis)

朕緯演講中提到的 **LAD 0.86 / RCA 0.91 / LCX 0.93** 數字，主要來自 2023 年發表於 *JACC Cardiovascular Interventions* 的 individual patient-level data meta-analysis。

### Study Design

**[Collet C, Johnson NP, Mizukami T, et al. Impact of Post-PCI FFR Stratified by Coronary Artery. *JACC Cardiovasc Interv.* 2023;16(19):2396-2408.](https://doi.org/10.1016/j.jcin.2023.08.018)**

- **Design**：Systematic review + individual patient-level meta-analysis of 9 studies
- **Sample size**：**3,336 條血管 / 2,760 名患者**
- **主要 endpoint**：TVF (cardiac death + target vessel MI + clinically driven TVR)

### 關鍵結果：post-PCI FFR 平均值與血管別差異

| 統計指標 | 數值 (95% CI) |
|---------|---------------|
| **整體加權平均 post-PCI FFR** | **0.89** (0.87-0.90) |
| **LAD 平均 post-PCI FFR** | **0.86** (0.85-0.88) |
| **Non-LAD 平均 post-PCI FFR** | **0.93** (0.91-0.94) |
| LAD vs Non-LAD 差異 | **p < 0.001** |

進一步分解 non-LAD：
- **RCA 平均 ≈ 0.91**
- **LCX 平均 ≈ 0.93**

### 預後預測能力 (AUC)

| 血管 | AUC for TVF | 95% CI |
|------|-------------|--------|
| **LAD** | **0.52** (poor) | 0.47-0.58 |
| **Non-LAD** | **0.66** (moderate) | 0.59-0.73 |
| LAD vs Non-LAD | **p = 0.005** | — |

> **Pearl 1**：在 LAD，post-PCI FFR 的「絕對數值」對未來事件的預測力幾乎等同擲銅板 (AUC 0.52)；在 non-LAD 則有合理的鑑別力 (AUC 0.66)。

> **Pearl 2**：整體上，post-PCI FFR 每降低 0.10 個單位，TVF 風險增加約 52%（主要由 TVR 驅動）。

### 補充驗證 — Zhang 2024 International Post-PCI FFR Registry

[Zhang J, Hwang D, et al. *JAMA Netw Open.* 2024;7(6):e2418072](https://doi.org/10.1001/jamanetworkopen.2024.18072) 在 2,147 名患者中將 post-PCI FFR 切成三層：

| 殘餘缺血層級 | Post-PCI FFR | 比例 | TVF 相對風險 |
|-------------|-------------|------|--------------|
| **Residual ischemia** | **≤ 0.80** | 12.5% | (reference, 最高) |
| **Suboptimal** | **0.81 - 0.86** | 25.7% | 約 0.57× residual |
| **Optimal** | **> 0.86** | 61.8% | 0.34× residual |

- Residual ischemia 組 vs Optimal 組：**adjusted HR 2.94, 95% CI 1.82-4.73, p < 0.001**

> **Pearl 3**：在 multi-vessel 與不同病變類型的 real-world 患者中，post-PCI FFR > 0.86 是相對安全的閾值；介於 0.81-0.86 仍有比 optimal 高的 TVR 風險。

---

## 4. ΔFFR 與症狀改善：TARGET-FFR substudy

朕緯演講中提到的「**ΔFFR ≈ 0.18 改善 symptom**」，最接近的原始文獻是 TARGET-FFR 試驗的 substudy：

### Study Design

**[Collet C, Collison D, Mizukami T, et al. Differential Improvement in Angina and Health-Related Quality of Life After PCI in Focal and Diffuse Coronary Artery Disease. *JACC Cardiovasc Interv.* 2022;15(24):2506-2518.](https://doi.org/10.1016/j.jcin.2022.09.048)**

- **Design**：TARGET-FFR 試驗的 subanalysis (NCT03259815)
- **Sample size**：103 名患者
- **Patient-reported outcome**：7-item Seattle Angina Questionnaire (SAQ-7)，分別於 baseline 與 PCI 後 3 個月評估
- **病變分類**：以 median PPG index 分為 **focal disease (high PPG)** 與 **diffuse disease (low PPG)**

### 關鍵結果

#### ΔFFR (PCI 前後 FFR 變化)

| 病變類型 | ΔFFR (mean ± SD) |
|---------|------------------|
| **Focal CAD** (high PPG) | **0.30 ± 0.14** |
| **Diffuse CAD** (low PPG) | **0.19 ± 0.12** ← 朕緯演講中的「0.18」 |
| 差異 | **p < 0.001** |

#### 症狀改善 (SAQ-7 summary score, 3 個月)

| 病變類型 | SAQ-7 score | 殘餘 angina 比例 |
|---------|-------------|------------------|
| **Focal CAD** | **87.1 ± 20.3** | **27.5%** |
| **Diffuse CAD** | **75.6 ± 24.4** | **51.9%** |
| 差異 | mean diff 11.5 (95% CI 2.8-20.3), **p = 0.01** | **p = 0.020** |

> **Pearl 4**：PCI 後殘餘 angina **整體發生率 39.8%**；diffuse 病變組殘餘 angina 將近 focal 病變組的兩倍 (51.9% vs 27.5%)。

> **Pearl 5**：**ΔFFR 越小，症狀改善越不理想**。ΔFFR ≈ 0.19 (diffuse 病變的平均值) 代表「即使做了 PCI，生理上得到的 gain 有限」，因此患者仍可能有 angina。

### 為什麼 ΔFFR 重要？

- ΔFFR = post-PCI FFR − pre-PCI FFR
- 反映「PCI 真正解除多少缺血量」
- **大的 ΔFFR (≈ 0.30)** → focal 病變、PCI 真的把狹窄打通 → 症狀改善佳
- **小的 ΔFFR (≈ 0.19)** → diffuse 病變、PCI 僅處理局部 → 整條血管壓力下降仍存在 → 症狀改善差

---

## 5. Pullback Pressure Gradient (PPG)：focal vs diffuse

### 基礎概念

[Collet C, Sonck J, et al. *J Am Coll Cardiol.* 2019;74(14):1772-1784.](https://doi.org/10.1016/j.jacc.2019.07.072) 提出 **Pullback Pressure Gradient (PPG) index** 來量化冠狀動脈病變的型態：

- **PPG index 接近 1.0** → **focal 病變**（壓力下降集中於短節段）
- **PPG index 接近 0** → **diffuse 病變**（壓力下降均勻分布於整條血管）

### 為何 PPG 重要？

| 病變型態 | PPG 表現 | PCI 預期效果 |
|---------|---------|--------------|
| **Focal** | 高 PPG | PCI 可有效解除壓力下降，ΔFFR 大，症狀改善佳 |
| **Diffuse** | 低 PPG | PCI 僅治療局部，整條血管壓力下降仍在，ΔFFR 小，症狀殘餘 |
| **Mixed** | 中等 PPG | 介於兩者之間 |

### 臨床操作

[Sonck J, Mizukami T, et al. *Catheter Cardiovasc Interv.* 2022;99(5):1518-1525.](https://doi.org/10.1002/ccd.30064) 證實 **manual FFR pullback** 與 motorized pullback 衍生的 PPG index 一致性極佳 (mean diff < 0.01)，且 inter-operator 與 intra-operator reproducibility 皆優異，意味著在一般 cath lab 環境也可以使用。

> **Pearl 6**：在做 pre-PCI FFR 時，順手做一次手動 pullback，即可粗略判斷 focal vs diffuse 病變，預估患者 PCI 後 angina 改善的機率。

---

## 6. 臨床應用：cath lab 如何使用

### PCI 前

1. **量測 pre-PCI FFR**（若 FFR > 0.80，原則上不需 PCI）
2. **做 FFR pullback**（manual 也可以），觀察：
   - 壓力下降是否集中（focal） vs 均勻分布（diffuse）
   - 主要壓力下降節段在哪裡（決定支架位置）
3. **與患者討論預期**：若是 diffuse 病變，告知 PCI 後仍有約 50% 機率殘餘 angina

### PCI 後

依照血管別評估 post-PCI FFR：

| 目標血管 | 期望 post-PCI FFR | 警示值 (考慮 optimization) |
|---------|------------------|----------------------------|
| **LAD** | **≥ 0.86 (合格)，> 0.88 較佳** | **< 0.82 須處理** |
| **LCX** | **≥ 0.93** | **< 0.88 須處理** |
| **RCA** | **≥ 0.91** | **< 0.88 須處理** |

### 不理想時的處置（依 TARGET-FFR PIOS 流程）

當 post-PCI FFR < 期望值時，依序考慮：

1. **支架後擴張 (post-dilation)** 使用較大的 non-compliant balloon、較高壓力
2. **影像評估 (IVUS / OCT)** 找出 under-expansion 或 malapposition 部位
3. **追加支架 (additional stent)** 若有 edge dissection 或未涵蓋的病變
4. **再次評估 FFR**

> **Pearl 7**：在 TARGET-FFR 試驗中，分派到 PIOS 組的患者有 **30.5% 接受了進一步處置**（post-dilation 或 additional stent）。雖然主要終點 (FFR ≥ 0.90) 未達顯著差異，但 **FFR ≤ 0.80 的比例顯著下降 11.2%（p = 0.045）**。

---

## 7. 限制與未來方向

### 目前證據的限制

1. **觀察性 + meta-analysis 為主**：尚缺乏大型 RCT 直接證明「依血管別 cutoff 進行 optimization」可改善硬性 endpoint
2. **PCI optimization 困難**：TARGET-FFR 顯示即使積極處置，仍有大量患者無法達到 FFR ≥ 0.90，反映 diffuse disease 的本質限制
3. **缺乏即時決策工具**：手動 PPG 需要操作經驗，AI / automated pullback 工具仍在開發

### 進行中或新發表的研究

- **PPG Global Registry** ([Munhoz D, et al. *Am Heart J.* 2023](https://doi.org/10.1016/j.ahj.2023.07.016))：全球性註冊研究，預期釐清 PPG 對 PCI 決策的影響
- **Ikeda K, et al. *Circ Cardiovasc Interv.* 2025**：PPG 對 post-PCI 臨床結果的影響 ([PMID 41137850](https://pubmed.ncbi.nlm.nih.gov/41137850/))
- **ORBITA-FIRE**：在 placebo-controlled 設計下找出 angina 真正的生理閾值

---

## 8. Take Home Messages

> **TH 1**：**單一 post-PCI FFR cutoff（如 ≥ 0.90）不適用所有血管。** LAD 因解剖學原因 FFR 本來就比較低，應採血管別目標值。

> **TH 2**：**Vessel-specific 平均值**：LAD 0.86 / RCA 0.91 / LCX 0.93 (Collet 2023 meta-analysis, n = 3,336 vessels)。

> **TH 3**：**Suboptimal range**：post-PCI FFR 0.81-0.86 雖未到 residual ischemia，但 TVF 風險仍高於 optimal (> 0.86) 組。

> **TH 4**：**ΔFFR (PCI 前後變化) 比絕對值更能預測症狀改善。** ΔFFR ≈ 0.30 (focal) 對應 87.1 SAQ-7；ΔFFR ≈ 0.19 (diffuse) 對應 75.6 SAQ-7，殘餘 angina 機率近兩倍。

> **TH 5**：**PCI 前做 FFR pullback** 評估 PPG，可預測 PCI 後 angina 改善的機率，並與患者進行知情討論。

> **TH 6**：**Post-PCI FFR 不理想時**，依序考慮 post-dilation、影像導引、追加支架。TARGET-FFR 證明此策略可降低殘餘 ischemia 比例。

---

## 9. 縮寫對照

| 縮寫 | 完整名稱 | 中文 |
|------|---------|------|
| AUC | Area Under the Curve | 受試者操作特徵曲線下面積 |
| CAD | Coronary Artery Disease | 冠狀動脈疾病 |
| CI | Confidence Interval | 信賴區間 |
| DES | Drug-Eluting Stent | 藥物洗脫支架 |
| FFR | Fractional Flow Reserve | 血流儲備分數 |
| HR | Hazard Ratio | 風險比 |
| iFR | Instantaneous wave-Free Ratio | 瞬時無波形比 |
| IVUS | Intravascular Ultrasound | 血管內超音波 |
| LAD | Left Anterior Descending artery | 左前降支 |
| LCX | Left Circumflex artery | 左迴旋支 |
| MI | Myocardial Infarction | 心肌梗塞 |
| OCT | Optical Coherence Tomography | 光學相干斷層掃描 |
| PCI | Percutaneous Coronary Intervention | 經皮冠狀動脈介入治療 |
| PIOS | Physiology-guided Incremental Optimization Strategy | 生理學導引漸進式最佳化策略 |
| PPG | Pullback Pressure Gradient | 拉回壓力梯度 |
| RCA | Right Coronary Artery | 右冠狀動脈 |
| RCT | Randomized Controlled Trial | 隨機對照試驗 |
| SAQ-7 | 7-item Seattle Angina Questionnaire | 七項 Seattle 心絞痛問卷 |
| TVF | Target Vessel Failure | 目標血管失敗 |
| TVR | Target Vessel Revascularization | 目標血管再血管化 |
| ΔFFR | Delta FFR (post-PCI FFR − pre-PCI FFR) | FFR 變化值 |

---

## 10. 參考文獻

1. Collet C, Johnson NP, Mizukami T, et al. Impact of Post-PCI FFR Stratified by Coronary Artery. [*JACC Cardiovasc Interv.* 2023;16(19):2396-2408.](https://doi.org/10.1016/j.jcin.2023.08.018) [PMID: 37821185](https://pubmed.ncbi.nlm.nih.gov/37821185/)

2. Hwang D, Lee JM, Lee HJ, et al. Influence of target vessel on prognostic relevance of fractional flow reserve after coronary stenting. [*EuroIntervention.* 2019;15(5):457-464.](https://doi.org/10.4244/EIJ-D-18-00913) [PMID: 30561367](https://pubmed.ncbi.nlm.nih.gov/30561367/)

3. Hwang D, Koo BK, Zhang J, et al. Prognostic Implications of Fractional Flow Reserve After Coronary Stenting: A Systematic Review and Meta-analysis. [*JAMA Netw Open.* 2022;5(9):e2232842.](https://doi.org/10.1001/jamanetworkopen.2022.32842) [PMID: 36136329](https://pubmed.ncbi.nlm.nih.gov/36136329/)

4. Zhang J, Hwang D, Yang S, et al. Angiographic Findings and Post-Percutaneous Coronary Intervention Fractional Flow Reserve. [*JAMA Netw Open.* 2024;7(6):e2418072.](https://doi.org/10.1001/jamanetworkopen.2024.18072) [PMID: 38904958](https://pubmed.ncbi.nlm.nih.gov/38904958/)

5. Collet C, Collison D, Mizukami T, et al. Differential Improvement in Angina and Health-Related Quality of Life After PCI in Focal and Diffuse Coronary Artery Disease. [*JACC Cardiovasc Interv.* 2022;15(24):2506-2518.](https://doi.org/10.1016/j.jcin.2022.09.048) [PMID: 36543445](https://pubmed.ncbi.nlm.nih.gov/36543445/)

6. Collison D, Didagelos M, Aetesam-Ur-Rahman M, et al. Post-stenting fractional flow reserve vs coronary angiography for optimization of percutaneous coronary intervention (TARGET-FFR). [*Eur Heart J.* 2021;42(45):4656-4668.](https://doi.org/10.1093/eurheartj/ehab449) [PMID: 34279606](https://pubmed.ncbi.nlm.nih.gov/34279606/)

7. Collet C, Sonck J, Vandeloo B, et al. Measurement of Hyperemic Pullback Pressure Gradients to Characterize Patterns of Coronary Atherosclerosis. [*J Am Coll Cardiol.* 2019;74(14):1772-1784.](https://doi.org/10.1016/j.jacc.2019.07.072) [PMID: 31582137](https://pubmed.ncbi.nlm.nih.gov/31582137/)

8. Sonck J, Mizukami T, Johnson NP, et al. Development, validation, and reproducibility of the pullback pressure gradient (PPG) derived from manual fractional flow reserve pullbacks. [*Catheter Cardiovasc Interv.* 2022;99(5):1518-1525.](https://doi.org/10.1002/ccd.30064) [PMID: 35233906](https://pubmed.ncbi.nlm.nih.gov/35233906/)

9. Munhoz D, Collet C, Mizukami T, et al. Rationale and design of the pullback pressure gradient (PPG) global registry. [*Am Heart J.* 2023;266:177-187.](https://doi.org/10.1016/j.ahj.2023.07.016) [PMID: 37611857](https://pubmed.ncbi.nlm.nih.gov/37611857/)

10. Ikeda K, Mizukami T, Sakai K, et al. Impact of Pullback Pressure Gradient on Clinical Outcomes after Percutaneous Coronary Interventions. [*Circ Cardiovasc Interv.* 2025;18(12):e016022.](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016022) [PMID: 41137850](https://pubmed.ncbi.nlm.nih.gov/41137850/)

---

*本文件由謝慕揚醫師為讀書會共筆整理。內容僅供醫療專業人員教學參考，不構成個別病例的臨床決策建議。*
