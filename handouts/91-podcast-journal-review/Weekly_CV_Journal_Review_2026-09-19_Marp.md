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
  section.lead h2 { color: #9ec5ff; }
  section.lead h3 { color: #ffffff; font-weight: normal; }
  section.lead p { color: #f1f3f5; }
  section.lead strong { color: #ffe082; }
  section.lead a { color: #ffd166; text-decoration: underline; }
  section.lead blockquote {
    background-color: #fff5f5;
    border-left: 5px solid #ba181b;
    color: #1a2740;
  }
  section.lead blockquote p { color: #1a2740; }
  section.lead blockquote strong { color: #ba181b; }
  section.divider {
    background-color: #0072bc;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 { color: #ffffff; border-bottom: none; font-size: 2.4em; text-align: center; }
  section.divider h2 { color: #ffffff; font-size: 1.5em; text-align: center; font-weight: bold; }
  section.divider h3 { color: #ffe082; font-size: 1.2em; text-align: center; font-weight: normal; }
  section.divider p, section.divider strong { color: #ffffff; }
  section.bignum { background-color: #1a2740; color: #ffffff; text-align: center; }
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
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.68em; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.74em; }
  section.abbr { font-size: 0.62em; }
  .qr { position: absolute; right: 40px; bottom: 80px; text-align: center; font-size: 0.65em; color: #555; }
  .qr img { width: 110px; height: 110px; border: 1px solid #dcdde1; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-09-12 ~ 2026-09-19'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-09-12 ~ 2026-09-19

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每張重點投影片附 QR Code，可掃描跳轉原文（DOI）

> 本週主題：**影像與抗栓的「證據落地週」——把上週的裝置與大方向，換成本週的影像與抗栓決策依據**

---

# 🎯 本週主題與固定欄目

## 沒有大 RCT，NEJM／Lancet 皆無心血管原始研究；重量級證據在 JACC／Circulation 系列

- 🩺 **一張正常 stress CMR 可以「保固」多久？**（CE-MARC 15.5 年）
- 🧰 **鈣化病灶 PCI 該不該用 IVUS/OCT？**（網絡統合分析）
- 💊 **DCB 治支架內再狹窄，CKD 病人也有效嗎？**（AGENT IDE）
- 🫀 **心衰＋腎病，TAVI vs SAVR 怎麼選？**（TriNetX 權衡）
- ⚡ **PFA 打完到底持不持久？**（FRANCE PFA 登錄）

> **本週六大固定欄目**：⭐ Top 5 Picks｜🫀 TAVI｜🔧 TEER｜📚 Honorable Mentions｜🔬 Case Reports｜📖 參考文獻＋縮寫

---

# ⭐ Top 5 Picks 一覽

| # | 研究 | 期刊 | 方向 | 關鍵數字 |
|---|------|------|------|---------|
| 1 | **CE-MARC 保固期** CMR vs SPECT | *JACC Img* | 💡 | 追蹤 15.5 年；正常 CMR 保固 **6.8 年**、SPECT 5.1 年；異常 CMR HR 2.74 |
| 2 | **鈣化冠脈影像導引 PCI** | *JACC Adv* | ✅ | 4,003 人；MACE IVUS **RR 0.56**、OCT 0.65；支架血栓 RR 0.15/0.12 |
| 3 | **AGENT IDE**（DCB 治 ISR × CKD） | *Circ Interv* | ✅ | CKD HR 0.70、非 CKD 0.74；**交互作用 P=0.90** |
| 4 | **TAVI vs SAVR**（心衰＋CKD） | *JAHA* | ⚠️ | TAVI 死亡 **HR 1.56**、AKI **HR 0.69**（權衡） |
| 5 | **FRANCE PFA** 病灶耐久性 | *Circ EP* | 💡 | >12 放電/PV → 84% 持久 PVI；**二尖瓣峽部僅 31%** |

> **Pearl of the Week**：本週關鍵字＝**影像與抗栓的證據升級**——正常 CMR 保固近 7 年、鈣化病灶用影像更安全、DCB 不因 CKD 退縮、TAVI vs SAVR 是權衡、PFA 不是打了就持久。

---

<!-- _class: divider -->
# ⭐ Top 5 Picks
## 逐篇設計與結果

---

# CE-MARC：正常 stress CMR 保固近 7 年
## [Bisaccia G, et al. *JACC Cardiovasc Imaging* 2026](https://doi.org/10.1016/j.jcmg.2026.07.016)

- **設計**：CE-MARC 長期追蹤，疑似心絞痛者同做 stress CMR＋SPECT，冠脈攝影為金標準
- **族群/追蹤**：652 人；**中位 15.5 年**
- **保固期**（維持 97.5% 免 MACE）：**CMR 6.8 年、SPECT 5.1 年**
- **預後**：異常 CMR 校正後 **HR 2.74（1.70–4.42）**；年齡/抽菸/糖尿病縮短保固期

> **Take home**：正常 CMR 短期不必重複檢查；CMR 長期預後價值優於 SPECT。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABQ0lEQVR42u1YQQ7DIAyLxgN4El/nSXkAUuY4tOulO+ww+VCEKhAXy3GcpBY3a9nz8vXFDavFNBuLO+84vOxu/esF2AYwAhsOANZ8NNxdBRtYArYkrU8Aa25NDFsjgaRODRvWTN5cC1vqjTIDto1TBRvz1Me5hfL0YydU3XnViClllhaXmNxWl8FWrtvDehE2t9eJ5Cl5I7aZ5/yK8AalGcQWGdZgzRoq2LahGbHN2kslTw8wLKYQnlQuIKYZxAxr+bBOH3JRXZ91XSp620WhGMM1carkKfVGG4kgb13K36KyoBK2tCfib2ddIHVRDbBOPbUd02AusF/S6UPczkpa3aZQ/5bpwELvhwNL9b00E2Nh1ZkBa5YxTqYFTKe3NM5WKbnKiyphSrzFpfXVmrNoa4XKeujU05qzjuleqdY//6t+eXkDkL/nit0ZaSMAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# 鈣化冠脈病灶：影像導引降 MACE 與支架血栓
## [Panuccio G, et al. *JACC Adv* 2026;5(10 Pt 2):103237](https://doi.org/10.1016/j.jacadv.2026.103237)

- **設計**：網絡統合分析，10 研究、**4,003 人**（IVUS vs OCT vs 血管攝影導引）
- **MACE**：IVUS **RR 0.56（0.37–0.86）**、OCT **RR 0.65（0.52–0.82）**；兩影像模態相當
- **支架血栓**：IVUS RR 0.15、OCT RR 0.12；OCT 最小支架面積較大（+0.87 mm²）
- 隨機試驗敏感度分析方向一致

> **Take home**：鈣化病灶 PCI **常規用 IVUS 或 OCT 導引**，MACE 與支架血栓都更低。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABiklEQVR42u1YQW7DMAwT5gf4Sf66n+QHCHBFSk7aQ3cZhnFAjSBI6gurUCQt2++X22fzZ5vLYrW9G96G92l946d4/rJv1l9sBtoRqNsaXq/AGcjjd020gLcsqup9OwqL16aMFkwAB8CHuP8HtFHeQwxdtLtazMCE03GqvKUmrPF86WpCrZmaENS95U0RbTTXZHMBsB/8AVuTtzAFG+SDlYgFflXelgJQb6ljs/6FZG0DbfAh7kbAZnQK0S6bYCnlq4SLBBatLdDCF0BaEpg2odplqGfxNpWWpYa7qWpC8pam0IvAomhpDfjuxNkOK2TRWsaDVY1mF4c1Uw15mzbRsunCLES9rC4AJiUQFdB0okzIr3+SWMmabL5NU6j02Lf0uYxdRt4aHyzrrJpvZ979VJXnHXPVxHgNECqF85DuymeHk3IZdMEK0bPDPauZNx9kFexlVjPSGrb8POEyiIQtOweryRJKOs7sbrs22jydZbbRTYyHt5nE/KnOwppw/IvPbQ3hNP6Zx//G5gM8YYNbqyjZJgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# AGENT IDE：DCB 治 ISR，效益不因 CKD 而異
## [Tehrani BN, et al. *Circ Cardiovasc Interv* 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016978)

- **設計**：AGENT IDE 事後分析，冠脈 ISR 隨機 DCB vs 普通氣球，依有無 CKD 分層
- **族群**：DCB 組 406 人，**25% 有 CKD**（eGFR <60）
- **2 年 TLF**：CKD 者 DCB 23.6% vs POBA 30.0%（**HR 0.70**）；非 CKD 28.1% vs 34.9%（HR 0.74）
- **交互作用 P=0.90**——效益一致

> **Take home**：**ISR 病人（含 CKD）優先考慮藥物塗層氣球**，不因腎功能退縮。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABj0lEQVR42u1Y220EIAyLygCMxOoZiQGQqGPDtT93P61UVzqEEI8fKzKOk9jPx4r3488eZ2C0nRFjYfaMvusK+494Mf7iEWgHUBfaDuyjzdHquHHviTYIciGkvWBj02Y0a7TRSA2s/wEtGYsNYivw05i3WCu8uclYY95SE+b4Pn01QQOYu6JaTDjyZsrbkGpJddu98YxtfaiIxSMEgVJG+fXNDpuaUEcJgi1a4MQEyL2T2SF9FezAqwiDtA/wpr+MGrtKxOIwtjQhXRUsaQ/2zWIlYsq/ntkBU7GlDePGVsHoviqexYRUClaQPZnQDnXLjYO3Wk0VrKCmuCp/qy/mqrei61CaWDcX26Ldp8wJVmRHb301gWl3EfBiCVnc8HXjySqS340+YXm7GpIhhbyMrhKEa12mikyVL62jqybc2kEZLU6CGK6xffRqriVT+eDsxtlPWPxo9I3hzFsGk7+MPuGUPMa9mviqyFLGxhktXU2oD0YRc64ik+1Q+ltKhLUmMP+qAUKfk9Z6++7H//7jJ9zqjrZCbR5IAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TAVI vs SAVR（心衰＋CKD）：死亡較高、AKI 較少
## [Mortada I, et al. *J Am Heart Assoc* 2026:e051598](https://doi.org/10.1161/JAHA.126.051598)

- **設計**：TriNetX 全球網絡、21 共變數傾向配對；心衰＋CKD 成人 TAVI vs SAVR
- **族群**：配對後各 **1,034 人**，追蹤 2 年
- **全因死亡**：**TAVI HR 1.56（1.21–2.01）**（SAVR 較低）
- **AKI**：**TAVI HR 0.69（0.60–0.80）**（TAVI 較少）；MI/中風/再住院相近

> ⚠️ **Take home**：觀察性資料、**存選擇偏差**——是「腎臟保護 vs 長期存活」的**權衡**，非因果結論。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABQElEQVR42u2YPW4FIQyErXAAjsTVOdIeAInMD7xUL0WKaIqHtmCX5pM9Hput/Wat+pz8evIUVttzP6PhQ998r7G+6t36rxOwDTBeKuLhwccQNiIBBmwdgcS+WhzbXEWqPLZaUh1CF8VGvT3cLL0m6U11ylSeJ6hOvUCoOv1xlxS9UWmS3LivGWxwXT23FmaJMCSncI+mivCm5eQUEessTBpvZ1NA6LAJ0psq1HoDbYzemEo5CdMq7x05/mYkQSKnLoqUnLojWHUHLEVvZd9YN3RBevNIWcM1a86cXs/BQ+2++hkyc+K2+kmlY2ijS/G3Pu236lY0k7Q5xG3rhRc0v9k3fJ15kvxtn17giXcH9YVzlznGq4S2oNlyyECm5ze6XIXFTZ1UYDS6pHs9PGTWrYWgfiqZvW4KQXr7/K/6y8k36vHj9B16ObMAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# FRANCE PFA：真實世界「劑量—耐久性」曲線
## [Beneyto M, et al. *Circ Arrhythm Electrophysiol* 2026:e014506](https://doi.org/10.1161/CIRCEP.125.014506)

- **設計**：FRANCE PFA 全國登錄；復發重做者（n=145）3D remapping 評估病灶
- **復發型態**：AF 58%、AT 28%、典型 AFL 8%
- **持久 PVI 僅 42%**；**放電 >12 次/PV → 84%**；頂部/後壁 >16 次 → 88%
- **二尖瓣峽部阻斷耐久性僅 31%**（與放電次數無關）

> **Take home**：PFA 肺靜脈要**打足次數**；**二尖瓣峽部**是 pentaspline 的罩門。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABQUlEQVR42u2YQY7DMAwDhdUD/KR8XU/yAwx4KdJpe2mBvSx4qGEYTnwZKCIlJ/abseJ78vFkBkbujRX7Pa9+jmv9xLvxXycNA8YE4WjY5MRLEzZEKWdP4K3eR3qxIW6Vu5Ix9GLrfMNaCJ0Vm9KsqXbh0SnfqNN5PaaRTjVmQAWYT3dx8pA1SpDKOo+4VTZeZxriFoyeCxuQRouUKxPP55viCzZYyYH7kR/XRKeqUx23UVyNalargIRg6+rAxDPxEPEodBDpYltio9NjblIELcUkbkU59GYdtkob72UZDalAfmLTW8pG4kg1hGrTh3DKclWwfOophXmsg23JZdaHnPYyiOdTF5hsr5Ur0qpHkm/Eyb1l04fc2gyacA83NhlvyHv97lkC67fDKt/uq596ErN7lorCPhfVbeRv3z9Zfzv5BfI842TtomiSAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 結構性主動脈瓣方向

---

# TAVI #2：平均 vFFR 預測 TAVI 預後（台北榮總）
## [Legaspi EP, Serruys PW, et al. *Catheter Cardiovasc Interv* 2026](https://doi.org/10.1002/ccd.70889)

- **設計**：TAVI 前冠脈攝影**無顯著狹窄（<70%）**者，計算三大冠脈平均 vFFR（n=164）
- **終點**：全因死亡或心衰住院（平均追蹤 1,241 天），事件 26.2%
- **平均 vFFR 每降 0.1 → 風險升（adjHR 1.62，1.03–2.55，P=0.035）**
- 「單一血管最低 vFFR」則與終點無關 → **患者層級整體生理負荷**更重要

> **Take home**：即使無阻塞狹窄，**瀰漫性冠脈生理受損**仍有 TAVI 預後意義。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABR0lEQVR42u1YMa5DIQyLPgfgSFw9R+IASKmdhHZqhw5fHorQE4jFcmIneRZv1rHfy8eXbVhjL5u44bp4t3X+7N36rxeCAcYBhDMS5xq4bxVsxLNJ3TGy12cdbOH4grcRetg2Nw4vDnXyLTwypnnWybfW6XML6bSX23TwVtTRXTRiehokwmrX4lR4K4W+UKWTqGiBxuuHm0Kw/Kp4yPRKOYDktzSrEdOkC0IwamFGFi8VfxsJDzG9RUGn1rcEEErAQ3yrTMh476ocYyhnZFsikm/OOMaliynnMt5bvEXCqy5Ox9+sg0jXpVSHjodkQBshawR9WMZ7rRq2m3VWkRXqQ3JeqO6oOFTq36wlkH2vTo9Uc9ZzUqgGWGteCG8tVGFVmgG7KCSNWvNpW5yd7My15vrkivCmh9AM2HMWO7c7qKro9Pe/6puXB0iq1sVEMt5bAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TAVI #3：傳導軸「避開它 / 到達它」
## [Jilaihawi H, Makkar RR, et al. *Heart Rhythm* 2026](https://doi.org/10.1016/j.hrthm.2026.09.009)

- 核心論點：TAVR 傳導傷害與傳導系統起搏 (CSP) 取決於**同一條 His-Purkinje 軸**
- **TAVR**：當代 PPM 率近 **16%**；以膜性中隔長度導引可降至 **3–5%**；植入每低於 His 束 1 mm，起搏勝算 ↑25%
- **CSP**：越接近左束支/心內膜，每 1 mm 多 0.25–0.63% EF 獲益
- **共同工具**：由常規心臟 CT 重建傳導軸

> **Take home**：**TAVR 要避開、CSP 要命中**；CT 量化植入深度把 PPM 壓到個位數。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABk0lEQVR42u1YQW4EMQhDzQPypHydJ80DkCjYZHtqL61UHzaKRjPJxWKMMVh+v8Lel7+7fKzW6tez0vtzZx/ZiQ/7Yf3HZaE9hbrRbs/0APLada6JtsK4CtvO1ci9nuuxpYy2QKbbdgZWHW1F9Zl3fOqibd4WNuvNE2HeQhOaq19bVxNmeTRpsRHtljdFtJ4QARAAifYYtFcUbf/0nUyxpiuEt2qEJloSFZoAGoMSokwoqNtbDRBS8BZkVtUElIPDZ50EqavLhEoro9jOc8sywV6VFxWts6wvtihv8xYyJNcIgqre5jW0hvyi/B5R3j42zhbxJId19RbxXKwRdlAsWnJDmLfQMSclCmcHVtTVTGCnwaG9QYFQ5W3GmLHuIgO2QbU6TIe7kGhsJ8NMFy0ieY2i04+J8hamq3cbG1AC3YRsbOG4ZujB/hHGLHX7MkgBO8ppJVT9LWY1zuTK6220ZzUtCzkRnnPlWU1stpAHBJbl7ZlCNo35tGlLmbdsH2DGUnmecDWBhoG8JWbhWc17Hv/nl59lKZ9pofNbkgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 二尖瓣緣對緣與瓣膜影像

---

# TEER #1：不成比例 FMR 由「瓣膜形態」驅動
## [Arao Y, Kagiyama N, et al. *Circ J* 2026](https://doi.org/10.1253/circj.CJ-26-0057)

- **設計**：接受 TEER 的功能性 MR，依 EROA/LVEDV 分不成比例 (d-FMR) vs 成比例 (n=114)
- **d-FMR** 者 LVEDV 較小、tenting 較低，卻 EROA 較大
- 較多**假性脫垂 (29% vs 8%)、極度瓣環擴張 (53% vs 29%)、深裂隙 (24% vs 4%)**
- 形態因子數目與 d-FMR 相關（**OR 4.15，P<0.001**），也與 **TEER 後殘餘 MR** 相關

> **Take home**：以**表型/形態**解讀 FMR，並據以預測 TEER 後殘餘 MR。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABRklEQVR42u2Yy23EMAxEiagAl+TWWZILEMDMR5vbBsglmMMKhqFdXR74maFc82bt+pz8evIU1sL2auznufm77v1V79Z/nRAGjEtUYFvPDU7sQ9gQJbAxdAU87bPYnEoSxrFNn/eVxcZ6E9VMa59Tb0oly+w8QX3q9YgHz/VSlyANAVVvhdH5zYhbn4jp8T6FjRFj/ReR+mjvpMQNoiHDut2qIIypNxVYAW+YSr1zNASxUiMwp07rjvF6UwHP1rA9loToG2WEcWOZSd9SPGtao1EdQrXDytFeltzYFNgLVrmMXlBvssxMtRjJlF4QzI8IeyAJ8oWXsbZNP20OkQiz2E755cxvnCrbk9u5OyTNvXJVaZ3+ybovyLbUrYRMYqMXML/W3qx7FrSXk5JnkpzZ0vV2xOSyhUXds6oUNMtI0Bzy+ZL155Nv73LkqJ/lgIwAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TEER #2：CT planimetry 量測二尖瓣狹窄
## [Steinhoff P, et al. *Int J Cardiovasc Imaging* 2026](https://doi.org/10.1007/s10554-026-03803-9)

- **設計**：85 名 MS（平均壓差 ≥5 mmHg），90 天內同時有心臟 CT 與超音波
- CT planimetry 量瓣口面積**高度可重複（ICC 0.983）**
- 與平均壓差反向相關（rho −0.60）、與超音波 planimetry 中度相關（rho 0.58）
- **與壓力半時間 (PHT) 法相關性弱**

> **Take home**：超音波不清楚或退化性 MS 時，**CT planimetry 是可靠補充**（同套 CT 兼做 TMVR 規劃）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABR0lEQVR42u1YwY3DMAwTzgN4JK+ukTKAAZUinfY+PaCfAx81gkCpP4REkVKj3pwd35s/b67AGQhn6d3fsfZPvDv/dQNsCxhH5bhiz2Rc+NEEG7IEYAPB7FwqdsKG7OWORmWILWaiskidFTbWseEhb2Z8Y58Smx6jPtVBkwJPrJe6uPAN+pYsaN6fJtj6eSobAhTUSN/gBd2eC8Cack417VJWKV0dzIRzmdRUdQTfpL2A6sI3ipvydhz/suEbT/Otcutt1KeL4nYcYd/zkgm2IYLNzhhHkfTJG+0gJXHqCx+vBzbyTay7B2AX7c1fHdFvH76hF9Se1LceQszmkFty2x18dhntWWwEjkk99xr5ac/hm6UsmUJ47VlBJfHi23MHrKNvQGiGrZMmUwi6g9NeX4dmzKHP/KY9q3NFoz/Dko++ff/J+uzmAbU37Ve+IL/aAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

# 📚 Honorable Mentions（1/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **全穀類與心代謝風險** | *EHJ* | 87 RCT；+48 g/day → SBP **−0.82 mmHg**、LDL −0.07、總膽固醇 −0.10；60–100 g 效益最大 | [DOI](https://doi.org/10.1093/eurheartj/ehag519) |
| **SODa-BIC**（碳酸氫鈉/重症酸中毒） | *NEJM* | 500 人；30 天 MAKE **40.2% vs 39.4%，P=0.78 → 中性/陰性** | [DOI](https://doi.org/10.1056/NEJMoa2600526) |
| **TAVI 後感染性心內膜炎** | *Int J Cardiol* | 捷克全國 9,887 例；IE **1.3%**、院內死亡 **27%**；腸球菌/金黃葡萄球菌最多 | [DOI](https://doi.org/10.1016/j.ijcard.2026.134928) |
| **RAISE 分數（AS 併 ATTR-CA）** | *Int J Cardiol* | AMYLOCOR 340 人；ATTR 盛行率 4.1%；**AUC 0.69（低於原始）** | [DOI](https://doi.org/10.1016/j.ijcard.2026.134787) |

---

# 📚 Honorable Mentions（2/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **PFA 平台間腦病灶負荷差異** | *Circ EP* | 無聲腦梗塞發生率相近、但**病灶負荷不同**（letter） | [DOI](https://doi.org/10.1161/CIRCEP.126.015214) |
| **骨質肌少症與新發 AF** | *JACC Asia* | UK Biobank n=482,137；骨質肌少症 **aHR 1.33**（單純肌少症則否） | [DOI](https://doi.org/10.1016/j.jacasi.2026.08.006) |
| **長時間太空飛行與心臟** | *Circulation* | 13 太空人、164 天；微重力心臟改變**初期下降後回穩、可逆** | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.125.078665) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構／冠脈介入 × 5

---

# Case #1：TAVR 中鈣化腫瘤栓塞致左主幹阻塞
## [Suzuyama H, et al. *JACC Case Rep* 2026:110341](https://doi.org/10.1016/j.jaccas.2026.110341)

- 96 歲女性，重度 AS，經股 self-expanding **Evolut FX** 植入
- 心內超音波見**後二尖瓣葉活動性鈣化病灶**，於瓣膜展開時消失
- 植入後急性**左主幹阻塞**致心因性休克 → **VA-ECMO＋救援 PCI** 成功；IVUS 見鈣化＋軟組織
- CT 提示**二尖瓣環鈣化（鈣化無定形腫瘤）**經放大瓣口栓塞

> **教訓**：術中活動性瓣上鈣化病灶＝潛在栓塞源；**TAVR team 常備 ECMO＋冠脈救援**。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABiklEQVR42u1YMW4DMQwT4gfck/x1P8kPOEAVSbnt0i5BEA4xbsjZC4+hSFmRf687PofPHe6oNfbMXAMb874SW/XjEf+sdxwW2sKZhbPgFWB+wazX2vdEWzjHBr1xgV48fDVGO2++lgxqxx3tEQPkGtZok3+9ag3cErmrbhvn78fXE7So1UI+6GNtb45o130tyVWKRbmVObgqodCCW6hXTltoGROWaDsaUGLgmRU3bbNM3AI2ZdB6uNKU2y2bZTTkYqIt1ypL4Ww+i+dcjd/Ub5W8NLGyCHqCqRIAD9Jt1wLUhCfY6jYBjwHRFacINs2yBqn8DfmYK7fqwRQQJybowJ7c6tbQmQt/WNZZJlbpsejH+sZmyu2gLYyfthzpEL59wpIJRPcJs9sGS7/95laJFvReV91SA8dv1dtEGPutelrUF50WMgjze1m7rnpyBpzznTflA6yyZJPjnGUUAMY1Ytt7sjTPGOE0kNZ9Qqq+jj+4z2oUasjffcLX1hM49BjHbH1vkZ+R+6sOvwA0rokoMjEAPQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #2：高風險 TMVR 防 LVOT 阻塞
## [Bashir H, Garcia S, et al. *JACC Case Rep* 2026:110266](https://doi.org/10.1016/j.jaccas.2026.110266)

- 74 歲女性，退化 27-mm 外科二尖瓣生物瓣、重度 MS＋雙心室衰竭，redo 高風險
- **ECMO 支撐**下 valve-in-valve TMVR
- **球囊輔助前葉移位 (BATMAN)** ＋葉內部署 26-mm 球擴瓣
- **左心室起搏導絲**（免置放 RV 暫時性起搏導線）＋13-F 可調彎鞘通過鈣化瓣葉
  <small>原文：*LV pacing guidewire … rapid pacing while avoiding right ventricular instrumentation*</small>

> **教訓**：小 neo-LVOT 的**組合技**——BATMAN＋MCS＋LV 起搏導絲＋可調彎鞘。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABk0lEQVR42u2Yy20EMQxDhbgAleTWXZILMKCYpD3IJXvZAOFhBwOsMb4QWurpE/X7s+Jz+d7ljP202VuNFX3liCx82uevePH8x+VW27fqBumDmkvv/u6pdoexIcz9RDirTUTbWS3kSba/2rndPeq611ktfLtzLRlVOtbYt5cJP15fJjwwS+TXithOOF8c1Q78JPB1IMZ0M3UC2bX412/3LrpX4k3VnuSKJizMrkRzdQIKLm0QrA6jbAnG/BIESuDa6UaymRIsi9QdPEP56XAs1bLvGsTsqRSwQZZnLQMKALE6gWWETbOMYUSfMEOYfQ6eTFBXIN8yxbovb9l9teMH9GCqF+Hp2yowoZBoYleb4TzpNJhhsJ+hyNvb2Pa30swIl0YJ27ls5XgKrnhbxrwN6GQHnqrC0m+r9i4Qkl345Nl5djgcu225enLfuYxeZbG4i4UynnnR0pAG8G257xM07ARtgIMvE6QW4wPbsBzGvj27Guos7cGcO8ZnV3N8mxrQypcJpcG8hC9tmZx3NZ99/F9ffgOWfYpaXupEeQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #3：PCI 後後房血腫致休克——經心包救援
## [Youssef A, et al. *JACC Case Rep* 2026:110336](https://doi.org/10.1016/j.jaccas.2026.110336)

- 76 歲女性、既往 CABG，高風險左主幹＋LCx PCI 併近端 LCx 穿孔（3 覆膜支架封閉）
- 數小時後進行性休克 → **50×40 mm 後房局限性血腫壓迫左心房**
- 兩家中心因既往 CABG 拒絕外科；劍突下引流失敗
- **大口徑經心包抽吸（20-F Triever）** 清除機化血腫，血流動力立即恢復，免於外科

> **教訓**：既往 CABG 者穿孔常成**局限性血腫**；外科不可行時大口徑經心包抽吸可救命。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABiElEQVR42u1YQWoEMQwzzQPypHw9T8oDBlxLcpZe2ksLVaEh7IbkIjyyLDvy8/XE/+P3Hk/UGmeN3E+sZ+6Yias6v8UX6zceC+0q1APQNzGndt17oq0wMrA3wjPHwdkYLeKpwx9Ae4rdm5QAe53RAqTgMbZ5ljFvryZ82L6a8FoHca5cqwi3vDmi3fibkK8WMVLCVsFQFPjpi70lCLUF3pMJTK6ObTK2SjRbJlTBpQ4Eq8NOWwVjFSsaQBkkXBM3vpV3ZnaKId0Imw7HUm9B2mtpyFvSYKarJkRbmiMp42+6oqWNEVe5w1hvO7lUzphiy1dvr6tJhZdOjIDTVxMS9UvaNU4Yuxok1Lj1l61Z9sEytuoXxASYhFjWfdns4ivTOE4LhauCbfEWmQXk67HXW9Uv6RgAO/cO7CLHaaWVbzTvy562ZGvY+ttbHfT1aXdXus8TWLxkHRltW00Q2hZbKMM25m3PaqRgmoM5O8bXrEZTO1lcV7TRHRkKREq+xGHrWc3/PP6HH98BzG6P1pwlQWAAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #4：合併三房心的退化性 MR 之 TEER
## [Li S, Zhong Y, et al. *JACC Case Rep* 2026:110331](https://doi.org/10.1016/j.jaccas.2026.110331)

- 78 歲女性，後葉脫垂重度退化性 MR；術前意外發現**完整無孔三房心 (CTS) 膜**
- 透過**經膜通路**依序植入 **3 個夾子**
- MR 由重度 → trace，平均跨瓣壓差 3 mmHg；術後 7 天出院

> **教訓**：複雜解剖（三房心）下 **M-TEER 可行且安全**——關鍵在**縝密的術前影像與經膜穿刺規劃**。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABiklEQVR42u1YQY4DIQyLlgfwJL6eJ/UBSGlsM6NeupdVtT4UjaoBenCpY8dEvR87vpt/23xEj/HAtwYW1p6FpX75iV/Gf2w22kWcuRtzJX/Bati97om2j7HPdvTLzMET1tQZbczaM5sGveKOlgTQ+w5rtMW/HrXWmGep3Fx5K01Yr4+vJmiwxCQL45Y3R7RdWRkkrRjbmCEOnkwgWuhAASEZS30wdYdQieFsoWDJ6XL1Mvz1wiwaHD5MU942B2gNFZCvpKOla5VBbC9NABmKBLZlgixMgOvSBF8msL4wOUwoEcNUE6okWSEm0M5c0S5pF2VBapDbmAkSAcUH2gS6GtsqC+qA2pse4LCxl53soHJj36i8Y+sOsoZ+SAP6ha3eChsShPqEI7+2VXYbBANaHl9zVTBFGwJWS+aqt3d2OLksGSfDO5exb2TMkUeMKuPMu44jsMqUeszvE2S7dUcJ37sanLCqTFPbruY6W3XmC32j/V3N9ZnqIU2TzrlTSlbZEVvjFPm9cv/Q5hMeRoYiO2iS/wAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #5：CABG 後十年巨大 LV 假性動脈瘤
## [Goyal D, et al. *BMJ Case Rep* 2026;19(9):e273169](https://doi.org/10.1136/bcr-2026-273169)

- 60 多歲女性，10 年前 CABG，偶然發現心臟陰影
- CT：**9.0×7.5 cm 巨大鈣化 LV 假性動脈瘤**、窄頸、部分腔內血栓
- 3D 重建呈**「雙腔左心室」**外觀（推測外科相關慢性包裹性破裂）
- 橋血管通暢、原生冠脈無顯著病變；病人拒絕手術，保守追蹤 12 個月穩定

> **教訓**：**多模態影像**辨識罕見「雙腔 LV」外觀；病因鑑別＋共享決策。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABOUlEQVR42u1YwQ0CMQyL6AAdqat3pBsgUnCcFF7Hgwfyg+oEhH6sxHaSs7g5bv+bjzeX4QxG+PQZGdvyh92dX90A2yKqjR/OMHFeKtiQpUFIeGzGuGxoYUNZN/KWIPWwgWmAp5a35BvJZnJ8o06v9XqEdFqHqCqH7S4qfDN6iPk7FMFmRTbAo4dsFFTH36INZPncZXRKNUXe6CRtvxt+oqGFXcY7Ts8KFlckb4CEasJ1o3uWDt8SWHXSUoQL6TS10HW01cBk+Fa+QXmmCpT4xjqyxad1FE4Zf/N2j0xgFVRJp+kbwdG3RTFVsFXGalMYOZYstTmEX9VMdXaZ2rOaad7zeUjNvUYJRE1xevuCH74NpTkkDa2sY+5inVbeEKS/7fx3htxenzZy6iu0Z9k4m4IQ3/7vq765eQLgAeHqPa38wwAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 💎 Take Home Message
## 本週 7 大臨床啟示

---

# 💎 本週 Take Home（1/2）

1. **CE-MARC 💡**：正常 stress CMR 保固 **6.8 年**（SPECT 5.1 年），異常 CMR HR 2.74 → 正常者短期不必重複、CMR 作 gatekeeper。
2. **鈣化病灶影像導引 ✅**：IVUS/OCT 導引 PCI **降 MACE 與支架血栓**（RR 0.56/0.65）→ 鈣化常規用影像。
3. **AGENT IDE ✅**：DCB 治 ISR 效益**不因 CKD 而異**（交互作用 P=0.90）→ 含 CKD 皆優先 DCB。
4. **TAVI vs SAVR（心衰＋CKD）⚠️**：TAVI 死亡較高（HR 1.56）、AKI 較少（HR 0.69）→ **權衡**，觀察性資料審慎。

---

# 💎 本週 Take Home（2/2）

5. **FRANCE PFA 💡**：持久 PVI 僅 42%，>12 放電/PV 才達 84%；**二尖瓣峽部僅 31%** → 打足次數、認清罩門。
6. **TAVI 細節 🫀**：平均 vFFR 預測預後（adjHR 1.62/每降 0.1）；傳導軸「避開/命中」——CT 量化把 PPM 從 16%→個位數；TAVI 後 IE 1.3%、院內死亡 27%。
7. **結構＋介入救援思維 🔧**：TAVR 冠脈栓塞備 ECMO＋PCI；高風險 TMVR 用 **BATMAN＋ECMO**；PCI 後後房血腫大口徑經心包抽吸；複雜解剖下 TEER 仍可行——**影像 × heart team × 個體化**。

---

<!-- _class: small-text -->
# 📖 參考文獻（1/2）

**Top 5 Picks**
1. Bisaccia G, et al. Long-Term Warranty Period of Stress CMR and SPECT in Stable Angina. [*JACC Cardiovasc Imaging* 2026.](https://doi.org/10.1016/j.jcmg.2026.07.016) PMID 42747370
2. Panuccio G, et al. Intravascular Imaging-Guided PCI for Calcified Coronary Lesions: A Network Meta-Analysis. [*JACC Adv* 2026;5(10 Pt 2):103237.](https://doi.org/10.1016/j.jacadv.2026.103237) PMID 42753331
3. Tehrani BN, et al. CKD and Outcomes After Paclitaxel-Coated Balloon for Coronary ISR (AGENT IDE). [*Circ Cardiovasc Interv* 2026:e016978.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016978) PMID 42751771
4. Mortada I, et al. TAVI vs SAVR in Heart Failure and CKD. [*J Am Heart Assoc* 2026:e051598.](https://doi.org/10.1161/JAHA.126.051598) PMID 42757916
5. Beneyto M, et al. Recurrent Arrhythmias and Lesion Assessment Late After PFA (FRANCE PFA). [*Circ Arrhythm Electrophysiol* 2026:e014506.](https://doi.org/10.1161/CIRCEP.125.014506) PMID 42755708

**TAVI / TEER**
6. Legaspi EP, Serruys PW, et al. Mean vFFR Predicts Outcomes After TAVI. [*Catheter Cardiovasc Interv* 2026.](https://doi.org/10.1002/ccd.70889) PMID 42754994
7. Jilaihawi H, et al. The Cardiac Conduction Axis in TAVR and CSP. [*Heart Rhythm* 2026.](https://doi.org/10.1016/j.hrthm.2026.09.009) PMID 42749238
8. Arao Y, et al. Determinants of Disproportionality in Functional MR. [*Circ J* 2026.](https://doi.org/10.1253/circj.CJ-26-0057) PMID 42749617
9. Steinhoff P, et al. CT Planimetry for Mitral Stenosis. [*Int J Cardiovasc Imaging* 2026.](https://doi.org/10.1007/s10554-026-03803-9) PMID 42754742

---

<!-- _class: small-text -->
# 📖 參考文獻（2/2）

**Honorable Mentions**
10. Naghshi S, et al. Whole-grain consumption and cardiometabolic risk: meta-analysis of RCTs. [*Eur Heart J* 2026:ehag519.](https://doi.org/10.1093/eurheartj/ehag519) PMID 42743912
11. Serpa Neto A, et al. Sodium Bicarbonate for Critically Ill Adults with Metabolic Acidosis and Shock (SODa-BIC). [*N Engl J Med* 2026;395(11):1062-74.](https://doi.org/10.1056/NEJMoa2600526) PMID 42283370
12. Toušek P, et al. Infective endocarditis after TAVI - national registry. [*Int J Cardiol* 2026:134928.](https://doi.org/10.1016/j.ijcard.2026.134928) PMID 42749087
13. Roldán Guerra Á, et al. External validation of the RAISE score (AMYLOCOR). [*Int J Cardiol* 2026:134787.](https://doi.org/10.1016/j.ijcard.2026.134787) PMID 42754100
14. Takase T, et al. Silent Cerebral Lesion Burden Across PFA Platforms. [*Circ Arrhythm Electrophysiol* 2026:e015214.](https://doi.org/10.1161/CIRCEP.126.015214) PMID 42746736
15. Lee KY, et al. Osteosarcopenia as a Risk Factor for AF. [*JACC Asia* 2026.](https://doi.org/10.1016/j.jacasi.2026.08.006) PMID 42747365
16. Appadurai V, et al. Prolonged Spaceflight and Cardiac Structure/Function. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.125.078665) PMID 42741837

**Case Reports**
17. Suzuyama H, et al. [*JACC Case Rep* 2026:110341.](https://doi.org/10.1016/j.jaccas.2026.110341) ｜ 18. Bashir H, et al. [110266.](https://doi.org/10.1016/j.jaccas.2026.110266) ｜ 19. Youssef A, et al. [110336.](https://doi.org/10.1016/j.jaccas.2026.110336) ｜ 20. Li S, et al. [110331.](https://doi.org/10.1016/j.jaccas.2026.110331) ｜ 21. Goyal D, et al. [*BMJ Case Rep* 2026:e273169.](https://doi.org/10.1136/bcr-2026-273169)

---

<!-- _class: abbr -->
# 縮寫對照（1/2）

| 縮寫 | 全名 | 中文 |
|------|------|------|
| CMR / SPECT | Cardiac Magnetic Resonance / Single-Photon Emission CT | 心臟磁振造影／單光子放射斷層 |
| PCI | Percutaneous Coronary Intervention | 經皮冠狀動脈介入 |
| IVUS / OCT | Intravascular Ultrasound / Optical Coherence Tomography | 血管內超音波／光學同調斷層 |
| MACE | Major Adverse Cardiovascular Events | 主要不良心血管事件 |
| ISR | In-Stent Restenosis | 支架內再狹窄 |
| DCB / POBA | Drug-Coated Balloon / Plain Balloon Angioplasty | 藥物塗層氣球／普通氣球 |
| TLF / TLR / TVR | Target Lesion Failure / Lesion / Vessel Revascularization | 標的病灶失敗／再血管化 |
| TAVI / SAVR | Transcatheter / Surgical Aortic Valve Replacement | 經導管／外科主動脈瓣置換 |
| AS / AR | Aortic Stenosis / Regurgitation | 主動脈瓣狹窄／逆流 |
| CKD / AKI | Chronic Kidney Disease / Acute Kidney Injury | 慢性腎病／急性腎損傷 |

---

<!-- _class: abbr -->
# 縮寫對照（2/2）

| 縮寫 | 全名 | 中文 |
|------|------|------|
| PPM / CSP / LBBAP | Permanent Pacemaker / Conduction-System / LBB Area Pacing | 永久節律器／傳導系統起搏 |
| vFFR | Angiography-derived Fractional Flow Reserve | 血管攝影衍生血流儲備分數 |
| PFA / PVI | Pulsed-Field Ablation / Pulmonary Vein Isolation | 脈衝場消融／肺靜脈隔離 |
| AF / AT / AFL | Atrial Fibrillation / Tachycardia / Flutter | 心房顫動／頻脈／撲動 |
| TEER / FMR | Transcatheter Edge-to-Edge Repair / Functional MR | 經導管緣對緣修復／功能性二尖瓣逆流 |
| EROA / LVEDV | Effective Regurgitant Orifice Area / LV End-Diastolic Volume | 有效逆流口面積／左室舒張末容積 |
| MS / MVA / PHT | Mitral Stenosis / Valve Area / Pressure Half-Time | 二尖瓣狹窄／瓣口面積／壓力半時間 |
| TMVR / LVOT | Transcatheter Mitral Valve Replacement / LV Outflow Tract | 經導管二尖瓣置換／左室流出道 |
| ATTR-CA / IE | Transthyretin Cardiac Amyloidosis / Infective Endocarditis | 轉甲狀腺素蛋白心臟類澱粉／感染性心內膜炎 |
| MCS / VA-ECMO | Mechanical Circulatory Support / Venoarterial ECMO | 機械循環支持／靜脈-動脈體外膜氧合 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

📅 2026-09-19｜涵蓋 2026-09-12 ~ 2026-09-19

> 本講義為讀書會共筆之教學整理，僅供醫療專業同仁臨床教學交流參考，不作為個案診療依據。本期無新大型 RCT，NEJM/Lancet 無心血管原始研究；所選文獻多為登錄／觀察性／統合分析／事後分析，關鍵數字以各篇 abstract 為準。
