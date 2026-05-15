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
  section.abbr {
    font-size: 0.72em;
    background-color: #f8f9fa;
  }
  section.abbr h1 { color: #ba181b; border-bottom: 3px solid #ba181b; font-size: 1.3em; padding-bottom: 0.2em; }
  section.ref {
    font-size: 0.62em;
    background-color: #f8f9fa;
  }
  section.ref h1 { color: #0072bc; border-bottom: 2px solid #0072bc; font-size: 1.3em; padding-bottom: 0.2em; }
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
footer: '謝慕揚 MD, PhD, FESC | Critical Care Biweekly Review | 2026-05-15'
---

<!-- _class: lead -->
# Critical Care 雙週期刊回顧
## 2026-05-01 ～ 2026-05-15
**謝慕揚 MD, PhD, FESC**
ICM · Crit Care · CCM · Lancet Respir Med · AJRCCM · Ann Intensive Care · Resuscitation

---

<!-- _class: abbr -->
# 縮寫對照 (1/2) — 通氣 · 感染 · 腎臟

| 縮寫 | 英文全稱 | 中文 |
|------|----------|------|
| PBW | Predicted Body Weight | 預測體重 |
| DP | Driving Pressure | 驅動壓 (Pplat − PEEP) |
| PEEP | Positive End-Expiratory Pressure | 呼氣末正壓 |
| FRC | Functional Residual Capacity | 功能殘留量 |
| VILI | Ventilator-Induced Lung Injury | 呼吸器誘發肺損傷 |
| NIV | Non-invasive Ventilation | 非侵入性通氣 |
| HFNC | High-Flow Nasal Cannula | 高流量鼻導管氧療 |
| SFR | SpO₂/FiO₂ Ratio | 脈氧飽和度/吸氧濃度比值 |
| ELF | Epithelial Lining Fluid | 肺泡上皮表面液 |
| TDM | Therapeutic Drug Monitoring | 治療藥物濃度監測 |
| CI | Continuous Infusion | 持續輸注 |
| MIC | Minimum Inhibitory Concentration | 最低抑菌濃度 |
| AKI | Acute Kidney Injury | 急性腎損傷 |
| CRRT | Continuous Renal Replacement Therapy | 連續性腎臟替代治療 |
| RCA | Regional Citrate Anticoagulation | 局部枸橼酸抗凝 |

---

<!-- _class: abbr -->
# 縮寫對照 (2/2) — 血流動力學 · 復甦 · 統計

| 縮寫 | 英文全稱 | 中文 |
|------|----------|------|
| ECMO | Extracorporeal Membrane Oxygenation | 體外膜氧合 |
| CVP | Central Venous Pressure | 中心靜脈壓 |
| PPV | Pulse Pressure Variation | 脈壓變異度 |
| VExUS | Venous Excess Ultrasound | 靜脈鬱血超音波評估 |
| OHCA | Out-of-Hospital Cardiac Arrest | 院外心跳停止 |
| MPA | Manual Pressure Augmentation | 手動加壓輔助除顫 |
| TTI | Transthoracic Impedance | 胸腔阻抗 |
| OSFD | Organ Support-Free Days | 器官支持無需天數 |
| NMA | Network Meta-Analysis | 網絡整合分析 |
| aOR | Adjusted Odds Ratio | 校正後勝算比 |
| CrI | Credible Interval | 可信區間 (Bayesian) |
| PP | Posterior Probability | 後驗機率 (Bayesian) |
| PTA | Probability of Target Attainment | 目標達成率 |
| MDR | Multidrug-resistant | 多重抗藥性 |
| EBV | Epstein-Barr Virus | EB 病毒 |

---

# 本期重點 10 大 Pearls

1. **PBW 高估女性肺容積** → 4.2% 超額 DP ≥15 風險 → 8.4% 超額死亡 (ICM)
2. **Etomidate ≈ Ketamine 死亡率**；Ketamine 增加血流動力學不穩 (Crit Care NMA)
3. **肥胖 ICU 插管**：NIV 全程前給氧 + Videolaryngoscopy 常規化 (ICM Review)
4. **TOL/TAZ & CAZ/AVI 標準 CI 劑量** 均可達 ELF PK/PD 目標 (Crit Care RCT)
5. **EBV 再活化 + Immunoparalysis** = 敗血症有害免疫內型 (Crit Care)
6. **Citrate CRRT 代謝併發症** — Delphi 共識監測與管理框架 (Crit Care)
7. **ADQI/ELSO 共識**：ECMO 病人 AKI + 液體 + CRRT 管理 (ICM)
8. **液體去升階梯**：正液體平衡 = 工作診斷；五大補液陷阱 (Ann Intensive Care)
9. **MPA 除顫 RCT 陰性**：降低 TTI 但存活率相同 AOR 1.00 (Resuscitation)
10. **REMAP-CAP Ivermectin 陰性**：重症 PP 優越性 44.2%，關閉問題 (CCM)

---

<!-- _class: divider -->
# 機械通氣與肺保護

---

# PBW 方程式高估女性肺容積
## *Intensive Care Med* 2026 · [DOI](https://doi.org/10.1007/s00134-026-08442-1) · PMID 42096093

**設計**：10 個 Randomized Controlled Trial (RCT) + 2 個真實世界資料集；n=**30,516**（39.4% 女性）

| 指標 | 數值 | 意義 |
|------|------|------|
| 女性 Driving Pressure (DP) ≥15 cmH₂O 超額風險 | **+4.2%**（aOR 1.26） | 相同 Vt/kg PBW 但肺更小 |
| CT 測量肺容積差異 | 女性少 **343 mL** | 解釋超額 DP 風險 |
| 超額 28 天死亡（DP 介導）| **8.4%** | 量化臨床後果 |

> **解方**：以 **DP ≤15 cmH₂O** 個人化驅動壓目標替代固定 Vt/kg PBW 通氣

---

<!-- _class: divider -->
# 緊急插管與氣道管理

---

# 緊急插管誘導藥物 — Network Meta-Analysis (NMA)
## *Crit Care* 2026 · [DOI](https://doi.org/10.1186/s13054-026-06067-w) · PMID 42121165

**設計**：9 個 RCT，**4,672 位**重症成人；Etomidate vs Ketamine vs Propofol vs Ketofol

| 比較 | 死亡率 OR (95% CI) | 確定性 |
|------|--------------------|--------|
| Ketamine vs **Etomidate** | 0.96 (0.80–1.16) | 中等 |
| Ketamine vs Propofol | 1.53 (0.80–2.93) | 低 |
| Etomidate vs Propofol | 0.63 (0.32–1.24) | 極低 |

**Ketamine vs Etomidate 次要結果**（Ketamine 較多）：
- 心血管塌陷 (Cardiovascular Collapse)：OR **1.44** (1.20–1.71) 中等確定性
- 插管後低血壓 (Post-induction Hypotension)：OR **1.34** (1.07–1.68) 低確定性
- Vasopressor 使用：OR **1.45** (1.21–1.74) 低確定性

> **結論**：死亡率相近，但 Ketamine 反而增加血流動力學不穩定；Propofol 幾乎無 RCT 依據

---

# 肥胖重症病人的氣道管理
## *Intensive Care Med* 2026 · [DOI](https://doi.org/10.1007/s00134-026-08454-x) · PMID 42126552

**核心挑戰**
- 頸部脂肪 → 氣道狹窄、Functional Residual Capacity (FRC) 大幅降低
- **安全窒息時間 (Safe Apnea Time) 極短**（有時 <60 秒）

| 步驟 | 建議 |
|------|------|
| 前給氧 | 從誘導前到喉鏡期間 **NIV 全程維持** |
| 血流動力學 | 評估前負荷、心縮力、右心室應力 |
| 插管技術 | 優先 **Videolaryngoscopy**（常規化）|
| 高難度氣道 | 考慮**清醒插管** |
| 誘導藥物 | Ketamine 或 Etomidate 均可 |

> **重點**：肥胖病人不是「難插管」，而是「難維持氧合」— 先給氧，後插管

---

<!-- _class: divider -->
# ARDS 定義更新

---

# 2023 Global ARDS 定義 — SpO₂/FiO₂ 的流行病學效度
## *Crit Care* 2026 · [DOI](https://doi.org/10.1186/s13054-026-06043-4) · PMID 42104520

**背景**：2023 Global 定義擴大納入 High-Flow Nasal Cannula (HFNC) 病人，並允許用 SpO₂/FiO₂ Ratio (SFR) 替代 PaO₂/FiO₂ (P/F) 定義缺氧

| 定義 | 限制 | 擴大意義 |
|------|------|---------|
| 2012 Berlin | 僅插管病人 | 適合試驗但排除了早期病人 |
| **2023 Global** | 含 HFNC + SFR | 涵蓋更廣，流行病學反映更真實 |

- 本研究確認：SFR 在擴大定義下的**預後效度**與 P/F 相近
- Global 定義下 ARDS 發生率顯著提升（納入了過去「隱性 ARDS」的 HFNC 族群）

> **臨床意義**：HFNC 上的病人若 SFR 達缺氧閾值，**應視為 ARDS** — 評估俯臥位、監測 P-SILI

---

<!-- _class: divider -->
# 感染症與抗生素藥動學

---

# TOL/TAZ vs CAZ/AVI 持續輸注的肺部滲透 — 隨機 PK 試驗
## *Crit Care* 2026 · [DOI](https://doi.org/10.1186/s13054-026-06075-w) · PMID 42129898

**設計**：n=30，1:1 隨機，ICU Nosocomial Pneumonia；血漿 + 支氣管肺泡灌洗 (BAL) 測量 Epithelial Lining Fluid (ELF) 濃度

| 藥物成分 | ELF/血漿 AUC 比值 (Median) |
|----------|---------------------------|
| Ceftolozane (TOL/TAZ) | **0.66** |
| Tazobactam (TOL/TAZ) | 0.44 |
| Ceftazidime (CAZ/AVI) | 0.41 |
| Avibactam (CAZ/AVI) | 0.44 |

- 標準 Continuous Infusion (CI) 劑量：兩藥均可達 ELF Probability of Target Attainment (PTA) 目標
- 嚴格目標（Tazobactam CT ≥4 mg/L）→ TOL/TAZ PTA 下降
- 個體間變異度大 → **建議 Therapeutic Drug Monitoring (TDM)**

> **結論**：兩藥均有足夠 ELF 滲透；CI 給藥為首選；TDM 是個人化的關鍵

---

<!-- _class: divider -->
# 敗血症免疫調節

---

# EBV 再活化與 Immunoparalysis — 敗血症有害免疫內型
## *Crit Care* 2026 · [DOI](https://doi.org/10.1186/s13054-026-05966-2) · PMID 42098862

**概念**：Sepsis 同時存在「過度發炎」與「免疫麻痺 (Immunoparalysis)」兩個對立免疫臂

```text
Sepsis 早期 → 過度發炎主導
Sepsis 後期 → 免疫麻痺 (Immunoparalysis) 主導
              ↑
        EBV 再活化標誌此內型
```

- **EBV 再活化 + Immunoparalysis 共存** = 有害免疫內型 (Harmful Immune Endotype)
- 與器官衰竭、次發感染及死亡高度相關
- 提示：精準免疫調節治療應鎖定此族群（如 IFN-γ、GM-CSF）

> **臨床意義**：感染控制後仍持續惡化的病人 → 考慮 EBV 監測；「燒退了卻繼續衰竭」可能是免疫麻痺在作怪

---

<!-- _class: divider -->
# 腎臟替代治療與液體管理

---

# Regional Citrate Anticoagulation (RCA) 代謝併發症 — Delphi 共識
## *Crit Care* 2026 · [DOI](https://doi.org/10.1186/s13054-026-06066-x) · PMID 42129846

**背景**：RCA 已成 Continuous Renal Replacement Therapy (CRRT) 首選抗凝，但 Citrate 代謝障礙（肝衰竭、低心輸出量）時有 Citrate Accumulation 風險

| 問題 | 共識建議 |
|------|---------|
| 適應症評估 | 依肝功能 + 血流動力學個別化決定 |
| 監測指標 | Total Ca / Ionized Ca 比值 → **>2.5 = 累積警示** |
| 發生累積時 | 降低 Citrate 輸注率或改 Heparin 抗凝 |
| 代謝性鹼中毒 | 降低 Citrate 劑量，調整 Bicarbonate 補充 |

> **重點**：RCA 不是「開了就放著」— 肝衰竭、重症休克病人**必須定期監測** Ca²⁺ 比值

---

# ADQI/ELSO 共識：ECMO 期間 AKI + 液體 + CRRT 管理
## *Intensive Care Med* 2026 · [DOI](https://doi.org/10.1007/s00134-026-08440-3) · PMID 42113209

**2025 年 6 月第 36 屆 Acute Disease Quality Initiative (ADQI)** × Extracorporeal Life Support Organization (ELSO) 聯合共識

| 工作組 | 核心主題 |
|--------|---------|
| 1 | Acute Kidney Injury (AKI) 流行病學、危險因子 (~50% ECMO 病人) |
| 2 | 液體管理：正液體平衡獨立預測死亡 |
| 3 | Continuous Renal Replacement Therapy (CRRT) 適應症與液體移除時機 |
| 4 | ECMO 上 CRRT 操作最佳實踐（迴路整合、抗凝） |
| 5 | 生物標記、抗生素及 Vasopressor 在 ECMO 的藥動學變化 |

> **臨床意義**：ECMO + CRRT 並不罕見，PK 變化大 — 抗生素劑量需重新計算，不能沿用標準劑量

---

# 液體去升階梯：如何執行 + 五大陷阱
## *Ann Intensive Care* 2026 · [DOI 1](https://doi.org/10.1016/j.aicoj.2026.100075) · PMID 42111229 | [DOI 2](https://doi.org/10.1016/j.aicoj.2026.100074) · PMID 42125087

**ROSE 四時相框架**（Fluid De-escalation = Stabilization + Evacuation 期）

**五大補液陷阱（Van Regenmortel 評論）**

| 陷阱 | 常見錯誤 | 正確做法 |
|------|---------|---------|
| 1 | 混淆復甦/維持/補充三種指徵 | 每瓶明確標記目的 |
| 2 | 忽視隱藏液體來源（每日 1-2 L）| 計算所有輸入 |
| 3 | 低估高氯/高鈉負擔 | 優先 Balanced Crystalloids |
| 4 | 反射性補液（乳酸↑、CVP↓、尿量↓）| 動態預測指標先測試 |
| 5 | 只看 Fluid Responsiveness，不看 Fluid Tolerance | 搭配 VExUS 等評估 |

> **觀念**：液體過負荷 = 獨立工作診斷；去液化應像脫呼吸器一樣有結構化計畫

---

<!-- _class: divider -->
# 心肺復甦術

---

# 手動加壓輔助除顫 (MPA) — 隨機對照試驗
## *Resuscitation* 2026;224:111121 · [DOI](https://doi.org/10.1016/j.resuscitation.2026.111121) · PMID 42092447

**設計**：澳洲 216 救護站 Cluster-RCT；可電擊心律的 Out-of-Hospital Cardiac Arrest (OHCA)；**n=560**

- **MPA**：電擊瞬間維持雙手加壓，降低 Transthoracic Impedance (TTI)

| 終點 | 介入 | 對照 | 效果 |
|------|------|------|------|
| **存活出院（主要）** | 39.8% | 39.9% | **AOR 1.00** (0.71–1.40) p=0.99 ❌ |
| TTI 降低 | ✅ 顯著 (-8.5 Ω) | — | 物理目標達成 |
| 12 個月存活 | 相似 | 相似 | — |

**限制**：MPA 執行率僅 **23.6%**；試驗提前終止

> **結論**：MPA 降低 TTI 但無臨床益處；低執行率是主要挑戰；**不建議常規推廣**

---

<!-- _class: divider -->
# 平台試驗報告

---

# REMAP-CAP：Ivermectin vs COVID-19 住院病人 — 陰性
## *Crit Care Med* 2026 · [DOI](https://doi.org/10.1097/CCM.0000000000007134) · PMID 42101205

**設計**：多國多因素適應性平台 RCT；巴基斯坦 / 印度 / 愛爾蘭；2021.06–2022.09
**主要終點**：Organ Support-Free Days (OSFD)（有序尺度，死亡賦值 -1）

| 次族群 | OSFD aOR (95% CrI) | PP 優越性 |
|--------|-------------------|-----------|
| 重症 (n=61) | **0.94** (0.40–2.07) | **44.2%** ❌ |
| 非重症 (n=89) | **1.04** (0.48–2.34) | **53.7%** — |

- 重症院內存活 35.1% vs 37.5%（aOR 1.00）
- 因外部無效性證據（院外 COVID-19 患者試驗）而**停止收案**

> **結論**：Ivermectin 對 COVID-19 住院病人（含重症）**明確無效**。適應性平台設計即便樣本小仍提供清晰的 Bayesian 陰性結論。

---

<!-- _class: divider -->
# Honorable Mentions

---

# 其他值得關注

| 主題 | 期刊 | 重點 |
|------|------|------|
| **急性白血病 ICU** IPD Meta-analysis (n=2,003，55 ICUs) | ICM | 機械通氣 OR 6.46；存活率隨年份改善 (OR 0.93/yr) |
| **DNC 前昏迷動作特徵** 前瞻性研究 | Crit Care | 脊髓介導動作 vs 不明神經起源動作的盛行率與影像特徵 |
| **ICU 倖存者社經後果** 韓國全國資料庫 | CCM | ICU 出院後收入下降、失業率升高 — Post-ICU Syndrome 的非醫療面向 |
| **PRoVENT-PED** 全球兒童機械通氣（83 ICU，34 國，n=1,427）| Lancet Respir Med | PARDS 死亡率 27% vs 非 PARDS 12%；PEEP、ΔP、FiO₂ 是唯一可調節預後因子 |

---

# 本期觀察

1. **女性肺保護**是本期最大議題：PBW 本身有偏差 → 轉向 DP-guided 個人化通氣
2. **Etomidate 恐懼症**需要重新審視：NMA 顯示 Ketamine 的血流動力學代價並不比 etomidate 的腎上腺抑制更安全
3. **液體管理革命**：ROSE + 表型引導去液化 — 兩篇 Ann Intensive Care 是病房教學的核心閱讀
4. **REMAP-CAP 完整關閉 Ivermectin 問題**：Bayesian 平台設計效率極高，即便樣本小也能得到清晰結論
5. **ECMO 腎臟共識 (ADQI/ELSO)**：ECMO + CRRT 患者的抗生素劑量不能沿用常規，這是臨床上容易忽略的藥動學陷阱

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
2026-05-15 | Critical Care Biweekly Review

---

<!-- _class: ref -->
# 參考文獻 (1/2)

1. von Wedel D, et al. PBW equation overestimates lung sizes of female critically ill patients. [*Intensive Care Med* 2026.](https://doi.org/10.1007/s00134-026-08442-1) PMID 42096093
2. Zampieri FG, et al. Induction agents for emergency intubation: NMA. [*Crit Care* 2026.](https://doi.org/10.1186/s13054-026-06067-w) PMID 42121165
3. Russotto V, Casey JD, Myatra SN, et al. Airway management in critically ill patients with obesity. [*Intensive Care Med* 2026.](https://doi.org/10.1007/s00134-026-08454-x) PMID 42126552
4. Benítez-Cano A, et al. ELF penetration TOL/TAZ vs CAZ/AVI: randomized PK trial. [*Crit Care* 2026.](https://doi.org/10.1186/s13054-026-06075-w) PMID 42129898
5. EBV reactivation and immunoparalysis in sepsis. [*Crit Care* 2026.](https://doi.org/10.1186/s13054-026-05966-2) PMID 42098862
6. ARDS Global definition epidemiology and SpO₂:FiO₂ validity. [*Crit Care* 2026.](https://doi.org/10.1186/s13054-026-06043-4) PMID 42104520
7. Citrate anticoagulation CRRT Delphi consensus. [*Crit Care* 2026.](https://doi.org/10.1186/s13054-026-06066-x) PMID 42129846
8. Gist KM, et al. ADQI/ELSO consensus: ECMO, AKI, fluid, CRRT. [*Intensive Care Med* 2026.](https://doi.org/10.1007/s00134-026-08440-3) PMID 42113209

---

<!-- _class: ref -->
# 參考文獻 (2/2)

9. Bircher RE, et al. How to perform fluid de-escalation in critical care. [*Ann Intensive Care* 2026;16:100075.](https://doi.org/10.1016/j.aicoj.2026.100075) PMID 42111229
10. Vanden Eede M, Van Regenmortel N. Five classic fluid pitfalls. [*Ann Intensive Care* 2026;16:100074.](https://doi.org/10.1016/j.aicoj.2026.100074) PMID 42125087
11. Nehme Z, et al. MPA defibrillation RCT in shockable OHCA. [*Resuscitation* 2026;224:111121.](https://doi.org/10.1016/j.resuscitation.2026.111121) PMID 42092447
12. Hashmi M, et al. REMAP-CAP: Ivermectin for COVID-19. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007134) PMID 42101205
13. Chean D, et al. Acute leukemia ICU mortality IPD meta-analysis. [*Intensive Care Med* 2026.](https://doi.org/10.1007/s00134-026-08449-8) PMID 42081104
14. DNC comatose movements cohort study. [*Crit Care* 2026.](https://doi.org/10.1186/s13054-026-06037-2) PMID 42135815
15. Household income decline after critical illness. [*Crit Care Med* 2026.](https://doi.org/10.1097/CCM.0000000000007152) PMID 42089734
16. van Vliet R, et al. PRoVENT-PED: paediatric MV epidemiology. [*Lancet Respir Med* 2026.](https://doi.org/10.1016/S2213-2600(26)00044-5) PMID 42081907
