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
  section.lead a { color: #74b9ff; }
  section.lead blockquote, section.lead blockquote * { color: #2d3436; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: #ffffff;
    border-bottom: none;
    font-size: 2.5em;
    text-align: center;
  }
  section.divider h2 { color: #ffe066; }
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
  section.small-text table { font-size: 0.6em; }
footer: '謝慕揚 MD, PhD, FESC | Syncope (NEJM Clinical Practice) | 2026'
---

<!-- _class: lead -->

# Syncope 暈厥的診斷與處置

## NEJM Clinical Practice（Rose Anne Kenny, MD, DSc）

**整理：謝慕揚 MD, PhD, FESC** | 2026-08-08

[原文連結：N Engl J Med 2026;395:582-591](https://doi.org/10.1056/NEJMcp2517255)

> 本簡報為 NEJM 臨床綜論之教學整理（非 RCT），僅供醫療專業人員教學參考。

---

# 臨床案例（Case Vignette）

75 歲獨居退休男性，因**不明原因跌倒 (unexplained fall)** 致顴骨骨折入急診。

- 病史：hypertension、hyperlipidemia、depression（皆治療中）
- 事件：午後遛狗時發生，合併**尿失禁**，**對事件無記憶、無目擊者**
- 過去 6 個月：另 1 次類似跌倒 + 2 次短暫意識喪失 (TLOC)
- 誘因情境：進食後站起、久坐後站起、**夜間排尿**時發作

> **教學提問**：以「跌倒」表現的老年病人，背後可能是暈厥嗎？該如何評估與處置？

---

<!-- _class: divider -->

# 定義與流行病學

---

# 什麼是暈厥？

**暈厥 (syncope)**：因暫時性腦部灌流不足 (transient cerebral hypoperfusion) 所致的短暫意識喪失，伴姿勢張力喪失，之後**快速自發完全恢復**；發作多 **< 1 分鐘**。

| 流行病學 | 數字 |
|----------|------|
| 一生發生暈厥 | 一般人口 1/3–1/2 |
| 女 vs. 男盛行率 | 22% vs. 15% |
| 累積發生率 | 20–29 歲女 ~5% → ≥80 歲 ~50% |
| 復發性暈厥 | 高達 20% |
| 心因性暈厥占比 | 年輕 ≤5%、老年可達 30% |

> **暈厥與跌倒重疊**：老年暈厥常「以不明原因跌倒表現」；跌倒占老年急診 15%，其中 20–30% 為不明原因。

---

# 復發性暈厥：預後較差

相較非復發性暈厥，**復發性暈厥**在 24 個月追蹤：

| 結局 | Hazard Ratio | 95% CI |
|------|--------------|--------|
| 死亡 (death) | **1.87** | 1.26–2.77 |
| 主要不良心血管事件 (MACE) | **2.69** | 2.02–3.59 |

> **好消息**：透過結構化診斷路徑 + 延長心律監測，「不明原因暈厥」比例已由早期 ~37% 降至近期 **< 10%**。

---

<!-- _class: divider -->

# 三大機轉分類

## 反射性 · 姿勢性 · 心因性

---

# 三大機轉一覽

| 類型 | 機轉 | 重點 |
|------|------|------|
| **反射性 (reflex)** | 自主神經失調 → 血管擴張／心跳過緩 | 含 vasovagal、situational、carotid sinus syndrome；年輕人 >90%、老年 ~40% |
| **姿勢性低血壓 (OH)** | 站立血壓代償不足 | <50 歲 <5%、>70 歲 >20%、機構老人 50–68% |
| **心因性 (cardiac)** | 心輸出量／腦灌流下降 | 緩／快脈心律不整、流出道阻塞、肺高壓、PE、主動脈剝離 |

> **複雜性暈厥 (complex syncope)**：老年人高達 1/3 為多重機轉並存，需**多面向評估**。

---

# 反射性暈厥三型

- **血管迷走神經性 (vasovagal)**：最常見；心跳過緩（迷走過度）＋低血壓（交感撤除），常兩者合併
- **情境性 (situational)**：排尿、吞嚥、咳嗽、情緒壓力誘發
- **頸動脈竇症候群 (CSS)**：幾乎只見於老年人；占暈厥 9–17%，占不明原因跌倒**高達 30%**

> **Pearl**：vasovagal 預後多良性，但 **>30% 發作會受傷、~15% 為重大傷害**；高齡、復發、**無前驅症狀 (no prodrome)** 會增加受傷風險。

---

<!-- _class: divider -->

# 診斷閾值（記牢這些數字）

---

# 各類診斷的閾值

| 診斷 | 閾值 |
|------|------|
| Vasovagal（血管抑制型） | SBP ≤ 80、HR < 40、或 asystole ≥ 3 秒 |
| 頸動脈竇過敏 | 按摩時 pause ≥ 3 秒 或 SBP 降 ≥ 50 mm Hg |
| OH（一般） | 站立 SBP 降 ≥ 20 或 DBP 降 ≥ 10 mm Hg |
| Initial OH | 站起 **15 秒內**短暫下降（多良性） |
| Classic OH | 站起 **3 分鐘內**持續 SBP 降 ≥ 20（併supine HTN則 ≥30）／DBP 降 ≥ 10 |
| Postprandial | 餐後 **2 小時內** SBP 降 ≥ 20 mm Hg |

---

<!-- _class: divider -->

# 診斷評估流程

---

# 初始評估：四大支柱（Class I）

```text
Suspected syncope / TLOC
        │
初始評估：病史 + 目擊者描述
        + 平躺與站立血壓 + 身體檢查 + ECG
        │
   ┌────┴─────┐
 病因明確      病因不明
   │             │
 治療        風險評估 → 進一步檢查
```

> 起點永遠是**仔細病史**（含本次、過去發作與目擊者描述，可電話訪談）＋ **supine/standing BP** ＋ **ECG**。

---

# 病史線索：三大機轉鑑別

| 反射性 | 姿勢性 (OH) | 心因性 |
|--------|-------------|--------|
| 長期反覆、<40 歲起 | 站起後不久 | 運動時／平躺時 |
| 不愉快刺激後 | 久站、運動後站立 | 突發心悸後緊接暈厥 |
| 久站、進食中、悶熱處 | 餐後低血壓 | 年輕猝死家族史 |
| 前驅：蒼白/盜汗/噁心 | 與血管擴張藥/利尿劑時序相關 | 肺高壓/結構性/冠脈/心包病 |
| 頭轉或壓頸動脈竇誘發 | 自主神經病變/parkinsonism | ECG 心律不整特徵 |
| 無心臟病 | | |

---

# 紅旗 ECG：提示心律不整性暈厥

- 雙束支阻滯 (bifascicular block)、QRS ≥ 0.12 秒
- Mobitz I 二度 AV block、PR 明顯延長之一度 AV block
- 無藥物下之竇性心搏過緩/慢速 AF（40–50 bpm）
- 非持續性 VT (NSVT)、預激 QRS
- 長／短 QT、早期再極化
- V1–V3 type 1 ST 上升（**Brugada**）
- 右胸負 T、epsilon 波（**ARVC**）
- LVH（**HCM**）

---

<!-- _class: divider -->

# 暈厥的擬似症（Mimics）

---

# 別被誤導：暈厥 vs. 癲癇

最常見擬似症是**癲癇 (epilepsy)**，僅憑病史常難區分。

> **Pearl**：**尿失禁無法區分暈厥與癲癇**（可見於 10–20% 暈厥，尤其老年）；咬舌、抽動、事件後嗜睡也可見於暈厥。

| 擬似症 | 鑑別點 |
|--------|--------|
| 癲癇 | 意識喪失久、有 postictal 期、非快速恢復 |
| 心因性假性暈厥 | 事件中 BP/HR 正常、無真正腦灌流不足 |
| 低血糖 | 血糖低、漸進、非突然倒下 |
| 椎基底 TIA | 局部神經徵象、少見意識喪失 |
| 跌倒發作／猝倒 | 意識保留 |

---

<!-- _class: divider -->

# 風險分層與紅旗徵象

---

# 提高「心因性」機率的紅旗

- 年齡 **> 60 歲**、**男性**
- 有心臟病（缺血/瓣膜/結構性/裝置故障）
- **前驅短暫**、暈厥前**心悸或胸痛**
- **突發**暈厥；**運動時或坐/臥姿**發作
- 暈厥次數少（1–2 次）、心臟檢查異常
- 遺傳性疾病或 **<50 歲早發猝死家族史**、已知先天性心臟病

> **短期預後**（≤30 天）看病因與可逆性；**長期預後**（≤12 月）看治療成效、疾病進展與受傷風險。

---

# 提高「受傷」機率 + 元凶藥物

**受傷風險特徵**：不明原因/反覆跌倒、前驅短暫或缺如、骨質疏鬆、認知障礙、多重用藥 (polypharmacy)。

> **Culprit medications**：diuretic、antianginal、psychotropic、anticholinergic、opioid、anticoagulant、antiplatelet；**近期新開降壓藥／抗心律不整藥**也與暈厥相關。

---

<!-- _class: divider -->

# 進階檢查與監測

---

# 依初始評估選擇進階檢查

| 情境 | 檢查 |
|------|------|
| 疑心律不整 | 立即 ECG 監測 |
| 已知/疑結構性心臟病 | 心臟超音波 (TTE) |
| 每月 1–2 次事件 | 外部監測可能需 4 週 |
| >40 歲疑反射性、頭轉暈厥、不明跌倒 | 頸動脈竇按摩（平躺+直立）|
| 疑反射性暈厥 | 傾斜床測試 (tilt-table) |
| 判斷低血壓/餐後低血壓 | 24 小時動態血壓 (ABPM) |

> **ILR / 植入式監測**：4 廠商（Abbott、Biotronik、Boston Scientific、Medtronic），電池達 4 年，適合不頻繁事件。

---

# 動態血壓與血液檢查

**SynABPM 1 研究**（已確立反射性暈厥病人）：
日間 **≥1 次 SBP < 90 mm Hg** 對反射性暈厥診斷 → **specificity 91%、sensitivity 32%**。

**血液檢查（有指徵才做）**：

| 懷疑 | 檢查 |
|------|------|
| 出血 | Hct / Hgb |
| 低血氧 | SpO₂、血液氣體 |
| 心肌缺血 | Troponin |
| 肺栓塞 | D-dimer / CT |

---

<!-- _class: divider -->

# 處置與治療

## 機轉導向 (mechanism-specific)

---

# 治療的核心原則

治療針對**機轉**（低血壓／心跳過緩／心跳過速），而非單純病因；因常難歸因單一病因，故**針對所有可能病因一起治療**。

**就醫地點決策**：

| 風險 | 處置 |
|------|------|
| 無嚴重病/受傷風險的反射性 | 門診處理 |
| 中度風險、病因不明 | 急診觀察 6–12 小時心律監測（降低住院）|
| **高風險** | 住院 |

> RCT（124 位 >50 歲）：急診觀察 vs. 住院，30 天與 6 個月嚴重結局**相似**，觀察組**費用明顯較低**。

---

# 低血壓與藥物治療

**低血壓（無結構性心臟病）**：增加水分/電解質、避免誘因、**停用元凶藥 (deprescribing)**。

> **降壓藥低血壓風險最低者**：ACE inhibitors（OR 0.85；0.81–0.89）與 CCB（OR 0.81；0.74–0.90）。

**OH 藥物（系統回顧）**：

- **droxidopa、midodrine**：一致減少姿勢性症狀
- **atomoxetine、fludrocortisone**：中度療效
- **fludrocortisone** 預防 vasovagal 復發 RCT：HR 0.69（0.46–1.03；**P=0.07**，未達顯著）

---

# 器械與介入治療

- **心臟節律器 (cardiac pacing)**：症狀性心跳過緩最有效；反射性暈厥＋紀錄到心跳過緩者，**暈厥復發風險降 >50%**。裝置後仍暈厥 → 多因與心跳過緩無關的低血壓。
- **心臟神經節燒灼 (cardioneural ablation)**：燒灼epicardial ganglionated plexuses 降迷走活性；緩脈型反射性暈厥有前景；多項 RCT 進行中。
- **心室性心律不整**：矯正可逆病因、抗心律不整藥、導管燒灼、**ICD**、緊急去顫。

---

<!-- _class: divider -->

# 指引比較與案例結論

---

# ESC 2018 vs. ACC–AHA–HRS 2017

| 面向 | ESC 2018 | ACC–AHA–HRS 2017 |
|------|----------|-------------------|
| 專責暈厥單位 | **強烈建議** | 未強調 |
| ILR 早期使用 | 對不明暈厥/跌倒**更早** | 相對保守 |
| 病人衛教/行為改變 | **強調更多** | 相對較少 |

> 本篇綜論作者立場**較貼近 ESC 指引**。

---

# 案例結論（作者建議）

75 歲男性 → 判定**中至高風險**：急診觀察單位監測，做 ECG、心臟超音波、姿勢性血壓。

- 若無心律不整/結構性心臟病，但站立降至 **80/55 mm Hg** 伴頭暈 → 做**頸動脈竇按摩**
- 直立位按摩出現 **pause ≥ 3 秒並意識喪失** → 確立 **CSS**
- 考量年齡與外傷 → 直接植入**雙腔節律器 (dual-chamber pacemaker)**，並**調整元凶藥（降壓藥、抗憂鬱藥）** 處理 OH

> 與最新美國與歐洲暈厥指引一致。

---

# 臨床重點總結（Key Points）

> - 暈厥＝暫時性腦灌流不足；分**反射性、姿勢性、心因性**。
> - **病史 + 身體檢查 + ECG + 姿勢性血壓** → 多數可找出病因。
> - **風險分層**決定住院與檢查。
> - 治療**機轉導向**，降低復發與受傷。
> - 老年暈厥常「以跌倒表現」，>1/4 為**複雜性暈厥**。
> - 尿失禁、咬舌、抽動**無法**可靠區分暈厥與癲癇。

---

<!-- _class: small-text -->

# 縮寫對照表

| 縮寫 | 全名 | 縮寫 | 全名 |
|------|------|------|------|
| TLOC | Transient Loss of Consciousness | OH | Orthostatic Hypotension |
| CSS | Carotid Sinus Syndrome | ABPM | Ambulatory BP Monitoring |
| ILR | Implantable Loop Recorder | TTE | Transthoracic Echocardiography |
| ICD | Implantable Cardioverter–Defibrillator | PE | Pulmonary Embolism |
| MACE | Major Adverse Cardiovascular Events | NSVT | Nonsustained Ventricular Tachycardia |
| ARVC | Arrhythmogenic RV Cardiomyopathy | HCM | Hypertrophic Cardiomyopathy |
| SCD | Sudden Cardiac Death | TIA | Transient Ischemic Attack |
| HR / OR | Hazard Ratio / Odds Ratio | CI | Confidence Interval |

---

<!-- _class: small-text -->

# 參考文獻（節選）

1. Kenny RA. Syncope. [*N Engl J Med*. 2026;395(6):582-591.](https://doi.org/10.1056/NEJMcp2517255)
2. Brignole M, et al. 2018 ESC guidelines for diagnosis and management of syncope. [*Eur Heart J*. 2018;39(21):1883-1948.](https://doi.org/10.1093/eurheartj/ehy037)
3. Shen WK, Sheldon RS, et al. 2017 ACC/AHA/HRS syncope guideline. [*Heart Rhythm*. 2017;14(8):e155-e217.](https://doi.org/10.1016/j.hrthm.2017.03.004)
4. Zimmermann T, et al. Recurrent syncope: incidence & prognosis. [*Europace*. 2020;22(12):1885-1895.](https://doi.org/10.1093/europace/euaa227)
5. Rivasi G, et al. SynABPM 1 study. [*Eur Heart J*. 2022;43(39):3765-3776.](https://doi.org/10.1093/eurheartj/ehac347)
6. Sheldon R, et al. Fludrocortisone for prevention of vasovagal syncope (POST 2). [*J Am Coll Cardiol*. 2016;68(1):1-9.](https://doi.org/10.1016/j.jacc.2016.04.030)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

[原文：Kenny RA. Syncope. N Engl J Med 2026;395:582-591](https://doi.org/10.1056/NEJMcp2517255)
