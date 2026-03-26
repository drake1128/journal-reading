# NEJM AI 教學講義

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-01-16**

---

Medical LLM Agents
NEJM AI
MedAgentBench: A Virtual EHR Environment to
Benchmark Medical LLM Agents
MedAgentBench：評估醫療大型語言模型代理的虛擬電子病歷環境
NEJM AI 2025;2(9). DOI: 10.1056/AIdbp2500144
整理：謝慕揚MD, PhD, FESC
日期：2026-01-16
核心發現摘要
重大發現：本研究建立首個評估LLM 在醫療記錄環境中代理能力的標準化基準。目前
最佳模型Claude 3.5 Sonnet v2 成功率為69.67%，顯示AI 代理在醫療應用中具有潛
力，但仍需改進。 臨床意義：醫師僅27% 時間用於直接臨床照護，其餘為文書與行政工作。AI 代理可望
減輕行政負擔，協助醫師回歸臨床照護。 Contents
研究概述
1.1
從Chatbot 到Agent 的演進
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 研究資訊
2.1
基本資料
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2
研究背景
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . MedAgentBench 框架
3.1
系統架構
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2
任務類別
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3
病人資料
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 主要結果
4.1
模型表現比較. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2
關鍵發現
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3
常見錯誤模式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Agentic AI 在醫療的潛在應用
5.1
可自動化的臨床工作流程
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 臨床醫師可現行採用的AI 工具與協定
研究限制
結論
參考文獻


NEJM AI 教學講義
Medical LLM Agents
10 縮寫對照表


NEJM AI 教學講義
Medical LLM Agents
研究概述
本研究來自Stanford University，建立了MedAgentBench 評估套件，用於測試大型語言模型
(Large Language Models, LLMs) 在醫療記錄環境中的代理能力。這是首個需要與醫療記錄環
境進行自主互動的標準化基準。 1.1
從Chatbot 到Agent 的演進
• 傳統LLM (Chatbot)：依賴使用者提示，提供獨立輸出
• AI Agent：主動解讀高層指令、規劃行動、與外部系統互動、迭代優化回應
• 關鍵轉變：從「AI 作為工具」轉向「AI 作為隊友」
Chatbot vs Agent 範例
臨床情境：社區型肺炎(Community-Acquired Pneumonia, CAP) 治療
Chatbot 回應：回答「CAP 的住院治療方案是什麼？」
Agent 執行：
1. 計算個人化病人風險評分
2. 評估Pseudomonas 感染風險因子
3. 分析藥物交互作用與過敏史
4. 整合先前培養數據與本地抗生素敏感性資料
5. 排隊抗生素與支持性照護醫囑供醫師審核簽署
6. 自主排程追蹤門診
研究資訊
2.1
基本資料
標題：MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents
作者：Yixing Jiang, Kameron C. Black DO MPH, Gloria Geng, Danny Park, James Zou PhD,
Andrew Y. Ng PhD, Jonathan H. Chen MD PhD
機構：Stanford University
期刊：NEJM AI 2025;2(9)
DOI：10.1056/AIdbp2500144
資源：https://github.com/stanfordmlgroup/MedAgentBench
2.2
研究背景
• 醫師僅約27% 時間用於直接臨床照護，其餘用於文書與行政工作
• 傳統QA-based AI 基準(如MedQA、MedMCQA) 已達飽和，模型表現已達超人水準
• 缺乏評估LLM 在醫療情境中代理能力的標準化基準
• 需要基於FHIR (Fast Healthcare Interoperability Resources) API 的基準測試


NEJM AI 教學講義
Medical LLM Agents
MedAgentBench 框架
3.1
系統架構
1. 臨床醫師指定任務：例如「檢查病人最近的鉀離子數值，若過低則開立補充」
2. Agent 協調器：解讀任務並規劃function calls
3. 執行任務：透過FHIR server 發送請求修改醫療記錄資料庫
4. 回饋給臨床醫師：摘要已執行的任務
3.2
任務類別
Table 1: MedAgentBench 任務類別總覽
任務類別
範例指令
EHR 系統情境
病人資訊檢索
(Patient
Informa-
tion Retrieval)
查詢姓名與生日對應的
MRN
N/A
檢驗結果檢索
(Laboratory Result
Retrieval)
查詢過去24 小時最近的
Magnesium level
提供時間、檢驗代碼、單位換算
規則
病人數據彙總
(Patient Data Ag-
gregation)
計算過去24 小時的平均血
糖值
提供時間與GLU 代碼
記錄病人數據
(Recording Patient
Data)
記錄血壓測量值118/77
mmHg
提供時間與flowsheet ID
檢查開立
(Test Ordering)
查詢HbA1C，若超過一年
則重新開立
提供LOINC code: 4548-4
轉介開立
(Referral Ordering)
開立骨科手術轉介
提供SNOMED code
藥物開立
(Medication Order-
ing)
檢查K+ level，若過低則依
劑量指示開立補充
提供NDC code、劑量計算規則、
LOINC code
3.3
病人資料
特徵
數值
獨立個體數
年齡(years, mean±SD)
58.15±19.82
女性比例
47%


NEJM AI 教學講義
Medical LLM Agents
特徵
數值
總記錄數
785,207
Observation records
563,426
Procedure records
124,969
Condition records
74,821
MedicationRequest records
21,991
主要結果
4.1
模型表現比較
Table 3: 各模型在MedAgentBench 的表現
模型
大小
形式
整體SR
Query SR
Action SR
Claude 3.5 Sonnet
v2
N/A
API
69.67%
85.33%
54.00%
GPT-4o
N/A
API
64.00%
72.00%
56.00%
DeepSeek-V3
685B
Open
62.67%
70.67%
54.67%
Gemini-1.5 Pro
N/A
API
62.00%
52.67%
71.33%
GPT-4o-mini
N/A
API
56.33%
59.33%
53.33%
o3-mini
N/A
API
51.67%
54.67%
48.67%
Qwen2.5
72B
Open
51.33%
38.67%
64.00%
Llama 3.3
70B
Open
46.33%
50.00%
42.67%
Gemini 2.0 Flash
N/A
API
38.33%
34.00%
42.67%
Gemma2
27B
Open
19.33%
38.67%
0.00%
Gemini 2.0 Pro
N/A
API
18.00%
25.33%
10.67%
Mistral v0.3
7B
Open
4.00%
8.00%
0.00%
註：SR = Success Rate (成功率)；Query SR = 查詢型任務成功率；Action SR = 行動型
任務成功率
4.2
關鍵發現
1. 最佳表現：Claude 3.5 Sonnet v2 整體成功率69.67%，Query 任務達85.33%
2. Query vs Action：大多數模型在查詢型任務表現優於行動型任務
3. 開源vs 閉源：閉源模型仍優於開源模型，開源社群仍有改進空間
4. 臨床應用潛力：可優先探索僅需資訊檢索的使用案例
4.3
常見錯誤模式
• 未精確遵循指令：如Gemini 2.0 Flash 在54% 案例中輸出無效動作
• 答案格式錯誤：模型輸出完整句子，而非預期的純數值
• 範例：模型輸出”[“value”: 5.4]”，但預期答案為”[5.4]”


NEJM AI 教學講義
Medical LLM Agents
Agentic AI 在醫療的潛在應用
5.1
可自動化的臨床工作流程
應用領域
說明
術前風險評估
(Preoperative
Risk
Assessment)
自動整合病人資料評估手術適應症
法規遵循監測
(Regulatory
Compli-
ance)
監測醫院安全措施的法規遵循情況
臨床分診
(Clinical Triage)
初步評估病人緊急程度與分類
EHR 系統設定
(EHR Configuration)
協助電子病歷系統的維護與設定
保險事前授權
(Prior Authorization)
自動化保險事前授權申請流程
病人溝通
(Patient Communica-
tion)
處理病人訊息與回覆
文件撰寫
(Documentation)
協助臨床文件撰寫與紀錄


NEJM AI 教學講義
Medical LLM Agents
臨床醫師可現行採用的AI 工具與協定
實用工具與建議
一、現行可用的AI 輔助工具
1. Ambient Clinical Intelligence (環境臨床智慧)
• Nuance DAX Copilot (Microsoft/Nuance)
• Abridge
• Suki AI
• 功能：自動將醫病對話轉錄為臨床文件
2. Clinical Documentation AI
• Epic 整合的AI 功能(InBasket message drafting)
• 各EHR 廠商的LLM 整合功能
• 功能：草擬病人訊息回覆、摘要病歷
3. 通用LLM 工具(需注意PHI 保護)
• ChatGPT、Claude、Gemini (不可輸入PHI)
• 功能：文獻搜尋、教育、一般寫作輔助
二、FHIR 標準與互操作性
• FHIR (Fast Healthcare Interoperability Resources)：美國21st Century
Cures Act 規定的醫療資料存取標準
• 多數商用EHR 廠商已支援FHIR API
• 可作為AI Agent 與EHR 系統整合的標準介面
三、採用建議
1. 優先探索查詢型任務：目前LLM 在資訊檢索任務表現較佳(Query SR 85.33% vs
Action SR 54%)
2. 保持人工監督：目前最佳模型成功率僅69.67%，仍需醫師審核
3. 關注PHI 保護：使用任何AI 工具時需確保病人資料保護
4. 選擇經驗證的工具：優先選用經FDA/CE 認證或與EHR 廠商整合的工具
研究限制
1. 無法捕捉完整真實情境：真實醫療情境需要團隊間的協調與溝通
2. 缺少臨床筆記：病人資料中未包含clinical notes 等結構化數據


NEJM AI 教學講義
Medical LLM Agents
3. 需要醫院特定設定：需要hospital-specific EHR system context
4. 病人代表性：所有病人資料來自Stanford Hospital，可能存在偏差
5. 任務範圍：專注於醫療記錄情境，未涵蓋外科或護理領域
結論
1. 結論一：MedAgentBench 是首個評估LLM 在醫療記錄環境中代理能力的標準化基準，
使用FHIR 標準可輕鬆遷移至實際EHR 系統
2. 結論二：目前最先進的LLM 展現初步能力(最佳69.67%)，但尚無法可靠處理所有臨
床相關任務的完整複雜性
3. 結論三：LLM 在查詢型任務表現優於行動型任務，建議優先探索資訊檢索類的臨床應
用
4. 結論四：Agent-based task frameworks 是推進AI 系統有效整合至臨床工作流程的必要
下一步
Take-Home Message
1. AI Agent 從「工具」演進為「隊友」，可主動規劃與執行臨床任務
2. 目前技術成熟度：查詢任務較可靠，行動任務仍需改進
3. 臨床應用建議：優先採用資訊檢索類工具，保持人工監督
4. FHIR 標準是AI 與EHR 整合的關鍵基礎設施
5. 持續關注MedAgentBench 進展可了解AI 醫療應用的最新發展
關鍵詞：Large Language Model (LLM)、AI Agent、Electronic Health Record (EHR)、FHIR、
Clinical Documentation、MedAgentBench
參考文獻
1. Jiang Y, Black KC, Geng G, et al. MedAgentBench: A Virtual EHR Environment to
Benchmark Medical LLM Agents. NEJM AI. 2025;2(9). 2. Zou J, Topol EJ. The rise of agentic AI teammates in medicine. Lancet. 2025;405:457. 3. Sahni NR, Carrus B. Artificial intelligence in US health care delivery. N Engl J Med. 2023;389:348-358. 4. Sinsky C, Colligan L, Li L, et al. Allocation of physician time in ambulatory practice: a
time and motion study in 4 specialties. Ann Intern Med. 2016;165:753-760. 5. Tripathi S, Sukumaran R, Cook TS. Eﬀicient healthcare with large language models:
optimizing clinical workflow and enhancing patient care. J Am Med Inform Assoc. 2024;31:1436-1440.


NEJM AI 教學講義
Medical LLM Agents
縮寫對照表
縮寫
全名
LLM
Large Language Model (大型語言模型)
AI
Artificial Intelligence (人工智慧)
EHR
Electronic Health Record (電子病歷)
FHIR
Fast Healthcare Interoperability Resources (快速醫療互
操作性資源)
API
Application Programming Interface (應用程式介面)
SR
Success Rate (成功率)
MRN
Medical Record Number (病歷號)
LOINC
Logical Observation Identifiers Names and Codes
SNOMED
Systematized Nomenclature of Medicine
NDC
National Drug Code
CPT
Current Procedural Terminology
PHI
Protected Health Information (受保護健康資訊)
CAP
Community-Acquired Pneumonia (社區型肺炎)
QA
Question-Answering (問答)
