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
  section.lead blockquote p, section.lead blockquote strong { color: #2d3436; }
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
  section.ref { font-size: 0.62em; }
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
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-10-17 ~ 2026-10-24'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-10-17 ~ 2026-10-24

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Pick／文章附 QR Code，可掃描跳轉原文

---

<!-- _class: small-text -->
# 🎯 本週主題與固定欄目

## 預期落空，場域精準

**一句話**：期待的新藥（factor XIa）**落空**；真正落地的是「把對的工具放對場域、把舊規則依療效個別化」。（本週 **EuroIntervention 無新上線文章**）

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 結構性主動脈瓣
3. 🔧 **TEER Section** — MitraClip／PASCAL／複雜解剖
4. 📚 **Honorable Mentions** — EHJ／JACC／Circulation
5. 🔬 **Case Reports** — 結構性／介入併發症
6. 📑 縮寫對照 ＋ 完整參考文獻

---

<!-- _class: divider -->
# ⭐ Top 5 Picks

---

# ⭐ Top 5 Picks 一覽

| # | 試驗 / 主題 | 期刊 | 方向 | 關鍵數字 |
|---|------------|------|------|---------|
| 1 | **LIBREXIA-ACS**（milvexian + 抗血小板） | NEJM | ❌ | HR 1.05（0.91–1.21），p=0.50，因無效中止 |
| 2 | **ACHIEVE-4**（orforglipron CV 安全性） | Lancet | ✅ | MACE-4 HR 0.84（0.59–1.20），p<0.0001 NI |
| 3 | **ICare-FASTER**（急診 POC hs-cTnI） | Circulation | ✅ | 停留 −47 分鐘；30 天 MI/死 0.39% vs 0.39% |
| 4 | **POET II**（心內膜炎縮短抗生素） | NEJM | 💡 | 安全 NI；但復發 5.1% vs 1.6%，p=0.04 |
| 5 | **TRIUMPH-1/2-OSA**（retatrutide 治 OSA） | NEJM | ✅ | AHI 最多 −34/hr；減重 12–22% |

---

# ⭐ Pick 1 — LIBREXIA-ACS（❌ Negative）

## [LIBREXIA-ACS Investigators. *N Engl J Med*. 2026;395(16).](https://doi.org/10.1056/NEJMoa2608717)

| 項目 | 內容 |
|------|------|
| 設計 | Phase 3、雙盲、安慰劑對照，14,194 人 |
| 介入 | 口服 milvexian 25 mg BID（factor XIa 抑制劑）加在抗血小板上，ACS 後 7 天內 |
| Primary | CV 死亡／MI／缺血性中風：5.4% vs 5.1%，**HR 1.05（0.91–1.21），p=0.50** |
| 安全 | BARC 3c/5 出血 0.3% vs 0.3%（HR 1.04）——未增加大出血 |
| 結論 | 因無效（futility）提前中止；「抗栓不出血」假說在 ACS 未成立 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABRklEQVR42u1YsW0EMQwTcgN4JK+ukW4AAwpJ6S/Vp0gRsHjjYVjvhqBEib6oN+vE5+bXmzuwrqqIjf2sYhz7fMW79V83wLaBUdgmxBm7CTYyRvZ2rLpuni8vbBvZPBGW2MhbVYo6I2yst5sJBW9dezb1Jp0ylfMz0mmvlzx/uotLvbG/HXCFkntCD96gUPGW0kKGEJrU2wgTwcpJrk1OAY8IK0EgB8TiwSSnQHVNZ9uSQzrVG1PJqiNpg9ADW0Kez9hSaKNT9F7plO6oR6qUazOzUg1ELU7U2fDGQU+iVisiJ78e2OR1sRNYJ9SHN5aZrHg33g5tsCGP0exVG2AvHxIaVfnAM/Jv0ObYcnlyn3la48PHwukfq7eMLFzTuC8vbKGJwDbSVWfFm+QZAsYp5vauf7Rg09/mnaWWy6lqVG+f71V/ufkGdXDenJzPTvkAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# ⭐ Pick 2 — ACHIEVE-4（✅ 安全性非劣）

## [Klein KR, et al. *Lancet*. 2026;408(10564):1557-1570.](https://doi.org/10.1016/S0140-6736(26)01865-9)

| 項目 | 內容 |
|------|------|
| 設計 | Phase 3、事件驅動、開放標籤、主動對照 NI，2,749 人 |
| 族群 | 第二型糖尿病＋高 CV 風險（85.9% 已有 CV 病） |
| 介入 | 口服 orforglipron vs 皮下 insulin glargine |
| Primary | MACE-4 4.2% vs 5.0%，**HR 0.84（0.59–1.20），p<0.0001 NI** |
| 安全 | 顯著低血糖 6.8% vs 19.2%（較少）；腸胃道副作用 62% |

> ⚠️ 這是 CV **安全性非劣**，不是 cardioprotection（HR 0.84 的 CI 跨 1）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABkElEQVR42u1YQY4DIQyLlgfwpPk6T5oHIGVtJ7Sn9lKt1oeiOQBzsYKxTSJfjx3fn5/9vANjZMbE6sIS29yKa//Em/EfP4H2Ajyg3XMRba5xX1hi3xMtysjaopgEzDqPO4YzWlRYEzBhc+mNNpfmUTid0aaOviZ1y4x5K01gPZ+frybUAOaZReA9j7w5ol1DRw/qAielLK6YyxQtiimZDUENqS6RmzIBOJfgBfQW8yMRprdMXOXRhxgLnNh3rS1PX267pA+cFHs9mcALxUgTddFEjPStbVC+6Llz7ZPEhq07ECpV60EJBgZTBeOFOsGGyOllU9zw1FtKAaoaDXK2U7i6Q1QCp+SKw0UJW+fVoEFEPx9c9bYTV5U0Kz3WxLO2MjKprh47pbe2+bYiDTW2wsyRCFfnLSPLh5q1uxm/HUSGJbTh6w79diBjR6VcvX+t32XZCaG19zbv1YgGJ9+mnsDevZp23uatd/ej46LQ7vCurbhagjCOBVv3aqpZV+0743x7NGE9m422vP223P/q5y9HTovvJfYl7QAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# ⭐ Pick 3 — ICare-FASTER（✅ Positive）

## [Than M, et al. *Circulation*. 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.080866)

| 項目 | 內容 |
|------|------|
| 設計 | 實務型 stepped-wedge cluster-RCT，6 院、59,980 次就診 |
| 介入 | 急診床邊即時（POC）hs-cTnI vs 中央實驗室 hs-cTn |
| Primary（效能） | 急診停留時間 **−13%（−47 分鐘）**，p<0.001 |
| Safety | 30 天 MI 或心因死亡 **0.39% vs 0.39%**（p=0.54） |
| 結論 | POC hs-cTnI 納入加速診斷路徑：安全且更快 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABi0lEQVR42u1YQWoEMQwzzQPypHzdT5oHGFxbcspe2ksL1WFDGHaSi9BqZNmW36+w9+XvLh+rtZ4TO9eD1519ZCc+7If1H5cF7xTqhV1QC3POb1G0RWPBi+2A6sVzkbyU0eJpm1D10bZci+HGbNJoW6iN1qHbeh5h3Y4nvG5dT+B6AK9f3fa1N00lgMwcs/X1zLkkt17PYnXBuxpkSbcPRZVQUPvfJ07Sm+29qtwWpTY2y+rQxUIU7YKDQQydEALSFebWyC3E0AWiDkU9AWipW6YacFtVWNTBArpFCfNbL46q3wIn6m/QDRhyhL8yMGwIMxbXKET9FkKF8VIMh1lXNjEyhi0wbBPLVT2hO7JDueYYr6duvp1gMG6mrITuGZ19bqB9aKhwYFm0McZ7NbBVc8IMECbYxK0O2r3DdL7crBfCfVnD7kYSyHUz2MxqygTaEF46iFSeJzAbfLEdpjxZQv1CjeBHtzKV52A3ifm6tVh5xtjRcfLtEZ4nzKyGtYxtL0KOsN++5/F/f/kJ1jmPoBUvumQAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# ⭐ Pick 4 — POET II（💡 概念轉移，留意復發）

## [Bundgaard H, et al. *N Engl J Med*. 2026;395(16):1600-1609.](https://doi.org/10.1056/NEJMoa2607887)

| 項目 | 內容 |
|------|------|
| 設計 | 國際、開放標籤 RCT，508 人（左心 IE，穩定後隨機） |
| 介入 | 依臨床反應**停藥** vs 標準 4–6 週療程 |
| 效能 | 存活且無抗生素天數 183 vs 169 天，差 13 天，p<0.001 優越 |
| 安全 | 死亡/心臟手術/栓塞 8.2% vs 10.7%，p<0.001 NI |
| ⚠️ 復發 | **5.1% vs 1.6%，p=0.04**（縮短組較高） |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABRUlEQVR42u1YQQrDMAwzywPypHw9T+oDAp4lpSs7dLDL0GGhlIRchCzLdiJv1or/zcebI2q12vZZ+zwGzjHWI+7Wr24ApjC2YywgLHijcNbfBFux1A5QFx0gsTfDVsCizwYOzbDlXFHBnaTOCBv0lmCssHHvozfmKWS2P6M81SKqN3cx8pCA3mqPhIXqTLABGDJ07mjGsMEmeEPYtveaxJRiQ0Z02AgDOn2wtQ0MkV1wYK+aJdddKg2orSYeAsaYDsC2jy4xPQVGDyG8tKlZ5WxxhZLUNRvvVdtWiRD4suRn01uGmjfoLXZP4pOn0hiDK38zqqcIIoYFmgnakuHWh1BpIXg2vGnOmsEkXefs4NT35qtaSYFW8wIO4O1MECNskpySdJrNWXmVMBHoNGfxzWHo5aF5zVksrCz6otHI3/4vWd/dPAEYmuN/bD0ROwAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# ⭐ Pick 5 — TRIUMPH-1/2-OSA（✅ Positive）

## [Grunstein RR, et al. *N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2611477)

| 項目 | 內容 |
|------|------|
| 設計 | 兩個 phase 3、雙盲、安慰劑對照（共 691 人） |
| 族群 | 中重度 OSA、BMI ≥27（±第二型糖尿病） |
| 介入 | 每週 retatrutide（GIP/GLP-1/glucagon 三重）4/9/12 mg |
| 結果 | AHI（9 mg）−34.3 / −24.7 vs 安慰劑 −9.9 / −10.3；減重 12–22% |
| 意義 | 代謝—睡眠—CV 風險鏈：「減重即治本」再添選項 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABNUlEQVR42u1YsQ3DMAwj6gNykl73STnAgCqKadolHToUHGIYhhwvBEXRcpAXY+E++Xqyo8bIuRCjPmzJPWI9cDX+dVLYojAOzqltxbWaYCuWxt6ojonhhY1zAZbYiCcrrVtaYaPeSFqsbUp7NnrrOn2LLYzqVEN5RLzdxUVvGK+0nlsX3naU5dbatVAuFy56yynfyE/vdclpK410kb0CVtRVYKI3AiswCGWTTDrVQvZdnySNReGjNxmaqGuQNnXKKkjeCLvgQZ2SiYcUJFlHX1vppDeuRNUdpkAa9SEHHlSghDrVKVMpybW/pY+/dakGDn+DArc+RCAFz6h/Ux/SFse+N9Ot71XHqy9W74X2N9EYww+b/E2qM8OGdV6vm5PecuZHLdj4m95ZJE1vQCO93f+rfjl5AmYo0nLy02wrAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 風險分層：影像 × 生物標記 × 真實世界

---

# 🫀 TAVI 1 — AI 3D CT 體組成預測死亡

## [Hadzic I, et al. *Circ Cardiovasc Imaging*. 2026:e020106.](https://doi.org/10.1161/CIRCIMAGING.126.020106)

- 多中心回溯 **915 人**，中位追蹤 22 個月，死亡 17.5%
- 深度學習全自動分割胸腹骨盆 CT → 脂肪／肌肉體積與衰減值
- **低皮下脂肪體積、高脂肪衰減 → 死亡↑**；高骨骼肌體積／衰減 → 存活↑
- 加入體組成鑑別力 Harrell C **0.66 → 0.71**（p<0.001）
- 臨床：術前 CT「順手」做 AI 衰弱／體組成，補強手術風險分數

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABj0lEQVR42u1YwW3EMAwTqgE8klbXSBnAgCuRSq6f9lMU5eOMILnEH0JHUaTtfL+2vTd/t3lZLa/7woeV9aM/WewP+2H9x2ahjQLpDdzqXrD5Wt810VYZgTaqqn66toXZpdFmweN966O9UN4F3varLtoDum70Wr8CuSpvqQnx9dLVhHvZSqhB7nXLmyLa7EdBvbusq2ohyoReuSELjXB1bQu8q9aWBMA4S3ZZC8XSRHv6r8e09eFtovVClreULEzeIq1tdJymgjl5i3oapgP8TqgywegN2FzNYbgFTbQ+5jFAiWzMXXBNJgQly8YhlCBwCqvq7cviQm/BXlm9RVgIXjN8TVVvL8P8QjG7sONzZPV2fPjLJBj5oNplU1t2HJdudmhNaFngCGOQ3KK8DfoEzAVK2dFVsDYGT9pNRnXqg252wFBwsMIZzbRzGQnsMJATgXUzb0w2x2g4OGgSPk8wVJUJfRiijJaHdTi1S2HePmgTx4yTIo82b5l5ZxDr+lujCX/EAT7hyGaH95H732x+AvguiFnG6V6hAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# 🫀 TAVI 2 — NT-proBNP：TAVR 用出院值

## [Zheng HJ, et al. *Open Heart*. 2026;13(2):e004319.](https://doi.org/10.1136/openhrt-2026-004319)

- 傾向配對 556 人（TAVR 278／SAVR 278），LVEF ≥50%
- 出院 NT-proBNP >1000 pg/mL：TAVR 2 年無事件 77.3% vs 91.4%（**adj HR 3.21**，p<0.001）
- **SAVR 不預測**（HR 1.18，p=0.50；交互作用 p=0.008）——體外循環發炎抹平預後價值
- 6 個月 NT-proBNP ≤1000 pg/mL 則不分術式都預後佳
- 臨床：**TAVR 看出院值、SAVR 改看 6 個月值**

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABgklEQVR42u1YwW3EMAwT6gE8UlbXSB7AgCqSTu51/bRA+TjBCIz4Q8g0RSnqfez4HP7ucEXH6O2ssa7qVYVfce2v+CH+4zAEb1QCXsNeF1b/WqZoG6fQKqsAvwDbFy1SGjGRZFLCG21lcemPM1pdPTb9BeYy5i01QY/rXr6aoKB2bVCiVe068uaINgcVTCD7ofUmZpqiFV31rOZBK/C2aAP5bKiJRbSumhBjiQ+pKrZZ1GxzO44xUDCxxq+s6So+7AmccbPXU8FYeUM1dwvndOUtIlV/wWHkNlmITZmgq3+MLvWBefZ8ZdRbiYPIMJhtTybsyfTe/hZPzJi3yid1IFh/E/oQrh4MVw/ACnu9paeVV1TxnWnrb9E8wsZwLw/G3seTty9Pu+JuHHx5O6i0JIASizDV27t3OFx9ZiDOfRnt9yCHVS/8ZzVHykLdhPU8QQqGMkGX641W1C2h1UDMeLL08gzS3u3MW/UOtDQaNrp26EcTHgMmJtQyntV85vF/f/gNjjaQeJ5Mv0UAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# 🫀 TAVI 3 — KOSUTAVI 真實世界 5 年死亡

## [Zehir R, et al. *Anatol J Cardiol*. 2026.](https://doi.org/10.14744/AnatolJCardiol.2026.6567)

- 單中心 **859 名**高風險重度 AS（2020–2025）
- 死亡率：30 天 6.5%、1 年 12.4%、5 年 26.3%
- 30 天死亡獨立因子：慢性腎衰竭（HR 7.75）、心因性休克（HR 5.83）、重大血管傷害（HR 22.7）、心包填塞（HR 17.9）
- **瓣膜型號、入路、性別皆無關**
- 臨床：早期死亡由腎功能＋操作併發症主導 → 術前優化腎功能、積極血管保護

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABi0lEQVR42u1YwW3EMAwTmgE8klf3SBkggEqKcu7ucf20QPk4wzCc+EMQNEU58v244nP4u8MzMI5cMRb218jA5JjXV/ww/uMQaCdQA20D5p4T/z3RgsYD2CIwj6IX62GNlvCwIaX705nbzEVWoQdvtNTqSYT9ib2vbssTiPYxfT1B4yxJjJQe2t5MdQu/hfU+SO4/lkqga2E3SqtjVYFYtrcMNBIe6ZVuy82GKbei9HjW7elbeQG1ssEsv02sV90+S08gq9l+O8UqtWHKLQMYoCrP7JAQproVt7lU0aJ9zNXBsgIts+JSSMgyNNPKW5Hg1gP9NmYbmqUSyhN63gy7+u3UFRPDKr5anT2hO4ix/dYVbXZ309VBkcY3JxS9ul/lY1XIXHVbllUdWXU66ihtbxkdgNV2ybhUfF1zQvcOumVKtoqRvn0ZKq+a38ozxvl297xUQuXbUGlL99ePkVu3vHfWL0t0MBZiPd+FNdoQ1PuZ0VYJ/a6oBq2b37D2hJdsU4YwjP328x7/94fft4KDLjnrJNsAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 影像導引 × 複雜解剖

---

# 🔧 TEER 1 — 單純 TEE 導引 MV-TEER

## [Xing WZ, et al. *Zhonghua Xin Xue Guan Bing Za Zhi*. 2026;54(10):1206-1211.](https://doi.org/10.3760/cma.j.cn112148-20260901-00550)

- 回溯 **46 例**二尖瓣逆流，**僅用 TEE 導引**（減 X 光／對比劑）完成 MV-TEER，全部成功
- 中位追蹤 15.8 個月：1 年心衰再住院 20%、死亡 1 例、無再介入
- LVESD 47.2→39.7 mm、LVEF 44.98%→51.84%、6MWT 298→375 m（皆 p<0.05）
- 臨床：單純 TEE 導引在選定病人**安全可行**，降輻射／對比劑負擔的概念驗證

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABi0lEQVR42u1YUWpDMQwzywFypFzdR8oBAp4tOet+2p8xpkFNW94jP8JVJNkWz+vY+/Bnh9uyRoTZGjtfV9Rz1jof9qL+4rDhjb0OMA++5neLor1dte7qTMw2tNGe/OsTZ/g/QBueTEi0Np3gZdGCqB7hzYe9hHkLTUiE3z66msDaD3HgQ8mbsILhfjl6a7xrkr11uERpQiHEb9FDE21q10RXEzO0KyAII1TRttKW+VZLZ6mZKhMCnlsIBwjQpDVVBUMzobfV26+Qo8rbtrAWB+DX1YQSMSgD2Ju87VQm29u6aCkLDnewAx3WdIcDHXgQACFH1nkNvGUGg3Y5aazJBDpCa5etNt8t2tsbDLw0Fk7RlqHqvIktdqdHklnVeRdCgldauK3GvVNNjD0vOGMt1Cx0M5jVsMDQyOfyta0+OyDc0iDWUJ7Lwlu+rojZDOWZ1xAP2GHh2YH7hC7mhM692tuPsakGjrsmvavhys56jljSO0aYAgP5jWGhvKthUIRZVNY9qlPke+X+O4efOw+BtKX+M5AAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# 🔧 TEER 2 — 複雜移位的 SAVV-TEER

## [Papadopoulos GE, et al. *Catheter Cardiovasc Interv*. 2026.](https://doi.org/10.1002/ccd.70953)

- 4 例高／極高風險成人先天心臟病（ccTGA＋右位心、d-TGA Mustard 術後、髂股扭曲、IVC 中斷＋奇靜脈延續）
- **3 例 PASCAL ACE、1 例 MitraClip**；全部成功，系統性房室瓣逆流 3+ → 1+，平均壓差 1.5–2.1 mmHg
- 2 例股靜脈、2 例右頸內靜脈入路
- 核心：入路選擇看輸送系統**力學軌跡與同軸性**；下腔不利時右頸內靜脈可為首選

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABSklEQVR42u1YSQ4DIQyzygN4El/nSTwAKbUTZnpqpV4qH4pGo6FcrHgJKeLN2viffDxZ4GoLG2OD26E9vx94t351IjDE2PjWI1SN++WCTXgSFUuHTpwsoxO2mETFurXww0YwPfhRNfTBJr2l5MhpfdvorXw67sfIp3ec9JkxMs7Wg9ONio4ZSrmjQBNOVas1XqgySUywSXIEA9CqNALybaI3yYxi6+I0yKzIdfGCvNmZvemFHhnCLtiQelOSnKbglCFqVTP1puqdNmHi0xRb9QVyWix71G0mrbJqBYhM4ZK9l1vFJsoIPvnWLjtU22o+GVJGyHKdRk/t+XCaRsjr5Ty/9jC6h6zyApJcWHmhrZdPmxG2M2fta4qJCjqnOWujDKtlhk3tvtwabvPpuZOjIs5rrk82U3W6xTWzOesyqZ6IsJqz/v9kfXPyBFSzyWn15gbKAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## EHJ ｜ JACC ｜ Circulation

---

# 📚 Honorable Mentions (1/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| **EHJ — 急診急性心衰共識** | EMS／急診的表型分類與早期處置實務 | [DOI](https://doi.org/10.1093/eurheartj/ehag744) |
| **JACC Clin EP — ASCEND CSP** | 專用 CSP ICD lead 做 LOT-CRT 的 6 個月成果 | [DOI](https://doi.org/10.1016/j.jacep.2026.10.003) |
| **JACC Asia — CSP vs BiVP** | 傳導系統節律 vs 雙心室節律 RCT 統合分析 | [DOI](https://doi.org/10.1016/j.jacasi.2026.09.002) |
| **Circulation — KCNQ1 變異圖譜** | 13,403 變異功能圖譜，助長 QT 症候群 VUS 判讀 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.080900) |

---

# 📚 Honorable Mentions (2/2)

| 主題 | 重點 | 連結 |
|------|------|------|
| **Circulation — RACAD 回顧** | 放射相關冠狀動脈病變機轉與診療 state-of-the-art | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.079541) |
| **JACC HF — 子癇前症後心臟** | 產後亞臨床心衰的結構／功能變化與監測時機 | [DOI](https://doi.org/10.1016/j.jchf.2026.103421) |
| **EHJ — FH 與胸腺老化** | 中國世代：高膽固醇↓胸腺輸出，statin 部分保留 | [DOI](https://doi.org/10.1093/eurheartj/ehag810) |
| **JACC Adv — 瓣膜病 AF 基因** | UK Biobank：AF 多基因風險分數的獨立貢獻 | [DOI](https://doi.org/10.1016/j.jacadv.2026.103355) |
| **Circulation 社論 — TAVR 耐久性** | 年輕／低風險 TAVR vs 手術的耐久性抉擇 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.080256) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## JACC Case Reports — 罕見但可處置

---

# 🔬 Case 1 — ViV TAVI 即時血流動力導引

## [Konami Y, et al. *JACC Case Rep*. 2026:110841.](https://doi.org/10.1016/j.jaccas.2026.110841)

- 90 歲、19 mm 失效生物瓣、嚴重瓣內逆流，瓣中瓣（ViV）植入自擴瓣
- 同步監測主動脈／左室壓：第一次釋放後停止快速起搏，主動脈波形「**全平**」、左室仍脈動 → 回收
- 第二次釋放主動脈脈動恢復才定位；後擴張把侵入性平均壓差 23 → 11 mmHg
- **教學點**：主動脈波形平＋左室仍脈動＝警訊，提示多模態再確認、必要時回收

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABjklEQVR42u1YwW0DMQwT6gFuJK+ukW4AAYpEykk/zacFykcMI8idPwSPomhZ/rzCPoe/O7yt1spc/bTjcruyX9X/L3uz/uOw0O5Cve7d8IzgdyGv95poG179gtVoYuvRljLa9GI1wGoBlkdby0u0Rxi6aJMldnlAuqw4Vd3CE+79fet6wiyvTQG87E0RbVmBUwkotMHf/iCpW8h1Qw8WNLHCr1pl4wBVZeVdOb1MtsrWiHYAG/pviFaZ0xYCXz+JWZZbEMuE0KJFX4N0NT0hw0a3pYGqLxrCypStsrzZIIx7PE2SW/pAG2+3XYeATZZbo1xbDC0AmK0Je8Jo4BRdg1ftZYhhzDM5jQw+ppsT2m8h2jwM66bxixdKs7lCCt/LkpWV5JP2JZxv++uzuBb9gdHx0nWwZw4vkLykh/LdoVOunaC7wXbq3svQ0TL9zBO2rBJ4JSe33YXBrf48YWEHDEF2DsZREhvumd1laKOF0+aJ4i6bwZ5Oy8zAACY9q2G4vTlZ8kk4urOazzz+zw8fg62PfBEhJ54AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# 🔬 Case 2 — 頸動脈入路 TAVR＋股頸分流

## [Mourad N, et al. *JACC Case Rep*. 2026:110524.](https://doi.org/10.1016/j.jaccas.2026.110524)

- 67 歲、不適合股動脈入路；moyamoya 側枝不足
- 左頸動脈試夾 → 近紅外光譜 (NIRS) 腦氧下降 **>50%** → 建立**股—頸動脈分流**維持腦灌流
- 成功植入 26 mm Evolut FX+，無神經學併發症
- **教學點**：腦血管儲備受損者頸動脈入路有低灌流風險；NIRS 即時偵測、分流保護

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABiUlEQVR42u1Y0YlDMQwzlwEyUlb3SBkg4LPkJJRC76eU00dDKI/kR6iyrNji9Vr2vXzvclquFoE9R8xhPXBkY/3YH+s/LhPtCEKN8GXjIs9zTbRJY7LawnMnZnxPa8poQaxZ96Ae1NHyN6FCriaNtvhMYokZJ8K6pSfM8bh1PeEsfjs0cO1NEa3H5bM79WCQriraNm99QRgLzpCwQ1O3ZLJYBcmro1OoKoGsotuO6miphBD2hGq1+OsB2xM5pCuqhMFCyxKLYFMg1a7tCcZs47CC7k22yrYGUGv4gBK8urCybhkPqIHjDJrcLlIKjzWk8UV5mGyVobisZNCIuZxBNDGeWFvtDLotN5NEi9bAzayIKiuL0KwyBi63HcJxSCWLVhmfD0ZWY9uCsN/Ww3yH29KAtt/uGQLbBF8TQzaDUQxF6X7y1AxE911GK4BuzzxBVQl7VnPzTJSMpecJtiure7Ed2rOaCgxtT+1kdfs0WfI7txGe1djJ5B5npKDvCUbd6r4ivyP3T13+AhANqHtHELXrAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# 🔬 Case 3 — PCI 後頑固肺水腫（醫源性 AR）

## [Vijayachandra Y, et al. *JACC Case Rep*. 2026:110849.](https://doi.org/10.1016/j.jaccas.2026.110849)

- 49 歲、LAD 慢性全閉塞分期 PCI 失敗後反覆急性肺水腫
- 超音波：非冠竇與左冠竇 **7 mm 撕裂** → 重度偏心性急性主動脈逆流（AR）
- 心包補片重建＋冠脈繞道後痊癒
- **教學點**：PCI 後失代償不全是缺血；導管造成的瓣葉撕裂雖罕見，要用超音波迅速排除

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABmUlEQVR42u2YQWoFMQxDTXOAHMlXz5FygIBrSZlPN+2mlKrQMHwyPxvhkZ/tRH2+Tvwffu9wR6+xc+Atz1wxC3/1/i2+WL9x2GqzVY9a/RQ16+m9p9oOY0t9IrzOrLGxd1aLYE5E9Q+obffOJUscvtqqhUioVVRT7nX17cOED48vE15rK85wwsWbo1rQoE0bgi1MmxC8TWPbdm15yrVD97Z41ywLgaullgrEk2iese1fCl4AF6pDa3YlGOUFzVCMar8eks2Vt6i2RScw3UI1wpS3VNhZ1hFWpRiswp6x7e9+qJY6Q1XYNMt2qqEFHK51w5e3/O518RVMsfTlbYsEu5LNGPKLIwUCbtvVkAZFjtG3vpNOcMwpYZajWd2NJxNUGtjeoEkI5/4WxQv9DDkm3pYxb5lo6LtYHW7raMtbjY0hx7IEY+88OzDCmHHmpdmwnstC1n1m3rR1wp158fWD1yBZ7vcJednFKiyUOasdLGfszJexb+/8yEnn3oM5d4yvu5p7fTc1oPl2NYMY4+Sb6nhNfft/5f5Th+/7xoagYPEg6wAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# 🔬 Case 4 — 法洛氏四重症的意外 STEMI

## [Iavarone M, et al. *JACC Case Rep*. 2026:110256.](https://doi.org/10.1016/j.jaccas.2026.110256)

- 77 歲、部分矯正法洛氏四重症、殘餘 VSD 雙向分流＋新發心房顫動，下壁 STEMI
- 血管攝影：遠端右冠狀動脈閉塞、大量血栓、**無明顯粥狀硬化** → 冠狀動脈栓塞
- 持續性機械抽吸血栓切除成功
- **教學點**：成人先天心臟病有心內分流＋栓塞危險因子時，STEMI 要想到冠狀動脈栓塞

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABj0lEQVR42u1YwW0DMQwz6gEyklfXSB7AgCqSctJP+ymK8hHjEPjOH8KhKFIjv19nvA9/d7hHrZk5M85Y5xHjkfhU+4/xw/qPw0K7CvXcq+DxFTgLfH33RAt4BZK3enCxeJ3OaDPEhLrVAmyPFggz4xLDFy3goeCwrypjxdnylpqw19fHVxN6BbULhfaSN0e0ADkJuO75XPzQB0velggc/vVVXEciVvg9eUvteuKc2b3MtMqkANSuoq66AzaunbeAob4GpKwxG98tdGBDykhg9DVS11MTUGJzv9yX8M801QTealwzM+RwTNFm60BSGUgDbdKWt08yzJTYDltNyN0ckHUkk5drL2ujOGnG1Mi6wbkygakhRN1ucK7+Vm6235V0bP2tog1+g+aWAc3X34YyDuOYcll0X/PMZYyNNDO0tto7Zwf6cD4IlRSK9M1l2fHhzhOWLRMUyXW36MK8W/fphywNZiCDUybvyRIri4MFJTVztHfSqBSZaT5jVMCRAbOe1bRDWKf3y9bfvkfuf3P4CW4iiYs8UGFKAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# 🔬 Case 5 — Bioadaptor 植入鈣化病灶

## [Amoey D, et al. *JACC Case Rep*. 2026:110419.](https://doi.org/10.1016/j.jaccas.2026.110419)

- 3 例嚴重鈣化冠狀動脈病灶
- 2 例先 rotational atherectomy、1 例用 OPN 超高壓球囊後擴張，植入 sirolimus 洗脫鈷鉻 **bioadaptor**（可「解箍」恢復血管舒縮）
- 6 個月血管攝影皆維持通暢
- **教學點**：鈣化病灶需比一般藥物洗脫支架更積極做鈣質修飾，才能完全擴張、發揮長期功能效益

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABkUlEQVR42u1YwW0DMQwT6gFuJK3ukW4AA6pI2pd+2k8LlI8YThDb92B0NEUp6vux4n34u8M7eowbTw1s5LoKW/3jI34Y/3HYaPPgbMCT/yB72fueaDuMiG3Du+Yg8l4Oa7QgQIe3v3vHHW01V1NzhTXa0qsv0ACxJRlceStNyK/TVxM0iJC3DBHe8uaIdjbIjiRefRBzfxq2JxOItsDbAg0Q50bLNGHJ2wHqkq4XkGvpylvFNgUbkksFg/x66i2MQQpngw/eNdtbRjUooUWca1LETHlLKUglXC6DBDaNLbXryWUTxLjKlbfQLklWiAn3MTmePuF+gaQazGXLhO3B5rE3KYtr6xO2W7glYiHqLl+0ecwM1Gzsis02l9XjxGhukR1s9VaOS5580etuS+aZyyQIcrkgLaarB5P7kiHPx5K55jIxNlRLLka1VLD71mVAW7uZwJq3yrnmlfDuG8eqx7yfcFLw3nfu1ciT16l6vH1CKU0cfXDv1Sx5m9r1r2mlI01AjlBrUUwIa7199+P//vATwtaL1G+1LT4AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 💎 整合 Take Home

---

# 💎 本週 7 大臨床啟示

1. **factor XIa 在 ACS 落空**：LIBREXIA-ACS milvexian HR 1.05、p=0.50、因無效中止；未增加大出血，但無抗缺血效益。
2. **口服 GLP-1 先過安全關**：ACHIEVE-4 orforglipron MACE-4 HR 0.84 不劣於 glargine，低血糖更少（非劣，非優越）。
3. **對的工具放對場域**：ICare-FASTER 急診 POC hs-cTnI 停留 −47 分鐘、30 天安全性不變。
4. **個別化但留意復發**：POET II 縮短心內膜炎抗生素安全非劣，但復發 5.1% vs 1.6%。
5. **TAVI 風險分層走向影像＋生物標記**：AI 體組成補強風險分數；NT-proBNP「TAVR 看出院、SAVR 看 6 個月」；早期死亡靠腎功能＋併發症。
6. **TEER 操作學在進步**：單純 TEE 導引 MV-TEER 可行；複雜解剖依「力學軌跡」選入路。
7. **Case 旋律**：ViV 血流動力警訊、頸動脈入路腦灌流、醫源性 AR、先天心冠狀動脈栓塞——罕見但可處置，超音波與即時監測救命。

---

<!-- _class: ref -->
# 📑 完整參考文獻 (1/2)

**NEJM**
1. LIBREXIA-ACS Investigators. Milvexian after ACS. [*N Engl J Med*. 2026;395(16).](https://doi.org/10.1056/NEJMoa2608717)（PMID 42670965）
2. Bundgaard H, et al. Response-Tailored vs Standard-Duration Antibiotics for IE (POET II). [*N Engl J Med*. 2026;395(16):1600-1609.](https://doi.org/10.1056/NEJMoa2607887)（PMID 42663314）
3. Grunstein RR, et al. Retatrutide for OSA (TRIUMPH-1/2-OSA). [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2611477)（PMID 42904878）

**Lancet**
4. Klein KR, et al. Orforglipron vs insulin glargine CV safety (ACHIEVE-4). [*Lancet*. 2026;408(10564):1557-1570.](https://doi.org/10.1016/S0140-6736(26)01865-9)（PMID 42815506）

**EHJ**
5. Miró Ò, et al. Acute heart failure in emergency settings. [*Eur Heart J*. 2026.](https://doi.org/10.1093/eurheartj/ehag744)（PMID 42906949）
6. Li F, et al. FH and thymic ageing. [*Eur Heart J*. 2026.](https://doi.org/10.1093/eurheartj/ehag810)（PMID 42900678）

**JACC Family**
7. ASCEND CSP. [*JACC Clin Electrophysiol*. 2026.](https://doi.org/10.1016/j.jacep.2026.10.003)（PMID 42909432）
8. CSP vs BiVP meta-analysis. [*JACC Asia*. 2026.](https://doi.org/10.1016/j.jacasi.2026.09.002)（PMID 42905032）
9. Cardiac structure after preeclampsia. [*JACC Heart Fail*. 2026.](https://doi.org/10.1016/j.jchf.2026.103421)（PMID 42909429）
10. AF in VHD genetics (UK Biobank). [*JACC Adv*. 2026.](https://doi.org/10.1016/j.jacadv.2026.103355)（PMID 42901089）

---

<!-- _class: ref -->
# 📑 完整參考文獻 (2/2)

**Circulation Family**
11. Than M, et al. ICare-FASTER (POC hs-cTnI). [*Circulation*. 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.080866)（PMID 42895015）
12. Hadzic I, et al. DL 3D CT body composition & TAVR mortality. [*Circ Cardiovasc Imaging*. 2026:e020106.](https://doi.org/10.1161/CIRCIMAGING.126.020106)（PMID 42899353）
13. Harvey ML, et al. KCNQ1 variant-effect maps. [*Circulation*. 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.080900)（PMID 42899351）
14. Xia J, et al. Radiation vasculopathy (RACAD). [*Circulation*. 2026;154(16):1627-1645.](https://doi.org/10.1161/CIRCULATIONAHA.126.079541)（PMID 42895999）
15. Barbanti M, Maisano F. TAVR durability (Editorial). [*Circulation*. 2026;154(16):1545-1546.](https://doi.org/10.1161/CIRCULATIONAHA.126.080256)（PMID 42895998）

**TAVI / TEER（補充）**
16. Zheng HJ, et al. NT-proBNP after TAVR vs SAVR. [*Open Heart*. 2026;13(2):e004319.](https://doi.org/10.1136/openhrt-2026-004319)（PMID 42901732）
17. Zehir R, et al. KOSUTAVI. [*Anatol J Cardiol*. 2026.](https://doi.org/10.14744/AnatolJCardiol.2026.6567)（PMID 42904374）
18. Xing WZ, et al. TEE-guided MV-TEER. [*Zhonghua Xin Xue Guan Bing Za Zhi*. 2026;54(10):1206-1211.](https://doi.org/10.3760/cma.j.cn112148-20260901-00550)（PMID 42907226）
19. Papadopoulos GE, et al. SAVV-TEER in complex transposition. [*Catheter Cardiovasc Interv*. 2026.](https://doi.org/10.1002/ccd.70953)（PMID 42894438）

**Case Reports（JACC Case Rep）**
20. ViV TAVI hemodynamics [110841](https://doi.org/10.1016/j.jaccas.2026.110841)｜21. Carotid-access TAVR [110524](https://doi.org/10.1016/j.jaccas.2026.110524)｜22. Iatrogenic AR post-PCI [110849](https://doi.org/10.1016/j.jaccas.2026.110849)｜23. STEMI in ToF [110256](https://doi.org/10.1016/j.jaccas.2026.110256)｜24. Bioadaptor in calcified lesions [110419](https://doi.org/10.1016/j.jaccas.2026.110419)

---

<!-- _class: abbr -->
# 📑 縮寫對照 (1/2)

| 縮寫 | 全稱 | 中文 |
|------|------|------|
| ACS | Acute Coronary Syndrome | 急性冠心症 |
| MACE / MACE-4 | Major Adverse CV Events (4-component) | 主要不良心血管事件（四點式） |
| HR / CI / NI | Hazard Ratio / Confidence Interval / Non-Inferiority | 風險比／信賴區間／非劣性 |
| GLP-1 RA / GIP | GLP-1 Receptor Agonist / Glucose-dependent Insulinotropic Polypeptide | GLP-1 受體促效劑／葡萄糖依賴胰島素刺激多肽 |
| hs-cTn / hs-cTnI | High-sensitivity cardiac Troponin (I) | 高敏感性心肌肌鈣蛋白（I） |
| POC / ED / LOS | Point-of-Care / Emergency Dept / Length of Stay | 床邊即時／急診／停留時間 |
| IE | Infective Endocarditis | 感染性心內膜炎 |
| OSA / AHI | Obstructive Sleep Apnea / Apnea-Hypopnea Index | 阻塞性睡眠呼吸中止／呼吸中止低通氣指數 |
| TAVR / TAVI / SAVR | Transcatheter / Surgical Aortic Valve Replacement | 經導管／外科主動脈瓣置換 |
| AS / AR / ViV | Aortic Stenosis / Regurgitation / Valve-in-Valve | 主動脈瓣狹窄／逆流／瓣中瓣 |

---

<!-- _class: abbr -->
# 📑 縮寫對照 (2/2)

| 縮寫 | 全稱 | 中文 |
|------|------|------|
| NT-proBNP | N-terminal pro-B-type Natriuretic Peptide | N 端前 B 型利鈉肽 |
| LVEF / LVMI / LVESD | LV Ejection Fraction / Mass Index / End-Systolic Diameter | 左室射出分率／質量指數／收縮末徑 |
| TEER / MR | Transcatheter Edge-to-Edge Repair / Mitral Regurgitation | 經導管緣對緣修補／二尖瓣逆流 |
| TEE / SAVV | Transesophageal Echo / Systemic Atrioventricular Valve | 經食道超音波／系統性房室瓣 |
| ccTGA / d-TGA | congenitally corrected / dextro-Transposition of Great Arteries | 先天矯正型／右移型大血管轉位 |
| CSP / LBBAP / BiVP / CRT | Conduction System / LBB Area / Biventricular Pacing / Resync Therapy | 傳導系統／左束支區域／雙心室節律／再同步治療 |
| AF / VHD / PRS | Atrial Fibrillation / Valvular Heart Disease / Polygenic Risk Score | 心房顫動／瓣膜性心臟病／多基因風險分數 |
| RACAD / STEMI / NIRS | Radiation-Associated CAD / ST-Elevation MI / Near-Infrared Spectroscopy | 放射相關冠病／ST 上升型梗塞／近紅外光譜 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

> 本投影片為讀書會共筆之教學整理，僅供醫療專業人員教學與學術討論參考，不構成個別臨床決策建議。數據以原始文獻為準。
