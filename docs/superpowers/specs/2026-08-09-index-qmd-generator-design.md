# index.qmd 自動生成器 — 設計文件

**日期**：2026-08-09
**作者**：謝慕揚 MD, PhD, FESC（設計對話），Claude Code（撰寫）
**狀態**：設計定案，待實作

---

## 1. 問題

`handouts/` 底下有 24 個主題資料夾，其中 23 個各有一份手寫的 `index.qmd` 當作 Quarto 網站的分類頁（`nejm-case-records` 沒有，見 §5.3）。這些頁面**沒有跟著新增的講義更新**：

- `05-cardiac-imaging/index.qmd` 的「教學講義 Handouts」段落**完全空白**，但該資料夾實際有 122 個檔案
- `09-hypertension`、`13-icu-renal`、`14-diabetes-metabolic`、`21-pulmonary-hypertension`、`22-copd-asthma`、`95-management-leadership` 的 index 各只有 1 條連結
- 177 份 Marp 投影片、102 份 PDF **完全沒有在網站上露出**

結果：新增的講義只要沒手動加進 index，在 https://drake1128.github.io/journal-reading/ 上就等於不存在。

## 2. 目標與非目標

**目標**：新增講義後，執行一個指令就讓該資料夾的 `index.qmd` 反映實際檔案，且**不破壞任何手寫內容**。

**非目標**：
- 不重寫 Quarto 網站架構
- 不處理 `featured.qmd` 與 `_quarto.yml` 的 sidebar（那是刻意策展的，維持手動）
- 不搶救舊的 LaTeX 轉檔內容（只出報告，由人決定）

## 3. 現況調查（實測數據，2026-08-09）

### 3.1 index.qmd 的結構差異

23 個 index 不是同一種東西：

| 特徵 | 數量 |
|---|---|
| 有 `## 教學講義 Handouts` 區塊 | 20 |
| 有 `## LaTeX Files` 區塊 | 17 |
| 有 `## 從 LaTeX 轉換的網頁 (Pandoc → Quarto)` 區塊 | 17 |
| 有 `## 互動投影片 Interactive Slides` 區塊 | 3 |
| 使用 Quarto `listing:` 卡片牆 | 1（`classroom-teaching`） |

**含手寫敘述、無法從檔名推導的資料夾（6 個）**：

| 資料夾 | 手寫內容 |
|---|---|
| `classroom-teaching` | 整頁 listing 卡片牆 + 31 行模組導覽 |
| `90-ai-technology` | 12 行敘述 |
| `99-misc` | 9 行敘述 + 「問卷與量表 Surveys & Instruments」區塊 |
| `95-management-leadership` | 9 行敘述 |
| `14-diabetes-metabolic` | 4 行敘述 |
| `15-oncology` | 3 行敘述 |

另有 `91-podcast-journal-review` 頂端手寫的「每週心血管期刊文獻回顧」清單（帶日期區間註解）、`08-genetic-medicine` 的「⭐ 基因體醫學入門系列（讀書會三個月課程）」。

**結論**：任何「整頁重生」的做法都會摧毀這些內容。

### 3.2 檔案盤點（各主題資料夾頂層）

| 類型 | 數量 | 備註 |
|---|---|---|
| `*教學講義.md` | 163 | 現行講義命名 |
| `*教學共筆.md` | 1 | `Murmur Man 心雜音助記法 教學共筆.md` |
| `*handout.md` | 451 | 舊 LaTeX → pandoc 轉檔 |
| `*_Marp.md` | 177 | Marp 投影片原始檔 |
| `*.pdf` | 102 | 共 84 MB |
| 其他 `.md` | 16 | 如 `Entresto_Seminar_2026.md` |

**配對可靠性**：
- `_Marp.md` ↔ `.pdf` 同字根配對：101/102 PDF 成功（**99%**）
- 中文長文講義 ↔ `_Marp.md`：**配不起來**，因為命名慣例不同
  - `AI-ECG 偵測肥厚性心肌病變 教學講義.md` ↔ `AI_ECG_HCM_Detection_Marp.md`
  - `Acute Heart Failure 當代管理 教學講義.md` ↔ `Acute_Heart_Failure_Management_Marp.md`
  - `CMR_Myocardial_Inflammation_LLC2018_Marp.md` 根本沒有對應的中文講義

### 3.3 451 個 `handout.md` 的品質問題

只有 13 個（3%）跟現有 `.qmd` 重複 —— 它們是獨立內容且目前網站上看不到。但抽樣顯示是**壞掉的 LaTeX → Markdown 轉檔**：

```
handouts/01-ischemic-heart-disease/cath hemodynamics handout.md:
    {\bfseriesemergency_red 右心導管血行動力學}
    [0.5cm]
    {emergency_blue 超音波評估與臨床應用}

handouts/01-ischemic-heart-disease/NEJM ACS DAPT withdrawal of aspirin handout.md:
    titlepage
    {****教學部教學文件****}
```

Regex 掃描（`{\`、`\bfseries`、`[0.5cm]`、`titlepage`、`\begin{`、`emergency_red` 等）：**170/451（38%）確定含 LaTeX 殘骸**。其餘 281 個只是沒命中 regex，不代表品質可發布。

repo 是 **public**，這些內容不應自動上站。

### 3.4 PDF 在網站上全部 404

`_quarto.yml` 沒有宣告 `resources:`，Quarto 不會把未被引用的 PDF 複製進 `_site`。實測：

```
/handouts/02-heart-failure/Acute_Heart_Failure_Management.pdf   404
/handouts/02-heart-failure/BioVAT_HF.pdf                        404
/handouts/05-cardiac-imaging/AI_ECG_HCM_Detection.pdf           404
/handouts/01-ischemic-heart-disease/index.html                  200
/handouts/01-ischemic-heart-disease/FFR ... 教學講義.html        200
/handouts/01-ischemic-heart-disease/STEMI_D2B_Improvement.html   200
```

`.md` 講義頁與 `.html` 互動教材正常，唯獨 PDF 沒被部署。

## 4. 設計決策

| # | 決策 | 理由 |
|---|---|---|
| D1 | 只改寫 `<!-- AUTO-INDEX:START -->` … `<!-- AUTO-INDEX:END -->` 之間 | 6 個資料夾含無法推導的手寫內容（§3.1） |
| D2 | 三群分列，**不強行配對**講義與投影片 | 中文講義 ↔ Marp 字根不同，猜錯比不猜更糟（§3.2） |
| D3 | `handout.md` 不進自動清單，另出報告 | 38% 確定含 LaTeX 亂碼，repo 是 public（§3.3） |
| D4 | `_quarto.yml` 加 `resources: [handouts/**/*.pdf]` | 否則投影片區塊全部 404（§3.4） |
| D5 | 手動 CLI + CI `--check` 守門（黃燈，不擋部署） | 純手動會重演「index 空了很久沒人發現」；CI 自動 commit 會與兩台機器來回的工作流產生 rebase 衝突 |
| D6 | `## LaTeX Files` 與 `## 從 LaTeX 轉換的網頁` 兩節**原封保留** | 使用者明確要求保留；它們在自動區塊外，腳本本來就不會碰 |

## 5. 架構

單一 Python 腳本 `.claude/scripts/update_index.py`，**只用標準函式庫**（無 pip 依賴）。

```
discover(folder) -> Entries      掃描資料夾，回傳分類後的條目
render(entries)  -> str          產生 Markdown 區塊字串（純函式，不碰檔案）
apply(path, block) -> bool       把區塊寫回標記之間，回傳是否有變更
```

`render` 是純函式，可以餵假資料直接驗證輸出格式，不需要動到 23 個真實檔案。

### 5.1 檔案發現規則

只掃各主題資料夾**頂層，不遞迴**。子資料夾（如 `weekly-cv-review-2026-05-30/`）是獨立 Quarto 頁面，由使用者手寫連結，腳本不介入。

| 區塊標題 | 收錄規則 |
|---|---|
| `## 教學講義 Handouts` | `*.md`，檔名含 `教學講義` / `教學共筆` / `講義` |
| `## 投影片 Slide Decks` | `*.pdf`；若某 `*_Marp.md` 無同字根 PDF，則連該 `_Marp.md` |
| `## 互動教材 Interactive` | `*.html` **且 `git ls-files` 查得到** |

`.html` 用 git 追蹤狀態判斷，是為了沿用既有的 `.gitignore` 白名單機制（`handouts/**/*.html` 全擋 + `!` 逐一放行 + `!handouts/classroom-teaching/**/*.html` 目錄放行）。沒進版控的暫存 HTML 自動不列，不需要另一套規則。

**排除清單**：`*handout.md`、`index.qmd`、`INDEX.md`、`README.md`、`_` 開頭的檔案。

空區塊不輸出標題（該類別沒檔案就整節省略）。

### 5.2 顯示標題

1. `.md` → 讀檔案第一個 `# H1`，去掉 `教學講義` / `教學共筆` 等後綴
2. 讀不到 H1，或是 `.pdf` / `.html` → 用檔名，去副檔名與 `_Marp` 後綴，底線換空格

現況把副檔名寫進顯示文字（`[AI-ECG 偵測肥厚性心肌病變 教學講義.md](...)`），新版輸出 `[AI-ECG 偵測肥厚性心肌病變](...)`。

### 5.3 區塊行為

- **首次執行**：把區塊**附加到檔案末端**，現有內容一行不動
- 標記認**內容不認位置** —— 使用者之後可自由把區塊搬到頁面任何地方
- **沒有 `index.qmd` 的資料夾一律跳過**，並列進報告（§5.5）
- 區塊內排序：按顯示標題排序（中文走 Unicode 序，穩定可預期）

**為何不自動建立 index.qmd**：24 個資料夾裡只有 `handouts/nejm-case-records/` 沒有 `index.qmd`，而它的結構本來就不同 —— 63 個 per-case 子資料夾各有自己的 `index.qmd`，且已逐一掛在 `_quarto.yml` sidebar 上。該資料夾頂層 66 個檔案中有 64 個是被 D3 排除的 `NEJM Case N-YYYY handout.md`，自動建立只會產生一個**只有 1 條目、且無人連結的孤兒頁**。要不要替它建索引是策展決定，不是腳本該替使用者做的。

### 5.4 執行模式

```bash
python3 .claude/scripts/update_index.py           # 改寫，印出變更摘要
python3 .claude/scripts/update_index.py --check   # 唯讀；有落差 exit 1 並列出過期資料夾
```

`--check` 不寫任何檔案，包含不寫報告。

### 5.5 未收錄報告

腳本同時寫出 `docs/index-report.md`（**進版控**，讓兩台機器都看得到），內容：

- 掃到但未收錄的檔案，依資料夾分組
- 偵測到 LaTeX 殘骸的檔案清單（標明命中哪個 pattern）
- 被跳過（無 `index.qmd`）的資料夾
- 各資料夾的收錄統計

這是日後決定要不要搶救 451 個舊轉檔的依據。

## 6. 現有檔案改動

| 檔案 | 改動 |
|---|---|
| `_quarto.yml` | `project:` 底下加 `resources: [handouts/**/*.pdf]`（站台 +84 MB；GitHub Pages 上限 1 GB） |
| `.github/workflows/publish.yml` | render 前插入 `--check` 步驟，`continue-on-error: true` |
| `CLAUDE.md` | Post-Completion Workflow 加一行：產完講義後跑 `update_index.py` |
| 23 個 `handouts/*/index.qmd` | 末端附加 AUTO-INDEX 區塊（`nejm-case-records` 無 index.qmd，跳過） |

## 7. 錯誤處理

| 情況 | 行為 |
|---|---|
| `index.qmd` 不存在 | 跳過該資料夾並列進報告（§5.3） |
| 只有 START 標記、缺 END | 報錯並跳過該檔案，不猜測邊界 |
| 檔案編碼不是 UTF-8 | `errors='ignore'` 讀取，取不到 H1 就 fallback 到檔名 |
| `git ls-files` 不可用（非 git 環境） | 警告並改為列出所有 `.html` |
| 資料夾無任何可收錄檔案 | 寫入空的 START/END 標記對 |

## 8. 驗證計畫

1. 跑 `--check` 取得基準線
2. **只對 `05-cardiac-imaging` 一個資料夾試跑**，`git diff` 逐行檢查
3. 全跑後檢查 §3.1 那 6 個含手寫內容的資料夾 + `91-podcast-journal-review` + `08-genetic-medicine`，`git diff` 必須**只有新增行、沒有刪除行**
4. 確認 17 個資料夾的 `## LaTeX Files` 與 `## 從 LaTeX 轉換的網頁` 兩節逐字未變（D6）
5. 本機 `quarto render`，curl 抽驗講義頁、PDF、互動 HTML 各一
6. 全部通過才 commit

第 3、4 步是這個設計的核心風險點，必須逐字比對而非目視。
