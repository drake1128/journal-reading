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
  section.divider h2 { color: #ffffff; font-size: 1.4em; text-align: center; font-weight: bold; }
  section.divider h3 { color: #ffe082; font-size: 1.1em; text-align: center; font-weight: normal; }
  section.divider p, section.divider strong { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  a { color: #0072bc; }
  table { font-size: 0.70em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 5px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.88em;
  }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.66em; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.78em; }
footer: '謝慕揚 MD, PhD, FESC | EASE 感染性心內膜炎早期手術 | 2012'
---

<!-- _class: lead -->
# 感染性心內膜炎的早期手術
## EASE — Early Surgery versus Conventional Treatment for Infective Endocarditis
### N Engl J Med 2012;366:2466-73 · 經典重讀

**謝慕揚 MD, PhD, FESC**

[原文連結：doi.org/10.1056/NEJMoa1112843](https://doi.org/10.1056/NEJMoa1112843)

> 至今**唯一**針對「以預防栓塞為目的之早期手術」的隨機試驗

---

# 一句話總結

**左側 IE + 嚴重瓣膜疾病 + vegetation > 10 mm**，隨機分派後 **48 小時內開刀**：

| 6 週複合終點（住院死亡或栓塞） | 早期手術 | 傳統治療 |
|---|---|---|
| | **1 (3%)** | **9 (23%)** |

**HR 0.10（95% CI 0.01–0.82），P = 0.03**

好處**完全來自減少栓塞：21% → 0%**

> **死亡率沒有差別**：6 個月 3% vs 5%，HR 0.51（0.05–5.66），P = 0.59

---

# 臨床背景：手術時機吵了幾十年

- 全身性栓塞見於約 **1/3** 的 IE 病人，其中高達 **65%** 侵犯中樞神經
- 栓塞是 IE **僅次於心衰竭的第二大死因**
- **栓塞風險在診斷後第一週最高** → 這是「早期手術」的理論基礎

| 當年的指引 | 對 vegetation 相關手術的建議 |
|------|------|
| 2006 ACC–AHA | **Class IIa**：僅限反覆栓塞 + 持續存在的 vegetation |
| 2009 ESC | **Class IIb**：僅限孤立性、非常大的 vegetation（> 15 mm） |

> 過去所有比較都是**觀察性研究** — 受基線差異、治療選擇偏差、存活者偏差影響。

---

<!-- _class: divider -->
# 試驗設計
## 南韓兩家中心 · 76 人 · 開放標籤隨機

---

# 試驗設計

| 項目 | 內容 |
|------|------|
| 設計 | 前瞻性、隨機、開放標籤 |
| 地點 | 南韓 Asan Medical Center（71 人）+ 首爾大學醫院（5 人） |
| 期間 | 2006/09 – 2011/03 |
| 分派 | 1:1；早期手術 37 / 傳統治療 39 |
| **早期手術定義** | **隨機分派後 48 小時內**瓣膜手術 |
| 傳統治療 | 依 AHA 指引；出現緊急適應症或抗生素後症狀持續才手術 |
| 主要終點 | **6 週內住院死亡或臨床栓塞事件** |
| 樣本數 | 74 人（80% power；假設 23% vs 3%） |
| 追蹤 | 中位數 **749 天**，**100% 完成追蹤** |

---

# 栓塞事件的定義（相當嚴格）

必須**同時**符合：

```text
1. 急性出現栓塞的臨床症狀或徵象
   ＋
2. 後續影像確認新的病灶

腦栓塞：由神經科醫師依腦部 MRI 確認
皮膚表現、轉移性膿瘍 → 不算栓塞事件
```

> **重要**：研究者**沒有系統性做追蹤影像去找無症狀栓塞**。
> 所以本試驗測的是「**臨床上有意義的栓塞**」，不是所有栓塞。

---

# 收案與排除 — 全篇最關鍵的一段

**納入**：左側 IE ＋ **嚴重瓣膜疾病** ＋ **vegetation > 10 mm**

**排除**（依 2006 ACC–AHA 手術適應症訂定）：

| 排除項目 | 為什麼 |
|------|------|
| 中重度心衰竭、心臟傳導阻斷、膿瘍、黴菌性 IE | 這些本來就有 **class I** 適應症 |
| **年齡 > 80 歲**、嚴重共病（如癌症） | 高手術風險族群 |
| **大範圍栓塞性中風且有出血轉化風險** | **最重要的一條** |
| **人工瓣膜 IE、右側 vegetation、vegetation ≤ 10 mm** | 完全不適用 |
| 外院轉入且距診斷 > 7 天 | 已度過高風險期 |

---

# 篩選漏斗

```text
134 位確診 IE
   ├─ 26 人需緊急手術（已有 class I 適應症）→ 排除
   └─ 18 人無大 vegetation 或無嚴重瓣膜疾病 → 排除
        ↓
   90 人評估合格性
   └─ 14 人排除（5 大中風、5 醫療狀況差、4 拒絕）
        ↓
   76 人隨機分派 → 早期手術 37 / 傳統治療 39
```

> **134 人裡只有 76 人（57%）進入試驗。**
> EASE 的結論只適用於這個**被高度篩選過的中間地帶**。

---

# 病人族群

| 特徵 | 傳統治療 (n=39) | 早期手術 (n=37) |
|------|-----------------|-----------------|
| 年齡 | 47.8 ± 17.5 歲 | 45.5 ± 14.9 歲 |
| **EuroSCORE** | **6.7 ± 1.7** | **6.4 ± 1.6** |
| 入院時已有栓塞 | 44%（腦部 28%） | 51%（腦部 30%） |
| LVEF | 60.7% | 61.7% |
| 二尖瓣 / 主動脈瓣 | 59% / 28% | 59% / 30% |
| **Vegetation 直徑** | **14.1 ± 3.5 mm** | **13.5 ± 3.2 mm** |
| ‧ > 15 mm | 33% | 30% |
| 嚴重逆流 | 92% | 97% |

> **年輕（平均 46 歲）、低手術風險、LVEF 正常** — 這不是台灣典型的 IE 病人。

---

# 致病菌 — 外推性的關鍵

| 微生物 | 傳統治療 | 早期手術 |
|--------|----------|----------|
| Viridans streptococci | 33% | 27% |
| 其他 streptococci | 31% | 30% |
| **Staphylococcus aureus** | **13%** | **8%** |
| Enterococcus | 3% | 5% |
| 培養陰性 | 18% | 27% |

> 全體只有約 **11% 是 *S. aureus***，遠低於歐美當代的 25–35%。
> **EASE 是一個以 streptococcal IE 為主的族群** — 手術風險低、預後好。

---

# 抗生素治療：兩組完全一樣

| 項目 | 傳統治療 | 早期手術 | P |
|------|----------|----------|---|
| 退燒天數中位數 | 2 天 | 2 天 | 0.21 |
| 菌血症持續 | 1 (3%) | 0 | 1.00 |
| Beta-lactam 為基礎 | 100% | 100% | — |
| 療程中位數 | 35 天 | 35 天 | 0.93 |

> **這張表很重要**：結果的差異**純粹來自手術時機**，不是抗生素效果不同。

---

# 手術實況

**早期手術組（37 人，100% 在 48 小時內完成）**
分派→手術中位時間 **24 小時**（IQR 7–45）；二尖瓣 22 人（修補 8 / 置換 14）；主動脈或雙瓣 15 人

**傳統治療組（39 人）**

| 結局 | 人數 |
|------|------|
| **最終仍接受手術** | **30 人 (77%)** |
| ‧ 住院中出現緊急適應症 | 8 人 (21%)，中位 6.5 天 |
| ‧ 擇期手術（> 2 週後） | 22 人 |
| **從未手術、內科治療出院** | **11 人 (28%)** |

> **EASE 真正比較的不是「開刀 vs 不開刀」，而是「現在開 vs 之後開」。**

---

<!-- _class: divider -->
# 結果
## 栓塞 21% → 0%，死亡率沒有差別

---

# 主要終點（6 週）

| 終點 | 傳統治療 (n=39) | 早期手術 (n=37) | P |
|------|-----------------|-----------------|---|
| **住院死亡或栓塞事件** | **9 (23%)** | **1 (3%)** | **0.01** |
| ‧ 住院死亡 | 1 (3%) | 1 (3%) | 1.00 |
| ‧ **栓塞事件** | **8 (21%)** | **0** | **0.005** |
| — 腦部 / 冠狀動脈 | 5 (13%) / 1 (3%) | 0 / 0 | — |
| — 膕動脈 / 脾臟 | 1 (3%) / 1 (3%) | 0 / 0 | — |

**HR 0.10（95% CI 0.01–0.82），P = 0.03**

> 傳統治療組**所有事件都發生在瓣膜手術之前**；兩組均無 30 天手術死亡。

---

# 6 個月次要終點與長期追蹤

| 終點 | 傳統治療 | 早期手術 | P |
|------|----------|----------|---|
| **複合終點**（死亡／栓塞／復發／心衰竭再住院） | **11 (28%)** | **1 (3%)** | **0.003** |
| 死亡 | 2 (5%) | 1 (3%) | 1.00 |
| 栓塞事件 | 8 (21%) | 0 | 0.005 |
| IE 復發 | 1 (3%) | 0 | 1.00 |

複合終點 **HR 0.08（0.01–0.65），P = 0.02**；log-rank P = 0.009
**6 個月全因死亡 HR 0.51（0.05–5.66），P = 0.59 → 無差異**

追蹤 749 天：兩組均**無栓塞事件、無因心衰竭住院**

---

# 怎麼正確解讀這個 HR 0.10

**✅ EASE 證明了什麼**
在經高度篩選的族群，48 小時內開刀能**幾乎消除早期全身性栓塞**（21% → 0%），且**不增加手術死亡或 IE 復發**

**❌ 常見誤讀**

| 誤讀 | 事實 |
|------|------|
| 早期手術能降低死亡率 | 6 個月 3% vs 5%，HR 0.51（0.05–5.66）— **沒有訊號** |
| 所有 IE 都該早開刀 | 排除 PVE、右側、黴菌、大中風、> 80 歲、嚴重共病 |
| vegetation > 10 mm 就是適應症 | 必須 **＋ 嚴重瓣膜疾病** |
| 這是內科 vs 外科的對決 | 傳統治療組 **77% 最後也開刀了** |

---

# 統計面要留意的地方

- **樣本極小**（76 人），事件數更小（**9 vs 1**）
- 主要終點 95% CI **0.01–0.82** — **上界非常靠近 1**，精確度低
- 開放標籤；栓塞雖有影像確認，仍存在偵測偏差可能
- 由**兩家高手術量的韓國醫學中心**執行，其中一家貢獻 **93%** 的病人
- 依中心分層隨機但**未做分中心分析**（收案數差距太大）

---

# 限制

1. 樣本數極小（n=76），僅 10 個主要終點事件
2. 單一國家、兩家高手術量中心（一家佔 93%）→ **低手術量醫院不適用**
3. 族群窄：無 PVE、無右側 IE、無黴菌、無大中風、≤ 80 歲、**EuroSCORE ≈ 6.5**
4. **致病菌以 streptococci 為主，*S. aureus* 僅 11%**
5. 未系統性偵測無症狀栓塞
6. 開放標籤設計
7. 早期手術組二尖瓣 **14/22 採置換**；長期人工瓣膜相關風險在 2 年追蹤內尚未浮現

---

# 從 EASE 到 2023 ESC 指引

**2023 ESC 心內膜炎指引的框架**：

- **心衰竭、無法控制的感染（膿瘍／假性動脈瘤／瘻管）、高危險菌種** → 緊急／急迫手術，**Class I**
- **預防栓塞**：左側原生瓣膜 IE、vegetation ≥ 10 mm **且在適當抗生素治療下仍發生栓塞** → 建議手術
- **孤立的大 vegetation（≥ 10 mm）＋ 嚴重瓣膜疾病 ＋ 手術風險低** → **可考慮手術**（← 這條就是 EASE 的直接產物）

> **始終停留在「可考慮 (may be considered)」的層級** —
> 這正確反映了 n = 76、只有 10 個事件的證據強度。

---

<!-- _class: divider -->
# 臨床應用
## 誰是 EASE 的族群？

---

# 決策路徑

```text
確診左側原生瓣膜 IE
        ↓
有 class I 適應症嗎？（心衰竭、膿瘍/瘻管、感染無法控制、高危險菌種）
        ↓ 有 → 緊急／急迫手術（不需要 EASE 佐證）
        ↓ 沒有
Vegetation > 10 mm ？ → 是
        ↓
合併嚴重瓣膜疾病（多為嚴重逆流）？ → 是
        ↓
有大範圍栓塞性中風／出血轉化風險？
        ↓ 有 → 暫緩，先做腦部影像 + 神經科討論時機
        ↓ 沒有
手術風險可接受（低 EuroSCORE、非高齡）？ → 是
        ↓
→ EASE 族群：考慮 48 小時內手術以預防栓塞
```

---

# 四個實務提醒

1. **一定要先做腦部影像**：EASE 排除了大中風合併出血轉化風險的病人 — **先掃再決定**

2. **心臟團隊 (Endocarditis Team)**：手術時機應由心內、心外、感染科共同決定

3. ***S. aureus* IE 不能直接套用 EASE**：栓塞與死亡風險更高，手術風險也更高，需個案討論

4. **修補優於置換**：早期手術反而是修補機會最高的時候（瓣膜破壞尚輕）——EASE 只有 8/22 做修補，當代實務更重視這點

---

# Clinical Pearls

> **Pearl 1**：**EASE 減少的是栓塞，不是死亡**。21% → 0% 是真的；死亡率 HR 0.51 的 CI 從 0.05 到 5.66，什麼都沒說。

> **Pearl 2**：**傳統治療組 77% 最後還是開刀了**。真正的問題是「現在開，還是等出事再開」。

> **Pearl 3**：栓塞風險在**診斷後第一週最高** — 「先打兩週抗生素再說」在高風險族群不安全。

> **Pearl 4**：*S. aureus* 僅 11%、EuroSCORE ≈ 6.5、兩家高手術量中心 — **套用到你的病人前，先看這三個數字。**

---

<!-- _class: small-text -->
# 參考文獻

1. Kang DH, Kim YJ, Kim SH, et al. Early Surgery versus Conventional Treatment for Infective Endocarditis (EASE). [*N Engl J Med*. 2012;366:2466-2473.](https://doi.org/10.1056/NEJMoa1112843)
2. Delgado V, Ajmone Marsan N, de Waha S, et al. 2023 ESC Guidelines for the management of endocarditis. [*Eur Heart J*. 2023;44:3948-4042.](https://doi.org/10.1093/eurheartj/ehad193)
3. Otto CM, Nishimura RA, Bonow RO, et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. [*Circulation*. 2021;143:e72-e227.](https://doi.org/10.1161/CIR.0000000000000923)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

[EASE — N Engl J Med 2012;366:2466-73](https://doi.org/10.1056/NEJMoa1112843)
