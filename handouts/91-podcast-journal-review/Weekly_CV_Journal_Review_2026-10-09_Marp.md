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
  section.abbr { font-size: 0.6em; }
  .qr {
    position: absolute;
    right: 40px;
    bottom: 80px;
    text-align: center;
    font-size: 0.65em;
    color: #555;
  }
  .qr img { width: 110px; height: 110px; border: 1px solid #dcdde1; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-10-03 ~ 2026-10-09'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-10-03 ~ 2026-10-09

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Top Pick / 分欄文獻附 QR Code，可掃描跳轉原文

---

# 🎯 本週主題與固定欄目

## 介入與裝置治療的實證週

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選（PE 介入／易損斑塊／節律／HBR 球囊／AI 穿戴）
2. 🫀 **TAVI Section** — 傳導障礙處置 × 新瓣膜登錄 × PCI 時機
3. 🔧 **TEER Section** — TRI-FR 血流動力學 × PADN × AFR 救援
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — 結構／冠脈介入／EP × 5
6. 📖 **參考文獻 + 縮寫對照**

---

# ⭐ Top 5 Picks

| # | 試驗／研究 | 期刊 | 關鍵數字 |
|---|------------|------|----------|
| 1 | **STORM-PE** | *JACC Cardiovasc Interv* | RV/LV 下降 **0.52 vs 0.24**（p<0.001） |
| 2 | **PREVENT 子分析** | *Circulation* | LRP 預防性 PCI aHR **0.23**；非 LRP 無益 |
| 3 | **CONDUCT-AF** | *Eur Heart J* | CSP vs BVP：LVEF 差 **0.4%**（p=0.002 NI） |
| 4 | **SELUTION DeNovo HBR** | *EuroIntervention* | TVF 4.9% vs 7.9%（➰ 未達檢定力） |
| 5 | **LINK-HF2** | *JACC Heart Fail* | HF 再住院 HR **0.90**（p=0.76，❌ 中性） |

---

<!-- _class: divider -->
# Pick #1
## STORM-PE
### 中高風險肺栓塞的機械取栓 RCT

---

# STORM-PE — 設計

**Rosovsky R, Konstantinides S, Weinberg I, et al.** *JACC Cardiovasc Interv* 2026.
🔗 [DOI: 10.1016/j.jcin.2026.07.042](https://doi.org/10.1016/j.jcin.2026.07.042)

- 前瞻、多中心、隨機對照試驗 (RCT)，**22 中心，n = 100**
- 對象：中高風險急性肺栓塞 (Pulmonary Embolism, PE)
- 分組：**電腦輔助真空機械取栓 (CAVT) + 抗凝（n=47）vs 單純抗凝（n=53）**
- 主要終點：**48 小時右心室／左心室 (RV/LV) 比值變化**（影像 surrogate）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABU0lEQVR4nO2XwY3EMAhFkVJASqJ1l0QBllj433ZmdzVzhcNYUeT4+UCAj7H4mzHlSz4SkxhXvO8xb3fT/BbtQTRsvNyTe8KYx2ITEjbGGraM3GXxE52IyYKmDQmiPa5mBF6MaXp0pnd/5UEpoUr0PH/1U0g4wszUx7j+1Z1KguyjpRHnCHjMjq+Lia9ykhyZ+OLReoLq4rBXnSlpXchMGxXLCH74VboQwSmRb9SY3Ht7E+JIQL5R9h4FV5MR9uY0LVWIeLAqtyBCEceX4NEpTUiG+qJWTJiMO9rVxCAOhHru6jJ3Z1dMaLUpDXfOrQvJ3iTdeaqLPtWllqQvV8DzNMN5sTuUarK6AEbbYbt2IeeWs7X7dJ31BNmHftNR89hJNSGy0xAp+ZIHTQhOWnZPWyh9yOCJgQvi2LfqenKivTiKTQ+yVMJWndFemVhO3owv+Uh+AOXGeHo2L8srAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# 0.52 vs 0.24
## 48h RV/LV 比值下降 — CAVT vs 單純抗凝
### 差異 0.27｜p < 0.001

7 天重大不良事件 **4.3% vs 7.5%**（安全性相當，NS）
並改善 **90 天功能與生活品質**

---

# STORM-PE — 臨床啟示

> ✅ 中高風險 PE 機械取栓第一次有了**隨機 + 功能終點**的證據

- 右心受壓的中高風險 PE，**CAVT 是可考慮的早期減壓選項**
- 適合右心儲備差、擔心後續惡化者 → PERT 團隊討論

> ⚠️ 主要終點為 **48h RV/LV surrogate**（非死亡率，n=100），廠商 (Penumbra) 支持；硬終點待更大型試驗

---

<!-- _class: divider -->
# Pick #2
## PREVENT 子分析
### 預防性 PCI 要「看斑塊成分」

---

# PREVENT 子分析 — 設計

**Wee Y, Ahn JM, Kang DY, et al.** *Circulation* 2026.
🔗 [DOI: 10.1161/CIRCULATIONAHA.126.080384](https://doi.org/10.1161/CIRCULATIONAHA.126.080384)

- PREVENT 試驗（FFR>0.80 易損斑塊預防性 PCI vs OMT）事後分析
- n = **598 人／632 病灶**（IVUS 斑塊負荷>70%、最小管腔<4 mm²，加做 NIRS）
- 脂質豐富斑塊 (LRP)：4-mm 最大脂質核心負荷指數 **maxLCBI₄ₘₘ > 315**

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABVElEQVR4nO2YUa5CIQxEm7AAlsTWWRILIOF1ZoqJ+vS3/ZAQw+X4MbZM6dXOh7HtR76SZT7aGlwM38OzjRoET20BNl9w+mYR4hqdWJ/b8KhvFSIIpH/OVpAszf9+TypBts+0ziT313OQSsIlj/nmnzwSYx4InzLxU91JJAiehBvCuSL/JcihcSl8U/W24ZkvQmDfjikfa1GEuGqPJfZYYJD5NWoQXF8SzrSPsHIF4nUOwnWVwShtPbydTRA/u0XFJLytKkQbDCpOJZuCGkSVmHsqz+7jW/nSCSxCpbFA5etViPpNXrC2ZeJwST6xHjcahJspukUILRu9gG62G9FsciLDOJIsM4jxqUFu98QbI7rOMmQozzTHlPzdqxC95bAEDmX+qi5CBp1hLbJfiaCHmuykcBhvP5pPDt+k1Q5ve3sDyyRyiZFP/i0xnvyTSD6MH/lK/gDS5FJMg0KdKgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# PREVENT 子分析 — 結果

| 族群 | 預防性 PCI vs OMT | 校正 HR |
|------|------------------|---------|
| **LRP（脂質豐富）** | 7.3% vs 17.6% | **0.23（0.13–0.41）** |
| **非 LRP** | 5.5% vs 4.2% | 1.00（0.54–1.86） |

治療 × LRP **交互作用 p < 0.001**（中位追蹤 5.6 年）

> **形態同樣「嚴重」，只有 NIRS 脂質豐富者從預防性 PCI 獲益** — 成分比狹窄嚴重度更關鍵

---

# PREVENT 子分析 — 臨床啟示

> FFR 陰性、IVUS 看來嚇人的非阻塞斑塊：
> **先問「它是不是脂質豐富 (LRP)」**

- 有 NIRS / OCT 佐證的高脂質核心 → 預防性 PCI 才站得住腳
- 否則以**強效降脂等 OMT** 為主，避免 oculostenotic reflex 式過度支架

➰ 務實界限：事後分析、NIRS 僅部分病灶、需前瞻驗證

---

<!-- _class: divider -->
# Pick #3
## CONDUCT-AF
### 房室結燒灼後：CSP vs BVP

---

# CONDUCT-AF — 設計與結果

**Žižek D, Ivanovski M, Mrak M, et al.** *Eur Heart J* 2026.
🔗 [DOI: 10.1093/eurheartj/ehag699](https://doi.org/10.1093/eurheartj/ehag699)

- 多中心 RCT，n=82；難治性心房顫動 (AF) + 心衰、窄 QRS，接受房室結燒灼
- **傳導系統節律 (CSP / 左束支區) vs 雙心室節律 (BVP)**

| 終點 | 數值 |
|------|------|
| 6 個月 LVEF | CSP 36→46%｜BVP 34→46% |
| **組間差** | **0.4%（−3.1~3.8），p=0.002 for NI** |
| CSP 優勢 | paced QRS −14 ms、程序／透視時間更短 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABUElEQVR4nO2Xwa0DMQhEkVKAS6J1l+QCLPFhsB0nX8mVOcRaZRPeHggwwIp9OFN+5CsZ4ucx5GFdRG1o/BblIOo+ujkvaf7d3EhC3Me0hfv+lP8DKuJxbR0GJSQW2Q4bFTFEEWUo4fVrHZQS2c6u610/hSTPgHY94f/6TiVJmyi022eLnJ9YVxPUXfjbIZE71vVk9ZVLxKcS64m4OFIuyDa0QkFCvtGVsxI9tFGGzSgIAmnQrhuQ/Cvb1eQ0mBnTDCN3cJC4y4xYZm/OVHMQTIwMKj7lmW0CIm115bk3u+11NYnhoFiaQFI0g4XAX/Q/yDfdpyBQcDa/KEnMi2e/riVrC3Ch5NzQnXkCclrL8v3aOusJqg89Bl3w8pqAnDcJe6sDEhLdruMR3UIhImt78nUAr9ckBNnOzof53/pkIakSwTtEz2yf7amYfDg/8pX8Ac8VDA63jDPLAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# CONDUCT-AF — 臨床啟示

> ✅ 「ablate-and-pace」病人：**CSP 非劣於 BVP**，且更簡、QRS 更生理

- 房室結燒灼後的生理性節律（左束支區）是 BVP 的合理替代
- 尤其 BVP 置放困難或希望縮短手術者

➰ 務實界限：n=82、主要終點為影像 LVEF、追蹤僅 6 個月

---

<!-- _class: divider -->
# Pick #4
## SELUTION DeNovo HBR
### 高出血風險 PCI 的藥物球囊

---

# SELUTION DeNovo HBR — 設計與結果

**Rissanen TT, Eccleshall S, Krackhardt F, et al.** *EuroIntervention* 2026;22(19):e1025-e1035.
🔗 [DOI: 10.4244/EIJ-D-26-00889](https://doi.org/10.4244/EIJ-D-26-00889)

- SELUTION DeNovo（n=3,323）之預設高出血風險 (HBR) 子分析；HBR **n=522**
- **sirolimus 藥物球囊 (SEB) + 必要時支架 vs 系統性 DES**

| 1 年終點 | SEB vs DES |
|------|------|
| 標的血管失敗 (TVF) | 4.9% vs 7.9% |
| 大出血 (BARC 3-5) | 2.3% vs 3.2% |
| NACE | 6.8% vs 10.7% |
| 6 個月停所有抗血小板 | **27.8% vs 14.9%（p<0.001）** |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABXElEQVR4nO2Xwa0DMQhEkVzAluTWKckFWOIzA87fJEqucIi1WsW8PRDDABb7sLb8yFeyxNfAT5ELNuxl9iDTd2PJWHNf5p/448YmxH10s7vs3Lf5VSfiLjvcl7Ujpm5AtN+8riWItinycYm95UEpoUrgbD4v+qkksXiQ6fJz3akkqWCoRC7dqDSKlOxAzHcuEezcRn9nG2InyO5+8MdZV5NjM/YKuq9tSKgENrx5nE8KLiQsLRs9VllXouz1IPB6MsIaDW3nUNCAGJsYhYtewTQceaLlhDlIBccYFUfbgqDBqmU9Dq3MRy8pJzsnFA4CnAiOfsqJv/JcWZU15uImJMYl7I7jZ1qvJrEy5uhsxnGgBTm3HCo4Bqhb3SkmMyQSCRjPvt3AaklU5ZFywZ84mdiEqJ3R6b/yNSI5dQqv101IRnvlHfH1BlZJ8pbjpWVfJ+b3ya6QfFg/8pX8AWm13zSuoFCRAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# SELUTION DeNovo HBR — 臨床啟示

> ➰ SEB 策略數值有利、能更早停抗血小板，但**未達檢定力、非優越**

- HBR PCI 的工具箱可納入**藥物球囊（少放支架、縮短 DAPT）**
- 須接受約 **17% 需 bailout 支架**
- ❌ 不能據此宣稱 SEB 優於 DES — 待專為 HBR 設計的大型試驗

---

<!-- _class: divider -->
# Pick #5
## LINK-HF2
### AI 穿戴偵測 ≠ 改善結果（負向教材）

---

# LINK-HF2 — 設計與結果

**Sideris K, Schmalfuss C, Lewis EF, et al.** *JACC Heart Fail* 2026.
🔗 [DOI: 10.1016/j.jchf.2026.103422](https://doi.org/10.1016/j.jchf.2026.103422)

- 隨機、開放標籤、盲性終點；5 個 VA 中心；急性心衰出院後戴連續貼片至 90 天
- n=171（AI 導引監測 + 臨床通報 80｜標準照護 91）

| 終點 | 數值 |
|------|------|
| **HF 再住院** | 16.3% vs 18.7%（**HR 0.90，0.43–1.84，p=0.76**） |
| 複合（住院／急診／死亡） | HR 1.03（p=0.89，NS） |
| AI 偵測生理不穩定 | **HR 0.76（0.60–0.97，p=0.025）** |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABTklEQVR4nO2XUY7EIAxDI/UAHImrcyQOUClrO7Sd1e7ML/6YqKoorx9pwCaNfBNnfMlHMgNxzH62gXHOzufoHqQjRxBMHznOlgeepwtBjiDRBuYCZOojfEgOEJY2/QjWvHED1tiHcLVzcLDGv/bBVrJUcl9/9LOPPDE00f/xnV2ExWNgDgaDca2/BeHuw30c6xUmjl3pQeB2Iypke3W3IKXd66ygXKQYE1J2UvnWZUSUKVwZpdVbt7a3E2pCW09a4cr3F7/eTHj4x2V7OjdciDxPVVzyZRt1e+JeMlHFVFu3SptzuYsDoTJCKonVrbxoezPJuc4KvRLV4pmQap1CdT0ve7YgFaubY0X5HelBru7pWXYj0mUnempP72lCnr+cu5NqXkQnLaEWvxuRLH0w99qPJiT1l6OffiZ+KcaBlErK/1jL496J28mb+JKP5Ae/8QOeb3LfSAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# LINK-HF2 — 臨床啟示

> ❌ AI 偵測**準**（不穩定 HR 0.76），但**未改善臨床事件** — 偵測準 ≠ 結果好

- 導入穿戴／遠距監測前，要先設計好**「偵測到異常後怎麼做」的結構化反應路徑**
- 否則只增加警訊疲勞
- 務實界限：可行性研究、n=171、臨床終點為探索性（勿解讀為「遠距監測無效」）

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 結構性主動脈瓣方向
### 傳導障礙處置 × 新瓣膜 × PCI 時機

---

# TAVI #1 — GLAM-TAVI：傳導障礙處置

**Novelli L, Occhipinti G, Laudani C, et al.** *Rev Esp Cardiol (Engl Ed)* 2026.
🔗 [DOI: 10.1016/j.rec.2026.10.001](https://doi.org/10.1016/j.rec.2026.10.001)

- 歐美 6 中心登錄；TAVI 後傳導障礙 (CD) 345 例（個體化觀望 160 / 標準指引 185）

| 1 年終點 | 個體化 vs 標準 |
|------|------|
| 主要複合（死亡/再住院） | 13.6% vs 7.1%（aHR 1.23，NS） |
| **永久節律器 (PPM)** | **49.4% vs 80.2%（aHR 0.61）** |
| **心血管死亡** | **8.4% vs 1.2%（aHR 9.10）** |

> ⚠️ pacemaker-sparing 少裝節律器，**但可能以較高心血管死亡為代價**

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABUklEQVR4nO2XwQ3DMAhFkTyAR2J1j+QBLFE+327TRu0VDrWiKMnzgQAfsNiXteRPfpIpvpoNv/uzTcW7aA2ibmOburqRNH+fVYjb2Nz2bg4bdkkrRtypcdUjZoi2x7zXIog2IgzDz3MREirxBDzXh34yCZd/8EwUvdedTLIVLCuiTb/GrgIEBirtXduXWoUwyOR98Pl4NJu4dlnzoAwNd44yZIQLUfN8Cy8qOJ/AhQNpCKHAZJpfh7BXLPgSu9rJg3TC2cT1IaEP41BQgSDIFAfsxZzCP6hAZhS8k4ZOaH4ZAhciDYUTwTidNp2g8iEBOdZFu7jUxGQS3yjcV0qWIM8pQPY3+rgEOacc282f03ERgv7PiTgOOkofFyGc1jFAdQ4pUozssiesfNczRj6hdgeP1/L+P4mE0WaBQbO9ncDyCE857BsxQ4le9ZNJvqw/+UketNi6tpslWhcAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TAVI #2 — Octapro MyPro 登錄

**Ielasi A, Moscarella E, Verček G, et al.** *Int J Cardiol* 2026;465:134967.
🔗 [DOI: 10.1016/j.ijcard.2026.134967](https://doi.org/10.1016/j.ijcard.2026.134967)

- 新一代球擴瓣 Octapro 真實世界登錄，n=303（歐洲+印度）
- VARC-3 技術成功 **97%**、程序死亡 0.3%、30 天 PPM **14.2%**、中重度瓣旁漏 3.3%
- **PPM 獨立預測因子：植入深度（閾值 4.75 mm）＋ 基礎右束支傳導阻滯 (RBBB)**

> 💡 與其事後糾結要不要裝節律器，不如**術中就把植入深度做淺**；對基礎 RBBB 者更嚴控深度

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABkElEQVR4nO2YwQ3DMAhFkTyAR/LqjJQBLFH4gFOl6qmXf6hltSQvlYwDH1yx72PLH/4GL/ExTPdUt/c08RljUcLlq3bo0+/Ajun3OaGvelzi0+IRc29wSQ3TwHtY9HB5dIQT5sFCDSM0Ytc95+Ip+4ghJogUjOXf85GfRDDHVXtvoRxP7SOCWHjstAvG1OPKYIX4hrB5aEyFHmuLMSOMLQ9iqRz9Cz6IirEzrnv7rQWDDlYKSsbyyKD2SyGFXTekS4egj+CEUSiQfJJqMVDr3GCFK3e6ZDhlwyhh9zjuBwI8H5QsdHxQo32oLBTYK71hhPGB1uyt+Y2XUG+FDYYTXjEgyXqykBVmIFvq8W67U5ARIoqRfCjRMu3ujMlgOeHtg2SVVsS1cUIc1LQbST3dOid8q8xqufHSZZkNVqseOYduHa6gnjDClodQCxwx9zlxMkIEBfpH2KVwnYJ0ULp9wF84ms7ZEWNGWEqcIneHCSnsylyHNnv6SQNTzM5RuFwhhaltp+tZ1sdiRvh9/OFv8AVid9Tup/NYuwAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# TAVI #3 — ASCoP：TAVI + 高風險 PCI 時機

**Munafò AR, Esposito G, Khokhar A, et al.** *Int J Cardiol* 2026.
🔗 [DOI: 10.1016/j.ijcard.2026.134968](https://doi.org/10.1016/j.ijcard.2026.134968)

- 多中心登錄，n=519；依 PCI 時機分三組（同時 30.1% / TAVI 前 64.1% / TAVI 後 5.8%）

| 策略 | 1 年結果 |
|------|------|
| **TAVI 後才分階段 PCI** | 主要複合終點**較差**（HR **2.31**，1.24–4.32） |
| **TAVI 前先 PCI** | MACCE **較低**（HR 0.55，0.35–0.85） |

> 💡 傾向 **TAVI 前或同時**完成高風險血運重建；務實界限：觀察性、TAVI 後組僅 n=30

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABk0lEQVR4nO2Yva3DMAyECXgAj6TVNZIHMMDHu6P04gCp0lwRQYXsT4VIH3/kyM/jjh/8Dl5R46jlOWt9nxk1MYYlHHXqI2fNesM1Zr33hHXq44qaiS1lU/LRGmrB7zDs4WgjssRiDSENeL1iDruSG9MUMgSv8Trf4tMIavD4lSqSjn/LfUaQB1d6i3PSjvXGEDKZlUAollFbmI/ncrwZZMAF6sZQYsula0cIdcxbuoY4Jjd2wrCDtEPq4EeA41GfwxOqYnTRUP5gH2EKj+56ZtIOPkIyrrBOHQpB2jGPV8Vbwez+MWmKfI+9W/FeUJlsMAohkFrLGkvIJ8bfbn7RTbTj/eCJKte1bkWhKYR+Z7C4Sd30fewQtIOXxBJtEPlqfh2hvK7IQ/WArtMTdhepEpdw/5K2I+ziRsenHB+7LJtBDfierQSlveqJH/z/NYIaIo1wV1pCiuLqe9uudSsE7aD+LnQfgUtbqIY4QyW2XJeMpyluUJUZtwrp5WGKE1QyW1uWKaaQIfhQdF+LHeHn8YPfwT82rwvVl9ga6wAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 二尖瓣／三尖瓣緣對緣與瓣膜介入
### Drake 的 TEER 操作面向

---

# TEER #1 — TRI-FR 血流動力學子分析

**Donal E, Leurent G, Zygouri A, et al.** *Heart* 2026.
🔗 [DOI: 10.1136/heartjnl-2026-328062](https://doi.org/10.1136/heartjnl-2026-328062)

- TRI-FR 隨機試驗（經導管三尖瓣緣對緣修復 T-TEER + 藥物 vs 單純藥物）之**探索性子分析**
- 聚焦**基礎侵入性右心血流動力學**（右房壓、肺動脈壓、後負荷）與治療反應的關係

> 💡 T-TEER 成敗取決於**右心儲備與後負荷** — 術前右心導管有助於精準化病人選擇與時機；不可逆右心衰竭／重度肺高壓者效益有限

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABlUlEQVR4nO2YQQ7DMAgEkfwAP8lf95PygEgUdiFJK/XUyx5q5WB3ejAYFmzz7+O0P/wNHhZj5DTn53SLL8eShCt2PfLbNncsMfeYaMLY9ThgB22aHsshDdOgmOAcljxMO9IIh++FYYZJON53Oj6WiBQXhUjB3P79feSnEORIx69wPAxaH9onBLHxVAu7bWrBE4V+VICcc0OPd4uxHDyZgrOEzTuuNSESzmyiYqCADCw14XmtIG8Z2oxxSRh7ZwfRpcPQR2jCTru2I+sGirMi9I34BaQM5zlUUOtB5w/QtvI9zmEpQsgDGwevzFu0RhKGsO0rnNkIp+DVxUINphg7AtnqX89CpwZTyQwdBESCvm9504NseLPHmUxHYzpKwrSDAcLMGzRuuixk/2hoJ0dfOjUhUxDlYrMRNnvWbCXYrbojWChscL8krKeRzRMYuFiwSktCBEUWDV6ASpjfL8RC0J6tetr0jCFRiBrCyrzvMFGFzEKrS5v7rSZa0OsNz7qd9Kud1INIQUoFXxr6WqwIv48//A2+AC6WwOR863xVAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TEER #2 — PADN 治療 M-TEER 後持續肺高壓

**Chen X, Zhang Z, Lan X, et al.** *Pulm Circ* 2026;16(4):e70404.
🔗 [DOI: 10.1002/pul2.70404](https://doi.org/10.1002/pul2.70404)

- 試驗性研究，n=6；成功 M-TEER 後仍持續 WHO Group 2 肺高壓者接受**肺動脈去神經術 (PADN)**

| 終點 | 數值 |
|------|------|
| 術後立即平均肺動脈壓 (mPAP) | 38.5 → 34.0 mmHg（p=0.028） |
| 6 分鐘步行距離 | 377 → 436 m（p=0.046） |
| 三尖瓣逆流改善 | 5/6（83%） |

> 💡 M-TEER「殘餘肺高壓」是未滿足缺口；PADN 可行、安全、短期有改善訊號（n=6、多數 6 月未達顯著）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABSklEQVR4nO2XS47EIAxELXEAjsTVORIHQKqxXSad6d/WXjRCEeRlYflTdgQf1pYf+UqW6GprYI0teh12l1GDDLWxYQKzLfEz/KsSRG20d8dePbdSBHP7U68liUhHK0Yswu7R3Wd7yYNUElVy7Zf6ySO35a59qztJZNlN+tRtQe7YHvMyxNJQt39ie0sR4tF1Y3ccZltFiBUHZc8rZtohop1PzJG+GGo1HLc8yCXRY8HXJjAnD7KJurC72rkv92MiKEHAVhautUPoTjqJbmZDCuN8i3Y2ASh4Vsp9MhNPx8gm7GbRJeSaU0oQ0H/qyHnU5eRBOlkhMJvuvGSmAuHy2cSJlm9MdvkkpiceYoBCFWKxbWdTpOsQqgtHgIi2lCLWLqgueP7HyCZLvIjBH+u71bkEEWc6UvwPGzUIq4QCExX8r34SyYf1I1/JHyx0gcLpT46dAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TEER #3 — AFR 救援：M-TEER 後左房僵硬致反覆肺水腫

**Sooknanan NN, Fernandez-Hazim CM, Tuluca A, et al.** *JACC Case Rep* 2026:110447.
🔗 [DOI: 10.1016/j.jaccas.2026.110447](https://doi.org/10.1016/j.jaccas.2026.110447)

- 70 歲女性，M-TEER 後僅殘餘輕度 MR 卻反覆肺水腫
- 血流動力學：左房壓升高、**高大 V 波** → 左房順應性下降（stiff LA／左房高壓 LAH）
- 植入**心房血流調節器 (AFR)** 持久左至右分流，12 個月無再住院

> 💡 M-TEER 後反覆肺水腫但 MR 不重 → 想到**左房僵硬／LAH**；AFR 可作左房減壓救援

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABnElEQVR4nO2YUY7DIAxELXGAHImrc6QcAIkdz9jdblf96s98FKEo4uUDzDDGifO+7fjCz+AdaOMsPPG+rxPo2aYlnJh1wos837Nj3BNi1gOf3CALw1jNuGN4QzzRuQ/THsaGLq7cAYw4w5RGPtfWDvzTkBPkEczp//aX82kE1fAJrSIXdL16nxHkxBHpNIxrPZYyTGFQyMHzB10v+vHqXTGDZcOTZy4PX8ocC9KuuEGEmbpg7I++PU9u4gVzypOpuOwtRS23M4SaNWPfqSPqW0fIRJGhX1rHoMDx4glTHZ1AdFkbf0XtBCtvyDkU+51Xy2kJJ8/crJBf0vgarnBTx5upQ86RPle7YgaZNzbP3HkKfKcON1gX884ein30DcMMch3SCGLPeCcvmdjBqdSBFlFupxFPOFiuaUGq21rajlCewXivughHp2U3qHaXNGRsquQc4ePXCAuL0aVbycQOzvYMvZfD2cL+2aC/OCoy2t5Moa6Q3Adm6UfOdoVLVcWuyvh4wo53/2bg7XKYQh5BXSpL0VUWO8L37Qs/gz9CCdMIkYJO8gAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

# 其他值得一讀（1/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **DanGer Shock SYNTAX 子分析** | *EuroIntervention* | 高基礎 SYNTAX → 180 天死亡 aOR **3.12**；孤立左主幹亞組 Impella aOR 0.17（假說生成） | [DOI](https://doi.org/10.4244/EIJ-D-26-00460) |
| **Multivessel TALENT 子分析** | *EuroIntervention* | 標準化器械成功（核心 QCA 88.0%）< 操作者目視（97.4%）；未達者 1 年事件更高 | [DOI](https://doi.org/10.4244/EIJ-D-26-00413) |
| **DEEP-PFA** RCT | *Circ Arrhythm EP* | EP 醫師主導深度鎮靜下，雙極接觸力導管行 AF 脈衝場消融 (PFA) | [DOI](https://doi.org/10.1161/CIRCEP.126.015420) |

---

# 其他值得一讀（2/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **過度小樑化 CMR 風險分數** | *JACC Cardiovasc Imaging* | 589 人／17 中心；以不良重塑與纖維化建立 CMR 風險分數預測 MACE | [DOI](https://doi.org/10.1016/j.jcmg.2026.07.027) |
| **ACHD 後天性風險因子** | *Eur Heart J* | 9,826 人；吸菸 HR 1.67、睡眠呼吸中止 2.22、冠心病 1.78 皆獨立增死亡 | [DOI](https://doi.org/10.1093/eurheartj/ehag787) |
| **中國院內心跳停止登錄** | *Circulation* | BASIC-IHCA、37 院；中低收入國家首批多中心 IHCA 基準數據 | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.080404) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構 × 冠脈介入 × EP
### 本週 5 例

---

# Case #1 — TAVR 遇上突出的 RCA 支架

**Iyengar A, Wong A, Muuse J, et al.** *JACC Case Rep* 2026:110627.
🔗 [DOI: 10.1016/j.jaccas.2026.110627](https://doi.org/10.1016/j.jaccas.2026.110627)

81 歲女性重度 AS，右冠狀動脈 (RCA) 開口支架 10 mm 段突入主動脈根部。

**四步可重現流程**：
1. 導絲穿支架網眼 → **創造 neo-ostium**
2. 瓣膜成形球囊 **crush（壓貼主動脈壁）**
3. 控制性球擴瓣部署
4. 開口優化 → 無冠脈阻塞

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABmUlEQVR4nO2YMa7EMAhEkXyAHImr+0g+QCQWZnB+/kZbbTPFWi4SPxdAxoBj8Xmc9oPfwWU5xnKznHg9opbMJaGn1SMNPyLJmRvxmuuaMK0eMc9j9sblY5VzunDh4Zj1UFwcOkOez/F0RQnSdoY8vYmHhpRgH8H7fJxPGcgBV2pXpFL8LfcJweVB2zNhxKSukedcEZbJltmCwa61Usoc7acY3LUikzEyXPsUmjDVgWPHQpcyoWR24MUgbK/SsdMbP8LNTyn4VzegEeRjFmpBiPahvEG5MIjFaorCXG6O8OP8XaIWgyXeivoJgUDUzu2SsGYu16yKZ/TGNCEayU7D1VcGfeqvogeha3Q610c4sEUQLnY91U6eSBWszKrQWd8Q9UrDe0soQtrenS9iT4GrQjTmHXsmDFZmRYjlgaYymIzZTmpCjtX5mBeLyseasK9BvFOiyv0rHWpwNzioclsmLgv5swEVg9d3Y9rQhbhfxu59qm2/uaIH+7dThX/xhiEKIZPZW4wrVzupBnkEeewo6k7JivDz+MHv4AvLB3efwr9j1QAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #2 — 腋動脈 Impella 5.5 橋接 CIED 心內膜炎

**Tamura Y, Nakahara S, Saito M, et al.** *J Artif Organs* 2026;29(4).
🔗 [DOI: 10.1007/s10047-026-01599-y](https://doi.org/10.1007/s10047-026-01599-y)

53 歲擴張型心肌病、CRT-D 感染（MSSA、休克、LVEF 10%）；17 年舊除顫導線拔除極高風險。

- 先經鎖骨下動脈植入 **Impella 5.5** + 外科引流囊袋（感染源控制）
- 穩定後第 6 天在支持下**完整拔線**，最終橋接至 **永久左心室輔助裝置 (LVAD)**

> 💡 腋動脈 Impella 5.5 = 分階段源控制、高風險拔線、器官恢復與橋接的穩定平台

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADGAQAAAACh4MLwAAABUElEQVR4nO2XSw7DMAhEkXqAHMlX95FyAEuUmcHpT+0WFrWiKMnrgg5mwOZf1rI/+UlOi3U7x809rnU43m30ICNiBBHkPT42IREjvyF2O/KhEUHsc0nabsQnMnzEBuxFnHswtiT44W/7oJTsKtnXZ/2UES2qmPdX36kkqAwIaUi1KfMr3aWa5B4MOOl8eFW268lpnmVBz+MP+Q8aEDwatExdIefj/xSTKNnQcl7O505pO5DTFiLFYqoNsWdtVxNX21faYcyNCM0YKrL/Q1TOKS0Iq/ayvcVd2YbQXbJLjDSYJgRCTnVXtdmlewfCDF+1K13bENnwVPgq5TbkmgL0YXBmGS3I8yknXJBT567tcoJxKd52o0DUe3qqJ5qYXH2Mcu7TYQ9CRe1Ip3k+HTYgpl4Bz8MBsQvhkOL7GPG+E0tJVgnP0+xpjx5cTb6sP/lJ7hONLB5BDIVoAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case #3 — 「刻意分盤手法」輔助 ASD 封堵器判讀

**Ohashi H, Mitani Y, Harada T, et al.** *JACC Case Rep* 2026:110640.
🔗 [DOI: 10.1016/j.jaccas.2026.110640](https://doi.org/10.1016/j.jaccas.2026.110640)

3 例複雜心房中隔缺損 (ASD)（邊緣不足、鬆軟中隔、中隔瘤），GORE CARDIOFORM 封堵。

- 鎖定前輕拉滑桿、在兩盤間製造暫時間隙（**intentional disc separation**）
- 以 TEE + 透視互補確認花瓣方向與中隔貼合 → 安全部署、無殘餘分流

> 💡 嚴格定位為**影像輔助、非機械穩定測試**；困難解剖提升判讀信心

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABnUlEQVR4nO2YQa6EMAxDI3GAHqlX75E4QKX82G6LPtKsZuPFVAgBj0UTXCcl8vOY8YPfwTtqXJl1ruvZMhquI7ol7DXrgrMNcF7XUc89Yc36uqOOzMG3krfOsCPl0fkduj1EyhFEjnriDCENnMdkTID/NeQEuQQx/ed4rU8jqMFMl1UkE//yPiPIicPeyjDaOKFcnrBM4l7ShjTaoB+PlXg7qEKhNdf1onTtCEvUbciGJRPcHsNwg5iyFlyXvdUZ9TksIaZcvcPYSuFXYBnxhEozcz9Uk4NheUIVChUQWgVtIz0hbRhpxmPlfkbsQucGu9bchBNDICVnubIn5BJEkw5pqxGO81XMYMLbdp/+JH7XFTsYdDWmn2Eh97E6DDeoUixja9xYkB+ZuMFtD3AL9enUdXpCpplZX2U5t7QdIf147G4iVevmKXRWcLXqy9J0zmXPfvD8Gmlri6mt25KJHVwFWeo+DmcLz88G/sIZCm7bmydUbx5L2gzLG6qMaNOW71BsYCrfu50EeXpNN8glyMTvdnJtix3h5/GD38E/rYgRvYMkxdMAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #4 — 斑塊內出血：被低估的冠脈不穩定機轉

**Duband B, Souteyrand G, Motreff P.** *Ann Cardiol Angeiol (Paris)* 2026:102087.
🔗 [DOI: 10.1016/j.ancard.2026.102087](https://doi.org/10.1016/j.ancard.2026.102087)

49 歲女性 LAD 血栓性阻塞引發急性冠心症 (ACS)，抽吸+抗栓、未置放支架。

- 1 個月光學同調斷層 (OCT)：**癒合的斑塊糜爛**、無顯著殘餘狹窄
- 5 個月後復發 → OCT 見**斑塊內出血 (intraplaque hemorrhage)**，快速進展為重度狹窄

> 💡 表面「癒合」的斑塊仍可能脆弱；defer stenting 策略須警覺短期快速進展並追蹤

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABl0lEQVR4nO2YQY7DMAwDBeQBeZK/7iflAQK0Immnwe721AsPNYzAyfgQqTSlNOr9yPjCz+AVPY6+ntWL2ouIYQlHv/XB2SR741qbwn7ro2b11MZrdGSHM+xr5/uc/ZjcHXYone9e1z+hGEElGwJBQLP+aMgJ6giO5/x9Pn2gBgPCrk4/10/vM4LXoFL0C0zpWreOsB9EuxpkklR0QikQuCO8pBQYRu7SAaszhol8w5LhynS4fQTd4ODrz12QkXjI5Ba1F0QHAYGw0CW5HM4RMse3VUAsJw4iVeMHVxzL23AQT4qlXCHukOng40SV7oeWUKcNS1VmdJR0ZU84mXK256e0LD+2hGx2kr0ko5GuyxRKzsz9aiXUAqssu0HZm77YdonmlnKE6+SVouF1cprCfFU5Ohx+gdgyMYNUhA6fzFjNuynUuFY7qQ8LbXeE+68ROVyxOD/qihvEgTsYz24nh6YnDNXhWO2kgsswhpTz8jluWTIxhbUdbh6ruzSFkokUnfvLuExh3GV5tb1w4rnLshl8P77wM/gDs0GIta1WPFAAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #5 — 難治 LV summit VT：多能量序貫消融

**Bhagirath P, Regany M, Pierucci N, et al.** *Heart Rhythm* 2026.
🔗 [DOI: 10.1016/j.hrthm.2026.09.055](https://doi.org/10.1016/j.hrthm.2026.09.055)

難治性左心室頂部 (LV summit) 心室頻脈 (VT)，依序以三種能量消融：

**單極射頻 (RF) → 局部脈衝場消融 (PFA) → 雙極 RF**

- 以心臟磁振造影 (CMR) 呈現各能量在心肌的**消融足跡／病灶範圍**

> 💡 單一能量無效時，多能量序貫是進階選項；CMR 可視化不同能量的深度與範圍

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADeAQAAAAB6HIMaAAABl0lEQVR4nO2Ywa0DIQxELVEAJdE6JVEAkr89Y1YkXznlMoegaLXL48CQsTGYf27bfvA7uCxai9c+m8/4jO7ssiEJR3y1Nazn9Juf5xKFMeu2rOHFfcYofgrDeM1nu8bqwjBIiAgpKy2jDOmLkLK7W5+p6dVDShAhuMb9e4tPIciG9U41EPSW+4RgJQwKSgXIdhmImjD6YvqRjOERyzy3TBRi1lQQ0B+zuCTkppFqJve6DUFPNhGDxiUPJeSXwfUgSgYOeTbklp2acGbkdZoFHqdxytRikCGI8oF2di9rS0Kr6iy/8j3/BGjShMwTiLyB9cbamyREsVNOYWNiVoXIE47K109RWelNDi5GYSz5zDyBgXCKJhywsD0l8K604Zow+lrVaKkjnyjTNCFz8DEyRYxzIFaDde6hWfyp0ylFDZ5SfTNh9BpS8akG62qE1pioKa5yUg7iYJG+ntBhPBbfFzlS0Ghk7MzYpVPc1obla9yW3XW8LORlAyzzX4oKpE32udI7VY9LQoRgVeiVLXA+loSf2w9+B/8ARPHp0PtFTU0AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: lead -->
# 💎 Take Home Message

### 1. **STORM-PE ✅** 中高風險 PE 機械取栓有隨機證據（RV/LV ↓ 0.52 vs 0.24；surrogate 終點）
### 2. **PREVENT 子分析 ✅** 預防性 PCI 看成分 — 只有 NIRS 脂質豐富者獲益（aHR 0.23）
### 3. **CONDUCT-AF ✅** 房室結燒灼後 CSP 非劣於 BVP，程序更簡、QRS 更生理
### 4. **SELUTION HBR ➰ / LINK-HF2 ❌** 藥物球囊未達檢定力；AI 偵測準 ≠ 改善結果
### 5. **TAVI 傳導障礙 🫀** 淺植入 > 事後觀望（GLAM 觀望少 PPM 但心血管死亡偏高；Octapro 閾值 4.75 mm + RBBB）
### 6. **TAVI + 高風險 PCI（ASCoP）** 「TAVI 後才補 PCI」1 年最差（HR 2.31）
### 7. **瓣膜介入「成功後沒好」找機轉 🔧** 右心儲備（TRI-FR）／殘餘肺高壓（PADN）／左房僵硬（AFR）

---

<!-- _class: small-text -->
# 完整參考文獻 (1/2)

**Top 5 Picks**
1. Rosovsky R, et al. STORM-PE. [*JACC Cardiovasc Interv* 2026.](https://doi.org/10.1016/j.jcin.2026.07.042) PMID [42836810](https://pubmed.ncbi.nlm.nih.gov/42836810/)
2. Wee Y, Ahn JM, et al. PREVENT 子分析（NIRS 脂質負荷）. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.080384) PMID [42836296](https://pubmed.ncbi.nlm.nih.gov/42836296/)
3. Žižek D, et al. CONDUCT-AF. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag699) PMID [42834810](https://pubmed.ncbi.nlm.nih.gov/42834810/)
4. Rissanen TT, et al. SELUTION DeNovo HBR substudy. [*EuroIntervention* 2026;22(19):e1025-e1035.](https://doi.org/10.4244/EIJ-D-26-00889) PMID [42837205](https://pubmed.ncbi.nlm.nih.gov/42837205/)
5. Sideris K, et al. LINK-HF2. [*JACC Heart Fail* 2026.](https://doi.org/10.1016/j.jchf.2026.103422) PMID [42853165](https://pubmed.ncbi.nlm.nih.gov/42853165/)

**TAVI Section**
6. Novelli L, et al. GLAM-TAVI. [*Rev Esp Cardiol* 2026.](https://doi.org/10.1016/j.rec.2026.10.001) PMID [42843586](https://pubmed.ncbi.nlm.nih.gov/42843586/)
7. Ielasi A, et al. Octapro MyPro registry. [*Int J Cardiol* 2026;465:134967.](https://doi.org/10.1016/j.ijcard.2026.134967) PMID [42838146](https://pubmed.ncbi.nlm.nih.gov/42838146/)
8. Munafò AR, et al. ASCoP registry. [*Int J Cardiol* 2026.](https://doi.org/10.1016/j.ijcard.2026.134968) PMID [42838145](https://pubmed.ncbi.nlm.nih.gov/42838145/)

---

<!-- _class: small-text -->
# 完整參考文獻 (2/2)

**TEER Section**
9. Donal E, et al. TRI-FR haemodynamics. [*Heart* 2026.](https://doi.org/10.1136/heartjnl-2026-328062) PMID [42850060](https://pubmed.ncbi.nlm.nih.gov/42850060/)
10. Chen X, et al. PADN post-M-TEER. [*Pulm Circ* 2026;16(4):e70404.](https://doi.org/10.1002/pul2.70404) PMID [42840917](https://pubmed.ncbi.nlm.nih.gov/42840917/)
11. Sooknanan NN, et al. AFR for LAH post-M-TEER. [*JACC Case Rep* 2026:110447.](https://doi.org/10.1016/j.jaccas.2026.110447) PMID [42848362](https://pubmed.ncbi.nlm.nih.gov/42848362/)

**Honorable Mentions**
12. Marquard JM, et al. DanGer Shock SYNTAX substudy. [*EuroIntervention* 2026;22(19):e1036-e1047.](https://doi.org/10.4244/EIJ-D-26-00460) PMID [42837204](https://pubmed.ncbi.nlm.nih.gov/42837204/)
13. Oshima A, et al. Multivessel TALENT device success. [*EuroIntervention* 2026;22(19):e1048-e1063.](https://doi.org/10.4244/EIJ-D-26-00413) PMID [42837202](https://pubmed.ncbi.nlm.nih.gov/42837202/)
14. Li X, et al. DEEP-PFA. [*Circ Arrhythm Electrophysiol* 2026.](https://doi.org/10.1161/CIRCEP.126.015420) PMID [42845271](https://pubmed.ncbi.nlm.nih.gov/42845271/)
15. Casas G, et al. Excessive trabeculation CMR risk score. [*JACC Cardiovasc Imaging* 2026.](https://doi.org/10.1016/j.jcmg.2026.07.027) PMID [42841847](https://pubmed.ncbi.nlm.nih.gov/42841847/)
16. Umei M, et al. ACHD acquired risk factors. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag787) PMID [42834856](https://pubmed.ncbi.nlm.nih.gov/42834856/)
17. Wang C, et al. IHCA in China registry. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.080404) PMID [42836281](https://pubmed.ncbi.nlm.nih.gov/42836281/)

**Case Reports**
18. Iyengar A, et al. [*JACC Case Rep* 2026:110627.](https://doi.org/10.1016/j.jaccas.2026.110627) PMID [42841825](https://pubmed.ncbi.nlm.nih.gov/42841825/) ｜ 19. Tamura Y, et al. [*J Artif Organs* 2026.](https://doi.org/10.1007/s10047-026-01599-y) PMID [42853285](https://pubmed.ncbi.nlm.nih.gov/42853285/) ｜ 20. Ohashi H, et al. [*JACC Case Rep* 2026:110640.](https://doi.org/10.1016/j.jaccas.2026.110640) PMID [42848359](https://pubmed.ncbi.nlm.nih.gov/42848359/) ｜ 21. Duband B, et al. [*Ann Cardiol Angeiol* 2026:102087.](https://doi.org/10.1016/j.ancard.2026.102087) PMID [42844064](https://pubmed.ncbi.nlm.nih.gov/42844064/) ｜ 22. Bhagirath P, et al. [*Heart Rhythm* 2026.](https://doi.org/10.1016/j.hrthm.2026.09.055) PMID [42849683](https://pubmed.ncbi.nlm.nih.gov/42849683/)

---

<!-- _class: abbr -->
# 縮寫對照表 (1/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| PE | Pulmonary Embolism | 肺栓塞 |
| RV / LV | Right / Left Ventricle | 右／左心室 |
| CAVT | Computer-Assisted Vacuum Thrombectomy | 電腦輔助真空機械取栓 |
| PERT | Pulmonary Embolism Response Team | 肺栓塞反應團隊 |
| PCI | Percutaneous Coronary Intervention | 經皮冠狀動脈介入 |
| FFR | Fractional Flow Reserve | 血流儲備分數 |
| IVUS / OCT | Intravascular Ultrasound / Optical Coherence Tomography | 血管內超音波／光學同調斷層 |
| NIRS | Near-Infrared Spectroscopy | 近紅外光譜 |
| LCBI | Lipid Core Burden Index | 脂質核心負荷指數 |
| LRP | Lipid-Rich Plaque | 脂質豐富斑塊 |
| OMT | Optimal Medical Therapy | 最佳藥物治療 |
| DES / SEB | Drug-Eluting Stent / Sirolimus-Eluting Balloon | 藥物釋放支架／希羅莫斯藥物球囊 |
| HBR / DAPT | High Bleeding Risk / Dual Antiplatelet Therapy | 高出血風險／雙重抗血小板治療 |
| TVF / NACE | Target Vessel Failure / Net Adverse Clinical Events | 標的血管失敗／淨臨床不良事件 |
| AF | Atrial Fibrillation | 心房顫動 |
| CSP / BVP | Conduction System / Biventricular Pacing | 傳導系統節律／雙心室節律 |
| PFA / VT / RF | Pulsed Field Ablation / Ventricular Tachycardia / Radiofrequency | 脈衝場消融／心室頻脈／射頻 |
| LVEF | Left Ventricular Ejection Fraction | 左心室射血分數 |
| HR / aHR / aOR | (adjusted) Hazard / Odds Ratio | （校正）風險比／勝算比 |
| NI / NS | Non-Inferiority / Not Significant | 非劣性／未達顯著 |

---

<!-- _class: abbr -->
# 縮寫對照表 (2/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| TAVI / TAVR | Transcatheter Aortic Valve Implantation / Replacement | 經導管主動脈瓣植入／置換 |
| AS | Aortic Stenosis | 主動脈瓣狹窄 |
| PPM | Permanent Pacemaker | 永久性節律器 |
| RBBB / LBBB | Right / Left Bundle Branch Block | 右／左束支傳導阻滯 |
| CD | Conduction Disturbance | 傳導障礙 |
| VARC-3 | Valve Academic Research Consortium-3 | 瓣膜學術研究聯盟第 3 版 |
| TEER / M-TEER / T-TEER | (Mitral/Tricuspid) Transcatheter Edge-to-Edge Repair | （二尖／三尖瓣）經導管緣對緣修復 |
| MR / TR | Mitral / Tricuspid Regurgitation | 二尖瓣／三尖瓣逆流 |
| PADN | Pulmonary Artery Denervation | 肺動脈去神經術 |
| PH / mPAP | Pulmonary Hypertension / mean Pulmonary Artery Pressure | 肺高壓／平均肺動脈壓 |
| LAH / AFR | Left Atrial Hypertension / Atrial Flow Regulator | 左心房高壓／心房血流調節器 |
| ASD / PFO | Atrial Septal Defect / Patent Foramen Ovale | 心房中隔缺損／開放性卵圓孔 |
| TEE / CMR / LGE | Transesophageal Echo / Cardiac MR / Late Gadolinium Enhancement | 經食道超音波／心臟磁振造影／晚期釓增強 |
| ACS / NSTEMI | Acute Coronary Syndrome / Non–ST-Elevation MI | 急性冠心症／非 ST 上升心梗 |
| RCA / LAD | Right Coronary Artery / Left Anterior Descending | 右冠狀動脈／左前降支 |
| CIED / IE / MSSA | Cardiac Implantable Electronic Device / Infective Endocarditis / Methicillin-Sensitive S. aureus | 心臟植入式電子裝置／感染性心內膜炎／甲氧西林敏感金黃葡萄球菌 |
| MCS / LVAD | Mechanical Circulatory Support / Left Ventricular Assist Device | 機械循環支持／左心室輔助裝置 |
| ACHD / IHCA | Adult Congenital Heart Disease / In-Hospital Cardiac Arrest | 成人先天性心臟病／院內心跳停止 |
| SYNTAX | Synergy Between PCI with Taxus and Cardiac Surgery score | 冠脈病變複雜度評分 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**
心臟內科｜結構性心臟病介入

*本文件為讀書會共筆之教學整理，*
*僅供醫療專業同仁臨床教學交流參考。*
