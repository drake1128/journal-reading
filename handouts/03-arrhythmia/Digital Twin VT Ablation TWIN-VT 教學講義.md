# Digital Twin–Guided Ablation for Ventricular Tachycardia / 數位孿生引導心室頻脈消融術

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-04-02**
**原文連結：[*N Engl J Med*. 2026;394(13):1345-1347.](https://doi.org/10.1056/NEJMc2517822)**

---

## 目錄

- [1. 研究概述](#1-研究概述)
- [2. 研究方法](#2-研究方法)
- [3. 主要結果](#3-主要結果)
- [4. 臨床意義](#4-臨床意義)
- [5. 結論](#5-結論)
- [參考文獻](#參考文獻)

---

## 1. 研究概述

本文為 **TWIN-VT 研究** (NCT03536052) 之前瞻性研究報告，由 Johns Hopkins 團隊發表於 *New England Journal of Medicine*。研究在 **FDA investigational device exemption (IDE)** 核准下進行，探討利用病人專屬心臟數位孿生 (patient-specific cardiac digital twin) 技術引導缺血性心室頻脈 (ischemic ventricular tachycardia, VT) 之 catheter ablation。

### 研究背景

- 缺血性心肌病 (ischemic cardiomyopathy) 患者之 VT 源自慢性心肌梗塞疤痕 (chronic myocardial infarction scar) 內的折返迴路 (reentrant circuits)
- 傳統 VT ablation 依賴術中電生理標測 (electroanatomical mapping)，耗時且消融範圍 (lesion set) 較大
- Digital twin 技術可於術前透過電腦模擬預測 VT 迴路位置，實現精準消融

### 研究設計

| 項目 | 內容 |
|------|------|
| 研究類型 | 前瞻性單中心研究 (prospective single-center study) |
| 登錄號 | NCT03536052 |
| 法規核准 | FDA investigational device exemption |
| 收案人數 | 10 位受試者 |
| 適應症 | 缺血性心肌病合併 VT |
| 研究機構 | Johns Hopkins University |

---

## 2. 研究方法

### Digital Twin 工作流程

研究採用以下步驟建構病人專屬心臟數位孿生並引導消融：

```text
Step 1: Contrast-enhanced cardiac MRI (CE-CMR)
        影像擷取心臟結構與疤痕分布
            │
Step 2: 建構 cardiac digital twin
        根據 MRI 資料生成病人專屬心臟三維模型
            │
Step 3: Virtual VT induction (虛擬 VT 誘發)
        在數位孿生中進行 rapid pacing
        建立所有可能的 VT reentrant circuits
            │
Step 4: Virtual ablation (虛擬消融)
        在數位孿生中模擬消融
        找出最小有效消融靶點 (minimal effective ablation targets)
            │
Step 5: Import targets to electroanatomical mapping system
        將虛擬消融靶點匯入臨床標測系統
            │
Step 6: Clinical catheter ablation
        依據匯入靶點進行實際消融手術
```

### 關鍵技術特點

- **術前規劃 (pre-procedural planning)**：所有 VT 迴路分析與消融靶點規劃均於術前完成
- **Personalized model**：每位病人依據自身 cardiac MRI 建構獨一無二的數位孿生
- **Minimal lesion set**：虛擬消融目標為以最少的消融範圍達到最大療效
- **Integration with mapping system**：虛擬消融靶點可直接匯入臨床電生理標測系統

---

## 3. 主要結果

### 療效結果

| 指標 | 結果 |
|------|------|
| 追蹤時間 (follow-up) | 平均 405.4 天 |
| VT-free 比例 | **8/10 (80%)** 完全無 VT 復發 |
| 抗心律不整藥物 (antiarrhythmic drugs) | 8/10 未使用抗心律不整藥物 |
| ICD shock | **0 次**（所有受試者均無 ICD shock） |

### 2 位 VT 復發者

- 2 位受試者在術後 **1 個月內** 各發生 **1 次 VT episode**
- 均由 **antitachycardia pacing (ATP)** 成功終止
- 之後持續追蹤 VT-free
- 藥物已降階 (deescalated medications)

> **Pearl 1**: 即使有 VT 復發，也僅限於術後早期單次事件，且 ATP 可終止，不需 ICD shock

> **Pearl 2**: 所有 10 位受試者在追蹤期間均無 ICD shock，顯示 digital twin–guided ablation 可有效降低 ICD shock 負擔

---

## 4. 臨床意義

### 精準醫療 (Precision Medicine) 的典範

1. **個人化消融策略 (personalized ablation strategy)**
   - 每位病人的 VT 迴路取決於其獨特的疤痕型態 (scar morphology)
   - Digital twin 可於術前完整模擬所有可能的 VT 迴路
   - 實現真正的 patient-specific treatment planning

2. **最小化消融範圍 (minimal lesion set)**
   - 傳統 substrate-based ablation 通常需要大範圍消融
   - Digital twin 引導可精確定位關鍵消融靶點
   - 可能減少消融相關併發症 (ablation-related complications)

3. **縮短手術時間的潛力 (potential to reduce procedure time)**
   - 術前已完成 VT 迴路分析
   - 消融靶點可直接匯入標測系統
   - 減少術中 mapping 與 VT induction 的需求

### 研究限制

- **樣本數極小**：僅 10 位受試者，為 single-center 研究
- **缺乏對照組**：無隨機化 (non-randomized)，無法直接比較傳統 ablation
- **選擇性偏差 (selection bias)**：受試者為經篩選的缺血性 VT 患者
- **單一中心經驗**：Johns Hopkins 為 digital twin 技術開發中心，外推性 (generalizability) 待驗證
- **技術門檻**：需要高品質 cardiac MRI 與專業的計算模擬團隊

---

## 5. 結論

TWIN-VT 研究為首個以 FDA IDE 核准進行的 digital twin–guided VT ablation 前瞻性研究。雖然樣本數僅 10 人，但結果顯示：

- **80% 受試者 (8/10)** 在平均 405.4 天追蹤期間完全無 VT 復發且不需抗心律不整藥物
- **所有受試者均無 ICD shock**
- 2 位術後早期 VT 復發者經 ATP 終止後亦保持 VT-free

此研究為計算心臟學 (computational cardiology) 在臨床電生理的應用提供了重要的概念驗證 (proof of concept)。未來需要更大規模的隨機對照試驗 (randomized controlled trial) 來確認其臨床效益與安全性。

---

## 參考文獻

1. Chrispin J, Prakosa A, Kholmovski E, et al. Digital Twin–Guided Ablation for Ventricular Tachycardia. [*N Engl J Med*. 2026;394(13):1345-1347.](https://doi.org/10.1056/NEJMc2517822)
2. Donahue JK, et al. Mechanism of Ventricular Tachycardia in Chronic Myocardial Infarction Scar. [*Circ Res*. 2024;134:328-342.](https://doi.org/10.1161/CIRCRESAHA.123.323415)
3. Reddy VY, et al. Prophylactic Catheter Ablation for the Prevention of Defibrillator Therapy. [*N Engl J Med*. 2007;357:2657-2665.](https://doi.org/10.1056/NEJMoa065457)
4. Arevalo HJ, et al. Arrhythmia Risk Stratification of Patients after Myocardial Infarction Using Personalized Heart Models. [*Nat Commun*. 2016;7:11437.](https://doi.org/10.1038/ncomms11437)
5. Trayanova NA, et al. Imaging-Based Simulations for Predicting Sudden Cardiac Death and Guiding Ventricular Tachycardia Ablation. [*Circ Arrhythm Electrophysiol*. 2017;10:e004743.](https://doi.org/10.1161/CIRCEP.117.004743)
6. Prakosa A, et al. Personalized Virtual-Heart Technology for Guiding the Ablation of Infarct-Related Ventricular Tachycardia. [*Nat Biomed Eng*. 2018;2:732-740.](https://doi.org/10.1038/s41551-018-0282-9)
