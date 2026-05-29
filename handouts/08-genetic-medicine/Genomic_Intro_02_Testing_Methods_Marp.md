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
  section.lead { background-color: #1a2740; color: #ffffff; }
  section.lead h1 { color: #ffffff; font-size: 2.1em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.divider {
    background-color: #0072bc; color: white;
    display: flex; justify-content: center; align-items: center;
  }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.5em; text-align: center; }
  section.divider h2 { color: #ffe169; }
  section.divider h3 { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.68em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b; background-color: #fff5f5;
    padding: 0.5em 1em; font-size: 0.88em;
  }
  pre {
    background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1;
    border-radius: 8px; padding: 0.8em; font-size: 0.64em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.82em; }
footer: '謝慕揚 MD, PhD, FESC | 基因體醫學入門 第二課：檢測方式與優勢 | 2026'
---

<!-- _class: lead -->
# 基因體醫學入門 · 第二課
## 目前的檢測方式與優勢
### Testing Methods & Advantages — Sanger / NGS / Panel / WES / WGS
**讀書會共筆整理** | 心臟科取向入門 | 2026
講者：謝慕揚／新育／凱鈞（擇一）｜審稿：洛嘉

---

# 這一課的目標

- 第一課學了**字彙**；這一課看這些變異**怎麼被測出來**
- 搞懂三件事：
  1. **定序原理**（Sanger vs NGS，白話版）
  2. **檢測選單**（單基因 / panel / 全外顯子 WES / 全基因體 WGS）怎麼挑
  3. **NGS 的優勢與限制**——尤其報告怎麼看、地雷在哪

> 心臟科實務主軸：**疾病導向的基因 panel** 是最常用、CP 值最高的選擇。

---

<!-- _class: divider -->
# Part 1
## 定序原理：白話版

---

# Sanger 定序：老牌黃金標準

- 1977 年問世的**鏈終止法 (chain-termination)**，毛細管電泳判讀
- 一次讀**一段**（單一基因/單一外顯子），準確、判讀單純
- 缺點：**慢、貴、無法規模化**——要測很多基因就不切實際

> 現今角色：**確認 (confirmation)**——NGS 找到的關鍵變異，常再用 Sanger 驗證；以及家族單點 cascade 篩檢。

---

# NGS：大規模平行定序

- **次世代定序 (next-generation sequencing, NGS)** = **massively parallel sequencing**
- 把 DNA 打碎成大量短片段，**同時**讀數百萬～數十億條（Illumina 的 sequencing-by-synthesis 為主流）
- 再用電腦**比對 (align)** 回參考基因體、找出差異

關鍵名詞：
- **read**：一條被讀出的短序列
- **覆蓋深度 coverage / depth**（如 100×）：同一位置被讀了幾次 → 愈深愈可靠
- 動畫見延伸資源（Virology Lab / Henrik's Lab / iBiology）

---

# 一張圖看懂流程

```text
檢體(血) → 抽 DNA → 打碎+建庫(library prep) → 上機定序(平行)
   → 產生數百萬條 reads → 比對參考基因體(align)
   → 變異判讀(variant calling) → ACMG 分級 → 報告
                                   │
                        關鍵變異 →─┴─→ Sanger 確認
```

> 從抽血到報告，**判讀 (interpretation)** 往往才是最耗時、最需要專業的瓶頸——不是機器，是人。

---

<!-- _class: divider -->
# Part 2
## 檢測選單：panel / WES / WGS 怎麼挑

---

# 四種範圍，由小到大

| 方法 | 範圍 | 一句話 |
|------|------|--------|
| 單基因 Sanger | 1 個基因/位點 | 已知家族變異的 cascade 確認 |
| **疾病基因 panel** (NGS) | 數十～數百個**選定**基因 | **心臟科最常用**：聚焦、好判讀 |
| 全外顯子 **WES** | 所有基因的外顯子 (~1–2%) | 表型複雜/panel 陰性時擴大搜尋 |
| 全基因體 **WGS** | 整個基因體（含非編碼區） | 最完整，含 CNV/結構變異，資料最龐大 |

---

# 範圍越大 ≠ 越好：四象限權衡

| 面向 | panel | WES | WGS |
|------|-------|-----|-----|
| 偵測廣度 | 低（只看選定基因） | 中高 | 最高 |
| **VUS 數量** | **少** | 多 | 最多 |
| **意外發現** (secondary findings) | 少 | 多 | 多 |
| 判讀複雜度/成本 | 低 | 中 | 高 |
| 適用時機 | 表型明確（如典型 HCM） | 表型不典型/多系統 | 研究、疑難、CNV 重要時 |

> **臨床智慧**：表型越明確，越該用**窄 panel**——少踩 VUS、少製造焦慮、判讀更乾淨。

---

# 別忘了「點變異以外」的方法

| 變異類型 | 適合的方法 | 心臟例子 |
|----------|------------|----------|
| 點變異 SNV / 小 indel | NGS、Sanger | 多數 HCM/LQTS 變異 |
| **拷貝數變異 CNV**（大段缺失/重複） | **MLPA**、array CGH、NGS-CNV pipeline | `LDLR` 大段缺失 → FH |
| 重複序列、偽基因區 | 長讀長定序 (long-read)、特殊設計 | 部分基因難測區 |

> 標準短讀長 NGS 對 **CNV、重複序列、偽基因 (pseudogene)** 區域有盲點——FH 若 panel 陰性但臨床高度懷疑，要追加 CNV 偵測（如 MLPA）。

---

<!-- _class: divider -->
# Part 3
## NGS 的優勢與限制

---

# 優勢 (Advantages)

> NGS 的革命：**一次、平行、便宜地**看很多基因。

- **高通量**：一次測數十～數百基因（甚至全外顯子/基因體）
- **每鹼基成本大幅下降**：讓臨床基因檢測得以普及
- **可發現非預期診斷**：表型重疊時（如「心肌肥厚」可能是 HCM、Fabry、ATTR、Noonan…）一次釐清
- **可量化**：覆蓋深度、變異等位比例 (VAF) 提供品質與somatic線索

---

# 限制與「地雷」(Limitations)

- **VUS 負擔**：基因看越多，意義未明變異越多 → 溝通與追蹤成本
- **意外/次要發現 (secondary findings)**：ACMG 建議回報的次要發現清單**包含多個心臟基因**（心肌病、心律不整、FH、主動脈病變）——檢測前須**知情同意**是否想知道
- **技術盲點**：CNV、重複序列、偽基因、低覆蓋區可能漏掉
- **判讀瓶頸**：報告品質取決於實驗室與資料庫；分級會**隨時間改變**
- **週轉時間 (TAT) 與成本**：panel 數週、WES/WGS 更久更貴

---

# 報告怎麼看（實戰檢查清單）

```text
□ 基因 + HGVS 座標（c. 與 p.，含參考轉錄本 NM_）
□ ACMG 分級：P / LP / VUS / LB / B
□ 合子性 zygosity：het / hom / compound het / hemizygous
□ 覆蓋深度與品質：關鍵區域夠深嗎？有無低覆蓋警示
□ 分類依據：ClinVar / gnomAD(MAF) / ClinGen 證據
□ 實驗室建議：是否需 Sanger 確認、是否建議家族篩檢
□ 次要發現：報告範圍是否包含、病人是否同意知道
```

> 看到 **VUS** 不要當成陽性處理；看到 **P/LP** 才啟動臨床決策與 cascade 篩檢。

---

# 台灣現況（健保與送驗）

- 部分**疾病導向 panel** 在特定適應症下有健保給付，許多仍需**自費**；給付範圍與品項**會隨政策更動**。
- 送驗管道：醫學中心**基因醫學部／精準醫學中心**之高通量定序實驗室（如臺大醫院基因醫學部、臺北榮總精準醫學暨基因體中心）。
- **務必確認當下的給付與費用**：報告前向所屬實驗室/基因醫學部查證最新資訊。

> 詳細的台灣健保給付與檢測現況，見內部講義《基因精準醫學與心臟病》第 8 節。

---

# Take-home（第二課）

> 1. **Sanger** = 黃金標準、用於**確認**與單點 cascade；**NGS** = 大規模平行、臨床主力。
> 2. 選範圍的原則：**表型越明確 → panel 越窄越好**（少 VUS、少意外發現、好判讀）。
> 3. NGS 有**盲點**（CNV、重複序列、偽基因）——高度懷疑而 panel 陰性時要追加方法（如 MLPA）。
> 4. 報告看：**HGVS 座標 → ACMG 分級 → 合子性 → 覆蓋深度 → 證據與建議**。
> 5. **次要發現含心臟基因**、且分類**會變**——檢測前同意、檢測後可重新分類。

下一課：把這些方法**用在真實心臟病人**——從表型到檢測、判讀、家族篩檢、治療。

---

<!-- _class: small-text -->
# 延伸資源（已查證）

- 影片：Next Generation Sequencing Animation（Virology Lab）<https://www.youtube.com/watch?v=cSdyHLm6EQY>
- 影片：NGS (Illumina) — An Introduction（Henrik's Lab）<https://www.youtube.com/watch?v=CZeN-IgjYCo>
- 影片：NGS 2 — Illumina Sample Prep, Eric Chow（iBiology）<https://www.youtube.com/watch?v=PFwSe09dJX0>
- Illumina — NGS for Beginners：<https://www.illumina.com/science/technology/next-generation-sequencing/beginners.html>
- 臺大醫院基因醫學部：<https://www.ntuh.gov.tw/gene/Index.action> ｜ 臺北榮總精準醫學暨基因體中心 NGS：<https://wd.vghtpe.gov.tw/cpmg/Fpage.action?muid=14440&fid=13251>

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**讀書會共筆整理** · 審稿：洛嘉
僅供醫療專業人員教學參考
