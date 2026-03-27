# lecture Nobel alpha fold

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-03-27**

---

\maketitle


> **《The Thinking Game》**是一部關於 DeepMind 公司追求人工通用智慧（AGI）的紀錄片，以 AlphaFold 解決蛋白質摺疊問題為主軸，展現了 AI 如何從遊戲訓練場進化為解決人類最重大科學問題的工具。本片入選 Tribeca Film Festival，深入呈現 Demis Hassabis 和團隊二十年來的願景與奮鬥。
> **核心成就：**AlphaFold 成功預測了超過 2 億個蛋白質結構，解決了困擾科學界 50 年的蛋白質摺疊問題，為疾病研究、藥物開發開啟全新紀元。


\tableofcontents

---


## Nobel 2024


Demis Hassabis won the 2024 Nobel Prize in Chemistry, sharing it with John M. Jumper for their development of the AI model AlphaFold, which predicts complex protein structures, a breakthrough in understanding the building blocks of life. Their work significantly aids research in medicine and environmental technology. 


    
    [Image]


## DeepMind 的起源與願景


### 創辦人 Demis Hassabis 的背景


| p{10cm}} Demis Hassabis 生平與成就 |  |  |
| --- | --- | --- |
| **階段** | **重要事件** |  |
| **表格續接** |  |  |
| **階段** | **重要事件** |  |
| 童年（4歲） | 首次展現西洋棋天賦 |  |
| 6歲 | 成為倫敦8歲以下組西洋棋冠軍 |  |
| 青少年時期 | 世界同齡排名第二的西洋棋選手 |  |
| 8歲 | 用西洋棋比賽獎金購買第一台電腦 |  |
| 12歲 | 在奧地利國際西洋棋錦標賽中，經歷10小時對局後因疲勞而認輸的關鍵反思：   「我們是否在浪費這些腦力？」 |  |
| 16歲 | 贏得 Bullfrog Productions 程式設計比賽，加入該公司 |  |
| Gap Year | 在 Bullfrog 開發《Theme Park》遊戲，設計 AI 行為系統 |  |
| 17歲 | 拒絕 Peter Molyneux 100萬英鎊的挽留，前往劍橋大學 |  |
| 劍橋時期 | 主修電腦科學，對神經科學與蛋白質摺疊問題產生興趣 |  |
| 博士研究 | 進入 UCL 研究神經科學，為 AI 研究尋找靈感 |  |


### DeepMind 的創立


> **創立時間：**2010年
> **共同創辦人：**
> itemize
>     \item Demis Hassabis（執行長）
>     \item Shane Legg（首席科學家）
> itemize
> **核心使命：**建立世界上第一個通用學習機器（General Learning Machine），最終實現人工通用智慧（AGI）
> **創辦理念：**
> itemize
>     \item 在學術界，「AI」幾乎是令人尷尬的詞彙
>     \item 如果說你在研究 AI，別人會認為你不是認真的科學家
>     \item Hassabis 認為：「Shane 和我像是守護著一個無人知曉的秘密」
> itemize


### 早期融資困境


| p{10cm}} DeepMind 早期融資挑戰 |  |  |
| --- | --- | --- |
| **挑戰** | **描述** |  |
| **表格續接** |  |  |
| **挑戰** | **描述** |  |
| 投資人疑慮 | 「我們要解決所有智慧問題」——這種說法讓投資人側目 |  |
| 典型反應 | 「你講了這麼多偉大願景，但你們的產品是什麼？怎麼賺錢？」 |  |
| 類比困境 | 就像買彩票一樣：巨額資金、巨大風險、大量運算需求 |  |
| 策略轉變 | 需要找不是為了最佳投資決策，而是單純覺得「這很酷」的投資人 |  |
| 突破口 | Peter Thiel（PayPal、Facebook 早期投資人）成為首位重要投資人 |  |
| 地點爭議 | Thiel 堅持要求搬到矽谷，但 Hassabis 堅持留在倫敦   ——認為矽谷「快速行動、打破常規」的文化不適合長期研究 |  |


### 秘密運營時期


DeepMind 成立初期處於完全隱密模式：

- 沒有公開網站
- 辦公室位於秘密地點
- 員工不能透露工作內容或地點
- 面試者曾開玩笑說：「我已經告訴妻子我的確切位置，以防這是詐騙集團」


## 從遊戲到 AGI 的道路


### Atari 遊戲與深度強化學習


> **核心創新：**將深度學習與強化學習結合
> **訓練方式：**
> itemize
>     \item 給 AI 代理（agent）遊戲卡帶
>     \item 只提供像素畫面和分數
>     \item AI 必須自己學會遊戲規則和策略
> itemize
> **Pong 遊戲的轉折：**
> itemize
>     \item 初期完全無法運作，團隊一度想放棄
>     \item 「也許我們根本就錯了，連 Pong 都做不到」
>     \item 突然間，AI 得到了第一分
>     \item 三個月後，沒有人類能打敗它
> itemize
> **Breakout 遊戲的驚喜：**
> itemize
>     \item 300 局後達到人類水平
>     \item 500 局後發現最優策略：挖隧道繞到牆後面
>     \item 這個策略連程式設計師都沒想到
> itemize


### Google 收購


| p{10cm}} Google 收購 DeepMind |  |  |
| --- | --- | --- |
| **項目** | **內容** |  |
| **表格續接** |  |  |
| **項目** | **內容** |  |
| 收購時間 | 2014年 |  |
| 收購金額 | 報導約 4 億英鎊（約 6.5 億美元） |  |
| 收購原因 | 需要大規模運算能力加速 AGI 研發時程 |  |
| 關鍵考量 | 商業公司是否會理解研究的重要性？   是否會給予足夠時間讓研究開花結果？ |  |
| 決策邏輯 | 「沒有時間可以浪費，還有太多問題需要解決」   「大腦還在運轉時，就要完成這些事情」 |  |
| 獨立性保障 | DeepMind 獲准在倫敦獨立運營，建立自己的文化   專注於純研究而非產品開發 |  |
| 軍事限制 | 獲得 Google 承諾：DeepMind 技術不會用於軍事用途 |  |


### AlphaGo：圍棋之戰


| p{11cm}} AlphaGo 發展歷程 |  |  |
| --- | --- | --- |
| **階段** | **重要事件** |  |
| **表格續接** |  |  |
| **階段** | **重要事件** |  |
| 圍棋挑戰 | 圍棋被視為 AI 的「聖杯」   棋盤配置數量超過宇宙中的原子數   傳統 AI 方法完全失敗 |  |
| 訓練方法 | 先用 10 萬局人類專家對局訓練   再透過強化學習，與自己對弈數百萬局 |  |
| 李世石對戰 | 2016年3月，首爾   五局三勝，AlphaGo 最終 4:1 獲勝 |  |
| 第37手 | 專業評論員一致認為沒有人類會下這步棋    AlphaGo 自己估計人類下這步的機率：萬分之一   圍棋研究數千年，AlphaGo 發現了全新策略 |  |
| 中國反應 | 比賽期間，中國政府下令切斷直播訊號   這成為中國的「Sputnik 時刻」   啟動了 AI 競賽 |  |
| 柯潔對戰 | 2017年，對戰世界排名第一的柯潔    AlphaGo 完勝 |  |


### Alpha Zero：從零開始


> **核心創新：**完全移除人類知識，從零開始學習
> **「Zero」的意義：**
> itemize
>     \item 零人類知識輸入
>     \item 只知道遊戲規則
>     \item 透過自我對弈學習
>     \item 成為自己的老師
> itemize
> **訓練速度：**
> itemize
>     \item 早上開始，完全隨機下棋
>     \item 下午茶時間，達到超人類水平
>     \item 晚餐時，成為史上最強西洋棋程式
> itemize
> **通用性：**同一系統可以玩圍棋、西洋棋、日本將棋等任何完美信息雙人遊戲


### AlphaStar：星海爭霸


| p{10cm}} AlphaStar 挑戰 |  |  |
| --- | --- | --- |
| **特點** | **說明** |  |
| **表格續接** |  |  |
| **特點** | **說明** |  |
| 遊戲複雜度 | 即時決策（非回合制）   無法看到對手行動（不完美信息）   需要同時管理數千個單位 |  |
| 訓練方法 | 借鑒大型語言模型的「預測下一步」方法   學習「給定這個畫面，人類會怎麼做？」 |  |
| 倫理考量 | 遊戲是戰爭模擬   需要警惕 AI 技術的軍事應用潛力 |  |
| 公開展示 | 與職業玩家 MaNa 進行直播對決    MaNa 最終獲勝，但 AlphaStar 展現了職業級水準 |  |


## 蛋白質摺疊問題


### 問題背景


> **什麼是蛋白質？**
> itemize
>     \item 生命的機器（The machines of life）
>     \item 構建一切、控制一切
>     \item 是生物學運作的原因
> itemize
> **蛋白質摺疊問題：**
> itemize
>     \item 蛋白質由胺基酸序列組成
>     \item 胺基酸序列決定蛋白質的 3D 結構
>     \item 3D 結構決定蛋白質的功能
>     \item 問題：能否從序列預測結構？
> itemize
> **潛在應用：**
> itemize
>     \item 癌症治療
>     \item 阿茲海默症研究
>     \item 藥物研發
>     \item 環境保護（分解塑膠的蛋白質）
> itemize
> **歷史困境：**
> itemize
>     \item 1960年代就提出這個問題
>     \item 50多年來無人解決
>     \item 實驗方法需要數月甚至數年才能確定單一蛋白質結構
>     \item 有些結構永遠無法用實驗確定
> itemize


### 劍橋的種子


Hassabis 在劍橋大學時期首次接觸蛋白質摺疊問題：

quote
「我的朋友 Tim Stevens 幾乎像傳教士一樣談論蛋白質摺疊問題。我當時就想：人類聰明到能摺疊蛋白質嗎？這個問題一直留在我腦海中，我覺得它是可以解決的——但需要 AI 來做。」
quote


### AlphaFold 的誕生


| p{10cm}} AlphaFold 發展時間線 |  |  |
| --- | --- | --- |
| **階段** | **重要事件** |  |
| **表格續接** |  |  |
| **階段** | **重要事件** |  |
| 項目啟動 | 遊戲只是 AI 的訓練場   真正目標是解決真實世界的挑戰 |  |
| Foldit 遊戲 | 團隊嘗試玩蛋白質摺疊遊戲   表現不錯，但即使是世界最強玩家也無法解決問題 |  |
| 初期挑戰 | 數據稀缺：僅有半世紀累積的實驗數據   無法像遊戲一樣無限生成訓練數據 |  |
| 團隊組建 | John Jumper 成為團隊負責人   招募計算生物學家加入 |  |


## CASP 競賽


### 什麼是 CASP


> **性質：**蛋白質摺疊的「奧運會」
> **舉辦頻率：**每兩年一次
> **比賽方式：**
> enumerate
>     \item 主辦方提供約 100 個蛋白質的胺基酸序列
>     \item 這些蛋白質的結構已由實驗確定，但尚未公開
>     \item 參賽團隊用計算方法預測結構
>     \item 預測結果與實驗結構比對評分
> enumerate
> **評分標準：**
> itemize
>     \item GDT 分數衡量預測準確度
>     \item 分數超過 90 被認為是「解決」蛋白質摺疊問題的門檻
> itemize


### CASP13（2018年）


| p{10cm}} CASP13 結果 |  |  |
| --- | --- | --- |
| **項目** | **結果** |  |
| **表格續接** |  |  |
| **項目** | **結果** |  |
| DeepMind 表現 | 在最困難類別的 43 個蛋白質中，25 個預測最準確   領先第二名近 50 |  |
| Hassabis 評價 | 「我們是最先進的，但離解決蛋白質摺疊問題還很遠」 |  |
| 生物學家反應 | 「預測品質參差不齊，並不比之前的方法更實用」 |  |
| 團隊反思 | 「我們是世界上最不擅長解決某個問題的團隊中最好的」   「我們知道自己還很差」   「梯子再高也到不了月球」 |  |


### 重新出發


CASP13 後的關鍵轉變：


- 認識到「把最好的演算法丟上去」是天真的想法
- 需要融入領域知識
- 組建「突擊隊」（Stripe Team），由 John Jumper 領導
- 招募計算生物學家，填補生物學知識空白
- 完全重寫數據處理管線


quote
「你無法強迫創意階段，必須給那些花朵綻放的空間。」——Hassabis
quote


### CASP14（2020年）——歷史性突破


| p{10cm}} CASP14 的突破 |  |  |
| --- | --- | --- |
| **項目** | **內容** |  |
| **表格續接** |  |  |
| **項目** | **內容** |  |
| 時代背景 | 2020年 COVID-19 疫情   團隊在家工作   「我在一個房間試圖解決蛋白質摺疊   我丈夫在另一個房間試圖讓機器人走路」 |  |
| 新冠挑戰 | SARS-CoV-2 的 ORF8 蛋白是最困難的目標之一   團隊投入最多時間嘗試改進預測 |  |
| 技術進步 | 從需要 1-2 天摺疊一個蛋白質   進步到每秒摺疊數百甚至數千個 |  |
| John Moult 信件 | CASP 創辦人 John Moult 寫信：   「你們的團隊在 CASP14 表現驚人   無論是相對其他團隊還是絕對準確度   恭喜，這真的非常傑出」 |  |
| 歷史宣告 | 「經過半個世紀，我們終於有了蛋白質摺疊問題的解決方案」 |  |


## 開放與影響


### 開放決策


> **關鍵對話：**
> 研究人員不斷詢問：「我有一個與瘧疾/傳染病相關的蛋白質，我們不知道結構，能用 AlphaFold 解決嗎？」
> 團隊討論：
> itemize
>     \item 「我們可以在一個月內輕鬆預測所有已知序列」
>     \item 「10億、20億個蛋白質都沒問題」
>     \item 「為什麼我們要做一個服務讓人們提交蛋白質？」
>     \item 「我們應該直接摺疊所有東西，然後送給全世界」
> itemize
> **Hassabis 的決定：**「當然這就是我們應該做的！為什麼之前沒人提議？」


### AlphaFold 資料庫


| p{10cm}} AlphaFold 資料庫發布 |  |  |
| --- | --- | --- |
| **項目** | **內容** |  |
| **表格續接** |  |  |
| **項目** | **內容** |  |
| 發布內容 | 2 億個蛋白質結構預測 |  |
| 開放方式 | 完全免費、開放程式碼 |  |
| 合作夥伴 | 與 EMBL-EBI（歐洲分子生物學實驗室）合作 |  |
| 即時反響 | 發布當天：   「日本有大量活動」   「655 個用戶」   「10 萬用戶」   「這太瘋狂了」 |  |
| 科學家反應 | 「就像拉開窗簾，看到整個蛋白質結構的世界」   「這些是給人類的禮物」 |  |
| 長期影響 | 「我猜測，未來每一個生物學和化學成就   都會以某種方式與 AlphaFold 相關」 |  |


### 歷史意義


quote
「AlphaFold 是一個里程碑時刻。這是人們不會忘記的時刻，因為世界改變了。」
quote

quote
「AlphaFold 釋放給世界的那一刻，我們就不再是 AlphaFold 故事中最重要的人了。」
quote


## AGI 與未來展望


### AGI 的定義與追求


| p{10cm}} 人工通用智慧（AGI）的特徵 |  |  |
| --- | --- | --- |
| **特徵** | **說明** |  |
| **表格續接** |  |  |
| **特徵** | **說明** |  |
| 通用性 | 能夠執行任何認知任務，而非僅限於特定領域 |  |
| 學習能力 | 能夠學習做許多不同的事情，就像人類一樣 |  |
| 新穎問題 | 能夠解決從未見過的新問題 |  |
| 認知靈活性 | 具備人類般的認知廣度和適應性 |  |
| 超越人類 | 有潛力遠超人類能力 |  |


### 深度思考：責任與風險


| p{10cm}} AGI 的機遇與挑戰 |  |  |
| --- | --- | --- |
| **面向** | **內容** |  |
| **表格續接** |  |  |
| **面向** | **內容** |  |
| 比較歷史 | 比網際網路更重大   比行動通訊更重大   更像是電力或火的發明 |  |
| 曼哈頓計畫比喻 | DeepMind 與曼哈頓計畫有相似之處    Oppenheimer 和 Hassabis 都在釋放新力量    教訓：Oppenheimer 沒有足夠早地思考道德問題 |  |
| 外星文明比喻 | 「如果收到郵件說高等外星文明即將到達地球   所有政府會召開緊急會議    AGI 的到來將是人類面臨的最重要時刻」 |  |
| 風險擔憂 | 軍事應用（自主武器）   虛假信息   心理操控   社會失業   「如何永遠控制比你更強大的東西？」 |  |
| 發展態度 | 反對「快速行動、打破常規」   主張「你無法先打破再修復」   需要用科學方法，嚴謹地理解每一步 |  |
| 全球協調 | 需要全球協調，但擔憂人類在這方面越來越差而非越來越好 |  |


### Hassabis 的終身使命


> **人生目標：**
> quote
> 「我一生的目標是解決人工通用智慧。在這個過程中，用 AI 作為終極工具，解決世界上最複雜的科學問題。」
> quote
> **時間緊迫感：**
> quote
> 「如果你真的認真對待這件事，就沒有太多時間。生命很短暫。」
> quote
> **對 AGI 的態度：**
> quote
> 「人們常問我：如果你錯了，AGI 還很遠怎麼辦？我從不擔心這個。我實際上擔心的是相反的情況——它來得比我們能準備的更快。」
> quote
> **當下的判斷：**
> quote
> 「AGI 已經在地平線上了。非常明確，下一代將生活在因 AI 而徹底不同的未來世界。」
> quote


## 關鍵人物


| p{10cm}} 紀錄片主要人物 |  |  |
| --- | --- | --- |
| **人物** | **角色與貢獻** |  |
| **表格續接** |  |  |
| **人物** | **角色與貢獻** |  |
| Demis Hassabis | DeepMind 共同創辦人兼執行長   童年西洋棋神童   遊戲設計師出身   2024年諾貝爾化學獎得主（因 AlphaFold） |  |
| Shane Legg | DeepMind 共同創辦人兼首席科學家   與 Hassabis 在 UCL 相遇   共同堅信 AGI 的可能性 |  |
| John Jumper | AlphaFold 團隊負責人   帶領團隊實現 CASP14 突破   2024年諾貝爾化學獎共同得主 |  |
| Peter Thiel | 首位重要投資人    PayPal、Facebook 早期投資人   以逆向思維著稱 |  |
| Peter Molyneux | Bullfrog Productions 創辦人    Hassabis 的早期導師   曾出價 100 萬英鎊挽留 Hassabis |  |
| John Moult | CASP 創辦人   宣布 AlphaFold 解決蛋白質摺疊問題 |  |
| 李世石 | 韓國圍棋傳奇   2016年與 AlphaGo 對戰   被稱為「圍棋界的費德勒」 |  |
| 柯潔 | 中國圍棋世界排名第一   2017年對戰 AlphaGo |  |


## 重要引言


### 關於 AI 的本質


quote
「建構 AGI 是人類有史以來踏上的最令人興奮的旅程。」——Demis Hassabis
quote

quote
「人腦是我們擁有的唯一存在證明——或許是整個宇宙中——通用智慧是可能的。」——Demis Hassabis
quote

quote
「Shane 和我 20 多年來一直知道的事情，現在所有人都意識到了：AI 將是人類發明的最重要的東西。」——Demis Hassabis
quote


### 關於科學研究


quote
「如果你想做生物學研究，你必須準備好失敗，因為生物學非常複雜。我經營實驗室近 50 年，有一半時間我只是個業餘心理醫生，在什麼都不行的時候讓同事保持開心。大約 80-90
quote

quote
「教訓是：野心是好事，但時機要對。提前時代 50 年沒有意義——你無法在這樣的事業中生存 50 年才產生成果。你會死於嘗試。」——Demis Hassabis
quote


### 關於責任


quote
「技術本身是中性的。我們作為社會、人類、公司、政府如何決定使用它，才決定事情是好是壞。」——Demis Hassabis
quote

quote
「這是人類歷史的十字路口。AI 有潛力在每個方面改變我們的生活。駕馭這項技術可能超越我們所知的一切。」——紀錄片旁白
quote


## 紀錄片資訊


| p{10cm}} 紀錄片基本資訊 |  |  |
| --- | --- | --- |
| **項目** | **內容** |  |
| **表格續接** |  |  |
| **項目** | **內容** |  |
| 片名 | The Thinking Game（思考的遊戲） |  |
| 類型 | 紀錄片 |  |
| 入選影展 | Tribeca Film Festival 官方入選 |  |
| 主題 | DeepMind 的創立與發展   從遊戲 AI 到 AlphaFold 的歷程    AGI 的追求與倫理思考 |  |
| 時長 | 約 80 分鐘 |  |


## 詞彙表


| p{9cm}} 關鍵術語解釋 |  |  |
| --- | --- | --- |
| **術語** | **解釋** |  |
| **表格續接** |  |  |
| **術語** | **解釋** |  |
| AGI (Artificial General Intelligence) | 人工通用智慧。能夠執行任何人類智力任務的 AI 系統，具備跨領域學習和推理能力 |  |
| DeepMind | Google 旗下的 AI 研究公司，總部位於倫敦，由 Demis Hassabis 創立 |  |
| AlphaGo | DeepMind 開發的圍棋 AI，2016年擊敗世界冠軍李世石 |  |
| AlphaFold | DeepMind 開發的蛋白質結構預測系統，解決了 50 年來的蛋白質摺疊問題 |  |
| Alpha Zero | 從零開始學習的通用遊戲 AI，無需人類知識即可達到超人類水平 |  |
| Reinforcement Learning | 強化學習。AI 透過與環境互動、獲得獎勵來學習的方法 |  |
| Deep Learning | 深度學習。使用多層神經網路進行機器學習的技術 |  |
| CASP | Critical Assessment of protein Structure Prediction，蛋白質結構預測的國際競賽 |  |
| Protein Folding | 蛋白質摺疊。蛋白質從胺基酸序列形成 3D 結構的過程 |  |
| GDT Score | 衡量蛋白質結構預測準確度的評分標準 |  |
| Sputnik Moment | 史普尼克時刻。指引發重大科技競賽的轉折點，源自1957年蘇聯發射第一顆人造衛星 |  |


## 延伸閱讀


1. Jumper J, Evans R, Pritzel A, et al. Highly accurate protein structure prediction with AlphaFold. [*Nature](https://doi.org/10.1038/s41586-021-03819-2). 2021;596(7873):583-589.*
2. Senior AW, Evans R, Jumper J, et al. Improved protein structure prediction using potentials from deep learning. [*Nature](https://doi.org/10.1038/s41586-019-1923-7). 2020;577(7792):706-710.*
3. Silver D, Huang A, Maddison CJ, et al. Mastering the game of Go with deep neural networks and tree search. [*Nature](https://doi.org/10.1038/nature16961). 2016;529(7587):484-489.*
4. Silver D, Schrittwieser J, Simonyan K, et al. Mastering the game of Go without human knowledge. [*Nature](https://doi.org/10.1038/nature24270). 2017;550(7676):354-359.*
5. Mnih V, Kavukcuoglu K, Silver D, et al. Human-level control through deep reinforcement learning. [*Nature](https://doi.org/10.1038/nature14236). 2015;518(7540):529-533.*
6. Varadi M, Anyango S, Deshpande M, et al. AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models. [*Nucleic Acids Res](https://doi.org/10.1093/nar/gkab1061). 2022;50(D1):D419-D426.*


> **關鍵詞：**人工智慧、深度學習、強化學習、蛋白質摺疊、AlphaFold、AlphaGo、DeepMind、AGI、CASP、Demis Hassabis