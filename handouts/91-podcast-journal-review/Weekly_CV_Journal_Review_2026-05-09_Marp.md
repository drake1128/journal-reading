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
  section.lead h1 { color: #ffffff; font-size: 1.9em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong, section.lead a { color: #dfe6e9; }
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
    font-size: 2.4em;
    text-align: center;
  }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; font-size: 0.85em; }
  h3 { color: #555555; }
  table { font-size: 0.66em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 5px 8px; }
  td { padding: 4px 8px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.85em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 0.66em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.78em; }
  section.ref { font-size: 0.58em; }
  section.ref h1 { font-size: 1.3em; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-05-09'
---

<!-- _class: lead -->

# 每週心血管期刊文獻回顧

## 2026-05-03 ~ 2026-05-09

**謝慕揚 MD, PhD, FESC** | 2026-05-09

NEJM · Lancet · EHJ · JACC · Circulation · EuroIntervention

---

# 本週主題：「降溫」週

> **兩個熱門概念被踩剎車：**
> - **CHIP-BCIS3**: Impella in HR-PCI **無效，且可能有害**
> - **TAILORED-CHIP**: Tailored DAPT **無效，且更多出血**

> **三個正面/概念性發現：**
> - **ALLEPRE**: 護理師主導 ACS 預防 4 年 MACE ↓ 28%
> - **TRISCEND II by TR**: EVOQUE TTVR 跨嚴重度都有效
> - **ORBITA-FIRE**: 引發 angina 的生理閾值 << 缺血閾值

---

# Top 5 Picks 一覽

| # | 試驗 | 期刊 | 結果 | 關鍵數字 |
|---|------|------|------|---------|
| 1 | **CHIP-BCIS3** | NEJM | ❌ Negative + harm signal | Win ratio 0.85 (0.63-1.15); CV death 26.7% vs 14.5% |
| 2 | **TAILORED-CHIP** | EHJ | ❌ Negative + 出血 ↑ | Primary HR 1.19 (0.90-1.58); BARC 2/3/5 7.2% vs 4.8% |
| 3 | **ALLEPRE** | EHJ | ✅ Positive | MACE HR 0.70 (0.57-0.85), driven by MI ↓ |
| 4 | **TRISCEND II by TR** | EHJ | ✅ Consistent | Win ratio 1.64 / 2.20 across severity |
| 5 | **ORBITA-FIRE** | Circulation | 💡 Concept-shift | Median FFR_angina 0.29 (vs 0.80 cutoff) |

---

<!-- _class: divider -->

# NEJM

---

# CHIP-BCIS3 — Impella in HR-PCI ⚠️
## [Perera D, et al. NEJM 2026-05-07](https://doi.org/10.1056/NEJMoa2515704) | NCT05003817

| 項目 | 內容 |
|------|------|
| 設計 | UK 21 中心 RCT, N=300 (Impella 148 vs SoC 152) |
| 族群 | LVEF ≤35% (or ≤45% + severe MR) + 廣泛 CAD, 計畫性複雜 PCI |
| Primary | Hierarchical composite — **win ratio** |
| **Win ratio** | **0.85** (95% CI 0.63-1.15), **P=0.30** |
| All-cause death | HR **1.54** (0.99-2.41) |
| CV death (TCT/MD) | **26.7% vs 14.5%** |
| Major bleeding | 10.8% vs 7.3% |
| Vascular complication | 16.9% vs 10.6% |

> **Take Home**：HR-PCI **不需常規 Impella**；應依個別血流動力學保留為救援策略

---

# CHIP-BCIS3 — Editorial 重點
## [Nallamothu BK, Wanamaker BL — "Price of Protection"](https://doi.org/10.1056/NEJMe2602727)

- 「**Adoption before evidence**」的長期問題終於被踩剎車
- Impella 在 HR-PCI 應從預設策略 → 個別評估
- 與既有 RCT (PROTECT II, DanGer Shock) 一致地未顯示 routine 使用 benefit

> ⚠️ **Drake 已有專屬講義**（git history `75f7ecc`：CHIP-BCIS3 + Anatomy teaching debate）

---

<!-- _class: divider -->

# European Heart Journal

---

# TAILORED-CHIP ⚠️
## [Kang DY, et al. EHJ 2026 (ehaf652)](https://doi.org/10.1093/eurheartj/ehaf652)

| 項目 | 內容 |
|------|------|
| 設計 | RCT, **N=2018** 高風險複雜 PCI |
| 介入 | Tailored: Ticagrelor 60 BID + ASA <6mo → Clopidogrel 單藥 >6mo |
| 對照 | Standard DAPT: Clopidogrel + ASA × 12 mo |
| Primary (12-mo composite) | Tailored **10.5%** vs DAPT **8.8%** — HR **1.19** (0.90-1.58), P=0.21 |
| **Bleeding (BARC 2/3/5)** | Tailored **7.2%** vs DAPT **4.8%** ⚠️ |

> **Pearl**：Tailored DAPT 概念美好，臨床效益 **未獲驗證**；標準 DAPT 仍是預設選項
> **病人複雜度**：22.6% LM, 19.5% bifurcation, 84.1% diffuse long, 93.7% MV PCI

---

# ALLEPRE — Nurse-Coordinated Prevention ✅
## [Magnani G, et al. EHJ 2026 (ehag255)](https://doi.org/10.1093/eurheartj/ehag255)

| 項目 | 內容 |
|------|------|
| 設計 | Pragmatic, multicenter RCT, **N=2057** ACS 病人 |
| 介入 | NCPP — 4 年內 9 次護理師個別衛教 |
| **Primary (MACE)** | NCPP **16.2%** vs SoC **22.6%** — HR **0.70** (0.57-0.85), **P<0.001** |
| Driver: Non-fatal MI | 9.3% vs 15.2% — HR **0.60** (0.46-0.77), P=0.0001 |
| 行為改變 | 運動、體重、用藥順從性皆顯著改善 |

> **Take Home**：護理師主導二級預防 **真的有效**且 effect size 大；值得納入 ACS post-discharge pathway

---

# TRISCEND II — by Baseline TR Severity ✅
## [Lurz P, Hahn RT, Kodali S, et al. EHJ 2026 (ehaf676)](https://doi.org/10.1093/eurheartj/ehaf676)

| 結果 | Severe TR (n=172) | Massive/Torrential (n=220) |
|------|-------------------|---------------------------|
| 1-yr TR ≤mild | 95.2% | 95.3% |
| Win ratio (TTVR vs control) | **1.64** (1.11, 2.43) | **2.20** (1.55, 3.14) |
| 18-mo all-cause mortality diff | NS (0.2%) | NS (-5.8%) |
| 18-mo HF hosp diff | NS (+9.8%) | **-15.2%** (-28.9, -1.5) |

> **臨床啟示**：EVOQUE TTVR 改善 TR 嚴重度與 QoL **不分嚴重度**；HF hosp 受益最明顯仍是 advanced disease

---

# EHJ 其他焦點 (1/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| **TAVI in mechanical valve (FIH)** | Amat-Santos: 經導管置換機械瓣的人類首例 | [DOI](https://doi.org/10.1093/eurheartj/ehag019) |
| **DCB vs DES for ISR — Great Debate** | Cortese & Mehilli | [DOI](https://doi.org/10.1093/eurheartj/ehag070) |
| **Tricuspid TEER → TTVR sweet spot** | Marsan & Bax editorial | [DOI](https://doi.org/10.1093/eurheartj/ehaf954) |
| **CPAP CV benefit (multi-trial)** | Azarbarzin: 高風險 OSA 才有 CV benefit | [DOI](https://doi.org/10.1093/eurheartj/ehaf447) |
| **SCAD antiplatelet 反思** | Cerrato & Dang: 強效抗血小板可能有害 | [DOI](https://doi.org/10.1093/eurheartj/ehaf1051) |
| **VESALIUS-CV (PCSK9 一級預防)** | Liuzzo & Volpe weekly scan | [DOI](https://doi.org/10.1093/eurheartj/ehag011) |

---

# EHJ 其他焦點 (2/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| **Digoxin × GDMT** | RALES/EMPHASIS-HF/PARADIGM-HF/DAPA-HF 合併分析 | [DOI](https://doi.org/10.1093/eurheartj/ehag387) |
| **EPA cardioprotection** | 不只 TG 機轉的評論 | [DOI](https://doi.org/10.1093/eurheartj/ehag287) |
| **SAFE-PAD long-term** | DCB vs non-DCB for femoropopliteal — long-term | [DOI](https://doi.org/10.1093/eurheartj/ehaf721) |
| **Subacute coronary occlusion** | Grey zone 的處理複雜性 review | [DOI](https://doi.org/10.1093/eurheartj/ehaf1077) |
| **Nurse & allied professional CV impact** | Editorial: 跨領域團隊照護的價值 | [DOI](https://doi.org/10.1093/eurheartj/ehag251) |
| **Environmental risk factors** | Piepoli & Weidinger 政策聲明 | [DOI](https://doi.org/10.1093/eurheartj/ehag270) |

---

<!-- _class: divider -->

# JACC Family

---

# DOBERMANN-D + DOBERMANN-T ⚠️
## [DOBERMANN-D](https://pubmed.ncbi.nlm.nih.gov/41801171/) + [DOBERMANN-T](https://pubmed.ncbi.nlm.nih.gov/41801170/) — JACC 2026

族群：AMI/PCI 後 ORBI risk score ≥10（in-hospital cardiogenic shock 中至高風險）

| 試驗 | 介入 | Primary endpoint | 結果 |
|------|------|------------------|------|
| **DOBERMANN-D** | 24h 低劑量 dobutamine vs placebo | 48h NT-proBNP | **NS** (僅降 2%) |
| **DOBERMANN-T** | 1h tocilizumab (anti-IL-6R) | NT-proBNP + 梗塞大小 | 趨勢但 **NS** |

- 安全性：兩組皆安全
- Dobutamine 從 hour 15 起 SBP 較低（持續 LV afterload ↓）

> **Take Home**：Pre-shock window 概念吸引人，但兩種介入 **皆未在生物標記上顯著改善**

---

# JACC — 高敏 Troponin 與 ED 演算法

| 主題 | 重點 | 連結 |
|------|------|------|
| **hs-cTnT-gen6** | 新一代 assay 在疑似 MI 的診斷準確度與 cutoff | [PMID 41879583](https://pubmed.ncbi.nlm.nih.gov/41879583/) |
| **ESC 0/1 vs 0/2 or 0/3-h** | 多中心 prospective 比較三種演算法 | [PMID 41706062](https://pubmed.ncbi.nlm.nih.gov/41706062/) |
| **cTnI/cTnT ratio** | Old dogs, new tricks — myocardial injury 新詮釋 | [PMID 41739020](https://pubmed.ncbi.nlm.nih.gov/41739020/) |
| **MI universal definition risk** | Boeddinghaus IPD meta-analysis | [PMID 41553312](https://pubmed.ncbi.nlm.nih.gov/41553312/) |

> ED MI rule-out 與 troponin 應用是 JACC 本週另一重心

---

# JACC — 其他

| 主題 | 重點 | 連結 |
|------|------|------|
| **單顆藥複方降壓被忽略** | Choi K, et al.: 美國 2015-2025 SPC 仍 underuse | [DOI](https://doi.org/10.1016/j.jacc.2026.03.088) |
| **MI 後二級預防（美國）** | Chiu N, Libby P, et al. | [DOI](https://doi.org/10.1016/j.jacc.2026.03.157) |
| **數位 CBT 治療 MI 後焦慮** | Johnsson A, et al. RCT | [DOI](https://doi.org/10.1016/j.jacc.2026.02.5068) |
| **AMI + CS 中 cardiac arrest** | Freund A, et al. pooled analysis | [DOI](https://doi.org/10.1016/j.jacc.2026.01.068) |
| **VA-ECMO flow ramp 血流動力學** | Xu C, et al. + editorials | [DOI](https://doi.org/10.1016/j.jacc.2025.09.1610) |
| **Epicardial fat radiomics** | Segar & Pandey editorial — HF risk stratification | [DOI](https://doi.org/10.1016/j.jacc.2026.03.160) |

---

<!-- _class: divider -->

# Circulation Family

---

# ORBITA-FIRE — FFR_angina 💡
## [Ahmed-Jushuf F, et al. Circulation 2026-05-08](https://doi.org/10.1161/CIRCULATIONAHA.125.078738)

| 項目 | 內容 |
|------|------|
| 設計 | 多中心、雙盲、placebo-controlled, **N=65** stable 1V CAD |
| 方法 | PCI 後 in-stent balloon 漸進膨脹直到 angina；對照 placebo inflation |
| Pre-PCI FFR | median **0.59** (0.46-0.70) |
| **FFR_angina at rest** | **0.29** (0.23-0.35) |
| FFR_angina low-intensity | 0.38 (0.30-0.48) |
| FFR_angina high-intensity | 0.45 (0.36-0.55) |
| RFR_angina (rest → high) | 0.22 → 0.32 |
| 全部 vs 缺血 cutoff | P<0.001 — **顯著低於** FFR 0.80 / RFR 0.89 |

> **Pearl**：缺血 ≠ 症狀；ORBITA-FIRE 提供「症狀導向生理學」新框架

---

# ORBITA-FIRE — 臨床意義

- 引發 angina 的 FFR/RFR **遠低於缺血診斷閾值**
- 閾值 **高度個人化**，並隨心臟負荷變化
- **較低個人化閾值** → 較高症狀重現性 + PCI 後較大症狀緩解
- 補強了 **ORBITA / ORBITA-2** 對 stable angina PCI 的論述：
  - PCI 對「真正高負荷誘發」的病人最有效
  - 對「邊際缺血」的病人，PCI 症狀效益有限

> **可能改變實務**：Stable angina PCI 病人選擇可加入「症狀-生理 coupling」評估

---

# SUPPORT I — Supira pVAD 早期可行性 ➰
## [Kandzari DE, et al. Circ Cardiovasc Interv 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016010)

| 項目 | 內容 |
|------|------|
| 設計 | 4 中心、單組、可行性研究, **N=15** |
| 裝置 | Supira pVAD (low-profile microaxial, 最大 5.5 L/min) |
| 病人 | 80% MV PCI、67% unprotected LM、60% atherectomy/IVL |
| Technical / procedural success | 93.3% / 86.7% |
| Primary feasibility | **15/15 (100%)** |
| 主要安全 (裝置 MAE) | 1/15 (6.7%) |
| 90-day deaths | 2 例（皆與裝置無關） |

> **臨床對照**：Supira 是 Impella 之外的另一條 microaxial 路線；CHIP-BCIS3 給 Impella 潑冷水的同時，新裝置仍嘗試找證據

---

# Circulation 其他焦點

| 主題 | 重點 | 連結 |
|------|------|------|
| **CARDIO-TTRansform Phase 3** | Eplontersen 治療 ATTR-CM design paper | [DOI](https://doi.org/10.1161/CIRCHEARTFAILURE.126.014205) |
| **Stellate ganglion 光療治 VT** | 非侵入性神經調節，門診治療室性心律不整 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.125.078175) |
| **CCCTN — CS vasoactive 變異** | 各中心 norepinephrine vs 其他選擇差異大 | [DOI](https://doi.org/10.1161/CIRCHEARTFAILURE.125.013778) |
| **TriSelect — TTVR screen failure 1-yr** | 篩選失敗病人的預後 | [DOI](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016124) |
| **HCM intermediate variants** | 整合進臨床與家族篩檢 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.125.077435) |
| **Vascular Aging review** | 機轉與介入 review | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.125.075567) |
| **TEER 後 fatty muscle (CT)** | Opportunistic CT 預測 mitral TEER 預後 | [DOI](https://doi.org/10.1161/CIRCIMAGING.125.018763) |

---

<!-- _class: divider -->

# EuroIntervention

---

# FAVOR III Europe 2-Year Follow-Up
## [Andersen BK, et al. EuroIntervention 2026](https://doi.org/10.4244/EIJ-D-25-01255)

| 項目 | QFR | FFR | HR (95% CI) | P |
|------|-----|-----|-------------|---|
| 2-yr MACE | 9.7% | 7.4% | 1.34 (0.98-1.81) | 0.064 |
| 1→2-yr (landmark) | 3.2% | 3.2% | 0.97 (0.58-1.62) | 0.92 |

- 1 年結果（先前發表）：QFR **未達 non-inferiority**
- 2 年累積：QFR 仍數值較差，但僅邊緣顯著

> **臨床啟示**：QFR 的 **超額風險集中於前 12 個月**；1 年後事件率類似
> 對需要長期追蹤的中度狹窄，**FFR 仍為首選**

---

# EuroIntervention 其他焦點 — Physiology + DCB 主題

| 主題 | 重點 | 連結 |
|------|------|------|
| **Editorial: Physiology beyond the wire** | Campo & Biscaglia — 2026 是 physiology 定義年? | [DOI](https://doi.org/10.4244/EIJ-D-26-00289) |
| **Deep learning for plaque burden prediction** | García-García: derivation + external validation | [DOI](https://doi.org/10.4244/EIJ-D-25-01352) |
| **Slow flow / no reflow review** | Brugaletta — 機轉、預防、治療 | [DOI](https://doi.org/10.4244/EIJ-D-25-01346) |
| **DCB → plaque redistribution natural history** | Dobrolińska — 影像追蹤 | [DOI](https://doi.org/10.4244/EIJ-D-25-01145) |
| **DCB for CABG failure** | Marschall — vein graft DCB | [DOI](https://doi.org/10.4244/EIJ-D-25-01273) |
| **Intracoronary imaging guidance for de novo DCB** | Amabile et al. — IVUS/OCT 指引 | [DOI](https://doi.org/10.4244/EIJ-D-25-01066) |

---

<!-- _class: divider -->

# 整合 Take Home

---

# 本週 5 大臨床啟示

> **1. Impella in HR-PCI 不該是預設選項**（CHIP-BCIS3）
> 應從 routine 退回個別評估；CV 死亡訊號值得警惕

> **2. Tailored DAPT 在複雜 PCI 未獲驗證**（TAILORED-CHIP）
> 早升階 + 晚降階 = 更多出血而無 ischemic 好處；維持標準 DAPT

> **3. 護理師主導 ACS 預防 effect size 大**（ALLEPRE）
> 4 年 MACE HR 0.70；應納入 post-discharge pathway

---

# 本週 5 大臨床啟示（續）

> **4. EVOQUE TTVR 跨 TR 嚴重度都有效**（TRISCEND II）
> 可考慮擴大適應症；HF hosp 好處集中在 massive/torrential

> **5. 缺血 ≠ 症狀**（ORBITA-FIRE）
> Median FFR_angina 0.29，遠低於 0.80 cutoff；
> 改善 stable angina PCI 病人選擇的概念基礎

> **Bonus**: QFR 不能取代 FFR；excess risk 持續 2 年（FAVOR III Europe）

---

<!-- _class: divider -->

# 縮寫對照

---

<!-- _class: small-text -->

# 縮寫對照

| 縮寫 | 全名 | 縮寫 | 全名 |
|------|------|------|------|
| HR-PCI | High-risk PCI | TR | Tricuspid regurgitation |
| pVAD/mAFP | (microaxial) percutaneous VAD | TTVR | Transcatheter tricuspid valve replacement |
| LVEF | Left ventricular ejection fraction | TEER | Transcatheter edge-to-edge repair |
| MR | Mitral regurgitation | DAPT | Dual antiplatelet therapy |
| ACS | Acute coronary syndrome | BARC | Bleeding Academic Research Consortium |
| MACE | Major adverse CV events | LM/MV | Left main / Multivessel |
| MI/STEMI/NSTEMI | Myocardial infarction | NT-proBNP | N-terminal pro-BNP |
| FFR | Fractional flow reserve | ORBI | In-hospital CS risk score |
| RFR | Resting full-cycle ratio | ATTR-CM | TTR amyloid cardiomyopathy |
| QFR | Quantitative flow ratio | CCCTN | Critical Care Cardiology Trials Network |
| NCPP | Nurse-coordinated prevention prog | HCM | Hypertrophic cardiomyopathy |
| OSA | Obstructive sleep apnea | DCB/DES/ISR | Drug-coated balloon / DES / In-stent restenosis |
| SCAD | Spontaneous coronary artery dissection | IVL | Intravascular lithotripsy |
| SPC | Single-pill combination | GDMT | Guideline-directed medical therapy |

---

<!-- _class: ref -->

# 參考文獻 (1/3) — NEJM + EHJ

1. Perera D, et al. **CHIP-BCIS3**. [*NEJM*. 2026.](https://doi.org/10.1056/NEJMoa2515704)
2. Nallamothu BK, Wanamaker BL. Editorial. [*NEJM*. 2026.](https://doi.org/10.1056/NEJMe2602727)
3. Kang DY, et al. **TAILORED-CHIP**. [*EHJ*. 2026.](https://doi.org/10.1093/eurheartj/ehaf652)
4. Capodanno D. Editorial. [*EHJ*. 2026.](https://doi.org/10.1093/eurheartj/ehaf649)
5. Magnani G, et al. **ALLEPRE**. [*EHJ*. 2026.](https://doi.org/10.1093/eurheartj/ehag255)
6. Lurz P, et al. **TRISCEND II by TR severity**. [*EHJ*. 2026.](https://doi.org/10.1093/eurheartj/ehaf676)
7. Helseth R, et al. Digoxin × GDMT meta-analysis. [*EHJ*. 2026.](https://doi.org/10.1093/eurheartj/ehag387)
8. Liuzzo G, Volpe M. **VESALIUS-CV scan**. [*EHJ*. 2026.](https://doi.org/10.1093/eurheartj/ehag011)
9. Amat-Santos IJ, et al. **TAVI in mechanical valve FIH**. [*EHJ*. 2026.](https://doi.org/10.1093/eurheartj/ehag019)
10. Cortese B, et al. DCB vs DES for ISR debate. [*EHJ*. 2026.](https://doi.org/10.1093/eurheartj/ehag070)
11. Marsan NA, Bax JJ. TTVR sweet spot. [*EHJ*. 2026.](https://doi.org/10.1093/eurheartj/ehaf954)
12. Azarbarzin A, et al. CPAP CV benefit. [*EHJ*. 2026.](https://doi.org/10.1093/eurheartj/ehaf447)

---

<!-- _class: ref -->

# 參考文獻 (2/3) — JACC + Circulation

13. Holle SLD, et al. **DOBERMANN-D**. [*JACC*. 2026.](https://doi.org/10.1016/j.jacc.2026.01.020)
14. Kunkel JB, et al. **DOBERMANN-T**. [*JACC*. 2026.](https://doi.org/10.1016/j.jacc.2026.01.019)
15. Sinha SS, et al. DOBERMANN editorial. [*JACC*. 2026.](https://doi.org/10.1016/j.jacc.2026.02.5107)
16. Koechlin L, et al. hs-cTnT-gen6. [*JACC*. 2026.](https://doi.org/10.1016/j.jacc.2025.12.052)
17. Glaeser J, et al. ESC 0/1 vs 0/2-3h algorithm. [*JACC*. 2026.](https://doi.org/10.1016/j.jacc.2025.12.056)
18. Choi K, et al. SPC underuse for HTN. [*JACC*. 2026.](https://doi.org/10.1016/j.jacc.2026.03.088)
19. Boeddinghaus J, et al. Universal MI definition risk meta-analysis. [*JACC*. 2026.](https://doi.org/10.1016/j.jacc.2025.11.043)
20. Ahmed-Jushuf F, et al. **ORBITA-FIRE**. [*Circulation*. 2026.](https://doi.org/10.1161/CIRCULATIONAHA.125.078738)
21. Kandzari DE, et al. **SUPPORT I (Supira pVAD)**. [*Circ CV Interv*. 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016010)
22. Masri A, et al. **CARDIO-TTRansform** Phase 3 design. [*Circ HF*. 2026.](https://doi.org/10.1161/CIRCHEARTFAILURE.126.014205)
23. Hamilton DE, et al. CCCTN vasoactive variation. [*Circ HF*. 2026.](https://doi.org/10.1161/CIRCHEARTFAILURE.125.013778)

---

<!-- _class: ref -->

# 參考文獻 (3/3) — EuroIntervention + 補充

24. Rudolph F, et al. **TriSelect**. [*Circ CV Interv*. 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016124)
25. Harano Y, et al. Stellate ganglion phototherapy for VT. [*Circulation*. 2026.](https://doi.org/10.1161/CIRCULATIONAHA.125.078175)
26. Walsh R, et al. HCM intermediate variants. [*Circulation*. 2026.](https://doi.org/10.1161/CIRCULATIONAHA.125.077435)
27. Andersen BK, et al. **FAVOR III Europe 2-yr**. [*EuroIntervention*. 2026.](https://doi.org/10.4244/EIJ-D-25-01255)
28. Campo G, Biscaglia S. Physiology beyond the wire editorial. [*EuroIntervention*. 2026.](https://doi.org/10.4244/EIJ-D-26-00289)
29. García-García HM, et al. Deep learning for plaque burden. [*EuroIntervention*. 2026.](https://doi.org/10.4244/EIJ-D-25-01352)
30. Brugaletta S, et al. Slow flow / no reflow review. [*EuroIntervention*. 2026.](https://doi.org/10.4244/EIJ-D-25-01346)
31. Marschall A, et al. DCB for CABG failure. [*EuroIntervention*. 2026.](https://doi.org/10.4244/EIJ-D-25-01273)
32. Amabile N, et al. Imaging guidance for de novo DCB. [*EuroIntervention*. 2026.](https://doi.org/10.4244/EIJ-D-25-01066)
33. TCT/MD: [Impella in HR-PCI Doesn't Help, Might Harm — CHIP-BCIS3](https://www.tctmd.com/news/impella-support-high-risk-pci-doesnt-help-might-harm-chip-bcis3)
34. TCT/MD: [DOBERMANN — Dobutamine and Tocilizumab in Pre-Shock](https://www.tctmd.com/news/dobermann-dobutamine-and-tocilizumab-show-promise-pre-shock-patients)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC** — 讀書會共筆整理人
2026-05-09 | Weekly CV Journal Review (NEJM · EHJ · JACC · Circulation · EuroIntervention)
