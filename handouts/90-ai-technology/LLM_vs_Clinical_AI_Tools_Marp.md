---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: 'Microsoft JhengHei', 'PingFang TC', sans-serif; background-color: #ffffff; color: #2d3436; }
  section.lead { background-color: #1a2740; color: #ffffff; justify-content: center; }
  section.lead h1 { color: #ffffff; font-size: 1.9em; border-bottom: none; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #ffd166; text-decoration: underline; }
  section.divider { background-color: #0072bc; color: white; display: flex; justify-content: center; align-items: center; }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.2em; text-align: center; }
  section.divider h2, section.divider h3 { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.72em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote { border-left: 4px solid #ba181b; background-color: #fff5f5; padding: 0.5em 1em; font-size: 0.88em; }
  section.lead blockquote, section.lead blockquote p, section.lead blockquote strong { color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.82em; }
  section.ref { font-size: 0.74em; }
footer: '謝慕揚 MD, PhD, FESC | 通用 LLM vs 專用臨床 AI | 2026'
---

<!-- _class: lead -->
# 通用 LLM 勝過專用臨床 AI 工具？
## Nature Medicine 2026 盲化評比
**謝慕揚 MD, PhD, FESC** ｜ 2026-06-14
[Vishwanath K, et al. Nat Med 2026 — DOI: 10.1038/s41591-026-04431-5](https://doi.org/10.1038/s41591-026-04431-5)

---

# 核心結論 (Bottom Line)

> 「**專為醫療打造**」的臨床 AI 工具(OpenEvidence、UpToDate Expert AI)正進臨床,卻幾乎沒有獨立評估。這篇把它們跟三個**通用前沿 LLM** 放上同一天平 ——

- **通用 LLM(GPT-5.2 / Gemini 3.1 Pro / Claude Opus 4.6)三項全勝**
- 在真實臨床問題上,**專用臨床 AI ≈ Google 搜尋 AI Overview**

**→「專為醫療打造」≠「比較好」;進臨床前必須獨立、真實、盲化驗證。**

---

# 臨床問題：專用醫療 AI 真的比較好嗎？

- 一堆「**臨床專用**」AI 產品快速進醫療現場,但**大多缺乏獨立第三方評估**
- 行銷常暗示「醫療專用 = 更安全更準」 —— **這假設從沒被嚴格檢驗**
- 我們其實不知道:它們是否真的優於「直接用通用 LLM」或「Google 一下」？
- 本研究量化回答:**專用臨床 AI vs 通用前沿 LLM,誰強？**

---

# 研究設計：誰 vs 誰、怎麼比

| 項目 | 內容 |
|------|------|
| **專用臨床 AI** | **OpenEvidence**、**UpToDate Expert AI** |
| **通用前沿 LLM** | **GPT-5.2**、**Gemini 3.1 Pro**、**Claude Opus 4.6** |
| **階段 1** | **500 題 MedQA**（醫學知識） |
| **階段 2** | **500 題 HealthBench**（與臨床醫師一致性） |
| **階段 3** | **RCQ**：100 題**真實臨床環境**醫師提問（去識別化） |
| **RCQ 評分** | **12 位美國醫師**隨機、**盲化**評分,**1,800 筆**標註 |

> RCQ 不是考古題,而是**真實臨床問題 + 盲化醫師評分** —— 更貼近實務、更難猜題。

---

# 結果：通用 LLM 三項全勝

- **MedQA、HealthBench、RCQ —— 通用前沿 LLM 全部勝過專用臨床 AI 工具。**
- 在最貼近實務的 **RCQ** 上,**專用臨床 AI ≈ 自動啟用的 Google 搜尋 AI Overview**。
- 作者結論:**AI 工具進臨床前,需要獨立、真實世界的評估。**

> 「醫療專用 AI」底層也是 LLM;**包裝成醫療產品 ≠ 贏過直接用最新通用模型** —— 在這份盲化評比裡反而是輸的。

---

<!-- _class: divider -->
# 教學啟示
## 該怎麼選/評 AI 工具？

---

# Specialized ≠ Better

- **領域專用包裝 ≠ 臨床表現更好** → 看**獨立數據**,不看行銷
- **獨立、盲化、真實世界評估是底線**（真實臨床問題 + 盲化醫師評分）
- **導入前三問**:
  1. 有沒有**第三方獨立評估**？
  2. 比較對象是不是**當代最新通用模型**(而非舊基準)？
  3. 題目是**真實臨床問題**還是考古題？
- **快速折舊**:通用模型迭代極快;專用工具跟不上,優勢會被吃掉
- 臨床現場:**「直接問最新通用 LLM」常常就是個強 baseline**

---

# 限制與該保留的地方

- **某時間點快照**:模型版本都會更新,排名可能隨版本變動
- **RCQ 來自單一 live 臨床環境**的醫師提問 → 機構/科別偏向,外推需謹慎
- 評的是**答案品質/一致性,不是病人結果 (patient outcomes)**
- 專用工具的價值可能不只「答對」(來源可追溯、引用、工作流整合、法規責任) —— 未必完全捕捉
- **不是叫大家別用專用工具** —— 而是:**用之前要有獨立證據,別把行銷當實證**

---

# Take Home

> **1.** Nature Medicine 盲化評比:**通用前沿 LLM 三項全勝**過 OpenEvidence、UpToDate Expert AI。

> **2.** 真實臨床問題上,**專用臨床 AI ≈ Google AI Overview**。

> **3.** **「Specialized ≠ Better」** —— 看獨立數據,不看行銷。

> **4.** 導入前問:**第三方評估？當代最新模型？真實臨床問題？**

> **5.** 評的是**答案品質、非病人結果**;為快照、版本會變,結論動態看待。

---

<!-- _class: ref -->
# 參考文獻

1. Vishwanath K, Alyakin A, Ghosh M, et al; Oermann EK (senior). General-purpose large language models outperform specialized clinical AI tools on medical benchmarks. [*Nat Med*. 2026 Jun 12.](https://doi.org/10.1038/s41591-026-04431-5) ｜ PMID [42286322](https://pubmed.ncbi.nlm.nih.gov/42286322/) ｜ [Nature 全文](https://www.nature.com/articles/s41591-026-04431-5)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

本案重點：通用 LLM 勝過專用臨床 AI;「Specialized ≠ Better」;進臨床前要獨立、盲化、真實世界驗證

> 本投影片為讀書會共筆之教學整理，僅供醫療專業人員教學參考；臨床決策請以原始文獻及醫師個人判斷為依據。
