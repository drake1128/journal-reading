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
footer: '謝慕揚 MD, PhD, FESC | DB-OTO Gene Therapy | 2026'
---

<!-- _class: lead -->

# DB-OTO Gene Therapy for Inherited Deafness

## 基因治療恢復先天性耳聾 — CHORD Trial

**謝慕揚 MD, PhD, FESC**
資料來源：[*N Engl J Med*. 2026;394:1074-83](https://doi.org/10.1056/NEJMoa2400521)

---

# 大綱

1. 疾病背景與 DB-OTO 設計
2. 研究方法
3. 主要結果
4. 安全性
5. 臨床意義與討論
6. 重點整理

---

<!-- _class: divider -->

# 第一部分：疾病背景與 DB-OTO 設計

---

# OTOF-Related Deafness

- 先天性耳聾影響美國每 1000 名新生兒中 **1.7 名**
- 主要由基因缺陷造成
- **OTOF** 基因 biallelic variants → 占先天性遺傳性耳聾 **1-3%**
- Otoferlin = inner hair cells 的 **calcium sensor**
- 缺乏 otoferlin → **synaptic transmission 中斷** → profound deafness

## 目前治療
- **無藥物治療** — 終身 cochlear implants
- Cochlear implants 的限制：speech understanding ↓、music appreciation ↓

---

# DB-OTO 基因治療設計

```text
DB-OTO Gene Therapy
│
├── Vector:     Dual AAV1 (OTOF cDNA 太大，需兩個 AAV)
├── Promoter:   Myo15 (hair cell-specific)
├── Payload:    Human OTOF cDNA → otoferlin protein
├── Delivery:   Intracochlear infusion (round window approach)
├── Dose:       7.2 × 10¹² vector genomes / ear (240 μL)
│
└── Mechanism:
    Inner hair cell → 表現 otoferlin
    → 恢復 synaptic vesicle fusion
    → 恢復與 cochlear nerve 的 synaptic transmission
    → 聽力恢復
```

---

<!-- _class: divider -->

# 第二部分：研究方法

---

# CHORD Trial 設計

- **Open-label, single-group, phase 1-2** registrational study
- 收案：12 名 OTOF biallelic variants 的先天性耳聾兒童
- **Part A**：單耳治療 (n=9)
- **Part B**：雙耳同時治療 (n=3)
- 追蹤：48 週 + 每年至 4 年

## 主要終點

| 終點 | 定義 |
|------|------|
| **Primary** | Week 24: PTA average threshold **≤ 70 dB HL** |
| **Key secondary** | Week 24: ABR click threshold **≤ 90 dB nHL** |

---

# 聽力閾值參考

| dB HL | 聽力能力 | 臨床意義 |
|-------|---------|---------|
| ≤ 25 | **Normal hearing** | 可聽到耳語 |
| ≤ 45 | 可聽到 soft speech | 日常對話無障礙 |
| ≤ 60 | 可聽到 conversational speech | 基本溝通 |
| ≤ 70 | **Primary endpoint 閾值** | **可避免 cochlear implant** |
| ≤ 80 | 可聽到 loud speech | 需放大音量 |
| > 90 | **Profound deafness** | 無法聽到割草機 |

> 從 > 90 dB HL 到 ≤ 25 dB HL = **從完全聾到正常聽力**

---

<!-- _class: divider -->

# 第三部分：主要結果

---

# Primary Endpoint — 75% 達標

| 結果 | 數據 |
|------|------|
| **Primary: PTA ≤ 70 dB HL** | **9/12 (75%)** |
| 95% CI | 43-95% |
| P value | **1.1 × 10⁻¹³** |
| **Key secondary: ABR ≤ 90 dB nHL** | **9/12 (75%)** |
| 可聽到 soft speech (≤ 45 dB HL) | 6/12 (50%) |
| **Normal hearing (≤ 25 dB HL)** | **3/12 (25%)** |

| 分組 | 達標率 |
|------|--------|
| Part A 單耳 | 6/9 (67%) |
| Part B 雙耳 | **3/3 (100%)** |

---

# 個案亮點

## Participant 1（10 月大 → 27 月大追蹤）
- 治療耳達 **normal hearing (18.75 dB HL)**
- 語言發展「much improvement」
- 可偵測遠距聲音（cochlear implant 無法達成）

## 16 歲青少年 (2 名)
- 均有聽力改善 → **挑戰「僅幼兒有效」的觀點**

## Participant 3（唯一無反應者）
- 後續接受 cochlear implant **仍有效** → DB-OTO 不妨礙後續植入

---

# 持續性 — 效果穩定至 72 週

- 8 名追蹤超過 24 週的患者
- 聽力均**穩定或持續改善**至 72 週
- Inner hair cells 為 non-dividing cells → 基因治療效果預期持久

## 局部發現
- 2 名患者在高頻 (≥ 4 kHz) 有局部聽力下降
- 對應 round window 附近的 cochlear region
- 對 speech perception 無臨床顯著影響

---

<!-- _class: divider -->

# 第四部分：安全性

---

# 安全性結果

| 項目 | 結果 |
|------|------|
| Total adverse events | 67 |
| Surgery-related | 17 |
| Serious adverse events | **2** |
| SAE 1 | Mastoiditis (對側 cochlear implant 相關) |
| SAE 2 | Walking instability (varicella 接種後) |
| 兩者均完全緩解 | ✓ |
| 持續性前庭不良反應 | **無** |
| 因 AE 退出研究 | **無** |

> **安全性良好**：無 DB-OTO 直接相關的 serious adverse events

---

<!-- _class: divider -->

# 第五部分：臨床意義

---

# 歷史性突破 — 感覺功能的完全恢復

| 比較 | 聽覺 (DB-OTO) | 視覺 (Luxturna) |
|------|--------------|----------------|
| 正常化 | **3/12 normal hearing** | 仍需輔助裝置 |
| 細胞基質 | Hair cells 完整 | 視網膜退化 |
| 裝置需求 | **可完全脫離 cochlear implant** | 仍依賴輔助 |
| 持續性 | 72 週穩定 | 效果可能衰退 |

> **首次透過 gene therapy 實現感覺功能的完全正常化**

---

# Clinical Pearls

> **Pearl 1**：Gene therapy 成功的關鍵 = **細胞結構完整** — OTOF 患者的 inner hair cells 未退化，是基因添加治療的理想標靶

> **Pearl 2**：手術遞送方式與 **cochlear implant 手術相同**（round window approach），技術成熟

> **Pearl 3**：Preexisting anti-AAV1 antibodies 未影響療效 → 暗示**重複治療**和**不需排除有抗體者**的可能性

> **Pearl 4**：16 歲患者仍有效 → **治療窗口比預期寬廣**

---

<!-- _class: divider -->

# 重點整理

---

# Take-Home Messages

1. **DB-OTO = dual AAV1 gene therapy**，遞送 otoferlin 至 inner hair cells
2. **75% (9/12) 達到可避免 cochlear implant 的聽力水平**
3. **25% (3/12) 達到 normal hearing** — 從完全聾到可聽見耳語
4. 效果在 **72 週追蹤中穩定或持續改善**
5. **安全性良好**，無 DB-OTO 直接相關的 SAE
6. 精準醫療里程碑：**首次 gene therapy 完全恢復感覺功能**

---

<!-- _class: small-text -->

# 參考文獻

1. Valayannopoulos V, et al. DB-OTO Gene Therapy for Inherited Deafness. [*N Engl J Med*. 2026;394:1074-83.](https://doi.org/10.1056/NEJMoa2400521)
2. Lv J, et al. AAV1-hOTOF gene therapy for DFNB9. [*Lancet*. 2024;403:2317-25.](https://doi.org/10.1016/S0140-6736(23)02874-X)
3. Russell S, et al. Voretigene neparvovec (Luxturna). [*Lancet*. 2017;390:849-60.](https://doi.org/10.1016/S0140-6736(17)31868-8)

---

<!-- _class: lead -->

# 謝謝聆聰

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
