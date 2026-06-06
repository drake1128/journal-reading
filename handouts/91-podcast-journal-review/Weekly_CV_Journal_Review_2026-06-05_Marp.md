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
  section.lead h3 { color: #ffffff; font-weight: normal; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #ffd166; text-decoration: underline; }
  section.divider {
    background-color: #0072bc;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: #ffffff;
    border-bottom: none;
    font-size: 2.4em;
    text-align: center;
  }
  section.divider h2 {
    color: #ffffff;
    font-size: 1.5em;
    text-align: center;
    font-weight: bold;
  }
  section.divider h3 {
    color: #ffe082;
    font-size: 1.2em;
    text-align: center;
    font-weight: normal;
  }
  section.divider p, section.divider strong { color: #ffffff; }
  section.bignum {
    background-color: #1a2740;
    color: #ffffff;
    text-align: center;
  }
  section.bignum h1 { color: #ffffff; font-size: 3.5em; border-bottom: none; }
  section.bignum h2 { color: #b0c4de; font-size: 1.3em; }
  section.bignum p { color: #dfe6e9; font-size: 1.0em; }
  section.bignum strong { color: #ffe082; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  a { color: #0072bc; }
  table { font-size: 0.68em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 5px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.9em;
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
  section.small-text { font-size: 0.74em; }
  section.abbr { font-size: 0.66em; }
  section.ref { font-size: 0.6em; }
  .qr {
    position: absolute;
    right: 40px;
    bottom: 80px;
    text-align: center;
    font-size: 0.65em;
    color: #555;
  }
  .qr img { width: 110px; height: 110px; border: 1px solid #dcdde1; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-05-29 ~ 2026-06-05'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-05-29 ~ 2026-06-05

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜EHJ｜JACC 系列｜EuroIntervention

📱 每篇 Top Pick 附 QR Code，可掃描跳轉原文

---

# 🎯 本週主題與固定欄目

## Finerenone 版圖擴張 × 結構性介入真實世界落地

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 本週 TAVI 重要文獻
3. 🔧 **TEER Section** — 緣對緣 / 三尖瓣介入
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — 精選病例
6. 📑 **參考文獻** — 含 DOI / PMID 連結

> **本週主軸**：FIND-CKD 把 NS-MRA 推進到非糖尿病 CKD、FINE-HEART 證明其降低猝死；ReTAVI 與 COAPT Transportability 把 TAVI-in-TAVI 與 M-TEER 從試驗帶到登錄資料。

---

# ⭐ Top 5 Picks 一覽

| # | 試驗 | 期刊 | 方向 | 關鍵數字 |
|---|------|------|------|---------|
| 1 | **FIND-CKD**（Finerenone 治非糖尿病 CKD） | NEJM | ✅ | 複合腎/心血管 HR 0.77（p=0.04） |
| 2 | **ReTAVI Registry**（TAVI-in-TAVI） | EuroInterv | ✅ | 30 天死亡 3.5%、中風 0.7%（n=143） |
| 3 | **P2Y12 IPD Meta**（早停 Aspirin） | EHJ | ⚖️ | 大出血 RR 0.46；ACS 支架血栓 RR 1.81 |
| 4 | **COAPT Transportability**（M-TEER） | JACC | ✅ | HF 住院 ARR 17.0%（n=15,275） |
| 5 | **FINE-HEART**（Finerenone 猝死） | JACC | ✅ | 猝死 HR 0.81（p=0.034, n=18,991） |

> 圖示：✅ Positive ｜ ⚖️ 利弊並陳 ｜ 💡 Concept-shift ｜ ➰ Early-phase

---

<!-- _class: divider -->
# 📘 NEJM
## Finerenone 跨入非糖尿病 CKD

---

# 🔑 FIND-CKD — Finerenone 治非糖尿病 CKD

## [FIND-CKD Investigators. *N Engl J Med* 2026](https://doi.org/10.1056/NEJMoa2604625)

| 項目 | 內容 |
|------|------|
| 設計 | 雙盲 Phase 3 RCT，追蹤 32 個月；n=**1,584** |
| 族群 | **非糖尿病**慢性腎病（CKD） |
| 主要終點 | eGFR slope **+0.7 mL/min/1.73m²/yr**（p<0.001） |
| 次要終點 | 複合腎/心血管事件 HR **0.77**（0.60–0.99, p=0.04） |
| 安全 | Hyperkalemia 17% vs 13.3% |

> NS-MRA 的腎保護效益**延伸至非糖尿病 CKD**，補上長期缺口。

<div class="qr"><img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https%3A%2F%2Fdoi.org%2F10.1056%2FNEJMoa2604625"><br>FIND-CKD</div>

---

<!-- _class: divider -->
# 🟢 European Heart Journal
## 早停 Aspirin 的效益與代價

---

# ⚠️ P2Y12 Monotherapy — IPD Meta-analysis

## [P2Y12 Monotherapy Collaboration. *Eur Heart J* 2026](https://doi.org/10.1093/eurheartj/ehag381)

| 項目 | 內容 |
|------|------|
| 設計 | IPD meta-analysis，**11 個 RCT**，n=**37,443** |
| 介入 | 早期停 Aspirin（≤1 個月）→ P2Y12 單藥 vs 標準 DAPT |
| 大出血 | RR **0.46** ✓ 降低 54% |
| 支架血栓（ACS 亞組） | RR **1.81** ⚠️ ACS 患者需謹慎 |

> 出血效益明確，但**不可一體適用於 ACS**——支架血栓風險升高，須個體化。

<div class="qr"><img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https%3A%2F%2Fdoi.org%2F10.1093%2Feurheartj%2Fehag381"><br>P2Y12 Meta</div>

---

<!-- _class: divider -->
# 🔵 JACC
## M-TEER 真實世界 × Finerenone 猝死

---

# 🔧 COAPT Transportability — M-TEER 真實世界

## [COAPT Transportability Investigators. *J Am Coll Cardiol* 2026](https://doi.org/10.1016/j.jacc.2026.04.025)

| 項目 | 內容 |
|------|------|
| 設計 | TVT Registry 真實世界分析，n=**15,275** |
| 結果 | HF 住院 ARR ~**17%**，與 COAPT 試驗幾乎相同 |
| Take home | M-TEER 在功能性 MR 的效益**高度可複現** |

> 試驗效益成功外推至真實世界——支持臨床推廣。

<div class="qr"><img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https%3A%2F%2Fdoi.org%2F10.1016%2Fj.jacc.2026.04.025"><br>COAPT-T</div>

---

# 💊 FINE-HEART — Finerenone 與猝死

## [FINE-HEART Investigators. *J Am Coll Cardiol* 2026](https://doi.org/10.1016/j.jacc.2026.04.045)

| 項目 | 內容 |
|------|------|
| 設計 | FIDELIO + FIGARO + FINEARTS 合併（pooled），n=**18,991** |
| 結果 | 猝死（Sudden Death）HR **0.81**（0.67–0.98, p=0.034） |
| 一致性 | 心腎代謝（CKM）各次族群效果一致 |

> Finerenone 除腎/心衰益處外，**降低猝死**的訊號值得納入整體獲益考量。

<div class="qr"><img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https%3A%2F%2Fdoi.org%2F10.1016%2Fj.jacc.2026.04.045"><br>FINE-HEART</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 本週 TAVI 重要文獻

---

# 🫀 ReTAVI Registry — TAVI-in-TAVI

## [ReTAVI Registry Investigators. *EuroIntervention* 2026](https://doi.org/10.4244/EIJ-D-25-01268)

| 項目 | 內容 |
|------|------|
| 設計 | 全球最大前瞻多中心登記：**59 中心**，n=**143** |
| 族群 | 退化 CoreValve/Evolut 上以 SAPIEN 3 行 redo-TAVI（ViV） |
| 30 天 | 死亡 **3.5%**、中風 **0.7%**、PPM **6.3%**、Δ壓差 **−12.0 mmHg** |
| 臨床 | 台灣 redo 需求高峰 2025–2030，現為建立術式的關鍵時機 |

> TAVI-in-TAVI 短期安全性確立——須留意冠脈再通路與瓣膜選擇規劃。

<div class="qr"><img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https%3A%2F%2Fdoi.org%2F10.4244%2FEIJ-D-25-01268"><br>ReTAVI</div>

---

# 🫀 TAVI — 其他焦點

| 主題 | 重點 | 連結 |
|------|------|------|
| **TAVI + 冠狀動脈介入系統性回顧** | CAD + AS 盛行率 ~50–70%；趨勢為「保守選擇性 PCI」（FFR<0.80） | [DOI](https://doi.org/10.4244/EIJ-D-25-00874) |
| **小環 TAVI SEV vs BEV Meta**（n=13,846） | SEV 血流動力學優（較低壓差、較大 EOA、PPM OR 1.63），但 PVR 較多（OR 2.26）；亞洲女性小環尤需衡量 | [DOI](https://doi.org/10.1097/CRD.0000000000001333) |

> 臨床啟示：TAVI 病人的 CAD 處置與瓣膜選擇須整合解剖、血流動力學與長期耐久度。

---

<!-- _class: divider -->
# 🔧 TEER / 三尖瓣介入 Section
## 本週 TEER 重要文獻

---

# 🔧 TEER — 其他焦點

| 主題 | 重點 | 連結 |
|------|------|------|
| **COAPT Transportability**（同 Top Pick #4） | TVT Registry 15,275 例，HF 住院 ARR ~17% | [DOI](https://doi.org/10.1016/j.jacc.2026.04.025) |
| **ASE M-TEER 超音波導引指引 2026** | 術前 MR checklist、術中 en-face TEE 截面標準化、術後急性成功定義 | [DOI](https://doi.org/10.1016/j.echo.2026.03.003) |
| **TEER 年齡與再住院** | TVT Registry：各年齡層（<65 / 65–75 / >75）30 天、90 天再住院率相似；高齡不應拒絕 TEER | [DOI](https://doi.org/10.1016/j.shj.2026.100848) |

> 高齡本身不應成為拒絕 TEER 的理由——以解剖與症狀，而非年齡，決定治療。

---

# 🔬 Case Reports（本週 5 例）

| 主題 | 作者 / 期刊 | 連結 |
|------|------------|------|
| **首例異位性跨腔靜脈 TTVR**（Cross-Caval） | Estévez-Loureiro R et al., *EuroIntervention* | [DOI](https://doi.org/10.4244/EIJ-D-25-01160) |
| **致命性 TTVR 人工瓣膜心內膜炎**（屍解） | Panday SR et al., *JACC Case Rep* | [DOI](https://doi.org/10.1016/j.jaccas.2026.108766) |
| **TTVR（EVOQUE）治 LVAD 患者重度 TR** | Giustino G et al., *JACC Case Rep* | [DOI](https://doi.org/10.1016/j.jaccas.2026.108582) |
| **單次三重：MitraClip + PFA + LAAC** | Frittitta V et al., *JACC Case Rep* | [DOI](https://doi.org/10.1016/j.jaccas.2026.108055) |
| **LMCA 開口突出支架套索取出** | Sarsari M et al., *Eur Heart J Case Rep* | [DOI](https://doi.org/10.1093/ehjcr/ytag327) |

---

# 📚 Honorable Mentions

| 主題 | 重點 | 連結 |
|------|------|------|
| **Tirzepatide CV Biomarkers（SURMOUNT-1）** | NT-proBNP↓、hsCRP↓ — 待 SURPASS-CVOT 確認轉化 | [DOI](https://doi.org/10.1016/j.jacc.2026.04.044) |
| **FLOW Semaglutide 亞組分析** | 糖尿病合併 CKD：各 CV 風險層腎與存活效益一致 | [DOI](https://doi.org/10.1016/j.jacc.2026.02.5125) |
| **SMART-REACH2 終生風險模型** | 已確診 **ASCVD** 患者終生風險與預防效益模型（非主動脈狹窄） | [DOI](https://doi.org/10.1093/eurheartj/ehag400) |
| **女性性別與 AF 腦中風** | 女性**非一致危險因子**；風險升高僅見 ≥75 歲（HR 1.24） | [DOI](https://doi.org/10.1016/j.jacadv.2026.102826) |

---

<!-- _class: divider -->
# 🎓 整合 Take Home
## 本週 5 大臨床啟示

---

# 🎓 本週 5 大臨床啟示

1. **FIND-CKD** — NS-MRA 效益延伸至非糖尿病 CKD：eGFR slope 改善、複合 HR 0.77。
2. **ReTAVI** — TAVI-in-TAVI 安全性確立（30 天死亡 3.5%）；台灣應提前建立術式。
3. **P2Y12 Monotherapy** — 出血降低 54%，但 ACS 支架血栓 RR=1.81，不可一體適用。
4. **COAPT Transportability** — 15,275 例真實世界 ARR=17%，M-TEER 效益可複現。
5. **FINE-HEART** — Finerenone 降低猝死 HR 0.81（p=0.034），擴大整體獲益版圖。

> 共通教訓：**看原始數字，不看摘要結語。**

---

<!-- _class: abbr -->
# 縮寫對照

| 縮寫 | 全名 | 縮寫 | 全名 |
|------|------|------|------|
| CKD | Chronic Kidney Disease | TEER/M-TEER | (Mitral) Transcatheter Edge-to-Edge Repair |
| NS-MRA | Non-Steroidal Mineralocorticoid Receptor Antagonist | TTVR | Transcatheter Tricuspid Valve Replacement |
| eGFR | estimated Glomerular Filtration Rate | MR | Mitral Regurgitation |
| TAVI/TAVR | Transcatheter Aortic Valve Implantation/Replacement | ARR | Absolute Risk Reduction |
| ViV | Valve-in-Valve | HR/RR | Hazard Ratio / Risk Ratio |
| SEV/BEV | Self-Expanding / Balloon-Expandable Valve | CKM | Cardiovascular-Kidney-Metabolic |
| EOA | Effective Orifice Area | LAAC | Left Atrial Appendage Closure |
| PPM | Prosthesis-Patient Mismatch / Permanent Pacemaker | PFA | Pulsed Field Ablation |
| PVR | Paravalvular Regurgitation | LVAD | Left Ventricular Assist Device |
| PCI/FFR | Percutaneous Coronary Intervention / Fractional Flow Reserve | LMCA | Left Main Coronary Artery |
| CAD/AS | Coronary Artery Disease / Aortic Stenosis | IPD | Individual Patient Data |
| DAPT/ACS | Dual Antiplatelet Therapy / Acute Coronary Syndrome | HF | Heart Failure |

---

<!-- _class: ref -->
# 📑 參考文獻 (1/2)

**NEJM**
1. FIND-CKD Investigators. Finerenone in Non-Diabetic CKD (FIND-CKD). [*N Engl J Med* 2026.](https://doi.org/10.1056/NEJMoa2604625) (PMID 42246672)

**European Heart Journal**
2. P2Y12 Monotherapy Collaboration. Aspirin Discontinuation and P2Y12 Monotherapy After PCI: IPD Meta-analysis. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag381) (PMID 42247196)
3. Holtrop J, et al. Lifetime CV Risk Prediction in Established ASCVD: SMART-REACH2 Model. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag400)

**JACC family**
4. COAPT Transportability Investigators. Real-World Transportability of M-TEER Benefit (TVT Registry). [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.04.025) (PMID 42233929)
5. FINE-HEART Investigators. Finerenone and Sudden Death: Pooled Analysis. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.04.045) (PMID 42233928)
6. Sattar N, et al. Long-Term Changes in CV Risk Biomarkers With Tirzepatide: SURMOUNT-1 Post Hoc. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.04.044)
7. Tuttle KR, et al. Kidney/Survival Benefits of Semaglutide in Diabetic CKD: FLOW CV Subgroup. [*J Am Coll Cardiol* 2026.](https://doi.org/10.1016/j.jacc.2026.02.5125)
8. McGarvey C, et al. Female Sex Is Not a Uniform Risk Factor in AF. [*JACC Adv* 2026.](https://doi.org/10.1016/j.jacadv.2026.102826)

---

<!-- _class: ref -->
# 📑 參考文獻 (2/2)

**EuroIntervention**
9. ReTAVI Registry Investigators. Redo-TAVI with SAPIEN 3 in Failed CoreValve/Evolut. [*EuroIntervention* 2026.](https://doi.org/10.4244/EIJ-D-25-01268) (PMID 42219979)
10. PCI and TAVI: A Systematic Review. [*EuroIntervention* 2026.](https://doi.org/10.4244/EIJ-D-25-00874)
11. Estévez-Loureiro R, et al. First-in-Human Heterotopic Cross-Caval TTVR. [*EuroIntervention* 2026.](https://doi.org/10.4244/EIJ-D-25-01160)

**Imaging / Structural Heart**
12. ASE Guidelines for Echo Guidance of M-TEER. [*J Am Soc Echocardiogr* 2026.](https://doi.org/10.1016/j.echo.2026.03.003)
13. Age and Rehospitalization After TEER (TVT Registry). [*Struct Heart* 2026.](https://doi.org/10.1016/j.shj.2026.100848)
14. Small-Annulus TAVI: SEV vs BEV Meta-analysis. [*Cardiol Rev* 2026.](https://doi.org/10.1097/CRD.0000000000001333)

**Case Reports**
15. Panday SR, et al. Fatal Prosthetic Valve Endocarditis After TTVR: Cardiac Autopsy. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.108766)
16. Giustino G, et al. TTVR for Severe TR Post-LVAD. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.108582)
17. Frittitta V, et al. Triple Percutaneous Therapy for MR and AF. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.108055)
18. Sarsari M, et al. Snare Retrieval of Protruding Ostial LMCA Stent. [*Eur Heart J Case Rep* 2026.](https://doi.org/10.1093/ehjcr/ytag327)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

2026-05-29 ~ 2026-06-05

*本文件為讀書會共筆整理，僅供醫療專業人員教學參考*
