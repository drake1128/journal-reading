# ICM AI in ICU

**整理：謝慕揚 MD, PhD, FESC**
**日期：2025-05-10**

---

\maketitle


> **重點訊息：**人工智慧（AI）已深入日常生活，並將成為醫療照護的核心組成，包括加護病房（ICU）。然而，儘管已發表大量AI模型，真正進入臨床常規使用的仍屬少數。本文綜合分析真實世界的成功與失敗案例，並提出實用的檢核清單，以支持安全有效的ICU AI部署。
> **關鍵概念：**AI部署不僅是技術問題，更是社會技術挑戰（socio-technical challenge）。在電腦中訓練模型與將人機系統嵌入真實臨床環境的限制、變異性和文化中，是根本不同的兩件事。


\tableofcontents

---


## 研究資訊


| p{10cm}}  **項目** | **內容** |  |
| --- | --- | --- |
| **項目** | **內容** |  |
| 文章類型 | Editorial（社論） |  |
| 標題 | Deploying AI in the ICU: Learning from Successes and Failures |  |
| 作者 | Matthieu Komorowski, Maurizio Cecconi |  |
| 機構 | Imperial College London, UK    Humanitas University  | IRCCS Humanitas Research Hospital, Milan, Italy |
| 期刊 | Intensive Care Medicine |  |
| 年份 | 2025 |  |
| 卷期頁碼 | 51:2410--2413 |  |
| DOI | [10.1007/s00134-025-08131-5](https://doi.org/10.1007/s00134-025-08131-5) |  |
| 收稿日期 | 2025年5月10日 |  |
| 接受日期 | 2025年9月17日 |  |
| 發表日期 | 2025年9月29日 |  |


## 背景：從預測性到可行動AI


### AI在重症醫學的發展趨勢


人工智慧正經歷從**預測性AI**（predictive AI）到**可行動AI**（actionable AI）的重要轉變。傳統AI僅預測風險，而可行動AI不僅預測風險，更能引導或建議治療選擇。


> **預測性AI（Predictive AI）：**
> itemize[leftmargin=*]
>     \item 預測疾病風險
>     \item 預測死亡率
>     \item 預測併發症發生
> itemize
> **可行動AI（Actionable AI）：**
> itemize[leftmargin=*]
>     \item 引導治療決策
>     \item 建議藥物調整
>     \item 提供即時警示與行動建議
> itemize


### 部署的挑戰


儘管已發表大量AI模型，真正進入臨床常規使用的仍屬少數。部署AI於ICU不僅是技術練習，更是社會技術挑戰。在電腦中訓練模型（in silico）與將人機系統（Human-AI system）嵌入真實臨床環境，是根本不同的任務。


## 成功案例分析


### 已證實效益的AI工具


| p{4cm}p{6.5cm}}  **應用領域** | **工具/系統** | **臨床效益** |
| --- | --- | --- |
| **應用領域** | **工具/系統** | **臨床效益** |
| 急性神經科 | Viz.ai 中風偵測平台 | 自動標記CT血管攝影疑似大血管阻塞並即時警示中風團隊，顯著縮短血管再通時間 |
| 心臟科 | AI增強ECG判讀 | 加速心導管室啟動，用於細微心肌梗塞病例 |
| 加護病房 | 早期sepsis偵測演算法 | 改善指引遵從度，部分案例降低死亡率 |
| 急診醫學 | AI檢傷分類系統 | 改善病患流程，縮短等候時間 |
| 臨床文件 | 環境AI文件系統（Ambient AI documentation） | Kaiser Permanente部署後產生數百萬份筆記，減少行政負擔，改善醫師與病患體驗 |


### 成功的共同特徵


1. **針對工作流程瓶頸**：解決臨床實際痛點
2. **低摩擦整合**：融入現有工作流程
3. **可行動輸出**：產生可執行的建議或警示
4. **輔助而非取代**：補充而非替代臨床判斷
5. **嚴謹評估**：包括RCT比較AI輔助與標準照護


## 失敗案例與教訓


### 造成傷害的案例


| p{10cm}}  **案例** | **問題與教訓** |  |
| --- | --- | --- |
| **案例** | **問題與教訓** |  |
| 英國AKI警示試驗 | 某些環境中的警示與較高14天死亡率相關，可能因非預期的工作流程改變、過度診斷或過度治療所致 |  |
| 放射科AI輔助 | AI輔助可改善部分使用者的診斷準確度，但對其他使用者反而降低準確度 |  |


### 關鍵教訓


> AI必須設計為**增強**（augment）而非**覆蓋**（override）臨床專業。介面應能適應不同使用者的技能水準。


## AI部署失敗的根本原因分析


### 錯誤的使用案例（Wrong Use Case）


許多AI模型與臨床需求對齊不佳：

- 死亡率預測缺乏可行動時間軸
- 低精確度（positive predictive value）的sepsis模型導致警報疲勞
- 開發過程中缺乏臨床醫師參與


**解決方案：**臨床醫師可識別高價值、可行的目標，如簡化文件、自動化重複監測、優化藥物滴定。多學科合作至關重要。


### 數據挑戰（Data Challenges）


| p{10cm}}  **挑戰類型** | **說明** |  |
| --- | --- | --- |
| **挑戰類型** | **說明** |  |
| 數據異質性 | ICU AI需要來自監測器、輸液幫浦、實驗室、EHR的即時、多模態、高頻數據 |  |
| 數據格式不一 | 異質數據格式限制可攜性與泛化性 |  |
| 記錄不完整 | 缺失數據影響模型準確度 |  |
| 延遲問題 | 數據傳輸延遲影響即時決策 |  |
| 與放射科對比 | 放射科通常使用乾淨、結構化的影像輸入，ICU數據複雜度更高 |  |


### 成本障礙（Cost Barriers）


- 高效能ICU AI需要即時高規格運算基礎設施
- 需要專門維護團隊
- 數位成熟度不均
- 報銷模式/投資報酬率（ROI）不明確
- 可能加劇數位健康不平等


### 安全與驗證挑戰（Safety and Validation Challenges）


> itemize[leftmargin=*]
>     \item **效能退化**：模型在不同環境表現下降
>     \item **直接病患傷害**：錯誤建議導致不良結果
>     \item **高風險應用**：如vasopressor控制、呼吸器設定
>     \item **強化學習風險**：即時學習在臨床環境不安全
>     \item **生成式模型風險**：如大型語言模型的幻覺（hallucination）與有限可解釋性
> itemize


**迫切需求：**建立共識的驗證框架，包括離線策略評估（off-policy evaluation）、模擬測試、安全基準等，可在前瞻性使用前應用。


### 工作流程整合挑戰（Workflow Integration Challenges）


- 設計不良的介面增加認知負擔
- 干擾既有工作流程
- 問題有時僅在真實使用中才浮現
- 即使高效能模型也可能因整合不佳而被棄用
- **自動化偏見**（automation bias）：盲目接受AI輸出的風險


### 倫理與法律責任問題（Ethical and Liability Concerns）


| p{10cm}}  **議題** | **說明** |  |
| --- | --- | --- |
| **議題** | **說明** |  |
| 監管框架不確定 | 高風險AI的監管框架仍不明確 |  |
| 責任歸屬 | 發生傷害時，責任歸屬（臨床醫師、開發者、機構）常不清楚 |  |
| 效能基準未定 | AI應達到平均臨床醫師表現、專家共識、還是優於特定次群體？ |  |
| 信任問題 | 缺乏明確標準導致AI可能同時被低估信任和過度期待 |  |
| 效率悖論 | 若臨床醫師保有完全責任，可能需重新驗證每個AI輸出，抵消效率收益 |  |


## 臨床AI實施檢核清單


> 此檢核清單為實用、多利害關係人指南，用於設計和部署安全、有用、可擴展的急性照護AI系統。主要作為早期規劃工具，框定ICU AI專案的關鍵考量。應與更詳細的監管、技術和營運框架並用，特別是部署後期階段。


### 1. 策略規劃（Strategic Planning）


**引導問題：**我們是否用正確的方法解決正確的問題？


| }  **檢核項目** |  |  |
| --- | --- | --- |
| **檢核項目** |  |  |
| 清楚定義臨床問題及為何AI是適當解決方案 |  |  |
| 選擇高影響、較低風險的使用案例作為務實切入點（非普遍規則；高風險專案若有足夠保障措施也可適用） |  |  |
| 設定可測量、以病患為中心或以流程為基礎的成果及KPI以監測影響（如治療時間、假警報率、30天死亡率、臨床醫師採用率） |  |  |
| 規劃完整產品生命週期：設計、部署、模型更新、安全、上市後評估，範圍與專案成熟度相稱 |  |  |
| 組建多學科團隊：臨床醫師、工程師、人因專家、病患、監管人員、商業主管 |  |  |
| 規劃擴展：商業模式、ROI、資源需求、長期支持 |  |  |


### 2. 設計與工作流程整合（Design and Workflow Integration）


**引導問題：**AI工具能否自然融入臨床實務？


| }  **檢核項目** |  |  |
| --- | --- | --- |
| **檢核項目** |  |  |
| 與臨床醫師共同設計：直覺介面，支持而非覆蓋專業判斷 |  |  |
| 確保無縫融入現有工作流程（如與EHR整合） |  |  |
| 輸出應為可行動或決策支持性質（如警示、警告），特別是在臨床醫師保留最終責任的情境 |  |  |
| 啟用手動覆蓋並記錄例外情況（fail-safes） |  |  |


### 3. 數據、驗證與安全（Data, Validation and Safety）


**引導問題：**模型在真實世界是否安全、公平、穩健？


| }  **檢核項目** |  |  |
| --- | --- | --- |
| **檢核項目** |  |  |
| 遵循既定軟體和數據標準（如HL7、FHIR）以確保可攜性 |  |  |
| 從非干擾性測試開始（如shadow mode）；盡可能規劃隨機臨床試驗 |  |  |
| 遵循良好機器學習原則（GMLP），包括外部驗證、偏見評估和次群體效能差異評估 |  |  |


### 4. 採用與治理（Adoption and Governance）


**引導問題：**如何確保採用、信任和問責？


| }  **檢核項目** |  |  |
| --- | --- | --- |
| **檢核項目** |  |  |
| 提供訓練並解釋工具的目的和功能 |  |  |
| 識別超級使用者；建立持續反饋迴路 |  |  |
| 迭代直到臨床醫師信任並依賴該工具 |  |  |
| 及早定義法律、倫理和監管角色（如知情同意、問責、治理路徑） |  |  |
| 規劃部署後監測和治理（大多數醫療器材法規要求） |  |  |


## 結論與建議


### 核心結論


1. **從成功與失敗中學習**：成功的AI採用需要分析成功與失敗案例
2. **AUC不足以評估臨床準備度**：Area under the curve對早期開發有用，但對臨床準備度評估不足
3. **人因與安全工程驅動採用**：採用必須由人因、安全工程和真實世界驗證驅動
4. **無縫工作流程整合**：AI工具應設計為無縫工作流程整合，連結明確人類行動
5. **漸進式驗證**：逐步驗證以避免已知和未預見風險


### 研究設計建議


> **理想方法：**
> itemize[leftmargin=*]
>     \item RCT測試以病患為中心的結果改善
> itemize
> **替代設計（亦可提供嚴謹證據）：**
> itemize[leftmargin=*]
>     \item 實用試驗（pragmatic trials）
>     \item 前瞻性觀察研究
>     \item 具反饋機制的階段性推出
> itemize


### 部署後要求


部署後監測、治理和迭代優化至關重要，且在許多司法管轄區是監管要求，以確保持續的安全、效能和信任。


## 詞彙表


| p{10cm}}  **術語** | **定義** |  |
| --- | --- | --- |
| **術語** | **定義** |  |
| Actionable AI | 可行動AI，不僅預測風險，更能引導或建議治療選擇 |  |
| AUC | Area Under the Curve，曲線下面積，用於評估模型區辨能力 |  |
| Automation bias | 自動化偏見，盲目接受AI輸出的傾向 |  |
| EHR | Electronic Health Records，電子健康紀錄 |  |
| FHIR | Fast Healthcare Interoperability Resources，快速醫療互操作性資源標準 |  |
| GMLP | Good Machine Learning Principles，良好機器學習原則 |  |
| Hallucination | 幻覺，生成式AI產生看似合理但錯誤的資訊 |  |
| HL7 | Health Level Seven，健康資訊交換標準 |  |
| KPI | Key Performance Indicator，關鍵績效指標 |  |
| Off-policy evaluation | 離線策略評估，使用歷史數據評估新策略效能 |  |
| ROI | Return on Investment，投資報酬率 |  |
| Shadow mode | 影子模式，AI在背景運行但不影響臨床決策的測試方式 |  |
| Socio-technical challenge | 社會技術挑戰，同時涉及技術和社會/組織因素的複雜問題 |  |


## 參考文獻


1. 
2. Cecconi M, Greco M, Shickel B, et al. Implementing artificial intelligence in critical care medicine: a consensus of 22. [*Crit Care](https://doi.org/10.1186/s13054-025-05532-2). 2025;29:290.*
3. Pinsky MR, Bedoya A, Bihorac A, et al. Use of artificial intelligence in critical care: opportunities and obstacles. [*Crit Care](https://doi.org/10.1186/s13054-024-04860-z). 2024;28:113.*
4. Smit JM, Krijthe JH, van Bommel J, et al. The future of artificial intelligence in intensive care: moving from predictive to actionable AI. [*Intensive Care Med](https://doi.org/10.1007/s00134-023-07102-y). 2023;49:1114-1116.*
5. Zhang J, Whebell S, Gallifant J, et al. An interactive dashboard to track themes, development maturity, and global equity in clinical artificial intelligence research. [*Lancet Digit Health](https://doi.org/10.1016/S2589-7500(22)00032-2). 2022;4:e212-e213.*
6. Siegler J, Frost E, Penckofer M, et al. Treatment time metrics following implementation of the Viz.ai artificial intelligence intracranial occlusion-detection and communication platform: A multicenter analysis. [*Stroke](https://doi.org/10.1161/str.56.suppl_1.TP243). 2025;6(Suppl\_1):ATP243-ATP243.*
7. Lin C-S, Liu W-T. Artificial Intelligence Enabled Rapid Identification of ST-Elevation Myocardial Infarction Using Electrocardiogram (ARISE): A Pragmatic Randomized Controlled Trial. [*NEJM AI](https://doi.org/10.1056/AIoa2400190). 2023;1(7):AIoa2400190.*
8. Boussina A, Shashikumar SP, Malhotra A, et al. Impact of a deep learning sepsis prediction model on quality of care and survival. [*npj Digit Med](https://doi.org/10.1038/s41746-023-00986-6). 2024;7:1-9.*
9. Taylor RA, Chmura C, Hinson J, et al. Impact of artificial intelligence-based triage decision support on emergency department care. [*NEJM AI](https://doi.org/10.1056/AIoa2400296). 2025;2:AIoa2400296.*
10. Tierney AA, Gayre G, Hoberman B, et al. Ambient artificial intelligence scribes: learnings after 1 year and over 2.5 million uses. [*Catal Non-issue Content](https://doi.org/10.1056/CAT.25.0040). 2025;6:CAT.25.0040.*
11. Arabi YM, Alsaawi A, Alzahrani M, et al. Electronic sepsis screening among patients admitted to hospital wards: a stepped-wedge cluster randomized trial. [*JAMA](https://doi.org/10.1001/jama.2024.25982). 2025;333:763-773.*
12. Wilson FP, Martin M, Yamamoto Y, et al. Electronic health record alerts for acute kidney injury: multicenter, randomized clinical trial. [*BMJ](https://doi.org/10.1136/bmj.m4786). 2021;372:m4786.*
13. Yu F, Moehring A, Banerjee O, et al. Heterogeneity and predictors of the effects of AI assistance on radiologists. [*Nat Med](https://doi.org/10.1038/s41591-024-02850-w). 2024;30:837-849.*
14. Kwong JCC, Nickel GC, Wang SCY, Kvedar JC. Integrating artificial intelligence into healthcare systems: more than just the algorithm. [*npj Digit Med](https://doi.org/10.1038/s41746-024-01066-z). 2024;7:1-3.*
15. Nauka PC, Kennedy JN, Brant EB, et al. Challenges with reinforcement learning model transportability for sepsis treatment in emergency care. [*npj Digit Med](https://doi.org/10.1038/s41746-025-01485-6). 2025;8:1-5.*
16. Davis FD. Perceived usefulness, perceived ease of use, and user acceptance of information technology. [*MIS Q](https://doi.org/10.2307/249008). 1989;13:319-340.*


## 附錄：原文出處


> **完整引用：**  
> Komorowski M, Cecconi M. Deploying AI in the ICU: learning from successes and failures. *Intensive Care Med*. 2025;51:2410-2413. doi:[10.1007/s00134-025-08131-5](https://doi.org/10.1007/s00134-025-08131-5)
> **致謝聲明：**  
> 原文作者聲明：ChatGPT（版本4o）用於文章早期草稿階段，提供內容建議和文字潤飾。