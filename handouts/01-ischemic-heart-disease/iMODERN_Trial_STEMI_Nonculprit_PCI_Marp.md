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
footer: '謝慕揚 MD, PhD, FESC | iMODERN Trial | 2026'
---

<!-- _class: lead -->

# iMODERN Trial

## STEMI 多支血管病變：即時 vs. 延遲非罪犯病灶 PCI

**謝慕揚 MD, PhD, FESC**
資料來源：[*N Engl J Med*. 2026;394:958-68](https://doi.org/10.1056/NEJMoa2512918) | 2026-03-06

---

# 大綱

1. 研究背景與臨床問題
2. iMODERN 試驗設計
3. 主要結果
4. 與先前試驗比較
5. 臨床啟示與結論

---

<!-- _class: divider -->

# 研究背景

---

# STEMI 合併多支血管病變

- STEMI 病人中 **40-65%** 合併 multivessel disease
- 2025 ACC/AHA 指引建議 **complete revascularization** (Class 1A)
- **未解的問題**：非罪犯病灶何時處理最好？

| 策略 | 時機 | 優點 | 疑慮 |
|------|------|------|------|
| **即時 (Immediate)** | Primary PCI 時 | 一次解決、減少再住院 | 急性期風險、contrast load |
| **延遲 (Staged)** | 數日至數週後 | 可評估 ischemia、避免過度治療 | 等待期間事件風險 |

---

# 先前試驗回顧

| 試驗 | 年份 | 設計 | 結果 |
|------|------|------|------|
| **COMPLETE** | 2019 | Complete vs. culprit-only | Complete revascularization **獲益** |
| **BIOVASC** | 2023 | Immediate vs. staged | Immediate noninferior；24 月差異消失 |
| **MULTISTARS AMI** | 2023 | Immediate vs. staged | Immediate noninferior；主要獲益來自減少 unplanned revasc |
| **OPTION-STEMI** | 2024 | Immediate vs. deferred FFR | Immediate **未達** noninferiority |

> 先前試驗多為 noninferiority 設計，且 unplanned revascularization 佔終點一大部分

---

<!-- _class: divider -->

# iMODERN 試驗設計

---

# 試驗概述

- **全名**：iFR-Guided Multivessel Revascularization during PCI for AMI
- **設計**：國際多中心 (41 sites)、開放標籤、**superiority** RCT
- **收案**：2017/12 – 2022/02 (n = 1,146)
- **追蹤**：3 年

```text
STEMI + Successful Primary PCI + Nonculprit Lesion >50%
                    |
         Randomization 1:1
           /              \
    iFR Group (n=558)    MRI Group (n=588)
    即時 iFR 評估         6 週內 Cardiac Stress MRI
    iFR ≤0.89 → PCI      Ischemia → PCI
```

---

# 兩組策略比較

| 項目 | iFR Group | MRI Group |
|------|-----------|-----------|
| **評估工具** | Pressure wire (iFR) | 1.5T/3T cardiac stress MRI |
| **時機** | Primary PCI 當場 | 6 週內 |
| **介入標準** | iFR ≤ 0.89 | Perfusion defect (ischemia) |
| **Bailout** | — | 可用 iFR 作替代 |
| **Vasodilator** | 不需要 | Adenosine / Regadenoson |
| **Core lab** | 獨立 angiography core lab | Duke CMR Center |

---

# 主要終點

**Primary endpoint** (3 年):

全因死亡 + 再發 MI + 心衰住院

**Superiority design** — 假設即時 iFR-guided PCI 可減少事件

---

<!-- _class: divider -->

# 主要結果

---

# 介入治療比較

| 項目 | iFR Group | MRI Group |
|------|-----------|-----------|
| Ischemia testing 完成 | 97.3% (iFR) | 81.1% (MRI) + 11.1% (iFR bailout) |
| **陽性率** | **44.9%** | **20.2%** |
| **接受非罪犯病灶 PCI** | **42.6%** | **18.7%** |
| 非罪犯 PCI 中位時間 | 0 天 | 40 天 |
| 總支架數/病人 | 2.1 ± 1.4 | 1.8 ± 1.1 |

> **iFR 陽性率是 MRI 的 2.2 倍** — 導致更多 PCI，但結果並不更好

---

# 主要複合終點：無顯著差異

| 終點 (3 年) | iFR | MRI | HR (95% CI) |
|-------------|-----|-----|-------------|
| **主要複合終點** | **9.3%** | **9.8%** | **0.95 (0.65–1.40); P = 0.81** |
| 全因死亡 | 4.1% | 3.9% | 1.04 (0.58–1.88) |
| 再發 MI | 5.4% | 5.5% | 0.99 (0.59–1.64) |
| **心衰住院** | **0.6%** | **2.3%** | **0.24 (0.07–0.84)** |

> 即時 iFR-guided PCI **未優於**延遲 MRI-guided PCI

---

# 次要終點亮點

| 終點 (3 年) | iFR | MRI | HR (95% CI) |
|-------------|-----|-----|-------------|
| Cardiac death | 1.9% | 2.0% | 0.95 (0.40–2.23) |
| Target-lesion failure | 10.2% | 10.5% | 0.98 (0.68–1.42) |
| **Stroke / TIA** | **1.3%** | **3.7%** | **0.36 (0.15–0.86)** |
| Major bleeding | 1.9% | 1.1% | 1.73 (0.63–4.76) |
| Unplanned revasc | 8.6% | 8.4% | 1.03 (0.68–1.55) |
| Stent thrombosis | 1.7% | 0.6% | 3.12 (0.84–11.51) |

> Stroke/TIA 有利 iFR group；Stent thrombosis 有不利趨勢

---

# 亞組分析

- 所有預先指定亞組 (糖尿病、性別、年齡、anterior STEMI、LVEF、nonculprit 血管數) 結果一致
- **無任何亞組**顯示即時策略有顯著優越性
- Interaction P-values 皆不顯著

---

<!-- _class: divider -->

# 討論與臨床啟示

---

# 關鍵訊息：更多 PCI ≠ 更好結果

| 比較項目 | iFR Group | MRI Group |
|----------|-----------|-----------|
| 非罪犯病灶 PCI 率 | **42.6%** | **18.7%** |
| 3 年主要終點 | 9.3% | 9.8% |
| 差異 | **無** | **無** |

> MRI-guided 策略少做了 **一半以上的 PCI**，但 3 年臨床結果相同

---

# iFR vs. MRI：為何差異這麼大？

| 特性 | iFR | Cardiac Stress MRI |
|------|-----|--------------------|
| 測量原理 | Epicardial pressure gradient | Myocardial perfusion |
| 敏感度 | 較高 (small territories) | 較低 (may miss small ischemia) |
| 偽陽性風險 | STEMI 時基礎血流增加 → iFR 偏低 | 低 |
| 偽陰性風險 | 低 | 小範圍 ischemia 可能未偵測 |
| 需要 adenosine | 不需要 | 需要 |

> 兩種工具的 "ischemia threshold" 不同，但最終臨床結果無異

---

# 與先前試驗整合觀點

| 試驗 | Immediate vs. Deferred | 結論 |
|------|------------------------|------|
| BIOVASC | Immediate noninferior | 24 月差異消失 |
| MULTISTARS AMI | Immediate noninferior | 獲益來自 unplanned revasc |
| **OPTION-STEMI** | **Immediate 未達 noninferiority** | **支持延遲** |
| **iMODERN** | **Immediate 未達 superiority** | **支持延遲** |

> OPTION-STEMI + iMODERN 一致顯示：**即時策略並不優於延遲策略**

---

# 臨床實務建議

> **Pearl 1**: STEMI + multivessel disease — complete revascularization 有證據支持，但**不必急於在 primary PCI 時全部完成**

> **Pearl 2**: 延遲 ischemia-guided 策略 (MRI 或 iFR) 可在 6 週內安全執行，且可**減少 >50% 不必要的非罪犯病灶 PCI**

> **Pearl 3**: 即時 iFR group 心衰住院較低 (HR 0.24) 是值得關注的探索性發現，需後續研究確認

---

# Take-Home Messages

1. **Immediate iFR-guided PCI ≠ Superior** to deferred MRI-guided PCI (HR 0.95; P = 0.81)
2. **Ischemia testing 可減少不必要的 PCI** — MRI-guided 僅 18.7% vs. iFR-guided 42.6% 需要介入
3. **延遲策略安全可行** — 6 週內完成 ischemia assessment 不增加事件風險
4. **心衰住院有利即時策略** — 但為探索性結果，CI 寬

---

<!-- _class: small-text -->

# 參考文獻

1. Rao SV, et al. 2025 ACC/AHA ACS Guideline. [*Circulation*. 2025;151:e1-e197.](https://doi.org/10.1161/CIR.0000000000001309)
2. Mehta SR, et al. COMPLETE trial. [*N Engl J Med*. 2019;381:1411-21.](https://doi.org/10.1056/NEJMoa1907775)
3. Diletti R, et al. BIOVASC trial. [*Lancet*. 2023;401:1172-82.](https://doi.org/10.1016/S0140-6736(23)00351-1)
4. Stähli BE, et al. MULTISTARS AMI. [*N Engl J Med*. 2023;389:1368-79.](https://doi.org/10.1056/NEJMoa2304932)
5. Boscarelli D, et al. OPTION-STEMI. [*Eur Heart J*. 2024;45:3505-16.](https://pubmed.ncbi.nlm.nih.gov/38641031/)
6. Mehta SR, et al. FULL REVASC trial. [*N Engl J Med*. 2024;391:2113-24.](https://doi.org/10.1056/NEJMoa2404415)
7. Nijveldt R, et al. iMODERN trial. [*N Engl J Med*. 2026;394:958-68.](https://doi.org/10.1056/NEJMoa2512918)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
