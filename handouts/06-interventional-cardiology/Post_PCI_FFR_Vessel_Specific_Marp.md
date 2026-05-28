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
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; font-size: 0.85em; }
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
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
  section.ref { font-size: 0.7em; }
  section.ref h1 { font-size: 1.4em; }
  a { color: #0072bc; }
footer: '謝慕揚 MD, PhD, FESC | Post-PCI FFR 血管別目標值 | 2026'
---

<!-- _class: lead -->

# Post-PCI FFR：血管別目標值與症狀改善

## LAD 0.86 / RCA 0.91 / LCX 0.93，以及 ΔFFR ≈ 0.18 背後的文獻

**謝慕揚 MD, PhD, FESC** | 2026-05-18

主要文獻：[Collet C et al. *JACC Cardiovasc Interv* 2023;16(19):2396-2408](https://doi.org/10.1016/j.jcin.2023.08.018)

---

# 為什麼要做 post-PCI FFR？
## TARGET-FFR (Collison, EHJ 2021) — [DOI: 10.1093/eurheartj/ehab449](https://doi.org/10.1093/eurheartj/ehab449)

- **造影看起來漂亮 ≠ 生理上最佳化**
- TARGET-FFR：260 名患者 angiographically successful PCI 後 → **68.1% 的 post-PCI FFR < 0.90**
- Hwang 2022 meta-analysis (n = 5,277)：每降 0.01 FFR，**TVF 風險 ↑ 4%**（adjusted HR 1.04, 95% CI 1.02-1.05）

> **核心訊息**：post-PCI FFR 是 PCI 的 quality metric，不可僅憑造影判斷。

---

# 為何 LAD 與 non-LAD 的 FFR 不同？
## 解剖與生理基礎

- **LAD 灌流心肌量遠大於 LCX/RCA** → hyperemic flow 需求最大
- 流量大 → 沿途壓力下降大 → **同樣狹窄的 LAD 比其他血管的 FFR 低**
- 因此 LAD 在 PCI 後即使完美，FFR 也很難達到 ≥ 0.90

> 簡言之：**不要用單一 cutoff 評估所有血管**。

---

# Hwang 2019：早期血管別 cutoff
## EuroIntervention — [DOI: 10.4244/EIJ-D-18-00913](https://doi.org/10.4244/EIJ-D-18-00913)

835 名第二代 DES 患者，分析 post-PCI FFR 對 TVF 的預測：

| 血管 | n | 最佳 cutoff | TVF (低/高 cutoff) | HR (95% CI) |
|------|---|-------------|--------------------|-------------|
| **LAD** | 603 | **≤ 0.82** | 10.9% vs 2.5% | **4.08** (2.63-6.34) |
| **Non-LAD** | 232 | **≤ 0.88** | 8.0% vs 1.9% | **6.00** (1.78-20.26) |

> 第一篇明確指出 **post-PCI FFR cutoff 必須依血管別調整** 的研究。

---

<!-- _class: divider -->
# Collet 2023 Meta-Analysis
## 血管別 post-PCI FFR 的證據集大成

---

# Collet 2023 — Study Design
## JACC Cardiovasc Interv — [DOI: 10.1016/j.jcin.2023.08.018](https://doi.org/10.1016/j.jcin.2023.08.018)

- **Design**：Systematic review + **individual patient-level data** meta-analysis of 9 studies
- **n = 3,336 條血管 / 2,760 名患者**
- **主要 endpoint**：TVF（cardiac death + target vessel MI + clinically driven TVR）

---

# Collet 2023 — 關鍵數字
## 整體與血管別 post-PCI FFR 平均值

| 指標 | 數值 (95% CI) |
|------|---------------|
| 整體加權平均 | **0.89** (0.87-0.90) |
| **LAD 平均** | **0.86** (0.85-0.88) |
| **Non-LAD 平均** | **0.93** (0.91-0.94) |
| → **RCA 平均** | **≈ 0.91** |
| → **LCX 平均** | **≈ 0.93** |
| LAD vs Non-LAD | **p < 0.001** |

> **這就是朕緯演講中提到的 0.86 / 0.91 / 0.93 數字的原始出處。**

---

# Collet 2023 — 預測力的差異
## LAD vs Non-LAD 的 AUC

| 血管 | AUC for TVF | 95% CI | 判讀 |
|------|-------------|--------|------|
| **LAD** | **0.52** | 0.47-0.58 | 幾乎等於擲銅板 |
| **Non-LAD** | **0.66** | 0.59-0.73 | 中等鑑別力 |
| LAD vs Non-LAD | **p = 0.005** | — | — |

> **Pearl**：在 LAD，post-PCI FFR 「絕對數值」對未來事件預測力差；在 non-LAD 較可信。

> **Overall**：每 0.10 ↓ FFR，TVF 風險 ↑ 52%（主要由 TVR 驅動）

---

# Zhang 2024 國際登錄研究驗證
## JAMA Network Open — [DOI: 10.1001/jamanetworkopen.2024.18072](https://doi.org/10.1001/jamanetworkopen.2024.18072)

n = 2,147 患者，將 post-PCI FFR 分三層：

| 殘餘缺血層級 | Post-PCI FFR | 比例 | 相對 TVF 風險 |
|-------------|-------------|------|---------------|
| **Residual ischemia** | ≤ 0.80 | 12.5% | (reference, 最高) |
| **Suboptimal** | 0.81 - 0.86 | 25.7% | 中等 |
| **Optimal** | **> 0.86** | 61.8% | 最低 |

- Residual ischemia vs Optimal：**adjusted HR 2.94 (1.82-4.73), p < 0.001**

> **0.86 是 real-world 中 optimal 與 suboptimal 的分界。**

---

<!-- _class: divider -->
# ΔFFR ≈ 0.18-0.19
## 與症狀改善的關係

---

# TARGET-FFR Substudy — Study Design
## JACC Cardiovasc Interv — [DOI: 10.1016/j.jcin.2022.09.048](https://doi.org/10.1016/j.jcin.2022.09.048)

- **Design**：TARGET-FFR 試驗的 subanalysis (NCT03259815)
- **n = 103 患者**
- **病變分類**：以 median PPG index → **focal** (high PPG) vs **diffuse** (low PPG)
- **Patient-reported outcome**：SAQ-7，PCI 前與 PCI 後 3 個月評估
- **Residual angina**：SAQ-7 score < 100

---

# ΔFFR：focal vs diffuse 病變
## PCI 前後 FFR 變化

| 病變類型 | ΔFFR (mean ± SD) |
|---------|------------------|
| **Focal CAD** (high PPG) | **0.30 ± 0.14** |
| **Diffuse CAD** (low PPG) | **0.19 ± 0.12** ← 朕緯演講中的「0.18」 |
| 差異 | **p < 0.001** |

> **ΔFFR ≈ 0.19 = diffuse 病變的 PCI 後 FFR gain**

---

# ΔFFR 與症狀改善
## SAQ-7 與殘餘 angina

| 病變類型 | SAQ-7 (3 個月) | 殘餘 angina |
|---------|---------------|-------------|
| **Focal** | **87.1 ± 20.3** | **27.5%** |
| **Diffuse** | **75.6 ± 24.4** | **51.9%** |
| 差異 | mean diff 11.5 (2.8-20.3), **p = 0.01** | **p = 0.020** |

> **PCI 後整體殘餘 angina 比例 39.8%**
> **Diffuse 病變組殘餘 angina ≈ focal 組的 2 倍**

---

# ΔFFR 為什麼重要？
## ΔFFR = post-PCI FFR − pre-PCI FFR

- 反映「PCI 真正解除多少缺血」
- **大 ΔFFR (≈ 0.30)** → focal 病變、PCI 確實打通 → 症狀改善佳
- **小 ΔFFR (≈ 0.19)** → diffuse 病變、整條血管壓力下降仍在 → 症狀殘餘

> **Pearl**：絕對 FFR 數值之外，**ΔFFR 是另一個獨立的症狀預測指標**。

---

<!-- _class: divider -->
# Pullback Pressure Gradient
## 預測症狀改善的工具

---

# PPG — 概念
## Collet 2019 *JACC* — [DOI: 10.1016/j.jacc.2019.07.072](https://doi.org/10.1016/j.jacc.2019.07.072)

PPG index 量化壓力下降的「分布」：

| PPG index | 病變型態 | PCI 預期效果 |
|-----------|---------|--------------|
| **接近 1.0** | **Focal**（壓力下降集中於短節段） | ΔFFR 大，症狀改善佳 |
| **接近 0** | **Diffuse**（壓力下降均勻分布） | ΔFFR 小，症狀殘餘 |
| 中等 | Mixed | 介於兩者 |

> 36% 的血管病變型態用 FFR pullback 評估後與單純造影**重新分類**。

---

# Manual PPG 也可以
## Sonck 2022 — [DOI: 10.1002/ccd.30064](https://doi.org/10.1002/ccd.30064)

- 比較 **manual pullback** 與 motorized pullback：
  - mean difference < 0.01
  - 95% LOA: −0.14 to 0.12
  - inter-operator / intra-operator reproducibility 皆優異

> **臨床 implication**：一般 cath lab 不需特殊設備，**手動 pullback 即可估算 PPG**。

---

<!-- _class: divider -->
# 臨床應用

---

# PCI 前評估流程

1. **量測 pre-PCI FFR**（> 0.80 原則上不需 PCI）
2. **做 FFR pullback**（manual 即可）
3. **觀察壓力下降型態**：
   - 集中 → focal → 預期 ΔFFR 大，症狀改善佳
   - 均勻 → diffuse → 預期 ΔFFR 小，告知患者可能殘餘 angina
4. **決定支架位置**（鎖定主要壓力下降節段）

---

# PCI 後血管別目標

| 目標血管 | 期望 post-PCI FFR | 警示值 |
|---------|------------------|--------|
| **LAD** | **≥ 0.86** (合格)；**> 0.88** 較佳 | < 0.82 須處理 |
| **LCX** | **≥ 0.93** | < 0.88 須處理 |
| **RCA** | **≥ 0.91** | < 0.88 須處理 |

> 不要再用單一 0.90 cutoff！

---

# 不理想時的處置
## TARGET-FFR PIOS 流程

依序考慮：

1. **支架後擴張 (post-dilation)**：較大 non-compliant balloon、較高壓力
2. **影像評估 (IVUS / OCT)**：找 under-expansion / malapposition
3. **追加支架 (additional stent)**：若有 edge dissection
4. **再量測 FFR**

> TARGET-FFR PIOS 組 **30.5% 接受進一步處置**；雖然 FFR ≥ 0.90 達成率未達顯著差異，但 **FFR ≤ 0.80 比例顯著降低 11.2%（p = 0.045）**。

---

# Take Home Messages
## 給 cath lab 同事的 7 條摘要

1. **單一 FFR cutoff 不適用所有血管**
2. **血管別平均值**：LAD 0.86 / RCA 0.91 / LCX 0.93 (Collet 2023, n = 3,336)
3. **Suboptimal range** 0.81-0.86 仍有風險，> 0.86 才算 optimal
4. **ΔFFR 比絕對值更能預測症狀改善**：≥ 0.30 (focal) vs ≈ 0.19 (diffuse)
5. **Diffuse 病變組殘餘 angina ≈ focal 組的 2 倍**
6. **PCI 前 FFR pullback** 預測 PCI 後症狀改善
7. **Post-PCI FFR 不理想** → post-dilation / IVUS / 追加支架

---

<!-- _class: divider -->
# 參考文獻

---

<!-- _class: ref -->

# 參考文獻 (1/2)

1. Collet C, Johnson NP, Mizukami T, et al. Impact of Post-PCI FFR Stratified by Coronary Artery. [*JACC Cardiovasc Interv.* 2023;16(19):2396-2408.](https://doi.org/10.1016/j.jcin.2023.08.018) [PMID: 37821185](https://pubmed.ncbi.nlm.nih.gov/37821185/)

2. Hwang D, Lee JM, Lee HJ, et al. Influence of target vessel on prognostic relevance of FFR after coronary stenting. [*EuroIntervention.* 2019;15(5):457-464.](https://doi.org/10.4244/EIJ-D-18-00913) [PMID: 30561367](https://pubmed.ncbi.nlm.nih.gov/30561367/)

3. Hwang D, Koo BK, Zhang J, et al. Prognostic Implications of FFR After Coronary Stenting: Systematic Review and Meta-analysis. [*JAMA Netw Open.* 2022;5(9):e2232842.](https://doi.org/10.1001/jamanetworkopen.2022.32842) [PMID: 36136329](https://pubmed.ncbi.nlm.nih.gov/36136329/)

4. Zhang J, Hwang D, Yang S, et al. Angiographic Findings and Post-PCI FFR. [*JAMA Netw Open.* 2024;7(6):e2418072.](https://doi.org/10.1001/jamanetworkopen.2024.18072) [PMID: 38904958](https://pubmed.ncbi.nlm.nih.gov/38904958/)

5. Collet C, Collison D, Mizukami T, et al. Differential Improvement in Angina and QoL After PCI in Focal and Diffuse CAD. [*JACC Cardiovasc Interv.* 2022;15(24):2506-2518.](https://doi.org/10.1016/j.jcin.2022.09.048) [PMID: 36543445](https://pubmed.ncbi.nlm.nih.gov/36543445/)

---

<!-- _class: ref -->

# 參考文獻 (2/2)

6. Collison D, Didagelos M, Aetesam-Ur-Rahman M, et al. Post-stenting FFR vs coronary angiography (TARGET-FFR). [*Eur Heart J.* 2021;42(45):4656-4668.](https://doi.org/10.1093/eurheartj/ehab449) [PMID: 34279606](https://pubmed.ncbi.nlm.nih.gov/34279606/)

7. Collet C, Sonck J, Vandeloo B, et al. Measurement of Hyperemic Pullback Pressure Gradients. [*J Am Coll Cardiol.* 2019;74(14):1772-1784.](https://doi.org/10.1016/j.jacc.2019.07.072) [PMID: 31582137](https://pubmed.ncbi.nlm.nih.gov/31582137/)

8. Sonck J, Mizukami T, Johnson NP, et al. Validation and reproducibility of PPG from manual FFR pullbacks. [*Catheter Cardiovasc Interv.* 2022;99(5):1518-1525.](https://doi.org/10.1002/ccd.30064) [PMID: 35233906](https://pubmed.ncbi.nlm.nih.gov/35233906/)

9. Munhoz D, Collet C, Mizukami T, et al. PPG global registry rationale and design. [*Am Heart J.* 2023;266:177-187.](https://doi.org/10.1016/j.ahj.2023.07.016) [PMID: 37611857](https://pubmed.ncbi.nlm.nih.gov/37611857/)

10. Ikeda K, Mizukami T, Sakai K, et al. Impact of PPG on Clinical Outcomes after PCI. [*Circ Cardiovasc Interv.* 2025;18(12):e016022.](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016022) [PMID: 41137850](https://pubmed.ncbi.nlm.nih.gov/41137850/)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
2026-05-18

*本投影片為讀書會共筆整理，僅供醫療專業人員教學參考。*
