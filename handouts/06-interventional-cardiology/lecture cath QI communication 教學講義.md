# lecture cath QI communication

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-01-04**

---

titlepage
    
    
    
    {\bfseries 優化病人-團隊互動系統
}
    
    {\bfseries Optimizing Patient-Team Interaction Systems
}
    
    
    
    {emergency_blue 導管室品質管理與病人安全教學講義
}
    
    
    
    
> **學習目標**  
> [10pt]
>     itemize[leftmargin=2cm]
>         \item 了解團隊溝通的核心原則
>         \item 掌握 SBAR、Brief、Huddle、Debrief 等工具
>         \item 建立導管室安全文化
>         \item 降低醫療錯誤與不良事件
>     itemize

    
    
    
    {謝慕揚醫師 MD, PhD, FESC
}
    {國立臺灣大學醫學院附設醫院新竹分院
}
    {心血管中心
}
    
    \vfill
    
    {整理日期：2026-01-04
}
    
titlepage


---

\tableofcontents

---


## 前言：為什麼需要優化病人-團隊互動？


### 醫療溝通失誤的影響


關鍵數據{

- 超過 **60
- 不良交班導致近 **80
- 近 **30
- 五年內交班失誤導致 1,744 例死亡與 17 億美元訴訟成本


}


### 導管室的特殊挑戰


導管室（Cardiac Catheterization Laboratory, CCL）是高風險環境，具有以下特點：


| p{10cm}}  **挑戰類型** | **說明** |  |
| --- | --- | --- |
| **挑戰類型** | **說明** |  |
| 程序複雜度 | 從診斷性心導管到複雜 PCI、TAVR、電生理手術等，程序日益複雜 |  |
| 團隊組成多元 | 心臟科醫師、麻醉醫師、護理師、放射師、技術員等多專業協作 |  |
| 時間壓力 | 急性心肌梗塞（STEMI）需在 90 分鐘內完成 Door-to-Balloon |  |
| 輻射暴露 | 長時間 fluoroscopy 對病人與醫護人員的輻射風險 |  |
| 併發症潛在風險 | 血管穿孔、血腫、對比劑腎病、心律不整等 |  |


## TeamSTEPPS 框架概述


### 什麼是 TeamSTEPPS？


**TeamSTEPPS**（Team Strategies and Tools to Enhance Performance and Patient Safety）是由 AHRQ 與美國國防部共同開發的實證團隊合作訓練計畫。自 2006 年推出以來，已有超過 1,500 家醫院實施，培訓超過 30 萬名醫療專業人員。


### TeamSTEPPS 五大核心原則


tikzpicture[scale=0.9]
    
    \node[circle, draw=emergency_red, fill=emergency_red!20, minimum size=3cm, text width=2.5cm, align=center, font=\bfseries] at (0,0) {病人安全
團隊照護};
    
    
    \node[rectangle, draw=emergency_blue, fill=lightblue, rounded corners, minimum width=3cm, minimum height=1.2cm, align=center] at (0,4) {**領導力**
Leadership};
    \node[rectangle, draw=emergency_blue, fill=lightblue, rounded corners, minimum width=3cm, minimum height=1.2cm, align=center] at (4,0) {**情境監測**
Situation Monitoring};
    \node[rectangle, draw=emergency_blue, fill=lightblue, rounded corners, minimum width=3cm, minimum height=1.2cm, align=center] at (0,-4) {**相互支援**
Mutual Support};
    \node[rectangle, draw=emergency_blue, fill=lightblue, rounded corners, minimum width=3cm, minimum height=1.2cm, align=center] at (-4,0) {**溝通**
Communication};
    
    
    \draw[->, thick, emergency_blue] (0,1.8) -- (0,3.2);
    \draw[->, thick, emergency_blue] (1.8,0) -- (2.8,0);
    \draw[->, thick, emergency_blue] (0,-1.8) -- (0,-3.2);
    \draw[->, thick, emergency_blue] (-1.8,0) -- (-2.8,0);
tikzpicture


### 四大可教導技能


| p{5cm}p{6cm}}  **技能** | **定義** | **導管室應用** |
| --- | --- | --- |
| **技能** | **定義** | **導管室應用** |
| **溝通**    Communication | 結構化資訊交換流程，確保團隊成員間資訊清晰準確 | SBAR 報告    Call-Out    Check-Back    Handoff |
| **領導力**    Leadership | 最大化團隊成員活動能力，確保行動被理解、資訊被分享 | Brief（術前簡報）    Huddle（臨時會議）    Debrief（術後檢討） |
| **情境監測**    Situation Monitoring | 持續掃描環境，追蹤團隊成員表現，維持共同心智模式 | STEP 工具    I'M SAFE 自我評估    Cross-monitoring |
| **相互支援**    Mutual Support | 預測並滿足團隊成員需求，維持情境覺察的能力 | Task Assistance    Feedback    CUS 警示    Two-Challenge Rule |


## 溝通工具：SBAR


### SBAR 定義與背景


SBAR 起源{
SBAR 技術最初由美國海軍為核潛艦通訊開發，2003 年由 Kaiser Permanente 的快速反應團隊首次引入醫療領域。研究顯示 SBAR 可有效減少遺漏錯誤、提高醫療團隊滿意度，並降低病人不良事件發生率。
}


### SBAR 四要素詳解


| p{5cm}p{6cm}}  **要素** | **內容** | **導管室範例** |
| --- | --- | --- |
| **要素** | **內容** | **導管室範例** |
| **S** - Situation   （情況） | 目前發生什麼事？    自我介紹    病人身份確認    簡述當前問題 | 「我是心導管室護理師王小明，我正在照顧病人陳先生，67 歲男性，剛完成 LAD PCI。他現在出現右股動脈穿刺處血腫擴大。」 |
| **B** - Background   （背景） | 相關臨床背景    病史、檢驗結果    目前治療 | 「病人使用 Heparin 抗凝，ACT 目前 180 秒。術中使用 7Fr sheath，使用 closure device 止血。病人有服用 Aspirin 和 Ticagrelor。」 |
| **A** - Assessment   （評估） | 你認為問題是什麼？    根據觀察做出判斷 | 「我評估可能是 closure device 失效或持續出血。血腫大小從 3 公分擴大到 6 公分，病人主訴穿刺處疼痛加劇。」 |
| **R** - Recommendation   （建議） | 需要什麼處置？    提出具體建議    確認對方回應 | 「建議您來評估病人，考慮是否需要延長壓迫或進行血管攝影檢查。請問您多久可以到達？」 |


### SBAR 在導管室的應用情境


- **術中緊急通報**：向主治醫師報告併發症
- **跨科會診**：聯繫心臟外科、麻醉科
- **交班報告**：導管室到恢復室的病人交接
- **快速反應團隊啟動**：RRT 或 Code Blue 情境


使用 SBAR 時務必記得：

- 先自我介紹 — 不要假設對方認識你
- 使用病人雙重身份核對（姓名 + 出生日期或病歷號）
- 建議階段要具體 — 說明需要什麼、何時需要
- 確認對方理解並接受建議（Check-Back）


## 領導工具：Brief、Huddle、Debrief


### 運動類比理解三種會議


想像一支棒球隊：

- **Brief**（賽前會議）：比賽開始前討論策略、分配角色
- **Huddle**（暫停會議）：比賽中暫停，調整戰術、因應變化
- **Debrief**（賽後檢討）：比賽結束後回顧表現，找出改進方向


### Brief（術前簡報）


#### 定義與目的


Brief 是在開始工作或程序前進行的短暫會議，用於：

- 分享計畫與討論團隊組成
- 分配角色與責任
- 建立期望與工作氛圍
- 預測可能結果與應變計畫


#### 導管室 Pre-PCI Time-Out Checklist


| p{10cm}}  **項目** | **確認內容** |  |
| --- | --- | --- |
| **項目** | **確認內容** |  |
| **病人身份** | 姓名、出生日期、病歷號雙重核對 |  |
| **同意書** | 手術同意書已簽署、病人了解程序風險 |  |
| **過敏史** | 藥物過敏、對比劑過敏史、shellfish 過敏 |  |
| **禁食狀態** | NPO 時間、最後進食時間 |  |
| **抗凝/抗血小板** | 目前使用的 anticoagulant 與 antiplatelet agent    Loading dose 是否已給予 |  |
| **腎功能** | eGFR、Creatinine、對比劑腎病風險評估 |  |
| **預期程序** | 診斷性心導管 / PCI / 結構性介入    預計使用的 stent 或 device |  |
| **血管通路** | Radial / Femoral、ultrasound 引導 |  |
| **備血狀態** | 是否需要備血、Type  | Screen 完成 |
| **心臟外科備援** | 是否需要 surgical backup、通知狀態 |  |
| **團隊角色** | 主刀醫師、助手、scrub nurse、circulating nurse、技術員 |  |
| **特殊考量** | Pacemaker、ICD、LVAD、困難血管通路 |  |


### Huddle（臨時會議）


#### 定義與觸發時機


Huddle 是工作中的即時簡短會議，用於：

- 建立情境覺察
- 強化既定計畫
- 根據情況變化調整團隊合作計畫


#### 需要召開 Huddle 的情境


| p{9cm}}  **觸發情境** | **討論重點** |  |
| --- | --- | --- |
| **觸發情境** | **討論重點** |  |
| 病人狀況改變 | 血壓下降、心律不整、對比劑過敏反應 |  |
| 程序複雜度增加 | 發現 Left Main 病變、需要改用 rotational atherectomy |  |
| 設備問題 | 導管故障、影像系統異常 |  |
| 團隊成員變動 | 換班、需要額外人手支援 |  |
| 時間壓力 | 緊急 STEMI 進入、多個急診同時到達 |  |
| 安全疑慮 | 任何團隊成員發現潛在風險 |  |


### Debrief（術後檢討）


#### Debrief 核心問題


> enumerate
>     \item 溝通是否清楚？
>     \item 角色與責任是否明確？
>     \item 情境覺察是否維持？
>     \item 工作負荷分配是否合理？
>     \item 是否有尋求或提供協助？
>     \item 是否有犯錯？如何在未來預防？
>     \item 什麼做得好？可以繼續保持什麼？
>     \item 什麼可以改進？如何改進？
> enumerate


## 情境監測工具


### STEP 工具


STEP 是維持情境覺察的掃描工具：


| p{10cm}}  **要素** | **監測內容** |  |
| --- | --- | --- |
| **要素** | **監測內容** |  |
| **S** - Status of the Patient | 病人生命徵象、意識狀態、疼痛程度、出血情況 |  |
| **T** - Team Members | 團隊成員狀態、疲勞程度、是否需要支援 |  |
| **E** - Environment | 設備運作、藥物準備、輻射劑量、無菌環境 |  |
| **P** - Progress Toward Goal | 程序進度、是否按計畫進行、預期完成時間 |  |


### I'M SAFE 自我評估


> 在開始工作前，評估自己是否處於最佳狀態：
> itemize
>     \item **I** - Illness（生病）：我今天身體健康嗎？
>     \item **M** - Medication（藥物）：我正在服用影響判斷力的藥物嗎？
>     \item **S** - Stress（壓力）：我目前的壓力程度是否會影響工作？
>     \item **A** - Alcohol and Drugs（酒精與毒品）：最近 8-24 小時內有飲酒嗎？
>     \item **F** - Fatigue（疲勞）：我是否有足夠休息？是否過度疲勞？
>     \item **E** - Eating and Elimination（飲食與排泄）：我是否有適當進食、飲水？
> itemize


## 相互支援工具


### CUS 警示語


當發現安全疑慮時，使用 CUS 警示語逐步升級：


| p{10cm}}  **警示等級** | **說明與範例** |  |
| --- | --- | --- |
| **警示等級** | **說明與範例** |  |
| **C** - I am **Concerned** | 「我有些擔心這個 lesion 的鈣化程度...」 |  |
| **U** - I am **Uncomfortable** | 「我對於不使用 IVUS 就直接 stenting 感到不安...」 |  |
| **S** - This is a **Safety** issue | 「這是安全問題！我們需要暫停程序重新評估。」 |  |


### Two-Challenge Rule（雙重挑戰規則）


當你的擔憂第一次被忽視時，有責任再次提出（至少兩次）。如果仍被忽視，應向更高層級報告或啟動 chain of command。


### Check-Back（覆誦確認）


> **醫師**：「請給病人 Heparin 5000 units IV bolus。」  
> [5pt]
> **護理師**：「確認，Heparin 5000 units IV bolus。」  
> [5pt]
> **醫師**：「正確。」  
> [5pt]
> **護理師**：（給藥後）「Heparin 5000 units 已經給予。」


## Handoff（交班）工具


### I-PASS 交班法


| p{10cm}}  **要素** | **內容** |  |
| --- | --- | --- |
| **要素** | **內容** |  |
| **I** - Illness Severity | 病人嚴重程度：穩定 / 需密切觀察 / 不穩定 |  |
| **P** - Patient Summary | 病人摘要：診斷、重要病史、今日處置 |  |
| **A** - Action List | 待辦事項：待完成的檢查、待追蹤的結果 |  |
| **S** - Situation Awareness | 情境提醒：可能發生的變化、應變計畫 |  |
| **S** - Synthesis by Receiver | 接收者總結：複述重點、澄清疑問 |  |


### 交班五大原則


1. **Accountability**：在雙方都確認責任轉移前，你仍對病人負責
2. **Uncertainty**：有任何不確定時，必須在交班完成前釐清
3. **Verbal communication**：不能假設對方會閱讀或理解書面交班
4. **Acknowledgment**：直到對方確認理解並接受，你才能解除責任
5. **Opportunity**：交班是重新檢視病人安全與照護品質的好時機


## 導管室安全 Checklist 範本


### WHO 風格導管室安全核對表


> **【Sign In — 程序開始前】**
> itemize[leftmargin=1cm]
>     \item[$\square$] 病人身份確認（姓名、出生日期、病歷號）
>     \item[$\square$] 程序同意書已簽署
>     \item[$\square$] 過敏史確認
>     \item[$\square$] 禁食狀態確認
>     \item[$\square$] 抗凝/抗血小板藥物狀態
>     \item[$\square$] 腎功能與對比劑劑量計畫
>     \item[$\square$] 所有團隊成員自我介紹
> itemize
> **【Time Out — 程序開始時】**
> itemize[leftmargin=1cm]
>     \item[$\square$] 確認病人、程序部位、預計程序
>     \item[$\square$] 預期困難或特殊考量討論
>     \item[$\square$] 必要設備與藥物已備妥
>     \item[$\square$] 心臟外科備援狀態（如適用）
> itemize
> **【Sign Out — 程序結束前】**
> itemize[leftmargin=1cm]
>     \item[$\square$] 程序名稱確認並記錄
>     \item[$\square$] 器材計數正確
>     \item[$\square$] 血管通路處理方式
>     \item[$\square$] 術後照護計畫
>     \item[$\square$] 需要注意的併發症徵兆
>     \item[$\square$] 抗血小板/抗凝續用計畫
> itemize


## 建立安全文化


### 心理安全環境


關鍵原則{

- 所有團隊成員都有權利和責任為病人安全發聲
- 提出安全疑慮不會遭受懲罰或嘲諷
- 鼓勵主動報告錯誤與 near miss
- 領導者應示範接受回饋與建議的開放態度


}


### 從錯誤中學習


| p{9cm}}  **方法** | **說明** |  |
| --- | --- | --- |
| **方法** | **說明** |  |
| **RCA**    Root Cause Analysis | 針對嚴重不良事件進行系統性根本原因分析 |  |
| **FMEA**    Failure Mode and Effects Analysis | 預防性分析可能的失效模式與其影響 |  |
| **M | M Conference** | 定期召開 Morbidity  |
| **PDSA Cycle**    Plan-Do-Study-Act | 快速循環改善，測試變革並評估成效 |  |


## 參考資料


1. Agency for Healthcare Research and Quality. TeamSTEPPS 3.0. [*AHRQ TeamSTEPPS Program](https://www.ahrq.gov/teamstepps-program/). 2023.*
2. Müller M, Jürgens J, Redaèlli M, et al. Impact of the communication and patient hand-off tool SBAR on patient safety: a systematic review. [*BMJ Open](https://doi.org/10.1136/bmjopen-2018-022202). 2018;8(8):e022202.*
3. Naidu SS, Abbott JD, Bagai J, et al. SCAI expert consensus update on best practices in the cardiac catheterization laboratory. [*Catheter Cardiovasc Interv](https://doi.org/10.1002/ccd.29744). 2021;98(2):255-276.*
4. Shahid S, Thomas S. Situation, Background, Assessment, Recommendation (SBAR) Communication Tool for Handoff in Health Care – A Narrative Review. [*Safety in Health](https://doi.org/10.1186/s40886-018-0073-1). 2018;4(1):7.*
5. Starmer AJ, Spector ND, Srivastava R, et al. Changes in Medical Errors after Implementation of a Handoff Program. [*N Engl J Med](https://doi.org/10.1056/NEJMsa1405556). 2014;371(19):1803-1812.*
6. Institute for Healthcare Improvement. SBAR Tool: Situation-Background-Assessment-Recommendation. [*IHI Tools](https://www.ihi.org/resources/Pages/Tools/SBARToolkit.aspx). 2023.*
7. The Joint Commission. Sentinel Event Alert: Inadequate hand-off communication. 2017.


## 附錄：常用溝通工具速查表


> **SBAR**（緊急報告）
> itemize[leftmargin=1cm]
>     \item S - Situation（情況）：發生什麼事？
>     \item B - Background（背景）：相關臨床背景
>     \item A - Assessment（評估）：你認為問題是什麼？
>     \item R - Recommendation（建議）：你建議怎麼做？
> itemize
> **CUS**（安全警示）
> itemize[leftmargin=1cm]
>     \item C - I am Concerned（我擔心）
>     \item U - I am Uncomfortable（我不安）
>     \item S - This is a Safety issue（這是安全問題）
> itemize
> **I-PASS**（交班）
> itemize[leftmargin=1cm]
>     \item I - Illness Severity（嚴重程度）
>     \item P - Patient Summary（病人摘要）
>     \item A - Action List（待辦事項）
>     \item S - Situation Awareness（情境提醒）
>     \item S - Synthesis by Receiver（接收者總結）
> itemize


*本講義整理自 AHRQ TeamSTEPPS、IHI、SCAI 等國際醫療品質與病人安全資源*