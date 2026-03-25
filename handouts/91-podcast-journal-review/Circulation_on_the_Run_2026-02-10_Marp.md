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
footer: '謝慕揚 MD, PhD, FESC | Circulation on the Run Feb 10, 2026 | 2026'
---

<!-- _class: lead -->

# Circulation on the Run
## February 10, 2026 期刊回顧

**謝慕揚 MD, PhD, FESC**
資料來源：*Circulation*. 2026;153(6) | 2026-03-02
[原文連結 Original Article](https://www.ahajournals.org/do/10.1161/podcast.20260209.180892/full/)

---

# 大綱

1. **Fontan 手術長期預後** — PCCC 登錄研究
2. **HELZ2 Helicase** — ApoB / 脂質代謝新靶點
3. **APOL1 風險變異** — 高血壓的精準醫療
4. **其他文章** — BTK, MOD RNA FOXM1, Obstructive Shock, Lp(a)
5. **專題：Stressor-Associated AF** — VITAL-AF 試驗

---

<!-- _class: divider -->

# Fontan 手術長期預後

---

# Fontan — 研究設計

- **資料來源**：Pediatric Cardiac Care Consortium (PCCC)
- **收案期間**：1982-2011 年
- **患者數**：**1,175 位** (男性 62.6%, systemic LV 53.3%)
- **追蹤中位數**：**20.6 年** (IQR 18.2-24.4)
- **主要事件**：85 例死亡 + 49 例心臟移植

> 目標：探討 pre-Fontan hemodynamics 是否預測**長期**死亡/移植風險

---

# Fontan — 主要結果

| 預測因子 | 結果 |
|----------|------|
| **Pre-Fontan mean PAP** (最強預測因子) | 連續性關聯，無明確 cut-off |
| 低 mean PAP tertile → 25yr 存活 | **83.7%** (95% CI 77.6-88.3) |
| 高 mean PAP tertile → 25yr 存活 | **73.7%** (95% CI 65.5-80.3), P=0.02 |
| **Systemic RV** vs. LV | aHR **2.39** (95% CI 1.65-3.46) |
| **Fontan >4 歲** vs. 2-4 歲 | aHR **1.80** (95% CI 1.25-2.60) |

---

# Fontan — 臨床啟示

> **Pearl 1**: Pre-Fontan mean PAP 為連續性風險，沒有「安全」閾值

> **Pearl 2**: Systemic RV 患者長期預後差 (HR 2.39)，需更積極追蹤

> **Pearl 3**: 研究支持 **4 歲前完成 Fontan**，延遲手術增加長期風險

---

<!-- _class: divider -->

# HELZ2 Helicase 與脂質代謝

---

# HELZ2 — 發現與機轉

- **來源**：UT Southwestern，forward genetic screen in mutagenized mice
- **HELZ2**：Helicase with zinc finger 2
- **功能**：結合 ApoB mRNA → 透過 helicase activity 降解

| 發現 | 說明 |
|------|------|
| Colby 突變 (L1833P) | **Gain-of-function** mutation |
| ApoB mRNA | 降解增強 → ApoB 蛋白減少 |
| 肝臟脂質 | 堆積增加（不影響體重） |
| Atheroprotection | 在 ApoE-/- 及 LdlR-/- 小鼠中證實 |

---

# HELZ2 — 臨床潛力

```text
HELZ2 活性增強
    |
    ├── ↑ ApoB mRNA 降解
    |       └── ↓ Atherogenic lipoproteins → Atheroprotection
    |
    └── ↑ 肝臟脂質堆積 → 需注意 MASLD 風險
```

> **Pearl**: HELZ2 藥理學調控可能為 **statin-intolerant** 患者提供替代策略，同時也是 MASLD 的潛在治療靶點

---

<!-- _class: divider -->

# APOL1 風險變異與高血壓

---

# APOL1 — 研究背景

- **>40% 非裔美國人**攜帶 APOL1 risk variants (G1/G2)
- APOL1 RV 與慢性腎臟病已知相關
- 來自 **UPenn** 的 cell-specific inducible transgenic 小鼠研究
- 在人類腎臟中，APOL1 高度表現於 **podocytes** 及 **endothelial cells**

---

# APOL1 — 機轉與結果

| 模型 | 結果 |
|------|------|
| Podocyte G2 APOL1 | **嚴重次發性高血壓**（先蛋白尿再腎病變） |
| Podocyte G0 (參考型) | 無高血壓 |
| Endothelium G2 | 老化後輕度高血壓；高鹽加劇 |

**機轉路徑**：
G2 APOL1 → **STING 活化** → **Endothelin-1** 產生 → 高血壓

**保護策略**：
- STING knockout → 保護
- Endothelin inhibitor → 保護

---

# APOL1 — 臨床意義

> **Pearl 1**: APOL1 G2 RV → STING → endothelin-1 路徑解釋了非裔族群高血壓的部分機轉

> **Pearl 2**: STING 抑制劑或 **endothelin receptor antagonists** 可能提供 precision therapeutics

---

<!-- _class: divider -->

# 其他重要文章

---

# BTK 在心血管疾病的角色

- **BTK (Bruton Tyrosine Kinase)**：Tec-family kinase
- 表現於 **platelets, macrophages, neutrophils**
- 參與 **platelet activation** 及血栓形成

| 世代 | 藥物 | 心血管毒性 |
|------|------|------------|
| 第一代 | Ibrutinib | AF, HTN, bleeding 較多 |
| 第二代 | Acalabrutinib, Zanubrutinib | 心律不整較少 |

- 本文為 New Drugs and Devices 綜述
- 探討 BTK 治療在心血管疾病的潛力

---

# 其他短文摘要

### Cardiomyocyte MOD RNA FOXM1
- Cardiomyocyte-specific **modRNA** 誘導 **FoxM1** overexpression
- 促進 cardiomyocyte proliferation → MI 後心臟修復
- 小鼠及豬模型均有效

### Obstructive Shock 罕見案例
- 來自 University of Utah 的 clinical vignette
- Sarcoma 相關 obstructive shock

### Lp(a) 與中風亞型 (Letter)
- Lp(a) 與 **large-artery atherosclerotic stroke** 因果關聯較強
- 其他 ischemic stroke subtypes 證據仍不一致

---

<!-- _class: divider -->

# 專題：Stressor-Associated AF
## VITAL-AF 試驗

---

# VITAL-AF — 研究設計

| 項目 | 內容 |
|------|------|
| **設計** | Pragmatic, cluster-randomized AF screening trial |
| **時間** | 2018-2019 |
| **地點** | 16 個 MGH 基層醫療診所 |
| **族群** | **30,265 位** >= 65 歲患者 |
| **新發 AF** | 約 1,000 例 |
| **Stressor-associated** | **約 30%** |

- **Stressor-associated AF**：在可逆性生理壓力因子下新診斷的 AF
- 例如：手術後、急性疾病、感染、代謝異常

---

# 發現一：風險因子譜驚人相似

| 風險因子 | Stressor-Associated AF | Primary AF |
|----------|:----------------------:|:----------:|
| 年齡 | 相似 | 相似 |
| 高血壓 | 相似 | 相似 |
| 心衰竭 | 相似 | 相似 |
| 糖尿病 | 相似 | 相似 |

> **Pearl**: 兩者共享相同的 **proarrhythmic substrate**
> Stressor 只是「觸發因子」，患者本身已具備 AF 的體質基礎

---

# 發現二：Stressor-Associated AF 並非良性

- **>20%** 的 stressor-associated AF 患者達到複合終點
- 相較**無 AF** 的風險：約 **5 倍**
- 與 **primary AF** 的風險：**相當**

> **Pearl**: 臨床上常視 stressor-associated AF 為「暫時性、良性」，但本研究清楚顯示其長期風險與 primary AF 相當！

---

# 發現三：治療嚴重不足

- Stressor-associated AF 接受 OAC 的比率比 primary AF **低 25%**
- 即使 **CHA2DS2-VASc >= 4** 仍較少處方 OAC

> **Pearl**: 這可能反映臨床醫師認為此類 AF 為「暫時性」而不需長期抗凝的偏見，但數據顯示這是**危險的假設**

---

# Stressor-Associated AF — 臨床建議

1. **重新審視分類**：不應自動視為良性或暫時性
2. **風險評估**：以相同標準 (CHA2DS2-VASc) 評估所有新診斷 AF
3. **抗凝治療**：高風險患者無論觸發因素，均應考慮 **OAC**
4. **長期追蹤**：與 primary AF 相同強度的追蹤

---

# 進行中的相關試驗

| 試驗 | 研究問題 |
|------|----------|
| **PACES** | 心臟手術後新發 AF 的抗凝治療 |
| **LeAAPS** | 心臟手術中預防性 LAA exclusion |
| **ASPIRE-AF** | 非心臟手術後 perioperative AF 的 NOAC vs usual care |

> 這三項試驗將進一步釐清 stressor-associated AF 的最佳治療策略

---

# 本期重點回顧

| 主題 | 核心訊息 |
|------|----------|
| **Fontan** | Pre-Fontan mean PAP 預測長期預後；支持 4 歲前手術 |
| **HELZ2** | 降解 ApoB mRNA → atheroprotection；statin 替代潛力 |
| **APOL1** | G2 RV → STING → endothelin-1 → 高血壓；precision Tx |
| **Stressor AF** | 非良性 (5x 風險)；OAC 處方不足；需同等重視 |

---

<!-- _class: small-text -->

# 參考文獻

1. Canter CE, et al. Pre-Fontan Hemodynamics & Long-Term Outcomes. [*Circulation*. 2026;153(6):382-395.](https://doi.org/10.1161/CIRCULATIONAHA.125.076880)
2. Jiang Y, Zhang Z. HELZ2 Regulates Apob mRNA Stability. [*Circulation*. 2026;153(6):415-434.](https://doi.org/10.1161/CIRCULATIONAHA.125.076468)
3. Li F, et al. APOL1 Risk Variant Expression & Hypertension. [*Circulation*. 2026;153(6):396-414.](https://doi.org/10.1161/CIRCULATIONAHA.124.071351)
4. von Hundelshausen P, et al. Btk in CV Disease. [*Circulation*. 2026;153(6):435-456.](https://doi.org/10.1161/CIRCULATIONAHA.125.076186)
5. Wu Y, et al. modRNA-Induced FoxM1 & MI Recovery. [*Circulation*. 2026;153(6):463-466.](https://doi.org/10.1161/CIRCULATIONAHA.125.075791)
6. Goodwin A, et al. A Rare Case of Obstructive Shock. [*Circulation*. 2026;153(6):457-462.](https://doi.org/10.1161/CIRCULATIONAHA.125.075924)
7. Haimovich JS, et al. Stressor-Associated AF: VITAL-AF. [*Circulation*. 2026;153(6):367-378.](https://doi.org/10.1161/CIRCULATIONAHA.125.076421)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
