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
footer: '謝慕揚 MD, PhD, FESC | RECOVERY Trial 10-Year | 2026'
---

<!-- _class: lead -->

# Early Surgery or Conservative Care for Asymptomatic Aortic Stenosis at 10 Years

## RECOVERY Trial 十年最終結果

**謝慕揚 MD, PhD, FESC**
資料來源：[*N Engl J Med*. 2026;394:1167-74](https://doi.org/10.1056/NEJMoa2511920) | 2026-03-28

---

# 大綱

1. 研究背景 (Background)
2. 研究方法 (Methods)
3. 主要結果 (Results)
4. 與其他試驗比較
5. 臨床意義與限制
6. 結論 (Conclusions)

---

<!-- _class: divider -->

# 第一部分：研究背景

---

# 無症狀嚴重主動脈瓣狹窄的臨床難題

- **Severe AS** 有症狀 → AVR（指引一致推薦 Class I）
- **Asymptomatic severe AS** → 傳統策略：**watchful waiting**
  - 無症狀期 sudden death 風險低 (<1%/年)
- 但 **watchful waiting 的隱憂**：
  - 不可逆 myocardial damage（壓力超負荷）
  - 等待症狀出現時可能已太遲
  - 急診手術風險高於擇期手術

> **關鍵問題**：早期手術的獲益能否超過人工瓣膜長期併發症的風險？

---

# RECOVERY Trial 背景

- **原始 RECOVERY trial** (Kang et al., *NEJM* 2020)
  - 145 位無症狀 very severe AS 患者
  - 中期結果（≥4 年追蹤）：早期手術顯著降低心血管死亡
- **延伸追蹤的必要性**：
  - 人工瓣膜長期風險（bioprosthetic valve degeneration、thromboembolism）
  - 需證實早期手術的獲益是否「可持續」
- **本文**：RECOVERY trial **十年最終追蹤結果**

---

<!-- _class: divider -->

# 第二部分：研究方法

---

# 研究設計

- **多中心 RCT**：韓國 4 家醫學中心（open-label）
- **收案**：2010/7 – 2015/4，共 **145** 位患者
- **隨機分配 1:1**：
  - 早期手術組 (n=73)：2 個月內接受 surgical AVR
  - 保守治療組 (n=72)：watchful waiting → 出現症狀/LVEF↓/快速進展時介入

### Very Severe AS 定義

| 參數 | 標準 |
|------|------|
| Aortic valve area | **≤0.75 cm²** |
| Peak aortic jet velocity | **≥4.5 m/s** |
| 或 Mean gradient | ≥50 mmHg |

---

# 研究終點

| 終點 | 定義 |
|------|------|
| **Primary** | Operative mortality + 心血管死亡 (composite) |
| **Secondary** | 全因死亡、thromboembolic events、repeat AVR、心衰住院 |

### 統計方法
- Intention-to-treat analysis
- Stratified Cox proportional-hazards regression + **Firth correction**
- Competing-risk analysis (Fine & Gray)
- 中位追蹤：**144 個月**（12 年）

---

# 基線特徵

| 特徵 | 早期手術 (n=73) | 保守治療 (n=72) |
|------|----------------|----------------|
| 年齡 (歲) | 65.0 ± 7.8 | 63.4 ± 10.7 |
| 男性 | 51% | 47% |
| 糖尿病 | 18% | 10% |
| Bicuspid aortic valve | 67% | 54% |
| EuroSCORE II | 0.9 ± 0.3% | 0.9 ± 0.4% |
| Peak Vmax (m/s) | 5.14 ± 0.52 | 5.04 ± 0.44 |
| AVA (cm²) | 0.63 ± 0.09 | 0.64 ± 0.09 |
| LVEF (%) | 64.8 ± 5.2 | 64.8 ± 4.1 |

---

<!-- _class: divider -->

# 第三部分：主要結果

---

# Primary Endpoint：Operative Mortality 或心血管死亡

| | 早期手術 | 保守治療 | HR (95% CI) |
|---|---------|---------|-------------|
| **Events** | **2/73 (3%)** | **17/72 (24%)** | **0.10 (0.02–0.43)** |
| **P value** | | | **P = 0.002** |

### 10 年累積發生率
- 早期手術：**1%**
- 保守治療：**19%**

> **NNT = 6**（10 年內預防一例心血管死亡）

---

# 全因死亡 (All-Cause Mortality)

| | 早期手術 | 保守治療 | HR (95% CI) |
|---|---------|---------|-------------|
| **Events** | **11/73 (15%)** | **23/72 (32%)** | **0.42 (0.21–0.86)** |

### 10 年累積發生率
- 早期手術：**11%**
- 保守治療：**25%**

> **NNT = 7**（10 年內預防一例全因死亡）

---

# 次要終點一覽

| 終點 | 早期手術 | 保守治療 | HR (95% CI) |
|------|---------|---------|-------------|
| Operative mortality / CV death | 2 (3%) | 17 (24%) | **0.10 (0.02–0.43)** |
| All-cause mortality | 11 (15%) | 23 (32%) | **0.42 (0.21–0.86)** |
| Thromboembolic event | 3 (4%) | 7 (10%) | 0.39 (0.10–1.48) |
| Repeat AVR | 3 (4%) | 4 (6%) | 0.67 (0.15–2.99) |
| **心衰住院** | **0 (0%)** | **14 (19%)** | **0.03 (0.00–0.49)** |

> **Pearl**：早期手術組 **零** 心衰住院！

---

# 保守治療組的「真實結局」

- 72 位保守治療組患者中：
  - **85% (61/72)** 最終接受 AVR
  - **19% 為急診手術**（從急診入院）
  - 中位等待時間：**1048 天**（約 2.9 年）
- 10 年累積結果：
  - **97% 死亡或接受 AVR**

> **Pearl**：Watchful waiting 並不是「不手術」，而是「延遲手術」— 但延遲付出了代價。

---

# 延遲手術的代價

- 保守治療組 AVR **前**：10 人死亡（全部心血管死亡）
- 保守治療組 AVR **後**：13 人死亡（7 人心血管死亡）

> **Pearl**：未接受 AVR → 心血管死亡最高
> 延遲 AVR（隨機分配至手術的時間越長）→ 心血管死亡亦較高
> **時間就是心肌 (Time is Myocardium)**

---

<!-- _class: divider -->

# 第四部分：與其他試驗比較

---

# 無症狀 Severe AS 早期介入 — 主要 RCT 比較

| 試驗 | N | Vmax 門檻 | 介入方式 | 中位追蹤 | All-cause mortality |
|------|---|----------|---------|---------|-------------------|
| **RECOVERY** | 145 | ≥4.5 m/s | SAVR | **144 月** | HR 0.42 ✓ |
| **AVATAR** (ext.) | 157 | ≥4.0 m/s | SAVR | 63 月 | **有利早期手術** ✓ |
| **EARLY TAVR** | 901 | ≥4.0 m/s | TAVR | ~46 月 | 無顯著差異 ✗ |
| **EVOLVED** | 224 | Severe + fibrosis | SAVR | — | 見 JAMA 2025 |

---

# 為什麼 EARLY TAVR 結果不同？

1. **追蹤時間短**：46 個月 vs. RECOVERY 144 個月
   - AS 為慢性進行性疾病，需長期追蹤才能看到差異
2. **保守組 87% 在 11.1 個月即接受 AVR**
   - 「保守」組幾乎等於「延遲 11 個月手術」組
   - 兩組差異被嚴重稀釋
3. **AVATAR extended follow-up (63 月)** 開始出現 mortality 差異

> **Pearl**：追蹤時間是決定性因素 — 隨著追蹤延長，早期介入的優勢持續擴大。

---

<!-- _class: divider -->

# 第五部分：臨床意義與限制

---

# 臨床 Take-Home Messages

1. **Very severe AS (Vmax ≥4.5, AVA ≤0.75)** + 無症狀 + 手術低風險
   → **強烈考慮早期 surgical AVR**
2. 早期手術 **NNT = 6**（心血管死亡）、**NNT = 7**（全因死亡）
3. 保守治療 = 延遲手術，但 97% 最終需手術，且 19% 急診入院
4. 早期手術組 **零** 心衰住院 → 及時解除壓力超負荷預防不可逆損傷

> **核心理念**：在 very severe AS 中，早期介入不是「過度治療」，而是「預防性治療」。

---

# 研究限制

1. **Very severe AS 門檻高** (Vmax ≥4.5) → 不一定適用一般 severe AS
2. **Open-label** → 非致死終點可能有 ascertainment bias
3. **樣本數小** (n=145) → primary endpoint 事件數少
4. **族群年輕** (64 歲)、**共病少** (EuroSCORE 0.9%)
5. 均為 **surgical AVR** → TAVR 長期效果未知
6. **高手術量中心** → 外推性受限
7. 部分追蹤期間逢 **COVID-19 pandemic**

---

<!-- _class: divider -->

# 結論

---

# RECOVERY Trial 10-Year — 結論

### 無症狀 very severe AS 患者：

- 早期 surgical AVR vs. conservative care
- **Operative mortality / 心血管死亡**：HR **0.10** (P=0.002)
- **全因死亡**：HR **0.42**
- 十年追蹤曲線 **持續分離**，早期手術優勢 **無衰減**

### 臨床啟示：

> **對於手術風險低的 very severe AS 無症狀患者，早期 AVR 可顯著改善長期存活。**
> **"Don't wait for symptoms — the damage may already be done."**

---

<!-- _class: small-text -->

# 參考文獻 (1/2)

1. Otto CM, et al. 2020 ACC/AHA VHD guideline. [*Circulation*. 2021;143:e35-e71.](https://doi.org/10.1161/CIR.0000000000000923)
2. Praz F, et al. 2025 ESC/EACTS VHD guidelines. [*Eur Heart J*. 2025;46:4635-4736.](https://doi.org/10.1093/eurheartj/ehaf194)
3. Otto CM, et al. Calcific AS: a review. [*JAMA*. 2024;332:2014-26.](https://doi.org/10.1001/jama.2024.16477)
4. Généreux P, et al. EARLY TAVR trial. [*NEJM*. 2025;392:217-27.](https://doi.org/10.1056/NEJMoa2405880)
5. Kang DH, et al. RECOVERY trial (original). [*NEJM*. 2020;382:111-9.](https://doi.org/10.1056/NEJMoa1912846)
6. Banovic M, et al. AVATAR extended FU. [*Eur Heart J*. 2024;45:4526-35.](https://doi.org/10.1093/eurheartj/ehae585)
7. Hillis GS, et al. Asymptomatic severe AS — waiting game? [*Circulation*. 2022;145:874-6.](https://pubmed.ncbi.nlm.nih.gov/35254880/)
8. Maznyczka A, et al. Timing of AV intervention. [*JACC Cardiovasc Interv*. 2024;17:2502-14.](https://doi.org/10.1016/j.jcin.2024.08.046)
9. Pellikka PA, et al. Natural history of asymptomatic AS. [*JACC*. 1990;15:1012-7.](https://pubmed.ncbi.nlm.nih.gov/2312956/)
10. Pellikka PA, et al. Outcome of 622 adults. [*Circulation*. 2005;111:3290-5.](https://doi.org/10.1161/CIRCULATIONAHA.104.495903)

---

<!-- _class: small-text -->

# 參考文獻 (2/2)

11. Banovic M, et al. AVATAR trial. [*Circulation*. 2022;145:648-58.](https://doi.org/10.1161/CIRCULATIONAHA.121.057639)
12. Blankenberg S. To wait or not to wait (editorial). [*NEJM*. 2025;392:278-9.](https://doi.org/10.1056/NEJMe2415973)
13. Lancellotti P, et al. Asymptomatic AS in valve clinics. [*JAMA Cardiol*. 2018;3:1060-8.](https://doi.org/10.1001/jamacardio.2018.3152)
14. Gahl B, et al. Natural history & early intervention (meta-analysis). [*JAMA Cardiol*. 2020;5:1102-12.](https://doi.org/10.1001/jamacardio.2020.2497)
15. Loganath K, et al. EVOLVED trial. [*JAMA*. 2025;333:213-21.](https://doi.org/10.1001/jama.2024.22730)
16. Lindman BR, et al. AVR for asymptomatic AS — the time has come. [*JAMA Cardiol*. 2025;10:305-6.](https://doi.org/10.1001/jamacardio.2024.5648)
17. Généreux P, et al. AVR vs surveillance (meta-analysis). [*JACC*. 2025;85:912-22.](https://doi.org/10.1016/j.jacc.2024.11.006)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
