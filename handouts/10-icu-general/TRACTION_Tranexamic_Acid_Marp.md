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
  section.lead h1 { color: #ffffff; font-size: 2.1em; }
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
  table { font-size: 0.64em; width: 100%; }
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
    font-size: 0.66em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.82em; }
  section.lead blockquote {
    background-color: rgba(255,255,255,0.10);
    border-left: 4px solid #ffe28a;
    color: #ffffff;
  }
  section.lead blockquote strong { color: #ffe28a; }
footer: '謝慕揚 MD, PhD, FESC | TRACTION：非心臟手術的 Tranexamic Acid | 2026'
---

<!-- _class: lead -->
# 全院 Tranexamic Acid 政策能安全減少輸血嗎？
## TRACTION 試驗（非心臟大手術）
**謝慕揚 MD, PhD, FESC** | 2026-06-11
NEJM 2026 · 加拿大 10 院 · 8273 人
[原文連結 (DOI)](https://doi.org/10.1056/NEJMoa2515820)

---

# 一句話重點

> 在 10 家加拿大醫院、8273 位高輸血風險非心臟大手術病人中，**全院 tranexamic acid（傳明酸, TXA）政策**使紅血球輸血由 **9.8% → 7.4%**（RR 0.73，NNT 37），且 **90 天靜脈血栓栓塞 (VTE) 達不劣性**。

- 即使 **60.5% 是腫瘤手術**，血栓也沒增加。
- TXA 便宜、易得；務實的 cluster-crossover 設計把它升級為「醫院政策」並驗證安全。

---

# 背景：為什麼仍有疑慮

- 圍術期出血是輸血主因；血品供給日益吃緊。
- **TXA** = 抗纖維蛋白溶解藥，已在心臟、骨科手術證實減少失血/輸血。
- 廣義非心臟手術採用率不一 → 主因擔心**血栓**（尤其癌症等促凝狀態）。
- **POISE-3 (2022)**：TXA 減少大出血，但**未達 30 天心血管不劣性** → 留安全性問號。
- **TRACTION 提問**：整院常規給 TXA，能否不顯著增加 VTE 而減少輸血？

---

# 設計：cluster-crossover 的巧思

| 項目 | 內容 |
|------|------|
| 設計 | 多中心、雙盲、整群隨機、安慰劑對照、**整群交叉** |
| 隨機單位 | **醫院**（非個別病人）；每 4 週切換 TXA vs 安慰劑政策 |
| 對象 | 估計輸血風險 ≥5% 的非心臟大手術（多為 ≥3h） |
| TXA 劑量 | 開刀 1 g IV（>100 kg 給 2 g）+ 縫合前 1 g |
| 共同主要終點 | ①住院紅血球輸血；②90 天 VTE（不劣性上界 1.46） |
| 規模 | 8273 人、10 院、25 個 4 週期；資料連結 >98% |

> 兩個共同主要終點**都要達成**才宣告有益（不需多重校正）。腫瘤手術佔 **60.5%**。

---

# 主要結果

| 主要終點 | TXA | 安慰劑 | 效應 |
|------|------|------|------|
| **紅血球輸血** | 7.4% | 9.8% | **RR 0.73 (0.61–0.86)**；−2.7 pp；**NNT 37** |
| **90 天 VTE (PP)** | 2.1% | 2.1% | **RR 0.96 (0.65–1.38)** → 上界 1.38 < 1.46，**達不劣性** |
| 90 天 VTE (ITT) | 2.1% | 2.2% | RR 0.92 (0.62–1.30) |

- 效益在各次族群一致（年齡、手術別、急迫性、腫瘤與否、輸血風險）。

> 兩個共同主要終點皆達成：**輸血顯著↓、VTE 不劣於安慰劑**。

---

# 次要與安全終點

| 終點 | TXA | 安慰劑 |
|------|------|------|
| 每 100 人輸血單位 | 24.7 | 34.2（差 −9.5） |
| 心肌梗塞 | 0.7% | 0.8% |
| 中風 | 0.2% | 0.2% |
| 肺栓塞 | 0.2% | 0.1% |
| ICU 入住 | 16.7% | 17.5% |
| 90 天存活 | 97.8% | 97.6% |

- 嚴重不良事件：TXA 1 例圍術期癲癇、安慰劑 1 例過敏（各 1 例）。
- 心血管與血栓事件兩組相近。

---

# 亮點：癌症手術族群

- 過去因擔心**促凝**，癌症常被排除於 TXA 試驗。
- TRACTION 納入 **5002 位腫瘤手術（60.5%）**。
- 癌症族群 90 天 VTE：**2.4% (TXA) vs 2.6% (安慰劑)，RR 0.92 (0.68–1.48)** → 未增加。

> 提供「**癌症病人接受非心臟大手術可安全用 TXA**」的可貴實證。

---

# 與 POISE-3 的關係

| 面向 | POISE-3 (2022) | TRACTION (2026) |
|------|------|------|
| 對象 | 出血/心血管風險 | 高**輸血**風險大手術 |
| 設計 | 個別病人隨機 | 醫院整群交叉、登錄為基礎 |
| 主訊息 | 減大出血；**未達心血管不劣性** | 減輸血；**VTE 達不劣性** |
| 腫瘤 | ~22% 骨科 | **60.5% 腫瘤** |

> 注意：兩者主要安全終點定義不同（POISE-3 心血管複合 vs TRACTION VTE）。

---

# 臨床啟示與我的觀點

> 讀書會討論觀點，非指引建議。

- **支持** TXA 納入高輸血風險非心臟大手術的常規止血策略——便宜、易得、可標準化進麻醉流程。
- **癌症手術不再是禁區**（VTE 未增）。
- **政策思維**：醫院層級 + 登錄為基礎 RCT 能低成本快速產出高品質證據（每月 >500 人）。
- **限制**：僅限可資料連結醫院；亞臨床 VTE 可能低估；加拿大族群；已排除心臟/髖膝置換等。

---

<!-- _class: lead -->
# Take-home

> ① 全院 TXA 政策：輸血 **9.8% → 7.4%**（NNT 37）。
> ② 90 天 VTE **達不劣性**——含 60.5% 腫瘤手術。
> ③ 便宜、可標準化；與外科/麻醉建立**標準給藥流程**值得考慮。

---

<!-- _class: small-text -->
# 參考文獻

1. Houston BL, et al. TRACTION. [*N Engl J Med*. 2026. DOI:10.1056/NEJMoa2515820.](https://doi.org/10.1056/NEJMoa2515820)
2. Devereaux PJ, et al. POISE-3. [*N Engl J Med*. 2022;386:1986-1997.](https://doi.org/10.1056/NEJMoa2201171)
3. CRASH-2 collaborators. [*Lancet*. 2010;376:23-32.](https://doi.org/10.1016/S0140-6736(10)60835-5)
4. WOMAN Trial Collaborators. [*Lancet*. 2017;389:2105-2116.](https://doi.org/10.1016/S0140-6736(17)30638-4)
5. Myles PS, et al. ATACAS. [*N Engl J Med*. 2017;376:136-148.](https://doi.org/10.1056/NEJMoa1606424)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC**
本文件為讀書會共筆整理，僅供教學參考
