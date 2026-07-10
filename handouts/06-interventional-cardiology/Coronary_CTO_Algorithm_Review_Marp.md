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
    font-size: 2.4em;
    text-align: center;
  }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.66em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.85em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 0.6em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.8em; }
  section.ref { font-size: 0.62em; }
  section.ref h1 { font-size: 1.4em; }
footer: '謝慕揚 MD, PhD, FESC | Coronary CTO PCI — Algorithm & 技術文獻彙整 (2015–2026)'
---

<!-- _class: lead -->
# 冠狀動脈 CTO PCI
## Algorithm 與重要技術文獻彙整 (2015–2026)
**謝慕揚 MD, PhD, FESC** | 2026-06-16
讀書會共筆式文獻地圖 — 演算法・技術・評分・實證
[完整講義 (Markdown, 67 篇附超連結)](https://github.com/drake1128/journal-reading)

---

# 為什麼需要「演算法」？

> **核心觀念**：現代 CTO PCI 不是單一技巧，而是**演算法驅動 (algorithm-driven)** 的決策流程，依病灶特徵在四大策略間「早切換 (change early)」。

| 策略 | 全名 | 適用情境 |
|------|------|---------|
| **AWE** | Antegrade Wire Escalation | 短病灶、近端帽清楚、遠端血管佳 |
| **ADR** | Antegrade Dissection & Re-entry | 長病灶 (≥20 mm)、良好遠端著陸區 |
| **RWE** | Retrograde Wire Escalation | 近端帽模糊、可用 interventional collateral |
| **RDR** | Retrograde Dissection & Re-entry (reverse CART) | 複雜、順向失敗、長閉塞 |

---

<!-- _class: divider -->
# §2　Crossing Algorithms
核心演算法地圖

---

# 三大演算法傳承

| 演算法 | 來源 / 年代 | 重點 | 連結 |
|--------|-----------|------|------|
| **Hybrid Algorithm** | 北美 Brilakis 2012 | dual injection + 四象限決策 + early change | [DOI](https://doi.org/10.1016/j.jcin.2012.02.006) |
| **APCTO Club Algorithm** | 亞太 Harding 2017 | 重 antegrade / IVUS / collateral 細節 | [DOI](https://doi.org/10.1016/j.jcin.2017.06.071) |
| **Global Crossing Algorithm** | 全球整合 JACC 2021 | Hybrid + APCTO + EuroCTO 統一框架 | [DOI](https://doi.org/10.1016/j.jacc.2021.05.055) |

> 入門必讀：**Global CTO Crossing Algorithm (JACC State-of-the-Art 2021)** — 目前最廣用的共同語言。

---

# 演算法決策骨架（簡化）

```text
  雙投影評估 (dual injection)
        │
  評估 proximal cap / length / distal vessel / collateral
        │
   ┌────┴─────────────┬──────────────────┐
   │ cap 清楚          │ cap 模糊          │
   │ length <20 mm     │ 或 length ≥20 mm  │
   ▼                   ▼                   ▼
  AWE ───失敗/超時──► ADR            Retrograde (RWE/RDR)
   │                   │                   │
   └──── 任一步驟卡關 → 「早切換」而非硬卡同一招 ◄──┘
```

**關鍵字**：efficiency、change strategy early、避免在單一策略耗盡時間/對比劑/輻射。

---

# 演算法的「忠誠度」與未來

| 主題 | 重點 | 連結 |
|------|------|------|
| **遵循 Global Algorithm** | 遵循初始策略選擇 → 更高成功率/效率 (PROGRESS-CTO) | [PubMed](https://pubmed.ncbi.nlm.nih.gov/41903926/) |
| **遵循 Hybrid Algorithm** | 忠實遵循 → 較佳結果 | [DOI](https://doi.org/10.1016/j.rec.2020.09.009) |
| **子演算法 (algorithms within)** | cap 模糊、balloon-uncrossable 等情境解法 | [DOI](https://doi.org/10.1002/ccd.27987) |
| **Minimalistic Hybrid** | radial-first、小管徑、降併發症 | [DOI](https://doi.org/10.1016/j.ijcard.2018.11.021) |
| **ML 預測成功** | 機器學習預測 antegrade wiring / hybrid 成功 | [DOI](https://doi.org/10.1016/j.jcin.2024.04.043) |

---

<!-- _class: divider -->
# §3　共識與指引
Consensus & Guidelines

---

# 必讀共識文件

| 文件 | 角色 | 連結 |
|------|------|------|
| **Guiding Principles** (Circulation 2019) | 全球「指導原則」：indication・安全・訓練 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.119.039797) |
| **EuroCTO 2019 共識** (EuroIntervention) | 歐洲視角 indication 與技術標準 | [DOI](https://doi.org/10.4244/EIJ-D-18-00826) |
| **Global Safety 共識** (Heart Lung Circ 2024) | 以「安全」為核心：併發症預防 | [DOI](https://doi.org/10.1016/j.hlc.2023.11.030) |
| **CTO-ARC 定義** (Circulation 2021) | 成功/併發症/試驗設計的共同語言 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.120.046754) |
| **鈣化 CTO 專家回顧** (EuroIntervention 2023) | IVL / atherectomy / balloon-undilatable | [DOI](https://doi.org/10.4244/EIJ-D-22-01096) |

---

<!-- _class: divider -->
# §4　技術深入
Antegrade · ADR · Retrograde

---

# Antegrade & Dissection/Re-entry (ADR)

| 文獻 | 重點 | 連結 |
|------|------|------|
| **Antegrade techniques** (Prog Cardiovasc Dis 2025) | wire escalation / parallel wiring | [DOI](https://doi.org/10.1016/j.pcad.2024.07.001) |
| **Dissection Techniques** (CCI 2025) | 最新 ADR 技術總整理 | [DOI](https://doi.org/10.1002/ccd.31573) |
| **"Vessel architecture"** (CCI 2018) | subadventitial space 與 re-entry 概念 | [DOI](https://doi.org/10.1002/ccd.27025) |
| **ADR 趨勢與結果** (JACC Interv 2023) | PROGRESS-CTO 真實世界 | [DOI](https://doi.org/10.1016/j.jcin.2023.09.021) |
| **RECHARGE registry** (Circ Interv 2017) | ADR 在 Hybrid 框架成效 | [DOI](https://doi.org/10.1161/CIRCINTERVENTIONS.116.004791) |
| **CrossBoss First or Last?** (JACC Interv 2018) | CrossBoss 策略思辨 | [DOI](https://doi.org/10.1016/j.jcin.2017.11.022) |

---

# Retrograde（逆向 + reverse CART）

| 文獻 | 重點 | 連結 |
|------|------|------|
| **Retrograde Approach** (Circ Interv 2020) | 權威回顧：collateral・reverse CART（必讀） | [DOI](https://doi.org/10.1161/CIRCINTERVENTIONS.119.008900) |
| **Technical Analysis** (JACC Interv 2023) | 逆向各步驟成功率拆解 (PROGRESS-CTO) | [DOI](https://doi.org/10.1016/j.jcin.2023.08.031) |
| **Reclassifying Bailout** (JACC Interv 2024) | 逆向作為 bailout 的風險與定位 | [DOI](https://doi.org/10.1016/j.jcin.2024.09.051) |
| **Retrograde Carlino** (CCI 2023) | 微量對比劑輔助逆向通過 | [DOI](https://doi.org/10.1002/ccd.30565) |
| **Primary vs Secondary 逆向** (JIC 2022) | 一開始逆向 vs 順向失敗後轉逆向 | [DOI](https://doi.org/10.25270/jic/22.00059) |

---

<!-- _class: divider -->
# §5–6　評分與影像
Risk Scores & Intravascular Imaging

---

# 術前風險與難度評分

| 評分 | 用途 | 連結 |
|------|------|------|
| **J-CTO** (2011) | 預測 30 分鐘內導線通過難度（最廣用） | [DOI](https://doi.org/10.1016/j.jcin.2010.09.024) |
| **PROGRESS-CTO** (2016) | 預測技術成功 | [DOI](https://doi.org/10.1016/j.jcin.2015.09.022) |
| **PROGRESS-CTO Complications** (2016) | 預測圍術期併發症 | [DOI](https://doi.org/10.1161/JAHA.116.004272) |
| **EuroCTO (CASTLE)** (2019) | 2 萬例登錄的成功預測 | [DOI](https://doi.org/10.1016/j.jcin.2018.11.020) |
| **PROGRESS-CTO Perforation** (2023) | 專測冠脈穿孔風險 | [DOI](https://doi.org/10.4244/EIJ-D-22-00593) |
| **JR-CTO**（逆向, 2024) | 預測逆向成功 | [DOI](https://doi.org/10.1016/j.jcin.2024.03.023) |

---

# 血管內影像導引 (IVUS / OCT)

> **旗艦研究**：影像導引 vs 血管攝影導引 → **改善臨床預後**（Hong D, *Circulation* 2023）。

| 文獻 | 重點 | 連結 |
|------|------|------|
| **Prognostic Impact** (Circulation 2023) | 影像導引改善 CTO PCI 預後（隨機資料） | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.123.065876) |
| **Intravascular Imaging** (Interv Cardiol Clin 2026) | 最新影像導引回顧 | [DOI](https://doi.org/10.1016/j.iccl.2025.09.011) |
| **Euro-CTO IVUS registry** (Clin Res Cardiol 2026) | 歐洲 IVUS 實際使用樣態 | [DOI](https://doi.org/10.1007/s00392-025-02788-0) |

**影像三大用途**：① cap puncture 定位 ② re-entry / true lumen 確認 ③ stent 尺寸與貼合優化

---

<!-- _class: divider -->
# §7　臨床實證
為什麼要做 CTO PCI？

---

# 關鍵隨機試驗 (RCTs)

> **解讀**：多數**硬終點 (death/MI) 為 neutral**，但**心絞痛 / QoL 改善一致** → CTO PCI 是「**症狀導向**」的合理選擇。勿把 neutral 誤讀為「無效」（注意 crossover / power）。

| 試驗 | 結果方向 | 連結 |
|------|---------|------|
| **DECISION-CTO** (Circulation 2019) | MACE 無差異（高 crossover、提早停收） | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.118.031313) |
| **EURO-CTO** (Eur Heart J 2018) | ✅ 心絞痛 / QoL 改善；硬終點無差異 | [DOI](https://doi.org/10.1093/eurheartj/ehy220) |
| **EXPLORE** (JACC 2016) | STEMI+非IRA CTO：整體 LVEF 無改善 | [DOI](https://doi.org/10.1016/j.jacc.2016.07.744) |
| **ISCHEMIA — CTO 次分析** (JACC 2025) | 侵入 vs 保守，最新次族群 | [DOI](https://doi.org/10.1016/j.jacc.2025.01.029) |

---

# 三句話總結

> **1. 演算法先行**：以 Global Crossing Algorithm 把 antegrade / ADR / retrograde 串成「早切換」流程。

> **2. 影像 + 評分護航**：J-CTO / PROGRESS-CTO 分層風險；IVUS 解決 cap 模糊、re-entry、stent 優化（Circulation 2023 證實改善預後）。

> **3. 實證定位**：硬終點多 neutral，但**心絞痛與 QoL 穩定改善** → 症狀導向、由有經驗團隊執行（Global Safety 2024）。

---

<!-- _class: ref -->
# 參考文獻 (1/2)

- Wu EB, et al. Global CTO Crossing Algorithm. *J Am Coll Cardiol.* 2021. [DOI](https://doi.org/10.1016/j.jacc.2021.05.055) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34412818/)
- Brilakis ES, et al. A percutaneous treatment algorithm for crossing CTOs. *JACC Cardiovasc Interv.* 2012. [DOI](https://doi.org/10.1016/j.jcin.2012.02.006)
- Harding SA, et al. APCTO Club Algorithm. *JACC Cardiovasc Interv.* 2017. [DOI](https://doi.org/10.1016/j.jcin.2017.06.071)
- Riley RF, et al. Algorithms within the algorithm. *Catheter Cardiovasc Interv.* 2019. [DOI](https://doi.org/10.1002/ccd.27987)
- Brilakis ES, et al. Guiding Principles for CTO PCI. *Circulation.* 2019. [DOI](https://doi.org/10.1161/CIRCULATIONAHA.119.039797)
- Galassi AR, et al. EuroCTO Club 2019 consensus. *EuroIntervention.* 2019. [DOI](https://doi.org/10.4244/EIJ-D-18-00826)
- Wu EB, et al. Global Safety Recommendations. *Heart Lung Circ.* 2024. [DOI](https://doi.org/10.1016/j.hlc.2023.11.030)
- Ybarra LF, et al. CTO-ARC Consensus. *Circulation.* 2021. [DOI](https://doi.org/10.1161/CIRCULATIONAHA.120.046754)
- Mashayekhi KA, et al. Heavily calcified CTO (European CTO Club). *EuroIntervention.* 2023. [DOI](https://doi.org/10.4244/EIJ-D-22-01096)
- Megaly M, et al. Retrograde Approach to CTO PCI. *Circ Cardiovasc Interv.* 2020. [DOI](https://doi.org/10.1161/CIRCINTERVENTIONS.119.008900)
- Azzalini L, et al. Subadventitial techniques / vessel architecture. *Catheter Cardiovasc Interv.* 2018. [DOI](https://doi.org/10.1002/ccd.27025)

---

<!-- _class: ref -->
# 參考文獻 (2/2)

- Maeremans J, et al. RECHARGE Registry (ADR). *Circ Cardiovasc Interv.* 2017. [DOI](https://doi.org/10.1161/CIRCINTERVENTIONS.116.004791)
- Rempakos A, et al. ADR Trends and Outcomes. *JACC Cardiovasc Interv.* 2023. [DOI](https://doi.org/10.1016/j.jcin.2023.09.021)
- Allana SS, et al. Retrograde Technical Analysis. *JACC Cardiovasc Interv.* 2023. [DOI](https://doi.org/10.1016/j.jcin.2023.08.031)
- Morino Y, et al. J-CTO Score. *JACC Cardiovasc Interv.* 2011. [DOI](https://doi.org/10.1016/j.jcin.2010.09.024)
- Christopoulos G, et al. PROGRESS-CTO Score. *JACC Cardiovasc Interv.* 2016. [DOI](https://doi.org/10.1016/j.jcin.2015.09.022)
- Szijgyarto Z, et al. EuroCTO (CASTLE) Score. *JACC Cardiovasc Interv.* 2019. [DOI](https://doi.org/10.1016/j.jcin.2018.11.020)
- Kostantinis S, et al. PROGRESS-CTO Perforation Score. *EuroIntervention.* 2023. [DOI](https://doi.org/10.4244/EIJ-D-22-00593)
- Tanaka H, et al. JR-CTO Score. *JACC Cardiovasc Interv.* 2024. [DOI](https://doi.org/10.1016/j.jcin.2024.03.023)
- Hong D, et al. Intravascular Imaging-Guided CTO PCI. *Circulation.* 2023. [DOI](https://doi.org/10.1161/CIRCULATIONAHA.123.065876)
- Lee SW, et al. DECISION-CTO. *Circulation.* 2019. [DOI](https://doi.org/10.1161/CIRCULATIONAHA.118.031313)
- Werner GS, et al. EURO-CTO. *Eur Heart J.* 2018. [DOI](https://doi.org/10.1093/eurheartj/ehy220)
- Henriques JP, et al. EXPLORE Trial. *J Am Coll Cardiol.* 2016. [DOI](https://doi.org/10.1016/j.jacc.2016.07.744)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
完整講義（67 篇，含全文/PMID/DOI 超連結）見 handout `.md`
**謝慕揚 MD, PhD, FESC**
