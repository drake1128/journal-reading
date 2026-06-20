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
  section.abbr { font-size: 0.62em; }
  .qr {
    position: absolute;
    right: 40px;
    bottom: 80px;
    text-align: center;
    font-size: 0.65em;
    color: #555;
  }
  .qr img { width: 110px; height: 110px; border: 1px solid #dcdde1; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-06-13 ~ 2026-06-20'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-06-13 ~ 2026-06-20

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Pick / 文章附 QR Code，可掃描跳轉原文

> 本期已與上一期（2026-06-19）交叉去重，全為新刊出或未收錄之文獻。

---

# 🎯 本週主題與固定欄目

## 精準化 × 可近性的雙軸

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 本週 TAVI 重要文獻
3. 🔧 **TEER Section** — PASCAL / MitraClip / TriClip 進展
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — JACC Case Rep / EuroIntervention × 5
6. 📖 **參考文獻 + 縮寫對照**

---

# ⭐ Top 5 Picks

| 試驗／研究 | 期刊 | 關鍵數字 |
|------------|------|----------|
| **Elecoglipron**（VISTA/SOLSTICE） | *Lancet* | 體重 **−11.8%**（36 週）；HbA1c **−1.88%** |
| **Black Americans CV 死亡率** | *JACC* | 進度報告：種族落差持續（2000–2024） |
| **AI-ECG 偵測 HCM** | *JACC Adv* | AUC **0.946**；特異度 **100%**；提前 2.6 年 |
| **CKM 危險因子治療** | *JACC* | 高血壓／高血脂僅約 **50%** 接受治療 |
| **Genome-First FH 族群差異** | *Circulation* | 非洲血統 VUS → MI OR **1.91** |

---

<!-- _class: divider -->
# Pick #1
## Elecoglipron（VISTA + SOLSTICE）
### 口服小分子 GLP-1 受體促效劑

---

# Elecoglipron — 設計

**Davies MJ, et al.（VISTA）/ Aroda VR, et al.（SOLSTICE）**
🔗 [VISTA DOI: 10.1016/S0140-6736(26)00748-8](https://doi.org/10.1016/S0140-6736(26)00748-8)

- **每日一次口服小分子 GLP-1 受體促效劑 (GLP-1 Receptor Agonist, GLP-1 RA)**，無飲食／飲水限制
- **VISTA**：肥胖／過重、無糖尿病，Phase 2 劑量探索 RCT，n=**310**，36 週
- **SOLSTICE**：第二型糖尿病 (Type 2 Diabetes, T2D)，Phase 2b RCT，n=**404**（含 oral semaglutide 對照）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAAB50lEQVR4nO2YMW7lMAxEH78MpJRvkKPQN8vV5KPkBlQZgMZsIf9ss9mtFmERVYbZPBCjEYcmvjzX4+sa/BT/XZxmZhsn8wCuHdsxM7OjIi0uCRy4dl7iVNAkRcnegtnBPK6dDRKuHaZt3wj07+JJHwlbGaC/F1uc2zxyHkvA3w/0h7MBgg1nvrXEuhBbF7Mg7QNOM2Nxz6O9H9s8LjPbC9KidQJJLTw//0hZkDYcaFLTUAC+3KzVpNVogSSgaWRXdtEHeE3axaaAPhTewhVetLeBwhdzLgF0LUmUpHWghWfX3WF8XbqKtFL2oUBBdjWNhMK6FV1LBoDCW9x6KEk7miQNuHvbAqh8y6CPpsESMCSuKKmEgD4Sp0vS83sU1W3QpPWReNOQlGWVICWefWQfdOVTDCV7+4CzBRt3cNj6+HgdQPZRcQYLsiv7SMjnY0FX1Vvm2ZdrIY3sasG6dPVo7+LH7i18m29Mo2u5WT0lPGCJ9rxe15urnGZmOQvuEz6zg7fwdivBFV7SE1DAcw6nj7UJaUXn28e9q5lvL+93lkzItWgqR7ssy28fwBUsfyg6g920Th/LDfKZd+rR/t4kiZNpbR6JWw8Y9fa3K5SpSWtOWAGtcorkmcvWSHPPkBV1az+b/P9W/AWzm49R83OlXAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# −10.5% → −11.8%
## VISTA 體重變化（26 → 36 週，75 mg）
### vs placebo −0.6%／−0.3%；尚未進入平台

SOLSTICE：HbA1c **−1.88%**（75 mg）vs placebo −0.15%

---

# Elecoglipron — 臨床啟示

> 💡 口服小分子 GLP-1 RA（非胜肽、無飲食限制）若 Phase 3 重現此效力，將大幅改善代謝治療的**可近性與順從性**。

- 已宣布進入 **Phase 3**，含**心血管與腎臟結局試驗**
- 對台灣龐大 T2D／肥胖共病心血管族群具高度潛在意義
- 仍須等待 head-to-head 與長期心血管硬終點數據

---

<!-- _class: divider -->
# Pick #2
## Excess CV Mortality
### Black Americans, 2000–2024（JACC 進度報告）

---

# Black Americans CV 死亡率 — JACC 進度報告

**Arun AS, Yancy CW, Krumholz HM, et al.**
🔗 [DOI: 10.1016/j.jacc.2026.05.013](https://doi.org/10.1016/j.jacc.2026.05.013) ｜ PMID: 42319310

- 回顧 2000–2024 年美國黑人 vs 白人族群的**心血管超額死亡**與**壽命年損失**
- 經二十餘年努力，種族落差**仍持續存在**
- 強調結構性與社會決定因素的長期影響

> 💡 證據不足以消弭不平等 — 需政策與照護路徑改革。台灣應警覺城鄉與社經落差對心血管照護的影響。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABtElEQVR4nO2YsW0lMQxEn0wBG3I7+KXod+CSFleSO9CW4gIMcMMPaDEXaO3k7hxcYDMwA0ESk8GQQ4oq4u92Pv3DAT8eQAFgAd6HS9EAaOP7sT1Bk4RLwRL7eesmKTLw9gSUcgfqsY1J4FHqFyP43HPcH+vOsXHcvwnBn1bfN3v1l/P2Ut++GsHnHqlDU2DBYwXXyIJtL6UA9djqsS3BWUpZM2BD0wJJpm7XWQlqCIqmaNBwWTC8z8sE2CqA97MiOG99eXsGCi1BTK98W4LKzrENGLQctRep45qRnVmnYGTpWQz2cvtVoUJZd1x4z8Gb5qpgeLfAghy9HqkPGi5cg2bqpm4pdIqimTTXAVMLOfLtqr14N8mCKYfhWWqvSYOG9+HdokESnU7eOq7hGjRJFi1Hvl1vy3HcgSV2YMBjzVB7K8c6alu0z/NZASyeE2D7eIc0C4bLrgaRI6ZHKaVUwDtHeaxU9hzzAoomyaYE1CdveWoItOvl5n28XybA9u7xbq8btCXa7LBJYgrNJJOGS+pztEnCm9SBsxR7LaVs50qOOevjP6ThXbryLYcWys8f1395fgOyIjlqVHA9mgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# Pick #3
## AI-ECG 偵測 HCM
### Viz HCM 演算法外部驗證

---

# AI-ECG 偵測 HCM — 設計與結果

**Park J, et al.** *JACC Adv* 2026;5(7):102914.
🔗 [DOI: 10.1016/j.jacadv.2026.102914](https://doi.org/10.1016/j.jacadv.2026.102914)

- 150 例心臟磁振造影 (Cardiac MRI) 確診肥厚型心肌病 (Hypertrophic Cardiomyopathy, HCM) + 83 對照
- Viz HCM 12 導程心電圖 (Electrocardiogram, ECG) 演算法

| 指標 | 數值 |
|------|------|
| **AUC** | **0.946**（0.916–0.970） |
| 敏感度 / **特異度** | 58% / **100%** |
| 提前診斷 | 中位 **2.6 年** |

心尖型 (apical) HCM 為正確偵測預測因子（OR 4.71）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAACAElEQVR4nO2YMW7cMBBFH5cCUo6AHCBHGQE5QI4U+Ei5wegoPoCBUWmAwk8xK3e20wTLwix2oZ3maXb4/yebeHedt/dr8FX8rIgSoCfDdH+06reP6Whv4JK4UM+VnnRJOWFvb0BrG+wcDbxLHBtHWx4I9O5a7t/HBt7sz/KyilgeB/RPtNDH/jM5V+f49UCgT4tSgJ8rHBv2BGAaDwT6qLi31oD+/Ls+Fzhba+uEtKhWepeAriiVkDSjgh0bx9ZWXlekOFd67q01jm3O3mIxYFiAK31YSNFn7C1KB8AxDYvyMimmnASkGCCpnLcrlNQkz0ibgHcFFl0CHxYU/4S0CikGjknpw1SaMO3cDhMWw9TT775ggU1Jq1D6AKDrLg594l0GpQOiONMr7s5Im650ST19VCyvV5iR9ga0lbaCxYJjqoQzZRq/54Rh0ZOePu42Mafe3mBv6/4tef0R51qpZv/23B4I9MEqqx3U9AYwrpPafL1FUv37Jba114bFpJogUWEGpyTXVFFhRtqkzEt5uUP9Pift29khGXhP7+l1lJiRNgFKvgAp+rxedrvuauL1R3TFAoNq8pwK5uA93wK5V7endIfr9sPiXOgvbXyPZmp4s5z5RnTBwWHvzxvsU07CjSs0KsGeOLZxHdbmo33TBB+mew7PK6JPR9u+bvL/W/EvZoycdMP/HB4AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# AI-ECG 偵測 HCM — 臨床啟示

> 💡 高特異度（100%）+ 可提前偵測 → 適合作為**機會性篩檢 (opportunistic screening)** 的「rule-in」工具。

- 敏感度 58% → **不可**作為排除工具
- 心尖型 HCM 偵測力最佳
- 可整合於健檢／門診 ECG 流程，及早轉介影像確診

---

<!-- _class: divider -->
# Pick #4
## CKM Syndrome
### 心血管代謝危險因子治療現況

---

# CKM 危險因子治療 — NHANES

**Gong J, Wadhera RK, et al.** *J Am Coll Cardiol* 2026 Jun 17.
🔗 [DOI: 10.1016/j.jacc.2026.04.031](https://doi.org/10.1016/j.jacc.2026.04.031)

- NHANES 2015–2023，n=**6,384**，Cardiovascular-Kidney-Metabolic (CKM) syndrome ≥stage 2

| 危險因子 | 治療率 | 治療者控制率 |
|----------|--------|--------------|
| 高血壓 | **51.3%** | 44.7% |
| 高血脂 | **48.8%** | 68.2% |
| 糖尿病 | 83.4% | 47.3% |

缺口最大：**20–44 歲年輕成人**、女性、西班牙裔

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABgUlEQVR4nO2YMW4kQQhFX021NCF7gzkKczPLN8NH2RswOa3voMoT2VppA5vAqKWmRfL1gQ/0EJ/befkiAL8RQAkwc/tKB8Dr57FdwCUteIfFeYspKTvwdgHGuIMXFH4Aj3F8M4LP7dhvez1vMT6S+50I/h15vBy4pHPc22BD6ZKmovC5fSmb9MLbGIPHyzUBjsf9HGP86cHbtsACvPD13YA3lF4AjqksiiVxHXKKJCzKYiqARR3WhDfKhMVypoRp9smphdKnVDAVUvToU5Q+FVgoHdN6+mADCq9VdblGQw9s0lSAKykoC/DZhTdmUhaYZjomSX2wLWD1ob1l0Ud714KEaSnwaooe2JgJFhsbPhtpCM+5UCYAizbaC6apmNrzFOiS02W76nyJSY9euPAYY4yDt5kc9spzTe+Abd9Za1NCSeE9sG0NmUnB3Lsc1aLenhG/pp+3uK6T4e+9EW+KNeuxWB3RgLfnnSUlrIGV9Jmn7ErbA2tdgg2wjd9/XP8VeQfqg0HAWliIWQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# CKM 危險因子治療 — 臨床啟示

> 💡 真實世界中**僅約半數**接受高血壓／高血脂治療，且控制不足。

- 年輕族群、女性是被忽視的高風險群
- 勿因「年輕」低估心血管代謝風險
- 及早起始 guideline-directed 治療

---

<!-- _class: divider -->
# Pick #5
## Genome-First FH
### 非洲 vs 歐洲血統的差異

---

# Genome-First FH — 族群差異

**Winters AH, Gidding SS, et al.** *Circulation* 2026;153(24):1928–1939.
🔗 [DOI: 10.1161/CIRCULATIONAHA.126.080694](https://doi.org/10.1161/CIRCULATIONAHA.126.080694)

- Genome-first，n=**104,300** 非洲血統（All of Us / BioMe / MyCode）
- 致病變異盛行率：非洲 1:306 vs 歐洲 1:273（**相當**）
- 非洲血統致病變異者 LDL-C 多升高 **20.81 mg/dL**
- **意義未明變異 (Variant of Unknown Significance, VUS)**：非洲血統機率高 1.61 倍，且 VUS → **MI OR 1.91**（歐洲血統無此關聯）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABpklEQVR4nO2YsW3mMAyFP5oCUsrADZBRpA1upKwmj5INpNKAjHeFnB+HwyVFioRFBMENmw+P5CMtE/8/1/ZOAH4igDqA96KOq0lLyDJDsBVJi8rfrnoEtg0wq4DtnFYvqwxLX0zwcWS8MCq5Se2bCD6KeD/SqJfVbyP49yRAkDgcfB7ef5PFiMC2wWFmUKAwXhJcZrZHYEtkAQzOX53BpK1ACO8dlVFtx19rgrRkHDWAbqhDbjM3V5vgvQBhvJeZBeW23KxJieG9SM3V1sDyXiSpM4PopsYjoRIgaWYFYNsA75xWyZoc5JaGpRGkF8rMcmlSJsXfkhtAN6TmHXW8r3ZgQYZg67dcM7dlIGHqjdWhD7DJ/Q3BJkm6996OS95LjHpbu6XN3FJu57OACeceYdZvDHO1xHHuAKeZ7Yf3CGx3Tu+EdtTLuiFyOszMEsys87mtVSTM/0KRRJbtPHVYTZpbDDbMKqP6qwFw2H5cFmVmQbnnFPhdfxG89xEp5PYknfsBh1kE3TbWmgST47KawHbmFxO8c/5+D5n59t4Y89R+3rg+FfkDhqklEegZeg0AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Genome-First FH — 臨床啟示

> 💡 現行變異分類資源以歐洲族群為主 → 可能造成**非洲血統家族性高膽固醇血症 (FH) 的低診斷**。

- 對台灣／東亞：本土變異庫同樣不足，VUS 判讀須謹慎
- 不宜輕易視 VUS 為「良性」
- 推動本土基因資料庫是精準血脂醫療的關鍵

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 本週 TAVI 相關文獻
### Drake 主要臨床方向

---

# TAVI #1 — 慢性發炎性疾病患者的 TAVR

**Verma BR, Waksman R, et al.** *Am J Cardiol* 2026 Jun 18.
🔗 [DOI: 10.1016/j.amjcard.2026.06.010](https://doi.org/10.1016/j.amjcard.2026.06.010)

- 單中心，n=**2,880**；慢性發炎性全身疾病 (Chronic Inflammatory systemic Diseases, CIDs) 佔 6.4%
- 住院死亡（0.0% vs 1.7%）、1 年死亡（8.9% vs 8.91%）**無差異**
- **血管併發症較多**：10.3% vs 6.1%（p=0.036）；非計畫性血管介入 5.4% vs 1.9%（p=0.003）

> 💡 CIDs 病人 TAVR 安全，但**血管入路併發症↑** → 加強術前血管評估與入路規劃

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAAB5klEQVR4nO2YMYodQQxEn74aHPYcyKC5mfGRfIOeo+wBDJpwoT/loOd/J15+ZFbBKmwlRVFdJcnEh3W/fdyDr+arJkoAz5h9QCiDvviOWQ7tDUISfTRwDdtQ4pKyILc3wGwHIDjN9bOdO6e1TwT0snkaMGFWAfSi6W8Gcd/ifasB6B/VAEGD+xbWs/02idbFWRDtDQ4zg/DE33aIdu53M9sKokWrMibhGgD9eqvoYOfOudsGfbxvuIa/mZlx7iW5HS5NYnYBSmYf0qAX5fa+0eBbHnQ1Amgr48qhZUWtMibMLkme4UV1izRmH65BH5ce+vBEWXBOQBnSUIYklyAmIY3K3NKlZHZdw1iv+cuQNPuQJA2ewkiKcpvXJPMwrqEMT2ZlbjOWYj1jQlW/RRoTPC8NSANi9lGU2wzPmF2TWC+zay4HLohWwx/hu6Jh9gHMinsZ158C11hDwmNTK6kECfBLvUHX7JcDl0W7Em3Nt8+ZoSLaXIBjErOPp/0WTYfH7vA4g+AZyvCaaBNghReES4Wz7PZ0ADhWUjS4vLciWsx2zr2B2X7fgMO2o+helgHhGsq1864FLYo62BOtrinXMyjqCX9vNdZ/zWbq43tDHJ8F6FXzMDPOH8rrIuoJUFK39nXJ/2/NP56pocrMJwl6AAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TAVI #2 — 術前冠狀動脈 CTA vs ICA

**Kaya M, et al.** *J Med Imaging Radiat Oncol* 2026 Jun 16.
🔗 [DOI: 10.1111/1754-9485.70134](https://doi.org/10.1111/1754-9485.70134)

- n=**95**，TAVI 前同時做冠狀動脈 CT 血管攝影 (CTA) 與侵入性冠狀動脈攝影 (ICA)
- 70% 狹窄切點：CTA 與 ICA **高度一致**，敏感／特異度佳
- 阻塞性冠狀動脈疾病 (CAD) 盛行率 82.1%
- 1 年存活 93.7%，**與 CAD 存在與否無關**（p=0.466）

> 💡 術前 CTA 可作為冠狀動脈評估的**實用非侵入選項**，有機會減少不必要的 ICA

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABnElEQVR4nO2YMY7jMAxFn0IBKekb7FHkmw1yM/oocwO5DEDjbyEn20yaLRIVQwgwZDYPFPlJqYif7bi8cMCvB1AHsA6AR9IAaDkFW5NkvSWoI8kk9RnYLkApK3679gat7it7qW8m+Nnq+d3XrK14r0/P59keHg/Avkt+jOAHO/NNwiMhfZ58e9Zpey5gjjq94JKUbMfCfSFBkhQTnOmFfS3LVv7IdBu/KttR1gnY0KlszTq48IA2Tb41KXBJIUUCNFxTsCmSNpZ6S4+cKG7gMY4SD5OkMM0Rt95MGrEyhSlwzaIhcCxUv8F2XzjK1wcIXpg6JklSb9DGNqeohQsu2Oq+VjDdKtxLeS/BSxvDmxTpMkW60mMWDeltwKhz9i/XLHUqQUuQwnpTx0blfp7tApt1qsfYl4Vj2d5M8Mr0KFKT8mymzKJveymljFH82lGnQvoMM9LznkV62EPi5tA3huSaQlL6OYfYLL2+DRh8iJvG6DsB2z+PfX9dO9cOrrrPMveOe9a4/UkxU77B+R7S0vVsDROwld83rv/y/AXVUkS1QTzOOQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# TAVI #3 — 乳頭肌位置與 TAVR 後 MR

**Li X, Chen M, et al.** *Catheter Cardiovasc Interv* 2026 Jun 16.
🔗 [DOI: 10.1002/ccd.70703](https://doi.org/10.1002/ccd.70703)

- 1,159 例 TAVR 中，125 例術前二尖瓣逆流 (Mitral Regurgitation, MR) ≥3+
- 以多排電腦斷層 (MSCT) 分析乳頭肌 (Papillary Muscle, PM) 幾何
- **PM 下移 (inferior displacement)** 為 MR 不改善的獨立預測因子（OR **5.629**，p=0.014）

> 💡 術前評估乳頭肌幾何可預測 TAVR 後 MR 是否改善 → 協助規劃是否需後續二尖瓣介入

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABjElEQVR4nO2YMY7dMAxEn0wBW9I3yFHkm+Vq+kf5BwhAlx+QMSmk/5FiNwFS7LJYwoVtNoPhDMdWEe/XtX3QgO8OoAAwCZpJgwZAGymwNUkWDO+ShsskRQZsG1DKgavSrp23+8FZ6icj+GfnLHY/HvsXIvigc5bhHW71yxC8U0tv6tMOJNLb06fRXheQxaeruqIN7/h6ToFt0iVZNAWaA/Uk2DBJwfA+QOo2OcyAbVqAJgkw9fkmBbZow6VoFliAyzLNVLFWB8+ZjhS8bbiunXEWAO/Qrh2LHLtXWgKbpEUDcvCG1PE+JSd1C4Acets4fyp4u5eyAzx2TJ3zyDHTbtLwZYTpBUuy36INsEDPaMCVR2+DmVZLeBZJ9LbydEa8LS+0LFk/KzCtLzdFy5FZG2cppVTvnGVwu3Yqt/GpCP7SWSn/2BvnAQww9QTYmBO04I/d23J8Iz073iu3eTOg7Blm+uJtUrfWXQ7eKiCo3q9K8V5/UT2uH5HgrOb1n8UzrRi0HLlQvs+4/qvzGwKcWdr955SFAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## PASCAL × MitraClip × TriClip
### Drake 的 TEER 操作面向

---

# TEER #1 — PASCAL Precision vs MitraClip G4

**Enta Y, Hayashida K, et al.** *Catheter Cardiovasc Interv* 2026 Jun 17.
🔗 [DOI: 10.1002/ccd.70702](https://doi.org/10.1002/ccd.70702)

- 日本 OCEAN-Mitral 登記，原發性 MR (PMR)：PASCAL **n=150** vs MitraClip G4 **n=679**（傾向分數配對）
- 30 天 MR ≤2+（92.3% vs 92.1%）、MR ≤1+（71.6% vs 65.8%）、裝置成功（95.0% vs 92.1%）**均無顯著差異**
- PASCAL：1 例單葉裝置附著 (Single Leaflet Device Attachment, SLDA) 成功回收 → 最終 0 例

> 💡 兩款最新世代裝置早期療效相當；PASCAL 結構或與**較低 SLDA** 相關，提供 PMR 另一可靠選項

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABl0lEQVR4nO2YQYrcQAxFn1yGXpYhB5ijyDcb5mblG6mWA2p+FnZ3Q0gIZJHRYoQxNtp8pK//VWXi93Ff/pCA7wygAGgSXYlnPwvp+fXYFnBJcABNH7egSYoKdVsAs535ztzX+Q4wbf3PCP6WUZAczP3LEPwa6+srP6yP/S3WStgEK0cazF1AF7MCtgUOMwO/hbfwde53M9sqYENnhGcf2fWMAhqCwoEmZRd9vH5LYANcGoknTh/gigraiwJJXM0dLbwV6un5drpauCT6yF4FW9PlodJQuDTK8M0VnmcBu67qFeGbBl1NowX00TSy0pw2jcQBSfnQkwLYrswKdJkZXclxixq+EJ5dekjHqW+tCN/Cde2TfnpWdtXg2wLYm5LjvrFyPZ9bhZ4ugAKzfYWcxjTmvs69ALbnHkJC0wA/HbZAT5/nrNE0gMRb1NE3l9TCW6Dw0xRqeP0KGA58/pBB4zDcepTgWzh4i4t42Yc0avDtlbGN+3a0wGynjyJ1k3Sd5bvOWajhp485fWxKTQKvMaf2fcf1T5mfBjpGF15vo70AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TEER #2 — 次發性 MR 的 GDMT 與 TEER 利用率

**Bhasin V, Scherrer-Crosbie M, et al.** *Cardiology* 2026 Jun 19.
🔗 [DOI: 10.1159/000551963](https://doi.org/10.1159/000551963)

- 次發性 MR (secondary MR) + LVEF <50%，n=**508**；20% 死亡
- 3 個月僅 **53%** 達最佳化指引導向藥物治療 (Guideline-Directed Medical Therapy, GDMT)
- 高齡、慢性腎臟病 (CKD) 較少達標
- 僅 **9 例（1.8%）**接受 TEER

> 💡 次發性 MR 死亡率高，但 GDMT 落實不足、TEER 嚴重未被使用 → 建立心衰竭—瓣膜整合照護路徑

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABlElEQVR4nO2YwW3cQAxFH0UBPo472FI4nRkuKR3MlpIOZo4LjPBzGO1ugMQIkIPNg3kQIPDyQP4vkjLx9zi2DxLwnQHUAVxN0oRZViFjfj3bBiEJAnDp5Wd1ST1D3TbArDLMrO6jTmDY/skE/8iEdybX/esI/ogny3H5YaXVS98zsQl2EFdG1agUMTKwbXA1M2Afb95jh8PMXjOwoRU9gFn0iATfEBaVq3kPSvPzNQPbBkjt9sqEOd5ul3eIOWqSnnoP7t30Hp6qp6WtabXAKG2WLGwuuRqE1LyH1HLoDXVW3aRG0aqeeoZZj3qsVk6AcLWZxaeoxyQmMUuTxALLojeA0wVAUSq9eT9NKmmWBuFp9KYOxGkE3Z852NYHbZXLpQWZhY3wvkyBdyBy3AuPPQSWQzlbnIBtY5iZ7UWztMMqsIOrJZj19ztr1JfOLM07k5ifS/BRPPRGkfe73lJ44ZmZw2bR7dKkd0aG/e33GzAOq94xq5QMekM9JLnauYesQzVFT5/zFFgbCESOuWDf/7j+K/ML4u1BYdpzAYcAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TEER #3 — TTVR 降低交感神經活性（功能性 TR）

**Nelles D, Nickenig G, et al.** *Heart Vessels* 2026 Jun 19.
🔗 [DOI: 10.1007/s00380-026-02719-7](https://doi.org/10.1007/s00380-026-02719-7)

- 28 例功能性三尖瓣逆流 (Functional Tricuspid Regurgitation, FTR) ≥III 接受經導管三尖瓣修復 (TTVR)
- microneurography 量測肌肉交感神經活性 (Muscle Sympathetic Nerve Activity, MSNA)
- 12 個月：TR、NYHA 顯著改善；**MSNA 發生率 192.8 → 72.6**（p=0.01）、頻率 167.8 → 93.4（p=0.001）

> 💡 TTVR 改善**不僅來自血流動力學減壓，也有神經生理機轉**（樣本小，需驗證）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABjklEQVR4nO2YMW7cQAxF3ywFuJwFfAAfhbpBjhT4ZrNH0QEMUOUCFH6K0S4CJ2nSmIUHrOY3H5/i/9Q08fdzXP4BwDcCKABMog8FCgfAswQ3l2ThFkhDkkmKCtwWoOFwy8WP1wDYr/ZRoae/If39JW7LVzL4dB5c+rDtB3BcoxQ3wQLLx832VUAXewVujzkNfxZQY04XugB27osDyZhAAe/9w0MC06CrgG5Ioiv7MCnxWXW4SaKPxLMPCzdJKsJtKFzhdIFLgz4KcZN4tHJWjcw6PeSM+PnhhWcJD0Hh2UVX4tllGglWoqcXwLZVWwPY1+PqJrGvNXLB6TIJSKBLGnV0y329t2YBXQmt/TxaEd2wwAIFCeCmUWZO3TSyD3CTZmBV8bfwhEkvwQLwGnvImVkKTlvDFZTRDaZu54Vb1PE3lwTQZeEKEs+9wpw+/7OwrRk0aHC8RYHd8ok4cH97zy5pvGwVdJsp76bxzFOgxm55ATT5gG3rcUWBbUV0A2Y0TKPTNOECurXvN67/Qn4B/nw4msdhJIsAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

<!-- _class: small-text -->
# 其他值得一讀（1/2）

| 研究 | 期刊 | 重點 | DOI |
|------|------|------|-----|
| **HCM 心尖部動脈瘤與猝死** | *JACC Adv* | n=510；<10 mm 0.2%/年 vs ≥40 mm 8.2%/年 | [10.1016/j.jacadv.2026.102919](https://doi.org/10.1016/j.jacadv.2026.102919) |
| **PULSTA 經導管肺動脈瓣** | *Circ CV Interv* | n=58，植入成功 98.3%；5 年免再介入 98.2% | [10.1161/CIRCINTERVENTIONS.126.016616](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016616) |
| **急性 HF 停用 β-blocker** | *JACC Adv* | 短期停用或與死亡↑（HR 2.30），證據確定性**極低** | [10.1016/j.jacadv.2026.102929](https://doi.org/10.1016/j.jacadv.2026.102929) |

---

<!-- _class: small-text -->
# 其他值得一讀（2/2）

| 研究 | 期刊 | 重點 | DOI |
|------|------|------|-----|
| **MINOCA 新定義** | *Eur Heart J* | 從「梗塞」到「損傷」，重新框定為工作診斷 | [10.1093/eurheartj/ehag434](https://doi.org/10.1093/eurheartj/ehag434) |
| **育齡女性風險認知落差** | *JACC Adv* | 56.8% 低估 CVD、58.3% 低估中風風險 | [10.1016/j.jacadv.2026.102862](https://doi.org/10.1016/j.jacadv.2026.102862) |
| **經導管乳頭肌接合術** | *EuroIntervention* | 功能性 MR 的新介入概念（編輯評論） | [10.4244/EIJ-D-25-01353](https://doi.org/10.4244/EIJ-D-25-01353) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## JACC Case Rep / EuroIntervention
### 結構介入為主 × 5 例

---

# Case #1 — 高風險 TAVR 的 IVUS 導引 Chimney Stenting

**Nguyen PT, et al.** *JACC Case Rep* 2026 Jun 18.
🔗 [DOI: 10.1016/j.jaccas.2026.108903](https://doi.org/10.1016/j.jaccas.2026.108903)

兩例不利冠狀動脈解剖之 TAVR。瓣膜釋放後血管攝影看似正常，但**血管內超音波 (IVUS)** 揭示冠狀動脈危險貼近／開口受壓 → chimney stenting 維持通暢，無併發症。

> **為什麼值得讀**：主動式冠狀動脈保護的影像導引決策；**血管攝影可能低估**阻塞風險，IVUS 提供互補價值

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAAB6klEQVR4nO2YMa4bMQxEn1YLuKRv4KNob/aRm8lH8Q24pQEak4JrJ0X+T5rALD4LQ142g8FoNGQTn9Zj+bwH382/NZEDdCnPYcKS7xHl0C4wJAHYbGe6050uyQtyuwCtbexbv23SXOF+hr2tbwT0aa2v0+Oixoj9DNsbAf1b8yonbK42U8lvB/THkg9J3UdAMHr+leQ1b9m1tQacfJwcYN23R2vtXJLbLAcGJmkGI7/V4xb5ALrUNbHZffTnl5Jo6Z6Yh3yEzTBhs+TrgJx8vLqPYCRy+SjLLTalKSl1i005vaInHLcMCFOYumaY5ERVJXQf0oSULpDaqIl2xCFaktjuwAgrqNsFwBQZGvePdW9Ad05e8nVw0mPldM0UQyTnBdH+lsO7J88jn4mSaGfkySY2M9IEVf1W83jCGE8ljICyntA1+0urHJeuZKpZgMeZMK3QLj9OUuxtNa37VtITBhnCffCkOhhU9NvMMOTgECZpvsaHqmgHNoOMN0qLKJoTjtnh8Nj8TXnUQ7uwt9baajPgfpnduZ9ZAZv1btly7Gr2drp99NsWsEJwfSOgL+rlCZgkdR37hLJ+C8A14NFa7Fu7TPmo7bcAOebkmrEkt89dzZHDB4CpV54iIeeFX6nGZsnZoX1v8v9b8yeQPKM4GuaXAAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #2 — TAVI 後延遲性冠狀動脈阻塞致 MI

**Krajewska N, Kołtowski Ł, et al.** *Kardiol Pol* 2026 Jun 18.
🔗 [DOI: 10.33963/v.phj.113101](https://doi.org/10.33963/v.phj.113101)

TAVI 後**延遲性冠狀動脈阻塞 (Delayed Coronary Obstruction, DCO)** 導致心肌梗塞之影像報告。

> **為什麼值得讀**：DCO 罕見但致命，可發生於術後數小時至數日；高風險解剖（低開口、窄 sinus、valve-in-valve）應預先規劃冠狀動脈保護

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABkUlEQVR4nO2YMW7kMAxFn4bq5RvkKPQN9khBDraA5ig5QAC6HEDGTyF7UmwCBFtkWIRwYZnNA6n/TamIz2O/fJGA3wygADB1BQoUDoCPx7NdwCWxrRWndcAkRYa6XYBSVvB9oSxeW2cr9YcJvpGxuO7LQwk+zbQXxXXg42EE/0YFBBVK6/VtsbeVJrYMbKdOw+8PkEOnaMY0EGm040MKtnBJFoADFpg6LQPbBajbelfBvvitPP80wRehYOA00TRA4ZanpxL4AAunabRO63nYLNzUj23WRJMih07Dp0KBWTcLH0k85ADzY6k+wJL0NGa5JPW55WaXU7CpjyZTH+1oq9Tz1E3BaP0U6exvjrrFIdUBNA3c1PPodJwObNJ0kiz+Fk7rtG6a/wUS9fSYQ1zqAx8cdpeCLQBM4hSCRRJ/O89ZAIxttWDgtyXDHFKBgsMVsPhzqxSw1/Xv49k+MhbsTy+1Seo5zoD1/nYrDNziugJPkeQ+ROrHalv3BQX2uiao28c5C1zqcybJodPye8f1X5l36kk7vjbm0IIAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #3 — 漏斗胸致前負荷不足、竇性心搏過速

**Alkhatib R, Ziada KM, et al.** *JACC Case Rep* 2026 Jun 18.
🔗 [DOI: 10.1016/j.jaccas.2026.108778](https://doi.org/10.1016/j.jaccas.2026.108778)

65 歲女性長期心悸，高劑量 β-blocker 仍竇速。右心導管充填壓極低（RAP 1 mmHg），CMR 示嚴重漏斗胸（Haller index 8.1）。Ravitch 修補後心悸完全緩解。

> **為什麼值得讀**：胸壁變形可致**前負荷不足**與代償性竇速，是**可逆**病因；不明原因竇速且充填壓低者應評估胸壁結構

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAAB6klEQVR4nO2YMY5bMQxEn0wBLvlvsEehb7YnC0AfJTfgLxeQMSkkJ00W2SawimUlfDaDwXCG/E18Wo/L5z34bv6riQrApPkeLnzyHWM7tBcISXAfnu3ACitMUm3I7QVo7cb5fv15k7LDxwFn6y8E9Gn15+M+ejRinAfcXgjoi81rMTy751Ty6wH9pTog6MSPDueN8z0BF+eGaC9wb60B14prAXR4tNaODdGiWQUELilVMb/t52CoAjDJlHhaBawvW6LFamZEqGJ4DheeW6bD4hbCKgZhhSpUsSu3U64yaeoWTxVWW3K7RozhGi5TDpeKsakSgBhLErGiwbWzbq1ieE5iTQkxfEPdXphmBVbB+d7P9jiw4lpbpkP90cBkVcUUxn7corWHx/C0AtcgZkxsiTaHa8YuntPKBvv6rYrhCWgpIQZs6gkS6y574nQN2HWrwZSDkHJ4Tn/AtaluKyBM+j1uEzw7+u3S7YratSestWFPtFZhShXTE9basOuULYQuq+W0Ux77ob1wttZa9xzcH29pxcdBBzy3TN6QNPm0iqflsuWUdaARQAORfaDzaKAXAfpa824Vj9bGeWtvqYp+3vZD+/TbeUsqWVfkvhe6tA4cmxely/a9IgGsgLDfW43nlrdD+/6T/9+avwBGLaBbCFL6zQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #4 — 免疫檢查點抑制劑相關心包炎

**Roy R, Addetia K, et al.** *JACC Case Rep* 2026 Jun 18.
🔗 [DOI: 10.1016/j.jaccas.2026.108818](https://doi.org/10.1016/j.jaccas.2026.108818)

53 歲轉移性肺腺癌使用 pembrolizumab，反覆胸膜性胸痛。連續 CT 示進行性心包增厚，echo + CMR 確認心包發炎（無心肌炎）。NSAID + colchicine + 類固醇、停用 ICI 後緩解。

> **為什麼值得讀**：**免疫檢查點抑制劑 (ICI) 相關心包炎**需高度警覺；多模態影像對診斷至關重要（心臟腫瘤學必讀）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAAB4klEQVR4nO2YMW7kQAwEa3YEOJz9gZ9C/cxfo5/iH1ChAS76Amp9l6zvksMyMANhJCYNqqfZ5BAP43Z5nIOf5N+SKACmvM65xKp6W3ZEa5KmxHKgzlNSNER7AcbYOfb5sUu+wecVjrE9EdDD2O6Hd141sDyusD8R0D8mE3L5tryY/HxAD5KSg3EMjp3jDWApnwjou+T7GAN4CXsJgA1uY4xrQ7SoIphhLEleKiGpnyagMGBKU87yGQbnl45o5TOqR5jCcnmu0t6Genu/YgUVm4HCFNa0tgFL93YmyVleNO6H9gIkjLHfriRskBjV0dqhPf97LlcUHwBYasrbsKTI4FOeS1MOlqsnb60cl6RZahbMxresOJCnyzUFWTXviNZYrrBcmlEOwapNtERL1rCwxPKSsqQtE6wAJ3ZngiW01QSWSg2+9CGhrauRVGTI5VMqwF15e3cFWL3OIDHa6m3UmKOsHnGfgnuiVdiUKyhNSACy5y07Z4dTY+t59ot2aC8cY4yxLQdurz6DzysbsLyfB7uASeLY9fE2P/a7aXx/IqBvon76DPL05Oc+oaXe/k7Oj/02Rh77eHWFbcfeubYsrzGn1owta/u1Y/Rcp7+tRtZVbwFmwJ+uZnnL2WH8bPL/W/IXYumqEDuJAmgAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #5 — 序貫生物製劑後猛爆性嗜酸性球心肌炎

**Lee J, Kim D, et al.** *JACC Case Rep* 2026 Jun 18.
🔗 [DOI: 10.1016/j.jaccas.2026.108889](https://doi.org/10.1016/j.jaccas.2026.108889)

35 歲潰瘍性結腸炎，序貫生物製劑（vedolizumab）+ 類固醇減量後心因性休克，LVEF 10%、嗜酸性球 2,154/μL。切片確診嗜酸性球心肌炎，VA-ECMO + 類固醇支持；復發改用 mepolizumab 後恢復。

> **為什麼值得讀**：生物製劑 + 類固醇減量者若嗜酸性球↑ + 急性 HF，警覺**嗜酸性球心肌炎**；早期切片指引升級至標靶治療

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAAB1klEQVR4nO2YMW5jMQxEn8wPuJRvkKPQN8vVlKPkBvzlAjRmC/p7t1hj0wRmEVaC2AyI0cxQQzyt2+l5D36a/2uiADCtOucUs+bt2RGtSzKJuYA6m6RoiPYEjHFlH/q8SmuDXxfYx/ZCQE9re5xubxp47he4vhDQF5vnIOfa5iomvx7Qv+rO2/CExO2gcVfefowxgHP4OQC2/XobY1xazrYqMIkpadW0JfWbLQoHTDIt5rJwuN90RKtlWgoHV3jOlbO0tyFvUXiZl8ITt0DhCu86WzHXYWeSFnMpsJ6asI/c38eF24WEDRKnHK0dWhTknb0Cv1vDVF/eAlM5l2nllAXgOVvyttT1cDTAAmv7ygK7y1el3LJgWjrvoQnhOZcFTCVeNtETbeJF1IeUJX2ZcF9w8GKCwhOaaoIWlQqgciNTWTNviDY8p0q4cq6CzVRT3oaDW3geacGCxOmqtxYk1ISl9VgfeqJVuGkllCYkANn0ldXu4MXVUtqiR0e0AaUJczFlWrVLtuTtCVwS+/X8+W6f1yM0frwQ0PPagIEDt7eAtSXaLwP0IkBfUzBqeVRQsaG33mJBrTn1zdjWyyTV2mtHMu+cb/mTwNffe3o/tOPnJ//bmr8BCEKy0fI0WngAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: lead -->
# 💎 Take Home Message

### 1. **口服小分子 GLP-1 RA 來勢洶洶** — VISTA 36 週 −11.8%，已進 Phase 3（含 CV/腎臟結局）
### 2. **心血管死亡率種族落差未消弭** — 證據不足，需政策改革
### 3. **AI-ECG 揪 HCM** — 特異度 100%、提前 2.6 年；rule-in 工具
### 4. **CKM 危險因子治療嚴重不足** — 高血壓/高血脂僅約半數受治療
### 5. **FH 變異判讀有族群偏誤** — 非洲血統 VUS 即帶 MI 風險
### 6. **結構介入**：PASCAL≈MitraClip G4；次發性 MR 的 GDMT/TEER 雙雙不足；TTVR 降交感
### 7. **TAVI 細節**：CIDs 血管併發症↑；術前 CTA 可靠；乳頭肌下移預測 MR 不改善；DCO 須警覺

---

<!-- _class: small-text -->
# 完整參考文獻 (1/2)

**Top 5 Picks**
1. Davies MJ, et al. Elecoglipron (VISTA). [*Lancet* 2026;407:2503–2514.](https://doi.org/10.1016/S0140-6736(26)00748-8)
2. Aroda VR, et al. Elecoglipron (SOLSTICE). [*Lancet* 2026;407:2515–2527.](https://doi.org/10.1016/S0140-6736(26)00802-0)
3. Arun AS, et al. Excess CV Mortality Among Black Americans. [*JACC* 2026.](https://doi.org/10.1016/j.jacc.2026.05.013)
4. Park J, et al. AI for HCM Detection From ECG. [*JACC Adv* 2026;5(7):102914.](https://doi.org/10.1016/j.jacadv.2026.102914)
5. Gong J, et al. Cardiometabolic Risk Factor Treatment in CKM Syndrome. [*JACC* 2026.](https://doi.org/10.1016/j.jacc.2026.04.031)
6. Winters AH, et al. Genome-First FH (African vs European). [*Circulation* 2026;153:1928–1939.](https://doi.org/10.1161/CIRCULATIONAHA.126.080694)

**TAVI Section**
7. Verma BR, et al. TAVR in Chronic Inflammatory Diseases. [*Am J Cardiol* 2026.](https://doi.org/10.1016/j.amjcard.2026.06.010)
8. Kaya M, et al. Pre-TAVI CTA vs ICA. [*J Med Imaging Radiat Oncol* 2026.](https://doi.org/10.1111/1754-9485.70134)
9. Li X, et al. Papillary Muscles and MR After TAVR. [*Catheter Cardiovasc Interv* 2026.](https://doi.org/10.1002/ccd.70703)

---

<!-- _class: small-text -->
# 完整參考文獻 (2/2)

**TEER Section**
10. Enta Y, et al. PASCAL vs MitraClip G4 (OCEAN-Mitral). [*Catheter Cardiovasc Interv* 2026.](https://doi.org/10.1002/ccd.70702)
11. Bhasin V, et al. GDMT and TEER in Secondary MR. [*Cardiology* 2026.](https://doi.org/10.1159/000551963)
12. Nelles D, et al. Autonomic Modulation After TTVR. [*Heart Vessels* 2026.](https://doi.org/10.1007/s00380-026-02719-7)

**Honorable Mentions**
13. Rowin EJ, et al. HCM With Apical Aneurysms. [*JACC Adv* 2026;5(7):102919.](https://doi.org/10.1016/j.jacadv.2026.102919)
14. Lee SY, et al. PULSTA Pulmonary Valve. [*Circ Cardiovasc Interv* 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016616)
15. Alaeiilkhchi N, et al. Beta-Blocker Discontinuation in Acute HF. [*JACC Adv* 2026;5(7):102929.](https://doi.org/10.1016/j.jacadv.2026.102929)
16. Bucciarelli-Ducci C, et al. New definition of MINOCA. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag434)
17. Stanislas KA, et al. Risk Discordance in Women. [*JACC Adv* 2026;5(7):102862.](https://doi.org/10.1016/j.jacadv.2026.102862)
18. Tekieli L, et al. Transcatheter approximation of papillary muscles. [*EuroIntervention* 2026;22(12):e712–e715.](https://doi.org/10.4244/EIJ-D-25-01353)

**Case Reports**
19–23. Nguyen PT (108903) · Krajewska N (v.phj.113101) · Alkhatib R (108778) · Roy R (108818) · Lee J (108889). [*JACC Case Rep / Kardiol Pol* 2026.](https://doi.org/10.1016/j.jaccas.2026.108903)

---

<!-- _class: abbr -->
# 縮寫對照表 (1/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| GLP-1 RA | Glucagon-Like Peptide-1 Receptor Agonist | 升糖素類似胜肽-1 受體促效劑 |
| T2D | Type 2 Diabetes | 第二型糖尿病 |
| HbA1c | Glycated Hemoglobin | 糖化血色素 |
| HCM | Hypertrophic Cardiomyopathy | 肥厚型心肌病 |
| ECG | Electrocardiogram | 心電圖 |
| CMR | Cardiac Magnetic Resonance Imaging | 心臟磁振造影 |
| CKM | Cardiovascular-Kidney-Metabolic syndrome | 心—腎—代謝症候群 |
| CKD | Chronic Kidney Disease | 慢性腎臟病 |
| FH | Familial Hypercholesterolemia | 家族性高膽固醇血症 |
| LDL-C | Low-Density Lipoprotein Cholesterol | 低密度脂蛋白膽固醇 |
| VUS | Variant of Unknown Significance | 意義未明變異 |
| MI | Myocardial Infarction | 心肌梗塞 |
| TAVR / TAVI | Transcatheter Aortic Valve Replacement / Implantation | 經導管主動脈瓣置換術 |
| CIDs | Chronic Inflammatory systemic Diseases | 慢性發炎性全身疾病 |
| CTA | CT Angiography | 電腦斷層血管攝影 |
| ICA | Invasive Coronary Angiography | 侵入性冠狀動脈攝影 |
| CAD | Coronary Artery Disease | 冠狀動脈疾病 |

---

<!-- _class: abbr -->
# 縮寫對照表 (2/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| MSCT | Multi-Slice Computed Tomography | 多排電腦斷層 |
| MR | Mitral Regurgitation | 二尖瓣逆流 |
| PMR | Primary Mitral Regurgitation | 原發性二尖瓣逆流 |
| PM | Papillary Muscle | 乳頭肌 |
| M-TEER / TEER | (Mitral) Transcatheter Edge-to-Edge Repair | （二尖瓣）經導管緣對緣修復 |
| SLDA | Single Leaflet Device Attachment | 單葉裝置附著 |
| GDMT | Guideline-Directed Medical Therapy | 指引導向藥物治療 |
| LVEF | Left Ventricular Ejection Fraction | 左心室射出分數 |
| FTR | Functional Tricuspid Regurgitation | 功能性三尖瓣逆流 |
| TTVR | Transcatheter Tricuspid Valve Repair/Replacement | 經導管三尖瓣修復／置換 |
| TR | Tricuspid Regurgitation | 三尖瓣逆流 |
| MSNA | Muscle Sympathetic Nerve Activity | 肌肉交感神經活性 |
| SCD | Sudden Cardiac Death | 心因性猝死 |
| IVUS | Intravascular Ultrasound | 血管內超音波 |
| DCO | Delayed Coronary Obstruction | 延遲性冠狀動脈阻塞 |
| ICI | Immune Checkpoint Inhibitor | 免疫檢查點抑制劑 |
| VA-ECMO | Veno-Arterial Extracorporeal Membrane Oxygenation | 靜脈—動脈體外膜氧合 |
| MINOCA | MI with Non-Obstructive Coronary Arteries | 非阻塞性冠狀動脈心肌梗塞 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**
心臟內科｜結構性心臟病介入

*本文件為讀書會共筆之教學整理，*
*僅供醫療專業同仁臨床教學交流參考。*
