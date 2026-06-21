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
  section.lead h1 { color: #ffffff; font-size: 2.0em; }
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
  table { font-size: 0.70em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.86em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 0.62em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.82em; }
footer: '謝慕揚 MD, PhD, FESC | AI-ECG for HCM Detection | 2026'
---

<!-- _class: lead -->
# AI 偵測肥厚性心肌病變
## Artificial Intelligence for the Detection of Hypertrophic Cardiomyopathy From Standard ECG
**謝慕揚 MD, PhD, FESC** | 2026-06-20
Park J, et al. *JACC Advances* 2026;5(7):102914
[原文連結 — https://doi.org/10.1016/j.jacadv.2026.102914](https://doi.org/10.1016/j.jacadv.2026.102914)

---

# 一句話總結

> FDA 核准的 AI-ECG 演算法 (**Viz HCM**)，以 **cMRI 為金標準**驗證，偵測 HCM 達 **特異度 100%、PPV 100%、AUC 0.946**，但**敏感度僅 58%**——這是追求高特異度的「刻意取捨」。

- **本質**：高度可信的「**rule-in**」工具（有就幾乎一定是），而非「rule-out」。
- **最大亮點**：比臨床診斷**中位提早 2.6 年**抓到未察覺的 HCM。
- **最易被抓**：心尖肥厚型 (apical HCM)，校正後 OR **4.71**。

---

# 臨床問題：HCM 的「診斷落差」

- HCM 最常見的遺傳性心肌病變，盛行率 **0.2%（1/500）**，全球約 **2,000 萬人**。
- 卻**長期被低估診斷**：美國未診斷者高達 **85%**，診斷延遲可達 2 年。
- 早診斷 → 及早給 cardiac myosin inhibitor、猝死預防。

> **既有 AI-ECG 研究的致命弱點**：多以 ICD 碼或 echo 當 ground truth。HCM 的 ICD 碼錯誤分類率達 **1/3**，PPV 低至 **68%**，常混入高血壓性心臟病、主動脈瓣狹窄。

**本研究創新 → 以 cMRI + 醫師逐案判讀為金標準**

---

# 研究方法 (Methods)

- **單中心、回溯性**：Cedars-Sinai，2010–2023；ICD-10 42.1/42.2 篩出 314 人。
- **HCM 確診**：cMRI + 醫師判讀，MWT ≥15 mm（或 ≥13 mm + 家族史/基因）。
- **對照組**：83 位 cMRI 確認無心肌病者。

| AI 演算法 Viz HCM | 內容 |
|------|------|
| 法規 | **FDA 核准 (DEN230003)** |
| 訓練資料 | 831,329 ECG / 301,106 病人 |
| 架構 | 影像式 ECG → CNN → 機率 0–1 |
| **操作閾值** | **0.84**（調高以追求高特異度） |

最終分析：**150 HCM + 83 對照 = 233 人**，平均 56 歲、62% 男性。

---

# 主要結果：診斷效能

> **AUC 0.946 (95% CI 0.916–0.970)** — 鑑別力極佳

| 指標 | 數值 (95% CI) | 解讀 |
|------|---------------|------|
| 敏感度 | **58%** (50.0–65.6%) | 150 位中抓到 87 位 |
| 特異度 | **100%** (95.6–100%) | 83 位對照全數正確 |
| PPV | **100%** (95.8–100%) | **零偽陽性** |
| NPV | 57% | 「陰性」無法排除 HCM |

- HCM 組 vs 對照：MWT **18.0 vs 10.0 mm**、有 LGE **77% vs 0%**、基因突變 **49% vs 1%**。

---

<!-- _class: divider -->
# 誰會被抓到？
## 正確偵測 vs 漏診的預測因子

---

# True Positive vs False Negative (Table 2)

| 變項 | True Positive (87) | False Negative (63) | P |
|------|------|------|---|
| 年齡 | 60 | 66 | 0.030 |
| 男性 | **72%** | 52% | 0.012 |
| 肥厚型態 | — | — | **0.007** |
| ├ 中膈 septal | 68% | **87%** | |
| ├ 心尖 apical | **28%** | 8% | |
| MWT (mm) | 19.0 | 18.0 | NS |
| 有 LGE | 80% | 73% | NS |
| 高臨床風險 | 23% | 24% | NS |

> **關鍵陰性發現**：MWT、LGE、猝死高風險在 TP/FN 間**無差異**——影像表型嚴重度**不必然**轉化為 ECG 可偵測的訊號。

---

# 多變項分析：唯一顯著因子 = 心尖型

| 預測因子 | 單變項 OR (P) | 多變項 OR (P) |
|----------|----------------|----------------|
| 男性 | 2.39 (0.012) | 1.80 (0.127) |
| MRI 最大室壁厚度 | 1.10 (0.033) | 1.09 (0.069) |
| **心尖亞型 (apical)** | **4.48 (0.004)** | **4.71 (0.005)** ✅ |

> **心尖 HCM (Yamaguchi syndrome)** 常伴巨大倒 T 波 (giant T-wave inversion)，是 AI 最容易學到的特徵。中膈型、女性、ECG 變化不明顯者較易被漏掉。

校正後 OR 4.71（95% CI 1.71–15.48）— 是唯一在多變項模型中仍顯著的預測因子。

---

# 時間軸：能提早多久診斷？

```text
57 位 HCM 在 cMRI 前已有 AI-positive ECG
        ▼
28 位在 cMRI 前 ≥1 年就有陽性 ECG
        ▼
9 位 (32%) 最早陽性旗標時尚未被臨床診斷
   └ 其中 4 位已具高猝死風險特徵
        ▼
中位 lead-time = 2.6 年 (IQR 1.1–5.3)
```

> AI-ECG 有潛力在臨床診斷前**數年**標記未察覺的 HCM，爭取及早確診、HCM 專屬治療與猝死預防的時間窗。AI 機率分數跨年度維持穩定分層（對照<偽陰性<真陽性，P<0.001）。

---

# 討論：為何敏感度只有 58%？

- 統合分析 (Queiroz) 顯示 CNN-ECG 整合敏感度/特異度約 **89%/88%**。
- 本研究刻意把操作點調高 (0.84) → **極高特異度、犧牲敏感度**。

> **低盛行率疾病的篩檢邏輯**：HCM 盛行率僅 0.2–1.4%。即使偽陽性率低，大規模篩檢時少量偽陽性也會**壓垮臨床量能**（多餘的 cMRI、會診、成本）。作者主張：對 all-comers，可靠的「**rule-in**」比高敏感度的「rule-out」更實用。

**cMRI 金標準** = 本研究最大強項：克服 ICD 碼/echo 的高錯誤分類（達 1/3）。

---

# 研究限制 (Limitations)

- **單中心、回溯性、對照組小 (n=83)**，外推性受限。
- **對照組「太乾淨」**：皆為 cMRI 確認無心肌病者，未挑戰 phenocopy（高血壓性心臟病、基因型陽性表型陰性）→ **真實世界特異度恐較低**。
- **選擇偏差**：ICD 碼選入 + 做 cMRI 的族群，表型可能較進展。
- **刻意優化高特異度** → 敏感度僅 58%，漏掉部分 HCM。
- 無法做特徵層級解釋（GradCAM）。

---

# 臨床啟示與我的觀點

1. **這是 rule-in、不是 rule-out**：AI 標記「疑似 HCM」轉介 cMRI 的訊號很強（零偽陽性）；但 AI「陰性」**不能**排除 HCM（NPV 僅 57%）。
2. **心尖型最易被抓 (OR 4.71)**；中膈型、女性、影像重但 ECG 變化不明顯者**易被漏**——仍需臨床警覺與影像。
3. **Lead-time 2.6 年**：整合進 EHR / 心電圖室自動判讀，可作被動式早期警報。
4. **落地提醒**：對照組過於理想化，真實門診混入 phenocopy 時特異度恐不如 100%——應搭配臨床情境與影像確認，勿單以 ECG 下診斷。

---

<!-- _class: small-text -->
# 參考文獻（精選）

1. Park J, et al. Artificial Intelligence for the Detection of HCM From Standard ECG. [*JACC Adv*. 2026;5(7):102914.](https://doi.org/10.1016/j.jacadv.2026.102914)
2. Ko WY, Siontis KC, Attia ZI, et al. Detection of HCM using a CNN-enabled ECG. [*J Am Coll Cardiol*. 2020;75(7):722-733.](https://doi.org/10.1016/j.jacc.2019.12.030)
3. Desai MY, et al. Real-World AI-based ECG analysis to diagnose HCM. [*JACC Clin Electrophysiol*. 2025;11(6):1324-1333.](https://doi.org/10.1016/j.jacep.2025.02.024)
4. Queiroz I, et al. Systematic review and meta-analysis on CNN ECGs in HCM diagnosis. [*J Electrocardiol*. 2025;89:153888.](https://doi.org/10.1016/j.jelectrocard.2025.153888)
5. Ommen SR, et al. 2024 AHA/ACC/... guideline for the management of HCM. [*J Am Coll Cardiol*. 2024;83(23):2324-2405.](https://doi.org/10.1016/j.jacc.2024.02.014)
6. Hughes MK, et al. Accurate diagnosis of apical HCM using explainable advanced ECG analysis. [*EP Europace*. 2024;26(4):93.](https://doi.org/10.1093/europace/euae093)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC**
AI-ECG for HCM Detection | JACC Advances 2026
