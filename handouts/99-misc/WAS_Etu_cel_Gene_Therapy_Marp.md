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
    font-size: 28px;
    padding: 50px 60px;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 52px; border-bottom: none; }
  section.lead h2 { color: #9ec5ff; }
  section.lead h3 { color: #ffffff; font-weight: normal; }
  section.lead p { color: #f1f3f5; }
  section.lead strong { color: #ffe082; }
  section.lead a { color: #ffd166; text-decoration: underline; }
  section.lead blockquote {
    background-color: #fff5f5;
    border-left: 5px solid #ba181b;
    color: #1a2740;
  }
  section.lead blockquote p { color: #1a2740; }
  section.lead blockquote strong { color: #ba181b; }
  section.divider {
    background-color: #0072bc;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 { color: #ffffff; border-bottom: none; font-size: 60px; text-align: center; }
  section.divider h2 { color: #ffffff; font-size: 36px; text-align: center; }
  section.divider h3 { color: #ffe082; font-size: 30px; text-align: center; font-weight: normal; }
  section.divider p, section.divider strong { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 40px; }
  h2 { color: #0072bc; font-size: 32px; }
  h3 { color: #555555; font-size: 30px; }
  a { color: #0072bc; }
  table { font-size: 27px; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 12px; }
  td { padding: 5px 12px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.4em 1em;
    font-size: 28px;
  }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.6em; font-size: 25px; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 15px; }
  section.small-text { font-size: 17px; }
  section.small-text li { margin-bottom: 4px; }
footer: '謝慕揚 MD, PhD, FESC | WAS 基因治療 Etu-cel | NEJM 2026'
---

<!-- _class: lead -->
# Wiskott–Aldrich 症候群的基因治療
## Etuvetidigene Autotemcel (Etu-cel)
### N Engl J Med 2026;395:1193-205 · 27 位病人 · 最長追蹤 13.3 年

**謝慕揚 MD, PhD, FESC**

[原文連結：doi.org/10.1056/NEJMoa2515005](https://doi.org/10.1056/NEJMoa2515005)

> 單次輸注 → 存活 **96%**、嚴重感染 **2.00 → 0.15**／人年、**無插入性致癌**

---

# 一句話總結

無 HLA 相合親屬捐贈者的 WAS 病人，接受**自體慢病毒基因修正造血幹細胞** etu-cel：

| 指標 | 治療前 1 年 | 治療後 |
|---|---|---|
| 嚴重感染（次／人年） | **2.00** | **0.15**（>6–18 月） |
| 中重度出血（次／人年） | **2.00** | **0.80**（第 1 年） |
| 整體存活 | — | **96%**（1 年、5 年） |

最長 **13.3 年**：**無異常克隆增生、無插入性致癌**

---

<!-- _class: divider -->
# 背景
## Wiskott–Aldrich 症候群

---

# WAS 是什麼？

- **X 性聯**遺傳，*WAS* 基因變異 → **WASP** 蛋白缺乏
- 先天性免疫缺陷 + 血小板疾病
- 經典三聯徵：
  - **小血小板性血小板低下** → 出血
  - **濕疹**
  - **反覆嚴重感染**
- 另有自體免疫、自體發炎、惡性腫瘤 → **壽命縮短**

---

# 目前的治療選擇

| 策略 | 內容 | 問題 |
|---|---|---|
| 支持療法 | 血小板輸注、IVIG、抗生素預防 | 無法根治 |
| 免疫調節 | 類固醇、rituximab、anti–IL-1 | 治標 |
| **異體 HSCT** | 3–5 年存活 **~90%** | 捐贈者、GVHD、排斥 |

> **≥5 歲**或**非相合親屬捐贈者**：HSCT 併發症與死亡率仍高

---

# Etu-cel 是什麼？

```text
自體 CD34+ 造血幹／前驅細胞（骨髓或動員周邊血）
    |
體外以 SIN 慢病毒載體 (LV-w1.6WAS) 轉導人類 WAS cDNA
    |   啟動子：由內生性 WAS 基因座重建（生理性）
    |
Rituximab + 減量強度前處置 (busulfan + fludarabine)
    |
單次靜脈輸注（新鮮 17 人／冷凍 10 人）
```

---

<!-- _class: divider -->
# 研究設計
## 三個研究的整合分析

---

# 研究設計

| 來源 | 人數 | 設計 |
|---|---|---|
| TIGET-WAS | 8 | 第 1–2 期 |
| OTL-103-4 | 10 | 第 3 期 |
| 擴大使用計畫 | 10（治療 9） | 恩慈使用 |

- 28 人入組、**27 人接受治療**；2010/4 – 2025/1
- 開放標籤、**單組、無對照**
- 比較基準：**病人自身治療前 1 年**

---

# 主要終點與納入條件

## 主要療效終點
1. 整體存活
2. **嚴重感染率**：治療後 >6 至 18 個月
3. **中重度出血率**：治療後前 12 個月

## 納入條件
- 基因確診 + **無 HLA 相同親屬捐贈者**
- 嚴重變異、WASP 缺失、或 Zhu 分數 ≥3（擇一）

---

# 受試者特徵（N = 27）

| 特徵 | 數值 |
|---|---|
| 治療時中位年齡 | **2.6 歲**（1.0–35.1） |
| ≥5 歲 | 9 人（33%） |
| Class II 嚴重基因型 | 22 人（81%） |
| Zhu 分數 ≥3 | 26 人 |
| CD34+ 中位劑量 | 16.9 × 10⁶/kg |
| 藥品 VCN 中位數 | 2.3 copies/cell |
| 存活者中位追蹤 | **5.7 年**（2.3–13.3） |

---

<!-- _class: divider -->
# 主要結果

---

# 整體存活

- 1 年與 5 年整體存活：**96%（95% CI 76–99）**
- 唯一死亡：
  - 擴大使用計畫中一位**成人**
  - 治療後 **4.5 個月**
  - 原有**鐵沉積性腦病變**惡化
  - 判定**與 etu-cel 無關**

---

# 嚴重感染大幅下降

| 期間 | 次／人年（95% CI） |
|---|---|
| 治療前 1 年 | **2.00**（1.50–2.61） |
| 治療後 >6–18 個月 | **0.15**（0.04–0.39） |
| 治療後 >5 年 | **0.05**（0.01–0.16） |

- 最常見嚴重感染：**中心靜脈導管相關**
- 需治療的 **CMV 再活化**：>6 個月後不再出現

---

# 中重度出血下降

| 期間 | 次／人年（95% CI） |
|---|---|
| 治療前 1 年 | **2.00**（1.50–2.61） |
| 治療後第 1 年 | **0.80**（0.49–1.22） |
| 治療後 >5 年 | **0.02**（0.00–0.10） |

年化住院率：**2.85 → 0.46**（>6–12 月）→ **0.09**（>5 年）

---

# 回歸正常生活

治療 **3 年**後：

- 全數**不再需要保護性隔離**
- **>80%** 上學或上幼兒園
- 約**一半**參與運動

> 這是家屬最在意、也最能用來衛教的結果

---

<!-- _class: divider -->
# 次要終點
## 植入、免疫、血小板

---

# 植入與 WASP 表現

- 嗜中性球植入：中位 **23 天**
- **無植入失敗**、無人需回輸備份細胞
- **無人**事後接受異體 HSCT 或脾臟切除
- 多系列植入穩定至最後追蹤
- WASP 表現：**淋巴球 > 骨髓系**
  - 減量前處置 + WASP 陽性淋巴球的**選擇性優勢**

---

# 免疫重建

| 指標 | 結果 |
|---|---|
| T 細胞增生反應 | **1 年**達正常範圍 |
| IVIG 停用 | **26/26** 存活者，中位 320.5 天 |
| 長期抗生素停用 | 25 人（93%），中位 405 天 |
| 疫苗反應 | 多數有保護性抗體（**含活疫苗**） |

> IVIG 全停 + 活疫苗有效 = **B 細胞功能真正修復**

---

# 血小板：上升，但未完全正常

| 時間點 | 中位數（×10⁹/L） |
|---|---|
| 基線 | **18.0** |
| 第 1 年 | **59.0** |
| 第 5 年 | **68.3** |

- 血小板輸注停用：中位 **46.5 天**
- **96%** 最後追蹤時 **≥50 × 10⁹/L**
- 平均血小板體積：>90% 正常化

---

# 免疫失調：濕疹與自體免疫

| 面向 | 結果 |
|---|---|
| 濕疹（23 人） | 第 2 年 92% 無濕疹；**第 6 年起全無** |
| 原有自體免疫（10 人） | 除 1 人外**皆緩解** |
| 早期自體免疫血球低下 | 5 人（19%），皆緩解 |
| 晚期自體免疫 | 4 人（15%），短期或免治療 |

HSCT 後自體免疫也約 **14–20%**

---

<!-- _class: divider -->
# 安全性
## 最重要的問題：會不會致癌？

---

# 基因毒性：零訊號

- **無**異常克隆增生
- **無**複製型慢病毒（RCL）
- **無**抗 WASP 抗體
- 插入位點分析：**多克隆植入**
  - 無原致癌基因富集
  - Shannon 多樣性**未收縮**

---

# 不良事件

| 項目 | 數據 |
|---|---|
| 嚴重不良事件 | **57 件／19 人** |
| 發生時間 | **60%** 在前 6 個月 |
| 類型 | **54% 為感染**（導管感染最多） |
| ≥3 級 AE | 0–6 月 126 件 → >6 月–1 年 **7 件** |
| 惡性腫瘤 | **甲狀腺乳突癌 1 例**（近 5 年） |

---

# 為什麼這次沒有白血病？

| 產品 | 載體／啟動子 | 致癌 |
|---|---|---|
| 早期 WAS 基因治療 | γ-反轉錄病毒 + 強 LTR | **有** |
| Eli-cel（CALD） | 慢病毒 + 強啟動子 | **有** |
| **Etu-cel** | SIN 慢病毒 + **生理性啟動子** | **無** |

> **溫和的生理性啟動子**勝過強力病毒啟動子

---

# Etu-cel vs 異體 HSCT

| 面向 | 異體 HSCT | Etu-cel |
|---|---|---|
| 整體存活 | ~90% | **96%** |
| 捐贈者 | 需要 | **不需要** |
| GVHD／排斥 | 有 | **無** |
| 前處置 | 清髓 | 減量 + rituximab |
| 血小板 | 多數正常 | 上升但未全正常 |

---

# 研究限制

1. **單組、開放標籤、無同期對照**
2. 以自身前 1 年比較 → **迴歸均值**的可能
3. 95% CI **未作多重性校正**，僅描述性
4. 僅 27 人，**26 人在同一中心**
5. 甲狀腺癌 1 例的意義需更長追蹤

---

# 臨床 Pearls（1/2）

> **Pearl 1**：男嬰出血 + **小血小板** + 濕疹 + 反覆感染 → 想到 WAS

> **Pearl 2**：嚴重感染 **2.00 → 0.15** 次／人年，>5 年 **0.05**

> **Pearl 3**：IVIG 全停、活疫苗有效 = B 細胞真正修復

---

# 臨床 Pearls（2/2）

> **Pearl 4**：血小板升至 ~60–70 × 10⁹/L，**96% ≥50** → 解除活動限制

> **Pearl 5**：13.3 年**無插入性致癌**：載體與啟動子設計是關鍵

> **Pearl 6**：學術研發 → 藥廠 → 回授權 Telethon **非營利上市**

---

<!-- _class: small-text -->
# 參考文獻

1. Ferrua F, et al. Etuvetidigene autotemcel for the treatment of Wiskott–Aldrich syndrome. [*N Engl J Med*. 2026;395:1193-1205.](https://doi.org/10.1056/NEJMoa2515005) PMID 42777242
2. Candotti F. Clinical manifestations and pathophysiological mechanisms of the Wiskott-Aldrich syndrome. [*J Clin Immunol*. 2018;38:13-27.](https://doi.org/10.1007/s10875-017-0453-z)
3. Vallée TC, et al. How I treat Wiskott-Aldrich syndrome. [*Blood*. 2025;146:41-51.](https://doi.org/10.1182/blood.2024026288)
4. Vallée TC, et al. Wiskott-Aldrich syndrome: a study of 577 patients. [*Blood*. 2024;143:2504-16.](https://doi.org/10.1182/blood.2023021411)
5. Burroughs LM, et al. Excellent outcomes following HCT for WAS: a PIDTC report. [*Blood*. 2020;135:2094-105.](https://doi.org/10.1182/blood.2019002939)
6. Albert MH, et al. HSCT for WAS: an EBMT Inborn Errors Working Party analysis. [*Blood*. 2022;139:2066-79.](https://doi.org/10.1182/blood.2021014687)
7. Aiuti A, et al. Lentiviral HSC gene therapy in patients with WAS. [*Science*. 2013;341:1233151.](https://doi.org/10.1126/science.1233151)
8. Ferrua F, et al. Lentiviral HSPC gene therapy for WAS: interim phase 1/2 results. [*Lancet Haematol*. 2019;6:e239-53.](https://doi.org/10.1016/S2352-3026(19)30021-3)

---

<!-- _class: small-text -->
# 參考文獻（續）

9. Magnani A, et al. Long-term safety and efficacy of lentiviral HSPC gene therapy for WAS. [*Nat Med*. 2022;28:71-80.](https://doi.org/10.1038/s41591-021-01641-x)
10. Labrosse R, et al. Outcomes of HSC gene therapy for WAS. [*Blood*. 2023;142:1281-96.](https://doi.org/10.1182/blood.2022019117)
11. Calabria A, et al. Long-term lineage commitment in haematopoietic stem cell gene therapy. [*Nature*. 2024;636:162-71.](https://doi.org/10.1038/s41586-024-08250-x)
12. Braun CJ, et al. Gene therapy for WAS — long-term efficacy and genotoxicity. [*Sci Transl Med*. 2014;6:227ra33.](https://doi.org/10.1126/scitranslmed.3007280)
13. Duncan CN, et al. Hematologic cancer after gene therapy for cerebral adrenoleukodystrophy. [*N Engl J Med*. 2024;391:1287-301.](https://doi.org/10.1056/NEJMoa2405541)
14. Moratto D, et al. Long-term outcome in 194 patients with WAS treated by HCT 1980-2009. [*Blood*. 2011;118:1675-84.](https://doi.org/10.1182/blood-2010-11-319376)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

[原文：N Engl J Med 2026;395:1193-205](https://doi.org/10.1056/NEJMoa2515005)
