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
  section.ref { font-size: 0.62em; }
footer: '謝慕揚 MD, PhD, FESC | Critical Care Bi-Weekly Review | 2026'
---

<!-- _class: lead -->

# 重症醫學雙週文獻回顧
## Critical Care Bi-Weekly Review
**2026-03-22 至 2026-04-05**
**謝慕揚 MD, PhD, FESC**
Journals: *CCM, Critical Care, ICM, Resuscitation, Chest*

---

# 大綱 Outline

1. **敗血症指引與定義** — SSC 2026 Guidelines, Refractory Septic Shock, Biomarkers
2. **ARDS 與呼吸治療** — ARDS Resolution Definition, HFNC vs Helmet CPAP, Ventilation Updates
3. **ICU 感染** — tNGS for Pneumonia, Inhaled Antibiotics, IAPA
4. **ECMO 與血行動力學** — VA-ECMO Complications, Cardiogenic Shock
5. **心肺復甦與心臟停止** — Bystander CPR, AI Prognostication
6. **AKI、CRRT 與其他重要文獻** — CRRT Dosing, Albumin, Muscle Ultrasound

---

<!-- _class: divider -->

# 敗血症指引與定義

---

# SSC 2026 Guidelines — Adult
## [Prescott HC et al., *CCM* + *ICM* 2026](https://doi.org/10.1097/CCM.0000000000007075)

- **近年最重要的 ICU 指引更新** — SCCM / ESICM 聯合制定
- 同步發表於 *Critical Care Medicine* 與 *Intensive Care Medicine*
- 全面更新 Surviving Sepsis Campaign 建議

| 類別 | 項目數 |
|------|--------|
| Strong recommendations | 多項升級 |
| Conditional recommendations | 涵蓋 fluid, vasopressor, corticosteroid |
| New topics | AI-assisted screening, point-of-care ultrasound |

> **Clinical Pearl**: 本版強調個人化治療 (personalized medicine) 與 de-escalation 策略

---

# SSC 2026 Guidelines — Pediatric
## [Weiss SL et al., *ICM* 2026](https://doi.org/10.1007/s00134-026-08360-2)

- **68 位專家、13 個國際組織** 聯合制定
- 涵蓋新生兒至青少年族群

| 建議類型 | 數量 |
|---------|------|
| Strong recommendations | 5 |
| Conditional recommendations | 24 |
| Good practice statements | 10 |
| Carried forward (2020) | 22 |
| **New recommendations** | **20** |

> **Clinical Pearl**: 新增 20 條建議，反映 pediatric sepsis 近 5 年的研究突破

---

# Refractory Septic Shock — 首次臨床定義
## [Leone M et al., *CCM* 2026](https://doi.org/10.1097/CCM.0000000000007124)

- **SCCM / ESICM Joint Delphi Consensus**
- 首次為 refractory septic shock 建立**臨床診斷標準**
- 目的：統一研究定義、改善臨床試驗 enrollment

### 核心概念
- 持續性血行動力學不穩定 (hemodynamic instability) despite adequate resuscitation
- 需要高劑量 vasopressor 支持
- 合併持續性 organ dysfunction

> **Clinical Pearl**: 此定義將成為未來 rescue therapies 臨床試驗的入選標準基礎

---

<!-- _class: small-text -->

# Sepsis: Biomarkers & Outcomes
## 生物標記與預後相關研究

| 主題 | 作者 | 期刊 | 重點發現 |
|------|------|------|---------|
| NLR 替代 mHLA-DR | [Lafon T et al.](https://doi.org/10.1007/s00134-026-07429-6) | ICM | Neutrophil-to-lymphocyte ratio 可作為 mHLA-DR 的簡易替代指標 |
| DPP3 & Angiotensin II | [van Lier D et al.](https://doi.org/10.1186/s13054-026-05412-3) | Crit Care | DPP3 降解 Angiotensin II，與 sepsis 嚴重度相關 |
| Proenkephalin A & AKI | [Arlt B et al.](https://doi.org/10.1186/s13054-026-05398-7) | Crit Care | Proenkephalin A 可早期預測 sepsis-associated AKI |
| Vitamin D & Sepsis | [Han Y et al.](https://doi.org/10.1186/s13054-026-05405-2) | Crit Care | Vitamin D deficiency 與 sepsis mortality 獨立相關 |
| Sepsis & Psychiatric Morbidity | [Wetterberg H et al.](https://doi.org/10.1097/CCM.0000000000007089) | CCM | Sepsis 存活者精神疾病風險顯著增加 |

---

<!-- _class: divider -->

# ARDS 與呼吸治療

---

# ARDS Resolution — 首次共識定義
## [Weir TE, Fan E, Goligher EC; *CCM* 2026](https://doi.org/10.1097/CCM.0000000000007107)

- **Modified Delphi method**, 3 rounds of consensus
- 首次定義 **ARDS resolution** 的臨床標準
- 解決長期以來研究中缺乏統一 endpoint 的問題

### 定義核心要素
- 氧合改善 (oxygenation improvement)
- 影像學改善 (radiographic resolution)
- 脫離呼吸器支持 (liberation from mechanical ventilation)

> **Clinical Pearl**: 統一 ARDS resolution 定義將改善臨床試驗設計，使不同研究結果可互相比較

---

# HFNC vs Helmet CPAP in AHRF
## [Coppola S et al., *CCM* 2026](https://doi.org/10.1097/CCM.0000000000007116)

- **Crossover study**, n = 33, acute hypoxemic respiratory failure
- 比較 HFNC 與 Helmet CPAP 的生理效應

### 主要發現

| 參數 | HFNC | Helmet CPAP 10 cmH2O |
|------|------|----------------------|
| Minute ventilation 降低 | Yes | Yes |
| ΔPes 降低 | Yes | Yes |
| Oxygenation 改善 | Moderate | **Best** |
| Patient comfort | High | Moderate |

> **Clinical Pearl**: Helmet CPAP 10 cmH2O 提供最佳氧合效果；兩者皆可降低呼吸功 (work of breathing)

---

<!-- _class: small-text -->

# Ventilation Updates
## 呼吸器相關新知

**RELAx Bayesian Re-analysis — Lower vs Higher PEEP in Non-ARDS**
- [Caroli A et al., *CCM* 2026](https://doi.org/10.1097/CCM.0000000000007098)
- Bayesian 分析再次確認：非 ARDS 患者使用 lower PEEP 策略不劣於 higher PEEP
- 支持 individualized PEEP 而非一律高 PEEP

**Sex-specific Tidal Volume Differences**
- [Urner M et al., *CCM* 2026](https://doi.org/10.1097/CCM.0000000000007102)
- 女性患者更常接受 excessive Vt (mL/kg PBW)
- 臨床需注意以 predicted body weight 計算 Vt

**"Respiratory Envelope" Framework**
- [Meuwese CL et al., *Crit Care* 2026](https://doi.org/10.1186/s13054-026-05415-0)
- 提出整合呼吸力學的新概念框架
- 結合 driving pressure, compliance, PEEP 的綜合評估

---

# ARDS Complications & Trends
## ARDS 併發症與流行病學趨勢

**ARDS Complications — Systematic Review**
- [Granton D et al., *Crit Care* 2026](https://doi.org/10.1186/s13054-026-05408-z)
- 系統性回顧 ARDS 住院期間與出院後併發症
- 強調 neuromuscular weakness, cognitive impairment, PTSD

**ARDS 20-Year NIS Trends (2000-2020)**
- [Padappayil P et al., *Chest* 2026](https://doi.org/10.1016/j.chest.2026.01.032)
- 美國全國住院樣本 (NIS) 20 年趨勢分析
- In-hospital mortality 逐步下降，但 resource utilization 仍高
- COVID-19 期間 ARDS 發生率顯著上升

> **Clinical Pearl**: ARDS 存活者的長期功能障礙需要系統性追蹤計畫

---

<!-- _class: small-text -->

# ICU 感染
## Infection & Antimicrobial Updates

| 主題 | 作者 | 期刊 | 重點 |
|------|------|------|------|
| **tNGS for ICU Pneumonia (Taiwan)** | [Tseng HY et al.](https://doi.org/10.1186/s13054-026-05420-3) | Crit Care | RPIP targeted NGS vs standard culture；台灣多中心研究，提升病原體辨識率 |
| Amikacin Nebulization PK | [Gregoire N et al.](https://doi.org/10.1186/s13054-026-05395-0) | Crit Care | 霧化 amikacin 的肺部藥物動力學分析 |
| Inhaled Antibiotics for VAP | [Kalil AC et al.](https://doi.org/10.1097/CCM.0000000000007110) | CCM | Editorial：吸入性抗生素治療 VAP 的角色與限制 |
| IAPA Review | [Sedik S et al.](https://doi.org/10.1186/s13054-026-05388-z) | Crit Care | Influenza-associated pulmonary aspergillosis 完整回顧 |

> **Clinical Pearl**: tNGS (targeted next-generation sequencing) 顯著縮短 ICU 肺炎病原體鑑定時間，台灣研究值得關注

---

<!-- _class: divider -->

# ECMO 與血行動力學

---

# VA-ECMO — Bleeding & Complications
## VA-ECMO 出血與併發症

**VA-ECMO Bleeding Correlates**
- [Pladet et al., *Crit Care* 2026](https://doi.org/10.1186/s13054-026-05392-1)
- 系統性分析 VA-ECMO 出血相關因子
- Anticoagulation management 仍為核心挑戰

**ECMO Complications — Standardized Definition**
- [Brown et al., *ICM* 2026](https://doi.org/10.1007/s00134-026-07445-6)
- 首次建立 ECMO 併發症的標準化定義
- 目標：改善跨中心資料比較與研究品質

**Cerebral Hypercapnia on VA-ECMO**
- [Koszutski et al., *ICM* 2026](https://doi.org/10.1007/s00134-026-07438-5)
- VA-ECMO 期間腦部 hypercapnia 的機轉與臨床意義
- 影響神經預後 (neurological outcome)

---

# STORM-ECMO & Cardiogenic Shock
## VT Ablation、Cardiogenic Shock 相關研究

**VT Ablation Timing on VA-ECMO**
- [Saura O et al., *Crit Care* 2026](https://doi.org/10.1186/s13054-026-05401-6)
- VA-ECMO 支持下 VT ablation 的最佳時機探討
- Early ablation 可能改善預後

**Landiolol in Cardiogenic Shock**
- [Tavecchia et al., *Chest* 2026](https://doi.org/10.1016/j.chest.2026.02.015)
- Ultra-short-acting beta-blocker landiolol 用於 cardiogenic shock 合併 tachyarrhythmia
- 小劑量起始，可改善血行動力學

**Frailty & Cardiogenic Shock Mortality**
- [Ling RR et al., *Crit Care* 2026](https://doi.org/10.1186/s13054-026-05410-5)
- Frailty 是 cardiogenic shock 死亡的獨立預測因子
- 臨床決策需納入 frailty assessment

---

<!-- _class: divider -->

# 心肺復甦與心臟停止

---

# Resuscitation 重點
## Bystander CPR & Pediatric Cardiac Arrest

**Bystander CPR in Drowning — 傳統 CPR 效果顯著優於 Hands-only**
- [Abe Y et al., *Resuscitation* 2026](https://doi.org/10.1016/j.resuscitation.2026.110598)
- Conventional CPR (含 rescue breathing): **AOR 11.53**
- Hands-only CPR: AOR 3.63
- 溺水患者需要 rescue breathing，hands-only 不足

**OHCA in Children — Meta-analysis**
- [Mellett-Smith et al., *CCM* 2026](https://doi.org/10.1097/CCM.0000000000007095)
- 兒童 out-of-hospital cardiac arrest 存活率仍偏低
- Bystander CPR 與 shockable rhythm 為最強預後因子

**Diastolic BP During Pediatric IHCA**
- [Loaec et al., *CCM* 2026](https://doi.org/10.1097/CCM.0000000000007088)
- CPR 期間 diastolic BP > 25 mmHg 與 ROSC 相關

---

<!-- _class: small-text -->

# Cardiac Arrest: AI & Biomarkers
## AI 預後預測與生物標記

| 主題 | 作者 | 期刊 | 重點發現 |
|------|------|------|---------|
| EEG Machine Learning Prognostication | [Xhepa S et al.](https://doi.org/10.1186/s13054-026-05418-x) | Crit Care | ML 分析 EEG 可提升心臟停止後神經預後預測準確度 |
| Plasma Proteomics | [Wang N et al.](https://doi.org/10.1016/j.resuscitation.2026.110602) | Resuscitation | 血漿蛋白質體學發現新 prognostic biomarkers |
| ML for Recurrent CA Prediction | [Thuccani M et al.](https://doi.org/10.1016/j.resuscitation.2026.110595) | Resuscitation | 機器學習預測 recurrent cardiac arrest 風險 |
| AED Pricing Analysis | [Fijacko N et al.](https://doi.org/10.1016/j.resuscitation.2026.110590) | Resuscitation | AED 價格分析：呼籲降低公共取得門檻 |

> **Clinical Pearl**: AI/ML 在心臟停止後預後預測的應用快速發展，但仍需前瞻性驗證

---

<!-- _class: divider -->

# AKI 與其他重要文獻

---

# AKI & CRRT
## 急性腎損傷與連續性腎臟替代治療

**Obesity & CRRT Outcomes**
- [Kusirisin P et al., *Crit Care* 2026](https://doi.org/10.1186/s13054-026-05396-z)
- 肥胖對 CRRT 預後的影響：需調整 dosing 策略

**Lower vs Standard CRRT Dose — Meta-analysis**
- [Lumlertgul N et al., *Crit Care* 2026](https://doi.org/10.1186/s13054-026-05403-4)
- 低劑量 vs 標準劑量 CRRT 的整合分析
- 標準劑量 (20-25 mL/kg/h) 仍為建議基準

**Urinary Angiopoietin-2 for AKI**
- [Bailey ZA et al., *Crit Care* 2026](https://doi.org/10.1186/s13054-026-05399-0)
- 尿液 Angiopoietin-2 可作為 AKI 早期生物標記
- 反映腎臟微血管損傷 (microvascular injury)

> **Clinical Pearl**: CRRT 劑量仍建議維持 20-25 mL/kg/h，低劑量策略未顯示明確優勢

---

<!-- _class: small-text -->

# 其他重要文獻
## Miscellaneous Key Publications

| 主題 | 作者 | 期刊 | 重點 |
|------|------|------|------|
| Albumin 20% 完整回顧 | [Hahn RG et al.](https://doi.org/10.1186/s13054-026-05407-0) | Crit Care | 高濃度白蛋白在重症的角色與適應症 |
| Fibrinogen Threshold | [Chen S et al.](https://doi.org/10.1186/s13054-026-05393-2) | Crit Care | 重症患者 fibrinogen 補充閾值探討 |
| SAP Subphenotypes | [Wan J et al.](https://doi.org/10.1186/s13054-026-05411-4) | Crit Care | Severe acute pancreatitis 亞表型分類 |
| Muscle Atrophy Ultrasound | [Lin CC et al.](https://doi.org/10.1186/s13054-026-05416-z) | Crit Care | 超音波評估 ICU 肌肉萎縮的標準化方法 |
| Centenarian ICU Admissions | [Raykateeraroj et al.](https://doi.org/10.1186/s13054-026-05419-9) | Crit Care | 百歲人瑞 ICU 入住趨勢與預後分析 |

> **Clinical Pearl**: 超音波評估肌肉萎縮是 ICU-acquired weakness 早期偵測的實用工具

---

# 總結 Key Takeaways

1. **SSC 2026** = 近年最重要的敗血症指引更新，成人 + 兒童同步發表
2. **ARDS resolution** 首次獲得共識定義，改善臨床試驗 endpoint 一致性
3. **Refractory septic shock** 獲得首個臨床診斷標準 (SCCM/ESICM Delphi)
4. **AI/ML** 在心臟停止後預後預測的應用日益增加，EEG + proteomics 為研究熱點
5. **ECMO 併發症** 開始建立標準化定義，促進跨中心研究品質
6. **溺水 bystander CPR** 含 rescue breathing 效果顯著優於 hands-only (AOR 11.53 vs 3.63)

> 本雙週期為 **sepsis guidelines 的里程碑時期**，臨床實務將因此改變

---

<!-- _class: small-text -->

# 參考文獻 References (1/2)

1. Prescott HC et al. Surviving Sepsis Campaign 2026 Guidelines — Adults. [*CCM*. 2026.](https://doi.org/10.1097/CCM.0000000000007075)
2. Weiss SL et al. SSC 2026 International Guidelines — Pediatric Sepsis. [*ICM*. 2026.](https://doi.org/10.1007/s00134-026-08360-2)
3. Leone M et al. Refractory Septic Shock Definition — Delphi Consensus. [*CCM*. 2026.](https://doi.org/10.1097/CCM.0000000000007124)
4. Lafon T et al. NLR as Alternative to mHLA-DR in Sepsis. [*ICM*. 2026.](https://doi.org/10.1007/s00134-026-07429-6)
5. van Lier D et al. DPP3 and Angiotensin II in Sepsis. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05412-3)
6. Arlt B et al. Proenkephalin A for Sepsis-Associated AKI. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05398-7)
7. Han Y et al. Vitamin D Deficiency and Sepsis Outcomes. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05405-2)
8. Wetterberg H et al. Sepsis and Psychiatric Morbidity. [*CCM*. 2026.](https://doi.org/10.1097/CCM.0000000000007089)
9. Weir TE, Fan E, Goligher EC. Consensus Definition of ARDS Resolution. [*CCM*. 2026.](https://doi.org/10.1097/CCM.0000000000007107)
10. Coppola S et al. HFNC vs Helmet CPAP in AHRF. [*CCM*. 2026.](https://doi.org/10.1097/CCM.0000000000007116)
11. Caroli A et al. RELAx Bayesian Re-analysis — PEEP in Non-ARDS. [*CCM*. 2026.](https://doi.org/10.1097/CCM.0000000000007098)
12. Urner M et al. Sex-Specific Tidal Volume Differences. [*CCM*. 2026.](https://doi.org/10.1097/CCM.0000000000007102)
13. Meuwese CL et al. Respiratory Envelope Framework. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05415-0)
14. Granton D et al. ARDS Complications Systematic Review. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05408-z)
15. Padappayil P et al. ARDS 20-Year NIS Trends. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.01.032)

---

<!-- _class: small-text -->

# 參考文獻 References (2/2)

16. Tseng HY et al. tNGS for ICU Pneumonia — Taiwan Multicenter Study. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05420-3)
17. Gregoire N et al. Amikacin Nebulization Pharmacokinetics. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05395-0)
18. Kalil AC et al. Inhaled Antibiotics for VAP — Editorial. [*CCM*. 2026.](https://doi.org/10.1097/CCM.0000000000007110)
19. Sedik S et al. IAPA Review. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05388-z)
20. Pladet et al. VA-ECMO Bleeding Correlates. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05392-1)
21. Brown et al. ECMO Complications Standardized Definition. [*ICM*. 2026.](https://doi.org/10.1007/s00134-026-07445-6)
22. Koszutski et al. Cerebral Hypercapnia on VA-ECMO. [*ICM*. 2026.](https://doi.org/10.1007/s00134-026-07438-5)
23. Saura O et al. VT Ablation Timing on VA-ECMO. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05401-6)
24. Tavecchia et al. Landiolol in Cardiogenic Shock. [*Chest*. 2026.](https://doi.org/10.1016/j.chest.2026.02.015)
25. Ling RR et al. Frailty and Cardiogenic Shock Mortality. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05410-5)
26. Abe Y et al. Bystander CPR in Drowning. [*Resuscitation*. 2026.](https://doi.org/10.1016/j.resuscitation.2026.110598)
27. Mellett-Smith et al. OHCA in Children Meta-analysis. [*CCM*. 2026.](https://doi.org/10.1097/CCM.0000000000007095)
28. Loaec et al. Diastolic BP During Pediatric IHCA. [*CCM*. 2026.](https://doi.org/10.1097/CCM.0000000000007088)
29. Xhepa S et al. EEG ML Prognostication Post-Cardiac Arrest. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05418-x)
30. Lumlertgul N et al. Lower vs Standard CRRT Dose Meta-analysis. [*Crit Care*. 2026.](https://doi.org/10.1186/s13054-026-05403-4)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC**
