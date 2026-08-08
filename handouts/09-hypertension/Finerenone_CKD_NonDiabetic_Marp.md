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
  section.lead a { color: #8ec7ff; }
  section.lead blockquote, section.lead blockquote * { color: #2d3436; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: #ffffff;
    border-bottom: none;
    font-size: 2.5em;
    text-align: center;
  }
  section.divider h2 { color: #ffe08a; }
  section.divider h3 { color: #ffffff; }
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
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
footer: '謝慕揚 MD, PhD, FESC | Finerenone FIND-CKD | 2026'
---

<!-- _class: lead -->
# Finerenone 用於非糖尿病 CKD
## FIND-CKD Trial — N Engl J Med 2026;395:533-545

**整理：謝慕揚 MD, PhD, FESC** | 2026-08-08

[原文連結：https://doi.org/10.1056/NEJMoa2604625](https://doi.org/10.1056/NEJMoa2604625)

> 本投影片為讀書會共筆整理，供醫療專業人員教學參考，非治療指引。數據均引自原文全文。

---

# 一句話重點

- 對象：**無糖尿病**的 CKD 成人，已用 RAS inhibitor
- 藥物：**Finerenone**（nonsteroidal MRA, nsMRA）vs placebo
- **Primary（total eGFR slope）差異 0.7 mL/min/1.73 m²/年（95% CI 0.3 to 1.1，P<0.001）→ positive**
- Composite kidney–CV 事件 **HR 0.77（0.60–0.99）**
- Hyperkalemia 較多但可管理、無致死

> 首度把 finerenone 在 type 2 diabetes CKD 的腎臟保護延伸到**非糖尿病 CKD**。

---

<!-- _class: divider -->
# 背景與方法

---

# 背景：為何做 FIND-CKD

- CKD 全球約 8 億人；**逾半數並無糖尿病**
- RAS inhibitor、SGLT2 inhibitor 已是標準治療，但**殘餘風險高**（尤其嚴重 albuminuria）
- Mineralocorticoid receptor (MR) 過度活化 → 鈉水滯留、pro-inflammatory / pro-fibrotic
- Steroidal MRA（spironolactone/eplerenone）受 hyperkalemia、AKI 限制（BARACK-D >50% 停藥）
- **Finerenone**：選擇性 nsMRA，已於 FIDELIO / FIGARO / FIDELITY（type 2 diabetes CKD）證實有效

---

# 方法（Trial Design）

| 項目 | 內容 |
|------|------|
| 設計 | Phase 3、國際、雙盲、隨機、placebo-controlled |
| 分組 | 1:1 finerenone vs placebo（N=1584：793 / 791） |
| 起始劑量 | eGFR ≥60 → 20 mg/day；25–<60 → 10 mg/day（可加至 20 mg 目標） |
| 分層 | 基線 SGLT2i（是/否）、篩檢 UACR（≤1000 vs >1000） |
| 追蹤 | 計畫治療 ≥32 個月；**中位 36.6 個月** |
| 資助 | Bayer；NCT05047263 |

---

# 納入 / 排除條件

**納入（缺一不可）**
- 成人、**無糖尿病**（排除 T1DM/T2DM 或 HbA1c ≥6.5%）
- eGFR 25–<60 且 UACR 200–500，**或** eGFR 25–<90 且 UACR 500–3500
- Serum K ≤4.8 mmol/L；穩定 ACEi/ARB ≥4 週

**排除**
- 有 steroidal MRA 指徵
- Polycystic kidney disease、lupus nephritis、ANCA vasculitis
- 6 個月內免疫抑制治療

---

# 族群基線特徵

| 特徵 | Finerenone | Placebo |
|------|-----------|---------|
| 平均年齡（歲） | 54.5 | 54.8 |
| 女性 | 34.7% | 32.9% |
| Asian / White | 56.4% / 38.8% | 53.2% / 43.0% |
| Chronic glomerulonephritis | 56.2% | 57.8% |
| 平均 eGFR | 46.8 | 46.6 |
| 中位 UACR | 827.5 | 810.7 |
| Serum K | 4.5 | 4.5 |
| SGLT2i 使用 | 17.0% | 17.1% |

> 整體：RAS inhibitor **99.7%**、SGLT2i **17.0%**；偏向男性、Asian、進展性 CKD。

---

<!-- _class: divider -->
# 結果

---

# Primary Endpoint：total eGFR slope
## [DOI: 10.1056/NEJMoa2604625](https://doi.org/10.1056/NEJMoa2604625)

| eGFR slope | Finerenone | Placebo | 差異（95% CI） |
|------------|-----------|---------|----------------|
| **Total（baseline→月32）** | **−3.3 (−3.6,−3.1)** | **−4.0 (−4.3,−3.8)** | **0.7 (0.3–1.1), P<0.001** |
| Acute（baseline→月3） | — | — | **−1.2 (−1.7,−0.6) /3 月** |
| Chronic（月3→停藥，年化） | −2.9 | −4.1 | **1.2 (0.9–1.6)** |

> **Acute dip 可逆**：finerenone 前 3 個月使 eGFR 暫時下降 → total slope 低估效益；**chronic slope 差 1.2** 更能反映長期腎臟保護。停藥後 finerenone 組 eGFR 回升。

---

# Secondary Endpoints（hierarchical）
## [DOI: 10.1056/NEJMoa2604625](https://doi.org/10.1056/NEJMoa2604625)

| Endpoint | Fin n(%) | Pbo n(%) | HR (95% CI) | P |
|----------|----------|----------|-------------|---|
| **Composite kidney–CV** | 110 (13.9) | 134 (16.9) | **0.77 (0.60–0.99)** | **0.04** |
| Composite kidney（≥57%↓/failure） | 104 (13.1) | 125 (15.8) | 0.78 (0.60–1.01) | 0.06 |
| Composite CV（HHF/CV death） | 10 (1.3) | 16 (2.0) | 0.60 (0.27–1.33) | — |

> **注意**：kidney composite P=0.06 **未達顯著** → 依 hierarchical 規則，CV composite 之後為 **nominal**，CI 跨越 1，**不可宣稱 CV 硬終點效益**。本試驗未 power 於臨床事件。

---

# Exploratory：Albuminuria 與 40% 複合
## [DOI: 10.1056/NEJMoa2604625](https://doi.org/10.1056/NEJMoa2604625)

| Endpoint | Finerenone | Placebo | 效果 (95% CI) |
|----------|-----------|---------|---------------|
| UACR 月6 相對變化 | −41.3% | −9.1% | 相對差 **35.4% (30.9–39.6)** |
| UACR 下降 ≥30%（月6） | 56.0% | 24.4% | OR 3.99 (3.22–4.95) |
| eGFR ≥40%↓ 或 kidney failure | 21.2% | 26.0% | HR 0.76 (0.62–0.93) |
| 全因死亡 | 2.4% | 3.5% | — |

> Albuminuria 早期即大幅下降（−41% vs −9%），為 finerenone 早期藥效 marker（未校正 multiplicity，僅供參考）。

---

# 安全性：Hyperkalemia、AKI、血壓
## [DOI: 10.1056/NEJMoa2604625](https://doi.org/10.1056/NEJMoa2604625)

| 指標 | Finerenone | Placebo |
|------|-----------|---------|
| **Hyperkalemia（任一）** | **17.0%** | **13.3%** |
| ↳ 導致永久停藥 | 1.5% | 0.1% |
| ↳ 導致住院 / 致死 | 0.9% / 0 | 0.6% / 0 |
| Serum K >5.5 / >6.0 | 18.8% / 4.3% | 12.2% / 2.3% |
| Acute kidney injury | 2.9% | 3.2% |
| SBP 變化（月3） | −5.1 mmHg | −0.1 mmHg |

> K 於月1 上升 +0.12 mmol/L 後趨穩；**無致死、住院 <1%、僅 1.5% 因此停藥**——遠低於 steroidal MRA。前提是嚴格篩選＋分段劑量＋K>5.5 暫停/減量 protocol。

---

<!-- _class: divider -->
# 臨床意涵與限制

---

# 臨床意涵

- **首度將 finerenone 腎臟保護延伸至非糖尿病 CKD**；效果幅度（total 0.7、chronic 1.2）與 RAS inhibitor、SGLT2i（0.5–1.0）相當
- eGFR slope 為 surrogate；meta-analysis 顯示 slope 減 0.75 → 約 **23% 腎臟硬終點風險↓**，與 HR 0.77 一致
- 不論是否併用 SGLT2i 效益一致 → 假設互補，但**未直接測試疊加**
- 對台灣以 **chronic glomerulonephritis 為主**（約 57%）的非糖尿病 CKD 具參考價值，可為 RAS inhibitor（±SGLT2i）之上的候選第三支柱，須配 K 監測

---

# Limitations

- **Surrogate（eGFR slope）主要終點；未 power 於臨床硬終點**
- Kidney composite 未顯著（P=0.06）、CV composite 為 nominal → **勿過度解讀**
- 族群偏男性、進展性 CKD、嚴重 albuminuria、Black 病人極少
- 排除 polycystic kidney disease、lupus nephritis、ANCA vasculitis、極低 eGFR / 低度 albuminuria → **不可外推**
- 僅 17% 基線用 SGLT2i；未直接比較/疊加
- Sponsor（Bayer）分析（UMCG 獨立核對）

---

# Clinical Pearls

> **Pearl 1**：FIND-CKD 為 finerenone 在非糖尿病 CKD 的首個 phase 3 RCT，primary 為 positive（0.7 mL/min/1.73 m²/年，P<0.001）。

> **Pearl 2**：eGFR slope 要分 acute dip（可逆）vs chronic slope；chronic 差異 1.2 > total 0.7。

> **Pearl 3**：Hyperkalemia 可管理（致死 0、停藥 1.5%），關鍵在入選 K ≤4.8 + 分段劑量 protocol。

> **Pearl 4**：本試驗**未證明心血管硬終點效益**，臨床溝通勿誇大。

---

<!-- _class: small-text -->
# 參考文獻（1）

1. Heerspink HJL, Neuen BL, Agarwal R, et al. Finerenone in Persons with CKD without Diabetes (FIND-CKD). [*N Engl J Med*. 2026;395(6):533-545.](https://doi.org/10.1056/NEJMoa2604625)
2. Bakris GL, et al. Effect of Finerenone on CKD Outcomes in Type 2 Diabetes (FIDELIO-DKD). [*N Engl J Med*. 2020;383:2219-2229.](https://doi.org/10.1056/NEJMoa2025845)
3. Pitt B, et al. Cardiovascular Events with Finerenone in Kidney Disease and Type 2 Diabetes (FIGARO-DKD). [*N Engl J Med*. 2021;385:2252-2263.](https://doi.org/10.1056/NEJMoa2110956)
4. Agarwal R, et al. Finerenone in T2D and CKD: FIDELITY pooled analysis. [*Eur Heart J*. 2022;43:474-484.](https://doi.org/10.1093/eurheartj/ehab777)
5. Heerspink HJL, et al. Dapagliflozin in Patients with CKD (DAPA-CKD). [*N Engl J Med*. 2020;383:1436-1446.](https://doi.org/10.1056/NEJMoa2024816)

---

<!-- _class: small-text -->
# 參考文獻（2）

6. The EMPA-KIDNEY Collaborative Group. Empagliflozin in Patients with CKD. [*N Engl J Med*. 2023;388:117-127.](https://doi.org/10.1056/NEJMoa2204233)
7. Inker LA, et al. A meta-analysis of GFR slope as a surrogate endpoint for kidney failure. [*Nat Med*. 2023;29:1867-1876.](https://doi.org/10.1038/s41591-023-02418-0)
8. Hobbs FDR, et al. Low-dose spironolactone and cardiovascular outcomes in moderate stage CKD (BARACK-D). [*Nat Med*. 2024;30:3634-3645.](https://doi.org/10.1038/s41591-024-03263-5)
9. KDIGO CKD Work Group. KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of CKD. [*Kidney Int*. 2024;105(4S):S117-S314.](https://doi.org/10.1016/j.kint.2023.10.018)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

[FIND-CKD — https://doi.org/10.1056/NEJMoa2604625](https://doi.org/10.1056/NEJMoa2604625)

**謝慕揚 MD, PhD, FESC**
