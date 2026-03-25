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
  table { font-size: 0.68em; width: 100%; }
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
  section.small-text { font-size: 0.78em; }
  section.tiny-text { font-size: 0.72em; }
  section.tiny-text table { font-size: 0.62em; }
footer: '謝慕揚 MD, PhD, FESC | STEMI Multivessel PCI Trials Comparison | 2026'
---

<!-- _class: lead -->

# STEMI 多支血管病變
# 非罪犯病灶 PCI 時機

## 五大隨機對照試驗的方法學比較與臨床整合

**謝慕揚 MD, PhD, FESC**
2026-03-06

---

# 臨床問題的演進

```text
第一階段：Should we treat nonculprit lesions at all?
  → PRAMI (2013), CvLPRIT (2015), DANAMI-3 (2015), COMPLETE (2019)
  → 答案：YES — Complete revascularization 優於 culprit-only

第二階段：When should we treat? Immediate vs. Staged?
  → BIOVASC (2023), MULTISTARS AMI (2023)
  → 答案：Immediate appears noninferior

第三階段：Does physiology-guided timing matter?
  → OPTION-STEMI (2024), iMODERN (2026)
  → 答案：Immediate NOT superior; deferred is safe
```

---

<!-- _class: divider -->

# 五大試驗總覽

---

<!-- _class: tiny-text -->

# 基本試驗資訊比較

| 項目 | COMPLETE | BIOVASC | MULTISTARS AMI | OPTION-STEMI | iMODERN |
|------|----------|---------|----------------|--------------|---------|
| **第一作者** | Mehta SR | Diletti R | Stähli BE | Boscarelli D | Nijveldt R |
| **期刊** | *N Engl J Med* | *Lancet* | *N Engl J Med* | *Eur Heart J* | *N Engl J Med* |
| **年份** | 2019 | 2023 | 2023 | 2024 | 2026 |
| **收案人數** | **4,041** | 1,525 | 840 | 885 | 1,146 |
| **收案期間** | 2013–2017 | 2018–2022 | 2018–2022 | 2018–2023 | 2017–2022 |
| **中心數** | 140 sites | 27 sites | 37 sites | 14 sites | 41 sites |
| **國家** | 31 國 | 6 國 | 7 國 | 5 國 | 多國 |
| **註冊號** | NCT01740479 | NCT03621501 | NCT03135275 | NCT03338999 | NCT03298659 |

> **COMPLETE** 是最大規模試驗 (N=4,041)，奠定 complete revascularization 的基礎

---

<!-- _class: divider -->

# 方法學比較

---

<!-- _class: tiny-text -->

# 研究設計與族群

| 項目 | COMPLETE | BIOVASC | MULTISTARS AMI | OPTION-STEMI | iMODERN |
|------|----------|---------|----------------|--------------|---------|
| **設計** | **Superiority** | **Noninferiority** | **Noninferiority** | **Noninferiority** | **Superiority** |
| **盲性** | Open-label | Open-label | Open-label | Open-label | Open-label |
| **族群** | STEMI only | ACS (STEMI + NSTEMI) | STEMI only | STEMI only | STEMI only |
| **NSTEMI 比例** | 0% | **~60%** | 0% | 0% | 0% |
| **比較** | Complete vs. culprit-only | Immediate vs. staged | Immediate vs. staged | Immediate vs. deferred FFR | Immediate iFR vs. deferred MRI |
| **追蹤** | Median 3 yr | 1 yr (→ 24 mo) | 1 yr | 1 yr | **3 yr** |
| **分析方法** | ITT | ITT | ITT | ITT | ITT |

> 注意：BIOVASC 納入 ~60% NSTEMI，與其他四個純 STEMI 試驗不同

---

<!-- _class: tiny-text -->

# 介入策略的關鍵差異

| 項目 | COMPLETE | BIOVASC | MULTISTARS AMI | OPTION-STEMI | iMODERN |
|------|----------|---------|----------------|--------------|---------|
| **介入指引** | Angiography | Angiography | Angiography | **FFR** | **iFR + MRI** |
| **介入標準** | ≥70% (or 50-69% + FFR) | Visual ≥70% | ≥70% visual | FFR ≤ 0.80 | iFR ≤ 0.89 / MRI ischemia |
| **Immediate 時機** | — | Index procedure | Index procedure | Index procedure | Index procedure |
| **Deferred 時機** | Staged (median 23 days) | Within 6 weeks | 19–45 days | 1–5 days (same hospitalization) | Within 6 weeks |
| **Physiology 使用** | Optional (50-69%) | No | No | **Mandatory (FFR)** | **Mandatory (iFR/MRI)** |

> OPTION-STEMI 與 iMODERN 是唯二「**physiology-first**」的試驗

---

# Immediate vs. Deferred：時間定義差異

```text
               Index PCI    24hr    住院中    1-5天    2-6週    19-45天
                  |          |       |        |        |        |
COMPLETE:         culprit ─────────────────────────── staged ──────
                                                    (median 23d)

BIOVASC:        immediate ─────────────────────────── staged ──────
                (index PCI)                          (within 6wk)

MULTISTARS AMI: immediate ─────────────────────────── staged ──────
                (index PCI)                          (19-45 days)

OPTION-STEMI:   immediate ──── deferred ───
                (index PCI)   (1-5 days, same hospitalization)

iMODERN:        immediate ─────────────────────────── deferred ────
                (index PCI)                          (within 6wk)
```

> OPTION-STEMI 的 "deferred" 僅延遲 1-5 天；其餘試驗延遲 3-6 週

---

<!-- _class: tiny-text -->

# 主要終點定義比較

| 試驗 | 主要終點成分 | 包含 Unplanned Revasc? | 追蹤時間 |
|------|-------------|----------------------|----------|
| **COMPLETE** | CV death + MI | **否** | 3 年 |
| **BIOVASC** | All-cause death + MI + stroke + **unplanned revasc** | **是** | 1 年 |
| **MULTISTARS AMI** | All-cause death + MI + stroke + **unplanned revasc** + HF hosp | **是** | 1 年 |
| **OPTION-STEMI** | All-cause death + MI + **unplanned revasc** | **是** | 1 年 |
| **iMODERN** | All-cause death + MI + HF hospitalization | **否** | 3 年 |

> **COMPLETE** 與 **iMODERN** 使用 hard endpoints (不含 unplanned revascularization)
> BIOVASC、MULTISTARS AMI、OPTION-STEMI 的主要終點含 unplanned revasc — 此為**主觀終點**，open-label 設計下易受偏差影響

---

# 為什麼終點定義如此重要？

| 試驗 | 主要複合終點差異 | 其中 Unplanned Revasc 貢獻 |
|------|-----------------|---------------------------|
| **MULTISTARS AMI** | 8.5% vs. 16.3% (顯著) | 主要差異來源：**4.4% vs. 11.1%** |
| **BIOVASC** | 7.6% vs. 9.4% (noninferior) | 部分貢獻 |

> **Pearl**: 當主要終點包含 unplanned revascularization 時，即時策略天然有利 — 因為 staged group 等待期間的任何介入都可能被計算為「unplanned」

> 這也是 **COMPLETE** 與 **iMODERN** 刻意排除此終點的原因

---

<!-- _class: divider -->

# 結果比較

---

<!-- _class: tiny-text -->

# 主要終點結果一覽

| 試驗 | 介入組 | 對照組 | HR / 差異 | P 值 | 結論 |
|------|--------|--------|-----------|------|------|
| **COMPLETE** | 7.8% (complete) | 10.5% (culprit-only) | HR 0.74 (0.60–0.91) | **0.004** | Complete revasc **獲益** |
| **BIOVASC** | 7.6% (immediate) | 9.4% (staged) | Diff −1.8% (upper CI 0.9%) | Noninferior | Immediate **noninferior** |
| **MULTISTARS AMI** | 8.5% (immediate) | 16.3% (staged) | HR 0.55 (0.36–0.84) | **<0.001** NI | Immediate **noninferior + superior** |
| **OPTION-STEMI** | 5.3% (immediate) | 4.1% (deferred) | HR 1.31 (upper CI 2.42) | NI **not met** | Immediate **未達 noninferiority** |
| **iMODERN** | 9.3% (iFR) | 9.8% (MRI) | HR 0.95 (0.65–1.40) | 0.81 | Immediate **未優於** deferred |

---

# 各試驗 Hard Endpoints 比較

| 終點 | COMPLETE | BIOVASC | MULTISTARS AMI | OPTION-STEMI | iMODERN |
|------|----------|---------|----------------|--------------|---------|
| **全因死亡** | 2.9% vs 3.5% | 2.2% vs 2.0% | 1.4% vs 2.4% | 1.6% vs 1.1% | 4.1% vs 3.9% |
| **MI** | 5.4% vs 7.9% | 3.0% vs 3.4% | 1.9% vs 2.6% | 1.6% vs 1.1% | 5.4% vs 5.5% |
| **CV death + MI** | **7.8% vs 10.5%** | 4.7% vs 5.2% | 3.1% vs 4.0% | NR | — |
| **HF 住院** | NR | NR | 0.7% vs 1.2% | NR | **0.6% vs 2.3%** |

> Hard endpoints (死亡 + MI) 在大多數試驗中差異不大；COMPLETE 是唯一在 hard endpoints 達到顯著的試驗

---

<!-- _class: tiny-text -->

# 非罪犯病灶 PCI 執行率

| 試驗 | 介入組 PCI 率 | 對照組 PCI 率 | 差距 | 指引方式 |
|------|--------------|--------------|------|----------|
| **COMPLETE** | 100% (by design) | ~2% (crossover) | 98% | Angiography |
| **BIOVASC** | ~97% | ~94% | ~3% | Angiography |
| **MULTISTARS AMI** | ~96% | ~93% | ~3% | Angiography |
| **OPTION-STEMI** | 65.5% (FFR+) | 64.3% (FFR+) | ~1% | FFR |
| **iMODERN** | **42.6%** (iFR+) | **18.7%** (MRI+) | **23.9%** | iFR / MRI |

> **iMODERN** 兩組 PCI 率差異最大 (42.6% vs. 18.7%)，反映 iFR 與 MRI 對 ischemia 偵測的根本差異

> Angiography-guided 試驗幾乎所有非罪犯病灶都接受 PCI；physiology-guided 試驗則大幅篩掉不需介入的病灶

---

<!-- _class: divider -->

# 方法學剖析

---

# Angiography-Guided vs. Physiology-Guided

| 特性 | Angiography-Guided | Physiology-Guided |
|------|-------------------|-------------------|
| **代表試驗** | COMPLETE, BIOVASC, MULTISTARS | OPTION-STEMI, iMODERN |
| **介入決策** | 視覺評估狹窄程度 | 功能性缺血評估 |
| **介入閾值** | ≥70% stenosis | FFR ≤0.80 / iFR ≤0.89 / MRI ischemia |
| **PCI 率** | 高 (>90%) | 低 (18-65%) |
| **優點** | 簡單直接 | 避免過度治療 |
| **疑慮** | 可能過度介入 | STEMI 急性期生理值可能不準 |

> Physiology-guided 策略**大幅減少 PCI 率**，但臨床結果與 angiography-guided 相當

---

# 非罪犯病灶 Ischemia 評估工具比較

| 工具 | FFR | iFR | Cardiac Stress MRI |
|------|-----|-----|--------------------|
| **原理** | Pressure-based (adenosine) | Pressure-based (resting) | Perfusion-based |
| **閾值** | ≤ 0.80 | ≤ 0.89 | Perfusion defect |
| **需要 Adenosine** | **是** | 否 | **是** (vasodilator) |
| **STEMI 考量** | 反應減弱 → 偽陰性 | 基礎流量增加 → 偽陽性 (~11%) | 較不受急性期影響 |
| **時機** | 即時或延遲 | 即時可行 | 需延遲 (通常 2-6 週) |
| **陽性率 (iMODERN)** | — | **44.9%** | **20.2%** |
| **侵入性** | 侵入性 | 侵入性 | **非侵入性** |

---

# Noninferiority vs. Superiority 設計的影響

| 設計 | 意義 | 結果解讀 |
|------|------|----------|
| **Superiority** | H₀: 兩組無差異；拒絕 → 新策略較優 | 需 P < 0.05 才能宣稱優越 |
| **Noninferiority** | H₀: 新策略劣於對照；拒絕 → 新策略不劣於 | 需 upper CI < margin |

| 試驗 | 設計 | 結果 |
|------|------|------|
| COMPLETE | Superiority | **Positive** — Complete revasc 優於 culprit-only |
| BIOVASC | Noninferiority (margin 4%) | **Met** NI |
| MULTISTARS AMI | Noninferiority (margin 6.3%) | **Met** NI + superiority |
| OPTION-STEMI | Noninferiority (margin HR 1.88) | **Not met** |
| iMODERN | Superiority | **Negative** — 即時未優於延遲 |

> MULTISTARS AMI 的 NI margin (6.3%) 較寬鬆，部分學者認為不夠嚴格

---

<!-- _class: divider -->

# 臨床整合分析

---

# 三個層次的臨床問題

```text
問題一：Should we do complete revascularization?
┌─────────────────────────────────────┐
│  COMPLETE: YES (HR 0.74, P=0.004)  │  → 強烈支持
│  Meta-analyses: YES                 │
└─────────────────────────────────────┘

問題二：Immediate or staged?
┌─────────────────────────────────────────────────┐
│  BIOVASC: Immediate noninferior                 │
│  MULTISTARS AMI: Immediate noninferior          │  → 兩者皆可
│  OPTION-STEMI: Immediate NOT noninferior        │
│  iMODERN: Immediate NOT superior                │
└─────────────────────────────────────────────────┘

問題三：Physiology-guided or angiography-guided?
┌─────────────────────────────────────────────────┐
│  FLOWER-MI (2021): FFR vs. angio — 無差異       │
│  FULL REVASC (2024): FFR vs. culprit-only — 中性│  → 尚無定論
│  iMODERN: iFR vs. MRI — PCI 率差 2x, 結果同    │
└─────────────────────────────────────────────────┘
```

---

# 矛盾結果的解讀

## 為什麼 BIOVASC / MULTISTARS 支持即時，而 OPTION-STEMI / iMODERN 不支持？

| 可能原因 | 說明 |
|----------|------|
| **終點定義** | 含 unplanned revasc 的試驗天然有利 immediate group |
| **Deferred 時間** | OPTION-STEMI 僅延遲 1-5 天 (同次住院)，其餘 3-6 週 |
| **Physiology 使用** | 有 physiology 的試驗可篩掉不需介入的病灶 |
| **NSTEMI 比例** | BIOVASC 含 60% NSTEMI — 非罪犯病灶辨識更困難 |
| **NI margin 寬鬆** | MULTISTARS AMI margin 6.3%，可能不夠嚴格 |
| **事件率** | iMODERN 事件率低於預期，power 不足 |

---

# 從證據到實務：決策流程

```text
STEMI + Multivessel Disease + Successful Primary PCI
                    |
    ┌───────────────┴───────────────┐
    │                               │
  血行動力學穩定?                   血行動力學不穩定?
    │                               │
    ├── 非罪犯病灶明顯              └── 僅處理 culprit
    │   (>90% stenosis)?                 考慮 IABP/ECMO
    │   → 可即時處理
    │
    ├── 狹窄 50-90%?
    │   → 兩種合理策略:
    │   ┌──────────────────────────────────────┐
    │   │ A) 即時 physiology-guided PCI         │
    │   │    (iFR/FFR → 陽性才 PCI)            │
    │   │                                      │
    │   │ B) 延遲 ischemia-guided PCI          │
    │   │    (MRI/FFR/iFR within 6 weeks)      │
    │   └──────────────────────────────────────┘
    │
    └── 兩種策略結果相當 (iMODERN)
```

---

# 各策略的利弊權衡

| 考量因素 | 傾向即時 (Immediate) | 傾向延遲 (Staged) |
|----------|---------------------|-------------------|
| **單次手術** | 減少再次 catheterization | — |
| **Contrast volume** | — | 分次降低 contrast 用量 |
| **AKI 風險** | 可能增加 | 較低 |
| **精準度** | STEMI 急性期生理值不穩 | 恢復後評估更準確 |
| **病人偏好** | 一次解決 | 有時間考慮 |
| **心衰住院** | iMODERN: HR 0.24 (探索性) | — |
| **Stent thrombosis** | — | iMODERN: 趨勢較低 |
| **等待期間風險** | 無等待 | 極低 (iMODERN 兩組事件率相當) |

---

# 2025 ACC/AHA 指引建議

| 建議 | Class | LOE |
|------|-------|-----|
| STEMI + multivessel disease → **complete revascularization** | **I** | **A** |
| 非罪犯病灶 PCI **during primary PCI** may be preferable to staged | **IIa** | **B-R** |

> 指引更新主要基於 BIOVASC 與 MULTISTARS AMI
> **iMODERN 與 OPTION-STEMI 的結果挑戰了「即時優先」的建議**

---

<!-- _class: divider -->

# 總結與 Take-Home Messages

---

# Take-Home Messages

> **1.** Complete revascularization 在 STEMI + multivessel disease 是**確立的標準**，但**何時做、如何選**仍有彈性

> **2.** 含 unplanned revascularization 的試驗偏好即時策略；用 hard endpoints 的試驗 (COMPLETE, iMODERN) 則顯示**延遲策略安全可行**

> **3.** Physiology-guided 策略可**大幅減少不必要的 PCI** (iMODERN: 42.6% vs. 18.7%)，且不犧牲臨床預後

> **4.** 閱讀文獻時務必注意：**終點定義、NI margin、族群差異 (STEMI vs. NSTEMI)、deferred 時間定義**

---

<!-- _class: small-text -->

# 參考文獻

1. Mehta SR, et al. Complete Revascularization with Multivessel PCI for MI (COMPLETE). [*N Engl J Med*. 2019;381:1411-21.](https://doi.org/10.1056/NEJMoa1907775)
2. Diletti R, et al. Immediate vs staged complete revascularisation in ACS (BIOVASC). [*Lancet*. 2023;401:1172-82.](https://doi.org/10.1016/S0140-6736(23)00351-1)
3. Stähli BE, et al. Timing of Complete Revascularization (MULTISTARS AMI). [*N Engl J Med*. 2023;389:1368-79.](https://doi.org/10.1056/NEJMoa2304932)
4. Boscarelli D, et al. Timing of FFR-guided Complete Revascularization (OPTION-STEMI). [*Eur Heart J*. 2024;45:3505-16.](https://pubmed.ncbi.nlm.nih.gov/38641031/)
5. Nijveldt R, et al. Immediate or Deferred Nonculprit-Lesion PCI (iMODERN). [*N Engl J Med*. 2026;394:958-68.](https://doi.org/10.1056/NEJMoa2512918)
6. Mehta SR, et al. FFR-Guided Complete Nonculprit Revascularization (FULL REVASC). [*N Engl J Med*. 2024;391:2113-24.](https://doi.org/10.1056/NEJMoa2404415)
7. Puymirat E, et al. FFR-Guided vs Angiography-Guided PCI (FLOWER-MI). [*N Engl J Med*. 2021;385:306-15.](https://doi.org/10.1056/NEJMoa2104650)
8. Rao SV, et al. 2025 ACC/AHA ACS Guideline. [*Circulation*. 2025;151:e1-e197.](https://doi.org/10.1161/CIR.0000000000001309)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
