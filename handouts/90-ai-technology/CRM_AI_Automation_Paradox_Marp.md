---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: 'Microsoft JhengHei', 'PingFang TC', sans-serif; background-color: #ffffff; color: #2d3436; }
  section.lead { background-color: #1a2740; color: #ffffff; }
  section.lead h1 { color: #ffffff; font-size: 2.0em; }
  section.lead h2 { color: #b0c4de; }
  section.lead h3 { color: #dfe6e9; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #8ec7ff; }
  section.lead blockquote { background-color: #f5f6fa; color: #2d3436; border-left: 4px solid #ba181b; }
  section.lead blockquote strong { color: #ba181b; }
  section.divider { background-color: #0072bc; color: white; display: flex; flex-direction: column; justify-content: center; align-items: center; }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.4em; text-align: center; }
  section.divider h2 { color: #ffe066; text-align: center; }
  section.divider h3 { color: #ffffff; text-align: center; }
  section.divider p, section.divider strong { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.55em; }
  h2 { color: #0072bc; font-size: 1.1em; }
  h3 { color: #555555; }
  table { font-size: 0.68em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote { border-left: 4px solid #ba181b; background-color: #fff5f5; padding: 0.5em 1em; font-size: 0.86em; }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.7em; font-size: 0.58em; line-height: 1.35; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.80em; }
  section.ref { font-size: 0.62em; }
  section.flow pre { font-size: 0.46em; line-height: 1.25; padding: 0.5em; }
footer: '謝慕揚 MD, PhD, FESC | 機組資源管理 CRM — 駕馭 AI 的自動化悖論 | 2026'
---

<!-- _class: lead -->
# 機組資源管理 CRM
## 駕馭 AI 的自動化悖論
### Crew Resource Management — Navigating AI's Automation Paradox

**謝慕揚 MD, PhD, FESC** | 2026-08-25

[N Engl J Med 2026;395(8):731-734 — doi:10.1056/NEJMp2600938](https://doi.org/10.1056/NEJMp2600938)

> **To err is AI.** 出錯是必然的；能不能接住，才是訓練要處理的事。

---

# 一分鐘摘要

**核心主張**：AI 是以**副駕 (copilot)**、而非**自動駕駛 (autopilot)** 的身分進到臨床。

1. **能力越強的 AI 越危險** — 表現越流暢，醫師越傾向外包；一外包，偵測其失誤的技能就開始萎縮。
2. **危害是「人」的危害** — 去技能化的醫師、以及從未習得／習得錯誤的學員，正好最沒能力接住 AI 的流暢陷阱與靜默失誤。
3. **解方是可教、可測的行為** — 航空業的**機組資源管理 (CRM)** 已被驗證可轉譯為醫療訓練架構，可改寫成五項人機協作能力。

> **先驗證再信任 (verify then trust)** —— 培養永遠不完全授權、永遠保有指揮權的**醫師—機長 (clinician-pilot)**。

---

<!-- _class: divider -->
# 第一部分
## 自動化悖論是什麼

---

<!-- _class: flow -->
# 自動化悖論：一個會自我強化的迴圈

```text
                    【同一個提問 Initial Prompt】
                                |
                +---------------+---------------+
                |                               |
        自動化悖論路徑                       CRM 路徑
     反射式提問 Reflexive              深思式提問 Deliberate
                |                               |
       強迫性依賴 Compelled            校準式依賴 Calibrated
                |                               |
   去技能 / 從未習得 / 習得錯誤            升級技能 Upskilling
                |                               |
     推理外包 Offloaded Reasoning       共同推理 Co-reasoning
                |                               |
        盲目信任 Blind Trust           驗證後信任 Verified Trust
                |                               |
                +--------- 輸出 Output ---------+
                                |
                        流暢陷阱 Fluency Trap
                                |
        (陷阱未被察覺)          (情境警覺 → 交叉查核 → 丟棄或採納)
```

**依賴越深 → 對 AI 失誤的脆弱度越高。這是矛盾的正回饋。**

---

# 三個要分開的名詞

| 名詞 | 定義 | 誰最危險 |
|------|------|---------|
| **去技能化 Deskilling** | 曾經會，因長期外包而退化 | 主治醫師、資深臨床醫師 |
| **從未習得 Never-skilling** | 一開始就有 AI，根本沒建立過該能力 | 醫學生、PGY、住院醫師 |
| **習得錯誤 Mis-skilling** | 學到 AI 的錯誤推理模式，並誤以為正確 | 缺乏監督的學員 |

> **Pearl**：討論 AI 對醫學教育的衝擊時，**never-skilling 與 mis-skilling 比 deskilling 更值得擔心** —— 資深醫師至少還有「內在參照點」可對照 AI 的輸出，**學員沒有**。

---

# 流暢陷阱 (Fluency Trap)

**定義**：輸出**讀起來通順、結構完整、語氣有信心**，因此被誤判為正確。

AI 本身的三個限制，在流暢的外殼下特別難被發現：

| 限制 | 說明 | 臨床風險 |
|------|------|---------|
| **虛構 Confabulation** | 憑空生成看似合理的內容 | 不存在的指引、劑量、文獻 |
| **易受錯誤訊息影響** | Susceptibility to misinformation | 錯誤前提被沿用 |
| **迎合傾向 Sycophancy** | 順著使用者的既有假設走 | **強化確認偏誤** |

> 臨床上最致命的組合是**迎合傾向 + 確認偏誤**：你心裡已有診斷，去問 AI，AI 順著你講，你的信心被**錯誤地**強化了。

---

<!-- _class: divider -->
# 第二部分
## 原文案例
### 被 AI「確認」掉的肺栓塞

---

# 案例：61 歲男性，進行性呼吸困難

| 步驟 | 發生了什麼 |
|------|-----------|
| **病人** | 61 歲男性，**進行性呼吸困難 (progressive dyspnea)** 入院 |
| **R2 住院醫師** | 使用 **AI 病歷助手 (AI scribe)**；主要診斷為**急性失代償性心衰竭** |
| **關鍵動作** | 請 AI「**交叉查核**」自己的推理 |
| **AI 回應** | **確認**他的判斷，並提出**指引導向治療**建議 |
| **住院醫師** | 印象深刻 → 接受該計畫 |
| **被漏掉的** | **肋膜性胸痛 (pleuritic chest pain)** —— 他自己**刻意問出來**、**交給 AI 記錄**的 |
| **主治醫師** | 「這會不會是**慢性心衰竭之上疊加的肺栓塞**？」→ 回查病歷 → 接手 |
| **結果** | **CTPA 確認節段性肺栓塞 (segmental PE)** |

---

# 這個案例的四層教訓

| 層次 | 發生了什麼 | 對應 CRM 能力 |
|------|-----------|-------------|
| **1. 資料層** | AI scribe 漏掉關鍵病史 → 是**遺漏 (omission)**，不是幻覺 | 交叉查核 |
| **2. 推理層** | AI **順著**住院醫師的假設走，沒有挑戰它 | 集體決策 |
| **3. 信任層** | 因 AI「確認」而提高信心 —— 但 AI 是在**不完整資料上**確認的 | 情境警覺 |
| **4. 系統層** | 主治醫師救得回來，是因為他**知道 AI 會這樣壞** | 任務管理 |

> **Pearl 1**：**AI 的「確認」不是獨立驗證。** 把資料擷取與推理查核交給同一個系統 = 封閉迴路。
>
> **Pearl 2**：最諷刺的是 —— **住院醫師的臨床技能其實是好的**（他問出了肋膜性胸痛）。失敗在於**外包後不再回頭查核**。技能沒退化，**警覺退化了**。

---

<!-- _class: divider -->
# 第三部分
## 為什麼借用航空的 CRM

---

# CRM：為高風險駕駛艙而生的團隊訓練

**機組資源管理 (crew resource management, CRM)**：維持**協調 (coordination)、警覺 (vigilance)、表現 (performance)** 的團隊訓練策略。

**為什麼特別適合人機協作**：

1. **已被驗證可轉譯到醫療** — 涵蓋 2008–2018、納入 **297 篇**研究的系統性回顧：**以原則為基礎的訓練（CRM、TeamSTEPPS）與模擬訓練，是達成團隊功能改善最有機會的兩類介入**。
2. **它處理的正是「人 vs 高能力自動化系統」** — 航空業在 1980 年代就走過「自動化提升安全、同時製造新脆弱性與錯置信任」這一段。
3. **產出可教、可測的能力項目**，而不是抽象的態度呼籲。

> **To err is AI** —— 出錯必然發生，重點不是消除錯誤，而是**建立能接住錯誤的機組文化**。

---

# 兩個前置能力：沒有這兩項，其餘免談

## [1] 單飛 Flying Solo

> 要能跟 AI 副駕一起警覺地工作，臨床醫師必須**先取得獨立執業所需的知識與技能**。

**一個無法獨立推理走完臨床問題的醫師，手上沒有可用來評判 AI 輸出的內在參照 (internal reference)。**

## [2] 主導權 Asserting Leadership

> **AI 永遠是下屬，臨床醫師永遠在指揮。**

保留對**每一個決策**的當責 (accountability)。AI 建議被採納時，是「**我**決定採納」，不是「AI 說的」。

---

<!-- _class: divider -->
# 第四部分
## 五大 CRM 核心能力

---

# 能力 1：情境警覺 Situational Awareness

**定義**：追蹤現在發生什麼、預期接下來可能發生什麼、辨認**紅旗 (red flags)**。

**臨床翻譯**：即時監測自己的不確定性 —— 察覺自己**跨出了知識領域的認識論邊界**（**"felt uncertainty"**），然後**慢下來**。

| 限制 | 說明 | 後果 |
|------|------|------|
| **依賴領域知識** | 不知道什麼算紅旗，就偵測不到紅旗 | 呼應「單飛」前提 |
| **必須依風險校準** | 監測強度要對應臨床任務風險 | 否則**警覺疲勞 (vigilance fatigue)** |

**該啟動警覺的兩個時機**：① 因任務**不熟悉**而求助 AI 時 ② AI 輸出**感覺哪裡微妙地不對勁**時

> **訓練法（原文明確建議）**：讓學員接受**在不知情下被刻意植入錯誤**的 AI 資訊，然後**測量他們抓到多少**。
> **評量**：評估學員**過度診斷或低估 AI 失誤**的頻率。

---

# 能力 2：溝通 Communication

**定義**：結構化、**閉環 (closed-loop)** 的資訊交換。

> **提示 (prompting) 是一項臨床技能，類似「照會專家」，而不只是技術技能。回應的品質取決於問題怎麼問。**

**對 AI 的三個要求**：① 精準框定提問 ② 預期提示詞如何形塑輸出 ③ 驗證回應真的回答了你想問的

**教學上要學員說清楚三件事**：

| 問題 | 訓練目的 |
|------|---------|
| **我在問什麼** | 迫使問題明確化 |
| **我為什麼問** | 暴露背後的臨床假設 |
| **我要怎麼判斷這個答案** | **預先設定驗證標準**（最關鍵） |

**技巧**：放聲思考 (think-aloud)、結構化覆誦 (structured read-back) —— 直接借自航空與手術室。

---

# 能力 3：任務管理 Task Management

**目標：校準式依賴 (calibrated reliance)** —— 哪些自己留著、哪些交出去、以什麼順序。

| 分類 | 警覺程度 | 臨床例子 |
|------|---------|---------|
| 可低警覺委派 | 最低 | 格式整理、文獻初步搜尋、衛教文字草稿 |
| 需仔細驗證 | 高 | 鑑別診斷生成、藥物交互作用、劑量計算 |
| **不可委派** | — | 最終診斷決定、告知壞消息、知情同意、風險溝通 |

> **核心習慣（原文原句）**
> **「就這個任務、這個工具、這個風險等級而言，此刻適當的依賴程度是什麼？」**
> *"Given this task, this tool, and these stakes, what level of reliance is appropriate right now?"*

---

# 能力 4：交叉查核 Cross-Checking

**定義**：有紀律地拿**獨立證據**驗證 AI 的建議 —— 並辨認**何時「丟棄」才是正確的臨床作為**。

> **要教會學員：決定丟棄 AI 的建議，是一個正當的臨床行為。**
> *Decisions to discard AI advice are legitimate clinical acts.*

**具體訓練**：
- 練習**在依據 AI 輸出行動之前，先找到確證來源 (confirmatory sources)**
- 在督導下演練 **go/no-go 決策**（借自航空的起飛決斷）

**原文點名的研究缺口** —— 缺乏經驗證的評量工具來檢驗學員能否：
① 偵測**虛構** ② 在流暢輸出中辨認**遺漏或謬誤** ③ 做出恰當的**丟棄判斷**

> 有了這些工具，這項能力才會**從默會 (tacit) 變成可測量 (measurable)**。

---

# 能力 5：集體決策 Collective Decision Making

**CRM 的認識論主張**：推理不是腦袋裡的孤立認知行為，而是發生在「世界之中」的**分散式集體歷程**。

**在 AI 情境下 → 臨床共同推理 (co-reasoning)**。AI 可擴增五個環節：資料擷取、問題表徵、假說生成、處置推理、決策後監測。

```text
Step 1: 臨床醫師先「獨立」推理
Step 2: 再去詢問 AI
Step 3: 用 AI 來「精煉、挑戰、擴展」自己的思考
Step 4: 明確比較「醫師推導的推理」vs「AI 推導的推理」
Step 5: 差異之處 = 學員推理歷程的一扇窗 → 自我反思
```

> **Pearl**：這個順序把 AI 從「答案來源」變成「**對照組**」。
> **先想再問** = 一次診斷推理的形成性評量；**先問再想** = 一次錨定偏誤 (anchoring bias)。

---

<!-- _class: divider -->
# 第五部分
## Centaur vs Cyborg
### 兩種協作模式

---

# 半人馬 Centaur vs 賽伯格 Cyborg

| | **半人馬 Centaur** | **賽伯格 Cyborg** |
|---|---|---|
| **整合方式** | 策略性**任務切分**，人機分工明確 | 與 AI **緊密整合**，界線模糊 |
| **對輸出的態度** | **仔細評估** AI 輸出 | 較高程度的流程內建信任 |
| **適用情境** | **高風險或未經驗證** | **已驗證工具 + 低風險任務** |
| **臨床例子** | LLM 生成鑑別診斷後逐項覆核 | 已驗證的 AI-ECG 篩檢、影像自動量測 |

> **原文的預設規則**
> **因為 AI 能力進展的速度快於驗證資料累積的速度，當某個工具在特定任務上的熟練度未知時，臨床醫師應「預設採用 centaur 模式」。**

**白話**：**證據不足時，預設值是分工與覆核，不是整合與信任。**

---

<!-- _class: divider -->
# 第六部分
## 教學設計
### 把隱形互動變成可評量的行為

---

# 一個現實的教育目標

原文很誠實地承認兩件事：

- 教育者**無法控制所有的 AI 使用**
- 也**不能假設 AI 使用都在監督下發生**

**因此更務實的目標是：讓 AI 的使用「相對於特定臨床任務與情境」變得可見、可討論 (visible and discussable)。**

**那個一直存在、卻從沒被正式教過的技能** —— 判斷**何時信任照會醫師、何時質疑建議、何時尋求第二意見**：

- 典型上是**靠觀察學來的**
- **很少被明確教授**
- **幾乎從未被正式評量**

> **把它命名為一項能力，就把隱性行為轉化成有定義的、可教的活動。**

---

# 督導者可以直接觀察的四件事

| 可觀察行為 | 督導者問的問題 |
|-----------|--------------|
| **提示詞如何框定** | 他問清楚了嗎？他預期到這樣問會得到什麼嗎？ |
| **輸出如何被評估** | 他有沒有找獨立來源？他知道哪裡該懷疑嗎？ |
| **go/no-go 判斷是否恰當** | 採納或丟棄的理由講得出來嗎？ |
| **依賴程度的辯護** | 「這任務 × 這工具 × 這風險」他說得出理由嗎？ |

> **雙向收益**：這些是**可遷移的一般性技能**，能同時磨利**督導者自己**的批判性評估能力，不只是學員的。

---

# AI 作為教學副駕 Teaching Copilot

**現實的反對意見**：這整套 CRM 訓練本身就是額外的教學負擔。

**原文回應**：AI 也可以當**教學副駕** —— 納入學員的學習歷程可促進基礎技能發展。

**教育設計要考慮三件事，不只一件**：① **用哪一個 AI** ② **怎麼用** ③ **誰在用、在訓練的哪個階段**

| 對象 | 建議模式 | 理由 |
|------|---------|------|
| **學員／低年資** | **教練模式 (coach-mode)** —— **提示推理但不給答案** | 保住「先獨立推理」的順序 |
| **進階臨床醫師** | CRM 可**保存技能並加速學習** | 已有內在參照，可承受較高整合度 |

> **附帶條件**：負擔只有在 **AI 副駕本身也依同樣原則被訓練**時才會減輕 —— 設計成會**標示不確定性、揭露自身限制、支持（而非競爭）臨床醫師的警覺**。

---

<!-- _class: divider -->
# 第七部分
## 支持這篇 Perspective 的關鍵證據

---

# 自動化偏誤的隨機分派試驗
## Qazi et al., NEJM AI 2026;3(5) — [doi:10.1056/AIoa2501001](https://doi.org/10.1056/AIoa2501001)

| 項目 | 內容 |
|------|------|
| **設計** | 單盲隨機分派臨床試驗（2025-06-20 至 2025-08-15） |
| **對象** | **44 位醫師**，全部完成 **20 小時 AI 素養訓練** |
| **介入** | 1:1 分派診斷 6 個臨床案例；對照組收到 ChatGPT-4o **無誤**建議，試驗組其中 **3 案**收到**刻意植入錯誤**的建議（隨機排序以減少錨定） |
| **主要結果** | 複合式診斷推理正確率（鑑別診斷、支持／反對證據、首選診斷、下一步） |
| **結果** | **84.9% → 73.3%**，校正後下降 **14.0 個百分點** |

> **為什麼重要**：受試者**全部受過 20 小時 AI 素養訓練**。也就是說 —— **知道 AI 會出錯，並不足以讓你在它出錯時抓到它。**
>
> **限制**：單一國家 (巴基斯坦)、樣本小 (n=44)、臨床案例文本而非真實病人、單一模型。方向明確，外推需保留。

---

# 航空類比的完整版
## Ong et al., npj Digit Med 2026;9:201 — [doi:10.1038/s41746-026-02410-1](https://doi.org/10.1038/s41746-026-02410-1)

由**臨床醫師**與**德國漢莎航空飛航安全部門**專家共同撰寫。

**核心主張**（與本文一致）：視角必須從「AI 作為**自動駕駛 autopilot**」轉為「與**數位副駕 digital copilot** 協作」。

**三項具體要求**：

| # | 要求 | 對應本文 |
|---|------|---------|
| 1 | **情境式訓練 (scenario-based training)** | 植入錯誤的模擬教案 |
| 2 | **臨床醫師基準測量 (clinician benchmarking)** | 抓錯率／誤報率的量化 |
| 3 | **最低無輔助執業時數 (minimum unaided practice)** | **直接對應「單飛」前置能力** |

---

<!-- _class: divider -->
# 第八部分
## 在台灣臨床教學現場怎麼落地

---

# 三件明天就能做的事

| # | 動作 | 怎麼做 |
|---|------|-------|
| **1** | **在晨會加一句話** | 學員報 case 時多問一句：「**這段推理裡，哪些是你自己想的、哪些是 AI 給的？**」—— 這一句就達成了「讓 AI 使用可見」 |
| **2** | **先想再問的硬規則** | 查房前要求學員**先寫下自己的鑑別診斷**，再問 AI，然後**兩份並排比較**。差異之處就是當天的教學點 |
| **3** | **正名「丟棄」** | 學員說「AI 說要做 X 但我覺得不對」時，**明確稱讚這個行為**並要求講出理由。要讓「推翻 AI」變成**有面子**的事 |

> 以上為講義整理者依原文架構所做的在地化建議，非原文內容。

---

<!-- _class: small-text -->
# 一個可以直接跑的模擬教案

```text
教案：植入式錯誤的 AI 輔助診斷演練（60 分鐘）

準備：6 個臨床案例的 AI 生成鑑別診斷，其中 3 個植入錯誤（學員不知情）
      錯誤類型建議涵蓋：
        (a) 遺漏型 —— 漏掉一個關鍵病史（如本文案例的肋膜性胸痛）
        (b) 虛構型 —— 引用不存在的指引建議或劑量
        (c) 迎合型 —— 順著學員在提問中透露的假設走

執行：學員逐案作答 → 紀錄「採納 / 修改 / 丟棄」與理由；不提示哪些案例有錯

回饋：1. 揭露錯誤位置
      2. 計算個人「抓到率」與「誤報率」（過度懷疑也要計分）
      3. 針對「明明抓到卻仍採納」的案例深入討論 ← 最有價值的部分
      4. 重點回饋語言：「你的丟棄判斷是正確的臨床行為」

評量：對應「交叉查核」能力，可納入 EPA 或 milestone 觀察紀錄
```

---

# 依科別的風險分層建議

| 情境 | 建議模式 | 理由 |
|------|---------|------|
| AI-ECG 篩檢（已驗證、有前瞻資料） | Cyborg 可接受 | 任務特定熟練度已知 |
| LLM 生成鑑別診斷 | **Centaur（預設）** | 熟練度未知 + 高風險 |
| AI scribe 病歷記錄 | **Centaur（必須逐項核對）** | 本文案例即為遺漏型失誤 |
| 影像自動量測（LVEF、心腔徑） | Cyborg，但需定期抽核 | 已驗證但仍有邊界個案 |
| 導管室即時決策輔助 | **不可委派** | 風險等級最高、時間壓力大 |

> 以上為講義整理者依原文原則所做的在地化分層，非原文內容。

---

<!-- _class: small-text -->
# 常見誤解與反駁

| 誤解 | 原文的回應 |
|------|-----------|
| 「AI 這麼強，基本功可以少學一點」 | **完全相反。** 無法獨立推理的醫師「沒有可評判 AI 輸出的內在參照」。基本功是使用 AI 的**前置條件** |
| 「我知道 AI 會幻覺，所以我會小心」 | 隨機試驗：**20 小時 AI 素養訓練後，遇到植入錯誤仍讓診斷推理掉了 14 個百分點**。知識 ≠ 行為 |
| 「AI 確認了我的判斷，所以更可信」 | 本文案例的核心失誤。AI 只在**它看得到的資料上**確認你 —— 而那份資料可能已被它自己漏掉一半。**確認不是驗證** |
| 「凡事都要查核，那用 AI 幹嘛」 | CRM 要的是**校準式依賴**，不是最大化懷疑。過度警覺會造成**警覺疲勞**，同樣是失效模式 |
| 「這是資訊科的事，臨床教學不用管」 | 原文明確把它放進**醫學教育的潛在課程**，並主張列為可觀察、可評量的能力 |
| 「AI 越進步，這問題會自己消失」 | **能力越強，悖論越深** —— 越流暢的副駕越容易誘發外包 |

---

# 一頁速查表：五大核心能力

| # | 能力 | 一句話 | 可觀察行為 |
|---|------|-------|-----------|
| 1 | **情境警覺** | 監測自己的不確定性，感覺不對就慢下來 | 抓到植入錯誤的比率；過度／低估 AI 失誤 |
| 2 | **溝通** | 提示是臨床技能，不是技術技能 | 說得出「問什麼／為什麼問／怎麼判斷答案」 |
| 3 | **任務管理** | 校準式依賴：留、驗、不可授權 | 說得出「這任務 × 這工具 × 這風險」的理由 |
| 4 | **交叉查核** | 先找確證來源再行動；**丟棄是正當的臨床行為** | go/no-go 決策；偵測虛構、遺漏、謬誤 |
| 5 | **集體決策** | 先獨立推理，再用 AI 精煉、挑戰、擴展 | 醫師推理 vs AI 推理的並排比較 |

**前置能力**：[1] **單飛 Flying Solo** — 先具備獨立執業能力 　[2] **主導權** — AI 永遠是下屬

---

# 分岔點只有一個

```text
反射式提問 → 盲目信任 → 推理外包 → 去技能 → 更依賴   ✗
深思式提問 → 情境警覺 → 交叉查核 → 驗證後信任 → 升級技能  ✓
                          ↑
                  分岔點就在這裡：
              「我有沒有拿獨立證據去對？」
```

> **To err is AI.**
> 出錯是必然的；**能不能接住，才是訓練要處理的事。**

---

<!-- _class: ref -->
# 參考文獻

1. Abdulnour R-EE, Akbarialiabad H, Haghighi A, Leachman SA. Crew Resource Management — Navigating AI's Automation Paradox. [*N Engl J Med*. 2026;395(8):731-734.](https://doi.org/10.1056/NEJMp2600938) (PMID: [42485645](https://pubmed.ncbi.nlm.nih.gov/42485645/))
2. Abdulnour R-EE, Gin B, Boscardin CK. Educational Strategies for Clinical Supervision of Artificial Intelligence Use. [*N Engl J Med*. 2025;393(8):786-797.](https://doi.org/10.1056/NEJMra2503232) (PMID: [40834302](https://pubmed.ncbi.nlm.nih.gov/40834302/))
3. Ong AY, Merle DA, Pollreisz A, et al. Flight rules for clinical AI: lessons from aviation for human-AI collaboration in medicine. [*NPJ Digit Med*. 2026;9(1):201.](https://doi.org/10.1038/s41746-026-02410-1) (PMID: [41620563](https://pubmed.ncbi.nlm.nih.gov/41620563/))
4. Buljac-Samardzic M, Doekhie KD, van Wijngaarden JDH. Interventions to improve team effectiveness within health care: a systematic review of the past decade. [*Hum Resour Health*. 2020;18(1):2.](https://doi.org/10.1186/s12960-019-0411-3) (PMID: [31915007](https://pubmed.ncbi.nlm.nih.gov/31915007/))
5. Sikora A, Celi LA, Abdulnour R-EE. Can AI Say "I Don't Know"? [*N Engl J Med*. 2026;394(19):1873-1875.](https://doi.org/10.1056/NEJMp2517624) (PMID: [42112850](https://pubmed.ncbi.nlm.nih.gov/42112850/))
6. Qazi IA, Ali A, Khawaja AU, Akhtar MJ, Sheikh AZ, Alizai MH. Automation Bias in Large Language Model–Assisted Diagnostic Reasoning among Physicians Trained in AI Literacy — A Randomized Clinical Trial. [*NEJM AI*. 2026;3(5).](https://doi.org/10.1056/AIoa2501001)

文獻書目資料經 PubMed 與 Crossref 查證。講義文獻 2–6 對應原文參考文獻 1–5。

---

<!-- _class: ref -->
# 縮寫對照表

| 縮寫／英文 | 中文 | 說明 |
|-----------|------|------|
| **AI** | 人工智慧 | Artificial Intelligence |
| **CRM** | 機組資源管理 | Crew Resource Management |
| **CTPA** | 電腦斷層肺動脈血管攝影 | Computed Tomographic Pulmonary Angiography |
| **LLM** | 大型語言模型 | Large Language Model |
| **Automation paradox** | 自動化悖論 | AI 越可靠，人越依賴，越依賴則越無力偵測其失誤 |
| **Fluency trap** | 流暢陷阱 | 流暢、自信但不正確的輸出誘發未經驗證的信任 |
| **Silent failure** | 靜默失誤 | 不會自我聲張的錯誤（如遺漏） |
| **Confabulation** | 虛構 | 生成看似合理但無事實依據的內容 |
| **Sycophancy** | 迎合傾向 | 順從使用者既有假設而非挑戰它 |
| **Deskilling / Never-skilling / Mis-skilling** | 去技能／從未習得／習得錯誤 | 三種技能損害型態 |
| **Calibrated reliance** | 校準式依賴 | 知道該信任哪個 AI、信任什麼、何時信任 |
| **Verified trust / Co-reasoning** | 驗證後信任／共同推理 | 先查核再信任；先獨立推理再用 AI 精煉 |
| **Felt uncertainty** | 感受到的不確定 | 察覺已跨出知識領域邊界的後設認知訊號 |
| **Centaur / Cyborg** | 半人馬／賽伯格 | 策略性任務切分 vs 緊密整合 |
| **Go/no-go decision** | 起飛決斷 | 借自航空的二元行動判斷點 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC** | 2026-08-25

[N Engl J Med 2026;395(8):731-734 — doi:10.1056/NEJMp2600938](https://doi.org/10.1056/NEJMp2600938)

> **本講義僅供醫療專業人員教學參考**
