# Assessment of Short-Answer Questions by ChatGPT in a Medical School Course / 使用 ChatGPT 評量醫學院課程簡答題

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-01-30**
**原文連結：[NEJM AI — Assessment of Short-Answer Questions by ChatGPT in a Medical School Course](https://doi.org/10.1056/AIcs2500239)**

---

## 核心重點摘要

> **研究目的**：比較 AI (GPT-4o) 與人類評分者對醫學生開放式簡答題的評分一致性。
> **核心問題**：AI 能否減輕簡答題評分的負擔，同時維持評分品質？

---

## 1. 研究背景 (Background)

### 1.1 教育學原理

- 頻繁的低風險測驗 (frequent low-stakes testing) 是促進學習的有力工具
- 簡答題 (short-answer questions) 能促進批判性思考 (critical thinking)
- 然而，簡答題在形成性評量 (formative testing) 中使用不足
- 原因：需要耗時的人工評分

### 1.2 研究目的

主要目標：比較 AI (GPT-4o) 與人類評分者對醫學生開放式簡答題的評分一致性。

---

## 2. 研究方法 (Methods)

### 2.1 研究設計

| 項目 | 說明 |
|------|------|
| 研究類型 | Retrospective case study |
| AI 模型 | GPT-4o (Generative Pretrained Transformer 4o) |
| 研究對象 | 169 位 Harvard Medical School 一年級醫學生 |
| 課程 | 2023-2024 學年 Foundations course |
| 人類評分者 | 10 位受過訓練的評分者 |

### 2.2 評分標準

學生答案依據兩個獨立標準進行評分：

1. **Factual accuracy（事實正確性）**：答案內容是否正確
2. **Completeness（完整性）**：答案是否涵蓋所有重要面向

### 2.3 資料集設計

| 資料集 | Multi-grader Set | Single-grader Set |
|--------|------------------|-------------------|
| 樣本數 | n = 822 responses | n = 8,964 responses |
| 評分方式 | 10 位人類評分者獨立評分相同答案 | 每個答案由一位人類評分者評分 |
| 用途 | Prompt 優化與教學原則校準 | 模擬真實世界條件進行模型評估 |

### 2.4 Prompt Engineering 策略

> **重點提醒**：GPT prompts 經過反覆優化 (iteratively refined)，以達成：
> - **Semantic fairness（語意公平性）**：避免因用詞不同而影響評分
> - **Pedagogical alignment（教學原則一致性）**：符合教育學評量標準
> - **Linguistic flexibility（語言彈性）**：容許學生不同的表達方式

### 2.5 統計分析

**Quadratic-weighted Cohen's Kappa**：

- 用於衡量 AI 與人類評分的一致性程度
- 考慮評分差異的大小（差異越大，懲罰越重）
- Kappa 值解讀：

| 範圍 | 一致性程度 |
|------|-----------|
| < 0.20 | Poor agreement |
| 0.21–0.40 | Fair agreement |
| 0.41–0.60 | Moderate agreement |
| 0.61–0.80 | Substantial agreement |
| 0.81–1.00 | Almost perfect agreement |

---

## 3. 研究結果 (Results)

### 3.1 Multi-grader Dataset 結果

| 評分標準 | Quadratic-weighted Kappa | 一致性程度 |
|----------|--------------------------|-----------|
| Factual accuracy | 0.443 ± 0.127 | Moderate |
| Completeness | 0.429 ± 0.145 | Moderate |

> **重要發現**：94% 的 GPT 生成的 factual accuracy 評分落在人類評分者評分範圍內。這表示 GPT 的評分變異性與人類評分者之間的變異性相當。

### 3.2 Single-grader Dataset 結果

| 評分標準 | Adjusted Kappa* | 一致性程度 |
|----------|-----------------|-----------|
| Factual accuracy | 0.741 | Substantial |
| Completeness | 0.655 | Substantial |

*Adjusted for rater variability using an attenuation factor

> **臨床意義**：超過 85% 的 GPT 評分與人類評分者的分數差距在 1 分以內。在實際應用情境中，GPT-4o 與人類評分者達到 substantial agreement。

### 3.3 結果視覺化比較

| 指標 | Factual Accuracy | Completeness |
|------|-------------------|--------------|
| Multi-grader Kappa | 0.443 (Moderate) | 0.429 (Moderate) |
| Single-grader Kappa | 0.741 (Substantial) | 0.655 (Substantial) |
| GPT 分數在人類範圍內 | 94% | – |
| GPT 與人類差距 ≤1 分 | >85% | >85% |

---

## 4. 討論 (Discussion)

### 4.1 為何 Single-grader Kappa 較高？

- Multi-grader dataset 反映了人類評分者之間的變異性
- 即使是受過訓練的人類評分者，對同一答案的評分也存在差異
- Single-grader dataset 使用 attenuation factor 校正評分者變異性
- 校正後的 kappa 值更能反映 GPT 與「理想人類評分」的一致性

### 4.2 Prompt Engineering 的重要性

| 原則 | 實踐方式 |
|------|----------|
| Pedagogical principles | 將教育學評量原則融入 prompt 設計 |
| Semantic fairness | 確保不同用詞但意義相同的答案獲得相同評分 |
| Linguistic flexibility | 容許學生使用不同的專業術語或表達方式 |
| Iterative refinement | 根據 multi-grader dataset 的回饋不斷優化 prompt |

### 4.3 研究限制

- 單一機構研究（Harvard Medical School）
- 僅評估一門基礎課程
- 未評估長篇申論題或臨床推理題
- AI 評分的長期教育效果尚待研究

---

## 5. 臨床與教育應用

### 5.1 潛在應用場景

1. **形成性評量 (Formative Assessment)**
   - 提供即時回饋給學生
   - 增加低風險測驗的頻率
   - 減輕教師評分負擔

2. **大規模開放式線上課程 (MOOCs)**
   - 使簡答題在大規模教育中變得可行
   - 提供個人化學習回饋

3. **自我評量工具**
   - 學生可使用 AI 進行自我練習
   - 獲得即時的正確性與完整性回饋

### 5.2 實施建議

> **使用 AI 評分系統的建議**：
> 1. 進行機構特定的 prompt 優化與驗證
> 2. 建立人類監督機制（特別是高風險評量）
> 3. 定期校準 AI 與人類評分的一致性
> 4. 向學生說明 AI 評分的角色與限制
> 5. 保留人類複審的管道

---

## 6. Key Points 重點整理

1. **研究目的**：評估 GPT-4o 評分醫學生簡答題與人類評分者的一致性
2. **評分標準**：Factual accuracy（事實正確性）與 Completeness（完整性）
3. **主要發現**：
   - Multi-grader dataset：Kappa 約 0.43–0.44（moderate agreement）
   - Single-grader dataset：Kappa 0.66–0.74（substantial agreement）
   - 94% GPT 評分落在人類評分範圍內
   - >85% GPT 評分與人類差距 ≤1 分
4. **成功關鍵**：Iterative prompt engineering 結合教學原則與語言彈性
5. **應用價值**：AI 評分系統有潛力減輕簡答題評分負擔，使此類題型更廣泛應用於醫學教育
6. **注意事項**：目前達到 moderate-to-substantial agreement，高風險評量仍需人類監督

---

## 7. Cohen's Kappa 補充說明

### 7.1 什麼是 Cohen's Kappa？

Cohen's Kappa (κ) 是衡量兩位評分者一致性的統計指標，校正了隨機一致的機率。

**公式**：κ = (Po − Pe) / (1 − Pe)

- Po = 觀察到的一致比例 (observed agreement)
- Pe = 隨機預期的一致比例 (expected agreement by chance)

### 7.2 Quadratic-weighted Kappa

- 適用於有順序性的評分量表（如 1–5 分）
- 評分差距越大，懲罰越重（二次方權重）
- 比 linear-weighted kappa 對大差距更敏感
- 適合評估「差多少」比「對不對」更重要的情境

---

## 參考文獻

1. Kuling G, Pullman S, Vasilev D, et al. Assessment of Short-Answer Questions by ChatGPT in a Medical School Course. [*NEJM AI*. 2026;3(2).](https://doi.org/10.1056/AIcs2500239)
2. Roediger HL, Karpicke JD. Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention. [*Psychol Sci*. 2006;17(3):249-255.](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
3. McHugh ML. Interrater Reliability: The Kappa Statistic. [*Biochem Med (Zagreb)*. 2012;22(3):276-282.](https://pubmed.ncbi.nlm.nih.gov/23092060/)
4. Kung TH, Cheatham M, Medenilla A, et al. Performance of ChatGPT on USMLE: Potential for AI-Assisted Medical Education Using Large Language Models. [*PLOS Digit Health*. 2023;2(2):e0000198.](https://doi.org/10.1371/journal.pdig.0000198)
