# Post-Carotid Stenting Surveillance — 製作進度 PROGRESS

> **2026-06-12 第二輪修訂（已完成）**：① 前面枯燥頁加入 **4 張自製 SVG 圖解**（頸動脈支架解剖、neointimal hyperplasia 三階段、duplex=解剖+生理、硬支架→PSV 假升）。② 全簡報加 **References**：重點頁左下角附 Authors·期刊·年份，並新增一張 **Key references** 投影片（10 篇，已用 PubMed 核實 PMID）。③ **Case 2 改為文獻 case series**（原 H464703 真實病人移除，含那張怪怪的 follow-up 影像）：ISR 自然史/進展（CREST 6%、AbuRahma 2022 進展率）＋ DCB 治療 series（Montorsi 2012 n=7、Gandini 2014 n=9）。④ 共 30 頁，1280×720 零溢出。原檔仍備份於 `..._BACKUP_pre-cases.html`。


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

## ✅ 待辦（已於 2026-06-12 完成）

1. ~~找出過去治療的 carotid stenting 案例~~ → **完成**：用了兩位真實病人。
2. ~~放入 duplex / angiograph / 照片到 Case 1、Case 2~~ → **完成**：原本兩張示意案例頁改為 **6 張真實案例頁**（Case 1 ×4、Case 2 ×2），13 張影像全部 **base64 內嵌**。
   - **Case 1（縱向追蹤）**：嚴重雙側狹窄 → 右側 CAS → 追蹤確認 **無 in-stent restenosis**（in-stent PSV 49→59、ratio 1.1→1.48，遠低於 ISR cutoff）→ **對側（左）疾病**惡化 → 對側血管成形術 → 穩定。涵蓋講題兩大重點（ISR + contralateral progression）。
   - **Case 2**：index CAS（支架置放 / 撐開後 / 腦部 baseline run）＋ 6 週後 angiographic follow-up（支架通暢）＋ concomitant CAD（系統性疾病提醒）。
3. ~~影像去識別化~~ → **完成**：Affiniti 7 那兩個 US series 頂端有姓名/病歷號/DOB/日期 banner，已裁切移除；其餘影像本無 PHI。案例文字一律用**相對時間軸**（Baseline / Month 0 / ~16 mo / ~20 mo / ~3 yr），無姓名/病歷號/日期。
4. **最後檢查** → 已用 Playwright 於 1280×720 驗證：**29 張投影片全部零溢出、13 張圖 0 broken**。原檔備份為 `Post_Carotid_Stenting_Surveillance_BACKUP_pre-cases.html`。
   - 字體仍走 Google Fonts CDN；若要 **100% 離線**（含字體內嵌）再告知。

## 🖼️ 圖片策略：Stand-Alone 單一 HTML

- 圖片一律 **base64 內嵌**進 HTML（不是用外部相對路徑），讓整份投影片是**一個檔案、可離線、可隨身帶**。
- 流程：Drake 提供圖片 → Claude 將圖片 base64 內嵌到對應投影片 → 維持 viewport 不溢出（`max-height: min(50vh,400px)`）。
- 字體目前走 Google Fonts CDN（需網路）；若要 100% 離線，再請 Claude 把字體也內嵌（檔案會變大）。

## ⏰ 提醒

- Google Calendar：6/9、6/10、6/11 連續三晚 21:00–21:30 提醒整理投影片。
