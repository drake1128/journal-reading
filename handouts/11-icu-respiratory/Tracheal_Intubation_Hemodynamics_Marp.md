---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: 'Microsoft JhengHei', 'PingFang TC', sans-serif; background-color: #ffffff; color: #2d3436; }
  section.lead { background-color: #1a2740; color: #ffffff; }
  section.lead h1 { color: #ffffff; font-size: 2.2em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.divider { background-color: #0072bc; color: white; display: flex; justify-content: center; align-items: center; }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.5em; text-align: center; }
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
footer: '謝慕揚 MD, PhD, FESC | 重症插管血流動力學 | 2026'
---

<!-- _class: lead -->
# 重症病人氣管插管的血流動力學
## The Hemodynamics of Tracheal Intubation in Critically Ill Patients
**整理：謝慕揚 MD, PhD, FESC** | 2026-08-02

J Intensive Care 2026;14:42 — narrative review
[原文連結 https://doi.org/10.1186/s40560-026-00877-4](https://doi.org/10.1186/s40560-026-00877-4)

---

# 為何重要：peri-intubation 高風險
## INTUBE 國際研究 — JAMA 2021;325:1164–72

重症病人常已有 hypovolemia、vasoplegia、hypoxemia、acidosis → 放大插管崩潰風險。

| Peri-intubation 併發症 | 發生率 |
|------------------------|--------|
| 心血管不穩定 (cardiovascular instability) | **42.6%** |
| 嚴重低血氧 (severe hypoxemia) | **9.3%** |
| 心跳停止 (cardiac arrest) | **3.1%** |

> **插管相關低血壓**是最常見也最具後果的併發症，與 **ICU 及 28 天死亡率獨立相關**——即使短暫也一樣。

---

# 兩種「困難氣道」概念

| 類型 | 內涵 |
|------|------|
| **Anatomically difficult airway** | 視野 / 進入氣道本身困難（解剖層面） |
| **Physiologically difficult airway** | 潛在心肺脆弱性，插管過程易生理惡化 |

- 兩者**可重疊並互相影響**
- 成功處理解剖困難（達成 first-pass success）有助避免後續生理惡化
- **first-pass failure 與併發症風險增加相關**

> 本 review 聚焦生理性困難氣道的血流動力學基礎。缺乏 RCT → 需仰賴生理學推理。

---

# 血流動力學時間軸（Fig. 1）

```text
Pre-induction  高交感張力維持「表面穩定」= 脆弱平衡
      │
Induction      induction agent → 抑制 adrenergic tone → SVR↓ CO↓
      │
Apnea          desaturation + 高碳酸 + 酸中毒 → 收縮力↓ 心律不整↑
      │
轉正壓通氣 PPV  胸內壓↑ → venous return↓ RV afterload↑
      │
Post-intubation  sedation / ventilator / vasopressor 持續形塑
```

> 威脅是**累加**而非孤立——把插管視為一段**軌跡**，強調持續預判與主動處置。

---

<!-- _class: divider -->
# Adrenergic Collapse
## 誘導期的交感崩潰

---

# 誘導前的 catecholamine surge = 警訊
## INTUBE 洞察 — Am J Respir Crit Care Med 2022;206:449–58

- 休克時內生 catecholamine（epinephrine、norepinephrine）代償維持 CO 與 SVR
- 過量 → 心肌耗氧↑、缺血、心律不整
- INTUBE：**插管前低收縮壓 + 高心跳** 獨立預測 peri-intubation 不穩定
- 病人已在**代償極限**，輕微交感下降即可觸發崩潰

> 床邊「心跳快、壓力靠壓撐住」**不是穩定，是 adrenergic dependence 的警訊**。

---

# 開刀房 vs. ICU：相反解讀

| 情境 | 對交感 surge 態度 | 理由 |
|------|------------------|------|
| **開刀房 (OR)** | 要**壓抑 (blunt)**：opioids、β-blocker、加深麻醉 | 穩定病人的 surge 會引發高血壓、心律不整、缺血 |
| **ICU** | surge 是**維持灌流的最後防線** | 壓抑 → 移除最後循環支撐 → 崩潰 |

> 同一件事，在 OR 是保護、在 ICU 可能是災難。
> 所有 induction agent 都**普遍壓抑交感**；RSI 時 sympatholysis 常在 **< 1 分鐘**驟然發生 → 必須**預防**而非反應。

---

# Induction agents 對血流動力學（Table 1）

| 藥物 | CO | SVR | MAP | HR | 收縮力 | 備註 |
|------|----|----|-----|----|-------|------|
| **Propofol** | ↓ | ↓↓ | ↓↓ | ↓/→ | ↓ | 心血管不穩定**危險因子** |
| **Ketamine** | ↑ | →/↑ | →/↑ | ↑ | ↑ | 增加心肌耗氧 |
| **Etomidate** | → | →/↑ | → | → | ↓/→ | **腎上腺抑制** |
| **Midazolam** | ↓ | ↓ | ↓ | ↓/→ | ↓ | 譫妄風險 |
| **Remimazolam** | → | ↓/→ | ↓/→ | → | → | ICU 資料有限 |

> **預期不穩定時避免 propofol**，優先血流動力學耐受性佳的替代藥。

---

# 臨床證據：propofol、Casey、Matchett
## INTUBE / Matchett ICM 2022 / Casey NEJM 2025;doi:10.1056/NEJMoa2511420

- **INTUBE**：propofol **無論劑量**都增加崩潰風險，且為**唯一可調控**危險因子
- **Matchett 2022 RCT**：ketamine vs. etomidate — 7 天存活 **85.1% vs. 77.3%**；28 天無顯著差 (66.8% vs. 64.1%)
- **Koroki 2024 Bayesian**：ketamine 降死亡率機率 83.2%；**Greer 2025** 則反向
- **Casey 2025 NEJM RCT (n=2365)**：28 天死亡率 **28.1% vs. 29.1% (NS)**；ketamine 組 **cardiovascular collapse 較高 22.1% vs. 17.0%**（RD 5.1%，95% CI 1.9–8.3）

> ketamine 與 etomidate **無一致贏家** → 依情境個別化；共識是**避免 propofol**。

---

<!-- _class: divider -->
# Hypoxemia、Apnea 與右心

---

# 低血氧與 apnea 的心臟後果

- 冠脈血流雖代償增加，嚴重 hypoxemia 仍不足以防缺血
- 肥胖、ARDS、PE、aspiration 者風險更高
- **Apnea → CO₂↑、pH↓**
  - 初期：CO₂ / H⁺ → 血管擴張、冠脈血流↑
  - **pH < 7.2**：心肌收縮力↓、β-adrenergic 反應↓、心律不整↑

> apnea 不只是缺氧——更是**酸中毒對心臟的直接打擊**；同時的鎮靜劑再疊加血管擴張與心肌抑制。

---

# 右心室衰竭 (RV failure)

被低估的 peri-intubation 不穩定貢獻者。右心特性：

1. **RCA 雙相灌流**（收縮＋舒張）→ RV 對短暫低血氧相對耐受
2. **薄壁** → 易受 pressure overload（肺動脈壓↑）
3. **HPV + ARDS 微血栓** → 肺血管阻力↑ → 肺高壓

> **RV 惡化循環**：RV afterload↑ → LV 充填↓ → RCA 血流↓ → RV 缺血 → 循環崩潰。

---

# Heart–lung interactions：轉正壓通氣

- **自主呼吸**：吸氣負壓助靜脈回流（RV preload↑）；FRC 時肺血管阻力最低
- **轉 PPV**：正壓 → 靜脈回流壓力梯度↓ → 全身低灌流；肺容積↑ → 肺血管阻力↑ → RV 射出變差
- 衝擊隨**平均氣道壓**上升而加劇，**PEEP** 是主因

> **PEEP 初始設低 5–6 cmH₂O，穩定後逐步達標。**
> **Awake / flexible bronchoscopy intubation** 保留負壓吸氣益處、避開 apnea desaturation（需高技術）。

---

<!-- _class: divider -->
# 實務 Care Bundle（Fig. 2）

---

# Care Bundle（1）：氧合 + 喉鏡
## Preoxygenation net-meta Pitre 2025 / VL Prekker NEJM 2023;389:418–29

| 裝置 | 角色 |
|------|------|
| **NIV** | PEEP + 壓力支持；降 RV preload / LV afterload；**第一線**（尤其 PaO₂/FiO₂ < 200） |
| **HFNC** | 輕度 PEEP、沖死腔；apnea 期 **apneic oxygenation** |
| 面罩 | 最基本；HFNC 優於面罩 |

- **Videolaryngoscopy 第一線**：改善 first-pass success、減少食道插管 / 吸入
- first-pass success 在重症至關重要

---

# Care Bundle（2）：輸液與升壓
## PrePARE Lancet Respir Med 2019 / Russell JAMA 2022;328:270–9

- **不建議 routine fluid bolus**（PrePARE、Russell 均無支持）
- 分開評估 **fluid responsiveness**（PLR、PPV）與 **fluid tolerance**；用 **POCUS**（心 / IVC / B-line）導引
- **主動預防**低血壓暴露 > 被動反應
- 誘導前考慮 **arterial line**（AWAKE trial 降低血壓暴露）
- **PREVENTION (NCT05014581) / FLUVA (NCT05318066)** 評估 pre-emptive vasopressor

> 懷疑 RV failure / 肺高壓 → 考慮 pulmonary arterial catheter。

---

# Care Bundle（3）：準備與插管後

- **Checklist + 團隊溝通**：角色分配、應變計畫；checklist 應納入病人生理優化策略
- **Induction agent**：有風險者優先 ketamine / etomidate；用 NMBA 時足量鎮靜避免知覺
- **插管後**：
  - 預判 PPV → venous return↓、LV preload↓，據此調升壓劑 / 輸液
  - PEEP 5–6 cmH₂O 起、穩定後達標
  - 鎮靜審慎滴定，避免血管擴張與交感 surge

---

# Knowledge Gaps（Table 2）

1. **預防性升壓劑**降低 peri-intubation 不穩定的效益與安全性
2. 發展並驗證預測誘導後血流動力學軌跡的**評分系統**
3. **右心室功能障礙**的早期辨識與處置指引
4. 涵蓋藥理 + 非藥理策略的 **care bundle** 成效

> benzodiazepine 角色未明：合併 midazolam/remimazolam 與 ketamine/etomidate 是否更能降低麻痺期知覺，尚待研究。PREVENTION / FLUVA 結果值得期待。

---

# Take-home messages

> **1.** 床邊「心跳快、壓力撐住」= adrenergic dependence 警訊，非穩定。

> **2.** OR 要 blunt 的交感 surge，在 ICU 是維持灌流的最後防線。

> **3.** 預期不穩定 → **避免 propofol**；ketamine 與 etomidate 無一致贏家，個別化。

> **4.** apnea 的酸中毒（pH<7.2）直接打擊心肌與 β 反應；留意 RV failure 惡化循環。

> **5.** 不 routine bolus；主動預防低血壓（arterial line、pre-emptive vasopressor）；NIV + VL 第一線；PEEP 5–6 起。

---

<!-- _class: small-text -->
# 參考文獻（精選）

1. Kotani Y, et al. The hemodynamics of tracheal intubation in critically ill patients: a narrative review. [*J Intensive Care*. 2026;14:42.](https://doi.org/10.1186/s40560-026-00877-4)
2. Russotto V, et al. Intubation practices and adverse peri-intubation events (INTUBE). *JAMA*. 2021;325:1164–72.
3. Russotto V, et al. Peri-intubation cardiovascular collapse: INTUBE study. *Am J Respir Crit Care Med*. 2022;206:449–58.
4. Kotani Y, Russotto V. Induction agents for tracheal intubation in critically ill patients. *Crit Care Med*. 2025;53:e173–81.
5. Matchett G, et al. Etomidate versus ketamine for emergency endotracheal intubation: RCT. *Intensive Care Med*. 2022;48:78–91.
6. Koroki T, et al. Ketamine versus etomidate: a Bayesian meta-analysis. *Crit Care*. 2024;28:48.
7. Greer A, et al. Ketamine versus etomidate for RSI: systematic review. *Crit Care Med*. 2025;53:e374–83.
8. Casey JD, et al. Ketamine or etomidate for tracheal intubation of critically ill adults. [*N Engl J Med*. 2025.](https://doi.org/10.1056/NEJMoa2511420)

---

<!-- _class: small-text -->
# 參考文獻（續）

9. Karamchandani K, et al. Tracheal intubation with a physiologically difficult airway: international Delphi study. *Intensive Care Med*. 2024;50:1563–79.
10. Janz DR, et al. Fluid bolus on cardiovascular collapse (PrePARE): RCT. *Lancet Respir Med*. 2019;7:1039–47.
11. Russell DW, et al. Fluid bolus and cardiovascular collapse: RCT. *JAMA*. 2022;328:270–9.
12. Pitre T, et al. Preoxygenation strategies: network meta-analysis. [*Lancet Respir Med*. 2025.](https://doi.org/10.1016/S2213-2600(25)00029-3)
13. Prekker ME, et al. Video versus direct laryngoscopy in critically ill adults. *N Engl J Med*. 2023;389:418–29.
14. Jozwiak M, Teboul J-L. Heart–lungs interactions. *Ann Intensive Care*. 2024;14:122.
15. Kouz K, et al. Continuous vs. intermittent arterial pressure monitoring (AWAKE). *Br J Anaesth*. 2022;129:478–86.

*部分文獻原文僅附卷頁而無 DOI，為避免杜撰 DOI 保留 Vancouver citation；完整 63 篇見原文。*

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**整理：謝慕揚 MD, PhD, FESC**
J Intensive Care 2026;14:42
[https://doi.org/10.1186/s40560-026-00877-4](https://doi.org/10.1186/s40560-026-00877-4)
