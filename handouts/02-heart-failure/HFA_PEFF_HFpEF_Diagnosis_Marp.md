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
  section.lead a { color: #8ecae6; }
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
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.68em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.85em;
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
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.8em; }
footer: '謝慕揚 MD, PhD, FESC | HFA–PEFF HFpEF Diagnosis | 2019 ESC HFA'
---

<!-- _class: lead -->

# How to Diagnose HFpEF

## HFA–PEFF 診斷演算法（ESC 心衰竭學會共識）

**謝慕揚 MD, PhD, FESC**
資料來源：*Eur Heart J*. 2019;40(40):3297-3317 | Pieske B, et al.
[原文連結 https://doi.org/10.1093/eurheartj/ehz641](https://doi.org/10.1093/eurheartj/ehz641)

---

# 大綱

1. 為何需要新的診斷演算法
2. 四步驟總覽 P → E → F1 → F2
3. Step 1 (P)：Pre-test assessment
4. Step 2 (E)：HFA–PEFF Score 三領域
5. Score 計分與判讀
6. Step 3 (F1)：Functional testing
7. Step 4 (F2)：病因與鑑別診斷
8. 限制與臨床要點

---

<!-- _class: divider -->

# 第一部分：背景與總覽

---

# 為何需要新的診斷建議

- ≥60 歲族群 **4.9%** 罹患 HFpEF；佔 HF 住院一半以上，且持續增加
- 舊準則的 echo cut-off、共病、biomarker、侵入性/運動測試定位**彼此不一致**
- 非侵入性參數常落在**非診斷性中間區間** → 單一參數不足以診斷
- **新演算法特色**：

| 特色 | 內容 |
|------|------|
| 單一入口 | 只有一個 entry point，所有病人皆可分類 |
| 逐步式 | 從初始臨床評估到專科檢查 |
| 分數整合 | 整合互補領域參數，給出診斷「機率」 |
| 最終仲裁 | 不明確時以侵入性血流動力學/運動負荷確認 |

---

# 四步驟總覽：P → E → F1 → F2

```text
Step 1 (P) Pre-test assessment ── 門診：症狀/風險因子/ECG/lab/NP/標準 echo
        │  懷疑 HFpEF（LVEF 正常、無瓣膜病/缺血、≥1 風險因子）
        ▼
Step 2 (E) Echo + NP Score ────── 三領域計分（Major=2 / Minor=1）
        │
        ├─ ≥5 分 ──────────────► 確診 HFpEF
        ├─ 2–4 分 ─┐
        └─ ≤1 分 ──┼──────────► HFpEF 不太可能 → 找其他病因
                   ▼
Step 3 (F1) Functional testing ── 運動 echo / 侵入性血流動力學
        │  合計 ≥5 分 → 確診
        ▼
Step 4 (F2) Final aetiology ────── 找特定病因（amyloid、缺血、浸潤…）
```

---

<!-- _class: divider -->

# 第二部分：Step 1 (P) 前測評估

---

# Step 1 (P)：Pre-test assessment

| 項目 | 重點 |
|------|------|
| 病史/人口學 | 運動性呼吸困難敏感但特異性僅約 50%；老年、肥胖、失能可為非心因性 |
| ECG | 診斷價值低；**最重要是偵測 AF**（高度預測 HFpEF） |
| 實驗室 | eGFR、肝功能、HbA1c、TSH、CBC、ferritin、TSAT（貧血加重症狀） |
| NP（低 cut-off） | NT-proBNP ≥125 或 BNP ≥35 pg/mL（敏感指標） |
| 標準 echo | 測量 LVEF（cut-point **≥50%**）；排除 HFrEF/瓣膜病/肺高壓/心包積液 |

> **Pearl（NP 陷阱）**：正常 NP **不能排除** HFpEF。高達 **20%** 侵入性證實的 HFpEF，NP 低於閾值（尤其肥胖）；LVH 使壁應力正常化、AF 本身抬高 NP。

---

# Table 1：支持 HFpEF 的風險因子

- 高齡（男性 ≥70 歲；女性亦然）
- 過重／肥胖
- 代謝症候群／糖尿病
- 身體活動不足／失能 (deconditioning)
- 動脈高血壓
- **心房顫動 (AF)**
- ECG 異常（AF 以外）
- Natriuretic peptide 升高（BNP ≥35 或 NT-proBNP ≥125 pg/mL）

> 在無明顯非心因性呼吸困難下，LVEF 正常、無瓣膜病/缺血、且 ≥1 風險因子 → **懷疑 HFpEF**，進 Step 2。

---

<!-- _class: divider -->

# 第三部分：Step 2 (E) HFA–PEFF Score

---

# Functional Domain 功能領域

| 參數 | Major (2 分) | Minor (1 分) |
|------|-------------|-------------|
| **e′** | septal <7 或 lateral <10 cm/s（<75 歲）<br>septal <5 或 lateral <7 cm/s（≥75 歲） | — |
| **平均 E/e′** | ≥15 | 9–14 |
| **TR velocity / PASP** | TR >2.8 m/s 或 PASP >35 mmHg | — |
| **LV GLS** | — | <16% |

- e′ 反映 LV relaxation，隨年齡下降 → **年齡分層**
- E/e′ 反映 mPCWP，受 LVH 影響，不可作唯一指標
- PASP 升高 + RV 功能下降 = HFpEF 死亡重要預測因子

---

# Morphological Domain 形態領域

| 參數 | Major (2 分) | Minor (1 分) |
|------|-------------|-------------|
| **LAVI** | >34 mL/m²（SR）<br>>40 mL/m²（AF） | 29–34（SR）<br>34–40（AF） |
| **LVMI + RWT** | LVMI ≥149（男）/ ≥122（女）g/m² **且** RWT >0.42 | LVMI ≥115（男）/ ≥95（女）g/m²<br>**或** RWT >0.42<br>**或** wall thickness ≥12 mm |

- LAVI 是 LV 充填壓間接指標；AF 本身使 LA 擴大 → **SR/AF 分開 cut-off**
- **LVH 不存在不能排除 HFpEF**
- 無法測 LAVI/LVMI/壁厚時 → 改用 **CMR**

---

# Biomarker Domain 生物標記領域

| 節律 | Major (2 分) | Minor (1 分) |
|------|-------------|-------------|
| **Sinus rhythm** | NT-proBNP >220 或 BNP >80 pg/mL | NT-proBNP 125–220 或 BNP 35–80 pg/mL |
| **Atrial fibrillation** | NT-proBNP >660 或 BNP >240 pg/mL | NT-proBNP 375–660 或 BNP 105–240 pg/mL |

- Step 2 採比 Step 1 更**高 cut-off**（提高特異性），並依 SR/AF 分層
- AF 病人 NP 平均約 SR 的 **3 倍** → AF cut-off = SR 三倍

---

# HFA–PEFF Score 計分規則

```text
三大領域：Functional / Morphological / Biomarker
  ├─ 每領域：任一 Major 陽性 → 2 分
  │          無 Major、有 Minor → 1 分
  ├─ 同領域內 Major/Minor「不相加」（多個 major 仍算 2 分）
  └─ 只在「不同領域之間」相加  →  總分 0–6

   ≥5 分  → 確診 HFpEF
   2–4 分 → 診斷不確定 → Step 3 (F1)
   ≤1 分  → HFpEF 不太可能 → 找其他病因
```

> **範例**：Functional 2 major + 1 minor 仍算 **2 分**；再加 Morphological minor（1 分）+ Biomarker major（2 分）= **5 分 → 確診**。不需每參數都取得即可計分。

---

<!-- _class: divider -->

# 第四部分：Step 3 (F1) 功能性檢測

---

# Diastolic Stress Test（運動 echo）

- 適用 Step 2 分數 **2–4 分**；異常常僅於**運動時**顯現
- semi-supine bicycle，量測峰值運動的 **E/e′** 與 **TR velocity**

| 運動 echo 發現 | 加分 |
|------|------|
| 峰值 平均 **E/e′ ≥15** | Step 2 分數 **+2 分** |
| **E/e′ ≥15 且 TR velocity >3.4 m/s** | **+3 分** |
| Step 2 + Step 3 合計 **≥5 分** | **確診 HFpEF** |

> 單獨 TR velocity 上升**不可**診斷（可能只是正常高動力反應）。限制：10–20% 峰值運動 E/e′ 測不到、TR velocity 僅約 50% 可測、約 20% 對照組偽陽性。

---

# Invasive Haemodynamic Stress Test

| 情境 | 閾值 | 意義 |
|------|------|------|
| 靜態充填壓升高 | LVEDP **≥16** 或 PCWP **≥15 mmHg** | 直接**確診** |
| 靜態正常、運動時 | 峰值運動 PCWP **≥25 mmHg** | 分類為 HFpEF（<25 為非心因性） |
| LV relaxation | tau >48 ms | 支持 HFpEF |

- 正常靜態 LVEDP/mPCWP **不能排除** HFpEF（代償期僅運動顯現）
- **預後**（10 年死亡率）：靜態低+運動低 mPCWP 6.6%；靜態低+運動高 28.2%；靜態高+運動高 **35.2%**
- 侵入性血流動力學被視為診斷 HFpEF 的**臨床參考標準**

---

<!-- _class: divider -->

# 第五部分：Step 4 (F2) 病因追查

---

# 特定心肌病因（Table 2 節錄）

| 類別 | 代表病因 |
|------|---------|
| 缺血性 | MI scar、stunning、epicardial CAD、微血管/內皮功能障礙 |
| 浸潤性 | **Amyloidosis**、sarcoidosis、haemochromatosis、Fabry/Danon/Pompe |
| 發炎/免疫 | 心肌炎（病毒、HIV、Chagas）、RA/SLE/scleroderma、嗜酸性球心肌炎 |
| 基因性 | HCM、restrictive CM、non-compaction、肌萎縮症早期 |
| 毒性 | 酒精、古柯鹼、anabolic steroids、重金屬、anthracyclines、trastuzumab、放射線 >3 Gy |
| 代謝/內分泌 | 甲狀腺、acromegaly、Cushing、營養缺乏（thiamine/carnitine/selenium） |

> 檢查工具：ergometry（缺血、chronotropic incompetence 33–77%）、**CMR**（LGE/T1-mapping/ECV）、DPD scintigraphy（amyloid）、心肌切片、基因檢查。

---

# 應排除的 HFpEF Masqueraders

> **重點**：以下造成 LVEF 正常之 HF 樣症狀，但**不屬於 HFpEF 症候群**：
>
> - **Constrictive pericarditis（縮窄性心包炎）**、心包積液
> - **原發性瓣膜性心臟病**、mitral stenosis
> - **High-output failure**（嚴重貧血、敗血症、甲狀腺毒症、AV 瘻管、妊娠）
> - 顯著 **CAD** 導致的 HF 樣症狀
> - 心律問題（arrhythmia、pacing、傳導障礙）

---

# 限制與未解問題

- **化約為單一診斷**：HFpEF 為多因子症候群，未來應細分亞群
- **Early HFpEF**（約 45%）：靜態充填壓正常、僅運動時升高；LAVI 較小、診斷力弱 → LA strain 可能更佳
- **LVEF 角色受限**：除排除 HFrEF 外幾無診斷角色
- **運動測試無共識**：負荷方案與關鍵量測未定；6MWT vs. CPET 未明
- **HFpEF 與 AF 高度重疊**：SR/AF 分層閾值仍需前瞻驗證
- **未來**：machine learning + 分子表型化整合多維資料

---

# 臨床要點總結

> **1. 四步驟、單一入口、全數可分類**：P → E → F1 → F2

> **2. Score 核心**：三領域，Major=2 / Minor=1；同領域不相加、跨領域才加；**≥5 確診、≤1 不太可能、2–4 需 functional testing**

> **3. 不靠單一參數**：正常 NP 不排除 HFpEF（尤其肥胖）

> **4. 中間分數靠負荷測試仲裁**：運動 echo（E/e′≥15 +2；+TR>3.4 → +3）；侵入性（靜態 PCWP≥15/LVEDP≥16；運動 PCWP≥25）

> **5. 確診後務必追病因**：amyloid/缺血/浸潤；排除 constrictive、瓣膜、high-output

---

<!-- _class: small-text -->

# 參考文獻

1. Pieske B, Tschöpe C, de Boer RA, et al. How to diagnose heart failure with preserved ejection fraction: the HFA–PEFF diagnostic algorithm. *Eur Heart J*. 2019;40(40):3297-3317. https://doi.org/10.1093/eurheartj/ehz641 ｜ PMID 31504452
2. Ponikowski P, et al. 2016 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. *Eur Heart J*. 2016;37(27):2129-2200.
3. Paulus WJ, Tschöpe C, et al. How to diagnose diastolic heart failure (HFnEF consensus). *Eur Heart J*. 2007;28(20):2539-2550.
4. Reddy YNV, Carter RE, Obokata M, Redfield MM, Borlaug BA. A simple, evidence-based approach (H2FPEF score). *Circulation*. 2018;138(9):861-870.

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
