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
    padding: 40px 60px;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 52px; border-bottom: none; }
  section.lead h2 { color: #b0c4de; font-size: 34px; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #74b9ff; }
  section.lead blockquote, section.lead blockquote * { color: #2d3436; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: #ffffff;
    border-bottom: none;
    font-size: 60px;
    text-align: center;
  }
  section.divider h2 { color: #ffe066; }
  section.divider h3 { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 40px; }
  h2 { color: #0072bc; font-size: 32px; }
  h3 { color: #555555; }
  table { font-size: 27px; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.4em 1em;
    font-size: 28px;
  }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 15px; }
  section.small-text { font-size: 17px; }
  section.small-text h1 { font-size: 40px; }
  .note { font-size: 17px; }
footer: '謝慕揚 MD, PhD, FESC | Polygenic Risk Scores (NEJM Review) | 2026'
---

<!-- _class: lead -->

# 常見基因變異的臨床應用

## 多基因風險分數（PRS）與藥物基因體學 — NEJM Review

**整理：謝慕揚 MD, PhD, FESC** | 2026-09-24

[原文：Hunter DJ, Inouye M. N Engl J Med 2026;395:1206-17](https://doi.org/10.1056/NEJMra2413201)

> NEJM 綜論（非 RCT）之教學整理，僅供醫療專業人員教學參考

---

# 為什麼要讀這篇？

- 人類基因體草圖發表 **25 年**：罕見疾病與腫瘤已被改變
- 但**常見成人疾病**（CAD、AF、糖尿病）幾乎沒被改變
- 180 萬病人中只有 **6.1%** 病歷裡有基因檢測
- 問題：**PRS 已能預測風險，為何進不了診間？**

---

# 基因體分析的四個層級

| 方法 | 涵蓋 | 臨床成本 | PRS |
|------|------|---------|-----|
| **SNP array** | ~100 萬 SNP | ~$300 | ✅ |
| 標靶定序套組 | 少數疾病基因 | ~$500 | ❌ |
| 全外顯子定序 | ~1% 基因體 | >$1,000 | — |
| **全基因體定序** | 全部＋調控區 | $1,000–3,000 | ✅ |

- 研究端 SNP array 只要 **~$20**
- 定序變便宜後 → **PRS 幾乎可「順便」取得**

---

# 「常見疾病—常見變異」假說落空

- 原本預期：少數常見變異、各自效應大
- 實際：**相對風險 ≥1.5 的常見變異屈指可數**
- 原因：**負向天擇**淘汰高外顯率變異
- 門檻 RR 1.5 ≈「一位一等親罹病」
  - 這種家族史**已被用來調整 statin 建議**

---

# 少數值得記得的單一常見變異

| 族群 | 變異 | 相對風險 | 疾病 |
|------|------|---------|------|
| 歐洲 | **Factor V Leiden** | 2.3 | **VTE** |
| 歐洲 | **Prothrombin** | 1.5 | **VTE** |
| 歐洲 | APOE4 | 3–4 | 阿茲海默症 |
| 東亞 | **ALDH2\*2** | 0.2 | 酒精依賴 |
| 非洲 | APOL1 | 2.0–2.3 | CKD |

---

<!-- _class: divider -->

# 多基因風險分數（PRS）

## 把數千個小效應變異加總

---

# PRS 是什麼？

- GWAS 找到**數萬個**小效應常見變異
- 加權加總 → 個人遺傳傾向 = **PRS**
- 已驗證 **>5000 個 PRS**、數百種疾病
- 三大用途：
  1. **風險預測與分層**
  2. **診斷輔助**
  3. **預測治療反應**

---

# UK Biobank：PRS 能清楚分層

- PRS **最高 5%／中間 20%／最低 5%** 累積風險曲線明顯分開
- 心臟科相關：
  - **缺血性心臟病**（N=323,086）
  - **心房顫動**（N=227,653）
  - 第二型糖尿病、CKD
- 註：以住院診斷定義 → AF、糖尿病**絕對風險被低估**

---

<!-- _class: divider -->

# 心血管疾病

## PRS 證據最完整的領域

---

# CAD：風險預測

- CAD PRS 表現 **≥ 年齡以外任何單一傳統危險因子**
- **遺傳不是命運**
  - 健康生活型態可抵銷部分 CAD 遺傳風險
  - Khera et al., NEJM 2016

---

# 告知 PRS → 行為與結局改變

**MI-GENES 隨機試驗**

- 對無 CAD 者揭露 CAD PRS
- 對照：只揭露傳統危險因子
- 結果：
  - **LDL-C 較低**
  - **statin 起始與遵從性較高**
  - **10 年 MACE 較少**

---

# 誰從降脂治療獲益更多？

- 隨機試驗**回溯分析**：CAD PRS 高者
  - **Statin**：相對與絕對風險下降較大
  - **Alirocumab**（ODYSSEY OUTCOMES）
  - **Evolocumab**（FOURIER）
- 血壓／LDL-C PRS → 預測**較難控制**的病人

---

# 指引立場

| 組織 | 立場 |
|------|------|
| **AHA 2022** | PRS 科學聲明＋暫行指引 |
| **ESC 指引** | **不建議**用於 CVD 風險預測 |
| **ESC 共識 2025** | 可作為 **risk modifier** |

- ASCVD 計算器、QRISK3 **尚無法納入 PRS**

> **Pearl**：PRS 最適合當**灰色地帶病人的 risk enhancer**

---

<!-- _class: divider -->

# 其他疾病

---

# 癌症

- **攝護腺癌**：PRS 找到的癌症
  - 比 PSA＋MRI 找到的**更具臨床意義**
- **乳癌**：PRS 是風險分層**最大單一貢獻者**
  - 已納入 **BOADICEA／CanRisk**
- **WISDOM**：10–14% 女性篩檢建議改變
  - 總篩檢次數**沒有明顯增加**

---

# 糖尿病、免疫疾病、COPD

| 疾病 | PRS 貢獻 |
|------|---------|
| 第二型糖尿病 | 過重＋高 PRS ＞ 肥胖＋低 PRS |
| 第一型糖尿病 | AUC **>0.90**；鑑別 T1D／T2D／MODY |
| 僵直性脊椎炎 | 優於 CRP、MRI、HLA-B27 |
| COPD | 加上肺量計 → 診斷更準 |
| 視神經炎 | 協助 MS 治療決策 |

---

# 「敏感度／特異度太差」？

- 批評：用篩檢試驗標準，PRS 不及格
- 作者：**PRS 是危險因子，不是診斷工具**
- 年齡、性別、家族史用同標準**也會不及格**

> **Pearl**：PRS 像血壓一樣呈常態分布，可沿用現有風險溝通方式

---

# 成本效益與實作挑戰

- 成本效益支持：癌症篩檢、**CVD 預防（statin）**、**AAA 篩檢**
- 挑戰：
  - 臨床等級檢測少（eMERGE、MGB）
  - **歐洲血統為主** → 其他族群表現差
  - **不同 PRS 結果不一致** → 需 benchmarking

---

<!-- _class: divider -->

# 藥物基因體學

## Pharmacogenetics

---

# 藥物基因：證據已經在

- **HLA-B\*1502 + carbamazepine** → SJS
- FDA 生物標記清單常用藥：
  - **clopidogrel、warfarin**
  - allopurinol、phenytoin、tramadol、SSRI
- 美國退伍軍人：**99%** 帶 ≥1 個可行動變異

---

# 12 基因套組隨機試驗

**歐洲 7 國，開放標記（Lancet 2023）**

- 依基因型調整用藥
- **臨床相關藥物不良反應 ↓30%**

**最大瓶頸**

- 急需用藥時**等不及結果**
- 需要**預先檢測**＋病歷內嵌**決策支援**

---

# 臨床採用的六大障礙

1. 門診以**治療**為重心，而非預防
2. 臨床等級基因分析**不易取得**
3. 擔心**基因決定論**（但證據很少）
4. 缺乏**決策支援**與分類指引
5. **給付**：無國家核准全民使用
6. **資料安全**與歧視疑慮

---

# 未來展望

- **愛沙尼亞**：~20% 成人入庫，已回饋個人結果
- **英國 NHS 十年計畫**
  - 全民 PRS
  - 10 年內**所有新生兒**基因體定序
  - 藥物基因整合入電子病歷
- 仍須跨越：法規、決策支援、財務、資安

---

# Take-home Messages

1. 有份量的**單一常見變異很少**
2. **PRS** 與家族史、傳統危險因子大致獨立
3. CAD PRS 可輔助 **statin／PCSK9i** 決策
4. 藥物基因：瓶頸在**開藥當下拿不到資料**
5. **非歐洲族群**準確度較低

---

<!-- _class: small-text -->

# 參考文獻（1/2）

1. Hunter DJ, Inouye M. Clinical uses of common genetic variants associated with common diseases. [*N Engl J Med*. 2026;395(12):1206-17.](https://doi.org/10.1056/NEJMra2413201)
2. Inouye M, et al. Genomic risk prediction of coronary artery disease in 480,000 adults. [*J Am Coll Cardiol*. 2018;72(16):1883-93.](https://doi.org/10.1016/j.jacc.2018.07.079)
3. Patel AP, et al. A multi-ancestry polygenic risk score improves risk prediction for CAD. [*Nat Med*. 2023;29(7):1793-803.](https://doi.org/10.1038/s41591-023-02429-x)
4. Khera AV, et al. Genetic risk, adherence to a healthy lifestyle, and coronary disease. [*N Engl J Med*. 2016;375(24):2349-58.](https://doi.org/10.1056/NEJMoa1605086)
5. Kullo IJ, et al. Incorporating a genetic risk score into CHD risk estimates (MI-GENES). [*Circulation*. 2016;133(12):1181-8.](https://doi.org/10.1161/CIRCULATIONAHA.115.020109)
6. Naderian M, et al. Effect of disclosing a PRS for CHD on adverse cardiovascular events. [*Circ Genom Precis Med*. 2025;18(2):e004968.](https://doi.org/10.1161/CIRCGEN.124.004968)
7. O'Sullivan JW, et al. Polygenic risk scores for cardiovascular disease: AHA scientific statement. [*Circulation*. 2022;146(8):e93-e118.](https://doi.org/10.1161/CIR.0000000000001077)
8. Schunkert H, et al. Clinical utility and implementation of PRS for predicting CVD: ESC clinical consensus statement. [*Eur Heart J*. 2025;46(15):1372-83.](https://doi.org/10.1093/eurheartj/ehae649)
9. Mega JL, et al. Genetic risk, CHD events, and the clinical benefit of statin therapy. [*Lancet*. 2015;385(9984):2264-71.](https://doi.org/10.1016/S0140-6736(14)61730-X)
10. Natarajan P, et al. PRS identifies subgroup with greater relative benefit from statin therapy. [*Circulation*. 2017;135(22):2091-101.](https://doi.org/10.1161/CIRCULATIONAHA.116.024436)

---

<!-- _class: small-text -->

# 參考文獻（2/2）

11. Damask A, et al. High PRS for CAD and greater benefit from alirocumab (ODYSSEY OUTCOMES). [*Circulation*. 2020;141(8):624-36.](https://doi.org/10.1161/CIRCULATIONAHA.119.044434)
12. Marston NA, et al. Predicting benefit from evolocumab using a genetic risk score (FOURIER). [*Circulation*. 2020;141(8):616-23.](https://doi.org/10.1161/CIRCULATIONAHA.119.043805)
13. Schunkert H, Natarajan P, Samani NJ. The inherited basis of coronary artery disease. [*N Engl J Med*. 2026;394(6):576-87.](https://doi.org/10.1056/NEJMra2405153)
14. McHugh JK, et al. Assessment of a polygenic risk score in screening for prostate cancer. [*N Engl J Med*. 2025;392(14):1406-17.](https://doi.org/10.1056/NEJMoa2407934)
15. Fergus KB, et al. Integrating breast cancer PRS at scale in the WISDOM Study. [*Genome Med*. 2025;17(1):97.](https://doi.org/10.1186/s13073-025-01524-7)
16. Kiflen M, et al. Cost-effectiveness of PRS to guide statin therapy for CVD prevention. [*Circ Genom Precis Med*. 2022;15(5):e003423.](https://doi.org/10.1161/CIRCGEN.121.003423)
17. Abramowitz SA, et al. Evaluating performance and agreement of CHD polygenic risk scores. [*JAMA*. 2025;333(1):60-70.](https://doi.org/10.1001/jama.2024.23784)
18. Swen JJ, et al. A 12-gene pharmacogenetic panel to prevent adverse drug reactions. [*Lancet*. 2023;401(10374):347-56.](https://doi.org/10.1016/S0140-6736(22)01841-4)
19. Chanfreau-Coffinier C, et al. Projected prevalence of actionable pharmacogenetic variants among US veterans. [*JAMA Netw Open*. 2019;2(6):e195345.](https://doi.org/10.1001/jamanetworkopen.2019.5345)
20. Tapela NM, et al. PRS for SBP and LDL-C and treatment effectiveness. [*Eur J Prev Cardiol*. 2022;29(6):925-37.](https://doi.org/10.1093/eurjpc/zwab192)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

[原文連結：N Engl J Med 2026;395:1206-17](https://doi.org/10.1056/NEJMra2413201)
