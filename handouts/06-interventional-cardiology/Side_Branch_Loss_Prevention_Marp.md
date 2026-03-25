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
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
footer: '謝慕揚 MD, PhD, FESC | Side Branch Loss Prevention | 2026'
---

<!-- _class: lead -->

# Preventing Side Branch Loss
# 預防 Bifurcation PCI 中的分支血管丟失

**謝慕揚 MD, PhD, FESC**
資料來源：EBC 15th-17th Consensus Documents | 2026-03-13
[17th EBC Consensus — EuroIntervention 2023](https://doi.org/10.4244/EIJ-D-23-00124)

---

# 大綱

1. 為什麼要討論這個主題
2. Side Branch Occlusion 的預測因子與 V-RESOLVE Score
3. SB 保護策略：Jailed Wire vs. Jailed Balloon
4. Provisional Stenting 步驟式流程
5. 搶救策略與錯誤防範
6. Take-Home Messages

---

<!-- _class: divider -->

# 第一部分：問題的嚴重性

---

# 為什麼要討論 Side Branch Loss？

- Side branch loss 是 bifurcation PCI 中**最常見且可預防**的嚴重併發症
- LAD-Diagonal bifurcation 是最常遇到的 bifurcation location
- Bifurcation lesions 佔所有 PCI 的 **15-20%**
- Side branch occlusion (SBO) 發生率：**5-20%**
- 正確的 wire management 和保護策略是介入醫師的**核心能力**

> **SBO = Periprocedural MI = 影響病人預後**

---

# SBO 的臨床後果

| 結果 | SBO 組 | 非 SBO 組 | P 值 |
|------|--------|----------|------|
| Procedural success | 82.9% | 94.7% | 0.007 |
| Periprocedural MI | 14.6% | 3.5% | 0.003 |
| In-hospital MACE | 17.1% | 5.3% | 0.007 |
| Unplanned two-stent | 24.8% | 6.0% | < 0.001 |

> **Pearl**：丟失一條有意義的 diagonal branch = 造成 periprocedural MI

---

<!-- _class: divider -->

# 第二部分：預測與評估

---

# SBO 的獨立預測因子

| 預測因子 | OR | P 值 |
|----------|-----|------|
| **MV/SB diameter ratio ↑** | 7.71 | 0.01 |
| **Bifurcation angle ↑** | 1.03/degree | < 0.01 |
| **SB diameter stenosis ≥ 50%** | 2.34 | < 0.001 |
| **Proximal MV stenosis ≥ 50%** | 2.34 | < 0.001 |
| **SB TIMI flow < 3** | 3.59 | < 0.01 |
| **Plaque ipsilateral to SB** | Significant | — |

> **Pearl**：True bifurcation + 高角度 + SB ostial disease = 最高風險組合

---

# OCT/IVUS 的額外預測價值

## OCT (ORBID Study)
- **Lipid-rich plaque**：SBO 組 100% vs. 64%
- **Lipid plaque contralateral to SB**：OR 8.14
- **Spotty calcification**：SBO 組 60% vs. 0%

## IVUS
- **MV plaque thickness at SB junction**
- **SB diameter ratio (media-to-media / intima-to-intima)**

> **Pearl**：Intravascular imaging 可以幫助預判 SBO 風險，但 V-RESOLVE score 不需要 imaging 即可評估

---

<!-- _class: small-text -->

# V-RESOLVE Score：術前快速評估（總分 0-43）

| 項目 | 參數 | 分類與計分 | 最高分 |
|------|------|-----------|--------|
| 1 | Plaque distribution | Opposite=0; **Ipsilateral=2** | 2 |
| 2 | MV TIMI flow (pre-stenting) | TIMI 3=0; **≤2=5** | 5 |
| 3 | Bifurcation core DS | <50%=0; 50-70%=4; **>70%=8** | 8 |
| 4 | Bifurcation angle | <70°=0; 70-90°=4; **>90°=6** | 6 |
| 5 | **MV/SB diameter ratio** | <1.15=0; 1.15-1.5=6; **>1.5=12** | **12** |
| 6 | SB DS (pre-stenting) | <50%=0; 50-70%=4; **>70%=10** | 10 |

| 分數 | 風險 | SBO 率 |
|------|------|--------|
| 0-3 | 低 | 1.5% |
| 4-7 | 中低 | 4.8% |
| 8-11 | 中高 | 7.2% |
| **≥12** | **高** | **16.7%** |

**≥12 分 → 必須使用 Jailed Balloon Technique**

---

<!-- _class: divider -->

# 第三部分：Side Branch 保護策略

---

# 三個層級的 SB 保護

```text
Level 1: Jailed Wire Technique (JWT)
    └── SB 內放一條 guidewire → 標記 + 維持 access

Level 2: Jailed Balloon Technique (JBT)
    └── SB 內放未充氣 balloon → 阻擋 plaque shift + 可充氣搶救

Level 3: Upfront Two-Stent Strategy
    └── DK Crush / Culotte / TAP → 真正大 SB + 嚴重 ostial disease
```

> **原則**：根據 V-RESOLVE score 選擇策略層級

---

# Jailed Wire Technique (JWT)

## 操作方式
- SB 放入 workhorse guidewire
- MV stent 部署 → wire 被 jailed 在 stent struts 下

## 功能
- 維持 SB access「路標」
- 輕微改變 SB takeoff angle
- 標記 SB ostium 位置

## 限制
- Wire 佔空間小 → **無法阻擋 plaque/carina shift**
- SBO rate 仍約 **19.9%** (in high-risk lesions)

---

# Jailed Balloon Technique (JBT)

## 操作方式
- SB 放入 semi-compliant balloon（**直徑 = MV stent / 2，且 ≤ SB 直徑**）
- Balloon 未充氣，MV stent 部署時被 jailed

## 功能
- **佔據 SB ostium 空間** → 阻擋 plaque + carina shift
- SB flow 正常 → 未充氣撤出
- SB flow 受損 → **原地充氣搶救**

## 結果 (CIT-RESOLVE Trial)
- SBO rate：JWT **19.9%** vs. JBT **9.1%** (P = 0.02)
- Periprocedural MI：JWT 14.9% vs. JBT 7% (P = 0.03)

---

# CIT-RESOLVE Trial：JBT vs. JWT

| 結果 | JBT (n=143) | JWT (n=141) | P 值 |
|------|------------|------------|------|
| **SB occlusion** | **9.1%** | **19.9%** | **0.02** |
| Periprocedural MI | 7% | 14.9% | 0.03 |
| 1-yr cardiac death | 0.7% | 0.7% | 1.0 |
| 1-yr MACE | 8.4% | 10.6% | 0.52 |

> **Pearl**：高風險病灶 (V-RESOLVE ≥ 12) 應使用 JBT，可將 SBO 率降低一半

---

<!-- _class: divider -->

# 第四部分：Provisional Stenting 流程

---

# Step-by-Step Provisional Stenting

```text
Step 1: Wire Both Branches
    ├── Wire MV → Wire SB
    └── ⚠️ 永遠先確保 SB wire 在位

Step 2: Pre-dilation (if needed)
    └── 觀察 SB flow 變化

Step 3: Deploy MV Stent
    └── Jailed wire 或 jailed balloon 在 SB

Step 4: POT (Proximal Optimization Technique) ← 關鍵！
    └── NC balloon sized to proximal MV reference

Step 5: Evaluate SB Flow
    ├── TIMI 3 → 觀察
    └── Compromised → Rewire + KBI

Step 6: Re-POT
    └── KBI 後必須做 re-POT
```

---

# POT：Bifurcation PCI 成功的關鍵

## 什麼是 POT？
- **Proximal Optimization Technique**
- NC balloon 尺寸 = proximal MV reference diameter
- 充氣位置：stent 近端到 carina 之間

## 為什麼重要？
- 確保 proximal stent 完全 apposed
- **打開 SB 對側的 stent struts** → 利於 rewire
- 預防 proximal stent malapposition
- 改善 SB access

> **Pearl**：每次 MV stenting 後都必須做 POT — 這是最容易被忽略但最重要的步驟

---

<!-- _class: divider -->

# 第五部分：錯誤防範

---

# 常見致命錯誤

| 錯誤 | 後果 | 預防 |
|------|------|------|
| 未 wire SB 就 stent MV | SB 完全喪失 access | **永遠先 wire 兩條血管** |
| **拔掉 SB 唯一的 wire** | **無法 rewire = SB 永久丟失** | **確認不需要前永遠保持 wire** |
| 未做 POT | SB access 困難 | **每次 MV stenting 後都做 POT** |
| 忽略 SB ostial disease | 高風險 SBO | **V-RESOLVE 評估** |
| KBI 後未做 re-POT | Proximal distortion | **KBI 後一定 re-POT** |

---

# 高風險情境 Checklist

- True bifurcation lesion (Medina x,x,1)？
- Bifurcation angle > 70°？
- SB diameter ≥ 2.0 mm？
- SB ostial stenosis ≥ 50%？
- MV/SB diameter ratio > 1.5？
- Plaque ipsilateral to SB？
- **V-RESOLVE score ≥ 12？**

> **≥ 3 項 → 使用 Jailed Balloon Technique 或考慮 Upfront Two-Stent Strategy**

---

# SB Rewiring：Guidewire 選擇（第一線）

## Hydrophilic Polymer-Jacketed Wire

| Wire | Tip Load | Tip | 特性 |
|------|----------|-----|------|
| **Fielder FC** | **0.8 gf** | 0.014" | **首選**。滑順、torque 佳 |
| **Fielder XT-A** | **1.0 gf** | 0.010"/0.014" tapered | FC 失敗後升級。Tapered tip 增加穿透力 |
| **SION Black** | **0.8 gf** | 0.014" polymer | Torque 極佳、低摩擦。操控手感不同 |

> **Pearl**：Fielder FC 首選 → 失敗換 Fielder XT-A → 再換 SION Black

---

# SB Rewiring：CTO Wire（最後手段）

## ⚠️ CTO Wire 的使用需極度謹慎

| Wire | Tip Load | Tip | 建議 |
|------|----------|-----|------|
| **UB3** | **3.0 gf** | 0.014" | CTO wire 首選 |
| **Gaia 1st** | **1.7 gf** | 0.010"/0.014" tapered | 較安全的選項 |
| **Gaia 2nd** | **3.5 gf** | 0.011"/0.014" tapered | 必要時使用 |
| ~~Gaia 3rd~~ | ~~4.5 gf~~ | ~~0.012"/0.014"~~ | **不建議使用** |

> **Pearl**：CTO wire tip load 是 Fielder FC 的 2-5 倍，極易造成 **SB dissection**。一旦 dissection，搶救非常困難。**絕對不用 Gaia 3rd (4.5 gf)**。

---

# Wire 升級流程與搶救策略

```text
Wire 升級策略：
  Fielder FC (0.8 gf) → Fielder XT-A (1.0 gf) → SION Black (0.8 gf)
      |── 全部失敗
      v
  ⚠️ CTO Wire: UB3 (3.0) / Gaia 1st (1.7) / Gaia 2nd (3.5)
      └── ❌ 不用 Gaia 3rd (4.5 gf)

搶救流程：
  Step 1: POT (打開 strut access)
  Step 2: Rewire (Fielder FC → XT-A → SION Black)
  Step 3: Micro-catheter 輔助 (FineCross, Twin-Pass Torque)
  Step 4: CTO Wire — 最後手段，注意 dissection 風險
```

> **預防永遠勝於搶救。不可拔掉 SB 中唯一的 wire。**

---

# Take-Home Messages

1. **永遠 wire 兩條血管** — MV 和 SB 都要有 wire
2. **永遠不要拔掉 SB 唯一的 wire** — 除非確認 SB flow 正常且不再需要 access
3. **術前用 V-RESOLVE score 評估風險** — ≥ 12 分用 jailed balloon
4. **每次 MV stenting 後都做 POT** — 這是 bifurcation PCI 成功的關鍵
5. **KBI 後必須 re-POT** — 矯正 proximal stent distortion
6. **Jailed Balloon > Jailed Wire** — 高風險病灶 SBO 從 20% 降到 9%

---

<!-- _class: small-text -->

# 參考文獻

1. Pan M, et al. 17th EBC consensus – SB preservation techniques. [*EuroIntervention*. 2023;19(1):26-36.](https://doi.org/10.4244/EIJ-D-23-00124)
2. Burzotta F, et al. 15th EBC consensus. [*EuroIntervention*. 2021;16(16):1307-1317.](https://doi.org/10.4244/EIJ-D-20-00169)
3. Albiero R, et al. 16th EBC consensus – provisional stenting. [*EuroIntervention*. 2022;18(5):e362-e376.](https://doi.org/10.4244/EIJ-D-22-00165)
4. Zhang D, et al. Predictors of SB occlusion. [*Chin Med J*. 2015;128(11):1471-8.](https://doi.org/10.4103/0366-6999.157654)
5. Zhang D, et al. JBT vs JWT: CIT-RESOLVE. [*Front Cardiovasc Med*. 2022;9:814873.](https://doi.org/10.3389/fcvm.2022.814873)
6. Kini AS, et al. OCT predictors (ORBID). [*Catheter Cardiovasc Interv*. 2017;89(2):259-268.](https://doi.org/10.1002/ccd.26524)
7. Wu X, et al. LAD bifurcation SBO & V-RESOLVE. [*Front Cardiovasc Med*. 2025;12:1648244.](https://doi.org/10.3389/fcvm.2025.1648244)

---

# 教學資源

- **Dr. Emmanouil Brilakis** YouTube: @manosbrilakis — Complex PCI 教學
- **Medtronic Academy** — [Bifurcation PCI](https://www.medtronicacademy.com/en-us/content/bifurcation-pci)
- **European Bifurcation Club** — [bifurc.eu](https://bifurc.eu)
- **IntechOpen** — [Step-by-step Bifurcation PCI](https://www.intechopen.com/chapters/1215749)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*記住：永遠不要拔掉 Side Branch 的 Wire！*

*本文件僅供醫療專業人員教學參考*
