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
  section.lead h1 { color: #ffffff; font-size: 2.0em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #8ec5ff; }
  section.lead blockquote, section.lead blockquote strong { color: #2d3436; }
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
  section.divider h2, section.divider h3 { color: #ffe066; }
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
  section.small-text { font-size: 0.8em; }
footer: '謝慕揚 MD, PhD, FESC | Door-to-Unload in STEMI-CS | 2026'
---

<!-- _class: lead -->
# Door-to-Unload Time 與死亡率
## STEMI 併發心因性休克、接受微軸流幫浦 (Impella) 的時效分析
**謝慕揚 MD, PhD, FESC** | 2026-07-19
Nagai S, et al. *EuroIntervention*. 2026;22(12):e678-e689
[原文連結 (DOI: 10.4244/EIJ-D-25-01369)](https://doi.org/10.4244/EIJ-D-25-01369)

> 讀書會共筆式整理，非官方指引；臨床決策請以原文與最新指引為準。

---

# 一句話重點 (Bottom Line)

> STEMI 併發心因性休克 (CS) 且使用 **微軸流幫浦 (mAFP／Impella)** 的病人，
> **到院到卸載的時間 (door-to-unload) 愈短、預後愈好**。

- Door-to-unload 中位數 **99 分鐘**
- 整體院內死亡率 **39.2%**
- 以 90 分鐘為界：**延遲置放 (>90 min) 校正後 OR = 1.56 (95% CI 1.26–1.95)**

**「Time is myocardium」→ 延伸為「Time is circulatory support」**

---

# 背景：為什麼要「卸載 (unloading)」？

- STEMI-CS 死亡率極高（歷史約 40–50%）。
- **DanGer Shock (NEJM 2024)**：常規 Impella CP 使 180 天死亡由 58.5% → **45.8%**（併發症增加）。→ 第一個證明 MCS 在 AMI-CS 有存活益處的 RCT。
- 微軸流幫浦的雙重效益：

| 效益 | 機轉 |
|------|------|
| **卸載 (unloading)** | 降低 LV 壁張力、前負荷、心肌耗氧 |
| **循環支持 (support)** | 把血從 LV 打入主動脈，維持器官灌流、打破休克螺旋 |

> 尚未解答的問題：既然裝置有效，**「多快裝上」重不重要？** ← 本研究

---

# "Door-to-Unload" 是什麼？

- **Door-to-unload time** = 到院 (door) → 成功置放 mAFP、完成左心室卸載 (unload) 的時間。
- 類比 **door-to-balloon time**，但衡量的是「循環支持啟動」的速度。
- **假說**：door-to-unload 愈短 → 院內死亡率愈低。

> 與 STEMI-DTU 的「策略性延遲再灌流去卸載」不同——本研究是**休克病人 MCS 啟動時效**的觀察性註冊分析（見後）。

---

<!-- _class: divider -->
# 研究方法與結果

---

# 研究方法 (Methods)

| 項目 | 內容 |
|------|------|
| 設計 | 全國多中心、回溯性註冊研究 |
| 資料來源 | **J-PVAD**（日本經皮心室輔助裝置註冊） |
| 期間 | 2020/02 – 2023/12 |
| 對象 | STEMI 併 CS 且接受 **mAFP 置放** |
| 樣本數 | **1,783 人** |
| 主要暴露 | Door-to-unload time（並以 90 min 分組） |
| 主要結果 | **院內死亡率** |
| 統計 | 多變量 logistic regression、restricted cubic spline |

分組：≤60 / 61–90 / 91–150 / >150 min；主要切點 **90 min**。

---

# 主要結果：死亡率隨延遲遞增

| Door-to-unload time | 院內死亡率 |
|---------------------|-----------|
| ≤ 60 min | **32.9%** |
| 61–90 min | **33.0%** |
| 91–150 min | **40.1%** |
| > 150 min | **48.3%** |

- 中位數 **99 min**（實務上多數 >90 min）；整體死亡率 **39.2%**。
- ≤60 與 61–90 兩組幾乎相同（約 33%）→ **90 分鐘內為平台，之後上升**。

> **延遲置放 (>90 min) vs 早期 (≤90 min)：adjusted OR 1.56 (95% CI 1.26–1.95)**
> Restricted cubic spline：90 min 內風險平穩，之後上升。

---

# 延遲置放的預測因子

哪些病人／情境 mAFP 較慢裝上？（＝可改善的著力點）

- **年齡較大**
- **院所量能較低 (lower institutional volume)**
- **心跳較快、肌酸酐較高**（病況較重）
- **先前已用 IABP 或 VA-ECMO**
- **在 mAFP 前先做 PCI**（先打通、後裝置的順序）

> 低量能中心、以及「先 PCI／先其他 MCS 再上 Impella」的流程 → 是造成延遲、可被 QI 介入的主因。

---

# 次族群分析：VA-ECMO (ECPELLA)

| 次族群 | 特徵 | 時間–死亡率關聯 |
|--------|------|----------------|
| 無先前 MCS | 基線較輕 | 延遲 → 死亡率↑ |
| 僅先前 VA-ECMO | 基線更重、死亡率更高 | **關聯依然成立** |

> 不論「單純 Impella」還是「ECMO 再加 Impella (ECPELLA)」，
> **愈早完成左心室卸載都與較好存活相關**——延遲的傷害不因基線嚴重度消失。

---

<!-- _class: divider -->
# 如何解讀？
## 放進 DanGer Shock 與 STEMI-DTU 的脈絡

---

# 三個「卸載」研究，回答不同問題

| 研究 | 族群 | 介入 | 結果 |
|------|------|------|------|
| **DanGer Shock** (NEJM 2024) | STEMI **併休克** | Impella vs 標準 | 死亡 **↓**（45.8 vs 58.5%）→ 「要不要用」 |
| **本研究 J-PVAD** (EuroInt 2026) | STEMI **併休克**、皆用 mAFP | 早 vs 晚置放 | 早置放死亡率↓ → 「**多快用**」 |
| **STEMI-DTU** (JACC 2026) | 前壁 STEMI **無休克** | 卸載 30min 後**延遲**PCI | 梗塞範圍無差、併發症↑ → 無休克者**不建議** |

> **不矛盾**：無休克者為縮小梗塞而延遲再灌流 → 沒好處；
> 併休克者一旦決定用 mAFP → **應盡快裝上**。卸載對休克的價值在「循環支持與速度」。

---

# 臨床啟示 (Clinical Implications)

- **建立 "door-to-unload" 品質指標**：如同 door-to-balloon，**目標 ≤ 90 分鐘**。
- **提前決策、平行作業**：明確休克者及早啟動 shock team，避免「先 PCI 再考慮裝置」的串接延遲。
- **量能與轉診**：低量能中心延遲風險高 → 標準化流程、shock team、區域協作。
- **ECPELLA 同樣適用**：已上 VA-ECMO 者若計畫加裝 Impella，仍應盡早完成卸載。

---

# 研究限制 (Limitations)

- **觀察性、回溯性註冊** → 只能顯示**關聯**、非因果；殘餘干擾難排除。
- **適應症偏差**：時間與病況嚴重度互相糾纏。
- **日本單一國家註冊** → 外推性需謹慎。
- **僅院內死亡**，缺長期與神經學結果。
- **90 min 為資料驅動切點** → 需前瞻性驗證。

---

# Take Home Messages

> **1.** STEMI-CS 用 Impella：door-to-unload 中位數 **99 min**，院內死亡 **39.2%**。

> **2.** 死亡率隨延遲遞增；**>90 min：adjusted OR 1.56 (1.26–1.95)**。

> **3.** 「Time is myocardium」→「**Time is circulatory support**」：決定用就**盡快裝（目標 ≤90 min）**。

> **4.** 可改善因子：低量能中心、先 PCI／先其他 MCS 再上 Impella。

> **5.** 與 STEMI-DTU 不矛盾——卸載對**休克**的價值在循環支持與速度，而非縮小梗塞。

---

<!-- _class: small-text -->
# 參考文獻

1. Nagai S, et al; J-PVAD Investigators. Door-to-unload time and mortality in STEMI complicated by cardiogenic shock. [*EuroIntervention*. 2026;22(12):e678-e689.](https://doi.org/10.4244/EIJ-D-25-01369)
2. Møller JE, et al; DanGer Shock Investigators. Microaxial Flow Pump or Standard Care in Infarct-Related Cardiogenic Shock. [*N Engl J Med*. 2024;390(15):1382-1393.](https://doi.org/10.1056/NEJMoa2312572)
3. Kapur NK, et al. Unloading the LV Before Reperfusion in Anterior STEMI (DTU-STEMI Pilot). [*Circulation*. 2019;139(3):337-346.](https://doi.org/10.1161/CIRCULATIONAHA.118.038269)
4. Kapur NK, et al. LV Unloading in Anterior STEMI Without Shock: The STEMI-DTU RCT. [*J Am Coll Cardiol*. 2026;88(1):76-90.](https://doi.org/10.1016/j.jacc.2026.03.071)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC**
Door-to-Unload in STEMI-CS | 2026
