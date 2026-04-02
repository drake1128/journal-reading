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
footer: '謝慕揚 MD, PhD, FESC | CLOSURE-AF Trial | 2026'
---

<!-- _class: lead -->

# CLOSURE-AF Trial
## 心房顫動患者左心耳封堵術 — 陰性試驗 (Negative Trial)
**Landmesser U, Skurk C, et al.**
**N Engl J Med 2026;394:1270-1280**
**整理：謝慕揚 MD, PhD, FESC | 2026-04-02**
[原文連結 (DOI)](https://doi.org/10.1056/NEJMoa2513310)

---

# 核心訊息 (Take-Home Message)

> **LAAO 在高風險 AF 患者中未達非劣性 (Noninferiority NOT Met)**

- 高中風風險 (CHA₂DS₂-VASc ≥ 4) **且** 高出血風險的 AF 患者
- LAAO vs 最佳藥物治療 (best medical care, 含 DOACs)
- 主要複合終點：LAAO 組事件率反而**較高** (16.8 vs 13.3 /100 pt-yr)
- 預期中的出血減少優勢**並未出現**
- RMST 差異：**−0.36 年** (95% CI: −0.70 to −0.01)

---

<!-- _class: divider -->

# 研究背景

---

# 為何進行 CLOSURE-AF？

## 臨床問題

- AF 患者約 **90%** 血栓源自左心耳 (left atrial appendage, LAA)
- 高出血風險患者長期使用 OAC 困難
- LAAO 理論上可取代長期 OAC，降低出血風險

## 既往證據的不足

| 試驗 | 對照組 | 時代 | 限制 |
|------|--------|------|------|
| PROTECT AF | Warfarin | Pre-DOAC | 未比較 DOAC |
| PREVAIL | Warfarin | Pre-DOAC | Coprimary 1 未達 |
| OPTION | DOAC (AF ablation 後) | DOAC 時代 | 較低風險族群 |

> CLOSURE-AF 是**首個在 DOAC 時代**比較 LAAO vs 最佳藥物治療的大型 RCT

---

<!-- _class: divider -->

# 研究方法

---

# 試驗設計 (Study Design)

## Multicenter RCT — 德國 40 個中心

| 項目 | 內容 |
|------|------|
| 設計 | 前瞻性、隨機、開放性 (open-label) |
| 隨機分派 | 1:1 LAAO vs Best Medical Care |
| 分析 | **非劣性 (Noninferiority)**，margin HR 1.3 |
| 統計方法 | Restricted Mean Survival Time (RMST) |
| 原計畫收案 | 1,586 人 |
| 實際收案 | **912 人** (因 OPTION trial 數據提前終止) |
| 追蹤時間 | 中位數 ~3 年 |

---

# 收案族群 (Study Population)

## 高中風風險 + 高出血風險

**高中風風險**：CHA₂DS₂-VASc ≥ 4 (平均 **5.2**)

**高出血風險** (符合任一)：
- HAS-BLED ≥ 3 (平均 **3.0**)
- 曾發生 intracranial / intraspinal / intraocular bleeding (BARC 3c)
- 曾發生 BARC 3a 或 3b bleeding
- CKD eGFR 15-29 mL/min/1.73m²
- 反覆出血致無法使用 anticoagulation

> 平均年齡 **77.9 歲**，女性 **38.6%**，白人 **93.6%**

---

# 介入方式與對照

## LAAO 組 — 使用裝置

| 裝置 | 廠商 |
|------|------|
| Watchman / Watchman FLX | Boston Scientific |
| Amplatzer Amulet | Abbott |
| LAmbre (bailout only) | Lifetech |

- 術後短期抗血栓藥物 (依仿單及術者判斷)

## 藥物治療組 (Best Medical Care)

- 醫師主導 (physician-directed)
- 包含 DOAC (如適用)、抗血小板藥物、或其他方案

---

# 研究終點 (Endpoints)

## 主要複合終點 (Primary Composite Endpoint)

- **Stroke** (ischemic or hemorrhagic)
- **Systemic embolism** (全身性栓塞)
- **Major bleeding** (ISTH criteria)
- **CV death or unexplained death**

## 次要終點

- 各組成終點個別分析
- All-cause mortality (全因死亡)
- Periprocedural complications (手術併發症)

---

<!-- _class: divider -->

# 主要結果

---

# 主要終點：非劣性未達 (Noninferiority NOT Met)

## Primary Composite Endpoint

| | LAAO 組 | 藥物治療組 |
|--|:---:|:---:|
| 事件數 | 155 | 127 |
| Patient-years | 920.8 | 957.0 |
| **事件率 (/100 pt-yr)** | **16.8** | **13.3** |

## RMST 分析

- RMST 差異：**−0.36 年** (95% CI: −0.70 to −0.01)
- 整個 CI 位於零的左側 → LAAO 組無事件存活時間**更短**

> **結論：Noninferiority NOT Met — LAAO 組表現反而較差**

---

# 各組成終點分析

| 終點 (/100 patient-years) | LAAO 組 | 藥物治療組 | 解讀 |
|--------------------------|:---:|:---:|------|
| Stroke (ischemic + hemorrhagic) | 2.6 | 2.7 | 相似 |
| Major bleeding | **7.4** | **6.2** | LAAO 未減少出血 |
| CV / unexplained death | **9.5** | **7.7** | LAAO 較高 |
| All-cause mortality | **14.8** | **13.5** | LAAO 較高 |

> **預期中的出血減少優勢完全未出現**

---

# 手術相關結果 (Procedural Outcomes)

## 裝置植入成功率：98.3% (414/421)

## Periprocedural Complications (7 天內)：**5.7%**

| 併發症 | 數量 |
|--------|:---:|
| Major bleeding (手術相關) | 18 例 |
| 手術相關死亡 | 2 例 |
| Device embolization | 1 例 |

> 高風險族群的 periprocedural events 造成早期事件負擔，抵消潛在長期獲益

---

# Per-Protocol 分析 — 結果一致

## 與 ITT 分析方向一致

- RMST 差異：**−0.40 年** (95% CI: −0.76 to −0.04)
- 進一步確認 LAAO 未達非劣性

> Per-protocol 分析排除 crossover 後，**差異反而更大** (−0.40 vs −0.36)

---

<!-- _class: divider -->

# 討論與臨床意義

---

# 為何 LAAO 在本試驗中失敗？

## 四個關鍵因素

**1. 高風險族群的脆弱性 (Frailty)**
- 平均年齡 78 歲，CHA₂DS₂-VASc 5.2
- 對 periprocedural complications 耐受度低

**2. 出血減少假說未獲驗證**
- Major bleeding: LAAO 7.4 vs 藥物 6.2 /100 pt-yr
- 術後短期仍需抗血栓藥物 + periprocedural bleeding

**3. DOAC 時代的高效藥物治療**
- 對照組不再是 warfarin，而是包含 DOACs

**4. 手術併發症的早期代價**
- 5.7% complication rate (含 2 例死亡)

---

# 與其他 LAAO 試驗的比較

| 試驗 | 族群 | 對照組 | CHA₂DS₂-VASc | 結果 |
|------|------|--------|:---:|------|
| PROTECT AF | 中低風險 | Warfarin | ~3.4 | Noninferior → Superior |
| PREVAIL | 中低風險 | Warfarin | ~3.8 | Noninferior (mixed) |
| OPTION | Ablation 後 | DOAC | ~3.2 | Noninferior |
| **CLOSURE-AF** | **高風險** | **Best Medical Care** | **5.2** | **NOT Met** |

> 族群風險越高，LAAO 的 net clinical benefit 越不確定

---

# 臨床啟示 (Clinical Implications)

## 對 LAAO 適應症的重新思考

> 在高中風且高出血風險的 AF 患者中，目前的證據**不支持**以 LAAO 取代藥物治療

- **病人選擇至關重要** — 高齡、高共病患者可能無法從介入策略獲益
- **DOACs 仍是基石** — 即使高出血風險族群，最佳藥物治療仍是首選
- **Risk-benefit 需個別化評估** — 不應一概而論

## 未來方向

- 持續中的試驗比較 LAAO vs OAC 在**中等風險**患者
- 結果可能重新定義 LAAO 的最適族群

---

# 研究限制 (Limitations)

- **地理限制**：僅在德國進行，93.6% 白人
- **提前終止**：912/1,586 人，個別終點 **underpowered**
- **開放性設計**：可能產生 detection bias
- **藥物治療組異質性**：非標準化治療方案
- **追蹤時間**：中位數 ~3 年，可能不足以觀察長期效益

---

<!-- _class: small-text -->

# 參考文獻

1. Hindricks G, et al. 2020 ESC AF Guidelines. [*Eur Heart J*. 2021;42:373-498.](https://doi.org/10.1093/eurheartj/ehaa612)
2. Joglar JA, et al. 2023 ACC/AHA AF Guideline. [*Circulation*. 2024;149:e1-e156.](https://doi.org/10.1161/CIR.0000000000001193)
3. Connolly SJ, et al. Dabigatran vs warfarin (RE-LY). [*N Engl J Med*. 2009;361:1139-51.](https://doi.org/10.1056/NEJMoa0905561)
4. Patel MR, et al. Rivaroxaban vs warfarin (ROCKET AF). [*N Engl J Med*. 2011;365:883-91.](https://doi.org/10.1056/NEJMoa1009638)
5. Granger CB, et al. Apixaban vs warfarin (ARISTOTLE). [*N Engl J Med*. 2011;365:981-92.](https://doi.org/10.1056/NEJMoa1107039)
6. Holmes DR, et al. PROTECT AF. [*Lancet*. 2009;374:534-42.](https://doi.org/10.1016/S0140-6736(09)61343-X)
7. Holmes DR Jr, et al. PREVAIL. [*J Am Coll Cardiol*. 2014;64:1-12.](https://doi.org/10.1016/j.jacc.2014.04.029)
8. Wazni OM, et al. OPTION. [*N Engl J Med*. 2024;391:1210-20.](https://doi.org/10.1056/NEJMoa2408687)
9. Whitlock RP, et al. LAAOS III. [*N Engl J Med*. 2021;384:2081-91.](https://doi.org/10.1056/NEJMoa2101897)
10. Landmesser U, et al. CLOSURE-AF. [*N Engl J Med*. 2026;394:1270-80.](https://doi.org/10.1056/NEJMoa2513310)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A
**CLOSURE-AF Trial: Noninferiority NOT Met**
**LAAO 在高風險 AF 患者中未優於藥物治療**
