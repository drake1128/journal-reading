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
  section.divider h2 { color: #ffe169; }
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
    font-size: 0.68em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
footer: '謝慕揚 MD, PhD, FESC | HI-PEITHO 中危險肺栓塞導管溶栓 | 2026'
---

<!-- _class: lead -->
# HI-PEITHO
## 超音波導引導管溶栓治療急性中危險肺栓塞
### Ultrasound-Facilitated, Catheter-Directed Fibrinolysis for Acute PE
**謝慕揚 MD, PhD, FESC** | 讀書會共筆整理 | 2026-05-29
NEJM 2026;394:1979-90
[原文連結 (DOI: 10.1056/NEJMoa2516567)](https://doi.org/10.1056/NEJMoa2516567)

---

# 一句話總結

- 對象：**急性中危險 PE** 且具**心肺窘迫徵象**者
- 介入：抗凝血 **+ 超音波導引導管溶栓 (USCDT)** vs 單純抗凝血
- 7 日複合終點（PE 相關死亡 / 心肺失代償或崩潰 / 症狀性復發）：
  - **4.0% vs 10.3%，RR 0.39 (0.20–0.77)，P=0.005**
- 差異**主要來自較少心肺失代償/崩潰**
- 30 日大出血**無顯著增加、無顱內出血**

> 首個證明導管導向治療能改善中危險 PE **臨床結果**的 RCT

---

<!-- _class: divider -->
# 背景與設計

---

# 背景：中危險 PE 的兩難

- 高危險（血流動力學不穩）：共識為早期清除血栓
- **中危險**：看似穩定但有 RV 功能不全 + 惡化風險 → **最佳策略長期不明**
- 全身溶栓（PEITHO）：能防崩潰，但**大出血/顱內出血**增加 → 少用
- **USCDT**：超音波增強纖溶 → 更低 alteplase 劑量、更短輸注 → 理論上更安全
- 過去僅單臂/影像終點，**缺乏臨床結果的 RCT** → HI-PEITHO 補缺口

---

# 研究設計與納入族群

- 多國、適應性、開放標籤 RCT，**主要終點盲性判讀**
- NCT04790370 | Boston Scientific 資助 | 59 中心（美/歐）| 544 人（介入 273 / 對照 271）
- **納入**：CTPA 證實中危險 PE，且
  - **RV/LV ≥ 1.0 + troponin↑**
  - 隨機前 6 小時內 **≥ 2 項心肺窘迫**：SBP ≤110、HR ≥100、RR >20 或低血氧
- **排除**：持續血流動力學不穩定（高危險 PE）

> 平均年齡 58 歲，僅約 10.1% ≥75 歲，平均 NEWS 6.0

---

# 介入與對照

| | 介入組 | 對照組 |
|--|--------|--------|
| 治療 | **EkoSonic USCDT + 抗凝血** | 單純抗凝血 |
| 啟動 | 隨機後 2 小時內（73.3% 達成） | — |
| alteplase | 雙側平均 **16.92 mg**，輸注 **7.16 小時** | — |
| 主要抗凝血 | 未分段肝素 71.6% | 55.7% |

> **設計亮點**：溶栓劑量/時程**標準化**（非術者自由裁量）、抗凝血方案兩組一致 → 結果可複製

---

# 主要療效終點（7 日，ITT）

| 終點 | 介入 (273) | 對照 (271) | RR (95% CI) |
|------|-----------|-----------|-------------|
| **任何主要事件** | **11 (4.0%)** | **28 (10.3%)** | **0.39 (0.20–0.77)** P=0.005 |
| 心肺失代償/崩潰 | 10 (3.7%) | 28 (10.3%) | 0.4 (0.2–0.7) |
| PE 相關死亡 | 3 (1.1%) | 1 (0.4%) | 3.0 (0.3–28.5) |
| 症狀性復發 | 1 (0.4%) | 1 (0.4%) | 1.0 (0.1–15.8) |

> 差異**幾乎全由心肺失代償/崩潰驅動**；死亡與復發人數太少無法單獨下結論

---

# 安全性：關鍵在「不增加顱內出血」

| 出血 | 介入 | 對照 | P 值 |
|------|------|------|------|
| ISTH 大出血（7 日） | 4.1% | 2.2% | 0.32 |
| ISTH 大出血（30 日） | 4.1% | 3.0% | 0.64 |
| **顱內出血** | **0** | **0** | — |

- **救援治療：2.9% vs 9.2%**（對照組更常需升級）
- ICU 收治：71.1% vs 50.2%；住院天數略短
- 30 日任何原因死亡：1.1% vs 0.7%（NS）

> 兩組皆**無顱內出血** → 相較全身溶栓的核心安全優勢

---

<!-- _class: divider -->
# 限制與臨床意義

---

# 限制

- **開放標籤**隨機（以盲性判讀 + 客觀救援標準緩解）
- 事件率/死亡率低 → 無檢力比較次族群或出血差異；**不能對降死亡下結論**
- 族群偏年輕、衰弱度中等、**多為白人**
- 未比較大口徑機械取栓或減量全身溶栓
- 12 個月長期追蹤進行中

---

# Take-home Message

> 在**審慎挑選**、具心肺窘迫徵象的中危險 PE，USCDT + 抗凝血可**顯著減少早期心肺崩潰**，出血安全性可接受（**無顱內出血**）。

- 降低的是「**崩潰**」而非「死亡」
- 須權衡器材成本、ICU 資源、操作可近性
- 病人選擇框架：**RV/LV ≥1.0 + troponin↑ + ≥2 心肺窘迫徵象**
- 在 **PERT 多專科決策**下個別化使用

---

<!-- _class: small-text -->
# 參考文獻

1. Rosenfield K, et al. Ultrasound-Facilitated, Catheter-Directed Fibrinolysis for Acute PE (HI-PEITHO). [*N Engl J Med*. 2026;394(20):1979-1990.](https://doi.org/10.1056/NEJMoa2516567)
2. Klok FA, et al. Rationale and design of the HI-PEITHO study. [*Am Heart J*. 2022;251:43-53.](https://doi.org/10.1016/j.ahj.2022.05.011)
3. Meyer G, et al. Fibrinolysis for patients with intermediate-risk PE (PEITHO). [*N Engl J Med*. 2014;370:1402-1411.](https://doi.org/10.1056/NEJMoa1302097)
4. Konstantinides SV, et al. 2019 ESC guidelines for acute pulmonary embolism. [*Eur Heart J*. 2020;41:543-603.](https://doi.org/10.1093/eurheartj/ehz405)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC**
讀書會共筆整理 · 僅供醫療專業人員教學參考
