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
  section.lead h1 {
    color: #ffffff;
    font-size: 2.2em;
  }
  section.lead h2 {
    color: #b0c4de;
  }
  section.lead p, section.lead strong {
    color: #dfe6e9;
  }
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
  h1 {
    color: #ba181b;
    border-bottom: 3px solid #ba181b;
    padding-bottom: 0.2em;
  }
  h2 {
    color: #0072bc;
  }
  h3 {
    color: #555555;
  }
  table {
    font-size: 0.72em;
    width: 100%;
  }
  th {
    background-color: #0072bc;
    color: white;
    padding: 6px 10px;
  }
  td {
    padding: 4px 10px;
  }
  tr:nth-child(even) {
    background-color: #f0f4f8;
  }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.88em;
  }
  code {
    background-color: #f1f2f6;
    color: #2d3436;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.85em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 0.68em;
  }
  pre code {
    background-color: transparent;
    color: #2d3436;
  }
  strong {
    color: #ba181b;
  }
  em {
    color: #555;
  }
  footer {
    color: #787878;
    font-size: 0.6em;
  }
  section.small-text {
    font-size: 0.85em;
  }
footer: '謝慕揚 MD, PhD, FESC | Esmolol 在重症加護的應用 | 2026'
---

<!-- _class: lead -->

# Esmolol 在重症加護的應用

## 適應症、使用時機與劑量

**謝慕揚 MD, PhD, FESC**
心臟內科 / 加護病房 | 2026-02-27

---

# 大綱

**基礎篇**
1. 藥物特性與藥動學
2. 作用機轉
3. 適應症
4. ICU 使用時機

**臨床篇**
5. 使用劑量與給藥方式
6. 臨床要點與監測
7. 重要臨床試驗
8. Beta-blocker 比較
9. 新興應用

---

<!-- _class: divider -->

# 第一部分：Esmolol 藥物特性

---

# 基本資料

- **學名**：Esmolol hydrochloride
- **商品名**：Brevibloc
- **分類**：超短效 beta-1 選擇性阻斷劑 (ultra-short-acting cardioselective beta-1 blocker)
- **給藥途徑**：僅限 IV
- **Beta-1 選擇性**：約 beta-2 的 2.3 倍（與 metoprolol 相當）

> Esmolol 是 **唯一** 可在 ICU 中作為「試探性」使用的 beta-blocker — 停藥後 **30 分鐘內** 效果完全消退

---

# 藥動學參數

| 項目 | 數值 | 臨床意義 |
|------|------|----------|
| 作用起始 (Onset) | **< 60 秒** | 幾乎即時生效 |
| 分布半衰期 | ~2 分鐘 | 快速達到效果部位 |
| **消除半衰期** | **~9 分鐘** (4-16 min) | 停藥後效果快速消退 |
| 作用持續時間 | 10-20 分鐘 | 短效可控 |
| 停藥後消退 | 10-30 分鐘 | 低血壓時快速恢復 |
| 有 loading 達穩態 | ~5 分鐘 | 需快速控制時使用 |
| 無 loading 達穩態 | ~30 分鐘 | 穩定病人可不給 loading |

---

# 代謝特點：RBC Esterases

**代謝途徑**
- 由紅血球 **細胞質 (cytosol)** 中的酯酶水解
- **非** 血漿膽鹼酯酶、**非** 肝臟 CYP450 系統
- 產物：acid metabolite (ASL-8123) + methanol

**臨床意義**
- **肝腎功能不全者無需調整劑量**
- 在 ICU 多重器官衰竭 (MODS) 的病人特別安全
- 這是其他 beta-blocker 無法比擬的優勢

---

<!-- _class: divider -->

# 第二部分：作用機轉

---

# Beta-1 受體阻斷的基本效應

```text
Beta-1 受體阻斷
  |-- 降低心率 (Negative chronotropy)       --> 減少心肌耗氧量
  |-- 降低心肌收縮力 (Negative inotropy)     --> 降低 MVO2
  |-- 延長舒張充填時間 (Diastolic filling)   --> 改善冠狀動脈灌流
  |-- 降低心輸出量（輕微）                    --> 血壓可能下降
```

> **關鍵概念**：在 sepsis 中，心率控制改善 diastolic filling, stroke volume 增加, 可能 **維持甚至改善** cardiac output

---

# Sepsis 中的多重保護機轉

**血行動力學改善** — 降低心率延長 diastolic filling, 增加 stroke volume, 降低 MVO2

**抗發炎效應** *(2025 新證據)*
- 上調 **alpha-7 nAChR / STAT3 / NF-kB** pathway
- 增加 ChAT+CD4+ T lymphocytes（膽鹼能抗發炎途徑）
- 降低促發炎細胞因子：IL-1、IL-6、TNF-alpha

**免疫調節**
- 交感過度活化透過 beta-1 受體耗竭 T cells
- Esmolol 阻斷此途徑，保護免疫功能

*Ref: Front Pharmacol. 2025;16:1498227*

---

<!-- _class: divider -->

# 第三部分：適應症

---

# FDA 核准適應症

1. **心室上心搏過速 (SVT)** — 心率控制
2. **心房顫動 / 心房撲動 (AF/AFL)** — 急性心率控制
3. **周術期心搏過速與高血壓** — Perioperative use

---

# 重症常見 Off-label 使用

| 適應症 | 臨床情境 | 治療目標 |
|--------|----------|----------|
| **主動脈剝離** (Aortic dissection) | 急性 Type A/B | HR < 60 bpm, SBP < 120 mmHg |
| **甲狀腺風暴** (Thyroid storm) | 交感神經亢進症狀控制 | HR 控制，穩定後轉口服 propranolol |
| **嗜鉻細胞瘤手術** (Pheochromocytoma) | 術中心率控制 | **須合併 alpha-blocker** |
| **Septic shock** | 持續性 tachycardia (HR >= 95) | HR 80-94 bpm (Morelli protocol) |
| **電痙攣治療 / ECT** | 減緩交感反應 | 心率與血壓控制 |

---

<!-- _class: divider -->

# 第四部分：ICU 使用時機

---

# 何時優先選擇 Esmolol？

**適合使用**
- 需要 **快速起效、快速消退** 的 beta-blockade
- 血行動力學不穩定，擔心低血壓風險
- **不確定** 病人對 beta-blocker 的耐受性
- 急性 AF with RVR
- 術後或 procedure 後心搏過速
- **多重器官衰竭** (不需肝腎劑量調整)
- 急性主動脈剝離需精準心率控制

---

# 相對禁忌

| 禁忌 | 說明 |
|------|------|
| 失代償性心衰竭 (Decompensated HF) | 負性肌力作用可能惡化心衰 |
| 嚴重氣喘急性發作 | Beta-2 阻斷可致支氣管痙攣 |
| 嚴重竇性心搏過緩 (HR < 50) | 可能加重心搏過緩 |
| 二度/三度 AV block（無 pacemaker） | 傳導阻滯風險 |
| Cardiogenic shock | 負性肌力作用致命 |
| 同時 IV calcium channel blocker | 嚴重心搏過緩風險 |
| Pheochromocytoma **單獨使用** | 須 **先合併 alpha-blocker** |

---

<!-- _class: divider -->

# 第五部分：使用劑量

---

# 標準給藥方式

**Loading Dose（負荷劑量）**

| 情境 | 劑量 |
|------|------|
| 標準 | 500 mcg/kg IV, over 1 min |
| 擔心低血壓 | 250 mcg/kg IV, over 1 min |

**Maintenance Dose（維持劑量）**

| 項目 | 數值 |
|------|------|
| 起始 | 50 mcg/kg/min |
| 調整 | 每 4-5 分鐘增加 50 mcg/kg/min |
| 最大 | 200-300 mcg/kg/min |
| 建議使用時間 | < 48 小時 |

---

# 劑量調整流程

```text
步驟 1: Loading dose 500 mcg/kg IV over 1 min
            |
步驟 2: 開始 50 mcg/kg/min infusion
            |
步驟 3: 等待 4-5 分鐘，評估 HR 與 BP
            |
     [目標達成] --> 維持目前劑量
            |
     [未達標]  --> 再次 Loading 500 mcg/kg
                       |
                   增加 infusion 至 100 mcg/kg/min
                       |
                   重複直到達標或最大劑量 (200-300 mcg/kg/min)
```

---

# 各臨床情境劑量速查

| 情境 | Loading | Maintenance | 目標 |
|------|---------|-------------|------|
| **AF with RVR** | 500 mcg/kg / 1 min | 50-200 mcg/kg/min | HR < 110 bpm |
| **SVT** | 500 mcg/kg / 1 min | 50-200 mcg/kg/min | HR 控制或轉復 |
| **主動脈剝離** | 500 mcg/kg / 1 min | 50-200 mcg/kg/min | HR < 60, SBP < 120 |
| **Septic shock** | 無標準 loading | 25-2000 mg/hr | HR 80-94 bpm |
| **甲狀腺風暴** | 250-500 mcg/kg | 50-100 mcg/kg/min | 症狀控制後轉口服 |
| **周術期** | 500 mcg/kg / 1 min | 50-200 mcg/kg/min | HR / BP 控制 |

---

# 給藥注意事項

- **稀釋**：10 mg/mL 可直接使用；250 mg/mL 需稀釋
- **途徑**：僅限 IV 使用，高濃度時建議使用 central line
- **配伍禁忌**：避免與 sodium bicarbonate 同管
- **外滲風險**：高濃度溶液若外滲可致皮膚壞死

---

<!-- _class: divider -->

# 第六部分：臨床要點與監測

---

# 監測項目

| 項目 | 頻率 | 備註 |
|------|------|------|
| **心率 (HR)** | 持續監測 | Telemetry 必備 |
| **血壓 (BP)** | 每 5-15 分鐘（調整期間） | 建議 arterial line |
| **ECG** | 持續監測 | 注意 AV block、QT |
| **IV 注射部位** | 每班檢查 | 注意外滲 (extravasation) |
| **尿量** | 每小時 | 評估灌流 |
| **Lactate** | 每 4-6 小時 | Sepsis 病人追蹤 |

---

# Clinical Pearls

> **Pearl 1**：Esmolol 是 ICU 中的 **「試探性 beta-blocker」** — 無法耐受時停藥 30 分鐘內效果消退

> **Pearl 2**：Septic shock 使用 esmolol 時，**norepinephrine 劑量可能減少** — 心率控制改善了血行動力學效率 (Morelli 2013)

> **Pearl 3**：急性主動脈剝離，esmolol 比 labetalol 更適合 **精準滴定** — labetalol offset 長達數小時

> **Pearl 4**：甲狀腺風暴使用 beta-blocker 有 **CV collapse** 風險，Esmolol 因超短效特性比 propranolol 更安全

---

# 低血壓處理流程

```text
Esmolol 使用中出現低血壓
     |
  1. 降低 infusion rate（或暫停）
     |
  2. 等待 10-30 分鐘 -- 效果自然消退
     |
  3. 必要時 IV fluid bolus 或 vasopressor
     |
  4. 完全恢復後，考慮以較低劑量重新開始
```

> **關鍵優勢**：停藥 30 分鐘內效果幾乎完全消退 — 這是 Esmolol 最大的安全特點

---

<!-- _class: divider -->

# 第七部分：重要臨床試驗

---

# Morelli et al. 2013 — 里程碑研究

*JAMA* 2013;310(16):1683-1691

| 項目 | 內容 |
|------|------|
| **設計** | Open-label, randomized, phase 2, single-center |
| **收錄** | 154 位 septic shock (HR >= 95, 高劑量 NE) |
| **介入** | Esmolol titrate HR 80-94 bpm vs 標準治療 |
| **28 天死亡率** | **49.4% vs 80.5%** (adj. HR 0.39; 95% CI 0.26-0.59; p < 0.001) |
| **次要結果** | NE 需求降低、lactate 下降、輸液需求減少 |
| **限制** | 單一中心、open-label、對照組死亡率異常高 |

---

# STRESS-L Trial 2023 — 重要負面試驗

*JAMA* 2023;330(17):1641-1652

| 項目 | 內容 |
|------|------|
| **設計** | Open-label, multicenter (**40 UK ICUs**), randomized |
| **收錄** | 126 位 (原計畫 340 位，因可能有害 **提前終止**) |
| **介入** | **Landiolol** (非 esmolol) vs 標準治療 |
| **主要結果** | SOFA score 無差異 (8.8 vs 8.1; p = 0.24) |
| **死亡率** | 28d: 37.1% vs 25.4% (p=0.16); 90d: 43.5% vs 28.6% (p=0.08) |

> **注意**：STRESS-L 使用的是 **landiolol** 而非 esmolol，兩者藥理不同。提醒 single-center 結果不一定能 multicenter 重現。

---

# Meta-analyses 總結 (2021-2026)

| 研究 | 年份 | 樣本 | 結果 |
|------|------|------|------|
| Hasegawa *Chest* | 2021 | 7 RCTs, 613 pts | **RR 0.68** (0.54-0.85; p<0.001) 有利 |
| Sato *Chest* | 2025 | 8 RCTs, 885 pts | RR 0.84 (0.68-1.02; p=0.08) 不顯著 |
| Alexandru *Crit Care* | 2024 | 7 RCTs, 854 pts | RD -0.10 (-0.22-0.02; p=0.11) 不顯著 |
| **Tang *CCM*** | **2026** | **10 RCTs, 1035** | **Esmolol: RR 0.69** (0.56-0.85) 有利 |

> **2026 最新結論** (Tang NMA)：**Esmolol 顯著降低 28 天死亡率**，且 Esmolol **優於** Landiolol

---

<!-- _class: divider -->

# 第八部分：Beta-blocker 比較

---

# Esmolol vs 其他 ICU Beta-blockers

| 特性 | **Esmolol** | **Labetalol** | **Metoprolol** | **Landiolol** |
|------|:---:|:---:|:---:|:---:|
| 受體 | Beta-1 | Alpha+Beta | Beta-1 | Beta-1 |
| 半衰期 | **9 min** | 5.5 hr | 3-7 hr | 4 min |
| Onset | **<60 sec** | 2-5 min | ~5 min | <60 sec |
| 連續滴注 | Yes | No | No | Yes |
| 降壓 | 中等 | **強** | 弱 | 弱 |
| 降心率 | **強** | 中等 | 強 | 強 |
| Offset | **10-30 min** | 數小時 | 數小時 | ~10 min |
| 代謝 | **RBC** | 肝臟 | 肝臟 | 血漿/肝 |
| 肝腎調整 | **不需要** | 需要 | 需要 | 部分 |

---

# 如何選擇？

**選 Esmolol**
- 血行動力學不穩定 / 多重器官衰竭 (MODS)
- 不確定 beta-blocker 耐受性
- 需精準可滴定的心率控制（主動脈剝離、ICU AF）

**選 Labetalol**
- 需同時降壓 + 降心率（如高血壓急症合併心搏過速）

**選 Metoprolol**
- 穩定後需轉換口服（長期 rate control）

**選 Landiolol**
- 在日本 / 歐洲較常用，台灣可用性有限

---

<!-- _class: divider -->

# 第九部分：新興應用

---

# 難治性心室顫動 (Refractory VF)

**原理**
- Adrenaline 過度使用導致交感風暴
- 惡化心肌缺血 + 降低除顫成功率
- Esmolol 對抗 beta-adrenergic 過度刺激

**現有證據**
- Case series: 4/6 patients ROSC after esmolol; 50% 存活出院
- **REVIVE Project (2025, UK)**：進行中的系統性研究

> **目前定位**：Off-label，傳統 ACLS 失敗時可考慮。等待 REVIVE-3 結果。

---

# 其他新興應用

**Esmolol Cardioplegia**
- Blood-based esmolol cardioplegia（極化停搏）vs 傳統高鉀去極化停搏
- Beta-blockade 引起 diastolic arrest，減少心肌損傷
- 減少術後 cardiac troponin 釋放

**ECMO 期間心率控制**
- VA-ECMO 心率控制可改善心室 unloading
- 超短效特性適合 ECMO 的不穩定環境
- 尚無正式 guideline 推薦

**周術期心肌保護**
- Meta-analysis: esmolol 減少術後心肌缺血 (RR 0.43)
- 未增加臨床顯著的心搏過緩或低血壓

---

<!-- _class: divider -->

# 總結

---

# Take-Home Messages

**Esmolol 的獨特優勢**
1. **超短效** — 半衰期僅 9 分鐘
2. **RBC 代謝** — 不需肝腎劑量調整
3. **可滴定** — 連續 infusion 精準控制
4. **安全** — 停藥 30 分鐘恢復

**證據現況**
1. **AF rate control** — Guideline 推薦 (Class I)
2. **主動脈剝離** — 第一線用藥 (ACC/AHA 2022)
3. **Septic shock** — Esmolol 可能有利 (2026 NMA)，但 landiolol 不一致
4. **Refractory VF** — 新興領域，等待 RCT

---

<!-- _class: small-text -->

# 參考文獻 (1/2)

1. Morelli A, et al. Esmolol in septic shock. *JAMA*. 2013;310(16):1683-91.
2. Whitehouse T, et al. STRESS-L Trial. *JAMA*. 2023;330(17):1641-52.
3. Tang Z, et al. Esmolol vs Landiolol NMA. *Crit Care Med*. 2026;54(2).
4. Sato R, et al. Meta-analysis with TSA. *Chest*. 2025;167(1):181-92.
5. Hasegawa D, et al. Beta-blockers in sepsis. *Chest*. 2021;159(6):2289-300.
6. Alexandru MG, et al. Meta-analysis. *Crit Care*. 2024;28(1):382.
7. Isselbacher EM, et al. Aortic Disease Guideline. *Circulation*. 2022;146(24):e334-e482.
8. Joglar JA, et al. AF Guideline. *Circulation*. 2024;149(1):e1-e156.

---

<!-- _class: small-text -->

# 參考文獻 (2/2)

9. Van Gelder IC, et al. ESC AF Guidelines. *Eur Heart J*. 2024;45(36):3314-3414.
10. Poveda-Jaramillo R, et al. Ultra-short-acting beta-blockers. *JCVA*. 2018;32(3):1415-24.
11. Krenz JR, et al. Esmolol in aortic dissection. *Am J Emerg Med*. 2021;44:188-92.
12. Wiest D. Esmolol pharmacokinetics. *Clin Pharmacokinet*. 1995;28(3):190-202.
13. Evans L, et al. Surviving Sepsis Campaign 2021. *ICM*. 2021;47(11):1181-1247.
14. Bahn RS, et al. ATA Thyrotoxicosis Guidelines. *Thyroid*. 2011;21(6):593-646.
15. Brevibloc (Esmolol) Package Insert, Baxter Healthcare.

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**
心臟內科 / 加護病房

*本文件僅供醫療專業人員教學參考*
