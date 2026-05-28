# Targeted Sequencing of Pleural Fluid 在 Tuberculous Pleuritis 的診斷應用

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-04-09**
**原文連結：[NEJM Evidence — Sequencing of Pleural Fluid and Plasma for Tuberculous Pleuritis](https://doi.org/10.1056/EVIDoa2500237)**

---

## 目錄
1. [研究背景](#1-研究背景)
2. [TBP 診斷的瓶頸](#2-tbp-診斷的瓶頸)
3. [研究設計](#3-研究設計)
4. [核心方法 — Masked Genome Alignment](#4-核心方法--masked-genome-alignment)
5. [病人特徵](#5-病人特徵)
6. [診斷效能結果](#6-診斷效能結果)
7. [Plasma 分析與其他發現](#7-plasma-分析與其他發現)
8. [臨床意涵與限制](#8-臨床意涵與限制)
9. [參考文獻](#參考文獻)

---

## 1. 研究背景

- 結核病 (TB) 是 **2023 年全球感染症死因第一**
- **Tuberculous pleuritis (TBP, 結核性肋膜炎)** 為常見肺外結核
- 肋膜腔內 *M. tuberculosis* (MTB) 為 **paucibacillary**（菌量極低）
- 傳統診斷工具皆有明顯瓶頸 → 常需 invasive pleural biopsy
- 此瓶頸延誤抗結核治療啟動，影響全球 TB 控制

---

## 2. TBP 診斷的瓶頸

| 工具 | 敏感度 | 限制 |
|------|-------|------|
| Pleural fluid MTB **culture** | <50% | 4–8 週 turnaround |
| Pleural fluid MTB **PCR (Xpert MTB/RIF Ultra)** | 40–80% | 培養陰性病例敏感度差 |
| Pleural fluid **ADA** | 中等 | 為間接 marker，非直接證實 MTB |
| **Pleural biopsy** | 較高 | Invasive |
| Metagenomic NGS | 受限 | NTM (nontuberculous mycobacteria) DNA 干擾 |

---

## 3. 研究設計

| 項目 | 內容 |
|------|------|
| 設計 | Prospective cohort study |
| 地點 | Prince of Wales Hospital, Hong Kong SAR |
| 收案期間 | 2022/09 – 2024/03 |
| 對象 | ≥18 歲、新發 unilateral pleural effusion 需 thoracentesis |
| 排除 | 既往 TBP / 細菌性 pleural infection、同側 instrumentation、3 個月內抗結核 >14 天 |
| 樣本 | 配對 pleural fluid + plasma |
| 註冊 | NCT05397730 (MYDNITE study) |

### 主要結果
**Targeted MTB sequencing** vs **MTB culture** 的診斷敏感度比較（McNemar's test）

---

## 4. 核心方法 — Masked Genome Alignment

### Targeted MTB sequencing
- 使用 **客製化 capture probe (Roche)** 富集整個 MTB 基因組 cell-free DNA
- 比對「**masked** MTB 參考基因組」：將與 NTM 序列高度相似的區域**遮蔽**
- 比對到 1075 種 Actinobacteria 基因組以識別非特異區域
- 計算 MTB DNA fragments per 10 million reads (**RP10M**)

### 為什麼要 mask？
- NTM 與 MTB 部分基因組序列相似 → metagenomic NGS 容易誤判
- 遮蔽相似區域後，剩下的訊號才是「真 MTB DNA」
- 可允許設定**極低 cutoff (2 RP10M)** 維持高特異度

---

## 5. 病人特徵

- 篩檢 1277 人，符合條件 403 人 → 最終分析 **329 人**
- TBP **34 人 (10.3%)**；non-TBP 295 人
- TBP 中 16 人 (47%) culture 陽性

| 項目 | TBP (n=34) | Non-TBP (n=295) |
|------|-----------|-----------------|
| Age (median) | 69.5 | 70.0 |
| Male | 67.6% | 59.7% |
| Previous pulmonary TB | 17.6% | 5.1% |
| Pleural fluid lymphocytes (%) | 84.0 | 45.0 |
| Pleural fluid TP (g/L) | 48.0 | 37.0 |
| Pleural fluid LDH (U/L) | 269.5 | 215.0 |
| **Pleural fluid ADA (U/L)** | **45.0** | **8.8** |

Non-TBP 主要為：malignant pleural effusion (134)、fluid overload (93)、parapneumonic effusion (55)。

---

## 6. 診斷效能結果

### 主要終點 — Pleural Fluid Targeted Sequencing vs Culture

| 工具 | Sensitivity | Specificity | PPV | NPV | AUROC |
|------|-------------|-------------|-----|-----|-------|
| **Targeted sequencing** (cutoff 2 RP10M) | **97.1%** (84.7–99.9) | **99.7%** (98.1–100) | 97.1% | 99.7% | **0.9996** |
| Pleural fluid MTB culture | 47.1% (29.8–64.9) | 100% | 100% | 94.2% | NA |
| Pleural fluid MTB PCR (Xpert Ultra) | 26.5% (12.9–44.4) | 100% | 100% | 92.2% | NA |
| Pleural fluid ADA (cutoff 40 U/L) | 61.8% | 92.9% | 50.0% | 95.5% | 0.8869 |

> **Targeted sequencing 敏感度 97.1% vs Culture 47.1%（P<0.001），AUC 0.9996**

### 次族群表現
- **Culture 陽性 TBP**：sensitivity 93.8% (15/16)
- **Culture 陰性 TBP**：sensitivity **100% (18/18)** — 比 PCR (16.7%) 顯著更佳
- 33/34 TBP 中 MTB DNA 中位 267.6 RP10M (IQR 30.8–2644.3)
- Non-TBP 中 288/295 (97.6%) 完全偵測不到 MTB DNA；7 例為極低訊號 (<5 RP10M)

### 1 例特殊案例
- 1 名「false positive」病人後來 22 個月後 effusion 復發、ADA 升高，臨床高度懷疑 TBP，但拒絕 biopsy → 可能是真陽性提早被偵測

---

## 7. Plasma 分析與其他發現

### Plasma targeted sequencing
- TBP 31 例配對血漿中，**28 例 (90%) 偵測到 MTB DNA**
- AUC **0.9475** (0.8929–1.0000)
- 同樣 28 例血漿用 PCR (Xpert Ultra) **0% 陽性** → sequencing 大幅勝出
- 開啟未來 **blood-based TB diagnostic test** 可能性

### 抗藥突變分析
- 對 16 例 TBP 樣本（含 8 例 culture 陰性）分析 WHO 「group 1」抗藥相關突變區域
- 未偵測到抗藥突變，與表現型藥敏一致

### Cell-free DNA fragmentomics
- Pleural fluid cfDNA 在 TBP、parapneumonic effusion、malignant effusion、fluid overload 之間有不同的 **end motif profile** → 未來可發展液體切片區分肋膜病因

---

## 8. 臨床意涵與限制

### 重點摘要
> **Pearl 1**：對 paucibacillary 的 TBP，**masked genome targeted sequencing 敏感度 97.1%、特異度 99.7%**，遠優於 culture 與 PCR。
>
> **Pearl 2**：對 **culture 陰性 TBP**（最棘手的族群）敏感度 100%。
>
> **Pearl 3**：Turnaround **約 1 週**，遠快於培養 4–8 週，可加速啟動治療。
>
> **Pearl 4**：可能**減少對 invasive pleural biopsy 的需求**。
>
> **Pearl 5**：Plasma sequencing AUC 0.9475，提示未來可能發展 blood-based TB 診斷。
>
> **Pearl 6**：對非典型 TBP（淋巴球比例低、ADA 不高）特別有價值。

### 限制
- 單中心 (Hong Kong)，TBP n=34 樣本量小，diagnostic performance 可能高估
- 需要 capture-based sequencing + bioinformatics，**資源與技術門檻高**
- 需要在獨立、更大世代驗證
- 未測試於 tuberculous meningitis、peritonitis 等其他 paucibacillary 肺外結核（作者建議擴展）

### 對台灣 ICU 與胸腔的啟示
- 對 lymphocytic exudative pleural effusion 但 culture/Xpert 陰性病例，未來可能成為**非侵入性確診工具**
- 對抗 MDR-TB 也提供 non-invasive 抗藥分型潛力
- 仍需等待大型驗證後才能進入常規檢查清單

---

## 參考文獻

1. Lam WKJ, Chan KKP, Wang G, et al. Sequencing of Pleural Fluid and Plasma for Tuberculous Pleuritis. [*NEJM Evid*. 2026;5(4).](https://doi.org/10.1056/EVIDoa2500237)
2. Chan KKP, Lee YCG. Tuberculous pleuritis: clinical presentations and diagnostic challenges. [*Curr Opin Pulm Med*. 2024;30:210-216.](https://doi.org/10.1097/MCP.0000000000001052)
3. Shaw JA, Koegelenberg CFN. Pleural tuberculosis. [*Clin Chest Med*. 2021;42:649-666.](https://doi.org/10.1016/j.ccm.2021.08.002)
4. Aggarwal AN, Agarwal R, Sehgal IS, Dhooria S. Adenosine deaminase for diagnosis of tuberculous pleural effusion: a systematic review and meta-analysis. [*PLoS One*. 2019;14:e0213728.](https://doi.org/10.1371/journal.pone.0213728)
