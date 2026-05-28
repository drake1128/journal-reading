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
  section.lead p, section.lead strong, section.lead a { color: #dfe6e9; }
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
  h2 { color: #0072bc; font-size: 0.85em; }
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
  section.small-text { font-size: 0.78em; }
  section.ref { font-size: 0.62em; }
  section.ref h1 { font-size: 1.4em; }
footer: '謝慕揚 MD, PhD, FESC | POPular PAUSE TAVI | 2026'
---

<!-- _class: lead -->

# POPular PAUSE TAVI

## TAVI 周術期口服抗凝劑：續用 vs 中斷？

**謝慕揚 MD, PhD, FESC** | 2026-05-05

[N Engl J Med 2025;392(5):438-449](https://doi.org/10.1056/NEJMoa2407794) | [ESC 2024 Hot Line 5](https://www.escardio.org/The-ESC/Press-Office/Press-releases/Oral-anticoagulants-should-be-paused-before-transcatheter-aortic-valve-implantation)

---

# 臨床問題
## [van Ginkel DJ, et al. NEJM 2025](https://doi.org/10.1056/NEJMoa2407794)

- TAVI 病人約 **1/3** 因 AF 等合併症需長期 OAC
- 過去做法分歧：
  - **持續 OAC**：理論上減少血栓栓塞、但可能增加出血
  - **中斷 OAC**：理論上減少出血、但短暫無抗凝可能升高血栓
- Observational data 暗示 continuation 可能不增加出血 — 但**沒有隨機證據**
- POPular PAUSE TAVI 是**第一個直接比較兩種策略的 RCT**

---

# 試驗設計
## [ClinicalTrials.gov NCT04437303](https://clinicaltrials.gov/study/NCT04437303)

| 項目 | 內容 |
|------|------|
| Design | International, open-label, **non-inferiority** RCT |
| 中心 | 22 European sites（NL、BE、DK、IT、IE、LU） |
| Randomization | 1:1 → continuation vs interruption (≥48h pre-TAVI) |
| Population | TAVI 病人合併長期 OAC 適應症 |
| Funding | ZonMw、St. Antonius Research Fund |

---

# 排除條件（高血栓族群）
## [van Ginkel DJ, et al. NEJM 2025](https://doi.org/10.1056/NEJMoa2407794)

> **以下病人不可中斷 OAC，因此排除：**

- Mechanical heart valve prosthesis
- Intracardiac thrombus
- VTE 在 TAVI 前 **3 個月**內
- AF 病人合併 TIA 或 stroke 在 TAVI 前 **6 個月**內

➡️ 試驗結論**不適用於上述高血栓族群**

---

# 主要與次要終點
## [van Ginkel DJ, et al. NEJM 2025](https://doi.org/10.1056/NEJMoa2407794)

**Primary Composite Endpoint (30 days)**:

- CV death + Stroke + MI + Major vascular complication + Major bleeding
- **Non-inferiority margin: 4%** absolute risk difference

**Secondary**:

- Thromboembolic events (stroke / TIA / MI / systemic embolism)
- Bleeding (any / major / life-threatening)

---

# Baseline Characteristics
## [van Ginkel DJ, et al. NEJM 2025](https://doi.org/10.1056/NEJMoa2407794)

| 項目 | 數值 |
|------|------|
| **N (mITT)** | **858** (431 continue / 427 interrupt) |
| 平均年齡 | **81 歲** |
| 女性 | 34.5% |
| **CHA₂DS₂-VASc** | **4.5**（中-高風險） |
| **DOAC** | **81.9%** |
| VKA | 18.1% |

> 反映當代 TAVI 真實世界 — 高齡、DOAC 為主

---

# 主要終點：未達 Non-Inferiority
## [van Ginkel DJ, et al. NEJM 2025](https://doi.org/10.1056/NEJMoa2407794)

| Outcome | Continuation | Interruption | Risk Diff (95% CI) |
|---------|--------------|--------------|---------------------|
| **Primary composite** | **71 (16.5%)** | **63 (14.8%)** | **+1.7% (−3.1 to +6.6)** |

**P = 0.18 for non-inferiority**

> **95% CI 上界 +6.6% > 4% margin**
> ➡️ **無法宣稱 continuation 不劣於 interruption**

---

# 次要終點：出血明顯增加
## [van Ginkel DJ, et al. NEJM 2025](https://doi.org/10.1056/NEJMoa2407794)

| Outcome | Continuation | Interruption | Risk Diff (95% CI) |
|---------|--------------|--------------|---------------------|
| **Any bleeding** | **31.1%** | **21.3%** | **+9.8% (+3.9 to +15.6)** |

> **持續 OAC 增加近 10% 絕對出血風險**
> 95% CI 完全不跨 0 — 統計顯著

➡️ **NNH ≈ 10**：每 10 位 continuation 病人多 1 位出血

---

# 次要終點：血栓事件相當
## [van Ginkel DJ, et al. NEJM 2025](https://doi.org/10.1056/NEJMoa2407794)

| Outcome | Continuation | Interruption | Risk Diff (95% CI) |
|---------|--------------|--------------|---------------------|
| **Thromboembolic** | **8.8%** | **8.2%** | **+0.6% (−3.1 to +4.4)** |

> 兩組血栓栓塞事件**幾乎相同**
> 95% CI 跨 0 — **沒有觀察到中斷 OAC 帶來的血栓代價**

➡️ 暫停 OAC ≥48 小時並未換來更多 stroke / TIA / MI / systemic embolism

---

# 結果整合

```text
                    ┌──────────────────────────────┐
                    │   30-day outcomes            │
                    └──────────────────────────────┘

Continuation ──── Bleeding 31.1% ────►  +10% 多出血
                                         (NNH ≈ 10)
                  Thromboembolic 8.8% ─► 與 interruption 相當

Interruption ──── Bleeding 21.3% ────►  較少出血
                  Thromboembolic 8.2% ─► 沒有付出血栓代價
```

> **Continuation = 多出血、不減血栓** ➡️ 預設應選擇 interruption

---

# 與既往 Observational 證據對比
## [ESC Press Release 2024](https://www.escardio.org/The-ESC/Press-Office/Press-releases/Oral-anticoagulants-should-be-paused-before-transcatheter-aortic-valve-implantation)

| 證據來源 | 對 continuation 的看法 |
|---------|------------------------|
| Observational studies | 不增加出血、可能減少 stroke |
| **POPular PAUSE TAVI (RCT)** | **顯著增加出血、未減少 stroke** |

> **教訓**：observational data 受 selection bias 影響 — 醫師對高出血風險病人傾向中斷 OAC，反而讓 continuation 看起來「比較安全」

---

# 臨床啟示

> **Pearl 1**：對於符合納入條件之 TAVI 病人，**TAVI 前 ≥48 小時暫停 OAC** 為合理預設策略

> **Pearl 2**：高血栓族群（機械瓣、近期 VTE、AF + 近期 stroke）**不適用**此結論，仍需個案化處理

> **Pearl 3**：DOAC 半衰期短，48 小時中斷通常已足夠 — 結論最適用於 DOAC 病人（佔 81.9%）

> **Pearl 4**：穿刺技術（超音波導引、closure device）優化仍是減少出血的另一個重要槓桿

---

# 侷限性
## [van Ginkel DJ, et al. NEJM 2025](https://doi.org/10.1056/NEJMoa2407794)

- **Open-label**：操作者與病人未盲化
- **歐洲族群為主**：對亞洲（含台灣）外推需小心
- **30 天終點**：無中-長期平衡資料
- **VKA 亞群偏少**（18.1%）：INR-controlled warfarin 病人代表性受限
- **未涵蓋高血栓族群**（機械瓣、近期 VTE/stroke）

---

# Take Home Messages

> 1. **首個 RCT** 挑戰 continuation 假說 — Continuation **不能宣稱 non-inferior**

> 2. 30 天 **any bleeding 31.1% vs 21.3%** — 持續 OAC **多 10% 出血**

> 3. 30 天 **thromboembolic 8.8% vs 8.2%** — 暫停 OAC **沒有血栓代價**

> 4. **預設策略**：TAVI 前 ≥48 小時暫停 OAC（DOAC/VKA），**排除高血栓族群**

---

<!-- _class: ref -->

# 參考文獻

1. van Ginkel DJ, Bor WL, Aarts HM, et al; POPular PAUSE TAVI Investigators. Continuation versus Interruption of Oral Anticoagulation during TAVI. [*N Engl J Med*. 2025;392(5):438-449.](https://doi.org/10.1056/NEJMoa2407794) PMID: 39216096.

2. European Society of Cardiology. Oral anticoagulants should be paused before transcatheter aortic valve implantation. [*ESC Press Release*. 31 Aug 2024.](https://www.escardio.org/The-ESC/Press-Office/Press-releases/Oral-anticoagulants-should-be-paused-before-transcatheter-aortic-valve-implantation)

3. van Ginkel DJ, et al. Periprocedural continuation versus interruption of oral anticoagulant drugs during TAVI: rationale and design of the POPular PAUSE TAVI trial. [*EuroIntervention*. 2023.](https://pubmed.ncbi.nlm.nih.gov/37605804/)

4. ClinicalTrials.gov [NCT04437303](https://clinicaltrials.gov/study/NCT04437303)

5. PCRonline. ESC Congress 2024: POPular PAUSE TAVI. [*PCRonline News*. 2024.](https://www.pcronline.com/News/Whats-new-on-PCRonline/2024/ESC/POPular-PAUSE-TAVI-Continuation-or-interruption-of-oral-anticoagulation-during-TAVI)

6. Sex Differences in TAVI Outcomes — POPular PAUSE TAVI SubAnalysis. [*PMC12684620*.](https://pmc.ncbi.nlm.nih.gov/articles/PMC12684620/)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

[NEJM 原文](https://doi.org/10.1056/NEJMoa2407794) | [ESC Press Release](https://www.escardio.org/The-ESC/Press-Office/Press-releases/Oral-anticoagulants-should-be-paused-before-transcatheter-aortic-valve-implantation)
