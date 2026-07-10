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
  section.lead h1 { color: #ffffff; font-size: 2.1em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #74b9ff; }
  section.lead blockquote { color: #2d3436; }
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
    font-size: 2.4em;
    text-align: center;
  }
  section.divider h2 { color: #ffe66d; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.70em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.92em;
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
  section.small-text { font-size: 0.78em; }
  section.small-text table { font-size: 0.60em; }
footer: '謝慕揚 MD, PhD, FESC | 乳癌放療與病竇症候群／傳導系統 文獻回顧 | 2026'
---

<!-- _class: lead -->
# 乳癌放射治療與病竇症候群／傳導系統疾病
## Breast Cancer Radiotherapy & Sick Sinus Syndrome / Conduction Disease
**讀書會晨會 · 文獻回顧 (Literature Review)**
謝慕揚 MD, PhD, FESC ｜ 2026-06-21
[關鍵文獻：Kim 2022, JAMA Oncol — SAN dose & arrhythmia](https://pubmed.ncbi.nlm.nih.gov/36136325/)

---

# 臨床緣起 (The Case)

- **61 歲**病人，病房診斷**病竇症候群 (Sick Sinus Syndrome, SSS)**，需植入永久性節律器
- 病人難以接受「這麼年輕就要裝節律器」
- 完整 risk factor 檢查：
  - **無**內分泌病因（甲狀腺低下等）
  - **無**致病藥物
  - **唯一關聯：先前的乳癌放射治療 (radiotherapy, RT)**

> 問題：乳癌 RT 與日後 SSS／傳導系統病變，到底有沒有關聯？

---

<!-- _class: divider -->
# 結論先講
## Bottom Line

---

# 四個重點 (Key Pearls)

> **1.** 有生物學合理性、也有文獻支持；但「乳癌 RT → SSS」的**直接證據**以個案＋劑量學推論為主——因果屬「**相容**」而非「確證」。

> **2.** 解剖反直覺：竇房結 (SAN) 在**右心房**上腔靜脈交界 → **右側**乳癌 RT（含內乳鏈/鎖骨上照野）對 SAN 劑量最高。

> **3.** 最強「劑量—反應」證據來自**肺癌世代**（SAN 劑量 → 心房顫動與死亡率）。

> **4.** 對本案：確認**側別＋照野＋潛伏期**，排除其他病因後可記錄為「possible radiation-associated sinus node dysfunction」。

---

<!-- _class: divider -->
# 解剖與機轉
## 為什麼是「右側」？

---

# 關鍵：側別決定受傷的結構

```text
                乳癌放射治療 (Breast RT)
                          │
          ┌───────────────┴───────────────┐
       左側 (Left)                  右側 (Right) ＋ IMN/鎖骨上照野
          │                               │
   心臟/左心室/LAD 劑量↑           竇房結 (SAN, 右房-SVC 交界) 劑量↑
          │                               │
   缺血性心臟病、心衰              竇房結動脈微血管損傷 ＋ 纖維化
   (傳統「心臟劑量」概念)                  │
                              病竇症候群 (SSS) / 緩脈 / AF
                      (＋ 房室結/希氏纖維化 → AV block)
```

- 機轉同 RIHD：**結內微血管損傷 ＋ 進行性間質纖維化**
- Domanský：**心臟底部（傳導系統起點）是最具放射敏感度的次區域**
- 傳導病變多**晚發（10–20 年）**，但亦可早發（個案 6 個月）

---

# 劑量學：乳癌 RT 對竇房結的劑量

| 研究 | 技術 / 對象 | 左側 SAN | 右側 SAN |
|------|------------|----------|----------|
| **Errahmani 2023** | 3D-CRT, n=116 | 0.47 Gy | **1.57 Gy**（>85% >1 Gy）|
| **Loap 2023** | VMAT, n=12（含區域照野）| 2.8 Gy | **9.6 Gy（max 13.1）** |

- **右心房 (RA) 是 SAN 劑量的最佳替代指標**（R² > 0.80）
- 現代 IMRT/VMAT ＋ 區域照野 → 右側 SAN 劑量從 <1 Gy 升至 ~10 Gy
- 質子治療 (IMPT)、DIBH 可大幅降低結劑量

> 「附帶 SAN 照射」從理論變成臨床上真實存在的暴露

---

<!-- _class: divider -->
# 證據層級
## Dose–Response & Direct Evidence

---

# 劑量—反應：SAN 劑量 → 心律不整（肺癌）

| 研究 | 對象 | 重點發現 |
|------|------|----------|
| **Kim 2022** *JAMA Oncol* | n=560 肺癌 | **SAN Dmax 是新發 AF 最強預測子**：aHR **14.9–15.7**；SAN 劑量↑ → 存活↓ |
| **Graven-Nielsen 2026** *Acta Oncol* | n=273 NSCLC | SAN/RA 劑量與新發 AF、新發心臟病顯著相關 → RA、SAN 應列為 OAR |
| **Butler 2024** *JACC CardioOncol* | n=539（含乳癌/HL）| 乳癌 5 年 AF 僅 1.3%；本研究**肺靜脈**劑量才是最強預測子（爭議點）|

> SAN 劑量與 **AF** 強相關 → 對「SAN 劑量 → 竇房結功能不良」具高度外推合理性（但非對 SSS 的直接測量）

---

# 直接證據：竇房結毒性 / SSS（個案）

- **Pohjola-Sintonen 1990, *Cancer***
  - 33 歲，Hodgkin **縱膈 RT 12 年後** → 症狀性 **SSS 需節律器**（併收縮性心包炎）
  - 文獻中最直接的「RT → SSS → 節律器」個案
- **Qian 2017, *Pract Radiat Oncol***
  - 右側中央肺腫瘤 SABR；1 名於 **6 個月後** SSS 需節律器
  - 顯示竇房結毒性可**早發**

> 緩脈/竇房結毒性與心房顫動共享「心房-竇房結重塑與纖維化」基礎（tachy-brady syndrome）

---

# 直接證據：傳導阻斷 (AV / Complete Block)

- **Orzan 1993**：胸部 Hodgkin RT 後 **13–20 年** 完全心臟阻斷 4 例，多為**結下**，併冠脈/瓣膜/心包病變
- **Slama 1991**：縱膈 RT（Hodgkin/肺/**乳癌**）後結下完全房室阻斷 6 例
- **Bourouis 2022**：**年輕乳癌女性**電療後完全心臟阻斷（與本案情境最近）

> **Slama 放射歸因準則**：① >40 Gy ② 潛伏 ≥10 年 ③ interval 心電圖異常（束支阻斷）④ 心包受累 ⑤ 併存其他放射心臟/縱膈病灶

---

# 族群層級結果與側別（含台灣世代）

| 研究 | 世代 | 重點 |
|------|------|------|
| **Patt 2005** *JCO* | SEER-Medicare, n=16,270 | 傳導異常 左 9.7% vs 右 9.6%（HR 1.07, NS）— 但**舊式 RT、未測 SAN 劑量** |
| **Yang 2025** *Breast* | **台大 NTU, n=975** | 10 年主要 CV 事件 3.7%；右 3.8% vs 左 3.4%（NS）；風險分層：低 0.7% / 中 2.5% / **高 13.7%** |

- 「整體左右無差異」≠「SAN 劑量右側較高」矛盾：前者反映**舊技術、混合終點、SAN 劑量被稀釋**
- 對**個別病人**：右側 ＋ 區域照野 ＋ 可重建高 SAN 劑量 = 有力歸因依據

---

<!-- _class: divider -->
# 套用到本案
## Application to the Case

---

# 這位 61 歲 SSS 病人怎麼歸因？

1. **側別與照野**：右側？含鎖骨上/IMN/區域？→ 若是，SAN 劑量可達數～10 Gy，歸因↑
2. **潛伏期**：RT 與發病間隔？晚發 10–20 年、早發 6 個月皆相容
3. **劑量還原**：請放腫科調舊計畫，重建 SAN/RA 劑量（RA 為良好替代指標）
4. **共病佐證**：找其他 RIHD 線索（心包增厚、瓣膜逆流、冠脈口病變）
5. **排除其他**：已排除甲狀腺/藥物；再確認電解質、睡眠呼吸中止、浸潤性疾病

> **處置不變**：症狀性 SSS → 節律器；但可記錄為「possible radiation-associated sinus node dysfunction」並納入 cardio-oncology 長期追蹤

---

# 證據缺口 (Evidence Gaps)

- **直接證據有限**：乳癌專一的「RT → SSS」幾乎只有個案；最強劑量—反應數據來自**肺癌（終點為 AF）**
- **混雜與終點異質**：大型乳癌世代多為舊技術、混合終點、未測 SAN 劑量
- **尚無劑量上限**：傳導系統的 OAR 劑量限制未確立
- **進行中**：WATCH 等前瞻研究（乳癌 RT 後 AF 篩檢）或能填補空白

---

<!-- _class: small-text -->
# 參考文獻（部分 · 全部經 PubMed 查證）

1. Pohjola-Sintonen S, et al. Sick sinus syndrome as a complication of mediastinal radiation therapy. [*Cancer*. 1990;65(11):2494-6.](https://pubmed.ncbi.nlm.nih.gov/2337864/)
2. Kim KH, et al. Association of sinoatrial node radiation dose with atrial fibrillation and mortality in patients with lung cancer. [*JAMA Oncol*. 2022;8(11):1624-34.](https://pubmed.ncbi.nlm.nih.gov/36136325/)
3. Errahmani MY, et al. Supraventricular cardiac conduction system exposure in breast cancer patients treated with radiotherapy. [*Clin Transl Radiat Oncol*. 2023;38:62-70.](https://pubmed.ncbi.nlm.nih.gov/36388244/)
4. Loap P, et al. Radiation exposure of cardiac conduction nodes during breast proton therapy. [*Int J Part Ther*. 2023;10(1):59-64.](https://pubmed.ncbi.nlm.nih.gov/37823017/)
5. Qian Y, et al. Sinoatrial node toxicity after stereotactic ablative radiation therapy to lung tumors. [*Pract Radiat Oncol*. 2017;7(6):e525-9.](https://pubmed.ncbi.nlm.nih.gov/28669706/)
6. Orzan F, et al. Associated cardiac lesions in patients with radiation-induced complete heart block. [*Int J Cardiol*. 1993;39(2):151-6.](https://pubmed.ncbi.nlm.nih.gov/8314649/)
7. Slama MS, et al. Complete AV block following mediastinal irradiation: six cases. [*PACE*. 1991;14(7):1112-8.](https://pubmed.ncbi.nlm.nih.gov/1715548/)
8. Yang WC, et al. Cardiotoxicity following breast cancer irradiation in an Asian cohort. [*Breast*. 2025;84:104581.](https://pubmed.ncbi.nlm.nih.gov/40991981/)

*完整 21 篇書目見講義 .md（含 Graven-Nielsen 2026、Butler 2024、Patt 2005、Domanský 2024、Bourouis 2022、RIHD 回顧等）*

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**核心訊息：** 排除其他病因後，放射相關竇房結功能不良是合理解釋；
右側乳癌 RT 與區域照野對 SAN 劑量最高。

> 本文件為讀書會共筆整理，供教學與臨床討論，非臨床指引或正式醫囑。
