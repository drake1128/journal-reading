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
  section.lead a { color: #8ecae6; }
  section.lead blockquote, section.lead blockquote * { color: #2d3436; }
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
footer: '謝慕揚 MD, PhD, FESC | CMR 心肌發炎診斷 Lake Louise 2018 | 2018'
---

<!-- _class: lead -->

# CMR in Nonischemic Myocardial Inflammation

## 非缺血性心肌發炎的 CMR 診斷｜Lake Louise Criteria 2018 更新版

**謝慕揚 MD, PhD, FESC**
資料來源：J Am Coll Cardiol. 2018;72(24):3158–76 | 2026-07-21

[原文連結 (DOI: 10.1016/j.jacc.2018.09.072)](https://doi.org/10.1016/j.jacc.2018.09.072)

---

# 大綱

1. 背景與更新動機
2. 臨床情境與其他檢查
3. CMR 診斷標的（病生理對應）
4. Parametric mapping 原理：T1／T2／ECV
5. 舊版 vs 2018 更新版 LLC 對照
6. T1-based 與 T2-based markers 對照
7. 各種 CMR 組合的診斷效能
8. 臨床應用場景與限制
9. Clinical Pearls

---

<!-- _class: divider -->

# 第一部分：背景與更新動機

---

# 為何要更新 Lake Louise Criteria？

- **2009 原始 LLC I**：3 個標的（edema / hyperemia / necrosis-scar），由 T2W、EGE、LGE 的**訊號強度**評估；**3 選 2** 即高度可能心肌炎
- 原始準確度 78%（sens 67%、spec 91%）；meta-analysis 驗證 accuracy 83%、AUC 83%
- **傳統「訊號強度」的限制**：
  - 發炎轉瀰漫時 T2／EGE 訊號趨均質，難辨局部病灶
  - 以骨骼肌為參考的 global SI ratio → 合併**骨骼肌發炎**易偽陰性
  - 浸潤性心肌病也擴張細胞外空間、增加 gadolinium 攝取

> **契機**：T1／T2 的逐像素 **parametric mapping** 可直接量化 → 據以修訂 LLC

---

<!-- _class: divider -->

# 第二部分：臨床情境與其他檢查

---

# 其他診斷工具的角色（原文 Table 1）

| 檢查 | 角色與限制 |
|------|-----------|
| Troponin/CK、發炎指標 | 不夠敏感；病毒血清學不特異 |
| ECG / Holter | ST-T、傳導、心律不整；不敏感也不特異 |
| Echocardiography | 排除他因、監測 wall motion；非特異 |
| PET | 與 CMR 一致性佳；可近性低、成本高 |
| **CMR** | **唯一非侵入性 biopsy-like 驗證發炎**；ESC 心衰指引 **Class I** |
| **EMB** | 確認**特定病因** gold standard；CMR 定位減少 sampling error |

> ESC（Caforio 2013）：≥1 臨床表現 + ≥1 診斷判準（含 CMR）＝臨床懷疑心肌炎；無症狀者需 ≥2 項

---

<!-- _class: divider -->

# 第三部分：CMR 診斷標的

---

# CMR 標的與病生理對應

| 標的 | 病理 | CMR 表現 | 判準層級 |
|------|------|----------|----------|
| **水腫 edema** | 組織含水↑ | T2↑（T2W 高亮 / T2 map） | 主判準 (T2-based) |
| **充血 / capillary leak** | 細胞外空間擴張 | EGE、native T1↑、ECV↑ | 主判準 (T1-based) |
| **壞死 / 纖維化** | myocyte 損傷、疤痕 | LGE（斑塊、subepicardial/midwall） | 主判準 (T1-based) |
| 功能異常 | functio laesa | wall motion abnormality | **支持判準** |
| 心包異常 | 心包發炎 | 心包積液、增厚、T2↑、pericardial LGE | **支持判準** |

> 心肌炎 LGE 好發 **basal–mid inferolateral wall**、subepicardial（≠ 缺血的 subendocardial）

---

<!-- _class: divider -->

# 第四部分：Parametric Mapping 原理

---

# T1 / T2 / ECV：各自的角色

| 參數 | 反映 | 特性 | 臨床價值 |
|------|------|------|----------|
| **T2 mapping** | 水腫（自由水↑） | 對**急性發炎較特異**；可分辨活動 vs 已癒合 | 標示「正在發炎」；rule-out 佳 |
| **Native T1 mapping** | 細胞內外水腫、充血、壞死、纖維化 | 高度**敏感但不特異**（慢性纖維化亦↑） | 病變心肌敏感；NPV 92%，rule-out 佳 |
| **ECV** | 擴張的細胞外空間 | 捕捉 LGE 看不到的瀰漫變化 | 附加 biomarker |

- 常用序列：T1 → **MOLLI / ShMOLLI / SASHA**；T2 → gradient/spin echo multiecho
- **須在地驗證**；閾值 method-specific、為 sensitivity/specificity 取捨（參考 SCMR / EACVI）

---

# 互補性：MyoRacer 試驗（EMB 為標準）

| 時相 | Native T1 | T2 mapping |
|------|-----------|------------|
| **急性（≤14 天）** | 準確度最高 **81%** | 佳 |
| **慢性（>14 天）** | 降到 **45%** | **唯一達可接受準確度 73%** |

> **結論**：**T1-based 與 T2-based 需並用**——急性靠 T1、慢性靠 T2 mapping；此即 2018 更新版要求「兩類各 ≥1 項」的證據基礎

---

<!-- _class: divider -->

# 第五部分：舊版 vs 2018 更新版 LLC

---

# 舊版 vs 2018 更新版 LLC（原文 Table 3）

| 診斷標的 | 原始 LLC I（3 選 2） | **2018 LLC II（2 選 2）** |
|----------|---------------------|---------------------------|
| **水腫 (T2-based)** | T2W：regional 高 SI 或 global SI ratio ≥2.0 | T2W 判準 **或** **T2 relaxation time↑** |
| **相關損傷 (T1-based)** | EGE ratio ≥4.0（或另計 LGE） | **native T1↑ 或 ECV↑ 或 LGE**（非缺血分布） |
| **陽性判定** | T2W／EGE／LGE **≥2 項** | T2-based 與 T1-based **各 ≥1 項** |
| 支持：心包發炎 | cine 心包積液 | 積液 或 LGE/T1/T2 map 心包高訊號 |
| 支持：LV 功能 | systolic wall motion abnormality | systolic wall motion abnormality |

> Regional = ≥10 相鄰像素；閾值用已發表/在地常規值；**T1 mapping 為 EGE 的 alternative**

---

# 判定邏輯與細則

```text
懷疑急性/活動性心肌發炎（有臨床 pre-test probability）
        |
   ┌────┴─────────────────────────┐
   ▼                              ▼
 T2-based 主判準              T1-based 主判準
 （水腫）                     （相關損傷）
 T2W 高 SI / SI ratio≥2.0     native T1↑ / ECV↑
 或 T2 map T2↑                或 LGE（非缺血分布）
   |                              |
   └──── 兩類各 ≥1 陽性 ──────────┘
                |
        強證據支持急性心肌發炎（特異度最高）

僅一類陽性 → 適當情境仍可支持，但特異度較低
```

> T1 mapping 與 LGE 配對時，T1 異常區應**超出** LGE 範圍；先排除 ACS

---

<!-- _class: divider -->

# 第六部分：T1-based vs T2-based markers

---

# T1-based 與 T2-based markers 對照

| 面向 | **T2-based** | **T1-based** |
|------|--------------|--------------|
| 方法 | T2W、**T2 mapping** | **LGE、native T1、ECV** |
| 反映病理 | 心肌**水腫** | T1/ECV：水腫+充血+壞死+纖維化；LGE：壞死/疤痕/部分急性水腫 |
| 對急性的特異性 | **較特異** | **較不特異**（慢性纖維化、缺血、浸潤亦↑） |
| 主要價值 | 標示「正在發炎」；rule-out | 敏感偵測病變/不可逆損傷；rule-out |
| 更新版角色 | **必備一項**（水腫） | **必備一項**（損傷） |

> LGE 標示的是擴張的細胞外空間（壞死/纖維化/水腫），**本身不代表「正在發炎」**

---

<!-- _class: divider -->

# 第七部分：各種組合的診斷效能

---

# 診斷效能：AUC\*（原文 Table 2 / Figure 1）

| 判準 / 組合 | Median AUC\* (%) | 研究×病例 |
|--------------|-------------------|-----------|
| T2W imaging | 73 (58–100) | 13 × 981 |
| LGE | 83 (53–96) | 14 × 1,073 |
| **T1 mapping** | **89 (71–99)** | 9 × 682 |
| T2 mapping | 80 (73–86) | 6 × 449 |
| 原始 Lake Louise Criteria | 84 (57–90) | 8 × 630 |
| **T2 mapping + LGE** | **90 (83–97)** | 2 × 120 |
| **T1 mapping + LGE** | **96 (82–97)** | 5 × 350 |

> 含至少一項 **mapping** 的組合 AUC\* 整體偏高；但新組合證據較少、異質性高，仍待驗證。**Gadolinium-free**（T2-based＋T1 mapping）適合不宜對比劑者

---

<!-- _class: divider -->

# 第八部分：臨床應用與限制

---

# 特定病因的 CMR 特徵（原文 Table 5）

| 時相 | T2 | T1 | LGE |
|------|----|----|-----|
| **急性 (active)** | ↑ | ↑ | ± |
| **慢性 (chronic)** | ±/↑ | ±/↑ | ±（ECV 提供附加資訊） |
| **已癒合 (healed)** | ±/↓ | ±/↑ | ± |

- **Infarct-like 急性心肌炎**：年輕男性、廣泛水腫+inferolateral 壞死；LLC 敏感度/特異度皆高
- **Giant cell**：猛爆、需及早免疫抑制｜**Eosinophilic**：瀰漫 subendocardial LGE
- **Sarcoidosis**：native T1 mapping 為最佳鑑別、偵測亞臨床侵犯
- 自體免疫（RA/SSc/SLE）、pheochromocytoma/Takotsubo、Chagas、HIV、ICI-mediated

---

# 限制與注意事項

- **僅適用於懷疑「活動性/急性」發炎**；慢性期敏感度下降
- **native T1/ECV 不特異**：慢性纖維化、amyloidosis、缺血皆↑ → 判讀 T1 延長須警覺非發炎病變
- **T2W**：訊噪比低、受心律不整/運動影響；合併骨骼肌發炎易偽陰性（參考 serratus anterior）
- **EGE**：影像一致性差，多數中心不常規用；移除 EGE 不顯著降低準確度
- **LGE 不可單獨用**：輕症不敏感、對「活動性」不特異
- **Mapping 仍在標準化**：閾值 method-specific、須在地驗證；缺跨廠商標準 phantom
- 多數研究**異質性高、偏差風險高**

---

<!-- _class: divider -->

# 第九部分：Clinical Pearls

---

# Clinical Pearls（1/2）

> **Pearl 1｜核心變革**：從「3 選 2」改為「**2 選 2**」——至少 1 個 **T2-based**（水腫）＋ 至少 1 個 **T1-based**（相關損傷），提高**特異度**

> **Pearl 2｜mapping 入列**：T2 mapping 可替代 T2W；**native T1 或 ECV** 可替代 EGE（T1 mapping 為 EGE 的 alternative）

> **Pearl 3｜T2 特異、T1 敏感**：T2-based 對「正在發炎」較**特異**；T1/ECV 敏感但不特異。急性靠 T1、慢性靠 T2 mapping，**互補缺一不可**

---

# Clinical Pearls（2/2）

> **Pearl 4｜組合效能**：T1 mapping+LGE ≈ 96%、T2 mapping+LGE ≈ 90%；**gadolinium-free**（T2-based＋T1 mapping）適合不宜對比劑者

> **Pearl 5｜支持判準**：心包積液/發炎與 LV wall motion abnormality 屬**支持性**；單有心包積液不能證明 pericarditis

> **Pearl 6｜判讀提醒**：Regional = ≥10 相鄰像素；用已發表/在地常規值；T1 與 LGE 配對時 T1 異常區應超出 LGE；先排除 ACS

---

<!-- _class: small-text -->

# 參考文獻

1. Ferreira VM, Schulz-Menger J, Holmvang G, et al. CMR in Nonischemic Myocardial Inflammation: Expert Recommendations. [*J Am Coll Cardiol*. 2018;72(24):3158–76.](https://doi.org/10.1016/j.jacc.2018.09.072)
2. Friedrich MG, Sechtem U, Schulz-Menger J, et al. CMR in myocarditis: a JACC White Paper. [*J Am Coll Cardiol*. 2009;53(17):1475–87.](https://doi.org/10.1016/j.jacc.2009.02.007)
3. Kotanidis CP, Bazmpani MA, Haidich AB, et al. Diagnostic Accuracy of CMR in Acute Myocarditis: A Systematic Review and Meta-Analysis. [*JACC Cardiovasc Imaging*. 2018;11(11):1583–90.](https://doi.org/10.1016/j.jcmg.2017.12.008)
4. Ferreira VM, Piechnik SK, Dall'Armellina E, et al. T1 Mapping for the diagnosis of acute myocarditis using CMR. [*JACC Cardiovasc Imaging*. 2013;6(10):1048–58.](https://doi.org/10.1016/j.jcmg.2013.03.008)
5. Lurz P, Luecke C, Eitel I, et al. Comprehensive CMR in Patients With Suspected Myocarditis: MyoRacer-Trial. [*J Am Coll Cardiol*. 2016;67(15):1800–11.](https://doi.org/10.1016/j.jacc.2016.02.013)
6. Caforio ALP, Pankuweit S, Arbustini E, et al. ESC Working Group position statement on myocarditis. [*Eur Heart J*. 2013;34(33):2636–48.](https://doi.org/10.1093/eurheartj/eht210)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

*本文件僅供醫療專業人員教學參考*
