---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Noto Sans TC', 'Microsoft JhengHei', sans-serif;
    font-size: 26px;
  }
  h1 { color: #1a5276; font-size: 42px; }
  h2 { color: #2e86c1; font-size: 34px; }
  table { font-size: 22px; margin: auto; }
  th { background-color: #2e86c1; color: white; }
  blockquote { border-left: 4px solid #e74c3c; padding-left: 16px; color: #555; font-size: 22px; }
  .columns { display: flex; gap: 40px; }
  .col { flex: 1; }
  footer { font-size: 14px; color: #888; }
footer: 'Thrombus Aspiration in STEMI — Journal Reading | 謝慕揚'
---

# Thrombus Aspiration in STEMI
## 血栓抽吸——文獻整理

**Journal Reading Handout**
謝慕揚 Mu-Yang Hsieh, MD
心臟血管內科 | 新竹臺大分院

> 最後更新：2026-03-14

---

# Overview

- Thrombus aspiration 曾被認為是 primary PCI 的重要輔助治療
- 早期小型 RCT（TAPAS）顯示有臨床獲益
- 後續大型試驗（TASTE、TOTAL）及 IPD meta-analysis 均未證實常規使用優勢
- 甚至發現**增加中風風險**的趨勢
- 目前指引：**常規使用 Class III**，選擇性使用 Class IIb

---

# 文獻演進時間軸

```
2008  TAPAS (n=1,071)      → 正面結果 → 指引升級為 Class IIa
        ↓
2013  TASTE (n=7,244)      → 中性結果（30-day mortality 無差異）
        ↓
2015  TOTAL (n=10,063)     → 中性結果 + 中風風險增加
        ↓
2017  IPD Meta-analysis    → 確認無常規使用獲益
      (n=19,047)             → 指引降級為 Class III
```

---

# TAPAS Trial (2008)

**Thrombus Aspiration during PCI in Acute MI Study**
Svilaas T, et al. *NEJM* 2008; 358: 557–567

<div class="columns">
<div class="col">

### 設計
- **n = 1,071** STEMI 病人
- 血栓抽吸 vs. 傳統 PCI
- 主要終點：Myocardial blush grade (MBG)

</div>
<div class="col">

### 結果
- MBG 顯著優於傳統 PCI
- **1 年 cardiac death**：3.6% vs. 6.7%
  - HR 1.93 (1.11–3.37), p = 0.020
- 1 年 cardiac death/reinfarction：5.6% vs. 9.9%

</div>
</div>

---

# TAPAS — 影響與限制

### 影響
- 正面結果直接導致國際指引將 manual thrombectomy 升級為 **Class IIa**
- 臨床實務中被廣泛採用

### 限制
- 樣本量較小（n = 1,071）
- **Powered for MBG, not clinical events**
- 主要終點為替代指標（surrogate endpoint），非臨床硬終點

> ⚠️ 後續大型試驗將推翻這個結論

---

# TASTE Trial (2013–2014)

**Thrombus Aspiration in STEMI in Scandinavia**
Fröbert O, et al. *NEJM* 2013; 369: 1587–1597

- **n = 7,244** STEMI 病人
- **Registry-based RCT**（SWEDEHEART）
- 整體試驗成本僅 ~US$300,000（~$50/patient）

| 終點 | Aspiration | PCI alone | HR (95% CI) | p |
|------|-----------|-----------|-------------|---|
| 30-day mortality | 2.8% | 3.0% | 0.94 (0.72–1.22) | 0.63 |
| 1-year mortality | 5.3% | 5.6% | 0.94 (0.78–1.15) | 0.57 |

> **結論：常規血栓抽吸在降低死亡率上無顯著優勢**

---

# TOTAL Trial (2015–2016)

**此領域規模最大的 RCT**
Jolly SS, et al. *NEJM* 2015; 372: 1389–1398

- **n = 10,063** STEMI 病人 | Export catheter (Medtronic)
- 主要終點（180 天）：CV death, recurrent MI, cardiogenic shock, NYHA IV HF

| 終點 | Aspiration | PCI alone | HR (95% CI) | p |
|------|-----------|-----------|-------------|---|
| Primary (180 d) | 6.9% | 7.0% | 0.99 (0.85–1.15) | 0.86 |
| Primary (1 yr) | 8.0% | 8.0% | 1.00 (0.87–1.15) | 0.99 |
| **Stroke (30 d)** | **0.7%** | **0.3%** | **2.06 (1.13–3.75)** | **0.02** |
| **Stroke (1 yr)** | **1.2%** | **0.7%** | **1.66 (1.10–2.51)** | **0.015** |

---

# TOTAL — Key Message

> 常規 aspiration thrombectomy **不優於**傳統 PCI
> 且**顯著增加中風風險**

### 重要數據
- Crossover: Thrombectomy → PCI alone **4.6%**
- Bailout thrombectomy in PCI-alone group: **7.1%** (355 pts)

### 中風風險機制推測
- 血栓碎片經主動脈弓 → 腦血管
- 導管操作增加 air/debris embolism

---

# IPD Meta-Analysis (2017)

**Thrombectomy Trialists Collaboration**
Jolly SS, James S, et al. *Circulation* 2017; 135: 143–152

- 納入所有 n ≥ 1,000 的 RCTs：**TAPAS + TASTE + TOTAL**
- **總病人數：19,047**

| 終點 | Aspiration | PCI alone | 結果 |
|------|-----------|-----------|------|
| CV death (30 d) | 2.4% | 2.9% | 無顯著差異 |
| Stroke/TIA (30 d) | — | — | Aspiration 組有增加趨勢 |

### 次族群分析
- **High thrombus burden**：CV death 有減少趨勢，但同時 stroke 風險增加
- 需權衡獲益與風險

---

# 現行指引建議

| 指引 | 常規使用 | 選擇性使用 |
|------|---------|-----------|
| **2021 ACC/AHA STEMI** | **Class III** (No Benefit), LOE A | — |
| **2017 ESC STEMI** | **Class III** (Not Recommended) | — |
| **日本循環器學會** | — | **Class IIb** |

---

# Take-Home Messages

1. **TAPAS 的陷阱**：小樣本 + surrogate endpoint → 過度樂觀 → 被大型試驗推翻
2. **常規使用無益**：TASTE + TOTAL + IPD meta-analysis 一致結論
3. **中風風險**：TOTAL 顯示 aspiration thrombectomy 顯著增加 stroke（HR 2.06）
4. **選擇性使用仍為 IIb**：High thrombus burden 時可考慮，但需權衡 stroke risk
5. **教訓**：Surrogate endpoint 的正面結果不應直接改變臨床實務，需以 clinical hard endpoint 為準

---

# 關鍵參考文獻

1. Svilaas T, et al. *NEJM* 2008; 358: 557–567 **(TAPAS)**
2. Vlaar PJ, et al. *Lancet* 2008; 371: 1915–1920 **(TAPAS 1-yr)**
3. Fröbert O, et al. *NEJM* 2013; 369: 1587–1597 **(TASTE)**
4. Lagerqvist B, et al. *NEJM* 2014; 371: 1111–1120 **(TASTE 1-yr)**
5. Jolly SS, et al. *NEJM* 2015; 372: 1389–1398 **(TOTAL)**
6. Jolly SS, et al. *Lancet* 2016; 387: 127–135 **(TOTAL 1-yr)**
7. Jolly SS, et al. *Circulation* 2017; 135: 143–152 **(IPD Meta-analysis)**
