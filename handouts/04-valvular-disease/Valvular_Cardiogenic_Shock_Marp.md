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
  section.lead a { color: #8fc9ff; }
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
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
footer: '謝慕揚 MD, PhD, FESC | Valvular Cardiogenic Shock | 2024'
---

<!-- _class: lead -->

# Valvular Cardiogenic Shock
## 瓣膜性心因性休克的臨床特徵與預後

**謝慕揚 MD, PhD, FESC** | 2026-07-09

Cleveland Clinic CICU 世代研究 (2010–2021)｜JACC: Advances 2024

[原文連結：JACC Adv. 2024;3(11):101303 (DOI)](https://doi.org/10.1016/j.jacadv.2024.101303)

---

# 為什麼要談 VCS？

- **心因性休克 (CS)** 高異質性、住院死亡率居高不下；隨機試驗多集中在 **AMI 後**
- AMI 仍是 CS 最常見病因，但**原發瓣膜功能障礙**造成的 CS 正在**增加**
- **VCS** 是獨特、被忽視、真實世界預後從未被系統性報告的次族群

> **為何 VCS 上升？** 人口老化 × 追蹤不足 × 人工瓣膜病人激增 × 靜脈藥物濫用 (IE)

---

# VCS 的機轉是異質的

| 瓣膜型態 | 典型情境 |
|----------|----------|
| **自體瓣膜** | 「無準備心室」上的急性惡化：黏液樣 MV 的**腱索斷裂**、IE 的急性瓣膜關閉不全 |
| **生物瓣膜** | 漸進退化卻突發失能；脆弱族群快速退化、災難性失能 |
| **機械瓣膜** | 結構失效罕見，但**急性瓣膜血栓**風險持續 |

> 經導管治療進步 → 對手術高風險 VCS 病人提供新的根治選項

---

<!-- _class: divider -->
# 研究方法與族群定義

---

# 研究設計

- **地點**：Cleveland Clinic 24 床封閉式 CICU
- **期間**：2010/01/01 – 2021/12/31，回溯、單中心、EMR 辨識

**CS 診斷（即時判定）** — 符合任一：

```text
收縮壓 < 90 mmHg
  或 需血管加壓劑/機械輔助維持血流動力學
  或 PCWP ≥ 15 mmHg 且 CI ≤ 2.2 L/min/m²
  ＋ 末梢器官灌流不足徵象
```

---

# VCS 的定義（關鍵）

> **VCS** = 急性重度原發瓣膜障礙，或慢性瓣膜病變的**急性惡化**，被判定為此次 CICU 入院 CS 的**主要病因**

**特別排除：**

- **功能性 MR**（因 LV 功能不良）→ 不算 VCS
- **混合型休克**（SVR < 800 dyn·s/cm⁵）→ 排除

以入 CICU 後**第一次完整 TTE** 判定：瓣膜位置、自體/人工、逆流/狹窄/混合

---

<!-- _class: divider -->
# 發生率與基本特徵

---

# 族群：2,754 位 CS 中 16% 為 VCS

- 辨識 2,820 位 CS → 排除 44 疑似敗血、22 資料不全
- **最終 2,754 位 CS**

| 分組 | 人數 | 比例 |
|------|------|------|
| **VCS** | **442** | **16%** |
| 非 VCS | 2,312 | 84% |

---

# VCS vs 非 VCS 基本特徵

| 特徵 | VCS | 非 VCS | p |
|------|-----|--------|---|
| 年齡中位 (歲) | **70** | 64 | <0.001 |
| 女性 (%) | **40.3** | 32.1 | 0.001 |
| 心房顫動 (%) | **57.7** | 48.6 | 0.001 |
| COPD (%) | **25.8** | 20.3 | 0.012 |
| 曾瓣膜置換/修補 (%) | **32.6** | 8.0 | <0.001 |
| 尖峰 Troponin T (ng/mL) | **0.11** | 0.41 | <0.001 |
| 尖峰 Lactate (mmol/L) | **4.6** | 4.2 | 0.029 |

> **鑑別線索**：Troponin **偏低** + Lactate **偏高** + 瓣膜手術史 → 想到 VCS

---

# VCS 一樣是「真正危重」

| 支持措施 | VCS 使用比例 |
|----------|-------------|
| 機械通氣 | 39.4% |
| 暫時性機械循環支持 (MCS) | 37.6% |
| 血管加壓劑 / 強心劑 | 47.3% |

> 上述比例與非 VCS **相似** → VCS 並非較輕症，而是同等危重的族群

---

<!-- _class: divider -->
# 瓣膜位置與型態

---

# 自體佔多數、主動脈瓣最常見

**自體 vs 人工（n = 442）**

| 型態 | 人數 | 比例 |
|------|------|------|
| **自體 (NVD)** | 313 | **71%** |
| 人工 (prosthetic) | 129 | 29% |

**位置**：主動脈瓣 **64%** ＞ 二尖瓣 33% ＞ 三尖瓣 3%

---

# NVD vs 人工瓣膜

| 特徵 | NVD | 人工瓣膜 | p |
|------|-----|----------|---|
| 年齡中位 (歲) | **72** | 66 | 0.001 |
| 慢性腎臟病 (%) | **45.7** | 35.0 | 0.047 |
| 先前 PPM/ICD (%) | 15.7 | **27.1** | 0.008 |

> 兩組在右心導管、MCS、機械通氣使用率**無顯著差異**

---

# 病灶型態與治療策略

**病灶性質**：逆流 **43%** ＞ 狹窄 36% ＞ 混合 21%

**治療策略**：藥物 **40%** ／ 手術 38% ／ 經導管 22%

| 經導管術式 (n=97) | 比例 |
|-------------------|------|
| 主動脈瓣氣球擴張 (BAV) | **47%** |
| TAVR | 27% |
| 二尖瓣介入 | 12% |
| 多瓣膜介入 | 11% |

> 入 CICU 至經導管治療中位 **7 天**；經導管組近半是 BAV（暫時性 salvage）

---

<!-- _class: divider -->
# 死亡率結果

---

# VCS 死亡率高於非 VCS

| 結果 | VCS | 非 VCS | p |
|------|-----|--------|---|
| **1 年全因死亡** | **44%** | 37% | <0.001 |
| **30 天全因死亡** | **28%** | 20% | <0.001 |

VCS 中位存活時間：999 天 (Q1–Q3: 429–1,836)

> **但校正共病後**，VCS 本身**非**獨立死亡因子：
> **adjusted HR 1.13 (95% CI 0.96–1.33; p = 0.15)**
> → 高死亡率來自**年長、共病多**的族群本質，而非「瓣膜性」本身

---

# 狹窄性病灶預後最險惡

| 病灶 | 30 天死亡 | 1 年死亡 |
|------|-----------|----------|
| **主動脈瓣狹窄 (AS)** | 31% | **55%** |
| 主動脈瓣逆流 (AR) | 21% | 32% |
| 二尖瓣逆流 (MR) | 23% | 35% |
| **二尖瓣狹窄 (MS)** | **50%** | **56%** |

- 主動脈瓣病變預後 **差於** 二尖瓣病變
- **狹窄性病灶 (AS、MS) 預後最差**

---

# 治療策略：手術 > 經導管 > 藥物

**藥物治療 vs 任何介入（經導管或外科）：**

| 分析 | HR (95% CI) | p |
|------|-------------|---|
| 多變項 Cox 校正 | **3.78 (2.72–5.27)** | <0.001 |
| 傾向分數配對 | **3.44 (2.16–5.47)** | <0.001 |

- 敏感度分析：需未測混淆因子 **Γ > 2** 才能解釋掉 → 結果穩健

> **解讀陷阱**：觀察性資料，開刀者本就較年輕、共病少。真正訊息是——**能被選來接受介入者預後遠優於只能藥物治療者**

---

<!-- _class: divider -->
# 臨床啟示

---

# 臨床啟示 (1/2)

1. **VCS 佔 CICU 中 CS 的 16%**，1 年死亡 44%，不容忽視
2. 自體 (71%)、主動脈瓣 (64%)、逆流 (43%) 為主
3. **手術後預後可接受**：初期手術風險後，追蹤期額外死亡很少
4. **系統性錯失機會**：即使高量能中心，仍有大比例不被視為手術候選；這些病人 MCS/插管率高 → **非治療惰性，而是無法達成成功手術**

---

# 臨床啟示 (2/2)

5. **早期辨識、轉診至高量能瓣膜中心**可能改善手術候選資格與預後
6. **擴大緊急情境下經導管治療**（TAVR、valve-in-valve）→ 擴大能接受根治的族群
7. **人工瓣膜功能障礙將增加**（2019 美國 >130,000 例主動脈瓣置換）→ valve-in-valve 是年長高風險病人的更佳選項

---

# Take-Home Messages

> **1.** 每 6 位 CS 有 1 位是 VCS；**Trop 低 + Lactate 高 + 瓣膜手術史**應提高警覺

> **2.** 自體/主動脈瓣/逆流為主；但**狹窄病灶（AS、MS）最險惡**

> **3.** 校正後 VCS 非獨立死亡因子（HR 1.13）— 死亡來自族群本質

> **4.** **能接受任何介入者預後遠優於藥物治療**（HR 3.78 / 配對 3.44）

> **5.** 早期辨識、轉診、擴大經導管治療角色是關鍵

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

[Nair RM, et al. JACC Adv. 2024;3(11):101303 — DOI](https://doi.org/10.1016/j.jacadv.2024.101303)

---

<!-- _class: small-text -->

# 參考文獻

1. Nair RM, Chawla S, Alkhalaileh F, Abdelghaffar B, Bansal A, Higgins A, Lee R, Rampersad P, Khot UN, Jaber WA, Reed GW, Cremer PC, Menon V. Characteristics and Outcomes of Patients With Valvular Cardiogenic Shock. [*JACC Adv*. 2024;3(11):101303.](https://doi.org/10.1016/j.jacadv.2024.101303) PMID: [39429239](https://pubmed.ncbi.nlm.nih.gov/39429239/); PMCID: PMC11490668

*本投影片為讀書會共筆整理，僅供醫療專業人員教學參考，非臨床診療指引。*
