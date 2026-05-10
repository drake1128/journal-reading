# Mainz 2024 Quarto Site — 設計與製作歷程

> 本文件紀錄 `handouts/04-valvular-disease/mainz-2024/quarto/` Quarto 雙語網站從建置到正式發佈到 GitHub Pages 的完整歷程，包含 ch5 TAVI 併發症案例庫的圖文擷取流程、PDF 整理規範、CI/CD 流程與排錯紀錄。
>
> 檔名以 `_` 開頭，Quarto 不會將本文件納入網站渲染。
>
> 整理：謝慕揚 MD, PhD, FESC

---

## 1. 專案概觀

**目標**：以 Quarto 製作 Mainz 2024 Fellowship Training Report 的雙語（zh-TW + English）網站，作為個人結構性心臟病進修紀錄與教學資源。

**Quarto 子專案位置**：`handouts/04-valvular-disease/mainz-2024/quarto/`

**章節結構**：

| 檔名 | 中文 | English |
|------|------|---------|
| ch1 | Mainz Fellowship Report (`zh/ch1-report.qmd`) | TEER (`en/ch1-teer.qmd`) |
| ch2 | TEER (`zh/ch2-teer.qmd`) | TAVI for AS (`en/ch2-tavi-as.qmd`) |
| ch3 | TAVI for AS (`zh/ch3-tavi-as.qmd`) | TAVI for AR (`en/ch3-tavi-ar.qmd`) |
| ch4 | TAVI for AR (`zh/ch4-tavi-ar.qmd`) | Acknowledgements (`en/ch4-acknowledgements.qmd`) |
| **ch5** | **TAVI Complications Case Library** | — |
| ch6 | Acknowledgements | — |

**共用資源**：
- `_quarto.yml` — 子專案配置（無 `embed-resources`，繼承自根 `_quarto.yml`）
- `styles.css` — 自訂樣式
- `../images/` — 圖檔目錄（quarto/ 之外，sibling）
- `../Reference.bib` — 文獻資料庫

---

## 2. ch5 TAVI 併發症案例庫（核心新增）

**規模**：109 篇全文寫作 + 582 張原文圖片，分布於 19 大類別（Cat 1-19）。

### 2.1 案例擷取與圖文整合管線

```
download/<PMID>_<Author>_<Year>.pdf
    │
    ├─ PyMuPDF 擷取每頁嵌入圖（filter <200px）
    │   ├─ images/tavi-complications/<dir>/fig-NN_pPP.<png|jpeg>
    │   ├─ images/tavi-complications/<dir>/_manifest.json   (PDF 來源、頁碼、寬高、bytes)
    │   └─ images/tavi-complications/<dir>/_text.txt        (頁面文字快照)
    │
    ├─ 案例 narrative 寫入 zh/ch5-tavi-complications.qmd
    │   每篇 #### 標題 + PubMed 連結 + 教學重點 + figure gallery
    │
    └─ PDF 重新命名 + 分類存檔
        case-library-pdfs/<NN-category-slug>/Author_Year_Keyword.pdf
        + INDEX.md（PMID ↔ filename ↔ title 對應表）
```

### 2.2 案例分類（Cat 1-19）

| # | 類別 | 已寫案例 |
|---|------|---------:|
| 1 | Coronary obstruction / Anomaly / BASILICA / Spasm | 12 |
| 2 | Annular / Aortic root rupture / Dissection / Calcification | 3 |
| 3 | Valve embolization / Migration / Dislocation | 6 |
| 4 | Paravalvular leak (PVL) | 12 |
| 5 | Thrombosis / Leaflet / HALT | 8 |
| 6 | Endocarditis / Mycotic | 5 |
| 7 | Stroke / Cerebral / TIA | 1 |
| 8 | Vascular access / Bleeding / Iliofemoral | 10 |
| 9 | Mitral injury / SAM / LVOT obstruction / Suicide LV | 13 |
| 10 | Cardiac tamponade / Pericardial | 1 |
| 11 | Iatrogenic VSD / Septal injury / Fistula | 4 |
| 12 | Multi-valve / Combined procedures | 6 |
| 13 | Bicuspid / Special anatomy / Small annulus | 8 |
| 14 | Valve-in-Valve / Redo / Explantation | 2 |
| 15 | Heart failure / ECMO / Pulm HTN | 1 |
| 16 | Procedural rescue / Bailout / Snare / Wire loss | 4 |
| 17 | Device malfunction | 1 |
| 18 | Special populations (pediatric LAMPOON 等) | 1 |
| 19 | Bowel / GI / Non-cardiac collateral | 1 |
| 20 | Other / Miscellaneous | 0（無下載案例） |

**初始排除**：Jha 2026 (post-MI VSD)、Kodesh 2026 (RCA STEMI + MR cardiogenic shock) — 與 TAVI 併發症無直接關係，於 review 階段移除。

### 2.3 圖檔擷取規範

- **工具**：PyMuPDF (fitz)
- **過濾條件**：忽略寬或高 < 200 px 的圖（排除 logo / icon）
- **命名**：`fig-NN_pPP.<ext>` — NN 為頁內順序，PP 為頁碼，副檔名依 PDF embed 格式（多為 png 或 jpeg）
- **每篇 sidecar**：
  - `_manifest.json` — 機器可讀，包含每張圖的 page、width、height、bytes
  - `_text.txt` — 全文文字快照（後續可以從中提取 figure legend）
- **總量**：582 張圖、317 MB

### 2.4 PDF 重命名與分類

從 `download/<PMID>_<Author>_<Year>.pdf` → `case-library-pdfs/<NN-category-slug>/Author_Year_Keyword.pdf`

- **Author**：原樣（去掉非英數字、保留底線）
- **Year**：原樣（4 位數）
- **Keyword**：從原文標題去掉 stop words 後取前 50 字元，以 `_` 連接（如 `Continuous_Assessment_Left_Ventricular_Outflow`）
- **PMID 保留方式**：寫入 `case-library-pdfs/INDEX.md` 對應表，每筆有 PubMed 連結

---

## 3. 圖檔路徑解析（重要！）

### 3.1 設計選擇

`images/` 目錄位於 `mainz-2024/images/`（quarto/ 的 sibling），原因：
- 同時供 LaTeX (`main Mainz 2024.tex`) 與 Quarto 兩種輸出共用
- 避免重複儲存

但 Quarto 預設只 copy 專案 root 之內的資源到 `_site/`。要讓 Quarto 找到外部圖：

### 3.2 解法 — Junction / Symlink

**本地（Windows）**：
```powershell
New-Item -ItemType Junction `
  -Path  handouts/04-valvular-disease/mainz-2024/quarto/images `
  -Target ../images
```

**CI runner（Ubuntu）**：在 `.github/workflows/publish.yml` 中加入：
```yaml
- name: Symlink images into Mainz 2024 Quarto project
  run: |
    ln -s ../images handouts/04-valvular-disease/mainz-2024/quarto/images
```

**`.gitignore`** 排除這個 junction（每台機器需要本地建立）：
```
handouts/04-valvular-disease/mainz-2024/quarto/images
```

### 3.3 qmd 圖片參考路徑

所有 qmd 檔（zh/*.qmd, en/*.qmd）統一使用：

```markdown
![caption](../images/tavi-complications/<dir>/fig-NN_pPP.png)
```

從 `quarto/zh/<chapter>.qmd` 解析 → `quarto/images/...`（junction）→ 實際 `mainz-2024/images/...`。

---

## 4. CI/CD：GitHub Pages 發佈

### 4.1 最終 workflow（`.github/workflows/publish.yml`）

```yaml
on:
  push:
    branches: [master]

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          lfs: true                              # ★ 拉取 LFS 物件
      - name: Symlink images
        run: ln -s ../images handouts/04-valvular-disease/mainz-2024/quarto/images
      - uses: quarto-dev/quarto-actions/setup@v2
      - uses: quarto-dev/quarto-actions/render@v2
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: _site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/deploy-pages@v4
        id: deployment
```

**Pages 來源切換**：透過 GitHub REST API 把 `build_type` 從 `legacy`（gh-pages branch）改為 `workflow`（artifact-based）：

```bash
gh api -X PUT "repos/drake1128/journal-reading/pages" -F build_type="workflow"
```

### 4.2 Git LFS 設定（`.gitattributes`）

只把 ch5 新增的 TAVI 圖檔與案例 PDF 走 LFS，既有的其他圖檔保留為一般 git blob 不動。

```
handouts/04-valvular-disease/mainz-2024/images/tavi-complications/**/*.png filter=lfs diff=lfs merge=lfs -text
handouts/04-valvular-disease/mainz-2024/images/tavi-complications/**/*.jpg filter=lfs diff=lfs merge=lfs -text
handouts/04-valvular-disease/mainz-2024/images/tavi-complications/**/*.jpeg filter=lfs diff=lfs merge=lfs -text
handouts/04-valvular-disease/mainz-2024/case-library-pdfs/**/*.pdf filter=lfs diff=lfs merge=lfs -text
```

### 4.3 Pages Artifact 限制（1 GB）

GitHub Pages 部署 artifact 上限 **1 GB**。第一次部署 artifact 達 **1.02 GB → 觸頂 → ch5 HTML 被截斷**（end mid-base64 string）。

關鍵原因：根 `_quarto.yml` 設了 `embed-resources: true`，把所有圖片以 base64 inline 進 HTML，導致 ch5 單檔 ~400 MB。

**解法**：在根 `_quarto.yml` 改成 `embed-resources: false`：

```yaml
format:
  html:
    embed-resources: false   # 圖檔以外部 file ref 引用，HTML 維持 ~100 KB-1 MB
```

修正後 artifact 從 1.02 GB → **380 MB** ✓

---

## 5. 排錯歷程（Today, 2026-05-09 → 2026-05-10）

### 5.1 問題 — 本地能看到圖、Pages 全部 404

| # | 排錯里程碑 | 對應 commit |
|---|----------|-----------|
| 1 | 圖檔路徑：原 `../../images/` 從 quarto/zh/ 解析到 quarto 專案外，Quarto 不 copy → 改成 `../images/` 並建立 `quarto/images` junction → 本地預覽 OK | (path rewrite, included in `a07ffef`) |
| 2 | `actions/checkout@v4` 預設不拉 LFS → CI 抓到的是 130 byte pointer file，不是真的圖 → 加 `with: lfs: true` | `49f5fee` |
| 3 | CI runner 沒有 junction（windows-only artifact，已 gitignore）→ Quarto 找不到 `quarto/images/` → 加一個 `ln -s ../images quarto/images` 的 step | `49f5fee` |
| 4 | `quarto-actions/publish@v2` 透過 git push 推 ~321 MB 到 gh-pages branch → **HTTP 408 timeout** → 改用 artifact-based deploy（`upload-pages-artifact` + `deploy-pages`），同步把 Pages source 從 legacy 改成 workflow | `51bb916` |
| 5 | 第一次 artifact-based deploy artifact = 1.02 GB（超過 1 GB Pages 上限，HTML 被截斷）→ 找到根 `_quarto.yml` 的 `embed-resources: true` 把 ch5 整個 inline 成 base64 → 改成 `false` → artifact 380 MB ✓ | `01450e2` |

### 5.2 失敗訊號的 forensics 紀錄

- **HTTP 408 (gh-pages push timeout)**：log 出現 `error: RPC failed; HTTP 408 ... send-pack: unexpected disconnect while reading sideband packet`
- **Pages 1 GB 超量**：log 出現 `Uploaded artifact size of 1096911015 bytes exceeds the allowed size of 1 GB. Deployment might fail.`（Deploy step 還是會回報 success，但檔案會被截斷）
- **HTML 被截斷的判讀**：`tail -c 50 ch5.html` 不是 `</html>` 而是 base64 亂碼結尾 → 確診內容超量

### 5.3 驗證程序

部署完成後的標準健康檢查：

```bash
# 1. 確認 ch5 HTML 完整
curl -sL "<URL>" | tail -c 50  # 應該結尾為 </html>

# 2. 確認圖片參考都是外部 file ref（沒被 inline）
curl -sL "<URL>" | grep -oE 'src="\.\./images/[^"]*"' | wc -l   # 期望: 505
curl -sL "<URL>" | grep -c 'data:image'                        # 期望: 0

# 3. 隨機抽樣圖片 URL 確認都 200
curl -s -o /dev/null -w "%{http_code}\n" "<image_url>"
```

---

## 6. 本地開發環境

### 6.1 必要設定（首次 clone）

```powershell
# 1. 拉 LFS
git lfs install
git lfs pull

# 2. 建立 Quarto 找圖用的 junction
New-Item -ItemType Junction `
  -Path  handouts/04-valvular-disease/mainz-2024/quarto/images `
  -Target ../images

# 3. （可選）安裝 Quarto 本機渲染
# https://quarto.org/docs/get-started/
```

### 6.2 預覽伺服器

```powershell
cd handouts/04-valvular-disease/mainz-2024/quarto
quarto preview
# → http://127.0.0.1:4848/
```

### 6.3 PDF 重新擷取圖片（如有新增 case）

```powershell
cd download
python _extract_figures.py <PDF.pdf>
# → 會在 ../handouts/04-valvular-disease/mainz-2024/images/tavi-complications/<dir>/ 產生 fig + manifest + text
```

---

## 7. 相關 commit 快速索引

| Commit | 主題 |
|--------|------|
| `a07ffef` | Expand TAVI complications case library — 109 cases + 582 figures（內容主線）|
| `49f5fee` | Fix GitHub Pages: pull LFS and symlink quarto/images on CI |
| `51bb916` | Switch GitHub Pages to artifact-based deploy（避開 gh-pages push 408 timeout）|
| `01450e2` | Disable embed-resources at site root: keeps Pages artifact under 1 GB |

---

## 8. 已知限制與後續可優化

- **Artifact 380 MB 仍偏大**：每次 push 都要重新 upload。可進一步：
  - 把 `images/tavi-complications/` 內的 PNG 壓縮成優化過的 JPEG（很多 5 MB 的圖其實 < 800 KB 就夠）
  - 估計可降到 ~150 MB
- **gh-pages branch 已停用**：可刪除以節省 repo 體積
- **Figure caption 目前是我手寫的中文**，並非原文 figure legend；後續可以用 `_text.txt` 抓真正 legend 替換
- **GitHub LFS 配額**：免費 1 GB 儲存 + 1 GB/月頻寬。每次 fresh clone 會消耗頻寬，需注意

---

**建檔日期**：2026-05-10（接續 2026-05-09 的整合工作）
**整理**：謝慕揚 MD, PhD, FESC
