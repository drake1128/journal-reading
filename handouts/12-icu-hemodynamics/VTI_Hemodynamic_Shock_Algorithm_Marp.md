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
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
  section.case { background-color: #f8f9fa; }
  section.case h1 { font-size: 1.6em; }
footer: '謝慕揚 MD, PhD, FESC | VTI-Based Shock Algorithm | 2022'
---

<!-- _class: lead -->

# VTI-Based Algorithm for Hemodynamic Shock

## 以 LVOT VTI 為基礎的血流動力學休克鑑別診斷演算法

**謝慕揚 MD, PhD, FESC**
資料來源：[The Ultrasound Journal 2022;14:36](https://doi.org/10.1186/s13089-022-00286-2)
Spanish Critical Care Ultrasound Network Group

---

# 大綱

1. **問題背景**：為什麼需要新的演算法？
2. **VTI 原理**：什麼是 VTI？如何測量？
3. **核心演算法**：VTI-Based Algorithm
4. **臨床案例**：4 Cases Demonstration
5. **臨床應用要點**

---

<!-- _class: divider -->

# 第一部分：問題背景

---

# 傳統心超在 ICU 的挑戰

### 現有演算法的問題

- 過度強調 **結構性觀點**（structural perspective）
- 未能提供明確的 **治療指引**
- 容易導致 **不必要的治療**

### 臨床困境

> 看到 Low LVEF → 就給 Inotropes？
> 看到 Dilated RV → 就診斷 PE？
> 看到 Fluid Responsive → 就給 Fluids？

**這樣的決策邏輯可能是錯的！**

---

# 結構性 vs 功能性觀點

| | 結構性觀點 | 功能性觀點 |
|---|---|---|
| **評估重點** | LVEF、室壁運動、瓣膜形態 | **Forward Flow (VTI)** |
| **問題** | 結構異常 ≠ 需要治療 | 以灌流為導向決策 |
| **風險** | 過度治療 | 精準治療 |

### 核心原則

> **結構性心臟異常不一定需要治療，除非造成 Low Cardiac Output！**

---

<!-- _class: divider -->

# 第二部分：VTI 原理

---

# 什麼是 VTI？

**VTI = Velocity-Time Integral**
（速度-時間積分）

- Pulsed Wave Doppler 在 LVOT 測得的速度-時間曲線下面積
- 代表每次心跳通過該點的 **血柱長度（cm）**

### 計算公式

```text
Stroke Volume = VTI × CSA
              = VTI × π × (LVOT diameter / 2)²
```

---

# 標準化 VTI 的概念

### 問題：LVOT 直徑測量再現性差

### 解決方案：假設 LVOTd = 2 cm（人群平均值）

**簡化公式：**
```text
SV ≈ VTI × π ≈ VTI × 3.14
```

### VTI 與 SV 對照

| VTI (cm) | 14 | 16 | **18** | 20 | 22 | 24 |
|----------|----|----|--------|----|----|----|
| SV (mL) | 44 | 50 | **56.5** | 63 | 69 | 75 |

> **VTI 18 cm ≈ SV 60 mL（正常下限）**

---

# VTI 測量技巧

### 切面
- **Apical 5-chamber** 或 **Apical 3-chamber view**

### 取樣位置
- Aortic valve **近端 1 cm** 處

### 品質指標
- 頻譜內部「暗」、外緣「亮」
- 應包含 aortic valve closure click
- **AF 時取 5 次平均**

### RVOT VTI
- RVOT 直徑稍大 → cutoff 略低：**15 cm**

---

<!-- _class: divider -->

# 第三部分：VTI-Based Algorithm

---

# 演算法總覽

```text
              LVOT/RVOT VTI Measurement
                        |
        ┌───────────────┼───────────────┐
        |               |               |
     < 16 cm        16-20 cm         > 20 cm
        |          (Gray zone)          |
   Low Cardiac      Clinical       DISTRIBUTIVE
     Output         context            SHOCK
        |           crucial             |
        ↓               ↓          Vasopressors
   依序評估         結合組織灌流      then reassess
   (見下頁)           指標判斷
```

---

# VTI > 20 cm：Distributive Shock

### 意義
- Adequate forward flow（stroke volume 正常）
- 休克原因是 **Low Systemic Vascular Resistance**

### 常見原因
- Sepsis / SIRS
- Anaphylaxis
- Post-CPB
- Pancreatitis
- Post massive transfusion

### 治療
- **Vasopressors** 為主
- 給藥後 **再次評估 VTI**（確保 SV 未被高 afterload 降低）

---

# VTI < 16 cm：Low Cardiac Output

### 依序評估：

```text
1. Pericardial function → Tamponade?
         ↓ No
2. RV function → Obstructive shock?
         ↓ No
3. LV function → Cardiogenic shock?
         ↓ No
4. Valvular function → Valvular shock?
         ↓ No
5. Fluid responsiveness → Hypovolemic shock?
```

---

# Step 1: Cardiac Tamponade

### 評估指標
- 中-大量 pericardial effusion
- RA 或 RV collapse
- Dilated IVC with no variation

### 治療
- Fluids
- Pericardial drainage ± Surgery

---

# Step 2: Obstructive Shock (RV Failure)

### 評估指標
- **RV/LV area ratio > 1**
- **TAPSE < 14 mm**
- Dilated IVC with no variation
- Paradoxical IVS motion

### 常見原因
- Massive PE
- Tension pneumothorax
- Acute cor pulmonale (ARDS, COPD, Asthma)
- Decompensated chronic PHTN

---

# Step 3: Cardiogenic Shock (LV Failure)

### 評估指標
- Visual **LVEF < 40%**
- Visual LV dilatation
- Elevated filling pressure (E/A > 2)

### 常見原因
- Sepsis-related cardiomyopathy
- Myocardial infarction
- Stress cardiomyopathy (Takotsubo)
- Decompensated cardiomyopathy
- Myocarditis

### 治療
- Inotropes ± Vasopressors

---

# Step 4 & 5: Valvular & Hypovolemic Shock

### Step 4: Cardiogenic Valvular Shock
- Acute massive MR/AR
- Critical AS or MS

### Step 5: Fluid Responsiveness

| 呼吸模式 | 評估方法 |
|---------|---------|
| **自主呼吸** | VTI ↑ > 12% by PLRT 或 VTI ↑ > 10% by mini-fluid challenge |
| **機械通氣** | IVC distensibility > 13% 或 VTI/Peak velocity variation > 10% |

### 治療
- Fluids 或 RBC transfusion

---

# Gray Zone：VTI 16-20 cm

### 結合組織灌流指標判斷

- **Arterial lactate**
- **ScvO2**（< 70% = hypoperfusion）
- **Venous-arterial CO2 gap**（> 6 mmHg = hypoperfusion）

### 決策原則

> 若 hypoperfusion 持續（儘管 SaO2 和 Hb 已優化），
> 應採取措施增加 SV。

---

<!-- _class: divider -->

# 第四部分：臨床案例

---

<!-- _class: case -->

# Case 1：Low EF ≠ Cardiogenic Shock

### 患者
73 歲，DM、HTN、Dilated IHD with **LVEF 25-30%**

### 情境
急性膽囊炎行緊急手術，麻醉誘導後 BP 60/30，HR 100

### TTE 發現
| 參數 | 數值 |
|------|------|
| **LVOT VTI** | **19 cm** ✓ |
| CO | 5.9 L/min |
| IVC | 20 mm, distensibility 10% |

---

<!-- _class: case -->

# Case 1：診斷與治療

### 傳統思維
> 看到 LVEF 25% → 給 Inotropes！

### VTI-Based 思維
> VTI 19 cm = Adequate forward flow
> 儘管 EF 低，但 chronic dilated cardiomyopathy 有高 EDV 代償

### 診斷：**Distributive Shock**（麻醉藥物導致血管阻力下降）

### 治療：**Vasopressors**（而非 Inotropes）

> **Pearl：Low EF 不等於 Cardiogenic Shock！**

---

<!-- _class: case -->

# Case 2：Multiple Abnormalities - What to Prioritize?

### 患者
67 歲男性，CKD on HD、PE 病史、Chronic IHD

### 情境
動靜脈瘻管膿瘍引流術後 2h，BP 低，HR 110，Lactate 4.5

### TTE 發現
| 參數 | 數值 | 判讀 |
|------|------|------|
| LVEF | ~35% | Impaired |
| RV/LV ratio | 0.9 | Borderline |
| TAPSE | 13 mm | Impaired |
| **LVOT VTI** | **21 cm** ✓ | **Adequate** |
| PLRT | +13% | Fluid responsive |

---

<!-- _class: case -->

# Case 2：診斷與治療

### 困惑：所有參數都 impaired？

### VTI-Based 判讀
```text
VTI 21 cm + HR 110 → CO 7.2 L/min = Adequate!
```

### 診斷
- **主因：Distributive Shock**（Sepsis from abscess）
- **次因：Fluid Responsive with Hypoperfusion**

### 治療
1. **先給 Fluids**（因有 tissue hypoperfusion）
2. **再加 Vasopressors**

> **Pearl：以 VTI 為主導，判斷主要貢獻因素！**

---

<!-- _class: case -->

# Case 3：VTI 動態變化 - Mixed Shock

### 患者
42 歲女性，無過去病史，十二指腸潰瘍穿孔術後

### 病程演變

| 時間點 | VTI | 其他發現 | 診斷 |
|--------|-----|---------|------|
| 術後 24h | **21.5 cm** | Inferolateral ST↑, LV 正常 | Distributive |
| 數小時後 | **14 cm** ↓ | Anterior akinesia, LVEF 35%, IVC 22mm, E/A 1.9 | **Mixed Shock** |

### 最終診斷
Distributive + Cardiogenic from **Stress Cardiomyopathy**
（Coronary angiography 正常）

---

<!-- _class: case -->

# Case 3：治療與追蹤

### 治療
- **Dobutamine 5 mcg/kg/min**
- **Diuretics**

### VTI 追蹤

```text
VTI 14 cm → 17 cm → 21 cm（4 天後）
```

### 結果
- LV 收縮恢復
- 停用 Dobutamine

> **Pearl：連續監測 VTI 追蹤治療反應！**

---

<!-- _class: case -->

# Case 4：Classic Hypovolemic Shock

### 患者
65 歲男性，升結腸癌穿孔行右半結腸切除術，術中出血 1.5 L

### TTE 發現

| 參數 | 數值 | 意義 |
|------|------|------|
| **LVOT VTI** | **16 cm** | Low |
| **IVC** | **8 mm** | Small |
| **Distensibility** | 20% | Variable |
| **E/A ratio** | 0.9 | Low filling pressure |
| **PLRT** | +15% | Fluid responsive |

### 診斷：**Hypovolemic Shock**

### 治療：500 mL Fluid → NE 由 0.5 降至 0.25 mcg/kg/min

---

<!-- _class: divider -->

# 第五部分：臨床應用要點

---

# 核心治療原則

| VTI | 主要考慮 | 治療方向 |
|-----|---------|---------|
| **> 20 cm** | Distributive Shock | Vasopressors |
| **16-20 cm** | Gray Zone | 結合 Lactate, ScvO2 判斷 |
| **< 16 cm** | Low CO | 依序排除：Tamponade → RV → LV → Valvular → Hypovolemia |

---

# 避免過度治療

### 不必要的 Inotropes
- Adequate VTI 時使用 → 增加心肌氧耗和心律不整風險

### 不必要的 Fluids
- Adequate VTI + Fluid Responsive + **無 Hypoperfusion** → 不需輸液

### 關鍵原則

> **結構性異常不一定需要治療，除非造成 Low Cardiac Output！**

---

# Tachycardia 的判讀

| 類型 | 機制 | CI | 處置 |
|------|------|----|----|
| **Compensatory** | 代償 Low SV | < 2.2 L/min/m² | 增加 SV（fluids 或 inotropes） |
| **Reactive** | 炎症反應 | > 2.5 L/min/m² | 治療原發病因 |

---

# VTI 測量的限制

### SV 會被高估的情況
- Subaortic stenosis
- LVOT dynamic obstruction (SAM)
- Moderate-to-severe Aortic Regurgitation
- Aortic prosthetic valve

### 解決方案
改測 **RVOT VTI**（cutoff 15 cm）

---

# Take Home Messages

1. **VTI 是簡單、非侵入性的 SV 評估工具**

2. **VTI ≥ 18 cm = Normal SV**；**< 16 cm = Low SV**

3. **Low EF 不等於 Cardiogenic Shock**
   - 若 VTI adequate → 考慮 Distributive Shock

4. **以功能性觀點（Forward Flow）指導治療**
   - 避免不必要的 Inotropes 和 Fluids

5. **連續監測 VTI** 追蹤治療反應

---

<!-- _class: small-text -->

# 參考文獻

1. Mercadal J, et al. A simple algorithm for differential diagnosis in hemodynamic shock based on LVOT VTI measurement. [*Ultrasound J*. 2022;14:36.](https://doi.org/10.1186/s13089-022-00286-2)

2. Cecconi M, et al. Consensus on circulatory shock and hemodynamic monitoring. [*Intensive Care Med*. 2014;40(12):1795-1815.](https://doi.org/10.1007/s00134-014-3525-z)

3. Porter TR, et al. Guidelines for the use of echocardiography as a monitor for therapeutic intervention in adults. [*J Am Soc Echocardiogr*. 2015;28:40-56.](https://doi.org/10.1016/j.echo.2014.09.009)

4. Cholley B. Echocardiography in the ICU: beyond "eye-balling". [*Intensive Care Med*. 2019;45:898-901.](https://doi.org/10.1007/s00134-019-05577-y)

5. Blanco P. Rationale for using the VTI for assessing SV and CO in POCUS. [*Ultrasound J*. 2020;12(1):21.](https://doi.org/10.1186/s13089-020-00170-x)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
