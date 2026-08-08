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
    font-size: 2.4em;
    text-align: center;
  }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.68em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.86em;
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
  section.small-text { font-size: 0.8em; }
footer: '謝慕揚 MD, PhD, FESC | Deprescribing in CVD Polypharmacy | AHA 2026'
---

<!-- _class: lead -->

# 心血管病人多重用藥的減藥策略
## Deprescribing in CVD Experiencing Polypharmacy

**謝慕揚 MD, PhD, FESC** | 2026-07-11

AHA Scientific Statement｜Circulation 2026;154

[原文連結：DOI 10.1161/CIR.0000000000001459](https://doi.org/10.1161/CIR.0000000000001459)

---

# 核心觀念

- **多重用藥 (polypharmacy)** = 長期用 **≥5 種**藥；**hyperpolypharmacy** = **≥10 種**
- CVD 病人是所有疾病中**多重用藥盛行率最高**的族群
- 與不當處方、順從性下降、CVD 控制變差、生活品質降低、不良預後相關

> **減藥 (deprescribing)** = 在監督下停用或減量藥物。AHA 背書為**高品質心血管照護的關鍵一環**。目標不是「少開藥」，而是**提升處方品質**。

---

# 多重用藥有多普遍？

| 族群 | 盛行率 |
|------|--------|
| 美國成人 1999→2018 | 8.2% → **17.1%** |
| ≥65 歲 (2009→2018) | 23.5% → **44.1%** |
| **CVD 成人 (2017)** | **61.7%（最高）** |
| HF 病人 | 74%（門診）～84%（住院）|
| HFpEF 年長者 | hyperpoly **76%**；100% ≥1 PIM |

> 驅動因素：多重共病、GDMT 疊加、多開方者、照護轉銜不良、**處方瀑布**、自動續方

---

# GDMT 如何堆疊藥量

| 疾病 | 核心藥物 |
|------|---------|
| 高血壓 | Thiazide / ACEI·ARB / DHP CCB / MRA |
| HFrEF | β-blocker / ARNI·ACEI·ARB / MRA / SGLT2i |
| 缺血性心臟病 | Aspirin / β-blocker / ACEI·ARB / nitrate / P2Y₁₂ |
| AF | 抗凝血劑 / β-blocker / non-DHP CCB |
| 血脂異常 | Statin (+ezetimibe/PCSK9i) |

共病連鎖：高血壓/血脂 → 冠心病 → HF → AF，每環各有 GDMT ＋ 非心血管共病 → **多重用藥難以避免**

> 一線希望：GLP-1 RA、SGLT2i「一藥多用」；長效注射劑取代每日口服

---

# 多重用藥的不良後果

- **臨床事件**：年長 AF（≥9 種藥）全因死亡、大出血、出血風險↑ → 惡性循環（多重用藥→不順從→ADE）
- **HFpEF**：hyperpolypharmacy → 住院率↑
- **順從性**：藥物數與順從率呈**反比**
- **經濟**：年長 CVD＋多重用藥 年度醫療支出 **2 倍（$19,068 vs $8,815）**
- **衰弱 (frailty)**：與多重用藥雙向關係，併存預後更差

---

<!-- _class: divider -->
# 誰該考慮減藥？

---

# 四類病人（減藥觸發點）

1. **已發生 ADE** — 常非特異/無症狀，易誤為老化；**反覆跌倒**要警覺
2. **多重用藥 / PIM** — 藥物已無適應症、效益有限、風險不成比例、不符病人優先順序；合併認知障礙者優先
3. **處方瀑布** — 新藥後出現新症狀 → 想是否為藥物引起，別再加一顆藥
4. **安寧 / 末期** — 目標轉向症狀控制與減少負擔；反覆住院也是時機

---

# 找出可減的藥：調節 + 工具

**藥物調節 (medication reconciliation) 4 步驟：**

```text
Verify（最完整用藥史）→ Identify（比對差異）
→ Reconcile（協同決策）→ Communicate（記錄溝通）
```

**辨識 PIM 工具（Table 2）：**
- **Explicit**（明確規則）：AGS Beers、STOPP/START、FORTA
- **Implicit**（臨床判斷）：MAI
- 「病人為中心 (patient-in-focus)」列表法 RCT 結果較佳

> 工具**輔助而非取代**臨床判斷

---

# 善用「過期適應症」

| 情境 | 可能不再需要的藥 |
|------|----------------|
| AF 房室結電燒後 | rate-slowing 藥、抗心律不整藥 |
| PCI 後心絞痛已解 | 長效硝酸鹽、ranolazine |
| PCI 後（技術進步）| 縮短 DAPT 療程 |
| MI 保留 EF | β-blocker 長期角色不確定 |
| 初級預防 | **aspirin 風險可能>效益** |

---

# Table 3：可減的心血管藥物

| 藥物 | 理由 | 漸減 |
|------|------|------|
| α-blocker | 姿勢性低血壓 | 否 |
| clonidine | CNS 反應、低血壓、心搏過緩 | **是** |
| 抗心律不整藥 | 電燒後、永久 AF、HFrEF | 否 |
| 抗凝血劑 | LAA 關閉後、VTE 完成、風險>效益 | 否 |
| aspirin | 初級預防、已用抗凝、>100mg | 否 |
| **β-blocker** | 無併發症 MI 保留 EF >3y、HFpEF、AVN 電燒後 | **是** |
| digoxin | 進階腎病毒性 (eGFR<30) | 否 |
| 長效硝酸鹽/ranolazine | PCI 後無症狀 | 否 |

---

# Table 3：可減的非心血管藥物

| 藥物 | 理由 |
|------|------|
| 抗膽鹼藥 (>1) | 認知障礙、跌倒、譫妄 |
| CNS 活性藥 (≥3) | 跌倒、骨折 |
| gabapentinoids | HF、跌倒 |
| **NSAIDs（慢性）** | HF、缺血性心臟病、GI 出血 |
| PPI（長期無症狀）| C. diff、肺炎、骨折風險 |
| thiazolidinediones | HF |
| 保健品/維生素 | 紅麴＋statin、魚油、CoQ10… |

> **治療競爭**經典例：NSAID 治關節炎卻惡化 HF/冠心病

---

# 如何安全地減藥（漸減與 ADWE）

- 減藥需**監督**，留意**藥物戒斷事件 (ADWE)** 與反彈，多可用**漸減**避免
- **β-blocker**：突停高劑量 metoprolol 有**猝死**風險 → 受體半衰期 1.5 天，**每週減 50%**
- **Amiodarone**：半衰期 60 天 → **不需漸減**
- 減藥期間**監測**原疾病新/惡化症狀（ADWE）→ 可放慢、停在低劑量、或重新啟用

---

# 共享決策 + 團隊

- **92%** Medicare 病人願意停掉至少 1 種藥；HFpEF **90%** 願意；藥物越多意願越高
- SDM 要同時講**效益**（少副作用、順從性/生活品質）與**風險**（症狀復發、疾病進展）
- **團隊減藥**：藥師、護理師辨識 PIM、設計漸減、衛教/監測 ADWE
- 藥師主導計畫 RCT：出院後用藥數與 PIM 顯著↓、維持至 90 天；**社區藥師**尤其有價值

---

# 減藥的安全性證據

| 情境 | 證據 |
|------|------|
| **Aspirin 停用** | 初級預防：停用者 MACE 可能↑ |
| **Statin 停用** | 餘命<1 年似安全；長期不明，非隨機顯示 MACE↑ |
| **抗高血壓藥停用** | **HF 風險↑**；MI/中風/死亡無差異 |
| **HFimpEF 停 GDMT** | HFrEF **復發** |

> 決策必須**個別化**＋ SDM ＋**密切監測** ＋多專科團隊；仍需更高品質證據

---

# Take-Home Messages

> **1.** CVD 多重用藥盛行率最高（61.7%）；＝更多 ADE、更差順從、2 倍支出

> **2.** 減藥＝提升處方品質，是 optimal prescribing 的一部分（AHA 背書）

> **3.** 四觸發點：ADE、PIM、處方瀑布、安寧；用 Beers / STOPP-START 找 PIM

> **4.** 漸減有學問：β-blocker 每週減 50%；amiodarone 免漸減；監測 ADWE

> **5.** 92% 病人願停藥；SDM ＋ 藥師/護理師團隊是關鍵

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

[DiDomenico RJ, et al. AHA Scientific Statement. Circulation 2026;154 — DOI](https://doi.org/10.1161/CIR.0000000000001459)

---

<!-- _class: small-text -->

# 參考文獻

1. DiDomenico RJ, Marrs JC, Bress AP, et al; on behalf of the AHA Clinical Pharmacology Committee. Deprescribing in Patients With Cardiovascular Disease Experiencing Polypharmacy: A Scientific Statement From the American Heart Association. [*Circulation*. 2026;154:e00–e00.](https://doi.org/10.1161/CIR.0000000000001459)
2. Krishnaswami A, et al. Deprescribing in older adults with cardiovascular disease. [*J Am Coll Cardiol*. 2019;73:2584–2595.](https://doi.org/10.1016/j.jacc.2019.03.467)
3. Scott IA, et al. Reducing inappropriate polypharmacy: the process of deprescribing. [*JAMA Intern Med*. 2015;175:827–834.](https://doi.org/10.1001/jamainternmed.2015.0324)
4. O'Mahony D, et al. STOPP/START criteria version 3. [*Eur Geriatr Med*. 2023;14:625–632.](https://doi.org/10.1007/s41999-023-00777-y)

*本投影片為讀書會共筆整理，僅供醫療專業人員教學參考，非臨床診療指引。*
