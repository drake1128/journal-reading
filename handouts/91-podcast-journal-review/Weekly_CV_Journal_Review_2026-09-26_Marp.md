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
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-09-19 ~ 2026-09-26'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-09-19 ~ 2026-09-26

**整理：謝慕揚 MD, PhD, FESC**
涵蓋：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

> **本週主題：精準化與真實世界落地週** — 抗栓依性別／情境精準化、結構性介入從 RCT 走入真實世界

---

# 🎯 本週主題與六大固定欄目

**本週定位：精準化與真實世界落地週**
NEJM／Lancet 本週無新心血管原始研究；重量級證據集中在 **EuroIntervention 專輯號、EHJ、Circulation、JACC 系列**。

- **主線一（抗栓／冠脈生理精準化）**：SMART-CHOICE 3 性別分層、FFR 導引 NSTE-ACS 安全減 PCI
- **主線二（右心／EP／代謝機轉）**：sotatercept 右心力學、星狀神經節阻斷降 POAF、SELECT 中介分析
- **主線三（結構性介入真實世界＋再定義）**：DEDICATE 外推、TTVI／M-TEER 採用趨勢、M-TEER 成功再定義

| 欄目 | 內容 |
|------|------|
| ⭐ Top 5 | 抗栓精準化＋右心／EP／代謝機轉 |
| 🫀 TAVI | RCT 外推 × 小瓣環 × AI 規劃 |
| 🔧 TEER | 成功再定義 × ePVS × 腫瘤病人 |
| 📚 Honorable | LAAO/DOAC、RWS、tenecteplase ICH、LQT2、SWEDEPAD、EV-ICD、低壓差 AS |
| 🔬 Cases | 結構／冠脈介入 × 5 |

---

<!-- _class: divider -->
# ⭐ Top 5 Picks
## 抗栓精準化 × 右心／EP／代謝機轉

---

# ⭐ Top 5 Picks 總覽

| # | 研究 | 期刊 | 方向 | 關鍵數字 |
|---|------|------|------|----------|
| 1 | SMART-CHOICE 3 性別分層 | *EuroIntervention* | ✅ | 女 DHR 0.45、男 0.77；交互作用 P=0.288 |
| 2 | FFR 導引 NSTE-ACS（5 RCT） | *EuroIntervention* | ✅ | NSTE-ACS HR 0.86、CCS 0.78；P-int 0.792 |
| 3 | Sotatercept 右心力學 | *Circulation* | 💡 | RV 自由壁應變 +6.2%；耦合保留 |
| 4 | 星狀神經節阻斷降 POAF | *JACC Clin EP* | ✅ | 18.5% vs 44.4%；OR 0.288，P=0.007 |
| 5 | SELECT 中介分析 | *Eur Heart J* | 💡 | 腰圍中介 64%、hsCRP 42%（CI 極寬） |

> **Pearl**：本週關鍵字＝**精準化**與**真實世界**。抗血小板依性別／情境精準（clopidogrel 單方男女一致、FFR 安全減 PCI），右心「別只看 TAPSE」，semaglutide 保護超越減重。

---

# ⭐ Pick 1｜SMART-CHOICE 3 性別分層
## [clopidogrel vs aspirin 單方 · DOI](https://doi.org/10.4244/EIJ-D-26-00332)

- **設計**：SMART-CHOICE 3 RCT 性別分層子研究；高再發缺血風險 PCI 後單一抗血小板維持
- **族群**：南韓 5,506 人（女 1,002、男 4,504）
- **主要終點**：全因死亡／MI／中風複合

| 族群 | clopidogrel vs aspirin | adjHR |
|------|------------------------|-------|
| 女性 | 4.3% vs 9.4% | **0.45（0.24–0.85）** |
| 男性 | 4.4% vs 6.0% | 0.77（0.56–1.07） |
| 交互作用 | — | **P=0.288** |

> **臨床**：高風險 PCI 後 clopidogrel 單方效益**不因性別而異**；不必因性別調整策略（留意亞洲 CYP2C19）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAACvAQAAAACj6bPYAAABTUlEQVR42u1XMZKEMAwzR5EyT8hP4GOZgRk+Bj/hCZQUDDrZUG53F1WbIrNxsRpblmwMn85t3/Cfw7fxDDbtaQP201+4f+zj+Zcw/z4D5+hoQ74sfrWHnB1owemp8uo1kEywPIXVQVol5NGrIMnlkOdyjkcVcRkdmxdvn0XTsa9YJmA1K++zeWGZGwk17yFGpuaFxcHc2EPFOsgKS6Dx6L2wfmUIsiSQK8UhiWbVJFy61wWXCbhK+8Jerwt0vGjwIlu3vMC6Y4KRVYXhleS6ZKpmaWWJBVbg5eyfeSnhMpp1A9vHuaQuqyDLGMzMbX0MfmmvS8wlxEk/mFyh7bl07dPr8OhD47HPJKkFW+gjq+YlOzaeuq2ANO4UZ2SpEYnnhuSdw1OLaKmkUnxehjNoIH3TohUgcWKrtvXZ6LE0nrg0G97laKbh8vtp2CT8C5VNBBrzNFyGAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# ⭐ Pick 2｜FFR 導引 NSTE-ACS
## [5 RCT 個體資料統合 · DOI](https://doi.org/10.4244/EIJ-D-26-00055)

- **設計**：5 項 FFR vs 攝影導引 PCI 之 RCT 個體病人資料統合，依冠心症型態分層
- **族群**：2,493 人（CCS 1,316、NSTE-ACS 1,177）
- **主要終點**：1 年 MACE

| 族群 | FFR 導引 HR |
|------|-------------|
| NSTE-ACS | 0.86（0.63–1.18） |
| CCS | 0.78（0.58–1.05） |
| 交互作用 | **P=0.792** |

> **臨床**：FFR 導引在 NSTE-ACS 與 CCS 效益一致，被 defer 病灶未增風險 → **安全減少不必要 PCI**（罪犯處理後再評估非罪犯血管較穩妥）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAACvAQAAAACj6bPYAAABTElEQVR42u1XO66DMBAcHoVLH8E3CReLBFIuBjfhCJQukDeza8p0eUwVF1bsIqPd+ayBfVoNv+uvrxu4HhgtbWZ79ZO1P3xc/3LNv89mdTqeSGYn6kTc+yGXADIWOO+V9WogH/ksvbE6SLCx2zGqINnTkI+RUA2Xodj8YoG+KRR7mQXF0cp1vL2xXttocA3BZSuQTxcrBpM19mV1OEazFb7l++VDnbLKYw5IotEu90PODDxbEFx66hWBYveQqXd3Z8ArYn0plcoxDKwX0yFIHzKY1h54QFrzKaiSigV1Gk6RcNkwW3JrwLmkLwWKtaUQjb/WCHgGrSAK2E4vcHJzNgWXbGxkXfhDkrHXJKE1tvBHls3Lsx91r4LJCY1SyWURvX1QUuulPjWQFGuflz1yNe9Ybj40aRfZax0+NBk8sakUax7rEi5/n4a3XL8BIwMBbVB4i7EAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# ⭐ Pick 3｜Sotatercept 與肺高壓右心
## [運動血流動力學研究 · DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.081334)

- **設計**：肺動脈高壓病人，休息＋運動同步超音波＋侵入壓力；治療 24 週前後
- **族群**：30 人（70% 女性）

- PA 後負荷 (Ea) ↓；**RV 收縮力 (Ees) 依後負荷等比 ↓**，但**RV-PA 耦合保留**（差 +0.08，P=0.42）
- 瓣環指標（TAPSE、S′）↓，但 **RV 自由壁應變 +6.2%（+4.5～+7.8）**、FAC ↑、右房功能改善

> **臨床**：收縮力下降在此屬「能量上有利」的重塑，非惡化 → 評估肺高壓右心**別只看 TAPSE**，看 load-independent 指標與變形／耦合。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQAAAAAXBJgHAAABqklEQVR42u1YsY3DMAyk34VKj6BNnMUCWEAWszfRCCpVCOEfSeO7dI9TExeKHRU6k7zj0aIfrirfHeLOW3Dt8sx9l6PKogXPm9Yf+XT97w4QbKr9YXDegIGfl9p/VARFgKDkdOF42bdXxUJH4FlY2lr7PASrpQJ3MgMB6mDHXbI6SO+NXwfOBbx5vxc6FzRogLtTDgUbb55Ss1C7QAqQBckS+eDGoElOJ7Lv9adXQyDYWRjSEXs/HJrYVjVloCIoRoOjOiWDC2QEzbkABpgepAuyRI8BEgAaVNTkyFAk1aTkGDxDAKIzWQy8LLiq7DD6o7kw3nFhaqL3Ixx6GQ1OE8aFnIXVrYG3pxrCSHYobo/AQWuLtoxM5oJpsRc/YAxjoxslciVmWIMRHSKdIUvkSoQA+JubNk3IgllTsRLAuSbIJg8LHUFyTbwTMLKyK9G5MKw5jFCkPsMjuV0Nl6ax8H2iwq0f6jDYehAzE7L/R0R2HdwJMF9Sog7QHPhTWyTA/ZoPcRPmRhtbNp8bi/DdeszOEEYYNHuk+4PbJ4IBEGR4ViWz8fsVZ/7OLz5cwJbOQldrAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# ⭐ Pick 4｜星狀神經節阻斷降 CABG 後 AF
## [RCT · DOI](https://doi.org/10.1016/j.jacep.2026.07.006)

- **設計**：體外循環 CABG 病人隨機接受預先左側星狀神經節阻斷 (SGB) 或對照
- **族群**：124 人；主要終點＝術後 5 天內 POAF

| 組別 | POAF 發生率 |
|------|-------------|
| SGB | **18.5%** |
| 對照 | 44.4% |
| OR | **0.288（0.106–0.731），P=0.007** |

- 伴隨 CRP／IL-6／hs-cTnT／CK-MB 下降、住院縮短；無糖尿病者效益更明顯

> **臨床**：交感是 POAF 可介入標的；預先 SGB 近乎減半 POAF（單中心小樣本，待大型試驗；留意氣胸／Horner 風險）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQAAAAAXBJgHAAABqklEQVR42u1YMY7DMAxjr4PHPME/aT4WIAHyseQnfkJGD0FUUk7Hbgd5qQchhQfLEknRhX1ZBb+dwJ0LXK8WJqTdFn4OVv7wbf3vDjMYzOp4zMW2YbUWruAMFtTXcMIPr6OtBa8eGVhJ+4HMzvTJYLQlOwQqhg4ZEAcCIb9OQTYeB04D3rzeIZwLvi5MmWx8mhrQeBqYwcHDgWdJ5AIDkINxYMdsPPzM6WINGEiILbgLZ+NCfTA4LCrCM2AhHAIL2AX2Y7dgPch4UJWdC1AhUiwS78avliQFCiW6C7r+rYTMgFxAdBcoBbbz+tCAxChNjM2ASMz14w9ISVbDomswl0RZgp/LATnlFF2DRdef7ZPLbDXcIxUdbqRkc2nRmqjp3MRI05lINItWZTojP1w4MPcH0U6V80gOhXOBXfBqBDsU0cBlmBnw96iSBKuyd19ipNr7yyHaoTSPJCJSmxyEqYtPPDmYyQrXRBEi3Cv7iNZgdnnYOrwXBMerWTUgdXm1SZbgcIyfTK0GUHiSknpQ93kzZZqTWUgMfy84F6RDjj/vQvh0/v2L03vnDRoHsdkRPrmUAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# ⭐ Pick 5｜SELECT 中介分析
## [semaglutide 降 MACE 機轉 · DOI](https://doi.org/10.1093/eurheartj/ehag524)

- **設計**：SELECT 中介分析（counterfactual 法）；探討 semaglutide 降 MACE 20% 之中介
- **族群**：已知 CVD、BMI≥27、無糖尿病成人

| 候選中介 | 點估計中介% |
|----------|-------------|
| 腰圍 | 64.0%（CI 極寬） |
| hsCRP | 42.1% |
| 合併（多變量） | **31.4%（−30.1～143.6）** |

> **臨床**：MACE 效益**無法以已知危險因子完全解釋** → GLP-1 心血管保護是**超越減重的類效應**，仍有未知機轉（中介估計 CI 極寬，屬「機轉未明」）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAACvAQAAAACj6bPYAAABS0lEQVR42u1XMZKDQAxTLgUlT9ifwMeYgRk+Rn6yT6CkYHAkw3Xp7lAVFzvBRYQtS14Qn+LAN/3n9AFG10ZFv45101McP/gY/5Lm37cRW78++QKC7CPq/ZATto5Hs2DgLzw9kKyy4rF6IcdAH3M1QZJLjk+AaOHh8pxYFajDMbFX5AzNv9q5u7FzbA9Bot1LvEjo/VVOpTkwlIQk+H5/YyUNSJevdWCVq2FiqYomuwsezIzhEMklybOxDpGwnbTXnKFC8B2WiRWXlORw7hSD4RUerO11ivN+XYYcXSG0auEyODncW2N2t6QpGMYnaSzNcu0Uh/sgFtlrygUGLmUFm3QJeR1Ur2WTHHJ0XUTyDUz7ki4A1evRZd7w5OipD9Xrufug+Lg8IUXokgW6bnhdGh43Z5PWZ+GSNPKYoK+EME5sFgiH+3w/DW9IvwGXWQXEfWFO9QAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## RCT 外推 × 小瓣環 × AI 規劃

---

# 🫀 TAVI #1｜DEDICATE 外推真實世界
## [TAVR vs SAVR 低中風險 · DOI](https://doi.org/10.1016/j.jtcvs.2026.09.009)

- **設計**：以荷蘭全國登錄檢驗 DEDICATE（低中風險 TAVR vs SAVR）之可外推性；PS 配對＋加權
- **族群**：SAVR 登錄 3,389；試驗 1,211（TAVR 654、SAVR 557）

- 試驗 TAVR vs 登錄 SAVR：1 年死亡 **HR 0.46（0.24–0.87）**
- 重新加權貼近真實族群後：**TAVR 絕對死亡下降由 ARR 3.7% → 2.2%**；對中風相對效益**不易複製**

> **臨床**：TAVR 相對存活優勢仍在、**絕對獲益在真實世界縮小** → 跟低中風險病人談時**別直接引用試驗絕對數字**。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQAAAAAXBJgHAAABoElEQVR42u1YMY6EMAw0R0HJE/IT8jEkkPgY/CRPSJkCMTt29q7b7mQ3myICUsSxZ8YTBB9Gke+K48ojHMu8c5JVpgt8khnlRz6N/11hBDPQlvkoMmBPTeYD+s01gl0sgumUsbQBjGWJiACl8S2xMlERsACZm+OcAyIgDnJdUxs44YI/DjoXjtLekzsXbDwKwlwlTZoS46ljBFUZwIkvIxgBceCsB7IpEVce3yJQQpy+VSD+KEa37nugs2JxRyJzf3NfMRwYJZ1xABnqBvmT5skXiTy+2KG57Z4kMyDnKigX+smvakjc4FyFR7oSKhuJyayaeDnrwcq+QEqaNNMkjN6KpHJoosDGrKO660Hvjb9yyERsaP59gZq4wRwKedn7pTcXiAMQhHd6swLuObBSSG+LB9ydqroC4oBixB4V0plGbQS3YZJVUKPk7ZVvseObOyQi2KiAEI9kgmxEnM4An9htyqibm1kM8cq46mo+scRoonRh7DgIiCATeqpDMDgG5YCX1n5vRAgONPdQw2yYdPYHxgW9rDAHW0gVvn9x4ldeauWqL35xkYQAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# 🫀 TAVI #2｜小主動脈瓣環（SCOPE I 事後）
## [長期臨床＋QoL · DOI](https://doi.org/10.1007/s00392-026-03025-y)

- **設計**：SCOPE I 事後分析；依 CT 瓣環面積 ≤430 / >430 mm² 分組
- **族群**：732 人（小瓣環 44.1%）

- 儘管壓差較高、PPM 較多，**3 年死亡、心衰住院、KCCQ、「存活且健康良好」皆無差異**（OR 0.95）
- 探索性：**小瓣環＋球擴瓣 (BEV) 者結果較差**（RR 0.59，交互作用 P=0.004）

> **臨床**：小瓣環 TAVR 長期存活與 QoL 與大瓣環相當；**小瓣環可個體化傾向 SEV / supra-annular**（探索性，待前瞻驗證）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAACvAQAAAACj6bPYAAABVklEQVR42u1XMY7DMAxTLkNGP0E/ST4WIAH8sfQneULGDEFY0i46dbtaUz0YrYcSFEVRNXw6t/2e//18G8+EjHPC5ae+4f6zj+crz/z5BKId5sPjWISLvT3kaudos50dafNTHwW57MNGtEhI81LdIEiVM12GzaK01D2mzJrqiujYapaUgS29vdNeS/oSGHAsYtk3h8Qxiyp7SKPALEVouewCAkcBTTIFFFYE8aiCsne7Y/b2LGfXBy+jgHVuryULy5pq1pWxPgZoybNbh9U5YzNENcAktCQ7RyyLXS4PaB+XLzXWzYO07HdqedmA6sscMNYvTgGls7SkXTIikoQsVyuQvNprWViO1Zy95tAalCRCY7PWLAvJS214jGgT3x5hW8FZQ0T7QczuQ260ZIyWFTKtzoiedVkUS7NBliyZErStl+XuZZegDQ81RNhDGSG+/P01/PbzE74+C51W0TwtAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# 🫀 TAVI #3｜TAVI-TEC：AI 術前 CT 規劃
## [自動化規劃工具 · DOI](https://doi.org/10.1007/s12928-026-01356-1)

- **設計**：全自動 AI 框架，對 S3U 之 TAVI 前 CTA 做分割、鈣化、地標、瓣環平面與瓣膜尺寸預測

| 指標 | 表現 |
|------|------|
| 每例量測時間 | 2–6 分鐘 |
| 瓣環面積一致性 | CCC 0.934、ICC 0.935 |
| 瓣膜尺寸預測準確率 | **77.1%（70.1–83.9%）** |

> **臨床**：AI 可加速並標準化 TAVI 術前 CT 規劃、降低變異；尚限單一瓣膜平台、尺寸預測仍有 ~23% 不一致（多為相鄰尺寸），為輔助非取代人工。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAACvAQAAAACj6bPYAAABVklEQVR42u1XO7KDMBBbPwqXHGFvQi7GDMxwseQmHIHShYd9kj28Kt0LquLCQ7ZAaD9axeLdOe0b/nf4NJzHMezxHKsV/orzx96ej4Tx+jGiPGIj5Man2O+HXK2QZZlsCVyDCJJZbonVQYJlfnWqCkjUcro6R1NL3tO4gSAvRcf+nZKO4ZqduxNbHSwj8nMMFFQAGeCWI1anHgSuRVDL2YuRYBxGXPP7a7k2qntu42LjKoG01HPartkUiaXwOFQAOdW0T6tlxXDaQI0VzCUz+YpqmQVFZHbJXCYMSZNXjEt1ifqQZVuaaCTBXJKlQV7RSEhsAvj9LIHGSYGiL8EvEBgRaF3qqofEgm9IankCyJoBogRJ9iWNyLU0q2tcgS07ltfav0DkfShB7FjslJBA0k9mEHSGXMTSaA3YrCqHx5XVhKckgeB1h9c2WI/MLnN437+Gnwz/AthK/kmTcGiKAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 成功再定義 × ePVS × 腫瘤病人

---

# 🔧 TEER #1｜重新定義 M-TEER 的「成功」
## [解剖 vs 生理 · DOI](https://doi.org/10.1002/ccd.70901)

- **形式**：觀點／回顧——傳統以解剖終點（殘餘 MR、壓差）定義成功，是否足夠？

- 解剖與生理反應不一定一致；**術中 LAP 反應與殘餘 MR「不匹配」與較差預後相關**
- 術中平均 LAP 下降在**退化性 MR** 與較佳預後相關、**功能性 MR 則否**（MR 病因很重要）
- 單次 LAP 受左房順應性／充盈壓／容積／麻醉影響，**不應視為成功的絕對指標**

> **臨床**：M-TEER 成功的未來在**整合解剖＋血流動力學**；留意退化性 MR 的術中 LAP 反應（尚無明確生理目標，待 RCT）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAACvAQAAAACj6bPYAAABWklEQVR42u1Xu62EMBBcngOHlOBOoDEkW6IxrhOXQOgAsW/GoBdd9o6JzoHl2+BG6/l4MX+3TvuW/10+DWveQ/XNcm385eePvV0fKePvR/c2jSXZZMHb7F6fhyzWJpziy1eAW1BBZt5yEELOXhK4tCSCBJfzvpi/9izikvs0rrX1TaHYyyzjkZqNf97RmATge65wqKXnIVc2VixSSL7BoYKLrUgBNDgggigfV8gHYg01Egy42RVdgkv3uFFDg8Ak7muNmy08MWjHQxHrdGPmSxLQKjZB4KWu2G7O3rQiCnidzNgFkLuiS+oFaDaAS0RQeZ7L/jDvOFFDOOWqSJ/oly9X+FKSsSu5RNAankpTXOw9dgW/3y3LksCz2Y+by0niyz4V9OGOlqRdRLMPWy2sLCaCPAxiPXoUVF2XfLdYSiIuDcoBjfFUDJV9wrs+R+gUziUKX34/DT9d/gWBswmc5iS3FQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# 🔧 TEER #2｜術前 ePVS 預測 M-TEER 死亡
## [估計血漿容積 · DOI](https://doi.org/10.1007/s00392-026-03021-2)

- **設計**：前瞻 311 人；以 Hakim 公式（血比容、體重、性別）算 ePVS

| 指標 | 1 年死亡 | 5 年死亡 |
|------|----------|----------|
| ePVS 高 | 14.4% | 63.0% |
| ePVS 低 | 4.7% | 26.0% |

- 校正後 ePVS（HR 2.38）與 NT-proBNP（HR 4.30）皆獨立；**兩者皆高 HR 14.27**

> **臨床**：ePVS 幾乎零成本（血比容＋體重），可獨立預測 M-TEER 死亡、與 NT-proBNP 合併再分層 → 高 ePVS 者術前積極 decongestion。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAACvAQAAAACj6bPYAAABVElEQVR42u1XMZKDMBATR0HJE/wT+BgzMJOPcT/xE1K6YNhINunS3aEqLnZiF9nRrqRdEJ/Oie/zn59P8MxxIPbxQNEtzh98PP/yzL8fI8ocWxr28aFfke9PuaHMzzXKhBp6V0pchfWlZDmH32efTSnZy4ltrFdPLxWZMpcaHIy9ziOChX1r5+7CHgkTFolEDXWkZBjUUMxEybBa6IOqSyolQcHQy0yUj0wOUS4Yt3Q/SmaTFbwLuxgYS1h78zrW1EGfiCPJczRW+prXgJKS3NnBSla+LMmBUvOyQs2DrrenpJnT0ZForyRSZ9GlpIHl4m6n/cCjy7qDrCH/MywinFtiLNtIlODVMkmoD/mBpjPrbJmXZE5bezg0j+TZCiBJVoCWpbKtW4n06ZXXMaI3VJSkLS0IQDKhbMtdI5JpW6c05EOlMxjeteEpUXtx2Pr30/CG5xeZB/ycvxj9pwAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# 🔧 TEER #3｜合併癌症的 M-TEER
## [統合分析 · DOI](https://doi.org/10.1007/s11357-026-02539-7)

- **設計**：系統回顧＋統合（8 研究，7 項 M-TEER；癌症 1,522、對照 4,716）

- **長期全因死亡較高**：HR 1.72（1.03–2.90，I²=74.8%）
- **30 天死亡與程序成功兩組相當**；配對世代長期死亡差異不顯著

> **臨床**：合併癌症者 M-TEER**做得成、短期安全，但長期存活受癌症本身牽動** → 與腫瘤科共同決策、以症狀緩解為目標選病人（全觀察性，異質性高）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAACvAQAAAACj6bPYAAABT0lEQVR42u1XMZKDQAxTjoJyn7A/gY8xw83wMfgJT9iSgsGRdjNXpbugKi4y4CIaWZZtEO/iwjf97/QFxsjnY4wzH3qL6wdv4yNp/n0SWun2fiuzcGO/H/IXx4A5YhPVAZ0JMi17vxLNCCm0sSCbIFXOdIKd49JSvypsra6lY19mYWGR/rxzv5YYy4Q+yiyW3e2QAoqNkHUUgFQdWnLmyCRbUdsaCsvYWVNZUr37KFO+v7CTtOzaKOBrZ2EZa1oCdawPBi3VPhj0tMUSoupgGT2dktWxqFQNA0/DHCBBZIuWF9iiK2a2bfPl4hnr0Dp5UMsqqGPg9aJKSPnSouWyQ5O1+hLi69kk6WwdW3eZZV9Wfyh0FYTpKmD7tCWSTphun2ZJj5avCy+aL7lT4IIkt5UlViqbrvUptzNvwP37sl14vCerOXUfWDbJ99Pw4+knQX0E9JFQmI8AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

# 📚 Honorable Mentions（1/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **LAAO vs DOAC 網絡統合** | *JACC Adv* | 67,693 人；療效 HR 1.02、大出血 HR 0.98——**LAAO 未顯優越** | [DOI](https://doi.org/10.1016/j.jacadv.2026.103269) |
| **Radial Wall Strain（TARGET）** | *EuroInterv* | AI 由攝影算 RWS≥13% **獨立預測 5 年非標的血管事件（adjHR 4.82）** | [DOI](https://doi.org/10.4244/EIJ-D-26-00126) |
| **Tenecteplase 溶栓後 ICH 模型** | *Eur Heart J* | 6 RCT、15,954 人；女性 +49%、低體重、高齡×高劑量→**高齡減量、溶栓前控壓** | [DOI](https://doi.org/10.1093/eurheartj/ehag754) |
| **LQT2 lumacaftor（phase 2）** | *Eur Heart J* | 16 人 KCNH2 trafficking 缺陷；QTc **−31 ms**——變異導向精準治療 | [DOI](https://doi.org/10.1093/eurheartj/ehag753) |

---

# 📚 Honorable Mentions（2/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **SWEDEPAD-1（安全警訊）** | *Circ CV Interv* | 重症肢缺血：paclitaxel 塗層**未改善保肢、3 個月大截肢反增（adjHR 1.43）** | [DOI](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016977) |
| **EV-ICD 真實世界（Enlighten）** | *Circulation* | 787 人；1 年免主要併發症 89.1%、電擊成功 100%、ATP 74.2% | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.080942) |
| **低壓差 AS 新流量準則** | *Circ CV Imaging* | 不確定 AS 43%→9%；重分類重度 AS 換瓣獲益（HR 0.50） | [DOI](https://doi.org/10.1161/CIRCIMAGING.125.018621) |

> ⚠️ **SWEDEPAD-1 重點**：冠脈的 DCB 經驗**不能直接外推到周邊重症肢缺血**——早期截肢風險反升。

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構／冠脈介入 × 5

---

# 🔬 Case #1｜M-TEER 急性右向左分流救援
## [平行中隔球囊阻塞 · DOI](https://doi.org/10.1016/j.jaccas.2026.110445)

- 78 歲男性，重度 MR＋TR 接受 M-TEER；大口徑經中隔穿刺後**立即嚴重低血氧**（IASD 急性右向左分流）
- 於經中隔鞘**平行處充起順應性球囊暫封中隔** → 恢復氧合、順利部署 PASCAL、術末關閉中隔

> **學習點**：高風險（右心壓高／順應性差）者術前預期右向左分流；**平行球囊暫封**可在不另穿刺、不放棄通路下救援。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQAAAAAXBJgHAAABrUlEQVR42u1YsY3DMBBj3oXKjKBNnMUMOEAWczbRCCldGLknT/oy3YNuosKAo0L0HcmjgviwGr47xp03uGassd/iQDzjzvdrtB98Wv+7QwTX4OGvBXysEdv1EfrNiuCOfcbU9strUiEeDfMZCFgDYKl8PQeBvjwpoC74EZAHM1BBJlay08+D1AK/fB8PuxZyqRVlIx1ZiKFTI4LXUvnRR6cAYbAfXh4QAcobFOKcVkAExOJFwMOBtZWnqkFOUpdmLRysAY+ETKFkK55mHqDSDpfKwyMgYyxmJob41zV41MKmNHcXSAGNRRVijdSCvQsLZzJbkZLEJe41vAhSiIoGe3ZBk8mMQKxjDdaW1pySdHeBZZcXtxyQeoTdDzgSpIDY5AdihNkTRyRh9+kM6JNp88/Gp0KqogHD4hTupMpsRg2KB9QllA/MCUWuLE+snZOX/mpOaa37wdzHE+D3g+hR7TbGUyun5MRDMnhkTMmo5s/Kui79BTS7H+i+IP4lJ1WScsatTUFdkqQV2CfTuDONsdhhnHJnWkZC0bA23xeGEDMwT70L5QQ/+P6/c+rOL4VDtNpf5PgvAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# 🔬 Case #2｜IVL 氣球嵌頓於右冠狀動脈
## [外科取出的教訓 · DOI](https://doi.org/10.1016/j.jaccas.2026.110448)

- 72 歲男性 NSTEMI，右冠狀動脈嚴重鈣化以 IVL 處理；**治療後氣球無法退出**
- 多導絲、平行球囊、snare 皆失敗 → 緊急 CABG；外科亦無法取出，於開口處切斷留置

> **學習點**：IVL **通過遇阻力應重評鈣化修飾策略、勿硬推**；嵌頓解套失敗率高，及早外科備援；鈣化預處理順序＋影像確認可預防。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQAAAAAXBJgHAAABsUlEQVR42u1YMY6EMBAzl2LKfUJ+Ah9DAmk/tvyEJ1BSoJ2zJ1y53WnSbKRFYlPEiT0eB/iHseM7kzjzBseIxc/JL/jmK98fvv/g0/jfGSJ4eFsc07G4vx5P13+pCFacI5f07SjC8twxdkCAGbYdc+VrHwSTr1UPiIV8BNTBCFTq75Jk83UQtcCdn/cjvRZiiH17oTimvzpNRED9xaYpgRWEQT6SdYC52pvbFwsuUiqx5CLg4sCyY9BpUJM4s3VwwST+ZgqqRts8txpZAYNfFQPR8CCKW7IS6UNckj4kGOZH2ZNZoBKjL8iWFo9aSGZBm2ZTglhggxzoz56sA5TWnXkQZEGySEYg1cWS4crRINNZIAFKBSFH5QNPVyJN0I+FrtxCQg9P3NWPeAbHjNaZchF4S0ZX65LnREfKTqq4l2RzmJUUViQnFErATRldeY2mQB1Ysg7uvtACc/TGfD/wO67KCrR965ET+bNQomwpSiM9Ky+KKXMLaNl+0O4LV1VCUV4DrMutjRFxU0hAfme6zyD0F1Xhne5Mur3LGWRQyfeFqAV5MWGUxoJ18IPv952uM78GRLuTQoFW4AAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# 🔬 Case #3｜TAVI 後獲得性心內交通
## [經導管關閉 · DOI](https://doi.org/10.1002/ccd.70914)

- 4 名 TAVI 後**醫源性心內交通**（VSD、主動脈—右心室瘻、根部損傷）
- 機轉：嚴重瓣環／瓣環下鈣化、積極後擴張、valve-in-valve 框架斷裂
- TTE＋TEE＋CT 多模態定位；heart team 後**全數經導管關閉成功**，追蹤 8 月–2.5 年穩定

> **學習點**：嚴重鈣化／valve-in-valve 是危險因子；**多模態影像**為核心；**經導管關閉是安全有效第一線**，免高風險再手術。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAK8AAACvAQAAAACj6bPYAAABVUlEQVR42u1XMY6EMBAbjoIyT8hP4GMrgcTHdn+SJ1CmQMzZE3TVdrdxtSkiSIE1sccezN+ty77H/z6+DGtxLzb4mSvf/Pqxt+sjx/h8cq+L746XkU9e+kNuVud05ukF3DrbKII0y3U4xiKERJX+JK4GElzOaYeYjlXEJXdAlhqbQrGtWdKGO01/vdOfS1ugHF4sqxwlkFDO6rCCLZul/lw6jcegWIsmWQQX2xbECiuAdofjkftD7iWuE2grCe3PpUdZhu3lTbYKLmEALPCFAqenRrH57o90MsZOAZfRGtEpjyzhMvrSPQoM8F1g63BWcOmUrTtDU1HlRD9oET0IuER4FVtuey2NVVWSQDl3lknyksqhYjmSKBTrMWSRRoo1afIyxi3U27jMqnHLKo1naoRKIB0RHc0Z9Uqm9ZNJcvKK++dlm/CoU4YIvH0XTQXfX8MPH/8CQwsQO7FFNlgAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# 🔬 Case #4｜冠狀竇 Reducer 腋靜脈救援
## [頸靜脈失敗時 · DOI](https://doi.org/10.1016/j.jaccas.2026.110453)

- 難治性心絞痛擬植入冠狀竇 Reducer (CSR)；**右內頸靜脈路徑因軸向不佳失敗**
- 改採**右腋靜脈＋35° 尾側投影**取得有利軌跡，mother-and-child 推送成功部署 CSR

> **學習點**：CSR 通路解剖決定成敗；頸靜脈不利時**腋靜脈可替代**；腋靜脈穿刺避開肺野、排除誤入動脈；mother-and-child 勿過度前推（穿孔風險）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQAAAAAXBJgHAAABrElEQVR42u1YsY3DMBC7vAuVGUGbJIsZiIEsFm+iEVyqMJ5P6vz4Kt2DbqLCiKNCzB2PpBJ4s1p8dow738F1uwL9jj2wYuH7Fe0r3q3/3SGCPHwhyu0BvK5P6DsrgiX6LaYWl20SlmdTSfwIIvplmytfz0HALtQe/KQu+BGQB7ek417JTj8P8vBn68fDPgtjqfuFWGrcf+fUiID844/eI2G8BMPMg5ij8HCoFVBTKuno7QIPV+PHNMaYSzMPtlEDtKyGprGsZh5MrYsHKgSGMBYzEzF0CJwF6kE5ALmZ2C8YPHjkLNi7MAuGnInuzMdS4UXAwzMaiAxVc9nMCMQ6rGxAyKLLypE0d4HeSC0mAilDUz6AWw/YeE4AayB3Zg3smihB7qpBESfTmcyqTAnKVLBiYJkQdj2QJ++KarOSwhLmhCJ3phssyQiqcujVnNI0AUgtHt7o1wNkVLtnNYZDnJATOYji5AiLGgh7VubjL6DZ9UD3BUqBIntVXI1yxq1NfqRzKQV2ZzruTLv8iL6gpHDOnenRJM0oMmvzfeEYxKh5gY4TkurnX5zTd34ARiC1dEcna5MAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# 🔬 Case #5｜年輕人復發多發黏液瘤＋栓塞
## [揭開 Carney complex · DOI](https://doi.org/10.1016/j.jaccas.2026.110444)

- 19 歲女性以**急性缺血性中風**表現；曾切除左房黏液瘤、復發並再發栓塞
- 多模態影像見**復發性左心室黏液瘤**＋栓塞性心肌梗塞；依復發黏液瘤＋雀斑樣色素＋家族史診斷 **CNC**
- 手術移除 20 餘顆腫瘤、完全切除，3 個月無復發

> **學習點**：年輕、心室、復發、多發黏液瘤 → 評估 **Carney complex**（伴雀斑／家族史）；多模態影像界定侵犯與無聲栓塞；終身多科追蹤＋家族篩檢。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQAAAAAXBJgHAAABq0lEQVR42u1YMZKDMAwUR+GSJ/gn8DFmYIaPwU/8BEoXnuhWEpcu3c26iQtPAkVW1u5qHdEPq8j3DfHNS7BmGTWdU8sy6I7vk5Yf+bT+9w0QTKp10UPTazrikz2jItilLvcqdQaCdOlRZO6AwCo/gUB7IZhlK0mtFYDBRwAegInFyjcK8HngWkDl9dnoWnivZOpEFx6dEhHc2Adset2jnUETchdUW9YzbGnNIMOe6UxsIlAjtHBvdgZaIE7uGeyo/N40rBmf2GrUe/VpkL37wLJKYqtxCzs0OmY88RnFRTDaj4/e/bc3cZkIEl4ov6J8UEBwEAsZQcuo/Ok+jmSl+wEa4MMhGRZQgO4H5sDe/eokhEFJHZQ9mVySyYRoPKBPppABIqJgLEIGTdhqROMjtArmQpUO+cASMjISmIjN0xLdD1RDAYsfhAFi+8Gewwl9OTFPfkayBoQd+nSeO+RE6/4ZQ+lg54PIyhBiMgRuBV3uCwhKVWIuiCS2FhwBKh/Mloa/qEa/M9lgjnvjzlej5xKJy6NnFTYC220uYCIeJUz60i53pu//O93e/AJ1erOA6ZD2/gAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# 💎 Take Home
## 精準化 × 真實世界落地

**抗栓精準化** ✅ clopidogrel 單方男女一致 · FFR 安全減 NSTE-ACS 的 PCI
**機轉再解讀** 💡 右心別只看 TAPSE · GLP-1 超越減重
**結構真實世界** 🫀 TAVR 絕對獲益縮小 · M-TEER 成功要整合生理

---

# 💎 本週 Take Home Message（1/2）

1. **SMART-CHOICE 3 ✅**：高風險 PCI 後 clopidogrel 單方，男女效益一致（女 HR 0.45、男 0.77，交互作用 P=0.288）→ 不因性別調整。

2. **FFR 導引 NSTE-ACS ✅**：NSTE-ACS 與 CCS 效益一致（HR 0.86 vs 0.78），defer 病灶未增風險 → 安全減少不必要 PCI。

3. **Sotatercept 💡**：右心收縮力等比下調、耦合保留、自由壁應變 +6.2% → 評估右心別只看 TAPSE。

4. **星狀神經節阻斷 ✅**：CABG 前預先 SGB 使 POAF 由 44.4%→18.5%（OR 0.288）→ 交感是可介入標的。

---

# 💎 本週 Take Home Message（2/2）

5. **SELECT 中介分析 💡**：semaglutide 降 MACE 無法以已知因子完全解釋（合併中介 ~31%）→ 保護超越減重。

6. **結構性介入 🫀**：DEDICATE 外推——TAVR 相對存活優勢仍在、**絕對獲益縮小**；小瓣環長期與大瓣環相當（BEV 可能較不利）；AI 加速 CT 規劃；**M-TEER 成功應整合解剖＋LAP 反應**；**術前 ePVS 是簡易死亡預測**；TTVI／M-TEER 真實世界採用增。

7. **安全與救援 ⚠️**：**SWEDEPAD-1**——周邊 paclitaxel 塗層在重症肢缺血反增早期截肢（冠脈經驗別外推）；救援技：平行球囊封中隔、IVL 遇阻力別硬推、TAVI 後心內交通經導管關閉、CSR 走腋靜脈、年輕復發心室黏液瘤想到 Carney complex。

---

<!-- _class: small-text -->
# 完整參考文獻（1/2）

**Top 5**
1. Kwon W, et al. SMART-CHOICE 3 sex-stratified. [*EuroIntervention* 2026;22(18):e990-e1000.](https://doi.org/10.4244/EIJ-D-26-00332) PMID 42765401
2. Paolucci L, et al. FFR-guided revascularisation in NSTE-ACS. [*EuroIntervention* 2026;22(18):e970-e977.](https://doi.org/10.4244/EIJ-D-26-00055) PMID 42765399
3. Reddy YNV, et al. Sotatercept & RV mechanics in PAH. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.081334) PMID 42770225
4. Tian Y, et al. Stellate ganglion block & POAF after CABG. [*JACC Clin EP* 2026.](https://doi.org/10.1016/j.jacep.2026.07.006) PMID 42782230
5. Colhoun HM, et al. SELECT mediation analysis. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag524) PMID 42777687

**TAVI**
6. Daeter E, et al. DEDICATE transportability. [*J Thorac Cardiovasc Surg* 2026.](https://doi.org/10.1016/j.jtcvs.2026.09.009) PMID 42772371
7. Cozzi O, et al. Small annulus & TAVR (SCOPE I). [*Clin Res Cardiol* 2026.](https://doi.org/10.1007/s00392-026-03025-y) PMID 42776203
8. Zerillo A, et al. TAVI-TEC AI planning. [*Cardiovasc Interv Ther* 2026.](https://doi.org/10.1007/s12928-026-01356-1) PMID 42786272

**TEER**
9. Vlachakis PK, et al. Defining M-TEER success. [*Catheter Cardiovasc Interv* 2026.](https://doi.org/10.1002/ccd.70901) PMID 42773681
10. Haus M, et al. ePVS & M-TEER mortality. [*Clin Res Cardiol* 2026.](https://doi.org/10.1007/s00392-026-03021-2) PMID 42766123
11. Biondi R, et al. M-TEER in cancer (meta-analysis). [*Geroscience* 2026.](https://doi.org/10.1007/s11357-026-02539-7) PMID 42786380

---

<!-- _class: small-text -->
# 完整參考文獻（2/2）

**Honorable Mentions**
12. Hiruma T, et al. LAAO vs DOAC network meta-analysis. [*JACC Adv* 2026.](https://doi.org/10.1016/j.jacadv.2026.103269) PMID 42777587
13. Huang J, et al. Radial wall strain (TARGET). [*EuroIntervention* 2026;22(18):e978-e989.](https://doi.org/10.4244/EIJ-D-26-00126) PMID 42765400
14. Armstrong PW, et al. Tenecteplase & ICH. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag754) PMID 42766418
15. Crotti L, et al. LQT2 lumacaftor phase 2. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag753) PMID 42771720
16. Sellgren L, et al. SWEDEPAD-1 paclitaxel & CLTI. [*Circ Cardiovasc Interv* 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016977) PMID 42779544
17. Boersma LVA, et al. EV-ICD (Enlighten registry). [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.080942) PMID 42770223
18. Vamvakidou A, et al. Transvalvular flow criteria in low-gradient AS. [*Circ Cardiovasc Imaging* 2026.](https://doi.org/10.1161/CIRCIMAGING.125.018621) PMID 42775464

**Case Reports**
19. Radhakrishna A, et al. Parallel septal balloon during M-TEER. [*JACC Case Rep* 2026:110445.](https://doi.org/10.1016/j.jaccas.2026.110445) PMID 42782237
20. Sharma P, et al. IVL balloon entrapment in RCA. [*JACC Case Rep* 2026:110448.](https://doi.org/10.1016/j.jaccas.2026.110448) PMID 42788913
21. Fontos G, et al. Intracardiac communications after TAVI. [*Catheter Cardiovasc Interv* 2026.](https://doi.org/10.1002/ccd.70914) PMID 42773734
22. Costantino J, et al. CSR via axillary access. [*JACC Case Rep* 2026:110453.](https://doi.org/10.1016/j.jaccas.2026.110453) PMID 42782233
23. Roveda G, et al. Recurrent myxomas & Carney complex. [*JACC Case Rep* 2026:110444.](https://doi.org/10.1016/j.jaccas.2026.110444) PMID 42782238

---

<!-- _class: abbr -->
# 縮寫對照（1/2）

| 縮寫 | 全名 | 中文 |
|------|------|------|
| PCI / CABG | Percutaneous Coronary Intervention / Coronary Artery Bypass Grafting | 經皮冠狀動脈介入／繞道手術 |
| DAPT | Dual Antiplatelet Therapy | 雙重抗血小板治療 |
| FFR | Fractional Flow Reserve | 血流儲備分數 |
| NSTE-ACS / CCS | Non–ST-Elevation ACS / Chronic Coronary Syndrome | 非 ST 上升急性冠心症／慢性冠心症 |
| MACE / MACCE | Major Adverse CV (and Cerebrovascular) Events | 主要不良心血管（腦血管）事件 |
| HR / OR / RR / ARR | Hazard/Odds/Risk Ratio; Absolute Risk Reduction | 風險比／勝算比／相對風險／絕對風險下降 |
| PAH / RV / RA | Pulmonary Arterial Hypertension / Right Ventricle / Atrium | 肺動脈高壓／右心室／右心房 |
| Ees / Ea / TAPSE | End-Systolic / Arterial Elastance; Tricuspid Annular Plane Systolic Excursion | 收縮末／動脈彈性；三尖瓣環收縮位移 |
| POAF / SGB | Postoperative AF / Stellate Ganglion Block | 術後心房顫動／星狀神經節阻斷 |
| GLP-1 / hsCRP | Glucagon-Like Peptide-1 / High-Sensitivity CRP | 類升糖素胜肽-1／高敏 C 反應蛋白 |
| STEMI / TNK / ICH | ST-Elevation MI / Tenecteplase / Intracranial Haemorrhage | ST 上升心梗／替奈普酶／顱內出血 |

---

<!-- _class: abbr -->
# 縮寫對照（2/2）

| 縮寫 | 全名 | 中文 |
|------|------|------|
| TAVI / TAVR / SAVR | Transcatheter / Surgical Aortic Valve Implantation/Replacement | 經導管／外科主動脈瓣植入／置換 |
| BEV / SEV / PPM | Balloon-Expandable / Self-Expanding Valve; Prosthesis-Patient Mismatch | 球擴瓣／自膨脹瓣；瓣膜—病人不匹配 |
| AS / DSE / AVA | Aortic Stenosis / Dobutamine Stress Echo / Aortic Valve Area | 主動脈瓣狹窄／多巴酚丁胺負荷超音波／瓣口面積 |
| TEER / M-TEER / T-TEER | (Mitral/Tricuspid) Transcatheter Edge-to-Edge Repair | （二尖／三尖瓣）經導管緣對緣修復 |
| TTVR / TTVI | Transcatheter Tricuspid Valve Replacement / Intervention | 經導管三尖瓣置換／介入 |
| MR / FMR / LAP | (Functional) Mitral Regurgitation / Left Atrial Pressure | （功能性）二尖瓣逆流／左心房壓 |
| ePVS / NT-proBNP | Estimated Plasma Volume Status / N-Terminal pro-BNP | 估計血漿容積狀態／N 端 B 型利鈉肽前體 |
| LAAO / DOAC / VKA | LA Appendage Occlusion / Direct Oral Anticoagulant / Vit K Antagonist | 左心耳封堵／直接口服抗凝／維生素 K 拮抗劑 |
| EV-ICD / ATP / VT | Extravascular ICD / Antitachycardia Pacing / Ventricular Tachycardia | 血管外去顫器／抗心搏過速起搏／心室頻脈 |
| RWS / IVL / CTO | Radial Wall Strain / Intravascular Lithotripsy / Chronic Total Occlusion | 橈向管壁應變／血管內碎石／慢性完全閉塞 |
| CLTI / IASD / CSR / CNC | Chronic Limb-Threatening Ischemia / Iatrogenic ASD / Coronary Sinus Reducer / Carney Complex | 慢性肢威脅缺血／醫源性心房中隔缺損／冠狀竇 Reducer／Carney 複合症 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
Weekly Cardiovascular Journal Review｜2026-09-19 ~ 2026-09-26

> 本講義為讀書會共筆之教學整理，僅供醫療專業同仁臨床教學交流參考，不作為個案診療依據。
