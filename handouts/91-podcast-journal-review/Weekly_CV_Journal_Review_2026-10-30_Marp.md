---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Microsoft JhengHei', 'PingFang TC', sans-serif;
    background-color: #ffffff;
    color: #2d3436;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 2.0em; border-bottom: none; }
  section.lead h2 { color: #b0c4de; }
  section.lead h3 { color: #ffffff; font-weight: normal; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #ffd166; text-decoration: underline; }
  section.lead blockquote,
  section.lead blockquote p,
  section.lead blockquote strong { color: #2d3436; }
  section.divider {
    background-color: #0072bc;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: #ffffff;
    border-bottom: none;
    font-size: 2.4em;
    text-align: center;
  }
  section.divider h2 {
    color: #ffffff;
    font-size: 1.5em;
    text-align: center;
    font-weight: bold;
  }
  section.divider h3 {
    color: #ffe082;
    font-size: 1.2em;
    text-align: center;
    font-weight: normal;
  }
  section.divider p, section.divider strong { color: #ffffff; }
  section.bignum {
    background-color: #1a2740;
    color: #ffffff;
    text-align: center;
  }
  section.bignum h1 { color: #ffffff; font-size: 3.5em; border-bottom: none; }
  section.bignum h2 { color: #b0c4de; font-size: 1.3em; }
  section.bignum p { color: #dfe6e9; font-size: 1.0em; }
  section.bignum strong { color: #ffe082; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  a { color: #0072bc; }
  table { font-size: 0.68em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 5px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.9em;
  }
  section:not(.lead):not(.divider):not(.bignum) blockquote { margin-right: 170px; }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 0.68em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.74em; }
  section.abbr { font-size: 0.66em; }
  section.ref { font-size: 0.6em; }
  .qr {
    position: absolute;
    right: 40px;
    bottom: 80px;
    text-align: center;
    font-size: 0.65em;
    color: #555;
  }
  .qr img { width: 110px; height: 110px; border: 1px solid #dcdde1; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-10-23 ~ 2026-10-30'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-10-23 ~ 2026-10-30

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Top Pick 附 QR Code，可掃描跳轉原文

---

# 🎯 本週主題與固定欄目

## 把介入的「時間窗」往外推、把急診的「效率神話」往內收

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 術前策略／術中幾何／耐久性
3. 🔧 **TEER Section** — 加夾片、bailout、團隊輻射
4. 📚 **Honorable Mentions** — EHJ／JACC／Circulation
5. 🔬 **Case Reports** — 介入救援 × 腫瘤心臟學
6. 💎 **Take Home Message**

> 本週 **EuroIntervention 無新上線文章**（PubMed 2026/10/23–10/30）。

---

# ⭐ Top 5 Picks 一覽

| # | 試驗 / 主題 | 期刊 | 方向 | 關鍵數字 |
|---|------------|------|------|---------|
| 1 | **LATE-MT**：24–72h 超晚期取栓 | NEJM | ✅＋警訊 | common OR 1.74（1.19–2.55）；sICH 4.8% vs 0；死亡 6.0% vs 1.8% |
| 2 | **MILD-MT**：輕症 LVO 取栓 | NEJM | ✅ | mRS 0–1 69.4% vs 50.0%，OR 2.32（P<0.001） |
| 3 | **PRESC1SE-MI 統合**：0/1h vs 0/3h | Lancet | ❌ Neutral | ED LOS GMR 1.03；直接出院 OR 1.31（NS） |
| 4 | **PCI-before-TAVI 統合** | Cardiol Rev | 💡 個別化 | 30d 死亡 RR 1.26（0.90–1.77），無益處 |
| 5 | **多夾片治 TEER 殘餘 MR** | JAHA | 💡 | 1 年死亡＋HF 住院 16.8% vs 29.2%（P=0.002） |

> **Pearl of the Week**：取栓往晚期／輕症推進（但出血與併發症要一起算）；「驗肌鈣蛋白快」≠「急診跑得快」。

---

<!-- _class: divider -->
# NEJM
## 腦血管介入的時間窗
### LATE-MT ×  MILD-MT

---

# ⭐ LATE-MT — 24 到 72 小時的超晚期取栓

## [Yang P, et al. (LATE-MT). N Engl J Med 2026](https://doi.org/10.1056/NEJMoa2609362)

| 項目 | 內容 |
|------|------|
| 設計 | 開放標籤隨機、盲性終點（中國多中心），336 人 ITT |
| 族群 | 前循環 LVO，發作 **24–72 小時**、影像仍有可救組織；中位 38.5h |
| 介入 | EVT ＋內科 vs 單純內科（各 168 人） |
| Primary | 90 天 mRS 分布：**common OR 1.74（95% CI 1.19–2.55）** |
| 安全性 | **sICH 4.8% vs 0%**；**90 天死亡 6.0% vs 1.8%** |

> **Take home**：影像挑過的病人超晚期取栓仍改善功能，但出血／死亡上升——positive，但不是 free。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABP0lEQVR42u1YwQkDMQwzzQAZKat7pA4QSCU5d6WPK/RT9LgQCrl8hC1LSmNdrBn3zdebZ2C1ldFXw4e+eI4xH3G1/nUDbAMYgW12bhyBEL8m2FClBjCdkBp3NC9s6mOEJzbWrVjnhI18Ax5ORoh7PnzTnG6mcRvNaS3x7UNdXPhGfVNPx3F0wcZBYAFTs5AhhC49ld6+ofr0VKiWSjdlW0GDMOIb+ihlG5KUbDZ1o9JGoVonQhN9a/L6VZYK0/eZU3YwayJQtA3MhW80hWBsY2erdDb6FlOOMHfCzB2ZXLweeCAgBFYN9fEFlo6JdwsvWdd9PGvUY0FuJa1zzCF5wjPKb2crlYGN+CZrOBNvfbF6L+xMroY2L2xD5kUZKda5vQHLwvi1O/GtsuUxCz5+qndWyExTUXP45Lf7/6rfb17/neGZEmNbLAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# ⭐ MILD-MT — 輕症（NIHSS <6）LVO 取栓

## [Liu J, Yi T, et al. (MILD-MT). N Engl J Med 2026](https://doi.org/10.1056/NEJMoa2609149)

| 項目 | 內容 |
|------|------|
| 設計 | 多中心開放標籤隨機（中國），300 人 mITT |
| 族群 | 輕症 **NIHSS <6** 前循環 LVO，小核心＋大 mismatch，<24h |
| 介入 | EVT＋內科（144）vs 單純內科（156） |
| Primary | 90 天 mRS 0–1：**69.4% vs 50.0%，OR 2.32（1.41–3.81），P<0.001** |
| 安全性 | sICH 3 vs 3（相當）；**嚴重操作併發症 13.2%**；全體 1 死 |

> **Take home**：輕症 LVO 不等於不積極——有可救組織時取栓大幅改善功能，但 13% 操作併發症提醒病例選擇。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABO0lEQVR42u1YwQ0DMQhDZQBGyuoZ6QZAooDJ/a6PPio/GlVVonwsxzZwEg/L5X/z8eaSXHqtOl55XHWW5S95Wr+6KTAJSguVaGy30ALJgi1ZSmxiWyywVypsyVj/a3OodLzVa7LxVnqLnajgDya9jU/vH5FPZ6Xe0qcZKsMeyZv6gKwA8aNAEt7cNl52XlNW+oJGby0z23hQGJYEW5oUkjv7TVQXmqgqWy25PPJgcxk7FMgKXp5aj2etJqRA2ob8SHhDIZhyYF0aeGpWBxo6N1DHk72VZjKlCkYgyre2gCN1u1PiqfXItK7yzZ5touyt9kO8M+QOE6I+pII3IDnsqfq3OCVVibBhzlrgDZHiQjUvlD1vvbHNgNqN3BmiqWbAmBauJcc11x/S0AMr15w1zVv0qMXi0//3qm9u3k6h1R6+nSmdAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# 13.2%
## MILD-MT 取栓組「嚴重操作相關併發症」發生率

輕症 LVO 取栓**功能獲益明確**（mRS 0–1：69% vs 50%）
但**技術門檻與病例選擇**同樣是成敗關鍵

---

<!-- _class: divider -->
# Lancet
## 肌鈣蛋白驗更快，急診並沒有更快
### PRESC1SE-MI 個人資料統合分析

---

# ⭐ PRESC1SE-MI 統合分析 — 0/1h vs 0/3h

## [Boeddinghaus J, et al. Lancet 2026](https://doi.org/10.1016/S0140-6736(26)01767-8)

| 項目 | 內容 |
|------|------|
| 設計 | 全部 5 個 RCT 的個人資料統合（IPD），**110,933 人次** |
| 族群 | 疑似心肌梗塞而至急診的胸痛病人 |
| Safety | 30d 死亡或新 type 1 MI：0.8% vs 1.0%，**OR 0.83（0.45–1.53）**（估計不精準） |
| Efficacy① | 急診停留：314 vs 308 min，**GMR 1.03（0.85–1.25）** |
| Efficacy② | 直接出院：67.0% vs 65.8%，**OR 1.31（0.79–2.16）** |

> **Take home**：更早複驗肌鈣蛋白**本身**不縮短急診停留、也不提高直接出院——要加速急診得動整個流程。對照上週 ICare-FASTER：換演算法沒用，換「落點／即時回報」才有用。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABjElEQVR42u1Yy23FMAwTmgE8klfPSB7AgCqSVt6pvbRAWeAFQeDPhWBoilbk18+O9+bPNlfUc2Fy410zRmIp5v6Ib56/2Cy0s4AWWiEUcoBfpmgL5FUMj3sP0HstTC9ntMVtQV2Y/gO0pYcVmwN+fdFCt4AazfA01i094QjgvL6e8DKzovSGBp4VR7T89UuDEGAiT1MljCK2eS6o8jFXtIJaIGViQbSuSkhChRu0HigD08ob7QMnIYDkCFu0e5BJoL0FW8nB2W8LMw2hBrSFka5KgFz3IRZKuGxPGT32KcFIYswJptwC6jzlgPRuLpqmGqItN0DEZfGVGGx1SxOo0pBEjuoQw9VvqdVoQ6gvoiPOnSe3k34bSuBNdYbpKUtlmGewaQuungBixXDKEPj1rQ686eiOs7u62WawzGb1JPOpHohvTjg1Ip5+gq0nnF7N0KUM9Op17tXo/rh1fdBZ8+3V3K/rubp2prrtzlJ3bJQbrXW7FGxmr/jm2+ieUpxr75SVOfdq3v343978BFCfjHbnbvR/AAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 術前策略 × 術中幾何 × 長期耐久性

---

# 🫀 PCI 要不要先做？—— 統合分析

## [Boukhris M, et al. Cardiol Rev 2026](https://doi.org/10.1097/CRD.0000000000001508)

- 併 **NOTION-3／PRO-TAVI／ACTIVATION** 等 **16 研究、8,207 人**；主要終點 30 天全因死亡。
- **30 天死亡 RR 1.26（0.90–1.77）**、1 年死亡 RR 1.00（0.87–1.15）——常規術前 PCI **無死亡益處**。
- 大出血 RR 1.19（0.98–1.44）、重大血管併發症 RR 1.48（0.95–2.30）偏向「不先 PCI」。
- NOTION-3（FFR 陽性／≥90% 狹窄者有益）與 PRO-TAVI（deferral 非劣、出血更少）方向相反。

> **Take home**：依冠狀動脈複雜度、病灶重要性與出血風險**個別化**，而非一律先打通。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABiElEQVR42u1YQWoEMQwznQfkSf66n5QHBFxb8k7pYfdSSlXYMMyGyUV4ZcmK5fN17H34s8Ntta7t1+73WWEr+5P5+bAX6y8OC60X6ivjmHGDd9Z3TbRVxmsq7Q175dRZF230X7+6qv8A7e5NgwRsZbRN1MaZN2OFeXtrwtejqwmzAvLVG1a7m04RbfRPy2wBNpDWSxxSmLcFD5oQeBLgU5O35QvVVqxtQhxaKJYoE0DXktko+aI7oPVcFO14WbCqRCvaZewpVBUEYNOlbG1zNNZvp2jSqvKWLjZdltCx5rCoJsBqwQR4BFTCReeEnJLSIFpvzYVrC9K2I8x8O2Yhy1sEHE6MD5XQ1dtvqmWjt0c0l3FUqNraUAJDjuw0TrFl2iUfDmmsiZbJcRSMOT1lNQHZweC/WBxplLPD5ujoZCzpoZzL4AgxIxmCpHDmZbqZAVJ3vr3vE3i5tAnVzkpttMk5wdrXTPoeDLzlcEuxTWnejk3AiOe6RlcTMm9fQzQL1ezwvnL/pcNPaY2bwf2+09cAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# 🫀 氣球擴張瓣「不對稱擴張」與晚期心衰

## [Ko T, et al. J Am Heart Assoc 2026](https://doi.org/10.1161/JAHA.126.049304)

- 前瞻登錄 589 人；不對稱指數 ＝[(最長/最短瓣高)−1]×100。主要終點 2 年心衰住院。
- 連續變項下與 2 年心衰無獨立關聯（adj HR/1% 1.02，0.98–1.06）。
- 閾值分析：**不對稱 >7.48% 者晚期（>30 天）心衰↑（adj HR 1.69，1.10–2.60）**，即使出院時瓣膜功能看似正常。

> **Take home**：術中透視的「展開對稱性」可能是傳統血液動力參數看不到的晚期心衰風險因子——釋放後多看一眼幾何。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABRElEQVR42u2YwQ0DMQgEUVyAS3LrlOQCLBF24S6vRMon2kes6OSLP6M1LHAWb9ax/8nHk225xl7HsI+98G7rPOzd+tUJYJJxbOANgK2R71uFDTwJMz03AULKqMNG6Wz6uDSU0q0CkHshNsRbuE2EGe5UKN46T++fUJ728stJ+nJF7vTcmxnnikCRO80ASwO5ICFdxp6IboN4oJqBDZ8a8eanCRc19PxHJ09RESbTYXpKV2Yi472GGMs1qyjoeEhrdYqQVVWnLpAK5gZCXG6osJGkeyTkBRoSGe+1QqpnJYKMv3UK3N47lDyEVDBe62z1ETq6OXWzytYyE6E+hGDUDdVBJxe6O4LLlbnpsK02NOhm1foemT6ktDJW1ZchK80yLAreQ43aDNh9CB1Yaq4nG9XzEJoBK0/t7kDqWpXmrP+XrK9OnmJsxRZbop22AAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# 🫀 瓣葉血栓（HALT）與 TAVI 退化（綜述）

## [Mazzinari G, et al. J Thromb Thrombolysis 2026](https://doi.org/10.1007/s11239-026-03412-2)

- HALT 在術後一年內發生率 **13–32%**；部分自行消退、部分持續。
- HALT 一年內**未必**造成血液動力惡化；10 年嚴重 SVD 率低（0.8–1.5%），但長期資料缺系統性連續 CT。
- 目前證據支持生物學關聯，但**尚不能證明 HALT 是臨床顯著 SVD 的因果前驅**。

> **Take home**：對把 TAVI 推向年輕／低風險族群的我們，耐久性仍是開放問題，需要連續 CT ＋標準化長期追蹤。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABQklEQVR42u1YQY4DIQyLlgfwJL6eJ/EApGxs0/bUSntZ+VA0GoXhYpnYSSbqzTrxPfl4sqPXQLjwnoV9rPMT79Z/nTS21RhHZYM8MxlXfzTB1iyNDdJigsuxY3hhQ3wCqAyxMd+yqbPCxntcQRWY5Rt1utfzMdKpFnnra325i0u+BTINOPOx9cAGVKCrXZfey62PTqlN5NhMGZ3RncJyUw5ccOBsDk20QPdYqFkUbOMcVrzJgZV12ybfKk+oFUnKAVsb3ghP14pOKcSeTb6lygEIpC6MeGOhh/E+/M2pDwkVrLj2Wz46JWM5rtHBUlzyba9nUaC/ITbrQ+LOMjRhm1nmzlkxZXTsyY3yrdRVHpVUBlbzgkThlW8vbCF/U09iNZ/WraR57c5prqeN8M8DBvxymrPuG4KVmfj42/dP1t9OfgGaENUnXrS31wAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 加夾片 × bailout × 團隊輻射

---

# 🔧 多夾片治療殘餘 MR（Cedars-Sinai）

## [Chehab O, et al. J Am Heart Assoc 2026](https://doi.org/10.1161/JAHA.126.050013)

- 826 名第一個夾片後仍有中度以上殘餘 MR；單夾片（113）vs 多夾片（713）。
- 多夾片組 **MR 降更多、跨瓣壓差較高**；技術成功與併發症相當。
- **1 年「死亡＋心衰住院」16.8% vs 29.2%（P=0.002）**，NYHA 改善更大更持久。
- 即使「中度」殘餘 MR，加夾片也和較少 MACE 相關。

> **Take home**：第一夾片後仍有顯著殘餘 MR 別急著收工——加夾片改善硬終點，代價是壓差略升，在「殘餘逆流 vs 殘餘狹窄」間拿捏。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABS0lEQVR42u1YsQ3DMAwT6gN8kl/3STlAgEtSTtAlHToUHGIYQWIvBCVSUmLdrIzn5uvNEVgNz74aDvrid4x8xd361w2wDWBsxxC2iU8gxNMEG1gCKlBHYNyg0QmbICWD64dtLcQUyZbhhY35xpSDYmbhtMm30um4tpFOa4E9boLc7mKSb32GMg2QSrPpwhuBkTFm3STOGC75Br+VudHiGExiI40eWiBLfW3r6AyoD28ykKHqKkXoxIQ3WS6KAkWBl2C5d+Et++m9Cq4TtnKPWS7HkqpOySSmrfoillSIlBXfBZs8pBBm0VhW7FIXlvreebW+LjpVvmUp9CPELjFV71EqqEMf3k6F7lqvrsmqf6tQzup7bTxkz1mpDqR488G254WQ8SqgbTlhO67CKpczmwFDlaumLbM5a7eU4aWFPWedE41TrX/+V/1y8waK0NwdIa1h0wAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# 🔧 Snare 輔助取出「鎖死在開啟位」的夾片

## [Jariwala P, et al. Catheter Cardiovasc Interv 2026](https://doi.org/10.1002/ccd.70957)

- 54 歲擴張型心肌病、嚴重 MR；第二夾片**機械鎖定失效**，外翻拉回左心房仍開啟、關不起來。
- 以 **snare（抓捕器）輔助**先讓夾片臂閉合再撤出，**免第二次中隔穿刺**、降低撕裂房中隔風險。
- 隨後成功補打夾片、顯著降低 MR。

> **Take home**：夾片「鎖死在開啟位」雖罕見，關鍵在「撤出前先讓臂閉合」——避免開臂硬拉撕裂組織。這類 bailout 思路值得每位 TEER 術者先想過。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABTklEQVR42u1YO25DMQwT6gP4SL66j/QOYEDlx+mWDh0KDjGCwIEXghJFKtVvzqnPy68vT+GM7vHgvk4t/q51vurd+a8X4gHG0bt712zdmyAzsIEl4Dlzg0MTOLKwbUACb6hpIDZ2nVBFYWOPUQUlhCup36RT0nU/QTq9Zx933c90yagpFIoeOxJC65KDrSZIK07dySnHWZejBfWYKwt4Q0M4RAuDUqVCAYnfuoRgA18cHSSwXNOT46dP2a3YdWAsRwskTTba1+hpXjG82QhsqQIm9iJ420CC5jc2t18QtqKZOrzRwmbgfNsvbH1i/LRoVXYrw1tBM0QzzenIIh0xM+SW0vdb4qT8pl3GqxZzZopn3dzLNPKKSSMnIzmHQxQKcpZGELanrilMLjUxOeTuWXL8ZV1k7VkMIUs1VXiLyW/eTFvU+cT46ef/qj+8fAOs2ugsc8I70AAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# 🔧 結構介入：超音波醫師輻射比術者更高

## [Haga Y, et al. Radiol Phys Technol 2026](https://doi.org/10.1007/s12194-026-01161-8)

- 前瞻量測 37 例結構介入（20 MV-TEER、17 LAAO）；EC 與 IC 各戴 2 個半導體劑量計。
- **EC/IC 單次事件劑量率比：透視 2.3、cine 3.8（皆 P<0.001）**。
- X 光輸出、C-arm 角度、source-to-detector 距離、個人遮蔽皆為獨立決定因子。

> **Take home**：TEER／結構介入的輻射防護不能只顧術者——站在病人旁的超音波醫師暴露更高（尤其 cine），要給 EC 專屬遮蔽並逐案優化 X 光輸出。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABOElEQVR42u1YsQ3DMAwT6gN6kl/3STrAgEpSTrZ26FBwqBEYSJyBEClSSdSbteN/8vEkA2skXln7WZWT9zH3I96tX50A2wTGAWBAyH2OIkITbCE8KBoLCJyJMjphyzkuTv2wUXL7uYYZthKPWx1hprfu03lfRn3ai4RWgNPbXUw4Va0aGyTXD03qRkggUfC8vLfII8BIeKzh7t2F04Pw7OpWE07b1trlwK+elAmnVFdMNQKLNtIo67esg5F65LdGGnGqUaRUMYnNaUYKCOxKVSO95XE2tsPlbz59Ckg9VdLfyOz00dsZPIhN8Zo+eqPGOuK7F6zytOcQmUl19LvNb/Rbhb7d3Ksk7fDqAnp9yyhMvfR2vgGFCgGhMrphOxNvrZP+RnrrXFh3R7j1aV3+ZjO//f9XfXHyAlAp2BIMUhwVAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
### EHJ ／ JACC ／ Circulation

---

# 📚 Honorable Mentions (1/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| **JACC 綜述 — hs-cTn：偵測不等於診斷** | 偵測已解決，分類（type 1/2/慢性損傷）才是難題；不能交給演算法 | [DOI](https://doi.org/10.1016/j.jacc.2026.09.019) |
| **EHJ Great Debate — 雙生物標記** | copeptin＋troponin vs 單用 hs-troponin，能否更快安全 rule-out MI | [DOI](https://doi.org/10.1093/eurheartj/ehag090) |
| **EHJ — 重新思考 factor XIa** | 針對上週 LIBREXIA-ACS 落空的評析與定位重估 | [DOI](https://doi.org/10.1093/eurheartj/ehag863) |
| **EHJ 綜述 — 皮質醇與 CKM** | 難控 T2DM 24%、頑固高血壓 27% 有隱性高皮質醇；可逆殘餘風險 | [DOI](https://doi.org/10.1093/eurheartj/ehag827) |

---

# 📚 Honorable Mentions (2/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| **SMART-CHOICE 3 次分析** | DAPT 後單用 clopidogrel：高缺血風險者減 MACCE（HR 0.67），出血相當 | [DOI](https://doi.org/10.1161/CIRCINTERVENTIONS.126.017277) |
| **LAAO 多模態影像指引** | 左心耳封堵全程影像框架；Watchman／Amulet 差異、DRT／leak 分類 | [DOI](https://doi.org/10.1161/CIRCIMAGING.126.020263) |
| **REFINE PET — LVEF reserve** | 34,976 人：負的 LVEF-R 與死亡梯度關聯，預測左主幹／三血管病變 | [DOI](https://doi.org/10.1161/CIRCIMAGING.126.020062) |
| **SGLT2i 的電生理效應（綜述）** | 改善自律神經平衡、減 AF／SCD 的機轉（late Na、microRNA） | [DOI](https://doi.org/10.1161/CIRCEP.126.015246) |

---

<!-- _class: divider -->
# 🔬 Case Reports
### 介入救援 × 心電圖 × 腫瘤心臟學

---

# 🔬 Case 1 — 骨水泥栓塞右心房＋肺栓塞，經皮取出

## [Gülaşti S, et al. Catheter Cardiovasc Interv 2026](https://doi.org/10.1002/ccd.70967)

- 72 歲女性，椎體成形術 1 個月後胸痛、低血壓、AF；超音波見右心房游離高回音線狀物。
- CT：骨水泥鑄型自 L2 經下腔靜脈延伸入右心房，遠端肺動脈亦有栓子。
- 以**三葉抓捕器＋球囊輔助**成功經皮取出，避免開心手術。

> **教學點**：椎體成形術後的心內異物／肺栓塞雖罕見但可致命，選對病人時經皮取出是安全有效的替代方案。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABTUlEQVR42u1YQY4DMQhDOw+YJ+XreVIegERtQ7unrtTLyoeiUZVpLhbYBibqTWR8b/68OYG4aseNp/IuvsfKn3gX/3UDbAsYga0AjyBxLvxpgg1Zug5Su5E0YjtxmWHDL8oKVH7Y1kX2BShnha1URyAsss6Kb9LpWa/HSKcdz8r+uosL3+hvKu5+vpZNTVdKAhACHRjEs+GbesGSSHcL1qamLGjeu70XAYQ4mGBrjqUK2qxz4ZvaKPKWYp2814Zv1KZON/sC6+ukU2VMHeGsAebCtzX8l1Qlh23kby0BCnb8zafXI2Pq76RcqaA2eRPZ6MDMnlJnxLfsOaRKA4mGTK85ZFSgZuqzy8ye1XNvaj734Vs7m5xkmoLT/DYTL21klhovbCEn6YHEZ3cebD2HqPWHU8+avZ7tnlrwmd96z8qYTWGK6+Nv3y9Zn908AMkc2LSU1U4bAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# 🔬 Case 2 — IVUS＋dobutamine 決定異常 RCA PCI

## [Votsis S, et al. Catheter Cardiovasc Interv 2026](https://doi.org/10.1002/ccd.70965)

- 54 歲 NSTEMI；右冠狀動脈起自左冠竇、走「惡性」動脈間走行。
- 術中 **IVUS＋dobutamine 激發**，峰量時證實開口與動脈間段皆顯著狹窄。
- 據此對兩處都做 PCI，結果良好。

> **教學點**：異常冠狀動脈「要不要處理」靜態影像難定奪；動態激發＋腔內影像能回答「機轉」並量身決策。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABR0lEQVR42u1YwY3DMAwTzgN4JK+ukTKAAR1pKm0/LXCfAx81iqCOP4QoknKi3qwd35OPJ1dgjapRGbP2LO5j7Z94t/7rBNhWERhgPkAWXppgQ5XGFXsmikZsVwwzbKhWzAQqQ2woGmmdXnUr8UhtZHn125EAqeyfkU61UCgyu57u4tJvIDSb0956YKtExcQshACpBrc2OqU2wWa2h/hwCkitVnqvXI5+4qKFO0lnCuSw0QL6DYFFHgnv8GvjbydDmQ77CHab6ZRSRac1vHLpN4X7SSsAO3Lw6TeVjjPSqPY3n6y/J14+pQgfnVZPIHlwlvzExUPIY2gCGQyv5TaHyHWjs9VpfqNIaSBnUgqrfiOVL6HgNL8ttRkzQv02vbBpvDzBmj53Z5ltdOKnhkyve73Gtsd90OmehT8Kepaxysjfvl+y/nbyC/n+5RQKk4m9AAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# 🔬 Case 3 — 南非國旗徵象不一定是阻塞性 MI

## [Wagner Useche MA, et al. JACC Case Rep 2026](https://doi.org/10.1016/j.jaccas.2026.110880)

- 74 歲女性，情緒壓力後急性胸痛；心電圖呈 South African Flag Sign（典型連第一對角支阻塞）。
- 急診冠狀動脈攝影為**非阻塞性**；超音波與 CMR 證實 **Takotsubo**（心尖氣球樣，LVEF 36%）。
- 藥物治療後恢復。

> **教學點**：高風險 ST 段等義徵象提示要緊急再灌流沒錯，但「徵象 ≠ 一定有血管阻塞」，兒茶酚胺風暴能完美模仿。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABjElEQVR42u1YsW0EMQwT4gFuJK/ukW4AA4pIyv+fImmCICzeuMI+N4RAkZQjv1873pe/u7yj1sgcOM19rbgSv2r/ET+s/7gstLNQj/txBM5CXv890QLeHVXVfeVGYXEczmjJBG0KsD/azIXvEMMWbbKwxVhw9Vqjj55oqQn3fP18NaEXaCACPOXNEW0J7GJzFWljH/ylup68hXDFQ8coYoX/NmUCudo4R7aXpTHatjMaRNB/t6nzgqu1NpgwJWLbt7bVYuivUD3hFKywZ5chehVUuAPMt5SBgjDSVBPgYqe5BlW3Nc3UHZZywmk02oQr2hBdKWIiA/a+abw9l2FskcnTtcuW0pfYKyNrgzNVMDlCCnn/NM63mh/ZZWk9l1FdwVImGcmCcb5FSZuxai5FR9fE+HxAYAzTkL6dZwcJLLNNQaU+pO9chslxPfgwbBXsy1sN3EG19X5PkJ2x3Qjb9h1MExlS4j3P211ub7QN+Jivb77laKZxLDVRxrR+qzkxbPd+Gqfx93v8X1x+AgJojKxyTQPHAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# 🔬 Case 4 — ICI 心肌炎：早診斷、延遲治療、猛爆

## [Ozaki K, et al. JACC Case Rep 2026](https://doi.org/10.1016/j.jaccas.2026.110981)

- 60 多歲女性黑色素瘤用 pembrolizumab；第 9 週前**無症狀** cTnI 升高（93 pg/mL），CMR 已符合心肌炎。
- 因無症狀＋數值輕升而**暫緩免疫抑制**；一週後猛爆（cTnI 4,115 pg/mL），需 ICU、類固醇脈衝、暫時性循環支持。

> **教學點**：ICI 心肌炎即使起初無症狀、數值不高，也可能迅速猛爆；診斷後仍要持續風險分層、及早介入。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABhUlEQVR42u1YQY4DIQyLlgfMk/g6T5oHREpjG6peupdVtT4UoVGAOVjBcRKi3o+M7+HfDu/oMW78NbAx8ypstfETv4z/OGy0Ezjv2fAaM6HOht37nmg3zl5chI1ve9saLa7+Wu3b3rFH2y5dKSOs0TK+VqOtWooyY95KE+br9NUEjfYwZtDDR94c0S7pQIqutRRlrr5tHSBCwiZjQ+A9o2zUFliBry25pr7tS+cXyOVnGK6+7ciCRb0tShnYaxpllUcHQNpmLw3X7IA5zu1rmbZRpvwVwXQGP/eXRplm3mfdRVbIsOXt2O4FDRhfy1dvqygCSAoSW0WZbS4TXSVlSmRQYNeKMXfLsFQ3gsNIx65VDXkbnKQBYdt2kay4ngW5dVXD5JXU2HHSbhrrrQpFkSH5tsCOsox7h8j9BsKSDEvnvizqNA5qgb17Xj0rBTOvd3173pSAE/0O9q3RMsqUfOlbb7T06klqVeZvNbx9NDvk7bhdFUyaUCrDdp/uG2XfJ/dPHT4Aoi+Q7VcWgekAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# 🔬 Case 5 — KRAS 抑制劑後 NBTE 與新發嚴重 MR

## [Villa-Etchegoyen C, et al. JACC Case Rep 2026](https://doi.org/10.1016/j.jaccas.2026.110900)

- 76 歲轉移性胰臟癌，用 KRAS 抑制劑 daraxonrasib 後漸進呼吸困難。
- 超音波見**新發嚴重 MR**＋瓣葉增厚＋寬基底回音團；併肺栓塞、反覆冠狀動脈血栓、血培養持續陰性。
- TEE 證實雙瓣葉受累，改用低分子量肝素。

> **教學點**：癌症病人新發 MR＋血栓事件而無感染證據，要想到非細菌性血栓性心內膜炎 (NBTE)；與 KRAS 抑制的時間關聯值得注意但未證實因果。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABj0lEQVR42u2YUWoEMQxDTXOAOZKvniPNAQKuJSWzX+1PC1Vhw7DMJj/CaJ4cR329VrwPf3Z4R69Rc10V1+y/vY2tyPUR36y/OGy12fLGnS24FVJ59dP7nmpbpKS2yC5vXC0+hrPaGy+oahvjf6iN1TaQbGO1JaNizccSrr4lE1DP1+PLBK22QROsFfLZeHNUO49dVecsmBbiPX2LD+qaqCp+wQQI9qwtkDUhWB8XgsyaCYxdPcUg44un2lJ47WiQ4N5x9S0E88tKoSxoYFMmwLGwbiukzlIE+6plJdk/orZCmW+fgL6L7GJYvF48v7LNsdpYOPnrmbzqEmXaoIc3gT2ZgF4xya6pe4RxlqnpIrhEMPKhfGtLLKiZiXjaMFeCKW3hVV14h7zheXegUZUR7HVTAeHphKV5wrmUhTVv993hyTIyIcO1q9kTj0MD9re2anMHBP2gttyZtyrmEA12n5C2TNjTDzYM6BgPzZznYOxsz7xR0WY8YxQfEMHXMYMzE/ZENIemCs68fc/jf//wE/HhfHfKGmvOAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 💎 Take Home Message
### 本週 7 大臨床啟示

---

# 💎 Take Home Message

1. **取栓時間窗往外推，但風險一起算**：LATE-MT 24–72h 取栓改善功能（common OR 1.74），代價 sICH 4.8% vs 0、死亡 6.0% vs 1.8%。
2. **輕症 LVO 不等於不積極**：MILD-MT mRS 0–1 69% vs 50%（OR 2.32），未增顱內出血，但 13% 嚴重操作併發症。
3. **「驗得快」≠「急診跑得快」**：PRESC1SE-MI 統合（11 萬人次）0/1h vs 0/3h **不縮短停留**（GMR 1.03）；要動的是整個流程。
4. **TAVI 前常規 PCI 無死亡益處**：統合分析 30d 死亡 RR 1.26，應依複雜度與出血風險個別化。
5. **TEER 第一夾片後別急收工**：加夾片 1 年死亡＋HF 住院 16.8% vs 29.2%，代價壓差略升；記得 snare bailout。
6. **結構介入輻射團隊一起扛**：超音波醫師 cine 劑量率達術者 3.8 倍；TAVI 耐久性（HALT→SVD）仍開放。
7. **肌鈣蛋白的命題是「分類」**：偵測非問題、分類才是；Case 旋律＝別被表象騙（SAFS≠OMI、無症狀 cTn 可猛爆、癌症新發 MR 想 NBTE）。

---

<!-- _class: ref -->
# 📖 完整參考文獻 (1/2)

**NEJM**
1. Yang P, et al. Mechanical Thrombectomy 24–72 h after Large-Vessel Stroke (LATE-MT). [N Engl J Med 2026;395(16).](https://doi.org/10.1056/NEJMoa2609362)（PMID 42929656）
2. Liu J, Yi T, et al. Endovascular Therapy for Mild Stroke with LVO (MILD-MT). [N Engl J Med 2026;395(16).](https://doi.org/10.1056/NEJMoa2609149)（PMID 42929671）
3. Editorial: Expanding Indications for Thrombectomy. [N Engl J Med 2026;395(16).](https://doi.org/10.1056/NEJMe2612692)（PMID 42929679）

**Lancet**
4. Boeddinghaus J, et al. 0/1 h vs 0/3 h troponin pathways: IPD meta-analysis. [Lancet 2026;408.](https://doi.org/10.1016/S0140-6736(26)01767-8)（PMID 42956796）
5. Cullen L, Greenslade J. Faster troponin, same time in the ED (Comment). [Lancet 2026;408.](https://doi.org/10.1016/S0140-6736(26)02097-0)（PMID 42956795）

**EHJ / JACC**
6. Spanos M, Januzzi JL. hs-cTn: Detection Is No Longer Diagnosis. [J Am Coll Cardiol 2026.](https://doi.org/10.1016/j.jacc.2026.09.019)（PMID 42949674）
7. Giannitsis E, et al. Dual biomarker strategy for ACS triage (Great Debate). [Eur Heart J 2026.](https://doi.org/10.1093/eurheartj/ehag090)（PMID 42954950）
8. Liuzzo G, Patrono C. Rethinking factor XIa inhibition after ACS. [Eur Heart J 2026.](https://doi.org/10.1093/eurheartj/ehag863)（PMID 42958932）
9. Khan MS, et al. Cortisol in cardio-kidney-metabolic disease. [Eur Heart J 2026.](https://doi.org/10.1093/eurheartj/ehag827)（PMID 42946534）

---

<!-- _class: ref -->
# 📖 完整參考文獻 (2/2)

**Circulation**
10. Lee JM, et al. Clopidogrel vs Aspirin by Atherothrombotic Risk (SMART-CHOICE 3). [Circ Cardiovasc Interv 2026:e017277.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.017277)（PMID 42953942）
11. Motairek I, et al. Multimodality Imaging for LAA Closure. [Circ Cardiovasc Imaging 2026:e020263.](https://doi.org/10.1161/CIRCIMAGING.126.020263)（PMID 42948875）
12. Hijazi W, et al. LVEF Reserve & Mortality (REFINE PET). [Circ Cardiovasc Imaging 2026:e020062.](https://doi.org/10.1161/CIRCIMAGING.126.020062)（PMID 42948888）
13. Ashok V, et al. Electrophysiological Impact of SGLT2 Inhibitors. [Circ Arrhythm Electrophysiol 2026:e015246.](https://doi.org/10.1161/CIRCEP.126.015246)（PMID 42948880）

**TAVI / TEER**
14. Boukhris M, et al. PCI Before TAVI: Meta-Analysis. [Cardiol Rev 2026.](https://doi.org/10.1097/CRD.0000000000001508)（PMID 42951893）
15. Ko T, et al. Balloon-Expandable Valve Asymmetry & HF Post-TAVR. [J Am Heart Assoc 2026:e049304.](https://doi.org/10.1161/JAHA.126.049304)（PMID 42960753）
16. Mazzinari G, et al. Leaflet Thrombosis & TAVI Degeneration (review). [J Thromb Thrombolysis 2026.](https://doi.org/10.1007/s11239-026-03412-2)（PMID 42961731）
17. Chehab O, et al. Multiple-Clip Implantation for Residual MR After TEER. [J Am Heart Assoc 2026:e050013.](https://doi.org/10.1161/JAHA.126.050013)（PMID 42960822）
18. Jariwala P, et al. Snare-Assisted Retrieval of Locked-Open TEER Device. [Catheter Cardiovasc Interv 2026.](https://doi.org/10.1002/ccd.70957)（PMID 42949126）

**Case Reports**：PMID 42960444 / 42960428 / 42961397 / 42955044 / 42955042（連結見講義）

---

<!-- _class: abbr -->
# 縮寫對照 (1/2)

| 縮寫 | 全稱 | 中文 |
|------|------|------|
| LVO | Large-Vessel Occlusion | 大血管阻塞 |
| EVT | Endovascular Therapy | 血管內取栓治療 |
| NIHSS | NIH Stroke Scale | 美國國衛院中風量表 |
| mRS | modified Rankin Scale | 改良 Rankin 量表 |
| sICH | symptomatic Intracranial Hemorrhage | 症狀性顱內出血 |
| OR/HR/RR | Odds/Hazard/Risk Ratio | 勝算比／風險比／相對風險 |
| hs-cTn | High-sensitivity cardiac Troponin | 高敏感性心肌肌鈣蛋白 |
| MI / OMI | (Occlusion) Myocardial Infarction | （阻塞型）心肌梗塞 |
| ED / LOS | Emergency Dept / Length of Stay | 急診／停留時間 |
| IPD | Individual Participant Data | 個人參與者資料 |
| TAVI/TAVR | Transcatheter Aortic Valve Implantation/Replacement | 經導管主動脈瓣植入／置換 |
| PCI / FFR | Percutaneous Coronary Intervention / Fractional Flow Reserve | 經皮冠狀動脈介入／血流儲備分數 |

---

<!-- _class: abbr -->
# 縮寫對照 (2/2)

| 縮寫 | 全稱 | 中文 |
|------|------|------|
| HALT | Hypoattenuated Leaflet Thickening | 低衰減瓣葉增厚 |
| SVD | Structural Valve Deterioration | 結構性瓣膜退化 |
| TEER / MR | Transcatheter Edge-to-Edge Repair / Mitral Regurgitation | 經導管緣對緣修補／二尖瓣逆流 |
| TEE | Transesophageal Echocardiography | 經食道心臟超音波 |
| NYHA | New York Heart Association class | 紐約心臟學會心功能分級 |
| LAAO / DRT | Left Atrial Appendage Occlusion / Device-Related Thrombus | 左心耳封堵／裝置相關血栓 |
| DAPT / MACCE | Dual Antiplatelet Therapy / Major Adverse Cardiac & Cerebrovascular Events | 雙重抗血小板治療／主要不良心腦血管事件 |
| CKM / T2DM | Cardio-Kidney-Metabolic / Type 2 Diabetes Mellitus | 心腎代謝／第二型糖尿病 |
| PET MPI / LVEF | PET Myocardial Perfusion Imaging / LV Ejection Fraction | 正子心肌灌流造影／左心室射出分率 |
| ICI / NBTE | Immune Checkpoint Inhibitor / Nonbacterial Thrombotic Endocarditis | 免疫檢查點抑制劑／非細菌性血栓性心內膜炎 |
| SGLT2i / EC / IC | SGLT2 inhibitor / Echocardiographer / Interventional Cardiologist | SGLT2 抑制劑／超音波醫師／介入心臟科醫師 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

2026-10-23 ~ 2026-10-30｜6 大固定欄目

> 本講義為讀書會共筆之教學整理，僅供醫療專業人員教學與學術討論參考，不構成個別臨床決策建議。所有數據以原始文獻為準。
