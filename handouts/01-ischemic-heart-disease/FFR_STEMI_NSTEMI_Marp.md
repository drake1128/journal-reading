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
footer: '謝慕揚 MD, PhD, FESC | FFR in STEMI/NSTEMI | 2026'
---

<!-- _class: lead -->

# FFR During STEMI & NSTEMI
## 急性心肌梗塞中 FFR 的角色與爭議

**謝慕揚 MD, PhD, FESC**
多篇文獻綜合整理 | 2026-03-03
[FULL REVASC (NEJM 2024)](https://doi.org/10.1056/NEJMoa2314149) | [FLOWER-MI (NEJM 2021)](https://doi.org/10.1056/NEJMoa2104650)

---

# 大綱

1. 臨床問題：為什麼要討論 FFR in acute MI？
2. FFR 在急性 MI 的可靠性
3. FFR-Guided CR vs Culprit-Only — 四大 RCTs
4. FFR-Guided vs Angiography-Guided
5. Complete Revascularization 時機
6. Guidelines 與臨床實務
7. Take-Home Messages

---

<!-- _class: divider -->

# 第一部分：臨床問題

---

# STEMI + Multivessel Disease

- 約佔 STEMI 的 **40-50%**
- Primary PCI 處理 culprit 後，**non-culprit lesions 怎麼辦？**

### 三個核心問題

1. **要不要做** complete revascularization？→ 已解決 (Class I)
2. **什麼時候做**？Immediate vs staged？→ 仍有爭議
3. **怎麼選** non-culprit lesion？FFR vs angiography？→ **核心爭議**

---

# 術語定義

| 術語 | 定義 |
|------|------|
| **Culprit lesion** | 造成急性 MI 的罪犯病灶 |
| **Non-culprit lesion** | 其他有 stenosis 但非造成此次 MI |
| **Complete revascularization (CR)** | 處理 culprit + 所有 significant non-culprit |
| **Culprit-only** | 僅處理 culprit |
| **FFR-guided CR** | FFR ≤ 0.80 → PCI non-culprit |
| **Angiography-guided CR** | Stenosis ≥ 70% → PCI non-culprit |

---

<!-- _class: divider -->

# 第二部分：FFR 在急性 MI 可靠嗎？

---

# Culprit Vessel — FFR 不可靠

### 不可靠的機制

```text
Acute MI → Microvascular obstruction (MVO)
    ├── Distal embolization + thrombus
    ├── Myocardial stunning → O₂ demand ↓
    ├── Vasospasm
    └── Attenuated adenosine response

結果：FFR 被高估 (false negative)
→ Significant lesion 誤判為 FFR > 0.80
```

### Cuculi et al. (2014) — IRA 的 FFR 變化

| 時間 | IRA FFR | 說明 |
|------|---------|------|
| Acute | **0.93** | 高估 (false negative) |
| 6 months | **0.89** | 微血管恢復後真正值 |

> **Rule：絕對不要用 FFR 評估 culprit vessel**

---

# Non-Culprit Vessels — 大致可靠

### Ntalianis et al. (2010) — 里程碑研究

- 101 AMI patients, 112 non-culprit lesions
- **Acute FFR vs 35 天後：0.77 ± 0.13 vs 0.77 ± 0.13 (p = NS)**
- Non-culprit 的 FFR 在急性期與恢復期**不變**

### 但有注意事項

- **~10% reclassification rate** 跨越 FFR 0.80 threshold
- **> 5 天後**測量最可靠 (ESC 建議)
- 大面積 MI 或 hemodynamic compromise → 即使 non-culprit 也可能受影響

> **Pearl**：Non-culprit FFR 約 90% concordance — 可用但不完美

---

<!-- _class: divider -->

# 第三部分：FFR-Guided CR vs Culprit-Only

---

# DANAMI-3-PRIMULTI (2015)

**Lancet 2015** | n = 627 | STEMI + multivessel disease
FFR-guided staged CR vs culprit-only | 追蹤 27 months

| 結果 | CR | Culprit-only | HR | P |
|------|----|--------------|----|---|
| **Primary composite** | **13%** | **22%** | **0.56** | **0.004** |
| Death | 5.4% | 6.0% | NS | NS |
| MI | 2.4% | 4.4% | NS | NS |

- **31%** 的 CR 組患者經 FFR 不需 non-culprit intervention
- 10 年追蹤 (2025)：CR 持續有益 (22% vs 31%)

---

# Compare-Acute (2017)

**NEJM 2017** | n = 885 | STEMI + multivessel disease
FFR-guided CR **during index procedure** vs culprit-only | 12 months

| 結果 | CR | Culprit-only | HR | P |
|------|----|--------------|----|---|
| **Primary composite** | **7.8%** | **20.5%** | **0.35** | **< 0.001** |
| Revascularization | 6.1% | 17.5% | — | — |

- **關鍵發現**：~44% angiographically significant lesions 有 FFR > 0.80
- → Angiography **高估** non-culprit lesion significance

---

# FULL REVASC (2024) — 最大型試驗

**NEJM 2024** | n = 1,542 | STEMI/high-risk NSTEMI | Scandinavia
FFR-guided CR vs culprit-only | **追蹤 4.8 年**（最長）

| 結果 | CR | Culprit-only | HR | P |
|------|----|--------------|----|---|
| **Primary composite** | **19.0%** | **20.4%** | **0.93** | **0.53** |
| Death or MI | 16.1% | 14.5% | 1.12 | NS |

> **結論：FFR-guided CR 無顯著獲益**
> Death or MI 甚至數值上較差
> → 與 DANAMI-3-PRIMULTI、Compare-Acute **截然相反**

---

# FIRE Trial (2023) — 老年患者

**NEJM 2023** | n = 1,445 | ≥ 75 歲 MI | Italy, Spain, Poland
**Physiology-guided** (FFR/iFR/QFR) CR vs culprit-only | 12 months

| 結果 | CR | Culprit-only | HR |
|------|----|--------------|----|
| **Primary composite** | **15.7%** | **21.0%** | **0.73** |
| CV death | ↓ 36% | — | — |
| MI | ↓ 38% | — | — |

- NNT = **19**
- 使用多種 physiology tools（不僅 FFR）

---

# 四大 FFR-Guided CR vs Culprit-Only 總覽

| Trial | N | 追蹤 | HR | P | 結論 |
|-------|---|------|----|---|------|
| **DANAMI-3** | 627 | 27 mo | **0.56** | 0.004 | CR 較好 |
| **Compare-Acute** | 885 | 12 mo | **0.35** | < 0.001 | CR 較好 |
| **FIRE** | 1,445 | 12 mo | **0.73** | 0.02 | CR 較好 |
| **FULL REVASC** | 1,542 | 4.8 yr | 0.93 | 0.53 | **無差異** |

> **The FFR Paradox**：為何最大型、最長追蹤的試驗反而陰性？

---

# 為何 FULL REVASC 是陰性？

### 可能解釋

1. **FFR false negative in acute MI**
   - 微血管障礙 → FFR 偏高 → 遺漏該治療的 lesions
2. **長期追蹤 (4.8 yr)** 暴露更多 late events
3. **Culprit-only 組的進步**
   - 更好的藥物治療 (high-dose statin, DAPT)
4. **Sample size & power**
   - Event rate 低於預期

> **核心矛盾**：FFR 可能讓你「少做 stent」（避免 over-treatment），但也可能讓你「漏掉該治的」（under-treatment）

---

<!-- _class: divider -->

# 第四部分：FFR vs Angiography Guidance

---

# FLOWER-MI (2021)

**NEJM 2021** | n = 1,163 | STEMI | France
FFR-guided vs **angiography-guided (≥ 70%)** staged CR | 12 months

| 結果 | FFR-guided | Angiography | HR | P |
|------|-----------|-------------|-----|---|
| **Primary** | **5.5%** | **4.2%** | **1.32** | **0.31** |

> **FFR 未優於 angiography** — 數值上甚至更差

---

# FRAME-AMI (2023)

**Eur Heart J 2023** | n = 562 | AMI (STEMI + NSTEMI) | Korea
FFR-guided vs **angiography-guided (> 50%)** | 3.5 years

| 結果 | FFR-guided | Angiography | HR | P |
|------|-----------|-------------|-----|---|
| **Primary** | **7.4%** | **19.7%** | **0.43** | **0.003** |
| Death | 2.1% | 8.5% | — | — |
| MI | 2.5% | 8.9% | — | — |

> **FFR 顯著優於 angiography** — 與 FLOWER-MI 矛盾！

---

# 為何 FLOWER-MI vs FRAME-AMI 矛盾？

| 特徵 | FLOWER-MI | FRAME-AMI |
|------|-----------|-----------|
| **Angiography 閾值** | **≥ 70%** | **> 50%** |
| 國家 | France | Korea |
| 追蹤 | 12 months | 3.5 years |
| FFR 結果 | 無優勢 | **FFR 較好** |

### 關鍵差異

- FRAME-AMI 的 angiography 組用 **> 50%** → 更多 over-treatment
- FLOWER-MI 的 angiography 組用 **≥ 70%** → 已是合理閾值
- **結論**：FFR 的價值在於避免對 50-69% 的 intermediate lesions over-treatment

---

<!-- _class: divider -->

# 第五部分：時機與 Guidelines

---

# Complete Revascularization 時機

| Trial | 比較 | 結果 | 結論 |
|-------|------|------|------|
| **COMPLETE** (n=4,041) | Staged CR vs culprit-only | HR 0.74 (p=0.004) | CR 有益 (angio-guided) |
| **MULTISTARS-AMI** (n=840) | Immediate vs staged | 8.5% vs 16.3% | **Immediate 較好** |
| **OPTION-STEMI** (n=994) | Immediate vs staged | 13% vs 11% | **Non-inferiority 未成立** |

> **Pearl**：Hemodynamically stable → immediate 或 staged 均可
> Killip ≥ II → **staged 較安全** (OPTION-STEMI: HR 1.79)

---

# Guidelines 總整理

### ESC 2023 ACS Guidelines

| 建議 | Class | Level |
|------|-------|-------|
| STEMI + multivessel → complete revascularization | **I** | **A** |
| Timing: index or staged ≤ 45 days | I | A |
| FFR for non-culprit assessment | **IIb** | — |

### ACC/AHA 2025 ACS Guidelines

| 建議 | Class |
|------|-------|
| Treat significant non-culprit in multivessel ACS | **1** |
| FFR 非 mandatory | — |

> **重點：Guidelines 推薦 CR，但不要求 FFR guidance**

---

<!-- _class: divider -->

# 第六部分：實務建議

---

# 何時使用 FFR？

| 場景 | 建議 |
|------|------|
| Culprit vessel | **不要用 FFR** |
| Non-culprit, ≥ 70% stenosis | **Angiography 已足夠** → 直接 PCI |
| **Non-culprit, 50-69%** | **最適合用 FFR** |
| Non-culprit, < 50% | Medical therapy |
| 測量時機 | **> 5 天後最可靠** |
| Unstable patients | 考慮 **iFR** (免 adenosine) |

---

# 臨床決策流程

```text
STEMI/NSTEMI + Multivessel Disease
    |
    ├── Primary PCI: 處理 culprit (不用 FFR)
    |
    ├── Non-culprit lesion:
    |   ├── ≥ 70% → 安排 PCI (angiography-guided)
    |   ├── 50-69% → FFR/iFR 評估
    |   |     ├── ≤ 0.80 → PCI
    |   |     └── > 0.80 → Medical therapy
    |   └── < 50% → Medical therapy
    |
    └── Timing:
        ├── Stable → immediate 或 staged
        └── Killip ≥ II → staged (較安全)
```

---

# Take-Home Messages

1. **Complete revascularization 有益** (Class I, Level A)
2. **Angiography-guided CR 已有充分證據** (COMPLETE, n = 4,041)
3. **FFR-guided CR 證據互相矛盾**
   - 支持：DANAMI-3, Compare-Acute, FIRE, FRAME-AMI
   - 不支持：**FULL REVASC, FLOWER-MI**
4. **FFR 不用在 culprit vessel** (MVO → false negative)
5. **FFR 最適合 intermediate lesions (50-69%)**
6. **> 5 天後測量最可靠**
7. **The FFR Paradox**：少做 stent (好) vs 漏掉該治的 (壞)

---

<!-- _class: small-text -->

# 參考文獻 (1/2)

1. Engstrom T, et al. DANAMI-3-PRIMULTI. [*Lancet.* 2015;386:665-671.](https://doi.org/10.1016/S0140-6736(15)60648-1)
2. Smits PC, et al. Compare-Acute. [*NEJM.* 2017;376:1234-1244.](https://doi.org/10.1056/NEJMoa1701067)
3. Puymirat E, et al. FLOWER-MI. [*NEJM.* 2021;385:297-308.](https://doi.org/10.1056/NEJMoa2104650)
4. Lee JM, et al. FRAME-AMI. [*Eur Heart J.* 2023;44:473-484.](https://doi.org/10.1093/eurheartj/ehac763)
5. Mehta SR, et al. COMPLETE. [*NEJM.* 2019;381:1411-1421.](https://doi.org/10.1056/NEJMoa1907775)
6. Bohm F, et al. FULL REVASC. [*NEJM.* 2024;390:1481-1492.](https://doi.org/10.1056/NEJMoa2314149)
7. Briguori C, et al. FIRE. [*NEJM.* 2023;389:889-898.](https://doi.org/10.1056/NEJMoa2300468)

---

<!-- _class: small-text -->

# 參考文獻 (2/2)

8. Stahli BE, et al. MULTISTARS-AMI. [*NEJM.* 2023;389:1368-1379.](https://doi.org/10.1056/NEJMoa2307823)
9. Ahn Y, et al. OPTION-STEMI. [*Lancet.* 2025.](https://doi.org/10.1016/S0140-6736(25)01529-6)
10. Ntalianis A, et al. FFR in Non-Culprit Lesions. [*JACC Cardiovasc Interv.* 2010;3:1274-1281.](https://doi.org/10.1016/j.jcin.2010.08.025)
11. Cuculi F, et al. MVO and FFR After STEMI. [*JACC Cardiovasc Interv.* 2014;7:1440-1449.](https://doi.org/10.1016/j.jcin.2014.07.007)
12. Byrne RA, et al. 2023 ESC ACS Guidelines. [*Eur Heart J.* 2023;44:3720-3826.](https://doi.org/10.1093/eurheartj/ehad191)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
