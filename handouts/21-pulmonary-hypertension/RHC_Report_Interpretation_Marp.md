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
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.7em; width: 100%; }
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
  section.small-text { font-size: 0.78em; }
  section.formula { background-color: #fffbe6; }
footer: '謝慕揚 MD, PhD, FESC | 右心導管報告判讀 | 2026'
---

<!-- _class: lead -->
# 右心導管報告判讀
## Reading the Right Heart Catheterization Report
### — 給胸腔內科醫師的講義 —

**謝慕揚 MD, PhD, FESC**｜2026-05-22

依 2022 ESC/ERS Pulmonary Hypertension Guidelines
[ESC/ERS 2022 PH Guidelines (DOI)](https://doi.org/10.1093/eurheartj/ehac237)

---

# 為什麼胸腔科醫師要會看 RHC？

- **RHC 是 PH 診斷與分型的金標準** (gold standard)
- 胸腔科常碰到的 PH 病人：
  - **COPD、ILD** → Group 3
  - **CTEPH** → Group 4（一定要排除！）
  - 不明呼吸困難轉介病例
- 不一定要親自做，但**必須看得懂**

> 核心訊息：RHC 報告其實只有 **6 個關鍵數字**。

---

<!-- _class: divider -->
# Part 1
## Swan-Ganz 導管路徑與測量

---

# 導管路徑與壓力測量點

```text
Internal jugular / Femoral vein
    ↓
Right Atrium (RA)         ← RAP / CVP
    ↓ (穿過 tricuspid valve)
Right Ventricle (RV)      ← RV systolic / end-diastolic
    ↓ (穿過 pulmonary valve)
Pulmonary Artery (PA)     ← PA systolic / diastolic / mean
    ↓ (氣球膨脹卡住)
Pulmonary Capillary Wedge ← PCWP (代表 LA pressure)
```

**測量時機：end-expiration，3 個呼吸週期取平均**

---

<!-- _class: divider -->
# Part 2
## 核心參數逐項解讀

---

# 1️⃣ Right Atrial Pressure (RAP)

| 項目 | 數值 |
|------|------|
| 正常 | 2–6 mmHg |
| 紅旗 | **Mean RAP > 14 mmHg** → RV failure，不良預後 |

**升高原因**：RV failure、TR/TS、tamponade、constrictive、容積過多
**降低原因**：低血容、出血

> 加護病房快速指標 — 但別忘了**單一數字 ≠ 容積狀態**

---

# 2️⃣ Right Ventricular Pressure (RVP)

| 項目 | 數值 |
|------|------|
| 正常 systolic | 15–30 mmHg |
| 正常 end-diastolic | 2–8 mmHg |

**判讀重點**：

- 沒有 **pulmonary stenosis** 時，**RV systolic = PA systolic**
- 若 RV − PA 落差 > 10 mmHg → 懷疑 PS
- RVEDP 升高 → RV failure、容積過多、心包疾病

---

# 3️⃣ Pulmonary Artery Pressure (PAP)

PA 壓力是**搏動性 (pulsatile)** — 有 systolic、diastolic、mean

| 項目 | 正常值 |
|------|--------|
| PA systolic (PASP) | 15–30 mmHg |
| PA diastolic (PADP) | 4–12 mmHg |
| **Mean PA (MPAP)** | **9–18 mmHg** |

---

<!-- _class: formula -->
# 🧮 MPAP 計算公式

```text
                PASP + 2 × PADP
    MPAP  =  ─────────────────────
                       3
```

⚠️ **不是算術平均** — diastolic 權重是 systolic 的 **2 倍**
（因為心臟舒張時間比收縮長）

### 例題
PA = 55/22 mmHg
MPAP = (55 + 2×22) / 3 = (55 + 44) / 3 = **33 mmHg** ✓

---

# 4️⃣ Pulmonary Capillary Wedge Pressure (PCWP)

別名：PAWP、PAOP

| 項目 | 數值 |
|------|------|
| 正常 | 4–12 mmHg |
| **PH 分型切點** | **> 15 mmHg = post-capillary** |

**PCWP ≈ LA pressure ≈ LVEDP**

> **這一個數字決定了整個 PH 病人的診斷路徑**：
>
> - PCWP > 15 → 左心問題 → **Group 2**
> - PCWP ≤ 15 → 肺血管/肺實質問題 → **Group 1, 3, 4, 5**

---

# 5️⃣ Cardiac Output (CO) 與 Cardiac Index (CI)

| 項目 | 正常 |
|------|------|
| CO | 4–8 L/min |
| CI = CO/BSA | 2.5–4.0 L/min/m² |

**兩種測量方法**：

| 方法 | 原理 | 適用 |
|------|------|------|
| **Thermodilution** | 注冷食鹽水測溫變化 | 常規 |
| **Fick** | VO₂ / (CaO₂ − CvO₂) | 低 CO、嚴重 TR、shunt 病人 |

⚠️ **算 PVR 要用同一筆 CO**

---

<!-- _class: formula -->
# 6️⃣ Pulmonary Vascular Resistance (PVR)

## ⭐ 這是整份報告**最重要的計算數字**

```text
                MPAP − PCWP
    PVR  =  ─────────────────
                    CO
```

- 單位 = **Woods Unit (WU)** = mmHg/(L/min)
- 1 WU = 80 dyn·s·cm⁻⁵

---

# 為什麼這公式有意義？

完全是水管原理 — **Ohm's Law 在血管的版本**：

$$ \Delta P = Q \times R \quad \Rightarrow \quad R = \Delta P / Q $$

| 變數 | 對應 |
|------|------|
| **ΔP (壓力差)** | MPAP − PCWP（肺循環入口 − 出口） |
| **Q (流量)** | Cardiac Output |
| **R (阻力)** | PVR |

→ PVR **只反映肺血管本身的阻力**，已把左心壓力扣除

---

# PVR 正常值與切點

| PVR | 解讀 |
|-----|------|
| < 2 WU | 正常 |
| **≥ 2 WU** | **2022 ESC/ERS 新切點 — 有肺血管疾病** |
| > 5 WU | 嚴重肺血管疾病 |

> 舊 guideline (2015) 用 > 3 WU；**2022 新版降到 > 2 WU**

---

<!-- _class: formula -->
# 🧮 PVR 手算三步驟

**Step 1**：算 MPAP
PA = 60/25 → MPAP = (60 + 2×25)/3 = **37 mmHg**

**Step 2**：找 PCWP
PCWP = 12 mmHg

**Step 3**：套公式
CO = 5 L/min
PVR = (37 − 12) / 5 = 25/5 = **5 WU**

→ **MPAP 高 + PCWP 正常 + PVR 高** = **Pre-capillary PH**

> 口訣：「**M 減 W，除以 C**」(MPAP minus Wedge, divided by CO)

---

<!-- _class: divider -->
# Part 3
## 肺動脈高壓的定義 (2022)

---

# 2022 ESC/ERS 完整定義

| 類型 | MPAP | PCWP | PVR |
|------|------|------|-----|
| **PH (any)** | **> 20 mmHg** | — | — |
| **Pre-capillary PH** | > 20 | **≤ 15** | **> 2 WU** |
| **Isolated post-cap (Ipc-PH)** | > 20 | **> 15** | ≤ 2 WU |
| **Combined (Cpc-PH)** | > 20 | **> 15** | **> 2 WU** |
| **Exercise PH** | MPAP/CO slope > 3 mmHg/L/min | — | — |

---

# 與 2015 版的差別

| 項目 | 舊 (2015) | 新 (2022) |
|------|-----------|-----------|
| MPAP cut-off | ≥ 25 mmHg | **> 20 mmHg** |
| PVR cut-off | > 3 WU | **> 2 WU** |
| 21–24 mmHg | 「正常」 | **已是 mild PH** |

> **臨床意義**：以前算「正常」的 borderline 病人，在高風險族群（系統性硬皮症、CHD、家族史）現在要積極追蹤。

---

<!-- _class: divider -->
# Part 4
## PA 壓力高低的臨床意義

---

# 🔑 一張表搞懂鑑別診斷

| MPAP | PCWP | PVR | 解讀 | WHO Group |
|------|------|-----|------|-----------|
| ≤20 | 正常 | 正常 | 沒有 PH | — |
| **>20** | ≤15 | **>2** | **Pre-capillary** | 1, 3, 4, 5 |
| **>20** | **>15** | ≤2 | **Ipc-PH** | **2** |
| **>20** | **>15** | **>2** | **Cpc-PH** | **2 + remodeling** |
| 高 | 正常 | 正常 | **High-flow** (shunt, 貧血, 甲亢) | — |

---

# 為什麼會「高 MPAP 但 PVR 正常」？

**例**：MPAP 30, PCWP 8, **CO 10 (high)**
→ PVR = (30 − 8) / 10 = **2.2** → 接近正常

通常是 **高流量狀態 (high-flow state)**：

- Left-to-right shunt (ASD, VSD)
- 嚴重貧血
- 甲狀腺亢進
- 透析瘻管流量過大

➡️ **不是真正的肺血管疾病**

---

# 「低 PA 壓力」的陷阱

- 嚴重低血容
- Cardiogenic shock 心輸出極低
- 嚴重 tricuspid stenosis

⚠️ **小心「假性正常 (pseudo-normalization)」**：

> 嚴重 PH 病人若心衰惡化、CO 大幅下降，PA 壓力可能「降下來」 — 但 PVR 反而更高、預後更差

---

<!-- _class: divider -->
# Part 5
## WHO 五大分類 (Group 1–5)

---

# WHO Group 1–5 (2022)

| Group | 名稱 | 機轉 | 代表病因 |
|-------|------|------|----------|
| **1** | **PAH** | Pre-cap | IPAH, HPAH, 藥物, SSc, HIV, CHD, Portopulmonary |
| **2** | **Left Heart Disease** | Post-cap | HFpEF, HFrEF, valvular disease |
| **3** | **Lung Disease / Hypoxia** | Pre-cap | **COPD**, ILD, OSA, 高海拔 |
| **4** | **PA Obstructions** | Pre-cap | **CTEPH**, 腫瘤, 血管炎 |
| **5** | **Multifactorial** | 混合 | 血液病, sarcoid, CKD, fibrosing mediastinitis |

---

# 胸腔內科最常碰到 — Group 3

## Lung Disease / Hypoxia

- **COPD、ILD、混合性肺病、OSA、高海拔**
- 通常 MPAP **20–35 mmHg**（mild）
- 若 MPAP > 35 mmHg → **severe PH-lung disease**，預後變差
- 治療**主軸是治療肺病本身** + 氧氣
- **INCREASE trial**：inhaled treprostinil 在 ILD + PH 有正面結果
  [INCREASE trial — NEJM 2021](https://doi.org/10.1056/NEJMoa2008470)

---

# 胸腔內科最常碰到 — Group 4

## CTEPH (Chronic Thromboembolic PH)

- 急性 PE 病人約 **2–4% 進展為 CTEPH**
- 診斷必須做 **V/Q scan** ⚠️ 不能只用 CTPA（敏感度不夠）
- ✅ **CTEPH 是少數可以治癒的肺高壓！**
  - **PEA** (Pulmonary endarterectomy) — 首選
  - **BPA** (Balloon pulmonary angioplasty) — 無法手術者
  - **Riociguat** — 藥物選擇
- 任何不明 PH **一定要排除 CTEPH**

---

# 治療路徑差異

| Group | 主要治療策略 |
|-------|--------------|
| 1 | PAH 標靶 (ERA, PDE5i, PCAs, sotatercept)，轉介 PH center |
| 2 | 治療左心病本身；**PAH 標靶不建議** |
| 3 | 治療肺病、氧氣；selective inhaled treprostinil |
| 4 | **轉介 CTEPH center** — PEA / BPA / riociguat |
| 5 | 治療原發病 |

---

# 🎯 胸腔內科同仁的關鍵決策

看到 PH 病人，問自己三件事：

> 1. **PCWP 高不高？**
>    高 → Group 2，回去查左心。
>
> 2. **有沒有 COPD/ILD？**
>    有 → Group 3，先治本病。
>
> 3. **V/Q scan 有沒有 mismatch？**
>    有 → Group 4，**立刻**轉介 CTEPH center。

---

<!-- _class: divider -->
# Part 6
## 實戰案例

---

# Case 1 — COPD GOLD III, 65 ♀

| Parameter | 數值 |
|-----------|------|
| RA mean | 9 |
| PA | **50/22** |
| MPAP | ? |
| PCWP | 11 |
| CO | 4.0 L/min |

**計算**：

- MPAP = (50 + 2×22)/3 = **31 mmHg**
- PVR = (31 − 11) / 4.0 = **5.1 WU**

→ MPAP 高 + PCWP 正常 + PVR 高 → **Pre-capillary PH**
→ COPD 病史 → **Group 3 PH**

---

# Case 2 — HFpEF, 72 ♂

| Parameter | 數值 |
|-----------|------|
| RA mean | 14 |
| PA | **55/26** |
| MPAP | ? |
| PCWP | **22** ⚠️ |
| CO | 4.5 L/min |

**計算**：

- MPAP = (55 + 2×26)/3 = **36 mmHg**
- PVR = (36 − 22) / 4.5 = **3.0 WU**

→ MPAP 高 + **PCWP 高** + PVR 高 → **Cpc-PH (Group 2 + remodeling)**
→ 優化 HF treatment；**不要**直接給 PAH 藥

---

# Case 3 — 過去 PE 病史, 48 ♀, 6 個月後仍喘

| Parameter | 數值 |
|-----------|------|
| RA mean | 11 |
| PA | **70/28** |
| MPAP | ? |
| PCWP | 9 |
| CO | 3.8 L/min |

**計算**：

- MPAP = (70 + 2×28)/3 = **42 mmHg**
- PVR = (42 − 9) / 3.8 = **8.7 WU** ⚠️

→ Pre-capillary，PVR 嚴重升高 → **強烈懷疑 CTEPH (Group 4)**
→ **立刻**安排 V/Q scan + 轉介 CTEPH center

---

<!-- _class: divider -->
# Part 7
## 常見陷阱與品質檢查

---

# PCWP 測量陷阱

1. **氣球未完全卡住** → 測到的還是 PA pressure
   - 檢查波形：有 a、v wave 才算到位
2. **嚴重 MR** → 大 v wave，高估 LV filling
3. **嚴重 COPD** → 胸腔內壓波動大，必須 **end-expiration** 讀
4. **PEEP 正壓通氣** → PCWP 虛高

---

# PVR 計算陷阱

- **用哪個 CO？**
  - 嚴重 TR、low CO state → **Fick 較準**
- **單位轉換**
  - 報告若是 dyn·s·cm⁻⁵ → ÷ 80 才得到 WU
- **Vasodilator testing**
  - IPAH 病人吸 NO 後重測 → 預測 CCB 反應

---

# Quality Check 清單

讀報告前先確認：

- [ ] 在**穩定狀態** (resting, awake)
- [ ] PCWP 波形合理（有 a、v wave）
- [ ] RA、RV、PA、PCWP 都記錄
- [ ] CO 標明測量方法
- [ ] **零點 (zero reference)** 在 mid-axillary line

---

<!-- _class: lead -->
# Take Home

### 1. RHC 報告只看 **6 個數字**
   RA、RV、PA、MPAP、**PCWP**、CO → 推 PVR

### 2. 三個 cut-off 背起來
   **MPAP > 20、PCWP > 15、PVR > 2 WU**

### 3. PCWP 決定 Group 2 vs others
   PCWP > 15 → 左心；PCWP ≤ 15 → 肺血管

### 4. 不明 PH **一定**要排除 CTEPH
   做 V/Q scan，不要只做 CTPA

---

<!-- _class: small-text -->
# 參考文獻

1. Humbert M, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. [*Eur Heart J*. 2022;43(38):3618-3731.](https://doi.org/10.1093/eurheartj/ehac237)
2. Simonneau G, et al. Haemodynamic definitions and updated clinical classification of PH. [*Eur Respir J*. 2019;53(1):1801913.](https://doi.org/10.1183/13993003.01913-2018)
3. Maron BA, et al. Revised definition of pulmonary hypertension. [*Eur Respir J*. 2024;63(4):2400087.](https://doi.org/10.1183/13993003.00087-2024)
4. Waxman A, et al. Inhaled Treprostinil in PH-ILD (INCREASE). [*N Engl J Med*. 2021;384(4):325-334.](https://doi.org/10.1056/NEJMoa2008470)
5. Delcroix M, et al. ERS Statement on CTEPH. [*Eur Respir J*. 2021;57(6):2002828.](https://doi.org/10.1183/13993003.02828-2020)
6. Hoeper MM, et al. Definitions and diagnosis of pulmonary hypertension. [*J Am Coll Cardiol*. 2013;62(25 Suppl):D42-D50.](https://doi.org/10.1016/j.jacc.2013.10.032)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
心臟內科｜結構性心臟病介入

*本講義為讀書會共筆之教學整理，依 2022 ESC/ERS Guidelines 編寫*
*僅供醫療專業同仁臨床教學參考，不作為個案診療依據*
