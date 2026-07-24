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
  section.abbr { font-size: 0.62em; }
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
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-07-18 ~ 2026-07-24'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-07-18 ~ 2026-07-24

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Pick／個案附 QR Code，可掃描跳轉原文

---

# 🎯 本週主題與固定欄目

## 把病人送對路線：新藥、去侵入化與抗栓再精簡

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 結構性主動脈瓣方向
3. 🔧 **TEER Section** — 二尖瓣／三尖瓣影像與節律
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — 結構／冠脈與心臟腫瘤急症 × 5
6. 📖 **參考文獻 + 縮寫對照**

> 本週 *Lancet* 無心血管原始研究；已與上一期（07-11～07-18）交叉去重。

---

# ⭐ Top 5 Picks 一覽

| 試驗／研究 | 期刊 | 方向 | 關鍵數字 |
|------|------|------|------|
| **SCOUT-HCM**（青少年 oHCM 用 mavacamten） | *NEJM* | ✅ | Valsalva LVOT 壓差組間差 **−48.0 mmHg**，p<0.001 |
| **2026 ACC HFpEF 專家共識** | *JACC* | 💡 | 更新診斷流程＋四大類 GDMT 落地 |
| **「食物即良藥」MTG RCT** | *Circulation* | ✅ | HbA1c 額外 **−0.40%**；食物安全 +215% |
| **STOP-IMH**（原發 PCI 後即刻 ticagrelor 單藥） | *EuroInt* | ➰ | 非穿刺部位出血 **2.0% vs 9.9%**（HR 0.20） |
| **MASTER**（臨床＋運動心電圖排除左主幹） | *EHJ* | 💡 | AUC 0.78，**NPV 98.2%**，免 41% 冠脈攝影 |

> **Pearl of the Week**：好照護是**分流的藝術**——把對的病人送進對的路線。

---

<!-- _class: divider -->
# ⭐ Top 5 Picks
## 逐篇設計與結果

---

# Pick 1｜SCOUT-HCM（NEJM）

## [Rossano JW, et al. N Engl J Med 2026;395(4):362-373](https://doi.org/10.1056/NEJMoa2601103)

- 三期、雙盲、隨機、安慰劑對照；28 中心、9 國
- 對象：**12 至 <18 歲、有症狀 (NYHA II–III) 阻塞型肥厚型心肌病 (oHCM)**
- n=44，1:1 → **mavacamten（心肌肌凝蛋白抑制劑）** vs 安慰劑
- 主要終點：第 28 週 **Valsalva LVOT 壓差**變化

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABPUlEQVR42u1YuQ0DMQwj4gE8klbXSDeAAUWin6S5FCkCFjGCwzluCIqk5EPcrIH/yceTC7laBGD5HD1qDxsP3K1fnSQ2S4wtHN1H99wmwnyKYCvGiBA98qVdaGLYCg+giY36c1InhK30diFdkLxRezp6o08vOz8hn87FyiZ1r3RR0Vvmm7Omtrca2BaqgkcvOIhQRG8tGGsJjDQ2nZpOSNW+yqrVvDqZVMoQVCc1bl1Fb8yQydhpWyp6owWSt+AQUtZQ8ino0wwQLMOGit5IFFHZWPErpLcqK59t55vQHNIL1QQ2CyrDW9bRx9vQW/XVyTeGGycQvsPE5pCCxx6x4AnNb6eU4EweUj2rAmROvPMfpfsC67hotCaGjbxVjEzVid2z/IxMkJqR2FWxvSCTb/uetQoaQnr7f6/65uQJI1vkw8D6qygAAAAASUVORK5CYII="><br>📱 Scan DOI
</div>

---

<!-- _class: bignum -->
# −48.0 mmHg
## Valsalva LVOT 壓差組間差（95% CI −67.7 至 −28.3）

**p<0.001**｜無人 LVEF <50%｜不良事件兩組相近

首個青少年 oHCM 心肌肌凝蛋白抑制劑三期試驗

---

# Pick 1｜臨床啟示

> 💡 **兒少 HCM 藥物治療里程碑**：把成人已成熟的 mavacamten 帶進 12–18 歲，壓差降幅與 EXPLORER-HCM 相當。

- 過去青少年阻塞型 HCM 缺核准藥，常走中隔減容手術
- **界限**：n=44、替代終點（壓差非事件）、僅 28 週
- myosin 抑制劑需嚴格 **LVEF 監測**與 CYP2C19／藥物交互作用管理
- 長期安全、對成長發育與心律不整之影響待追蹤

---

# Pick 2｜2026 ACC HFpEF 專家共識決策路徑

## [J Am Coll Cardiol 2026](https://doi.org/10.1016/j.jacc.2026.06.018)

- ACC 決策路徑：**射血分數保留型心衰 (HFpEF)** 的實作流程
- **診斷確立**：利尿鈉肽、H2FPEF／HFA-PEFF、運動或侵入血流動力學
- **排除 phenocopy**：類澱粉沉積、HCM、高血壓性心臟病
- **GDMT 落地**：SGLT2i（核心）、GLP-1 RA（肥胖表型）、MRA、利尿劑

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABO0lEQVR42u1YQQrDMAwzywP6JH/dT8oDAp4tNaWXDnYZOiyU4pCLsGXJieXDWvY/+XgyrdbINPP6ryN7b75e9rR+dVLYvDCOjEZ6RG0LYf1FsHXGJkACWMVDC5sjddGBHrbVfAs7tPKWqGOvI8A9Hb6hT6dfn1Cfck0EyOGpLip8M7bnum1Falrtmc3/DopyVVAVvqGgFJACNqi9MjUlsG0QWQjLuTTyFusWjEYYKnxrwyewS3s9tbS3faG9ntlTyVvs0cg5IHGro29dSmSsUAnxDbLWkCb5Fqf1y2gILbX4xoLK5M0vGx2nvinxjboBvmEscbU5ZO0bDeEJzW/0UChJz706fIP2GlqV3zKtexaVTYtvGxu5hytDmF7e0A5Bm5C613eH9kyycQrds05fyOthREff/i9Z3528AVV67YSJQZ1nAAAAAElFTkSuQmCC"><br>📱 Scan DOI
</div>

> 💡 把近年正向試驗（EMPEROR-Preserved、DELIVER、STEP-HFpEF、FINEARTS-HF）整合成門診可照走的流程；別漏掉可治療的**類澱粉沉積**。

---

# Pick 3｜「食物即良藥」MTG 隨機試驗（Circulation）

## [Circulation 2026](https://doi.org/10.1161/CIRCULATIONAHA.125.077982)

- RCT；南加州 460 名 Medicaid、第二型糖尿病、HbA1c 持續偏高
- 1:1:1 → 常規照護／低劑量 MTG（~$135/月）／高劑量 MTG（~$175/月）
- **醫療客製食材 (MTG)**：每週配送健康食材＋文化適配食譜＋電話營養諮詢
- 追蹤 6 個月

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABi0lEQVR42u1YSY7DMAwTxg/wk/x1PykPEKCRSDntpXNpgeGhRhDE9oVgKGqxeL3cvpfvXV6Wa1zLZ4wrt8tm1JEt/7E/1n9cFrxEPfAkcp/7fIuiTRoTns2d9EbsPEmShzJaCiCJLaj6aOujGLbeyqIt3WaszU3dEraqbtsTnh9dT+DKX19+lttt89ibphJAppPnCrQ+l+R2E+qIMoQCmdKtQ1G0nj6A4PLzTuTpvarcLuqhjCvaE3TRzoDTGt8O6cqiLZsFVMigEkQdhi5aQg1SivxrM2QzL2NtwB+QL5aq396Ao93gFDmaaFuxXcyYH6PQVIKzTniIoSzXVbk1JC8WjQ4HQ1mu6Qnx8FvagnWO0FQCsBkw764VZZVQi+msELJuzMdU0RaTd7gh1pAjRKMMk4R2Bj/ZQbt3WKffYaytod2XURKwsqVbg/WsZhvU+9RBhPI8YXS52Gy7KU+WNic26HqCsyblORidgboVrhh7xtitLhpJ4XlCewI6MmC+DLMmYb/9zuM/f/kLKTeTCcs30K0AAAAASUVORK5CYII="><br>📱 Scan DOI
</div>

---

<!-- _class: bignum -->
# HbA1c −0.40%
## MTG vs 常規照護（6 個月，額外降幅）

食物安全 **+215%**｜營養安全 **+365%**

「Food is Medicine」文獻多為 null → 本試驗**陽性**

---

# Pick 3｜臨床啟示

> 💡 **社會決定因子的結構性介入**可產生可量測的代謝獲益。0.40% 屬「社會處方」層級可加成效益。

- 過去 Food-is-Medicine RCT 多 null（2023 JAMA IM 客製餐點未顯著）
- 同時大幅改善食物與營養安全（心血管代謝上游因子）
- **界限**：開放標籤、單一地區、6 個月、替代終點（HbA1c 非事件）
- 啟示：值得納入整合照護與健保給付討論

---

# Pick 4｜STOP-IMH（EuroIntervention）

## [Yosofi B, et al. EuroIntervention 2026;22(14):e773-83](https://doi.org/10.4244/EIJ-D-26-00421)

- 多中心、開放標籤先導；200 名 **STEMI** 於原發性 PCI 後**立即**隨機
- **ticagrelor 單藥（省略阿斯匹靈）** vs ticagrelor＋阿斯匹靈
- 終點：13 個月 MACCE、出血、心肌內出血 (IMH)

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABO0lEQVR42u1YuQ3DMAwkogE0klbXSBpAAMM70nZlFymCKywERmQ1B/IeyuY3a9t78niyLFZbI/7s7r4G9jb2x+7Wv04C2wiMzWfDM8COeMZLEWwGPDNKt/uMbVsooxC2BXjZU0Fs24JvqJ4UNvCN2FA6Lb6VTs+fkE5zsbPY98NdRHrKWhXN+syXMlqA61qg6q7X00AFZ6McYL8qdUvXpTz3GV4qdWMWwD2KbxBCV9FCAGOkgnJUhE7WFxgayESLs8sa2KKPTFJLAwHZZGYkFupCqMS3itF0kvQ3GZ2GBPwYRSr3VfhWs7nl9JvZKsM3dDC6SX+7SKg0h5TxMheG3vyWL/Tm3iTbyjwdOpl11MpyFMmRSekO6Dn0NpZR7X5qVCttZIrd652ZhYCop5JOHXfnaVJ8e79X/XLyBdh00esjhoMSAAAAAElFTkSuQmCC"><br>📱 Scan DOI
</div>

> 結果：MACCE **4.1% vs 4.0%**（缺血無差、檢定力不足）；非穿刺部位出血 **2.0% vs 9.9%（HR 0.20，0.04–0.92）**；IMH 相近。

---

# Pick 4｜臨床啟示

> ➰ 「aspirin-free strategy」在**最急性 STEMI** 情境的探路——PCI 後即刻去阿斯匹靈，出血更少。

- 目前指引：短療程雙抗後降階為 P2Y12 單藥
- STOP-IMH 更進一步在原發 PCI 後**即刻**省略阿斯匹靈
- **界限**：先導、n=200、對缺血終點檢定力不足 → 尚屬研究階段
- 合讀 NEO-MINDSET：**PCI 複雜度不改變**單藥 vs 雙抗（見 Honorable）

---

# Pick 5｜MASTER 研究（EHJ）

## [De Carlo M, et al. Eur Heart J 2026](https://doi.org/10.1093/eurheartj/ehag464)

- 多中心病例對照；穩定 CCS 病人於最大**運動心電圖 (EST)** 後接受冠脈攝影
- 病例：**左主幹 ≥50% 或 LAD＋LCx 近端皆 ≥70%（LM-equivalent）**
- 335 病例 : 797 對照（1:3）；邏輯迴歸建模＋內外部驗證

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABRUlEQVR42u1YsQ3DMAwT6gNykl/3STnAgEpSSrZ06FBwqBEETr0QlElKjXxYO/4nH0/OwBqZETMO/DD5HXO/4mn96gTYJjASm4DhE3u8TbCBpUEK5zhJMN7DDFu9yZsdtpW5ePHMsFUdUdMtFTjdt7jo6sdIp/cCqmON2108aroB6SSBrC+Kexhh05UDY0Kojc99SxrvAnvNIQR7uPDWREkRTK4KLw8tAMmQjeiTvG2bPJWzoZqCB8aMtKBSMujjzlMbf2thQg4pqWJtFy0Eo0p1JDxR54It5R70jVVNSG1c+pCKKoVCy8EmT+u+sb0kgdnKdeGNFgdtCli3SUZ9CKop9uqxmWV6zhK8rBbOxkPm5bdRE02BtJoXRod+1MUzwqYWrrwuZMVu86ngZbrNWeqLaMKV+zZ52nNW1TScsv7/f9U3J29BmOvdrm7U5wAAAABJRU5ErkJggg=="><br>📱 Scan DOI
</div>

> 結果：AUC **0.78**；LMCAD 盛行率 5% 假設下 **NPV 98.2%**；可安全免除 **41%** 冠脈攝影（每省 58 例 CAG 漏診 1 例）。屬「排除」工具、病例對照設計易高估表現。

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 結構性主動脈瓣方向

---

# TAVI #1｜NOTION-3 冠脈狹窄嚴重度／位置次分析

## [Circ Cardiovasc Interv 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016286)

- 主試驗 (n=454)：重度 AS＋生理顯著穩定冠心，隨機 **PCI vs 保守**
- 主結果：PCI 降複合終點 **26% vs 36%（HR 0.71，0.51–0.99）**，但**出血較多（28% vs 20%，HR 1.51）**
- 本**預設次分析**：冠脈**直徑狹窄程度**與**近端病灶位置**是否改變 PCI 效益

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABkElEQVR42u1YUW7FIAyLxgE4ElfvkXoApCy2Q7ef7WeT5kkPVVULP5YxjkPk12PHa/Fni3fUGPfSO+tjJqZi7bf4ZvzFYqFdhXrktec1CHXgN2veE23RCISkN/OqmXGDZ1+0hW0Wn1DN+Adoj2hLrmGNlnzio6S7OWOs2/aEz4+vJ2jcIhncjsfePJUgMidMLOBjPW/JbfG5+g2GozDXr+8pw7EipTNpZReLRXrqtliVBiRd2JetJ2RKtPmY2GQhNvUE7Dtt4aP+4qyZeoIsd53zlTAxatiV2xRUlImUj9n6Lc5UccskRlWonE3T6lBbvzvMMIyJcNecoINGwPg+dc1Ut9j0wNYr4aDTqZnpqlvWMrmWqpjU66lbISTsdrOgLZgmxgZ8keRkJl+2OUF6UPTqtMCGwla3vfUhN4vuK317hyXdynK7nTTuy/K4gTp0Vwfruxp1jrr9MNbtuf1Q/WXQ9e3Lzs3Sc1GjWztrbpkbUSOoW0ZHb93CwTDYAvvm28cTkoXs9JLGfvu6j//9xXf9m5mllGhCvAAAAABJRU5ErkJggg=="><br>📱 Scan DOI
</div>

> 💡 用**病灶分層**辨識「哪種 TAVI 病人的冠心最該處理」，把 PCI 用在最該用的人、避免對次要病灶過度介入只增出血。

---

# TAVI #2｜無症狀重度 AS 早介入的成本效益

## [Genereux P, et al. Eur Heart J Open 2026;6(4):oeag115](https://doi.org/10.1093/ehjopen/oeag115)

- 以 **EARLY TAVR** 為輸入，終生 Markov 模型；九個歐洲醫療體系
- 早期 **TAVI（SAPIEN 3/3 Ultra）** vs 臨床監測延遲換瓣
- 早期 TAVI 皆為**經濟占優 (dominant)**：成本效益機率 **97.3%（英）～99.9%（比）**
- QALY +0.18～0.23；並淨省成本

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABQElEQVR42u1YsQ3DMAwTqgN8Ul73STlAgEpKStClHToUHGoYQRovBCWSci3frLD/yceT07A8t59HGDd/4+Vh79avToDtAEZgw0usxNOTTxFsYAl4wJutTZynuRa2F97ksJGuMKKSwnbVsT9I9VvplHTNFtLprN3u4be7aNQ01u42Y33RdUsH27RcVRY07tGsDLYq5R4Oc9tS4Q2WG73ZcrWVsI17XDUNGZ3Ccmuz6yAEIS3UBNJJWqRlmbBKLnj5Rowu+DFk+g1IJrPA3mlTWY1+Y/OTt7bfRigzh5C3S6TEljo6LSHsxpY9hJgObwwCZ2wdpQXGhNAcwkgd0nraFJrfiMo65b2Gc6W59+jQ77Kq3Rcq5ZtGJS2Us3n2dFS5L1PT+/5S8DLV7llJuuKyYp08nWm8vDdMKev//1d9c/IEz7filUnfpoUAAAAASUVORK5CYII="><br>📱 Scan DOI
</div>

> 💡 EARLY TAVR 已支持早介入（2025 指引 IIa），本文補上衛生經濟證據。惟**廠商參與、模型導向**，不能直接外推台灣健保。

---

# TAVI #3｜Vectorial Angle 預測 TAVI 後永久節律器

## [Dogan M, et al. Am J Cardiol 2026](https://doi.org/10.1016/j.amjcard.2026.07.009)

- 67 例球擴式 **Myval** TAVI；術前 CT 定義 **Vectorial Angle**（瓣膜最大徑向力方向 vs 傳導系統走向之角度）
- **PPM 植入率 17.9%**
- 獨立預測 PPM：**較窄 Vectorial Angle**（OR 0.935/度，p=0.007）＋**較短膜性中隔 (MSL)**（OR 0.447/mm，p=0.011）
- Vectorial Angle AUC 0.806，切點 ≤52°；校正後 **RBBB 失去獨立預測力**

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABjklEQVR42u1YwW0DMQwT6gE8klf3SDeAAVUkdWk/yacoygIxDgf4/GEUiqQV+XydeB/+7PCKWoO7mPvMHTPxKdb5iBfrLw4L7Sqc46rftLmNEwvgL1O0VUaiVXlT2+GMllALIUDO/BdoaysaOKNFVXPXg7abG2h9eUtNIAcej68m9IJw1Vu8bXlzRFs4QYPiKvQ2vsTBtLakbv31QAiDgE2Ydhn6K4WzPYJelrZoUVuQAZ1Fd0CFjbsMtY2V7Q5kr2ltoa7UgQ2EgTqTuunpDvSvTd5Wo22VevgqWIq3tDMkMWpa2jJBsPVIHEzRMtCCtzTcNgt9dPWyoCOQEmSsnMI2J1QxIWJ8s87HWBMi7vsOItnqeOPJ2++qpZsO7xGmmsD0RbSdxAYL7pwTkpGGxJCamfJWHMBbzaWLg/PdoW/oiGHoMm5972XM5Kot5wm+CnZrV6dcRkf3eYKSDI04xAfnyRKU4VqyXczurNEuigPzzEzfxHjzVgnhMQ61ntWAAEqPMegRtmn8PXL/ncNPwsOo+TnXNVEAAAAASUVORK5CYII="><br>📱 Scan DOI
</div>

> 💡 不只看植入深度／膜性中隔，還要看**徑向力是否正對傳導組織**；若驗證，術前可旋轉植入方位避開傳導束。單中心、n=67、Myval，屬假說生成。

---

<!-- _class: divider -->
# 🔧 TEER Section
## 二尖瓣／三尖瓣：影像預後與節律策略

---

# TEER #1｜RACI：功能性 TR 的 CMR 預後指標

## [Circ Cardiovasc Imaging 2026](https://doi.org/10.1161/CIRCIMAGING.126.019813)

- 633 例中重度以上**功能性三尖瓣逆流 (functional TR)** 接受 CMR
- **右心房室耦合指數 (RACI)** = 右心房容積／右心室舒張末容積
- 以 Youden 切點分正常（<0.62）vs 偏高（≥0.62）
- RACI 偏高 → 較差預後（反映右房相對右室失代償耦合）

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABi0lEQVR42u1YQQ7CMAyL6AP2pH49T9oDKpXYbgcXuICED1QTdOvFihzbaczXa8T/8LPDM2q1+j344cja4FP0cYs36xeHhbYXyDZzRG+1OYOvs757og3irP1AeVHbwty80RYlqsIA6Y+2+MAHvMWrL9q56JoibX0x5q00oT8/vpqwVxWWspDsNaqZI9rE3yEFA2lR1ei2CjZRVQiCuqxqW+Cba21lB9SuvMShVNe0ywoY3RZSAN4mW8+0y+gOKeFChWFqadplJwyXbYUiB92Bece2ttTbcgc6rzamvNXaSYw4YWqmmsAYQ8lKutgWNF+9fUTcQZvw1VtIqyws1F+Cbctb+RdzeOFcOcdXb3f8JmOX3poqGNtfOIME2JHMdXY4lp2RBl2ZfJjmhL5nMQ1o9AVjBdNsDmWQcLHFrGcHqq7uQNram89lmCBWJGMeM555+zXsXHnM+D4hxFgNPss1jNEyjSdv7dKYt1dtc086M3xnhwdvuU91nGuXURNoZOv6i5eN1rPD/z7++4d3GIOO2tDHB+wAAAAASUVORK5CYII="><br>📱 Scan DOI
</div>

> 💡 三尖瓣介入核心是**在右心失代償前介入**。RACI 把「右房-右室交互作用」量化為單一預後訊號，補足單看 TR 嚴重度或右室功能。呼應 TRI-FR「解剖卸載 ≠ 功能恢復」。

---

# TEER #2｜中度／中重度 MR 的自然病史

## [JACC Adv 2026](https://doi.org/10.1016/j.jacadv.2026.103057)

- Mayo Clinic 2010–2023；中度或中重度**二尖瓣逆流 (MR)** 連續病人
- 依機轉分**退化性 vs 功能性**
- 終點：全因死亡；次要含心衰住院、進展為重度 MR、二尖瓣介入

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABiklEQVR42u1YQW4EIQyLygN4El/nSTwAiTp2mO2lvVRVfViERsNwsTKO4yTO92vH+/J3lyuw2pnYO8buM/rJT3j/iB/Wf1wC7QDqtsauY+Js+LRM0Sa8FbsfbR2bM9oMb4ADeAFgf7RgLKh7ieGLNuFlwgXTLhqPrrylJqzxdftqQq2JHZSvl7w5ok2Q4i1osC9+wPaMbRaFEB9KxxK/K2/FVeFs4gOzz5MJCCmfWXZZHYKscM0yiEAv9h5hNo5tCUKmGAg80t503yyrykXV1ZeqbqaVN1TCKAVBwzBN0bI0sCgQatJAL66x7bQHKbbzibCrJkzJVysfnkdANc0yeLDcQdVVIZOOHVsPlpF8UixusbCMLf9+0lXpZt2X0W7dLnJIvoz9reosgyx9QJBlxlwVTO1DuXCKw3buHcgE+QRAPdIH274sO0d1EJon2CpYzWr490Vjya/zPIG+cVXSBflgPVmKZ7BAGnijVUVTI+nrGC9vb5N+4+w8q2GnUx2ELJmvG3/P4//i8hNxjIiYq5S97gAAAABJRU5ErkJggg=="><br>📱 Scan DOI
</div>

> 💡 TEER／外科證據多集中在**重度** MR；本研究量化「灰色地帶」的中度／中重度病人自然病史，界定「何時該把中度 MR 放上雷達」。單中心回溯，機轉分層是解讀關鍵。

---

# TEER #3｜三尖瓣 TEER 後的保瓣式節律策略

## [Azañón-Cantero P, et al. Pacing Clin Electrophysiol 2026](https://doi.org/10.1111/pace.70373)

- 3 例**三尖瓣 TEER** 後需永久節律；TEE＋ICE 影像導引
- 2 例**無導線節律器**、1 例**左束支區域節律 (LBBAP)**（CRT upgrade）
- 影像導引安全穿越修復後三尖瓣、避免干擾 TEER 夾子
- 全數成功、TR 未惡化；LBBAP 者 LVEF 30% → 57%（6 個月）

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABRElEQVR42u1YUQ5CIQxb5AAciatzJA5AMtcWn/5o4o/ph4QYkZ+mW7ti5Ju143/z8WZFrcZTww8D5xj7Fu/Wr24K27hQFc46AudywVYsFZ76jD6Bc0XzwjYFrNjzw5a7F7RZqKywqY7o/17spVO/Uaeg62wjnV520ud+mAmOHjUtVKppkVY0svHShDcotBBGAGRiu/QbnC1KAgH2YHH0k/TRqWwtz8waNtgCzUbrQDVZ0+2i0ynjpeVCCEZaWM/vFMLDhz20gAkF3sapb5A9D96U2RiQuFlil7kg3lhQlLjPXHbZEvCoWRudJicC2INURaNNJi9gF4GpwWozTwWJLwV0mtKmUX67ohIj3Haap010obgjfbz35Z2VeYKc1xsQCp3KmYpMVm9ABsuji2bmveQt1HU+81TvLFVWy2ie/v/J+vrmDj2Z6GtgOG7vAAAAAElFTkSuQmCC"><br>📱 Scan DOI
</div>

> 💡 TEER 後跨瓣植入導線恐惡化 TR 或干擾夾子；**保瓣策略（無導線／LBBAP）＋多模影像導引**是結構＋電生理團隊都該熟悉的思路。3 例個案，待更大系列驗證。

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀（含連結）

---

# 📚 Honorable Mentions（1/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **NEO-MINDSET 複雜 PCI 次分析** | *EuroInt* | n=3408；PCI 複雜度**不改變** P2Y12 單藥 vs 雙抗（p-int 0.68）→ 支持複雜 PCI 亦可單藥 | [DOI](https://doi.org/10.4244/EIJ-D-26-00409) |
| **PAD 藥物治療新進展（回顧）** | *EHJ* | 雙路徑抗栓、statin＋PCSK9i、GLP-1 RA/SGLT2i 之肢體與心血管獲益；表型導向 | [DOI](https://doi.org/10.1093/eurheartj/ehag516) |
| **咖啡因與 CVD：AHA 科學聲明** | *Circulation* | 咖啡因與心律不整／血壓／CVD；急性 vs 慢性不同、個體差異大 | [DOI](https://doi.org/10.1161/CIR.0000000000001454) |

---

# 📚 Honorable Mentions（2/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **ANOCA 內型導向治療** | *EuroInt* | n=525；侵入功能檢測分六內型依型調藥；多數內型 SAQ-7 顯著改善 | [DOI](https://doi.org/10.4244/EIJ-D-26-00148) |
| **優化 PFA：1000 例世代** | *JACC EP* | pentaspline PFA；8→10 次「olive」流程精進，評估安全與耐久 | [DOI](https://doi.org/10.1016/j.jacep.2026.06.011) |
| **AF 與院外心臟停止（丹麥全國）** | *JACC EP* | 647 萬人；AF 關聯 OHCA（HR 1.66）與死亡（HR 1.79），校正 IHD/HF 後仍成立 | [DOI](https://doi.org/10.1016/j.jacep.2026.06.009) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構／冠脈與心臟腫瘤急症 × 5

---

# Case #1｜微軸流泵橋接經腋動脈 TAVI-in-TAVI

## [Orlandi M, et al. Clin Case Rep 2026;14(8):e73225](https://doi.org/10.1002/ccr3.73225)

- 79 歲男性，先前 TAVI 嚴重退化 → **心因性休克**
- 先以**經瓣微軸流泵**暫時性機械循環支持迅速穩定
- 分期經**腋動脈** TAVI-in-TAVI（瓣中瓣），結局良好

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABSklEQVR42u1YQQrDMAwTywPypHw9T+oDDJ4sp7ttsMvQYaGUlFyEZclKkW9W4H/y8eQC16jt6nd9Y8UD79avTohtESNRDW7uPTcm2FAV27WZWyAx7LAhm1k7bIlJaJuorLClmi1mxtyN06bfpNMq13mMdHovUhkyk+MuHpySylfRWMaYPtjqzYrRQAiy5CA/8dECG0wihSxuU7Me/bbpaSlUGlh6pk2/SQLEU2yK03DRaVFZ1StFQC5nowU1GwlFq1VmYpNDWKsdst8jB6h6Hpz2rC8DuXAmvgu2FCo5cBM6rfxN2pyd3FAGYjNPx7G4JcEqhNhk8pDZjnvid0wyyiHKb0PZstOmUX7TfM/rBLmwmVknvIlW9GyF130hXlFEujDCdoLl0pUBPjmk54LuWa0Ls3tW5gkkl8LbTKd7FlqnvXzm6f9/1fcnTxKJ6e48eDfXAAAAAElFTkSuQmCC"><br>📱 Scan DOI
</div>

> 「先穩定、再分期介入」的結構搶救：MCS × 瓣中瓣 × 替代血管途徑三者整合。

---

# Case #2｜消融誘發嚴重冠脈痙攣，冠脈內腎上腺素搶救

## [JACC Clin Electrophysiol 2026](https://doi.org/10.1016/j.jacep.2026.06.021)

- 導管消融中發生**嚴重冠狀動脈痙攣**致血流動力學不穩
- 傳統血管擴張劑無效／合併嚴重低血壓時
- 以**冠脈內腎上腺素 (intracoronary adrenaline)** 成功緩解

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABh0lEQVR42u1YwQ0DIQyLygCMxOo3EgMgpbENVT/tp5XqR9EJ3R0fy0psh8jXa8X/8LPDGbXaHNxjRaye+BVj3eLN+sVhoR2FunACauEE1NHq1zRFC3gTL0skd4F3RjuI8yqoh2p3tCseuy9akJlXFa12vtjW7daE58dXE7SmAEeVrtiGvDmivdRfTSQn0PLdtBIKsEwBDANtMVy+YYq2oBa36/jCkVzbLhtQgC5WsdMpTBWs+FRIOI2WwOzZZZQsYGMloN2q79K1EthWkgXoAz9RBrZdRgUgpdVrJJZUe3KLAlBgEL3QMVd3YBnAvyQIicdXbzN3vqWpySz009TLqK5CyDK+tgJ75ls6lypWgXxHR8suo4vtrKj01dh6tu4gUzi2a5xqEMDoZaxVYWYes53LTlBklyncuqZxzQ5jq+5DGcJ5LjskE+cegb1nXj6cy4zzre4Tzvy4BzRrtLlZbcd/vblF7uLkC2tL87saol2d+VbJoaevJjAlPiWxsZzvav738d8/vAPYqYtEb9a2hgAAAABJRU5ErkJggg=="><br>📱 Scan DOI
</div>

> 鄰近冠脈之消融（右冠竇、二尖瓣峽部、心外膜）警覺急性痙攣；救援選項需納入冠脈內腎上腺素。

---

# Case #3｜右心房黏液瘤以反覆心室頻脈表現

## [Sharma V, et al. JACC Case Rep 2026](https://doi.org/10.1016/j.jaccas.2026.109422)

- 34 歲男性反覆**心室頻脈 (VT)**
- 大型帶蒂右房腫塊 → 右心腔擴大＋嚴重三尖瓣逆流，CT 見鈣化
- 手術切除＋三尖瓣環成形；病理**黏液瘤併鈣化與骨化生**，術後無心律不整

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABiElEQVR42u1YwW0DMQwT6gE8klf3SDeAAVck5Us+yacFygIxDhdd/CEEiqIU+/VZ8bn82eUVedoVDV9j9Rl946+Mv+LN+YvLRDsSdeOTcXuKPdFmGpVYop2rb6TaGu0EJTqy+g/QXpGMrdzy0xYteEt44u39tkQrTRjPj68m3AdkSNKCCSVvjmgnfvoEUflGQH3w5C2aQty1Bk0o8Ja5XaGyQryZWxWarYKBA1IGdAdor6+CJWDWl2IWWtgqWBIVCtDVzlB06hGeaJOu8mARj06BcjPVhFhsEEfK+LatMhpaJJm8BTds9RY0GEe+Qr3MWG+3uFqGITHT60b31dtNmV0ShCuMXU1JVrD5cjTbrDtTBdO8ANg1Qjr72yGcqDKSlhz21dsAY2sqZ62VbTDtDjfUY8uLwLazw+m/Ulr5Rue5jC3s2F1jf8vK0gRR7mu77xPoFrD3UKHFMu5ljTp2tnbTmLc1P0oWNEg6O8Zy4LVdnLK4rmhlvbis0/hQY9q23tV89vG/fPkNrAyN5zyzGf0AAAAASUVORK5CYII="><br>📱 Scan DOI
</div>

> 黏液瘤**以心室頻脈表現極罕見**；結構異常＋心律不整，心臟腫瘤需納入鑑別。

---

# Case #4｜嗜鉻細胞瘤破裂擬似急性冠心症候群

## [Hananias FE, et al. JCEM Case Rep 2026;4(8):luag207](https://doi.org/10.1210/jcemcr/luag207)

- 64 歲高血壓女性：胸痛、ECG 變化、心肌標記升高 → **初判 ACS**
- 冠脈攝影**無阻塞**；血壓忽高忽低；右腎上腺腫塊＋**腹腔內出血**
- 尿液間甲腎上腺素升高確診**嗜鉻細胞瘤**；α 阻斷後手術切除，恢復良好

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABQklEQVR42u1YMY4EIQyLlgfwJL7Ok3gAUtZ2YLrd4oqTi0UUg2gsO3bIRH5YO343X29WYLWcucYObp7x8YpP679ugG0AI7AJGI8N5+WCDSyRN7IIArOtaG7YrqZ+2BLfu0+gssKWj45ygVO9yaek62wjn97V5NboN108NL1lNqjvQtU5YSN789bePJ610JSpG30SFWqvz1LWxQtdTaELEnvWsMEmY3bqCN5K0x0+2Uu3bskKIxh5QWXGvCVjWf3UK98KD0M41Lxc6u2pNCDkpr7pkyEAE0rgsq3P+02B9rSGqCQxqTcWGPdQ8OZ5yDnlWz0syxTNJUPKp0PpUe1+2MwyNWelSCvPDqMMqXeveIsrq9UsQ64OjVZeqNd46GE5ZY10m7PaGZzN5qxTckzg6DY9685ZgAR4GgNtev3vf9Vfbt7VbtmDh7bxrwAAAABJRU5ErkJggg=="><br>📱 Scan DOI
</div>

> 「血壓劇烈波動＋非阻塞冠脈＋腎上腺腫塊」想到嗜鉻細胞瘤；**術前 α 阻斷**是安全手術關鍵。

---

# Case #5｜右側 IE 併敗血性肺栓塞與續發氣胸

## [Nasreddine F, et al. Radiol Case Rep 2026;21(10):4633-6](https://doi.org/10.1016/j.radcr.2026.06.149)

- 32 歲靜脈藥癮男性，右側**感染性心內膜炎 (IE)** 併 MRSA 菌血症
- **空洞化敗血性肺栓塞 (SPE)** ＋**續發氣胸**致急性呼吸惡化

<div class="qr">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABl0lEQVR42u2YS27EMAxDjeYAOZKvriPlAAJUkVQy3bSboigXYwwGsbMhFPrps+r7lev98ncvr9XrwGP/B7Zn4Wjt/Fg/rP942Wp3q26164yqoGZs+9xTbYfxYEipPI4L28NZLYO57sC6q2VUE46dUNuqhW/530snxr4lE+DV18+XCbPaBkHfxhNnS7VRhEC2Y1vwGXo+XNU2uxL4wteHXQleHFreMhm1wIGlXIaAV9kSrFNYhxSmVXawZQI/ugB7kGC6bunpBNYzKfDqrlGwqxO+0EAGoCVsbxkUkga4ZUUgrO3K28opaNeoFX5NfRsCLJDLgiEfCHvmMoCr79rOu4loD9sygV9/8WaBXeh0Toq3VCuFzAvQnCwVfHPZGUTuVheJqCq8nk5gbaB4wrcU76uWV2zUkl0isGkuU/JCRqucbmIbM4ENL1tIlTfa+vZlmH7cveSk4DKe1YTIoOnHFA/GsxpdLsyXrjk3ntWIWvEY2LZi1GRJVSK7s+1bMc6sRu3DVIy+84RhQoi6Sd+Wbxf5Hrn/0ctPe7Cfn6/zQlcAAAAASUVORK5CYII="><br>📱 Scan DOI
</div>

> 右側 IE 常併敗血性肺栓塞；**突發呼吸惡化**除肺栓塞外，警覺胸膜下空洞破裂造成氣胸。

---

<!-- _class: divider -->
# 💎 整合 Take Home
## 本週 7 大臨床啟示

---

# 💎 本週 Take Home（1/2）

1. **疾病修飾藥往青少年延伸（SCOUT-HCM）**：mavacamten 在青少年 oHCM 使 Valsalva LVOT 壓差多降 48 mmHg；n=44、替代終點、28 週。
2. **HFpEF 有了「照著走」的流程（2026 ACC 共識）**：SGLT2i 核心、GLP-1 RA 用於肥胖表型；主動確診並排除 phenocopy（別漏類澱粉沉積）。
3. **「食物即良藥」少見陽性 RCT**：MTG 多降 HbA1c 0.40%，大幅提升食物／營養安全；6 個月、替代終點。
4. **抗血小板往更早更精簡走**：原發 PCI 後即刻 ticagrelor 單藥出血更少（先導）；PCI 複雜度不改變單藥 vs 雙抗。

---

# 💎 本週 Take Home（2/2）

5. **穩定冠心去侵入化（MASTER）**：臨床＋運動心電圖以 NPV 98.2% 排除左主幹，免四成侵入攝影；「排除」工具、病例對照易高估。
6. **TAVI 三要點**：NOTION-3 次分析用病灶嚴重度／位置精緻化「哪種冠心該在 TAVI 前處理」；無症狀重度 AS 早介入多為經濟占優；**Vectorial Angle** 是 PPM 新 CT 預測參數。
7. **瓣膜介入「器械會互相影響、影像規劃是核心」**：功能性 TR 用 **RACI** 量化預後；中度 MR 的自然病史界定介入時機；三尖瓣 TEER 後需節律器採**保瓣式（無導線／LBBAP）**。

> ⚠️ 讀書會共筆整理，非精選專家意見；臨床決策請依病人實況與最新指南。

---

<!-- _class: ref -->
# 📖 參考文獻（1/2）

**Top 5 Picks**
1. Rossano JW, et al. Mavacamten in Adolescents with Obstructive HCM (SCOUT-HCM). [*N Engl J Med* 2026;395(4):362-373.](https://doi.org/10.1056/NEJMoa2601103) PMID 41910394
2. 2026 ACC Expert Consensus Decision Pathway: Management of HFpEF. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.06.018) PMID 42494134
3. "Food Is Medicine" Intervention on Glucose Control in Medicaid-Insured T2DM: RCT. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.125.077982) PMID 42478360
4. Yosofi B, et al. Ticagrelor monotherapy vs DAPT after primary PCI: STOP-IMH pilot. [*EuroIntervention* 2026;22(14):e773-83.](https://doi.org/10.4244/EIJ-D-26-00421) PMID 42200636
5. De Carlo M, et al. Clinical + stress ECG to exclude left main disease: MASTER. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag464) PMID 42489631

**TAVI Section**
6. PCI outcomes by coronary stenosis/location in TAVI: NOTION-3 substudy. [*Circ Cardiovasc Interv* 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016286) PMID 42495729
7. Genereux P, et al. Cost-effectiveness of TAVI for asymptomatic severe AS (9 countries). [*Eur Heart J Open* 2026;6(4):oeag115.](https://doi.org/10.1093/ehjopen/oeag115) PMID 42494367
8. Dogan M, et al. Vectorial Angle predicts PPM after balloon-expandable TAVI. [*Am J Cardiol* 2026.](https://doi.org/10.1016/j.amjcard.2026.07.009) PMID 42486382

---

<!-- _class: ref -->
# 📖 參考文獻（2/2）

**TEER Section**
9. RACI: Prognostic Marker in Functional TR. [*Circ Cardiovasc Imaging* 2026.](https://doi.org/10.1161/CIRCIMAGING.126.019813) PMID 42478366
10. Natural History of Moderate & Moderate-Severe MR. [*JACC Adv* 2026.](https://doi.org/10.1016/j.jacadv.2026.103057) PMID 42492126
11. Azañón-Cantero P, et al. Valve-Sparing Pacing After Tricuspid TEER. [*Pacing Clin Electrophysiol* 2026.](https://doi.org/10.1111/pace.70373) PMID 42482367

**Honorable Mentions**
12. Prado GFA, et al. P2Y12 monotherapy vs DAPT after complex PCI: NEO-MINDSET substudy. [*EuroIntervention* 2026;22(14):e765-72.](https://doi.org/10.4244/EIJ-D-26-00409) PMID 42200630
13. Garagoli F, et al. Peripheral artery disease: advances in medical therapy. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag516) PMID 42466921
14. Caffeine and Cardiovascular Disease: AHA Scientific Statement. [*Circulation* 2026.](https://doi.org/10.1161/CIR.0000000000001454) PMID 42473796
15. Farina J, et al. Endotype-guided therapy in ANOCA. [*EuroIntervention* 2026;22(14):e784-94.](https://doi.org/10.4244/EIJ-D-26-00148) PMID 42473746
16. Optimizing PFA: 1,000-Patient Cohort. [*JACC Clin Electrophysiol* 2026.](https://doi.org/10.1016/j.jacep.2026.06.011) PMID 42489615
17. AF and Out-of-Hospital Cardiac Arrest: Danish Cohort. [*JACC Clin Electrophysiol* 2026.](https://doi.org/10.1016/j.jacep.2026.06.009) PMID 42496631

**Case Reports**：18. TAVI-in-TAVI [10.1002/ccr3.73225] ｜19. 消融冠脈痙攣 [10.1016/j.jacep.2026.06.021] ｜20. RA myxoma/VT [10.1016/j.jaccas.2026.109422] ｜21. 嗜鉻細胞瘤 [10.1210/jcemcr/luag207] ｜22. 右側 IE/SPE [10.1016/j.radcr.2026.06.149]

---

<!-- _class: abbr -->
# 縮寫對照（1/2）

| 縮寫 | 全名 | 中文 |
|------|------|------|
| HCM / oHCM | (obstructive) Hypertrophic Cardiomyopathy | （阻塞型）肥厚型心肌病變 |
| LVOT / LVEF | LV Outflow Tract / Ejection Fraction | 左心室流出道／射血分數 |
| HFpEF | HF with preserved Ejection Fraction | 射血分數保留型心衰竭 |
| GDMT | Guideline-Directed Medical Therapy | 指引導向藥物治療 |
| SGLT2i / GLP-1 RA | SGLT2 Inhibitor / GLP-1 Receptor Agonist | 相應藥物類別 |
| MRA | Mineralocorticoid Receptor Antagonist | 礦物皮質素受體拮抗劑 |
| MTG / HbA1c | Medically Tailored Groceries / 糖化血色素 | 醫療客製食材／糖化血色素 |
| PCI / STEMI | Percutaneous Coronary Intervention / ST 段上升 MI | 經皮冠狀動脈介入／STEMI |
| DAPT / MACCE | Dual Antiplatelet Therapy / 主要不良心腦血管事件 | 雙抗／MACCE |
| IMH / BARC | Intramyocardial Haemorrhage / 出血分級 | 心肌內出血／BARC |
| CCS / CAG | Chronic Coronary Syndrome / Coronary Angiography | 慢性冠心症候群／冠脈攝影 |
| CCTA / EST | Coronary CT Angio / Exercise ECG Stress Test | 冠脈 CT／運動心電圖 |
| LM / LMCAD / NPV | Left Main (CAD) / Negative Predictive Value | 左主幹（病變）／陰性預測值 |

---

<!-- _class: abbr -->
# 縮寫對照（2/2）

| 縮寫 | 全名 | 中文 |
|------|------|------|
| TAVI / TAVR | Transcatheter Aortic Valve Implantation/Replacement | 經導管主動脈瓣植入／置換 |
| AS / aSAS / AR | (asymptomatic Severe) Aortic Stenosis / Regurgitation | （無症狀重度）AS／主動脈瓣逆流 |
| QALY / PPM / MSL | Quality-Adjusted Life Year / Permanent Pacemaker / Membranous Septal Length | 品質調整生命年／永久節律器／膜性中隔長度 |
| RBBB / FFR | Right Bundle Branch Block / Fractional Flow Reserve | 右束支阻滯／血流儲備分數 |
| TR / MR / TEER | Tricuspid / Mitral Regurgitation / Edge-to-Edge Repair | 三尖瓣／二尖瓣逆流／緣對緣修復 |
| TTVR / CMR / RACI | Transcatheter Tricuspid Valve Replacement / CMR / Right AV Coupling Index | 經導管三尖瓣置換／心臟磁振／右房室耦合指數 |
| LBBAP / TEE / ICE | LBB Area Pacing / Transesophageal / Intracardiac Echo | 左束支區域節律／經食道／心臟內超音波 |
| PFA / AF / OHCA | Pulsed Field Ablation / Atrial Fibrillation / Out-of-Hospital Cardiac Arrest | 脈衝場消融／心房顫動／院外心臟停止 |
| ANOCA / SAQ-7 | Angina Non-Obstructive Coronary Arteries / Seattle Angina Q | 非阻塞冠脈心絞痛／西雅圖問卷 |
| PAD / PCSK9i / ACS | Peripheral Artery Disease / PCSK9 Inhibitor / Acute Coronary Syndrome | 周邊動脈疾病／PCSK9 抑制劑／急性冠心症候群 |
| VT / IE / SPE / MCS | Ventricular Tachycardia / Infective Endocarditis / Septic Pulmonary Emboli / Mechanical Circulatory Support | 心室頻脈／感染性心內膜炎／敗血性肺栓塞／機械循環支持 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**
心臟內科｜結構性心臟病介入

> *本文件為讀書會共筆之教學整理，僅供醫療專業同仁臨床教學交流參考，不作為個案診療依據。*
