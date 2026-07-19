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
  section.lead a { color: #74b9ff; }
  section.lead blockquote { color: #2d3436; }
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
  section.divider h2 { color: #ffd166; }
  section.divider h3 { color: #ffffff; }
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
    font-size: 0.62em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.8em; }
  section.ref { font-size: 0.62em; }
footer: '謝慕揚 MD, PhD, FESC | Same-Day Discharge After PCI | 2026'
---

<!-- _class: lead -->
# 當日出院 PCI
## Same-Day Discharge After PCI
**謝慕揚 MD, PhD, FESC** | 2026-07-19

核心指引：[2021 ACC Expert Consensus Decision Pathway on SDD After PCI (JACC 2021)](https://doi.org/10.1016/j.jacc.2020.11.013)

---

# 名詞先釐清：三個別搞混

| 名詞 | 講的是 | 重點 |
|------|--------|------|
| **Ad-hoc PCI** | 手術**時機** | 攝影後同次直接做 PCI |
| **Same-Day Discharge (SDD)** | 住院**天數** | PCI 後當天回家 |
| **Ambulatory / Day-case** | 流程規劃 | 以 SDD 為目標的門診/日間流程 |

> 本講義聚焦 **SDD** — 病人抵院 **12 小時內出院**、不需監測式過夜住院（SCAI 定義）。

---

# 為什麼要 SDD？四大驅動力

- **病人偏好** — 回自己家恢復，睡眠與滿意度較佳
- **床位與資源** — 釋放住院床位，高手術量中心尤其關鍵
- **成本** — 每例約省 **US$5,128**（Amin, JAMA Cardiol 2018）
- **技術成熟** — Radial access + 新一代 DES + 強效抗血小板藥

> **核心觀念**：SDD 不是「趕人回家」，而是用**結構化風險評估**，把本來就低風險的病人管理得更安全、更省、更滿意。安全性來自**病人選擇**，不是縮短觀察。

---

<!-- _class: divider -->
# 實證基礎
## 從 EPOS 到 2025 Meta-analysis

---

# EPOS — 第一個關鍵 RCT (2007)

800 例經**股動脈**擇期 PCI，術後 4 小時 triage，隨機當日出院 vs 過夜。

| 24h 複合終點 | SDD | 過夜住院 |
|------|-----|---------|
| 全體 | **2.2%** (9/403) | 4.2% (17/397) |
| 適合早期出院者 | 0.3% (1/326) | 0.6% (2/312) |

- 非劣性 **P < 0.0001**；約 **80%** 擇期病人適合當日出院
- 即使股動脈時代，嚴選病人 SDD 不增加併發症

**原文：** [Heyde GS, et al. *Circulation*. 2007;115(17):2299-2306.](https://doi.org/10.1161/CIRCULATIONAHA.105.591495)

---

# Meta-analysis：20 年、14 RCT 一致結論

Nguyen 2025：**14 RCT、3,215 例**（30 天結果）

| 結果 | Risk Ratio (95% CI) | P |
|------|---------------------|---|
| MACE | 0.76 (0.46–1.27) | 0.30 |
| 大出血 | 1.29 (0.50–3.37) | 0.60 |
| 血管併發症 | 1.06 (0.78–1.45) | 0.70 |
| 再住院 | 1.15 (0.79–1.68) | — |
| 中風 | 0.99 (0.17–5.64) | 0.99 |

> SDD 對**嚴選低風險擇期 PCI** 病人，各面向與過夜住院**無統計差異**。

**原文：** [Nguyen NH, et al. *Eur Cardiol*. 2025;20:e19.](https://doi.org/10.15420/ecr.2025.21)

---

# 真實世界：安全、省錢，但用得不夠

**成本（Amin, JAMA Cardiol 2018）— 672,470 例**
- SDD 每例省 **US$5,128**；死亡/出血/AKI/AMI 無較高風險
- 各院差異 **0%–83%**

**趨勢（Bradley, JACC Interv 2021）— 819,091 例**
- SDD 4.5%（2009）→ **28.6%（2017）**
- 橈動脈 SDD 39.7% vs 股動脈 19.5%
- 增加**未伴隨** 30 天死亡/再住院上升

> 各院採用率差異極大 → 這是可改善的**照護價值缺口**。

[Amin 2018 (JAMA Cardiol)](https://doi.org/10.1001/jamacardio.2018.3029) ｜ [Bradley 2021 (JACC Interv)](https://doi.org/10.1016/j.jcin.2021.05.043)

---

<!-- _class: divider -->
# 怎麼選病人？
## ACC 2021 三段式 Checklist

---

# 三段式 Checklist：全部通過才放行

| 時間點 | 問什麼 | 關鍵條件 |
|--------|--------|---------|
| **① 術前** | 這病人本來適合嗎？ | 穩定擇期、無顯著貧血/腎損、DAPT 可依從、**可靠交通與照顧者** |
| **② 術後即刻** | 今天做得順嗎？ | PCI 成功、無 dissection/perforation/no-reflow、止血完成、血流動力學穩定 |
| **③ 出院前** | 現在放走安全嗎？ | 能下床、穿刺處 OK、理解用藥與警訊、**已安排追蹤與次日聯繫** |

> 任一關卡出現排除條件（exclusionary criteria）→ 改為留院觀察。

**原文：** [Rao SV, et al. 2021 ACC ECDP. *JACC*. 2021;77(6):811-825.](https://doi.org/10.1016/j.jacc.2020.11.013)

---

# Radial Access：現代 SDD 的關鍵促成因素

- **出血與血管併發症顯著較低** → 止血快、可早期下床
- 免除股動脈臥床時間 → 直接縮短觀察需求
- 真實世界：橈動脈 SDD 採用率（39.7%）遠高於股動脈（19.5%）
- SCAI 共識明列 radial access 為支持早期出院的技術進展

> **實務**：要建 SDD 流程，**預設 radial-first**。股動脈仍可 SDD（EPOS 已證實），但止血與觀察門檻較高。

---

# 併發症時間學：為什麼「過夜」保護有限

```text
併發症風險時間分布（示意）

風險
 高 │█                              █
    │█                            ██
    │██                          ██
 低 │ ███____________________████
    └────┬─────┬──────┬──────┬─────→ 時間
       0-6h   6h    12h    24h   >24h
      早期急性         ← 過夜窗口 →    晚期
      院內觀察攔截      保護價值有限    靠衛教/返院
```

- 併發症多發生在 **< 6 小時**（急性）或 **> 24 小時**（晚期）
- 過夜（6–24h）剛好落在事件最少的窗口 → 對低風險病人保護有限
- 術後 **4–6 小時**觀察攔截早期事件；晚期靠**衛教 + 次日聯繫 + 可返院**

---

# 出院後安全網 & 誰不適合

**安全網（重點不在省時間，在建好院外防護）**
- 次日電話追蹤（標配）｜明確返院紅旗指引
- 書面 + 口頭衛教（DAPT 不可自行停）｜清楚回診時間

**不適合 / 需留院觀察**
- 急性冠心症（STEMI、高風險 NSTE-ACS）
- 手術併發症（dissection bailout、perforation、no-reflow、殘餘缺血）
- 顯著貧血、明顯腎損、血流動力學不穩、未控制心律不整/心衰
- **社會因素**：無可靠交通/照顧者、獨居距遠、無法依從用藥

> 台灣實務：另需搭配健保給付認定、機構流程與護理人力共同設計。

---

<!-- _class: divider -->
# Take Home Messages

---

# Take Home Messages

> **1**　SDD 對**嚴選低風險擇期 PCI** 安全 — 14 RCT，MACE/出血/再住院與過夜住院無差異。

> **2**　安全來自**病人選擇**，不是縮短觀察 — 用 ACC 2021 **三段式 checklist**，任一關卡有排除條件就留院。

> **3**　**Radial-first** 是關鍵促成因素 — 出血少、止血快、早下床。

> **4**　併發症多在 **<6h 或 >24h**；**4–6h 觀察 + 次日電話 + 明確返院指引** = 完整安全網。

> **5**　每例約省 **US$5,000**、病人滿意度高，但各院採用率 0–83% — 可改善的**價值缺口**。

---

<!-- _class: ref -->
# 參考文獻

1. Rao SV, Vidovich MI, Gilchrist IC, et al. 2021 ACC Expert Consensus Decision Pathway on Same-Day Discharge After PCI. [*J Am Coll Cardiol*. 2021;77(6):811-825.](https://doi.org/10.1016/j.jacc.2020.11.013)
2. Heyde GS, Koch KT, de Winter RJ, et al. Same-day discharge vs overnight stay after PCI: the EPOS study. [*Circulation*. 2007;115(17):2299-2306.](https://doi.org/10.1161/CIRCULATIONAHA.105.591495)
3. Abdelaal E, Rao SV, Gilchrist IC, et al. Same-day discharge vs overnight hospitalization after uncomplicated PCI: systematic review and meta-analysis. [*JACC Cardiovasc Interv*. 2013;6(2):99-112.](https://doi.org/10.1016/j.jcin.2012.10.008)
4. Nguyen NH, Le TN, Nguyen HTT, et al. Same-day discharge following PCI: systematic review and meta-analysis of RCTs. [*Eur Cardiol*. 2025;20:e19.](https://doi.org/10.15420/ecr.2025.21)
5. Amin AP, Pinto D, House JA, et al. Association of same-day discharge after elective PCI with costs and outcomes. [*JAMA Cardiol*. 2018;3(11):1041-1049.](https://doi.org/10.1001/jamacardio.2018.3029)
6. Bradley SM, Kaltenbach LA, Xiang K, et al. Trends in use and outcomes of same-day discharge following elective PCI. [*JACC Cardiovasc Interv*. 2021;14(15):1655-1666.](https://doi.org/10.1016/j.jcin.2021.05.043)
7. Seto AH, Shroff A, Abu-Fadel M, et al. Length of stay following PCI: SCAI expert consensus document update. [*Catheter Cardiovasc Interv*. 2018;92(4):717-731.](https://doi.org/10.1002/ccd.27637)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC**
