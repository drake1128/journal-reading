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
  section.lead h1 { color: #ffffff; font-size: 2.0em; border-bottom: none; }
  section.lead h2 { color: #b0c4de; }
  section.lead h3 { color: #ffffff; font-weight: normal; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #ffd166; text-decoration: underline; }
  section.lead blockquote,
  section.lead blockquote p,
  section.lead blockquote strong { color: #2d3436; }
  section.divider {
    background-color: #0072bc;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 {
    color: #ffffff;
    border-bottom: none;
    font-size: 2.4em;
    text-align: center;
  }
  section.divider h2 {
    color: #ffffff;
    font-size: 1.5em;
    text-align: center;
    font-weight: bold;
  }
  section.divider h3 {
    color: #ffe082;
    font-size: 1.2em;
    text-align: center;
    font-weight: normal;
  }
  section.divider p, section.divider strong { color: #ffffff; }
  section.bignum {
    background-color: #1a2740;
    color: #ffffff;
    text-align: center;
  }
  section.bignum h1 { color: #ffffff; font-size: 3.5em; border-bottom: none; }
  section.bignum h2 { color: #b0c4de; font-size: 1.3em; }
  section.bignum p { color: #dfe6e9; font-size: 1.0em; }
  section.bignum strong { color: #ffe082; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  a { color: #0072bc; }
  table { font-size: 0.68em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 5px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.9em;
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
  section.small-text { font-size: 0.74em; }
  section.abbr { font-size: 0.66em; }
  .qr {
    position: absolute;
    right: 40px;
    bottom: 80px;
    text-align: center;
    font-size: 0.65em;
    color: #555;
  }
  .qr img { width: 110px; height: 110px; border: 1px solid #dcdde1; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-07-24 ~ 2026-07-31'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-07-24 ~ 2026-07-31

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Top Pick 附 QR Code，可掃描跳轉原文

---

# 🎯 本週主題與固定欄目

## 「支持與抗凝減量不減效、肺高壓與心肌病新藥齊發」

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 結構性主動脈瓣方向
3. 🔧 **TEER Section** — 二尖瓣影像與預後
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — 結構／冠脈與瓣膜急症 × 5
6. 📖 **參考文獻 + 縮寫對照**

> 📌 本週 **NEJM 無新心血管原始研究**（僅讀者來函）；**EuroIntervention 本週無新上線文獻**。

---

# ⭐ Top 5 Picks

| 試驗 | 期刊 | 方向 | 關鍵數字 |
|------|------|------|----------|
| **ADVANCE OUTCOMES**（ralinepag/PAH） | *Lancet* | ✅ | 臨床惡化 **HR 0.45**（p<0.0001） |
| **微軸流泵 vs VA-ECMO**（高危 PCI） | *Eur Heart J* | ✅ 非劣 | 30d MAE **7.34% vs 11.5%**（P非劣<0.001） |
| **RATE**（ECMO 抗凝減量） | *Lancet* | ✅ 非劣 | 低劑量肝素/LMWH 皆不劣於標準劑量 |
| **HOPE-3**（deramiocel/Duchenne） | *Lancet* | ✅ | PUL2.0 **+4.55%**（p=0.029） |
| **FIND-AF 2.0**（風險導向 AF 篩檢） | *Circulation* | 💡 | 四國 EHR >1,400 萬人 ML 模型 |

> **Pearl of the Week**：本週關鍵字是「**減法**」——MCS 與抗凝都證明「更輕、更少」可不劣於重裝方案；肺高壓與心肌病則在做「加法」（新機轉、新 modality）。

---

<!-- _class: divider -->
# Pick #1
## ADVANCE OUTCOMES
### 口服 ralinepag 治療肺動脈高壓

---

# ADVANCE OUTCOMES — 設計

## [McLaughlin VV, et al. *Lancet* 2026](https://doi.org/10.1016/S0140-6736(26)01011-1)

- 事件驅動、隨機、雙盲、安慰劑對照**三期試驗**
- 口服每日一次選擇性前列環素 IP 受體促效劑 **ralinepag** vs 安慰劑（每週滴定至最高耐受劑量）
- 對象：**肺動脈高壓 (PAH)**；728 隨機、**687 納入分析**（剔除中國 41 例）
- **80% 已用雙重背景 PAH 治療**
- 主要終點：首次臨床惡化（死亡／PAH 住院／啟動前列環素／疾病進展／長期反應不佳之複合）

<div class="qr"><img src="data:image/png;base64,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"><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# HR 0.45
## 首次臨床惡化 — ralinepag vs 安慰劑
### 18% vs 36%（95% CI 0.33–0.62）｜p<0.0001｜相對風險 ↓55%

因不良事件停藥 **19% vs 3%**（前列環素類副作用）

---

# ADVANCE OUTCOMES — 臨床啟示

> 在已用現代背景治療的 PAH，**加上口服 ralinepag 可再砍半臨床惡化**（WebSearch 交叉確認 55% RRR）。

- 屬**事件驅動的預後型**終點（非僅 6MWD 替代終點）→ 證據力強
- **耐受性是實務挑戰**：停藥率 19%，滴定需耐心（頭痛、腹瀉、下顎痛）
- 定位：selexipag 之外、每日一次口服的前列環素路徑選項
- 分析剔除中國站點 → 外推東亞需留意

---

<!-- _class: divider -->
# Pick #2
## 微軸流泵 vs VA-ECMO
### 高風險 PCI 的預防性機械循環支持

---

# 微軸流泵 vs VA-ECMO — 設計

## [Zhao G, et al. *Eur Heart J* 2026](https://doi.org/10.1093/eurheartj/ehag520)

- 前瞻、多中心、開放標籤、**非劣性**隨機試驗（中國）
- 對象：複雜三血管／無保護左主幹／最後通暢橋管 + **LVEF ≤35%**，非緊急高風險 PCI
- n=222：**微軸流泵 SynFlow 3.0**（109）vs **VA-ECMO**（113）
- 主要終點：30 天主要不良事件複合（死亡/MI/中風/再血運/大出血/AKI/CPR/手術/嚴重裝置併發症）

<div class="qr"><img src="data:image/png;base64,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"><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# 7.34% vs 11.5%
## 30 天 MAE — 微軸流泵 vs VA-ECMO
### 校正差 −4.6%（−12.6 至 3.5）｜**P非劣性 < 0.001**

住院 **4.1 vs 5.2 天**｜裝置併發症 **3.7% vs 11.5%**｜貧血 **9.2% vs 20.4%**

---

# 微軸流泵 vs VA-ECMO — 臨床啟示

> ⚠️ 這是**非劣性、非優越性**：微軸流泵並非「更會救命」，而是「**療效相當、負擔更輕**」。

- 少見的「兩種 MCS 平台頭對頭」RCT — 對 CHIP-PCI 極具參考（Drake 面向）
- **SynFlow 3.0 為中國裝置、台灣尚未上市** → 不直接改變本地實務
- 須與「Impella 在**無休克**高風險 MI 未改善預後」區分 → **適應症與族群決定價值**

---

<!-- _class: divider -->
# Pick #3
## RATE
### 葉克膜抗凝「減量」不劣於標準劑量

---

# RATE — 設計與結果

## [van Minnen O, et al. *Lancet* 2026;408:357-366](https://doi.org/10.1016/S0140-6736(26)00851-2)

- 開放標籤、**三臂非劣性**；荷蘭 7 ICU；n=330（每組 110）
- ①標準劑量普通肝素（aPTT 2.0–2.5×）②低劑量肝素（1.5–2.0×）③治療劑量 **LMWH**
- 主要終點：嚴重出血 + 嚴重血栓 + 6 個月死亡之複合（非劣性界限 <7.5pp）

| 組別 | 複合事件 | 對標準差值 |
|------|---------|-----------|
| 標準劑量肝素 | 81% | — |
| 低劑量肝素 | **72%** | −9.1pp（非劣性達標） |
| 治療劑量 LMWH | **75%** | −6.1pp（非劣性達標） |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyCAIAAABnRsZeAAAHl0lEQVR4nO3dQY7kOBIAwalB///LvQ9YgMCCzg1SZXZXpqSsdvAQiP75+/fvPwCdf6dvAPgaWQFisgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsT+7Fz88/NT3ccldjb7vvg21s+780RTb3JqN/OLv/7azpt0WgFisgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYltTtmtT845rO9OQ62vPPe/U956blF1/8rnZ3ynf+7ew5rQCxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsQOTtmunZvwu3Ob6dTk6NRe2BfnSu/8y9kx9UROK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUgJitAbGzK9nvu3Cm788nn5oanruX/w2kFiMkKEJMVICYrQExWgJisADFZAWKyAsRkBYiZsv0fvLiPduqTz00Gn5vBvXPT7YucVoCYrAAxWQFisgLEZAWIyQoQkxUgJitATFaA2NiU7W+bWTw3oTv1yWvfe6Jz7ryrHU4rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0Ds4JTtuT2pU85tUZ3aknvunqe+d+rate/9W1hzWgFisgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYltTtt/bwXnOne/qzvndc99757Xf47QCxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsS2pmzP7f48Z+qed773zg2sd+5nvfOu7tyDe+6v3WkFiMkKEJMVICYrQExWgJisADFZAWKyAsRkBYgd3GW7M/354mThnc+79uIu2xf/NtbunAze4bQCxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsTGdtm+ON957nvvnEk9d1dT72pqK/COF+/ZaQWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiP2c+7/spz55au7we7Ohd26NvfNdrb24rXbnbTitADFZAWKyAsRkBYjJChCTFSAmK0BMVoCYrACxrV22L05/vrjL9pzvTQav3bnn+Jyp6V6nFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUgtjVlu3ZuovF7M4t3Tp3uXHvuie7cznvOi/fstALEZAWIyQoQkxUgJitATFaAmKwAMVkBYrICxA5O2d7pe5Oya1MzmudmYV/coLxj6k3ucFoBYrICxGQFiMkKEJMVICYrQExWgJisADFZAWIHp2zPbavdmR18cWbxnHPv+cXtvN/brzz1GzmtADFZAWKyAsRkBYjJChCTFSAmK0BMVoCYrACxrSnbO6cSz+0c3ZlZPPe9O3bueWq364vO/Uu5c7bbaQWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiP1M7f5cm9o4e+fk6NSU7ff2wt65X3lt6m/SLlvgIrICxGQFiMkKEJMVICYrQExWgJisADFZAWJbu2zX7pyVPDcNufO9O9dObTM9N/1551zp937Bc5xWgJisADFZAWKyAsRkBYjJChCTFSAmK0BMVoDY1i7b77lzI+nUFtVz7nwbL05gn2OXLXARWQFisgLEZAWIyQoQkxUgJitATFaAmKwAsa0p2xdnJaecu+dzv+Bv+9t4cY72zud1WgFisgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYn+mvvjOWUl7YavvvfNdrZ17k1N/z1O/gtMKEJMVICYrQExWgJisADFZAWKyAsRkBYjJChA7OGV7bsLvxb2wU+6cdt2ZK71zAvvctec+2S5b4BmyAsRkBYjJChCTFSAmK0BMVoCYrAAxWQFil+6yXZva7vniHO25ez43o3nnltypqfEXOa0AMVkBYrICxGQFiMkKEJMVICYrQExWgJisALGfqanTqX20U588de3auV9/6pPvnITe8eIMrtMKEJMVICYrQExWgJisADFZAWKyAsRkBYjJChDbmrL9bV6co93x26aKp3bo3vm3sfO8TitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQOzPzsW/bW/onVOnO+6c3925dv1E55536hdcm/pepxUgJitATFaAmKwAMVkBYrICxGQFiMkKEJMVILY1Zbt255bcO3d/3rmvdOd779zPes73JqF3OK0AMVkBYrICxGQFiMkKEJMVICYrQExWgJisALGDU7Zrd067nnPn8+7c1Z3vee3OPbg77tyR7LQCxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsTGpmy/Z2pi9c5J2Z35zjvvamo779Rd7fwKTitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQMyUbebcnOW5acipXad3Tqzeaepd7XBaAWKyAsRkBYjJChCTFSAmK0BMVoCYrAAxWQFiPy/OaO74bROra3f+Rjte3Ci8NrWPdofTChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQOzhl+6IXJxp3TP2Cd77nOyewp67d4bQCxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsS2pmwB/pvTChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQOw/Tc757/+lKOEAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# RATE — 臨床啟示

> **ECMO 抗凝可以減量甚至改用治療劑量 LMWH**，安全性訊號更佳（嚴重出血數值上更低、血栓未增）。

- 重新檢視「ECMO 一定要打到 aPTT 2–2.5×」的舊習慣
- 與「微軸流泵不劣於 VA-ECMO」同屬本週「**重症支持減負**」主線
- 界限：單國、開放標籤、6 個月死亡率仍高（42–50%，族群病重）；LMWH 於腎功能不全/需快速逆轉時謹慎

---

<!-- _class: divider -->
# Pick #4
## HOPE-3
### deramiocel 細胞療法治晚期 Duchenne

---

# HOPE-3 — 設計與結果

## [McDonald CM, et al. *Lancet* 2026](https://doi.org/10.1016/S0140-6736(26)01385-1)

- 三期、多中心、隨機、雙盲、安慰劑對照；每 3 個月**門診靜脈輸注**；追蹤 12 個月
- 對象：≥10 歲**裘馨氏肌肉失養症 (DMD)**；n=106（deramiocel 54 vs 安慰劑 52）
- 介入：**deramiocel**（同種異體心球衍生細胞）
- 主要終點：上肢功能 **PUL2.0** 百分比變化

| 終點 | 結果 |
|------|------|
| **PUL2.0 vs 安慰劑** | **+4.55%**（0.47–8.63），**p=0.029** |
| 安全性 | 與安慰劑相似 |

<div class="qr"><img src="data:image/png;base64,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"><br>📱 Scan DOI</div>

---

# HOPE-3 — 臨床啟示

> deramiocel **安全地減緩晚期 DMD 的骨骼肌與心肌退化**，且**與基因型別無關**、每季門診輸注。

- DMD 死因逐漸從呼吸衰竭轉向**心肌病變** → 心臟科與神經科交界議題
- 主要終點（上肢功能）為**替代性、幅度溫和**（4.55%）
- 對心臟科意義：**DMD 心肌病變開始有「疾病修飾」選項** → 待心臟終點（LVEF、CMR 纖維化、心律不整）長期資料

---

<!-- _class: divider -->
# Pick #5
## FIND-AF 2.0
### 風險導向的心房顫動篩檢

---

# FIND-AF 2.0 — 設計與概念

## [Risk-Guided AF Screening Using EHR. *Circulation* 2026](https://doi.org/10.1161/CIRCULATIONAHA.126.079391)

- 開發＋外部驗證＋前瞻測試的**機器學習**模型（隨機森林）
- 變項：**年齡、性別、10 項共病**；預測 **6 個月內新發 AF**
- 資料：四國 EHR（英 208 萬、日 780 萬、以 217 萬、加拿大）
- 概念：以**風險導向**取代年齡單一門檻的無差別 AF 篩檢

<div class="qr"><img src="data:image/png;base64,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"><br>📱 Scan DOI</div>

---

# FIND-AF 2.0 — 臨床啟示

> 支持「**依風險分層做 AF 篩檢**」比全面篩檢更有效率；模型僅需現成 EHR 變項即可跨國運作。

- 與 LOOP、SAFER 等 AF 篩檢試驗合讀 → 從**無差別**走向**風險導向**
- 落地門檻低（不需穿戴裝置即可先鎖定高風險族群）
- 屬預測模型研究 → 是否降低中風的**臨床效益仍待介入試驗驗證**

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 本週結構性主動脈瓣方向
### Drake 主要臨床方向

---

# TAVI #1｜混合型 AS/AR：BEV vs SEV

## [Hasan I, et al. *J Cardiol* 2026](https://doi.org/10.1016/j.jjcc.2026.07.015)

- 單中心回溯（2012–2024），混合型主動脈瓣疾病（重度 AS + 中度↑ AR）；n=796 → 傾向配對每組 286
- **自膨瓣 (SEV)**：壓差較低（1 年 8.53 vs 12.5 mmHg，p<0.001）＝血流動力學較佳
- **球擴瓣 (BEV)**：**中風更少（p<0.001）、主要血管併發症更少（p=0.015）**；SEV 早期 PVL 較多但 1 年追平
- 1 年與 5 年**死亡率無差異**

> 💡 經典取捨：**SEV 壓差佳、BEV 併發症少** → 依解剖與風險個體化選瓣。單中心回溯、殘餘干擾難免。

<div class="qr"><img src="data:image/png;base64,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"><br>📱 Scan DOI</div>

---

# TAVI #2｜2019 低風險擴大後的全美影響

## [Elkasaby MH, et al. *Cardiol Rev* 2026](https://doi.org/10.1097/CRD.0000000000001404)

- 全美住院樣本（2016–2022）**81,142 例**；以 2019 Q3 FDA 低風險擴大為中斷點做分段迴歸
- TAVR 年量 **+134%**；平均年齡 79.7→78.2 歲；低風險比例 2.0%→6.0%
- **住院死亡率 1.58%→0.84%**；中風、PPM、血管併發症、住院天數皆改善（p<0.001）
- 少數族裔/低收入可近性小幅提升，但**新的種族間死亡率差距浮現**

> 💡 政策層級證據：擴大適應症帶來量增與結局改善，但**公平性 (equity)** 是規模化後的隱憂 → 對台灣擴大 TAVI 給付具參考。

<div class="qr"><img src="data:image/png;base64,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"><br>📱 Scan DOI</div>

---

# TAVI #3｜TF-TAVI vs SAVR 的環境足跡

## [Friedericy HJ, et al. *Heart* 2026](https://doi.org/10.1136/heartjnl-2026-328011)

- 前瞻、單中心；各 15 例 TF-TAVI 與 SAVR 的術中生命週期評估（10 個環境類別）
- **碳足跡 68.6 vs 181.2 kg CO₂-eq**（TF-TAVI 為 SAVR 的 **38%**）
- 材料少 51%、能耗少 52%、**用水少 97%**（SAVR 用水主要來自體外循環加溫冷卻）
- TF-TAVI 在**全部 10 個環境類別**皆優於 SAVR

> 💡 **永續醫療**新視角：微創介入除臨床與經濟效益，還有環境效益。界限：單中心、各 15 例、只算術中。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyCAIAAABnRsZeAAAHlElEQVR4nO3dQY4bORQFwdGg739lz3ZWhGEm/VmliL3U6mo5wcUD/fn169c/AJ1/pz8A8DayAsRkBYjJChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiP3svPjz+VSf4xI7N/uun8b6nc89yXO/0c7P3XlWa+c+87mfe6edp+G0AsRkBYjJChCTFSAmK0BMVoCYrAAxWQFisgLEtla2azsrvXPu3LOe23dOLWXPvfPUc97xbf8WnFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQExWgNjBle3anWvXtXPrz52fu7azZ935uTvP6tyOduovuPbEfwtrTitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQGxsZfttplanT1xwnvvMOz/3zvto7+S0AsRkBYjJChCTFSAmK0BMVoCYrAAxWQFisgLErGwzUze/Tr127dyqeOoz8/ucVoCYrAAxWQFisgLEZAWIyQoQkxUgJitATFaA2NjK9ttuBt1Zjk75tjtlp76T7/u34LQCxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsQOrmzvXI6ec+eNs3e+9pwn3uz7Pk4rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0Ds8757NM/Z2Uqe22je+c7neBr3c1oBYrICxGQFiMkKEJMVICYrQExWgJisADFZAWJbK9sn3nW65r7Sv+OJ9+9+2/d5h9MKEJMVICYrQExWgJisADFZAWKyAsRkBYjJChD7mf4Af+LcVnLtzgXnuSWlJ/l3nNvvTt2+7LQCxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsTGVrY7y8Jzu8OpnaUd7e+/dse5De6dz8pdtsBLyAoQkxUgJitATFaAmKwAMVkBYrICxGQFiH2mFpxrU+vAtTs3qVPvPOXODe7UO+8499d3WgFisgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYpfeZbs2tbN84q2iU5956mlMLWWnnLsTeuf3dVoBYrICxGQFiMkKEJMVICYrQExWgJisADFZAWJbd9me+5/u184tR6f2u2tTd52u3XkL8hPd+d2wsgUuIitATFaAmKwAMVkBYrICxGQFiMkKEJMVIHZwZTvlzh3t1C2qd95We+en2nnntal7cKduFHZaAWKyAsRkBYjJChCTFSAmK0BMVoCYrAAxWQFiPzsvvnPPeu61dy50p+6UPffXn1pv3/lz7/xurDmtADFZAWKyAsRkBYjJChCTFSAmK0BMVoCYrACxrbtsz5naO9551+md694pU6vitTv/gmvnFrpOK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUgJitAbOsu23OeuP29c7F655Nc+7Yd7c47u8sW+AqyAsRkBYjJChCTFSAmK0BMVoCYrAAxWQFiWyvbcwu/O29RvZN17/9NrU6nlrLn1r07nFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQExWgNhn6t7Qne3gExec3/YbnfPEb+wUd9kCLyErQExWgJisADFZAWKyAsRkBYjJChCTFSB26cr23M/d8cSd5Tnvu6vYd/L333nNaQWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiG2tbN93m+nanbvhc3/BOxecO9637r3zfmWnFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUg9nPurc9tB+/chk5tcM+Z2tFOLUenvht3rqh3OK0AMVkBYrICxGQFiMkKEJMVICYrQExWgJisALGDK9u1J96D+8Qd7RNvnD23hd2x8zTufJLnOK0AMVkBYrICxGQFiMkKEJMVICYrQExWgJisALGxle2dN5KeM7V2PfespjbHU8vRO79XU7fzrjmtADFZAWKyAsRkBYjJChCTFSAmK0BMVoCYrACxz503sN7piffC7pjaOt/5zuf+guee89Tv67QCxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsS27rK983bPHetl4c7u8H238+6Yuun23JOcWuiuTX0qpxUgJitATFaAmKwAMVkBYrICxGQFiMkKEJMVILa1sl278/bWnZ3lnRvNO/e7d+5Kz5m66XbNXbbAS8gKEJMVICYrQExWgJisADFZAWKyAsRkBYgdXNmuvW/fuXZu7Tr1zmtTt6ie+8x33ih85y3ITitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQGxsZftt7lydntuVnlu7nnvt1M2v77vJ2GkFiMkKEJMVICYrQExWgJisADFZAWKyAsRkBYhZ2b7c1Lr3zrXr++4MnnrtmtMKEJMVICYrQExWgJisADFZAWKyAsRkBYjJChAbW9meW/idc+dnPncj6RMXuueexo6p3fDUN9ZpBYjJChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIHVzZ3rl33HHnLarnPPFO2R07v9GdO9qpDa7TChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQ+9x5PyvwXE4rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUgJitATFaAmKwAsf8AayYL8lolopUAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 二尖瓣影像與預後
### Drake 的 TEER 操作面向

---

# TEER #1｜OCEAN-Mitral：發炎指標與預後

## [Omote K, Yamamoto M, et al. *J Am Heart Assoc* 2026](https://doi.org/10.1161/JAHA.125.048726)

- 日本 OCEAN-Mitral 登記 **3,511 例**接受二尖瓣 TEER；依高敏 CRP 分三組
- 中位追蹤 13 個月：826 死亡、911 心血管死亡/心衰住院複合
- **CRP 死亡 HR 1.98（1.63–2.40）**、**體溫 HR 1.49**；CRP>3.0 + 體溫 ≥37°C 風險最高
- CRP 在臨床/實驗室/超音波之外具**增量預後價值**

> 💡 TEER 選病人除解剖與逆流嚴重度外，**基線發炎狀態（CRP）也是預後訊號** → 納入共同決策與術後追蹤。觀察性、樣本大訊號一致。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKCAIAAAD0S4FSAAAGCUlEQVR4nO3dQa7jNhBAwTiY+195coGA+AGHafK5am9LlvXATYP8/P79+y+g6O/pGwBOkTdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsn7tfPjz+fyp+7jEnTvPrZ/zzj3v/IMvPqsX7TxnqzdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2RtTa2t9aaazs147cylTd3V1HzYznvVeyfXrN6QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pB1cGpt7dykztRk0rm5tB1Td/Xinme9d9LqDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWWNTaz3nZp7OzZad28Xtzut+G6s3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkmVr7D87tPTY1pzV1uujON/NzVm/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8gam1r7tsmkF3/vubm0qfNS1178j9as3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekHVwaq13zuPOrJXP/j+fXeu9k2tWb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyPr09pc6Z2qHsHMTYOd4r25g9YYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhqytvdbuPOdx7cXJsx1Tv+jOXc3u3Kft3H9k9YYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhqyDe61N7RB252TS2rl7nvrmO2e8zr1XU2/smtUbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuyLj0h9M6Jt3N39eIpn1NPY+3F/f/OsXpDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUPW2F5ra3fuEPZtu7jtePFJTr0b51i9IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwha2tq7c75oXPXndI717L3i3acm4ezekOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q9bYXmt3XtfJlT9nN7Wfm5qls3pDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUPWkyeE3nna5p13tXZuwm/txW/eMTWVaPWGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oasg1NrPS/uHvfidV905w5/Vm/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8j6tfPhO8/TnDpfcsfUHmDnrtubeHvxvbJ6Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlD1tbU2tqd5zzufPPUJFZvSu+cqaex8+bsXHfN6g1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVlbJ4ROzeLsuHMXt7XeHm87pk7bfPGbrd6QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pB1cGrtxQmwOyeTpqYD7zzl095yP2f1hix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGrIMnhK71Zp7unKa6cw5v55vPuXMK015rwL+QN2TJG7LkDVnyhix5Q5a8IUvekCVvyNraa+3bvDjV9OKedjvfvOPOu9ph9YYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhqyDJ4S+6M6ncee+dOfOWr3zszum/kGrN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZB08IfTO3afu3PNsav+wc9ed+vfv/EVTu7hZvSFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IevgXmt37ms1NcW149v2tHvx99755li9IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwh6+Bea99matZqakpv5/dO7T22Y33Pd05DWr0hS96QJW/IkjdkyRuy5A1Z8oYseUOWvCHL1NofM3XK54s7k631dmKbmmmzekOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q9bY1NqdJyruePG81LWpWatzT/LOf+Hcc7Z6Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlD1mfqjMg7vTjVdM6L78a5Jzk1ebbD6g1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVlbU2vAzazekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2T9A1cAM5otkx1hAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TEER #2｜TEER 的超音波影像導引（實作回顧）

## [Itabashi Y. *J Echocardiogr* 2026](https://doi.org/10.1007/s12574-026-00748-9)

- **術前 TTE**：機轉/嚴重度、瓣口面積、跨瓣壓差、tethering height、coaptation length、prolapse 寬度與 gap、鈣化分佈
- **術中 TEE**：穿間隔→抓瓣→釋放；X-plane、3D、**即時多平面重組 (live MPR)** 避開裝置聲影
- 早期偵測併發症（心包積液、瓣葉損傷、醫源性 ASD 伴右到左分流）
- **術後 TTE**：殘餘 MR、醫源性二尖瓣狹窄、單葉裝置附著/瓣葉穿孔

> 💡 把 TEER 全程「該看什麼、何時看」系統化的實作地圖；**live MPR** 是提升抓瓣效率與安全的關鍵技巧。適合團隊訓練共讀。

<div class="qr"><img src="data:image/png;base64,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"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

# 其他值得一讀（1/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **血漿紅外分子指紋 (IMF)** 分層冠心殘餘風險 | *Eur Heart J* | IMF+Age 死亡辨別 **C-index 0.79 vs SMART2 0.74**，反映 CHIP 生物學（無需定序） | [DOI](https://doi.org/10.1093/eurheartj/ehag587)｜[PMID](https://pubmed.ncbi.nlm.nih.gov/42522903/) |
| **Omega-3 與 AF**：35 試驗統合分析 | *Circ Arrhythm EP* | 114,592 人；**再次確認高劑量魚油與 AF 風險上升**的安全性訊號 | [DOI](https://doi.org/10.1161/CIRCEP.125.014785)｜[PMID](https://pubmed.ncbi.nlm.nih.gov/42517224/) |
| **CardioMEMS 肺動脈壓與心衰住院** | *JACC Heart Fail* | 併 4 研究；基線與 6 個月 PAP 變化**獨立預測 2 年內心衰住院** | [DOI](https://doi.org/10.1016/j.jchf.2026.103239)｜[PMID](https://pubmed.ncbi.nlm.nih.gov/42535981/) |

---

# 其他值得一讀（2/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **急診較高利尿劑劑量與急性心衰** | *JACC Heart Fail* | 21 家急診；較高起始 IV 利尿劑與**較低住院風險**，48h AKI 未顯著增加 | [DOI](https://doi.org/10.1016/j.jchf.2026.103235)｜[PMID](https://pubmed.ncbi.nlm.nih.gov/42535982/) |
| **癌症存活者 CV 風險預測模型**統合分析 | *Eur Heart J* | 34 研究/98 萬人；~1/3 模型 AUC≥0.70；**跨癌別可移植性有限** | [DOI](https://doi.org/10.1093/eurheartj/ehag562)｜[PMID](https://pubmed.ncbi.nlm.nih.gov/42517578/) |
| **EchoAI-Peds**：兒童超音波多任務深度學習 | *Circulation* | 迄今最完整兒童標註集；多切面多任務兒童心臟超音波 AI | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.080619)｜[PMID](https://pubmed.ncbi.nlm.nih.gov/42517220/) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構／冠脈與瓣膜急症 × 5

---

# Case #1｜Myval TAVI 球囊破裂 — 丙泊酚潤滑搶救

## [Akyüz AR, et al. *Catheter Cardiovasc Interv* 2026](https://doi.org/10.1002/ccd.70778)

24.5 mm **Myval** 釋放時球囊破裂、部分充盈失敗；回撤至降主動脈，**經球囊管腔注入稀釋丙泊酚 (propofol) 作為化學潤滑劑**克服摩擦、安全脫離；整體移除後換新鞘，第一枚瓣膜於降主動脈序列展開，再於原生瓣環植入第二枚 Myval，無併發症。

> **為什麼值得讀**：球擴瓣球囊破裂罕見但致命。示範冷靜 bailout——回撤至安全區、用潤滑劑化解卡阻、序列處理。**「丙泊酚當潤滑劑」**是極具巧思的臨場應變。

<div class="qr"><img src="data:image/png;base64,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"><br>📱 Scan DOI</div>

---

# Case #2｜LVAD 併 AR 與動態主動脈血栓的混合處理

## [Stegmann A, et al. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.109544)

長期 **LVAD** 病人出現顯著 AR 併升主動脈血栓；瓣環 >28 mm 且合併血栓不適合 TAVR → **混合策略**：短暫循環停止下清除血栓、介入性暫時封堵無法直接進入的 LVAD 出口導管、再行 **SAVR**。

> **為什麼值得讀**：LVAD 新發/惡化 AR 是長期支持難題，合併血栓更增栓塞風險。示範**外科＋介入混合團隊決策**與個體化路徑。機械循環支持與結構團隊跨專科協作的好教材。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyCAIAAABnRsZeAAAHiUlEQVR4nO3dS25kNxQFQZeh/W9ZnmpEGGASl+9VxFz17wQHB+zP7+/vPwCdf6dfAPA2sgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsRkBYj97Pzx5/OpXscldm72vfPTmHpH6+ddP/Kdr/nc895p59NwWgFisgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYlsr27Wdld45T1xD7ixW73y/U7+Nb3vetXO/DacVICYrQExWgJisADFZAWKyAsRkBYjJChCTFSB2cGW7dm7hd27ReO4G1p3nXZt6VVOf1dQdujue+G9hzWkFiMkKEJMVICYrQExWgJisADFZAWKyAsRkBYiNrWzfZ2fBeW5H+8QF59T9u3ducJ/IaQWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiFnZPsDOvnPqbtedR77zNfP/Oa0AMVkBYrICxGQFiMkKEJMVICYrQExWgJisALGxle37bgad2sLuPPLa1N2u33an7PvekdMKEJMVICYrQExWgJisADFZAWKyAsRkBYjJChA7uLJ1M+hf55aj525+feI3eOdC94mf5A6nFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUg9nnfPZrnnNtK3rmUvfO3ceeOlr+cVoCYrAAxWQFisgLEZAWIyQoQkxUgJitATFaA2NbK9n33pJ7baJ5bu965/T33yE/82ylTm2OnFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUg9nPuoe/clU6tine873nv3MJObVLP/dqn/qU4rQAxWQFisgLEZAWIyQoQkxUgJitATFaAmKwAsa27bLee+Mq7P3e8b+26due9sN+2or5zN+y0AsRkBYjJChCTFSAmK0BMVoCYrAAxWQFisgLEDq5sz+1o79wdTm1D1+58VTve97t63ztyWgFisgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYj9TTzx1m+mdi8Zze8epT2Nq63znLbnnTH2/a04rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0Bs6y7bOxerO4+8dufz3rkq3jG1DZ3yxH+Da04rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0Ds4F22d96yOXVr7I4nbo53XvOdr+qcndc89TmvOa0AMVkBYrICxGQFiMkKEJMVICYrQExWgJisALGDK9sdU+vAb9tZrk0tVqe+hak189R3dI7TChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQ+0z9b/Xvu6/0idvfqW9/x52f8xN/decWuk4rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0Bs6y7bOzea57aD3/aa7Wj/uvOmW3fZAl9BVoCYrAAxWQFisgLEZAWIyQoQkxUgJitA7NK7bO9cne44936n7km9c9/5xFe19sRvwWkFiMkKEJMVICYrQExWgJisADFZAWKyAsRkBYhdurLded6pR75zv3vO+97v+7bdO3ber9MKEJMVICYrQExWgJisADFZAWKyAsRkBYjJChDbWtluPfEDF7pTG9w7H/l9q9Op/e6OqX+/a04rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0DsZ+ePd1aYU/fC3rlKXLtzRzu1k96xfs1PvJ13ajW+5rQCxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsS27rKd2miufds2dOpzXrvzd3Xnq1p74u/ZaQWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiG3dZXunqTXkndvQqefd8b7d8J2f5DlOK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUgJitA7NKV7bltqF1pZeqTPPfId37Oa3fedOu0AsRkBYjJChCTFSAmK0BMVoCYrAAxWQFisgLEPlO70ieauiV35zuaWiSfe79Tjzy17p1aYFvZAheRFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQ27rL9ol3f66tl4V3LpJ3voX33Uc7tUm9847ktXOvymkFiMkKEJMVICYrQExWgJisADFZAWKyAsRkBYhtrWzX7lwWTm1S33cf7Z2L5Knl99RNt3dyWgFisgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYgdXtmt3/k/35zxx/Tm1DN5x7jXfuXa989futALEZAWIyQoQkxUgJitATFaAmKwAMVkBYrICxMZWtu+zs8J8382v59au5/723M2+a0+8q3jNaQWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiFnZPt7OVvLOm1+ndqVrU49859+uOa0AMVkBYrICxGQFiMkKEJMVICYrQExWgJisALGxle2d/9P92vvWn3e+o6m/PefO7+gcpxUgJitATFaAmKwAMVkBYrICxGQFiMkKEJMVIHZwZXvn3nHH+9afa+d2tDvOLUe/bevsLlvgMWQFiMkKEJMVICYrQExWgJisADFZAWKyAsQ+T7xTFriZ0woQkxUgJitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0DsPyOjDu9EvhHgAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case #3｜Ozaki 術後瓣膜旁逆流的經導管關閉

## [Badalova N, et al. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.109550)

62 歲男性 **Ozaki 手術**（自體心包瓣重建）後 NYHA III；右冠瓣與無冠瓣間中重度 **PVL**；因高手術風險（STS 9.1%），TEE 導引下以 **5×4 mm Amplatzer Duct Occluder II** 經股動脈成功關閉，僅微量殘餘，6 個月改善。

> **為什麼值得讀**：Ozaki 術後 PVL 少見、過去多需再開刀。證實**經導管 PVL 關閉可行且安全** → PVL 關閉技術可延伸到自體心包瓣術後。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyCAIAAABnRsZeAAAHq0lEQVR4nO3dQY4jORIAwa1F///Lvdc+cQagcxnMNrtLSqWyHDwEon5+//79H4DOf29fAPA1sgLEZAWIyQoQkxUgJitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsRkBYj92nnxz89PdR1D7Gz2nXk3bn2j9eeu33nmNZ/73Jl27obTChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQ25qyXduZ0jvn3DTkuRnNnYnVmdOft56Nv+1z1849G04rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0Ds4JTt2sxp17Vze1J35mh3PnfHznTvuau6tUN3x4t/C2tOK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUgJitA7NqU7fec22W787kvTnDe2r87cwb3RU4rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0DMlG1m5sbZW7tdd9555jXz7zmtADFZAWKyAsRkBYjJChCTFSAmK0BMVoCYrACxa1O239sMOnO+89ak7I6/bafs976R0woQkxUgJitATFaAmKwAMVkBYrICxGQFiMkKEDs4ZWsz6J92JkdnvnammRO6L97JHU4rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0Bsa8r2ezs4d7w4SXluJvXca2fO0fpb+JPTChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQ25qy/d6e1PU170xSrr/vi3dy53Nn7u7d8eLzfI7TChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQ+zk3Obrj3FXN/L47bk2O3vqNZs7g3po5PmfnbjitADFZAWKyAsRkBYjJChCTFSAmK0BMVoCYrACxrSnbf3jrkdOBL07Kfm829NxvNHM++9zn3rrmNacVICYrQExWgJisADFZAWKyAsRkBYjJChCTFSA2dJftjluThbdmQ9dmXtWOWxuUZ846r936Rk4rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0Ds186LX9zuuWP9uTO3qN66V7d2rM7cknvOzM3NTitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQOzgLttzezRvzUremlmcec0z9+++6Hu/r9MKEJMVICYrQExWgJisADFZAWKyAsRkBYjJChDb2mX7op3p3plzpTNnjs/NWK/deucd557JWxuFnVaAmKwAMVkBYrICxGQFiMkKEJMVICYrQExWgNiTU7a3pl3Pfe7OO5/b+3tr3/D3dtnO/I3OcVoBYrICxGQFiMkKEJMVICYrQExWgJisADFZAWI/M7d7ntvQeeua127Nlf5t17x2bivwi0/dzjs7rQAxWQFisgLEZAWIyQoQkxUgJitATFaAmKwAsYO7bHfmDmdu99y55pnbatfM0f7p3K9w7i/FLlvgI2QFiMkKEJMVICYrQExWgJisADFZAWKyAsSu7bK9NTl6zsytord+o1vznS9e1dqLv4LTChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQOzhle2sj6cxvZC9s5XvP1Uw739dpBYjJChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIbU3Z/sNbH9vfuePFScpb20xfvFc7Zv4trN3aVrvmtALEZAWIyQoQkxUgJitATFaAmKwAMVkBYrICxA7usj3n1tTpjhcnVnfu8847n/O96d6d5+rcM+m0AsRkBYjJChCTFSAmK0BMVoCYrAAxWQFisgLEDk7ZztxH++JW0Znfd+17k6O3foUXZ52dVoCYrAAxWQFisgLEZAWIyQoQkxUgJitATFaA2K/bF9C7NaM5czb0xb2/35sbnnknz3FaAWKyAsRkBYjJChCTFSAmK0BMVoCYrAAxWQFi16ZsZ86VzjTzmm9N6N7aGTzTzE23TitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQOzn1rbLF724RXXmdt61me98a7r31tS4KVtgEFkBYrICxGQFiMkKEJMVICYrQExWgJisALGtXbYv7v5cW08Wnpt2veV7+2hvzaTeupM7zl2V0woQkxUgJitATFaAmKwAMVkBYrICxGQFiMkKENuasl2bOVm4M2d5bpJy5r7Sne9769d/cd/w2sz57DWnFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQkxUgdnDKdm3mf7q/ZWeedeadfHFL7vqaZ067znzanVaAmKwAMVkBYrICxGQFiMkKEJMVICYrQExWgNi1KdvvOTcpe+udd5ybdj332nObfdfO/b63vpHTChCTFSAmK0BMVoCYrAAxWQFisgLEZAWIyQoQM2X7f3JunvXW1thz87u35krXbr3zzNeuOa0AMVkBYrICxGQFiMkKEJMVICYrQExWgJisALFrU7Yz/9P92otbRWfuSV279dpzXnxydjitADFZAWKyAsRkBYjJChCTFSAmK0BMVoCYrACxg1O2M+cdd8ycHD03SXlujnbHre28azPnaG89OU4rQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0Ds58WdssBkTitATFaAmKwAMVkBYrICxGQFiMkKEJMVICYrQExWgJisADFZAWKyAsRkBYjJChCTFSAmK0BMVoCYrACx/wE6igL1gxLiPgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #4｜巨大冠狀動脈假性動脈瘤的分階段經皮處理

## [Lluch-Requerey C, et al. *Catheter Cardiovasc Interv* 2026](https://doi.org/10.1002/ccd.70769)

74 歲男性（AF、AS、無法開心手術）罹患**巨大冠狀動脈假性動脈瘤**；**覆膜支架**排除病灶→**左心耳封堵 (LAAC)** 以停用抗凝→追蹤期間再因症狀性 AS 完成 **TAVI**。為文獻中最大者之一。

> **為什麼值得讀**：假性動脈瘤罕見但可致命、開心手術風險高者難處理。示範**影像導引整合式經皮策略**：覆膜支架→LAAC（推測助血栓化）→處理 AS，串接多種介入工具解決複雜結構問題。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKCAIAAAD0S4FSAAAGIUlEQVR4nO3dQY4jNxAAQcvY/395/YOG1lyiqnMi7iP1SErwUih+fv/+/Q9Q9O/0AwC3yBuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWb9O/vjz+fyt51jiefPc8/978rfP7r3yvfc92eE39TnvdPJJOr0hS96QJW/IkjdkyRuy5A1Z8oYseUOWvCHraGrt2c67R6emx6amuE5eecq9X07vN/nM6Q1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVkXp9aeTW0IO3FvB9jUTNvUZ3XCM3/P6Q1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVljU2tvNDV79NPmtHZugHsjpzdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2SZWuN/mtotx/ec3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekDU2tfbGuaWpHWBTG9Ge33fnnrY3vu89Tm/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8i6OLX20+55PJkA877f/627R7/n9IYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhqxPb7/UG/X2lrkhdAOnN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZB3tWjuZTJqaajqZD7u3XWxqX9q9Z37jt39vi9vUp+H0hix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGrKOptZN5mqk5nqktXzufeWpa7p6pZ975STq9IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwha+mutan3nZot2zlrdWLnf3TvV/dsaqbN6Q1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVmfqd1jOyfPTvTmtO697xsn/J5N/eqeOb0hS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFrbGrtxNTE2xu3bT3bOXk2NdO2c97x5Kmc3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekLX0htCdE1HPereL7pxo7M2l3eP0hix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGrKOptWc776bceb/k1CTWzp1nU9/RvU9jatOe0xuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LGbgjduSHsjTd1nrzyPTtnFqf2/01xekOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q9bYDaH3ZoB2zku98X1P7Jwd3DmXdu+pnN6QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pB1NLX20ybPftp82NT3+8atZjt/G05vyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/Iurhr7cS9Sayd81L37rU8MXUz6b3vaOdT3fsGnd6QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pD12TmndeKNk0knc2k77y29Z2qr2Rs3wDm9IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwha+mutWc7d4/1prh27g+bMjV3eMLpDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWWO71t5o542Z9+zcAHfvFzs1/3dvps3pDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWa/ctXbPyYTQvWmqnXNa9z6rk6e6NwH2xvlOpzdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2QdTa092znlY1/a93beiPps51O5IRT4y+QNWfKGLHlDlrwhS96QJW/IkjdkyRuyLk6tPZu6jfGeqcmknZ/kvaeamv+79/26IRT4Y/KGLHlDlrwhS96QJW/IkjdkyRuy5A1ZY1NrfO+NO89O7Jw7PPnbezeiPnN6Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlDlqm1P3BvqunE1Cs/T2KdzGlN3eJ675Wn9sM5vSFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8Ieuz82bDe954j+fOT/LZ1JzWs5/2a3d6Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlD1sVdazvnlk7snFu6dzflzkmsnZOF99735P91ekOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q9bRrjVgM6c3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVn/AUqlBs3CDikMAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case #5｜以慢性腹瀉與孤立性重度 TR 表現的類癌心臟病

## [Kothia D, et al. *JCEM Case Rep* 2026](https://doi.org/10.1210/jcemcr/luag191)

50 多歲女性以嚴重低血鈉（Na 114）、慢性水瀉、水腫、體重減輕表現；CT 見鈣化腸繫膜腫塊與肝病灶，chromogranin A 1434、尿 5-HIAA 108；超音波示**瓣葉回縮之孤立性重度 TR**，符合**類癌心臟病**；肝切片證實 G2 神經內分泌瘤。

> **為什麼值得讀**：**孤立性右側瓣膜病變（瓣葉回縮型重度 TR）＋慢性腹瀉**應高度警覺**類癌心臟病**；chromogranin A 與尿 5-HIAA 是關鍵篩檢，並須納入三尖瓣介入評估。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKCAIAAAD0S4FSAAAGBUlEQVR4nO3dQa4bRwxAwSjI/a/sbL0wBjHaHXKeqvb+Gkvz0BuC/fnx48dfQNHf0w8A3CJvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2T9c/KPP5/Pn3qOJe5tnnv+rnZuvDv5fU/+RyfflXfyZ05vyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IOppae9abxOpNRJ04mR6bejd67+QzpzdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2RdnFp7dm9SZ+dk0rN7W82m9qWdmPrc3jvp9IYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhqyxqTV+djJ5tvMeTzZwekOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5aptd9wb8Zr5661e3beH9rj9IYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhqyxqbXeZNLO+yWntqm98fd94zM/c3pDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUPWxam1nVu+TpxsCHvjv332xmfuvZPPnN6QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pD16e2XumfnNrVnO5/ZDaH/D6c3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkHU2tvXH26N4OsClTv+AbN6L1nuqZ0xuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LGbgidmh+amsS6Z+cs3c4Zr6k3Z4rTG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsi7eELpztqz3VG809U3unDu8x+kNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1ZF3etPds5tzQ1PTY1aXfPzq1m3zYP5/SGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oasi1NrO+d4vm2r2bN7s2X3JsCm5g6nthKefK7TG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsi5Ore3cELZz19qznfN/z+59kzvveH029V45vSFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8Ievzxhsk75maTPq2aap7z7xzKnGqMqc3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkHU2tTc0PmbT7WW8T27f9j9wQCvw2eUOWvCFL3pAlb8iSN2TJG7LkDVnyhqyjG0JP5ml603L3ZtruTXG98ZmnvPG7cnpDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUPW0dTazn1pO/d4vXHy7NnOuzinZsueP3eqFKc3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkXbwh9MS9GxV33vL57I0Tbzs33k1t+Jv6y05vyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/Iuji1NjW3dMJT/ffPndpa98abOqc4vSFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IevohtB7du5a27nF7d53tXOr2T07d/jZtQb8grwhS96QJW/IkjdkyRuy5A1Z8oYseUPW0a61b7PzPk1Ten/Kzk17J5zekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QdbRrbWpu6Z6du8dOnDzzG7epTf0KO399pzdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2RdvCF05/apN94+ee9zp0zthzvxxok3pzdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2RdnFp7NnXb5j1vvKlz6g7Qk7/8bXOHJ5zekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QNTa19m12TjXtvAP0jd/Vzpk2pzdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2SZWvtjpuaWpmbLpubSdt55+mzq3XB6Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlD1tjU2s59WifuTWKd3OM59VRTf3nnPNzUL+j0hix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGrM/OKZ8pJ9NFU3Y+89RUYm/y7ITTG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbso6m1oDNnN6QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZP0LIfAVpt1XTU0AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: lead -->
# 💎 Take Home Message

### 1. **ADVANCE OUTCOMES**：ralinepag 讓 PAH 臨床惡化砍半（HR 0.45）；停藥率 19%
### 2. **微軸流泵 vs VA-ECMO**：高危 PCI 微軸流泵不劣於（非優於）VA-ECMO、負擔更輕
### 3. **RATE**：ECMO 抗凝可減量 / 改 LMWH，不劣於標準劑量、出血更少
### 4. **HOPE-3**：deramiocel 減緩晚期 Duchenne 心肌/骨骼肌退化（+4.55%）
### 5. **TAVI**：SEV 壓差佳/BEV 併發症少；低風險擴大死亡率減半但浮現差距；TF-TAVI 碳足跡僅 38%
### 6. **TEER**：基線 CRP>3 是 Mitral TEER 後死亡獨立因子（HR 1.98）；影像導引系統化
### 7. **看主要終點與設計方向**：兩個 RCT 是「非劣性」≠「更好」；omega-3 高劑量 AF 訊號再確認

---

<!-- _class: small-text -->
# 完整參考文獻 (1/2)

**Top 5 Picks**
1. McLaughlin VV, et al. ADVANCE OUTCOMES (ralinepag/PAH). [*Lancet* 2026.](https://doi.org/10.1016/S0140-6736(26)01011-1) [PMID 42520828](https://pubmed.ncbi.nlm.nih.gov/42520828/)
2. Zhao G, et al. Micro-axial flow pump vs VA-ECMO for high-risk PCI. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag520) [PMID 42521444](https://pubmed.ncbi.nlm.nih.gov/42521444/)
3. van Minnen O, et al. RATE (heparin dosing in ECMO). [*Lancet* 2026;408:357-366.](https://doi.org/10.1016/S0140-6736(26)00851-2) [PMID 42413523](https://pubmed.ncbi.nlm.nih.gov/42413523/)
4. McDonald CM, et al. HOPE-3 (deramiocel/Duchenne). [*Lancet* 2026.](https://doi.org/10.1016/S0140-6736(26)01385-1) [PMID 42526472](https://pubmed.ncbi.nlm.nih.gov/42526472/)
5. FIND-AF 2.0: Risk-Guided AF Screening Using EHR. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.079391) [PMID 42517218](https://pubmed.ncbi.nlm.nih.gov/42517218/)

**TAVI Section**
6. Hasan I, et al. BEV vs SEV in mixed aortic valve disease. [*J Cardiol* 2026.](https://doi.org/10.1016/j.jjcc.2026.07.015) [PMID 42532263](https://pubmed.ncbi.nlm.nih.gov/42532263/)
7. Elkasaby MH, et al. 2019 Low-Risk Expansion & TAVR (ITS). [*Cardiol Rev* 2026.](https://doi.org/10.1097/CRD.0000000000001404) [PMID 42522062](https://pubmed.ncbi.nlm.nih.gov/42522062/)
8. Friedericy HJ, et al. TF-TAVI vs SAVR environmental LCA. [*Heart* 2026.](https://doi.org/10.1136/heartjnl-2026-328011) [PMID 42527114](https://pubmed.ncbi.nlm.nih.gov/42527114/)

---

<!-- _class: small-text -->
# 完整參考文獻 (2/2)

**TEER Section**
9. Omote K, et al. OCEAN-Mitral: Systemic inflammation & outcomes after Mitral TEER. [*J Am Heart Assoc* 2026.](https://doi.org/10.1161/JAHA.125.048726) [PMID 42517440](https://pubmed.ncbi.nlm.nih.gov/42517440/)
10. Itabashi Y. Echocardiographic imaging for TEER. [*J Echocardiogr* 2026.](https://doi.org/10.1007/s12574-026-00748-9) [PMID 42525232](https://pubmed.ncbi.nlm.nih.gov/42525232/)

**Honorable Mentions**
11. von Scheidt M, et al. Plasma IMF & residual CAD risk / CHIP. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag587) [PMID 42522903](https://pubmed.ncbi.nlm.nih.gov/42522903/)
12. Omega-3 & AF: updated meta-analysis of 35 trials. [*Circ Arrhythm Electrophysiol* 2026.](https://doi.org/10.1161/CIRCEP.125.014785) [PMID 42517224](https://pubmed.ncbi.nlm.nih.gov/42517224/)
13. Ambulatory PAP & HF hospitalizations (CardioMEMS). [*JACC Heart Fail* 2026.](https://doi.org/10.1016/j.jchf.2026.103239) [PMID 42535981](https://pubmed.ncbi.nlm.nih.gov/42535981/)
14. Higher ED diuretic dosing for acute HF. [*JACC Heart Fail* 2026.](https://doi.org/10.1016/j.jchf.2026.103235) [PMID 42535982](https://pubmed.ncbi.nlm.nih.gov/42535982/)
15. Kazemian S, et al. CV risk-prediction models in cancer survivors. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag562) [PMID 42517578](https://pubmed.ncbi.nlm.nih.gov/42517578/)
16. EchoAI-Peds: pediatric echo deep learning. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.080619) [PMID 42517220](https://pubmed.ncbi.nlm.nih.gov/42517220/)

**Case Reports**
17. Akyüz AR, et al. Balloon rupture during Myval TAVI — propofol bailout. [*Catheter Cardiovasc Interv* 2026.](https://doi.org/10.1002/ccd.70778) [PMID 42517461](https://pubmed.ncbi.nlm.nih.gov/42517461/)
18. Stegmann A, et al. AR & aortic thrombus in LVAD. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.109544) [PMID 42524783](https://pubmed.ncbi.nlm.nih.gov/42524783/)
19. Badalova N, et al. Transcatheter PVL closure after Ozaki. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.109550) [PMID 42524779](https://pubmed.ncbi.nlm.nih.gov/42524779/)
20. Lluch-Requerey C, et al. Giant coronary pseudoaneurysm. [*Catheter Cardiovasc Interv* 2026.](https://doi.org/10.1002/ccd.70769) [PMID 42521449](https://pubmed.ncbi.nlm.nih.gov/42521449/)
21. Kothia D, et al. Carcinoid heart disease with isolated severe TR. [*JCEM Case Rep* 2026.](https://doi.org/10.1210/jcemcr/luag191) [PMID 42516846](https://pubmed.ncbi.nlm.nih.gov/42516846/)

---

<!-- _class: abbr -->
# 縮寫對照表 (1/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| PAH / PH | Pulmonary Arterial Hypertension / Pulmonary Hypertension | 肺動脈高壓／肺高壓 |
| 6MWD | 6-Minute Walk Distance | 六分鐘步行距離 |
| MCS | Mechanical Circulatory Support | 機械循環支持 |
| VA-ECMO | Veno-Arterial Extracorporeal Membrane Oxygenation | 靜脈-動脈葉克膜 |
| ECMO / ECLS | Extracorporeal Membrane Oxygenation / Life Support | 體外膜氧合／維生支持 |
| PCI | Percutaneous Coronary Intervention | 經皮冠狀動脈介入 |
| CHIP-PCI | Complex High-risk Indicated Patients PCI | 複雜高風險介入 |
| LVEF | Left Ventricular Ejection Fraction | 左心室射血分數 |
| MAE / MACE | Major Adverse (Cardiovascular) Events | 主要不良（心血管）事件 |
| AKI | Acute Kidney Injury | 急性腎損傷 |
| UFH / LMWH | Unfractionated / Low-Molecular-Weight Heparin | 普通／低分子量肝素 |
| aPTT | Activated Partial Thromboplastin Time | 活化部分凝血活酶時間 |
| DMD | Duchenne Muscular Dystrophy | 裘馨氏肌肉失養症 |
| PUL2.0 | Performance of the Upper Limb 2.0 | 上肢功能量表 2.0 |
| AF | Atrial Fibrillation | 心房顫動 |
| EHR | Electronic Health Records | 電子病歷 |

---

<!-- _class: abbr -->
# 縮寫對照表 (2/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| CHIP（血液） | Clonal Hematopoiesis of Indeterminate Potential | 意義未明克隆性造血 |
| IMF | Infrared Molecular Fingerprinting | 紅外分子指紋（光譜） |
| hs-CRP | High-Sensitivity C-Reactive Protein | 高敏 C 反應蛋白 |
| PAP / HFH | Pulmonary Artery Pressure / HF Hospitalization | 肺動脈壓／心衰住院 |
| TAVI / TAVR | Transcatheter Aortic Valve Implantation / Replacement | 經導管主動脈瓣植入／置換 |
| SAVR / TF-TAVI | Surgical AVR / Transfemoral TAVI | 外科主動脈瓣置換／經股 TAVI |
| AS / AR | Aortic Stenosis / Regurgitation | 主動脈瓣狹窄／逆流 |
| BEV / SEV | Balloon-Expandable / Self-Expanding Valve | 球擴式／自膨式瓣膜 |
| PVL / PPM | Paravalvular Leak / Permanent Pacemaker | 瓣膜旁逆流／永久節律器 |
| LCA | Life Cycle Assessment | 生命週期評估（環境） |
| TEER | Transcatheter Edge-to-Edge Repair | 經導管緣對緣修復 |
| MR / TR | Mitral / Tricuspid Regurgitation | 二尖瓣／三尖瓣逆流 |
| TTE / TEE | Transthoracic / Transesophageal Echocardiography | 經胸／經食道超音波 |
| live MPR | Live Multiplanar Reconstruction | 即時多平面重組 |
| LVAD / LAAC | LV Assist Device / LA Appendage Closure | 左心室輔助器／左心耳封堵 |
| NET / 5-HIAA | Neuroendocrine Tumor / 5-Hydroxyindoleacetic Acid | 神經內分泌瘤／5-羥基吲哚乙酸 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**
心臟內科｜結構性心臟病介入

> *本文件為讀書會共筆之教學整理，僅供醫療專業同仁臨床教學交流參考。*
