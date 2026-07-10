# HFpEF Diagnostic Pitfalls & Differentiation from Valvular Disease / HFpEF 診斷陷阱與瓣膜病鑑別

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-06-27**
**核心參考：[Eur Heart J — HFA-PEFF diagnostic algorithm (Pieske et al. 2019)](https://doi.org/10.1093/eurheartj/ehz641)**

---

## 目錄

1. [核心觀念：HFpEF 是「排除性診斷」](#1-核心觀念hfpef-是排除性診斷)
2. [正式診斷流程（Universal definition、H₂FPEF、HFA-PEFF）](#2-正式診斷流程)
3. [診斷陷阱總覽](#3-診斷陷阱總覽)
4. [陷阱詳述](#4-陷阱詳述)
5. [專節：Severe AS / MR 算不算 HFpEF？](#5-專節severe-as--mr-算不算-hfpef)
6. [生物標記與影像陷阱](#6-生物標記與影像陷阱)
7. [臨床重點整理（Clinical Pearls）](#7-臨床重點整理)
8. [參考文獻](#參考文獻)
9. [縮寫對照](#縮寫對照)

---

## 1. 核心觀念：HFpEF 是「排除性診斷」

心衰竭合併保留射出分率（Heart Failure with preserved Ejection Fraction, HFpEF）依 2021 通用定義為：
- 有 **心衰竭症狀／徵象**；
- **左心室射出分率（LVEF）≥ 50%**；
- 有 **左心室充填壓上升 / 舒張功能障礙** 的客觀證據（利鈉胜肽升高、影像、或運動誘發）。

> **關鍵：HFpEF 不是「EF 正常的心衰竭都算」，而是要先「排除掉其他有特定病因、且通常可治療的疾病」之後，剩下的那一群。** 把瓣膜病、類澱粉、縮窄性心包炎當成 HFpEF，是臨床上最常見、也最可惜的錯誤——因為這些都有專屬治療（修瓣、tafamidis、心包剝離手術）。

---

## 2. 正式診斷流程

### 2.1 兩套評分系統（互補，但常不一致）

**H₂FPEF score**（Reddy/Borlaug, 2018；偏向客觀、好記）

| 項目 | 內容 | 分數 |
|------|------|------|
| **H**eavy | BMI > 30 kg/m² | 2 |
| **H**ypertensive | 使用 ≥ 2 種降壓藥 | 1 |
| **F**ibrillation | 心房顫動（AF） | 3 |
| **P**ulmonary hypertension | 都卜勒 PASP > 35 mmHg | 1 |
| **E**lder | 年齡 > 60 歲 | 1 |
| **F**illing pressure | Echo E/e′ > 9 | 1 |

- **0–1 分**：低機率（可大致 rule out）
- **2–5 分**：中間機率 → 需進一步檢查 / 運動誘發
- **6–9 分**：高機率（可 rule in）

**HFA-PEFF score**（ESC/HFA, 2019；四步驟 P-E-F-F）

- **P**（Pretest）：症狀、共病、心電圖、基本 echo
- **E**（Echo + 利鈉胜肽）：三個面向計分 — 功能（e′、E/e′、TR velocity）、形態（LAVI、LV mass、RWT）、生物標記（NT-proBNP）。**主要項目 2 分、次要 1 分**；**≥ 5 分確診**、2–4 分需進一步。
- **F**（Functional）：**舒張壓力測試（diastolic stress echo）或侵入性運動血流動力學**。
- **F**（Final）：找特定病因（amyloid、HCM、缺血等）。

> ⚠️ **兩套分數對同一病人常給出不一致的結果（discordance）**，尤其落在中間區間時。不要把單一分數當作絕對標準。

### 2.2 一定不能省略的最後一步：找特定病因
HFA-PEFF 的最後一個 F（Final aetiology）正是本講義重點——**確認是不是「偽裝成 HFpEF 的特定病因」**。

### 2.3 一頁式診斷流程（Decision Flow）

```text
病人：HF 症狀/徵象 + LVEF ≥ 50%
        │
        ▼
[Step 1] 利鈉胜肽 + 完整 echo（瓣膜、LV 壁厚、LA、TR velocity、GLS）
        │
        ▼
[Step 2] 先排除「特定可治病因」？
   ├─ 重度 AS / 原發 MR / 重度 TR ───────►  瓣膜性心衰竭 → 修瓣 (TAVR/SAVR/TEER)
   ├─ 不對稱 LVH + ECG 低電壓 + 腕隧道 ──►  疑類澱粉 → PYP 掃描 / 切片 (tafamidis)
   ├─ septal bounce + 心包鈣化 ─────────►  縮窄性心包炎 → 心包剝離手術
   ├─ RHC：PCWP 正常 + PVR 高 ──────────►  前微血管 PH (PAH/CTEPH) → 標靶/手術
   └─ 貧血 / 甲亢 / AV fistula ─────────►  高輸出心衰 → 矯正根本病因
        │  （以上皆排除後）
        ▼
[Step 3] 充填壓證據是否足夠？(H₂FPEF / HFA-PEFF)
   ├─ 高機率 (H₂FPEF 6–9 / PEFF ≥5) ────►  診斷 HFpEF，開始治療
   ├─ 中間 (H₂FPEF 2–5 / PEFF 2–4) ─────►  運動誘發：diastolic stress / 侵入運動 PCWP
   └─ 低機率 (H₂FPEF 0–1) ──────────────►  找其他原因 (CAD、肺、deconditioning)
```

> **使用方式**：HFpEF 的診斷重心在 **Step 2（排除）**，而非急著在 Step 3 給分數。先排除瓣膜病、類澱粉、縮窄、前微血管 PH，再談 HFpEF。

---

## 3. 診斷陷阱總覽

| 陷阱（會偽裝成 HFpEF 的疾病） | 為什麼會誤判 | 鑑別關鍵 | 為什麼重要 |
|---|---|---|---|
| **瓣膜病**（severe AS、原發 MR、重度 TR） | EF 保留 + 鬱血症狀 | 心臟超音波瓣膜評估 | 治療是修瓣，不是 HFpEF 藥 |
| **心臟類澱粉（ATTR / AL）** | 浸潤造成舒張障礙、EF 早期保留 | 不對稱 LVH、低電壓 ECG、PYP scintigraphy | tafamidis 等專屬藥物 |
| **HCM / Fabry / sarcoidosis** | LVH + 舒張障礙 | CMR、基因、酵素、影像 | 各有專屬處置 |
| **縮窄性心包炎** | 鬱血、充填壓高、EF 正常 | 呼吸相依、septal bounce、心包鈣化 | 心包剝離可治癒 |
| **高輸出心衰**（貧血、甲亢、AV fistula） | 鬱血但心肌正常 | 病史、CO 測量 | 治療根本病因 |
| **前微血管肺高壓**（PAH / CTEPH, Group 1/4） | 右心衰像 HFpEF | RHC：PCWP 正常、PVR 高 | 用標靶 / 手術，非利尿為主 |
| **缺血性 / CAD、非心因呼吸困難** | 運動喘 | 缺血評估、肺功能、deconditioning | 方向完全不同 |

---

## 4. 陷阱詳述

### 4.1 瓣膜性心衰竭（本講義重點）

嚴重瓣膜病會造成「有保留 EF 的心衰竭」，但歸類為 **瓣膜性心衰竭（valvular HF）**，**不是 HFpEF**。三個結構性介入醫師必須掌握的灰色地帶：

#### (a) Paradoxical Low-Flow Low-Gradient AS（矛盾型低流量低壓差主動脈瓣狹窄）
- 發生在 **小腔室、向心性肥厚、僵硬的左心室**——這正是 HFpEF 的表現型。
- 即使 EF ≥ 50%，因每搏輸出量低（SVi < 35 mL/m²），壓差被低估（mean gradient < 40 mmHg）卻是**真正的重度 AS**（AVA < 1.0 cm²）。
- 與 HFpEF **生理重疊**，容易互相掩蓋；確診需 DSE / CT 鈣化分數輔助。

#### (b) 原發（退化／器質性）MR vs 次發（功能性）MR — 因果方向相反
- **原發 MR（瓣葉本身病變、脫垂）= 心衰竭的「病因」** → 不是 HFpEF，要修瓣。
- **次發／心房性功能性 MR（Atrial Functional MR, AFMR）**：瓣葉正常，因 **慢性高充填壓 → 左房擴大 / 左房病變（LA myopathy）→ 瓣環擴張** 而漏 → 是 **HFpEF 的「後果」**，可共存。常見於 AF + HFpEF。
- **臨床意義**：看到 MR 先問「瓣葉有沒有病變？」器質性 → valvular HF；功能性 → 可能是 HFpEF 的表徵。

#### (c) AS + 心臟類澱粉「雙病理」
- 老年、尤其低流量低壓差 AS 病人，**ATTR 類澱粉共存比例不低**（文獻報告約 1/8）。
- 兩者都造成 LVH + 舒張障礙 → 互為陷阱；TAVR 術前評估時值得警覺。

> **EF 假性偏高**：重度 MR 時大量血液逆流回左房，LVEF 數值「看起來」正常甚至偏高，但**前向輸出其實已下降**。別被 EF 數字騙了。

### 4.2 心臟類澱粉（Cardiac Amyloidosis, 尤其 ATTR）— 最該主動篩檢的「可治 HFpEF」
- 在 HFpEF 族群中盛行率約 **6–14%**（依族群與篩檢方式；González-López 報告 HFpEF + LV 壁厚 ≥ 12 mm 的老年人約 13%）。
- **紅旗（red flags）**：不成比例的向心性 LVH、**ECG 低電壓或電壓/質量不相稱**、腕隧道症候群病史（常為雙側、早於心臟症狀數年）、對 ACEi/ARB/β-blocker 異常不耐（低血壓）、NT-proBNP 不成比例升高。
- **診斷**：先排除 AL（血/尿免疫固定電泳 + free light chain）；ATTR 可用 **⁹⁹ᵐTc-PYP/DPD 骨骼掃描（Perugini grade 2–3）** 非侵入確診。
- **為什麼重要**：ATTR 有疾病修飾藥（tafamidis 等），不能只當一般 HFpEF 治療。

### 4.3 其他浸潤 / 特定心肌病
- **HCM**（含心尖型）、**Fabry disease**（α-Gal A 缺乏，X 性聯）、**心臟結節病（sarcoidosis）**、**血色素沉著症（hemochromatosis）**。
- 工具：**心臟磁振造影（CMR）** 看 LGE 型態與 T1/ECV、基因檢測、酵素活性。

### 4.4 縮窄性心包炎（Constrictive Pericarditis）
- 鬱血、充填壓上升、EF 正常 → 很像 HFpEF，但**可手術治癒**。
- 線索：呼吸相依的心室交互依存（ventricular interdependence）、**septal bounce**、心包增厚 / 鈣化、肝靜脈血流型態；必要時侵入性同步測壓。

### 4.5 高輸出心衰（High-output HF）
- 貧血、甲狀腺亢進、動靜脈瘻管、肝病、Paget's disease。
- 心肌本身正常，治療是**矯正根本病因**。

### 4.6 前微血管肺高壓（Precapillary PH, Group 1/4）
- PAH 或慢性栓塞性肺高壓（CTEPH）造成右心衰，臨床像 HFpEF。
- **右心導管（RHC）鑑別**：HFpEF 是 **後微血管型（PCWP > 15 mmHg）**；前微血管型 PCWP 正常、PVR 升高。治療方向完全不同。

### 4.7 缺血 / CAD 與非心因性呼吸困難
- 冠心病 / 微血管缺血、肥胖、體能退化（deconditioning）、COPD、CKD 容積過量，都可能被歸成 HFpEF。

---

## 5. 專節：Severe AS / MR 算不算 HFpEF？

**直接回答：原則上不算。** HFpEF 的定義就要求排除瓣膜病這類特定病因；嚴重 AS / 原發 MR 屬 **valvular HF**，治療是修瓣。

| 情況 | 算 HFpEF？ | 說明與處置 |
|------|-----------|-----------|
| **Severe AS** | ❌ 不是 → valvular HF | 治療 = TAVR / SAVR。但 **paradoxical LFLG AS** 與 HFpEF 表現型重疊，且可能 **AS + ATTR 雙病理** |
| **Severe primary / organic MR**（瓣葉病變、脫垂） | ❌ 不是 → valvular HF | 治療 = 修瓣（surgery / TEER）。注意 **EF 被逆流假性墊高** |
| **Secondary / atrial functional MR**（瓣葉正常、LA 擴大致瓣環擴張） | ✅ 可視為 HFpEF 的後果，可共存 | 是高充填壓 + 左房病變的標記，治療以處理 HFpEF / AF / 容積為主 |

> **一句話總結**：**原發瓣膜病 = HFpEF 的「病因」，要排除（不是 HFpEF）；功能性／心房性 MR = HFpEF 的「後果」，可並存。** 臨床上三個重疊陷阱要記得：**LFLG AS、AS + amyloid、atrial functional MR**。

---

## 6. 生物標記與影像陷阱

### 6.1 利鈉胜肽（BNP / NT-proBNP）
- **可以是正常的，尤其肥胖病人**——脂肪組織會壓低利鈉胜肽 → **正常 BNP 不能排除 HFpEF**。
- **AF 會拉高**（需用較高閾值，如 HFA-PEFF：NT-proBNP SR > 220、AF > 660 pg/mL）。
- **腎功能差、高齡**亦升高 → 容易偽陽性。

### 6.2 EF 與影像
- **EF 保留 ≠ 收縮功能正常**：整體縱向應變（GLS）常已受損（subclinical dysfunction）。
- **重度 MR 使 EF 假性偏高**（前向輸出已降）。
- **舒張功能分級不完美**：E/e′、LAVI、TR velocity 各有侷限；LA 大可能是 AF 造成，而非充填壓。

### 6.3 「靜態正常」不能排除 → 需誘發
- 休息時充填壓可能正常，**運動才現形**。對 unexplained exertional dyspnea，應做 **diastolic stress echo** 或 **侵入性運動血流動力學（運動 PCWP）** 以 unmask。

---

## 7. 臨床重點整理

> **Pearl 1**：HFpEF 是排除性診斷——**先排除瓣膜病、類澱粉、縮窄性心包炎、前微血管 PH**，再下 HFpEF。

> **Pearl 2**：Severe AS 與原發 MR 不是 HFpEF，是要修的瓣膜病；**LFLG AS、AS+amyloid、atrial functional MR** 是三個會與 HFpEF 重疊的陷阱。

> **Pearl 3**：看到 MR 先分「器質性 vs 功能性」——器質性是病因（修瓣），功能性是 HFpEF 的後果。

> **Pearl 4**：肥胖病人 **BNP 正常不能排除 HFpEF**；AF 病人 BNP 要用較高閾值。

> **Pearl 5**：老年 + 不對稱 LVH + ECG 低電壓 + 雙側腕隧道 → 主動篩 **ATTR 類澱粉**（PYP scintigraphy），因為它「可治」。

> **Pearl 6**：靜態 echo 正常的喘，別急著否定——用 **運動誘發（diastolic stress / 侵入性運動 PCWP）** 確認。

---

## 參考文獻

1. Bozkurt B, Coats AJS, Tsutsui H, et al. Universal definition and classification of heart failure. [*Eur J Heart Fail*. 2021;23(3):352-380.](https://doi.org/10.1002/ejhf.2115)
2. Pieske B, Tschöpe C, de Boer RA, et al. How to diagnose heart failure with preserved ejection fraction: the HFA-PEFF diagnostic algorithm. [*Eur Heart J*. 2019;40(40):3297-3317.](https://doi.org/10.1093/eurheartj/ehz641)
3. Reddy YNV, Carter RE, Obokata M, et al. A Simple, Evidence-Based Approach to Help Guide Diagnosis of Heart Failure With Preserved Ejection Fraction (H₂FPEF). [*Circulation*. 2018;138(9):861-870.](https://doi.org/10.1161/CIRCULATIONAHA.118.034646)
4. González-López E, Gallego-Delgado M, Guzzo-Merello G, et al. Wild-type transthyretin amyloidosis as a cause of heart failure with preserved ejection fraction. [*Eur Heart J*. 2015;36(38):2585-2594.](https://doi.org/10.1093/eurheartj/ehv338)
5. AbouEzzeddine OF, Davies DR, Scott CG, et al. Prevalence of Transthyretin Amyloid Cardiomyopathy in Heart Failure With Preserved Ejection Fraction. [*JAMA Cardiol*. 2021;6(11):1267-1274.](https://doi.org/10.1001/jamacardio.2021.3070)
6. Hahn VS, Yanek LR, Vaishnav J, et al. Endomyocardial Biopsy Characterization of Heart Failure With Preserved Ejection Fraction and Prevalence of Cardiac Amyloidosis. [*JACC Heart Fail*. 2020;8(9):712-724.](https://doi.org/10.1016/j.jchf.2020.04.007)
7. Deferm S, Bertrand PB, Verbrugge FH, et al. Atrial Functional Mitral Regurgitation: JACC Review Topic of the Week. [*J Am Coll Cardiol*. 2019;73(19):2465-2476.](https://doi.org/10.1016/j.jacc.2019.02.061)
8. Farhan S, Silbiger JJ, Halperin JL, et al. Pathophysiology, Echocardiographic Diagnosis, and Treatment of Atrial Functional Mitral Regurgitation: JACC State-of-the-Art Review. [*J Am Coll Cardiol*. 2022;80(24):2314-2330.](https://doi.org/10.1016/j.jacc.2022.09.046)
9. Dumesnil JG, Pibarot P, Carabello B. Paradoxical low flow and/or low gradient severe aortic stenosis despite preserved left ventricular ejection fraction. [*Eur Heart J*. 2010;31(3):281-289.](https://doi.org/10.1093/eurheartj/ehp361)
10. Clavel MA, Magne J, Pibarot P. Low-gradient aortic stenosis. [*Eur Heart J*. 2016;37(34):2645-2657.](https://doi.org/10.1093/eurheartj/ehw096)

---

## 縮寫對照

| 縮寫 | 全名 | 中文 |
|------|------|------|
| HFpEF | Heart Failure with preserved Ejection Fraction | 保留射出分率心衰竭 |
| LVEF | Left Ventricular Ejection Fraction | 左心室射出分率 |
| AS | Aortic Stenosis | 主動脈瓣狹窄 |
| MR | Mitral Regurgitation | 二尖瓣逆流 |
| TR | Tricuspid Regurgitation | 三尖瓣逆流 |
| LFLG AS | Low-Flow Low-Gradient Aortic Stenosis | 低流量低壓差主動脈瓣狹窄 |
| AFMR | Atrial Functional Mitral Regurgitation | 心房性功能性二尖瓣逆流 |
| ATTR | Transthyretin Amyloidosis | 轉甲狀腺素蛋白類澱粉沉積 |
| AL | Light-chain Amyloidosis | 輕鏈類澱粉沉積 |
| HCM | Hypertrophic Cardiomyopathy | 肥厚型心肌病 |
| LVH | Left Ventricular Hypertrophy | 左心室肥厚 |
| CMR | Cardiac Magnetic Resonance | 心臟磁振造影 |
| LGE | Late Gadolinium Enhancement | 延遲釓增強 |
| LAVI | Left Atrial Volume Index | 左房容積指數 |
| GLS | Global Longitudinal Strain | 整體縱向應變 |
| DSE | Dobutamine / Diastolic Stress Echo | 多巴酚丁胺／舒張壓力超音波 |
| PASP | Pulmonary Artery Systolic Pressure | 肺動脈收縮壓 |
| PCWP | Pulmonary Capillary Wedge Pressure | 肺微血管楔壓 |
| PVR | Pulmonary Vascular Resistance | 肺血管阻力 |
| RHC | Right Heart Catheterization | 右心導管 |
| PH | Pulmonary Hypertension | 肺高壓 |
| CTEPH | Chronic Thromboembolic Pulmonary Hypertension | 慢性血栓栓塞性肺高壓 |
| BNP / NT-proBNP | (N-terminal pro) B-type Natriuretic Peptide | （N 端前）B 型利鈉胜肽 |
| AVA | Aortic Valve Area | 主動脈瓣口面積 |
| SVi | Stroke Volume index | 每搏輸出量指數 |
| TAVR / SAVR | Transcatheter / Surgical Aortic Valve Replacement | 導管／外科主動脈瓣置換 |
| TEER | Transcatheter Edge-to-Edge Repair | 導管緣對緣修補 |
| PYP / DPD | ⁹⁹ᵐTc-pyrophosphate / -DPD scintigraphy | 焦磷酸鹽骨骼掃描 |

---

*本文件僅供醫療專業人員教學參考。整理：謝慕揚 MD, PhD, FESC*
