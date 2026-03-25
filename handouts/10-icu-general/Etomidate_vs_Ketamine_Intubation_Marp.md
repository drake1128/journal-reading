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
footer: '謝慕揚 MD, PhD, FESC | Etomidate vs Ketamine | 2026'
---

<!-- _class: lead -->

# Etomidate vs Ketamine
## 重症插管誘導用藥選擇 — CCU 與心導管室觀點

**謝慕揚 MD, PhD, FESC**
資料來源：NEJM 2025, JAMA Network Open 2025, Critical Care 2024 | 2026-03-08
[RSI Trial — NEJM 2025](https://doi.org/10.1056/NEJMoa2511420)

---

# 大綱

1. 為什麼誘導藥物選擇很重要？
2. Etomidate vs Ketamine 藥理比較
3. 關鍵臨床試驗
4. 統合分析整合證據
5. CCU 與心導管室的特殊考量
6. 臨床實務建議

---

<!-- _class: divider -->

# 第一部分：問題的重要性

---

# Peri-Intubation Cardiovascular Collapse

- 重症病人插管時 **major adverse events 發生率 30.5%**
- ICU 內更高達 **41%**（Downing et al., Am J Emerg Med 2023）
- **INTUBE Study**（29 國, N=2,760）：
  - Cardiovascular collapse → ICU 死亡 adjusted **OR 2.47**
  - Propofol 是唯一顯著增加風險的誘導藥物

> **關鍵訊息**：誘導藥物的選擇是可修改的風險因素

---

# CCU / 心導管室的挑戰

- 病人常伴有 **ACS、cardiogenic shock、acute HF**
- 血流動力學儲備極低 (limited hemodynamic reserve)
- 可能正在使用 vasopressors / MCS (IABP, Impella, ECMO)
- 心導管室空間狹小，病人在 cath table 上
- **Semi-urgent to emergent** 插管情境

> **目標**：快速誘導 + 最小血流動力學波動

---

<!-- _class: divider -->

# 第二部分：藥理學比較

---

# Etomidate vs Ketamine — 藥理特性

| 特性 | Etomidate | Ketamine |
|------|-----------|----------|
| 劑量 | 0.2–0.3 mg/kg IV | 1–2 mg/kg IV |
| 起效 | 15–45 秒 | 30–60 秒 |
| 作用時間 | 3–12 分鐘 | 10–20 分鐘 |
| 機轉 | GABA-A agonist | NMDA antagonist |
| 血壓 | **穩定** | ↑（交感興奮） |
| 心率 | 穩定 | ↑ |
| 心肌氧耗 | 不增加 | **可能增加** |
| 腎上腺 | **抑制** (11β-hydroxylase) | 無影響 |
| 止痛 | 無 | **有** (dissociative) |
| 支氣管 | 中性 | **擴張** |

---

# Ketamine 在重症病人的陷阱

- **交感興奮機制**：釋放內源性 catecholamine → ↑ HR, ↑ BP
- 但在 **catecholamine-depleted** 的病人中：
  - 長期休克、嚴重心衰竭
  - 交感興奮效應 **可能不足**
  - 暴露出 **直接心肌抑制** 作用
  - 反而造成 **低血壓**

> **Pearl**：Catecholamine-depleted 的 cardiogenic shock 病人給予 ketamine，可能出現意外的低血壓！

---

<!-- _class: divider -->

# 第三部分：關鍵臨床試驗

---

# RSI Trial — NEJM 2025（里程碑 RCT）

- **設計**：Multicenter pragmatic RCT, 美國 14 中心
- **人數**：N = 2,365（Ketamine 1,176 vs Etomidate 1,189）
- **主要終點**：28 天院內全因死亡率

| 終點 | Ketamine | Etomidate | Risk Diff |
|------|----------|-----------|-----------|
| **28 天死亡率** | **28.1%** | **29.1%** | -0.8% (P=0.65) |
| CV collapse | **22.1%** | **17.0%** | **+5.1%** |
| SBP < 65 mmHg | 10.6% | 8.0% | — |
| 新增 vasopressor | 15.8% | 12.2% | — |
| Cardiac arrest | 1.4% | 1.0% | — |

---

# RSI Trial — 關鍵解讀

- **死亡率沒有差異** → 兩種藥物都是合理選擇
- Ketamine 的 **cardiovascular collapse 較高** (+5.1%)
  - 可能與重症病人 catecholamine depletion 有關
- Etomidate 的 adrenal suppression **未轉化為死亡率差異**
- **Unmasked design** 是限制之一

> **Bottom Line**：選擇哪種藥物，死亡率沒有差異；但 etomidate 在血流動力學穩定性方面有小幅優勢

---

# Brazilian Registry — JAMA Network Open 2025

- Target trial emulation, N = 1,810（18 家急診）
- 觀察性研究，使用 inverse probability weighting

| 終點 | Ketamine | Etomidate | RR |
|------|----------|-----------|-----|
| 28 天死亡率 | 54.4% | **60.5%** | **1.14** (1.03–1.27) |
| 7 天死亡率 | 30.1% | **35.2%** | 1.19 (1.04–1.35) |
| 30 min 內 hemodynamic instability | **24.2%** | 18.9% | — |

- **注意**：觀察性研究，病人死亡率 >50%（不同族群）
- Ketamine 組病前 shock index 較高

---

<!-- _class: divider -->

# 第四部分：統合分析

---

# Meta-Analysis 綜合結果

| 分析 | 研究數 | N | 死亡率結果 | 特殊發現 |
|------|--------|---|-----------|----------|
| Bandyopadhyay 2025 (RCTs) | 4 | 1,663 | RR 0.95 (0.72–1.25) | Hypotension: ketamine ↑ |
| Koroki 2024 (Bayesian) | 8 | 2,978 | RR 0.93 (CrI 0.79–1.08) | 83% prob ketamine better |
| Smischney 2025 (SR) | 23 | — | OR 0.76 (0.62–0.92)* | Etomidate ↓ survival to DC |

*Etomidate vs ketamine for survival to hospital discharge

> **整合結論**：死亡率無統計差異；Bayesian 分析提示 ketamine **可能**略優，但確定性不足

---

<!-- _class: divider -->

# 第五部分：CCU 與心導管室特殊考量

---

# ACS / STEMI 情境

| 考量 | Etomidate | Ketamine |
|------|-----------|----------|
| Heart rate | 穩定 | ↑ → 增加 MVO₂ |
| Blood pressure | 穩定 | ↑ → 增加 afterload |
| Rate-pressure product | 不影響 | **增加** |
| 心肌缺血風險 | 低 | 理論上較高 |

> **建議**：ACS 病人 → **優先考慮 etomidate**（不增加心肌氧耗）
> 若 ACS + 低血壓 → etomidate 仍優先；ketamine 可作為次選

---

# Cardiogenic Shock 情境

- **Etomidate 優勢**：
  - 血流動力學穩定性最佳
  - 不依賴內源性 catecholamine
  - 對心肌收縮力幾乎無影響

- **Ketamine 風險**：
  - Catecholamine-depleted → 直接心肌抑制
  - 可能造成意外低血壓

- **Etomidate 風險**：
  - Adrenal suppression 24–48 hrs
  - 在 vasopressor-dependent 病人中可能影響 cortisol response

> **建議**：Cardiogenic shock → **etomidate 優先**

---

# Septic Shock 合併心臟疾病

- **Ketamine 優勢**：
  - 無 adrenal suppression
  - 具止痛效果
  - 支氣管擴張（若合併 pneumonia）

- **Etomidate 風險**：
  - Adrenal suppression 在 sepsis 中可能有臨床意義
  - Relative adrenal insufficiency 更常見

> **建議**：Septic shock → **ketamine 優先**
> 混合型休克 → 個案評估

---

# 為什麼 CCU/Cath Lab 應避免 Propofol？

- **INTUBE Study**：propofol 唯一顯著增加 CV collapse（OR 1.28）
- 明顯降低 SVR 和心肌收縮力
- 劑量依賴性低血壓，在 hemodynamically compromised 病人中尤為危險
- Emgin et al. 2026：propofol 增加 PIC 風險 **OR 2.962**

> **原則**：Propofol 保留用於血流動力學穩定且有 anesthesia 支援的情境

---

<!-- _class: divider -->

# 第六部分：臨床實務建議

---

# 選藥流程

```text
緊急插管評估
    |
血流動力學狀態
    |
├── 穩定 (SBP > 90, 無 vasopressor)
│   → Etomidate 0.3 mg/kg 或 Ketamine 1.5 mg/kg
│
├── Cardiogenic shock
│   → Etomidate 0.2–0.3 mg/kg（優先）
│
├── Septic shock
│   → Ketamine 1–1.5 mg/kg（優先）
│
├── ACS / STEMI（穩定）
│   → Etomidate 0.3 mg/kg（優先）
│
└── 混合型休克
    → 個案評估
```

---

# Take-Home Messages

1. **RSI Trial (NEJM 2025)**：死亡率無差異 — 兩者都是合理選擇
2. **Cardiovascular collapse**：Ketamine 稍多（+5.1%），注意 catecholamine depletion
3. **ACS/Cardiogenic shock** → 傾向 **etomidate**（不增加 MVO₂、血流動力學穩定）
4. **Septic shock** → 傾向 **ketamine**（避免 adrenal suppression）
5. **避免 propofol** 作為 CCU/Cath lab 急診插管首選
6. **最重要的是插管前準備**：IV access、vasopressor 備妥、團隊溝通

> 藥物選擇重要，但**準備工作更重要**

---

<!-- _class: small-text -->

# 參考文獻

1. Casey JD, et al. Ketamine or Etomidate for Tracheal Intubation. [*NEJM*. 2025.](https://doi.org/10.1056/NEJMoa2511420)
2. Maia IWA, et al. Ketamine, Etomidate, and Mortality in ED Intubations. [*JAMA Netw Open*. 2025.](https://doi.org/10.1001/jamanetworkopen.2025.48060)
3. Bandyopadhyay A, et al. Ketamine vs etomidate for RSI: meta-analysis. [*Clin Exp Emerg Med*. 2025.](https://doi.org/10.15441/ceem.24.363)
4. Koroki T, et al. Bayesian meta-analysis. [*Crit Care*. 2024;28:146.](https://doi.org/10.1186/s13054-024-04831-4)
5. Smischney NJ, et al. Sedative agents for intubation: SR. [*J Intensive Care Med*. 2025.](https://doi.org/10.1177/08850666251337702)
6. Russotto V, et al. INTUBE Study. [*AJRCCM*. 2022;206:1373.](https://doi.org/10.1164/rccm.202204-0712OC)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
