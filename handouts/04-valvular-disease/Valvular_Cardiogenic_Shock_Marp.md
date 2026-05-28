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
footer: '謝慕揚 MD, PhD, FESC | 瓣膜性心源性休克 VCS | 2024'
---

<!-- _class: lead -->
# 瓣膜性心源性休克 (VCS)
## 臨床特徵與預後 — Cleveland Clinic CICU 12 年世代
### Characteristics and Outcomes of Patients With Valvular Cardiogenic Shock
**謝慕揚 MD, PhD, FESC** | 讀書會共筆整理 | 2026-05-29
JACC: Advances 2024;3(11):101303
[原文連結 (DOI: 10.1016/j.jacadv.2024.101303)](https://doi.org/10.1016/j.jacadv.2024.101303)

---

# 一句話總結

- Cleveland Clinic CICU 12 年、2,754 例心源性休克中，**16% 為瓣膜性 (VCS)**
- VCS 較年長、以**原生瓣膜 + 主動脈瓣**病變為主
- 短期/1 年死亡率高於非 VCS（**1 年 44% vs 37%**），但**校正共病後 VCS 非獨立危險因子**
- **接受瓣膜針對性介入者預後遠優於僅內科治療**（純內科 1 年死亡 HR 3.78），**外科最佳**

> 觀察性研究：「介入較好」需留意**選擇偏差**

---

<!-- _class: divider -->
# 背景與方法

---

# 背景與定義

- CS 多數研究侷限**心梗後**；**原發瓣膜障礙致 CS 正增加**（人口老化、人工瓣膜增多、心內膜炎）
- **VCS 定義**：急性嚴重原發瓣膜障礙 / 急性合併慢性惡化，為 CS **主要病因**
- **排除**：LV 功能不全的功能性 MR；混合型休克 (SVR <800)
- 常見情境：腱索斷裂、心內膜炎致瓣膜破壞、生物瓣退化、瓣膜血栓

---

# 研究設計

- 單中心、**回溯性世代**；Cleveland Clinic 24 床封閉式 CICU；2010–2021
- CS 診斷即時（SBP <90 / 需升壓劑或 MCS / RHC：PCWP ≥15 且 CI ≤2.2 + 灌流不足）
- 以**首份 TTE** 判定受累瓣膜、原生/人工、病灶性質
- 終點：**1 年全因死亡**（次要 30 日）
- 統計：KM/log-rank、Cox 校正、**1:1 傾向配對**、Rosenbaum bounds 敏感度

---

# 族群特徵（VCS vs 非 VCS）

| 特徵 | VCS (442) | 非 VCS (2,312) | P |
|------|-----------|----------------|---|
| 中位年齡 | 70 | 64 | <0.001 |
| 女性 | 40.3% | 32.1% | 0.001 |
| 曾瓣膜手術 | 32.6% | 8% | <0.001 |
| 峰值 troponin T | **0.11** | 0.41 | <0.001 |
| 峰值 lactate | 4.6 | 4.2 | 0.029 |

> 重症程度高（39% 機械通氣、38% MCS），但 **troponin 反而低** → 休克機轉為瓣膜血流動力學崩潰而非心肌壞死

---

# 瓣膜型態與治療策略

| 受累瓣膜 / 病灶 | 比例 |
|------|------|
| 原生瓣膜障礙 (NVD) | **71%** |
| 人工瓣膜障礙 | 29% |
| 主動脈瓣位置 | **64%** |
| 二尖瓣 / 三尖瓣 | 33% / 3% |
| 逆流 / 狹窄 / 混合 | 43% / 36% / 21% |

| 治療策略 | 比例 |
|------|------|
| 純內科 | 40% |
| 外科 | 38% |
| 經導管（BAV 47%、TAVR 27%…） | 22% |

---

# 預後：死亡率

| 終點 | VCS | 非 VCS | P |
|------|-----|--------|---|
| 1 年死亡 | **44%** | 37% | <0.001 |
| 30 日死亡 | **28%** | 20% | <0.001 |

- 校正共病後，VCS 本身**非** 1 年死亡獨立危險因子（HR 1.13，P=0.15）

| 病灶 | 1 年死亡 | 30 日死亡 |
|------|---------|----------|
| AS / MS（狹窄最差） | 55% / **56%** | 31% / **50%** |
| AR / MR | 32% / 35% | 21% / 23% |

---

# 預後：治療策略是關鍵

| 比較（VCS 病人） | HR (95% CI) | P |
|------|------|---|
| 純內科 vs 任何介入（校正） | **3.78 (2.72–5.27)** | <0.001 |
| 純內科 vs 任何介入（傾向配對） | 3.44 (2.16–5.47) | <0.001 |

- **外科介入長期存活最佳**，經導管居中，純內科最差
- 敏感度：需 Gamma > 2 的未測量混淆才能解釋掉關聯 → 對隱性偏差具一定穩健性

> **但**：較年輕、共病少者才被選去手術 → **選擇偏差**仍是主要解讀陷阱

---

<!-- _class: divider -->
# 限制與臨床意義

---

# 限制

- **單中心、回溯性、觀察性** → 需外部驗證，無法排除未測量混淆
- **治療選擇偏差**：「介入較好」可能部分反映病人選擇而非因果
- VCS 為回溯判定；排除 SVR <800 可能漏掉部分病人
- 死亡資料來自院內紀錄 → 可能**低估**
- 三尖瓣 VCS 等小亞群結論受限

---

# Take-home Message

> CICU 心源性休克中**約 1/6 為瓣膜性**；**主動脈瓣、原生瓣膜、狹窄性病灶預後最差**。死亡率差異**主要來自共病**而非「瓣膜性」本身。

- 「不手術」常非治療惰性，而是**無法安全手術**
- 這群病人正是**擴大緊急/急診經導管治療**（TAVR、TEER、valve-in-valve、緊急 BAV 過渡）+ **及早轉介高量瓣膜中心**的潛在受惠者
- 因果結論受限於觀察性設計與選擇偏差

---

<!-- _class: small-text -->
# 參考文獻

1. Nair RM, et al. Characteristics and Outcomes of Patients With Valvular Cardiogenic Shock. [*JACC Adv*. 2024;3(11):101303.](https://doi.org/10.1016/j.jacadv.2024.101303)
2. van Diepen S, et al. Contemporary management of cardiogenic shock: AHA scientific statement. [*Circulation*. 2017;136(16):e232-e268.](https://doi.org/10.1161/CIR.0000000000000525)
3. Otto CM, et al. 2020 ACC/AHA guideline for valvular heart disease. [*Circulation*. 2021;143(5):e72-e227.](https://doi.org/10.1161/CIR.0000000000000923)
4. Tang GHL, et al. Survival following TEER in patients with cardiogenic shock: a nationwide analysis. [*J Am Heart Assoc*. 2021;10(8):e019882.](https://doi.org/10.1161/JAHA.120.019882)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC**
讀書會共筆整理 · 僅供醫療專業人員教學參考
