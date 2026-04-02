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
footer: '謝慕揚 MD, PhD, FESC | Digital Twin VT Ablation | 2026'
---

<!-- _class: lead -->

# Digital Twin–Guided Ablation for Ventricular Tachycardia
## 數位孿生引導心室頻脈消融術

**TWIN-VT Study | NEJM 2026;394:1345-1347**
**整理：謝慕揚 MD, PhD, FESC | 2026-04-02**
[原文連結 — doi.org/10.1056/NEJMc2517822](https://doi.org/10.1056/NEJMc2517822)

---

<!-- _class: divider -->

# 研究概述

---

# 研究背景

- 缺血性心肌病 (ischemic cardiomyopathy) 患者之 **VT** 源自慢性 MI scar 內的 **reentrant circuits**
- 傳統 VT ablation 依賴術中 electroanatomical mapping，消融範圍大、耗時長
- **Digital twin** 技術：術前以電腦模擬預測 VT 迴路，實現精準消融

> **核心概念**：利用病人專屬心臟數位孿生 (patient-specific cardiac digital twin) 於術前規劃最小有效消融靶點

---

# TWIN-VT 研究設計

| 項目 | 內容 |
|------|------|
| 研究類型 | 前瞻性單中心研究 (prospective single-center) |
| 登錄號 | NCT03536052 |
| 法規核准 | **FDA investigational device exemption** |
| 收案人數 | **10** 位受試者 |
| 適應症 | 缺血性心肌病合併 VT |
| 研究機構 | Johns Hopkins University |

---

<!-- _class: divider -->

# 研究方法

---

# Digital Twin 工作流程

```text
Step 1: Contrast-enhanced cardiac MRI (CE-CMR)
        擷取心臟結構與疤痕分布
            |
Step 2: 建構 cardiac digital twin
        生成病人專屬心臟三維模型
            |
Step 3: Virtual VT induction — rapid pacing
        模擬所有可能的 VT reentrant circuits
            |
Step 4: Virtual ablation
        找出 minimal effective ablation targets
            |
Step 5: Import targets → electroanatomical mapping system
            |
Step 6: Clinical catheter ablation
```

---

# 技術關鍵特點

- **術前規劃 (pre-procedural planning)**
  - 所有 VT 迴路分析於術前完成
  - 不需術中反覆 VT induction

- **Personalized model**
  - 每位病人依自身 cardiac MRI 建構獨一無二的 digital twin

- **Minimal lesion set**
  - 虛擬消融目標：以**最少消融範圍**達到最大療效

- **Seamless integration**
  - 虛擬消融靶點直接匯入臨床 mapping system

---

<!-- _class: divider -->

# 主要結果

---

# 療效結果

| 指標 | 結果 |
|------|------|
| 平均追蹤時間 | **405.4 天** |
| VT-free 比例 | **8/10 (80%)** 完全無 VT 復發 |
| 抗心律不整藥物使用 | 8/10 未使用 antiarrhythmic drugs |
| ICD shock | **0 次**（所有受試者） |

> **所有 10 位受試者在追蹤期間均無 ICD shock**

---

# VT 復發者 (2/10) 分析

- 術後 **1 個月內**各發生 **1 次 VT episode**
- 均由 **antitachycardia pacing (ATP)** 成功終止
- 之後持續追蹤 **VT-free**
- 藥物已 **降階 (deescalated)**

> **即使有 VT 復發，也僅限於術後早期單次事件，不需 ICD shock**

---

<!-- _class: divider -->

# 臨床意義

---

# 精準醫療 (Precision Medicine) 典範

- **個人化消融策略 (personalized ablation)**
  - 每位病人的 VT 迴路取決於其獨特 scar morphology
  - Digital twin 可術前模擬所有可能的 VT circuits

- **最小化消融範圍 (minimal lesion set)**
  - 傳統 substrate-based ablation 需大範圍消融
  - Digital twin 精確定位關鍵消融靶點
  - 可能減少 ablation-related complications

- **縮短手術時間的潛力**
  - 術前完成 VT 迴路分析
  - 減少術中 mapping 與 VT induction 需求

---

# 研究限制

- **樣本數極小**：僅 **10 位**受試者
- **缺乏對照組**：non-randomized，無法直接比較傳統 ablation
- **Single-center**：Johns Hopkins 為技術開發中心，generalizability 待驗證
- **Selection bias**：經篩選的 ischemic VT 患者
- **技術門檻**：需高品質 cardiac MRI + 專業計算模擬團隊

---

<!-- _class: divider -->

# 結論

---

# Take-Home Messages

1. TWIN-VT 為首個 **FDA IDE 核准**的 digital twin–guided VT ablation 前瞻性研究

2. **80% (8/10)** 受試者在平均 405 天追蹤期間 VT-free，不需抗心律不整藥物

3. **零 ICD shock** — 有效降低 ICD shock 負擔

4. 為 **computational cardiology** 在臨床電生理應用提供重要 **proof of concept**

5. 未來需更大規模 **RCT** 確認臨床效益與安全性

---

<!-- _class: small-text -->

# 參考文獻

1. Chrispin J, Prakosa A, Kholmovski E, et al. Digital Twin–Guided Ablation for VT. [*N Engl J Med*. 2026;394:1345-1347.](https://doi.org/10.1056/NEJMc2517822)
2. Donahue JK, et al. Mechanism of VT in Chronic MI Scar. [*Circ Res*. 2024;134:328-342.](https://doi.org/10.1161/CIRCRESAHA.123.323415)
3. Reddy VY, et al. Prophylactic Catheter Ablation for Prevention of Defibrillator Therapy. [*N Engl J Med*. 2007;357:2657-2665.](https://doi.org/10.1056/NEJMoa065457)
4. Arevalo HJ, et al. Arrhythmia Risk Stratification Using Personalized Heart Models. [*Nat Commun*. 2016;7:11437.](https://doi.org/10.1038/ncomms11437)
5. Trayanova NA, et al. Imaging-Based Simulations for Predicting Sudden Cardiac Death. [*Circ Arrhythm Electrophysiol*. 2017;10:e004743.](https://doi.org/10.1161/CIRCEP.117.004743)
6. Prakosa A, et al. Personalized Virtual-Heart Technology for Guiding VT Ablation. [*Nat Biomed Eng*. 2018;2:732-740.](https://doi.org/10.1038/s41551-018-0282-9)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
Digital Twin–Guided VT Ablation | TWIN-VT Study
[NEJM 2026;394:1345-1347](https://doi.org/10.1056/NEJMc2517822)
