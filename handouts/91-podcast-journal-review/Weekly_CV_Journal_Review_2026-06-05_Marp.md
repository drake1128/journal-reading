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

涵蓋期刊：NEJM｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Top Pick 附 QR Code，可掃描跳轉原文

---

# 🎯 本週主題與固定欄目

## 腎保護、再次介入與抗血小板精準化

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 本週 TAVI 重要文獻
3. 🔧 **TEER Section** — MitraClip / TriClip 進展
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — 本週精選 5 例
6. 📖 **參考文獻 + 縮寫對照**

---

# ⭐ Top 5 Picks

| 試驗 | 期刊 | 關鍵數字 |
|------|------|----------|
| **FIND-CKD** | *NEJM* | 複合腎/心血管 Hazard Ratio (HR) **0.77** (p=0.04) |
| **ReTAVI Registry** | *EuroIntervention* | 30 天死亡 **3.5%**，中風 **0.7%** |
| **P2Y12 Monotherapy IPD Meta-analysis** | *Eur Heart J* | 大出血 Relative Risk (RR) **0.46** vs 12m Dual Antiplatelet Therapy (DAPT) |
| **COAPT Transportability** | *JACC* | 真實世界 Absolute Risk Reduction (ARR) **17.0%** |
| **FINE-HEART Sudden Death** | *JACC* | 猝死 HR **0.81** (p=0.034) |

---

<!-- _class: divider -->
# Pick #1
## FIND-CKD
### 非糖尿病慢性腎病的 Finerenone 首次 RCT 證據

---

# FIND-CKD — 研究設計

**Bacchetta J, et al.** *N Engl J Med.* 2026 Jun 4.
🔗 [DOI: 10.1056/NEJMoa2604625](https://doi.org/10.1056/NEJMoa2604625)

- 雙盲 Phase 3 Randomized Controlled Trial (RCT)
- 對象：**非糖尿病型慢性腎病 (Non-Diabetic Chronic Kidney Disease, ND-CKD)**
- 樣本數：n = **1,584**
- 介入：Finerenone（非鹽皮質素受體拮抗劑，Non-Steroidal Mineralocorticoid Receptor Antagonist, NS-MRA）
- 追蹤：**32 個月**

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1056%2FNEJMoa2604625"><br>📱 Scan DOI
</div>

---

# FIND-CKD — 主要結果

| 終點 | HR / 差異 | P |
|------|-----------|---|
| **Estimated Glomerular Filtration Rate (eGFR) slope（主要）** | **顯著改善**（+0.7 mL/min/1.73m²/yr） | **< 0.001** |
| **複合腎/心血管事件** | **HR 0.77**（0.60–0.99） | **0.04** |
| 複合腎事件 | HR 0.78（0.60–1.01） | 0.06 |
| 複合心血管事件 | HR 0.60（0.27–1.33） | NS |
| **高血鉀（Hyperkalemia）** | **17.0%** vs **13.3%** | — |

> ⚠️ 階層性測試：eGFR slope 達主要終點；複合腎/心血管 p=0.04 為次要終點。**個別腎或心血管複合未單獨達顯著。**

---

<!-- _class: bignum -->
# HR 0.77
## 複合腎 / 心血管事件
### FIND-CKD | N Engl J Med | 2026｜n = 1,584

首次在**非糖尿病**慢性腎病確認 NS-MRA 保護

---

# FIND-CKD — 臨床啟示

> **NS-MRA 保護效益不再限於糖尿病 CKD**
>
> FIDELIO-DKD + FIGARO-DKD（糖尿病）→ FIND-CKD（非糖尿病）

**實務重點**：
- Hyperkalemia（17% vs 13.3%）需定期監測血鉀
- Renin-Angiotensin-Aldosterone System inhibitor (RAASi) 合用時更需謹慎
- 台灣非糖尿病 IgA 腎病、局灶節段性腎絲球硬化症 (FSGS) 患者可能是受益族群

---

<!-- _class: divider -->
# Pick #2
## ReTAVI Registry
### TAVI-in-TAVI 全球最大前瞻性多中心登記

---

# ReTAVI Registry — 設計

**Abdel-Wahab M, et al.** *EuroIntervention.* 2026.
🔗 [DOI: 10.4244/EIJ-D-25-01268](https://doi.org/10.4244/EIJ-D-25-01268)

- 前瞻性多中心觀察性登記研究
- **59 個中心**（歐洲 + 加拿大）
- n = **143**（退化 CoreValve/Evolut 接受 redo-TAVI）
- 介入：SAPIEN 3 / SAPIEN 3 Ultra（Valve-in-Valve, ViV）
- 評估標準：Valve Academic Research Consortium-3 (VARC-3)

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.4244%2FEIJ-D-25-01268"><br>📱 Scan DOI
</div>

---

<!-- _class: bignum -->
# 3.5%
## 30 天全因死亡率
### ReTAVI Registry | EuroIntervention 2026｜59 centers

中風 **0.7%**｜永久性心律調節器 (PPM) **6.3%**

---

# ReTAVI Registry — 臨床啟示

> **TAVI-in-TAVI 安全性與初次 TAVI 相當**

**台灣視角**：
- 台灣 TAVI 起步晚（2012–2015），redo 需求高峰約 2025–2030
- **現在是建立 TAVI-in-TAVI 術式經驗的關鍵時機**

**技術要點**：
- SAPIEN BEV 在退化 SEV 骨架內密封性良好
- 術前 CT 評估：**冠狀動脈高度、frame fracture 風險**
- Commissural alignment 可減少冠狀動脈阻塞風險

---

<!-- _class: divider -->
# Pick #3
## P2Y12 Monotherapy IPD Meta-analysis
### 11 個 RCT，n = 37,443｜早期停 Aspirin 的效益與代價

---

# P2Y12 Monotherapy — 設計與結果

**Brouwer MA, et al.** *Eur Heart J.* 2026.
🔗 [DOI: 10.1093/eurheartj/ehag381](https://doi.org/10.1093/eurheartj/ehag381)

- 個體患者資料 (Individual Patient Data, IPD) 統合分析
- **11 個 RCT**，n = **37,443**
- 比較：早期停 Aspirin（≤1 個月）→ P2Y12 Monotherapy vs 12 月 DAPT

| 終點 | RR | 臨床意義 |
|------|-----|---------|
| **大出血（Major Bleeding）** | **0.46** | ✓ 大幅降低（−54%） |
| **支架血栓 — 全體** | NS | 整體安全 |
| **支架血栓 — ACS 亞組** | **1.81** ⚠️ | ACS 患者需謹慎 |

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1093%2Feurheartj%2Fehag381"><br>📱 Scan DOI
</div>

---

# P2Y12 Monotherapy — 臨床啟示

> **出血效益明確，但 ACS 支架血栓 RR=1.81 不容忽視**

**實務建議**：

| 族群 | 策略 |
|------|------|
| **穩定型 CCS（Chronic Coronary Syndrome）** | 1 個月 DAPT → P2Y12 monotherapy：效益明確 |
| **低出血風險 ACS** | 至少 3–6 個月 DAPT 再考慮轉 monotherapy |
| **高出血風險 ACS** | 個別化決策（出血 vs 缺血平衡） |

---

<!-- _class: divider -->
# Pick #4
## COAPT Transportability
### 試驗效益在 15,275 例真實世界患者中完整複現

---

# COAPT Transportability — 結果

**Stone GW, et al.** *J Am Coll Cardiol.* 2026.
🔗 [DOI: 10.1016/j.jacc.2026.04.025](https://doi.org/10.1016/j.jacc.2026.04.025)

- Transcatheter Valve Therapy (TVT) Registry，n = **15,275**
- 外部效度因果推論分析

| 分析 | 心臟衰竭住院 ARR |
|------|-----------------|
| **COAPT 試驗（原始）** | ~17% |
| **真實世界 TVT Registry** | **~17%** ✓ |

> **COAPT 效益在真實世界高度可複現**
> 
> 「試驗結果無法轉化臨床」的擔憂對 M-TEER **不成立**

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1016%2Fj.jacc.2026.04.025"><br>📱 Scan DOI
</div>

---

<!-- _class: divider -->
# Pick #5
## FINE-HEART Sudden Death
### Finerenone 跨 CKM 族群猝死保護

---

# FINE-HEART Sudden Death — 結果

**Filippatos G, et al.** *J Am Coll Cardiol.* 2026.
🔗 [DOI: 10.1016/j.jacc.2026.04.045](https://doi.org/10.1016/j.jacc.2026.04.045)

- FIDELIO-DKD + FIGARO-DKD + FINEARTS-HF 合併分析
- n = **18,991**；中位追蹤 2.9 年

| 終點 | Finerenone | Placebo | HR | P |
|------|-----------|---------|-----|---|
| **猝死 (Sudden Cardiac Death, SCD)** | 2.0% | 2.5% | **0.81**（0.67–0.98）| **0.034** |

效益在不同 Cardio-Kidney-Metabolic (CKM) 組合中**一致**

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1016%2Fj.jacc.2026.04.045"><br>📱 Scan DOI
</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 本週 TAVI 相關文獻
### Drake 主要臨床方向

---

# TAVI #2 — TAVI 合併冠狀動脈介入系統性回顧

**Auffret V, et al.** *EuroIntervention.* 2026.
🔗 [DOI: 10.4244/EIJ-D-25-00874](https://doi.org/10.4244/EIJ-D-25-00874)

- CAD 合併 AS：盛行率 **~50–70%**
- 爭議：哪些需要 pre-TAVI Percutaneous Coronary Intervention (PCI)？

**趨勢**：**保守選擇性 PCI**（僅針對 Fractional Flow Reserve (FFR) < 0.80 的血流受限病灶）

> ⚠️ **不是所有 CAD 都需要 pre-TAVI PCI**
>
> FAITAVI 試驗為此提供最新 RCT 資料

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.4244%2FEIJ-D-25-00874"><br>📱 Scan DOI
</div>

---

# TAVI #3 — 小環 TAVI：SEV vs BEV Meta-analysis

**Alomair MH, et al.** *Cardiol Rev.* 2026.
🔗 [DOI: 10.1097/CRD.0000000000001333](https://doi.org/10.1097/CRD.0000000000001333)

n = **13,846**；小環患者 Self-Expanding Valve (SEV) vs Balloon-Expandable Valve (BEV)

| 指標 | 優勝者 |
|------|--------|
| 血流動力學（壓差、Effective Orifice Area (EOA)） | **SEV 明顯優勢** |
| Patient-Prosthesis Mismatch (PPM) 風險 | **SEV 較低**（OR 1.63） |
| Paravalvular Regurgitation (PVR) | **BEV 較少**（SEV OR 2.26） |

> 亞洲女性瓣環偏小 → SEV 血流動力學優勢但需控制 PVL

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1097%2FCRD.0000000000001333"><br>📱 Scan DOI
</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## MitraClip × TriClip × PASCAL 進展
### Drake 的 TEER 操作面向

---

# TEER #1 — COAPT Transportability（詳見 Pick #4）

**Key Take-Away for TEER Operators**：

- COAPT-like 患者篩選標準（Mitral Regurgitation (MR) ≥ 3+、最佳藥物治療下仍有症狀）遵循好，**效益可複現**

- 15,275 TVT Registry 患者 = **全球最大真實世界 M-TEER 效度驗證**

- 台灣各中心應確立 COAPT-like 篩選流程作為 MitraClip / PASCAL 的標準

---

# TEER #2 — ASE M-TEER 超音波導引指引 2026

**Zoghbi WA, et al.** *J Am Soc Echocardiogr.* 2026.
🔗 [DOI: 10.1016/j.echo.2026.03.003](https://doi.org/10.1016/j.echo.2026.03.003)

**3 大核心模組**：

1. **術前評估**：MR 機制（Carpentier 分類）、適應症 TEE checklist
2. **術中導引**：Clip 定位最佳截面、**en-face（外科醫師視角）** 不可或缺
3. **術後評估**：急性成功標準（MR ≤ 2+）、早期併發症超音波特徵

> **TEER 操作者必須能自行判讀 TEE 或與 echo team 緊密合作**

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1016%2Fj.echo.2026.03.003"><br>📱 Scan DOI
</div>

---

# TEER #3 — 年齡不影響 TEER 術後再住院率

**Kapoor A, et al.** *Struct Heart.* 2026.
🔗 [DOI: 10.1016/j.shj.2026.100848](https://doi.org/10.1016/j.shj.2026.100848)

- TVT Registry 回溯性分析
- **結果**：各年齡層（< 65 / 65–75 / > 75 歲）30 天和 90 天再住院率**相似**

> **高齡本身不應成為拒絕 TEER 的理由**

再住院預測因子：**基礎腎功能、左心室射出分率（Left Ventricular Ejection Fraction, LVEF）**，而非年齡

台灣 TEER 患者平均年齡高（80+ 歲常見）→ 此結果直接支持積極策略

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1016%2Fj.shj.2026.100848"><br>📱 Scan DOI
</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

# 其他值得一讀

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **Tirzepatide CV Biomarkers** (SURMOUNT-1 post-hoc) | *JACC* | NT-proBNP↓, hsCRP↓ — **待 SURPASS-CVOT 確認** | [DOI](https://doi.org/10.1016/j.jacc.2026.04.042) |
| **FLOW GLP-1 CKD subgroup** | *JACC* | Semaglutide 腎保護跨 CV 風險層**一致** | [DOI](https://doi.org/10.1016/j.jacc.2026.04.021) |
| **SMART-REACH2** lifetime risk | *Eur Heart J* | **終生**心血管風險模型 → 推動積極治療 | [DOI](https://doi.org/10.1093/eurheartj/ehag352) |
| **Female Sex & AF Stroke** | *JACC Adv* | 女性 CHA₂DS₂-VASc 相同時腦中風風險更高 | [DOI](https://doi.org/10.1016/j.jacadv.2026.101772) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 本週精選 5 例
### EuroIntervention × 1｜JACC Case Rep × 3｜EHJ Case Rep × 1

---

# Case #1 — 首例異位性跨腔靜脈 TTVR

**Hahn RT, et al.** *EuroIntervention.* 2026.
🔗 [DOI: 10.4244/EIJ-D-25-01160](https://doi.org/10.4244/EIJ-D-25-01160)

**First-in-Human Heterotopic Cross-Caval Transcatheter Tricuspid Valve Replacement (TTVR)**

- 解剖條件不適合 orthotopic TTVR 的嚴重 Tricuspid Regurgitation (TR)
- **異位植入**：下腔靜脈與右心房交界阻斷逆流
- 開創性術式首次人體報告

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.4244%2FEIJ-D-25-01160"><br>📱 Scan DOI
</div>

---

# Case #2 — 致命性 TTVR 人工瓣膜心內膜炎（屍解報告）

**Kaur M, et al.** *JACC Case Rep.* 2026.
🔗 [DOI: 10.1016/j.jaccas.2026.108766](https://doi.org/10.1016/j.jaccas.2026.108766)

**Fatal Prosthetic Valve Endocarditis (IE) After TTVR**

- TTVR 後感染性心內膜炎致死——罕見但需高度警覺
- 屍解揭示：瓣葉 vegetation、血栓、組織侵犯
- 術後發燒 / 菌血症 → 必須積極排除人工瓣膜 IE

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1016%2Fj.jaccas.2026.108766"><br>📱 Scan DOI
</div>

---

# Case #3 — TTVR + LVAD：Edwards EVOQUE 56mm

**Aithal S, et al.** *JACC Case Rep.* 2026.
🔗 [DOI: 10.1016/j.jaccas.2026.108582](https://doi.org/10.1016/j.jaccas.2026.108582)

**TTVR with Edwards EVOQUE 56 mm After Prior Left Ventricular Assist Device (LVAD)**

- LVAD 後常見嚴重 TR（右室後負荷改變）
- **EVOQUE 56mm**（最大尺寸）在 LVAD 情境下的技術可行性
- 多器械協調：LVAD 血流對 TTVR sizing 和定位的影響

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1016%2Fj.jaccas.2026.108582"><br>📱 Scan DOI
</div>

---

# Case #4 — 三重一站式：MitraClip + PFA + LAAC

**Brubaker SG, et al.** *JACC Case Rep.* 2026.
🔗 [DOI: 10.1016/j.jaccas.2026.108055](https://doi.org/10.1016/j.jaccas.2026.108055)

**Simultaneous MitraClip + Pulsed-Field Ablation (PFA) + Left Atrial Appendage Closure (LAAC)**

- AF 合併 MR 合併高腦中風風險 → **一次手術三問題同解**
- 技術要點：單次房間隔穿刺、腎功能保護（顯影劑管理）
- 代表 2026 年「一站式治療（One-Stop Shop）」前沿趨勢

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1016%2Fj.jaccas.2026.108055"><br>📱 Scan DOI
</div>

---

# Case #5 — LMCA 開口突出支架套索取出

**Silva CM, et al.** *Eur Heart J Case Rep.* 2026.
🔗 [DOI: 10.1093/ehjcr/ytag327](https://doi.org/10.1093/ehjcr/ytag327)

**Snare Retrieval of a Protruding Stent at the Ostial Left Main Coronary Artery (LMCA)**

- LMCA 開口支架突出至主動脈 → 干擾 TAVI 後冠狀動脈介入
- **套索 (Snare) 技術**經皮取出——關鍵搶救手法
- LMCA 操作失誤可即刻致命 → 此類搶救報告珍貴

<div class="qr">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fdoi.org%2F10.1093%2Fehjcr%2Fytag327"><br>📱 Scan DOI
</div>

---

<!-- _class: lead -->
# 💎 Take Home Message

### 1. **FIND-CKD**：NS-MRA 保護延伸至非糖尿病 CKD — eGFR slope 改善，複合 HR 0.77
### 2. **ReTAVI**：TAVI-in-TAVI 安全性確立（30 天死亡 3.5%）— 台灣應建立術式
### 3. **P2Y12 Monotherapy**：出血降低 54%，但 ACS 支架血栓 RR=1.81
### 4. **COAPT Transportability**：15,275 例真實世界 ARR=17% — 試驗效益可複現
### 5. **FINE-HEART**：Finerenone 降低猝死 HR 0.81（p=0.034）
### 6. **Case Reports**：TTVR 普及化、MitraClip 一站式、LMCA 搶救
### 7. **看原始數字，不看摘要結語**

---

<!-- _class: small-text -->
# 完整參考文獻 (1/2)

**Top 5 Picks**：
1. Bacchetta J, et al. FIND-CKD. [*N Engl J Med.* 2026 Jun 4.](https://doi.org/10.1056/NEJMoa2604625) ｜ [PMID 42246672](https://pubmed.ncbi.nlm.nih.gov/42246672/)
2. Abdel-Wahab M, et al. ReTAVI Registry. [*EuroIntervention.* 2026.](https://doi.org/10.4244/EIJ-D-25-01268) ｜ [PMID 42219979](https://pubmed.ncbi.nlm.nih.gov/42219979/)
3. Brouwer MA, et al. P2Y12 IPD Meta-analysis. [*Eur Heart J.* 2026.](https://doi.org/10.1093/eurheartj/ehag381) ｜ [PMID 42247196](https://pubmed.ncbi.nlm.nih.gov/42247196/)
4. Stone GW, et al. COAPT Transportability. [*J Am Coll Cardiol.* 2026.](https://doi.org/10.1016/j.jacc.2026.04.025) ｜ [PMID 42233929](https://pubmed.ncbi.nlm.nih.gov/42233929/)
5. Filippatos G, et al. FINE-HEART Sudden Death. [*J Am Coll Cardiol.* 2026.](https://doi.org/10.1016/j.jacc.2026.04.045) ｜ [PMID 42233928](https://pubmed.ncbi.nlm.nih.gov/42233928/)

**TAVI Section**：
6. Auffret V, et al. TAVI + Coronary Interventions review. [*EuroIntervention.* 2026.](https://doi.org/10.4244/EIJ-D-25-00874) ｜ [PMID 42219978](https://pubmed.ncbi.nlm.nih.gov/42219978/)
7. Alomair MH, et al. Small Annulus SEV vs BEV Meta-analysis. [*Cardiol Rev.* 2026.](https://doi.org/10.1097/CRD.0000000000001333) ｜ [PMID 42237081](https://pubmed.ncbi.nlm.nih.gov/42237081/)

---

<!-- _class: small-text -->
# 完整參考文獻 (2/2)

**TEER Section**：
8. Zoghbi WA, et al. ASE M-TEER Guideline. [*J Am Soc Echocardiogr.* 2026.](https://doi.org/10.1016/j.echo.2026.03.003) ｜ [PMID 42242827](https://pubmed.ncbi.nlm.nih.gov/42242827/)
9. Kapoor A, et al. TEER Readmissions by Age. [*Struct Heart.* 2026.](https://doi.org/10.1016/j.shj.2026.100848) ｜ [PMID 42245276](https://pubmed.ncbi.nlm.nih.gov/42245276/)

**Honorable Mentions**：
10. Bhatt DL, et al. Tirzepatide SURMOUNT-1. [*J Am Coll Cardiol.* 2026.](https://doi.org/10.1016/j.jacc.2026.04.042) ｜ [PMID 42233927](https://pubmed.ncbi.nlm.nih.gov/42233927/)
11. Mahaffey KW, et al. FLOW CKD subgroup. [*J Am Coll Cardiol.* 2026.](https://doi.org/10.1016/j.jacc.2026.04.021) ｜ [PMID 42233552](https://pubmed.ncbi.nlm.nih.gov/42233552/)
12. Visseren FLJ, et al. SMART-REACH2. [*Eur Heart J.* 2026.](https://doi.org/10.1093/eurheartj/ehag352) ｜ [PMID 42246978](https://pubmed.ncbi.nlm.nih.gov/42246978/)
13. Andrade JG, et al. Female Sex & AF Stroke. [*JACC Adv.* 2026.](https://doi.org/10.1016/j.jacadv.2026.101772) ｜ [PMID 42240529](https://pubmed.ncbi.nlm.nih.gov/42240529/)

**Case Reports**：
14. Hahn RT, et al. Heterotopic Cross-Caval TTVR. [*EuroIntervention.* 2026.](https://doi.org/10.4244/EIJ-D-25-01160) ｜ [PMID 42219977](https://pubmed.ncbi.nlm.nih.gov/42219977/)
15. Kaur M, et al. Fatal TTVR IE autopsy. [*JACC Case Rep.* 2026.](https://doi.org/10.1016/j.jaccas.2026.108766) ｜ [PMID 42246908](https://pubmed.ncbi.nlm.nih.gov/42246908/)
16. Aithal S, et al. EVOQUE 56mm post-LVAD. [*JACC Case Rep.* 2026.](https://doi.org/10.1016/j.jaccas.2026.108582) ｜ [PMID 42240539](https://pubmed.ncbi.nlm.nih.gov/42240539/)
17. Brubaker SG, et al. MitraClip + PFA + LAAC. [*JACC Case Rep.* 2026.](https://doi.org/10.1016/j.jaccas.2026.108055) ｜ [PMID 42240254](https://pubmed.ncbi.nlm.nih.gov/42240254/)
18. Silva CM, et al. LMCA snare retrieval. [*Eur Heart J Case Rep.* 2026.](https://doi.org/10.1093/ehjcr/ytag327) ｜ [PMID 42244818](https://pubmed.ncbi.nlm.nih.gov/42244818/)

---

<!-- _class: abbr -->
# 縮寫對照表 (1/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| TAVI / TAVR | Transcatheter Aortic Valve Implantation / Replacement | 經導管主動脈瓣置換術 |
| TEER / M-TEER | Transcatheter / Mitral Edge-to-Edge Repair | 經導管邊緣對邊修復術 |
| TTVR | Transcatheter Tricuspid Valve Replacement | 經導管三尖瓣置換術 |
| ViV | Valve-in-Valve | 瓣中瓣 |
| PPM | Permanent Pacemaker (or Patient-Prosthesis Mismatch) | 永久性心律調節器植入 |
| SEV / BEV | Self-Expanding / Balloon-Expandable Valve | 自膨脹型 / 球囊膨脹型瓣膜 |
| PVR / PVL | Paravalvular Regurgitation / Leak | 人工瓣膜旁逆流 |
| CKD | Chronic Kidney Disease | 慢性腎病 |
| NS-MRA | Non-Steroidal Mineralocorticoid Receptor Antagonist | 非類固醇型 MRA |
| CKM | Cardio-Kidney-Metabolic Syndrome | 心-腎-代謝症候群 |
| SCD | Sudden Cardiac Death | 猝死 |
| eGFR | Estimated Glomerular Filtration Rate | 估計腎絲球過濾率 |
| RAASi | Renin-Angiotensin-Aldosterone System inhibitor | RAAS 抑制劑 |
| MR / TR / AS | Mitral / Tricuspid Regurgitation / Aortic Stenosis | 二尖瓣逆流 / 三尖瓣逆流 / 主動脈瓣狹窄 |
| DAPT / IPD | Dual Antiplatelet Therapy / Individual Patient Data | 雙重抗血小板 / 個體患者資料 |
| RCT | Randomized Controlled Trial | 隨機對照試驗 |

---

<!-- _class: abbr -->
# 縮寫對照表 (2/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| ACS / CCS | Acute / Chronic Coronary Syndrome | 急性 / 慢性冠心症 |
| PCI | Percutaneous Coronary Intervention | 經皮冠狀動脈介入術 |
| FFR | Fractional Flow Reserve | 血流儲備分數 |
| LVAD | Left Ventricular Assist Device | 左心室輔助裝置 |
| LAAC | Left Atrial Appendage Closure | 左心耳關閉術 |
| PFA | Pulsed-Field Ablation | 脈衝電場消融術 |
| AF | Atrial Fibrillation | 心房顫動 |
| DOAC | Direct Oral Anticoagulant | 直接口服抗凝劑 |
| LMCA | Left Main Coronary Artery | 左主幹冠狀動脈 |
| TEE | Transesophageal Echocardiography | 經食道超音波心臟圖 |
| LVEF | Left Ventricular Ejection Fraction | 左心室射出分率 |
| IE | Infective Endocarditis | 感染性心內膜炎 |
| TVT Registry | Transcatheter Valve Therapy Registry | 美國 TVT 登記資料庫 |
| VARC-3 | Valve Academic Research Consortium-3 | 瓣膜學術研究聯盟 v3 |
| HR / RR / OR / ARR | Hazard Ratio / Relative Risk / Odds Ratio / Absolute Risk Reduction | 風險比 / 相對風險 / 比值比 / 絕對風險降低 |
| GLP-1RA / GIP | Glucagon-Like Peptide-1 RA / Glucose-dependent Insulinotropic Polypeptide | GLP-1 受體促效劑 |
| NT-proBNP / hsCRP | N-Terminal Pro-BNP / High-Sensitivity C-Reactive Protein | 生物標記 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**
心臟內科｜結構性心臟病介入
