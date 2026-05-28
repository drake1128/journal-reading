---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: 'Microsoft JhengHei', 'PingFang TC', sans-serif; background-color: #ffffff; color: #2d3436; }
  section.lead { background-color: #1a2740; color: #ffffff; }
  section.lead h1 { color: #ffffff; font-size: 2.0em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #b0c4de; }
  section.divider { background-color: #0072bc; color: white; display: flex; justify-content: center; align-items: center; }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.5em; text-align: center; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.65em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote { border-left: 4px solid #ba181b; background-color: #fff5f5; padding: 0.5em 1em; font-size: 0.85em; }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.68em; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.8em; }
footer: '謝慕揚 MD, PhD, FESC | TBP Targeted Sequencing | 2026'
---

<!-- _class: lead -->
# Targeted Sequencing of Pleural Fluid
## 結核性肋膜炎 (TBP) 的非侵入性高敏分子診斷

**謝慕揚 MD, PhD, FESC** | 2026-04-09

[NEJM Evidence 2026;5(4) — DOI 10.1056/EVIDoa2500237](https://doi.org/10.1056/EVIDoa2500237)

---

# TBP 診斷的瓶頸

| 工具 | 敏感度 | 限制 |
|------|-------|------|
| Pleural fluid MTB **culture** | <50% | 4–8 週 |
| Pleural fluid **PCR** (Xpert Ultra) | 40–80% | Culture 陰性更差 |
| Pleural fluid **ADA** | 中等 | 間接 marker |
| **Pleural biopsy** | 較高 | Invasive |
| Metagenomic NGS | 受限 | NTM DNA 干擾 |

> TBP 為 **paucibacillary** → 傳統工具皆有瓶頸，常需 invasive biopsy

---

# 研究設計

| 項目 | 內容 |
|------|------|
| 設計 | Prospective cohort |
| 地點 | Prince of Wales Hospital, Hong Kong |
| 期間 | 2022/09 – 2024/03 |
| 篩檢 → 分析 | 1277 → **329 人** |
| TBP / Non-TBP | 34 / 295 |
| 樣本 | 配對 pleural fluid + plasma |
| 註冊 | NCT05397730 |

**主要終點**：Targeted MTB sequencing 對 culture 的診斷敏感度比較

---

# 核心方法 — Masked Genome Alignment

- **Capture-probe (Roche)** 富集整個 MTB 基因組 cell-free DNA
- 比對「**masked** MTB 參考基因組」：將與 NTM 相似序列遮蔽
- 對照 1075 種 Actinobacteria 基因組
- 計量 = MTB DNA reads per 10 million (**RP10M**)

> **為什麼要 mask？**
> NTM 與 MTB 基因組部分高度相似 → 一般 mNGS 易誤判
> 遮蔽相似區域後，**訊號雜訊比大幅提升**，可使用極低 cutoff (2 RP10M)

---

# 主要結果 — 診斷效能

| 工具 | Sensitivity | Specificity | AUROC |
|------|-------------|-------------|-------|
| **Targeted sequencing** | **97.1%** (84.7–99.9) | **99.7%** (98.1–100) | **0.9996** |
| MTB culture | 47.1% (29.8–64.9) | 100% | NA |
| MTB PCR (Xpert Ultra) | 26.5% (12.9–44.4) | 100% | NA |
| ADA (>40 U/L) | 61.8% | 92.9% | 0.8869 |

> **Sequencing 97.1% vs Culture 47.1% (P<0.001)**
> 相當於把 TBP 偵測率從 ~一半提升到 ~全部

---

# Culture-Negative TBP 的價值

| 子群 | Targeted sequencing | PCR (Xpert Ultra) |
|------|--------------------|--------------------|
| Culture **陽性** TBP (n=16) | **93.8%** (15/16) | 37.5% |
| Culture **陰性** TBP (n=18) | **100% (18/18)** | **16.7%** |

> 這正是臨床最棘手的族群 — 既往要靠 biopsy 才能確診的病人，
> 現在 sequencing 全部抓得到。

---

# Plasma Sequencing — Liquid Biopsy 潛力

- TBP 31 例血漿 → **28 例 (90%) 偵測到 MTB DNA**
- AUC **0.9475** (0.8929–1.0000)
- 同樣 28 例血漿 PCR (Xpert Ultra) 全部 **0% 陽性**
- 開啟未來 **blood-based TB diagnostic test** 的可能性

---

# 其他發現

### 抗藥突變分析
- 16 例樣本（含 8 例 culture 陰性）分析 WHO group 1 抗藥區
- 結果與表現型藥敏一致 → **non-invasive 藥敏分型潛力**

### Cell-free DNA fragmentomics
- 不同肋膜病因 (TBP / parapneumonic / malignant / fluid overload) 有不同的 **end motif profile**
- 未來可發展 pleural fluid「液體切片」區分病因

---

<!-- _class: divider -->
# Take Home Messages

---

# 臨床重點

> **Pearl 1**：Masked-genome targeted sequencing 對 TBP **敏感度 97.1%、特異度 99.7%**。

> **Pearl 2**：對 **culture 陰性 TBP** 敏感度 **100%**，遠超 PCR (16.7%)。

> **Pearl 3**：Turnaround ~**1 週**，遠快於培養 4–8 週。

> **Pearl 4**：可望**減少 invasive pleural biopsy** 的需求。

> **Pearl 5**：Plasma sequencing AUC 0.9475 → blood-based TB diagnostics 的雛形。

> **Pearl 6**：對非典型 TBP（淋巴球低、ADA 不高）特別有價值。

---

# 限制與未來方向

- 單中心、TBP n=34 樣本小 → 效能可能高估
- Capture sequencing + bioinformatics **資源/技術門檻高**
- 需要獨立大型世代驗證
- 可延伸至 tuberculous **meningitis** 與 **peritonitis** 等 paucibacillary 肺外結核

### 對台灣 ICU/胸腔
- Lymphocytic exudate + culture/Xpert 陰性 → 未來非侵入性確診工具
- 仍需等待大型驗證

---

<!-- _class: small-text -->
# 參考文獻

1. Lam WKJ, Chan KKP, Wang G, et al. **Sequencing of Pleural Fluid and Plasma for Tuberculous Pleuritis.** [*NEJM Evid*. 2026;5(4).](https://doi.org/10.1056/EVIDoa2500237)
2. Chan KKP, Lee YCG. Tuberculous pleuritis: clinical presentations and diagnostic challenges. [*Curr Opin Pulm Med*. 2024;30:210-216.](https://doi.org/10.1097/MCP.0000000000001052)
3. Aggarwal AN, et al. ADA for diagnosis of tuberculous pleural effusion: a systematic review and meta-analysis. [*PLoS One*. 2019;14:e0213728.](https://doi.org/10.1371/journal.pone.0213728)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
