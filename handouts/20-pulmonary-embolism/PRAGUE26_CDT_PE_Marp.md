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
  section.lead h2 { color: #9ec5ff; }
  section.lead h3 { color: #ffffff; font-weight: normal; }
  section.lead p { color: #f1f3f5; }
  section.lead strong { color: #ffe082; }
  section.lead a { color: #ffd166; text-decoration: underline; }
  section.lead blockquote {
    background-color: #fff5f5;
    border-left: 5px solid #ba181b;
    color: #1a2740;
  }
  section.lead blockquote p { color: #1a2740; }
  section.lead blockquote strong { color: #ba181b; }
  section.divider {
    background-color: #0072bc;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 { color: #ffffff; border-bottom: none; font-size: 2.4em; text-align: center; }
  section.divider h2 { color: #ffffff; font-size: 1.4em; text-align: center; font-weight: bold; }
  section.divider h3 { color: #ffe082; font-size: 1.1em; text-align: center; font-weight: normal; }
  section.divider p, section.divider strong { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  a { color: #0072bc; }
  table { font-size: 0.70em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 5px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.88em;
  }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.66em; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.78em; }
footer: '謝慕揚 MD, PhD, FESC | PRAGUE-26 導管導向溶栓 | 2026'
---

<!-- _class: lead -->
# 中高風險肺栓塞的導管導向溶栓
## PRAGUE-26 — Catheter-Directed Thrombolysis in Intermediate-High–Risk Pulmonary Embolism
### N Engl J Med 2026

**謝慕揚 MD, PhD, FESC**

[原文連結：doi.org/10.1056/NEJMoa2608012](https://doi.org/10.1056/NEJMoa2608012)

> 效益來自**避免崩潰**，不是來自降低死亡率

---

# 一句話總結

在 **ESC 定義的中高風險急性肺栓塞 (PE)** 病人：

抗凝血 **＋ 低劑量導管導向溶栓 (CDT, alteplase 20 mg)**

| 7 天複合終點 | CDT | 單純抗凝血 |
|---|---|---|
| 死亡 / PE 復發 / 心肺崩潰 | **0.7%** | **6.8%** |

**RR 0.10（95% CI 0.02–0.44），P < 0.001；風險差 −6.1 個百分點**

主要出血**未增加**（1.4% vs 2.2%）——但**顱內出血 2 例 vs 0 例**

---

# 為什麼中高風險 PE 難處理

- **血行動力學穩定**，但 sPESI ≥ 1 + **RV dysfunction** + troponin/BNP 上升
- 「看起來還好」，卻有一成左右會在數天內急轉直下

| 策略 | 問題 |
|------|------|
| 單純抗凝血 | 仍有人在 48–72 小時崩潰，屆時再救風險更高 |
| 全身性溶栓（PEITHO） | 減少代償失調，但**大出血／顱內出血明顯增加** |
| 導管導向溶栓 (CDT) | 理論上保留療效、減少出血，但**缺乏硬終點隨機證據** |

> PRAGUE-26 要問的是：**不用超音波輔助的傳統 CDT，做得到嗎？**

---

<!-- _class: divider -->
# 試驗設計
## 捷克 11 家中心 · 558 人 · 無業界贊助

---

# 試驗設計

| 項目 | 內容 |
|------|------|
| 設計 | 研究者發起、多中心、**開放標籤**、隨機 1:1 |
| 地點／期間 | 捷克 11 家三級心血管中心；2022/10 – 2026/03 |
| 樣本數 | 558（80% power 偵測 1.5% vs 6.0%） |
| 顯著門檻 | **P < 0.047**（O'Brien–Fleming，兩次期中分析） |
| 主要終點 | 7 天內死亡 / PE 復發 / **心肺代償失調或崩潰** |
| 資金 | 捷克衛生部，**無業界贊助** |

> 分層因子：年齡、性別、單／雙側 PE、CTPA 時間、直接入院或轉診

---

# 「心肺代償失調／崩潰」怎麼定義

```text
1. 心跳停止或需要 CPR
2. 休克徵象
   低血壓：SBP < 90 mmHg 或下降 ≥ 40 mmHg 持續 ≥ 15 分鐘
           （或需升壓藥維持 SBP ≥ 90）
   ＋器官灌流不足：意識改變、少尿／無尿、lactate > 2 mmol/L
3. 啟動 ECMO
4. 插管或開始非侵襲性正壓呼吸
5. 第 24 小時–第 7 天 NEWS ≥ 9（間隔 15 分鐘連續兩次確認）
```

> **注意**：第 4、5 項在**開放標籤**試驗中最容易受判讀影響——這是本試驗最主要的偏差來源。

---

# 收案與排除

**納入**：18–80 歲 · CTPA 證實**近端 PE**（主肺動脈或葉動脈）· 症狀 < 14 天
sPESI ≥ 1 + **RV/LV ≥ 0.9** + troponin 或 natriuretic peptide 上升

**排除（就是臨床紅旗清單）**：

- 活動性出血、任何出血性中風、6 個月內缺血性中風／TIA
- 3 個月內顱部外傷、7 天內大手術
- **活動性癌症或預期存活 < 2 年**
- Hb < 80 g/L、INR > 2.0、Plt ≤ 100K、**Cr > 2.26 mg/dL**
- 懷孕／哺乳、經卵圓孔的漂浮血栓

---

# 基線特徵

| 特徵 | CDT (n=280) | 標準治療 (n=278) |
|------|-------------|------------------|
| 年齡中位數 | 64 歲 | 64 歲 |
| 女性 | 41.1% | 40.6% |
| 雙側 PE | 98.2% | 98.2% |
| 外院轉入 | 49.3% | 49.6% |
| RV/LV ratio 中位數 | 1.13 | 1.14 |
| TAPSE 中位數 | 16 mm | 16 mm |
| troponin / ULN | 4.6 | 4.7 |
| **曾有血栓栓塞病史** | 22.5% | **32.4%** (SMD 22.3%) |

> 唯一 SMD > 20% 的變項，方向對 CDT 有利，判讀時要留意。

---

<!-- _class: divider -->
# 介入細節
## 刻意選了「任何導管室都做得到」的方式

---

# CDT 怎麼做

```text
導管：4-Fr valved infusion catheter（10 cm 灌注段）
      例 Cragg–McNamara 4-Fr（Medtronic）
      → 沒有超音波輔助、沒有大口徑抽吸裝置

給藥：每根導管 bolus alteplase 1 mg
      → 1 mg/hr/導管 持續灌注
      → 雙側總量 20 mg；單側 10 mg

抗凝：灌注期間「減量」UFH，目標 aPTT 50–60 秒

結束：拔管，不中斷接回治療劑量抗凝血
```

> **20 mg alteplase ≒ PEITHO 全身性溶栓劑量的五分之一**

---

# 執行時效 — 這是可複製的關鍵

| 指標 | 數值 |
|------|------|
| 隨機分派 → 開始 CDT 中位時間 | **76 分鐘**（IQR 49–126） |
| **3 小時內開始的比例** | **89.3%** |
| 導管置放成功率 | 99.6%（279/280） |
| 雙側 PE 實際 alteplase 劑量 | 19.9 ± 1.2 mg |
| 平均灌注時間 | 9.3 ± 0.95 小時 |

> 若你的流程要 8 小時才排得到導管室，**PRAGUE-26 的結果不能直接套用**。

---

<!-- _class: divider -->
# 結果
## 好處 100% 來自「避免崩潰」

---

# 主要終點與各成分

| 終點 | CDT (n=280) | 標準治療 (n=278) | RR (95% CI) |
|------|-------------|------------------|-------------|
| **主要複合終點（7 天）** | **2 (0.7%)** | **19 (6.8%)** | **0.10 (0.02–0.44)** |
| 任何原因死亡 | 0 (0%) | 4 (1.4%) | 0 |
| PE 復發 | 2 (0.7%) | 1 (0.4%) | 1.99 (0.18–21.77) |
| **心肺代償失調／崩潰** | **2 (0.7%)** | **15 (5.4%)** | **0.13 (0.03–0.57)** |

> 好處全部來自減少崩潰；PE 復發數字上甚至略多（無統計意義）。
> **不要把 RR 0.10 讀成「救命十倍」——死亡率本來就極低。**

---

# 次要與過程指標

| 指標 | CDT | 標準治療 |
|------|-----|----------|
| 24 小時 RV/LV ratio 中位數 | **0.94** | 1.07 |
| ICU 停留 | 2.1 天 | 2.8 天 |
| 住院天數 | 4.3 天 | 5.1 天 |
| **第一線治療失敗（需升級）** | **0 (0%)** | **12 (4.3%)** |
| 30 天 WHO class I | 58.2% | 44.6% |
| 30 天嚴重不良事件 | 6.4% | 7.6% |

> **崩潰 5.4% ＋ 需升級 4.3% ≒ 每 10 個中高風險 PE 就有 1 個在單純抗凝血下走偏。**

---

# 安全性：出血才是真正的對價

| 出血事件（7 天） | CDT | 標準治療 | P |
|----------|-----|----------|---|
| BARC ≥ 2 臨床相關出血 | 13 (4.6%) | 14 (5.0%) | 0.85 |
| GUSTO 主要出血 | 4 (1.4%) | 6 (2.2%) | 0.54 |
| ISTH 主要出血 | 5 (1.8%) | 7 (2.5%) | 0.58 |
| **顱內出血** | **2 (0.7%)** | **0** | 0.50 |
| 缺血性中風 | 0 | 1 (0.4%) | 0.50 |

30 天的數字與 7 天一致（BARC ≥ 2：5.7% vs 5.8%）。

---

# 兩例顱內出血的來龍去脈

1. **alteplase 灌注剛結束、高血壓危象時**發生
2. **第 5 天，在有紀錄的 LMWH 過量給藥情境下**發生

> 這兩例都不是「溶栓劑無可避免的代價」，而是**血壓控制**與**抗凝血劑量管理**的問題。

**反方向也要講**：標準治療組有 1 例致命性出血——發生在第 3 天崩潰後升級為
**全身性溶栓 + 機械取栓 + ECMO** 之後。

> **延後反應同樣有出血代價。**

---

# 與其他試驗的定位

| 試驗 | 介入 | 主要發現 |
|------|------|----------|
| **PEITHO** (2014) | 全身性 tenecteplase | 減少代償失調，**大出血／ICH 明顯增加** |
| **ULTIMA** (2014) | 超音波輔助 CDT | 改善 24 小時 RV/LV（替代終點） |
| **HI-PEITHO** (2026) | USCDT，族群加了惡化指標 | 減少複合終點，同樣來自減少崩潰 |
| **PEERLESS** (2025) | 大口徑機械取栓 vs CDT | 提示穩定化，未顯示硬終點優勢 |
| **PRAGUE-26** (2026) | **傳統 CDT（無超音波）** | 0.7% vs 6.8%，出血未增加 |

> **獨特貢獻**：把證據延伸到**便宜、普及的傳統 CDT**，且族群完全依 2019 ESC 定義。

---

# 限制

1. **單一國家、以白人為主** — 亞洲族群溶栓後 ICH 風險無法回答
2. **開放標籤**，且臨床事件委員會也知道分組（複合終點含插管、NEWS）
3. 無篩選紀錄，收案代表性不明
4. 未與 USCDT、全身性溶栓、機械取栓直接比較
5. **排除 > 80 歲** — 而這是台灣風險最高的一群
6. 排除活動性癌症、Cr > 2.26、Plt ≤ 100K → **真實世界不少人不符合條件**
7. 死亡率極低，可能反映三級中心可立即救援的環境

---

<!-- _class: divider -->
# 臨床應用
## 誰該做？怎麼做？

---

# 決策路徑

```text
CTPA 確診近端 PE（主肺動脈或葉動脈）
        ↓
血行動力學穩定？ ─ 否 → 高風險 PE：全身溶栓 / 取栓 / ECMO
        ↓ 是
sPESI ≥ 1 ?
        ↓ 是
RV/LV ≥ 0.9（Echo 或 CT）＋ troponin 或 BNP 上升？
        ↓ 是   → 這就是 PRAGUE-26 的族群
        ↓
檢查排除條件（出血史、近期手術/中風、Plt、INR、Cr、年齡 > 80）
        ↓
可行 → 3 小時內啟動 CDT：alteplase 20 mg / 約 10 小時
       ＋減量 UFH（aPTT 50–60）＋嚴格血壓控制
```

---

# 實務上的四個提醒

1. **時效可複製**：中位 76 分鐘、89.3% 在 3 小時內；流程慢就沒有這個結果
2. **PERT 有價值**：升級治療的決策多半由主治醫師會同 PE response team 判斷
3. **轉診網絡照抄 STEMI 模式**：本試驗 49.5% 病人是外院轉入的
4. **血壓控制與抗凝血劑量標準化，比選哪根導管更重要**——兩例 ICH 都出在這裡

---

# Clinical Pearls

> **Pearl 1**：CDT 的好處是**防止崩潰**，不是降低死亡率。向家屬解釋要說「減少接下來幾天惡化到需要插管、升壓藥或 ECMO 的機會」。

> **Pearl 2**：**20 mg alteplase ≠ 全身性溶栓**。低劑量 + 局部給藥 + 減量 heparin，三者缺一不可。

> **Pearl 3**：**RV/LV ≥ 0.9 + troponin 上升**是把「看起來還好」的 PE 分流出來的兩個開關。

> **Pearl 4**：單純抗凝血下，**每 10 人有 1 人走偏**（5.4% 崩潰 + 4.3% 需升級）。

---

<!-- _class: small-text -->
# 參考文獻

1. Kroupa J, Radvan M, Mrozek J, et al. Catheter-Directed Thrombolysis in Intermediate-High–Risk Pulmonary Embolism (PRAGUE-26). [*N Engl J Med*. 2026.](https://doi.org/10.1056/NEJMoa2608012)
2. Konstantinides SV, Meyer G, Becattini C, et al. 2019 ESC guidelines for acute pulmonary embolism. [*Eur Heart J*. 2020;41:543-603.](https://doi.org/10.1093/eurheartj/ehz405)
3. Meyer G, Vicaut E, Danays T, et al. Fibrinolysis for patients with intermediate-risk pulmonary embolism (PEITHO). [*N Engl J Med*. 2014;370:1402-11.](https://doi.org/10.1056/NEJMoa1302097)
4. Rosenfield K, Klok FA, Piazza G, et al. Ultrasound-facilitated, catheter-directed fibrinolysis for acute pulmonary embolism (HI-PEITHO). [*N Engl J Med*. 2026;394:1979-1990.](https://doi.org/10.1056/NEJMoa2516567)
5. Kucher N, Boekstegers P, Müller OJ, et al. Ultrasound-assisted catheter-directed thrombolysis (ULTIMA). [*Circulation*. 2014;129:479-86.](https://doi.org/10.1161/CIRCULATIONAHA.113.005544)
6. Jaber WA, Gonsalves CF, Stortecky S, et al. Large-bore mechanical thrombectomy vs catheter-directed thrombolysis (PEERLESS). [*Circulation*. 2025;151:260-73.](https://doi.org/10.1161/CIRCULATIONAHA.124.072364)
7. Kroupa J, et al. Design and rationale of PRAGUE-26. [*EuroIntervention*. 2025;21:e642-e648.](https://doi.org/10.4244/EIJ-D-24-01085)
8. Pruszczyk P, Klok FA, Kucher N, et al. Percutaneous treatment options for acute pulmonary embolism: ESC WG / EAPCI consensus. [*EuroIntervention*. 2022;18:e623-e638.](https://doi.org/10.4244/EIJ-D-22-00246)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

[PRAGUE-26 — N Engl J Med 2026](https://doi.org/10.1056/NEJMoa2608012)
