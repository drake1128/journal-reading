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
  section.lead h1 { color: #ffffff; font-size: 2.0em; border-bottom: none; }
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
  section.divider h1 { color: #ffffff; border-bottom: none; font-size: 2.4em; text-align: center; }
  section.divider h2 { color: #ffffff; font-size: 1.4em; text-align: center; font-weight: bold; }
  section.divider h3 { color: #ffe082; font-size: 1.1em; text-align: center; font-weight: normal; }
  section.divider p, section.divider strong { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  a { color: #0072bc; }
  table { font-size: 0.70em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 5px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.88em;
  }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.66em; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.78em; }
footer: '謝慕揚 MD, PhD, FESC | ASPIRED 昏厥心電圖監測 | 2026'
---

<!-- _class: lead -->
# 昏厥後立即行動式心電圖監測
## ASPIRED — Immediate Ambulatory ECG Monitoring in Syncope
### N Engl J Med 2026 · 英國 45 家醫院 · 2234 人

**謝慕揚 MD, PhD, FESC**

[原文連結：doi.org/10.1056/NEJMoa2605812](https://doi.org/10.1056/NEJMoa2605812)

> 主要終點**中性**：診斷變多，昏厥沒有變少

---

# 一句話總結

急診評估後仍**原因不明的昏厥**病人，立即戴 **14 天行動式心電圖貼片**：

| 1 年病人自述昏厥次數 | 介入組 | 標準照護 |
|---|---|---|
| 平均次數 | **1.37 ± 5.10** | **1.58 ± 8.56** |

**IRR 0.89（95% CI 0.68–1.18），P = 0.42 → 中性**

但：心律不整診斷率 **22.0% vs 9.0%**、診斷時間 **22 天 vs 54.5 天**
1 年全因死亡 **1.5% vs 2.9%（OR 0.50, 0.27–0.93）**

---

# 臨床背景：昏厥的兩難

- 英國每年約 **65 萬**、美國約 **120 萬**人次因昏厥就診急診
- **約 50%** 急診評估後找不到原因；其中約 **7%** 一個月內查出重要病理
- 昏厥 1 年復發率約 **50%**；**找到心律不整並治療後降到約 10%**

```text
診斷心律不整性昏厥 = 症狀與心電圖必須同時被抓到
        ↓
傳統監測（住院 telemetry、24–48 小時 Holter）診斷率低
        ↓
大量病人被收住院觀察 → 成本高，近一半仍無診斷就出院
```

> 假說：**急診當下就戴上 14 天貼片，及早診斷治療 → 昏厥應該會變少**

---

<!-- _class: divider -->
# 試驗設計
## 英國 NHS 45 家醫院 · 開放標籤優越性試驗

---

# 試驗設計

| 項目 | 內容 |
|------|------|
| 設計 | 開放標籤、隨機 1:1、**優越性**試驗 |
| 地點／期間 | 英國 NHS 45 家醫院；2022/07 – 2024/06 |
| 對象 | ≥ 16 歲，急診初步評估後**仍原因不明**的昏厥 |
| 隨機時機 | 到急診後 **72 小時內** |
| 裝置 | BodyGuardian Mini（Boston Scientific）；廠商僅提供裝置 |
| 主要終點 | **1 年內病人自述的昏厥次數** |
| 追蹤 | 每 4 週簡訊／email 詢問，共 2 年 + 電子病歷連結 |
| 資金 | British Heart Foundation、NHS Research Scotland |

> **設計亮點**：只收「原本沒有在急診出院時常規做心電圖監測」的醫院——確保對照組真的是標準照護。

---

# 樣本數估算的假設（值得回頭檢討）

```text
假設 標準照護組 1 年復發率      42.5%
     介入組心律不整檢出率        10.5%
     對照組心律不整檢出率         2.0%
        ↓
推得兩組復發率 33.1% vs 40.7%（IRR 0.81）
        ↓
保守設定為偵測 34% vs 40%（IRR 0.85）
90% power，每組 1064 人 → 加計 5% 失聯 → 每組 1117 人
```

> **後見之明**：實際復發率只有約 **28%**，遠低於假設的 42.5% → **統計效力被削弱**。

---

# 收案流程與追蹤完整度

篩選 **6260 人** → 隨機分派 **2234 人**（介入 1122 / 標準照護 1111）

| 情況 | 人數 |
|------|------|
| 1 年時退出試驗 | 165 (7.4%) |
| 停止回覆 4 週問卷但完成 1 年問卷 | 88 |
| 停止回覆所有問卷但同意病歷連結 | 244 |
| **完全無主要終點資料** | **264 (11.8%)** |
| **納入主要分析** | **1970 (88.2%)**（1004 / 966） |

---

# 基線特徵（兩組平衡）

| 特徵 | 介入組 (n=1122) | 標準照護 (n=1111) |
|------|-----------------|-------------------|
| 年齡 | 58.3 ± 19.8 歲 | 58.3 ± 19.7 歲 |
| 男性 | 52.9% | 51.3% |
| 曾有昏厥病史 | 46.7% | 43.8% |
| 過去 1 年 > 1 次昏厥 | 24.8% | 23.6% |
| 冠心病 | 8.5% | 7.9% |
| 心房顫動／撲動 | 8.7% | 7.7% |
| 有前驅症狀 | 39.9% | 40.7% |
| 昏厥前心悸 | 9.8% | 9.6% |

---

# 裝置實際使用 — 真實世界的殘酷

| 指標 | 數值 |
|------|------|
| 有可判讀 ECG 紀錄 | **930/1122 (82.9%)** |
| **未戴或未歸還裝置** | **192 人 (17.1%)** |
| 平均配戴時間 | 11.7 ± 3.1 天 |
| 達預設遵從性（≥ 7 天） | 825/926 (89.1%) |
| 平均可分析時間 | 10.9 ± 3.5 天 |

> **17% 根本沒戴或沒還**。任何要導入這種流程的醫院，都要先把「裝置回收」設計進去。

---

<!-- _class: divider -->
# 結果
## 主要終點中性，次要終點很吵

---

# 主要終點：中性

| 主要終點 | 介入組 | 標準照護 | IRR (95% CI) | P |
|----------|--------|----------|--------------|---|
| **1 年自述昏厥次數** | **1.37 ± 5.10** | **1.58 ± 8.56** | **0.89 (0.68–1.18)** | **0.42** |

所有預設敏感度分析結果一致（多重插補、把死亡當昏厥事件、排除離群值）。

| 其他昏厥終點 | 介入組 | 標準照護 | 效果量 |
|------|------|------|------|
| 病歷紀錄昏厥次數 | 0.22 ± 0.64 | 0.25 ± 0.82 | IRR 0.90 (0.71–1.15) |
| **1 年昏厥復發率** | 27.9% | 28.6% | OR 0.97 (0.79–1.17) |
| 首次住院天數 | 1.3 天 | 1.4 天 | 0.91 (0.76–1.08) |

---

# 診斷：這才是介入真正做到的事

| 終點 | 介入組 | 標準照護 | OR (95% CI) |
|------|--------|----------|-------------|
| **臨床重要心律不整（1 年）** | **22.0%** | **9.0%** | **2.95 (2.28–3.81)** |
| 有症狀的心律不整 | 9.3% | 5.9% | 1.66 (1.20–2.31) |
| **診斷時間中位數** | **22.0 天** | **54.5 天** | 0.35 (0.28–0.44) |

**Number needed to monitor ≈ 7**（每監測 7 人多找到 1 個臨床重要心律不整）

---

# 各類嚴重心律不整

| 心律不整 | 介入組 | 標準照護 | OR (95% CI) |
|----------|--------|----------|-------------|
| 持續性 VT | 1.5% | 0.6% | 2.67 (1.04–6.86) |
| **非持續性 VT** | **10.0%** | **1.2%** | **9.50 (5.29–17.06)** |
| 完全性房室阻斷 | 1.0% | 0.7% | 1.36 (0.55–3.41) |
| Mobitz II 二度房室阻斷 | 1.2% | 0.6% | 1.85 (0.73–4.65) |
| **停搏 ≥ 6 秒** | **2.7%** | **1.2%** | **2.32 (1.20–4.48)** |
| 心搏過緩 < 40 bpm | 1.7% | 0.7% | 2.37 (1.02–5.49) |

> nsVT 增加 9.5 倍主要反映**監測時間本身** — 這是延長監測的「診斷通膨」。

---

# 治療與後續檢查

| 介入 | 介入組 | 標準照護 | OR (95% CI) |
|------|--------|----------|-------------|
| 開始抗心律不整藥 | 10.8% | 7.3% | 1.47 (1.11–1.95) |
| **植入永久節律器** | **6.8%** | **4.6%** | **1.49 (1.04–2.13)** |
| 電燒 | 0.5% | 0.4% | 1.24 (0.33–4.64) |
| 植入 ICD | 0.6% | 0.4% | 1.74 (0.51–5.97) |
| **短期監測器使用數** | **0.29** | **0.40** | IRR 0.72 (0.63–0.84) |
| 植入式事件記錄器 (ILR) | 7.5% | 7.6% | 0.96 (0.70–1.33) |
| 心臟超音波 | 39.7% | 35.6% | 1.21 (1.01–1.44) |

> 早期貼片**取代了重複的短期 Holter，但沒有取代 ILR**。

---

# 為什麼診斷變多、治療變多，昏厥卻沒變少？

1. **昏厥本質是多因素的** — 即使介入組也只有 **22%** 找到心律不整；其餘血管迷走性、姿勢性低血壓，不是節律導向治療能處理的

2. **注意力效應 (attention effect)** — 戴著監測器的人對症狀更敏感，**回報更多事件**，直接稀釋主觀主要終點

3. **實際復發率低於預期**（28% vs 假設 42.5%）→ 效力被削弱

> **教科書級案例：過程指標改善 ≠ 病人為中心的結果改善。**
> 主要終點是由 **PPI（病人與公眾參與）** 選定的——他們在意「我還會不會暈倒」。

---

# 那個死亡率訊號怎麼看？

| 1 年全因死亡 | 介入組 | 標準照護 | OR (95% CI) |
|---|---|---|---|
| | **1.5%**（16/1095） | **2.9%**（31/1085） | **0.50 (0.27–0.93)** |

**支持它是真的**：KM 曲線持續分離；有機轉路徑（節律器 6.8% vs 4.6%，高度房室阻斷植入節律器是 **class I**）

**要保守的理由**：**次要終點、未校正多重比較**；絕對差只有 15 人；抗心律不整藥從未被證實改善存活

> 作者自己寫「**should be interpreted cautiously**」。
> **REMOSYNCED 試驗（NCT05066347）**可能提供外部驗證。

---

# 可行性與病人接受度

| 病人回饋 | 比例 |
|----------|------|
| 容易使用 | 91.3% |
| 舒適 | 73.3% |
| 願意再次使用 | 82.5% |
| 日常活動不受限 | 91.9% |

**診斷效率**：偵測到心律不整平均需 **5.4 ± 4.1 天**

- **71.6%（131/183）在 7 天內抓到**
- **28.4%（52 例）在第 2 週才出現**

> 只做 7 天，會漏掉約 **28%** 的診斷。

---

# 限制

1. **開放標籤** → performance bias（但兩組追蹤強度、住院天數、回診、檢查相近）
2. **主要終點主觀且病人自述** → 偵測／回報偏差；客觀次要終點較穩健
3. **實際復發率低於預期**（28% vs 42.5%）→ 效力下降
4. **17% 裝置未戴／未歸還** → 稀釋介入效果
5. 少數高頻復發個案影響主要終點
6. 死亡率是次要終點，**未校正多重比較**
7. 英國 NHS 情境；台灣給付、器材可近性與轉診習慣不同

---

<!-- _class: divider -->
# 臨床應用
## 改變什麼、不改變什麼

---

# ASPIRED 改變什麼、不改變什麼

| 問題 | 答案 |
|------|------|
| 減少昏厥復發？ | **不能**（主要終點中性） |
| 更快、更多抓到心律不整？ | **能**（22.0% vs 9.0%；22 天 vs 54.5 天） |
| 減少重複做 Holter？ | **能**（IRR 0.72） |
| 取代 ILR？ | **不能**（兩組都約 7.5%） |
| 減少住院天數？ | **不能**（1.3 vs 1.4 天） |
| 降低死亡率？ | **可能**，但證據等級不足以改流程 |

---

# 實務建議

1. **要說服醫院導入，理由是「更快診斷、減少重複檢查」**，不是「減少昏厥復發」
2. **14 天優於 7 天**：28% 的診斷出現在第 2 週
3. **裝置回收流程必須先設計好**：17% 未戴／未還就是白花的成本
4. **不要因為多抓到 nsVT 就過度治療**：要回到臨床脈絡判讀
5. **高風險特徵仍優先**（結構性心臟病、心悸後昏厥、運動中昏厥、家族猝死史）——貼片不取代臨床判斷

---

# Clinical Pearls

> **Pearl 1**：**診斷率提升 ≠ 病人結果改善**。診斷率翻 2.4 倍，昏厥復發一模一樣（27.9% vs 28.6%）。

> **Pearl 2**：昏厥復發的主因不是心律不整——密集監測也只有 **22%** 找得到節律問題。

> **Pearl 3**：**第 2 週抓到 28% 的診斷**。要做就做滿 14 天。

> **Pearl 4**：死亡率 OR 0.50 很吸引人，但那是**未校正多重比較的次要終點**——可以寫研究計畫，不適合改流程。

---

<!-- _class: small-text -->
# 參考文獻

1. Reed MJ, Goodacre S, Weir CJ, et al. Immediate Ambulatory Electrocardiographic Monitoring in Syncope (ASPIRED). [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2605812)
2. Brignole M, Moya A, de Lange FJ, et al. 2018 ESC guidelines for the diagnosis and management of syncope. [*Eur Heart J*. 2018;39:1883-1948.](https://doi.org/10.1093/eurheartj/ehy037)
3. Reed MJ, Newby DE, Coull AJ, Prescott RJ, Jacques KG, Gray AJ. The ROSE (Risk Stratification of Syncope in the Emergency Department) study. [*J Am Coll Cardiol*. 2010;55:713-21.](https://doi.org/10.1016/j.jacc.2009.09.049)
4. Thiruganasambandamoorthy V, Rowe BH, Sivilotti MLA, et al. Duration of electrocardiographic monitoring of emergency department patients with syncope. [*Circulation*. 2019;139:1396-1406.](https://doi.org/10.1161/CIRCULATIONAHA.118.036088)
5. Locati ET, Moya A, Oliveira M, et al. External prolonged electrocardiogram monitoring in unexplained syncope and palpitations (SYNARR-Flash). [*Europace*. 2016;18:1265-72.](https://doi.org/10.1093/europace/euv311)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

[ASPIRED — N Engl J Med 2026](https://doi.org/10.1056/NEJMoa2605812)
