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
footer: '謝慕揚 MD, PhD, FESC | 3D-CT Planning for Ostial RCA PCI | 2026'
---

<!-- _class: lead -->
# 3D-CT 術前規劃<br>開口型 RCA 病灶的 PCI
## Three-Dimensional CT for Preprocedural Planning of PCI for Ostial RCA Lesions — A Randomized Controlled Pilot Trial

**謝慕揚 MD, PhD, FESC** | 2026-06-26

[Circ Cardiovasc Interv 2025;18:e013584 — DOI 連結](https://doi.org/10.1161/CIRCINTERVENTIONS.123.013584)

---

# 臨床問題：開口型 RCA 為何難做？

開口型右冠狀動脈 (ostial right coronary artery, ostial RCA)：開口 5 mm 內 >70% 狹窄

即使用第二代藥物釋放支架 (drug-eluting stent, DES)，預後仍差：

- 1 年目標病灶失敗 (target lesion failure, TLF) ≈ **4.49%**
- 3 年目標病灶再血管化 (target lesion revascularization, TLR) 高達 **14.2%**

**四大難處**：漏斗狀 (funnel-shaped) 開口形態 · 回彈 (recoil) · 嚴重鈣化 → 膨脹不全 · 地理性錯位 (geographic mismatch) 約 **50–54%**

---

# 地理性錯位 (Geographic Mismatch) 的後果

| 錯位型態 | 機轉 | 後果 |
|----------|------|------|
| 支架突入主動脈 (protruding struts) | 支柱裸露於主動脈血流 | 血小板活化、血栓、再次接管困難 |
| 支架植入過遠 (too-distal) | 開口病灶未覆蓋 | 病灶裸露、再狹窄 |

> 過去資料顯示地理性錯位使 TLR **增為 3 倍**。準確顯像主動脈-開口平面（避免縮短 foreshortening / 重疊 overlap）是關鍵——但經驗術者常選到縮短視角。

---

<!-- _class: divider -->
# 研究設計

## Single-center · Open-label · Core-lab–blinded RCT

### NCT05172323

---

# 研究設計

## [Circ Cardiovasc Interv 2025;18:e013584](https://doi.org/10.1161/CIRCINTERVENTIONS.123.013584)

| 項目 | 內容 |
|------|------|
| 設計 | 單中心、前瞻、開放標籤、核心實驗室盲性 RCT（先導性 pilot） |
| 中心 | Ziekenhuis Oost-Limburg, Genk, Belgium |
| 收案 | 30 位主動脈-開口型 RCA 病灶（>70%，開口 5 mm 內） |
| 隨機 | 1:1 → 3DCT 導引 vs 血管攝影導引 PCI；依鈣化修飾分層 |
| 術者 / 期間 | 6 位 / 2022.01–2023.02 |

**假說**：個別化術前三維電腦斷層 (three-dimensional CT, 3DCT) 決定最佳 C-arm 角度 → 預防地理性錯位、減少對比劑與輻射。

---

# 3DCT 工作流程（Mimics, Materialise）

```text
心臟冠狀 CT（PCI 前 1 週–30 天；flash mode, SOMATOM Force）
    |
AI CT-Heart 3D 重建 + 鈣化分割
    |
量測 MLA + 鈣化弧度 (calcium arc)
    |
中心線 / best-fit 直徑與長度 → 候選支架尺寸與長度
    |
最佳 C-arm 角度：4 輔助點 → 2 垂直平面
    → S 曲線交會 → 垂直開口視角
```

與 3mensio 軟體交叉驗證，相關性良好。

---

# 介入流程與 IVUS

- **對照組角度**：術者自行決定 (operator discretion)
- **血管內超音波 (intravascular ultrasound, IVUS)**：兩組常規（OPTICROSS HD 60 MHz, 0.5 mm/s）；支架尺寸/長度兩組均依 IVUS
- **禁用**：Szabo technique、ostium locator、植入時同步 IVUS
- **主要終點**：術後 IVUS、核心實驗室盲性判讀

> **主要終點 = 無地理性錯位的病人百分比**：開口完全覆蓋 **且** 主動脈-開口交界與最近端突出支柱間 ≤3 mm。

---

# 主要結果：定位

## [DOI 連結](https://doi.org/10.1161/CIRCINTERVENTIONS.123.013584)

| 結果 | 3DCT (n=15) | 對照 (n=15) | P |
|------|-------------|-------------|---|
| 達最佳支架位置 | 全部 | — | — |
| 地理性錯位 | 0 | 5 (33%) | — |
| **無錯位百分比** | **100%** | **67.7%** | 0.06 |
| 支架距開口 ≤1 mm (post-hoc) | 11 (73%) | 5 (33%) | 0.03 |

---

# 主要結果：投影角度

3DCT 算出的最佳角度，比術者直覺選的更「極端」：

| 組別 | 平均角度 | P |
|------|---------|---|
| 介入組 (3DCT) | 左前斜 LAO 61.5±13.4（≈ LAO 61 / CRA 13） | <0.0001 |
| 對照組 | LAO 34.7±9.2（≈ LAO 35 / CRA 9） | |

> 先前回溯性研究最佳角度約 LAO 79 / CRA 41——個別化角度勝過通用 LAO。

---

# 次要結果：對比劑、輻射、時間皆降

## [DOI 連結](https://doi.org/10.1161/CIRCINTERVENTIONS.123.013584)

| 指標 | 3DCT | 對照 | P |
|------|------|------|---|
| 術中對比劑 (mL) | 60.7±21.5 | 116.7±37.5 | <0.0001 |
| 輻射 (mGy) | 251.9 (195.6–393.3) | 487.3 (407.4–634.0) | 0.026 |
| 手術時間 (min) | 37 (24–42) | 50 (42.5–67.5) | 0.009 |
| 病灶準備前 cine 取像 | 1 (1–1) | 4 (2–5) | 0.0002 |

**對比劑 / 輻射 / 時間約減 48%；手術約縮短 13 分鐘。**

---

# 次要結果：安全與整體對比劑

- **總對比劑（CT + PCI）兩組相當**：134±27.7 vs 116.7±37.5 mL（P=0.08）
- 支架膨脹 (stent expansion) 兩組皆優且相近：**≈0.87 vs 0.88**
- 6 個月主要不良心血管事件 (major adverse cardiovascular events, MACE)：**0% vs 6.7%**（1/15, P=0.16；1 位對照組第 76 天死亡，疑似支架血栓）

> Cath-lab 重點：3DCT 在「病灶準備前」即知正確角度，cine 次數中位數從 4 降至 1，對比劑與輻射近乎砍半。

---

# 3DCT vs IVUS 的相關性

| 量測 | 相關性 | P |
|------|--------|---|
| 鈣化弧度 (calcium arc) | R²=0.69 | <0.0001 |
| 最小管腔面積 (minimal lumen area, MLA) | R²=0.49 | 0.003 |
| 血管直徑 (vessel diameter) | R²=0.55 | <0.0001 |

> **警示**：3DCT 系統性低估直徑約 **12%**（可能因鈣化散射 calcium scatter）→ 最終支架尺寸仍以 IVUS 為準。

---

<!-- _class: divider -->
# 限制與臨床啟示

## Pilot · Hypothesis-generating

---

# 限制與臨床啟示

## 臨床啟示
- 首個證明 3DCT 術前規劃對主動脈-開口型 RCA PCI 有價值的 RCT
- 個別化角度勝過通用 LAO
- 術前 CT 可預先分級鈣化修飾工具（旋磨 rota、血管內碎石術 IVL）

## 限制
- 先導性、單中心、開放標籤、n=30，假說生成；對 TLR/MACE 檢力不足
- 多一次分階段 CT；禁用其他定位技巧（floating wire, Szabo, Ostial-PRO, 即時 IVUS）；無 CT-FFR

---

# 結論

- 主動脈-開口型 RCA：**術前 3DCT 規劃個別化 C-arm 角度** → 100% 最佳定位、消除地理性錯位
- 對比劑、輻射、手術時間 **近乎減半**
- 3DCT 可預測鈣化弧度與管徑，但 **低估直徑約 12%**
- 結果令人鼓舞但屬假說生成，需 **足夠檢力的大型試驗** 驗證硬終點，並探討分叉病灶應用

---

<!-- _class: small-text -->
# 參考文獻

1. van den Buijs DMF, et al. 3D CT for Preprocedural Planning of PCI for Ostial RCA Lesions. [*Circ Cardiovasc Interv*. 2025;18:e013584.](https://doi.org/10.1161/CIRCINTERVENTIONS.123.013584)
2. Mitomo S, et al. DES outcomes for ostial RCA. [*Int J Cardiol*. 2018;254:53-58.](https://doi.org/10.1016/j.ijcard.2017.10.066)
3. Dishmon DA, et al. Inaccurate stent placement in aorto-ostial disease. [*J Invasive Cardiol*. 2011;23:322-326.](https://pubmed.ncbi.nlm.nih.gov/?term=Dishmon+inaccurate+stent+placement+aorto-ostial+2011)
4. Rubinshtein R, et al. Geographic miss with aorto-ostial stenting. [*EuroIntervention*. 2015;11:301-307.](https://doi.org/10.4244/EIJV11I3A57)
5. Kočka V, et al. Optimal fluoroscopic projections of coronary ostia/bifurcations. [*JACC Cardiovasc Interv*. 2020;13:2560-2570.](https://doi.org/10.1016/j.jcin.2020.06.042)
6. Patel Y, et al. IVUS and long-term outcomes in ostial lesions. [*Catheter Cardiovasc Interv*. 2016;87:232-240.](https://doi.org/10.1002/ccd.25034)
7. Zhang M, et al. IVUS-derived calcium score to predict stent expansion. [*Circ Cardiovasc Interv*. 2021;14:e010296.](https://doi.org/10.1161/CIRCINTERVENTIONS.120.010296)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC** | 2026-06-26
