# A Simple Algorithm for Differential Diagnosis in Hemodynamic Shock Based on LVOT VTI Measurement

# 以 LVOT VTI 為基礎的血流動力學休克鑑別診斷演算法

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-04-03**
**來源：[*The Ultrasound Journal*. 2022;14:36.](https://doi.org/10.1186/s13089-022-00286-2)**

---

## 目錄

1. [核心發現摘要](#核心發現摘要)
2. [研究背景](#1-研究背景)
3. [VTI 的原理與計算](#2-vti-的原理與計算)
4. [VTI-Based Algorithm](#3-vti-based-algorithm)
5. [臨床案例](#4-臨床案例)
6. [討論與臨床意義](#5-討論與臨床意義)
7. [參考文獻](#參考文獻)

---

## 核心發現摘要

> **核心概念**：LVOT VTI（左心室流出道速度時間積分）可作為 stroke volume 的替代指標，以功能性觀點評估血流動力學休克，優於傳統結構性評估。
>
> **關鍵數值**：
> - **VTI > 20 cm** → Adequate forward flow → 考慮 **Distributive shock**
> - **VTI 16–20 cm** → Gray zone → 結合臨床判斷
> - **VTI < 16 cm** → Low cardiac output → 依序排除 Tamponade → RV failure → LV failure → Valvular disease → Hypovolemia
>
> **臨床意義**：結構性心臟異常（如 low EF）不一定需要治療，除非造成 low cardiac output（VTI < 18 cm）。

---

## 1. 研究背景

### 研究資訊

- **標題**：A simple algorithm for differential diagnosis in hemodynamic shock based on left ventricle outflow tract velocity–time integral measurement: a case series
- **作者**：Mercadal J, Borrat X, Hernández A, Denault A, Beaubien-Souligny W, González-Delgado D, Vives M; Spanish Critical Care Ultrasound Network Group
- **期刊**：*The Ultrasound Journal* (2022)
- **DOI**：[10.1186/s13089-022-00286-2](https://doi.org/10.1186/s13089-022-00286-2)

### 問題陳述

傳統心臟超音波在 ICU 的應用存在以下挑戰：
1. 缺乏標準化訓練認證
2. 學習曲線長
3. **現有演算法過度強調「結構性」觀點**，未能提供清晰的治療指引

### 結構性 vs 功能性觀點

| 觀點 | 傳統結構性 | 本文功能性 |
|------|-----------|-----------|
| **評估重點** | LVEF、室壁運動、瓣膜形態 | Forward flow (VTI) |
| **問題** | 結構異常不等於需要治療 | 以灌流為導向的決策 |
| **風險** | 可能導致不必要的治療 | 避免過度治療 |

---

## 2. VTI 的原理與計算

### 什麼是 VTI？

**VTI (Velocity-Time Integral)** 是脈衝波都卜勒在 LVOT 測得的速度-時間曲線下面積，代表每次心跳通過該點的**血柱長度（cm）**。

### 計算公式

**Stroke Volume = VTI × CSA**

其中 CSA (Cross-Sectional Area) = π × (LVOT diameter / 2)²

### 標準化 VTI 的概念

由於 LVOT 直徑測量的再現性差，本文建議：

1. 假設 **LVOTd = 2 cm**（人群平均值：20.3 ± 2.3 mm）
2. **SV ≈ VTI × π（即 VTI × 3.14）**
3. VTI 18 cm → SV ≈ 56.5 mL（接近正常下限 60 mL）

### VTI 與 SV 對照表

| VTI (cm) | 13 | 14 | 15 | 16 | 17 | **18** | 19 | 20 | 21 | 22 | 23 | 24 |
|----------|----|----|----|----|----|----|----|----|----|----|----|----|
| **SV (mL)** | 40.8 | 43.9 | 47 | 50.1 | 53.4 | **56.5** | 59.6 | 62.8 | 65.9 | 69.1 | 72.2 | 75.4 |

> **Pearl**：VTI 18 cm 是區分正常與 low SV 的分界點。考慮到測量時常低估 VTI，本演算法採用 **16–20 cm 作為 gray zone**。

### 測量技巧

- **切面**：Apical 5-chamber 或 Apical 3-chamber view
- **取樣位置**：Aortic valve 近端 1 cm 處
- **品質指標**：
  - 頻譜內部「暗」、外緣「亮」
  - 應包含 aortic valve closure click
  - AF 時取 5 次平均

### RVOT VTI

- **RVOT 直徑**稍大於 LVOT（21.7 ± 3.14 mm vs 20.3 ± 2.3 mm）
- **RVOT VTI cutoff** 應略低：**15 cm**（而非 18 cm）
- 適用切面：Subcostal short-axis RVOT 或 Parasternal long-axis RV outflow

---

## 3. VTI-Based Algorithm

### 演算法流程圖

```text
                    Clinical signs of shock
                            |
                    Basic Echocardiography
                            |
              Cardiovascular system forward flow
                            |
                   LVOT/RVOT VTI measurement
                            |
            ┌───────────────┼───────────────┐
            |               |               |
         < 16 cm        16-20 cm         > 20 cm
            |          (Gray zone)          |
            |               |               |
      Low Cardiac      Clinical         DISTRIBUTIVE
        Output         context              SHOCK
            |          crucial              |
            |               |          Vasopressors
            ↓               ↓          then reassess
```

### VTI < 16 cm：Low Cardiac Output 的鑑別診斷

**依序評估：**

1. **Pericardial function** → Cardiac tamponade?
   - 中-大量心包積液
   - RA 或 RV collapse
   - IVC 擴張無變異

2. **RV function** → Obstructive shock?
   - RV/LV area ratio > 1
   - TAPSE < 14 mm
   - IVC 擴張無變異
   - IVS paradoxical motion
   - **原因**：Massive PE、Tension pneumothorax、Acute cor pulmonale (ARDS, COPD)、Decompensated chronic PHTN

3. **LV function** → Cardiogenic shock?
   - Visual LVEF < 40%
   - LV 擴大
   - **原因**：Sepsis cardiomyopathy、MI、Stress cardiomyopathy、Decompensated cardiomyopathy、Myocarditis

4. **Valvular function** → Cardiogenic valvular shock?
   - Acute massive MR/AR
   - Critical AS 或 MS

5. **Fluid responsiveness** → Hypovolemic shock?
   - **自主呼吸**：VTI increase > 12% by PLRT 或 VTI increase > 10% by mini-fluid challenge
   - **機械通氣**：IVC distensibility > 13% 或 Aortic VTI/Peak velocity variation > 10%

### VTI > 20 cm：Distributive Shock

- **代表**：Adequate stroke volume
- **意義**：休克原因是 **low systemic vascular resistance**
- **治療**：Vasopressors ± 根據臨床進展再評估
- **原因**：Sepsis、Anaphylaxis、SIRS、Post-CPB、Pancreatitis、Post-MI、Post massive transfusion

### Gray Zone (VTI 16–20 cm)

需結合**組織灌流指標**判斷：
- Arterial lactate
- ScvO2
- Venous-arterial CO2 gap

> **Pearl**：若 hypoperfusion 持續，儘管 SaO2 和 Hb 已優化，應採取措施增加 SV。

---

## 4. 臨床案例

### Case 1：Anesthesia-Induced Hypotension with Low EF

| 項目 | 內容 |
|------|------|
| **患者** | 73 歲，DM、HTN、dilated IHD with LVEF 25–30%，接受 diuretic 治療 |
| **情境** | 因急性膽囊炎行緊急膽囊切除術，麻醉誘導後 BP 60/30，HR 100，對 volume 和 ephedrine 反應不佳 |
| **鑑別診斷** | (a) Septic shock from cholecystitis (b) Cardiogenic shock from acute IHD (c) Relative hypovolemia from diuretics |
| **TTE 發現** | LVOT VTI **19 cm**，CO 5.9 L/min，IVC 20 mm，distensibility 10%，E/A 1.2 |
| **判讀** | 儘管 LVEF 低，但 forward flow adequate（因慢性 dilated cardiomyopathy 有高 EDV 代償） |
| **診斷** | **Distributive shock**（麻醉藥物導致血管阻力下降） |
| **治療** | Vasopressors（而非 inotropes 或大量輸液） |

> **Pearl**：低 LVEF 不等於 cardiogenic shock！若 VTI adequate，應考慮 distributive shock。

---

### Case 2：Post-Surgical Shock with Multiple Comorbidities

| 項目 | 內容 |
|------|------|
| **患者** | 67 歲男性，CKD on HD、兩次 PE 病史（正在抗凝）、2006 年 MI 後 chronic IHD |
| **情境** | 左臂動靜脈瘻管膿瘍引流術後 2 小時，嚴重低血壓，HR 110，lactate 4.5 mmol/L，ScvO2 63% |
| **鑑別診斷** | (a) Hypovolemia from bleeding (b) Septic shock from abscess (c) Obstructive shock from new PE (d) Cardiogenic shock from new MI |
| **TTE 發現** | LVEF ~35%，RV/LV 0.9，TAPSE 13 mm，LVOT VTI **21 cm**，**PLRT 後 VTI 增加 13%**，IVC 15 mm，distensibility 20% |
| **判讀** | 所有結構參數都 impaired，但 VTI 21 cm + HR 110 → CO 7.2 L/min（adequate） |
| **診斷** | **Distributive shock**（SIRS/Sepsis）合併 **fluid responsive** |
| **治療** | 先 fluid therapy，再加 vasopressors，血流動力學明顯改善 |

> **Pearl**：當多個結構性參數都異常時，以 **VTI 為主導**判斷主要貢獻因素。

---

### Case 3：Mixed Shock with Stress Cardiomyopathy

| 項目 | 內容 |
|------|------|
| **患者** | 42 歲女性，無過去病史，因 NSAIDs 導致十二指腸潰瘍穿孔行緊急剖腹探查，合併出血 |
| **情境** | 術後瀰漫性續發性腹膜炎，需高劑量 noradrenaline 0.4 mcg/kg/min，PCT 20 ng/mL，CRP 30 mg/L |
| **病程演變** | 術後 24h ECG 出現 inferolateral ST elevation，但 TTE 示 LVOT VTI **21.5 cm**，LV 收縮正常。數小時後出現 bigeminy，再次 TTE 示 anterior/anteroseptal/apical akinesia，LVOT VTI **降至 14 cm**，LVEF 35%，IVC 22 mm（distensibility 5%），E/A 1.9 |
| **診斷** | **Mixed shock**（Distributive + Cardiogenic from stress cardiomyopathy），後經 coronary angiography 確認正常 |
| **治療** | Dobutamine 5 mcg/kg/min + diuretics → VTI 改善至 17 cm → 4 天後 LV 收縮恢復，VTI 回升至 21 cm，停用 dobutamine |

> **Pearl**：連續監測 VTI 可追蹤治療反應，VTI 的變化比 LVEF 更即時反映 hemodynamic status。

---

### Case 4：Hypovolemic Shock Post-Surgery

| 項目 | 內容 |
|------|------|
| **患者** | 65 歲男性，HTN、DM、preserved LVEF 的 IHD，因升結腸癌穿孔行右半結腸切除術，術中出血 1.5 L |
| **情境** | 術後 24h 逐漸加重的低血壓和心搏過速，需 noradrenaline 0.5 mcg/kg/min + vasopressin 0.03 U/min，lactate 3.5 mmol/L，ScvO2 64%，oliguria < 0.5 mL/kg/h |
| **TTE 發現** | LV 無擴大，moderate inferoseptal/inferior hypokinesia，RV 正常，IVC **8 mm**（distensibility 20%），LVOT VTI **16 cm**，E/A 0.9（低充盈壓），**PLRT 後 VTI 增加 15%** |
| **診斷** | **Hypovolemic shock**（術中大量失血未完全補充） |
| **治療** | 500 mL fluid → 血流動力學改善 → noradrenaline 降至 0.25 mcg/kg/min |

> **Pearl**：Small IVC + Low E/A + Fluid responsive + Low VTI = 經典 hypovolemic shock 表現。

---

## 5. 討論與臨床意義

### 核心原則

1. **結構性異常不一定需要治療**，除非造成 low cardiac output (VTI < 18 cm)
2. **VTI adequate (> 18 cm) + 休克** → 主因是 distributive shock，即使 EF 低
3. **RV dysfunction + adequate VTI** → RV dysfunction 不是休克主因
4. **Fluid responsive + adequate VTI** → 不一定要給 fluid，除非有 tissue hypoperfusion

### 治療決策要點

| VTI | 建議 |
|-----|------|
| **> 20 cm** | Vasopressors 為主 |
| **16–20 cm** | 結合組織灌流指標（lactate, ScvO2, CO2 gap）決定 |
| **< 16 cm** | 依序排除：Tamponade → RV failure → LV failure → Valvular → Hypovolemia |

### 避免過度治療

- **不必要的 Inotropes**：adequate VTI 時使用可能增加心肌氧耗和心律不整風險
- **不必要的 Fluids**：adequate VTI + fluid responsive 但無 hypoperfusion → 不需輸液
- **目標**：針對休克主因治療，避免 fluid overload 和 inotrope 過度使用

### VTI 測量的限制

**SV 會被高估的情況：**
- Subaortic stenosis
- LVOT dynamic obstruction (SAM)
- Moderate-to-severe aortic regurgitation
- Aortic prosthetic valve

**解決方案**：改測 **RVOT VTI**

### Tachycardia 的判讀

| 類型 | 特徵 | CI | 處置 |
|------|------|----|----|
| **Compensatory** | 代償 low SV | < 2.2 L/min/m² | 需增加 SV（fluids 或 inotropes） |
| **Reactive** | 炎症反應（sepsis/SIRS） | > 2.5 L/min/m² | 治療原發病因 |

---

## 6. 結論

1. **VTI 是簡單、非侵入性的 SV 評估工具**，適合 ICU 床邊快速判讀
2. **功能性觀點**（以 forward flow 為中心）優於傳統結構性觀點
3. **VTI-based algorithm** 可協助：
   - 快速鑑別休克類型
   - 個人化治療決策
   - 避免過度治療（fluid overload、inotrope overuse）
4. **是否能改善臨床預後**尚待前瞻性研究證實

---

## 參考文獻

1. Expert Round Table on Ultrasound in ICU. International expert statement on training standards for critical care ultrasonography. [*Intensive Care Med*. 2011;37(7):1077-1083.](https://doi.org/10.1007/s00134-011-2246-9)

2. Cecconi M, De Backer D, Antonelli M, et al. Consensus on circulatory shock and hemodynamic monitoring. Task force of the European Society of Intensive Care Medicine. [*Intensive Care Med*. 2014;40(12):1795-1815.](https://doi.org/10.1007/s00134-014-3525-z)

3. Zhang Y, et al. Cardiac Output measurement via echocardiography versus thermodilution: a systematic review and meta-analysis. [*PLoS ONE*. 2019;14(10):e0222105.](https://doi.org/10.1371/journal.pone.0222105)

4. Porter TR, et al. Guidelines for the use of echocardiography as a monitor for therapeutic intervention in adults: a report from the American Society of Echocardiography. [*J Am Soc Echocardiogr*. 2015;28:40-56.](https://doi.org/10.1016/j.echo.2014.09.009)

5. Ristow B, et al. Left ventricular outflow tract and pulmonary artery stroke distances independently predict heart failure hospitalization and mortality: the heart and soul study. [*J Am Soc Echocardiogr*. 2011;24:565-572.](https://doi.org/10.1016/j.echo.2011.01.012)

6. Cholley B. Echocardiography in the intensive care unit: beyond "eye-balling". A plea for the broader use of the aortic velocity-time integral measurement. [*Intensive Care Med*. 2019;45:898-901.](https://doi.org/10.1007/s00134-019-05577-y)

7. Blanco P. Rationale for using the velocity-time integral and the minute distance for assessing the stroke volume and cardiac output in point-of-care settings. [*Ultrasound J*. 2020;12(1):21.](https://doi.org/10.1186/s13089-020-00170-x)

8. Kou S, Caballero L, Dulgheru R, et al. Echocardiographic reference ranges for normal cardiac chamber size: results from the NORRE study. [*Eur Heart J Cardiovasc Imaging*. 2014;15(6):680-690.](https://doi.org/10.1093/ehjci/jet284)

9. Sattin M, Burhani Z, Jaidka A, Millington SJ, Arntfield RT. Stroke volume determination by echocardiography. [*Chest*. 2022;161(6):1598-1605.](https://doi.org/10.1016/j.chest.2022.01.022)

---

*本文件僅供醫療專業人員教學參考，臨床決策請結合個案情況。*
