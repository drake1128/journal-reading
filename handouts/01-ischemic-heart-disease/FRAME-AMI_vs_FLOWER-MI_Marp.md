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
footer: '謝慕揚 MD, PhD, FESC | FRAME-AMI vs FLOWER-MI | 2026'
---

<!-- _class: lead -->

# FRAME-AMI vs FLOWER-MI
## 為什麼結論相反？FFR-Guided Non-Culprit PCI 的爭議

**謝慕揚 MD, PhD, FESC**
NEJM 2021 vs Eur Heart J 2023 | 2026-03-03
[FLOWER-MI](https://doi.org/10.1056/NEJMoa2104650) | [FRAME-AMI](https://doi.org/10.1093/eurheartj/ehac763)

---

# 大綱

1. 核心爭議：同一個問題，相反的答案
2. FLOWER-MI 試驗詳析
3. FRAME-AMI 試驗詳析
4. Head-to-Head 五大差異
5. 矛盾的根源：Angiography 閾值
6. NSTEMI 驅動了 FRAME-AMI 的結果
7. 臨床整合與 Take-Home Messages

---

<!-- _class: divider -->

# 核心爭議

---

# 同一個問題，相反的答案

### 共同問題

Acute MI + multivessel disease → non-culprit PCI 用 **FFR** 或 **angiography** 導引？

| | FLOWER-MI | FRAME-AMI |
|---|---|---|
| **期刊** | *NEJM* 2021 | *Eur Heart J* 2023 |
| **FFR vs Angio** | HR **1.32** (p=0.31) | HR **0.43** (p=0.003) |
| **結論** | **FFR 無優勢** | **FFR 顯著較好** |

> **怎麼會差這麼多？**

---

<!-- _class: divider -->

# FLOWER-MI 詳析

---

# FLOWER-MI 設計

**NEJM 2021** | France, 41 centers | n = 1,171 | **STEMI only**

- FFR-guided (n=590) vs **Angiography-guided ≥ 70%** (n=581)
- **97% staged PCI** (mean 2.6 days post-index)
- FFR ≤ 0.80 → PCI; FFR > 0.80 → defer

### FFR 數據

- Mean FFR：0.79 ± 0.11
- **44.3%** non-culprit lesions FFR > 0.80 (FFR-negative)
- **33.8%** FFR 組患者完全不需 non-culprit PCI

---

# FLOWER-MI 結果

| Endpoint | FFR 組 | Angio 組 | HR | P |
|----------|--------|----------|-----|---|
| **Primary composite** | **5.5%** | **4.2%** | **1.32** | **0.31** |
| Death | 1.5% | 1.7% | 0.89 | NS |
| **Nonfatal MI** | **3.1%** | **1.7%** | **1.77** | NS |
| Revascularization | 2.6% | 1.9% | 1.34 | NS |

- 3 年追蹤：8.9% vs 7.6% (p = 0.41) → **仍無差異**

> **注意**：FFR 組 nonfatal MI **數值上更高** (3.1% vs 1.7%)

---

# FLOWER-MI 的 Deferred Lesion 警訊

### 子分析：FFR-deferred patients 的結局

- FFR 組中，所有 lesions 均 FFR > 0.80 而完全 deferred 的患者
- 1 年 event rate：**8.1%**
- 有做 PCI 的患者：**4.1%** (p = 0.02)

> **FFR-deferred 的 lesion 反而事件率更高！**
> → FFR 在 STEMI 急性期可能產生 **false negative**
> → Inappropriately defer significant lesions

---

# NEJM 社論：Peter Juni

*"PCI for Nonculprit Lesions in Patients with STEMI — No Role for FFR"*

### 主要論點

1. Angiography-guided CR **已經夠好**
2. FFR 增加 procedural complexity **卻無額外益處**
3. 直接以 angiography 處理所有 significant non-culprit lesions

---

<!-- _class: divider -->

# FRAME-AMI 詳析

---

# FRAME-AMI 設計

**Eur Heart J 2023** | Korea, 14 centers | n = 562

### 兩個關鍵不同

| 與 FLOWER-MI 的差異 | FRAME-AMI |
|---|---|
| **患者** | **STEMI (47%) + NSTEMI (53%)** |
| **Angio 閾值** | **> 50%** (不是 ≥ 70%) |

- FFR-guided (n=284) vs Angiography-guided > 50% (n=278)
- **60% immediate PCI** / 40% staged
- 追蹤中位數 **3.5 年**

---

# FRAME-AMI 結果

| Endpoint | FFR 組 | Angio 組 | HR | P |
|----------|--------|----------|-----|---|
| **Primary composite** | **7.4%** | **19.7%** | **0.43** | **0.003** |
| **All-cause death** | **2.1%** | **8.5%** | **0.30** | **0.020** |
| **MI** | **2.5%** | **8.9%** | **0.32** | **0.009** |
| Revascularization | 4.3% | 9.0% | 0.61 | 0.216 |

- FFR 組 stents/patient：2.2 vs Angio 組 **2.5** (p < 0.001)

> **All-cause death 與 MI 都顯著降低**

---

# FRAME-AMI 的隱藏關鍵：NSTEMI 驅動

### 次族群分析

| MI Type | Events (Angio) | Events (FFR) | 差異 |
|---------|---------------|-------------|------|
| **NSTEMI** | **27** | **9** | **較大** |
| STEMI | 13 | 9 | 較小 |

- **主要獲益來自 NSTEMI 族群**
- 單獨看 STEMI 患者 → 差異不顯著
- **Pooled STEMI-only (FLOWER-MI + FRAME-AMI)：FFR 無顯著優勢**

---

<!-- _class: divider -->

# Head-to-Head 五大差異

---

# 差異 1：Angiography 閾值 — 最重要！

| | FLOWER-MI | FRAME-AMI |
|---|---|---|
| **Angio 閾值** | **≥ 70%** | **> 50%** |
| FFR 閾值 | ≤ 0.80 | ≤ 0.80 |

```text
FLOWER-MI (≥ 70%):
  ≥ 70% lesion → 大多 FFR 也 ≤ 0.80
  → 兩組治療差異小 → 結果無差異

FRAME-AMI (> 50%):
  50-69% lesion → 全部做 PCI (angio 組)
  → 但很多 FFR > 0.80 (不需要治療)
  → Angio 組大量 over-treatment
  → FFR 組避免不必要 stenting → FFR 較好
```

> **FFR 的價值在於 intermediate lesions (50-69%)**

---

# Stent 數量說明一切

### Non-culprit stents per patient

| | FFR 組 | Angio 組 | 差距 |
|---|---|---|---|
| **FLOWER-MI** | 1.01 | 1.50 | 0.49 |
| **FRAME-AMI** | ~1.2 | ~1.5 | ~0.3 |

### Angiography 組 event rate

| | Angio 組 Event Rate |
|---|---|
| **FLOWER-MI** (≥ 70%) | **4.2%** at 1 yr |
| **FRAME-AMI** (> 50%) | **19.7%** at 3.5 yr |

- FRAME-AMI Angio 組 event rate 異常高
- 反映 **> 50% 閾值導致的 over-treatment harm**

---

# 差異 2：NSTEMI 的納入

| | FLOWER-MI | FRAME-AMI |
|---|---|---|
| **NSTEMI** | **0%** | **53%** |
| STEMI | 100% | 47% |

### 為什麼 NSTEMI 讓 FFR 表現更好？

1. **Microvascular dysfunction 較少** → FFR 更準確
2. **Intermediate lesions 更多** → FFR 更能 discriminate
3. **NSTEMI 的 non-culprit 更常是 "true" intermediate**

> **STEMI-only pooled data：FFR 無優勢**

---

# 差異 3-5

### 差異 3：Non-culprit PCI 時機

| | FLOWER-MI | FRAME-AMI |
|---|---|---|
| **Immediate** | 3% | **60%** |
| Staged | **97%** | 40% |

- Immediate PCI of non-significant lesions → 更高 periprocedural risk

### 差異 4：追蹤時間
- FLOWER-MI 12 months vs FRAME-AMI 3.5 years

### 差異 5：Statistical Power
- FLOWER-MI event rate ~5% → 遠低於預期 → **underpowered**
- 需要 ~8,000 patients 才有足夠 power

---

<!-- _class: divider -->

# 如何整合？

---

# Network Meta-Analysis 的答案

### Elbadawi et al. (JACC Cardiovasc Interv 2022)

**11 trials, 8,195 patients**

| 比較 | OR (95% CI) | 結論 |
|------|-------------|------|
| Angio-guided CR vs culprit-only | **0.43** (0.31-0.58) | 有益 |
| FFR-guided CR vs culprit-only | **0.52** (0.35-0.78) | 有益 |
| **FFR vs angiography guidance** | **0.81** (0.51-1.29) | **無差異** |

> **Meta-analysis 結論：FFR 與 angiography guidance 效果相當**

---

# 整合圖解：FFR 的 Sweet Spot

```text
Non-culprit lesion severity:

  < 50%        50-69%           ≥ 70%
    |             |                |
  Medical     FFR 最有價值      Angio 已足夠
  therapy    (避免 over-       (直接 PCI)
              treatment)
                 |
           ┌─────┴─────┐
           |            |
      FFR ≤ 0.80    FFR > 0.80
           |            |
         PCI        Medical Tx
```

- **≥ 70%**：FLOWER-MI 告訴我們 angiography 已夠好
- **50-69%**：FRAME-AMI 告訴我們 FFR 有附加價值
- **< 50%**：不需要介入

---

# 什麼時候 FFR 有價值 vs 不需要？

| 場景 | FFR 角色 | 依據 |
|------|---------|------|
| Non-culprit **≥ 70%** | **不需要** | FLOWER-MI |
| Non-culprit **50-69%** | **最有價值** | FRAME-AMI |
| Non-culprit **< 50%** | 不需要 | Medical therapy |
| **Culprit vessel** | **絕不使用** | MVO → false negative |
| **NSTEMI** | 可能更可靠 | 較少 MVO |
| **STEMI** | 可靠性稍低 | ~10% reclassification |

---

# Take-Home Messages

1. **FLOWER-MI 與 FRAME-AMI 看似矛盾，可以整合**
2. **最關鍵差異：Angiography 閾值** (≥ 70% vs > 50%)
3. **FFR 的 sweet spot = intermediate lesions (50-69%)**
4. **Stenosis ≥ 70% → 直接 PCI，不需 FFR** (FLOWER-MI)
5. **FRAME-AMI 獲益主要由 NSTEMI 驅動**
6. **Network meta-analysis：FFR vs angio guidance 效果相當**
7. **Complete revascularization 本身有益** (Class I)
   FFR 是策略選擇，不是必須

---

<!-- _class: small-text -->

# 參考文獻

1. Puymirat E, et al. FLOWER-MI. [*NEJM.* 2021;385:297-308.](https://doi.org/10.1056/NEJMoa2104650)
2. Lee JM, et al. FRAME-AMI. [*Eur Heart J.* 2023;44:473-484.](https://doi.org/10.1093/eurheartj/ehac763)
3. Juni P. No Role for FFR (Editorial). [*NEJM.* 2021;385:370-371.](https://doi.org/10.1056/NEJMe2108328)
4. Music L, et al. FLOWER-MI Deferred Lesion Sub-study. [*Circ Cardiovasc Interv.* 2021.](https://doi.org/10.1161/CIRCINTERVENTIONS.121.011314)
5. Lee JM, et al. FRAME-AMI QCA Substudy. [*Circ Cardiovasc Interv.* 2024.](https://doi.org/10.1161/CIRCINTERVENTIONS.123.013611)
6. Elbadawi A, et al. Network Meta-Analysis. [*JACC Cardiovasc Interv.* 2022.](https://doi.org/10.1016/j.jcin.2022.01.002)
7. Mehta SR, et al. COMPLETE. [*NEJM.* 2019;381:1411-1421.](https://doi.org/10.1056/NEJMoa1907775)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
