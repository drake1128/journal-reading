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
    justify-content: center;
  }
  section.lead h1 { color: #ffffff; font-size: 2.1em; border-bottom: none; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #ffd166; text-decoration: underline; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.4em; text-align: center; }
  section.divider h2, section.divider h3 { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.74em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.9em;
  }
  /* Disclaimer blockquote on a dark lead slide: force dark text so it stays
     readable on the light box (otherwise inherits section.lead light colour). */
  section.lead blockquote,
  section.lead blockquote p,
  section.lead blockquote strong { color: #2d3436; }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.68em; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.82em; }
  section.ref { font-size: 0.7em; }
footer: '謝慕揚 MD, PhD, FESC | KISS Trial — Bifurcation Side Branch | 2026'
---

<!-- _class: lead -->
# 分叉病變的側枝，要不要額外處理？
## The KISS Randomized Trial
**謝慕揚 MD, PhD, FESC** ｜ 2026-06-14
[JACC Cardiovasc Interv. 2026;19(8):961–972 — DOI: 10.1016/j.jcin.2026.02.012](https://doi.org/10.1016/j.jcin.2026.02.012)

---

# 核心結論 (Bottom Line)

> **非左主幹 (non-LM) 分叉病變**：主枝 (MB) 支架放好、做完 **POT（近端最佳化）**、側枝 (SB) 血流沒有受損 → **不需要常規再處理側枝。**

- **不處理側枝 (no-SBI)** 在術中心梗/心肌損傷上 **不劣於 (noninferior)** 常規處理 (SBI)
- 而且：手術更快、輻射更少、顯影劑更少、側枝撥離更少
- 一年標的病灶失敗 (TLF) **沒有差別**

**口訣：Keep It Simple — 主枝做好、POT 做足，側枝沒事就放手。**

---

# 臨床問題與背景

- **Provisional stenting（臨時性單支架）** 是多數分叉病變的首選策略
- 爭議點：放完主枝支架後，**要不要再對側枝多做一手？**
- 額外側枝介入 (SBI) 的常見做法：
  - **POT–SB–POT**：POT → 側枝氣球擴張 → 再 POT
  - **KBI（對吻氣球擴張）**：主枝＋側枝氣球同時擴張
- 「多做」想改善側枝開口；「少做」想避免側枝撥離、術中損傷、時間/輻射/顯影劑增加
- **KISS 要問**：當代以 POT 為基礎的策略下，「不常規處理側枝」是否**不劣於**「常規處理」

---

# 試驗設計

| 項目 | 內容 |
|------|------|
| **型態** | 多中心、跨國 RCT，**非劣性 (noninferiority) 設計** |
| **族群** | 非左主幹 (non-LM) 分叉病變；**616 人**（no-SBI 303 / SBI 313） |
| **基本資料** | 平均 67.7 歲、約 75% 男性；**81% 慢性冠心病**；多為 **LAD–對角枝** |
| **共同前置** | 主枝植入 **Resolute Onyx DES ＋ POT**，且**側枝血流未受損** |
| **隨機分組（在 MB＋POT 之後）** | ① no-SBI（不處理側枝）② SBI（POT–SB–POT 或 KBI） |
| **主要終點** | 術中心梗 / 心肌損傷（**ARC-2** 定義） |
| **次要終點** | 併發症、12 個月 TLF（心因死亡＋標的血管心梗＋標的病灶再血管化） |

> 隨機分組在「主枝支架＋POT 做好、側枝血流良好」**之後** → 問的是「**還要不要再多做側枝**」。

---

# 主要結果：術中心梗 / 心肌損傷

| 組別 | 事件率 | n |
|------|--------|---|
| **no-SBI（不處理側枝）** | **4.1%** | 11 |
| **SBI（處理側枝）** | **5.7%** | 16 |
| **統計** | **P < 0.001（非劣性達標）**｜P = 0.38（優越性未達標） | — |

- 年齡、性別、Medina 分類、側枝殘餘狹窄之間 **無顯著交互作用** → 結論一致
- no-SBI 組中，最終仍需 bailout 處理側枝的只有 **2.0%（n = 6）**

---

# 次要結果：手術負擔更輕、併發症更少

| 指標 | no-SBI | SBI | 方向 |
|------|--------|-----|------|
| 手術時間 | 較短 | 較長 | **no-SBI 較佳** |
| 輻射劑量 | 較低 | 較高 | **no-SBI 較佳** |
| 顯影劑用量 | 較少 | 較多 | **no-SBI 較佳** |
| **側枝撥離 (SB dissection)** | **0.0%** | **2.9%** | **no-SBI 較佳；P = 0.004** |

| 1 年結果 | no-SBI | SBI | 統計 |
|----------|--------|-----|------|
| **TLF** | 4.9%（15） | 6.4%（20） | **P = 0.442（無差異）** |

> **整體：少做側枝 → 術中不劣、併發症更少、手術更省、一年硬指標不吃虧（"less is more"）。**

---

# 一個重要觀察：KBI 反而比較傷？

在 **SBI 組內**比較兩種側枝處理方式：

| 側枝處理方式 | 術中心梗 / 心肌損傷 |
|--------------|---------------------|
| 只做側枝氣球擴張 (SB ballooning only) | **~3.4%** |
| **KBI（對吻氣球）** | **~8.9%** |

> ⚠️ **保守解讀**：這是 SBI 組內的**非隨機**次族群比較（hypothesis-generating），不能當隨機證據。但方向與臨床直覺一致 —— **若真的要處理側枝，單純側枝擴張可能比 KBI 溫和。**

---

<!-- _class: divider -->
# 臨床意義 — Take Home

---

# 本案 5 大臨床 Pearls

> **Pearl 1**：非左主幹分叉、主枝＋POT 做好、側枝血流良好 → **不必常規處理側枝**。

> **Pearl 2**：no-SBI 不只「不劣」，還更省、併發症更少、一年 TLF 不吃虧。

> **Pearl 3**：no-SBI ≠ 不看側枝 —— 仍允許 **2.0% bailout**；策略是「沒明顯受損就不動，真有問題才出手」。

> **Pearl 4**：要處理側枝時，**KBI 可能比單純側枝擴張帶來更多術中損傷**（觀察性）。

> **Pearl 5**：強化當代指引對 **provisional / 單支架策略** 的偏好；重點從「側枝影像美觀」回到「**病人術中安全與長期結果**」。

---

# 限制與注意事項

- **僅限非左主幹、相對單純分叉** —— 不適用左主幹或計畫性雙支架的複雜病灶
- 主要終點為**術中心梗/心肌損傷（替代指標）**，非硬性臨床事件；追蹤僅 12 個月
- 隨機分組前提是**側枝血流未受損** —— 若分組前側枝已明顯受損（TIMI 下降、嚴重夾層），結論不直接適用，臨床仍應出手
- KBI vs 單純側枝擴張為**組內非隨機**比較，僅供參考
- 單一支架平台（Resolute Onyx），外推到所有 DES 仍需審慎

---

<!-- _class: small-text -->
# 縮寫對照

| 縮寫 | 全名 (English) | 中文 |
|------|----------------|------|
| SB / MB | Side Branch / Main Branch | 側枝 / 主枝 |
| SBI | Side Branch Intervention | 側枝介入 |
| POT | Proximal Optimization Technique | 近端最佳化技術 |
| KBI | Kissing Balloon Inflation | 對吻氣球擴張 |
| DES | Drug-Eluting Stent | 藥物釋放支架 |
| MI | Myocardial Infarction | 心肌梗塞 |
| ARC-2 | Academic Research Consortium 2 | 學術研究聯盟第 2 版（事件定義） |
| TLF | Target Lesion Failure | 標的病灶失敗 |
| LM / LAD | Left Main / Left Anterior Descending | 左主幹 / 左前降支 |
| CCD | Chronic Coronary Disease | 慢性冠心病 |

---

<!-- _class: ref -->
# 參考文獻

1. Chevalier B, Cornillet L, Bouisset F, et al; KISS Trial Group. Side Branch Additional Treatment for Coronary Bifurcation Lesion Revascularization: Insights From the KISS Randomized Trial. [*JACC Cardiovasc Interv*. 2026;19(8):961–972.](https://doi.org/10.1016/j.jcin.2026.02.012) ｜ PMID [42055657](https://pubmed.ncbi.nlm.nih.gov/42055657/)
2. Keep bIfurcation Single Stenting Simple (KISS). [ClinicalTrials.gov NCT04285372.](https://clinicaltrials.gov/study/NCT04285372)
3. PCR Journal Club (Reviewed by Aaysha Cader). [Side branch additional treatment for coronary bifurcation lesion revascularisation: insights from the KISS randomised trial. PCRonline.](https://www.pcronline.com/PCR-Publications/PCR-Journal-Club/2026/Side-branch-treatment-in-bifurcation-lesions-KISS-trial)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

本案重點：非左主幹分叉，主枝＋POT 做好、側枝沒事就放手（Keep It Simple）

> 本投影片為讀書會共筆之教學整理，僅供醫療專業人員教學參考；臨床決策請以原始文獻及醫師個人判斷為依據。
