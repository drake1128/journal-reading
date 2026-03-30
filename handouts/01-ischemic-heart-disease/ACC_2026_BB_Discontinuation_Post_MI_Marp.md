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
footer: '謝慕揚 MD, PhD, FESC | Beta-Blocker Post-MI | ACC 2026'
---

<!-- _class: lead -->

# SMART-DECISION Trial
## Beta-Blocker Discontinuation after Myocardial Infarction

**謝慕揚 MD, PhD, FESC**
資料來源：*N Engl J Med* 2026 | Choi KH, Kang D, Kim W, Hahn JY, et al.
[原文連結](https://doi.org/10.1056/NEJMoa2601005)

---

# 大綱

1. Post-MI beta-blocker 的角色演變
2. SMART-DECISION 試驗設計
3. 基線特徵
4. 主要終點結果 — Noninferiority 分析
5. 次要終點
6. 與 ABYSS 試驗的比較
7. Post-MI beta-blocker 證據總覽
8. 臨床實務建議

---

<!-- _class: divider -->

# 第一部分：背景

---

# Post-MI Beta-Blocker — 角色正被重新定義

### 確定有益的族群
- **LVEF <40%** 或 **heart failure** — beta-blocker 仍是基石治療
- CAPRICORN, CIBIS-II, SENIORS 等試驗支持

### 爭議中的族群
- **LVEF ≥50%** — REDUCE-AMI (2024)：無益
- **LVEF ≥40%, no HF** — REBOOT, NOR-BEAT (2025)：無益
- **Mildly reduced EF 40-49%** — 可能有益 (Lancet IPD meta-analysis)

### 未解問題
- 已長期使用 beta-blocker 的穩定 post-MI 患者，**能否安全停藥？**
- ABYSS (2024)：未達 noninferiority
- **SMART-DECISION 試圖回答此問題**

---

# SMART-DECISION 試驗設計

- **Open-label, multicenter, randomized, noninferiority trial**
- 韓國 25 家醫院，2021-2023 年收案
- **N = 2540**，1:1 隨機分配
- 追蹤中位數 **3.1 年** (IQR 2.5-3.5)

| 停藥組 (n=1246) | 持續用藥組 (n=1294) |
|----------------|-------------------|
| 隨機分配後**立即停用** beta-blocker | 維持原 beta-blocker 同劑量 |

### 主要終點
- **Death + recurrent MI + HF hospitalization** (複合)
- Noninferiority margin: HR upper 95% CI < **1.4**

---

# 納入條件 — 穩定 Post-MI Population

### 核心條件
- 心肌梗塞病史
- Beta-blocker 使用**至少 1 年**
- Index MI 至篩選為 **event-free**
- **LVEF ≥40%**

### 排除條件
- Heart failure 治療中
- LVEF <40%
- Beta-blocker 禁忌症
- **Atrial fibrillation**

> **Pearl**：排除 AF 和 HF — 確保停藥安全性不受 rate control 或 HF 治療需求影響

---

<!-- _class: divider -->

# 第二部分：結果

---

# 基線特徵

| 特徵 | 停藥組 (n=1246) | 持續用藥組 (n=1294) |
|------|---------------|-------------------|
| 年齡 (歲) | 63.4 ± 9.9 | 63.0 ± 10.3 |
| 男性 | 87.3% | 87.0% |
| STEMI | 57.3% | 56.3% |
| PCI 治療 | 97.4% | 97.5% |
| 完全血管重建 | 73.1% | 76.6% |
| 高血壓 | 60.5% | 59.2% |
| 糖尿病 | 40.2% | 36.2% |
| **Median LVEF** | **59.0%** | **59.0%** |
| **MI 至隨機分配** | **4.6 年** | **4.8 年** |

> **Pearl**：中位 LVEF 59%、MI 後中位 4.7 年、98% 接受 PCI — 真正**穩定且低風險**的族群

---

# Beta-Blocker 使用情況

| Beta-Blocker 種類 | 停藥組 | 持續用藥組 |
|-------------------|--------|----------|
| **Carvedilol** | 47.8% | 47.4% |
| **Bisoprolol** | 32.4% | 32.2% |
| **Nebivolol** | 19.7% | 20.2% |
| Other | 0.1% | 0.2% |

- 三種主要 beta-blocker 均具備有利藥理特性：
  - Carvedilol: alpha-1 blocking + 抗氧化
  - Bisoprolol: 高度 beta-1 selectivity
  - Nebivolol: beta-1 selective + NO-mediated vasodilation

> 即使使用「最好的」beta-blocker，在穩定 post-MI 族群中停藥仍安全

---

# 主要終點 — Noninferiority 達標

## Death + Recurrent MI + HF Hospitalization

| | 停藥組 | 持續用藥組 |
|--|--------|----------|
| 事件數 | **58** | **74** |
| 4-year KM estimate | **7.2%** | **9.0%** |
| Risk difference | -1.8% (95% CI, -5.5 to 1.9) |

### HR = 0.80 (95% CI, 0.57-1.13)
### P = 0.001 for noninferiority

> HR 上限 **1.13 < 1.4** (noninferiority margin)
> 點估計值 0.80 甚至**數值上偏向停藥組**

---

# 次要終點 — 各組成部分

| 終點 | 停藥組 | 持續用藥組 | HR (95% CI) |
|------|--------|----------|-------------|
| **全因死亡** | 2.4% | 3.4% | 0.71 (0.43-1.16) |
| **再發 MI** | 2.3% | 2.6% | 1.11 (0.63-1.96) |
| **HF 住院** | 2.2% | 2.1% | 0.82 (0.42-1.57) |
| 心血管死亡 | 1.6% | 2.0% | 0.76 (0.40-1.42) |
| 任何住院 | 18.1% | 19.6% | 0.86 (0.68-1.08) |
| 心血管住院 | 10.0% | 13.1% | 0.72 (0.55-0.96) |
| 中風 | 3.8% | 4.0% | 0.97 (0.60-1.53) |

> **Pearl**：所有個別終點均無不利訊號。心血管住院甚至在停藥組**顯著較少** (HR 0.72)。

---

# 安全性與心臟功能

### 不良事件
| 項目 | 停藥組 | 持續用藥組 |
|------|--------|----------|
| 嚴重不良事件 | 11.5% | 13.4% |
| 嚴重心臟事件 | 5.7% | 6.1% |

### 心臟功能監測
- **LVEF 變化**：兩組無顯著差異
- **NT-proBNP 變化**：兩組無顯著差異
- **血壓**：停藥後輕度上升 (baseline mean SBP < 130 mmHg)
- **心率**：停藥後輕度上升

### 生活品質 (PROMIS-29)
- 基線相似，追蹤期間無顯著差異

> **停藥不會導致心臟功能惡化**

---

# Per-Protocol & 亞組分析

### Per-Protocol Analysis
- HR = **0.79** (95% CI, 0.56-1.12) — 與 ITT 一致

### 亞組分析 — 所有亞組一致

| 亞組 | Interaction P |
|------|-------------|
| STEMI vs. NSTEMI | NS |
| 年齡 <65 vs. ≥65 歲 | NS |
| 男性 vs. 女性 | NS |
| 糖尿病 yes vs. no | NS |
| Carvedilol vs. Bisoprolol vs. Nebivolol | NS |
| LVEF <50% vs. ≥50% | NS |
| 多血管疾病 yes vs. no | NS |

> 無任何亞組顯示停藥有害

---

<!-- _class: divider -->

# 第三部分：討論與結論

---

# SMART-DECISION vs. ABYSS — 為何結果不同？

| | SMART-DECISION | ABYSS |
|--|----------------|-------|
| **結果** | **Noninferiority 達標** | 未達 noninferiority |
| 主要終點 | Death + MI + **HF hosp** | Death + MI + stroke + **CV hosp** |
| 終點差異 | Hard endpoints | 含 soft endpoints |
| BB 最短使用 | **1 年** | 6 個月 |
| MI 至隨機分配 | **4.7 年** | 2.9 年 |
| 二級預防 | 更積極 (ezetimibe, P2Y12) | 較不積極 |
| 事件率 | 更低 | 較高 |

> **Pearl**：ABYSS 差異主要來自 angina 入院、診斷性 angiography 等 **soft events** — 在 open-label 設計中易受影響。ABYSS 中 death + MI + HF hosp 兩組亦相似。

---

# Post-MI Beta-Blocker 證據總覽

| 試驗 | 年份 | 族群 | BB 開始/停止 | 結論 |
|------|------|------|-------------|------|
| CAPRICORN | 2001 | LVEF ≤40% | **開始** | **有益** |
| REDUCE-AMI | 2024 | EF ≥50% | 開始 | 無益 |
| ABYSS | 2024 | BB ≥6月 | 停止 | 未達 noninferiority |
| REBOOT | 2025 | EF not reduced | 開始 | 無益 |
| NOR-BEAT | 2025 | No HF | 開始 | 無益 |
| Lancet IPD | 2025 | EF 40-49% | — | **可能有益** |
| **SMART-DECISION** | **2026** | **EF ≥40%, BB ≥1 yr** | **停止** | **Noninferior** |

> **當代共識**：Beta-blocker 的獲益限於 **LVEF <40%** 和 **heart failure** 患者

---

# 誰可以停藥？誰不行？

### 可以考慮停藥
- Post-MI **≥1 年**
- **LVEF ≥40%**
- 無 heart failure 症狀
- 無 atrial fibrillation
- 臨床穩定、無事件

### 仍需持續 beta-blocker
- **LVEF <40%** (CAPRICORN, CIBIS-II)
- **Heart failure** (HFrEF guideline-directed therapy)
- **Atrial fibrillation** (rate control)
- MI 後 **<1 年** (SMART-DECISION 未涵蓋)
- **Mildly reduced EF 40-49%** — 需個案評估

> **Pearl**：停藥後需監測血壓和心率變化

---

# 臨床實務流程建議

```text
Post-MI 患者評估 Beta-Blocker 是否繼續
    |
    ├── LVEF <40% or Heart Failure?
    |       → YES → 繼續 beta-blocker (Class I)
    |
    ├── Atrial Fibrillation?
    |       → YES → 繼續 (rate control 需要)
    |
    ├── MI 後 <1 年?
    |       → YES → 暫不停藥 (證據不足)
    |
    └── LVEF ≥40%, 無 HF, 無 AF, MI 後 ≥1 年, 穩定
            → 可考慮停藥 (SMART-DECISION)
            → 監測 BP 及 HR
```

---

<!-- _class: small-text -->

# 參考文獻

1. Choi KH, et al. Beta-Blocker Discontinuation Post-MI (SMART-DECISION). [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2601005)
2. Yndigegn T, et al. REDUCE-AMI. [*N Engl J Med*. 2024;390:1372-81.](https://doi.org/10.1056/NEJMoa2401479)
3. Ibanez B, et al. REBOOT. [*N Engl J Med*. 2025;393:1889-900.](https://doi.org/10.1056/NEJMoa2504826)
4. Silvain J, et al. ABYSS. [*N Engl J Med*. 2024;391:1277-86.](https://doi.org/10.1056/NEJMoa2404204)
5. Munkhaugen J, et al. NOR-BEAT. [*N Engl J Med*. 2025;393:1901-11.](https://doi.org/10.1056/NEJMoa2504827)
6. Rossello X, et al. BB + mildly reduced EF IPD meta-analysis. [*Lancet*. 2025;406:1128-37.](https://doi.org/10.1016/S0140-6736(25)01234-5)
7. Dargie HJ. CAPRICORN. [*Lancet*. 2001;357:1385-90.](https://doi.org/10.1016/S0140-6736(00)04560-8)
8. Byrne RA, et al. 2023 ESC ACS Guidelines. [*Eur Heart J*. 2023;44:3720-826.](https://doi.org/10.1093/eurheartj/ehad191)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
