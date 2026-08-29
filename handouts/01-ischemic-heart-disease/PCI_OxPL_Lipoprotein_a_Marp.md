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
  section.lead h3 { color: #dfe6e9; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #8ab4f8; }
  section.lead blockquote {
    background-color: #f5f6fa;
    color: #2d3436;
    border-left: 4px solid #ba181b;
  }
  section.lead blockquote strong { color: #ba181b; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: white;
    border-bottom: none;
    font-size: 2.4em;
    text-align: center;
  }
  section.divider h2 { color: #ffe066; text-align: center; }
  section.divider h3 { color: #ffffff; text-align: center; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.55em; }
  h2 { color: #0072bc; font-size: 1.1em; }
  h3 { color: #555555; }
  table { font-size: 0.68em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.85em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 0.62em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.8em; }
  section.ref { font-size: 0.62em; }
footer: '謝慕揚 MD, PhD, FESC | PCI 後 OxPL 與 Lp(a) 急性上升 | 2026'
---

<!-- _class: lead -->

# PCI 後氧化磷脂與 Lp(a) 的急性上升

## Percutaneous Coronary Intervention Results in Acute Increases in Oxidized Phospholipids and Lipoprotein(a)

### Tsimikas S, et al. *Circulation.* 2004;109(25):3164–3170

**謝慕揚 MD, PhD, FESC** | 2026-08-29

[原文連結 — https://doi.org/10.1161/01.CIR.0000130844.01174.55](https://doi.org/10.1161/01.CIR.0000130844.01174.55)

> **機轉型研究，無臨床終點** — 不可據以改變臨床決策

---

# 一句話總結

> **做一次 PCI，血漿裡幾分鐘內冒出一批氧化磷脂 (OxPL) 與 Lp(a)，6 小時退掉；但免疫系統會記得長達 6 個月。**

- 141 位穩定型心絞痛、選擇性且無併發症 PCI
- 術後即刻：**OxLDL-E06 ↑36%**、**Lp(a) ↑64%**（皆 P < 0.001）
- **6 小時回到 baseline**
- **只做血管攝影的 50 位對照組完全沒有變化**
  → 不是導管或顯影劑，是**器械真的動到了斑塊**

---

# 為什麼讀一篇 2004 年的老文章

1. **它解釋了 Lp(a) 為什麼「不只是一顆膽固醇顆粒」**
   致病關鍵在於它**攜帶氧化磷脂 (OxPL)**

2. **它示範了一個乾淨的對照設計**
   用「只做血管攝影」把導管 + 顯影劑的效應扣掉

3. **它提出一個至今未定論的假說**
   Lp(a) 原本可能是**抗氧化壓力的先天免疫成員**（類似 CRP）

> **給導管室的一句話**：我們每天做的每一次擴張與置放支架，
> 在生化層面上都是一次**可測量的斑塊擾動**。

---

<!-- _class: divider -->

# 到底測了什麼？

## OxLDL、OxPL、E06 抗體

---

# 名詞拆解

| 名稱 | 意義 |
|------|------|
| **OxLDL** | 氧化低密度脂蛋白 — 是統稱，不是單一分子 |
| **OxPL** | 氧化磷脂，具促發炎活性 |
| **E06** | 鼠源單株抗體，**只認氧化磷脂的 phosphorylcholine head group**，不認正常磷脂 |
| **MB47** | 抗 apoB-100 抗體，用來**把每孔的顆粒數固定住** |
| **OxLDL-E06** | 「**每一顆 apoB-100 顆粒上帶多少 OxPL**」 |
| **LPA4** | 新開發的抗 apo(a) 抗體，**不與 plasminogen 交叉反應** |

> **關鍵巧思**：MB47 先把每孔 apoB-100 顆粒數固定成飽和且相同
> → E06 訊號代表**「每顆顆粒的氧化程度」**，不是「總顆粒多寡」

---

# Assay 品質

- **LPA4 驗證**：以人類 Lp(a) 免疫小鼠，篩選可結合 apo(a) 胜肽 `TRNYCRNPDAEIRP` 的融合瘤
  - **不與 plasminogen 交叉反應**（apo(a) 與 plasminogen 高度同源，這點很重要）
  - 與市售 assay (Diasorin) **r = 0.96, n = 500, P < 0.0001**

- **所有 assay 三重複測**

- **Intra-assay CV 6–10%**

- 單位為 **RLU (relative light units)** — ⚠️ 非標準化單位，**跨研究不可直接比較**

---

<!-- _class: divider -->

# 研究設計

## Methods

---

# 族群與對照組

**PCI 組**
- 單中心前瞻性；原始 156 位**穩定型心絞痛**、**選擇性、無併發症** PCI
- 有血液檢體 **141 位**；6 個月血管攝影追蹤 **134 位 (95%)**
- 男 77%、DM 18%、HTN 44%、抽菸 39%、過去 MI 26%
- **氣球擴張 69%、支架 31%**（2004 年時代背景）

**對照組（本文設計的支柱）**
- **50 位只做診斷性血管攝影、無任何介入**，攝影前後各取一次

> 這一組把「顯影劑 + 導管 + 躺在台上」的效應扣除掉
> → 對照組沒變化，剩下的訊號才能歸因於**介入本身**

---

# 取樣時間點（9 個）

```text
PCI 前 → PCI 後即刻 → 6 小時 → 24 小時 → 3 天
       → 1 週 → 1 個月 → 3 個月 → 6 個月
```

**密集的早期取樣（即刻、6 小時）是抓到訊號的關鍵**
沒有這兩點，只會看到一片平坦

**統計**（GraphPad InStat v3.02）
- 組內時序：one-way ANOVA（Bonferroni／Kruskal-Wallis）
- 對照組前後：paired t test；相關性：**Spearman**
- 因 Lp(a)／OxLDL **絕對值非常態分布**，改以**個人內百分比變化**分析

---

# 免疫沉澱實驗：回答一個關鍵問題

**問題**：血漿裡的 OxPL，到底掛在 **Lp(a)** 上，還是掛在**其他 apoB 顆粒**上？

**做法**
- 取 5 位（Lp(a) 與 OxLDL-E06 術後值最高者）
- 時間點：pre-PCI、post-PCI、6 h、24 h、6 個月
- 加入**遞增劑量 LPA4 抗體（0 至 20 倍莫耳過量）**沉澱 Lp(a)
- 測上清液殘留的 Lp(a)、OxPL-E06、apoB-100

> 這個實驗產生了本文**最原創的發現**（見後）

---

<!-- _class: divider -->

# 結果

## Results

---

# 族群單純 — 這決定了外推的界線

| 項目 | 數值 |
|------|------|
| LAD / LCx / RCA | 56.7% / 22.4% / 20.9% |
| 參考管徑 | 2.8 ± 0.54 mm |
| MLD 術前／術後／6 個月 | 0.86 / 2.12 / 1.76 mm |
| %DS 術前／術後／6 個月 | 69.1 / 29.2 / 40.8 % |
| AHA/ACC A / B1 / B2 / C | 33.6 / 39.6 / 23.1 / 3.7 % |
| 病灶表面 平滑／不規則／潰瘍 | 85% / 9% / 6% |
| 鈣化／血栓 | 7.2% / 1.5% |

> ⚠️ 這是一群**簡單、平滑、幾乎無血栓與鈣化的 type A/B1 病灶**
> **不能外推到複雜病灶、ACS 或有併發症的 PCI**

---

# ⚠️ 兩種算法，兩種印象（最容易引用錯的地方）

| 指標 | 絕對中位數（術前→術後即刻） | P | 平均百分比變化 | P |
|------|---------------------------|---|--------------|---|
| **OxLDL-E06** | 6177 → 7240 RLU | **0.03** | **+36%** | **< 0.0001** |
| **Lp(a)** | 7.0 → 9.9 mg/dL | **0.27（不顯著）** | **+64%** | **< 0.001** |

> **用絕對中位數看，Lp(a) 的上升 P = 0.27，並不顯著。**
> 是**個人內 paired 百分比變化**才顯著。
>
> 兩者不衝突 — Lp(a) 族群分布極度右偏（range 0–180 mg/dL），
> 少數高值把中位數檢定的檢定力吃掉了。
>
> **引用時必須註明是 paired 個人內變化。**

---

# 對照組：完全沒有變化

| | 攝影前 | 攝影後 |
|---|---|---|
| Lp(a), mg/dL | 16.0 (1.0–108.0) | 16.0 (1.0–93.0) |
| OxLDL-E06, RLU | 6215 (3331–75 883) | 6475 (2870–68 202) |

- 兩組 baseline 各項皆無顯著差異
- **唯一例外**：PCI 組的 **IgG-LDL 免疫複合體較高 (P = 0.007)**

> **這一組是本文因果推論的支柱**：
> 訊號來自**介入**，不是來自導管或顯影劑。

---

# 其他結果

- **OxLDL-E06 與 Lp(a) 強相關**
  所有病人、所有時間點：**Spearman r = 0.68, P < 0.0001**

- **與血管攝影特徵完全無關**
  任何攝影參數都預測不了誰釋出比較多 OxPL
  **氣球擴張 vs 支架置放也沒有差別**

- **臨床事件太少，無法談預後**
  - 2 位亞急性閉塞併 MI（第 4 天）、1 位第 7 天猝死
  - 6 個月：**35 例標的血管再灌流**（33 PCI、2 CABG）因再狹窄
  - 非再狹窄事件者與全世代的標記**無顯著差異**

---

<!-- _class: divider -->

# 核心發現

## OxPL 與 Lp(a) 的「暫時分手，再復合」

---

# 免疫沉澱實驗的結果

LPA4 在每個時間點都沉澱掉 **約 95% 的 Lp(a)**（符合預期）。關鍵在 **E06 訊號**：

```text
術前            E06 表位幾乎全部跟著 Lp(a) 被沉澱   （綁在 Lp(a) 上）

術後「即刻」     只有約 50% 的 E06 跟著 Lp(a) 沉澱   ← 唯一的例外
                另外 50% 依 assay 設計，必然在
                「非 Lp(a) 的 apoB 顆粒」上

6 小時          E06 又幾乎全部回到 Lp(a) 身上

24 小時 ~ 6 個月  維持幾乎全部與 Lp(a) 結合
```

---

# 怎麼解讀

> 術後即刻出現的那一批 OxPL，**不是原本就掛在 Lp(a) 上的**。
>
> 它們是**獨立地被釋放或生成**，暫時掛在其他 apoB 顆粒（如 LDL）上；
> **接著在 6 小時內被轉移到 Lp(a) 身上。**

**推論**

- OxPL 與 Lp(a) 在急性期是**兩個獨立來源**
- 之後才重新結合
- → **Lp(a) 對 OxPL 有優先結合力，扮演「接收槽 (sink)」的角色**

---

<!-- _class: divider -->

# 三個可能機轉

---

# 機轉 1：斑塊被機械性擾動後釋出內容物

- PCI 造成**斑塊壓縮、重分布、破裂**，以及**內膜與中膜剝離**
- 破裂斑塊會留下「**排空的斑塊腔** (emptied plaque cavity)」
- 在不穩定心絞痛病人置放支架，會使**斑塊負荷明顯減少**
  → 支持斑塊物質被**壓出去或栓塞出去**
- **OxPL 與 Lp(a) 兩者都已知會富集在動脈粥樣硬化病灶內**

> **作者認為這是最可能的主要機轉。**

---

# 機轉 2：缺血／再灌流的短暫氧化壓力

Buffon 等人曾觀察到 LAD 氣球阻塞期間，**冠狀竇**出現持續 < 15 分鐘的游離脂質過氧化物上升。

> ⚠️ **但作者自己指出這個對照不完全：**
>
> - Buffon 的脂質過氧化物**只在局部冠狀竇，沒有出現在全身循環**
> - 本研究測到的是**全身血漿**的 OxPL
> - **E06 assay 本身並不偵測脂質過氧化物**

**可能的橋接**：局部產生的脂質過氧化物 → 氧化血管壁或血漿中的磷脂 → 後續才以 OxPL 被 E06 測到

**作者明言：這需要進一步研究。**

---

# 機轉 3：肝臟快速合成或釋出 apo(a)

- **apo(a) 基因帶有 IL-6 反應元件**，可被上調轉錄
  （機轉上類似細胞激素上調 CRP）
- 或是**既存肝臟儲存池的釋放**

**一個值得記住的量級估算**

```text
baseline Lp(a) 最高者，術後絕對上升幅度也最大

平均 Lp(a)  21.7 → 29.8 mg/dL      （↑ 約 8 mg/dL）
假設血漿容積 6 L
→ 做完一次 PCI 的時間內，全身多出 約 500 mg 的 Lp(a)
```

> 作者：**單靠一個斑塊破裂點，不太可能生出 500 mg 的 Lp(a)**
> → 這正是機轉 3（肝臟）必須被納入考慮的理由

---

<!-- _class: divider -->

# Lp(a) 是「垃圾車」還是「兇手」？

---

# 支持「保護性垃圾車」的證據鏈

1. apo(a) 的 **kringle V** 可**共價結合約 2 莫耳的 OxPL**（E06 可偵測）
2. Lp(a) 含**高量 PAF-AH (Lp-PLA2)**，可**移除氧化脂肪酸、破壞 OxPL 的促發炎特性**
3. 本研究顯示 OxPL 一旦釋出，**6 小時內就被 Lp(a) 收走**

> **假說**：Lp(a) 在生理上可能是**保護個體對抗氧化壓力**的角色，
> 是**先天免疫反應**的一員 — 就像 CRP 也會結合 OxLDL 一樣。
>
> 若是如此，**低濃度的 Lp(a) 反而可能是有益的**。

---

# 那它為什麼又致病？

> 當**血漿 Lp(a) 濃度高**時：
>
> - 更多 Lp(a) 顆粒**進入血管壁**
> - Lp(a) **優先結合細胞外基質**被留滯下來
> - 它**身上帶著高含量的 OxPL**
>
> → 變成強力的促發炎來源

**換句話說**

**Lp(a) 的致病性，來自「它是 OxPL 的載體」這個身分，
而不只是它帶的膽固醇。**

- 作者並指出：kringle V 攜帶 OxPL 的那一段，**會誘導巨噬細胞產生 IL-8**

---

<!-- _class: divider -->

# 長期免疫反應

## 一次手術，六個月的免疫尾巴

---

# 時間軸

```text
術後即刻    游離 autoantibody (IgM & IgG) 下降
            ＋ apoB-IC 同步上升
            → 解讀為「急性免疫複合體形成」，抗體被抗原吃掉了
               Cu-OxLDL IgM & MDA-LDL IgM   P < 0.0001
               Cu-OxLDL IgG P = 0.016; MDA-LDL IgG P < 0.0001

6 小時      autoantibody 回到 baseline
24 小時     apoB-IC 回到 baseline

1 個月      IgM autoantibody 達到高峰
1–3 個月    apoB-IC 達到高峰
6 個月      IgM 回到 baseline
            但 IgG 呈現「溫和而持續」的上升

對照組      以上變化全部沒有出現
```

apoB-IC：**IgM P = 0.021**；IgG 僅呈趨勢 **P = 0.099**

---

# 怎麼解讀免疫變化

**即刻下降 ≠ 抗體變少**
抗體與突然湧現的抗原**結合成免疫複合體**（所以 apoB-IC 同時上升）
→ 若釋出的 OxPL 確實促發炎、傷內皮，**被抗體抓走反而可能是好事**

**長期上升 = 記憶反應 (anamnestic response)**
代表這位病人的免疫系統**先前就已被 OxLDL 致敏過**，PCI 只是再暴露
也可能是產生了**全新種類**的 OxLDL 抗體

> ⚠️ **這些長期反應是保護還是有害？作者明說「不清楚」。**
> 旁證：以 OxLDL 或肺炎鏈球菌疫苗免疫動物（兩者都提高 OxLDL 自體抗體）
> 可減少動脈硬化 — 但其中必然還牽涉其他免疫機轉。

---

<!-- _class: divider -->

# 限制與臨床意義

---

# 限制 (Limitations)

**作者自陳**
1. **沒有直接捕捉並分析栓塞碎屑** → 「從哪裡來」始終是推論，不是直接證據
2. **族群過於單純**：只有穩定型心絞痛、選擇性、無併發症、病灶型態簡單
   → **有併發症的 PCI 是否相同，並不清楚**

**讀者應自行補上**

3. **無臨床終點連結** — 事件數太少，**完全無法回答「會不會害到病人」**
4. **2004 年的器械時代** — 69% 只做氣球擴張、31% 裸金屬支架；無 DES、無現代抗血小板策略
5. **RLU 非標準化單位**，跨研究不可比較
6. **統計方法簡單** — 無多變量校正

---

# 實務啟示

> ⚠️ 以下是**機轉層面的思考方向，不是臨床建議**。
> 本文沒有做任何介入試驗，不能據此改變處置。

- **No-reflow 的一個候選解釋**
  OxLDL-E06 與 Lp(a) 都含**血管活性成分**；作者推測 PCI 時釋放這些物質
  **可能造成微血管收縮與 no-reflow** — 但本研究**沒有測量 no-reflow**

- **✅ 最直接可用的一點：抽血時機會影響 Lp(a) 判讀**
  PCI 後即刻抽血測 Lp(a) 可能**高估**
  臨床上要測 Lp(a) 作風險評估，**應避開介入後急性期**（6 小時即回 baseline）

- **OxPL 不只是實驗室名詞** — 它是連結「機械性斑塊擾動」與「發炎」的具體分子

---

# 二十年後的位置

**這篇當年給了什麼**
- **首次在人體證明** PCI 造成血漿 OxPL 與 Lp(a) 急性上升，且**是介入特有的**
- **首次描述** OxPL 與 Lp(a) 的**急性解離、再結合**
- **提出 Lp(a) 作為 OxPL 載體／接收槽**的概念框架

**在時間軸上的位置**

Lp(a) 在 2004 年還是「有趣但沒藥可用」的危險因子；
此後 **Lp(a) 已成為主要的治療標的方向**，相關心血管結果試驗仍在進行／陸續讀出。

> 本篇屬於「**為什麼 Lp(a) 有害**」的機轉基礎工作之一 — 特別是把
> **OxPL 攜帶假說**放進人體資料。
>
> ⚠️ 本講義**不引用任何未經查證的試驗數值**；引用特定藥物結果請回查原文。

---

<!-- _class: divider -->

# Take Home

---

<!-- _class: small-text -->

# Take Home（1／2）

> **Pearl 1**：PCI 後即刻 OxLDL-E06 **↑36%**、Lp(a) **↑64%**（個人內百分比變化，P < 0.001），**6 小時內回到基準**。單純血管攝影的對照組**完全沒有變化**。

> **Pearl 2**：引用時務必分清 — **絕對中位數**的 Lp(a) 變化 **P = 0.27（不顯著）**，是 **paired 百分比變化**才顯著。這是本文最常被引用錯的地方。

> **Pearl 3**：術後即刻只有約 **50%** 的 OxPL 掛在 Lp(a) 上（其餘在其他 apoB 顆粒），**6 小時後幾乎全部回到 Lp(a) 身上** — 急性期獨立生成、之後再結合。

> **Pearl 4**：Lp(a) 可能是 OxPL 的**「接收槽」** — apo(a) kringle V 共價結合約 2 莫耳 OxPL，Lp(a) 富含 PAF-AH 可分解 OxPL。**低量或許是先天免疫的一環；高量時因大量進入血管壁、結合細胞外基質而致病。**

---

<!-- _class: small-text -->

# Take Home（2／2）

> **Pearl 5**：一次 PCI 留下**六個月的免疫足跡** — 即刻免疫複合體形成、IgM 於 1 個月達峰、IgG 於 6 個月仍緩升。**是否有臨床後果，至今未知。**

> **Pearl 6（實務可用）**：**要測 Lp(a) 做風險評估，別在 PCI 後急性期抽。**

> **Pearl 7（判讀紀律）**：本研究族群是**穩定型心絞痛、簡單病灶、無併發症的選擇性 PCI**，且**沒有臨床終點**。
> 它是**機轉研究**，**不能拿來支持任何處置決策**。

---

<!-- _class: ref -->

# 參考文獻

1. Tsimikas S, Lau HK, Han K-R, Shortal B, Miller ER, Segev A, Curtiss LK, Witztum JL, Strauss BH. Percutaneous Coronary Intervention Results in Acute Increases in Oxidized Phospholipids and Lipoprotein(a): Short-Term and Long-Term Immunologic Responses to Oxidized Low-Density Lipoprotein. [*Circulation*. 2004;109(25):3164–3170.](https://doi.org/10.1161/01.CIR.0000130844.01174.55)
2. Palinski W, Rosenfeld ME, Ylä-Herttuala S, et al. Low density lipoprotein undergoes oxidative modification in vivo. [*Proc Natl Acad Sci U S A*. 1989;86:1372–1376.](https://doi.org/10.1073/pnas.86.4.1372)
3. Ylä-Herttuala S, Palinski W, Rosenfeld ME, et al. Evidence for the presence of oxidatively modified low density lipoprotein in atherosclerotic lesions of rabbit and man. [*J Clin Invest*. 1989;84:1086–1095.](https://doi.org/10.1172/JCI114271)
4. Witztum JL, Steinberg D. The oxidative modification hypothesis of atherosclerosis: does it hold for humans? [*Trends Cardiovasc Med*. 2001;11:93–102.](https://doi.org/10.1016/S1050-1738(01)00111-6)
5. Tsimikas S, Shortal BP, Witztum JL, et al. In vivo uptake of radiolabeled MDA2, an oxidation-specific monoclonal antibody... [*Arterioscler Thromb Vasc Biol*. 2000;20:689–697.](https://doi.org/10.1161/01.ATV.20.3.689)
6. Tsimikas S, Palinski W, Witztum JL. Circulating autoantibodies to oxidized LDL correlate with arterial accumulation and depletion of oxidized LDL in LDL receptor–deficient mice. [*Arterioscler Thromb Vasc Biol*. 2001;21:95–100.](https://doi.org/10.1161/01.ATV.21.1.95)
7. Aikawa M, Sugiyama S, Hill CC, et al. Lipid lowering reduces oxidative stress and endothelial cell activation in rabbit atheroma. [*Circulation*. 2002;106:1390–1396.](https://doi.org/10.1161/01.CIR.0000028465.52694.9B)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

> 本內容為讀書會共筆整理，僅供醫療專業人員教學參考，
> 不代表任何單位之官方立場，亦不構成臨床處置建議。
