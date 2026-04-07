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
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.4em;}
  h2 { color: #0072bc; font-size: 0.9em; }
  h3 { color: #555555; }
  table { font-size: 0.65em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.85em;
  }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.7em; }
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-04-07'
---

<!-- _class: lead -->
# Critical Care 雙週期刊回顧
## 2026-03-24 ～ 2026-04-07
**謝慕揚 MD, PhD, FESC**
ICM · AJRCCM · Critical Care · CCM · Lancet Respir Med

---

# 本期重點 8 大 Pearls

1. **Refractory septic shock 有國際共識定義** (NE-eq >0.5 µg/kg/min + 灌流不全)
2. **三標記免疫模型** 比臨床嚴重度更能預測 sepsis 預後
3. **Non-ARDS 不需高 PEEP** — RELAx Bayesian 重分析
4. **量身高、護女性肺** — 35% 病人沒測身高
5. **Helmet CPAP > HFNC** 卸載呼吸功
6. **Remimazolam** 非劣於 propofol (SHOSREB)
7. **ARDS resolution** 首份 Delphi 共識定義
8. **Frailty** 獨立預測 cardiogenic shock 長期死亡

---

<!-- _class: divider -->
# Sepsis & 免疫調節

---

# Refractory Septic Shock — SCCM/ESICM Delphi 共識
## *Intensive Care Med* 2026 · [DOI](https://doi.org/10.1007/s00134-026-08344-2) · PMID 41874620

- 56 位專家、5 輪 Delphi、13 條共識
- 核心定義：
  - 已完成初步液體復甦
  - **NE-equivalent >0.5 µg/kg/min** (75%)
  - 乳酸升高 (94.6%) 或 CRT 延長 (76.8%)
  - 器官功能不全 (75%)
- 混合性休克應使用 **critical care ultrasound** 評估 (92.9%)

> **意義**：首份「升階決策」的觸發閾值 — 用於救援治療、MCS、trial enrollment

---

# 量化 Sepsis 免疫失調 + CAPE COD 重分析
## *Lancet Respir Med* 2026;14(4):327-340 · [DOI](https://doi.org/10.1016/S2213-2600(25)00429-1) · PMID 41856148

- Derivation n=398，External validation n=1,191 (5 cohorts)
- **3-biomarker model**：PCT + sTREM-1 + IL-6 → DIP1-3 (準確率 91.2%)
- cDIP 每 +10% → 死亡 OR **1.26**；次發感染 OR **1.50**
- **與臨床嚴重度獨立**

**CAPE COD 重分析**：hydrocortisone 在嚴重 CAP
- DIP3：OR 0.25 (0.05–0.85), p=0.042
- cDIP ≥0.63：OR 0.21 (0.10–0.72), p=0.011
- 用「臨床嚴重度」分層 → **看不到任何益處**

> **意義**：為何 sepsis 類固醇試驗結果不一致 — 沒有抓對族群

---

<!-- _class: divider -->
# ARDS 與機械通氣

---

# ARDS Resolution Delphi 共識
## *Crit Care Med* 2026 · [DOI](https://doi.org/10.1097/CCM.0000000000007107) · PMID 41925519

**首份「ARDS 解除」操作型定義**

1. **缺氧解除**
   - PaO2/FiO2 **>300** (或 SpO2/FiO2 >315)
   - 持續 **>24 小時**

2. **呼吸支持回歸正常**
   - 若仍插管，必須是非呼吸性原因
   - PEEP **≤5 cmH2O**
   - 無 prone / NMB / ECMO 等輔助治療

> **意義**：終於有標準終點 — 試驗、weaning、預後溝通通用

---

# RELAx Bayesian 重分析 — Non-ARDS PEEP
## *Crit Care Med* 2026 · [DOI](https://doi.org/10.1097/CCM.0000000000007117) · PMID 41914828

| 結果指標 | Lower PEEP (0–5) 較佳的後驗機率 |
|---------|-------------------------------|
| **VFD-28** OR 1.08 (0.87–1.35) | **75–78%** |
| **死亡率** | **72–89%** |
| 通氣時間縮短 | 11–28% |

> **意義**：非 ARDS 病人預設 **physiologic PEEP 5** 即足夠。常規高 PEEP 沒有好處且可能有害。

---

# 性別 × 潮氣容積 × 死亡 — Toronto Cohort
## *Crit Care Med* 2026 · [DOI](https://doi.org/10.1097/CCM.0000000000007103) · PMID 41914820

- **20,351 位** 機械通氣 ≥24 h，38% 女性
- Bayesian joint model (時變嚴重度)
- 每 +1 mL/kg PBW → 死亡 **HR 1.10** (1.07–1.13)
- 女性整個病程 VT/PBW 持續高於男性
- **35% 病人無身高紀錄**

> **意義**：肺保護差距不是「不會」、是「沒量身高」。**測量並記錄身高** 是最簡單的肺保護。

---

# HFNC vs Helmet CPAP vs COT — Crossover
## *Crit Care Med* 2026 · [DOI](https://doi.org/10.1097/CCM.0000000000007116) · PMID 41925582

- 33 位 AHRF 成人 crossover 比較

| 模式 | 分鐘通氣量 | 吸氣努力 (ΔPes) |
|------|----------|---------------|
| COT | 10.9 L/min | 高 |
| HFNC 60 L/min | 8.8–9.3 | 中 |
| **Helmet CPAP PEEP 10** | 8.8–9.3 | **最低** |

> **意義**：對自呼吸 AHRF 病人，**Helmet CPAP (PEEP 10) 比 HFNC 更能卸載吸氣努力**，可能降低 P-SILI 風險。

---

<!-- _class: divider -->
# 鎮靜與藥理

---

# SHOSREB — Remimazolam vs Propofol 輕度鎮靜
## *Intensive Care Med* 2026 · [DOI](https://doi.org/10.1007/s00134-026-08381-x) · PMID 41915173

- 多中心、單盲、非劣性 RCT，**164 位** 機械通氣病人
- Remimazolam besylate 0.20 mg/kg/h vs Propofol 0.61 mg/kg/h
- **鎮靜成功率 97.5% vs 97.5%** (差距 0%, 95% CI −6.5 ~ 6.4%)
- 達標 RASS 時間 88.6% vs 89.4% (p=0.54)
- **符合非劣性**

> **意義**：Remimazolam = 超短效 BZD、可 flumazenil 反轉、無 PRIS、不影響 TG。Propofol 禁忌 (高 TG、嚴重血流動力學不穩) 時的合理選擇。

---

<!-- _class: divider -->
# Cardiogenic Shock & ECMO

---

# Frailty 與 Cardiogenic Shock 長期死亡
## *Crit Care* 2026 · [DOI](https://doi.org/10.1186/s13054-026-05962-6) · PMID 41882780

- 雙國多中心 cohort
- Clinical Frailty Scale 評估入院前 frailty
- **校正休克嚴重度後，frailty 仍獨立預測長期死亡**

> **意義**：心因性休克決策不能只看血流動力學。Frailty 應納入：
> - MCS / 心臟移植評估
> - GOC 與家屬討論
> - 升階治療的權衡

---

# STORM-ECMO — V-A ECMO 上的早期 VT Ablation
## *Crit Care* 2026 · [DOI](https://doi.org/10.1186/s13054-026-05969-z) · PMID 41877285

- Refractory electrical storm 需要 V-A ECMO 的多中心 cohort
- **早期 VT ablation** vs 延遲
- 早期 ablation 與較佳的：
  - ECMO weaning
  - 存活率

> **意義**：在電氣風暴需 ECMO 情境，**不要為了「等穩定」而延遲 ablation** — ECMO 本身就是讓 ablation 安全進行的平台。

---

<!-- _class: divider -->
# Honorable Mentions

---

# 其他值得關注

| 主題 | 重點 |
|------|------|
| Severe pancreatitis 表型 | K-means 3 phenotypes；K2 renal-dominant 死亡率 44.8% |
| CRRT lower vs standard dose | Systematic review / meta-analysis |
| ICU 肌肉萎縮超音波 | 預測功能性結局 meta-analysis |
| Influenza-associated aspergillosis | 發生率與抗黴菌預防 |
| DPP3 與 angiotensin II | Vasopressor biomarker-guided 選擇 |
| Korea LST Decision Act | 380,488 病人 IHCA 影響 |
| Rilzabrutinib (BTK inhibitor) | Phase 2 RCT 主要終點未達顯著 |

---

# 本期觀察

1. **AJRCCM** 在此 2 週窗口 PubMed 無收錄 — 下次補回顧
2. 兩份 **Delphi 共識** 同期登場 → 重症進入「定義精準化」時代
3. **Precision medicine in sepsis** 邁出實質一步：免疫表型 > 臨床嚴重度
4. **Lung-protective ventilation 的差距** 來自「沒量身高」，不是「不會做」

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
2026-04-07

---

<!-- _class: small-text -->
# 參考文獻 (1/2)

1. Leone M, et al. Refractory septic shock SCCM/ESICM Delphi. [*Intensive Care Med* 2026.](https://doi.org/10.1007/s00134-026-08344-2) PMID 41874620
2. Yang X, et al. SHOSREB: Remimazolam vs propofol. [*Intensive Care Med* 2026.](https://doi.org/10.1007/s00134-026-08381-x) PMID 41915173
3. Michels EHA, et al. 3-biomarker immune model + CAPE COD reanalysis. [*Lancet Respir Med* 2026;14(4):327-340.](https://doi.org/10.1016/S2213-2600(25)00429-1) PMID 41856148
4. Weir TE, et al. ARDS resolution Delphi consensus. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007107) PMID 41925519
5. Caroli A, et al. RELAx Bayesian reanalysis. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007117) PMID 41914828

---

<!-- _class: small-text -->
# 參考文獻 (2/2)

6. Coppola S, et al. HFNC vs helmet CPAP vs COT crossover. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007116) PMID 41925582
7. Urner M, et al. Sex-specific tidal volumes and mortality. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007103) PMID 41914820
8. Frailty in cardiogenic shock binational cohort. [*Crit Care* 2026;30(1).](https://doi.org/10.1186/s13054-026-05962-6) PMID 41882780
9. STORM-ECMO. VT ablation timing on V-A ECMO. [*Crit Care* 2026.](https://doi.org/10.1186/s13054-026-05969-z) PMID 41877285
10. Maspero JF, et al. Rilzabrutinib phase 2 in asthma. [*Lancet Respir Med* 2026.](https://doi.org/10.1016/S2213-2600(25)00439-4) PMID 41936356
