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
  section.lead h2 { color: #9ec5ff; }
  section.lead h3 { color: #ffffff; font-weight: normal; font-size: 30px; }
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
  section.divider h1 { color: #ffffff; border-bottom: none; font-size: 64px; text-align: center; }
  section.divider h2 { color: #ffffff; font-size: 36px; text-align: center; font-weight: bold; }
  section.divider h3 { color: #ffe082; font-size: 30px; text-align: center; font-weight: normal; }
  section.divider p, section.divider strong { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 40px; }
  h2 { color: #0072bc; font-size: 32px; }
  h3 { color: #555555; font-size: 29px; }
  a { color: #0072bc; }
  table { font-size: 27px; width: 100%; display: table; }
  section.divider footer, section.lead footer, section.divider header { color: #dfe6e9; }
  th { background-color: #0072bc; color: white; padding: 6px 12px; }
  td { padding: 5px 12px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.4em 1em;
    font-size: 28px;
  }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.6em; font-size: 24px; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 15px; }
  section.small-text { font-size: 17px; }
  section.small-text h1 { font-size: 40px; }
  .note { font-size: 17px; color: #666666; }
footer: '謝慕揚 MD, PhD, FESC | SINGLE-AF 中度風險 AF 抗凝 | 2026'
---

<!-- _class: lead -->
# 中度中風風險 AF，該不該抗凝？
## SINGLE-AF — Anticoagulation for AF with Intermediate Stroke Risk
### N Engl J Med 2026;395:1155-65 · 南韓 18 中心 · 1803 人

**謝慕揚 MD, PhD, FESC** | 2026-09-24

[原文連結：doi.org/10.1056/NEJMoa2607978](https://doi.org/10.1056/NEJMoa2607978)

> 主要終點**正向**：DOAC 0.5% vs 不抗凝 1.5%（HR 0.31）

---

# 一句話總結

CHA₂DS₂-VASc **男 1 分／女 2 分**的 AF：DOAC vs 不抗凝

| 24 個月主要複合終點 | DOAC | 不抗凝 |
|---|---|---|
| 中風＋栓塞＋大出血＋CV 死亡 | **4 (0.5%)** | **13 (1.5%)** |

**差異 −1.0 個百分點（−2.0 至 −0.1），P = 0.03**
**HR 0.31（95% CI 0.10–0.94）**

> 第一個直接回答指引 **Class IIa** 灰色地帶的隨機試驗

---

# 臨床背景：Class IIa 的灰色地帶

- ACC/AHA 2023、ESC 2024：男 ≥2、女 ≥3 → **Class I**
- **男 1 分、女 2 分** → 僅 **Class IIa**「可考慮」
- 觀察性研究年中風率差很多：
  - 台灣健保（Chao 2015）約 **2.75%**
  - 丹麥約 **1.55%**；歐洲多國近期約 **0.7%**
- 從未有 **DOAC vs 不治療** 的隨機比較

---

<!-- _class: divider -->
# 試驗設計
## 開放標籤 · 判定者盲性 · 優越性試驗

---

# 試驗設計

| 項目 | 內容 |
|------|------|
| 設計 | 研究者主導、開放標籤、事件判定盲性 |
| 族群 | ≥19 歲 AF，CHA₂DS₂-VASc 男 1／女 2 |
| 分組 | 1:1 → DOAC vs **不抗凝** |
| DOAC | apixaban 5 mg BID 或 rivaroxaban 20 mg QD |
| 收案 | 2020-07 至 2023-06，南韓 18 中心 |
| 追蹤 | 24 個月（3、6、12、18、24 月） |

---

# 主要排除條件

- 腎功能：Cr ≥3.5 mg/dL 或 **CrCl <30 mL/min**
- 肝功能：AST/ALT >3× ULN 或 Child–Pugh B/C
- 其他抗凝適應症：機械瓣、中重度 MS、DVT
- 顯著結構性心臟病：DCM、HCM、類澱粉沉積

不抗凝組：電燒／電擊前後可**短期**用 DOAC；抗血小板僅限臨床適應症

---

# 主要終點與統計

**24 個月：中風＋全身性栓塞＋大出血 (ISTH)＋心血管死亡**

- 原含「全因死亡」→ 2025/1 DSMB（不知分組）發現死亡皆非心血管 → **改為心血管死亡**
- 預估事件率 **2.0% vs 4.5%** → 1800 人、80% power
- Fine–Gray 次分布風險模型（非 CV 死亡為競爭風險）
- 敏感度：CHA₂DS₂-VASc 升級時設限、win ratio

---

# 病人特徵（1）

| 特徵 | DOAC (902) | 不抗凝 (901) |
|------|-----------|-------------|
| 平均年齡 | 60.7 | 60.0 |
| ≥65 歲 | 33.7% | 31.3% |
| 男性 | 75.6% | 77.0% |
| 陣發性 AF | 70.5% | 73.0% |
| 先前 AF 電燒 | 29.5% | 31.6% |

---

# 病人特徵（2）

| 特徵 | DOAC | 不抗凝 |
|------|------|--------|
| 高血壓 | 48.2% | 53.5% |
| 心衰竭 | 10.3% | 8.0% |
| 糖尿病 | 7.4% | 7.8% |
| CHA₂DS₂-VASc 平均 | 1.3 | 1.3 |
| **HAS-BLED 平均** | **0.5** | **0.5** |

> **年輕（60 歲）、出血風險極低**的族群

---

# 實際用藥

- DOAC 組 **100%** 用 DOAC
  - apixaban 5 mg **67.4%**、rivaroxaban 20 mg 14.1%、15 mg 13.9%
  - 全劑量 81.6%、減量 18.4%
- 不抗凝組 crossover **5.5%**（50 人）
- **抗血小板：0.4% vs 36.5%** ← 注意
- 24 個月完成追蹤 **94.6%**（兩組相同）

---

<!-- _class: divider -->
# 結果
## 17 個事件 · P = 0.03

---

# 主要結果

| 終點 | DOAC | 不抗凝 | HR (95% CI) |
|------|------|--------|-------------|
| **主要複合終點** | **4 (0.5%)** | **13 (1.5%)** | **0.31 (0.10–0.94)** |

- 絕對差異 **−1.0 個百分點**（95% CI −2.0 至 −0.1），**P = 0.03**
- Win ratio **3.31**（95% CI 1.15–9.54）
- 敏感度分析（升級設限）結果一致
- NNT ≈ **100 人治療 2 年**避免 1 個事件

---

# 次要終點：中風與栓塞

| 終點 | DOAC | 不抗凝 | HR (95% CI) |
|------|------|--------|-------------|
| 中風（全部） | 3 (0.3%) | 10 (1.1%) | 0.30 (0.08–1.08) |
| **缺血性中風** | **1 (0.1%)** | **10 (1.1%)** | **0.10 (0.01–0.77)** |
| 出血性中風 | 2 (0.2%) | 0 | — |
| 全身性栓塞 | 0 | 1 (0.1%) | — |
| TIA | 0 | 3 (0.3%) | — |

<p class="note">次要終點未校正多重比較，CI 不可用於推論確定療效。不抗凝組年中風率約 0.6%。</p>

---

# 次要終點：死亡與住院

| 終點 | DOAC | 不抗凝 | HR (95% CI) |
|------|------|--------|-------------|
| 心血管死亡 | 0 | 0 | — |
| 全因死亡 | 3 (0.3%) | 5 (0.6%) | 0.60 (0.14–2.51) |
| 心肌梗塞 | 0 | 0 | — |
| 任何原因住院 | 18.6% | 17.6% | 1.07 (0.86–1.33) |
| 嚴重不良事件 | 8.9% | 9.3% | — |

---

# 出血

| 終點 | DOAC | 不抗凝 | HR (95% CI) |
|------|------|--------|-------------|
| 大出血 (ISTH) | 3 (0.3%) | 4 (0.5%) | 0.75 (0.17–3.35) |
| 顱內出血 | 2 (0.2%) | 1 (0.1%) | 2.00 (0.18–22.05) |
| 腸胃道出血 | 1 (0.1%) | 2 (0.2%) | 0.50 (0.05–5.51) |
| 致命性出血 | 0 | 0 | — |
| CRNMB | 22 (2.5%) | 14 (1.6%) | 1.58 (0.81–3.08) |

---

# 出血：怎麼解讀？

- DOAC 大出血約 **0.2%/年**（ARTESIA 2.1%、NOAH 1.5%/病人年）
- DOAC 組 2 例顱內出血**都是出血性中風**
  - 不抗凝組 1 例為硬腦膜下出血
  - 數字太小無法下結論，但臨床嚴重度高
- 不抗凝組 **36.5% 用抗血小板** → 墊高其出血率

> 安全性比較**對 DOAC 可能偏有利**

---

# 次族群分析（主要終點）

| 次族群 | DOAC | 不抗凝 | HR |
|--------|------|--------|-----|
| <65 歲 | 0.3% | 1.4% | 0.26 |
| ≥65 歲 | 0.7% | 1.8% | 0.37 |
| 糖尿病 | 1.5% | **6.1%** | 0.24 |
| 陣發性 AF | 0.5% | 1.1% | 0.44 |
| 非陣發性 AF* | 0.4% | **2.6%** | 0.15 |

<p class="note">*post hoc。效果在各次族群一致；女性僅 427 人、DOAC 組 0 事件無法估 HR。</p>

---

<!-- _class: divider -->
# 解讀與限制

---

# 優點

- **第一個**直接比較 DOAC vs 不抗凝（中度風險）的 RCT
- 事件由**不知分組**的委員會判定
- ITT 分析、追蹤完成率 **94.6%**
- 使用現代 DOAC，直接對應臨床

---

# 限制（1）

1. **開放標籤** → 仍可能有偏差
2. 事件遠少於預期（**17 起** vs 預估約 58）
   - HR 上限 **0.94** 貼近 1
   - 效果大小**可能被高估**
3. 主要終點中途修改（全因 → CV 死亡）

---

# 限制（2）

4. 5.4% 未完成 2 年追蹤
5. 不抗凝組 1/3 用抗血小板 → 安全性比較不公平
6. **僅南韓東亞人**；女性（23.7%）與非陣發性 AF 代表性不足

> 作者：需要**確認性試驗或匯總分析**

---

# 與其他抗凝試驗比較

| 試驗 | 族群 | 對照年中風率 |
|------|------|-------------|
| **SINGLE-AF** | 臨床 AF、中度風險 | **~0.6%** |
| ALONE-AF | 電燒後無復發 | 0.1% |
| OCEAN | 電燒後高風險 | 0.6%（aspirin） |
| NOAH-AFNET 6 | 裝置 AHRE | 1.1%（placebo） |
| ARTESIA | 亞臨床 AF | 1.2%（aspirin） |

---

# 關鍵觀念：兩個維度

```text
         臨床風險分數 (CHA2DS2-VASc)
                 ↑ 高
   NOAH / ARTESIA│
   (風險高、burden 低、出血多)
                 │
  ───────────────┼──────────────→ AF burden 高
                 │     SINGLE-AF
                 │ (風險中、burden 較高、出血極低)
```

- **AF burden** 與**臨床風險**是獨立維度
- 跨試驗比較要謹慎

---

<!-- _class: divider -->
# 臨床啟示

---

# 台灣臨床實務

- 台灣健保資料：中度風險年中風率約 **2.75%** → 支持抗凝
- SINGLE-AF 是**東亞族群** RCT，外推性相對高
- **East Asian paradox**：東亞人顱內出血風險較高
  - 嚴控血壓、正確劑量
  - 避免不必要的抗血小板併用

---

# 我的實務建議（個人意見）

- 中度風險＋HAS-BLED 低＋無抗血小板需求
  → **傾向開始 DOAC，與病人共同決策**
- 更傾向抗凝：**糖尿病、非陣發性 AF**、左房擴大
- **Aspirin 不是抗凝的替代品**
- CHA₂DS₂-VASc 2 年內約 13–17% 會升級 → **每年重評**

---

# Clinical Pearls

> **1.** DOAC 優於不抗凝：0.5% vs 1.5%，HR 0.31，P = 0.03

> **2.** 效益來自**缺血性中風**減少（1 vs 10）；大出血未增加

> **3.** 僅 17 個事件，效果大小精確度有限

> **4.** 2 例 ICH 皆為出血性中風 → 東亞病人須嚴控血壓

---

<!-- _class: small-text -->
# 參考文獻（1）

1. Kim D, et al. Anticoagulation for AF with Intermediate Stroke Risk. [*N Engl J Med* 2026;395:1155-65.](https://doi.org/10.1056/NEJMoa2607978) PMID 42663303
2. Joglar JA, et al. 2023 ACC/AHA/ACCP/HRS AF guideline. [*Circulation* 2024;149:e1-e156.](https://doi.org/10.1161/CIR.0000000000001193)
3. Van Gelder IC, et al. 2024 ESC AF guidelines. [*Eur Heart J* 2024;45:3314-414.](https://doi.org/10.1093/eurheartj/ehae176)
4. Lip GYH, et al. CHA2DS2-VASc: Euro Heart Survey. [*Chest* 2010;137:263-72.](https://doi.org/10.1378/chest.09-1584)
5. Lip GYH, et al. OAC, aspirin, or no therapy with 0 or 1 risk factor. [*J Am Coll Cardiol* 2015;65:1385-94.](https://doi.org/10.1016/j.jacc.2015.01.044)
6. Friberg L, et al. Benefit of anticoagulation unlikely with CHA2DS2-VASc 1. [*J Am Coll Cardiol* 2015;65:225-32.](https://doi.org/10.1016/j.jacc.2014.10.052)
7. Chao TF, et al. AF with 1 additional risk factor — OAC? (Taiwan) [*J Am Coll Cardiol* 2015;65:635-42.](https://doi.org/10.1016/j.jacc.2014.11.046)
8. Østergaard L, et al. Thromboembolism with CHA2DS2-VASc 1. [*Circulation* 2024;149:764-73.](https://doi.org/10.1161/CIRCULATIONAHA.123.066477)
9. Komen JJ, et al. OAC in AF at low stroke risk. [*Eur Heart J* 2022;43:3528-38.](https://doi.org/10.1093/eurheartj/ehac111)

---

<!-- _class: small-text -->
# 參考文獻（2）

10. Anjum M, et al. Norwegian AFNOR study. [*Eur Heart J* 2024;45:57-66.](https://doi.org/10.1093/eurheartj/ehad659)
11. Ruff CT, et al. NOAC vs warfarin meta-analysis. [*Lancet* 2014;383:955-62.](https://doi.org/10.1016/S0140-6736(13)62343-0)
12. Granger CB, et al. ARISTOTLE. [*N Engl J Med* 2011;365:981-92.](https://doi.org/10.1056/NEJMoa1107039)
13. Kim D, et al. SINGLE-AF design and protocol. [*Heart Rhythm O2* 2025;7:545-51.](https://doi.org/10.1016/j.hroo.2025.12.008)
14. Kim D, et al. ALONE-AF. [*JAMA* 2025;334:1246-54.](https://doi.org/10.1001/jama.2025.14679)
15. Verma A, et al. OCEAN. [*N Engl J Med* 2026;394:323-32.](https://doi.org/10.1056/NEJMoa2509688)
16. Healey JS, et al. ARTESIA. [*N Engl J Med* 2024;390:107-17.](https://doi.org/10.1056/NEJMoa2310234)
17. Kirchhof P, et al. NOAH-AFNET 6. [*N Engl J Med* 2023;389:1167-79.](https://doi.org/10.1056/NEJMoa2303062)
18. Kim HK, et al. The East Asian paradox. [*Thromb Haemost* 2021;121:422-32.](https://doi.org/10.1055/s-0040-1718729)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

[原文：N Engl J Med 2026;395:1155-65](https://doi.org/10.1056/NEJMoa2607978)
