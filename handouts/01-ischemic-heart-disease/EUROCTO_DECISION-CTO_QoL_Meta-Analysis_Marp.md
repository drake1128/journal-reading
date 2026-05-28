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
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #ffd166; }
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
  section.ref { font-size: 0.7em; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; font-size: 0.9em; font-weight: normal; }
  h3 { color: #555555; }
  table { font-size: 0.7em; width: 100%; }
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
footer: '謝慕揚 MD, PhD, FESC | EUROCTO + DECISION-CTO Pooled QoL Meta-Analysis | JACC 2026'
---

<!-- _class: lead -->
# Quality of Life After PCI or Medical Therapy for Chronic Total Coronary Occlusions
## EUROCTO + DECISION-CTO Pooled Patient-Level Meta-Analysis
**謝慕揚 MD, PhD, FESC** | 2026-05-04
[Werner GS, et al. *JACC*. 2026 — DOI: 10.1016/j.jacc.2026.02.5099](https://doi.org/10.1016/j.jacc.2026.02.5099)

---

# 為什麼這篇文獻重要？
## CTO PCI 的證據基礎，2026 年的關鍵更新

- CTO 佔 CCS 病人 15–20% 的病灶，側支循環無法完全防止缺血
- 兩大 RCT 結果方向相反：
  - **EUROCTO (2018 EHJ)** — Positive：症狀與 QoL 改善
  - **DECISION-CTO (2019 Circulation)** — Neutral：症狀與 hard endpoint 都未達標
- 2024 ESC CCS guidelines 至今仍**不建議**單純為了症狀做 CTO PCI

> **Werner 與 Park 兩 PI 攜手把資料合併重看：當 CTO 是「唯一」病灶時，PCI 到底有沒有用？**

---

<!-- _class: divider -->
# Study Design
## Post-hoc IPD Pooled Analysis

---

# 篩選邏輯與分組
## [Werner GS, et al. *JACC*. 2026](https://doi.org/10.1016/j.jacc.2026.02.5099)

| 來源試驗 | 原始 N | 篩選後納入 |
|---------|-------|----------|
| EUROCTO (2:1 PCI:OMT) | 396 | **272** |
| DECISION-CTO (1:1) | 834 | **246** |
| **Pooled** | **1,230** | **518** |

**嚴格納入條件**
- 單一 CTO，**無其他 significant non-CTO lesion**
- 排除 in-stent CTO、LVEF < 30%

**最終分組**：PCI + OMT n=294 vs OMT only n=224

> 此設計排除了 DECISION-CTO 原本最大的 confounder（multivessel + late non-CTO PCI）

---

# Endpoints 與評估工具
## [Werner GS, et al. *JACC*. 2026](https://doi.org/10.1016/j.jacc.2026.02.5099)

**Primary efficacy** — SAQ 12 個月相較 baseline 之變化量
**Primary safety** — 3 年 cardiac death + nonfatal MI

| 量表 | 解讀 |
|------|------|
| **SAQ** (5 domain, 0–100) | **越高越好**（症狀越輕） |
| SAQ summary score | physical limitation + angina freq + QoL |
| EQ-5D-3L + VAS (0–100) | 一般健康狀況 |

**Significant individual improvement 門檻**
- Physical limitation Δ ≥ 8 / Angina frequency Δ ≥ 20 / QoL Δ ≥ 16

統計：ANCOVA 校正 baseline、study、J-CTO、性別、糖尿病、年齡；Bonferroni primary P < 0.01

---

<!-- _class: divider -->
# Results

---

# 病人特徵 Baseline
## [Werner GS, et al. *JACC*. 2026](https://doi.org/10.1016/j.jacc.2026.02.5099)

| 變項 | OMT (n=224) | PCI (n=294) | P |
|------|-------------|-------------|---|
| 平均年齡 | 62.3 | 63.2 | 0.37 |
| 男性 | 84.8% | 81.3% | 0.29 |
| 糖尿病 | 29.5% | 28.9% | 0.87 |
| Single-vessel disease | 70.1% | 72.8% | 0.10 |
| LVEF (%) | 56.9 | 56.7 | 0.84 |
| **J-CTO score** | **1.73** | **1.87** | **0.05** |
| Prior CABG | 3.1% | 7.5% | 0.03 |

PCI 第一次成功率 88.7% → 第二次嘗試後 **92.2%**；OMT 一年內 crossover 6.7%

---

# Primary Efficacy — SAQ 12 個月變化
## [Werner GS, et al. *JACC*. 2026](https://doi.org/10.1016/j.jacc.2026.02.5099)

| Domain | OMT Δ | PCI Δ | P | Cohen's d |
|--------|-------|-------|---|-----------|
| Physical limitation | 5.6 | 10.1 | 0.01 (邊緣) | 0.26 |
| **Angina frequency** | **8.6** | **12.2** | **0.009** | 0.30 |
| **Quality of life** | **11.3** | **19.5** | **<0.001** | **0.42** |
| **Summary score** | **8.5** | **13.8** | **<0.001** | **0.45** |
| Treatment satisfaction | 2.1 | 5.2 | 0.027 | 0.22 |

> **PCI 在 angina frequency、QoL、summary score 都過 Bonferroni primary threshold**

---

# Angina Frequency 解讀（同事提問補充）
## [Werner GS, et al. *JACC*. 2026 — Table 2](https://doi.org/10.1016/j.jacc.2026.02.5099)

**SAQ 分數越高 = 症狀越輕**（與直覺相反，常被誤讀）

| 時間點 | OMT | PCI | P |
|--------|-----|-----|---|
| Baseline | 84.2 | **79.1** | **0.001** |
| 12 mo | 90.9 | 93.1 | 0.15 |
| **Δchange (ANCOVA)** | **8.6** | **12.2** | **0.009** |
| 達 Δ ≥ 20 比例 | 26.5% | **40.7%** | 0.002 |

> PCI 組從**較嚴重**（baseline 79.1）出發，12 個月後改善幅度比 OMT 多 3.6 分。
> 達到「臨床顯著改善」門檻者 NNT ≈ 7

---

# 達「臨床顯著改善」之比例
## [Werner GS, et al. *JACC*. 2026 — Figure 2](https://doi.org/10.1016/j.jacc.2026.02.5099)

| Domain (預設門檻) | OMT | PCI | P |
|-----|-----|-----|---|
| Physical limitation Δ ≥ 8 | 37.2% | 52.6% | 0.004 |
| Angina frequency Δ ≥ 20 | 26.5% | 40.7% | 0.002 |
| **QoL Δ ≥ 16** | **41.9%** | **66.1%** | **<0.001** |

QoL 改善 OR 在兩 sub-trial 都顯著
- EUROCTO subset：2.73 (1.59–4.71)
- DECISION-CTO subset：3.18 (1.69–5.99)

**多變量分析**：只有 baseline QoL 越低、被分到 PCI 是 QoL 改善的獨立預測因子

---

# 個別反應差異很大 (Waterfall)
## [Werner GS, et al. *JACC*. 2026 — Figure 3](https://doi.org/10.1016/j.jacc.2026.02.5099)

- 47.4% PCI 病人 baseline QoL < 50（最有可能受益）
- PCI 組仍有 6.9% 病人 QoL **惡化** ≥ 16 分
- OMT 組則有 17.4% 病人 QoL 惡化

> **Pearl**：症狀越重，PCI 越受益；baseline 已高的病人有 ceiling effect。
> **預測 QoL 改善的兩個獨立因子**：baseline QoL 越低（OR 0.50/10 分）、assigned to PCI（OR 2.77）

---

# Safety — 3 年 ITT
## [Werner GS, et al. *JACC*. 2026 — Table 4](https://doi.org/10.1016/j.jacc.2026.02.5099)

| 事件 | OMT (n=224) | PCI (n=294) | P |
|------|-------------|-------------|---|
| Cardiac death | 1.3% | 2.0% | 0.55 |
| Nonfatal MI | 1.3% | 3.4% | 0.20 |
| **Cardiac death + MI** (primary safety) | **2.7%** | **5.1%** | **0.17** |
| Stroke | 2.2% | 1.7% | 0.66 |
| **Ischemia-driven revasc** | **14.7%** | **5.4%** | **0.001** |
| **MACCE** | **18.8%** | **10.6%** | **0.005** |

**Hard endpoint 無顯著差異**（underpowered）；MACCE 差異主要來自 OMT 組 crossover revascularization

---

<!-- _class: divider -->
# Discussion
## 整合 ORBITA-CTO 看 2026 證據基礎

---

# 2026 CTO PCI 證據圖譜
## [Khan S, et al. ORBITA-CTO. *JACC* 2026](https://doi.org/10.1016/j.jacc.2026.03.027)

| 證據 | 設計 | 方向 | 主要限制 |
|------|------|------|---------|
| EUROCTO 2018 | Open-label RCT (n=396) | Positive | Open-label expectancy |
| DECISION-CTO 2019 | Open-label RCT (n=834) | **Neutral** | Multivessel confounder |
| ISCHEMIA-CTO subset (Bangalore 2025) | ISCHEMIA subgroup | Positive (Sx) | Subgroup |
| **Pooled (本篇)** | Post-hoc IPD (n=518) | **Positive (SAQ)** | Post-hoc selection |
| **ORBITA-CTO 2026** | **Sham-controlled (n=50)** | **Positive Pr=0.996** | n=50, J-CTO ≤ 3 |

> 兩篇 2026 文獻分別解決 DECISION-CTO 的 confounding 與 placebo 質疑

---

# 兩篇 2026 文獻為什麼能整合？

1. **DECISION-CTO 的 neutral 來自方法學瑕疵**
   - Multivessel 病人 randomization 後才處理 non-CTO → 兩組都沒完整 revascularization
   - Werner 把 confounder 排除後（n=246），方向與 EUROCTO **一致**

2. **ORBITA-CTO 解決 placebo 質疑**
   - Sham-controlled 仍 positive (Pr(benefit) = 0.996)
   - CTO PCI 的 angina benefit **不是純粹 expectation effect**

> **共識**：對正確選擇的 single-vessel symptomatic 病人，CTO PCI 提供**真實**的 angina/QoL 改善；但**不應以 prognosis 作為適應症**

---

<!-- _class: divider -->
# Limitations & Pearls

---

# 主要限制 Limitations

1. **Post-hoc**：無 prospective harmonization、無預先 SAP；屬 hypothesis-generating
2. **雙重 selection bias**：原 RCT 已排除最嚴重病人 + DECISION-CTO 篩剩 29%
3. **Baseline imbalance**：PCI 組 baseline 症狀較重 → 仰賴 ANCOVA 校正
4. **Open-label**：expectancy effect 無法排除（這就是 ORBITA-CTO 的價值）
5. **Underpowered for hard endpoints**：3 年事件率 < 6%
6. **Follow-up SAQ missing 約 1/5**
7. **Expert-center generalizability**：92.2% 成功率出自 high-volume 中心
8. **EQ-5D-3L 解析度不足**：對輕症測不出差異

---

# Clinical Pearls 給新竹院心臟科

> **A. 適應症要嚴格**：single-vessel CTO + symptomatic + viable + ischemic + J-CTO ≤ 3

> **B. Multivessel CAD 先處理 non-CTO**：先處理 non-CTO → 重新評估症狀 → 還有症狀才做 CTO PCI（Heart Team SOP）

> **C. 不要用 prognosis 當 indication**：benefit 限定為 angina / QoL，不是壽命

> **D. 把 baseline SAQ 量起來**：最強 predictor 是 baseline QoL，不是 J-CTO

> **E. Operator volume 是必要條件**：92.2% 成功率出自 expert centers

> **F. 證據層級已升級**：2026 起可同時引 ORBITA-CTO + 本篇 pooled analysis 作為最完整 RCT 證據

---

<!-- _class: divider -->
# Take-Home

---

# Bottom Line

**對於正確選擇的 single-vessel symptomatic CTO 病人**，CTO PCI 真的能改善 angina 與 QoL：
- SAQ angina frequency Δ +12.2 vs +8.6 (P=0.009)
- SAQ QoL Δ +19.5 vs +11.3 (P<0.001)
- 達臨床顯著 QoL 改善：66.1% vs 41.9% (P<0.001)

**但仍有三個 caveat 必須誠實標示**：
1. Hard endpoint（mortality, MI）無 powered 證據
2. Baseline 症狀越輕，PCI 益處越小（ceiling effect）
3. 結果限於 expert center 的成績

> **2026 起，CTO PCI 的 indication 框架：嚴格的解剖選擇 × 明確的症狀負擔 × 老實的期望管理**

---

<!-- _class: ref -->
# 參考文獻 (1/2)

1. Werner GS, Kim JH, Hildick-Smith D, et al. Quality of Life After PCI or Medical Therapy for Chronic Total Coronary Occlusions: EUROCTO and DECISION-CTO Meta-Analysis. [*JACC*. 2026.](https://doi.org/10.1016/j.jacc.2026.02.5099)
2. Khan S, Sajjad U, Fawaz S, et al. Randomized, Placebo-Controlled Trial of CTO PCI in Stable Angina (ORBITA-CTO). [*JACC*. 2026 (Epub).](https://doi.org/10.1016/j.jacc.2026.03.027)
3. Werner GS, et al. EUROCTO trial. [*Eur Heart J*. 2018;39:2484–2493.](https://pubmed.ncbi.nlm.nih.gov/29722796/)
4. Lee SW, et al. DECISION-CTO. [*Circulation*. 2019;139:1674–1683.](https://pubmed.ncbi.nlm.nih.gov/30813758/)
5. Bangalore S, et al. ISCHEMIA-CTO subgroup. [*JACC*. 2025;85:1335–1349.](https://pubmed.ncbi.nlm.nih.gov/40175016/)
6. Rajkumar CA, et al. ORBITA-2. [*N Engl J Med*. 2023;389:2319–2330.](https://doi.org/10.1056/NEJMoa2310610)
7. Spertus JA, et al. SAQ development. [*JACC*. 1995;25:333–341.](https://pubmed.ncbi.nlm.nih.gov/7829785/)

---

<!-- _class: ref -->
# 參考文獻 (2/2)

8. Thomas M, et al. SAQ Interpretation Review. [*JAMA Cardiol*. 2021;6:593–599.](https://pubmed.ncbi.nlm.nih.gov/33625463/)
9. Morino Y, et al. J-CTO score. [*JACC Cardiovasc Interv*. 2011;4:213–221.](https://pubmed.ncbi.nlm.nih.gov/21349461/)
10. Vrints C, et al. 2024 ESC CCS Guidelines. [*Eur Heart J*. 2024;45:3415–3537.](https://doi.org/10.1093/eurheartj/ehae177)
11. Lawton JS, et al. 2021 ACC/AHA/SCAI Revasc Guideline. [*JACC*. 2022;79:e21–e129.](https://doi.org/10.1016/j.jacc.2021.09.006)
12. Megaly M, et al. CTO Trials vs Registries. [*JACC Cardiovasc Interv*. 2022;15:1441–1449.](https://pubmed.ncbi.nlm.nih.gov/35863793/)
13. Vadalà G, et al. ERCTO Registry. [*EuroIntervention*. 2024;20:e185–e197.](https://doi.org/10.4244/EIJ-D-23-00490)
14. Ramunddal T, et al. ISCHEMIA-CTO Rationale & Design. [*Am Heart J*. 2023;257:41–50.](https://doi.org/10.1016/j.ahj.2022.11.009)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
NTUH Hsinchu · Cardiovascular Division
結構性心臟病與介入心臟學
