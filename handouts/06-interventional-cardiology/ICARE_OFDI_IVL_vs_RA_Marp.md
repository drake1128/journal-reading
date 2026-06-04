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
  section.lead h3 { color: #dfe6e9; font-weight: normal; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.divider {
    background-color: #0072bc; color: white;
    display: flex; justify-content: center; align-items: center;
  }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.5em; text-align: center; }
  section.divider h2 { color: #ffe169; text-align: center; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.66em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b; background-color: #fff5f5;
    padding: 0.5em 1em; font-size: 0.85em;
  }
  pre {
    background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1;
    border-radius: 8px; padding: 0.8em; font-size: 0.66em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.72em; }
  .qr { position: absolute; top: 30px; right: 30px; width: 110px; height: 110px; }
footer: '謝慕揚 MD, PhD, FESC | ICARE OFDI：IVL vs Rotational Atherectomy | 2026'
---

<!-- _class: lead -->
# ICARE OFDI 隨機試驗
## 鈣化冠狀動脈病灶：IVL 對比旋磨術 (RA)
### Intravascular Lithotripsy vs Rotational Atherectomy for Calcified Lesions
**讀書會共筆整理｜謝慕揚 MD, PhD, FESC**
新竹臺大分院 心血管中心 · 2026-06-03
[原文連結：EuroIntervention 2026 (DOI: 10.4244/EIJ-D-26-00426)](https://doi.org/10.4244/EIJ-D-26-00426)

---

# 一句話總結 (Bottom Line)

在中至重度**穩定型鈣化病灶**、以 **OFDI 影像導引**的 PCI：

- 主要終點**最小支架面積 (MSA)**：**IVL 6.0 vs RA 5.9 mm²**，**p for non-inferiority < 0.05** → **IVL 非劣於 RA**
- 幾何性支架擴張達標率**完全相同**（各 65.1%）
- **重大支架貼合不良**：RA 80.2% vs IVL **57.8%**（p=0.002）→ **IVL 較佳**
- 12 個月 **TLF**：RA 1.2% vs IVL 2.4%（p=0.61，等效）

> **能用 IVL 就用 IVL**（簡單、貼合好、結果不輸）；**過不去靠 RA** 開路。

---

# 背景：鈣化病灶為何棘手

- 冠狀動脈鈣化 (CAC) → 器械難到位、球囊/支架**擴張不全 (under-expansion)**
- **支架擴張不全**是 **ISR** 與 **支架血栓 (ST)** 最強的可改變危險因子
- 充分的**斑塊準備 (lesion preparation)** 是把鈣化「打開」的關鍵

> 鈣化病灶成敗 9 成決定在「**下支架之前**」的斑塊準備，而非支架本身。

---

# 兩種策略：RA vs IVL（機轉互補）

| 面向 | 旋磨術 RA (Rotablator) | 震波碎石 IVL (Shockwave C2) |
|------|------------------------|-----------------------------|
| 機轉 | **消磨**表淺鈣化 (ablation) | **聲波震波**裂解鈣化 |
| 對深層鈣化 | 作用有限 | **可裂解深層鈣化** |
| 學習曲線 | 較陡 | 較平緩（近似球囊） |
| 無法通過病灶 | **可先開路** | 需器械先能通過 |

> RA「由表面往內磨」、IVL「由內往外震裂」——ICARE 比較兩者在 **MSA** 上的高下。

---

<!-- _class: divider -->
# Part 1
## 研究設計 Study Design

---

# 研究設計與 PICO

- **多中心、前瞻、隨機、非劣性**試驗（法國 16 中心），全程 **OFDI 導引**

| 元素 | 內容 |
|------|------|
| **P** | 中至重度鈣化、**穩定型**病灶，計畫 PCI |
| **I** | **IVL**（Shockwave C2）為基礎斑塊準備 |
| **C** | **RA**（Rotablator）為基礎斑塊準備 |
| **O** | 支架置入後**最小支架面積 MSA**（OFDI） |

- 臨床終點：12 個月**標靶病灶失敗 (TLF)**

---

# 非劣性怎麼讀（關鍵數字）

```text
Non-inferiority margin = 0.75 mm²
  ├─ 依既往腔內影像研究預設
  ├─ 樣本數假設：SD 1.9 mm²、單側 α 5%、power 80%
  └─ 前提：假設兩組「無真實差異」

判定：IVL 的 MSA（含 CI）若未比 RA 差超過 0.75 mm² → 非劣
```

> **非劣性 ≠ 較優**：只是「沒有差到有臨床意義」。

---

# 病人族群 (N = 169)

- **RA n=86 · IVL n=83**；男性 **81.1%**；年齡 **71.8 ± 8.2 歲**
- 兩組基線平衡
- **鈣化結節 (calcified nodule) 高達 48%** —— 公認最難處理的鈣化亞型

> 近半數是鈣化結節 → 這是**高難度真實世界**族群，而非挑過的乾淨環狀鈣化。

---

<!-- _class: divider -->
# Part 2
## 結果 Results

---

# 主要結果：MSA 非劣性

<img class="qr" src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https%3A%2F%2Fdoi.org%2F10.4244%2FEIJ-D-26-00426" alt="DOI QR">

| 主要終點 | RA (n=86) | IVL (n=83) | 結果 |
|----------|-----------|------------|------|
| **MSA (mm²)** | **5.9 ± 2.2** | **6.0 ± 2.3** | **p(NI) < 0.05** → IVL **非劣** |

- 兩組 MSA 幾乎重疊（差距僅 0.1 mm²），遠在 0.75 mm² 界值內。

> 在與長期預後最相關的影像指標上，**IVL 與 RA 打成平手**。

---

# 次要結果：擴張、貼合與安全

| 次要終點 | RA | IVL | p | 解讀 |
|----------|----|----|---|------|
| 達標支架擴張 (expansion) | 65.1% | 65.1% | 0.994 | **完全相同** |
| **重大支柱貼合不良 (malapposition)** | **80.2%** | **57.8%** | **0.002** | **IVL 較少** |
| 周邊手術併發症 | — | — | NS | 無差異 |
| 12 個月 **TLF** | 1.2% | 2.4% | 0.61 | **等效** |

> **expansion**（張得夠不夠大）兩者相同；**apposition**（貼不貼壁）IVL 較佳。

---

# 機轉解讀：為何 RA 貼合較差？

- **RA** 僅磨**表淺**鈣化 → **深層鈣化環**仍頂住支架 → 較多 **malapposition**
- **IVL** 震波裂解**深層+表淺**鈣化 → 血管壁順應性改善 → 支架更易均勻貼壁
- 48% 鈣化結節族群中，IVL「由內往外」對結節基底可能更有利貼合

> expansion 相同、apposition IVL 較佳 → 兩者「撐開」能力一樣，IVL「貼好」略勝。
> （屬機轉討論，非試驗證明）

---

<!-- _class: divider -->
# Part 3
## 臨床意涵 Clinical Implications

---

# 怎麼選 IVL 或 RA

| 情境 | 傾向 | 理由 |
|------|------|------|
| 器械**可通過**、深層鈣化為主 | **IVL** | 處理深層鈣化、貼合佳、易上手 |
| 器械**無法通過 / 極緊**病灶 | **RA** | IVL 球囊需先送到病灶 |
| 操作者經驗有限 | **IVL** | 操作近似球囊 |
| 需修整表淺鈣化 | **RA** 或 **RA→IVL** | 互補機轉 |

> 務實結論：**能過用 IVL、過不去靠 RA**；**RA→IVL 混合**也是合理選項。

---

# 研究限制 (Limitations)

- **影像替代終點**：MSA 為 surrogate，非硬臨床終點
- **小樣本、事件極少**：對臨床終點**檢力不足**，「等效」需謹慎
- **僅穩定型病灶**：不含 ACS / 極端未擴張病灶 → 外推小心
- **OFDI = Terumo 平台、Terumo Europe 資助**：留意潛在偏倚（已揭露）
- 開放標籤、**操作者依賴**；malapposition 優勢屬**探索性**次要終點

---

# Take-home Pearls

> **1.** 鈣化 PCI 成敗在**斑塊準備**；MSA 是與預後最相關的影像指標。

> **2.** ICARE：OFDI 導引下 **IVL 的 MSA 不劣於 RA**（6.0 vs 5.9 mm²），安全性與 12 個月 TLF 相當。

> **3.** 擴張相同，但 **IVL 支架貼合明顯較佳**（malapposition 57.8% vs 80.2%）。

> **4.** 選擇邏輯：**能過用 IVL、過不去靠 RA**，可考慮 **RA→IVL** 混合。

> **5.** 限制：影像替代終點、小樣本、僅穩定病灶、廠商資助。

---

<!-- _class: small-text -->
# 參考文獻 References

1. Honton B, Motreff P, Mallet JS, et al. Intravascular lithotripsy in comparison to rotational atherectomy for calcified lesions: the **ICARE OFDI** randomised trial. *EuroIntervention*. 2026 May 19. [DOI 10.4244/EIJ-D-26-00426](https://doi.org/10.4244/EIJ-D-26-00426) · [PubMed 42200665](https://pubmed.ncbi.nlm.nih.gov/42200665/) · [NCT05394649](https://clinicaltrials.gov/study/NCT05394649)
2. Hill JM, et al. IVL for severely calcified coronary disease (**Disrupt CAD III**). *J Am Coll Cardiol*. 2020;76(22):2635-2646. [PubMed 33069849](https://pubmed.ncbi.nlm.nih.gov/33069849/)
3. Généreux P, et al. Ischemic outcomes after PCI of calcified vessels. *J Am Coll Cardiol*. 2014;63(18):1845-1854. [PubMed 24561145](https://pubmed.ncbi.nlm.nih.gov/24561145/)
4. Riley RF, et al. SCAI position statement on PCI of calcified lesions. *Catheter Cardiovasc Interv*. 2020;96(2):346-362. [PubMed 32406991](https://pubmed.ncbi.nlm.nih.gov/32406991/)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**讀書會共筆整理｜謝慕揚 MD, PhD, FESC**
*本投影片由 Claude Code 協助整理，內容已核對原文；臨床判斷以原始文獻為準*
