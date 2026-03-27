# 快速玻璃基板數位光處理 3D 列印技術：病患專屬頸動脈晶片用於個人化血栓研究

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-01-30**
**原文連結：[Advanced Materials — Rapid Glass-Substrate Digital Light 3D Printing Enables Anatomically Accurate Stroke Patient-Specific Carotid Artery-on-Chips for Personalized Thrombosis Investigation](https://doi.org/10.1002/adma.202508890)**

---

## 目錄

1. [研究背景與動機](#1-研究背景與動機)
2. [技術創新：超快速微製造平台](#2-技術創新超快速微製造平台)
3. [病患資料與臨床特徵](#3-病患資料與臨床特徵)
4. [計算流體力學 (CFD) 驗證](#4-計算流體力學-cfd-驗證)
5. [內皮化與生物功能化](#5-內皮化與生物功能化)
6. [血栓實驗結果](#6-血栓實驗結果)
7. [掃描電子顯微鏡 (SEM) 分析](#7-掃描電子顯微鏡-sem-分析)
8. [臨床意義與應用](#8-臨床意義與應用)
9. [研究限制](#9-研究限制)
10. [結論](#10-結論)
11. [參考文獻](#11-參考文獻)

---

## 1. 研究背景與動機

### 1.1 臨床問題：為何「低風險」狹窄患者仍會中風？

- 目前臨床指引以頸動脈狹窄程度作為中風風險評估主要依據
- 狹窄 < 70% 被歸類為「低風險」，通常不建議介入治療
- **臨床困境**：部分「低風險」患者仍發生缺血性中風
- 顯示單純測量狹窄程度無法完整預測血栓風險

> **Pearl — Virchow's Triad（血栓形成三要素）**：
> 1. 血流改變 (Altered blood flow)
> 2. 內皮損傷 (Endothelial damage)
> 3. 血液高凝狀態 (Hypercoagulability)
>
> 現有 CTA 影像僅能提供解剖學快照，無法動態評估這三要素的交互作用。

### 1.2 現有技術限制

| 技術限制 | 說明 |
|----------|------|
| 傳統微流體設計 | 使用簡化的管道幾何形狀，無法捕捉病患血管的複雜解剖特徵 |
| 自動 3D 重建 | 常無法準確呈現 ulceration 或複雜狹窄等關鍵細節 |
| 傳統 3D 列印 | 最小列印特徵 ≥ 100 µm，製造時間長（> 10 小時） |
| 體外血栓模型 | 缺乏病患專屬的解剖結構與血流動力學環境 |

---

## 2. 技術創新：超快速微製造平台

### 2.1 核心技術：Glass-Substrate DLP 3D Printing

- **DLP** (Digital Light Processing)：數位光處理立體光刻技術
- 使用 BMF S240 高精度 3D 印表機
- 創新改良：以處理過的玻璃載玻片作為列印基材

> **Pearl — 製造效率大幅提升**：
> - 製造時間：從 > 10 小時縮短至 **< 2 小時**
> - 成功率：約 100%
> - 層厚度：**5 µm**（遠優於傳統 100 µm）

### 2.2 玻璃載玻片表面處理流程

1. 異丙醇超音波震盪清洗 5 分鐘
2. 壓縮空氣吹乾後，Milli-Q 水超音波震盪 5 分鐘
3. 浸泡於 Toluene + TMSPM (90/10 w/w) 溶液 2 小時
4. 純乙醇沖洗後，氮氣吹乾

### 2.3 製造流程概述

```text
CTA 影像擷取 → 3D 重建與優化 → 縮小至微流體尺度
       ↓
DLP 3D 列印模具 → PDMS 翻模 → 機械夾具組裝
       ↓
內皮化 → 血液灌流實驗 → 即時血栓觀察
```

### 2.4 機械夾具系統創新

- 上半部：Formlabs Rigid 4k 樹脂
- 下半部：Formlabs Rigid 10k 樹脂
- 雙材料設計可防止操作與實驗過程中的滲漏與分離
- 組裝後以 80% ethanol 滅菌

---

## 3. 病患資料與臨床特徵

| 病患編號 | 年齡 | 臨床表現 | CTA 發現 |
|----------|------|----------|----------|
| Patient #1-H | 67 歲 | 急性左側大腦半球中風（TIA 後 2 個月） | 左側 C1 段纖維鈣化斑塊 70% 狹窄 |
| Patient #2-G | 71 歲 | 右側大腦半球症狀（顏面不對稱、吞嚥困難等） | 右側 C1 段約 10% 狹窄 |
| Patient #3-B | 78 歲 | 急性右側大腦半球中風 | 右側 C1 段纖維鈣化斑塊，約 40% 狹窄 |

---

## 4. 計算流體力學 (CFD) 驗證

### 4.1 血流動力學縮放原理

- 將 CTA 血管縮小至 CCA 管徑 200–300 µm
- 人類頸動脈 Reynolds number ≈ 200，屬層流 (laminar flow)
- 允許安全縮小至微流體尺度而不顯著改變整體流動模式

> **Pearl — 關鍵參數：Wall Shear Rate（壁面剪切率）**
> - 健康頸動脈：≈ 400 s⁻¹
> - 病理狀態（狹窄區）：> 1000 s⁻¹
> - CFD 分析確認微流體與 CTA 尺度的剪切率無統計學顯著差異（p > 0.05）

### 4.2 各病患最佳流速設定

| 病患 | 最佳流速 | 對應生理條件 |
|------|----------|-------------|
| Patient #1-H | 127 µL/min | 模擬體內血流動力學 |
| Patient #2-G, #3-B | 51 µL/min | 配合不同血管幾何結構 |

---

## 5. 內皮化與生物功能化

### 5.1 內皮細胞培養流程

1. 晶片以 80% ethanol 滅菌
2. Fibronectin 100 µg/mL 包覆 1 小時（37°C）
3. 注入 HUVEC 懸浮液（5 × 10⁶ cells/mL）
4. 翻轉培養技術：15–20 分鐘後翻轉晶片，確保管腔全面內皮化
5. 隔夜培養形成 confluent 單層

### 5.2 發炎刺激模型

- TNF-α 20 ng/mL 刺激 4 小時
- 結果：
  - ICAM-1 表現增加 **59.9 倍**
  - E-selectin 表現增加 **36.0 倍**
- 驗證模型具有生理相關性，可研究血管發炎與血栓關係

---

## 6. 血栓實驗結果

### 6.1 全面性血栓 (Global Thrombosis) 模型

- 使用 citrated 人血加入 10 mM CaCl₂ 重新鈣化
- 37°C 下以 γ₀ = 830 s⁻¹ 灌流 10 分鐘
- 觀察時間依賴性的血小板與 fibrin 沉積
- 血栓主要形成於頸動脈分叉處

> **Pearl — Fibrin 沉積量與狹窄程度的關係**：
> #1-H diseased (70% 狹窄) > #2-G (10% 狹窄) > #1-H healthy (0% 狹窄)
> 證實晶片能準確反映狹窄-血栓關係。

### 6.2 抗血栓藥物測試

| 藥物類別 | 藥物名稱 | 效果 |
|----------|----------|------|
| **抗凝血劑** | Clexane (5 U/mL) | **最有效**：同時減少血小板聚集與 fibrin 形成 |
| | Rivaroxaban (500 nM) | 主要抑制 fibrin 形成 |
| | Apixaban (500 nM) | 主要抑制 fibrin 形成 |
| **抗血小板藥物** | Tirofiban (330 ng/mL) | 有效阻斷血小板聚集與 fibrin |
| | PGE1 (1 µg/mL) | 有效阻斷血小板聚集與 fibrin |
| | PGI2 (1 µg/mL) | 有效阻斷血小板聚集與 fibrin |
| | Indomethacin (10 µM) | 中度減少血小板聚集 |
| | MRS2179 (100 µM) | 中度減少血小板聚集 |

### 6.3 局部血栓 (Localized Thrombosis) 模型

#### 6.3.1 雷射消融誘導內皮損傷

- 使用 RAPP UGA-42 Caliburn 雷射消融模組
- 波長 355 nm，輸出功率 70%
- 根據病患 CTA/DSA 影像定位潰瘍部位
- 控制損傷範圍：約 5–7 個內皮細胞脫落
- 模擬 plaque rupture 後的血栓形成

#### 6.3.2 剪切力依賴的血小板轉位

> **Pearl — 關鍵發現**：
> - 高剪切區 (> 1000 s⁻¹) 的血小板 translocation 事件比低剪切區 (< 1000 s⁻¹) 高出 **7–10 倍**
> - 中位數：高剪切區 ≈ 9 次 vs 低剪切區 ≈ 1 次
> - 這解釋了 thromboembolism 的機制

---

## 7. 掃描電子顯微鏡 (SEM) 分析

- 確認晶片內形成的血栓具有體內血栓的關鍵結構特徵
- 觀察到 **Polyhedrocytes**：多面體紅血球
  - 在血栓結構內被壓縮的紅血球
  - 是成熟血栓的特徵性表現
- 可見血小板與 fibrin 形成的複雜網絡結構

---

## 8. 臨床意義與應用

### 8.1 解答臨床困惑

為何部分「低風險」狹窄患者仍發生中風？本研究顯示：即使狹窄程度低於介入治療閾值——

- 局部血流動力學異常區域可能具有顯著血栓風險
- 內皮損傷部位在高剪切力環境下易形成不穩定血栓
- 血栓轉位導致栓塞性中風

### 8.2 潛在臨床應用

1. **個人化血栓風險評估**：根據病患專屬血管幾何建立晶片
2. **抗血栓藥物篩選**：測試不同藥物對個別患者的效果
3. **術前規劃**：評估介入治療的必要性
4. **血管裝置開發**：測試支架等裝置的血栓生成風險

---

## 9. 研究限制

- 目前僅針對頸動脈，可能無法代表其他血管床的血栓過程
- 模型僅包含內皮細胞與血小板，尚未納入：
  - 平滑肌細胞 (Smooth muscle cells)
  - 白血球 (Leukocytes)
  - 其他血管壁組成
- 無法同時保留 Reynolds number、Womersley number 與 wall shear rate
- 脈動流與慣性力效應在微尺度無法完全捕捉
- 流速條件基於文獻平均值，可進一步整合病患專屬流速測量

---

## 10. 結論

本研究重要貢獻：

1. 開發超快速（< 2 小時）病患專屬頸動脈晶片製造平台
2. 成功保留 CTA 影像中的複雜解剖特徵（狹窄、分叉、潰瘍）
3. CFD 驗證微流體與體內血流動力學相似性
4. 建立全面性與局部性血栓模型
5. 證實剪切力依賴的血小板轉位機制
6. 提供個人化抗血栓藥物測試平台

> 此平台為研究工具與臨床決策輔助，而非獨立診斷或治療規劃工具。

---

## 11. 參考文獻

1. Zhao YC, Wang Z, Nasser A, et al. Rapid Glass-Substrate Digital Light 3D Printing Enables Anatomically Accurate Stroke Patient-Specific Carotid Artery-on-Chips for Personalized Thrombosis Investigation. [*Adv. Mater.* 2026;38:e08890.](https://doi.org/10.1002/adma.202508890)
2. Saba L, Saam T, Jäger HR, et al. Carotid artery wall imaging: perspective and guidelines from the ASNR vessel wall imaging study group and expert consensus recommendations of the American Society of Neuroradiology. [*Lancet Neurol*. 2019;18:559-573.](https://doi.org/10.1016/S1474-4422(19)30016-9)
3. Jackson SP, Nesbitt WS, Westein E. Dynamics of platelet thrombus formation. [*J Thromb Haemost*. 2009;7 Suppl 1:17-20.](https://doi.org/10.1111/j.1538-7836.2009.03401.x)
4. Chen Y, Ju LA. Biomechanical thrombosis: the dark side of force and dawn of mechano-medicine. [*Stroke Vasc Neurol*. 2020;5:185-197.](https://doi.org/10.1136/svn-2019-000302)
5. Zhao YC, Zhang Y, Jiang F, et al. Piezo1 mechanosensing in red blood cells and its implications for mechano-sensitive thrombosis. [*Adv. Healthcare Mater.* 2023;12:2201830.](https://doi.org/10.1002/adhm.202201830)
