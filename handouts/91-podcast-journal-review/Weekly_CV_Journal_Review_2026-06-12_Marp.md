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
  /* Disclaimer blockquote sits on a dark lead slide; force dark text so it
     stays readable on the light box (otherwise it inherits section.lead's
     light text colour and becomes invisible). */
  section.lead blockquote,
  section.lead blockquote p,
  section.lead blockquote strong { color: #2d3436; }
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
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-06-05 ~ 2026-06-12'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-06-05 ~ 2026-06-12

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Top Pick 附 QR Code，可掃描跳轉原文

---

# 🎯 本週主題

## 影像引導 PCI 的中立衝擊 × CKM 症候群首部指引 × Finerenone 腎臟保護版圖擴展

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 結構性心臟病主動脈瓣方向
3. 🔧 **TEER Section** — MitraClip / PASCAL / TriClip 進展
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — JACC Case Rep 精選 × 5
6. 📖 **參考文獻 + 縮寫對照**

> ⚠️ EuroIntervention：本週無新收錄文章（PubMed 查詢結果為零）

---

# ⭐ Top 5 Picks 一覽

| # | 試驗／研究 | 期刊 | 結果方向 | 關鍵數字 |
|---|-----------|------|---------|---------|
| 1 | **2026 AHA/ACC/ADA/ASN CKM 指引** | *JACC* + *Circulation* | 💡 Concept-shift | 4-stage 框架；PREVENT 方程式 |
| 2 | **INFINITY**（Finerenone IPD 統合分析） | *Lancet* | ✅ Positive | 腎臟終點 HR **0.76**；CV 終點 HR **0.80** |
| 3 | **OPTIMAL**（IVUS vs. Angio，LMCA PCI） | *N Engl J Med* | ❌ Negative | HR **1.11**（0.87–1.42）；P=0.40 |
| 4 | **IVUS-CHIP**（IVUS vs. Angio，複雜高風險 PCI） | *N Engl J Med* | ❌ Negative | TVF 13.9% vs. 11.1%；HR **1.25**；P=0.08 |
| 5 | **ABYSS 心率次分析** | *Circulation* | 💡 Concept-shift | 高心率組停β-blocker後 MACE **9.2%** vs. 5.5% |

---

<!-- _class: divider -->
# Pick #1
## 2026 AHA/ACC/ADA/ASN CKM 指引
### Cardiovascular-Kidney-Metabolic 症候群首部聯合指引

---

## [Ndumele CE, et al. J Am Coll Cardiol / Circulation. 2026](https://doi.org/10.1016/j.jacc.2026.03.056)

| 項目 | 內容 |
|------|------|
| **文件性質** | 首部四學會聯合臨床實踐指引（AHA＋ACC＋ADA＋ASN） |
| **核心概念** | CKM 症候群 = 代謝風險因子（肥胖、T2DM）＋ CKD ＋ 心血管疾病的相互影響連續體 |
| **4-Stage 框架** | Stage 0：無危險因子；Stage 1：肥胖＋前糖尿病；Stage 2：代謝＋CKD；Stage 3：亞臨床或臨床 CVD |
| **風險評估** | 採用新版 PREVENT 方程式（PREVENT-CVD / PREVENT-ASCVD / PREVENT-HF） |
| **介入策略** | GLP-1 RA / SGLT2i / Finerenone 跨心腎代謝保護；Stage ≥2 全族群適用 |
| **重要意義** | 心臟科、腎臟科、內分泌科需建立整合照護路徑 |

> 💡 Stage ≥2 患者，無論有無糖尿病，均應考慮 SGLT2i 或 GLP-1 RA

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABfElEQVRYhdWXsZGEMAxFxRA4pARKcWfg0iiFEggJPP6nL5ndu9vZGKHAA34ECL6+ZJGvsYIh46nXQ+XGYDstAFnE784JZahpzzAuwckI7Kvougkz0bVOQHkCYT6b8nMGnkNE0pGBKvNHpjGJa6emQ9YmTv6o6kbi1UiSS9Nvvf2r05jkHazDBNXJR8QjzGfnwnxso43HTB6ZqK4PVUr366SK5qPd+cISu4MS9WutRsnFFS+hiQe6U9uz8L9wP6Efs5fQlV/vO6PEJotpo71dWfnUtROX+FwE+rWHVqP+kiKhySLcM0XD6nCFPRudyMR59OV8b+1EJqqd+dqz+Y5Z5dJCkN63TRXOD3U5iU5cIRNnZeso3FijE+0i8Nnewhp5RgtNPIZ6zUiqcQo9OOHrM59TLvfwCV9CE5/9ed7O5NbLe/+5n1wnPa1A2Lf+7SHBic8Z5ic8U1EnTyB0vuHqgwhPxLVM5wO1o6qZ7EwVmfRqNCKSqJqR2olNvsYP74388Nu780YAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# Pick #2
## INFINITY
### Finerenone IPD 統合分析 — 廣譜 CKD 腎臟與心血管保護

---

## [Neuen BL, Heerspink HJL, et al. Lancet. 2026;407:2375–2386](https://doi.org/10.1016/S0140-6736(26)01009-3)

| 項目 | 內容 |
|------|------|
| **設計** | IPD 統合分析；3 個 RCT：FIDELIO-DKD + FIGARO-DKD + FIND-CKD；n=14,574 |
| **族群** | 平均年齡 63.7 歲；平均 eGFR 56.4 mL/min/1.73 m²；中位 UACR 567 mg/g |
| **主要腎臟終點** | 腎衰竭＋eGFR 下降 ≥57% → HR **0.76**（0.68–0.86）**−24%** |
| **主要 CV 終點** | HF 住院＋CV 死亡 → HR **0.80**（0.70–0.91）**−20%** |
| **全因死亡** | HR **0.88**（0.79–0.99）**−12%** |
| **一致性** | 效益在糖尿病／非糖尿病、各 CKD 病因、各 eGFR 及蛋白尿分層均一致 |
| **安全性** | 高血鉀症較多但住院率低；SGLT2i 併用不影響效益 |

> 💡 FIND-CKD 涵蓋**非糖尿病** CKD — Finerenone 效益與糖尿病狀態無關，適應症將大幅擴展

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABk0lEQVRYhdWYPY6FMAyEjSgoOQJH4WYvHI2jcISUFCjemTH7BMWrMZY2Qvm2yM/Ynjyzn1GcYTbUeemOYZu900xLQD5aIOaqmR8D5rqDU8lJ774VfmMnIKt1x+i+vIHg5HELOn5/D7F+x4461/gGEtrxfXQo3ibewk1VD5Jyni+zsfX7tJZ7nuYkZ+DEV6p70niNlIT72TDs42pBWl/FU5MjVh/12iZnTm7STmLCOSsadRfSvf3/d1aCC6ixenbFnXnq3/t5mNilKjdjL6FOfMlN2PVYgxnqgOjhoxSSmqB/TB71OoTRpBPLTQ7TnHbCDlicui65CWI8K1+xu6oSk6L9eHgkuGi4UqQA1f88gROqE7p0eGW6DeurzVh1bkLPpspHnWxUepVCchN8lPBI0osa+ewtNYno1GviDQihX5xdTvL1o07dy4/K4VtqEt4ffyPn4ju6TAISfVvv6XhVX2pIesJsdCmksSq7vYGwXvMXF5CI5ETa0X7c5fAbspHdMDM5sxE+A5VPL1d4pG1ecpOf8Qc+0TXJWiWxPgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# Pick #3
## OPTIMAL
### IVUS 引導 vs. 攝影引導，非保護性左主幹 PCI — ❌ Negative

---

## [Testa L, De la Torre Hernandez JM, et al. N Engl J Med. 2026;394:2189–2199](https://doi.org/10.1056/NEJMoa2600440)

| 項目 | 內容 |
|------|------|
| **設計** | 國際多中心開放標籤 RCT；28 個歐洲中心；中位追蹤 **2.9 年** |
| **族群** | n=806；平均年齡 71.4 歲；78.4% 男性；34.7% DM |
| **隨機分配** | IVUS 引導（n=401）vs. 攝影引導（n=405） |
| **主要終點** | 複合：中風＋MI＋任何血運重建＋死亡 |
| **結果** | **33.7% vs. 30.9%；HR 1.11（0.87–1.42）；P=0.40** |
| **分項** | 死亡、MI、血運重建個別分項均無顯著差異 |

> 💡 高容量中心高品質攝影引導可能已達臨床可接受上限；**常規 IVUS 引導 LMCA PCI 尚無 RCT 支持**

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABmUlEQVRYhdWYMbKDMAxExVC45Ag+im8W+2gchSNQUjAou5LhJ38mNcIFQ3gUyF6t1xH5OapyiKS1qO5pKTrYkyMAedkHDnta+0s67HwUnIyqS+V94bOsbdgn1fYEgplfS+MqsLanEBk3VDTolrkKDyCuHd0mbd6F/1R1I6ldy+jGdoxbnut3n8YkfWDGZzk44/Xb5WIS1rPgsk0zf6KeY1xxjU1MO1CK+zWcpPHVS1VRyQita/frPSmdz1chMsECrPx69+sEBQ16rc/N5CXp05XVdUI/iUx8ZqFr6ffcS0whkYn7tWvDnATdqOqVBibUNfY7gYegKqhGrarYpKIPs7pfMyP9aScycedTKp7Ol1mVLuVMGzeT1FMndWJfPa7wZolNsFfn5nuJcTrfqZ24RKgQJDvpzmcbebHTVFxy1sAi6HysavpIdjFJz6M9RafrXCKhifs1ziUT8yjSEVTzucvcSvpJz1Nnshq6hzyBSE+dVE3mfxrPIO582kdwYtrxPrQ8Wg9043UuCUrObmQetflv1H1pscnP8QZvslINOKyjmgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# Pick #4
## IVUS-CHIP
### IVUS 引導 vs. 攝影引導，複雜高風險 PCI — ❌ Negative

---

## [Diletti R, Daemen J, et al. N Engl J Med. 2026;394:2200–2211](https://doi.org/10.1056/NEJMoa2601521)

| 項目 | 內容 |
|------|------|
| **設計** | 研究者發起、國際多中心 RCT；7 個歐洲中心；中位追蹤 **19.0 個月** |
| **族群** | n=2,020；平均年齡 69 歲；79.4% 男性；27.4% ACS |
| **複雜定義** | 重度鈣化、骨質增生、分叉、左主幹、CTO、ISR、病灶 >28 mm 或需 MCS |
| **主要終點** | TVF：心因性死亡＋目標血管 MI＋目標血管血運重建 |
| **結果** | **IVUS 13.9% vs. 攝影 11.1%；HR 1.25（0.97–1.60）；P=0.08** |
| **手術時間** | IVUS 88.8 分鐘 vs. 攝影 66.2 分鐘（**+22.6 分鐘**） |

> 💡 即便在高技術中心＋嚴格最佳化標準下，**常規 IVUS 引導複雜 PCI 仍無強力 RCT 支持**；選擇性應用仍合理

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABk0lEQVRYhdWYQa7DIAxEjViw5Ag5CjcLHC1H4QhZskC4HkP60y91XQepacrrojbjsVOiryszFlE4E3MPNbHTnWGA7PoDXQ/n+hK7ji3jxDPXjPuEvY2L65G5PIFI5s9UcAqI7SmEfJOIHLcNp/AAMrXDLXKZVfhPVT8keWlZqrEM37Yjf9apTbKWZPyggYznT5ezSRBPlUuLBz5KPMOfcn0AocuvxUnK3BimCdwDmVe/7oHhfPMUTBP0F4K+EzqkKMjxPIXfk923CH9brsxTJ/ATy0RvVn71il5SZ4R2yS6Zr3mQakMkjWqUN0RqmKC/VBqqmqEewhqVbbJrHTp1PvTtm6oMk9wJUrmcTwicT/qkAfI3dcLfQMif4s1km0DXWodwPq1JsemlENNkTkTL+bQlJh6myRWDzsorqnib7GyS9zyqbhfezyVkmszZX14R86jISO6vLvNzsp705tQZNIa7hxgntKZOqGbDfxoPINr14Hy8lnGi2tFnQFW3TBtSjTqPGiarGnEKRfNfoPtUbJOv6wUzGiHQt4HaCAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# Pick #5
## ABYSS 心率次分析
### β-blocker 中斷後的心率與 MI 後預後

---

## [ABYSS Secondary Analysis. Circulation. 2026](https://doi.org/10.1161/CIRCULATIONAHA.125.078635)

| 項目 | 內容 |
|------|------|
| **設計** | ABYSS 試驗預先設定次分析；β-blocker interruption vs. continuation post-MI；n≈3,698 |
| **族群** | 穩定 MI 後患者（距 MI ≥6 個月），LVEF ≥40% |
| **心率分群** | 低：<60 bpm｜中：60–67 bpm｜高：≥68 bpm |
| **MACE（心率梯度）** | 低心率 **5.5%** → 中心率 **6.4%** → 高心率 **10.4%**（P<0.001 for trend） |
| **停藥影響** | 停 β-blocker → 心率↑ ~10 bpm；血壓↑ 3.7/3.9 mmHg |
| **臨床意義** | 高心率患者停 β-blocker 危害最大；低心率患者停藥相對安全 |

> 💡 **停藥前先量靜息心率**——心率 ≥68 bpm 的 MI 後患者應維持 β-blocker

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABnElEQVRYhdWYva3DMAyEaahwqRE0ijaLNJpH8QguXQhi7kjnPSRA6tAshESfC/0cj7RFvkZThsh61L6Mda+62MwMQB62QMwdIsuQoooREZwk1b3xd9WZlPsZWbXfgeDkcQs8/U3uQySddhfc1y2Ia0fPTNVA8f1DVT8kno3Ude0znWVr73kak1yRqI0pK8aPCEm4nx3DmTeO8JCZDuwqNoFTQ8WvW8BjzMmd2olMqPgCpdCvX0/5LUQmbaxYPv9VVkg6n17383PywHoL08/qthTTddEemzTspHQ/XOhE4SEjm0IiEzg1lo9akqFo+LU0V7eEJpzbmZV5c/9rSl232ISKRwzX+vmmnbjkYfsxxeMu6Hl0vmp9yO+JHjhZG69anQ6pturIBJ2bqDnfYlUEzmcKCU9sPzx5uQp51RmaeNBJOHIOiakanHD51o+yYqv3+dmcLzLx3l/M+abfiHiVCUD8TW+QLO51/x4SneCU7a3aVVP4TeMGhF8w2l+vrOGJacc6/OvNdSIbvR+NS17ZCL+m87Fu8+tLj02+xhMdF1IjqU/fpwAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 本週 TAVI 相關文獻
### 結構性心臟病主動脈瓣方向

---

## [中度 AS + MR 雙重病變：重塑與臨床結果 — JACC CV Imaging 2026](https://doi.org/10.1016/j.jcmg.2026.04.015)

**PMID: [42274428](https://pubmed.ncbi.nlm.nih.gov/42274428/)**

| 項目 | 內容 |
|------|------|
| **研究問題** | 中度 AS（Aortic Stenosis）合併 MR（Mitral Regurgitation）對預後的獨立影響 |
| **臨床背景** | 個別病灶均未達介入門檻，但合併出現時血液動力學惡化顯著 |
| **主要發現** | 合併 MR 的中度 AS 患者預後顯著較差；心室重塑更嚴重 |
| **Heart team 意義** | 不能只看單個瓣膜嚴重度，需整體評估雙瓣膜合併心室負荷 |

> **臨床 Pearl**：「每個病灶都不夠嚴重，但合起來需要更積極評估。」

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABiElEQVRYhdWXMZaDMAxEh+eCkiNwFN8M+2gchSNQUvCs1Ug42d281AgVTuKfwjKjkQC+RhEG0qHfh5Mbg+20AGSB/zomqcM5blmMIzhJIluBriuYia7nJFKfQJjPipaOWeQ5BBh3u//5I9OYxLVzjjtKg5M/qrqReDWS5Mq7Xv/VaUzyDt71KGv5dLp4hPlsXJiPbbS0z+SRyZKOaWMdgn49qqL5V3e+uMTzUaJ+Lar1XF3xCE28K8rl1NwYxJ9CBCJ0j0RXfp13lhqbLHbL7e3K6oLTSztRic0ZYlmhV6M+korQBP6pCtJ8WIdFbL6LTZhPdz70mHumUcmiqrl0D5/vaCrZpo37CfTUqmtXBSPtyHbqwMR6iQY9RKyjMLUSnPApFJ/tLay5ZGmhiQed2mck9RNMvya7mITH93m0u4dP+AhNfPbnQuc7rJdf/ed+cr3p0d/E3qpfHvIAwjq0vkLVzNTJA8jZnc/ykfAErmU6n1yz/WTvVJHJVY3izsesdEbaco1NvsYPhwEKPtDN6QEAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

## [女性退化性生物瓣：ViV TAVR vs. 再次手術 — Catheter Cardiovasc Interv 2026](https://doi.org/10.1002/ccd.70693)

**Tagliafierro M, et al. Columbia University — PMID: [42283239](https://pubmed.ncbi.nlm.nih.gov/42283239/)**

| 項目 | 內容 |
|------|------|
| **設計** | 單中心回顧性研究；女性患者 Valve-in-Valve（ViV）n=92 vs. redoSAVR n=40 |
| **30 天死亡** | ViV 1.1% vs. redoSAVR 2.5%（P=0.303）NS |
| **30 天中風** | ViV 3.3% vs. redoSAVR 5.0%（P=0.480）NS |
| **1 年複合終點** | 兩組相似；ViV 組再住院略高但 P=NS |
| **Propensity score matching** | 校正後結果一致 |

> 💡 ViV TAVR 與 redoSAVR 短中期結果相當；手術風險較高的女性患者 ViV 是合理選擇

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABh0lEQVRYhdWYMbKDMAxExbig5Ag+im+WcLQchSNQUmTQ310ZMj8zqREqGPCjwPZqJWP2M57OMBvX5v7mwKCRPQF56AOH97jqpYX3HEpOCh6fvG8O7i8b3pP7fAeClV/bjF2odyJWNsxo8O0uJLTj2+Qz7kT+qepCEtlIXbd5L/jqrzzNSXpgxV8W5MvmUhIZBy7b9MLTCA/ZyyqemSCkmvDrEYqW/9memkDrmNRu8mtovc2heEtNqBplqPxaeep9Fy4nPRu7K0MhjMp3MxP48bSY+gxTBUTdnkI7mYmNmg/9WtpANh77kpdQ15UVGx4CJ4Fqor/LTXq3ISLnO7WTm1A7Ury0z1n50tSHXE7gbFXZSJdTlBUuZ7lJwRiykbWk98oceOYnVR3R0SNpF3xPTSK0C+xEK8+D6JWTk6PKfJwvOnxLTaL3j35UpymoJqpMAtL9LU6mXOuPu6QnqCjScvV+tTuQ8w9GuHZ6Ytb/uzS6Ns9UyEYqKDM5s5HOZyNVU6id3ORn/AHziHoANY1NIwAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

## [TAVR 圍術期持續 vs. 中斷口服抗凝劑：統合分析 — BMC Cardiovasc Disord 2026](https://doi.org/10.1186/s12872-026-06116-w)

**Gan X, et al. — PMID: [42277686](https://pubmed.ncbi.nlm.nih.gov/42277686/)**

| 項目 | 內容 |
|------|------|
| **設計** | 系統回顧＋統合分析；5 個研究，n=3,316 |
| **主要大出血** | 持續 OAC（Oral Anticoagulation）**不增加**主要出血風險（RR NS） |
| **主要血管並發症** | 兩組相似 |
| **中風** | 持續 OAC 顯示邊際性降低中風（borderline significant） |
| **裝置成功率** | 持續 OAC 組略高 |
| **局限** | 研究數量有限，以回顧性設計為主；需更大型 RCT |

> 💡 AF 患者 TAVR 圍術期持續抗凝可能安全，甚至可能降低中風，但現有證據仍不足以強力建議

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABj0lEQVRYhdWXMXLEIAxFxbig5Ag+CjcLHI2jcATKLRgUfYndTTLZ2jKFx/g1CH99SUQfV2EsOh7yGiY+BP2yHJAvst0jceUZ++bknBzMvZA8G4UZJZIwE3O9A0E8IHS2ch9CFEeGgk6utyCmnRmHqkbJL1VdSCwbQXJdcur2J099kvfKzFDIP07njyCejofEY9m4jiFR3YDQMr/G9Vf9sLXjlUg2itaFJGg99rwVT66JxDPOqn5dVPEU+PUXLibw466nxi52PbA4iW8CP5Z41JW3h8ykCvFMxK+TVsBXj7QOqJtcE9nJ8YN6CO6/FVbum4jWxyk1Jarzbb827TgmReJRtxuqcenv4HxSJx2Qp0KgCtQSOfUxKP/Qjk8SUT8kqlbsrgNCK87JriXwa+uV9S/wck1swUOsR5J5UMTEzgmOj35UfWPPr0mdzzOx3t+qjE2uSIH3VHApeU56lK0T4peH+Cdz6+RU1ahObkC28+l0oss5Ue2gesPzrLdP3IpvsrNR4yHtjsQFe66+ycf1DSBcco7Qzl22AAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 本週 TEER 相關文獻
### MitraClip / PASCAL / TriClip 進展

---

## [T-TEER 術後腎功能改善：跨 CKD 分期分析 — Clin Res Cardiol 2026](https://doi.org/10.1007/s00392-026-02961-z)

**Becker M, et al. Robert Bosch Hospital Stuttgart — PMID: [42262550](https://pubmed.ncbi.nlm.nih.gov/42262550/)**

| 項目 | 內容 |
|------|------|
| **設計** | 回顧性單中心；n=181，2021–2023 年；嚴重 TR（Tricuspid Regurgitation） |
| **手術** | T-TEER（Tricuspid Transcatheter Edge-to-Edge Repair），TriClip |
| **eGFR 改善** | **+4.8 mL/min/1.73 m²**（IQR 3.1–6.5）；P<0.001 |
| **AKI 率下降** | 各 CKD 分期均顯著下降：Rate Ratios **0.18–0.39**（降低 60–80%） |
| **各 CKD 期一致性** | 幾乎所有 CKD 分期均見腎功能改善 |
| **伴隨指標** | GGT 及血鉀下降（充血改善） |

> 💡 重度 TR 所致腎靜脈高壓是可矯正的腎損傷機制；T-TEER 解除充血帶來實質腎保護

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABh0lEQVRYhdWYsZGEMAxFxRAQugSX4s6wS6MUSiDcgLFO/8uwc3ez8QoH7MIjQOLrS0bk46qKJfPL/k8nLky80gOQVfzslbTpuexFySU4mVX3KnbcLJ5FtU1nsuMTCOLZqp6SwZ9CRJajNFPQU4hr51wOueP5paovEq9GkNI6nvpPncYk78U6NPLf6eIRxLPjYPGYh+hW+3yQRybuG939GulvuBXaCU3UrpnzmV9DQXtprngJTbwrdvh1HR6i/ha+T1YjGX074WzZ+bxZW2ziy3U9PORMVEhksgqcmrquPiPhjTDS4CQ3qLsg85ndG0oPTYTx4Jd1aIp/aycuoeKbDt8wv4aOzEl6BIJcq/sxHNqeej6Y99hEEqY19D7PtTnf0E5gwi7CCd8JG3nRHpr4YjUq5lG7ywLU4GTMo4rU335N54tMfPb3fYmOefTqMl8n105v+BuDGO4SnmA3BZ1kqoY6eQC5ne9awQm1Y/lP3LOa83Wrxq3GJlc14msRZiTMd9BObPJx/QCGwR47FxPcTQAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

## [M-TEER 術後 FSV 的差異：心房型 vs. 心室型繼發性 MR — Clin Res Cardiol 2026](https://doi.org/10.1007/s00392-026-02950-2)

**Grewe F, et al. University Hospital Regensburg — PMID: [42257863](https://pubmed.ncbi.nlm.nih.gov/42257863/)**

| 項目 | 內容 |
|------|------|
| **設計** | 回顧性單中心；n=103（Ventricular SMR n=60；Atrial SMR n=43） |
| **心室型 SMR FSV** | 術前 49.4 vs. 術後 49.5 mL；P=0.960（**無改變**） |
| **心房型 SMR FSV** | 術前 60.5 vs. 術後 66.8 mL；P=0.037（**顯著上升**） |
| **FSV 改善預測因子** | 心房型 MR（OR 5.12；P=0.048）＋低基礎 FSV（OR 0.36；P=0.002） |
| **預後相關性** | FSV 改善與降低死亡率或 HF 住院**無顯著相關** |

> 💡 心房型 SMR（HFpEF＋AF）行 M-TEER 後 FSV 可改善；FSV 為血液動力學適應指標，非獨立預後標記

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABjUlEQVRYhdWYu7WEMAxEtYeAkBIoxZ0tLo1SKMEhAQe9mZGX9zsbr1BgPpfAgvFIxuxtLM6wYcf54+CNh+6cCcjT4mqfvPoxbsXFLTkZ3LfFMK7G0evjmDDegTCflV9h5ngXYja2UvHy70JCO8fYIP6ezy9VfZDEaiQp9Rz2ef2zTnOS7yhVCln+O10+wnw2Do1k9HU5hyaencA3fA8F4ZyPXtpJSrAa28wqM3EFwq9rKN5SExwn5SC/3rlOPb5CAoK3HLOGNjBrTXj2mps8VfW6K4eHHNNLIWkJ9TD7OYSuaR1nfzY10WrEVSv0aOTj4rkJ+qIWtbH79aWdzOQJrW/mdD4E/NrofEV9yMeJjZo1nMSdtQR5NGNXlJpoRyLne/VIePlUSHIybfA8e/XKKuTUeGYSQdcuznywH9QHyU3UbTicBAq6/FrOl5lE78/9duTDWt7rz+dJ3+l59zcl0d3lDkQ6maUa6eQGRP2deuUeyYm08/NfwImHqKDM5FqN+uPCnSA6j63U3ORtfAHtkWviuYooxAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得讀
### 本週精選 6 篇

---

<!-- _class: small-text -->
# 📚 Honorable Mentions — 其他焦點

| 主題 | 重點 | 連結 |
|------|------|------|
| **GDMT 停藥 in HFimpEF：Meta-analysis + TSA** | 3 個 RCT；HFimpEF 中停用 GDMT → EF 再度下降風險顯著↑；停藥前需充分依據 | [JACC Heart Fail. 2026](https://doi.org/10.1016/j.jchf.2026.103172) |
| **Vericiguat 與 HFrEF 反覆住院／死亡** | HFrEF 新分析；Vericiguat 對複發性 HF 住院及死亡的效益評估 | [JACC Heart Fail. 2026](https://doi.org/10.1016/j.jchf.2026.103171) |
| **Statins → 降低老年退伍軍人 Frailty 發生率** | n=987,301；追蹤 5.3 年；Statin 使用 Incident Frailty（虛弱症）顯著減少（HR **0.76**） | [Eur Heart J. 2026](https://doi.org/10.1093/eurheartj/ehag451) |
| **TR 在肺動脈高壓（PH）中的獨立預後意義** | Mayo Clinic；n=1,318；中重度 TR 獨立預測死亡率，超出 RV 功能指標；PH Group 1–4 一致 | [JACC CV Imaging. 2026](https://doi.org/10.1016/j.jcmg.2026.04.016) |
| **心臟類澱粉沉積症（Cardiac Amyloidosis）屍體解剖盛行率** | Mayo Clinic；ATTR 型遠比臨床診斷率高，大量未診斷病例 | [Circulation. 2026](https://doi.org/10.1161/CIRCULATIONAHA.126.079522) |
| **Clopidogrel vs. Aspirin 單藥治療 post-PCI** | PCI 後雙抗結束後 Clopidogrel 與 Aspirin：MACE 及大出血均不劣於 Aspirin；韓國全國世代 | [JACC Asia. 2026](https://doi.org/10.1016/j.jacasi.2026.03.041) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## JACC Case Reports 精選
### 本週 5 則介入心臟科前沿案例

---

## Case 1｜急診 TAV-in-TAV：Evolut 功能失常合併重度 AR，表現如心肌梗塞

**Wells J, et al. University at Buffalo — PMID: [42283685](https://pubmed.ncbi.nlm.nih.gov/42283685/)**
🔗 [JACC Case Rep. 2026](https://doi.org/10.1016/j.jaccas.2026.108598)

| 項目 | 內容 |
|------|------|
| **患者** | 82 歲男性，既往 TAVR（Evolut 瓣膜），以胸痛＋ST 上升入急診 |
| **冠狀動脈** | 導管顯示無新病變 |
| **真正診斷** | Evolut 瓣膜急性重度 AR（Aortic Regurgitation）→ 血壓下降需升壓劑 |
| **處理** | 緊急 TAV-in-TAV → AR 改善 |
| **教學重點** | TAVR 術後生物瓣功能失常可以急性 AR 表現，誤以為 STEMI |

> 💡 STEMI 等效表現的鑑別診斷：記得排除 TAVR 瓣膜功能失常

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABh0lEQVRYhdWYMbKDMAxE5aGg5AgcxTeLfTSO4iNQUjDer5UMf/7PpI5Q4SF+NBuv1kpEPlYBS6ZDH9PJjWQ7PQB5iX86FtR0zi3DuAQnE9CK6LqpnhmbpHMB6hMI9XBPVuA5RGTeM6DkTWlM4t45551+cfLHVV8k3o0kufbpWLd/fRqT/Fau6hPV9p508Qj1NC6qR3gKpU+7rrEJ06NJZ17bMypfNR/FJvsKy2uMszjHMUQmIksTupxep6qEcQpfJwl+lzCV7w5cUWOTl+uxDLFU1hRc2sjEwGS2GxD7NSN1c7eEJoV75m6djtiHBcZjE85FrXTrQ1x96K4KTNw7PkXz+9+ELZBrj0C0D5vNmxhTsky78F4JTWR2h6gSU8XkM4cEJ/DazCd+kWf00MQrjWmDb6mZgOCkmBZPPk8Pn/AlNPHZn4tmCA67y+/759vEf+mdJP1yy8iQ8AT31EnXrPTJAwiTz+bNPHozODHvjP8C6B11zYKtxCajG02PZghdM9E7scnH+gE3yBqX96mV3QAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

## Case 2｜同台：ViV TAVR ＋ Bioprosthetic Valve Fracture ＋ LAA 閉合（台灣案例）

**Chang JH, et al. China Medical University Hospital（台中）— PMID: [42283684](https://pubmed.ncbi.nlm.nih.gov/42283684/)**
🔗 [JACC Case Rep. 2026](https://doi.org/10.1016/j.jaccas.2026.108776)

| 項目 | 內容 |
|------|------|
| **患者** | 74 歲男性，外科雙瓣手術後，嚴重生物瓣 AS ＋ LAA 血栓（抗凝 6 個月仍持續） |
| **背景** | 近期消化道出血史，不適合長期抗凝 |
| **三步驟策略** | ViV TAVR → BVF（Bioprosthetic Valve Fracture）確認 → Watchman FLX Pro LAA 閉合 |
| **腦保護** | Sentinel 腦部保護過濾器取出血栓碎屑，無神經學併發症 |
| **教學重點** | 單次手術同台完成三項手術的安全性與步驟順序 |

> 💡 台灣中心案例：高出血風險＋抗凝禁忌的 LAA 血栓 → LAAO 為合理圍堵策略

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABkElEQVRYhdWXvbHEIAyExRAQugRKobOD0lyKSyB0wKCnlfD7u7nYMgFzx+cAwWoliD6OyhgUT/kZBhaCrkwH5EX279y4hZGOwsrJOYnMRyWZd4kn8U5hbMztCQTxYI0y83MIUeqFWchbpD6JaWekDr0Y+aOqG4llI0hpM555/5enPsnPKE10IrG9O50/gngOTBIP4RbqjF1m3wTnn3H+CEE0zg2fQjvOCbQDv+Z1F8NuwTOpopfcll9DOxT4up+7iaz1jLotrvydgZmbc0LwPPMQdWVxwU0V4plILenLN1aPNFXd5JsQyfYlEpLuCHlYWblzEq3KIA95/NaOa2La0fqC898Jzle027ifYJOibmzedh07FVOIXwJdoy8SD9HXCZzvUohfIrpGJOjt1fm0kBd7TbklNoJ2G1Pvwj71TbB9Xu++9XLVDp9cE+v9oRrtR7WWrypzP7GXnnX4lpOXh/gnjBTUrhOqydDJAwh6T+03i0XknZBpGc6n2hHVbLxX32RlIybJwATVRGjHN/k4vgCLvOfiAMN43gAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

## Case 3｜Percutaneous Stentectomy：TAVR 前取出凸入主動脈腔的冠狀動脈支架

**Nakhle A, et al. Henry Ford Hospital — PMID: [42283678](https://pubmed.ncbi.nlm.nih.gov/42283678/)**
🔗 [JACC Case Rep. 2026](https://doi.org/10.1016/j.jaccas.2026.108749)

| 項目 | 內容 |
|------|------|
| **患者** | 89 歲女性，計畫接受 TAVR |
| **問題** | RCA（Right Coronary Artery）開口支架凸入主動脈腔，可能干擾瓣膜釋放 |
| **技術** | Goose Neck snare 抓取並取出凸出部分 |
| **後續** | IVUS 引導重新置放 RCA 開口支架，後續順利完成 TAVR |
| **教學重點** | 極罕見技術：有意圖地取出已部署支架（percutaneous stentectomy） |

> 💡 TAVR 前冠狀動脈複雜管理的創意解法：Snare 取出凸出支架後再 PCI

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABkklEQVRYhdWYMbKDMAxExVBQcgQfhZvFPhpH4QiUKRiUXcn8zP+Z1H9R4Un8KJC9Wikx+xrVGTY+8XE4uDHEzilAHpbfnrO34Zi2xYObOBndt2pYV+Qz+WrDMbu3OxDmwz0r7vchZtO+uIN8ZKpJUjvHtFMvSX6p6h9JViPJ0s7xWdY/dapJ3rE06AS5fTqdHmE+GxfkY7yFeo47Vm1CpZQWfm10Em98lNpRJtibqRWu/S6Ofg3CJDzEqHJqnVkNnrcgQELCfPfVfiqweNMmqYpw5RauDBecu0J0ScwZ6CLw6z4jnf1ZaXIYXp97mI4oo+rBtQli3mp2Gb8qNLUjTGr0cihoz/Nfjc6HPilAHlB08ezV/a3H3ZaoU2USCqHzWXYUOF8oRJrg/Ev0kjW1HI188VOaZGQ1wv+cfZCmok1qiAa3sF/ukRO+SZOrN3Kyw11EL88uI0Dylx7PGr4xZVWmh+gTnnX2cKqmUCd3IPkPBtWdIU5CO+l8A7UD1cz+nkc1Sa9GzBwx31E1I7WjTb7GC4vMGRCYsXD4AAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

## Case 4｜TEER 術中肺動脈穿孔：Ping Pong Guide 技術急救

**Kheifets M, et al. Toronto General Hospital — PMID: [42251605](https://pubmed.ncbi.nlm.nih.gov/42251605/)**
🔗 [JACC Case Rep. 2026](https://doi.org/10.1016/j.jaccas.2026.108773)

| 項目 | 內容 |
|------|------|
| **患者** | 接受 TEER 手術，術中右心導管操作後出現內管出血 |
| **診斷** | 左肺動脈穿孔＋假性動脈瘤 |
| **救治步驟** | Wedge balloon 暫時阻塞 → 第二股動脈入路 → 12 mm Amplatzer vascular plug 封閉穿孔頸部 |
| **Ping Pong Guide 技術** | 同側血管阻塞同時提供第二入路 |
| **教學重點** | TEER 術中罕見致命併發症；術中氣管插管後出血應優先排除肺動脈穿孔 |

> 💡 術中出血 → 先想到肺動脈穿孔，再考慮其他出血來源

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABiklEQVRYhdWYMZaDMAxExaOg5AgcxTeLfTSOwhEoKfyY1YzCJrt5qaO48HP8UyA0HsmYvR0VHDYevhw6NwbtnAnIzeLXMaMNfdoKxC05GYGtms+rxzNhtaHPQPsGwni4ZwvwPcRs2gvg5CXSnCS006edegnyR1UfJHEaSUo7x2NZ/53TnOQxSnOdeGyvTpePMJ6Nk8djzEI9x93n7ISeB0ZidBKusYV28hK6nWuHHPdc9MhCZiIPsTP8WlENiCwkIGYzawld+fcELmi5CfuMpYWu5crugrMUkpncbFLdfvRIp9RtuYm0I0W7un1ZIZ6b1E6pqG439GftZCbKgsn59P5Xo/OVdmYgI3ZT1wncn3rcrYRCchNVkVUnU853aScvYQQ8h5fzqZCXx20qJYnB+lKobrAOzk+dXU5y9aOKJG6u6vAtNYksUDXF/3Goll9V5uMkbnrq8ONdP3lIdoLrTEo1C3XyFQRQv1kiouwkPAR0voHacdXMWGtuUvX08bXItUPVjNRObvJ2/ACVRx2E2Y+G9wAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

## Case 5｜Takayasu 動脈炎冠狀動脈再狹窄：Stent-sparing 無支架策略

**Rayyan A, et al. University of Central Florida — PMID: [42283679](https://pubmed.ncbi.nlm.nih.gov/42283679/)**
🔗 [JACC Case Rep. 2026](https://doi.org/10.1016/j.jaccas.2026.108817)

| 項目 | 內容 |
|------|------|
| **患者** | 22 歲女性，Takayasu 動脈炎＋先天性 antithrombin III 缺乏 |
| **表現** | NSTEMI；RCA 開口多次 ISR（In-Stent Restenosis） |
| **IVUS 發現** | 新生內膜增生為主 |
| **無支架策略** | Excimer laser atherectomy → Cutting balloon → Paclitaxel Drug-Coated Balloon（bivalirudin 抗凝） |
| **結果** | TIMI 3 flow，避免再置支架 |
| **教學重點** | 年輕女性炎症性血管病；Drug-Coated Balloon 減少再狹窄循環 |

> 💡 Stent-sparing 策略在炎症性血管病的應用：DCB 避免金屬支架累積

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQMAAACXljzdAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABiUlEQVRYhdWYsZGEMAxF5SEgdAkuxZ0tLo1StgRCAg86fcns3d7OxnwUeMCPAI2/vgQiX2NRhEy7XaaOjeQ7BwF5SNztWVvq87OqcyEnk+pzEVtXy2fWVVLPqu0OBPlgT4rqfYjIvFVVIx+ZcpLQTp836CXIm6ouJFGNILUd017Wf3XKSX6jNtOJ5fbpdHwE+TyxWD6CU1iOabOVm0AppSkyETiJNjwK7TAT9JeCLmMlOM6ij2MgJ/b24deeVdI4hesJ/A0BV35VYNHGTZBDaaYN07W7srlgDu0QE+sip8+NGelwdQs3sUxELBOx6Qh1uKhzbpLc+Y6zb79ph5ego5fTN1CtgkfrmDauJvNW9JyVg29S/a2JiTtfeEi4YIJkFn5SNGZ7D2/kFV9TxCTCJzsNPxHJfyY7TrJ4j7GaHE4C/8vufMwkZv/RZXT3Xh5dhoCcX3pegXM08fAQfvJyPldNgU5uQLDlzlcjI3bi2hn/AqAdU01Wn0eJyajGbrfQDlQzQTvc5Gv8AKoS8m/Uh46VAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 💎 整合 Take Home
## 本週 5 大臨床啟示
### Pearls of the Week

---

# 本週 5 大臨床啟示

1. **IVUS 不是萬靈丹**：OPTIMAL（P=0.40）+ IVUS-CHIP（P=0.08）雙雙中性——常規 IVUS 在高技術中心的邊際獲益有限；**左主幹末端、重度鈣化等選擇性應用仍合理**。

2. **CKM 整合新框架**：2026 指引首度以 4-stage 框架整合代謝＋CKD＋CVD；SGLT2i/GLP-1 RA 適應症擴及所有 Stage ≥2，跨科協作路徑勢在必行。

3. **Finerenone 適應症突破**：INFINITY 確認 Finerenone 效益在非糖尿病 CKD 同樣成立（HR 0.76/0.80/0.88），腎臟科＋心臟科應同步評估。

4. **β-blocker 停藥前先量心率**：心率 ≥68 bpm 的 MI 後患者 MACE 最高（10.4%）；心率低者停藥相對安全。「一刀切」停藥策略需重新審視。

5. **T-TEER 帶來腎臟保護**：eGFR +4.8；AKI 率降 60–80%。重度 TR → 腎靜脈充血是**可矯正的腎損傷機制**，TriClip 術後密切追蹤腎功能有意義。

---

<!-- _class: abbr -->
# 縮寫對照（1/2）

| 縮寫 | 全文 | 縮寫 | 全文 |
|------|------|------|------|
| IVUS | Intravascular Ultrasound，血管內超音波 | PCI | Percutaneous Coronary Intervention，經皮冠狀動脈介入 |
| LMCA | Left Main Coronary Artery，非保護性左主幹 | TVF | Target-Vessel Failure，目標血管失敗 |
| CKM | Cardiovascular-Kidney-Metabolic | CKD | Chronic Kidney Disease，慢性腎臟病 |
| eGFR | Estimated Glomerular Filtration Rate | UACR | Urine Albumin-to-Creatinine Ratio |
| PREVENT | Predicting Risk of Cardiovascular Disease Events | HFrEF | Heart Failure with Reduced EF |
| HFpEF | Heart Failure with Preserved EF | HFimpEF | Heart Failure with Improved EF |
| GDMT | Guideline-Directed Medical Therapy | TAVR/TAVI | Transcatheter Aortic Valve Replacement/Implantation |
| ViV | Valve-in-Valve，瓣中瓣 | BVF | Bioprosthetic Valve Fracture |
| AS | Aortic Stenosis，主動脈瓣狹窄 | AR | Aortic Regurgitation，主動脈瓣逆流 |
| MR | Mitral Regurgitation，二尖瓣逆流 | TR | Tricuspid Regurgitation，三尖瓣逆流 |
| SMR | Secondary Mitral Regurgitation | TEER | Transcatheter Edge-to-Edge Repair |
| M-TEER | Mitral TEER | T-TEER | Tricuspid TEER |

---

<!-- _class: abbr -->
# 縮寫對照（2/2）

| 縮寫 | 全文 | 縮寫 | 全文 |
|------|------|------|------|
| FSV | Forward Stroke Volume，前向搏出量 | AKI | Acute Kidney Injury，急性腎損傷 |
| LAA | Left Atrial Appendage，左心耳 | LAAO | Left Atrial Appendage Occlusion |
| OAC | Oral Anticoagulation，口服抗凝劑 | MACE | Major Adverse Cardiovascular Events |
| RCA | Right Coronary Artery，右冠狀動脈 | ISR | In-Stent Restenosis，支架內再狹窄 |
| PH | Pulmonary Hypertension，肺動脈高壓 | ATTR | Transthyretin Amyloidosis |
| IPD | Individual Participant Data，個別病患資料 | ACS | Acute Coronary Syndrome |
| DM | Diabetes Mellitus，糖尿病 | MI | Myocardial Infarction，心肌梗塞 |
| AF | Atrial Fibrillation，心房顫動 | LVEF | Left Ventricular Ejection Fraction |
| DCB | Drug-Coated Balloon，藥物塗層氣球 | MCS | Mechanical Circulatory Support |
| CTO | Chronic Total Occlusion，慢性全閉塞 | LMCA | Left Main Coronary Artery |
| IPD | Individual Participant Data | GLP-1 RA | GLP-1 Receptor Agonist |
| SGLT2i | SGLT2 Inhibitor | PREVENT | Predicting Risk of CVD Events |

---

<!-- _class: small-text -->
# 參考文獻（1/2）

**NEJM**
1. Testa L, et al. IVUS-Guided vs. Angio-Guided PCI in Unprotected LMCA Disease. [*N Engl J Med*. 2026;394:2189–2199.](https://doi.org/10.1056/NEJMoa2600440)
2. Diletti R, Daemen J, et al. IVUS-Guided or Angio-Guided Complex High-Risk PCI (IVUS-CHIP). [*N Engl J Med*. 2026;394:2200–2211.](https://doi.org/10.1056/NEJMoa2601521)
3. Rocca B, Ten Cate H. Antidotes for Anticoagulation Reversal. [*N Engl J Med*. 2026;394:2235–2254.](https://doi.org/10.1056/NEJMra2506021)

**Lancet**
4. Neuen BL, Heerspink HJL, et al. Finerenone efficacy and safety in CKD: IPD pooled analysis (INFINITY). [*Lancet*. 2026;407:2375–2386.](https://doi.org/10.1016/S0140-6736(26)01009-3)

**European Heart Journal**
5. Qazi S, et al. Statins and survival free of incident frailty in older US veterans. [*Eur Heart J*. 2026.](https://doi.org/10.1093/eurheartj/ehag451)

**JACC Family**
6. Ndumele CE, et al. 2026 AHA/ACC/ADA/ASN Guideline for CKM Syndrome. [*J Am Coll Cardiol*. 2026;87(22S):e1889–e2007.](https://doi.org/10.1016/j.jacc.2026.03.056)
7. Impact of Concomitant MR in Moderate AS. [*JACC Cardiovasc Imaging*. 2026.](https://doi.org/10.1016/j.jcmg.2026.04.015)
8. Naser JA, et al. Prognostic Value of TR in PH. [*JACC Cardiovasc Imaging*. 2026.](https://doi.org/10.1016/j.jcmg.2026.04.016)
9. Withdrawal of GDMT in HFimpEF: Meta-Analysis with TSA. [*JACC Heart Fail*. 2026.](https://doi.org/10.1016/j.jchf.2026.103172)
10. Vericiguat on recurrent HF hospitalization/death in HFrEF. [*JACC Heart Fail*. 2026.](https://doi.org/10.1016/j.jchf.2026.103171)
11. Clopidogrel vs Aspirin Monotherapy post-PCI: Korea Cohort. [*JACC Asia*. 2026.](https://doi.org/10.1016/j.jacasi.2026.03.041)
12. Wells J, et al. Emergent TAV-in-TAV for Failed Bioprosthetic Valve With Severe AR. [*JACC Case Rep*. 2026.](https://doi.org/10.1016/j.jaccas.2026.108598)

---

<!-- _class: small-text -->
# 參考文獻（2/2）

**JACC Case Reports (continued)**
13. Chang JH, et al. Simultaneous ViV TAVR With BVF and LAAO for Refractory LA Thrombus. [*JACC Case Rep*. 2026.](https://doi.org/10.1016/j.jaccas.2026.108776)
14. Nakhle A, et al. Percutaneous Stentectomy: Extraordinary Problems Require Extraordinary Solutions. [*JACC Case Rep*. 2026.](https://doi.org/10.1016/j.jaccas.2026.108749)
15. Kheifets M, et al. PA Perforation From RHC: Ping Pong Guide Technique. [*JACC Case Rep*. 2026.](https://doi.org/10.1016/j.jaccas.2026.108773)
16. Rayyan A, et al. Recurrent Coronary Restenosis in Takayasu Arteritis: A Stent-Sparing Strategy. [*JACC Case Rep*. 2026.](https://doi.org/10.1016/j.jaccas.2026.108817)

**Circulation Family**
17. Ndumele CE, et al. 2026 AHA/ACC/ADA/ASN Guideline for CKM Syndrome. [*Circulation*. 2026.](https://doi.org/10.1161/CIR.0000000000001453)
18. ABYSS Heart Rate Secondary Analysis. [*Circulation*. 2026.](https://doi.org/10.1161/CIRCULATIONAHA.125.078635)
19. Prevalence of Cardiac Amyloidosis in Population-Based Autopsy Cohort. [*Circulation*. 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.079522)

**TEER / TAVI (外部期刊)**
20. Becker M, et al. Renal function after T-TEER. [*Clin Res Cardiol*. 2026.](https://doi.org/10.1007/s00392-026-02961-z)
21. Grewe F, et al. M-TEER FSV in atrial vs. ventricular SMR. [*Clin Res Cardiol*. 2026.](https://doi.org/10.1007/s00392-026-02950-2)
22. Tagliafierro M, et al. ViV TAVR vs. Redo Surgery in Women. [*Catheter Cardiovasc Interv*. 2026.](https://doi.org/10.1002/ccd.70693)
23. Gan X, et al. Perioperative OAC in TAVR: meta-analysis. [*BMC Cardiovasc Disord*. 2026.](https://doi.org/10.1186/s12872-026-06116-w)

> ⚠️ EuroIntervention：本週無新收錄文章（PubMed 查詢結果為零）

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

本週重點：IVUS 中立衝擊｜CKM 首部指引｜Finerenone 廣譜效益

> 本講義為讀書會共筆之教學整理，僅供醫療專業人員教學參考。臨床決策請以原始文獻及醫師個人判斷為依據。
