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
  section.lead { background-color: #1a2740; color: #ffffff; }
  section.lead h1 { color: #ffffff; font-size: 2.2em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #b0c4de; }
  section.divider { background-color: #0072bc; color: white; display: flex; justify-content: center; align-items: center; }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.5em; text-align: center; }
  section.divider h2 { color: #ffe169; }
  section.divider h3 { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.72em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote { border-left: 4px solid #ba181b; background-color: #fff5f5; padding: 0.5em 1em; font-size: 0.88em; }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.68em; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
footer: '謝慕揚 MD, PhD, FESC | Acute Heart Failure Management | 2026'
---

<!-- _class: lead -->
# 急性心衰竭的當代處置
## 從急診到長期緩解 — JACC State-of-the-Art Review
**整理：謝慕揚 MD, PhD, FESC**
2026-06-26
[原文連結 — J Am Coll Cardiol (DOI: 10.1016/j.jacc.2026.03.029)](https://doi.org/10.1016/j.jacc.2026.03.029)

---

# 核心觀念轉變

- 急性心衰竭 (Acute Heart Failure, AHF) 影響已開發國家約 **1–2% 的成人**
- 一次住院 = **疾病修飾的轉折點 (disease-modifying inflection point)**
- 從「以症狀為導向的去充血」→「以疾病修飾治療為核心」
- 整合指引：2021 ESC HF、2023 ESC focused update、2022 AHA/ACC/HFSA、2024 ACC consensus

> 目標不只是脫離急性鬱血，而是達成心衰竭緩解 (HF remission) / 恢復 (recovery)

---

<!-- _class: divider -->
# Part 1
## 初始評估與利鈉胜肽

---

# 初始評估：SPLASH 助記符

| 字母 | 英文 | 中文重點 |
|------|------|----------|
| **S** | Symptoms | 症狀（呼吸困難、端坐呼吸、水腫） |
| **P** | Past medical history | 過去病史 |
| **L** | Life signs | 生命徵象（BP、HR、SpO₂） |
| **A** | Assessment of congestion | 鬱血評估（理學、肺超音波） |
| **S** | STEMI exclusion | 排除 STEMI 或等效情況 |
| **H** | Hypoperfusion | 低灌流（冰冷、意識、乳酸、尿量） |

---

# 利鈉胜肽 (NP) 判讀

## 高陰性預測值 (high NPV) — 適合 rule-out

| 判讀 | BNP | NT-proBNP |
|------|-----|-----------|
| **排除** | < 100 ng/L | < 300 ng/L |
| **支持診斷** | > 400 ng/L | 年齡校正 (<50: >450; 50–75: >900; >75: >1800) |
| **灰色地帶** | 介於兩者 | 介於兩者 → TTE ± 肺超音波 + 抽血 |

> **hs-cTn** 在 AHF 常因 wall stress 升高 → 以**動態變化 + 缺血證據**判讀，**不自動診斷 MI**

---

<!-- _class: divider -->
# Part 2
## 早期治療與利尿劑策略

---

# 立即啟動 IV 環利尿劑

## 不必等待確認性檢查

| 情境 | Furosemide 起始劑量 |
|------|---------------------|
| 利尿劑未使用 / 口服低劑量 | 40 mg IV |
| 已用較高維持劑量 | ≥ 80 mg IV 或口服劑量 ×2 |

- 氧氣 ± 非侵襲性通氣 (NIV)：當 SpO₂ < 90%

> 利尿劑只治症狀（鬱血）；改變鈉貪婪 (sodium avidity) 的根本要靠 GDMT

---

# 利尿反應評估（給藥後 2 小時）

| 良好反應（任一） | 數值 |
|------------------|------|
| 尿量 | ≥ 300 mL / 2 h |
| 尿鈉 (urine Na) | ≥ 70 mmol/L |

**反應不足升階：**

```text
反應不足
  → 環利尿劑加倍 (單次上限 250 mg；每日 500–600 mg，腎損可至 1000 mg)
  → 加第二種利尿劑 (acetazolamide / thiazide)
  → 尖峰早、6–8 h 回基準 → 一天 3–4 次或持續輸注
```

---

# 血管擴張劑與頑固性阻抗

## IV 血管擴張劑（當 SBP > 110 mm Hg）

| 藥物 | 劑量範圍 |
|------|----------|
| Nitroprusside | 0.3 → 最高 5 µg/kg/min |
| Nitroglycerin | 10–20 → 最高 200 µg/min |

- **頑固性利尿劑阻抗** → 超過濾 (ultrafiltration, UF)

---

<!-- _class: divider -->
# Part 3
## GDMT 四大支柱

---

# 四大支柱（不分 LVEF 皆有益）

| 支柱 | 代表藥物 | 啟動時機 |
|------|----------|----------|
| **ARNI** | sacubitril/valsartan（無則 RASI） | 穩定後、輕度高血容/等容 |
| **β 阻斷劑 (BB)** | carvedilol / metoprolol succinate / bisoprolol | 鬱血改善後；已用且穩定則續 |
| **MRA** | spironolactone / eplerenone | **早期（前幾天）** |
| **SGLT2i** | dapagliflozin / empagliflozin | **早期，可在知 LVEF 前** |

> SGLT2i + MRA 最早啟動，不需等 LVEF 結果

---

# GDMT 啟動順序與細節

- **De novo HFrEF**：BB 在鬱血改善後；心搏過速/缺血為誘因 → 更早給 BB
- **ARNI 依 SBP 給藥 (PIONEER-HF)**：
  - SBP 100–119 → 起始 **24/26 mg BID**
  - SBP ≥ 120 → 起始 **49/51 mg BID**
- **ACEI → ARNI**：需 **36 h washout**（ARB 橋接）
- **IV iron**（HFrEF/HFmrEF + 鐵缺乏）：Tsat < 15–20% 益處最大

---

<!-- _class: divider -->
# Part 4
## 預後實證

---

# 關鍵試驗結果

## [STRONG-HF](https://pubmed.ncbi.nlm.nih.gov/?term=Mebazaa+STRONG-HF+heart+failure+2022) / [PIONEER-HF](https://pubmed.ncbi.nlm.nih.gov/?term=Velazquez+PIONEER-HF+sacubitril+2019) / [EMPULSE](https://pubmed.ncbi.nlm.nih.gov/?term=Voors+EMPULSE+empagliflozin+2022) / [SOLOIST-WHF](https://pubmed.ncbi.nlm.nih.gov/?term=Bhatt+SOLOIST-WHF+sotagliflozin+2021)

| 試驗 | 介入 | 主要結果 |
|------|------|----------|
| **STRONG-HF** | 出院前密集啟動 + 快速調升 + 密切追蹤 | 180 天死亡/HF 再住院 **↓34%** |
| **PIONEER-HF** | sacubitril/valsartan vs valsartan | 複合終點 **↓66%** |
| **EMPULSE** | empagliflozin | CV 死亡或 HF 事件 **↓31%** |
| **SOLOIST-WHF** | sotagliflozin | **↓33%** |

---

# 四聯療法的累積效益

- **四聯療法 (quadruple therapy)** ≈ 全因死亡相對風險 **↓73%**
- 中位存活延長 **7–11 年**

> **最強的「出院後拿不到 GDMT」預測因子 = 住院期間沒有啟動 GDMT** — 把握住院窗口

---

<!-- _class: divider -->
# Part 5
## 出院與脆弱期追蹤

---

# 脆弱期 (vulnerable phase) 調升

## 出院後第一個月風險最高，每週–每兩週追蹤

| 參數 | 安全調升門檻 |
|------|--------------|
| SBP | ≥ 95 mm Hg |
| HR | ≥ 55 bpm |
| eGFR | ≥ 30 mL/min/1.73 m² |
| K⁺ | ≤ 5.5 mmol/L |
| NT-proBNP | 未上升 > 10% |

> 目標：數週內、理想 < 3 個月達完整 GDMT；逐步**減量/停用環利尿劑**

---

<!-- _class: divider -->
# Part 6
## 裝置與逆向重塑

---

# 裝置適應症與「先 GDMT 再植入」

| 裝置 | 適應症 |
|------|--------|
| 一級預防 **ICD** | LVEF ≤ 35% |
| **CRT (±ICD)** | LVEF ≤ 35% + LBBB QRS ≥ 130 ms 或 non-LBBB ≥ 150 ms |
| **CSP** | LVEF > 35% 需節律調節時最佳 |

- **[PROVE-HF](https://pubmed.ncbi.nlm.nih.gov/?term=Felker+PROVE-HF+ICD+eligibility+2021)**：ICD 適格者用 ARNI 後 **6 月 32%、12 月 62% 不再符合** ICD 條件
- 減少 RV pacing；頑固房性快速心律不整 → **pace-and-ablate**（CSP + AV node ablation）
- 逆向重塑也可能使 **TEER 適應人數 ↓ 約 50%**

---

<!-- _class: divider -->
# Part 7
## 共病處置

---

# 共病處置（Table 1）

| 共病 | 處置要點 |
|------|----------|
| **CKD** | 較高利尿劑；續 BB/ARNI/SGLT2i；容忍 eGFR ↓≤50%；高血鉀用 MRA+SGLT2i+K-binders；UF 救援 |
| **AF** | BB 降 AF 負荷；不穩 → 電擊整流；陣發性/心搏過速性 CMP 優先 ablation |
| **VHD** | 嚴重 AS → TAVR/balloon valvuloplasty；續發 MR 於 GDMT 後考慮 TEER |
| **鐵缺乏** | 急性期後高達 80%；IV iron 改善功能/QoL |
| **高血壓** | IV 血管擴張劑；HFrEF 避免 non-DHP CCB (verapamil/diltiazem) |

---

<!-- _class: divider -->
# Part 8
## 緩解概念與全球不平等

---

# 從去充血到緩解

- 觀念：症狀導向去充血 → **疾病修飾治療** → HF remission / recovery
- 約 **20–30% 為非反應者 (nonresponders)**
- **「I NEED HELP」紅旗徵象** → 轉介進階心衰竭（LVAD / 移植）
- 全球不平等：藥物/裝置可近性熱圖差異 — **沒有任何國家達到一致全面可近性**

> **Take Home**：把急性事件轉化為長期緩解 — 立即去充血 + 住院內啟動四大支柱 + 脆弱期密集調升 + 先 GDMT 逆向重塑再評估裝置/瓣膜介入

---

<!-- _class: small-text -->
# 參考文獻 (1/2)

1. Bruno J, Arrigo M, Januzzi JL, Mebazaa A, et al. Contemporary Management of Acute Heart Failure. [*J Am Coll Cardiol*. 2026 (in press).](https://doi.org/10.1016/j.jacc.2026.03.029)
2. Mebazaa A, et al. STRONG-HF. [*Lancet*. 2022;400(10367):1938-1952.](https://pubmed.ncbi.nlm.nih.gov/?term=Mebazaa+STRONG-HF+heart+failure+2022)
3. Velazquez EJ, et al. PIONEER-HF. [*N Engl J Med*. 2019;380(6):539-548.](https://pubmed.ncbi.nlm.nih.gov/?term=Velazquez+PIONEER-HF+sacubitril+2019)
4. Voors AA, et al. EMPULSE. [*Nat Med*. 2022;28(3):568-574.](https://pubmed.ncbi.nlm.nih.gov/?term=Voors+EMPULSE+empagliflozin+2022)
5. Bhatt DL, et al. SOLOIST-WHF. [*N Engl J Med*. 2021;384(2):117-128.](https://pubmed.ncbi.nlm.nih.gov/?term=Bhatt+SOLOIST-WHF+sotagliflozin+2021)

---

<!-- _class: small-text -->
# 參考文獻 (2/2)

6. Felker GM, et al. PROVE-HF (ICD eligibility). [*Circulation*. 2021;144(2):180-182.](https://pubmed.ncbi.nlm.nih.gov/?term=Felker+PROVE-HF+ICD+eligibility+2021)
7. McDonagh TA, et al. 2021 ESC HF Guidelines. [*Eur Heart J*. 2021;42(36):3599-3726.](https://pubmed.ncbi.nlm.nih.gov/?term=McDonagh+2021+ESC+heart+failure+guidelines)
8. Heidenreich PA, et al. 2022 AHA/ACC/HFSA HF Guideline. [*J Am Coll Cardiol*. 2022;79(17):e263-e421.](https://doi.org/10.1016/j.jacc.2021.12.012)
9. Mullens W, Meekers E, et al. ADVOR. [*Eur Heart J*. 2023;44(37):3672-3682.](https://pubmed.ncbi.nlm.nih.gov/?term=Mullens+ADVOR+acetazolamide+2023)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC**
[原文 — J Am Coll Cardiol (DOI: 10.1016/j.jacc.2026.03.029)](https://doi.org/10.1016/j.jacc.2026.03.029)
