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
  section.lead h1 { color: #ffffff; font-size: 2.2em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: white;
    border-bottom: none;
    font-size: 2.5em;
    text-align: center;
  }
  section.divider h2 { color: #ffe169; }
  section.divider h3 { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.72em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.88em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.8em;
    font-size: 0.6em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
footer: '謝慕揚 MD, PhD, FESC | VERVE-102 PCSK9 鹼基編輯 | 2026'
---

<!-- _class: lead -->
# VERVE-102
## 體內鹼基編輯 PCSK9 治療高膽固醇血症（Heart-2）
### In Vivo Base Editing of PCSK9 for Hypercholesterolemia
**謝慕揚 MD, PhD, FESC** | 讀書會共筆整理 | 2026-05-29
NEJM 2026（線上 5/25）
[原文連結 (DOI: 10.1056/NEJMoa2601283)](https://doi.org/10.1056/NEJMoa2601283)

---

# 一句話總結

- **VERVE-102**：體內**腺嘌呤鹼基編輯**療法，單次靜脈輸注、GalNAc-LNP 送入肝細胞，**永久關閉 PCSK9**
- phase 1，35 位 **HeFH / 早發 CAD** 成人
- **單次給藥**達劑量依賴降幅：PCSK9 **−88%**、LDL **−62%（絕對 −78 mg/dL）**（1.0 mg/kg）
- 效果**持久**（部分追蹤 18 個月）；**無劑量限制毒性、無死亡**

> 「一次治療、終身有效」降膽固醇的早期人體概念驗證

---

<!-- _class: divider -->
# 背景與機轉

---

# 背景：PCSK9 與「早、久」原則

- PCSK9 **功能喪失變異**者：終身低 LDL、冠心病風險最多低 **88%**，無明顯不良影響
- 孟德爾隨機化：效益取決於 LDL 降幅 **× 累積暴露時間**（越早越久越好）
- 現行每日/定期給藥：**停藥率 30–50%/年** → 真實世界療效落差
- 構想：**單次基因編輯**模擬天然保護變異 → **持久**降 LDL

---

# 作用機轉：A·T → G·C 單鹼基置換

```text
單次 IV → GalNAc-LNP 經 ASGPR(+ApoE/LDLR) 入肝細胞
   → mRNA 轉譯 ABE，與 gRNA 鎖定 PCSK9 intron 1 之 5′ 剪接位
   → adenosine→inosine；nCas9 nickase 切對股 → 修復成 A·T→G·C
   → 剪接位改變 → 讀通至提前終止密碼子 → PCSK9 不表現
   → 血中 PCSK9 ↓ → LDL ↓
```

- **鹼基編輯**：不切斷雙股 DNA（nickase）→ 較傳統 CRISPR 精準
- **GalNAc** 經 ASGPR 增強肝細胞攝取
- 臨床前：高標靶專一性、不傳遞至生殖細胞系

---

# 研究設計與族群

- Heart-2，phase 1，開放性、**單次劑量遞增**；NCT06164730；Verve（Eli Lilly 子公司）
- 澳/加/紐/英；6 劑量 **0.3–1.0 mg 總 RNA/kg**；前驅給藥（地塞米松 + H1/H2）；住院觀察 ≥2 天
- **納入**：18–70 歲、HeFH 或早發 CAD、最大耐受 statin±ezetimibe 下 LDL ≥70

| 基線（35 人） | 數值 |
|------|------|
| 平均年齡 / 男性 | 52 歲 / 69% |
| 白人 | 86% |
| 平均 LDL | 129 mg/dL |
| statin（高強度） | 91%（71%） |

---

# 療效：劑量依賴的深度降幅

| 劑量 (mg/kg) | PCSK9 降幅 | LDL-C 降幅 |
|--------------|-----------|-----------|
| 0.3 | −51% | −9% |
| 0.45 | −59% | −44% |
| 0.6 | −61% | −45% |
| 0.7 | −64% | −33% |
| 0.8 | −77% | −51% |
| **1.0** | **−88%** | **−62%** |

> **1.0 mg/kg**：LDL 128 → 51 mg/dL，**絕對 −78 mg/dL**；降幅與長期 PCSK9 抑制劑相當，但僅需**單次輸注**

---

# 持久性

- 35 人中 **15 人追蹤 ≥1 年**，最長 **18 個月**
- day 28 值 ≈ 整個追蹤期時間加權值 → **穩定、持久**
- 鹼基編輯作用於 **DNA 層級**；成熟肝細胞壽命 200–300 天，降幅在肝細胞更新後仍維持

> **推估**：若 −78 mg/dL 維持 20 年，預計降 ASCVD 風險 **>50%**（外推，非實測）

---

# 安全性（初步可接受）

- **無劑量限制毒性、無死亡、無人退出**；無 > grade 3 事件

| 不良事件 | 人數 (%) |
|----------|----------|
| 任何不良事件 | 26 (74) |
| 輸注相關反應（grade 1–2） | 7 (20) |
| grade 3 吸入性肺炎（**與藥物無關**，GERD/裂孔疝） | 1 (3) |

- **ALT 暫時上升**：3 人 ≥2× ULN（峰 2.4×），第 3–4 天達峰、第 8 天前回降，無症狀
- **GalNAc-LNP 較前代 VERVE-101 安全** → LNP 配方改良是關鍵

---

<!-- _class: divider -->
# 限制與臨床意義

---

# 限制

- phase 1、**非預先設定期中分析**：無檢力評估效應量，**無心血管結果**
- 族群經**篩選（穩定）**、有**前驅給藥**、住院觀察 → 真實世界安全待驗
- 就「永久性」而言追蹤仍短；**off-target**、生殖細胞長期風險待觀察
- **多為白人**（含 off-target 篩選細胞）→ 外推性受限
- 全部納入 **15 年長期追蹤**

---

# Take-home Message

> 「**一次治療、終身有效**」降膽固醇從概念走向早期人體驗證：單次輸注 VERVE-102 達**深度且持久**的 PCSK9/LDL 下降，初步安全性可接受。

- 潛在解決高風險族群（HeFH、早發 CAD）的**順從性/停藥**痛點
- 新一代 GalNAc-LNP 對整個體內鹼基編輯領域有意義（VERVE-201 鎖定 ANGPTL3）
- **但**：phase 1、小型、短期、無硬終點 → 距臨床應用尚遠

---

<!-- _class: small-text -->
# 參考文獻

1. Vafai SB, et al. In Vivo Base Editing of PCSK9 with VERVE-102 for Hypercholesterolemia. [*N Engl J Med*. 2026 (online May 25).](https://doi.org/10.1056/NEJMoa2601283)
2. Musunuru K, et al. In vivo CRISPR base editing of PCSK9 durably lowers cholesterol in primates. [*Nature*. 2021;593:429-434.](https://doi.org/10.1038/s41586-021-03534-y)
3. Cohen JC, et al. Sequence variations in PCSK9, low LDL, and protection against coronary heart disease. [*N Engl J Med*. 2006;354:1264-1272.](https://doi.org/10.1056/NEJMoa054013)
4. Laffin LJ, et al. Phase 1 trial of CRISPR-Cas9 gene editing targeting ANGPTL3. [*N Engl J Med*. 2025;393:2119-2130.](https://doi.org/10.1056/NEJMoa2510029)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC**
讀書會共筆整理 · 僅供醫療專業人員教學參考
