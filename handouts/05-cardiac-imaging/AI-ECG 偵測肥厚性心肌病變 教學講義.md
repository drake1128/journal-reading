# Artificial Intelligence for the Detection of Hypertrophic Cardiomyopathy From Standard Electrocardiogram / 以人工智慧從標準心電圖偵測肥厚性心肌病變

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-06-20**
**原文連結：[JACC Advances — Artificial Intelligence for the Detection of Hypertrophic Cardiomyopathy From Standard Electrocardiogram](https://doi.org/10.1016/j.jacadv.2026.102914)**

---

## 目錄

- [1. 一句話總結 (Bottom Line)](#1-一句話總結-bottom-line)
- [2. 研究背景與臨床問題](#2-研究背景與臨床問題)
- [3. 研究方法 (Methods)](#3-研究方法-methods)
- [4. 主要結果 (Results)](#4-主要結果-results)
- [5. 誰會被偵測到？正確偵測的預測因子](#5-誰會被偵測到正確偵測的預測因子)
- [6. 時間軸分析：能提早多久診斷？](#6-時間軸分析能提早多久診斷)
- [7. 討論：高特異度的設計哲學](#7-討論高特異度的設計哲學)
- [8. 研究限制 (Limitations)](#8-研究限制-limitations)
- [9. 臨床啟示與我的觀點](#9-臨床啟示與我的觀點)
- [10. 縮寫對照表](#10-縮寫對照表)
- [參考文獻](#參考文獻)

---

## 1. 一句話總結 (Bottom Line)

> **核心訊息**：一套 FDA 核准的 AI 心電圖演算法 (Viz HCM, Viz.ai) 在以**心臟磁振造影 (cMRI) 為金標準**驗證的世代中，偵測肥厚性心肌病變 (HCM) 的 **特異度 (specificity) 達 100%、陽性預測值 (PPV) 達 100%、AUC 0.946**，但**敏感度 (sensitivity) 僅 58%**——這是「刻意設計」的取捨：在低盛行率的篩檢情境中，寧可當高度可信的「rule-in」工具，也不要製造大量偽陽性。

- 這是一套「**有就幾乎一定是**、**沒有不代表沒有**」的工具。
- **頂尖價值**：在 28 位有 cMRI 前 ≥1 年心電圖的病人中，AI 比臨床診斷**中位數提早 2.6 年**抓到 HCM。
- **最會被抓到的亞型**：心尖肥厚型 (apical HCM)，校正後勝算比 (adjusted OR) **4.71**。

---

## 2. 研究背景與臨床問題

### HCM 的「診斷落差」

- HCM 是最常見的遺傳性心肌病變，社區盛行率約 **0.2% (1/500)**，甚至高達 1.4%；全球疾病負擔估計達 **2,000 萬人**。
- 儘管盛行率高，HCM 仍**長期被低估診斷 (underdiagnosed)**：症狀非特異或無症狀，美國估計**未診斷者高達 85%**，診斷延遲可達 2 年。
- HCM 病人相較一般族群有更高的**病死率與經濟負擔**；早期診斷可及早啟動標靶治療 (cardiac myosin inhibitor) 與猝死預防。

### 既有 AI-ECG 研究的最大弱點

- 過去的 HCM AI-ECG 模型多以 **ICD 診斷碼**或**心臟超音波 (echo)** 作為「ground truth」。
- 但 ICD 碼在 HCM 的**錯誤分類率高達 1/3**，PPV 可能低到 **68%**，常混入高血壓性心臟病與主動脈瓣狹窄。
- **本研究的關鍵創新**：以 **cMRI + 醫師逐案判讀**作為金標準，克服上述限制。

---

## 3. 研究方法 (Methods)

### 研究設計

- **單中心、回溯性** — Cedars-Sinai Medical Center，2010–2023。
- 以 ICD-10 碼 **42.1 / 42.2** 篩出 314 位接受 cMRI 評估疑似 HCM 的成人。

### 病人納入流程 (Figure 1)

```text
ICD 42.1/42.2 + 6 個月內有 EKG + TTE
N = 314
   │  排除 102 人（其他心肌肥厚 40、其他/非缺血性心肌病 17、
   │               無心肌病 16、疑似類澱粉/類肉瘤/Fabry、缺血性等）
   ▼
cMRI + 醫師判讀確診 HCM   N = 212
   │  排除：無 EKG (21)、EKG 格式無法分析 (37)
   ▼
EKG 配對成功   N = 154
   │  排除：節律器 EKG 無法分析 (4)
   ▼
最終分析 EKG   N = 150 HCM
```

- **HCM 確診定義**：最大室壁厚度 (MWT) ≥15 mm（或合併家族史/基因診斷時 ≥13 mm）。
- **對照組**：83 位 cMRI 確認**無任何心肌病變**者（20 位 2010–2023 年齡配對 + 55 位 2025 補充 + 8 位有 HCM 懷疑/家族史但 cMRI 陰性）。

### AI 演算法：Viz HCM (Viz.ai)

| 項目 | 內容 |
|------|------|
| 法規狀態 | **FDA 核准** (DEN230003) |
| 訓練資料 | 831,329 筆 ECG / 301,106 位病人（4,470 陽性、298,394 陰性） |
| 訓練/驗證 | 80% / 20% 切分 |
| 架構 | 影像式 ECG → tensor → **卷積神經網路 (CNN)** → 機率分數 0–1 |
| **操作閾值 (operating threshold)** | **0.84**（≥0.84 判為 HCM-positive），刻意調高以追求高特異度 |

- 以**最接近 cMRI 日期**的 ECG 與金標準比對；同日多張 ECG 取機率中位數。
- 統計：Mann-Whitney U、卡方/Fisher、單變項與多變項邏輯斯迴歸（含 age, sex, race, MWT, 肥厚亞型）；AUC 之 CI 以 2,000 次 bootstrap 計算。

---

## 4. 主要結果 (Results)

### 整體診斷效能

> **AUC 0.946 (95% CI 0.916–0.970)** — 鑑別力極佳

| 指標 | 數值 (95% CI) | 解讀 |
|------|---------------|------|
| 敏感度 Sensitivity | **58%** (50.0–65.6%) | 150 位 HCM 中正確抓到 87 位 |
| 特異度 Specificity | **100%** (95.6–100%) | 83 位對照**全數正確判為陰性** |
| 陽性預測值 PPV | **100%** (95.8–100%) | **零偽陽性 (no false positive flags)** |
| 陰性預測值 NPV | 57% | 「陰性」無法排除 HCM |

### 兩組基本特徵 (Table 1，HCM vs 對照)

| 變項 | HCM (n=150) | 對照 (n=83) | P |
|------|-------------|-------------|---|
| 年齡（中位數） | 63 | 49 | <0.001 |
| 男性 | 64% | 59% | 0.268 |
| LVEF (cMRI, %) | 67 | 56 | <0.001 |
| 最大室壁厚度 MWT (mm) | **18.0** | 10.0 | <0.001 |
| 有 LGE | **77%** | 0% | — |
| HCM 致病基因突變 | 49% | 1% | <0.001 |
| 高血壓 | 80% | 39% | <0.001 |
| β-blocker 使用 | 71% | 34% | <0.001 |
| Cardiac myosin inhibitor | 11% | 0% | 0.001 |
| LVOT gradient >30 mmHg | 23% (21/93) | 0% | <0.001 |

- HCM 組年紀較大、室壁明顯較厚、近八成有 LGE——符合臨床預期的「表型較進展」族群。

---

## 5. 誰會被偵測到？正確偵測的預測因子

### True Positive vs False Negative (Table 2)

比較被「正確抓到 (TP, n=87)」與「漏掉 (FN, n=63)」的 HCM 病人：

| 變項 | True Positive | False Negative | P |
|------|---------------|----------------|---|
| 年齡（中位數） | 60 | 66 | 0.030 |
| 男性 | **72%** | 52% | 0.012 |
| 肥厚型態 | — | — | **0.007** |
| ├ 中膈為主 (septal) | 68% | **87%** | |
| ├ 心尖為主 (apical) | **28%** | 8% | |
| └ 同心圓 (concentric) | 3% | 5% | |
| MWT (mm) | 19.0 | 18.0 | 0.061 (NS) |
| 有 LGE | 80% | 73% | 0.300 (NS) |
| 高臨床風險 | 23% | 24% | 0.908 (NS) |

> **重要的「陰性發現」**：MWT、LGE 量、猝死高風險特徵在 TP 與 FN 之間**沒有顯著差異**。也就是說，**表型嚴重度（影像上的疾病負擔）不必然轉化為心電圖上可偵測的訊號**——HCM 的電氣表現是質量、幾何、纖維排列與纖維化複雜交互作用的結果。

### 邏輯斯迴歸 (Table 3)

| 預測因子 | 單變項 OR (P) | 多變項 OR (P) |
|----------|----------------|----------------|
| 男性 | 2.39 (0.012) | 1.80 (0.127) |
| MRI 最大室壁厚度 | 1.10 (0.033) | 1.09 (0.069) |
| **心尖亞型 (apical)** | **4.48 (0.004)** | **4.71 (0.005)** ✅ |

> **唯一在多變項模型中仍顯著的預測因子是「心尖肥厚型」(adjusted OR 4.71; 95% CI 1.71–15.48)。** 機轉：心尖 HCM (Yamaguchi syndrome) 常伴隨顯著的心電圖變化（巨大倒 T 波 / giant T-wave inversion），這正是 AI 最容易學到的特徵。

---

## 6. 時間軸分析：能提早多久診斷？

### 跨年度一致性 (Figure 3A)

- 233 位中 132 位有多張 ECG（550 張 HCM ECG + 154 張對照 ECG）。
- AI 機率分數在 cMRI 前後多年**維持穩定分層**：對照最低、偽陰性居中、真陽性最高（two-way ANOVA, F(2,280)=314, P<0.001）。

### Lead-time（提早診斷的時間）(Figure 3B)

```text
57 位 HCM 在 cMRI 前就有 AI-positive ECG
        │
        ▼
28 位在 cMRI 前 ≥1 年就有陽性 ECG
   （20 真陽性 + 8 偽陰性，以最接近 cMRI 的 ECG 計）
        │
        ▼
其中 9 位 (32%) 在「最早一次陽性旗標」時尚未被臨床診斷 HCM
   └ 其中 4 位在 cMRI 時已具高猝死風險特徵
        │
        ▼
中位 lead-time = 2.6 年 (IQR 1.1–5.3)
```

> **臨床含義**：AI-ECG 有潛力在臨床診斷前**數年**就標記出未被察覺的 HCM，爭取及早確診、HCM 專屬治療與猝死預防的時間窗。

---

## 7. 討論：高特異度的設計哲學

### 為什麼敏感度只有 58%？這是缺點還是特色？

- 近期統合分析 (Queiroz et al) 顯示 CNN-ECG 偵測 HCM 的整合敏感度/特異度約 **89% / 88%**。
- 本研究敏感度較低，是因為**刻意把操作點 (operating point) 調高 (0.84)** 以追求**極高特異度**。
- **為何在低盛行率疾病要這樣設計？**
  - HCM 社區盛行率僅 0.2–1.4%。即使偽陽性率很低，在大規模篩檢時**少量偽陽性也會壓垮臨床量能**，造成不必要的 cMRI、會診與成本，降低成本效益。
  - 作者主張：對一般族群（門診 all-comers），**可靠的「rule-in」比高敏感度的「rule-out」更實用**。
  - 對照之下，Swain et al 顯示猝死存活者中 96% 有高 HCM 機率（高敏感度取向）——但這群高風險病人本來就會做完整檢查，高敏感度的邊際價值有限。

### 為何 cMRI 金標準是關鍵強項

- ICD 碼/echo 為基礎的研究：HCM 錯誤分類率達 1/3、PPV 低至 68%，常混入高血壓性心臟病與主動脈瓣狹窄。
- 本研究的初篩排除率即達 39%（102 人中 40 人是非 HCM 的肥厚原因），凸顯純靠 ICD 碼的雜訊。
- cMRI 具高空間解析度、血液-組織對比、組織特性化能力——是當代 HCM 診斷金標準。

---

## 8. 研究限制 (Limitations)

- **單中心、回溯性、對照組樣本數小 (n=83)**，外推性受限。
- **對照組「太乾淨」**：皆為 cMRI 確認無心肌病者，未挑戰演算法去區分 HCM 的「表型相似疾病 (phenocopies)」（如高血壓性心臟病、基因型陽性但表型陰性者）→ **真實世界特異度可能較低**。
- **選擇偏差**：以 ICD 碼選入並做 cMRI 的族群，可能比一般 all-comers 表型更進展。
- **刻意優化高特異度**→ 漏掉部分 HCM（敏感度 58%）。
- 無法做特徵層級分析（如 GradCAM）解釋模型決策。

---

## 9. 臨床啟示與我的觀點

> **MEDICAL KNOWLEDGE（原文 Perspective）**：AI-ECG 演算法能以高特異度偵測 HCM，具大規模篩檢、減少不必要下游檢查的潛力。

> **TRANSLATIONAL OUTLOOK**：未來應整合縱貫性臨床資料、跨表型精進演算法，並以前瞻性研究驗證 AI 導引篩檢是否真能帶來「更早診斷、更好預後」。

### 給結構性心臟病/影像團隊的實務重點

1. **這是 rule-in 工具，不是 rule-out**：AI 標記「疑似 HCM」→ 轉介 cMRI/專家評估的訊號很強（零偽陽性）；但 AI「陰性」**不能**用來排除 HCM（NPV 僅 57%）。
2. **心尖型 HCM 最容易被 AI 抓到**（OR 4.71）；反過來說，**中膈型、女性、影像表型嚴重但 ECG 變化不明顯者較易被漏掉**——這類病人仍需仰賴臨床警覺與影像。
3. **Lead-time 2.6 年**是最吸引人的賣點：若整合進 EHR / 心電圖室自動判讀流程，可作為被動式的早期警報系統。
4. **落地前提醒**：本研究對照組過於理想化，真實門診中混雜高血壓性心臟病等 phenocopy 時，特異度恐不如 100%——導入時應搭配臨床情境與後續影像確認，而非單以 ECG 下診斷。

---

## 10. 縮寫對照表

| 縮寫 | 全名 | 中文 |
|------|------|------|
| HCM | Hypertrophic Cardiomyopathy | 肥厚性心肌病變 |
| AI | Artificial Intelligence | 人工智慧 |
| ECG / EKG | Electrocardiogram | 心電圖 |
| cMRI | Cardiac Magnetic Resonance Imaging | 心臟磁振造影 |
| CNN | Convolutional Neural Network | 卷積神經網路 |
| AUC | Area Under the Curve | 曲線下面積 |
| MWT | Maximal Wall Thickness | 最大室壁厚度 |
| LGE | Late Gadolinium Enhancement | 延遲釓顯影 |
| LVEF | Left Ventricular Ejection Fraction | 左心室射出分率 |
| LVOT | Left Ventricular Outflow Tract | 左心室出口 |
| PPV / NPV | Positive / Negative Predictive Value | 陽性／陰性預測值 |
| OR | Odds Ratio | 勝算比 |
| TTE | Transthoracic Echocardiography | 經胸心臟超音波 |
| ICD | International Classification of Diseases | 國際疾病分類碼 |

---

## 參考文獻

1. Park J, Kermanshahchi J, Love CJ, Reyes KR, Kukuev A, Meshesha S, Kon K, Rader F. Artificial Intelligence for the Detection of Hypertrophic Cardiomyopathy From Standard Electrocardiogram. [*JACC Adv*. 2026;5(7):102914.](https://doi.org/10.1016/j.jacadv.2026.102914)

2. Massera D, McClelland RL, Ambale-Venkatesh B, et al. Prevalence of unexplained left ventricular hypertrophy by cardiac magnetic resonance imaging in MESA. [*J Am Heart Assoc*. 2019;8(8):e012250.](https://doi.org/10.1161/JAHA.119.012250)

3. Maron BJ, Desai MY, Nishimura RA, et al. Diagnosis and evaluation of hypertrophic cardiomyopathy: JACC state-of-the-art review. [*J Am Coll Cardiol*. 2022;79(4):372-389.](https://doi.org/10.1016/j.jacc.2021.12.002)

4. Naidu SS, Sutton MB, Gao W, et al. Frequency and clinicoeconomic impact of delays to definitive diagnosis of obstructive hypertrophic cardiomyopathy in the United States. [*J Med Econ*. 2023;26(1):682-690.](https://doi.org/10.1080/13696998.2023.2208966)

5. Maron MS, Hellawell JL, Lucove JC, et al. Occurrence of clinically diagnosed hypertrophic cardiomyopathy in the United States. [*Am J Cardiol*. 2016;117(10):1651-1654.](https://doi.org/10.1016/j.amjcard.2016.02.044)

6. Aro AL, Nair SG, Reinier K, et al. Population burden of sudden death associated with hypertrophic cardiomyopathy. [*Circulation*. 2017;136(17):1665-1667.](https://doi.org/10.1161/CIRCULATIONAHA.117.030616)

7. Ko WY, Siontis KC, Attia ZI, et al. Detection of hypertrophic cardiomyopathy using a convolutional neural network-enabled electrocardiogram. [*J Am Coll Cardiol*. 2020;75(7):722-733.](https://doi.org/10.1016/j.jacc.2019.12.030)

8. Hillis JM, Bizzo BC, Mercaldo SF, et al. Detection of hypertrophic cardiomyopathy on electrocardiogram using artificial intelligence. [*Circ Heart Fail*. 2025.](https://doi.org/10.1161/CIRCHEARTFAILURE.124.012667)

9. Lampert J, Bhatt DL, Vaid A, et al. 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR guideline for the management of hypertrophic cardiomyopathy. [*J Am Coll Cardiol*. 2024;83(23):2324-2405.](https://doi.org/10.1016/j.jacc.2024.02.014)

10. Lampert J, Vaid A, Whang W, et al. A novel ECG-based deep learning algorithm to predict cardiomyopathy in patients with premature ventricular complexes. [*JACC Clin Electrophysiol*. 2023;9(8):1437-1451.](https://doi.org/10.1016/j.jacep.2023.05.025)

11. Desai MY, Jadam S, Abusafia M, et al. Real-World artificial intelligence-based electrocardiographic analysis to diagnose hypertrophic cardiomyopathy. [*JACC Clin Electrophysiol*. 2025;11(6):1324-1333.](https://doi.org/10.1016/j.jacep.2025.02.024)

12. Queiroz I, Defante MLR, Barbosa LM, et al. A systematic review and meta-analysis on the performance of convolutional neural networks ECGs in the diagnosis of hypertrophic cardiomyopathy. [*J Electrocardiol*. 2025;89:153888.](https://doi.org/10.1016/j.jelectrocard.2025.153888)

13. Swain SM, Giudicessi JR, Geske J, et al. Artificial intelligence electrocardiography predicts undiagnosed hypertrophic cardiomyopathy in post-HOC analysis of cardiac arrest survivors. [*Heart Rhythm O2*. 2025.](https://doi.org/10.1016/j.hroo.2025.07.094)

14. Hughes MK, Thornton GD, Manisty CH, et al. Accurate diagnosis of apical hypertrophic cardiomyopathy using explainable advanced electrocardiogram analysis. [*EP Europace*. 2024;26(4):93.](https://doi.org/10.1093/europace/euae093)

15. Lewontin M, Kaplan E, Bilchick KC, et al. Advanced diagnosis of hypertrophic cardiomyopathy with AI-ECG and differences based on ethnicity and HCM subtype. [*J Clin Med*. 2025;14(13):4718.](https://doi.org/10.3390/jcm14134718)

16. Love CJ, Lampert J, Huneycutt D, et al. Clinical implementation of an AI-enabled ECG for hypertrophic cardiomyopathy detection. [*Heart*. 2025.](https://doi.org/10.1136/heartjnl-2024-325608)

17. Armoundas AA, Narayan SM, Arnett DK, et al. Use of artificial intelligence in improving outcomes in heart disease: a scientific statement from the American Heart Association. [*Circulation*. 2024;149(14):e1028-e1050.](https://doi.org/10.1161/CIR.0000000000001201)
