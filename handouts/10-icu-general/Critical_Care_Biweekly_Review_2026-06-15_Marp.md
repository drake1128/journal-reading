---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Microsoft JhengHei', 'PingFang TC', 'Noto Sans TC', sans-serif;
    background-color: #ffffff;
    color: #2d3436;
    font-size: 0.95em;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 2.0em; border-bottom: none; }
  section.lead h2 { color: #b0c4de; font-size: 1.1em; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #b0c4de; }
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
  section.divider h2 { color: #dfe6e9; font-size: 1.1em; text-align: center; }
  section.divider h3 { color: #dfe6e9; font-size: 0.9em; text-align: center; }
  section.abbr table { font-size: 0.72em; width: 100%; }
  section.abbr th { background-color: #555555; color: white; padding: 5px 8px; }
  section.abbr td { padding: 3px 8px; }
  section.abbr tr:nth-child(even) { background-color: #f0f4f8; }
  section.abbr h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.4em; }
  section.ref { font-size: 0.62em; }
  section.ref h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.4em; }
  section.ref ol { padding-left: 1.2em; }
  section.ref li { margin-bottom: 0.3em; }
  section.small-text { font-size: 0.82em; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; font-size: 1.0em; }
  h3 { color: #555555; font-size: 0.9em; }
  table { font-size: 0.72em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.85em;
    color: #2d3436;
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
  ul li { margin-bottom: 0.25em; }
  ol li { margin-bottom: 0.25em; }
footer: '謝慕揚 MD, PhD, FESC | Critical Care 雙週期刊回顧 | 2026-06-15'
---

<!-- _class: lead -->
# Critical Care 雙週期刊回顧
## Biweekly Critical Care Literature Review
## 2026-06-01 ～ 2026-06-15

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-06-15**

ICM · Critical Care · CCM · Lancet Respir Med · AJRCCM · Chest · Resuscitation · Shock

---

<!-- _class: abbr -->
# 常用縮寫對照（一）

| 縮寫 | 全名 | 中文 |
|------|------|------|
| ICU | Intensive Care Unit | 加護病房 |
| RCT | Randomized Controlled Trial | 隨機對照試驗 |
| ARDS | Acute Respiratory Distress Syndrome | 急性呼吸窘迫症候群 |
| VAP | Ventilator-Associated Pneumonia | 呼吸器相關肺炎 |
| SBT | Spontaneous Breathing Trial | 自發呼吸試驗 |
| NMB | Neuromuscular Blockade | 神經肌肉阻斷 |
| PPC | Postoperative Pulmonary Complications | 術後肺部併發症 |
| SSD | Subglottic Secretion Drainage | 聲門下分泌物引流 |
| PoCLUS | Point-of-Care Lung Ultrasound | 床邊肺部超音波 |
| SOFA | Sequential Organ Failure Assessment | 連續器官衰竭評估 |
| AKI | Acute Kidney Injury | 急性腎損傷 |
| ECMO | Extracorporeal Membrane Oxygenation | 體外膜氧合 |
| CPR | Cardiopulmonary Resuscitation | 心肺復甦術 |
| PE | Pulmonary Embolism | 肺栓塞 |
| OHCA | Out-of-Hospital Cardiac Arrest | 院外心跳停止 |

---

<!-- _class: abbr -->
# 常用縮寫對照（二）

| 縮寫 | 全名 | 中文 |
|------|------|------|
| MDRO | Multidrug-Resistant Organism | 多重抗藥菌 |
| CRT | Capillary Refill Time | 微血管回充時間 |
| PPI | Peripheral Perfusion Index | 周邊灌流指數 |
| MS | Mottling Score | 皮膚花斑評分 |
| NGAL | Neutrophil Gelatinase-Associated Lipocalin | 中性球明膠酶相關脂質運載蛋白 |
| POLST | Physician Orders for Life-Sustaining Treatment | 醫師生命維持治療醫囑 |
| PIC | Perceived Inappropriateness of Care | 不適切照護感知 |
| ACP | Advance Care Planning | 預立照護計畫 |
| PTSD | Post-Traumatic Stress Disorder | 創傷後壓力症候群 |
| RRT | Renal Replacement Therapy | 腎臟替代療法 |
| TRALI | Transfusion-Related Acute Lung Injury | 輸血相關急性肺損傷 |
| PBM | Patient Blood Management | 病人血液管理 |
| DTFmax | Maximal Diaphragm Thickening Fraction | 最大橫膈增厚分率 |
| ICU-AW | ICU-Acquired Weakness | 加護病房獲得性衰弱 |
| CFS | Clinical Frailty Scale | 臨床衰弱量表 |

---

# 重點摘要 Key Pearls（1–5）

> **Pearl 1 — SNaPP (Lancet Respir Med)**：Sugammadex vs Neostigmine，n=3,498；PPC 或死亡 **RR 0.88 (0.77-1.00, p=0.049)**；主要靠 atelectasis（肺塌陷）減少驅動。

> **Pearl 2 — MICROINHALO (ICM)**：自動套囊壓力控制 + SSD；主要終點（氣管定殖率）**陰性**，但 **VAP 減半**（10.2% vs 19.5%，p=0.039）。

> **Pearl 3 — DIANA 子分析 (ICM)**：適切 empiric 抗生素 → 28 天死亡 **aOR 1.83 (1.11-3.06)**；Moderate severity（SOFA 3-9）效果最顯著。

> **Pearl 4 — PoCLUS 2025 共識 (ICM)**：**83 條 Delphi 聲明**，21 位專家，1,775 篇文獻；涵蓋 PTX、ARDS 分型、心因性肺水腫、低資源環境應用。

> **Pearl 5 — WEAN-US (Crit Care)**：多模態超音波整合模型預測困難脫機失敗 **AUROC 0.88 (0.78-0.95)**；SBT 失敗以心臟 E/e' 為主，拔管後失敗以神經肌肉損傷為主。

---

# 重點摘要 Key Pearls（6–10）

> **Pearl 6 — 術後 vs 內科 ARDS (Crit Care)**：n=1,077；術後 ARDS 90 天死亡率 **36% vs 49%（aHR 0.68）**；死亡預測因子不同——腎外器官衰竭比肺損傷指標更重要。

> **Pearl 7 — Hyperlactatemia 腎臟視角 (Crit Care)**：AKI 破壞腎臟乳酸清除 → **「清除受限型」高乳酸**，≠ 純粹組織缺氧；尿液乳酸為近端小管功能障礙新生物標記。

> **Pearl 8 — 皮膚灌流 Meta-analysis (Shock)**：n=2,727；**CRT 延長 OR 3.29、PPI 下降 OR 5.05**；三項零成本床邊工具均獨立預測敗血症 28 天死亡率。

> **Pearl 9 — 肺栓塞心跳停止 日本全國資料庫 (Resuscitation)**：n=10,390；ECMO 使用率 16%→20.8%，院內存活率 **20.9%→24.1%（p=0.04）**，神經學預後同步改善。

> **Pearl 10 — PIC 調查 (CCM)**：26% 臨床人員有不適切照護感知；多位共同感知 → **死亡 aOR 3.86（1.23-12.16）**。護理師比醫師更常報告 PIC。

---

<!-- _class: divider -->
# 一、呼吸支持與機械通氣
## Respiratory Support & Mechanical Ventilation

---

# SNaPP 試驗：Sugammadex vs Neostigmine
## [Leslie K, et al. *Lancet Respir Med*. 2026. PMID: 42263720](https://doi.org/10.1016/S2213-2600(26)00158-X)

- **設計**：Phase 4 RCT；澳洲、紐西蘭、香港 44 家醫院；n=3,498
- **族群**：≥40 歲、腹腔/胸腔手術、全身麻醉 ≥2 h；逆轉 rocuronium/vecuronium 誘導的 NMB
- **主要終點**：術後至出院（或 Day 7）之 PPC 或死亡

| 終點 | Sugammadex | Neostigmine | RR (95% CI) | p |
|------|-----------|-------------|-------------|---|
| **PPC 或死亡** | 19.0% | 21.5% | **0.88 (0.77-1.00)** | **0.049** |
| Atelectasis | 18.4% | 21.1% | 0.86 (0.76-0.99) | 0.030 |
| Pneumonia | 2.1% | 2.2% | 0.98 (0.62-1.53) | 0.92 |

> 差距在 CI 邊界（上界 1.00）；主要靠 atelectasis 驅動；無 ARDS 發生。**Aminosteroid NMB 逆轉時，Sugammadex 可適度降低 PPC 風險。**

---

# MICROINHALO 試驗：自動套囊壓力控制 + 聲門下引流
## [De Pascale G, et al. *Intensive Care Med*. 2026. PMID: 42228008](https://doi.org/10.1007/s00134-026-08459-6)

- **設計**：10 個 ICU，群體隨機 RCT；n=250（127 自動 vs 123 手動）
- **介入**：自動 ETT Pcuff 控制（依呼出 CO₂ 個別化）+ 自動 SSD vs 手動管理

| 終點 | 自動組 | 手動組 | p |
|------|--------|--------|---|
| **Day 3 氣管定殖（主要終點）** | 37% | 41.5% | **0.52（陰性）** |
| 臨床診斷 VAP | **12.6%** | 24.4% | **0.016** |
| 微生物確診 VAP | **10.2%** | 19.5% | **0.039** |
| Pcuff 超範圍比例 | 10.2% | 24.4% | <0.001 |

> 主要終點陰性，但 **VAP 發生率減半**。需以 VAP 為主要終點的 phase 3 試驗確認。

---

# WEAN-US：多模態超音波預測困難脫機失敗
## [Fogagnolo A, et al. *Crit Care*. 2026. PMID: 42243858](https://doi.org/10.1186/s13054-026-06113-7)

- **對象**：困難脫機（≥48h 機械通氣 + 首次 SBT 失敗）病人
- **四維度超音波評估**（SBT 進行中）：橫膈功能（DTFmax）、肺充氣（aeraton loss score）、心臟（E/e'、EF）、神經肌肉（握力、ICU-AW）

| 預測工具 | AUROC (95% CI) |
|---------|----------------|
| **整合模型** | **0.88 (0.78-0.95)** |
| 最佳單一指標（DTFmax） | ~0.74 |
| 心臟參數（E/e'） | ~0.72 |

- **SBT 失敗** → 高 E/e'（心臟問題）
- **拔管後失敗** → 低 DTFmax、低握力（神經肌肉問題）

> **兩種失敗機轉不同**，需個別化評估並針對性介入。

---

# 術後 ARDS vs 內科 ARDS：不同臨床亞型
## [Pensier J, et al. *Crit Care*. 2026. PMID: 42243987](https://doi.org/10.1186/s13054-026-06112-8)

- **設計**：20 年單中心前瞻資料回溯分析；n=1,077（術後 ARDS 455 例，42%）

| 指標 | 術後 ARDS | 內科 ARDS | p |
|------|---------|---------|---|
| **90 天死亡率** | **36%** | **49%** | <0.001 |
| 校正後 90 天死亡 aHR | 0.68 (0.56-0.83) | — | <0.001 |

- **死亡預測因子差異**：

| | 術後 ARDS | 內科 ARDS |
|---|---------|---------|
| 最主要死亡預測 | **Non-respiratory SOFA、手術部位** | PaO₂/FiO₂、driving pressure |
| PaO₂/FiO₂ 對死亡 | 無獨立預測力 | 有獨立關聯 |

> 術後 ARDS 管理重點：**預防手術併發症、保護腎外器官**，而非純優化肺保護通氣。

---

# PoCLUS 2025 共識：肺部床邊超音波 83 條聲明
## [Volpicelli G, et al. *Intensive Care Med*. 2026. PMID: 42257880](https://doi.org/10.1007/s00134-026-08487-2)

- **方法**：Delphi 共識；21 位國際專家；1,775 篇文獻（2012-2025）；共識門檻 80% full agreement

- **83 條聲明涵蓋範疇**：

| 主題 | 新亮點 |
|------|-------|
| Pneumothorax (PTX) | Lung sliding 消失 + lung point 確認；可替代 CXR |
| ARDS 分型 | 超音波肺充氣程度輔助「局灶 vs 彌漫型」分型 |
| 心因性肺水腫 | B-line 數量量化準確性提升 |
| 低資源環境 | 擴展應用範疇 |

> 2025 版大幅擴展 2012 版，建議所有 ICU 培訓採用此更新框架。

---

# ARDS 可以預防嗎？：60 年演進回顧
## [Yadav H, et al. *Intensive Care Med*. 2026. PMID: 42257879](https://doi.org/10.1007/s00134-026-08493-4)

- **醫源性 ARDS（可預防）**：
  - TRALI（輸血相關急性肺損傷）：男性血漿政策後急劇下降
  - 手術室 + 急診啟動 lung-protective ventilation
  - Bundle 照護（限制輸液 + 限制輸血 + 吸入預防 + 早期抗菌素）

- **非醫源性 ARDS**：藥物預防試驗在未選擇族群中持續失敗

- **未來方向**：
  - 生物次表型（hyperinflammatory vs hypo-inflammatory）精準治療
  - 個別化通氣策略

> 建置醫院層級的「ARDS 預防 bundle」是目前最具實證的策略；藥物預防在選定次表型中仍有潛力。

---

<!-- _class: divider -->
# 二、Sepsis 與感染管控
## Sepsis & Infection Control

---

# DIANA 研究子分析：適切抗生素與存活率
## [Cidade JP, et al. *Intensive Care Med*. 2026. PMID: 42228012](https://doi.org/10.1007/s00134-026-08448-9)

- **設計**：DIANA Study 預定子分析；大型國際 ICU 隊列；n=845（微生物確認感染）
- **「適切治療」定義**：至少一種抗生素對已知病原菌具 in vitro 活性
- **適切治療率：87.7%**（12.3% 仍接受不適切治療，主因 MDRO）

| 分析 | 適切 vs 不適切 | 95% CI | p |
|------|--------------|--------|---|
| **28 天死亡 aOR** | **1.83** | 1.11-3.06 | **0.02** |
| 28 天死亡 aHR | 1.51 | 1.03-2.21 | 0.035 |
| 無機械通氣天數 | 適切組較多 | — | — |

- **Moderate severity（SOFA 3-9）**效果最顯著

> 根據**當地流行病學 + 病人危險因子**及時啟動廣效適切抗生素，87.7% 仍有 de-escalation（降階梯）機會，應積極於培養回報後降階。

---

# ICU 營養支持：現行證據與演進標準
## [Peake SL, et al. *Intensive Care Med*. 2026. PMID: 42228011](https://doi.org/10.1007/s00134-026-08474-7)

- **急性期（前 7 天，尤其需器官支持病人）**：
  - 推薦：**低熱量低蛋白**策略（~6-12 kcal/kg/d + 0.2-0.5 g protein/kg/d）
  - 增加蛋白質未能改善存活率，AKI 病人甚至可能有害
  - 避免 refeeding syndrome（再餵食症候群）

- **恢復期（acute phase 解決後）**：
  - 合成代謝過程啟動，需求改變
  - 最佳巨量營養素目標**尚未確立**

- **實際執行**：喂食中斷（手術、管路）、胃腸不耐受仍是主要障礙

> 急性休克、需器官支持病人前 7 天採**低熱量低蛋白**是安全且可能有益的。

---

# ICU 病人血液管理（PBM）：敘事性綜述
## [Meybohm P, et al. *Intensive Care Med*. 2026. PMID: 42257882](https://doi.org/10.1007/s00134-026-08491-6)

| 策略 | 證據 | 重點 |
|------|------|------|
| Restrictive RBC 輸血（Hb <7 g/dL 觸發） | **強** | 消化道出血亦然 |
| IV 鐵補充（缺鐵性貧血） | 中等 | 腸外鐵首選 |
| 小容量採血管 + 封閉系統 | 中等 | 減少醫源性貧血 |
| 預防性 FFP（新鮮冷凍血漿） | **不支持** | 非出血病人不應使用 |
| 預防性血小板 | 有限 | 限高危血液腫瘤 |
| Erythropoietin（EPO） | 謹慎 | 血栓栓塞風險不確定 |

> **FFP 在非出血重症病人的預防性使用已無實證支持**；識別並治療缺鐵性貧血是 PBM 中較被忽視的策略。

---

<!-- _class: divider -->
# 三、AKI / 血液動力學 / 休克
## AKI / Hemodynamics / Shock

---

# 皮膚灌流指標預測敗血症死亡率：Meta-analysis
## [Shi LJ, et al. *Shock*. 2026. PMID: 42258324](https://doi.org/10.1097/SHK.0000000000002885)

- **設計**：系統性 meta-analysis；22 篇研究，n=2,727 敗血症病人
- **三項零成本床邊工具**：

| 指標 | 意涵 | 28 天死亡 OR (95% CI) | p |
|------|------|---------------------|---|
| **MS（皮膚花斑評分）升高** | 對稱性花斑，0-5 級 | 2.27 (1.79-2.87) | <0.001 |
| **CRT（微血管回充時間）延長** | >2 秒（食指按壓 5 秒後） | **3.29 (2.08-5.21)** | <0.001 |
| **PPI（周邊灌流指數）下降** | 脈搏血氧儀計算 | **5.05 (3.65-6.98)** | <0.001 |

- 敏感度分析穩定；無顯著發表偏誤

> CRT、PPI、MS 三者整合於每日查房，可強化早期高風險患者識別與液體復甦效果監測。

---

# Hyperlactatemia 的腎臟代謝視角
## [Payen D, et al. *Crit Care*. 2026. PMID: 42237139](https://doi.org/10.1186/s13054-026-06095-6)

- **傳統觀點**：乳酸升高 = 組織缺氧 + 無氧代謝 → 即刻擴大復甦

- **新觀點：「生產增加 + 清除受限」複合訊號**

| 概念 | 說明 |
|------|------|
| 腎臟近端小管 | 乳酸清除主要場所（次於肝臟，甚至更重要） |
| AKI 影響 | 直接破壞腎臟乳酸代謝能力 |
| **清除受限型 (clearance-limited phenotype)** | 即使無組織缺氧，血乳酸亦升高 |
| 尿液乳酸升高 | 近端小管代謝功能障礙早期標誌 |
| Lactylation | 乳酸作為蛋白質轉譯後修飾訊號，調節炎症→修復 |

> 在已知 AKI 的敗血症病人，**高乳酸不應自動觸發更大量液體復甦**；評估乳酸 2 小時 clearance ≥10% 比絕對值更有意義。

---

# SOFA-2 評分效度驗證：vs SOFA-1
## [Helleberg J, et al. *Crit Care*. 2026. PMID: 42226253](https://doi.org/10.1186/s13054-026-06093-8)

- **設計**：回溯觀察；4 個瑞典 ICU；2010-2021；n=29,820 次入院
- **SOFA-2（連續器官衰竭評估升級版）** vs **SOFA-1（原版）**

| 指標 | SOFA-2 AUROC | SOFA-1 AUROC | p |
|------|-------------|-------------|---|
| **Day 1 30 天死亡率** | **0.81 (0.80-0.81)** | 0.80 (0.79-0.81) | <0.001 |
| Day 2-7 | 兩者相近 | 兩者相近 | — |
| 創傷 subgroup (Day 1) | 0.81 | 相似 | — |

- 75-79% 病人入院時在兩版本間重新分類

> SOFA-2 在 **Day 1 早期預後評估**有微幅但統計顯著的更佳辨別力，適合作為 ICU 入院時分層工具；後續天數差異消失。

---

<!-- _class: divider -->
# 四、急救與心肺復甦
## Cardiac Arrest & Resuscitation

---

# 肺栓塞心跳停止：治療趨勢與預後（日本全國資料庫 2012-2024）
## [Ishida K, et al. *Resuscitation*. 2026. PMID: 42264174](https://doi.org/10.1016/j.resuscitation.2026.111167)

- **設計**：日本全國住院資料庫；回溯；2012-2024；n=10,390 PE 合併 CPR；中位年齡 74 歲

| 治療趨勢 | 2012 | 2023 | p |
|---------|------|------|---|
| **TL（血栓溶解治療）** | 16.0% | **6.7%** | <0.001 ↓ |
| **ECMO** | 16.0% | **20.8%** | 0.015 ↑ |

| 預後趨勢 | 2012 | 2024 | p |
|---------|------|------|---|
| **院內存活率** | 20.9% | **24.1%** | **0.04** |
| **神經學預後良好** | 17.4% | **20.6%** | **0.04** |

- 改善最顯著者：院內發生的 PE + 接受 ECMO 者

> PE 心跳停止管理正從 TL 主導轉向 ECMO 主導；ECMO 可作為橋接策略（→TL、導管取栓、手術取栓）。

---

# OHCA 後 AKI 生物標記：早期預測神經學預後
## [Lim SL, et al. *Resuscitation*. 2026. PMID: 42264173](https://doi.org/10.1016/j.resuscitation.2026.111163)

- **設計**：前瞻觀察；昏迷 OHCA 成人；n=82
- AKI 發生率 65.9%；不良神經學結果（CPC 3-5）54.9%
- **生物標記（測量時間點：0、24、72 h）**：

| 生物標記 | CPC 3-5 (不良預後) AUC | AKI AUC |
|---------|---------------------|---------|
| sCr（血清肌酸酐） | 0.57 | 0.65 |
| **Urinary NGAL（尿液 NGAL）** | **0.79** | **0.81** |
| Plasma NGAL | ~0.70 | ~0.75 |
| KIM-1（腎損傷分子-1） | 中等 | 中等 |

> 尿液 NGAL 在 OHCA 後的 AKI 偵測與神經學預後預測均優於傳統 sCr。入院時測量尿液 NGAL 可協助早期 AKI 風險分層。

---

<!-- _class: divider -->
# 五、ICU 照護品質與倫理
## ICU Quality & Ethics

---

# 不適切照護感知（PIC）：荷蘭全國 ICU 調查
## [CCM 2026. PMID: 42283554](https://doi.org/10.1097/CCM.0000000000007241)

- **設計**：單日橫斷面 + 6 個月追蹤；47 個 ICU；n=1,058 臨床人員（回覆率 72%）；525 病人

- **26% 臨床人員**對至少一名病人報告 PIC（不適切照護感知）

| 主要原因 | 比例 |
|---------|------|
| Distributive injustice（分配不公） | 70% |
| Disproportionality of care（照護比例不當） | 66% |

| 相關因子 | aOR (95% CI) |
|---------|-------------|
| 護理師 vs 醫師 | 1.78 (1.37-2.33) |
| 迴避 end-of-life 決策文化 | 1.92 |
| **多位共同感知 PIC → 死亡** | **3.86 (1.23-12.16)** |

> 共同感知的 PIC 不僅是職業倦怠前驅，**更是預後惡化的信號**。定期倫理查房、護醫溝通是可行介入策略。

---

# POLST 簽署者身份：AD 侵蝕現象
## [Oh TK, Song IA. *Am J Respir Crit Care Med*. 2026. PMID: 42286341](https://doi.org/10.1093/ajrccm/aamag276)

- **設計**：南韓全國健保資料庫；2020-2023；n=1,189,042 成人 ICU 入院

| POLST 類型 | 侵入性末期照護 aOR (95% CI) |
|------------|--------------------------|
| **PD-POLST（病人親簽）** | **0.43 (0.43-0.54) ↓ 顯著減少** |
| **SD-POLST（代理人代簽）** | **2.16 (1.98-2.35) ↑ 顯著增加** |
| 已有 AD 但代理人改簽 POLST | 1.69 (1.51-1.89)（AD 意願被「侵蝕」）|

- **「AD 侵蝕」現象**：即使病人事先立下 AD 限制治療，家屬代簽 POLST 後侵入性照護反而增加——**代理人趨向更積極治療，而非遵循病人原意**

> 提早、持續地與病人**本人**進行 ACP（預立照護計畫）討論，確保在認知能力喪失前明確記錄意願。

---

<!-- _class: divider -->
# 六、其他值得關注
## Honorable Mentions

---

# Honorable Mentions

- **ACORN 試驗 Post Hoc（AJRCCM 2026，PMID: 42275170）**
  - Cefepime vs Piperacillin-Tazobactam；**WBC ≥16,000/µL 亞群**中，piperacillin-tazobactam 死亡率更低（OR 0.51，0.29-0.90）
  - Post hoc 分析，**不改變臨床標準**；WBC 具 predictive enrichment 生物標記潛力

- **Tocilizumab 兒童敗血性休克（Shock 2026，PMID: 42241413）**
  - n=58；tocilizumab 死亡率 18.7% vs 46.1%（p=0.02）；GNB subgroup 改善最顯著
  - 回溯性、樣本小，**僅供假說生成**；需前瞻性 RCT

- **Frailty 不平衡：ICU 試驗隱藏偏誤（Crit Care 2026，PMID: 42231342）**
  - 模擬研究；100 人/組試驗中 36% 因 CFS 不平衡 → ≥2% 死亡率差異
  - ICU 試驗應常規報告 frailty 分布並分層

- **ICU 家屬 PTSD 觸發因素（ICM 2026，PMID: 42268369）**
  - 質性研究；n=17；三大主題：傳記軌跡中斷、ICU 環境導航、死亡時刻
  - PTSD 源自**整個照護過程的累積壓力**，應全程性啟動家屬支持介入

---

<!-- _class: ref -->
# 參考文獻（一）

**呼吸支持與機械通氣**

1. Leslie K, et al. Sugammadex versus neostigmine for reversal of neuromuscular blockade and postoperative pulmonary complications (SNaPP). [*Lancet Respir Med*. 2026.](https://doi.org/10.1016/S2213-2600(26)00158-X) PMID: 42263720.
2. De Pascale G, et al. Personalized automatic management of tracheal cuff pressure and subglottic secretions drainage to prevent pneumonia in critically ill intubated patients (MICROINHALO). [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08459-6) PMID: 42228008.
3. Fogagnolo A, et al. Integrated comprehensive assessment for predicting weaning success in difficult-to-wean critically ill patients: the WEAN-US study. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-06113-7) PMID: 42243858.
4. Pensier J, et al. Is postoperative ARDS different from medical ARDS? [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-06112-8) PMID: 42243987.
5. Volpicelli G, et al. International evidence-based recommendations for point-of-care lung ultrasound: 2025 focused update. [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08487-2) PMID: 42257880.
6. Yadav H, et al. Is acute respiratory distress syndrome a preventable disease? [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08493-4) PMID: 42257879.

**Sepsis 與感染管控**

7. Cidade JP, et al. Impact of appropriate antimicrobial therapy on patient outcomes: a sub analysis of the DIANA Study. [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08448-9) PMID: 42228012.
8. Peake SL, et al. Nutrition support in the ICU: current evidence and evolving standards. [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08474-7) PMID: 42228011.
9. Meybohm P, et al. Patient blood management in general intensive care patients. [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08491-6) PMID: 42257882.

---

<!-- _class: ref -->
# 參考文獻（二）

**AKI / 血液動力學 / 休克**

10. Shi LJ, et al. Meta-analysis of the prognostic value of skin perfusion parameters in sepsis patients. [*Shock*. 2026.](https://doi.org/10.1097/SHK.0000000000002885) PMID: 42258324.
11. Payen D, et al. Hyperlactatemia in sepsis and shock: a renal metabolic perspective. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-06095-6) PMID: 42237139.
12. Helleberg J, et al. Predictive validity of daily sequential organ failure assessment (SOFA)-2 score for 30-day mortality. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-06093-8) PMID: 42226253.

**急救與心肺復甦**

13. Ishida K, et al. Temporal trends in treatment and outcomes of patients with cardiac arrest due to pulmonary embolism: a nationwide inpatient database study. [*Resuscitation*. 2026.](https://doi.org/10.1016/j.resuscitation.2026.111167) PMID: 42264174.
14. Lim SL, et al. Prognostic Performance of Plasma and Urinary Biomarkers of Kidney Injury and Function After Out-Of-Hospital Cardiac Arrest. [*Resuscitation*. 2026.](https://doi.org/10.1016/j.resuscitation.2026.111163) PMID: 42264173.

**ICU 照護品質與倫理**

15. Perceived Inappropriateness of Care Study. Perceived Inappropriateness of Intensive Care Treatment Among Clinicians: A Cross-Sectional Nationwide Survey. [*Crit Care Med*. 2026.](https://doi.org/10.1097/CCM.0000000000007241) PMID: 42283554.
16. Oh TK, Song IA. Patient versus surrogate decision making for life sustaining treatment and terminal care intensity. [*Am J Respir Crit Care Med*. 2026.](https://doi.org/10.1093/ajrccm/aamag276) PMID: 42286341.

---

<!-- _class: ref -->
# 參考文獻（三）

**其他值得關注**

17. Rzewnicki DI, et al. Association of White Blood Cell Count with Treatment Response to Cefepime vs Piperacillin-Tazobactam. [*Am J Respir Crit Care Med*. 2026.](https://doi.org/10.1093/ajrccm/aamag257) PMID: 42275170.
18. Lau KK, et al. Tocilizumab Therapy in Gram-Positive and Gram-Negative Pediatric Septic Shock: A Comparative Pilot Study. [*Shock*. 2026.](https://doi.org/10.1097/SHK.0000000000002884) PMID: 42241413.
19. Dugan C, et al. Simulation study of frailty as a baseline confounder: the need to improve reporting intensive care trials. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-06118-2) PMID: 42231342.
20. Kentish-Barnes N, et al. Understanding multiple ICU-related triggers of family PTSD symptoms — a qualitative thematic study. [*Intensive Care Med*. 2026.](https://doi.org/10.1007/s00134-026-08504-4) PMID: 42268369.

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**整理：謝慕揚 MD, PhD, FESC**
**Critical Care 雙週期刊回顧 | 2026-06-01 ～ 2026-06-15**

*本回顧涵蓋 ICM · Critical Care · CCM · Lancet Respir Med · AJRCCM · Chest · Resuscitation · Shock*

*本文件僅供醫療專業人員教學參考*
