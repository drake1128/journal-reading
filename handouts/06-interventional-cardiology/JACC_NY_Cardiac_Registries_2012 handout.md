# 紐約州心臟登錄系統：歷史、貢獻與未來啟示 / The New York State Cardiac Registries

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-03-26**
**原文連結：[JACC — The New York State Cardiac Registries: History, Contributions, Limitations, and Lessons for Future Efforts](https://doi.org/10.1016/j.jacc.2011.12.051)**

> Hannan EL, Cozzens K, King SB III, Walford G, Shah NR. *J Am Coll Cardiol*. 2012;59(25):2309-16.

---

## 目錄

1. [歷史背景與緣起](#1-歷史背景與緣起)
2. [登錄系統的建立與運作](#2-登錄系統的建立與運作)
3. [公開報告的影響](#3-公開報告的影響)
4. [登錄系統的研究貢獻](#4-登錄系統的研究貢獻)
5. [侷限與批評](#5-侷限與批評)
6. [未來啟示與經驗教訓](#6-未來啟示與經驗教訓)
7. [參考文獻](#7-參考文獻)

---

## 1. 歷史背景與緣起

### 問題的發現

1988 年，紐約州衛生署長 Dr. David Axelrod 發現州內各醫院 coronary artery bypass graft (CABG) surgery 的院內死亡率存在高達 **五倍** 的差異。當時僅有行政資料 (administrative data)，無法充分解釋這些差異究竟源自病患嚴重度差異，還是醫療品質差異。

### HCFA 的前車之鑑

聯邦 Health Care Financing Administration (HCFA，即後來的 CMS) 曾於 1986-1992 年間使用 Medicare 行政資料發布醫院風險校正死亡率，但因以下問題於 1992 年停止：

- 使用行政資料的不精確性
- 病患分組方法的爭議
- 資料品質的多重疑慮

### 臨床登錄系統的誕生

鑑於行政資料的不足，紐約州衛生署 (DOH) 決定建立 **病患層級的臨床資料庫**，納入經文獻回顧確認的危險因子、人口學資料、併發症、手術類型及出院狀態。

> **Pearl 1**: 後續研究證實，臨床登錄資料比行政資料更能預測死亡率，且兩種資料庫對醫院品質的評估結論不盡相同。

---

## 2. 登錄系統的建立與運作

### 時間軸

| 年份 | 里程碑 |
|------|--------|
| 1989 | Cardiac Surgery Reporting System (CSRS) 建立 |
| 1990 | 首次於 JAMA 發表醫院績效報告，同日 DOH 向 New York Times 公開醫院名稱與風險校正死亡率 |
| 1991 | Pediatric Cardiac Surgery Reporting System 建立 |
| 1992 | Percutaneous Coronary Interventions Reporting System (PCIRS) 建立；首次公布外科醫師個人數據（rolling 3-year basis） |
| 1997 | PCIRS 年度報告開始發布 |

### 資料收集與品質管控

所有經 Certificate of Need 核准執行心臟手術的醫院，須將資料提交 DOH / University at Albany School of Public Health 進行：

1. **資料清理 (Cleaning)**：與行政資料庫 (SPARCS) 比對，確保所有病患皆已納入、出院狀態正確
2. **稽核 (Auditing)**：由 DOH 稽核人員到院查核病歷中的危險因子編碼
   - 選擇稽核醫院的依據：距上次稽核時間、過去問題紀錄、重要危險因子通報率異常偏高
   - 輕微問題→要求重新摘錄資料；重大問題→醫院須自費聘請獨立摘錄人員

### 報告方法學

- 使用 **logistic regression model** 計算每位病患的預期死亡機率
- 採用 backward stepwise elimination 搭配 training/validation samples 進行 cross-validation
- 風險校正死亡率 = (observed/expected) x statewide rate
- 使用 95% confidence intervals 判定 outlier 狀態（顯著高於/低於/與州平均無差異）
- 2004 年起改用 **in-hospital + 30-day mortality** 取代單純 in-hospital mortality

### 即時回饋機制

- 風險模型年度變化極小，醫院可即時估算自身風險校正死亡率
- DOH 於報告發布之間會發送 **alert letters** 給死亡率偏高的醫院
- 這些警告信常成為醫院啟動改善的契機

---

## 3. 公開報告的影響

### 3.1 死亡率的變化

| 指標 | 數據 |
|------|------|
| CABG in-hospital mortality (1989 → 1992) | 3.52% → 2.78% |
| Risk-adjusted mortality 下降幅度 (1989-1992) | **41%**（4.17% → 2.45%） |
| 首份報告前半年 (1990) vs 前一年 (1989) | 14% mortality decline |
| 紐約州 vs 美國其他地區 (1994-1999) | Risk-adjusted odds ratio = **0.66** (95% CI: 0.57-0.77) |

> **Pearl 2**: Peterson et al. 使用 Medicare 資料發現，1992 年紐約州的 CABG 風險校正死亡率為全美最低，且 1987-1992 年間的下降幅度高於所有低於平均死亡率的州。

### 3.2 醫院品質改善實例

**St. Peter's Hospital, Albany**
- 1991-1992 年被認定為 significantly higher than expected mortality
- 問題根源：emergency cases 死亡率 26%（州平均 7%），elective/urgent 則與州平均相當
- 改善措施：多團隊檢討急診病患術前穩定化流程
- 結果：1993 年 54 名 emergency CABG 病患**零死亡**

**Winthrop Hospital, Mineola**
- 首次公開報告中死亡率為全州最高之一，遭 DOH 列為觀察
- 改善措施：聘任新心臟外科主任、設置專責樓層、聘用心臟專科護理師與 PA、術前逐例審查、設置專責 cardiac anesthesia 服務
- Risk-adjusted mortality：9.2% → 4.6% → **2.3%**（1989-1991）

**Erie County Medical Center, Buffalo**
- 1989 年上半年全州最高風險校正死亡率
- 1990 年自願暫停手術實施改革
- Risk-adjusted mortality：7.31% (1989-1991) → 2.51% (1993-1995) → **1.77%** (1996-1998)
- 年手術量從 ~100 例上升至 219 例

### 3.3 對外科醫師的影響

- 1989-1992 年間，**27 名低手術量外科醫師** 停止在紐約州執行心臟手術
  - 部分離州、部分退休、部分轉型為非心臟手術
  - 該群組最後一年的 risk-adjusted CABG mortality 為 **11.9%**（州平均 3.1%）
- Jha & Epstein 研究：最差四分位 (worst quartile) 的外科醫師，**20%** 在報告發表後 2 年內停止執業，而前三個四分位僅約 5%

### 3.4 高風險病患迴避與外州轉介

此為公開報告制度最具爭議之處：

**支持迴避論的證據**：

- Omoigui et al.：Cleveland Clinic 接收的紐約州 CABG 病患從平均 61.4 人/年（1980-1988）增至 96.2 人/年（1989-1993），且病情較重
- Moscucci et al.：1998-1999 年紐約 PCI 病患的 AMI、cardiogenic shock、CHF 盛行率低於 Michigan 8 家醫院
- 調查顯示 67% 紐約外科醫師曾拒絕至少 1 名病患、83% 介入心臟科醫師同意公開報告降低了 PCI 的執行率

**反駁迴避論的證據**：

- 1990 年首份報告發布前無預期，最早可能的迴避行為始於 1991 年
- Hannan et al.：紐約州 Medicare CABG 病患的 AMI、年齡 ≥80 歲、緊急入院、女性比例均顯著**高於**美國其他地區
- 紐約州外州轉介率（1994: 9.9%; 1999: 10.4%）實際**低於**全國其他地區（10.4%; 10.5%）
- 紐約 PCI 高風險病患比例較低可能反映的是每人口 PCI 執行量較高（分母效應），而非高風險病患被排除

### 3.5 Shock 病患排除政策的影響

2006 年起 DOH 將 cardiogenic shock 病患排除於風險校正死亡率計算之外：

| 指標 | 2005（含 shock） | 2006-2008（排除 shock） |
|------|-------------------|------------------------|
| PCI shock 病患數 | 83 | 133、146、138/年 |
| PCI shock mortality | 34% | 45%（合併） |
| PCI shock 年增長 | — | 平均 **+67%/年** |
| CABG shock 病患數 | 32 | 46、41、43/年 |
| CABG shock mortality | 22% | 38% |

> **Pearl 3**: 將 shock 病患排除公開報告後，接受 PCI 的 shock 病患數平均每年增加 67%，顯示公開報告確實可能影響醫師對高風險病患的治療決策。

### 3.6 市場佔有率的影響

- Hannan et al. (2004)：1989-1992 年間醫院手術量無顯著變化
- Romano & Zhou：被認定為顯著低死亡率的醫院在報告發布後第一個月 CABG 量增加 22%
- Jha & Epstein (2006)：1989-2002 年間，最佳/最差四分位醫院的市場佔有率**無顯著變化**
- 1996-1997 調查：僅 22% 心臟科醫師常規與病患討論報告、僅 38% 用報告進行轉診決策

### 3.7 報告的預測能力

| 研究 | 方法 | 結論 |
|------|------|------|
| Jha & Epstein | 使用 1993 年數據預測 1996 年表現 | Top decile 醫院 risk-adjusted mortality 1.82% vs bottom decile 2.89% |
| 同上（跨 6 年彙整） | 使用 3 年前數據預測 | Top decile 1.59% vs bottom decile 2.78% |
| Glance et al. | 比較不同時間點評估 | **2 年前數據是好的預測指標**；3 年前數據辨識低表現醫院能力較差 |

---

## 4. 登錄系統的研究貢獻

紐約州心臟登錄系統被廣泛用於多領域的研究：

### Comparative Effectiveness 研究

- **CABG vs PCI** 的長期比較（結合 CSRS + PCIRS 建立縱向資料庫）
- **Drug-eluting stents vs bare-metal stents** 療效比較
- **Off-pump vs on-pump CABG** 比較

### 政策與品質研究

- Volume-mortality relationship 分析
- 短期再入院 (short-term readmissions) 研究
- Incomplete revascularization 對 PCI 預後的影響
- 醫療可近性分析：種族、民族、性別、保險類型對心臟手術的影響
- 心臟手術適當性 (appropriateness) 評估

### 跨資料庫整合

登錄資料可與多個資料庫進行串接 (matching & merging)：

| 串接資料庫 | 用途 |
|-----------|------|
| SPARCS (Statewide Planning and Research Cooperative System) | 再入院、非導致 revascularization 的 AMI |
| New York Vital Statistics | 短期與長期院外死亡 |
| National Death Index | 出院後 30 天死亡 |
| Social Security Death Master File | 65 歲以下死亡補充 |
| CSRS + PCIRS 相互串接 | 縱向追蹤、repeat revascularization |

### 風險模型與方法學發展

- 發展 pre-procedural risk indices（可用於 informed consent）
- 比較 clinical database vs administrative database 的預測能力
- 評估不同 risk-adjustment methods 的優劣

---

## 5. 侷限與批評

### 資料準確性問題

公開報告時代無可避免的資料問題實例：

1. 某醫院提報 300 例 isolated CABG **零死亡**，比對行政資料後發現漏報約 50 名病患、其中 18 人死亡
2. 某些醫院通報極高危險因子盛行率，稽核後發現與州平均相近（**upcoding**）
3. 某醫院將病患「出院」至院內未認證的 hospice，規避 in-hospital mortality 統計
4. 改用 30-day mortality 後，醫院自行通報的院外死亡與 National Death Index 比對差異極大

### 行政資料 vs 臨床資料

使用 ICD codes 的行政資料存在根本性限制：
- 缺乏客觀臨床定義（如 creatinine 具體數值、COPD 的 FEV1/PO2/PCO2 值）
- 主觀性高，在 pay-for-performance 時代可能導致危險因子盛行率逐年上升

### Shock 定義的差異

紐約登錄系統對 cardiogenic shock 的定義較為嚴格：收縮壓 <80 mmHg 或 cardiac index <2.0，**即使在藥物或機械支持下仍然如此**。多數其他定義不要求治療後仍達此標準，造成跨系統比較困難。

### 醫師態度

- 調查顯示醫師對公開報告的態度 **不甚熱絡**
- 許多醫師認為報告方法學不夠透明或不夠公平
- 有改善的空間：更多教育、更多容納醫師建議

---

## 6. 未來啟示與經驗教訓

作者總結三大核心經驗：

### 教訓一：確保資料完整性與準確性

> **Pearl 4**: 資料準確性是公開報告制度的命脈。需要多重機制：行政資料比對確保完整性、醫療紀錄稽核確保危險因子準確性、死亡登錄比對確保院外死亡的捕獲。

### 教訓二：多方利害關係人參與

- 紐約州 Cardiac Advisory Committee (CAC) 納入全球知名臨床專家與研究者
- 歷任主席包括 John Kirklin、Kenneth Shine、Spencer King
- 定期舉辦全州 town hall meetings 說明方法學並聽取建議
- 報告的接受度取決於呈現方式與各方參與程度

### 教訓三：Outlier 狀態的激勵效應

- 被認定為 outlier 或接近 outlier 是最強大的品質改善動機
- 若報告中幾乎無 outlier，則缺乏驅動改變的力量
- 無法區分品質差異的報告，對病患和轉診醫師亦缺乏指引價值

### 未來方向

1. 報告應更加 **易懂**（同時針對臨床醫師與一般民眾）
2. 納入更多 **outcome measures**（不僅限於死亡率）
3. 加入 **appropriateness** 評估
4. 從以 **procedure 為中心** 轉向以 **disease 為中心** 的報告
5. 考慮納入 **process measures**
6. 報告需盡可能 **即時** 以維持預測效力

---

## 7. 參考文獻

1. Krakauer H, Bailey C, Skellan KJ, et al. Evaluation of the HCFA model for the analysis of mortality following hospitalization. [*Health Serv Res*. 1992;27:317-35.](https://pubmed.ncbi.nlm.nih.gov/1500289/)
2. Hannan EL, Kilburn H Jr, Lindsey ML, Lewis R. Clinical versus administrative databases for CABG surgery. [*Med Care*. 1992;30:892-907.](https://doi.org/10.1097/00005650-199210000-00002)
3. Hannan EL, Racz MJ, Jollis JG, Peterson ED. Using Medicare claims data to assess provider quality for CABG surgery: does it work well enough? [*Health Serv Res*. 1997;31:559-78.](https://pubmed.ncbi.nlm.nih.gov/9086576/)
4. Hannan EL, Kilburn H Jr, O'Donnell JF, et al. Adult open heart surgery in New York State: an analysis of risk factors and hospital mortality rates. [*JAMA*. 1990;264:2768-74.](https://doi.org/10.1001/jama.1990.03450210068035)
5. Altman LK. Heart surgery death rates decline in New York. *New York Times*. December 5, 1990.
6. Chassin MR, Hannan EL, DeBuono BA. Benefits and hazards of reporting medical outcomes publicly. [*N Engl J Med*. 1996;334:394-8.](https://doi.org/10.1056/NEJM199602083340611)
7. Coronary artery bypass surgery in New York State: 2006-2008. New York State Department of Health, December 2010.
8. Percutaneous coronary angioplasty in New York State: 2006-2008. New York State Department of Health, December 2010.
9. Dziuban SW Jr, McIlduff JB, Miller SJ, Dal Col RH. How a New York cardiac surgery program uses outcomes data. [*Ann Thorac Surg*. 1994;58:1871-6.](https://doi.org/10.1016/0003-4975(94)91740-2)
10. Chassin MR. Achieving and sustaining improved quality: lessons from New York State and cardiac surgery. [*Health Aff*. 2002;21:40-51.](https://doi.org/10.1377/hlthaff.21.4.40)
11. Coronary artery bypass surgery in New York State: 1996-1998. New York State Department of Health, January 2001.
12. Hannan EL, Kilburn H Jr, Racz M, et al. Improving the outcomes of coronary artery bypass surgery in New York State. [*JAMA*. 1994;271:761-6.](https://doi.org/10.1001/jama.1994.03510340051033)
13. Peterson ED, DeLong ER, Jollis JG, et al. The effects of New York's bypass surgery provider profiling on access to care and patient outcomes in the elderly. [*J Am Coll Cardiol*. 1998;32:993-9.](https://doi.org/10.1016/S0735-1097(98)00332-5)
14. Hannan EL, Sarrazin MSV, Doran DR, Rosenthal GE. Provider profiling and quality improvement efforts in coronary artery bypass graft surgery. [*Med Care*. 2003;41:1164-72.](https://doi.org/10.1097/01.MLR.0000088452.49032.BF)
15. Omoigui NA, Miller DP, Brown KJ, et al. Outmigration for coronary artery bypass surgery in an era of public dissemination. [*Circulation*. 1996;93:27-33.](https://doi.org/10.1161/01.CIR.93.1.27)
16. Moscucci M, Eagle KA, Share D, et al. Public reporting and case selection for percutaneous coronary interventions. [*J Am Coll Cardiol*. 2005;45:1759-65.](https://doi.org/10.1016/j.jacc.2005.01.049)
17. Dranove D, Kessler D, McClellan M, Satterthwaite M. Is more information better? The effects of "report cards" on health care providers. [*J Polit Econ*. 2005;111:555-88.](https://doi.org/10.1086/374180)
18. Epstein AJ. Do cardiac surgery report cards reduce mortality? Assessing the evidence. [*Med Care Res Rev*. 2006;63:403-26.](https://doi.org/10.1177/1077558706288831)
19. Burack JH, Impellizzeri P, Homel P, Cunningham JN Jr. Public reporting of surgical mortality: a survey of New York State cardiothoracic surgeons. [*Ann Thorac Surg*. 1999;68:1195-202.](https://doi.org/10.1016/S0003-4975(99)00818-4)
20. Narins CR, Dozier AM, Ling FS, Zareba W. The influence of public reporting of outcome data on medical decision making by physicians. [*Arch Intern Med*. 2005;165:83-7.](https://doi.org/10.1001/archinte.165.1.83)
21. Hannan EL, Kumar D, Racz M, et al. New York State's cardiac surgery reporting system: four years later. [*Ann Thorac Surg*. 2004;58:1852-7.](https://doi.org/10.1016/0003-4975(94)91737-6)
22. Mukamel DB, Mushlin AI. Quality of care information makes a difference: an analysis of market share and price changes after publication of the New York Cardiac Surgery Mortality Reports. [*Med Care*. 1998;36:945-54.](https://doi.org/10.1097/00005650-199807000-00002)
23. Romano PS, Zhou H. Do well-publicized risk-adjusted outcomes reports affect hospital volume? [*Med Care*. 2004;42:367-77.](https://doi.org/10.1097/01.mlr.0000118872.33"; )
24. Jha A, Epstein AM. The predictive accuracy of the New York State coronary artery bypass surgery report-card system. [*Health Aff*. 2006;25:844-55.](https://doi.org/10.1377/hlthaff.25.3.844)
25. Hannan EL, Stone CA, Biddle TB, DeBuono BA. Public release of cardiac surgery outcomes data in New York: what do New York State cardiologists think of it? [*Am Heart J*. 1997;134:1120-8.](https://doi.org/10.1016/S0002-8703(97)70034-3)
26. Romano PS, Rainwater JA, Antonius D. Grading the graders: how hospitals in New York and California perceive and interpret their report cards. [*Med Care*. 1999;35:295-305.](https://doi.org/10.1097/00005650-199903000-00007)
27. Mukamel DB, Mushlin AI, Weimer D, et al. Do quality report cards play a role in HMOs' contracting practices? Evidence from New York State. [*Health Serv Res*. 2000;35:319-32.](https://pubmed.ncbi.nlm.nih.gov/10778820/)
28. Mukamel DB, Weimer DL, Zwanziger J, Mushlin AI. Quality of cardiac surgeons and managed care contracting practices. [*Health Serv Res*. 2002;37:1129-44.](https://doi.org/10.1034/j.1600-0560.2002.74.x)
29. Hannan EL, O'Donnell JF, Kilburn H Jr, et al. Investigation of the relationship between volume and mortality for surgical procedures performed in New York State hospitals. [*JAMA*. 1989;262:503-10.](https://doi.org/10.1001/jama.1989.03430040065031)
30. Hannan EL, Siu AL, Kumar D, et al. The decline in coronary artery bypass graft surgery mortality in New York State: the role of surgeon volume. [*JAMA*. 1995;272:209-13.](https://doi.org/10.1001/jama.1995.03530030047031)
31. Glance LG, Dick AW, Mukamel DB, Osler TM. How well do hospital mortality rates reported in the New York State CABG report card predict subsequent hospital performance? [*Med Care*. 2010;48:466-71.](https://doi.org/10.1097/MLR.0b013e3181d5dfb7)
32. Hannan EL. Ensuring accuracy and completeness of data used for outcomes assessment. [*Ann Thorac Surg*. 2012;93:1172-3.](https://doi.org/10.1016/j.athoracsur.2011.10.033)
