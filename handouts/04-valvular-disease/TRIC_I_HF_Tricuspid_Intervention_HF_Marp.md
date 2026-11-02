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
  section.lead h2 { color: #b0c4de; font-size: 34px; }
  section.lead h3 { color: #dfe6e9; font-size: 28px; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #b0c4de; }
  section.lead blockquote { color: #2d3436; background-color: #fff5f5; }
  section.lead blockquote p { color: #2d3436; }
  section.lead blockquote strong { color: #ba181b; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 { color: white; border-bottom: none; font-size: 56px; text-align: center; }
  section.divider h2 { color: #ffe066; font-size: 34px; text-align: center; }
  section.divider h3 { color: #ffffff; font-size: 28px; text-align: center; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 40px; }
  h2 { color: #0072bc; font-size: 32px; }
  h3 { color: #555555; font-size: 28px; }
  table { font-size: 27px; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 12px; }
  th strong { color: #ffe066; }
  td { padding: 5px 12px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 27px;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 24px;
    line-height: 1.35;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 15px; }
  ul, ol { line-height: 1.45; }
footer: '謝慕揚 MD, PhD, FESC | TRIC-I-HF 三尖瓣介入治療於心衰竭 | 2026'
---

<!-- _class: lead -->
# 三尖瓣介入治療於心衰竭
## TRIC-I-HF — Tricuspid-Valve Intervention in Heart Failure
### N Engl J Med 2026;395:1363-73

**謝慕揚 MD, PhD, FESC**

[原文連結：doi.org/10.1056/NEJMoa2606934](https://doi.org/10.1056/NEJMoa2606934)

> **第一個**證明 T-TEER 能降低「死亡或心衰竭住院」硬終點的隨機試驗

---

# 一句話總結

**症狀性重度 TR + 心衰竭事件高風險**，T-TEER + 藥物 vs 藥物：

| 終點 | 結果 |
|---|---|
| 1 年階層式複合（死亡→HFH→KCCQ） | **Win ratio 2.42**（1.76–3.33） |
| 3 年死亡或心衰竭住院 | **52.4% vs 21.0% 事件免除** |
| | **HR 0.40**（0.29–0.55） |
| 30 天主要不良事件 | **5.9%** |

> 好處**主要來自減少心衰竭住院**；死亡率 1 年不顯著，3 年才顯著

---

# 臨床背景：前兩個 RCT 看不到硬終點

| 試驗 | 結果 |
|---|---|
| **TRILUMINATE Pivotal**（NEJM 2023） | WR 1.48，**完全由 KCCQ 驅動** |
| **Tri.Fr**（JAMA 2025） | 複合評分改善，**由病人自評驅動** |
| TRILUMINATE 2 年（Circ 2025） | HFH 年化率 0.19 vs 0.26；死亡無差異 |

共同問題：**事件率太低**

- TRILUMINATE 藥物組 1 年死亡率 **8%**
- Tri.Fr 藥物組 1 年死亡率 **5.4%**

> 若 T-TEER 真能減少心衰竭事件，就該在**本來就會頻繁發生事件**的病人身上測試

---

<!-- _class: divider -->
# 試驗設計
## 德國 29 家高手術量中心 · 360 人 · 2:1 開放標籤策略試驗

---

# 試驗設計

| 項目 | 內容 |
|---|---|
| 設計 | 研究者發起、多中心、**開放標籤**、隨機、**策略試驗** |
| 地點 | **德國 29 家**心臟瓣膜中心 |
| 中心經驗 | 啟動前平均 **176 ± 163 例** T-TEER |
| 收案 | 2022/03 – 2025/06 |
| 分派 | **2:1**；修補組 237 / 藥物組 123 |
| 介入時機 | 隨機後 **14 天內** |
| 器械 | 任何 CE 認證：**PASCAL、TriClip、Cardioband** |
| 經費 | DZHK、LMU、Edwards 無限制研究經費 |

---

# 收案條件：全篇最關鍵的一段

```text
1. 至少「重度」TR（五級量表）
2. 最適藥物治療（含利尿劑）≥ 30 天仍有症狀
3. 心衰竭事件高風險（至少一項）：
   a. 過去 12 個月心衰竭失代償
   b. 心腎症候群：持續 eGFR < 60
   c. 心肝症候群：bilirubin / ALP / γ-GT 三項 ≥ 2 項升高
4. 全部病人術前右心導管，依血行動力學切點篩選
```

> 第 3 項是 **2023 年 7 月中途加入**計畫書——研究者刻意轉向更重的病人

---

# 兩個主要終點，依序檢定

```text
第一主要終點（1 年）— 階層式複合，win ratio
    第 1 層：全因死亡
    第 2 層：心衰竭住院
    第 3 層：KCCQ 改善 ≥ 15 分
        │ 顯著 →
        ▼
第二主要終點（至 3 年）
    全因死亡或心衰竭住院（time-to-event）
```

- Finkelstein–Schoenfeld 法：237 × 123 = **29,151 對**病人配對
- 樣本數：WR 1.818 → 336 人（85% power）；目標 **360 人**

---

# 交叉治療的規定

藥物組要交叉接受介入，必須**同時**符合：

1. 隨機分派後 ≥ 30 天
2. 心衰竭失代償**導致住院**
3. 該次住院**使用靜脈利尿劑**

> 交叉只能在**已發生一次主要終點事件之後**
> → 主要終點分析不受影響
> → 但次要終點（死亡、功能、超音波）會被**稀釋**

---

<!-- _class: divider -->
# 病人族群
## 80 歲 · 八成心腎症候群 · 近半心肝症候群 · LVEF 保留

---

# 這是一群「右心衰竭」的病人

| 特徵 | 修補組 (237) | 藥物組 (123) |
|---|---|---|
| 年齡 | 80.6 ± 5.9 | 80.2 ± 6.6 |
| NYHA III/IV | 76.4% | 72.4% |
| 過去 12 個月 HFH | 57.0% | 51.2% |
| **心腎症候群** | **81.9%** | **81.3%** |
| **心肝症候群** | **44.2%** | **50.0%** |
| 心房顫動／撲動 | 92.0% | 97.6% |
| NT-proBNP 中位數 | 2022 | 2076 |

---

# 超音波、血行動力學與藥物

| 參數 | 全體 |
|---|---|
| TR 嚴重度 | 重度 50.8%、massive 34.2%、torrential 10.3% |
| **LVEF** | **54.3 ± 8.6%** |
| TAPSE 中位數 | 19.1 vs 18.0 mm |
| RV FAC 中位數 | 37.1% vs 36.4% |
| 迴路利尿劑 | **94.2%**（中位 80 mg/日） |
| SGLT2i / MRA | 52.2% / 43.1% |

> **右心衰竭已出現，但 RV 功能尚可**——T-TEER 理論上最可能受益的窗口

---

# 手術實況

修補組 237 人中 **231 人**實際接受介入：

| 術式 | 人數 (%) |
|---|---|
| **T-TEER** | **227 (98.3%)** |
| Cardioband 瓣環成形 | 3 (1.3%) |
| 經導管瓣膜置換（違反計畫書） | 1 (0.4%) |

T-TEER 器械：**PASCAL 149 (65.6%)**、TriClip 75 (33.0%)

植入數：1 個 28.6%、**2 個 62.1%**、≥ 3 個 9.4%

> **七成以上需要 ≥ 2 個器械**——術前規劃要預留

---

<!-- _class: divider -->
# 結果
## Win ratio 2.42 · 3 年 HR 0.40 · NNT 4

---

# 第一主要終點：1 年 Win Ratio

| 階層 | 修補組勝 | 藥物組勝 |
|---|---|---|
| 第 1 層：全因死亡 | 15.0% | 10.9% |
| 第 2 層：**心衰竭住院** | **31.8%** | 9.8% |
| 第 3 層：KCCQ ≥ 15 分 | 11.2% | 3.2% |
| **總計** | **58.0%**（16,909 對） | **23.9%**（6,966 對） |

**Win ratio 2.42（95% CI 1.76–3.33；P < 0.001）**

> 三層每一層都是修補組贏——但**心衰竭住院貢獻最大**（勝差 22.0 個百分點）

---

# 第二主要終點：3 年死亡或心衰竭住院

| 時間 | 修補組免除率 | 藥物組免除率 |
|---|---|---|
| 1 年 | 73.9% | 48.4% |
| **3 年** | **52.4%** (43.2–63.6) | **21.0%** (12.7–34.6) |

**HR 0.40（95% CI 0.29–0.55；P < 0.001）**

事件：79 人 (33.3%) vs 76 人 (61.8%)

> 事後分析：1 年內預防一例死亡或 HFH 的 **NNT = 4**（95% CI 3–6）

---

# 個別成分（次要終點，未校正多重比較）

| 終點 | 修補組 | 藥物組 | HR (95% CI) |
|---|---|---|---|
| 1 年存活 | 86.5% | 82.5% | 0.74 (0.42–1.29) |
| **3 年存活** | **72.3%** | **53.9%** | **0.62 (0.40–0.96)** |
| 1 年免於 HFH | 79.6% | 51.3% | 0.35 (0.25–0.50) |
| 3 年免於 HFH | 62.4% | 31.0% | 0.35 (0.25–0.51) |

> **死亡率 1 年不顯著、3 年才顯著**——而 3 年追蹤只完成 **20.5%**

---

# 超音波、功能與生活品質

| 終點 | 修補組 | 藥物組 | 效應值 |
|---|---|---|---|
| 30 天 TR ≤ moderate | **70.3%** | 29.6% | — |
| 1 年 TR ≤ mild | **56.3%** | 19.2% | — |
| 1 年 NYHA I/II | **73.8%** | 57.0% | OR 2.13 (1.24–3.64) |
| KCCQ 變化（分） | +11.2 | +4.3 | 差 6.9 (1.8–12.0) |
| 6 分鐘步行 (m) | +40 | +20 | 差 20 (−0.1–40.1) |

> 藥物組數字**包含交叉病人**，組間差距被低估；KCCQ 差 6.9 分**低於 15 分門檻**

---

# 安全性與交叉治療

**30 天安全性**（n = 237）

| 事件 | 人數 (%) |
|---|---|
| 主要不良事件 | **14 (5.9%)** |
| 死亡 | 1（第 17 天，非心因性） |
| 單葉器械附著 (SLDA) | 4 (1.7%) |

**交叉**：藥物組 **48 / 123 (39%)** 接受介入
其中 **28 人 (58%) 在構成終點事件的那次住院期間**手術

> 真正的問題和 EASE 一樣：**「現在做，還是等出事再做？」**

---

<!-- _class: divider -->
# 解讀
## 為什麼這次看到硬終點？

---

# 原因一：病人更重

| 指標 | **TRIC-I-HF** | TRILUMINATE | Tri.Fr |
|---|---|---|---|
| 過去 1 年 HFH | **55.0%** | 23.8% | 40.3% |
| NYHA III/IV | **75.0%** | 55.1% | 42.3% |
| **藥物組 1 年死亡率** | **17.5%** | 8% | 5.4% |

> 藥物組 1 年死亡率是 TRILUMINATE 的 **2 倍**、Tri.Fr 的 **3 倍**
> **事件夠多，才有機會證明差異**

---

# 原因二、三：術者經驗與病人選擇

**量能–結果關係**

- 三尖瓣解剖變異大、瓣葉薄、coaptation gap 大、術中影像困難
- PASTE 註冊：中心年量 **≥ 21 例**，成功率顯著較高
- TRIC-I-HF 29 個中心啟動前平均 **176 例**

**病人選擇**

- 術前必做右心導管，排除可能無效的病人
- 心腎、心肝症候群：知道「誰再等下去會出事」

> 作者沒明說的第四點：2:1 + 允許交叉 → 藥物組其實是「**延遲介入組**」

---

<!-- _class: divider -->
# 方法學深度比較
## TRIC-I-HF vs TRILUMINATE Pivotal（Sorajja, NEJM 2023）

---

# 不同的問題，不同的設計

| 面向 | TRILUMINATE Pivotal | **TRIC-I-HF** |
|---|---|---|
| 性質 | **廠商主導器械核准試驗**（Abbott IDE） | **研究者發起策略試驗**（DZHK） |
| 問題 | TriClip **安不安全、有沒有效**？ | 高風險病人**該不該早做**？ |
| 器械 | 單一 TriClip G4 | PASCAL 66% / TriClip 33% / Cardioband |
| 群組 | 隨機 + **單臂組**（複雜解剖）+ roll-in | 單純隨機 |
| 中心 | 65 中心（美加歐），允許新手中心 | 29 德國中心，平均 **176 例** |

> 器械試驗要證明「可夾、安全」；策略試驗要回答「該不該早做」

---

# 病人篩選流程

| 面向 | TRILUMINATE Pivotal | **TRIC-I-HF** |
|---|---|---|
| 資格審查 | **中央資格委員會**：OMT、**可夾性**、分組 | **各中心心臟團隊**；不需中央審核 |
| TR 確認 | 核心實驗室**事先**確認 + TEE | 核心實驗室事後判讀 |
| 手術風險 | 外科醫師同意 **≥ intermediate** | **無要求** |
| **高風險富集** | **無** | **HFH 1 年內 / 心腎 / 心肝** |
| 右心導管 | 非必做（排除 sPAP > 70） | **全員必做**，依切點篩選 |

---

# 排除條件的邏輯不同

**TRILUMINATE：「夾不夾得到、夾了安不安全」**

- coaptation gap > 2 cm、抓取區鈣化、CIED 導線妨礙
- sPAP > 70 mmHg 或固定型 precapillary 肺高壓
- LVEF ≤ 20%、三尖瓣狹窄、TTE + TEE 無法評估
- **慢性透析**、預期壽命 < 12 個月

**TRIC-I-HF：「介入會不會太晚、太無效」**

- 全員右心導管，依血行動力學切點排除 futility
- **腎功能異常反而是納入條件**（eGFR < 60 = 心腎症候群）

> 一個把腎衰竭排除在外，一個把腎功能異常收進來

---

# 隨機、盲法與交叉

| 面向 | TRILUMINATE Pivotal | **TRIC-I-HF** |
|---|---|---|
| 隨機 | **1:1**；依中心分層 | **2:1**；依中心 + TR 嚴重度分層 |
| 盲法 | 開放標籤，**評估者盲化** | 開放標籤；未提評估者盲化 |
| **交叉** | **12 個月追蹤完成後**（2 年 61.5%） | **只在終點事件後**（1 年 39%） |

> TRILUMINATE：1 年比較乾淨、長期硬終點不可比
> TRIC-I-HF：主要終點乾淨、1 年次要終點被稀釋

---

# 終點階層的差異

| 階層 | TRILUMINATE Pivotal | **TRIC-I-HF** |
|---|---|---|
| 第 1 層 | **死亡 或 三尖瓣手術** | **全因死亡** |
| 第 2 層 | 心衰竭住院（次數） | 心衰竭住院 |
| 第 3 層 | KCCQ ≥ 15 分 | KCCQ ≥ 15 分 |
| 第二主要終點 | 無；以 powered secondary 支撐 labeling | **死亡或 HFH 至 3 年** |
| 30 天 MAE | **1.7%**（定義：CV 死亡、腎衰竭、手術） | **5.9%**（定義不同，不能並列） |

> TRILUMINATE 第 1 層幾乎全平手（90.6% vs 89.4%），勝負落到 KCCQ
> TRIC-I-HF 第 2 層 HFH 就決定大部分勝負（勝差 22 個百分點）

---

# 統計設計與樣本數

| 面向 | TRILUMINATE Pivotal | **TRIC-I-HF** |
|---|---|---|
| 樣本數 | 計畫約 450；**適應性設計 + 樣本數重估** | **固定 360**（WR 1.818、85% power） |
| 主要分析時機 | **首 350 人**完成 12 個月即分析 | 最後一人完成 12 個月 |
| 最終隨機人數 | **572** | 360 |
| 追蹤 | 5 年 | 3 年（3 年完成 20.5%） |

> 後續 222 人 HFH 年化率 0.09 vs 0.20，與前 350 人不同 → 「哪群人才是結果」不易回答

---

# 兩個試驗實際收到的病人

| 基線特徵 | TRILUMINATE | **TRIC-I-HF** |
|---|---|---|
| NYHA III/IV | 約 57% | **75%** |
| 過去 1 年 HFH | **23.8%** | **55.0%** |
| 腎／肝 | renal disease 35%；liver 6–9% | 心腎 **82%**；心肝 **46%** |
| TR torrential / severe | **51%** / 25–30% | **10%** / 51% |
| 對照組 1 年死亡率 | **8%** | **17.5%** |
| 30 天 TR ≤ moderate | **87%** | **70%** |

> TR 更嚴重但心衰竭較輕 → TR 降得漂亮、事件太少
> TR 較輕但腎肝已受損 → TR 降得普通、卻看到硬終點

---

# 方法學比較的五個結論

1. **不同的問題、不同的設計**：拿 TRIC-I-HF 批評 TRILUMINATE「沒看到硬終點」是誤解——它本來就不是為此設計

2. **中央資格委員會 vs 地方心臟團隊**：前者保證可夾性、排除最重病人（Kapadia 估僅 10–20% 符合）；後者貼近真實世界

3. **高風險富集 + 右心導管**才是 TRIC-I-HF 看到硬終點的方法學核心，不是器械或術者本身

4. **交叉規則決定哪些終點能被解讀**

5. **TR 嚴重度不是事件風險的主要決定因子，鬱血造成的器官傷害才是**

---

# 三個 RCT 並排比較

| | TRILUMINATE | Tri.Fr | **TRIC-I-HF** |
|---|---|---|---|
| 器械 | TriClip | TriClip | **PASCAL 66% / TriClip 33%** |
| 隨機 | 350 (1:1) | 300 (1:1) | **360 (2:1)** |
| 高風險收案 | 無 | 無 | **HFH / 心腎 / 心肝** |
| 術前右心導管 | 否 | 否 | **必做** |
| 主要結果 | WR 1.48，KCCQ 驅動 | PRO 驅動 | **WR 2.42，HFH 驅動** |
| 死亡率 | 無差異 | 無差異 | **3 年 HR 0.62** |

> 三個試驗互補；**沒有一個告訴我們末期右心衰竭或 precapillary 肺高壓該怎麼辦**

---

# 限制

1. **開放標籤**：KCCQ、NYHA 可能受影響（硬終點由獨立委員會判定）
2. **交叉 39%**：次要終點被稀釋，可能**低估**真實效果
3. **單一國家（德國）**：可近性、給付、經驗都是全球前段班
4. **多種器械混用**：無法比較 PASCAL vs TriClip
5. **3 年追蹤只完成 20.5%**：3 年死亡率好處不確定性大
6. 高風險條件 **2023 年 7 月中途加入**
7. 次要終點未校正多重比較

---

<!-- _class: divider -->
# 對台灣臨床實務的啟示

---

# 病人選擇 Checklist

```text
症狀性重度以上 TR，最適藥物治療 ≥ 30 天仍有症狀
  + 至少一項：
    [ ] 過去 12 個月心衰竭失代償／住院
    [ ] eGFR 持續 < 60 ml/min/1.73 m²
    [ ] bilirubin / ALP / γ-GT ≥ 2 項升高
  + 術前右心導管：排除 precapillary 肺高壓、「已經太晚」
  + 超音波：RV 功能尚可（TAPSE 18–19 mm、FAC 36–37%）
       ↓
  → TRIC-I-HF 證明有硬終點好處的族群
```

---

# 四個實務提醒

1. **不要等到失代償住院才做**：藥物組 48 位交叉中 28 位是住院時「被迫」手術，已付出一次終點事件的代價

2. **建立量能**：年量 ≥ 21 例與成功率相關；初期集中固定團隊

3. **七成病人需 ≥ 2 個器械**：術前規劃預留；器械選擇依解剖與團隊熟悉度

4. **心衰竭、腎臟、肝膽門診是找到這些病人的地方**：鬱血性肝病變與腎功能惡化常被歸因於老化而非 TR

---

# 指引脈絡

**2025 ESC/EACTS 瓣膜指引**

- 經導管三尖瓣介入 (TTVI) 用於症狀性重度 TR：**Class IIa，證據等級 A**
- 當時依據主要是**生活品質改善**（TRILUMINATE、Tri.Fr）

**TRIC-I-HF 之後**

- 第一次有「死亡或心衰竭住院」的硬終點證據
- 可預期下一版指引納入「**高心衰竭事件風險**」族群的建議
- 待解：末期 RV 衰竭、precapillary 肺高壓、器械間比較

---

# Clinical Pearls (1/2)

> **Pearl 1**：**第一個證明 T-TEER 減少「死亡或心衰竭住院」的 RCT**。WR 2.42、3 年 HR 0.40、1 年 NNT = 4——T-TEER 從「改善生活品質」走向「改變預後」。

> **Pearl 2**：**好處主要來自減少心衰竭住院**（HR 0.35）。死亡率 1 年不顯著、3 年才顯著，而 3 年追蹤只完成 20.5%。**不要說成「T-TEER 救命」。**

> **Pearl 3**：**選對病人是關鍵**。HFH / 心腎 / 心肝三選一 + 右心導管篩選 + RV 功能尚可。套到輕症病人身上，結果會回到 TRILUMINATE。

---

# Clinical Pearls (2/2)

> **Pearl 4**：**藥物組 39% 最後還是做了介入，多數在失代償住院時**。問題和 EASE 一樣：「現在做，還是等出事再做？」答案是現在做。

> **Pearl 5**：**29 個中心、平均 176 例經驗、七成植入 ≥ 2 個器械**。量能–結果關係在三尖瓣比二尖瓣更陡。外推前先看這三個數字。

> **Pearl 6**：**這是策略試驗，不是器械試驗**。PASCAL 66%、TriClip 33%——TRIC-I-HF 不能告訴你哪個器械好。

---

<!-- _class: small-text -->
# 參考文獻 (1/2)

1. Hausleiter J, et al. Tricuspid-Valve Intervention in Heart Failure. [*N Engl J Med*. 2026;395:1363-73.](https://doi.org/10.1056/NEJMoa2606934)
2. Patel MR. Transcatheter Tricuspid-Valve Intervention for Severe TR (editorial). [*N Engl J Med*. 2026;395:1438-9.](https://doi.org/10.1056/NEJMe2611648)
3. Stocker TJ, et al. Rationale and design of TRIC-I-HF-DZHK24. [*Eur J Heart Fail*. 2025;27:1895-904.](https://doi.org/10.1002/ejhf.3795)
4. Sorajja P, et al. TRILUMINATE Pivotal. [*N Engl J Med*. 2023;388:1833-42.](https://doi.org/10.1056/NEJMoa2300525)
5. Kar S, et al. TRILUMINATE Pivotal 2-year outcomes. [*Circulation*. 2025;151:1630-8.](https://doi.org/10.1161/CIRCULATIONAHA.125.074536)
6. Donal E, et al. Tri.Fr randomized clinical trial. [*JAMA*. 2025;333:124-32.](https://doi.org/10.1001/jama.2024.21189)

---

<!-- _class: small-text -->
# 參考文獻 (2/2)

7. Stocker TJ, et al. Cardiopulmonary hemodynamic profile predicts mortality after TTVR. [*JACC Cardiovasc Interv*. 2021;14:29-38.](https://doi.org/10.1016/j.jcin.2020.09.033)
8. Stolz L, et al. Cardiohepatic syndrome and prognosis after T-TEER. [*JACC Cardiovasc Interv*. 2022;15:179-89.](https://doi.org/10.1016/j.jcin.2021.10.033)
9. Wild MG, et al. PASTE registry 1-year results. [*J Am Coll Cardiol*. 2025;85:220-31.](https://doi.org/10.1016/j.jacc.2024.10.068)
10. Lurz P, et al. bRIGHT study 1-year results. [*J Am Coll Cardiol*. 2024;84:607-16.](https://doi.org/10.1016/j.jacc.2024.05.006)
11. Tomasoni D, et al. HFH and outcomes after T-TEER: EuroTR. [*Eur J Heart Fail*. 2025;27:1559-69.](https://doi.org/10.1002/ejhf.3757)
12. Praz F, et al. 2025 ESC/EACTS Guidelines for valvular heart disease. [*Eur Heart J*. 2025;46:4635-736.](https://doi.org/10.1093/eurheartj/ehaf194)
13. Abbott. TRILUMINATE Pivotal Clinical Investigation Plan (Version F), NCT03904147. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT03904147)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

[TRIC-I-HF — N Engl J Med 2026;395:1363-73](https://doi.org/10.1056/NEJMoa2606934)
