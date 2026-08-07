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
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-08-01 ~ 2026-08-08'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-08-01 ~ 2026-08-08

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Top Pick / 案例附 QR Code，可掃描跳轉原文

---

# 🎯 本週主題與固定欄目

## 「裝置與藥物：加了不一定更好——重估除顫器、心房分流與族群差異」

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 結構性主動脈瓣方向
3. 🔧 **TEER Section** — 本週以三尖瓣為主
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — 結構／冠脈介入 × 5
6. 📖 **參考文獻 + 縮寫對照**

---

# ⭐ Top 5 Picks 一覽

| # | 研究 | 期刊 | 方向 | 關鍵數字 |
|---|------|------|------|----------|
| 1 | **PRAGUE-25**（肥胖 AF：消融 vs 生活型態＋AAD） | *JACC Adv* | ✅ 消融佔優 | 無 AF **73% vs 35%** |
| 2 | **DECIDE-CRT**（NICM：CRT-D vs CRT-P） | *Circ HF* | ❌ 中性 | 死亡 **HR 0.90（0.71–1.13）** |
| 3 | **MRA × 種族**（4 試驗 IPD） | *Circ HF* | 💡 無族群差異 | 交互作用 **p=0.34** |
| 4 | **RELIEVE-HF 建模**（心房分流器） | *Circ HF* | 💡 選對病人 | **HFrEF 67% vs HFpEF 21%** 可能獲益 |
| 5 | **2026 ACC 成人疫苗指引** | *JACC* | 📋 指引 | 疫苗＝被低估的 CV 預防 |

> **Pearl of the Week**：「別急著加」——加去顫器、加分流器、因族群調藥，答案都指向**選對病人**才是關鍵。

---

<!-- _class: divider -->
# ⭐ Top 5 Picks
## 逐篇詳解

---

# Pick 1｜PRAGUE-25：肥胖 AF 的節律控制

## [PRAGUE-25 sub-analysis — *JACC Adv* 2026;5(9):103109](https://doi.org/10.1016/j.jacadv.2026.103109)

| 項目 | 內容 |
|------|------|
| **設計** | 隨機試驗 per-protocol 次分析；7 天 Holter 量化 AF 負荷 |
| **族群** | 肥胖（BMI 30–45）陣發／持續性 AF |
| **介入** | 導管消融 (CA) vs 生活型態調整＋抗心律不整藥 (AAD) |
| **結果** | 12 個月**無 AF 73% vs 35%**；生活型態組體重／HbA1c 改善更大 |
| **Take home** | 消融處理心律、生活型態處理代謝——**互補而非二選一** |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABhElEQVR42u2YzW0FMQiEUVwAJbl1l+QCLBGYwat3SS5RlIn0Vqv982XEDh9gi6+PY+/Fny1uy2PsOWIdm8eXedSnfP6wb46/WEy1M1Wn1DyjNAfPfNZUm2FkYIMR9hi7oi2sFsH0iuo/ULvtpHthiYNXWbXlW8grJ/Cq69vLhJdTlwkPzHzhjnTjF0W1q26JWcK2TDvJB03fJgRSXueaFxNS/NBVu5BW1gViGxNNlWAG064BwRnbkCVYlE7j3+8akYlmupXXV4uslqaSrjscTd5WVBcweysF6q+sb8GxeWVTf8gSjH0CMRvbdHkbnVwBiCHFpjBvrdkFSwwgAoI1K2/01YMzjnRXw5yCV2ldFGKTJRh7gwFLILzK/S3n3LJrsEPYt9WRVMtmho4leI88byEyyLF6Vp4dLsdIWg5o2nNZlbPomVe3v2Unw79/t0HE9xPq2uIRbeEejNsIxomM7a74Xs2I9QySyh3j49sRHdtuyGWZAIzVPhjwZa46O7y33H9r8ROm2oihbl2RKAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Pick 2｜DECIDE-CRT：NICM 多加去顫器未見存活優勢

## [DECIDE-CRT — *Circ Heart Fail* 2026](https://doi.org/10.1161/CIRCHEARTFAILURE.126.014213)

| 項目 | 內容 |
|------|------|
| **設計** | 美國 VA 170 家醫院世代（2006–2020），IPTW 加權 |
| **族群** | 非缺血性心肌病 (NICM) 一級預防 CRT；n=3,965 |
| **結果** | 全因死亡校正 **HR 0.90（95% CI 0.71–1.13，p=0.34）**；CRT-D 換機／感染更多 |
| **Take home** | GDMT 時代，**CRT-D vs CRT-P 應個體化**（延續 DANISH）；需 RCT 定論 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABj0lEQVR42u1YQWoEMQwzzQPmSfl6njQPCLiW5Ay9dC9bqA4bliWTXISQJTuRv68dn8v3Lu+oNe4YmfWPzytxFHN/xYv1H5cFbxbqglrwMte+1uBnnXuiLZyDODcBj3uCame0hRCUNrH+aJPSrT0/fdFCt+B2FeDNE2PdyhPmz5+vJ2gVkzQuVVnbm6cSji0U1CgHu/vclNubtXaRVZBM2L5KWNQqcTLLGBOeSoBxdYRhv+S9prpFswAfEOA6QbmBZE8lVGWBWwigEAbti8hdPQHuKjdQlQ2q15PbDVZDPVjQEGS5pll2oZ+hYpcUC4tw5VYIuyeHdDvRXD2B3ReSdz4km/qtXIvE0hMaqm3ybupWfaOGneAc4elg+9QXgyxOQJgq4YyQQKgqA7HGaJ/YHbJfxrFrV8P+sJM3Otq8Zwf1CZp0tDGey2RciF1CDdf+tt9qOs7ymSDS+/Vjnc6WJhbOL0tow8SqIth25m20J8s0o/lO6Hr7OhO6JjXf/paewAEnNfaKZ1+//bzH//3lN/rWmGHl3cn/AAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Pick 3｜MRA × 種族：療效無異質性

## [MRAs and Race in HF (IPD meta) — *Circ Heart Fail* 2026](https://doi.org/10.1161/CIRCHEARTFAILURE.125.014355)

| 項目 | 內容 |
|------|------|
| **設計** | RALES/EMPHASIS-HF/TOPCAT/FINEARTS-HF 個體資料統合 |
| **族群** | n=13,846（黑人 4.2%） |
| **結果** | 主要終點 HR 黑人 **0.87** vs 非黑人 **0.77**，**交互作用 p=0.34**；安全性亦無族群差異 |
| **Take home** | **不應以種族為由減用 MRA**（spironolactone/eplerenone/finerenone） |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABj0lEQVR42u2YwW1DMQxDhXoAj+TVPZIHMKCKpH7QS3tpgfIQI/hI/C8PCkXRjvx+3Xi//N3LE7XGiZFZT/ycia1Y9yN+WP/xsvBWUY/chZe579zArq1jSluchVecl8DjLJTamVZKyC6sPe1KAtf3hj/GuuW/X8A3Iq11K09YXz++nqDFCvOnzIH25qmEtoUN1HKw0/uutd0ABifIy8pUYVNaOACFWpycZRwTlkrgOOgRBhPjdLDVbZUx4LR61k5VNVBkTyVUZwEVY7cIg/bFUnt6wgUex+4Jddmgen1rOzuDAZjSdfVbBlrWE8xULMbZtKWl3yqTUxhtFJ6eoJ5ivmUsR5Ft/RZzgcFGHSdU28krp1X6UqmDdXZNjI9WsyMNB4SnEnS0YWKcqS5DYV1pFcPGYwsQLeRhqoTXOFCXSRvmZ4egD3Sv8Wl8LpNxbSVz6cH4riZbt/k6QaT17ccTGFRt1y7rmyWed5YErGOvNa1cl8zOtI9ulXW3rph8821nxVAspwPnOMZ++76P//uXn2PGlk5jw+9uAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Pick 4｜RELIEVE-HF：心房分流器「選對病人」

## [RELIEVE-HF individual modeling — *Circ Heart Fail* 2026](https://doi.org/10.1161/CIRCHEARTFAILURE.125.014100)

| 項目 | 內容 |
|------|------|
| **背景** | 隨機試驗（n=508）：HFrEF 益、HFpEF 害 |
| **建模** | 37 項基線變項個體化風險模型 |
| **結果** | 估 **HFrEF 67.2% vs HFpEF 21.4%** 可能獲益 |
| **Take home** | 適應症不能只靠 EF——看右心功能、肺血管阻力、血壓等個體輪廓 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABkElEQVR42u1YwW0DMQwTqgFuJK/ukW4AA6pI2od80k8LlI8YQRDbH0KhSFpR79eKz+XvLu/olXdkVX9jexWOYqyv+GH9x2XDG426oTa8qrmumdz2uSfaxpk145qLgPMeKLUzWsJrzCqsPdoB9pIPD3hf3vLf7xZbEWXNW2nCeP34aoIWK8ztpDhQ3jyZQOq2JhSVIe997opWpgDtAkjBDl+0rCdx0stoE5ZMoB1sC4P/0h1seVuwsERkkN5GVxUcvk01QQSA7TbCoHyx1K5eFrQwsFfgk+z1ZAL1djdXYktxMK0tiMrm6h9TjIWdudb2xX8ZZh6hMNWEUL7dQRey4Kq3tF0JAjVhQ7XNYHWiF7PNFHuXqfNKuCbT+I40NAjPLgMwYEMMK5kaCuuKFsDYYiovSAvMrrzdwabUZVSzYf52eHxB7ZbW7zKOaJjDCTVs9fY8cuPIgl4QZT79OMmWIhbOkyWmcb0oL83Eyhlt7f4KzhN80daZfe18y+mobb7dmhB8L5C3mjX56u1nHv/3l9/3Soqry00jVQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Pick 5｜2026 ACC 成人疫苗接種簡明指引

## [Adult Immunizations as Part of CV Care — *JACC* 2026](https://doi.org/10.1016/j.jacc.2026.07.004)

| 項目 | 內容 |
|------|------|
| **性質** | ACC Solution Set 簡明臨床指引 |
| **核心** | 流感／COVID-19／RSV／肺炎鏈球菌納入 CV 照護常規 |
| **證據** | 流感疫苗可降低 CV 事件與死亡（IAMI 等 RCT） |
| **Take home** | 疫苗＝**被低估的 CV 預防工具**；心臟科應主動把關接種狀態 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABQ0lEQVR42u1YwQkDMQwzzQAZyatnpAxgcC05198V+il6XAgHaT7CliWlljcr7Ln5erOt1siVtXcdHWfzeNnd+tcNwBTGAYROeD7qvFWwFapRYGY2sMI5tLBZzMXm6mEDpPoum1rYwLdMm4sTkUp845xu/2yhOe21wTSO6qUuQhriBS9YxmadSN2KaVRdO90018FWhSL/DePQ2ivSU3QQhtXyO85RhG+gGWUNreytoiHsadC2qmLd1pDxepuHcsHmBp1LRXvnwdNtbUkRmYW4vL4QIo10DWU8Cwp8+AZ3kMmWRg91ZqTOJEsnWwa9AJp29E3ITwc9lErSLXa1HAIPJSp4q9IsMFtmDwLLqJSRmHjBun221nuh7Z4/xkwlbIvyS6NvkErYrjcgvjal+JYnfjADD7F3FjjGVNn0E9K355+s327edFzeZsDH4s0AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 結構性主動脈瓣方向

---

# TAVI #1｜主動脈角度影響自膨瓣成功率

## [He Q, et al. — *Heart Lung Circ* 2026](https://doi.org/10.1016/j.hlc.2026.01.022)

- 單中心回溯 519 例**自膨瓣 (SEV) TAVR**；主動脈角度 (AA) 平均 55.4°
- **AA ≤55.5° vs >55.5°：技術成功 84.3% vs 75.1%（p=0.009）**
- 差異來自**第二枚瓣植入 8.8%→19.6%（p<0.001）**
- 雙葉瓣預測力有限

> **重點**：角度陡（>55°）者選瓣／釋放需更謹慎（考慮球擴瓣或角度不敏感新一代 SEV）。單中心回溯、亞洲族群。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABRElEQVR42u1YQY4DIQxDywN4El/Pk+YBSKntANpL99DDyociNB2Gi+UkdtKWb9Zq35s/b56G1TP6M1fj5hkvP+3d+q8bYJvACGwpbEDYcX5csIGlwtMfEJh8mmFbIyumftiijWyDWWeFLW8cR9z4emBTnT7zbqM6vXIy8Ih+jx4xXUozAEMhgEaBNMGGgAJPHNJia51HTPkDrihuwVJVzZrwpmSLa1soBBdsSLNBomQKUXvZ+ClZ2vAm3cGnFsRS2cHVYZs+hMJbSpKsUH5cLrUgIzhOekojXXyh9I2oxNsIn/6tU+K2OzDZqlly4W2qsYS47aOPhpSA7KUi7ZlGfYiE93LooyGas8q2cgfXRkOO3gqh2qSeaTUvnEmQ+ZZW2NTFldBVy+Q1Zx2tS7c5i5nWatpSW5JOc9avgPp4/ff/qk9uXgnS7P0t9n3JAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TAVI #2｜縱向應變的預後價值會「轉變」

## [Usuku H, et al. — *J Echocardiogr* 2026](https://doi.org/10.1007/s12574-026-00744-z)

- 日本 189 例 TAVI，術前後超音波；37 例死亡
- **術前看心尖 LS**；**術後看中段 LS**（AUC 0.65 vs 術前 0.54）
- 術後 **mid LS <12.5%** 者死亡率顯著較高

> **重點**：術後別只看 LVEF——追蹤**中段縱向應變**可更早捕捉預後不良者。單中心、事件數有限，cut-off 待外部驗證。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABRElEQVR42u1YSY7EIBArDQ/gSXy9nsQDSqJddpI59Uh9GfnQiCAiLlYttiHOm1HxPfnzZAfGOFkzsT979X+s+ol3479OGgwwDqy9yd7j2y7YEKWB6M1T8xBnDC9sK2Yis8MQW5ce1kT0rLCxxlBpCVRm9cY+3euZRn2qgUCx6n7ZxYhD0KedVoRRVWeSU7BuBTkklqYPNvHbEY3s7lmXnArJzGDETic0bbCRb1ljz/ThELZnx42y1WmtsOE3aoFaoA1J2xKbnBIYWXfdcu+iWcCjVhWTqAJ96q1YaVwbp423bO6VQaqQJ0kfb0ktYEfcZGKkpxRT/Q7KhJkPYXIlDXRxRv7tXBRHMrHht9v3FqXqmU73BV5kLtMb5eKRLmwlSOJes7iJ6Cj6YeMt73sWN3p5GGb3LJJwd+h1XfXht+9L1mcnLxOd4yXrSoBzAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TAVI #3｜曾胸部放療者 TAVR vs SAVR

## [Ntoumaziou A, et al. — *Future Cardiol* 2026（11,572 例統合）](https://doi.org/10.1080/14796678.2026.2713341)

- **死亡率無差異**（術後 OR 0.70；1 年 OR 1.04）
- **TAVR 併發症較少**：大出血 OR 0.38、AKI 0.51、術後 AF 0.20、呼吸道 0.39
- **TAVR 代價**：PPM OR 2.27、≥中度 AR OR 4.44

> **重點**：放療後（縱膈纖維化）族群 TAVR 死亡率不劣於 SAVR、圍術期併發症較少；代價是 PPM 與 AR。回溯統合，適應症偏差難免。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABj0lEQVR42u1YUWrFMAwz8wF6pFw9R8oBAp4lO3392X42mAYvlNI2P0KVZcUWX69t782fbS7L5TF9DbMReb8Cn2zsD/tm/cVmoh2J2vNaI+9Ejtf8rok2afRl/iCZr8JoUxTXrNd/gJYgwW2CNGm00O3CQ+JsenV1a0Xp89L1hF7TrpnSTfB+25si2lmVhV9/AXOqYlfdqaIlqxBwcovn9DFRtOxckMGpNaIVVQL/e8Jrv0V3MNqvJtpROHPBwa6GvUU9YRaxuGhlRqplq+z8eqC9nUFWCU5bYFpo10W5iVYZcGamZdttK4Pl6nILqAwz7BElD1Vut7VuTyCHM8j67Z0TvDsFzVb2pNNCnVVxp02oVlmlLxJbAZJUi+YE+i3M1hAVBjtFCKNF8zJ7kRy6DoZjQk8SHqcJ1TQeTSZbg59kbrrcQrd1Tifyodx5OaupGBaVGeqj8qymoqPxIKmbb0/6itWdglO7IZtqCi0nYJDxCeShPKup5lsku/Ap0iqDndldrHNs153VvOfxv775CTeBmUJdlpEoAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 本週以三尖瓣為主
### 二尖瓣 TEER 見 Case Reports

---

# TEER #1｜GDF-15／suPAR 預測 T-TEER 預後

## [Schlegl J, et al. — *BMC Cardiovasc Disord* 2026](https://doi.org/10.1186/s12872-026-06392-6)

- 前瞻 84 例**三尖瓣 T-TEER**（TriClip／PASCAL）；術前測 GDF-15、suPAR、NT-proBNP
- 12 個月死亡 11.9%、再住院 34.5%
- **GDF-15 AUC 0.823 > suPAR 0.742 > NT-proBNP 0.535（p=0.72，無辨別力）**

> **重點**：反映發炎／細胞壓力的生物標記比 NT-proBNP 更能預測 T-TEER 後預後——納入病人選擇。探索性小樣本（事件 10 例）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABPUlEQVR42u1YQQ7DMAhDywPypHydJ+UBSAwDaU+dtMvkw6IqapqLBcaGij8sk//Nx5stsUa8Tq8dZ1n2kqf1q5vAtgLjcI1Hpua7x0cSbBGlEWBmh25sGVzYIq1qmU1CbBY70soVN3AsdsDDkYlvWad7XQ9RndYC30I91q0uLHyTIyB6jjzYliGtpcCK6DHVwrEGHVULJHFLmoWAlALjOBU6zIGtajMlThKeDqK4SdVpO/6m4VvzHyv9FM5FVKfTU4FXNk3dL3HETcdtqQKcPHxLpmHfV34Xj9e3h06ox90Ac2Cz3kE8uOqk4Vu1Hw4zLeeS1GGuPiQRGsyUZ5bpOQutiFz9uVP1vZau2qYgXHNWpla5+HaEt30hO0w2bGkKBQxaxzTXew31VjhZsNWcJVcHgjDS9G///1Xf37wBJMbSsfj+SpcAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TEER #2｜經頸靜脈 T-TEER 克服惡劣下腔靜脈

## [Transjugular T-TEER for Hostile IVC — *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.109420)

- 當**惡劣下腔靜脈 (IVC) 解剖**使經股靜脈路徑無法安全進行時
- 改採**經右頸靜脈 (transjugular)**：超音波導引穿刺、preclosure、漸進擴張
- 關鍵：朝三尖瓣導航時**導管操作方向相反**，避免迷失定位；成功植入兩枚裝置

> **重點**：三尖瓣 TEER 預設經股靜脈；經頸靜脈是**罕見但實用的 bailout 路徑**，值得預先熟悉。技術示範個案。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABhElEQVR42u1YQW4EIQyLygPmSfl6nsQDkNLEBraX9lJV9WHRaJYdLpbl2AmW369l78PfHU6rNaaNjGW+nrAn+1PtP+yH9R+HhdYL9QD2MX1g33+nKNqicTTNDrSxnmyqtdHW2rD10VK9rYEAybpooViUFUmeLqxbeoJ/fXQ94a5pxW1CCdveFNFG/zzRQsW7NwVYVbdlAst2RvS+0oHgRdHGKa5IcMtCU1VCA86Givx9sNHkFnzWhqIl1YucSyrh9jML5YaYwBdJv10bYScvk2Kw9DS5JWC0B3ADvDNlHax1yxTux3T9NmlftuOs1evKfkutomHo5MVIUYBTtWNsYotP2gK7R9VJx7q+KiNQaLCyDmJVB2t4GBzsjJAuPZc1yEChxdGwrt/SBxgKrLUl7Ld2xsbblnPq0Z0d7nR2epshPZe9/PZcLKT8zLu7r9S/T2AntgvNlm6WOUdIJhrczMW5LQ2M3T2mcsd4dYsUC7a4qmj3DRgoxfgABxbV7fvK/a8OPwFmOIRpVisvIQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

# 📚 Honorable Mentions (1/2)

| 主題 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **牙周病×心外膜脂肪×冠心（SCAPIS）** | *EHJ* | 29,056 人；重度牙周病→冠心事件 **HR 1.42**、CACS OR 1.69 | [DOI](https://doi.org/10.1093/eurheartj/ehag569) |
| **二級預防的 index event bias** | *EHJ* | 一級預防模型對首次事件 AUC 0.84、對後續事件 **~0.55**；勿據此否定 LDL 治療 | [DOI](https://doi.org/10.1093/eurheartj/ehag582) |
| **供心保存 10°C vs 4–8°C** | *Circ HF* | 10°C 原發移植物功能不良 **2.9% vs 14.6%**、1 年存活 95.7% vs 86.2% | [DOI](https://doi.org/10.1161/CIRCHEARTFAILURE.126.014240) |

---

# 📚 Honorable Mentions (2/2)

| 主題 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **AI 無需 Doppler 測 HCM LVOT 阻塞** | *Circ Imaging* | 多視角深度學習外部驗證 **AUC 0.84**，顯著省成本 | [DOI](https://doi.org/10.1161/CIRCIMAGING.126.019956) |
| **CTO 三策略（Gulf 登記）** | *JACC Adv* | 741 例；PCI／CABG／藥物硬終點**無差異**；CABG 改善心絞痛 | [DOI](https://doi.org/10.1016/j.jacadv.2026.103015) |
| **AF 的肥胖悖論（英國 71,519 人）** | *JACC Adv* | 過重／肥胖死亡較低（HR 0.72／0.69）、過輕最高（1.87） | [DOI](https://doi.org/10.1016/j.jacadv.2026.103103) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構／冠脈介入 × 5

---

# Case 1｜FFR 的 adenosine 致命支氣管痙攣

## [Kim E, et al. — *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.109650)

- 79 歲、已知氣道疾病；LAD 壓力導線評估注射 **adenosine** 後嚴重支氣管痙攣→呼吸驟停→死亡
- 文獻首例 FFR 相關 adenosine 致命性支氣管痙攣

> **教訓**：**已知阻塞性氣道疾病者，FFR 優先用非充血指標（iFR/RFR）或替代充血劑**；使用 adenosine 場域須備 **aminophylline**。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABk0lEQVR42u1YQW7DMAwT5gfkSf66npQHGFBF0m53WS/DMB5qBEXi9MCqFEk56ue14vPydy/v6DVufGtgY66rsNU3X/Fm/cfLRjuJM4G5kr9gNuze90TbZeza9hVXDlaYj85o5+Jj06B33NGinmLsXGGNtvjXgwaosGhsy1tpwvx++WqCFhFWdZeh0ba8OaLNdaXoqv5Cu4kVlkxotMBZQEjGNlrahGWXjfsQ+EKd+ThtvUy1bbRFGkjBWs08u2wrQIttW0NbMBwtbbuMVQVvGWmySGBXJoS8jGEm62iCKxM2aceWAnzixhNt4ywyVv++1IyZwdTL7hdIqkEuXyZUnPgt5Iq4xl0W0gFoAiJu+npZaV6Q+RbnHU1spmiLSruDDZFzTHNlAscxaEI3F7NuMI+5MiHVa3v4BW/TOIMdL3vaRBjrrTIt+2uxqkoOznOZkGv4HTQ445lXZIiTdactb3cGuyizQHtSuvFZjdxWLeabak5taRN18pj7Wc3zSEEZ0nTS2dqVOlrUjOY8RX6O3P/m5QOZtZBLW1iNkQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case 2｜急診 TAVI 逆轉多重器官衰竭

## [Gent DG, et al. — *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.109639)

- 69 歲重度雙葉 AS；**血壓正常但嚴重低灌流**（lactate 8.6、ALT 5,379、Cr 189）、新發雙心室不良
- **急診經股 TAVR**：壓差 129→<10 mmHg，48 小時生化恢復，第 8 天出院

> **教訓**：惡化中重度 AS **血壓正常≠灌流足夠**；急診 TAVR 能迅速恢復前向血流、逆轉多重器官衰竭。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABmElEQVR42u1YwW0DMQwT6gE8klf3SB7AgEqRSpFP80mB8hHjDriz82B0FEUp8vd143P43uEJrHHqV6M21p1ZW3j4ihfrPw6Bdj1wAvDmP1h4xb4nWoRxADMe5h5EjlAPb7QIKV5BA+y4o82MZmzBdkab/emj2DtTNHblrTRhPV++mqAFkBCECm8lWsubI9p95xZdO9FwQxw8mUC0jG2OI6UFWpYJyywTUQESsG9FtUjrytt9CbXE4RQNpGAQB1O9hczOZi/As6Jt1yzLVCSlWuBwbnLDVG8pBfI2W2RgqE0VjPJVSvtgQpYmmPK2yBA0M80EqoRtlqXsQVuv1jFjTaAIPBWItmSerka+q8W2Yutcy4BtyNWw3xndsZnWsvyhQV9b+mCqt3JcUQS+9LolZcc3tupxVCCieLtteSvq3u58Qx7MtZZ17xAsZ5dRlSUz7svKLWQPE1Z3lM49b3KgxMqbTDrjeUKrAX1C7zvPajQDUYo5u5roMV158tF+zH1Wo3Yse6rgOk+QJtCEkwZiQljr7Wce//eH38Iwjai56T+hAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case 3｜ViV-TAVR 生物瓣骨折致左心室損傷

## [Kamioka N, et al. — *Cardiovasc Interv Ther* 2026](https://doi.org/10.1007/s12928-026-01326-7)

- 小瓣環行**瓣中瓣 (ViV) TAVR** 併**生物瓣骨折 (BVF)** 擴大瓣口
- 過程中發生**左心室損傷**（高壓球囊擴張的罕見嚴重併發症）

> **教訓**：BVF 是對付小瓣環／PPM 的利器，但**高壓球囊擴張非零風險**；審慎評估球囊尺寸／位置／支撐，備妥心包填塞與外科後援。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABQ0lEQVR42u1YwQ0DIQyLygCMxOqMdAMgpXYM6usq9VP5cegeUD5WYjumkTdrxXPz9eYKrJazZeJbPXmOsV5xt/51A2wjD6rVp/b40QQbqtSu2nTWEvvmhi3nCqKyxIZuTpTOClv1caBo+Mz4VjplK/dnpFOtazf34y4ufJO/wUDmOXpgA6oraG5QBF1usno2WlDRqIU+STmfngJV384mzQaO3QRbHp3GRliz1cbfULdRzeVUVQF9+KbmcihocrnwjQoVntrHziQec6Ft12XFKor48C2iCxXDm/zNZ9avGqByjy0HG50q8YJ1pQUg9OFb6bTaWv7GGprlEPmbjM7nLbPfWYptysBOcyFlI0ogpQ6r9wIVobxkxLeDTQ/AeqJOM2wkHvObiNed+MYUR2cTTp95WvmNUs1SaCic+/jb80/WbzdvGRbfNb5Q14gAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case 4｜大動脈炎人工瓣向 LVOT 移位

## [Tadokoro Y, et al. — *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.109647)

- 兩例**大動脈炎 (Takayasu)** 外科 AVR 後人工瓣**向下移位至 LVOT**，**無明顯瓣膜旁逆流**
- 進行性移位干擾二尖瓣前葉→類二尖瓣狹窄血流動力學；最終需雙瓣置換

> **教訓**：發炎性大動脈疾病影響瓣膜錨定；人工瓣可**無逆流地移位**——術後須長期影像追蹤瓣膜位置，勿只看逆流。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABiUlEQVR42u2YUWrEQAxDTXOAOdJcfY40Bwh4LcnJth/bn1KqwoawOyQ/QsjPdiJfX2e8X/7s5Y66jj2PXGfMc6wYiUd1/ohvrr94WWpnqS6pR/1Cc+qu555qy0YZ2w6Pkg23ndWmdFY6/NXuqMTe6XVWi9yWvHZ1JtPrmtuLCZ9uXybcMBsLfkZUEvqJo9qFv8IsYStvIXibeoumEMpD1RrSG5Rtqra0JeSVz0lvVWiuVYYMXGRYDHDYeluXZoMUuEYhN3w7L2mQNJblFj3hWCYhMdKACeVw5wEOp2vnjXtQpFQAzbXKYGObTBrUwZi3S8hiiQVLbPrylpi9xwMgl/0iPHNLfKH/soUpus6bjhYcQIAjzfNgWmX3/igyTOu9DDXF+rr6bzrzliKbsdFjgzNvj55tUhzD2Xl32A1ekValZ7yX0eQvHxbSeOed2iCSavMffE/Is2MQnHPSWO1UzyVyl3Fu21t1W5nsPDGqI2AaZ5WpWRhvkdB2bWeT/SJP1xns/cn9d14+ACvdilHZHEBkAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case 5｜DCA 作為 IgG4 冠脈病的診斷利器

## [Ujita A, et al. — *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.109649)

- 79 歲；LAD 支架內阻塞＋冠脈／主動脈**外膜增厚**、血清 **IgG4 升高**
- **方向性冠狀動脈旋切術 (DCA)** 取內膜組織作病理；prednisolone 後外膜消退、病灶縮小

> **教訓**：IgG4 冠脈侵犯診斷困難；**DCA 一石二鳥**（治療＋取得組織診斷），配合影像與血清 IgG4 導向類固醇治療。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABj0lEQVR42u1YwY3DMAwTTgNkJK/ukTyAAVUi5SCf3udQHB81giKNPwRBkZIs3p9t38u/XS7L4zHz2Tb2Ne2K+pTvP/bL+Y/LRDsSta9RUI3gh+enJYq24K1mdRex+ddcGW0qoQBHslq/6mhTwqXeIwxdtAWvhGrJKjCHsG7hCWs8H11P6DOpBAfVbW+KaNMKJopr0sEItfxBklvIlT4G6aaJXVO0yirFgvYFB+ssE60y+FXAu5JSpgNUIVtl5PMEbgtYFy30UPRu5BqkG7JKSGLZz6QYaAiu6WCrcBZUlBgy19rTVJXg/F0GGfBFFK2hs2XT6EGzNVVPmOzG7yECI8WQrTKYrdF1GWTBsBDNMkwNSF4yHKGavKtbBRrCfsaEZpVdrVun9+aAptvfTgogyTztzew5QjIdODZWnPHgfSvPDtUhwGPR6LaYZecyTI5+N2OyDvbY1UAM1dmG/D6BeuA4aUAuvFkq0XKxgN1dbG20FG0HhGzHeHRrvWM8PCvvapAR9C7uQIS78e8+/hOXL8aEn96rA93YAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 💎 Take Home Message
## 本週 7 大臨床啟示

---

# 💎 Take Home Message

1. **DECIDE-CRT**：NICM 的 CRT「多加去顫器」未見明確存活益處（HR 0.90，p=0.34），換機／感染更多——CRT-D vs CRT-P 應個體化。
2. **RELIEVE-HF**：心房分流器價值在「選對病人」（HFrEF 67% vs HFpEF 21% 可能獲益），不能只靠 EF。
3. **MRA × 種族**：療效與安全性無族群差異（p=0.34）——不以種族為由減用 MRA。
4. **PRAGUE-25 + 疫苗指引**：消融處理心律、生活型態處理代謝（73% vs 35%）；疫苗是被低估的 CV 預防工具。
5. **TAVI**：角度陡（>55°）降低自膨瓣成功率；術後追蹤 mid LS（<12.5% 高風險）；放療後 TAVR 死亡率不劣於 SAVR。
6. **TEER（三尖瓣）**：GDF-15／suPAR 比 NT-proBNP 更能預測預後；惡劣 IVC 可改經頸靜脈 T-TEER。
7. **五則介入警示**：氣道疾病者 FFR 勿用 adenosine（備 aminophylline）；惡化 AS 血壓正常≠灌流足夠；ViV 的 BVF 可致 LV 損傷。

---

<!-- _class: small-text -->
# 📖 參考文獻 (1/2)

**Top 5 Picks**
1. PRAGUE-25 AF-burden sub-analysis. *JACC Adv* 2026;5(9):103109. https://doi.org/10.1016/j.jacadv.2026.103109
2. DECIDE-CRT. *Circ Heart Fail* 2026. https://doi.org/10.1161/CIRCHEARTFAILURE.126.014213
3. MRAs and Race in HF (IPD meta). *Circ Heart Fail* 2026. https://doi.org/10.1161/CIRCHEARTFAILURE.125.014355
4. RELIEVE-HF individual modeling. *Circ Heart Fail* 2026. https://doi.org/10.1161/CIRCHEARTFAILURE.125.014100
5. Adult Immunizations — 2026 ACC Concise Clinical Guidance. *JACC* 2026. https://doi.org/10.1016/j.jacc.2026.07.004

**TAVI Section**
6. Aortic Angulation & SE-TAVR. *Heart Lung Circ* 2026. https://doi.org/10.1016/j.hlc.2026.01.022
7. Regional LV strain prognosis in TAVI. *J Echocardiogr* 2026. https://doi.org/10.1007/s12574-026-00744-z
8. TAVR vs SAVR after chest radiation (meta). *Future Cardiol* 2026. https://doi.org/10.1080/14796678.2026.2713341

**TEER Section**
9. Biomarkers after T-TEER (GDF-15/suPAR). *BMC Cardiovasc Disord* 2026. https://doi.org/10.1186/s12872-026-06392-6
10. Transjugular T-TEER for hostile IVC. *JACC Case Rep* 2026. https://doi.org/10.1016/j.jaccas.2026.109420

---

<!-- _class: small-text -->
# 📖 參考文獻 (2/2)

**Honorable Mentions**
11. Periodontitis, EAT & coronary events (SCAPIS). *EHJ* 2026. https://doi.org/10.1093/eurheartj/ehag569
12. Risk-factor attenuation in secondary prevention (index event bias). *EHJ* 2026. https://doi.org/10.1093/eurheartj/ehag582
13. Donor heart preservation 10°C vs 4–8°C. *Circ Heart Fail* 2026. https://doi.org/10.1161/CIRCHEARTFAILURE.126.014240
14. AI detection of LVOT obstruction in HCM. *Circ Cardiovasc Imaging* 2026. https://doi.org/10.1161/CIRCIMAGING.126.019956
15. Gulf CTO Registry. *JACC Adv* 2026;5(9):103015. https://doi.org/10.1016/j.jacadv.2026.103015
16. Obesity subphenotypes in AF. *JACC Adv* 2026;5(9):103103. https://doi.org/10.1016/j.jacadv.2026.103103

**Case Reports**
17. Fatal adenosine bronchospasm in FFR. *JACC Case Rep* 2026. https://doi.org/10.1016/j.jaccas.2026.109650
18. Emergency TAVR reversing multiorgan failure. *JACC Case Rep* 2026. https://doi.org/10.1016/j.jaccas.2026.109639
19. LV injury after BVF in ViV-TAVR. *Cardiovasc Interv Ther* 2026. https://doi.org/10.1007/s12928-026-01326-7
20. Prosthetic AV migration into LVOT in Takayasu. *JACC Case Rep* 2026. https://doi.org/10.1016/j.jaccas.2026.109647
21. DCA for suspected IgG4 coronary disease. *JACC Case Rep* 2026. https://doi.org/10.1016/j.jaccas.2026.109649

---

<!-- _class: abbr -->
# 縮寫對照 (1/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| CRT / CRT-D / CRT-P | Cardiac Resynchronization Therapy (with Defibrillator / Pacemaker) | 心臟再同步化治療（去顫器／節律器） |
| NICM | Non-Ischemic Cardiomyopathy | 非缺血性心肌病 |
| HFrEF / HFpEF | HF with Reduced / Preserved EF | 射血分數降低／保留之心衰竭 |
| GDMT | Guideline-Directed Medical Therapy | 指引導向藥物治療 |
| MRA | Mineralocorticoid Receptor Antagonist | 礦皮質素受體拮抗劑 |
| IPD | Individual Participant Data | 個體參與者資料 |
| AF / CA / AAD | Atrial Fibrillation / Catheter Ablation / Antiarrhythmic Drug | 心房顫動／導管消融／抗心律不整藥 |
| TAVI / TAVR / SAVR | Transcatheter / Surgical Aortic Valve Replacement | 經導管／外科主動脈瓣置換 |
| SEV / BEV | Self-Expanding / Balloon-Expandable Valve | 自膨式／球囊擴張式瓣膜 |
| AA / AS / AR | Aortic Angulation / Stenosis / Regurgitation | 主動脈角度／狹窄／逆流 |
| LS | Longitudinal Strain | 縱向應變 |
| PPM | Permanent Pacemaker | 永久節律器 |

---

<!-- _class: abbr -->
# 縮寫對照 (2/2)

| 縮寫 | 全名 | 中文 |
|------|------|------|
| ViV / BVF | Valve-in-Valve / Bioprosthetic Valve Fracture | 瓣中瓣／生物瓣骨折 |
| LVOT | Left Ventricular Outflow Tract | 左心室流出道 |
| TEER / T-TEER | (Tricuspid) Transcatheter Edge-to-Edge Repair | （三尖瓣）經導管緣對緣修復 |
| TR / MR | Tricuspid / Mitral Regurgitation | 三尖瓣／二尖瓣逆流 |
| IVC | Inferior Vena Cava | 下腔靜脈 |
| GDF-15 / suPAR | Growth Differentiation Factor-15 / Soluble uPAR | 生長分化因子-15／可溶性尿激酶受體 |
| NT-proBNP | N-Terminal pro-BNP | N 端 B 型利鈉肽前體 |
| FFR / iFR / RFR | Fractional / Instantaneous / Resting Full-cycle Flow Reserve | 血流分數／瞬時無波形／靜息全週期血流儲備 |
| DCA | Directional Coronary Atherectomy | 方向性冠狀動脈旋切術 |
| CTO / PCI / CABG | Chronic Total Occlusion / PCI / Bypass Grafting | 慢性完全阻塞／經皮介入／繞道手術 |
| HCM / EAT / CACS | Hypertrophic Cardiomyopathy / Epicardial Adipose Tissue / Coronary Artery Calcium Score | 肥厚型心肌病／心外膜脂肪／冠狀動脈鈣化分數 |
| TAK / IgG4-RD | Takayasu Arteritis / IgG4-Related Disease | 大動脈炎／IgG4 相關疾病 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

> 本講義為讀書會共筆之教學整理，僅供醫療專業同仁臨床教學交流參考，不作為個案診療依據。資料來源：PubMed（2026-08-01 至 2026-08-08）；試驗結果經 WebSearch 交叉查證。
