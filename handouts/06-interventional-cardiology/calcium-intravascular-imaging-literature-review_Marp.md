---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Noto Sans TC', 'Microsoft JhengHei', sans-serif;
    font-size: 24px;
  }
  h1 { color: #1a5276; font-size: 40px; }
  h2 { color: #2e86c1; font-size: 32px; }
  h3 { color: #1a5276; font-size: 26px; }
  table { font-size: 20px; margin: auto; }
  th { background-color: #8e44ad; color: white; }
  blockquote { border-left: 4px solid #e74c3c; padding-left: 16px; color: #555; font-size: 20px; }
  .columns { display: flex; gap: 30px; }
  .col { flex: 1; }
  footer { font-size: 14px; color: #888; }
footer: 'Coronary Calcium & Intravascular Imaging — Journal Reading | 謝慕揚'
---

# Coronary Calcium & Intravascular Imaging
## 冠狀動脈鈣化與血管內影像——文獻整理

**Journal Reading Handout**
謝慕揚 Mu-Yang Hsieh, MD
心臟血管內科 | 新竹臺大分院

> 最後更新：2026-03-14

---

# Overview

- 冠狀動脈鈣化（CAC）是 PCI 中最具挑戰的病灶型態
- 與 stent underexpansion、procedural complications、較差長期預後相關
- **Intravascular imaging（IVI）** = IVUS + OCT
- 2025 ACC/AHA/SCAI：IVI 在 complex PCI 升級為 **Class I**
- 新方向：IVI 從「PCI 治療指引」擴展至「vulnerable plaque 辨識與預防性介入」

---

# 文獻演進時間軸 (1/2)

```
2011  PROSPECT I            → Non-culprit vulnerable plaque 自然史（NEJM）
2018  ULTIMATE Trial        → IVUS-guided DES 優於 angiography
2020  PROSPECT ABSORB       → Vulnerable plaque preventive PCI pilot
2021  PROSPECT II           → NIRS-IVUS 辨識高風險斑塊
      COMBINE OCT-FFR       → FFR + OCT 結合——TCFA ↑5x MACE
      LEMON                 → OCT-guided LM PCI 可行性 pilot
2023  RENOVATE-COMPLEX-PCI  → IVI 在 complex lesions 優於 angio（NEJM）
      ILUMIEN IV            → OCT procedural ✓, clinical 中性（NEJM）
      OCTOBER               → OCT 在 bifurcation 降低 MACE（NEJM）
      OCTIVUS               → OCT ≈ IVUS 非劣性（Circulation）
```

---

# 文獻演進時間軸 (2/2)

```
2024  IVUS-ACS              → IVUS 在 ACS 改善預後（Lancet）
      OCCUPI                → OCT 在 complex lesions 降低 MACE（Lancet）
      PREVENT               → Preventive PCI for vulnerable plaque（Lancet）
2025  ECLIPSE IVI Sub       → IVI 在嚴重鈣化降低 TVF（JACC Interv）
      CALIPSO               → OCT + algorithm 在鈣化改善 MSA（JAMA Cardiol）
      指引升級               → IVI 在 complex PCI 升至 Class I
進行中 COMBINE-INTERVENE     → FFR + OCT-guided vs. FFR-alone
      INTERCLIMA            → OCT morphology vs. functional-guided
      VULNERABLE            → STEMI non-culprit vulnerable plaque
```

---

# Part I: IVI-Guided PCI 里程碑 RCTs

---

# RENOVATE-COMPLEX-PCI (2023)

**IVI vs. Angiography-guided PCI 在 complex lesions 的首個大型 RCT**
Hahn JY, et al. *NEJM* 2023; 388: 1668–1679

- **n = 1,639** | IVI 1,092 vs. Angio 547（2:1 隨機）
- IVI 選擇：IVUS 75%, OCT 25%
- 追蹤：中位 2.1 年

| 終點 | IVI | Angio | HR (95% CI) | p |
|------|-----|-------|-------------|---|
| **Primary composite** | **7.7%** | **12.3%** | **0.64 (0.45–0.89)** | **0.008** |
| Cardiac death | 1.7% | 3.8% | — | — |
| TV-MI | 3.7% | 5.6% | — | — |

> **5 年追蹤亦持續確認 IVI 的優勢**

---

# ILUMIEN IV (2023)

**OCT vs. Angiography-guided PCI（DM or complex lesions）**
Ali ZA, et al. *NEJM* 2023; 389: 1466–1480

- **n = 2,487** | 80 sites, 18 countries
- **Procedural endpoint**：Post-PCI MSA → OCT 組顯著較大 ✓
- **Clinical endpoint（2 yr TVF）**：**中性結果** ✗

### 解讀
- 納入之 lesion complexity 可能較低
- Substudy（2024）：complex lesion subset 中 OCT 有較大 MSA 優勢
- **提示 IVI 臨床獲益可能與 lesion complexity 成正比**

---

# OCTOBER (2023)

**OCT-guided PCI 在 bifurcation lesions 的首個 RCT**
Holm NR, et al. *NEJM* 2023; 389: 1477–1487

- **n = 1,201** | Left main ~19%
- 追蹤：中位 2 年

| 終點 | OCT | Angio | HR (95% CI) | p |
|------|-----|-------|-------------|---|
| **Primary MACE (2 yr)** | **10.1%** | **14.1%** | **0.70 (0.50–0.98)** | **0.035** |

> OCT-guided PCI 在 bifurcation 中顯著降低 MACE

---

# OCTIVUS (2023) & IVUS-ACS (2024)

<div class="columns">
<div class="col">

### OCTIVUS — OCT vs. IVUS
*Circulation* 2023; 148: 1195–1206

- **n = 2,008**
- 1 yr MACE: OCT 2.5% vs. IVUS 3.1%
- **非劣性成立** (p < 0.001)
- OCT ≈ IVUS

</div>
<div class="col">

### IVUS-ACS
*Lancet* 2024; 403: 1855–1865

- **n = 3,505** ACS 病人
- IVUS 1,753 vs. Angio 1,752
- 58 centers
- **IVUS 在 ACS 中改善預後**

</div>
</div>

---

# OCCUPI (2024)

**OCT-guided PCI 在 complex lesions**
Kim BK, et al. *Lancet* 2024; 404: 1029–1039

- **n = 1,604** | 20 hospitals, South Korea

| 終點 | OCT | Angio | HR (95% CI) |
|------|-----|-------|-------------|
| **Primary composite** | **4.6%** | **7.4%** | **0.62 (0.41–0.93)** |
| Spontaneous MI | 0.9% | 2.4% | 0.36 (0.15–0.86) |

- OCT 優化後 primary endpoint 僅 **2.9%** vs. 未優化 8.6% (HR 0.33)

> **優化程度直接影響預後**

---

# Part II: 鈣化病灶專屬證據

---

# ECLIPSE IVI Sub-analysis (2025)

**嚴重鈣化病灶中最大的 IVI 分析**
*JACC Cardiovasc Interv* 2025; 18(19): 2338–2351

- **n = 2,005** 嚴重鈣化病灶
- IVI 使用率 62.1%（OCT 40.3%, IVUS 25.6%）

| 終點 | OCT vs. Non-OCT | HR (95% CI) |
|------|-----------------|-------------|
| TVF | 7.2% vs. 12.2% | **0.57 (0.40–0.81)**, p = 0.002 |
| Adjusted TVF | — | **0.68 (0.55–0.84)**, p = 0.0003 |

- OCT vs. IVUS 校正後無顯著差異
- **結論：IVI 在嚴重鈣化應常規使用**

---

# CALIPSO Trial (2025)

**OCT-guided PCI 在鈣化病灶的首個專門 RCT**
*JAMA Cardiology* 2025

- 多中心（12 sites, France）
- 中重度鈣化病灶
- OCT 組搭配 **predefined calcium management algorithm**
- 主要終點：Post-PCI MSA（OCT 組顯著優勢）

### 限制
- 未以臨床硬終點為 primary outcome
- 需更大規模試驗驗證

> 目前尚無專門針對鈣化病灶、以 clinical endpoint 為主的大型 RCT

---

# Part III: 鈣化評估方法

---

# IVI 鈣化評估：IVUS vs. OCT

<div class="columns">
<div class="col">

### IVUS
- **IVUS-Based Calcium Score**（4 項各 1 分）：
  1. Superficial arc > 270° for ≥ 5 mm
  2. 360° circumferential calcium
  3. Calcified nodule
  4. Vessel diameter < 3.5 mm
- **Score ≥ 2** → calcium modification
- 可偵測 deep calcium
- 不需 contrast → 適用 CKD

</div>
<div class="col">

### OCT
- 解析度 **10–20 μm**（IVUS: 100–200 μm）
- 可精確測量 calcium **thickness, arc, length**
- 可偵測 **calcium fracture**（確認 modification 效果）
- 限制：穿透深度 1–2 mm、需 contrast flush

</div>
</div>

---

# Calcium Modification 技術

| 技術 | 機制 | 作用深度 | 關鍵試驗 |
|------|------|---------|---------|
| **Rotational Atherectomy** | 高速鑽石磨頭 | 表層 | — |
| **Orbital Atherectomy** | 離心力磨除 | 表層 | ECLIPSE (*Lancet* 2025) |
| **IVL** | 聲波震碎 | 表層 + 深層 | DISRUPT CAD I–IV |
| **Rotatripsy** | RA + IVL 合併 | 表層 + 深層 | Case series |

- DISRUPT CAD I–IV：single-arm，success 92.4%，30-day MACE 7.8%
- ECLIPSE：OA **未能**顯示優於 balloon angioplasty（TVF 11.5% vs. 10.0%）

> **最佳 calcium modification 策略尚無定論**

---

# Part IV: FFR + OCT / Vulnerable Plaque

---

# Paradigm Shift：從缺血到斑塊型態

### 傳統：Ischemia-Driven
- FFR ≤ 0.80 → PCI
- FFR > 0.80 → OMT

### 新方向：Plaque Morphology-Driven
- FFR-negative 的 non-flow-limiting 病灶仍可能因 **plaque vulnerability** 導致未來事件
- OCT / IVUS 可辨識：
  - **Thin-cap fibroatheroma (TCFA)**
  - Lipid-rich plaque
  - Healed plaque

> **「不缺血」≠「安全」**

---

# COMBINE OCT-FFR (2021)

**FFR + OCT 結合風險分層**
Kedhi E, et al. *Eur Heart J* 2021; 42: 4671–4679

- 糖尿病患者 | FFR-negative non-culprit lesions 行 OCT

| 組別 | 18 個月 MACE | HR (95% CI) |
|------|-------------|-------------|
| FFR-neg + **TCFA+** | **13.3%** | **4.65 (1.99–10.89)**, p < 0.001 |
| FFR-neg + TCFA− | 3.1% | reference |

- TCFA 是 MACE **最強預測因子**（HR 5.12）
- 5 年 post-hoc：≥ 2 項 OCT vulnerability features → 風險累加

> **即使 FFR 說「不缺血」，TCFA 使 MACE 風險增加 ~5 倍**

---

# PREVENT Trial (2024)

**Preventive PCI for Vulnerable Plaque 的里程碑 RCT**
Park SJ, et al. *Lancet* 2024; 403: 1753–1765

- **n = 1,606** | FFR > 0.80 + IVI vulnerable plaque
- Vulnerable plaque 定義（≥ 2 項）：MLA ≤ 4.0 mm², PB > 70%, TCFA, lipid-rich

| 終點 | Preventive PCI | OMT alone | HR (95% CI) | p |
|------|---------------|-----------|-------------|---|
| **2 yr** | **0.4%** | **3.4%** | **0.11 (0.03–0.36)** | **0.0003** |
| **4.3 yr** | **6.5%** | **9.4%** | **0.54 (0.33–0.87)** | **0.009** |

> **首度以 RCT 證實：對 FFR-negative vulnerable plaque 行 preventive PCI 可改善預後**

---

# 現行指引建議

| 指引 | IVI 在 Complex/Calcified PCI | 等級 |
|------|------------------------------|------|
| **2025 ACC/AHA/SCAI ACS** | 建議使用 IVUS 或 OCT 指引 PCI | **Class I** |
| **2024 ESC Guidelines** | LM & complex lesions 使用 IVI | **Class I** (↑ from IIa) |

---

# 研究限制

1. **鈣化專屬臨床試驗不足** — CALIPSO 僅以 imaging endpoint 為主
2. **OCT vs. IVUS 在鈣化病灶的 head-to-head 比較不足**
3. **Calcium modification 策略缺乏 randomized evidence**
4. **Imaging-defined optimization 依從性低**（僅 ~45%）
5. **IVI 臨床採用率仍低** — 美國僅 ~20–25%
6. 大多數試驗為 open-label，女性比例偏低

---

# 未來方向

1. **鈣化專屬大型 RCT**（clinical hard endpoint）
   - BALI (n=200), ROLLERCOASTER (n=150)
2. **AI 自動化影像分析** — 克服 expertise 門檻
3. **改良鈣化評分系統** — revised OCT-derived calcium score
4. **Hybrid imaging** — OCT + IVUS co-registration / dual catheter
5. **Vulnerable plaque 預防介入** — PREVENT 的延伸
6. **個人化 calcium modification algorithm**
7. **Real-world evidence** — 更多女性、高齡、CKD 患者

---

# Take-Home Messages

1. **IVI-guided PCI 在 complex lesions 已有 Class I 證據**
   - RENOVATE, OCTOBER, OCCUPI 一致正面
2. **OCT ≈ IVUS**（OCTIVUS noninferiority），各有優劣
3. **鈣化病灶專屬的高品質 RCT 仍不足**
4. **Calcium modification 最佳策略尚無定論**（IVL vs. RA vs. OA）
5. **Paradigm shift**：FFR-negative + TCFA → 5x MACE → preventive PCI 有效 (PREVENT)
6. **優化依從性**是影響預後的關鍵

---

# 關鍵參考文獻 (1/2)

### IVI-Guided PCI
1. Hahn JY, et al. *NEJM* 2023; 388: 1668–1679 **(RENOVATE)**
2. Ali ZA, et al. *NEJM* 2023; 389: 1466–1480 **(ILUMIEN IV)**
3. Holm NR, et al. *NEJM* 2023; 389: 1477–1487 **(OCTOBER)**
4. Kang DY, et al. *Circulation* 2023; 148: 1195–1206 **(OCTIVUS)**
5. Li X, et al. *Lancet* 2024; 403: 1855–1865 **(IVUS-ACS)**
6. Kim BK, et al. *Lancet* 2024; 404: 1029–1039 **(OCCUPI)**
7. ECLIPSE. *Lancet* 2025; 405: 1240–1251
8. CALIPSO. *JAMA Cardiol* 2025

---

# 關鍵參考文獻 (2/2)

### FFR + OCT / Vulnerable Plaque
9. Stone GW, et al. *NEJM* 2011; 364: 226–235 **(PROSPECT I)**
10. Erlinge D, et al. *Lancet* 2021; 397: 985–995 **(PROSPECT II)**
11. Stone GW, et al. *JACC* 2020 **(PROSPECT ABSORB)**
12. Kedhi E, et al. *Eur Heart J* 2021; 42: 4671–4679 **(COMBINE OCT-FFR)**
13. Park SJ, et al. *Lancet* 2024; 403: 1753–1765 **(PREVENT)**
