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
  section.lead a { color: #8ecae6; }
  section.lead blockquote, section.lead blockquote * { color: #2d3436; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 { color: #ffffff; border-bottom: none; font-size: 2.5em; text-align: center; }
  section.divider h2 { color: #ffe066; }
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
    font-size: 0.68em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
  section.ref { font-size: 0.62em; }
footer: '謝慕揚 MD, PhD, FESC | SirPAD Trial | 2026'
---

<!-- _class: lead -->
# SirPAD Trial
## Sirolimus-Coated Balloon Angioplasty for Infrainguinal Artery Disease
### 下肢動脈疾病之 Sirolimus 塗藥球囊血管成形術

**謝慕揚 MD, PhD, FESC** | 2026-08-08

[原文連結：N Engl J Med 2026;395:561-570 — DOI 10.1056/NEJMoa2600360](https://doi.org/10.1056/NEJMoa2600360)

> 讀書會共筆整理，僅供教學參考，非臨床決策依據。所有數值引自原文。

---

# 一句話重點

- **SirPAD** 是首個證實 **sirolimus 塗藥球囊 (SCB)** 在 **all-comers** 下肢 (infrainguinal) PAD，**不僅 non-inferior、更 superior** 於 uncoated balloon，降低 **1 年 MALE** 的 RCT。
- **Primary outcome：8.8% vs 15.0%**
  - median unbiased 風險差 **−4.9 pp (95% CI −8.5 to −1.3)**
  - **P<0.001 (noninferiority)；P=0.009 (superiority)**
- **全因死亡兩組相當**（11.8% vs 12.8%，P=0.67）→ 安全性未見警訊。

---

<!-- _class: divider -->
# 背景
## PAD 與 drug-coated device

---

# 背景：為何要做 SirPAD？

- **PAD** 全球影響 >1.13 億人，是行動障礙、截肢、死亡的重要原因。
- 血管內器材的 RCT **一直未能證明可降低 MALE**。
- **Paclitaxel DCB**（cytotoxic）：可降 restenosis 與 **TLR**，但**是否增加死亡**仍有爭議。
- **Sirolimus**（mTOR 抑制劑，cytostatic）：冠脈 DES 廣泛使用，理論上可抑制內膜增生、減少全身毒性疑慮。

> SirPAD 目的：驗證 SCB 對 uncoated balloon 是否 **non-inferior**，若成立再測 **superior**，以降低下肢 PAD 的 MALE。

---

<!-- _class: divider -->
# 研究方法
## Methods

---

# 試驗設計

- **Phase 3、investigator-initiated、多中心、前瞻、open-label、all-comers、隨機 noninferiority 試驗**；含序列 (hierarchical) superiority 檢定；**盲性結果判定**。
- 瑞士 **44 中心**篩選（Nov 2020–Dec 2024）→ 轉至 **2 個試驗中心**，**15 位操作者**執行。
- **1:1** 隨機（依中心、是否 CLI 分層），於導絲通過目標病灶後才分派。
- 資助：Concept Medical（不受限，不參與設計／分析／撰稿）。

---

# 流程與器材

```text
兩組皆先 uncoated balloon predilation（充氣至參考血管直徑）
        |
  ┌─────┴─────────────────────┐
  SCB 組                       對照組
  MagicTouch PTA SCB          任一核准 uncoated balloon
  (Concept Medical)
        |
  兩組皆 nominal pressure 充氣 120 秒
        |
  dissection / 殘餘狹窄 → 允許 bailout stent（本試驗 37.7%）
```

- 建議 statin、血壓／血糖控制、戒菸；至少 1 個月 DAPT；合適者 dual-pathway inhibition。
- 追蹤：6 與 12 個月。

---

# 終點定義

- **Primary（1 年 MALE）**：目標肢體**非計畫性大截肢** 或 因 **CLI** 之目標病灶 endo/外科 **revascularization**。
- **Key secondary（1 年）**：**任何**目標肢體非計畫性截肢（大或小）或 因 **critical/noncritical** 之目標病灶 revascularization。
- **Primary safety**：1 年**全因死亡**。
- **Noninferiority margin = 5 個百分點**；假設兩組 event rate 10%。
- 樣本 1200→1250（期中發現死亡高於預期，DSMB 建議續行擴充）。

---

<!-- _class: divider -->
# 結果
## Results

---

# 病人與病灶特徵（all-comers）

- 篩選 1544 → **ITT 1252（626 vs 626）**。
- 中位年齡 **75 歲**、女性 **35.1%**、糖尿病約 45%。
- **34.2% critical ischemia (Fontaine)**、**9.8% acute limb ischemia**。
- 目標病灶中位長 **150 mm**；**69.7%** femoropopliteal；**約 30% 膝下**。
- **57.1% total occlusion**；**bailout stent 37.7%**。
- 脫落 2.5%、撤回同意 0.4%。

> 設計貼近真實世界：長病灶、近半 CLI、含膝下 → external validity 高。

---

# 主要結果（Primary & Key Secondary）
## [DOI 10.1056/NEJMoa2600360](https://doi.org/10.1056/NEJMoa2600360)

| 終點 (1 年) | SCB (N=626) | Uncoated (N=626) | 風險差 (95% CI) | P |
|---|---|---|---|---|
| **Primary：MALE** | **55 (8.8%)** | **94 (15.0%)** | **−4.9 (−8.5, −1.3)** | **<0.001 NI；0.009 Sup** |
| **Key secondary** | **144 (23.0%)** | **193 (30.8%)** | **−7.8 (−12.7, −2.9)** | **0.002 Sup** |

- Primary 為 **median unbiased estimate**；不計期中分析為 **−6.2 pp (−9.8, −2.7)**。
- Primary 兩組成成分（截肢、因 CLI 之 revascularization）方向一致。

---

# 次要療效終點
## [DOI 10.1056/NEJMoa2600360](https://doi.org/10.1056/NEJMoa2600360)

| 終點 (1 年) | SCB | Uncoated | 風險差 (95% CI) |
|---|---|---|---|
| TLR（critical 或 noncritical） | 19.8% | 25.9% | −6.1 (−10.7, −1.4) |
| TLR（critical ischemia） | 8.3% | 13.3% | −5.0 (−8.4, −1.5) |
| 任何非計畫性截肢 | 5.9% | 8.8% | −2.9 (−5.8, 0.0) |
| 非計畫性大截肢 | 1.3% | 2.7% | −1.4 (−3.1, 0.2) |
| Rutherford ≥1 級改善（1yr） | 82.5% | 78.5% | 4.0 (−1.1, 9.1) |

> 除 primary/key secondary 外，CI 未校正多重性，不可用於假設檢定。

---

# 安全性
## [DOI 10.1056/NEJMoa2600360](https://doi.org/10.1056/NEJMoa2600360)

| 終點 (1 年) | SCB (N=626) | Uncoated (N=626) | 風險差 (95% CI) | P |
|---|---|---|---|---|
| **全因死亡** | **74 (11.8%)** | **80 (12.8%)** | **−1.0 (−4.6, 2.7)** | **0.67** |
| 嚴重不良事件 | 364 (58.1%) | 364 (58.1%) | 0.0 (−5.4, 5.4) | — |

- 各預定時間點死亡率相當。
- competing-risk（含 Cox）、sensitivity、subgroup 分析與主分析一致。

> 對 paclitaxel 器材的死亡疑慮，sirolimus DCB **1 年未見警訊**；死亡率高反映 all-comers 共病重、CLI 多。

---

<!-- _class: divider -->
# 討論與臨床意涵

---

# 討論重點

- **臨床意義的躍升**：paclitaxel DCB 過去**只證實降再介入 (TLR)**；SirPAD 首度顯示 sirolimus DCB **同時**降再介入與**臨床肢體結果**（截肢＋因 CLI 之 revascularization）。
- **external validity 高**：all-comers、近半 CLI、中位病灶 150 mm、約 30% 膝下（膝下再狹窄／截肢風險更高）。
- **安全**：全因死亡相當、SAE 完全相同 (58.1% vs 58.1%)。
- **臨床連結**：支持在長病灶、膝下、CLI 之下肢介入採用 **sirolimus DCB**，於不增死亡風險下降低 MALE 與再介入。

---

# 限制 (Limitations)

1. **未針對截肢 power**：任何截肢 5.9% vs 8.8%（RD −2.9，CI −5.8 to 0.0，觸及 0）→ 待進一步研究。
2. **追蹤僅 1 年**：療效是否衰減未知；**5 年追蹤進行中**（評估長期死亡是否過剩）。
3. **Open-label**：雖盲性判定，仍可能影響輔助治療與再介入門檻。
4. **單一醫療系統、以白人為主** → 外推性受限。
5. 器材製造商提供資金（但不參與設計／分析／撰稿）。

---

# Clinical Pearls

> **1.** 首個證明血管內器材（sirolimus DCB）能 **superior 降低 1 年 MALE** 的 RCT：8.8% vs 15.0%，P=0.009。

> **2.** 與 paclitaxel「只降再介入」不同，sirolimus DCB **同時**改善再介入與臨床肢體結果。

> **3.** 安全性未見警訊：死亡 11.8% vs 12.8% (P=0.67)、SAE 58.1% vs 58.1%；5 年死亡追蹤進行中。

> **4.** 流程：兩組皆 predilation → SCB/uncoated **120 秒 nominal pressure** → 需要時 bailout stent（37.7%）。

---

<!-- _class: divider -->
# 縮寫對照 & 參考文獻

---

<!-- _class: small-text -->
# 縮寫對照表

| 縮寫 | 全名 (中文) |
|---|---|
| PAD | Peripheral Artery Disease（周邊動脈疾病） |
| SCB / DCB | Sirolimus-Coated / Drug-Coated Balloon（塗藥球囊） |
| MALE | Major Adverse Limb Events（主要不良肢體事件） |
| CLI / CLTI | Critical Limb Ischemia / Chronic Limb-Threatening Ischemia |
| TLR | Target-Lesion Revascularization（目標病灶再血管化） |
| PTA | Percutaneous Transluminal Angioplasty |
| mTOR | mammalian Target Of Rapamycin |
| DSMB | Data and Safety Monitoring Board |
| RD / NI / Sup | Risk Difference / Noninferiority / Superiority |

---

<!-- _class: ref -->
# 參考文獻

1. Barco S, et al. Sirolimus-Coated Balloon Angioplasty for Infrainguinal Artery Disease (SirPAD). [*N Engl J Med*. 2026;395(6):561-570.](https://doi.org/10.1056/NEJMoa2600360)
2. Barco S, et al. Structured protocol summary of the "SirPAD" RCT. [*Trials*. 2022;23:334.](https://pubmed.ncbi.nlm.nih.gov/?term=SirPAD+structured+protocol+summary+Trials+2022+Barco)
3. Rosenfield K, et al. Paclitaxel-coated balloon for femoropopliteal disease (LEVANT 2). [*N Engl J Med*. 2015;373:145-153.](https://doi.org/10.1056/NEJMoa1406235)
4. Nordanstig J, et al. SWEDEPAD 2 (intermittent claudication). [*Lancet*. 2025;406:1115-1127.](https://pubmed.ncbi.nlm.nih.gov/?term=SWEDEPAD+2+Nordanstig+Lancet+2025)
5. Falkenberg M, et al. SWEDEPAD 1 (CLTI). [*Lancet*. 2025;406:1103-1114.](https://pubmed.ncbi.nlm.nih.gov/?term=SWEDEPAD+1+Falkenberg+Lancet+2025)
6. Parikh SA, et al. Mortality with paclitaxel-coated devices: patient-level meta-analysis. [*Lancet*. 2023;402:1848-1856.](https://pubmed.ncbi.nlm.nih.gov/?term=Parikh+paclitaxel+femoropopliteal+mortality+meta-analysis+Lancet+2023)
7. Bonaca MP, et al. Rivaroxaban in PAD after revascularization (VOYAGER PAD). [*N Engl J Med*. 2020;382:1994-2004.](https://doi.org/10.1056/NEJMoa2000052)
8. Liistro F, et al. IN.PACT BTK randomised trial. [*EuroIntervention*. 2022;17(17):e1445-e1454.](https://pubmed.ncbi.nlm.nih.gov/?term=IN.PACT+BTK+Liistro+infrapopliteal+EuroIntervention+2022)
9. Mazzolai L, et al. 2024 ESC Guidelines for peripheral arterial and aortic diseases. [*Eur Heart J*. 2024;45:3538-3700.](https://pubmed.ncbi.nlm.nih.gov/?term=2024+ESC+Guidelines+peripheral+arterial+aortic+diseases+Mazzolai)
10. GBD 2019 PAD Collaborators. Global burden of PAD 1990-2019. [*Lancet Glob Health*. 2023;11(10):e1553-e1565.](https://pubmed.ncbi.nlm.nih.gov/?term=Global+burden+peripheral+artery+disease+1990-2019+Lancet+Global+Health+2023)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

[SirPAD — N Engl J Med 2026;395:561-570](https://doi.org/10.1056/NEJMoa2600360)
