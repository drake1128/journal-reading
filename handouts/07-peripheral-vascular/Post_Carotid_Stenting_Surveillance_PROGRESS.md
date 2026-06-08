# Post-Carotid Stenting Surveillance — 製作進度 PROGRESS

**用途**：介入學會 Carotid Stenting 課程（週末上課用）
**講者**：謝慕揚 MD, PhD, FESC
**主檔**：`Post_Carotid_Stenting_Surveillance.html`（單一 self-contained HTML，瀏覽器直接開）
**線上**：https://drake1128.github.io/journal-reading/handouts/07-peripheral-vascular/Post_Carotid_Stenting_Surveillance.html
**最後更新**：2026-06-09

---

## ✅ 目前已完成

- **25 張投影片**，診間專業風（navy / 紅 / 藍），Bricolage Grotesque + IBM Plex 字體，Doppler 波形視覺母題。
- 內容：surveillance rationale → 六大監測目標 → ISR 定義/發生率/危險因子 → risk timeline → surveillance schedule 表 → duplex 為首選 → 為何 native criteria 誤判 → **stent-specific velocity criteria 關鍵表** → baseline & trend（含 SVG 趨勢圖）→ CTA/MRA/DSA → ISR 處置 → medical therapy → guidelines（SVS 2022 / ESVS 2023 / AHA-ASA）→ 一頁式 algorithm。
- **兩個 worked cases**（目前為示意，可編輯替換成真實案例）：
  - Case 1「watch」：無症狀、PSV 110→160→240、CTA ~55% → 強化藥物治療 + 縮短追蹤。
  - Case 2「act」：post-radiation、症狀性、PSV 360 / ratio 4.6、DSA ~85% → DCB 再介入。
- 全部投影片通過 **1280×720 零溢出**檢測。
- **瀏覽器內編輯**：按 `E` → 點文字直接改 → `Ctrl+S` 存到瀏覽器 → 右上 💾 匯出更新後的 .html。
- 已 commit + push（`.gitignore` 已 whitelist 此檔，正式追蹤）。

## 🔲 待辦（接下來兩天，每晚 ~30 min）

1. **找出過去治療的 carotid stenting 案例**（Drake）。
2. **放入 duplex / angiograph / 照片**到 Case 1、Case 2（或新增案例頁）。
3. 真實病人影像 **務必先去識別化**（去掉姓名 / 病歷號 / 日期）——本 repo 為公開 GitHub Pages 網站。
4. 最後檢查：文字校對、投影片不溢出、匯出一份 **Stand-Alone 單一 HTML 備份**帶去現場（避免現場無網路）。

## 🖼️ 圖片策略：Stand-Alone 單一 HTML

- 圖片一律 **base64 內嵌**進 HTML（不是用外部相對路徑），讓整份投影片是**一個檔案、可離線、可隨身帶**。
- 流程：Drake 提供圖片 → Claude 將圖片 base64 內嵌到對應投影片 → 維持 viewport 不溢出（`max-height: min(50vh,400px)`）。
- 字體目前走 Google Fonts CDN（需網路）；若要 100% 離線，再請 Claude 把字體也內嵌（檔案會變大）。

## ⏰ 提醒

- Google Calendar：6/9、6/10、6/11 連續三晚 21:00–21:30 提醒整理投影片。
