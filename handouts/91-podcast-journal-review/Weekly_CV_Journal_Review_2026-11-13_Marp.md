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
  section.bignum h1 { color: #ffffff; font-size: 3.3em; border-bottom: none; }
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
  section.ref { font-size: 0.66em; }
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
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-11-06 ~ 2026-11-13'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-11-06 ~ 2026-11-13　｜　AHA 2026 Late-Breakers 專號

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Top Pick 附 QR Code，可掃描跳轉原文

---

# 🎯 本週主題與固定欄目

## 漂亮的機轉，失望的終點

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — AHA 2026 跨期刊重磅 RCT
2. 🫀 **TAVI Section** — 操作者學習曲線／BMI／二葉瓣
3. 🔧 **TEER Section** — 三尖瓣 T-TEER 右心重塑
4. 📚 **Honorable Mentions** — Lancet／EHJ／JACC／Circulation
5. 🔬 **Case Reports** — 結構介入救援 × 5
6. 📖 **參考文獻 + 縮寫對照**

> 本週 **EuroIntervention 無新上線文章**（PubMed 2026/11/06–11/13 查無）。

---

# ⭐ Top 5 Picks

| 試驗 | 期刊 | 方向 | 關鍵數字 |
|------|------|------|----------|
| **Lp(a)HORIZON**（pelacarsen） | *NEJM* | ❌ | MACE **HR 1.02**（P=0.76），Lp(a)↓~73% |
| **ZEUS**（ziltivekimab） | *NEJM* | ❌ | 3-pt MACE **HR 0.99**（P=0.84），CRP↓64% |
| **OPTIMAL-DIABETES / -STROKE** | *NEJM* | 💡 | DM **HR 0.90**（NS）／Stroke **HR 0.79**（P=0.007） |
| **OptimPacing**（LBBP vs RV） | *NEJM* | ✅ | 複合 **HR 0.41**（P=0.003），提前中止 |
| **SWITCH-SWEDEHEART** | *NEJM* | ❌ | 缺血 **OR 0.90**；大出血 OR 0.80 |

> **Pearl of the Week**：把 Lp(a) 壓到地板、把 CRP 打到谷底、把糖尿病血壓逼到 <120——硬終點全沒動。生物標記漂亮 ≠ 事件減少。但「選對族群」（中風降壓）與「改對生理」（LBBP）仍有效。

---

<!-- _class: divider -->
# Pick #1
## Lp(a)HORIZON
### 降 lipoprotein(a)，心血管事件卻沒動

---

# Lp(a)HORIZON — 設計

## [Cho L, Nissen SE, et al. *N Engl J Med* 2026](https://doi.org/10.1056/NEJMoa2610159)

- 國際、隨機、安慰劑對照、雙盲 **phase 3 CVOT**（study chair：Steven Nissen）
- 族群：既有心血管疾病 + **lipoprotein(a) ≥ 70 mg/dL**，n = **8,322**
- 介入：pelacarsen 80 mg 皮下每月 vs 安慰劑；median 追蹤 **4.7 年**
- 藥效：12 個月 Lp(a) **64.4 vs 233.4 nmol/L**（約降 73%）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5CAAAAABRxsGAAAABz0lEQVR42u3bQZaDIBAFQO9/aecCQn4DkzykWOXFiMUiSDfNde/aLnJycnJycnJycnJycvK3yK/P7el3Tx00u68/jZyc/LHr5tWnTzO/K1nIycnv5owSAPtzS/+2/ljJycmTvvqzQvPVHgyYnJx85dzSvKP5uicnJ5+Xp1eD7/rh9pcjC3Ly7eVpjmvNp19k58jJN5XHWzXdV3uwSvjZDhc5+c7yZrKqHgoH4+rnzOYjC3Lyt8nTboI93QAdhNvk5OSj+eO0pCItswh6Jic/Wx6kjvsXFu79zmfnyMlfLu//7/s55QHR52mFnJx8IAEdzB797oNMGTk5+cD/Pq2SSA8IkJOTD0TQ9YV2MMxSCE5OTn6XbGm2q34Ej5ycfKosMS0XTnLK9TvIyU+Vl+aRdCO29Kafz86Rk79XXl8C1JNV8yfyyMmPlpds6YOvSiMnJ5+v+a8nm9Nc9n+fyiEn31ReOjeXFlLU6x9HI2hy8hPkg+mo6XB70XkicvIT5DPn3Er1TqVphZycPD7KWlqkp6v3YJ4jJyevHTZPvaU9YnJy8tH1eTDWdBn+5QianHx7+WCOq156sbKimJz8BPkWjZycnJycnJycnJycnHzH9geVTPj42I6BCQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# HR 1.02
## MACE — pelacarsen vs placebo
### 12.3% vs 12.1%｜95% CI 0.90–1.15｜P = 0.76

高 Lp(a) 次群（≥90 mg/dL）：**HR 1.00（0.87–1.15，P=0.99）**

---

# Lp(a)HORIZON — 臨床啟示

> ❌ **第一個 Lp(a)-lowering 的硬終點 CVOT：乾淨的 negative。**

- 藥效漂亮（Lp(a)↓73–78%），終點與安慰劑重疊
- 連最該獲益的高 Lp(a) 次群也沒差
- 安全性無疑慮（嚴重不良事件 37.3% vs 41.1%）

**Nissen 觀點**：單一 negative 不等於關閉假說；本試驗只收**次級預防**。OCEAN(a)（olpasiran）、ACCLAIM-Lp(a)（lepodisiran）仍進行中。

---

<!-- _class: divider -->
# Pick #2
## ZEUS
### IL-6 抑制把發炎打到谷底，MACE 仍沒動

---

# ZEUS — 設計與結果

## [Ridker PM, et al. *N Engl J Med* 2026](https://doi.org/10.1056/NEJMoa2612126)

- 多國雙盲 RCT；族群：ASCVD + **CKD** + 發炎（hs-CRP ≥ 2 mg/L），n = **6,376**
- 介入：ziltivekimab 15 mg 皮下每月 vs 安慰劑；median 33 個月
- 藥效（24 個月，vs 安慰劑）：free IL-6 **−76 pp**、hs-CRP **−64 pp**

| 終點 | ziltivekimab | placebo | HR (95% CI) |
|------|------|------|------|
| **3-point MACE** | 17.6% | 17.7% | **0.99 (0.88–1.11)**, P=0.84 |
| 嚴重感染 | 20.4% | 17.9% | 偏高 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5CAAAAABRxsGAAAABz0lEQVR42u3bQXLDIAwFUN//0u6ym0C+AE9reF7FcWpeOlMhS+p1v/W4yMnJycnJycnJycnJyXeRX9+P4HO/H2muUVqNnJz87i/36Wr/tEkdXI2cnLz9d9+815cw8OHqp/vVghM5OXn/Xv1X9VBDTk6+XN6PGf1TcnLyB/PzwdwgtZGTk8/XuNa8+ovqHDn5S+Vxq6a1+/dZ/6DDRU7+ZnlzB09jQVqorv8sOTl5Ow8oxZbSE/Ty3Z+c/AR5qeHTPE2r1f2YRk5OnlSxZvKF0i9mahqKnHxzeX1AMR1anC5Ak5OTX2nDtvRe0GNaVD8nJ99X3t/40wvp908zenJy8jvdo0ulrNI/+ARP1eTkZ8sXTikGX/3BJwty8s3l6epBglDqE83HFnLyfeWlonRQzypNKKdlMHJy8jhTDzbvtE80/2RBTr65PMjAgwGJIN48M2lJTr65PD2CgnGaJQyELnLyU+X10vHgTEaa/pOTk+fl3zAtSKvay2MLOfkx8sGOUTA+UR9zJCcnv+v7cX3qIi15PRhbyMkPlKct3lJ7mJycfD4/7zeLSsXm+SkRcvIT5PXq1ODExvL8nJx8c/krDnJycnJycnJycnJycvI3Hj8gJOb8D7o/iwAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# ZEUS — 臨床啟示

> ❌ **殘餘發炎假說再受挫**：發炎標記大降，事件沒動。

- 與 **CANTOS**（canakinumab 抑 IL-1β 曾降事件）對照
- Ridker：ZEUS 收的是「風險高得多」的 ASCVD+CKD 族群，可能稀釋效益
- IL-6 路徑定位待 **HERMES**（心衰）、**ARTEMIS**（MI 後），2027 上半年揭曉

---

<!-- _class: divider -->
# Pick #3
## OPTIMAL-DIABETES & -STROKE
### 同一個 <120，兩種族群，兩種答案

---

# OPTIMAL 姊妹試驗 — 收縮壓 <120 vs <140

## [DIABETES: *NEJM* 2026](https://doi.org/10.1056/NEJMoa2612922)　｜　[STROKE: *NEJM* 2026](https://doi.org/10.1056/NEJMoa2612924)

| 項目 | OPTIMAL-DIABETES | OPTIMAL-STROKE |
|------|------|------|
| 族群 | T2DM + 高風險，n=9,476 | 曾缺血性中風/TIA，n=4,368 |
| 達成血壓 | 121.8 vs 135.4 | 122.0 vs 135.2 |
| Primary | 6.0% vs 6.7% | 10.9% vs 13.5% |
| **HR (95% CI)** | **0.90 (0.77–1.06)** ❌ | **0.79 (0.67–0.94)** ✅ |
| P | 0.20 | 0.007 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5CAAAAABRxsGAAAAByklEQVR42u3cQXLDIAwF0Nz/0umyM52gfBnsjvFj1Wkc67EoCMnu633X8SInJycnJycnJycnJyffRf76Pn6v+/ONTx8MY7SikZOTv+tww0+DcMPZ9KORk5N//Luv5XX0obcfjZycPLlXMId09ycnJz9HXq8ZrRSenJx8ZX5e24a7f2ojJydfWeOa+el/q3Pk5LeSx62asJ4VOC7ucJGT31nex0yn8MPJzect5OS7yYOKVV27Gs7mut2fnHxf+ZevlMtA/bu6ndvqQJGTP1YeFIfTGQbXpbUwcnLypBsb7Op1nXm6AE1O/mx5ECQtVqWH5/RATU5O3jvTBtHT7L3V5yUnf7Y8aPMMY/YLWAfSf3Lyp8rTVSZoKtWXnJ2fk5NvKV9YnTrYJ1q5KpKT7yZviRYuIembP+Tk5EmDNe0TpVWxc/JzcvLd5PVxNu3/BM9VnPOkJTn55vJ0pK/MpdXlRU9DkZNvLu+/N9e/QXCWJicnn/8faK2GzyVrCzn5Y+T9taA1uYNLFzk5ee/54HpeaX7eWufIycl7+3a/YpXeipyc/Gh+PnOWDtq55OTki2pcLduJ+Tk5+ebyWwxycnJycnJycnJycnLyO44f0KZ8dZpl4I4AAAAASUVORK5CYII="><br>📱 STROKE DOI</div>

---

# OPTIMAL — 臨床啟示

> 💡 **降壓目標要看族群**，別一體適用。

- 糖尿病：追 <120 **無事件益處** → 權衡個別風險
- 曾中風/TIA：追 <120 **有益**（HR 0.79），但**腎臟終點代價上升**（eGFR↓≥50% 較多）
- 同一巴西計畫、同一目標、相反結果 → SPRINT-type 強化降壓不宜外推到所有族群

---

<!-- _class: divider -->
# Pick #4
## OptimPacing
### Left bundle-branch pacing 勝右心室起搏

---

# OptimPacing — 設計與結果

## [Qian Z, et al. *N Engl J Med* 2026](https://doi.org/10.1056/NEJMoa2612972)

- Investigator-initiated、國際、開放標籤 RCT；**期中分析即提前中止**
- 族群：房室傳導阻斷需起搏，n=**685**；median 35.1 個月
- 介入：**LBBP（342）vs 右心室起搏（343）**

| 終點（4 年累積） | LBBP | RV pacing |
|------|------|------|
| 死亡＋心衰住院＋起搏誘發心肌病 | **8.5%** | **19.2%** |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5CAAAAABRxsGAAAAB1UlEQVR42u3cy27CMBAFUP7/p+myUpWaex0a6vhkRSuET7IYz8PweK56PcjJycnJycnJycnJycnvIn+8vo7e9/2/H6+OPr5fjZyc/DleM7D1d5OuRk5Ofmj71RFgxjfXr0ZOTv6s9vfxbj3OHMjJyf86tgQ59j+NiuTky8urAni88Y/Dz8WVBTn58vK0x/WeV5/ozpGTLyqPRzUHqx/9OY5Bn5hwkZOvLA9EfSu675mdmhORk28jT7PtINEeP4lqikROvq28anlVE9qqR/3iSZCT7yqf/KxAFJTR7+xxkZPfXJ42oYIsIRaFj4icfFt5mjuP+1l92zkowcnJyeMJz2TOHoQfcnLybpKbJuTj2+yj1qkKmpz8lvKUFSiDBH+2q01OvrW8Ko+r2e9kp5ucnDw+azEZedKd/lR3jpz85vK+ixV8A6c6rEFOTp7s/r3yTKbeFe3k5FvL06BTRaMqEF3yrRxy8vXkk+cq0hHReM8/1eMiJ99G3rejgtHt5JvJycnjlnCamlfnnaqwQk5O3v0GWpqkp9l7UgOQk5P3+XR/rnH2AAc5Ofl7svcgDb+4giYnX15eHTIMkoFq5EROTn5+TvTRi5ycnJycnJycnJycnHzF6wvW9McqgZJXbgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# HR 0.41
## LBBP vs 右心室起搏（房室阻斷）
### 95% CI 0.23–0.75｜P = 0.003

複合終點相對風險**降 59%**，與植入無關的嚴重不良事件相當（11.8% vs 9.3%）

---

<!-- _class: divider -->
# Pick #5
## SWITCH-SWEDEHEART
### Prasugrel vs Ticagrelor：打平手

---

# SWITCH-SWEDEHEART — 設計與結果

## [Omerovic E, et al. *N Engl J Med* 2026](https://doi.org/10.1056/NEJMoa2609057)

- 瑞典 registry-based、**stepped-wedge cluster RCT**；7 區 3 群 2021–2024 輪替切換預設藥
- 族群：ACS 接受 PCI 的未篩選真實世界，n=**17,095**（39.4% STEMI）

| 終點（1 年） | ticagrelor 政策 | prasugrel 政策 | adjusted OR |
|------|------|------|------|
| 死亡＋MI＋中風 | 11.8% | 11.1% | **0.90 (0.77–1.06)** |
| 大出血 | 4.4% | 4.2% | 0.80 (0.64–0.99) |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5CAAAAABRxsGAAAAB20lEQVR42u3b0Y6CMBQEUP//p9nHTQzWGUCxcHjaLChHE2/b6eWxzHo8yMnJycnJycnJycnJya8if7w//q9be9na2afr+ruRk5Mv43s+nV0jVCequ5GTk6/eKagoL4vTuHT1dyMnJ4/fKx3pq3chJyc/vLasXfKywPxUVSQnn1menq1qRjB9+PTKgpx8enmVce3+67R0jpx8Pnm8VROO71VG/ZUdLnLymeVrv/tg3l1NzdPIev/Kgpz8kvLx66rYOV1pV7tI5OS3lY+H7CDjStPq8cz/zTdBTn5X+THZc9V68cGqSE5+NXmwFA7y6P5/aVkhJ7+3vBrGN8bTwd7R/o5icvI7yIOBuu93SiNrcnLyuLZU9Wb82jTQPmj0Jye/mrzKn6oAOu1wJCcnP7ItcePebzDfJycnT9BB5LW1c6KpVeTk95b36+YxYc+am5ycfEl/7amjetC16vQnJyePj6DzuPpwX34qh5x8Unn13FwwIxjLx5//oHSOnPxq8rSipN4gwKraisnJyePtm37DNqhau9I5cnLycS1IS0gacpOTk2+Vp/1T6cM3QZUhJyeP4+m+Y+PcFTQ5+fTyPuNKc+ag1JCTk+/fJzr1ICcnJycnJycnJycnJ5/x+AP1TirVrC/GNgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# SWITCH-SWEDEHEART — 臨床啟示

> ❌ **政策層級比較：prasugrel 不優於 ticagrelor。**

- 缺血事件無顯著差（OR 0.90，CI 貼近 1 → neutral，非 positive）
- 大出血略少（OR 0.80），但同樣貼近界限
- 選藥仍以**耐受性、順從性、成本**個別化

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 操作者學習曲線 × BMI × 二葉瓣
### Drake 的主要臨床方向

---

# TAVI #1 — 早期職涯操作者的成績

## [Salah HM, et al. *Circ Cardiovasc Interv* 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016960)

- STS/ACC TVT Registry：**634,723 例、3,126 位操作者、847 家中心**；14.2% 由「獨立執業 ≤5 年」者執行
- 校正後 **30 天死亡相當（2.38% vs 2.44%，RR 0.97，P=0.293）**
- **複合終點反而略低（11.19% vs 11.77%，RR 0.95，P<0.001）**

> 💡 當代團隊化 TAVR 流程下，資淺本身不等於成績差——對新進結構介入醫師養成是正面實證。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAAAAAA+16u1AAACMElEQVR42u3by3LCMBAEQP7/p5NjLmBm9MKh2qdUHIw6hy1pZ/34+abrQUNDQ0NDQ0NDQ0NDQ0NDM6t5vL+CTzy78fe7l3cHV0BDQ7Nc87pwXGquF/PsKS+fV62AhoZmjyYoSdcLfPaogJSugIaG5gaa691OUKFoaGj+uSataemiaWhobqUJrNOtib4K0tDQHNEEy9r80+HOLQ0NzUDM+H7XMbiz+USKS0NDE5xvgtwzSEFmahoNDc0RTX+WCcLPIDhNc1QaGppzmqB09WMRaSXrNz80NDSLNFUNSvOQtGRWo5Q0NDR7NOk39f+JmfmpqZ4NDQ3NGk260alGoZMkYzrxoKGhmdHMHGPSz86coWhoaJZrgvyiaksGs1LXOcd8fkNDQ7OwO1jFm1XZ65NSGhqaPZrrwtZ/Ih2l7CNUGhqaPZq+m9m/JRUUtrRa0tDQLNf0owhVY3SwCUpDQ3NY04cYaXOkr4Lxq5M0NDRrNIMzUIN/1790cWSii4aGJs0qqtQiKGLpoDQNDc05zUwvIu2O9l1UGhqaw5r0rab0MJT2QFZ2bmloaGa6HIPRaJpnpgepgZpGQ0MzuBfoQ4egrxlEHGndpKGh2a0Jph96XBWjVEcgGhqaPZr0fFONQEwfcmhoaG6lScci+scHJyIaGpq7aIJdURp+VhEHDQ3Nbk1wNzl21ENPnzit0dDQ9L3OoMuRCtORio2dWxoami+4aGhoaGhoaGhoaGhoaGhomusXZxaHg+YZjOMAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TAVI #2 — DOUBLE-CHOICE BMI 次分析

## [Buske M, Feistritzer HJ, et al. *Clin Res Cardiol* 2026](https://doi.org/10.1007/s00392-026-03042-x)

- 隨機 DOUBLE-CHOICE 預設次群（n=752）；30 天複合終點

| BMI 族群 | 30 天複合 | adjusted OR |
|------|------|------|
| **肥胖（≥30）** | 15.2% vs 27.6% | **0.48 (0.30–0.75)**, P=0.002 |
| **過瘦（<20）** | 55.0% vs 23.4% | **3.74 (1.30–9.52)**, P=0.005 |

> 💡 TAVI 術前別只看「胖＝高風險」——**過瘦才是被低估的高風險表型**。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5CAAAAABRxsGAAAAByklEQVR42u3cQW7DIBAFUN//0u2yUpTY/0NqhfBYRWoNDy9gZiA5flZtBzk5OTk5OTk5OTk5Ofm3yI/r9vd/D58eennZfT8aOTn5xZiB9wETPJuORk5O/rT/lytK/8SzKfWjkZOTd44Uc762kJOTv31t6Tfv6k2Qk5OPxudV4B4sRPdlFuTky8sHa1yDnz6gOkdOvoo8Pqr5j7j7lhMucvKV5S9rUoMFrHSFCvojJye/OG+tplkl6N15MDn5rvIqig4ml4YP6bJCTk6elI6rKxVpAfrt1Tly8q+Up4MEwXd3/hOuUOTke8vTADrY3/ti8/yNYnLyHeTBll0l2elj5OTkA/LqqmJ1Rjxw5YOcfFd5dXyTTrN/E+Tk5FdpargCnG/8M2dH5OTkA2lvtdMnNeUmhiAn31tejRSvBU2UQE5OnsTnacZbVbaOsJGTk8/f+Q+S7PSs9uZv5ZCTLyrvvzc3c57UX0kmJyePfwOtT5TTgthU7k9OvoM8rWwl8fTENUdycvIBefCH9JbTwDJFTk5eyc97mSmIkZOTD8Tn5zl3FQfcnEGTky8vT2tcwb4dzHXgBZKT7ypfopGTk5OTk5OTk5OTk5Ov2H4BMCvyDd7atD8AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TAVI #3 — 二葉瓣 vs 三葉瓣展開幾何

## [Feng D, et al. *J Am Heart Assoc* 2026](https://doi.org/10.1161/JAHA.126.049690)

- 回溯 212 例（bicuspid 106 / tricuspid 106）接受 Venus-A 自膨瓣，術後一年內 CT
- Bicuspid：**殘餘跨瓣壓差較高（12.0 vs 10.0 mmHg，P=0.014）**、橢圓度較大
- 中重度 PVL、植入深度、不對稱展開、HALT 發生率無顯著差

> 💡 二葉瓣對自膨瓣的展開對稱性／殘餘壓差挑戰更大 → 術前 sizing 要算進去。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5CAAAAABRxsGAAAABxklEQVR42u3cQZKDIBAFUO9/6cw+FfF/MJlSnytTGngs0kAD2V5XvTZycnJycnJycnJycnLyu8i34+vt5be7Tx93H1S1kZOT79e5+zStffe7VW3k5OTbJ9FuMNkNA+NmVrWRk5MvydP+PWg/OTn5SfIgeuwWRU5O/sXxeTX4TifeP5lZkJNfXl7Nh5fvfpydIye/sjxeqjnut8e1/9sKFzn5leXB736csaqSX1VEIScnf1UFBiOCNPxUq0jk5I+V97FgnICuWnhS709Ofl95kMBKk9LBDqnJJpGTP1Ye5IXHg/T0QVo8OTl5ks+q9jtVrZ4oipycPO2eTxy9nxlbyMlvKe936/feZK12cnxOTv4YeZCn6ivuh//k5OQHsWVlVN6vEy3tKCYnf4I8uDsnC129R05Ovp62Sls9magmJyfvTp1OrhONe//Z0wrk5DeXT64dVQ3pW0NOTn5QQrWtOD2APnmOh5z82fJxRAlaGMSlpXkBOTl5deI8SDFXT9ezc+Tk5NXKUrqB46S5Pzk5+cqIoJ8IkJOTL/0Xd7BCW222Iicnn81x9dmuNDP97ewcOfmV5Ze4yMnJycnJycnJycnJya94/QEQRTzR2xS3DgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 三尖瓣 T-TEER 的右心重塑
### Drake 的 TriClip 面向

---

# TEER #1 — T-TEER 後右心重塑（EuroTR）

## [Stolz L, et al. (EuroTR) *J Am Heart Assoc* 2026](https://doi.org/10.1161/JAHA.125.048944)

- 國際 EuroTR 登錄，18 家歐洲中心，n=**699**；median 影像追蹤 407 天
- **右心室中段徑 40.2→37.1 mm、舒張末面積 28.7→26.2 cm²（P<0.001）**
- **手術成功與正向右心室重塑相關（OR 1.82，1.07–3.09）**
- FAC、TAPSE 略降 → 多屬容積卸載後「正常化」，非惡化

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5CAAAAABRxsGAAAABz0lEQVR42u3cS5LDIAwFQN//0s4+ZeMncD6Y9ipVyUCziBBCmW2f9dnIycnJycnJycnJycnJnyLfrp+3z11McvC5o1Has5GTk7+P2n73CNOe83T9wWzk5OQX3/tT+WnQaa+hNBs5OfleH2s4VSAnJ/9gbEmT9M7xyMnJe/PzYC8v/cX3Thbk5NPL0w39nle/qM6Rk08qr93XVFZYKl5/+oaLnHxS+Y1n5LQUXc/8ycnXlrd34aBilUaedhn7pl4LcvJHykupdBqmSp0Y5OTke8qvl7LS7b60VnLyteX16lRni0aw05OTk8c3QcERNz1Qt4/gd3YUk5M/TV4/+6aLS/sae3styMlXkA/HlrSZOOiwICcn7+h3CpL0dICUSk5O3vHlTzsxSqfloXsicvIV5KVgkqbcaa/UUI2LnHwZeXp4DurM6chpNyM5OflQ+0RwGO9s9ycnX1uePqU9v10aK4UVcvK15fXfzaXNGsGdEDk5+VCNq7PifGOrIjk5ee3/t6SLq2flQ52W5OTknVdEpYsmcnLyDnk7ZrQz9bSBg5ycvDc/H6mFBbnBUGwhJ3+4fLjGNRJqfludIyf/b/kUDzk5OTk5OTk5OTk5OfmMzwspnZVcVQFaUwAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# TEER #2 — T-TEER vs TTVR：怎麼選？

## [Hahn RT, et al. *Curr Opin Cardiol* 2026](https://doi.org/10.1097/HCO.0000000000001359)

- T-TEER 目標：殘餘 TR ≤ 輕度；能否達標取決於**三尖瓣解剖 + 經食道超音波影像品質**
- T-TEER 安全性極佳，但特定解剖下療效受限 → TTVR 可能更合適

> 💡 三尖瓣介入不是「一種裝置打天下」——先用解剖與影像可行性選 T-TEER 或 TTVR，再談裝置。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAAAAAA+16u1AAACRUlEQVR42u3bQW7jMBAEQP//08lxgYVNdw8pOdktnWRAEFg+DDjT1OPrX7oeNDQ0NDQ0NDQ0NDQ0NDQ0u5rH++vPc3/dPXvVs0devrRaAQ0NzYWa14Xj/coD13pt0xXQ0NCc1qwr2boePvuZlr3hCmhoaG7WrBe9dr3ZotDQ0PwezcuNSdXQ/JSaRkND0zcqwXrXhe1kh0VDQ3NQM5x1Hrz7AZNbGpr/VRPHjK82MMNg47MpLg0NzXrnENSbPuJ4NNfJfRoNDU21s0kHF0ELtK59678yKHs0NDSHNOlbg3ML1SmnfqxBQ0NzjaYKMdIlpM3Qff0NDQ1NUNPW/ch2Jevbp+msk4aGZicjGA4z0tJ1cHtDQ0NzSDM89FTNSbejVhoamqs1ScAQnlysdizVcQcaGpoLNTutSPXhRPrv7FdoGhqandwz6H6Cshf8vCXFpaGhSacc1UBi6/TS7AwFDQ3NhZo0tuxbkTTE6GNQGhqaazTD/qZKMm5JcWloaIaJx04S2c86h40UDQ3NSc26oelTzLRQBpMPGhqamzVpu1NFmWlRPJR70tDQ7CQe6byjT0GqqQkNDc3NmmGdqwYm67th7EFDQ3NIUx1OTvuR4FRD1UPR0NBcrakqWXDgsf9oajBPpaGhOa1Jy1TaAg0PUe3nnjQ0NJdo0ilHPzWZRqM0NDQf0FSPrLdB67Tk6p0NDQ3NsL+pNjVVuzMYqtLQ0BzUVM3G9Lvm5oRUoqahoTmj+bUXDQ0NDQ0NDQ0NDQ0NDQ1Nc30DQFL9G9tT5hIAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## Lancet／EHJ／JACC／Circulation

---

# 其他值得一讀（1/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **DAPT-SHOCK-AMI** ❌ | *Lancet* | AMI-CS：cangrelor 血小板抑制更佳（100% vs 22%），但 30 天硬終點**非劣未達**（P=0.13） | [DOI](https://doi.org/10.1016/S0140-6736(26)00976-1) |
| **SYNCHRONIZE-CVOT** ✅ | *Lancet* | survodutide CV 安全：**HR 0.89（0.67–1.18）**，非劣 P<0.0001；腸胃道副作用多 | [DOI](https://doi.org/10.1016/S0140-6736(26)02140-9) |
| **TYDAL-TIMI 78（ANGPTL4）** ✅ | *NEJM* | 抗 ANGPTL4（MAR001）12 週三酸甘油酯**↓39–45%**（P<0.001，替代終點） | [DOI](https://doi.org/10.1056/NEJMoa2612463) |
| **STREAM 停 statin** 💡 | *NEJM* | ≥70 歲初級預防停 statin：2 年**非劣**，但事件數值偏多（12.7% vs 9.2%） | [DOI](https://doi.org/10.1056/NEJMoa2606634) |

---

# 其他值得一讀（2/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **ARC 主動脈症候群排除** ✅ | *EHJ* | 7 變數床邊規則，外部驗證 **sensitivity 100%**，可安全排除 36% | [DOI](https://doi.org/10.1093/eurheartj/ehag875) |
| **LAAC vs 抗凝（Evidence Review）** 💡 | *JACC* | OPTION／CLOSURE-AF／CHAMPION-AF 應視為各自實驗，以表型判讀適應症 | [DOI](https://doi.org/10.1016/j.jacc.2026.09.018) |
| **FRAGILE** RCT | *Circulation* | 前虛弱／虛弱者 CABG：off-pump vs on-pump 30 天與 1 年結果 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.125.078842) |
| **二尖瓣 cerclage 5 年** ➰ | *Circ Interv* | MR↓、LVEF↑，但 6/18 完全房室阻斷致試驗暫停；益處第一年最明顯 | [DOI](https://doi.org/10.1161/CIRCINTERVENTIONS.126.017202) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構介入救援 × 困難解剖個別化
### 2026-11-06 ~ 11-13 published × 5

---

# Case #1 — TMVR in incomplete ring + LAMPOON

## [Ozdemir D, et al. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.111216)

- 54 歲缺血性心肌病，曾 CABG、aortic ViV-TAVR、二尖瓣 31 mm Duran band 修補後嚴重復發 MR
- 前葉過長、neo-LVOT 阻塞風險高 → **antegrade LAMPOON 前葉撕裂**後行 valve-in-ring TMVR
- 借**鄰近主動脈人工瓣**當錨定點，術後無 PVL、無明顯 LVOT 壓差

> 複雜 valve-in-ring 要靠 multimodality 規劃；鄰近人工瓣解剖可「借來」錨定。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAAAAAA+16u1AAACNklEQVR42u3bQW7DMAwEwPz/0+0L7OxKopMWo1OMBK3GB4IiqdfPf1ovGhoaGhoaGhoaGhoaGhqaXc3r/br/3eW39/+j3wENDc2g5jpwXP6t2y9S5tYOaGhoTmsuY1Ww335vl5+CHdDQ0HxC0wsvH7ffJw0NzRdo0owlyGdoaGi+RZNa+zzlPgP6xGmNhoZmsdY59+kTlVsaGpquzfg+QqWNjSCSTXdxaWho7jOHNN4E9KDyEbwEGhqaQU26j51phepoE7wsGhqak5rF2aa0fJmOQKRlFxoamhlN0KEICplVihKHroP9GxoamjSV6c8jVd+zb6HS0NA8p6mmFRYfz6Q3NDQ0hzRpQSLNhYL5x+pIRUND85wmPZ6kh5dF8FZmQ0NDsz0vEDQrg3304H5AgoaG5pCm6l/0I41BwSQtjtDQ0MxoqkmHFPKmVxFesNiq2dDQ0CxmNmkSUpVJ0kwpUNPQ0BzX9EWK+7iUDkr3jzQ0NDOanRmFxatSvZqGhmZQk8abIBdKE6K+fkJDQ/OIJi1NLF5+SM9Gh7q4NDQ0O7XOIMD0tyeqe5Y0NDTPadIVHG3SzkjVaqWhoZnWpHeeqkuPwRFocKKLhoZme16g74Cm/ZDFfisNDc0jmjRtSecaq4HHvjNCQ0PzsCatTabl0KCKOhjTaGhoFjV9OlJds6oKnjQ0NMc16fkm7YcEeU+/IRoamhlNNevY9z62CyY0NDSDmj+7aGhoaGhoaGhoaGhoaGhomvULLFKnVWHhEWcAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #2 — Sutureless 主動脈瓣移位 bailout

## [Hamada Y, Kawamura T, et al. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.111211)

- 78 歲洗腎、微創雙瓣置換用 sutureless 主動脈瓣，脫離體外循環失敗、雙側冠狀動脈灌流不足
- **先預置經心尖 transcatheter 瓣膜**，再經股動脈 wire-loop 復位移位瓣
- 恢復冠狀動脈血流、即刻完成置換；5 個月心室功能保留、位置穩定

> 「先預置、再復位」把空環時間壓到最短。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAAAAAA+16u1AAACL0lEQVR42u3bQW4CMQwFUO5/6XaPSvh2nBmoXlaVoDCPheV8J4+f/7QeNDQ0NDQ0NDQ0NDQ0NDQ0u5rH+/X05vW/rd/39Gr9CWhoaM5oXheOP15dk4JPXuPS56OhoRnXBOVnbUhL1/YT0NDQ3KZ5WbpKi4aG5ns19VqVGmhoaD5AE1gDUmmTc9tujYaGpp40Hv7r4uSWhoamO2t8H1+uq9v6AS+e4tLQ0Kw7ljTITGtfcxtDQ0NznaY5p2zudOIGZiezoaGhaaYcaROSHn+q90KTZ6BoaGjSlKPUmJSOO9SPTSYhKA0NzYwmaEfWZa+Za5Y+ioaG5hJNMOgsvRr0OGl7Q0NDc1AT1JtgQ5Pepip9ZbdPo6GhmelsSoej0t4leHwaGpqLNfUWJa1GQXmkoaH5FM1MXLENGerTaGhompp0L1M6KpFOQBtnMmhoaGY0M4eeZjql4IehoaEZ12zfjWp2QNuLhoZmSJPudNLRaNC2NL+XhobmjKZZv0qtzHacQkNDc1BTn102Y5LGKaedE100NDQ7c890Opmq06NTZ6a4NDQ09ayzNMloTjbTqxb7yS0NDc1M1hlMO9eNTokZRKQ0NDSTmnUlqweewV6mGYzS0NAc1KRbjKarVEv3Uw4aGpppTelqU+kmZWmOSkNDc5smiD9mRhxpt0NDQzOuSechpWq0E5gc3K3R0NDUs870tkM62SzdpKShoTmo+dpFQ0NDQ0NDQ0NDQ0NDQ0NTWb/2mmOLzOqkkQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #3 — LOT-CRTD 救 TAVR 後 LBBB

## [Chin EYH, et al. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.111159)

- 67 歲高風險左主幹-LAD PCI 併心因性休克、嚴重 LV 功能不良
- TAVR 後新發 **LBBB** 且 LV 功能持續低下；單純 LBB pacing 僅高輸出才能矯正
- 加冠狀竇導線做 **LOT-CRTD**，3 個月 LV 功能完全恢復、逆重塑

> 與本週 OptimPacing（LBBP）主題呼應——TAVR 後 LBBB+LV 功能不良的裝置策略仍空白。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAAAAAA+16u1AAACQElEQVR42u3cS1bDQAwEwNz/0rBkg51uS4n5lFfwEpIpL/rNSDKPj790PWhoaGhoaGhoaGhoaGhoaKaax/Pr633f/cXhp5x/R78CGhqaF2qOg+ObV598ScO8uAIaGprXaM6TrHpLsLYqLWloaH6AJn01+HVyP2loaO7VpEeWw88L0o2GhuY2TWqtdizJsm44rdHQ0Ixrnds/3Vu5paH515q4zdiUP4LGxr1dXBoamqCnEeRNQK+i6/Am0NDQvFCTrmMyrXC4wL6tSkNDs645r2MEx51glX0eznc2NDQ0O5qgJFKdby5E17h/Q0NDU2mCcBr3PaubMMo0Ghqaccej36ekSTbe3tDQ0CxpqqrneSSlO6Xg3iVgGhqabU169qgejUgPQ0tVDhoamvG8QPXgU2Co2h7p7CQNDc2mZrKpSSsf1d5lvrOhoaEZZ1r60Vefanpe/9zc2dDQ0FSadJYhjccg3c5TdelJLxoamj7T+uHGanyi/5WGhuYtmjScgthLjzt9tZWGhmZTExxZ0uPJRWtQP6GhoXmLpppWSJOsqmPMJyFpaGguVgf7gaRgQCL9gLfMQ9PQ0Hzs/c+UdMvTb1uqtgcNDc2S5vH8SjubO9b5RBcNDc1OrbOqhFbzDUGm0dDQ3KFJn3S6WPSosnTe96ShodnWTCYY0m5J1xqloaG5QVN1O9PDy8WCJw0NzbomeDUdZ047Hv2CaGhoXqOpDi9VTKVh15c6aGholjS/9qKhoaGhoaGhoaGhoaGhoWmuTyytCwBy/rBmAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case #4 — TAVR 釋放球囊縱向破裂、順利回收

## [Iwata R, et al. *Catheter Cardiovasc Interv* 2026](https://doi.org/10.1002/ccd.71020)

- 八旬女性，23-mm SAPIEN 3 Ultra RESILIA；球囊近標稱充盈量時於 STJ 鈣化處破裂
- 立即抽吸→球囊完全塌陷、無殘餘對比劑→無阻力回收進 14-F eSheath
- 檢視見**縱向（非環向）撕裂、無碎片殘留**

> 回收前先確認「塌陷是否完全、幾何正常、抽吸反應、退出阻力」；破裂型態影響可回收性。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5CAAAAABRxsGAAAAByElEQVR42u3c0W6DMBAEQP7/p9PHSlVxd4lpazx+ihQSxkicz3chx2vVcZCTk5OTk5OTk5OTk5M/RX78PKqPfb775eC3zkZOvrX8/KY+O2d68MWzkZOTJ7bTcHH6bvWJcUgiJye/ID89root5OTkM+V9fv4dn5yc/J78fLygB2Hlz3YW5OTLy4Oq08RXv1ydIydfWR63apqt9b/qcJGTryzvq9DVvIJ0ffzN5OR7y8fJQHBwkLifeoNrQk6+t7yKCn0FbE6qQE5O3gWT/luqqZOTk7+qYJJ2bcd164s1anLybeXB4n06pTGmnyE5OXlM7Tu549mMm0VX6+fk5HvJ+yy6Wv37Shk5+d7y8T0eb3GnzHrm3p+c/EHydFFO1/c0y4/rY+TkW8v730ZUmUNVASMnJy+z4+FWuA81fTuXnJz8Que1L1Tfk7eQkz9XXvWOxgt69bRNFWXIybeVV0+yVcGkmiY5OfnMp8HT9GHcAI4Z5OTkaZsn7Qkd4QiSAXJy8rf+YSkNIdXvNMjJyTt5uilOQ1KapJOTk19IvtNNdnoRJtXPycmfJk8T6GDx7sPP3dU5cvKV5UsMcnJycnJycnJycnJy8hXHB9sc0jssxD0zAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case #5 — 三瓣同時衰敗的分階段 ViV

## [Del Castillo DV, Wang Y. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.110544)

- 78 歲紅斑性狼瘡、第 4 期 CKD、嚴重虛弱；8 年前三瓣外科生物瓣置換，如今三瓣同時衰敗
- 手術風險過高 → **分階段全經導管**：ViV-TAVR（＋BVF）→ ViV-TMVR → ViV-TTVR
- 全程無併發症，2 個月 NYHA III→II

> 禁忌再開刀的多瓣衰敗，分階段 triple ViV 是可行替代；關鍵在影像與順序安排。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAADNCAAAAAA+16u1AAACP0lEQVR42u3bQW6EMAwFUO5/6emymyZ8xwliqseKEWjIY2E5trk+/+m4aGhoaGhoaGhoaGhoaGhouprr/ghu/uuW35/Dq/UV0NDQnNGMA8f0walw/rTSCmhoaA5qhkudnw0XmJLSFdDQ0LxKMw9safZEQ0PzbZphNOr8pKGheYsmsM4TmCAepv98erdGQ0NTrzQePnu4cktDQ7PQZiznPaXg+XAXl4aGJtjfpIXMedGjE9NoaGie08wXE9Qi6sWM9O208jQaGpo0s0mHntLZiHqdtFT5oKGh2alJY1Vn3CFtZ5zu39DQ0AQLTNOMThs0fVmtPI2GhmYxppUamO0ZqMWMioaG5owmePD8viB+lSqcN5kSDQ3NEU16S31uev5Otlc5aGho2h2PUhG0dDXtnraqHDQ0NPUZqE74KbUt08IKDQ3Nw5p0bUEbdF7NTJ+72sWloaFp72/SOaZgbYuZzaZaJw0NTX1/E9Qm0wtpqSNtcdDQ0BzUlHoVwZuoR7yFUQkaGprdmvSsHRnTkNnqe9LQ0CxqggbI8HEpOC22tDIbGhqaPVWOtCG6UKq8L2tsr9nQ0NB8Gke9T1nvZ6bz1TQ0NDs19Y8V0i3QYtm0v7+hoaFp7wgWl5/ON5S+oaKhoXlOk05Gl/oh85+lcQcaGpq3aNKolfZH0whKQ0PzUk060RSMSdXKLjQ0NLs1wdV6NKqNOF9nv/qmoaHp1DoXw1TwIVU9qaGhodmp+dqDhoaGhoaGhoaGhoaGhoamcvwAkuj/4BcXTL4AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 💎 整合 Take Home

---

<!-- _class: lead -->
# 💎 本週 7 大臨床啟示

### 1. **降 Lp(a) ≠ 降事件**（Lp(a)HORIZON，HR 1.02）— 療效標記漂亮不保證臨床獲益
### 2. **殘餘發炎假說再受挫**（ZEUS，HR 0.99）— IL-6/CRP 大降、MACE 沒動，感染偏多
### 3. **降壓目標看族群**（OPTIMAL：DM 0.90 NS／Stroke 0.79 有益但腎臟代價）
### 4. **房室阻斷改 LBBP 真有用**（OptimPacing，HR 0.41，提前中止）
### 5. **Prasugrel ≈ Ticagrelor**（SWITCH-SWEDEHEART，缺血 OR 0.90）— 個別化選藥
### 6. **結構介入三訊號**：資淺操作者成績不輸資深；過瘦是 TAVI 隱藏高風險；三尖瓣 T-TEER 後右心逆重塑
### 7. **看主要終點與 CI，不要看摘要用語**（DAPT-SHOCK-AMI／SYNCHRONIZE／TYDAL／STREAM 各有陷阱）

---

<!-- _class: ref -->
# 完整參考文獻 (1/2)

**NEJM（AHA 2026 Late-Breakers）**
1. Cho L, Nissen SE, et al. Lp(a)HORIZON. [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMoa2610159)（PMID 43001734）
2. Ridker PM, et al. ZEUS (ziltivekimab). [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMoa2612126)（PMID 43001751）
3. Santo K, et al. OPTIMAL-DIABETES. [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMoa2612922)（PMID 43001746）
4. Sampaio Silva G, et al. OPTIMAL-STROKE. [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMoa2612924)（PMID 43001741）
5. Qian Z, et al. OptimPacing (LBBP). [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMoa2612972)（PMID 43001763）
6. Omerovic E, et al. SWITCH-SWEDEHEART. [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMoa2609057)（PMID 42670968）
7. O'Donoghue ML, et al. TYDAL-TIMI 78 (ANGPTL4). [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMoa2612463)（PMID 43002172）
8. Rodondi N, et al. STREAM (statin discontinuation). [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMoa2606634)（PMID 43001742）

**Lancet**
9. Motovska Z, et al. DAPT-SHOCK-AMI. [*Lancet* 2026.](https://doi.org/10.1016/S0140-6736(26)00976-1)（PMID 42998670）
10. Bozkurt B, et al. SYNCHRONIZE-CVOT (survodutide). [*Lancet* 2026.](https://doi.org/10.1016/S0140-6736(26)02140-9)（PMID 43003106）

---

<!-- _class: ref -->
# 完整參考文獻 (2/2)

**EHJ / JACC / Circulation**
11. Ohle R, et al. ARC (acute aortic syndrome rule-out). [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag875)（PMID 43006790）
12. LAAC or Anticoagulation for AF: JACC Evidence Review. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.09.018)（PMID 43018506）
13. Salah HM, et al. Early-Career Operators & TAVR. [*Circ Cardiovasc Interv* 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016960)（PMID 43012117）
14. Rogers T, et al. Mitral Cerclage Ventriculoplasty 5-Yr. [*Circ Cardiovasc Interv* 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.017202)（PMID 43012111）
15. FRAGILE Investigators. Off-Pump vs On-Pump CABG. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.125.078842)（PMID 43006184）

**TAVI / TEER + Case Reports**
16. Buske M, Feistritzer HJ, et al. DOUBLE-CHOICE BMI. [*Clin Res Cardiol* 2026.](https://doi.org/10.1007/s00392-026-03042-x)（PMID 43018714）
17. Feng D, et al. Bicuspid vs Tricuspid after TAVR. [*J Am Heart Assoc* 2026.](https://doi.org/10.1161/JAHA.126.049690)（PMID 43018038）
18. Stolz L, et al. T-TEER Right Heart Remodeling (EuroTR). [*J Am Heart Assoc* 2026.](https://doi.org/10.1161/JAHA.125.048944)（PMID 43018056）
19. Hahn RT, et al. T-TEER vs TTVR. [*Curr Opin Cardiol* 2026.](https://doi.org/10.1097/HCO.0000000000001359)（PMID 42989943）
20. Ozdemir D (111216)・Hamada Y (111211)・Chin EYH (111159)・Iwata R (ccd.71020)・Del Castillo DV (110544). *JACC Case Rep / Catheter Cardiovasc Interv* 2026.

---

<!-- _class: abbr -->
# 縮寫對照 (1/2)

| 縮寫 | 全名 (English) | 中文 |
|------|------|------|
| MACE | Major Adverse Cardiovascular Event | 重大不良心血管事件 |
| HR / OR / RR | Hazard / Odds / Risk Ratio | 風險比／勝算比／相對風險 |
| CVOT | Cardiovascular Outcomes Trial | 心血管結果試驗 |
| Lp(a) | Lipoprotein(a) | 脂蛋白(a) |
| IL-6 / CRP | Interleukin-6 / C-Reactive Protein | 介白素-6／C 反應蛋白 |
| ASCVD | Atherosclerotic Cardiovascular Disease | 動脈粥樣硬化性心血管疾病 |
| CKD / eGFR | Chronic Kidney Disease / est. GFR | 慢性腎臟病／腎絲球過濾率 |
| T2DM / TIA | Type 2 Diabetes / Transient Ischemic Attack | 第二型糖尿病／短暫性腦缺血 |
| LBBP / LBBB | Left Bundle-Branch Pacing / Block | 左束支起搏／傳導阻斷 |
| CRT-D / LOT-CRTD | (LBB-Optimized) CRT with Defibrillator | （左束支優化）CRT 併去顫器 |
| ACS / STEMI / MI | Acute Coronary Syndrome / ST-Elevation MI / Myocardial Infarction | 急性冠心症／ST 上升型／心肌梗塞 |
| PCI / CABG | Percutaneous Coronary Intervention / Bypass | 冠狀動脈介入／繞道 |

---

<!-- _class: abbr -->
# 縮寫對照 (2/2)

| 縮寫 | 全名 (English) | 中文 |
|------|------|------|
| TAVR / TAVI | Transcatheter Aortic Valve Replacement / Implantation | 經導管主動脈瓣置換／植入 |
| TMVR / TTVR | Transcatheter Mitral / Tricuspid Valve Replacement | 經導管二尖瓣／三尖瓣置換 |
| TEER / T-TEER | (Tricuspid) Transcatheter Edge-to-Edge Repair | （三尖瓣）緣對緣修補 |
| ViV / BVF | Valve-in-Valve / Bioprosthetic Valve Fracture | 瓣中瓣／生物瓣破裂擴張 |
| MR / TR | Mitral / Tricuspid Regurgitation | 二尖瓣／三尖瓣逆流 |
| LVOT / LAMPOON | LV Outflow Tract / Leaflet laceration | 左心室流出道／前葉撕裂技術 |
| PVL / HALT | Paravalvular Leak / Hypoattenuated Leaflet Thickening | 瓣膜旁漏／低衰減瓣葉增厚 |
| LVEF / FAC / TAPSE | LV Ejection Fraction / Fractional Area Change / Tricuspid Annular Plane Systolic Excursion | 左心室射出分率／面積變化分率／三尖瓣環收縮位移 |
| LAAC | Left Atrial Appendage Closure | 左心耳封堵 |
| AMI-CS | AMI–Cardiogenic Shock | 急性心梗併心因性休克 |
| GLP-1 / GCGR / ANGPTL4 | GLP-1 / Glucagon Receptor / Angiopoietin-Like Protein 4 | 相關受體與脂質調節蛋白 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**
心臟內科｜結構性心臟病介入

*本文件為讀書會共筆之教學整理，*
*僅供醫療專業同仁臨床教學交流參考。*
