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
  section.lead h1 { color: #ffffff; font-size: 2.0em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #ffd166; }
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
  section.ref { font-size: 0.7em; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; font-size: 0.9em; font-weight: normal; }
  h3 { color: #555555; }
  table { font-size: 0.7em; width: 100%; }
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
footer: '謝慕揚 MD, PhD, FESC | CHIP-BCIS3 — Microaxial Flow Pump in High-Risk PCI | NEJM 2026'
---

<!-- _class: lead -->
# Left Ventricular Unloading in High-Risk PCI
## CHIP-BCIS3 — 隨機對照試驗
**謝慕揚 MD, PhD, FESC** | 2026-05-07
[Perera D, et al. *N Engl J Med* 2026;394:1779-89](https://doi.org/10.1056/NEJMoa2515704)

---

# 為什麼這篇文獻重要？
## 「Protected PCI」的證據基礎，2026 年的最新 RCT

- 嚴重 LV dysfunction + 複雜 CAD 病人 PCI 死亡率高
- Microaxial flow pump (Impella CP) 過去十年使用量大幅成長，但**缺乏 vs. no MCS 的 RCT**
- 既有試驗：
  - **PROTECT II (2012)** — Impella vs. IABP，提早因 futility 終止
  - **DanGer Shock (2024)** — Impella CP 在 STEMI + shock 降低死亡

> **CHIP-BCIS3 的問題**：在「**沒有 shock**」的高風險擇期 PCI，事先放 Impella 到底有沒有用？

---

<!-- _class: divider -->
# Study Design
## Open-label RCT, 21 UK centers

---

# 試驗設計
## [Perera D, et al. *NEJM* 2026](https://doi.org/10.1056/NEJMoa2515704)

| 項目 | mAFP 組 (N=148) | SOC 組 (N=152) |
|------|-----------------|----------------|
| 干預 | **Elective Impella CP** before PCI | No planned MCS |
| Bailout MCS | — | 允許 IABP / VA-ECMO 但禁止 mAFP |
| Crossover | 不允許 | 不允許 |

**1:1 隨機分派 | NIHR 資助 | NCT05003817**

---

# 納入條件 (Key Inclusion)

- **LVEF ≤ 35%**（severe MR 時 ≤ 45%）
- **BCIS-JS ≥ 8**（範圍 0–12）
- **Complex PCI**（至少符合一項）：
  - Unprotected LM + occluded dominant RCA、left dominant、bifurcation
  - 多血管/LM/last conduit 的 calcium modification、或 SYNTAX ≥ 32
  - Retrograde CTO

**排除**：cardiogenic shock at randomization、acute STEMI、已使用 MCS

---

# Endpoints

**Primary：階層複合 (Win Ratio 分析)**
1. All-cause death
2. Disabling stroke
3. Spontaneous MI
4. CV hospitalization 次數
5. Periprocedural myocardial injury（hsTnT ↑ ≥ 20% baseline 或 ≥ 5×ULN）

**Sample size**：N=300，假設 win ratio ≥ 1.6 → 85% power

> Win Ratio > 1 = mAFP 較佳；< 1 = SOC 較佳

---

<!-- _class: divider -->
# Population
## 高齡、嚴重低 LVEF、極高解剖複雜度

---

# Baseline Characteristics
## [Perera D, et al. *NEJM* 2026](https://doi.org/10.1056/NEJMoa2515704)

| 變項 | mAFP (N=148) | SOC (N=152) |
|------|-------------|-------------|
| 年齡 (mean) | 72.2 ± 10.1 | 73.3 ± 9.3 |
| 男性 | 84.5% | 80.9% |
| Diabetes | **56.1%** | 48.0% |
| Previous PCI / CABG | 22.3% / 7.4% | 22.4% / 3.3% |
| **LVEF (median)** | **26%** | **28%** |
| **BCIS-JS (median)** | **12** | **12** |
| **SYNTAX (median)** | **38** | **38** |
| Urgent indication | 72.3% | 79.6% |

> 名副其實的「最高風險、最複雜」族群

---

# PCI 與 MCS 使用情形
## [Perera D, et al. *NEJM* 2026](https://doi.org/10.1056/NEJMoa2515704)

- **PCI 完成率**：299/300 (99.7%)
- **mAFP 成功置入**：144/148 **(97.3%)**
  - 2 例失敗（嚴重 PVD）、1 例置入時血管併發症、1 例 ALI
- **Staged PCI**：mAFP **10 人** vs. SOC **27 人**
- **SOC 組 Bailout MCS**：**9 人 (6.0%)**——8 IABP + 1 mAFP

> 94% 的 SOC 組病人「不需任何 MCS」就完成複雜 PCI

---

<!-- _class: divider -->
# Primary Outcome
## Win Ratio 0.85 (95% CI, 0.63–1.15) — Negative

---

# 主要終點 — Win Ratio
## [Perera D, et al. *NEJM* 2026](https://doi.org/10.1056/NEJMoa2515704)

22,496 對 pairwise 比較，中位追蹤 22 個月：

| 結果 | 數值 |
|------|------|
| mAFP 勝出 | **36.6%** |
| SOC 勝出 | **43.0%** |
| Tie | 20.4% |
| **Win Ratio** | **0.85 (95% CI, 0.63–1.15)** |
| **P value** | **0.30** |
| 差異 | −6.4 percentage points (−18.4 to +5.7) |

> **Negative trial**；point estimate 偏向 SOC 較佳

---

# 各階層拆解
## [Perera D, et al. *NEJM* 2026](https://doi.org/10.1056/NEJMoa2515704)

| 階層 | mAFP 勝出 % | SOC 勝出 % | 差異（百分點） |
|-----|------------|-----------|---------------|
| **Death from any cause** | 16.4 | 23.4 | **−7.0** |
| Disabling stroke | 0.8 | 0.6 | +0.2 |
| Spontaneous MI | 4.6 | 1.9 | +2.6 |
| CV hospitalization | 8.2 | 6.5 | +1.7 |
| **Periprocedural MI** | 6.6 | 10.5 | **−3.9** |

> 第一個 tier (death) 就把全局拉向 SOC

---

# 次族群分析

- 整體效果在預設 subgroups **broadly 一致**
- 唯一達 nominally significant 的次族群：
  - **Female: Win Ratio 0.57 (95% CI, 0.36–0.91)**——偏向 SOC

> 次族群分析為 hypothesis-generating；女性可能受到 mAFP 傷害較大，但需確認

---

<!-- _class: divider -->
# Secondary Outcomes
## CV 死亡率訊號 — Significant Increase

---

# 次要終點（24 個月累積發生率）
## [Perera D, et al. *NEJM* 2026](https://doi.org/10.1056/NEJMoa2515704)

| 終點 | mAFP | SOC | HR / RR (95% CI) |
|-----|------|-----|-----------------|
| **All-cause death** | 32.6% | 23.4% | **HR 1.54 (0.99–2.41)** |
| **CV death** | 26.7% | 14.5% | **HR 1.91 (1.11–3.30)** ★ |
| Disabling stroke | 3.5% | 4.5% | HR 0.53 (0.13–2.11) |
| Spontaneous MI | 6.8% | 12.4% | HR 0.64 (0.28–1.47) |
| CV hospitalization | 24.5% | 21.0% | HR 1.20 (0.72–1.98) |
| **Periprocedural MI** | **61.7%** | **50.0%** | **RR 1.23 (0.99–1.54)** |

★ **24 個月時 CV 死亡絕對增加 +12.2 百分點**

---

# 重點訊號

> **三大警訊**：
> 1. **CV 死亡顯著增加**（HR 1.91, 95% CI 1.11–3.30）
> 2. **Periprocedural MI 反而較多**（與「unloading 保護心肌」假說相反）
> 3. 兩組 revascularization 完整度幾乎一樣（residual SYNTAX 14 vs. 13；CRI 67% vs. 67%）

> **mAFP 沒有帶來「可以做更完整 revascularization」的理論優勢**

---

# 安全性 — 出血與血管併發症
## [Perera D, et al. *NEJM* 2026](https://doi.org/10.1056/NEJMoa2515704)

| 併發症 | mAFP (N=148) | SOC (N=151) | RR (95% CI) |
|-------|-------------|-------------|-------------|
| Major bleeding | 10.8% | 7.3% | 1.48 (0.71–3.09) |
| Minor vascular complication | 15.5% | 9.9% | 1.56 (0.85–2.88) |
| Major vascular complication | 1.4% | 0.7% | — |

> 強制術前 CT + ultrasound-guided access
> → trial 環境下血管併發症率比 real-world 低
> → **可能低估了 mAFP 的真實缺點**

---

<!-- _class: divider -->
# 三大試驗整合判讀
## CHIP-BCIS3 vs. PROTECT II vs. DanGer Shock

---

# Microaxial Flow Pump 的證據地圖

| 試驗 | 族群 | 比較 | 結果 |
|------|------|------|------|
| [PROTECT II 2012](https://doi.org/10.1161/CIRCULATIONAHA.112.098194) | Elective HR-PCI | Impella vs. IABP | Neutral, 提早終止 |
| [**CHIP-BCIS3 2026**](https://doi.org/10.1056/NEJMoa2515704) | Elective HR-PCI | **Impella vs. no MCS** | **Negative；CV death ↑** |
| [DanGer Shock 2024](https://doi.org/10.1056/NEJMoa2312572) | STEMI + cardiogenic shock | Impella vs. SOC | **Mortality ↓** |

> DanGer 的療效**不能外推到非 shock 的「預防性使用」**

---

# 臨床判讀：The Verdict

> **不論你過去多麼習慣 Protected PCI**：
> - **Cardiogenic shock**：可考慮 mAFP（DanGer evidence）
> - **High-risk PCI 但無 shock**：**不應該**作為常規（CHIP-BCIS3 evidence）
> - **Bailout 用途**：保留 standby、不常規植入

> 過去 registries / propensity-matched studies 顯示的「Impella 優勢」很可能是**選樣偏差**

---

<!-- _class: divider -->
# Limitations & Pearls

---

# Limitations

1. **N=300 偏小**——但實際事件率高於預期，type II error 風險低
2. **強制血管評估**——血管併發症率比 real-world 低，可能低估缺點
3. **追蹤中位 22 個月**——但 KM curves 已分歧偏向 SOC，更長追蹤不太可能反轉
4. **排除 cardiogenic shock**——不能外推（DanGer 已答）
5. **單一國家試驗**（英國 NHS）——對美國等體系外推性有限

---

# Clinical Pearls — 給新竹院 cath lab

1. **Elective Protected PCI 不應作為常規**——LVEF ≤ 35% + extensive CAD 但**無 shock**，預先放 Impella 不會改善預後，甚至**可能增加 CV 死亡**
2. **Bailout 仍有價值**——6% SOC 病人需要 bailout，多用 IABP；保留 standby
3. **Cardiogenic shock 仍照原則使用**——DanGer 結果未被動搖
4. **Vascular access 是關鍵**——若使用 mAFP，**術前 CT + ultrasound-guided puncture 是標配**
5. **「Complete revascularization」可分次完成**——SOC 組 staged PCI 多但結果反而較好

---

# 給會診同事的話術

> **「2026 年 NEJM 的 CHIP-BCIS3 顯示，計畫性放 Impella 在沒有 shock 的高風險 PCI 不但無益，CV 死亡風險還增加（HR 1.91, 95% CI 1.11–3.30）。我們把 Impella 留到真的需要 bailout 時再用，更符合實證。」**

---

<!-- _class: divider -->
# 參考文獻

---

<!-- _class: ref -->
# 參考文獻 (1/2)

1. Perera D, Ryan M, Ezad SM, et al. Left Ventricular Unloading in High-Risk PCI. [*N Engl J Med* 2026;394(18):1779-89.](https://doi.org/10.1056/NEJMoa2515704)
2. Perera D, Stables R, Thomas M, et al. Elective IABP during high-risk PCI: BCIS-1. [*JAMA* 2010;304(8):867-74.](https://doi.org/10.1001/jama.2010.1190)
3. O'Neill WW, Kleiman NS, Moses J, et al. PROTECT II: Impella 2.5 vs. IABP. [*Circulation* 2012;126:1717-27.](https://doi.org/10.1161/CIRCULATIONAHA.112.098194)
4. Møller JE, Engstrøm T, Jensen LO, et al. DanGer Shock: Microaxial flow pump in infarct-related cardiogenic shock. [*N Engl J Med* 2024;390:1382-93.](https://doi.org/10.1056/NEJMoa2312572)

---

<!-- _class: ref -->
# 參考文獻 (2/2)

5. Ryan M, Ezad SM, Webb I, et al. CHIP-BCIS3 rationale and design. [*Circ Cardiovasc Interv* 2024;17(3):e013367.](https://doi.org/10.1161/CIRCINTERVENTIONS.123.013367)
6. Pocock SJ, Ariti CA, Collier TJ, Wang D. The win ratio. [*Eur Heart J* 2012;33(2):176-82.](https://doi.org/10.1093/eurheartj/ehr352)
7. Lawton JS, Tamis-Holland JE, Bangalore S, et al. 2021 ACC/AHA/SCAI guideline for coronary artery revascularization. [*Circulation* 2022;145(3):e18-e114.](https://doi.org/10.1161/CIR.0000000000001038)
8. Sianos G, et al. The SYNTAX Score. [*EuroIntervention* 2005;1(2):219-27.](https://pubmed.ncbi.nlm.nih.gov/19758907/)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
2026-05-07

[Perera D, et al. *N Engl J Med* 2026;394:1779-89](https://doi.org/10.1056/NEJMoa2515704)
