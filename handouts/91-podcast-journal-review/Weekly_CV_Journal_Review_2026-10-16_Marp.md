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
  section.lead blockquote { color: #2d3436; }
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
  .qr {
    position: absolute;
    right: 40px;
    bottom: 80px;
    text-align: center;
    font-size: 0.65em;
    color: #555;
  }
  .qr img { width: 110px; height: 110px; border: 1px solid #dcdde1; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-10-10 ~ 2026-10-16'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-10-10 ~ 2026-10-16

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Pick／文章附 QR Code，可掃描跳轉原文

---

# 🎯 本週主題與固定欄目

## 表型與場域的精準化

**一句話**：同樣的治療，用在**對的場域、對的表型、對的病人**身上才有益。

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 結構性主動脈瓣方向
3. 🔧 **TEER Section** — 二尖瓣緣對緣與瓣膜介入
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — 結構／冠脈／EP × 5
6. 📖 **參考文獻 + 縮寫對照**

---

# ⭐ Top 5 Picks

| # | 試驗／研究 | 期刊 | 關鍵數字 |
|---|------------|------|----------|
| 1 | **SUBCUT-HF II** | *JACC* | 30 天 DAOH **多 4.0 天**（p<0.001） |
| 2 | **RELIEVE-HF**（表型） | *JACC HF* | 裝置相關 MACNE **0%**；HFpEF 反而有害 |
| 3 | **ICRAKI** | *NEJM* | IHD 死亡 **HR 1.30**（1.04–1.63） |
| 4 | **DCM 基因型**（SHaRe） | *Eur Heart J* | 高致心律不整基因 MVA **HR 3.25** |
| 5 | **CAUGHT-CAD** | *JACC Imaging* | 高密度鈣 β=0.79；非鈣化斑塊退縮 β=−9.83 |

---

<!-- _class: divider -->
# Pick #1
## SUBCUT-HF II
### 皮下 furosemide 微幫浦讓心衰病人提早出院

---

# SUBCUT-HF II — 設計

**Campbell RT, et al.** *J Am Coll Cardiol* 2026;88(15):1781-1793.
🔗 [DOI: 10.1016/j.jacc.2026.07.047](https://doi.org/10.1016/j.jacc.2026.07.047)

- 多中心、開放標籤、隨機、active-controlled（英國）
- 住院心衰、仍需腸胃外利尿劑者，n = **172**
- 介入：可穿戴、病人自操作之**皮下 furosemide 微幫浦**提早出院 vs 常規住院
- 主要終點：30 天**存活且不在院天數 (Days Alive and Out of Hospital, DAOH)**

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKUAAAClAQAAAAAVUAB3AAABVElEQVR42t1XsY3EMAzjfQqXHiGb5BcLkABZLNnEI7h0cYiekv676x684lQIdhqBFkkpsBcx8CFfTwDlxMpTfc68YB5feBX//wq7WLQwtXLXw4rZU1qtYy6ERex9Mkcpr3azGmN7T7WLsIjNUYqred8cW4mTuG/ByauvcyQ1JzP6ivGwfU5dKF9yT4KMpe7ZRilLUtjIR3yQL+JqYI02vvtm8KTsG7lht8PiczYjO6UsCQep5rAmJrFz2WHmrjwWJqpbypKb5uGaxkA9Gjso9pIwZFrkr31Jq93VHNHGRHVTdFJ1n5xq0TyXAU9avZ10EMKyRmHn7NG6MlXmzaMCeF+wibE5IkufZEhfMsLVHS+ZJ/V8c70tiA1FPHFi5yInFxIkrvKdy00rJx0Foa8G5+Tqs1u/TxpthOSfUnTqvhn7xr3kaCbe8P52LsRoK2KWfO4f1Q/p0vNExw7iDAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# +4.0 天
## 30 天 DAOH（提早出院 vs 常規）
### 95% CI 2.1–5.8｜p < 0.001

住院縮短 **5.5 天**；裝置相關問題 3%、無嚴重事件

---

# SUBCUT-HF II — 臨床啟示

> 把「排水」從病房搬回家，用病人中心終點（DAOH）證明**心衰「去住院化」可行**。

- 對**利尿反應良好、能被密切追蹤**的病人尤其適合
- 心衰再住院數值上略多（14% vs 6%，OR 2.45，**NS**）

> ⚠️ **務實界限**：由裝置／藥廠（SQ Innovation）支持、開放標籤、n=172；需配套居家追蹤，台灣尚無給付路徑。

---

<!-- _class: divider -->
# Pick #2
## RELIEVE-HF
### 心房分流器：HFrEF 安全、HFpEF 反而有害

---

# RELIEVE-HF — 設計與結果

**Rodés-Cabau J, et al.** *JACC Heart Fail* 2026.
🔗 [DOI: 10.1016/j.jchf.2026.103375](https://doi.org/10.1016/j.jchf.2026.103375)

- 隨機試驗之**預設 LVEF 分層安全性／耐久性分析**（主試驗整體中性，win ratio 0.86、p=0.20）
- 植入成功 **99.7%**、2 年通暢 **99.4%**、裝置／手術相關 MACNE **0%**

| 表型 | 安全性 |
|------|--------|
| **HFrEF** | 無超額不良事件、嚴重事件更少 |
| **HFpEF** | 出血↑、腎惡化↑、全因 MACNE↑ |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKUAAAClAQAAAAAVUAB3AAABTUlEQVR42t1XO66EMAycPApKjpCbsBdDChIXg5vkCJQpEN6xs+V2T0OxLiKgGXk+joF9qYYf+boDGA+70F52Zb4gtz98q/9/hR0EHW8sGO9ps9EIqUQ7kUc7CyEn4u5Y5Gg8vMsrP4Q21DYTSI5mwd9QyeSa1bp1T55LjkPtySgyaXajfHKhZNJT5iTu01b5pGWSKTOjJ8MlaiZpQiCZ1ZbcIEmeboRuZJJN7uRU2ttQ2dvWY0C8TemSG4PrtoRuIKQ4Ad2JaOks1edzlvYWxjTzGBDSVq1LCoEQLrmg1i3G8IxSP3nTetKrPyafzz4spWhrDt163g4T5w25t8VgQz0no9hWbS+SGENafb/5vIKb/5G723xd8GDzVZqAvpcYJZsf0O3obZUKz5s9sU/6aGZbVn2Q6XdlusT8aLP6fov/gC02PNdN6pLf/aN6A/Qu4tQB9IoXAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# RELIEVE-HF — 臨床啟示

> # 心房分流**不是「心衰通用」裝置**

- 裝置本身**耐久可靠**，問題在「用在誰身上」
- **HFpEF 要特別審慎**（出血與腎惡化增加）

> ⚠️ **務實界限**：次群分析、整體試驗中性——不可解讀為「HFrEF 該裝分流器」。

---

<!-- _class: divider -->
# Pick #3
## ICRAKI
### 重症 AKI：間歇性 vs 連續性腎替代療法

---

# ICRAKI — 設計與結果

**Gaudry S, et al.** *N Engl J Med* 2026 Oct 14.
🔗 [DOI: 10.1056/NEJMoa2608397](https://doi.org/10.1056/NEJMoa2608397)

- 多中心、開放標籤、**非劣性** RCT（法國）；重症 AKI 有 RRT 指徵者
- 起始模式：**間歇性血液透析 (IHD)** vs **連續性腎替代療法 (CRRT)**
- 主要終點：90 天主要不良腎事件 (MAKE)

| 終點 | IHD vs CRRT |
|------|-------------|
| 90 天 MAKE | 78.1% vs 71.6%（差 6.28%，CI −1.22~13.79） |
| 90 天死亡 | **HR 1.30（1.04–1.63）** → 提早中止 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKUAAAClAQAAAAAVUAB3AAABU0lEQVR42t1XMY6EMBAbjoIyT+An8DEkkPgY+5M8IWUKlDl7srpqu5MpNkUU0lgej8fB/MOq9iW3l5lN7jdO6Z7xYXP9sU/r/7fmL4BOLz9sIhpxpWjFZqCB1lq2ebpsewDN3Rbb/RG0BiBvNurRqJujiOgSnrS6RU++KBk3dU/Givqtf75QOwDi1QGmmyieuJLekudexKFo0dIdupkt3d2u5YZ2bOnM7mXPgJSiNXAzSwdPp9uqdQBp1YWSrWXMnJhaB5zvnoQDcjVMFSk3z7DB6X3jVJF2CevHvh+I1rTcUETaAH5bYGwbinRyXeiSjjFEGiRxmkIo0MpAg99W9Zw8ZnDbUUTMSXUlewako4dNhJw631q4GyyR3bs8cYgWQytMp36XAJENcnBi6l94fL2G3+Du7QG0oBWROsp187dk2cUvvOhJbpVBGs5T++0r/6h+Aaps9ABvBrD2AAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# ICRAKI — 臨床啟示

> **血流動力學不穩**的心臟重症併 AKI，**CRRT 作為起始模式可能較安全**。

- IHD 未達非劣、死亡率較高
- 穩定病人仍可個體化選擇 IHD

> ⚠️ **務實界限**：開放標籤、單國、非劣性設計（非證 CRRT 優越）、提早中止可能高估效應。

---

<!-- _class: divider -->
# Pick #4
## DCM 基因型與心律不整
### SHaRe 登錄：基因獨立於 LVEF 分層

---

# DCM 基因型 — 設計與結果

**Padalia K, et al.** *Eur Heart J* 2026 Oct 13.
🔗 [DOI: 10.1093/eurheartj/ehag648](https://doi.org/10.1093/eurheartj/ehag648)

- 國際 SHaRe 登錄；擴張型心肌病 (DCM)，n = **2,660**
- 依致病／可能致病變異分：高致心律不整基因 / 低致 / gene-elusive

| 終點（vs gene-elusive） | 高致心律不整基因 |
|------|------|
| 重大心室心律不整 (MVA) | **HR 3.25** |
| **LVEF ≥ 50% 仍** | MVA **HR 2.36** |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKUAAAClAQAAAAAVUAB3AAABSElEQVR42t1XMQ6DMBAzzcDIE/IT+BgSSP0Y/CRPYMyAuPoujN0qMzTDqWSxfPY5V9iXU/EntxuAfj8Ws93exg/k+sK38/stiGHWbwOLw7OcUrQDub+wFBJMxMUsR9ttBSH56wk0c8k6W/VooZY38UKS63Z7cs5R1J6Msw1nNm9imwulbqlgJCNnSXcOq1a3d6lhkMDttLrRjoVOXIp5QUe/KF3C1rGdS6kTuVU1t2MGJha73CpMFSW3sIXrVkf/ng7pBHgn+xDPc1KN5hHZmmgelp5hWt0ynUg7khYqBi1am7czE40GGZG0WcKnzRoQS0AqO5m4JHgqMyzbziCegHve2o2Wm5/dzpbKUR5535wl2yn15L1zrYhAiWF/Yi/hqJ3g5EGO5twAp0VIPRqXhFiFOG/6nSvMP5neJeHJML+/dPJU/tt/VB8RVO8rVIYx1QAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# DCM 基因型 — 臨床啟示

> **DCM 病人應積極基因檢測**

- 高致心律不整基因（**LMNA、DSP、FLNC、RBM20、PLN、SCN5A、DES、TMEM43**）
- **即使 LVEF>35%** 也要加強監測、提前討論一級預防 ICD

> ⚠️ 觀察性登錄、各基因事件數不均，具體 ICD 門檻待前瞻驗證。

---

<!-- _class: divider -->
# Pick #5
## CAUGHT-CAD
### 鈣化密度上升 = 斑塊穩定化

---

# CAUGHT-CAD — 設計與結果

**Vasanthakumar SA, et al.** *JACC Cardiovasc Imaging* 2026 Oct 15.
🔗 [DOI: 10.1016/j.jcmg.2026.07.029](https://doi.org/10.1016/j.jcmg.2026.07.029)

- 一級預防試驗事後分析；無症狀中風險、statin-naive；n = **338** / 840 病灶
- 基線與 3 年各做一次冠狀動脈電腦斷層血管攝影 (CTA)

| 斑塊變化（statin） | β | P |
|------|-----|---|
| **高密度鈣**進展 | 0.79 | 0.001 |
| **非鈣化斑塊**退縮 | −9.83 | <0.001 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKUAAAClAQAAAAAVUAB3AAABT0lEQVR42t1Xuw2EMAw1R5EyI2QTWAwJJBZLNmGElCkifM/OldedHsWliESaJ/t9bES/nCZ/8ppFJGjdtU16JHxIai/5dn5/FS0ADaXOV1urpKDaqWiOUWeVtW4pZNnoaHfsCTUez6BloDWjjI5mvJli0MlZ2by5JotRZhdbk5/TBU2cP75g8raZSvSyS9HYk4mW4wmrqWvSIam83fF0qxmD+6VaubxZaC0GZLiB3El42gSyo4l+xYOrSfC2gLxhuiWS/TY0qR4oIuTa6pCKFdjxELkOgKcNwykTNm8wmFtcwvAbO5W7zQDUBgZFVuXWZuloaMNvmctbsW1kGVaDSiZuKvvJ5gAf4IWbXD7f7jG2fYofD8xuV4kkZaPZXuLkyQO8jQ0PVvP51iYub6M2XOoLkHBT2XmD6S7PZ7ibnJO2cwEDAuniPwP8nesP/6jeWWX3qHhAPz4AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# CAUGHT-CAD — 臨床啟示

> # 「鈣化分數上升」≠「病情惡化」

- statin 下**高密度鈣增加 + 非鈣化斑塊退縮 = 斑塊被穩定化**
- 追蹤 CTA **別只看 Agatston 總分**
- LDL-C 降幅 ≥30% 者最明顯 → **強化而非動搖降脂**

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 結構性主動脈瓣方向
### Drake 主要臨床方向

---

# TAVI #1 — DapaTAVI frailty 子分析

**DapaTAVI Investigators.** *J Am Heart Assoc* 2026 Oct.
🔗 [DOI: 10.1161/JAHA.126.051379](https://doi.org/10.1161/JAHA.126.051379)

**重點**：TAVI 後 dapagliflozin 的益處（1 年全因死亡或心衰惡化）**不因基線衰弱 (frailty) 程度而減損**。

> 💡 **TAVI 後的 GDMT（含 SGLT2 抑制劑）不應因衰弱而省略**；衰弱者需留意低血壓／脫水監測。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKUAAAClAQAAAAAVUAB3AAABVUlEQVR42t1XMY6EMAwcjiIlT8hPyMeQQOJjy0/yhJQUKL6xubtqu9NQrAuLpGDk8XgwsDdx4kNuXwBSnzY+TVfmAfn8wrv4/y3sIGg62lqNyZLZJUVryMkTim05vbDI0V5kMnWwtifQzEnsGPVo3jdrY02uEnXfQpNHW3IktSYjbmH+zYV6Amyv52AXonlCtI6FiZo8g8ShSdEOF0h3Jc5MScwkRy1biJ9jUDFPUjQnMZyLQLvRULTO5a93oLM4pwftS8rkBRTXRmGBlMoq7RtbxgKDxJ0SaVLn6r9+RSSidW1t0bcgcWaVGBq0Pvkjx5ju5KVKa9ur80fn8jEoYp+k7mPK4D6pZjIiFiAH4pPWuWLncp8ssTOoNXl/u2/TMrGXxF5CV2bzml9M1wNbEJcEnzfrT+xcDJZllTfjA31bLWbBxBvevXPZ5ofVnUuqyc/9o/oGHOb4C+DBXl8AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TAVI #2 — 延長球囊充氣優化擴張

**EuroIntervention 2026 Oct.**
🔗 [DOI: 10.4244/EIJ-D-26-00494](https://doi.org/10.4244/EIJ-D-26-00494)

**重點**：原生三葉瓣 AS 以 **SAPIEN 3 Ultra RESILIA** 球擴瓣 TAVI，採**延長球囊充氣（8 秒）**策略 → 改善瓣膜擴張與血流動力學，可能減少額外後擴張（「double-tap」）需求。

> 💡 低成本、可操作的技術細節；**單中心、無對照、僅早期結果**。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKUAAAClAQAAAAAVUAB3AAABUElEQVR42t1XMY6EMBAzR0GZJ/AT+BjSIvEx+AlPSJkC4fUkd912J1NsilFIY83Y4xnAD6fgS153AMOerpER9IGx/ODT+f8reAh0YMZI5pduvKxoAhqO3J9lQs9hx2JHu9OKWsnn0I68+NGCtz2KeMPPW9VkTSuCW5Pt5P4vRF84eXsRszSJKW0sc7bydkfpOq5jmbkJN25O3hZIIMoNSUCTV5Pkdpauecmih2TlTZqMfmPjTZW8vLz1LFO6oLCd6rfV290X0OWArJ3ndmUZMpTWrz/TzFsfbPFs883MWzhIaZWsKslW51JGGKIN0LVpYM5tGRn2j07ljODlrU41HRUxunujewYcYSOTnIvmadp2rrBmxKbg7re6c4myOmx4PLBzSSXaubScAOl6Ygtq841P7FyhkpqbKrnaeYtKBhBi9vAJTdYsq1nad65v/KN6A03G7AFgt2MwAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TAVI #3 — 當代自膨 vs 球擴瓣（9 中心）

**Ann Thorac Surg 2026 Oct.**
🔗 [DOI: 10.1016/j.athoracsur.2026.09.056](https://doi.org/10.1016/j.athoracsur.2026.09.056)

**重點**：2021–2024、9 中心、傾向分數配對比較當代**自膨瓣 (SE)** vs **球擴瓣 (BE)**；主要結果：死亡、中風、永久性節律器 (PPM)；次要：瓣旁漏、急性腎損傷（評估至 400 天）。

> 💡 更新選瓣的真實世界基準；**回溯觀察性，不取代 RCT**，選瓣仍依解剖個體化。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5AQAAAABc1qPxAAABq0lEQVR42uVYOW7DMBBcRQVLPoE/kT5mQAb0MfEnfIJKFoI2M0unS7pgDCQsDMsqlsOdY2nz79fT/v6Lw8zSbbN79d1tPfE8+fPDfli/+MJQ0j35+Sh9PTd+27gNVfHTSjqA3Fb3hh08LGmLV+Il6D69objvDZ2+0G5tcfb8MJT0cx7wdT0PtlcQ7utDyfZYAb9SefWlQVnPofN8UexW0HM8CotD4hMIl468U2pz0x37nb0BOdi+AD6O/SpQvJDtfQHbu9kG5KE3Idup82ehzksU1xGO6u5L3p3e3vALjFYotYv+AqJbvujyZl3W89tgafcg+tYYMU0nNQYaqqG42aP4kcNpZFK7yjj7Cokj1YBcmGrbcFaY2xYnrtQ5MjSyjCVtBMsq7HkL0BjfIDqtzo/sHp3ulBp1Lu45kTsNHmMF2C7tOVPN22DdGp4jDBakGoKFTuP95XrKSYbpEtRLjNSkneFCaguox+lVnOdBM2wDeT6F14kvDXFX8xYHIR0gx8CMcQbIF4p90t9YxhgVNwfxLdXKyHOGnDLPeWMh8oV5XofBK3X+D/8W+QQ0WI//axvVoQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 二尖瓣緣對緣與瓣膜介入
### Drake 的 TEER 操作面向

---

# TEER #1 — 有無現場外科的 M-TEER

**Catheter Cardiovasc Interv 2026 Oct.**
🔗 [DOI: 10.1002/ccd.70874](https://doi.org/10.1002/ccd.70874)

**重點**：**同一組操作團隊**在「無現場心臟外科」與「有現場外科」兩中心做 M-TEER（重度 4+ MR，n=64）；no-CCH 以共享 heart team + 正式緊急轉送提供後援 → 早期結果相當。

> 💡 **關鍵不在有沒有現場外科，而在共享 heart team + 制度化緊急轉送**；樣本小（n=64）、回溯。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKUAAAClAQAAAAAVUAB3AAABU0lEQVR42t1XO66EMAwcHgVljpCbwMWQQNqLhZtwhJQp0HrHzj69ZrunodgUiNCM7PnYwD6chi/5WgBMVldgsYfxgtx+8On8/yvsIOj0xHjystlkdknRKvJ02IW2VKIVrDegmWEm0C1ohU1swKivzXljJ7M9k8l5C00elU30h1qTcUq6OnndF1Le3G+bsZNXDhuI0bw2urvSdIOWNyOax8jZHSDuZEkeYMnOtoTp0kPaSdvJVuJjTm4DLW+MSGuD94+8dedJ0bZz8gLbzLcm1qSLv1M22E4vmJS3t8uYjqBA1LwdFD9r87LCb1WcygQqaQfeUhFnCbXBBIk3i3VBivYX/1xOhnrPDKBAkH0AyeebeUUzA6VPcfHsLgwUzoA1x/WGncubGLyNpt+C4MPmcQZ58tpc/DPHDnzx0u/KrIiBwiq18+1350KsJORNOwO+9o/qBX5Y8nXaGHPRAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TEER #2 — 重度左室功能不良的 TEER

**JACC Case Rep 2026 Oct.**
🔗 [DOI: 10.1016/j.jaccas.2026.110759](https://doi.org/10.1016/j.jaccas.2026.110759)

**重點**：6 位 **LVEF 10–20%**、重度（4+）至 torrential（5+）MR 者（4 位近／處心因性休克），不適合移植／LVAD，隨 heart team 經驗累積以 M-TEER 救援。

> 💡 「最難的 MR 病人」可在審慎評估＋機械支持備援下以 TEER 作橋接／緩和；**6 例病例系列、無對照**。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5AQAAAABc1qPxAAABnUlEQVR42uVYMZKDQAwTR0HJE/Yn8DFmYIaPkZ/sEygpGHySSVLddRkVd1s4IRRe27IsB/HzWfD3X2wAusc+x9HEWjHufG5i+cIv54MvEA/eobt6Gt2gCxr+5nK+o3QXUPhtrse4T0yE2TnTPu5p7M43tDVCkTde56o5nWfQmXtjzZ9on8rLONH+bjq2WlSZfPQ4v2QHMOOCvMpdfGmPWMkvibp+VeHb6gTcApLMmUaR09jSHgz6GMhwhB5bbdA1jGkPMjpzz3hPXWNBWPs8qYWnrTRiGl+fz+kyGP4prpvKMfrodcIx0Ln8IonWB7iHyr0RZiGgx9Y7+1x5pkuhvV81WJx9Lr+KvED0KmYtGJ0jNS4GDXVZpzljHCwa4BosJHgk0OFstTZuBTWQ29F4NZwYDuK15HZV39jnCbN37qWfvX3Oz+S1nC4svFfJKPyb3HKkmjVcnC8ZJSEXXvVKwOVAY81Pu24no0tHlEzEYWU4Cub2pnUMvbPmz43lXlXrLSDNNWeridyqRDR8zjNo6Wc81yUtTuaN5d/9LfINJj2N1NQx1uQAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TEER #3 — M-TEER 後右至左分流（Editorial）

**JACC Case Rep 2026 Oct.**
🔗 [DOI: 10.1016/j.jaccas.2026.110354](https://doi.org/10.1016/j.jaccas.2026.110354)

**重點**：M-TEER 經中隔後殘餘心房分流；出現**右至左分流 + 低血氧**時，要先辨明是**中隔問題**還是**右心疾病進展**，再決定封堵或治本。

> 💡 與上期 stiff-LA／心房血流調節器 (AFR) 互為鏡像——**分流方向反映底層血流動力學**，盲目封堵可能無益。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5AQAAAABc1qPxAAABoUlEQVR42uVYQW6DQBAz5cCRJ+xP4GNIQeJjyU/2CRw5IKb2bJJTe6tcqV0pow0chtmxPQbE12vF379xBzDccatHF1vFvPN/F+sHvlk/eAPx4DMM/NXhsd+4Y+A1V/IdZbjGVTuWP+8LBm/yiLMcHYv+jeR39HnsbLw3uXpO1JVo7bb2PNH+2JfyCk60v1ZlvSfIt8ZBT/JLcdKxX1DlsRbfsUdsQZhJacZNaBf0fIDbKqVlYeXjqcpPMc9VOal2TJTXprHTeBqpFlJ0oBfMqDRTap3x2EXsyCdQyBHj4vmYlaOQ3ae0binH7Kt8Fd/6IN8WNKENn7YzL9jpQ5XzIJw8v5BizqUGkPFenkdtnRbWpKwFs2+wJMueDkrzzWmjNMClsSDFE+g4nB6uRg7SidqOzuvhpO3XGKms5DmDk+dbbbMsG9/lnHHyPG0U6xXftPM6maeRS4rnXLV6uKeDSvdqnOdZtAQeSq7pYvft0vY5tZ3XjGhXcqKOysqAaXT2/P3GQnm9vUnnfWNZisSttqEeVrRHvifLwor2vp7/188in0KnltDWiJngAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

<!-- _class: small-text -->
# 其他值得一讀（1/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **OCEANIC-STROKE 出血分析**（asundexian） | *Circulation* | 非心源性中風／高危 TIA 加 asundexian：減缺血性中風、未顯著增出血 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.081836) ｜ [PMID 42866879](https://pubmed.ncbi.nlm.nih.gov/42866879/) |
| **AHA 抗血小板管理科學聲明** | *Circulation* | 冠心症抗血小板個體化：藥物／強度／療程平衡血栓與出血 | [DOI](https://doi.org/10.1161/CIR.0000000000001478) ｜ [PMID 42866888](https://pubmed.ncbi.nlm.nih.gov/42866888/) |
| **2026 ACC 運動處方科學聲明** | *JACC* | 把運動處方納入心血管常規照護的實用指引 | [DOI](https://doi.org/10.1016/j.jacc.2026.09.008) ｜ [PMID 42878712](https://pubmed.ncbi.nlm.nih.gov/42878712/) |

---

<!-- _class: small-text -->
# 其他值得一讀（2/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **血管內影像導引 PCI 統合**（18 RCT） | *JACC Adv* | n=18,975；MACE RR **0.67**、支架血栓 RR 0.52；達影像優化者 RR 0.41 | [DOI](https://doi.org/10.1016/j.jacadv.2026.103340) ｜ [PMID 42879937](https://pubmed.ncbi.nlm.nih.gov/42879937/) |
| **HFpEF 大 V 波增加右心後負荷** | *Circulation* | 左房僵硬之高大 V 波「不成比例」加壓肺動脈 → 影響肺血管判讀 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.081799) ｜ [PMID 42860037](https://pubmed.ncbi.nlm.nih.gov/42860037/) |
| **ESC/EAPCI 暫時性機械循環支持共識** | *Eur Heart J* | 更新 2020 版；表型導向選病人、shock team、hub-and-spoke | [DOI](https://doi.org/10.1093/eurheartj/ehag708) ｜ [PMID 42870411](https://pubmed.ncbi.nlm.nih.gov/42870411/) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構／冠脈介入／EP
### 本週 5 例

---

# Case #1 — 全程無導線左室中隔心內膜節律

**Dababneh E, et al.** *JACC Case Rep* 2026 Oct 16.
🔗 [DOI: 10.1016/j.jaccas.2026.110628](https://doi.org/10.1016/j.jaccas.2026.110628) ｜ [PMID 42886148](https://pubmed.ncbi.nlm.nih.gov/42886148/)

86 歲完全性房室阻斷併心肌病，植入雙腔無導線節律器（AVEIR DR）＋ **WiSE 超音波左室中隔心內膜電極**；以「sync-to-pace」讓心房脈衝觸發左室刺激，QRS 142 ms。

> 💡 **首例完全無導線、房室同步、不依賴右室節律**的左室心內膜節律 — 生理性節律「去導線化」的概念里程碑。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5AQAAAABc1qPxAAABo0lEQVR42uVYMZKDMBATR0HJE/yT8DFmwgwfIz/xE1xSeNiTbNLddTcqci48IRTrXWm1Moif14bPf3EAmF4ReeJjOpfC5yG2L/yy/vAFgnFDcTFdc8Q5lGfwP1fwgsTMK84HnjxGWVUIZ/Bj3vP5mHcm7Q8u/AV3YtmtwYX5gTErZIqwYt7ZXtb03pxsb+tVxizC5endg57gF7nGVKvgBk7cAPiCM3N2mTaiMLLZfZg/MzDXBLZaJvWQfJgf8ybK1/6rtdq5GDMPDGUMLBR4iHU+woVo1sbJEkT/wuosO7q2S2MjN7b7yn6Ra01pmC/LvhAAL+aUlqr0W9OtyRdcFWc0lR0kuvrNGJxc65mHtF2DxehkKOsCHl1eH1aFCzJsuu7uRp/sg1XbI2RiNNl1DHi1ndGk7ZsmO5LPTCjV5lm1SV4pMkbCUU+X3ucVbar5Wu12MpBv35V0hdnDtU2XhqlZ5zC7VwFPeW0jxok5p9o1b+I4m+7oB7JelzrbV44272DpN5ZNjqLz3n5j4TWtmYk2YX02qhNdRg7oZYe5z//hZ5FvYGuRsDnW79YAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #2 — 突出開口支架：IVUS 導引救援

**Tsutsui Y, et al.** *JACC Case Rep* 2026 Oct 16.
🔗 [DOI: 10.1016/j.jaccas.2026.110771](https://doi.org/10.1016/j.jaccas.2026.110771) ｜ [PMID 42886149](https://pubmed.ncbi.nlm.nih.gov/42886149/)

RCA 開口支架過度突入主動脈、致導引導管脫位。以 **IVUS 導引尖端偵測 (tip detection)** 精準重新穿越，再於**遠端錨定球囊**支撐下行**支架推送 (stent push)** 推回理想位置。

> 💡 純導管、不需外科的開口支架定位不良 troubleshooting；IVUS 把「盲目重穿」變可視化。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5AQAAAABc1qPxAAABoklEQVR42uVYO26FQAw0oaDkCHsTuNhKIHEx3k32CJRbrHBmvLwu6aKJlFBYwCu89nxsnvnX125//4fTzKbXtXkd/Ci2XngefP+wb64f/MH8hTNMt20lTjA5At6pkl+WpnveebeVul4ZjZAm92g7wy8kP+cWwBecQJqcmIN1yf3Kib0XYv6wPad3ULL9fZUI0FvXoCb5zbhYTpWBcCdd290PEj1Yd5DtY9ER7px3Sg0cv+fGyhGEbR9LXWZ04ITN4a5JpQZHX+BwqLcB+PA6ndTCVONhLAh0Gh3mR4HJjG4r4T7J+1Vor1ZRNEcb7AbHKDrCvS7kpbej2S0F+ZWYZ6aEw5F6ULxW5x1pODqmGp012aqrfERG9L7rjXNGN1hAs5hlqRrgJtFNKLWucyB9U2+DdofDIOVMKai8xU4j1TlphsqJNOE+lDrHSI01CvXGdMGddpOhzru5xUjV7nDUOTeo2F6Tsu19e7UYaMC86ff2+Eyj0eKddKoRZEfRpPwyKzHvlVt+vljCbuSYp0jOJdp0yYPt3J+n53NpdB3m//VvkU+BAYNBs57TIAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #3 — M-TEER 後遲發瓣葉穿孔：血管塞封堵

**JACC Case Rep 2026 Oct.**
🔗 [DOI: 10.1016/j.jaccas.2026.110745](https://doi.org/10.1016/j.jaccas.2026.110745) ｜ [PMID 42886136](https://pubmed.ncbi.nlm.nih.gov/42886136/)

63 歲多瓣膜疾病、透析依賴，M-TEER 後**前葉遲發穿孔**致重度復發 MR。透視 + 3D 經食道超音波導引下以**血管塞 (vascular plug)** 封堵，避免高風險再手術。

> 💡 遲發瓣葉穿孔是 M-TEER 後復發 MR 的少見但可處理機轉；血管塞為不宜再開胸者提供微創救援。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5AQAAAABc1qPxAAABnUlEQVR42uVYS26EMAw1ZcEyR8hN4GIjDVIuBjfJEVhmEeG+56izanfVG6lFmigMC2O/jx3Mv792+/sPDjNbDnvWNnmptl24n3z/sB+uX3xgfuIdFvyqn9cTOyz4TxX8srzcac8Lgte2XQ9btMHde24Tkn5H8MMQ0pn5pA1OzEE4Z9wcwOswD7afiPu1KNn+El3bvBv0Nm41wW+uqz1y40K4s67s7oVw02lSIdvnqiPckXZbbrDd79SZeafyVJlDam1Ng/IVu27KzL2apVI9nGZFIYT26hGXb2Azl2gxsswLQ4bHRu3B+01nrw+Dyman3thcwXYXlh35pvCXnkl+oc5v2HqwLgCA4rU67xZdrRnfABXPJsR8rmFzwDwGKmVjobVgkoGzkvIkuiml5nT0SBqUn8QzHK1lEA62zkWocy9jeCLNCHeR63zAjSt22kkmBrlzSDz6qnKGC6QxQQUAWVl2tpNEuDE6A/Oun9vNxugcu00anK0teG9rUmL+OrFE2ccAKcac5rYR82jqLmU7GwvOanFcml2H+X/9LPIJuCWJzWoc1TsAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #4 — 鄰近 LAD 的 PVC：導絲導引酒精消融

**Guo C, et al.** *JACC Case Rep* 2026 Oct 16.
🔗 [DOI: 10.1016/j.jaccas.2026.110992](https://doi.org/10.1016/j.jaccas.2026.110992) ｜ [PMID 42886147](https://pubmed.ncbi.nlm.nih.gov/42886147/)

30 歲高負荷 PVC 起源於**前室間溝心外膜、緊鄰 LAD**，射頻有傷冠脈風險。經前室間靜脈小分支行**導絲導引無水酒精消融**，成功消除、冠脈無損傷、2 個月無復發。

> 💡 當射頻因鄰近冠脈而不安全時，**經靜脈導絲導引酒精消融**是可行替代；術後冠脈攝影確認無損傷是關鍵。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5AQAAAABc1qPxAAABpklEQVR42uVYMXKDQBCTQ0HJE+4n8DFm8Awfwz+5J1BewbCR9pIu6TIqHApsTCF2V9IKI34+nnj/GweA8cXvIy9LW05eP+L5gV+OP7yB6LiEHO8poj3OLfibC/xEYeUXMGPTY6xqhBP8mJ4FmHYW7QePLJ8ntt0Krpkf2GoSLsI68872cy3fJyfb8xBk3BhUftegB/ye9qpS+7gb9AS+thM8cuYvjfvAQLH7Zr5Vfq6lzXwMUg/FOXN57HRBYkfv/WKbOVbS+xwCS0SVzVUf4eSnEjYIzunzWYxtT2d9xB6Y2ftku7HtBG+zeq/KsXAAPvAjdxl1rqVetViKD1ze3tRx2StSb87KtdW4z5NroxaLj3D3l960z6nz2epwLzKM/tIzHHKxNGPlQ5XOe8fHW25r9PZcpLvK32vGGV+YYGalnyakcsQskzHOnFyjttJUkVvNJ7U8Mkux9yr6gj3Dse23vC6jc3jTK6WmvaoEdRXnzOlw1JsCcwYqwP+6VHKzs3zrYsk3FnFt6by/7G8s0yVvj8yxxtyebNfMFWGz7TDr/B/+LfIJl6uDj1/4bkEAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #5 — 嗜鉻細胞瘤危象：腎上腺動脈栓塞救援

**Wu K, et al.** *JACC Case Rep* 2026 Oct 16.
🔗 [DOI: 10.1016/j.jaccas.2026.110993](https://doi.org/10.1016/j.jaccas.2026.110993) ｜ [PMID 42886145](https://pubmed.ncbi.nlm.nih.gov/42886145/)

50 歲女性 basal-type Takotsubo (TTS) 併難治心因性休克、血壓極度不穩；6.5 cm 腎上腺腫瘤。藥物無法穩定 → **緊急經導管腎上腺動脈栓塞 (TAAE)** 救援，血流動力學持續穩定；1 個月後擇期切除，1 年無復發。

> 💡 極度血壓不穩 + TTS 要警覺隱匿嗜鉻細胞瘤；**TAAE → α 阻斷 → 擇期切除**的分階段策略預後佳。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5AQAAAABc1qPxAAABpElEQVR42uVYPW6GMAw1/QbGHCE3gYshgcTF4CY5AmMGFPc9h3Zqt+pVahkifgbHfj+xMf/62uzvfzjMbPRrLXXwvdh84Xnw7c2+uX7wg/mJPYynb9ks3Yh7rY53quCX5fFIu9vsWIZrsVEbHGX3yqTr/AvB3Ysf6c7u2uDE3ME1Ih3UE2IebD+vJX8sSrbH1RKSxjbypwY1wZu9Si/7kR4/AO9lmG+54qbrDWzHXoRsB727zmFz4XA6wjVbciw2cQf02CojXIO64aw7gb9znQj8qSRcsD3QH1s3WpXUgDmK7QW2Ho8veo6QcHUKzG0tEHsoT5b5WsLbIy63YcrgRp0vGRJf3Rhcx/YjRdIMiRrQWbPS4e5nIdcgduhtVhIumhg6DV6wEKey7AD5tmrhcNLz/DnGvHRvn0x5nrPYdeoHy8txhxoICYe4XWoEnh1F1XYybN+AOVQ2BO+lPZw/XWT07UqpxcQSbSMJx8zFfXuD3ph9iYZKOKv1cckxsXgsu1dxcJobdd4bSFdjjqMNto4abFk8sdBpxhiX2EoKz/N/+lvkHW1FjEtRR5mhAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: lead -->
# 💎 Take Home Message

### 1. **SUBCUT-HF II ✅** — 皮下利尿劑微幫浦，30 天 DAOH +4.0 天（心衰「去住院化」）
### 2. **RELIEVE-HF ➰** — 心房分流器 HFrEF 安全、HFpEF 反而有害（別一體適用）
### 3. **ICRAKI ❌(IHD)** — 重症 AKI 間歇透析死亡率較高（HR 1.30）→ 不穩者傾向 CRRT
### 4. **DCM 基因型 ✅** — 高致心律不整基因 MVA HR 3.25，LVEF≥50% 仍 HR 2.36
### 5. **CAUGHT-CAD ✅** — 鈣化密度上升＝斑塊穩定化（別只看 Agatston 總分）
### 6. **TAVI 表型化 🫀** — 衰弱者仍受益於 dapagliflozin；延長球囊充氣；SE vs BE 更新比較
### 7. **TEER 場域與表型 🔧** — 非必須現場外科；重度 LV 不良可救援；後中隔分流先辨機轉

---

<!-- _class: small-text -->
# 完整參考文獻 (1/2)

**Top 5 Picks**：
1. Campbell RT, et al. SUBCUT-HF II. [*J Am Coll Cardiol* 2026;88(15):1781-1793.](https://doi.org/10.1016/j.jacc.2026.07.047) PMID [42872757](https://pubmed.ncbi.nlm.nih.gov/42872757/)
2. Rodés-Cabau J, et al. RELIEVE-HF long-term by EF. [*JACC Heart Fail* 2026.](https://doi.org/10.1016/j.jchf.2026.103375) PMID [42886087](https://pubmed.ncbi.nlm.nih.gov/42886087/)
3. Gaudry S, et al. ICRAKI. [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMoa2608397) PMID [42873070](https://pubmed.ncbi.nlm.nih.gov/42873070/)
4. Padalia K, et al. DCM genotype & arrhythmic risk (SHaRe). [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag648) PMID [42864989](https://pubmed.ncbi.nlm.nih.gov/42864989/)
5. Vasanthakumar SA, et al. CAUGHT-CAD. [*JACC Cardiovasc Imaging* 2026.](https://doi.org/10.1016/j.jcmg.2026.07.029) PMID [42886154](https://pubmed.ncbi.nlm.nih.gov/42886154/)

**TAVI Section**：
6. DapaTAVI frailty substudy. [*J Am Heart Assoc* 2026.](https://doi.org/10.1161/JAHA.126.051379) PMID [42885795](https://pubmed.ncbi.nlm.nih.gov/42885795/)
7. Prolonged balloon inflation (SAPIEN 3 Ultra RESILIA). [*EuroIntervention* 2026.](https://doi.org/10.4244/EIJ-D-26-00494) PMID [42885346](https://pubmed.ncbi.nlm.nih.gov/42885346/)
8. Current-gen SE vs BE TAVR. [*Ann Thorac Surg* 2026.](https://doi.org/10.1016/j.athoracsur.2026.09.056) PMID [42880619](https://pubmed.ncbi.nlm.nih.gov/42880619/)

---

<!-- _class: small-text -->
# 完整參考文獻 (2/2)

**TEER Section**：
9. M-TEER with/without on-site surgery. [*Catheter Cardiovasc Interv* 2026.](https://doi.org/10.1002/ccd.70874) PMID [42876391](https://pubmed.ncbi.nlm.nih.gov/42876391/)
10. TEER in advanced HF/ventricular dysfunction. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.110759) PMID [42886123](https://pubmed.ncbi.nlm.nih.gov/42886123/)
11. Right-to-left interatrial shunting after Mitral TEER (editorial). [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.110354) PMID [42878375](https://pubmed.ncbi.nlm.nih.gov/42878375/)

**Honorable Mentions**：
12. OCEANIC-STROKE bleeding analysis (asundexian). [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.081836) PMID [42866879](https://pubmed.ncbi.nlm.nih.gov/42866879/)
13. AHA Antiplatelet Management Scientific Statement. [*Circulation* 2026.](https://doi.org/10.1161/CIR.0000000000001478) PMID [42866888](https://pubmed.ncbi.nlm.nih.gov/42866888/)
14. 2026 ACC Exercise Prescription Scientific Statement. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.09.008) PMID [42878712](https://pubmed.ncbi.nlm.nih.gov/42878712/)
15. IVI-guided PCI meta-analysis. [*JACC Adv* 2026.](https://doi.org/10.1016/j.jacadv.2026.103340) PMID [42879937](https://pubmed.ncbi.nlm.nih.gov/42879937/)
16. Prominent V waves & RV afterload (HFpEF). [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.081799) PMID [42860037](https://pubmed.ncbi.nlm.nih.gov/42860037/)
17. ESC/EAPCI temporary MCS consensus. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag708) PMID [42870411](https://pubmed.ncbi.nlm.nih.gov/42870411/)

**Case Reports**：
18. Dababneh E, et al. Totally leadless LV septal pacing. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.110628) PMID [42886148](https://pubmed.ncbi.nlm.nih.gov/42886148/)
19. Tsutsui Y, et al. IVUS-guided stent push. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.110771) PMID [42886149](https://pubmed.ncbi.nlm.nih.gov/42886149/)
20. Vascular plug closure post-TEER perforation. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.110745) PMID [42886136](https://pubmed.ncbi.nlm.nih.gov/42886136/)
21. Guo C, et al. Ethanol ablation PVC near LAD. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.110992) PMID [42886147](https://pubmed.ncbi.nlm.nih.gov/42886147/)
22. Wu K, et al. Adrenal arterial embolization for pheochromocytoma crisis. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.110993) PMID [42886145](https://pubmed.ncbi.nlm.nih.gov/42886145/)

---

<!-- _class: abbr -->
# 縮寫對照表 (1/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| DAOH | Days Alive and Out of Hospital | 存活且不在院天數 |
| HF / HFrEF / HFpEF | Heart Failure (reduced / preserved EF) | 心衰竭（射血分數降低／保留） |
| LVEF | Left Ventricular Ejection Fraction | 左心室射血分數 |
| MACNE | Major Adverse Cardiovascular or Neurological Events | 重大不良心血管或神經事件 |
| GDMT | Guideline-Directed Medical Therapy | 指引導向藥物治療 |
| SGLT2i | Sodium-Glucose Cotransporter 2 inhibitor | SGLT2 抑制劑 |
| AKI | Acute Kidney Injury | 急性腎損傷 |
| RRT / IHD / CRRT | Renal-Replacement Therapy / Intermittent HD / Continuous RRT | 腎替代療法／間歇透析／連續性 |
| MAKE | Major Adverse Kidney Event | 主要不良腎事件 |
| DCM | Dilated Cardiomyopathy | 擴張型心肌病 |
| MVA | Major Ventricular Arrhythmia | 重大心室心律不整 |
| ICD | Implantable Cardioverter-Defibrillator | 植入式心臟去顫器 |
| CTA | Computed Tomographic Angiography | 電腦斷層血管攝影 |
| LDL-C | Low-Density Lipoprotein Cholesterol | 低密度脂蛋白膽固醇 |

---

<!-- _class: abbr -->
# 縮寫對照表 (2/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| TAVI / TAVR | Transcatheter Aortic Valve Implantation / Replacement | 經導管主動脈瓣置換 |
| AS | Aortic Stenosis | 主動脈瓣狹窄 |
| SE / BE | Self-Expanding / Balloon-Expandable valve | 自膨／球囊擴張瓣膜 |
| PPM | Permanent Pacemaker Implantation | 永久性心律調節器植入 |
| PVL | Paravalvular Leak | 瓣旁漏 |
| TEER / M-TEER | (Mitral) Transcatheter Edge-to-Edge Repair | （二尖瓣）經導管緣對緣修復 |
| MR | Mitral Regurgitation | 二尖瓣逆流 |
| LVAD | Left Ventricular Assist Device | 左心室輔助裝置 |
| ASD | Atrial Septal Defect | 心房中隔缺損 |
| AFR | Atrial Flow Regulator | 心房血流調節器 |
| PCI | Percutaneous Coronary Intervention | 經皮冠狀動脈介入 |
| IVUS / OCT | Intravascular Ultrasound / Optical Coherence Tomography | 血管內超音波／光學同調斷層 |
| RCA / LAD | Right Coronary Artery / Left Anterior Descending | 右冠狀動脈／左前降支 |
| LAAO / DOAC / DAPT | LAA Occlusion / Direct Oral Anticoagulant / Dual Antiplatelet | 左心耳封堵／口服抗凝／雙重抗血小板 |
| TIA | Transient Ischemic Attack | 短暫性腦缺血發作 |
| MCS | Mechanical Circulatory Support | 機械循環支持 |
| PVC | Premature Ventricular Complex | 心室早期收縮 |
| TTS / TAAE | Takotsubo Syndrome / Transcatheter Adrenal Arterial Embolization | 章魚壺症候群／經導管腎上腺動脈栓塞 |
| WiSE | Wireless Stimulation Endocardially | 無線心內膜刺激 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**
心臟內科｜結構性心臟病介入

*本文件為讀書會共筆之教學整理，*
*僅供醫療專業同仁臨床教學交流參考。*
