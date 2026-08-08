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
  section.lead a { color: #8ecae6; }
  section.lead blockquote, section.lead blockquote strong { color: #2d3436; }
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
footer: '謝慕揚 MD, PhD, FESC | HF 床邊血流動力學分型 Nohria-Stevenson | 2003'
---

<!-- _class: lead -->

# Clinical Assessment Identifies Hemodynamic Profiles That Predict Outcomes in Heart Failure

## 心衰竭住院病人的床邊血流動力學分型 (Nohria-Stevenson)

**謝慕揚 MD, PhD, FESC** | 2026-07-21

Nohria A, et al. *J Am Coll Cardiol*. 2003;41(10):1797-1804
[https://doi.org/10.1016/S0735-1097(03)00309-7](https://doi.org/10.1016/S0735-1097(03)00309-7)

---

# 大綱

1. 為什麼需要床邊分型？
2. 兩軸判斷：鬱血 (wet/dry) × 灌流 (warm/cold)
3. 四型 2×2 分型矩陣
4. 各 Profile 人數與嚴重度梯度
5. 預後：Kaplan-Meier 與 HR
6. 臨床治療指引
7. 重點回顧

---

<!-- _class: divider -->

# 第一部分：為什麼要床邊分型？

---

# 背景：從 Forrester 到床邊

- 進展性心衰竭治療選擇多，卻缺**簡單臨床分型**來描述病人、指引治療、篩選試驗。
- **Forrester (1976)**：AMI 病人以 Swan-Ganz 導管分四型
  - 鬱血 = PCWP ≥ 18 mmHg；低灌流 = CI < 2.2 L/min/m²
- 慢性心衰竭中，囉音/水腫偵測填充壓不可靠；但 **orthopnea、proportional pulse pressure** 與血流動力學相關良好。
- **假說**：純用病史與理學檢查的四型 profile，能否界定住院心衰竭病人的預後分類？

---

# 研究族群一覽

- **設計**：前瞻性、單一中心 (Brigham and Women's Hospital)
- **對象**：1996/11–1999/7 連續收治 **452 位**心衰竭住院病人
- **入院 24 小時內**由主治/fellow 依理學檢查分型
- **基線**：平均年齡 55 歲、男性 69%、平均 LVEF 25.8%、缺血性病因 49%
- **追蹤**：平均 18 個月，追蹤率 99.5%
- **終點**：一年 **死亡 (n=117)**、**死亡或緊急移植 (n=137)**

---

<!-- _class: divider -->

# 第二部分：兩軸怎麼判斷？

---

# 鬱血 (Congestion) → wet vs. dry

出現任一項即偏向 **Wet (濕)**：

- Orthopnea 端坐呼吸
- 頸靜脈怒張 (JVD)
- 肺囉音 (rales)
- 肝頸靜脈迴流 (hepatojugular reflux)
- 腹水、周邊水腫
- 肺動脈瓣 P2 向左傳導
- Valsalva 方波型血壓反應 (square-wave)

---

# 灌流 (Perfusion) → warm vs. cold

出現任一項即偏向 **Cold (冷)**：

- 窄 proportional pulse pressure
  **(SBP − DBP) / SBP < 25%**
- 交替脈 (pulsus alternans)
- 症狀性低血壓 (無姿勢性)
- 四肢冰冷 (cool extremities)
- 意識/認知變差 (impaired mentation)

> 醫師整合多個徵象做主觀判斷 → 比任何單一徵象更能反映侵入性血流動力學。

---

<!-- _class: divider -->

# 第三部分：四型 2×2 矩陣

---

# 2×2 分型矩陣

| | **Warm 灌流佳** | **Cold 低灌流** |
|--------------|------------------------------|------------------------------|
| **Dry 無鬱血** | **A 乾暖**：n=123 (27%) | **L 乾冷**：n=16 (4%) |
| **Wet 有鬱血** | **B 濕暖**：n=222 (49%) | **C 濕冷**：n=91 (20%) |

- 對應 Forrester：A≈I、B≈II、C≈IV、L≈III
- 差別：本研究**完全用床邊評估**，非導管

---

# 分型真的對應血流動力學嗎？(RHC 子群)

| Profile | PCWP (mmHg) | CI (L/min/m²) |
|---------|-------------|----------------|
| A 乾暖 | 15.6 ± 7.9 | 2.3 ± 0.3 |
| B 濕暖 | 26.7 ± 6.0 | 2.1 ± 0.6 |
| C 濕冷 | 32.3 ± 6.9 | 1.9 ± 0.7 |
| L 乾冷 | 30.3 ± 4.0 | 1.6 ± 0.5 |
| *p* | < 0.0001 | 0.07 |

> **Wet 對應高 PCWP，Cold 對應低 CI** — 床邊判斷方向與侵入性量測一致。

---

<!-- _class: divider -->

# 第四部分：嚴重度與預後

---

# 病情嚴重度呈階梯：C > B > A

| 特徵 | A (123) | B (222) | C (91) | p |
|------|---------|---------|--------|---|
| LVEF (%) | 28.2 | 26.3 | 21.5 | 0.0004 |
| NYHA class | 2.3 | 3.1 | 3.5 | <0.0001 |
| 休息心率 | 81 | 88 | 91 | 0.0004 |
| 收縮壓 | 116 | 114 | 103 | <0.0001 |
| 血鈉 | 138 | 137 | 136 | 0.01 |
| Beta-blocker (%) | 35 | 23 | 19 | 0.04 |

---

# 存活分析 (Kaplan-Meier)

- 一年內 **117/452 (26%)** 未移植而死亡；另 42 人移植。
- **Profile C 最差 → B → A** (皆 p<0.01)
- 死亡+緊急移植終點：
  - A vs B：**p=0.002**
  - B vs C：**p=0.005**
  - A vs C：**p<0.001**
- Profile L 因事件太少未納入統計。

---

# 各 Profile 人數與 HR（單變項）

死亡加緊急移植，Profile A 為參考組：

| Profile | n (%) | HR (95% CI) | p |
|---------|-------|-------------|---|
| **A 乾暖** | 123 (27%) | Reference | — |
| **B 濕暖** | 222 (49%) | **2.10 (1.29–3.43)** | 0.003 |
| **C 濕冷** | 91 (20%) | **3.66 (2.16–6.21)** | <0.001 |
| L 乾冷 | 16 (4%) | 1.98 (0.75–5.24) | 0.17 |

---

# 多變項校正後仍獨立預測

校正年齡、缺血病因、血肌酸酐、NYHA、SBP、血鈉：

| Profile | 全體 HR | p | NYHA III/IV HR | p |
|---------|---------|---|-----------------|---|
| A | Reference | — | Reference | — |
| **B 濕暖** | **1.83** | **0.02** | **2.23** | 0.03 |
| **C 濕冷** | **2.48** | **0.003** | **2.73** | 0.009 |
| L 乾冷 | 1.94 | 0.19 | 1.94 | 0.28 |

> 即使**僅限 NYHA III/IV** 亞群，Profile B、C 仍具獨立預後價值。

---

# 一個關鍵洞見

> **51/326** 位描述嚴重症狀 (NYHA III/IV) 的病人，床邊評估其實是 **Profile A** — 且預後相對良好。

- NYHA 是「症狀」；床邊分型是「血流動力學狀態」。
- 分型提供了 **NYHA 功能分級之外**的額外預後資訊。
- 呈 Profile A 卻喊喘 → 應找**其他呼吸困難原因**。

---

<!-- _class: divider -->

# 第五部分：床邊分型如何指引治療

---

# 依 Profile 調整治療策略

```text
A 乾暖  → 代償良好、預後佳
          可安全啟動/加量 beta-blocker
          若失代償症狀 → 找其他病因
B 濕暖  → 目標：降填充壓、緩解症狀
          經驗性利尿 ± 血管擴張劑
          beta-blocker 維持、暫緩加量
C 濕冷  → 住院強化利尿，可能導管導引
          減量/暫停近期起始的 beta-blocker
          可能界定 inotrope 風險效益不同族群
L 乾冷  → 少見；考慮 CRT、二尖瓣修補、心室重塑
```

> 註：治療建議為作者提議，非隨機試驗證據。

---

# 臨床珍珠 Clinical Pearls

> **Pearl 1**：兩個問題定分型 —「濕不濕 (鬱血)」與「暖不暖 (灌流)」，床邊 2 分鐘即可完成。

> **Pearl 2**：Wet 找 orthopnea/JVD/水腫；Cold 找窄脈壓 (<25%)、四肢冰冷、意識改變。

> **Pearl 3**：Profile C (濕冷) 是最高風險，多變項 HR 2.48；別把喊喘的 Profile A 過度治療。

---

# 重點回顧 Take Home

- **床邊病史+理學檢查**即可把住院心衰竭分四型：A 乾暖 / B 濕暖 / C 濕冷 / L 乾冷。
- 分型**對應侵入性血流動力學** (wet↑PCWP、cold↓CI)，且**獨立預測**一年死亡/緊急移植。
- **Profile B、C 顯著高風險**（multivariate HR 1.83、2.48），NYHA III/IV 亞群亦然。
- 用途：**指引治療 + 篩選試驗族群**，並為 ESCAPE trial 分型基礎。

---

<!-- _class: small-text -->

# 參考文獻

1. Nohria A, Tsang SW, Fang JC, et al. Clinical assessment identifies hemodynamic profiles that predict outcomes in patients admitted with heart failure. *J Am Coll Cardiol*. 2003;41(10):1797-1804. https://doi.org/10.1016/S0735-1097(03)00309-7
2. Forrester JS, Diamond G, Chatterjee K, Swan HJ. Medical therapy of acute myocardial infarction by application of hemodynamic subsets. *N Engl J Med*. 1976;295(25):1404-1413.
3. Stevenson LW, Perloff JK. The limited reliability of physical signs for estimating hemodynamics in chronic heart failure. *JAMA*. 1989;261(6):884-888.
4. Drazner MH, Rame JE, Stevenson LW, Dries DL. Prognostic importance of elevated jugular venous pressure and a third heart sound in heart failure. *N Engl J Med*. 2001;345(8):574-581.
5. Shah MR, O'Connor CM, Sopko G, et al. ESCAPE: design and rationale. *Am Heart J*. 2001;141(4):528-535.

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
