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
footer: '謝慕揚 MD, PhD, FESC | CAD Genetics Review | 2026'
---

<!-- _class: lead -->

# The Inherited Basis of Coronary Artery Disease

## 冠狀動脈疾病的遺傳基礎

**謝慕揚 MD, PhD, FESC**
資料來源：[N Engl J Med 2026;394:576-87](https://doi.org/10.1056/NEJMra2405153) | 2026-03-12

---

# 大綱

1. 文章概述與背景
2. 單基因型冠心病 (Monogenic CAD)
3. 多基因風險架構 (Polygenic Risk)
4. 多基因風險評分 (PRS) 與臨床應用
5. 遺傳學導向的治療策略
6. Mendelian Randomization
7. 結論與未來方向

---

<!-- _class: divider -->

# 第一部分：文章概述

---

# 冠狀動脈疾病的遺傳背景

- CAD 是行為、環境、遺傳與隨機因素交互作用的結果
- 約 **50%** 的男性、**33%** 的女性一生中會發展 CAD
- 雙胞胎研究：致死性 CAD 的 **heritability 高達 50%**
- 自 2007 年起，GWAS 已識別數百個 CAD 易感性相關遺傳變異

> **Pearl**：Osler 在超過一世紀前即觀察到心絞痛的家族聚集現象

---

# 核心發現摘要

| 層面 | 發現 |
|------|------|
| **單基因 (Monogenic)** | FH 影響約 1/250 人口；*LDLR*, *APOB*, *PCSK9* |
| **多基因 (Polygenic)** | GWAS 識別 **346 個**顯著基因座 |
| **PRS 風險** | 最高 5% 者，CAD 風險為平均值的 **3-5 倍** |
| **臨床意義** | 高 PRS 者從降脂治療獲益更大；生活方式可抵消高遺傳風險 |

---

<!-- _class: divider -->

# 第二部分：單基因型冠心病

---

# 家族性高膽固醇血症 (FH)

- **盛行率**：異合子約 1/250；同合子約 1/200,000
- **遺傳模式**：不完全顯性遺傳
- **三大致病基因**：
  - *LDLR*：LDL 受體功能減損
  - *APOB*：Apolipoprotein B 功能改變
  - *PCSK9*：功能增強 (gain-of-function)

> **Pearl**：即使 LDL-C 水平相似，有 FH 變異者風險仍為無變異者的 **2-3 倍**

---

# FH 臨床表現與診斷線索

- LDL cholesterol：成人 **>190 mg/dL**、兒童 **>150 mg/dL**
- 合併早發性 CAD 家族史
- Xanthelasma 或 tendon xanthomas
- 異合子 FH 於 **45 歲前約 20%** 已有動脈粥狀硬化

| 族群 | FH 變異盛行率 |
|------|-------------|
| 一般人群 | 約 0.4% |
| LDL-C >190 mg/dL | 約 3.5% |
| 臨床判定「確定」FH | 24% |

---

# 其他罕見單基因型

| 疾病 | 基因 | 特徵 |
|------|------|------|
| 體染色體隱性高膽固醇血症 | *LDLRAP1* | 罕見，早發性 CAD |
| Sitosterolemia | *ABCG5/G8* | 植物固醇吸收增加 |
| Pseudoxanthoma elasticum | *ABCC6* | 血管鈣化 |
| NO 訊號路徑缺陷 | *GUCY1A1*, *PDE5A* | 血壓升高 |
| TG 調控異常 | *APOA5* | 早發性 MI |
| 膽固醇運輸異常 | *SCARB1* | 嚴重早發性 CAD |

---

<!-- _class: divider -->

# 第三部分：多基因風險架構

---

# GWAS 研究發現

- **研究規模**：>180,000 名 CAD 患者，總計超過 **100 萬人**
- **發現**：**346 個**全基因組顯著風險區域
- **顯著性閾值**：P < 5×10⁻⁸

| 風險因子 | 基因座數 | 代表性基因 |
|---------|---------|-----------|
| 血壓 | 135 | *ADAMTS7*, *NOS3*, *PHACTR1* |
| 發炎 | 126 | *IL6R*, *CXCR4*, *SMAD3* |
| 脂質代謝 | 117 | *LDLR*, *PCSK9*, *LPA* |
| 凝血 | 109 | *BCAR1*, *FGD6* |
| 機轉未明 | 76 | 尚待研究 |

---

# 基因表達的多組織分佈

- **肝臟**：*APOB*, *LDLR*, *PCSK9*, *LPA*, *HMGCR*, *SORT1*
- **血管平滑肌**：*ADAMTS7*, *TCF21*, *GUCY1A1*, *PDE5A*
- **血管內皮**：*NOS3*, *JCAD*, *PECAM1*, *PROCR*
- **免疫細胞**：*IL6R*, *LIPA*, *PHACTR1*, *TRIB1*
- **血小板**：*GUCY1A1*, *SH2B3*
- **大腦（神經內分泌）**：*BDNF*, *FTO*, *MC4R*

> **Pearl**：CAD 是多系統疾病，風險基因橫跨肝臟、血管、免疫、代謝等多個系統

---

<!-- _class: divider -->

# 第四部分：多基因風險評分 (PRS)

---

# PRS 的核心概念

1. 每個人隨機遺傳**數百個** CAD 風險對偶基因
2. 人群中 PRS 呈 **Gaussian distribution**
3. 各風險對偶基因獨立遺傳、具**乘法效應** → 高 PRS 端風險呈指數增加
4. 現行 PRS 納入所有具資訊性的遺傳變異（含未達 GWAS 顯著者）

| PRS 百分位 | Hazard Ratio | 風險描述 |
|-----------|-------------|---------|
| 45th–55th | 1.00 | 參考組 |
| >75th–85th | 1.76 | 明顯升高 |
| >85th–95th | 2.35 | 高風險 |
| >95th–97.5th | 3.11 | 極高風險 |
| >97.5th | **4.64** | 最高風險 |

---

# 哪些人最適合 PRS 評估？

| 族群 | PRS 的價值 |
|------|-----------|
| **中等臨床風險中老年人** | SCORE2 10年風險 5-10%；協助啟動降脂治療決策 |
| **年輕成人** | 40歲無傳統風險因子男性：最高 PRS 五分位 → 70歲前 CAD 風險 **30-40%**；最低 → 僅 **10%** |
| **早發性 CAD 患者** | 高 PRS 可釐清病因、預測復發事件 |

> **Pearl**：多基因風險的相對貢獻在年輕時（傳統風險因子盛行率較低時）更大

---

# PRS 的限制

1. **族群適用性**：數據主要來自歐洲血統人群
2. **標準化不足**：尚無統一共識的 PRS 或報告標準
3. **指南尚未納入**：目前指南未正式納入 CAD PRS
4. **成本效益**：研究與實施缺口尚待解決
5. **公平取得**：自費成本可能限制公平取得

---

<!-- _class: divider -->

# 第五部分：遺傳學導向治療

---

# 已驗證的遺傳學導向治療

| 基因/路徑 | 衍生藥物 | 機轉 |
|----------|---------|------|
| *LDLR* (FH) | **Statins** | 上調肝臟 LDL 受體 |
| *PCSK9* 失功能 | **Evolocumab, Alirocumab** | 罕見破壞性變異啟發藥物開發 |
| *NPC1L1* | **Ezetimibe** | 驗證藥理抑制降低 LDL-C |
| *ACLY* | **Bempedoic acid** | Mendelian randomization 支持 |

> **Pearl**：具有人類遺傳學支持的藥物更可能獲得監管核准

---

# 降脂治療效益：高 PRS vs 低 PRS

| 研究 | 藥物 | 情境 | 低 PRS | 高 PRS |
|------|------|------|--------|--------|
| WOSCOPS | Pravastatin | 初級預防 | -2.80% | **-7.90%** |
| ASCOT | Atorvastatin | 初級預防 | -1.06% | **-3.98%** |
| JUPITER | Rosuvastatin | 初級預防 | -0.36% | **-0.94%** |
| CARE | Pravastatin | 次級預防 | -1.95% | **-6.03%** |
| ODYSSEY | Alirocumab | 次級預防 | -1.50% | **-6.00%** |
| FOURIER | Evolocumab | 次級預防 | -1.40% | **-4.00%** |

> 高 PRS 者從降脂治療獲得的絕對風險下降約為低 PRS 的 **2-3 倍**

---

# 開發中的新治療標靶

| 標靶 | 藥物類型 | 現況 |
|------|---------|------|
| *LPA* / Lipoprotein(a) | Apo(a) 轉錄阻斷劑 | 心血管結局試驗進行中 |
| *ANGPTL3* | ANGPTL3 抑制劑 | 降低 TG 與 CAD 風險 |
| *APOC3* | APOC3 抑制劑 | 失功能變異降低 TG 與 CAD |
| *NOS3/GUCY1A1/PDE5* | PDE5 抑制劑 | 觀察性研究顯示 CAD 事件率下降 |
| NLRP3 inflammasome | 臨床試驗中 | 遺傳分析確認因果特徵 |

---

<!-- _class: divider -->

# 第六部分：Mendelian Randomization

---

# Mendelian Randomization 的因果推論

使用遺傳變異作為工具變數 (instrumental variables)，區分因果 vs 混淆生物標記

| 已驗證為**因果**風險因子 | 已**去優先化**（非因果） |
|------------------------|----------------------|
| 升高的 LDL cholesterol | 低 HDL cholesterol |
| 升高的 Triglyceride | 低 Vitamin D |
| 高血壓 | 高 CRP |
| 肥胖 | 高 Uric acid |
| 升高的 Lipoprotein(a) | |
| 第二型糖尿病 | |

> **Pearl**：身高較矮與 CAD 風險增加為因果性；習慣性飲酒可能增加 CAD 風險

---

<!-- _class: divider -->

# 第七部分：結論

---

# Key Points 重點整理

1. **罕見變異** → 以大效應直接指出治療標靶
2. **常見變異** → GWAS 顯示佔 CAD 遺傳風險相當比例
3. **多器官效應** → 橫跨肝臟、血管、免疫、代謝系統
4. **Mendelian randomization** → 區分因果 vs 相關風險標記
5. **PRS** → 整合常見變異效應為單一風險測量
6. **PRS 獨立於傳統因子** → 改善風險分層
7. **遺傳風險可修正** → 生活方式 + 降脂治療有效
8. **臨床應用尚無共識** → 跨族群、成本效益待解決

---

<!-- _class: small-text -->

# 參考文獻

1. Schunkert H, et al. The Inherited Basis of CAD. [*N Engl J Med*. 2026;394:576-87.](https://doi.org/10.1056/NEJMra2405153)
2. Lloyd-Jones DM, et al. Lifetime risk of developing CHD. [*Lancet*. 1999;353:89-92.](https://doi.org/10.1016/S0140-6736(99)80005-8)
3. Aragam KG, et al. Risk variants for CAD in over a million participants. [*Nat Genet*. 2022;54:1803-15.](https://doi.org/10.1038/s41588-022-01233-6)
4. Khera AV, et al. Genetic risk, healthy lifestyle, and coronary disease. [*N Engl J Med*. 2016;375:2349-58.](https://doi.org/10.1056/NEJMoa1605086)
5. Patel AP, et al. Multi-ancestry PRS for CAD. [*Nat Med*. 2023;29:1793-803.](https://doi.org/10.1038/s41591-023-02429-x)
6. Ference BA, et al. MR study of ACLY and CVD. [*N Engl J Med*. 2019;380:1033-42.](https://doi.org/10.1056/NEJMoa1806747)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
