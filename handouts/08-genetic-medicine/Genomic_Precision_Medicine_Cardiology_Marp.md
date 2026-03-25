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
footer: '謝慕揚 MD, PhD, FESC | Genomic Precision Medicine in Cardiology | 2026'
---

<!-- _class: lead -->

# Genomic Precision Medicine in Cardiology

## 基因精準醫學與心臟病

**謝慕揚 MD, PhD, FESC**
資料來源：EHRA/HRS/APHRS/LAHRS Expert Consensus 2022 及多篇文獻回顧 | 2026-03-11

---

# 大綱

1. 心臟基因醫學總論
2. 基因檢測方法與平台
3. Brugada Syndrome
4. Long QT Syndrome
5. Hypertrophic Cardiomyopathy (HCM)
6. Fabry Disease
7. ATTR Amyloidosis
8. 台灣健保給付現況
9. 臨床實務建議

---

<!-- _class: divider -->

# 第一部分：心臟基因醫學總論

---

# 為什麼心臟科醫師需要懂基因？

- 遺傳性心臟病盛行率約 **1/200–1/500**
- 35 歲以下心因性猝死 (SCD) 約 **25–35%** 與遺傳性心臟病相關
- 基因檢測可協助：
  - **確認診斷** — 如 LQTS 亞型分類
  - **風險分層** — 如 HCM sarcomere (+) vs. (-)
  - **指導治療** — 如 LQT3 使用 mexiletine
  - **家族篩檢** — Cascade screening 預防 SCD

> **Pearl**: 基因檢測不再只是研究工具，已成為臨床指引建議的標準評估

---

# 遺傳性心臟病分類

| 類別 | 疾病 | 主要基因 | 遺傳模式 |
|------|------|---------|---------|
| **離子通道病** | LQTS | *KCNQ1, KCNH2, SCN5A* | AD |
| | BrS | *SCN5A* | AD |
| | CPVT | *RYR2, CASQ2* | AD/AR |
| **心肌病變** | HCM | *MYBPC3, MYH7* | AD |
| | DCM | *TTN, LMNA* | AD |
| | ARVC | *PKP2, DSP* | AD |
| **代謝性** | Fabry | *GLA* | X-linked |
| **蛋白沉積** | ATTR | *TTR* | AD |

---

# 基因檢測建議等級 (2022 Consensus)

| 等級 | 適用情境 |
|------|---------|
| **Class I** | 臨床確診 LQTS、HCM、ARVC、Fabry 病人 |
| **Class I** | 已知致病變異之**一等親** cascade screening |
| **Class IIa** | 臨床疑似 BrS、DCM、CPVT |
| **Class IIa** | < 40 歲不明原因心臟驟停倖存者 |
| **Class IIb** | 不明原因猝死 molecular autopsy |
| **Class III** | 一般族群無症狀篩檢（**不建議**） |

---

<!-- _class: divider -->

# 第二部分：基因檢測方法

---

# 檢測技術比較

| 方法 | 優點 | 缺點 | 費用 (NTD) |
|------|------|------|-----------|
| **Sanger Sequencing** | Gold standard 準確度 | 一次一個基因 | ~5,000–10,000/gene |
| **NGS Gene Panel** | 高通量、快速 | 限 panel 內基因 | ~20,000–50,000 |
| **Whole Exome (WES)** | 涵蓋廣 | VUS 多、分析複雜 | ~50,000–80,000 |
| **Whole Genome (WGS)** | 最完整 | 成本最高 | ~80,000–150,000 |

> **Pearl**: 目前臨床首選為 **NGS gene panel** — 兼顧效率與成本

---

# ACMG 變異分類系統

| 分類 | 臨床處置 |
|------|---------|
| **Pathogenic** | 確認致病 → 調整治療、啟動家族篩檢 |
| **Likely Pathogenic** | 視同 pathogenic 處理 |
| **VUS** | ⚠️ **不可**用於臨床決策，需追蹤 |
| **Likely Benign** | 不需特別處置 |
| **Benign** | 排除該基因致病 |

> **Pearl**: 約 20–40% 結果為 VUS — 這是基因報告最常見的困擾，需謹慎向病人解釋

---

# 台灣基因檢測平台

- **台大醫院基因心臟疾病中心 (CGHD)**
  - 2016 年成立全台首間家族遺傳性心臟病基因門診
  - 2018 年建立全台唯一遺傳性心臟疾病 **NGS 檢測平台**
  - 至 2021 年已服務全國 **70+ 醫院、3,000+ 病人**

- **檢測範圍**：
  - 離子通道疾病（LQTS、BrS、CPVT）
  - 心肌病變（HCM、DCM、ARVC）
  - 家族性高血脂症、遺傳性主動脈瘤、肺高壓

- **SADS-TW Registry**：家族篩檢率從 < 10% → **~50%**

---

<!-- _class: divider -->

# 第三部分：Brugada Syndrome

---

# Brugada Syndrome 概述

- **盛行率**：全球 1/2,000–1/5,000；台灣約 **1/1,000**
- **好發**：男性 (80–90%)，30–50 歲
- **ECG 特徵**：V1–V3 coved-type ST elevation ≥ 2 mm
- **風險**：VF → 心因性猝死

### 誘發因子
- 發燒
- Sodium channel blockers
- 大量飲酒
- 迷走神經張力增加

---

# BrS 基因學

| 基因 | 蛋白 | 頻率 |
|------|------|------|
| ***SCN5A*** | Nav1.5 sodium channel | **20–25%** |
| *SCN10A* | Nav1.8 | ~5% |
| *CACNA1C* | Cav1.2 | ~2–3% |
| *CACNB2* | Cavβ2 | ~1–2% |

- **SCN5A** 是唯一被認定為 BrS **definitive gene**
- 約 **70–75%** BrS 基因檢測為**陰性**
- 近年 GWAS 顯示 BrS 可能為 **polygenic** 疾病

> **Pearl**: 基因檢測在 BrS 主要用於**家族篩檢**，診斷仍以 ECG 為基礎

---

<!-- _class: divider -->

# 第四部分：Long QT Syndrome

---

# LQTS 三大主要亞型

| 亞型 | 基因 | 頻率 | 觸發因子 | ECG 特徵 |
|------|------|------|---------|---------|
| **LQT1** | *KCNQ1* | **30–35%** | 運動（游泳） | Broad-based T wave |
| **LQT2** | *KCNH2* | **25–30%** | 情緒、聲響 | Low, notched T wave |
| **LQT3** | *SCN5A* | **5–10%** | 安靜/睡眠 | Late-onset peaked T |

- LQT1 + LQT2 + LQT3 合計佔 **~75%** LQTS
- 盛行率約 **1/2,000**

---

# LQTS 基因型導向治療

| 亞型 | 首選治療 | 特殊考量 |
|------|---------|---------|
| **LQT1** | **Beta-blocker** (nadolol) | 避免游泳、限制運動 |
| **LQT2** | **Beta-blocker** + 補 K⁺ | 目標 K⁺ > 4.0，避免聲響刺激 |
| **LQT3** | **Mexiletine** ± BB | BB 單獨效果差；考慮 ICD |
| 高風險 | **ICD** ± LCSD | 心臟停止倖存者 |

> **Pearl**: LQT3 避免單用 beta-blocker，優先用 mexiletine — 這是**基因型影響治療選擇**最成功的範例

---

<!-- _class: divider -->

# 第五部分：Hypertrophic Cardiomyopathy

---

# HCM 基因學

- 最常見遺傳性心臟病：盛行率 **1/200–1/500**
- 年輕運動員猝死最常見原因
- 約 **40–60%** 可檢出 sarcomere 致病變異

| 基因 | 蛋白 | 頻率 |
|------|------|------|
| ***MYBPC3*** | Myosin-binding protein C | **25–30%** |
| ***MYH7*** | β-myosin heavy chain | **15–25%** |
| *TNNT2* | Troponin T | ~5% |
| *TNNI3* | Troponin I | ~3–5% |

- **MYBPC3 + MYH7** 佔 sarcomere 突變的 **70–80%**

---

# Sarcomere (+) vs. (-) HCM

| 特徵 | Sarcomere (+) | Sarcomere (-) |
|------|--------------|--------------|
| 診斷年齡 | 較年輕 | 較年長 |
| 家族史 | 常見 | 較少 |
| LVH 型態 | 非對稱性中隔 | 較對稱，常合併 HTN |
| Fibrosis | 較多 | 較少 |
| **SCD 風險** | **較高** | 較低 |
| 進展至 HF | 較高 | 較低 |

> **Pearl**: Sarcomere-positive HCM 需更積極的風險評估與家族篩檢

---

# HCM Phenocopy 鑑別

| Phenocopy | 基因 | 鑑別線索 |
|-----------|------|---------|
| **Fabry Disease** | *GLA* | 低 α-Gal A，cornea verticillata |
| **ATTR Amyloidosis** | *TTR* | PYP scan 陽性，晚發型 |
| **Danon Disease** | *LAMP2* | 極度 LVH + WPW pattern |
| **PRKAG2** | *PRKAG2* | WPW + LVH |
| **Pompe Disease** | *GAA* | 嬰兒型嚴重 LVH |

> **Pearl**: 不明原因 LVH 務必排除 Fabry 和 ATTR — 兩者皆有**特異性治療**

---

# Mavacamten：HCM 治療新紀元

- **機轉**：Cardiac myosin ATPase allosteric inhibitor
- **FDA 核准**：2022 年用於 obstructive HCM (NYHA II–III)
- **關鍵試驗**：
  - EXPLORER-HCM (2020)：減少 LVOT gradient，改善症狀
  - VALOR-HCM (2022)：降低 septal reduction therapy 需求
- **Aficamten**：第二代 myosin inhibitor（SEQUOIA-HCM 進行中）
- **台灣**：Mavacamten 尚未取得 TFDA 核准（2026/3）

---

<!-- _class: divider -->

# 第六部分：Fabry Disease

---

# Fabry Disease 概述

- **遺傳**：**X-linked** — *GLA* 基因突變
- **病理**：α-Gal A 酵素缺乏 → Gb3 堆積
- **台灣特色**：新生兒篩檢發現 later-onset variant **IVS4+919G>A** 盛行率高達 ~1/1,250 男性

### 心臟表現
| 表現 | 特徵 |
|------|------|
| LVH | 同心圓肥厚 (concentric) |
| Fibrosis | CMR lateral wall LGE |
| 傳導異常 | Short PR, AV block |
| 心律不整 | AF, VT |

---

# Fabry Disease 診斷與治療

### 診斷
| 檢測 | 男性 | 女性 |
|------|------|------|
| α-Gal A 活性 | 低 → 可確診 | 可能正常 |
| Lyso-Gb3 | 升高 | 升高 |
| *GLA* 基因定序 | 確認突變 | **必須做** |

### 治療（台灣健保給付）
| 藥物 | 機轉 | 健保 |
|------|------|------|
| Agalsidase alfa/beta | ERT | ✅ 罕病給付 |
| Migalastat | Chaperone | ✅ 有條件 |
| ST-920 gene therapy | AAV | 臨床試驗中 |

---

<!-- _class: divider -->

# 第七部分：ATTR Amyloidosis

---

# ATTR 分類與診斷

- **ATTRv (variant)**：*TTR* 基因突變（> 150 種），autosomal dominant
- **ATTRwt (wild-type)**：無突變，老年性，> 65 歲男性

### 常見突變

| 突變 | 表型 | 分布 |
|------|------|------|
| **V30M** | 神經 ± 心臟 | 葡萄牙、日本 |
| **V122I** | 心臟為主 | 非裔美國人 3–4% |
| **T60A** | 心臟 + 神經 | 愛爾蘭 |

---

# ATTR-CM 診斷流程

```text
疑似 cardiac amyloidosis (LVH + HFpEF + red flags)
    |
Step 1: 排除 AL amyloidosis
    |-- Serum/urine immunofixation + free light chains
    |
Step 2: ⁹⁹ᵐTc-PYP bone scintigraphy
    |-- Grade 2-3 + 無 monoclonal protein → 確診 ATTR-CM
    |-- Grade 0-1 → endomyocardial biopsy
    |
Step 3: TTR 基因定序
    |-- 突變(+) → ATTRv → 家族篩檢
    |-- 突變(-) → ATTRwt
```

---

# ATTR 治療選擇

| 藥物 | 機轉 | 適應症 | 關鍵試驗 |
|------|------|--------|---------|
| **Tafamidis** | TTR stabilizer | ATTR-CM | ATTR-ACT |
| **Acoramidis** | TTR stabilizer | ATTR-CM | HELIOS-B |
| **Patisiran** | siRNA | ATTRv 神經 | APOLLO |
| **Vutrisiran** | siRNA (SC) | ATTRv 神經 | HELIOS-A |

### 台灣現況
- **Patisiran** 2023/5 起健保給付（ATTRv 神經病變）
- **Tafamidis** 用於 ATTR-CM：健保給付待確認

---

<!-- _class: divider -->

# 第八部分：台灣健保給付現況

---

# 基因檢測費用與給付

| 項目 | 健保 | 自費估計 |
|------|------|---------|
| 心臟遺傳疾病 NGS panel | ❌ | ~20,000–50,000 NTD |
| 單基因 Sanger | ❌ | ~5,000–10,000/gene |
| 癌症 NGS | ✅ 2024/5 起 | 補助 10,000–30,000 |
| Fabry 新生兒篩檢 | ✅ 部分補助 | — |
| 罕病基因檢測 | ✅ 部分補助 | 需罕病審查 |

> **Pearl**: 心臟遺傳疾病基因檢測目前健保**不給付**，但癌症 NGS 已有先例，未來有望擴展

### 罕見疾病法保障
- Fabry disease、ATTRv (FAP)：已列入**罕見疾病清單**
- 罕病醫療費用補助最高 **80%**，國際基因檢測費用補助 80%
- HCM、BrS、LQTS、wild-type ATTR-CM：**未列入**罕病

---

# 藥物治療健保給付總覽

| 疾病 | 藥物 | 健保 |
|------|------|------|
| Fabry | ERT (agalsidase) | ✅ 罕病給付 |
| Fabry | Migalastat | ✅ 有條件 |
| ATTRv 神經 | Patisiran | ✅ 2023/5 起 |
| ATTR-CM | Tafamidis | ⚠️ 待確認 |
| HCM | Mavacamten | ❌ 未核准 |
| BrS/LQTS | ICD | ✅ 符合適應症 |
| LQTS | BB, mexiletine | ✅ 常規藥物 |

---

<!-- _class: divider -->

# 第九部分：臨床實務建議

---

# 何時安排基因檢測？

| 臨床情境 | 建議 |
|---------|------|
| 確診 LQTS (Schwartz ≥ 3.5) | **Class I** |
| 確診 HCM (wall ≥ 15 mm) | **Class I** |
| 不明原因 LVH 疑似 Fabry | **Class I** |
| 確診 ARVC | **Class I** |
| 已知致病變異之一等親 | **Class I** cascade |
| 疑似 BrS + 家族 SCD 史 | **Class IIa** |
| < 40 歲不明原因心臟驟停 | **Class IIa** |

---

# 基因檢測的限制

1. **Incomplete penetrance** — 帶有致病變異者不一定發病
2. **Variable expressivity** — 同一突變不同嚴重度
3. **VUS 困境** — 20–40% 結果為 VUS，不可用於決策
4. **陰性不排除** — BrS 僅 20–25%、HCM 40–60% 可檢出
5. **Polygenic risk** — 部分疾病受多基因影響

> **Pearl**: 基因檢測是輔助工具，**臨床判斷仍是核心**

---

# 未來展望

- **Polygenic Risk Score (PRS)** — 多基因累積風險評估
- **Gene Therapy** — Fabry (ST-920)、ATTR (CRISPR in vivo editing)
- **CRISPR Gene Editing** — NTLA-2001 for TTR (NEJM 2021)
- **Pharmacogenomics** — 基因型指導藥物選擇
- **AI-ECG Screening** — 人工智慧心電圖篩檢遺傳性心臟病

> **Pearl**: CRISPR 基因編輯已在人體試驗中展現治療 ATTR 的潛力 — 單次注射可降低 TTR 蛋白 > 80%

---

<!-- _class: small-text -->

# 參考文獻 (1/2)

1. Wilde AAM, et al. EHRA/HRS/APHRS/LAHRS Expert Consensus on Genetic Testing. *Heart Rhythm*. 2022;19(7):e1-e54.
2. Ackerman MJ, et al. HRS/EHRA Expert Consensus on Genetic Testing. *Heart Rhythm*. 2011;8(8):1308-1339.
3. Kapa S, et al. Genetic Testing for LQTS. *Circulation*. 2009;120(18):1752-1760.
4. Campuzano O, et al. BrS 30 Years of Genetic Testing. *Heart Rhythm*. 2024;21(6):e230-e238.
5. Ho CY, et al. SHaRe Registry — HCM Genotype. *Circulation*. 2018;138(14):1387-1398.
6. Maron BJ, et al. HCM Diagnosis: JACC Review. *JACC*. 2022;79(4):372-389.
7. Olivotto I, et al. EXPLORER-HCM. *Lancet*. 2020;396:759-769.
8. Linhart A, et al. Fabry CV Management Consensus. *Eur J Heart Fail*. 2020;22:1076-1096.

---

<!-- _class: small-text -->

# 參考文獻 (2/2)

9. Maurer MS, et al. Tafamidis for ATTR-CM (ATTR-ACT). *NEJM*. 2018;379:1007-1016.
10. Adams D, et al. Patisiran for ATTRv (APOLLO). *NEJM*. 2018;379:11-21.
11. Gillmore JD, et al. CRISPR In Vivo Gene Editing for ATTR. *NEJM*. 2021;385:493-502.
12. Garcia-Pavia P, et al. ESC Cardiac Amyloidosis Position Statement. *Eur Heart J*. 2021;42:1554-1568.
13. Richards S, et al. ACMG Variant Classification Guidelines. *Genet Med*. 2015;17:405-424.
14. Ommen SR, et al. 2020 AHA/ACC HCM Guideline. *Circulation*. 2020;142:e558-e631.
15. Priori SG, et al. HRS/EHRA/APHRS Inherited Arrhythmia Consensus. *Heart Rhythm*. 2013;10:1932-1963.

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
