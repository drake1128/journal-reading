# tutorial how to make journal reading summary

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-03-27**

---

\maketitle


> 本文件旨在教導心血管團隊同仁如何運用 Claude Project 平台，結合預設的 LaTeX 模板與指令，將心血管領域的重要期刊文獻快速整理成結構化的繁體中文教學講義。透過此工作流程，可大幅提升文獻整理效率，並確保輸出格式的一致性與專業性。


\tableofcontents

---


## 前言：為什麼使用 Claude Project？


### 傳統文獻整理的挑戰


在日常臨床與教學工作中，我們經常需要閱讀並整理最新的心血管期刊文獻。傳統方式存在以下挑戰：


| p{10cm}}  **挑戰** | **說明** |  |
| --- | --- | --- |
| **挑戰** | **說明** |  |
| 時間成本高 | 閱讀原文、翻譯、整理格式需耗費大量時間 |  |
| 格式不一致 | 不同人員整理的講義風格差異大，難以建立標準化教材庫 |  |
| 術語翻譯困難 | 醫學專有名詞的中英對照需要專業知識 |  |
| 圖表製作繁瑣 | 將論文中的數據轉換為清晰的表格需要額外努力 |  |
| 更新維護困難 | 當有新文獻發表時，需要重新從頭整理 |  |


### Claude Project 的優勢


Claude Project 是 Anthropic 公司推出的專案管理功能，允許使用者建立具有特定指令（Instructions）和參考檔案的工作環境。


| p{10cm}}  **功能** | **效益** |  |
| --- | --- | --- |
| **功能** | **效益** |  |
| Project Instructions | 預設的系統指令確保每次輸出都遵循相同的格式規範 |  |
| Knowledge Files | 上傳的參考檔案（如 LaTeX preamble）作為範本 |  |
| 對話記憶 | 在同一專案中的對話可累積上下文 |  |
| 一致性輸出 | 所有講義都採用相同的排版風格與術語規範 |  |
| 快速迭代 | 可即時修正並重新生成內容 |  |


## Cardiology Journal Reading 專案架構


### 專案概述


「Cardiology Journal Reading」是一個專門用於整理心血管期刊文獻的 Claude Project，其核心設計理念如下：


> enumerate[leftmargin=*]
>     \item **標準化輸出**：所有講義採用統一的 LaTeX 模板
>     \item **雙語並陳**：繁體中文為主，保留英文醫學術語
>     \item **結構化內容**：使用 longtable 呈現數據，tcolorbox 強調重點
>     \item **可追溯引用**：所有文獻都附上 DOI 超連結
> enumerate


### 專案組成元件


| p{6cm}p{5cm}}  **元件** | **檔案名稱** | **功能說明** |
| --- | --- | --- |
| **元件** | **檔案名稱** | **功能說明** |
| LaTeX Preamble | Drake\_preamble.tex | 定義文件的套件載入、字體設定、顏色定義、版面配置等基礎設定 |
| 範例講義 | journal\_reading\_TEER\_2025-09.tex | 提供完整的講義範例，展示表格、章節、引用的標準格式 |
| 範例講義 | Nature\_2025\_obesity\_paradox.tex | 另一份範例，展示 tcolorbox 和詞彙表的使用方式 |
| Project Instructions | （內建於專案設定） | 指導 Claude 如何處理輸入並生成符合規範的輸出 |


### Project Instructions 內容解析


Project Instructions 是 Claude Project 的核心，它告訴 Claude 應該如何處理使用者的請求。以下是本專案 Instructions 的關鍵內容：

lstlisting[language=TeX,caption=Project Instructions 重點摘要]


, 不能直接用  


lstlisting

這些指令確保了：（1）表格格式正確編譯；（2）醫學術語保持專業性；（3）輸出具有一致的作者署名。


## 操作流程詳解


### 步驟一：存取 Claude Project


| p{13cm}}  **步驟** | **操作說明** |  |
| --- | --- | --- |
| **步驟** | **操作說明** |  |
| 1 | 開啟瀏覽器，前往 [https://claude.ai](https://claude.ai) |  |
| 2 | 使用您的帳號登入（需要 Claude Pro 或 Team 訂閱） |  |
| 3 | 在左側選單中找到「Projects」區塊 |  |
| 4 | 點選「Cardiology Journal Reading」專案進入 |  |
| 5 | 確認右上角顯示正確的專案名稱 |  |


### 步驟二：上傳期刊 PDF


當您要整理一篇新的期刊文獻時：


| p{13cm}}  **步驟** | **操作說明** |  |
| --- | --- | --- |
| **步驟** | **操作說明** |  |
| 1 | 在對話輸入框旁邊找到附件圖示（迴紋針符號） |  |
| 2 | 點擊後選擇「Upload file」 |  |
| 3 | 從電腦中選取要整理的期刊 PDF 檔案 |  |
| 4 | 等待檔案上傳完成（會顯示檔案名稱） |  |


importantbox
**檔案建議：**

- 優先使用期刊官方 PDF（非掃描版）
- 檔案大小建議不超過 20MB
- 確保 PDF 中的文字可被選取（非圖片格式）
- 來源期刊建議：JACC、Circulation、EuroIntervention、NEJM、European Heart Journal


importantbox


### 步驟三：發送整理指令


上傳 PDF 後，在對話框中輸入簡潔的指令：


> `請整理`
> 或更詳細的指令：
> `請依據過去期刊講義整理，整理成為繁體中文 latex code，請依照 tex 範例進行字體、樣式、格式，請多多使用 longtable 及 \textbackslash href\{\`}


Claude 會自動：

1. 讀取專案中的 Instructions 和參考檔案
2. 解析上傳的 PDF 內容
3. 按照預設格式生成 LaTeX 程式碼


### 步驟四：複製 LaTeX 程式碼


Claude 生成的輸出會是完整的 LaTeX 程式碼，您需要：


| p{13cm}}  **步驟** | **操作說明** |  |
| --- | --- | --- |
| **步驟** | **操作說明** |  |
| 1 | 檢視 Claude 輸出的 LaTeX 程式碼 |  |
| 2 | 點擊程式碼區塊右上角的「Copy」按鈕 |  |
| 3 | 或手動選取全部程式碼後按 Ctrl+C（Mac: Cmd+C） |  |


## 使用 Overleaf 編譯文件


### Overleaf 簡介


[Overleaf](https://www.overleaf.com) 是一個線上 LaTeX 編輯器，具有以下優點：


| p{10cm}}  **特點** | **說明** |  |
| --- | --- | --- |
| **特點** | **說明** |  |
| 無需安裝 | 完全在瀏覽器中運作，無需本地安裝 LaTeX 發行版 |  |
| 即時預覽 | 編輯後可立即看到 PDF 輸出結果 |  |
| 協作功能 | 可與團隊成員共同編輯同一份文件 |  |
| 版本控制 | 自動保存歷史版本，可隨時回溯 |  |
| 雲端儲存 | 文件儲存在雲端，可隨處存取 |  |


### 建立新專案


| p{13cm}}  **步驟** | **操作說明** |  |
| --- | --- | --- |
| **步驟** | **操作說明** |  |
| 1 | 前往 [https://www.overleaf.com](https://www.overleaf.com) 並登入帳號 |  |
| 2 | 點擊左上角綠色的「New Project」按鈕 |  |
| 3 | 選擇「Blank Project」 |  |
| 4 | 輸入專案名稱（例如：TEER\_2025\_講義） |  |
| 5 | 點擊「Create」建立專案 |  |


### 設定編譯器為 XeLaTeX


importantbox
**關鍵步驟！**由於我們的講義使用中文字體（Noto Serif CJK TC），必須使用 XeLaTeX 編譯器才能正確顯示中文。預設的 pdfLaTeX 無法處理 xeCJK 套件。
importantbox


| p{13cm}}  **步驟** | **操作說明** |  |
| --- | --- | --- |
| **步驟** | **操作說明** |  |
| 1 | 在 Overleaf 專案頁面，點擊左上角的「Menu」按鈕 |  |
| 2 | 在下拉選單中找到「Settings」區塊 |  |
| 3 | 找到「Compiler」選項 |  |
| 4 | 將編譯器從「pdfLaTeX」改為「XeLaTeX」 |  |
| 5 | 選單會自動儲存設定 |  |


### 貼上並編譯程式碼


| p{13cm}}  **步驟** | **操作說明** |  |
| --- | --- | --- |
| **步驟** | **操作說明** |  |
| 1 | 在左側編輯區，選取並刪除預設的範例程式碼 |  |
| 2 | 按 Ctrl+V（Mac: Cmd+V）貼上從 Claude 複製的 LaTeX 程式碼 |  |
| 3 | 點擊右上角綠色的「Recompile」按鈕 |  |
| 4 | 等待編譯完成（約 10-30 秒） |  |
| 5 | 在右側預覽區檢視生成的 PDF |  |


### 常見編譯錯誤與解決方案


| p{9cm}}  **錯誤訊息** | **解決方案** |  |
| --- | --- | --- |
| **錯誤訊息** | **解決方案** |  |
| `Font not found` | 確認已設定 XeLaTeX 編譯器；Overleaf 已內建 Noto 字體 |  |
| `Undefined control sequence` | 檢查是否遺漏套件載入，或有拼寫錯誤 |  |
| `Missing $ inserted` | 數學符號（如百分比、上下標）需包在 $ 符號內 |  |
| 表格無法正確顯示 | 檢查 longtable 環境前後是否有空行 |  |
| 中文顯示為方框 | 確認使用 XeLaTeX 而非 pdfLaTeX |  |
| 超連結無法點擊 | 確認 hyperref 套件已載入，且 DOI 格式正確 |  |


## 輸出格式規範詳解


### 文件結構


標準的期刊講義應包含以下章節：


| p{10cm}}  **章節** | **內容說明** |  |
| --- | --- | --- |
| **章節** | **內容說明** |  |
| 標題頁 | 論文標題（中英對照）、作者資訊、整理日期 |  |
| 概述/摘要框 | 使用 tcolorbox 呈現核心發現 |  |
| 研究背景 | 為何進行此研究、臨床問題為何 |  |
| 研究方法 | 設計、納入排除條件、主要終點 |  |
| 主要結果 | 使用 longtable 呈現關鍵數據 |  |
| 次要結果/亞組分析 | 額外的分析結果 |  |
| 討論/臨床意義 | 結果的解讀與臨床應用 |  |
| 研究限制 | 方法學與適用性限制 |  |
| 結論 | 主要結論與實務建議 |  |
| 詞彙表（選用） | 重要專有名詞解釋 |  |
| 參考文獻 | 原始論文及相關文獻的 DOI 連結 |  |


### 表格格式規範


> enumerate[leftmargin=*]
>     \item **不使用垂直線**：表格不加入 `|` 分隔線，使用 booktabs 的 `\textbackslash toprule`、`\textbackslash midrule`、`\textbackslash bottomrule`
>     \item **儲存格內換行**：使用 `\textbackslash newline` 而非 `\textbackslash\textbackslash`
>     \item **跨頁處理**：正確設定 `\textbackslash endfirsthead`、`\textbackslash endhead`、`\textbackslash endfoot`
>     \item **欄位寬度**：使用 `p\{寬度\`} 指定欄位寬度以控制換行
> enumerate


### 術語處理原則


| p{10cm}}  **類別** | **處理方式** |  |
| --- | --- | --- |
| **類別** | **處理方式** |  |
| 藥物名稱 | 保持英文原名，例如：Aspirin、Clopidogrel、Evolocumab |  |
| 檢驗項目 | 保持英文縮寫，例如：LDL、HDL、HbA1c、BNP |  |
| 檢查名稱 | 保持英文，例如：Echocardiography、Coronary angiography |  |
| 解剖結構 | 可中譯但附英文，例如：左心室 (Left ventricle, LV) |  |
| 臨床術語 | 首次出現時中英並列，後續可僅用縮寫 |  |
| 統計術語 | 保持英文，例如：HR、CI、p-value、OR |  |


### 參考文獻格式


所有引用應遵循以下 Vancouver 格式，並附上可點擊的 DOI 連結：

lstlisting[language=TeX,caption=參考文獻格式範例]
\item Goldstein BA, Arce CM, Hlatky MA, et al. Trends in 
the incidence of atrial fibrillation in older patients 
initiating dialysis in the United States. 
https://doi.org/10.1161/CIRCULATIONAHA.112.099606
{*Circulation*. 2012;126(19):2293-2301.}
lstlisting


## 進階技巧


### 批次處理多篇文獻


當需要在同一份講義中整理多篇相關文獻時：


| p{13cm}}  **步驟** | **操作說明** |  |
| --- | --- | --- |
| **步驟** | **操作說明** |  |
| 1 | 一次上傳多個 PDF 檔案 |  |
| 2 | 指定整理順序，例如：「請依序整理這三篇關於 TEER 的論文」 |  |
| 3 | Claude 會生成包含多篇文獻的整合講義 |  |
| 4 | 可要求 Claude 在最後加入「文獻比較表」彙整各研究差異 |  |


### 要求特定修改


如果 Claude 的初次輸出需要調整，可使用以下指令：


> itemize[leftmargin=*]
>     \item 「請在研究方法章節增加 flowchart 說明」
>     \item 「請將結果的表格拆分為主要終點和次要終點兩個表格」
>     \item 「請在討論章節加入與過去 COAPT 試驗的比較」
>     \item 「請增加詞彙表，解釋 TEER、EROA、LVESD 等專有名詞」
>     \item 「主要結果的 HR 和 CI 請用粗體強調」
> itemize


### 自訂 tcolorbox 強調框


在重要發現或臨床建議處，可使用以下格式：

lstlisting[language=TeX,caption=tcolorbox 使用範例]

> **重大發現：**MC4R 基因的功能喪失突變會導致
> 嚴重肥胖，但矛盾的是，這些突變攜帶者反而具有較低
> 的膽固醇水平和心血管疾病風險。

lstlisting


## 常見問題 (FAQ)


| p{9cm}}  **問題** | **解答** |  |
| --- | --- | --- |
| **問題** | **解答** |  |
| Claude 沒有遵循格式規範？ | 確認您在正確的 Project 中對話；可在指令中明確提醒「請參考專案中的 preamble 和範例檔案」 |  |
| PDF 無法上傳？ | 檢查檔案大小是否超過限制；嘗試使用較小的檔案或分割 PDF |  |
| 中文字體顯示異常？ | 確認 Overleaf 使用 XeLaTeX 編譯器 |  |
| 表格跨頁時標題遺失？ | 確認 longtable 的 `\textbackslash endhead` 區塊正確設定 |  |
| DOI 連結無法點擊？ | 確認 hyperref 套件已載入，且連結格式正確 |  |
| 如何加入圖片？ | 上傳圖片到 Overleaf，使用 `\textbackslash includegraphics` 引入 |  |
| 可以輸出 Word 格式嗎？ | 可使用 Pandoc 將 LaTeX 轉換為 DOCX，但可能會損失部分格式 |  |
| 如何分享給團隊？ | Overleaf 支援協作，可透過「Share」按鈕邀請成員；或下載 PDF 分享 |  |


## 工作流程總結


> enumerate[leftmargin=*]
>     \item **開啟專案**：登入 claude.ai，進入「Cardiology Journal Reading」Project
>     \item **上傳 PDF**：點擊附件圖示，上傳要整理的期刊 PDF
>     \item **發送指令**：輸入「請整理」或更詳細的整理要求
>     \item **檢視輸出**：審閱 Claude 生成的 LaTeX 程式碼
>     \item **複製程式碼**：點擊 Copy 按鈕複製完整程式碼
>     \item **開啟 Overleaf**：建立新專案或開啟現有專案
>     \item **設定編譯器**：在 Menu 中將 Compiler 改為 XeLaTeX
>     \item **貼上編譯**：貼上程式碼，點擊 Recompile
>     \item **檢查修正**：如有錯誤，修正後重新編譯
>     \item **下載分享**：下載 PDF 或分享 Overleaf 連結
> enumerate


## 結語


透過 Claude Project 與 Overleaf 的結合，我們可以將繁瑣的期刊文獻整理工作大幅簡化。這套工作流程不僅提升了效率，更確保了輸出講義的專業性與一致性。希望本指南能幫助團隊同仁快速上手，共同建立高品質的心血管教學資源庫。

如有任何問題或建議，歡迎與我聯繫討論。


flushright
謝慕揚醫師 MD, PhD, FESC  

心臟血管中心  

2025年12月
flushright


## 附錄：快速參考卡


> description[leftmargin=2cm,style=nextline]
>     \item[基本整理] 請整理
>     \item[完整指令] 請依據過去期刊講義整理，整理成為繁體中文 latex code
>     \item[指定格式] 請多多使用 longtable 及 \textbackslash href\{\}
>     \item[增加內容] 請在討論章節加入臨床建議
>     \item[修改表格] 請將這個表格改用 longtable 格式
>     \item[加入比較] 請加入與 XXX 試驗的比較表
> description


> description[leftmargin=3cm,style=nextline]
>     \item[編譯] Ctrl + Enter (Mac: Cmd + Enter)
>     \item[儲存] 自動儲存
>     \item[搜尋] Ctrl + F (Mac: Cmd + F)
>     \item[取代] Ctrl + H (Mac: Cmd + Option + F)
>     \item[註解] Ctrl + / (Mac: Cmd + /)
> description


## 參考資源


1. Claude AI 官方網站. [https://claude.ai](https://claude.ai)
2. Anthropic 官方文件. [https://docs.anthropic.com](https://docs.anthropic.com)
3. Overleaf 官方網站. [https://www.overleaf.com](https://www.overleaf.com)
4. Overleaf LaTeX 教學. [https://www.overleaf.com/learn](https://www.overleaf.com/learn)
5. XeLaTeX 與中文排版. [https://www.overleaf.com/learn/latex/Chinese](https://www.overleaf.com/learn/latex/Chinese)