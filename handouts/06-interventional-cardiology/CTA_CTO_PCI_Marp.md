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
footer: '謝慕揚 MD, PhD, FESC | CTA-Guided CTO PCI | 2026'
---

<!-- _class: lead -->

# Coronary CTA in CTO PCI
## CTA 導引慢性完全阻塞介入治療

**謝慕揚 MD, PhD, FESC**
資料來源：JACC Cardiovasc Interv 2026;19(1):1-14 | 2026-03-03
[Original Article (Kumar S, et al.)](https://doi.org/10.1016/j.jcin.2025.10.055)

---

# 大綱

1. 為什麼 CTO PCI 需要 CTA？
2. CTA 評估 CTO 的七大要素
3. CTA-Based Scoring Systems
4. RCT 證據：CTA 提升成功率
5. 即時融合導引與 AI 未來
6. 臨床實務建議

---

<!-- _class: divider -->

# 第一部分：CTA vs Angiography

---

# 為什麼 CTO PCI 需要 CTA？

- CTO 佔 coronary angiography 病灶 **15-25%**
- 傳統 angiography **僅提供 2D 投影**，無法看到阻塞段內部
- Angiography 常**低估**：
  - 阻塞段長度
  - 鈣化程度
  - Cap 形態
  - Side branch 位置

> **Key Point**：CTA 提供 3D 解剖資訊，可全面評估 angiography 盲區

---

# CTA vs Angiography 比較

| 評估項目 | Angiography | CTA |
|----------|-------------|-----|
| 阻塞段長度 | 常低估 | **精確測量** (curved MPR) |
| Proximal cap | 2D 投影，常有 ambiguity | **3D 評估** tapered vs blunt |
| Calcification | 低估程度 | **定量分析** (% CSA) |
| 血管走向 | 看不到阻塞段 | **完整 3D 路徑** |
| 遠端血管 | 依賴 collateral 顯影 | **直接評估** landing zone |
| 側枝路徑 | 有限 | 可視化 collaterals |

---

<!-- _class: divider -->

# 第二部分：CTA 評估七大要素

---

# 1. Proximal Cap Morphology

- **Tapered stump** → 有利 antegrade wiring
- **Blunt stump** → 更困難，常需 retrograde approach

## 2. Proximal Cap Ambiguity

- PROGRESS-CTO：CTA 解決 **27%** proximal cap ambiguity
- CTA/fluoroscopy fusion 解決 **63%** ambiguity

> **Pearl**：Cap 形態是決定 wiring 策略的第一步

---

# 3. Occlusion Length & 4. Calcification

### Occlusion Length
- Curved MPR 精確測量
- Length ≥ 9 mm → 100% specific for total occlusion
- CTA 在 **10%** 案例中改變長度估計 > 5 mm

### Calcification
- **Severe**：≥ 50% vessel cross-sectional area
- CTA 在 **18%** 案例中發現 angiography 未見鈣化
- 影響是否需要 rotational atherectomy

---

# 5-7. Vessel Course, Landing Zone, Collaterals

### 5. Vessel Course & Tortuosity
- **Bending > 45°** = 重要困難度預測因子
- Angiography 完全無法看到阻塞段走向

### 6. Distal Landing Zone
- CTA 辨識遠端血管：**68%** vs angiography **18%**
- 評估 stenosis、diameter、stent 長度

### 7. Collateral Circulation
- 評估 septal vs epicardial collaterals
- **Septal** 為 retrograde 首選（低 tamponade 風險）

---

<!-- _class: divider -->

# 第三部分：CTA Scoring Systems

---

# CT-RECTOR Score (2015)

**Opolski MP, et al.** JACC Cardiovasc Interv 2015 | n = 240

每項 1 分：Multiple occlusions, Blunt stump, Severe calcification, Bending, Duration ≥ 12 mo, Previous failed PCI

| 分級 | 分數 | 成功率 (GW ≤ 30 min) |
|------|------|---------------------|
| Easy | 0 | **95%** |
| Intermediate | 1 | **88%** |
| Difficult | 2 | **57%** |
| Very Difficult | ≥ 3 | **22%** |

**AUC = 0.83** vs J-CTO 0.71 (p < 0.001)

---

# KCCT Score (2017)

**Yu CW, et al.** Circ Cardiovasc Imaging 2017 | n = 684

8 項：Blunt entry, Proximal side branch, Bending, Length ≥ 15 mm, Severe calcification, Whole luminal calcification, Reattempt, Duration ≥ 12 mo

| KCCT Score | GW ≤ 30 min | Procedural Success |
|------------|-------------|-------------------|
| 0 | **100%** | **100%** |
| 1-2 | 84% | 94-100% |
| 3 | 51% | 84% |
| ≥ 4 | 30% | 62% |

**C-statistic = 0.78** vs J-CTO 0.65 (p < 0.001)

---

# CTA Scores 比較總覽

| Score | Year | N | Items | AUC | Endpoint |
|-------|------|---|-------|-----|----------|
| **CT-RECTOR** | 2015 | 240 | 6 | **0.83** | GW ≤ 30 min |
| **KCCT** | 2017 | 684 | 8 | **0.78** | GW + success |
| **RECHARGE** | 2021 | 131 | 6 | **0.72** | Procedural success |
| J-CTO (傳統) | 2011 | 494 | 5 | 0.65-0.71 | GW ≤ 30 min |

> **Pearl**：所有 CTA scores 均優於傳統 J-CTO score

---

<!-- _class: divider -->

# 第四部分：RCT 證據

---

# CTA-Guided CTO PCI — RCT (2021)

**Hong SJ, Kim BK, et al.** JACC Cardiovasc Imaging 2021

- **多中心 RCT**，韓國，10 位操作者
- **400 位 CTO 患者** → 1:1 隨機分配
- CTA-guided (n=200) vs Angiography-only (n=200)

| 結果 | CTA-guided | Angio-only | P 值 |
|------|-----------|------------|------|
| **Technical success** | **93.5%** | **84.0%** | **0.003** |
| Coronary perforation | 1% | 4% | 0.055 |
| Periprocedural MI | 0% | 2% | 0.123 |

**Absolute benefit: +9.5%** (95% CI: 3.4-15.6%)

---

# RCT 次族群分析

- **J-CTO ≥ 2 的高難度 CTO 獲益最大** (p-interaction = 0.035)
- Procedure time：兩組**無顯著差異**
- Fluoroscopy time：兩組無差異
- Contrast volume：兩組無差異
- 一年追蹤：cardiac death, TVR, MI 均無差異

> **Pearl**：CTA 導引提升成功率 ~10%，**不增加手術時間或 contrast 用量**
> 特別在 high-complexity CTO 獲益最顯著

---

<!-- _class: divider -->

# 第五部分：Fusion 導引與 AI

---

# CTA/Fluoroscopy 即時融合

**系統**：syngo CTO Guidance (Siemens)

```text
Pre-procedural CTA → 載入心導管室
    → 自動辨識冠狀動脈 centerline
    → 對齊 C-arm 座標系統
    → 即時疊加至 live fluoroscopy
    → 隨 C-arm 角度同步旋轉
```

| 應用場景 | 比例 |
|----------|------|
| Proximal cap ambiguity resolution | **63%** |
| Intra-CTO wire guidance | **56%** |
| Re-entry guidance | 15% |

---

# AI 與未來方向

### AI-QCT 自動分析
- Automated CTO detection：**82%** 準確率
- 處理時間：**116 sec** (人工 472 sec，快 75%)

### FFRCT 整合
- Virtual PCI modeling → 預測 post-PCI FFR
- 評估 tandem lesion interaction

### 未來展望
- **P4 Study**：全球 RCT (CTA-guided vs IVUS-guided PCI)
- Deep learning 策略預測
- 即時 AI 導引整合至 fluoroscopy

---

<!-- _class: divider -->

# 第六部分：臨床實務建議

---

# 何時安排 Pre-procedural CTA？

### 常規建議
- Proximal cap ambiguity
- 預期高難度 (J-CTO ≥ 2)
- 嚴重鈣化或鈣化不確定
- 考慮 retrograde approach
- Re-attempt（前次失敗）

### CTA 技術要求
- ECG-gated acquisition
- Thin-slice reconstruction (≤ 0.6 mm)
- 建議術前 **≤ 2 週**內取得

> **Pearl**：2024 ESC Guidelines 已正式承認 virtual PCI (CTA + FFRCT) 的新興角色

---

# CTA 評估 Checklist

| 評估項目 | 確認事項 |
|----------|---------|
| **Proximal cap** | Tapered or blunt? Side branch? |
| **Occlusion length** | Curved MPR 測量 (mm) |
| **Calcification** | % CSA? Whole luminal? |
| **Vessel course** | Bending > 45°? |
| **Distal vessel** | Landing zone quality? Diameter? |
| **Collaterals** | Septal or epicardial? Retrograde feasible? |
| **Scoring** | CT-RECTOR / KCCT score |

---

# Take-Home Messages

1. **CTA 顯著提升 CTO PCI 成功率** (RCT: 93.5% vs 84.0%)
2. **高難度 CTO 獲益最大** (J-CTO ≥ 2)
3. **CTA 發現 angiography 遺漏的關鍵資訊**
   - 27% cap ambiguity、18% hidden calcification、10% length change
4. **CTA-based scores 優於 J-CTO**
   - CT-RECTOR AUC 0.83 vs J-CTO 0.71
5. **不增加手術時間或 contrast 用量**
6. **趨勢：AI 整合 + virtual PCI planning**

---

<!-- _class: small-text -->

# 參考文獻

1. Kumar S, et al. The Role of CTA in CTO PCI. [*JACC Cardiovasc Interv.* 2026;19(1):1-14.](https://doi.org/10.1016/j.jcin.2025.10.055)
2. Hong SJ, Kim BK, et al. Effect of Coronary CTA on CTO PCI: A Randomized Trial. [*JACC Cardiovasc Imaging.* 2021;14(10):1993-2004.](https://doi.org/10.1016/j.jcmg.2021.04.013)
3. Opolski MP, et al. CT-RECTOR Score. [*JACC Cardiovasc Interv.* 2015;8(2):257-267.](https://doi.org/10.1016/j.jcin.2014.07.031)
4. Yu CW, et al. KCCT Score. [*Circ Cardiovasc Imaging.* 2017;10(7):e005800.](https://doi.org/10.1161/CIRCIMAGING.116.005800)
5. Kumar S, et al. PROGRESS-CTO Registry. [*Int J Cardiol.* 2022;367:60-65.](https://pubmed.ncbi.nlm.nih.gov/35964847/)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
