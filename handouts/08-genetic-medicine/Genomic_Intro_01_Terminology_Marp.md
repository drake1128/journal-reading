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
  table { font-size: 0.70em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b; background-color: #fff5f5;
    padding: 0.5em 1em; font-size: 0.88em;
  }
  pre {
    background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1;
    border-radius: 8px; padding: 0.8em; font-size: 0.66em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.82em; }
footer: '謝慕揚 MD, PhD, FESC | 基因體醫學入門 第一課：用字與縮寫 | 2026'
---

<!-- _class: lead -->
# 基因體醫學入門 · 第一課
## 基本基因用字與縮寫
### Genomic Medicine 101 — Terminology & Abbreviations
**讀書會共筆整理** | 心臟科取向入門 | 2026
講者：謝慕揚／新育／凱鈞（擇一）｜審稿：洛嘉

---

# 這一課的目標

- 把後兩課（檢測方式、臨床案例）會反覆出現的**字彙與縮寫**先講清楚
- 不需要背——建立**直覺**：看到一個基因報告，知道每個詞在說什麼
- 全程以**心臟疾病**當例子（HCM、LQTS、Brugada、Fabry、ATTR、FH）

> **一句話**：基因報告不可怕，它只是用一套固定的「文法」描述「哪個基因、哪個位置、改了什麼、有沒有意義」。

---

<!-- _class: divider -->
# Part 1
## 從 DNA 到蛋白質：最小必要知識

---

# DNA → 基因 → 蛋白質（中心法則）

```text
DNA  ──轉錄(transcription)──▶  mRNA  ──轉譯(translation)──▶  蛋白質
（基因 gene）                  （訊息）                      （功能）
```

- **基因 (gene)**：一段 DNA 的「食譜」，指導製造某個蛋白質
- 人類約 **20,000 個基因**，分布在 23 對染色體 (chromosome) 上
- **外顯子 (exon)**：真正轉譯成蛋白質的片段
- **內含子 (intron)**：基因內不轉譯的片段（會被剪接 splice 掉）

> **書寫慣例**：人類**基因符號**一律以**大寫、斜體**表示（如 *MYH7*、*LDLR*、*COL4A1*）；對應的**蛋白質**則用**正體**（如 β-myosin heavy chain）。本投影片以等寬字標示基因僅為視覺辨識。
>
> 心臟例子：*MYH7* 基因 → β-myosin heavy chain 蛋白 → 心肌收縮單位的一部分；出問題 → **肥厚性心肌病變 (HCM)**。

---

# 基因體 vs 外顯子體

| 名詞 | 是什麼 | 佔基因體 | 臨床意義 |
|------|--------|----------|----------|
| **基因體 (genome)** | 全部 DNA（~30 億鹼基對） | 100% | 最完整、也最貴最複雜 |
| **外顯子體 (exome)** | 所有基因的外顯子總和 | 約 1–2% | 卻涵蓋 **~85%** 已知致病變異 |
| **基因套組 (panel)** | 針對某疾病挑選的一組基因 | 極小 | CP 值高、判讀單純（**臨床最常用**） |

> 這就是為什麼「心肌病基因 panel」是心臟科最常開的檢測——聚焦、便宜、好判讀（第二課詳述）。

---

<!-- _class: divider -->
# Part 2
## 變異 (Variant) 的語言

---

# variant / mutation / polymorphism

- **變異 (variant)**：DNA 序列與參考序列不同之處——**中性詞，現今標準用語**
- **突變 (mutation)**：舊用語，常帶「有害」暗示 → 現多改稱 variant
- **多型性 (polymorphism)**：族群中**常見**的變異（次要等位基因頻率 MAF > 1%），多半無害

> **重點**：「有變異」≠「有病」。大多數變異是良性的；關鍵在後面的**分類 (classification)**。

---

# 變異的類型

| 類型 | 英文 | 說明 | 心臟例子 |
|------|------|------|----------|
| 單核苷酸變異 | **SNV** (single-nucleotide variant) | 單一鹼基改變（點變異） | *SCN5A* 點變異 → Brugada |
| 插入/缺失 | **indel** | 少數鹼基插入或缺失 | 可能造成 frameshift |
| 結構變異 | **SV** (structural variant，通常 **>50 bp**) | 大片段改變：deletion、duplication、insertion、inversion、translocation、complex rearrangement | *LDLR* 大段重排 → FH |
| 拷貝數變異 | **CNV** (copy-number variant) | **SV 的一種**：某段大片段 DNA 的缺失 (copy number loss) 或重複 (copy number gain) | *LDLR* 大段缺失/重複 → FH |

- **同義/錯義/無義**：silent (不改胺基酸)、missense (改胺基酸)、nonsense (提早終止 stop)
- **frameshift**：indel 造成讀框位移，常使蛋白質截短

> **SV ⊃ CNV**：CNV 嚴格來說是 SV 的一個子類（只涉及套數增減）。**FH 由 *LDLR* 的 SV/CNV 致病相當常見**——若 panel 只偵測點變異而不含 CNV/SV 偵測，可能漏診。

---

# Germline vs Somatic（心臟科很重要的分野）

| | 生殖細胞系 **germline** | 體細胞 **somatic** |
|--|--------------------------|---------------------|
| 來源 | 與生俱來，**每個細胞都有** | 後天獲得，**只在部分細胞** |
| 遺傳 | **會遺傳**給下一代 | 不會遺傳 |
| 心臟例子 | 遺傳性心肌病/離子通道病（HCM、LQTS） | clonal hematopoiesis (CHIP)、腫瘤 |
| 檢體 | 血液、口腔黏膜 | 腫瘤組織、特定細胞群 |

> 心臟遺傳病基本都是 **germline**；這也是為什麼一個人確診後，要談**家族篩檢 (cascade screening)**。

---

# 描述「一個人」的基因狀態

- **基因型 (genotype)** vs **表現型 (phenotype)**：帶什麼變異 vs 實際表現出什麼
- **合子性 (zygosity)**：
  - 同型合子 homozygous（兩條染色體都變異）
  - 異型合子 heterozygous（一條變異）
  - 複合異型合子 compound heterozygous（兩條各帶不同變異）
  - 半合子 hemizygous（男性 X 染色體單套，如 Fabry `GLA`）
- **新生變異 de novo**：父母都沒有、子代新出現
- **嵌合 mosaicism**：體內部分細胞帶變異

---

# Penetrance 與 Expressivity（最常被混淆）

| 名詞 | 定義 | 心臟例子 |
|------|------|----------|
| **外顯率 penetrance** | 帶變異者中「**會不會**」表現出疾病的比例 | HCM 致病變異**外顯率不完全**：帶變異不一定發病 |
| **表現度 expressivity** | 發病者「**症狀多重**」的變異程度 | 同一家族同一變異，有人輕微肥厚、有人猝死 |

> 臨床啟示：基因陽性但目前無症狀（**genotype-positive / phenotype-negative**）的家屬，仍需**定期追蹤**，因為外顯可能延遲發生。

---

# 三組最容易混淆的詞：expressivity / pleiotropy / heterogeneity

| 名詞 | 一句話定義 | 例子 |
|------|------------|------|
| **表現度差異 variable expressivity** | **同一基因／同一變異**，發病者「**嚴重度不同**」 | 同家族同一變異：有人輕微肥厚、有人猝死 |
| **多效性 pleiotropy** | **同一個基因**造成**多種不同表型** | *COL4A1*：腦小血管病變、眼部異常、腎臟表現、肌肉痙攣——病人可能來自**不同門診 entry**，查到最後竟是同一基因 |
| **遺傳異質性 genetic heterogeneity** | **不同基因**造成**相似表型** | HCM 可由 *MYH7*、*MYBPC3* 等多個基因致病 |

> **expressivity vs pleiotropy 最常被搞混**：前者談「**同表型、輕重不同**」；後者談「**同基因、不同表型**」。遺傳異質性則是反過來「不同基因 → 同表型」。

---

<!-- _class: divider -->
# Part 3
## 遺傳模式與家系圖

---

# 遺傳模式 (Inheritance Patterns)

| 模式 | 特徵 | 心臟例子 |
|------|------|----------|
| 體染色體顯性 **AD** | 一條變異即可發病；子代 **50%** 機率 | 多數 HCM、LQTS、ATTR(TTR) |
| 體染色體隱性 **AR** | 需兩條都變異 | 部分代謝性心肌病 |
| X 染色體連鎖 **X-linked** | 男性受影響較重 | **Fabry (`GLA`)** |
| 粒線體 **mitochondrial** | **母系**遺傳 | 粒線體心肌病 |

> AD「50:50」是給家屬諮詢時最關鍵的數字：每個孩子各有一半機率帶到變異。

---

# 家系圖 (Pedigree) 看圖說故事

```text
□ 男性   ○ 女性   ■/● 受影響   ╱ 已歿
箭頭(proband) = 先證者（家族中第一個被檢查的人）

      □──●  （父正常, 母帶 AD 變異/HCM）
        │
   ┌────┼────┐
   ●    □    ○   ← 每位子代各 50% 帶變異
 (HCM) (正常) (帶因待追蹤)
```

- **先證者 (proband)**：通常是因症狀就醫、啟動整個家族評估的人
- 畫出三代家系，常能一眼看出遺傳模式與**該篩檢誰**

---

<!-- _class: divider -->
# Part 4
## 變異怎麼命名、怎麼分級

---

# HGVS 命名法：報告上的「座標」

兩個層級，務必看清楚是哪一層：

```text
NM_000257.4(MYH7):c.1528G>C   ← c. = 在 DNA(coding)層級
                p.(Gly510Arg)  ← p. = 對應到蛋白質胺基酸改變
└─參考轉錄本─┘ └基因┘ └位置與改變┘
```

- **必須附參考轉錄本 (NM_...)**：同一基因不同轉錄本座標不同
- `c.` 看 DNA、`p.` 看蛋白質；報告兩者並列
- 看到 `fs`（frameshift）、`*`/`Ter`（提早終止）通常代表較強的致病證據

---

# 進階：allele 層級的寫法與 phasing

正式報告除了用 HGVS 描述**單一變異**外，因為一個基因有**兩條 allele**，部分實驗室會更精確地以 **allele 形式**呈現：

```text
NM_004006.2:c.[2376G>C];[3103del]
              └─ allele 1 ─┘ └ allele 2 ┘
```

- 中括號 `[ ]` 各代表**一條 allele**；上式表示**兩條 allele 各帶一個變異**
- 兩個變異分屬不同 allele → 互為 **in trans**（若在同一條則為 *in cis*）
- **phasing（定相）** 對**體染色體隱性 (AR)** 疾病判讀尤其關鍵：兩個致病變異**必須 in trans**（一父一母）才會致病；若 in cis，另一條 allele 仍正常。

> 看到 `c.[...];[...]` 不要當成兩個獨立報告——它在告訴你「**這兩個位點各在哪一條 allele**」。

---

# ACMG/AMP 五級分類（最重要的一張表）

| 分級 | 英文 | 臨床處置 |
|------|------|----------|
| 致病性 | **Pathogenic (P)** | 可作臨床決策、家族 cascade 篩檢 |
| 可能致病 | **Likely pathogenic (LP)** | 多數情況比照 P 處理 |
| 意義未明 | **VUS** (uncertain significance) | **不可**用於臨床決策或篩檢；持續追蹤 |
| 可能良性 | **Likely benign (LB)** | 一般不予理會 |
| 良性 | **Benign (B)** | 不予理會 |

- 依據 Richards et al. *Genet Med* 2015（ACMG/AMP）：28 條證據（PVS1/PS/PM/PP 致病、BA1/BS/BP 良性）組合判定。

---

# VUS：臨床上最容易踩雷的詞

> **VUS（意義未明變異）不是「壞消息」，也不是「沒事」——它是「證據還不夠」。**

- ❌ 不可據以做預防性治療、植入 ICD、或叫家屬一起檢測
- ✅ 可隨證據累積**重新分類**（reclassification）——可能升為 LP/P，也可能降為 LB/B
- ✅ 病人/家屬衛教重點：說明「未明」≠「危險」，避免過度焦慮或錯誤安心

> 詳見內部講義《基因醫學心臟病學：範例臨床情境分析》情境 1、8。

---

# 判讀靠的三大公開資料庫

| 資料庫 | 用途 | 心臟科怎麼用 |
|--------|------|--------------|
| **ClinVar** | 變異↔臨床意義的公開彙整 | 查這個變異別人怎麼分級 |
| **gnomAD** | >80 萬人的族群等位基因頻率 | 太常見 (高 **MAF**) → 傾向良性 |
| **ClinGen** | 基因/變異專家策展、規則細化 | 看該基因與疾病的關聯強度 |

- **MAF (minor allele frequency)**：族群中該變異的頻率；**愈罕見**愈可能與罕見遺傳病相關。

---

# ACMG 之外：ClinGen 疾病專屬判讀標準

- ACMG/AMP 2015 是**通用框架**；不少證據條目（如 PM1、PP2、BS3）需要**依基因/疾病微調**。
- **ClinGen 變異策展專家小組 (Variant Curation Expert Panel, VCEP)** 會針對特定疾病/基因發布**專屬判讀規格 (specifications)**，並進行**基因—疾病關聯效度 (gene–disease validity) 策展**。
- 與謝主任投影片中疾病相關的 Expert Panel：

| 疾病 / 基因群 | Expert Panel 產出 | 文獻 |
|----------------|-------------------|------|
| **RASopathy**（Noonan 等） | 更新版 ACMG/AMP 判讀規格 + 基因策展 | Wilcox EH, et al. *Genet Med Open*. 2025;3:103430 [PMID 40496714] |
| **肥厚性心肌病 HCM** | HCM 基因臨床效度評估（哪些基因證據足夠） | Ingles J, et al. *Circ Genom Precis Med*. 2019;12(2):e002460 [PMID 30681346] |

> 實務：判讀心臟基因變異前，先查該基因/疾病是否有 **ClinGen VCEP 專屬規格**，有則**優先採用**而非僅用通用 ACMG。

---

# 把字彙對到心臟基因（總整理）

| 疾病 | 代表基因 | 遺傳 | 用到的字彙 |
|------|----------|------|------------|
| 肥厚性心肌病 HCM | *MYH7*, *MYBPC3* | AD | missense、不完全外顯、遺傳異質性 |
| 長 QT 症候群 LQTS | *KCNQ1*, *KCNH2*, *SCN5A* | AD | SNV、離子通道 |
| Brugada 症候群 | *SCN5A* | AD | SNV、表現度差異大 |
| Fabry 氏症 | *GLA* | **X-linked** | 半合子（男性） |
| ATTR 類澱粉沉積 | *TTR* | AD | missense（如 V122I） |
| 家族性高膽固醇 FH | *LDLR*, *APOB*, *PCSK9* | AD | SV/CNV（*LDLR* 大段缺失/重複常見） |

---

# 縮寫對照表（共用）

| 縮寫 | 全名 (English) | 中文 |
|------|----------------|------|
| NGS | next-generation sequencing | 次世代定序 |
| WES / WGS | whole-exome / whole-genome sequencing | 全外顯子／全基因體定序 |
| SNV / indel | single-nucleotide variant / insertion-deletion | 單核苷酸變異／插入缺失 |
| SV / CNV | structural variant / copy-number variant | 結構變異／拷貝數變異（CNV 為 SV 子類） |
| VCEP | Variant Curation Expert Panel (ClinGen) | （ClinGen）變異策展專家小組 |
| VUS | variant of uncertain significance | 意義未明變異 |
| P / LP / B / LB | pathogenic / likely pathogenic / benign / likely benign | 致病／可能致病／良性／可能良性 |
| ACMG / AMP | Am. College of Medical Genetics / Assoc. for Molecular Pathology | 美國醫學遺傳學會／分子病理學會 |
| HGVS | Human Genome Variation Society | 人類基因體變異學會（命名法） |
| MAF / VAF | minor allele frequency / variant allele fraction | 次要等位基因頻率／變異等位比例 |
| AD / AR | autosomal dominant / recessive | 體染色體顯性／隱性 |

---

# Take-home（第一課）

> 1. **variant 是中性詞**；有變異不等於有病，關鍵在**分類**。
> 2. **germline**（遺傳、每個細胞、會傳下一代）是心臟遺傳病的主場 → 牽動**家族篩檢**。
> 3. 報告看三件事：**哪個基因/HGVS座標** → **ACMG 五級** → **資料庫證據 (ClinVar/gnomAD)**。
> 4. **VUS = 證據不足**，不做臨床決策、可隨時間重新分類。
> 5. **不完全外顯**：基因陽性、目前無症狀者仍需追蹤。

下一課：這些變異**怎麼被測出來**——Sanger、NGS、panel/WES/WGS 與各自優勢。

---

<!-- _class: small-text -->
# 延伸資源（已查證）

- NHGRI Talking Glossary of Genomic & Genetic Terms：<https://www.genome.gov/genetics-glossary>
- MedlinePlus — Help Me Understand Genetics：<https://medlineplus.gov/genetics/understanding/>
- Richards S, et al. ACMG/AMP variant interpretation standards. *Genet Med*. 2015;17:405-424. [PubMed 25741868](https://pubmed.ncbi.nlm.nih.gov/25741868/)
- Wilcox EH, et al. Updated ACMG/AMP specifications and gene curations from the ClinGen RASopathy expert panels. *Genet Med Open*. 2025;3:103430. [PubMed 40496714](https://pubmed.ncbi.nlm.nih.gov/40496714/) ｜ [DOI](https://doi.org/10.1016/j.gimo.2025.103430)
- Ingles J, et al. Evaluating the Clinical Validity of Hypertrophic Cardiomyopathy Genes. *Circ Genom Precis Med*. 2019;12(2):e002460. [PubMed 30681346](https://pubmed.ncbi.nlm.nih.gov/30681346/) ｜ [DOI](https://doi.org/10.1161/CIRCGEN.119.002460)
- HGVS 變異命名法：<https://hgvs-nomenclature.org/>
- 內部講義：《基因精準醫學與心臟病》《基因醫學心臟病學：範例臨床情境分析》

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**讀書會共筆整理** · 審稿：洛嘉
僅供醫療專業人員教學參考
