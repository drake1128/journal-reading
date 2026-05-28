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
  section.divider h2 { color: #ffe169; }
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
footer: '謝慕揚 MD, PhD, FESC | BioVAT-HF 幹細胞工程心肌 | 2026'
---

<!-- _class: lead -->
# BioVAT-HF
## 幹細胞衍生「生物性心室輔助組織」治療心衰竭
### Stem-Cell–Derived Biologic Ventricular Assist Tissue in Heart Failure
**謝慕揚 MD, PhD, FESC** | 讀書會共筆整理 | 2026-05-29
NEJM 2026;394:1991-2001
[原文連結 (DOI: 10.1056/NEJMoa2513525)](https://doi.org/10.1056/NEJMoa2513525)

---

# 一句話總結

- 對 **GDMT 無效、LVEF ≤ 35%** 的進展性心衰竭病人
- 將**異體 iPSC 衍生的工程心肌 (EHM) 組織**以外科縫貼於心外膜（**BioVAT 移植**）
- 3 個月期中分析：**標靶心壁厚度、LVEF、生活品質皆增加**
- 室性心律不整與移植**直接相關性低**，移植後無 VF
- 人類心肌「**再肌肉化 (remuscularization)**」的早期、開放性、**無對照組**臨床訊號

> 概念驗證成功，但仍是小型、無對照、短期的 phase 1–2 期中分析

---

<!-- _class: divider -->
# 背景與裝置
## 為什麼要再生心肌？BioVAT 是什麼？

---

# 背景：心肌流失無法修復

- 全球逾 **6,400 萬**人患心衰竭；約 5%/年進展為晚期，晚期死亡率可達 **50%/年**
- HFrEF 核心病理 = **心肌細胞流失**（每位病人約損失 **10 億**個心肌細胞）
- GDMT 與介入只能**延緩**惡化，無法**修復**失能心肌
- 心臟移植、機械循環輔助**無法規模化**滿足需求

> **細胞移植再肌肉化**直接針對病理根源；iPSC 與成熟分化技術讓「實體工程組織修補心臟」成為可能

---

# 什麼是 BioVAT？

| 項目 | 內容 |
|------|------|
| 細胞來源 | **異體 iPSC** 衍生心肌細胞 + 基質細胞 |
| 單一 EHM 單元 | 約 3,400 萬心肌細胞 + 600 萬基質細胞，膠原蛋白水膠，六角形 |
| 劑量 | 5 / 10 / 20 EHM 單元 = 0.05 / 0.10 / 0.24 單元/kg |
| 移植 | **左側小開胸**、off-pump，TachoSil 膜，Prolene 5-0 縫於心外膜 |
| 免疫抑制 | 術前 4–10 天開始（依 ISHLT 調整） |

> 加上會收縮的心肌 → 支持收縮與舒張；增厚心壁依 **Laplace 定律**降低室壁張力 → 促逆重塑

---

<!-- _class: divider -->
# 研究設計與結果

---

# 研究設計與族群

- **設計**：開放性、兩階段 (Part A 劑量探索 / Part B 概念驗證) phase 1–2；德國 2 中心
- **編號**：NCT04396899 | 資助：DZHK + Repairon
- **納入**：18–80 歲、症狀性 HFrEF、LVEF ≤ 35%、≥1 低/無動作 LV 自由壁節段、GDMT 無效
- **族群**：招募 26、治療 20（低 2 / 中 2 / 安全最大劑量 16）；療效分析 = 安全最大劑量 16 人，12 人完成 3 個月

| 基線 | 數值 |
|------|------|
| 年齡 / 男性 | 平均 59 歲 / 88% |
| LVEF | 25% ± 7 |
| 中位 NT-proBNP | 1,422 ng/L |

---

# 主要療效終點（3 個月，安全最大劑量 16 人）

| 主要終點 | 變化量 | 90% CI | P 值 |
|----------|--------|--------|------|
| **標靶心壁厚度** | **+4.5 mm** | 3.7–5.4 | **<0.001** |
| **LVEF** | **+3.9 個百分點** | 0.9–6.8 | **0.04** |
| **KCCQ-OSS** | **+6.7 分** | 1.0–12.5 | **0.06** |

> **統計重點**：顯著門檻為**雙側 α = 0.10**（非 0.05），Hochberg 程序判讀；三項皆 < 0.10 → 皆達標。KCCQ 在傳統 0.05 標準下並不顯著。

---

# 安全性

- **所有 20 人皆有不良事件**；196 件 AE、57 件嚴重 AE
- 最常見：腎/泌尿 (90%)、感染 (75%)、心臟 (70%)

| 死亡（3 例，皆判定與 BioVAT 無關） | 時間 |
|------|------|
| SIRS + 血管麻痺 | 術後第 6 天 |
| COVID-19 後心肺失代償 | 術後第 95 天 |
| A 型主動脈剝離 | 術後第 239 天 |

- VT：3 人/5 次，心外膜標測示**可能與移植無關**；移植後**無 VF**
- **免疫排斥訊號**：1 例停免疫抑制後出現高效價 DSA + LVEF 39%→28%

---

<!-- _class: divider -->
# 限制與臨床意義

---

# 限制與待解問題

- **無對照組** → 無法排除自然病程、GDMT 持續作用、安慰劑效應
- **n=20、追蹤短、替代終點**（心壁厚度/LVEF/KCCQ），無硬終點對照數據
- 顯著門檻 **α = 0.10**；KCCQ P=0.06 在 0.05 下不顯著
- 競爭事件（死亡、移植）使部分病人被移出分析 → 可能偏差
- 待釐清：長期免疫安全性、療效預測因子（如纖維化負荷）

---

# Take-home Message

> **概念驗證成功**：實體工程心肌可外科貼附、可能貢獻收縮，心壁增厚 / LVEF / 生活品質改善，且無移植直接相關之致命心律不整。

> **但**：小型、無對照、短期 phase 1–2 期中分析，**目前不改變臨床實務**，用於設計後續 phase 3。

- 對結構/介入心臟科：再生醫學與「裝置」交會的新領域，未來可能與 LVAD、心臟移植競合於晚期 HFrEF 治療階梯。

---

<!-- _class: small-text -->
# 參考文獻

1. Zimmermann W-H, et al. Stem-Cell–Derived Biologic Ventricular Assist Tissue in Heart Failure (BioVAT-HF). [*N Engl J Med*. 2026;394(20):1991-2001.](https://doi.org/10.1056/NEJMoa2513525)
2. Jebran A-F, et al. Engineered heart muscle allografts for heart repair in primates and humans. [*Nature*. 2025;639:503-511.](https://doi.org/10.1038/s41586-024-08463-0)
3. Tiburcy M, et al. Defined engineered human myocardium with advanced maturation. [*Circulation*. 2017;135:1832-1847.](https://doi.org/10.1161/CIRCULATIONAHA.116.024145)
4. Kirkeby A, et al. Pluripotent stem-cell-derived therapies in clinical trial: a 2025 update. [*Cell Stem Cell*. 2025;32:10-37.](https://doi.org/10.1016/j.stem.2024.12.001)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC**
讀書會共筆整理 · 僅供醫療專業人員教學參考
