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
    font-size: 26px;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 1.8em; border-bottom: none; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #b0c4de; }
  section.lead blockquote, section.lead blockquote p { color: #2d3436; }
  section.lead blockquote strong { color: #ba181b; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: white;
    border-bottom: none;
    font-size: 2.3em;
    text-align: center;
  }
  section.divider h2, section.divider h3 { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.5em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.8em; width: 100%; }
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
  section.ref ol { font-size: 0.7em; }
footer: '謝慕揚 MD, PhD, FESC | tMCS in Cardiogenic Shock — EAPCI/ACVC CCS | 2026'
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Temporary Mechanical Circulatory Support in Cardiogenic Shock

## 急性心肌梗塞合併心因性休克的暫時性機械循環輔助

EAPCI／ACVC Clinical Consensus Statement of the ESC
Chieffo A, Iannaccone M, Hassager C, … Thiele H, … Price S — *Eur Heart J* 2026

[原文連結：doi:10.1093/eurheartj/ehag708](https://doi.org/10.1093/eurheartj/ehag708)

**讀書會共筆整理人：謝慕揚 醫師 MD, PhD, FESC** | 2026-10-29

---

# Take Home Messages

1. **從「有哪些 device」到「哪個 phenotype 用哪個 device」**：更新 2020 consensus，以 SCAI SHOCK stage + SHARC 導引 device 選擇、時機、escalation 與 de-escalation
2. **Impella CP — DanGer Shock：Positive**（族群經嚴格篩選）：180 天死亡 45.8% vs 58.5%，HR 0.74（95% CI 0.55–0.99），p=0.04；併發症增加
3. **VA-ECMO routine — ECLS-SHOCK：Neutral**：30 天死亡 47.8% vs 49.0%，RR 0.98（0.80–1.19），p=0.81
4. **IABP routine — IABP-SHOCK II：Neutral**：39.7% vs 41.3%，RR 0.96（0.79–1.17），p=0.69
5. **系統面**：shock team、hub-and-spoke、預先寫好 escalation 與 futility protocol

---

# 為什麼要更新？2012–2026 證據演進

| 年份 | 里程碑 | 重點 | 方向 |
|------|--------|------|------|
| 2012 | IABP-SHOCK II | IABP routine 無存活效益 | Neutral |
| 2020 | EAPCI／ACVC expert consensus | 前版共識 | — |
| 2023 | ECLS-SHOCK、IPD meta-analysis | VA-ECMO routine 無存活效益、併發症增加 | Neutral |
| 2024 | DanGer Shock | Impella CP 降低 180 天死亡 | **Positive** |
| 2025 | DanGer Shock 長期追蹤 | 死亡率差異持續 | Follow-up |
| 2026 | 本篇 CCS | Phenotype-driven 建議 | — |

> 證據首度出現「同為 tMCS、方向相反」的結果 → 共識聚焦在 **patient／device selection**

---

# 關鍵 RCT 一覽：只有一個 positive

| Trial | 族群 | 比較 | Primary endpoint | 結果 (95% CI) | 方向 |
|-------|------|------|------------------|---------------|------|
| [IABP-SHOCK II](https://doi.org/10.1056/NEJMoa1208410) NEJM 2012, n=600 | AMI-CS | IABP vs 不放 | 30 天死亡 | 39.7% vs 41.3%；RR 0.96 (0.79–1.17) | Neutral |
| [ECLS-SHOCK](https://doi.org/10.1056/NEJMoa2307227) NEJM 2023, n=417 | AMI-CS；77% 曾 CPR | VA-ECMO vs usual care | 30 天死亡 | 47.8% vs 49.0%；RR 0.98 (0.80–1.19) | Neutral |
| [IPD MA](https://doi.org/10.1016/S0140-6736(23)01607-0) Lancet 2023, n=567 | AMI-CS | Early VA-ECMO vs OMT | 30 天死亡 | OR 0.93 (0.66–1.29) | Neutral |
| [DanGer Shock](https://doi.org/10.1056/NEJMoa2312572) NEJM 2024, n=355 | STEMI-CS、LVEF <45%；排除 OHCA 後昏迷 | Impella CP vs standard care | 180 天死亡 | 45.8% vs 58.5%；HR 0.74 (0.55–0.99) | **Positive** |

> 族群、終點時間點、device 皆不同，**不能直接橫向比較**

---

<!-- _class: divider -->

# Device 證據細看

## Microaxial flow pump ｜ VA-ECMO ｜ IABP

---

# Impella CP：DanGer Shock 的族群

## [Møller JE, et al. NEJM 2024](https://doi.org/10.1056/NEJMoa2312572)

- STEMI 合併心因性休克
- Lactate ≥2.5 mmol/L；SBP <100 mmHg 或需 vasopressor
- LVEF <45%
- **排除：OHCA 後仍昏迷者**
- 2013–2023 年，丹麥、德國、英國 14 中心；中位年齡 67 歲，79.2% 男性

> **180 天全死因死亡 45.8% vs 58.5%**，HR 0.74（95% CI 0.55–0.99），p=0.04
> 絕對差異 −12.7%，NNT ≈ 8；[長期追蹤（NEJM 2025）](https://doi.org/10.1056/NEJMc2508284)死亡率差異持續

---

# Impella CP：代價是併發症

## [Møller JE, et al. NEJM 2024](https://doi.org/10.1056/NEJMoa2312572)

| 指標 | Impella CP | Control | 備註 |
|------|-----------|---------|------|
| Composite safety | **24.0%** | 6.2% | HR 4.74 (2.36–9.55)，NNH ≈ 6 |
| 中重度出血 | **21.8%** | 11.9% | |
| 肢體缺血 | **5.6%** | 1.1% | |
| 腎臟替代療法 (RRT) | **41.9%** | 26.7% | |

> 每治療約 8 人救 1 命，約每 6 人有 1 人發生 safety composite
> 子群分析（女性、MAP 等）屬 hypothesis-generating

---

# VA-ECMO：AMI-CS 例行使用無存活效益

## [ECLS-SHOCK](https://doi.org/10.1056/NEJMoa2307227) ｜ [IPD meta-analysis](https://doi.org/10.1016/S0140-6736(23)01607-0)

| 指標 | ECLS-SHOCK (NEJM 2023) | IPD MA (Lancet 2023) |
|------|------------------------|----------------------|
| 30 天死亡 | 47.8% vs 49.0%；RR 0.98 (0.80–1.19) | OR 0.93 (0.66–1.29) |
| 出血 | 23.4% vs 9.6%；RR 2.44 (1.50–3.95) | OR 2.44 (1.55–3.84) |
| 周邊血管併發症 | 11.0% vs 3.8%；RR 2.86 (1.31–6.25) | OR 3.53 (1.70–7.34) |

- ECLS-SHOCK 有 77% 病人隨機前曾 CPR，族群與 DanGer Shock 很不同
- VA-ECMO 增加 LV afterload；出血與血管併發症明顯增加

> **AMI-CS 不例行使用 VA-ECMO**；保留給 shock team 個別化決策的特定 phenotype（整理人註）

---

# IABP：IABP-SHOCK II

## [Thiele H, et al. NEJM 2012](https://doi.org/10.1056/NEJMoa1208410)

- 600 位 AMI-CS 病人，皆預計早期血行重建（PCI 或 CABG）
- **30 天全死因死亡：39.7% vs 41.3%**，RR 0.96（0.79–1.17），p=0.69 → **Neutral**
- Major bleeding、stroke 等次要終點無顯著差異

> AMI-CS **不例行使用 IABP**

---

<!-- _class: divider -->

# Phenotype-driven 選擇與照護系統

## SCAI SHOCK stage ｜ SHARC ｜ Shock team

---

# 先分期：SCAI SHOCK stage

| Stage | 名稱 | 描述 |
|-------|------|------|
| **A** | At risk | 尚未休克，但屬高風險（如大面積 AMI） |
| **B** | Beginning | 低血壓或心搏過速，尚無灌流不足 |
| **C** | Classic | 灌流不足，需藥物或機械介入 |
| **D** | Deteriorating | 初始處置 ≥30 分鐘後仍未穩定 |
| **E** | Extremis | 循環崩潰、反覆心跳停止、需 ECPR |

- 另有 cardiac arrest modifier（A）
- **再分型：SHARC** — 標準化 CS 定義，區分 AMI-CS 與 HF-CS、LV／RV／BiV phenotype

> 分期回答「多嚴重」，分型回答「哪個心室、什麼病因」，兩者合起來才能選 device

---

# 把 RCT 族群對應到床邊 phenotype

| 床邊 phenotype | 證據 | 實務思考 |
|----------------|------|----------|
| STEMI-CS、LV 衰竭為主、未昏迷 | DanGer Shock（Positive） | 可考慮早期 Impella CP；規劃血管通路、出血與肢體灌流監測 |
| AMI-CS 例行 VA-ECMO | ECLS-SHOCK、IPD MA（Neutral） | 不例行使用 |
| AMI-CS 例行 IABP | IABP-SHOCK II（Neutral） | 不例行使用 |
| OHCA 後昏迷、RV／BiV 衰竭、refractory arrest | 不在 DanGer 族群，證據有限 | Shock team 個別化決策 |

> 整理人依各 RCT 納入條件整理，**非原文建議原句**；正式建議請以原文 Figure／Table 為準

---

# 照護系統：device 之外的成敗關鍵

| 要素 | 內容 |
|------|------|
| **Multidisciplinary shock team** | 介入、重症、心衰竭、心臟外科、灌注師共同決策，一通電話啟動 |
| **Regionalized hub-and-spoke** | Spoke 醫院早期辨識與穩定，及早轉至具 tMCS 能力的 hub |
| **Structured escalation** | 依 SCAI stage 與血行動力學目標，預先定義何時升級支持 |
| **De-escalation／weaning** | 灌流恢復後有計畫地撤除，減少 device 併發症 |
| **Futility 與照護目標** | 事先訂定 futility 標準，與家屬溝通 goals of care |

---

# 回到我們的 CCU：討論題

1. 本院 STEMI-CS 病人中，有多少真正符合 **DanGer Shock 納入條件**？
   - LVEF <45%、非 OHCA 後昏迷、lactate ≥2.5 mmol/L
2. Impella 的**血管通路與出血管理流程**是否標準化？
   - Large-bore access、closure、distal limb perfusion、hemolysis 監測
3. 何時啟動 **shock team**？誰負責 escalation 與 futility 判斷？
   - 書面 protocol 與 SCAI stage 觸發條件

---

<!-- _class: ref -->

# 參考文獻

1. Chieffo A, Iannaccone M, Hassager C, et al. Temporary mechanical circulatory support in cardiogenic shock: a clinical consensus statement of the EAPCI and ACVC of the ESC. [*Eur Heart J*. 2026. PMID 42870411.](https://doi.org/10.1093/eurheartj/ehag708)
2. Møller JE, Engstrøm T, Jensen LO, et al. Microaxial flow pump or standard care in infarct-related cardiogenic shock. [*N Engl J Med*. 2024;390(15):1382–1393. PMID 38587239.](https://doi.org/10.1056/NEJMoa2312572)
3. Møller JE, et al. Long-term outcomes of the DanGer Shock trial. [*N Engl J Med*. 2025;393(10):1037–1038. PMID 40888722.](https://doi.org/10.1056/NEJMc2508284)
4. Thiele H, Zeymer U, Akin I, et al. Extracorporeal life support in infarct-related cardiogenic shock. [*N Engl J Med*. 2023;389(14):1286–1297. PMID 37634145.](https://doi.org/10.1056/NEJMoa2307227)
5. Zeymer U, Freund A, Hochadel M, et al. Venoarterial extracorporeal membrane oxygenation in patients with infarct-related cardiogenic shock: an individual patient data meta-analysis of randomised trials. [*Lancet*. 2023;402(10410):1338–1346. PMID 37643628.](https://doi.org/10.1016/S0140-6736(23)01607-0)
6. Thiele H, Zeymer U, Neumann FJ, et al. Intraaortic balloon support for myocardial infarction with cardiogenic shock. [*N Engl J Med*. 2012;367(14):1287–1296. PMID 22920912.](https://doi.org/10.1056/NEJMoa1208410)

---

<!-- _class: lead -->
<!-- _paginate: false -->

# 謝謝聆聽

## Q & A

**讀書會共筆整理人　謝慕揚 醫師 MD, PhD, FESC**
結構性心臟病與介入心臟學｜重症醫學

> 本內容為讀書會共筆整理，未必涵蓋所有相關文獻
> 僅供學術與教育用途，不代表任何單位之官方立場
> 本內容未涉及任何利益衝突
