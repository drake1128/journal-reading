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
    font-size: 26px;
  }
  section.lead {
    background-color: #1a2740;
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 2.0em; border-bottom: none; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #b0c4de; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.3em; text-align: center; }
  section.divider h2 { color: #ffe066; text-align: center; }
  section.divider h3 { color: #ffffff; text-align: center; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; font-size: 1.35em; }
  h2 { color: #0072bc; font-size: 1.05em; }
  h3 { color: #555555; font-size: 0.95em; }
  table { font-size: 0.68em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 5px 8px; }
  td { padding: 3px 8px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.4em 0.9em;
    font-size: 0.85em;
  }
  pre {
    background-color: #f5f6fa;
    color: #2d3436;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 0.7em;
    font-size: 0.62em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  a { color: #0072bc; }
  footer { color: #787878; font-size: 0.55em; }
  section.small-text { font-size: 0.72em; }
  section.ref { font-size: 0.58em; }
  section.ref h1 { font-size: 1.6em; }
  ul, ol { margin: 0.2em 0; }
  li { margin: 0.1em 0; }
footer: '謝慕揚 MD, PhD, FESC | 高齡族群 M-TEER / T-TEER 老年評估工具 | 2026'
---

<!-- _class: lead -->
# 高齡族群的 M-TEER / T-TEER
## 把老年心臟學工具納入病人選擇與圍術期照護
### CGA、MNA-SF、KCCQ、認知篩檢——歷史、驗證系列與 Program 建置

**謝慕揚 MD, PhD, FESC** | 2026-09-12

錨定文獻：[Alkhatib R, et al. Circ Cardiovasc Interv 2026 (doi:10.1161/CIRCINTERVENTIONS.126.017207)](https://doi.org/10.1161/CIRCINTERVENTIONS.126.017207)

---

# 為什麼這一塊最容易被忽略

- TEER 病人**本質上是老年醫學病人**：COAPT 中位 74 歲、TRILUMINATE 78 歲、EuroTR 78.4 歲
- Program 建置時注意力集中在 **TEE 解剖、器械、技巧**
- 功能、營養、認知、健康狀態常只用一句「frail-looking」帶過

## Alkhatib 2026 (Circ CV Interv) 指出的三個缺口

1. 臨床試驗對 **frailty 與認知**描述不一致 → 無法指導「誰不該做」
2. **缺乏 TEER 專屬**的年齡相關風險工具（TAVR 已有 EFT、GASS-TAVR）
3. **長期功能獨立與 QoL 終點**資料稀少

> 建議整合：CGA、MNA-SF、Katz ADL、KCCQ、認知篩檢

---

# 本講義的立場

> 這些工具**沒有一個是為 TEER 發明的**。
> 它們各有 30–80 年歷史，經過多國、數千人的 validation 系列。
> 理解「從哪裡來、怎麼被驗證」，是正確用在 TEER 病人身上的前提。

| 工具 | 第一篇 | 關鍵 validation |
|---|---|---|
| CGA | Warren, BMJ **1943** | Rubenstein NEJM 1984 → Stuck Lancet 1993 → Cochrane 2017 |
| Katz ADL | Katz, JAMA **1963** | GASS-TAVR 2026 |
| MNA / MNA-SF | Guigoz, Facts Res Gerontol **1994** | Vellas 1999 → Rubenstein 2001 → Kaiser 2009 |
| KCCQ | Green & Spertus, JACC **2000** | Spertus 2005 (MCID) → Arnold 2013 (AS) → KCCQ-12 2015 → FDA COA |
| MMSE / Mini-Cog / MoCA | **1975 / 2000 / 2005** | EFT 2017 選用 Mini-Cog |

---

<!-- _class: divider -->
# Part 1
## CGA 周全性老年評估
### Comprehensive Geriatric Assessment

---

# CGA 是什麼：定義與領域

**NIH 共識會議 1987（JAMA 1988）**：多面向、跨專業的診斷過程，發現並解釋老年人的多重問題、盤點資源、評估服務需求、**發展協調的照護計畫**

| 領域 | 常用工具 | 在 TEER 的意義 |
|---|---|---|
| 功能 | Katz ADL、Lawton IADL、步速 | 術後能否恢復獨立 |
| 認知 | Mini-Cog、MoCA、MMSE | 譫妄風險、決策能力 |
| 營養 | MNA-SF、GNRI | 死亡率最強預測因子之一 |
| 衰弱 | Fried、CFS、EFT、SPPB | 6 週死亡率 |
| 情緒 / 社會 / 用藥 / 感官 | GDS、照顧者、多重用藥 | 出院去向、回診 |

> CGA **不是問卷，是流程**

---

# CGA 發展史 (1)：1943 → 1984

## 1943 — Marjory Warren，BMJ「Care of Chronic Sick」
- West Middlesex 濟貧院醫務所數百位「無望」臥床老人
- **逐一系統評估 → 分類 → 復健 → 出院**：CGA 雛形；「老年醫學之母」
- 主張綜合醫院應有專責老年病房

## 1984 — Rubenstein，NEJM：第一個 CGA RCT
- Sepulveda VA；高安養院風險衰弱住院老人，GEU (n=63) vs 常規 (n=60)
- **1 年死亡率 23.8% vs 48.3% (P<0.005)**
- 進安養院 12.7% vs 30.0%；功能與士氣改善；成本較低

---

# CGA 發展史 (2)：1993 → 2017

## 1993 — Stuck，Lancet 統合分析（28 試驗、~10,000 人）
- 住院型 GEMU「追蹤時仍住家中」**OR 1.68 (1.17–2.41)**
- **只有「評估者有醫療決策控制權 + 延續追蹤」的 program 才有效**
- → 老年評估必須進入 Heart Team，不能只是會診單

## 2011 BMJ → 2017 Cochrane — Ellis（29 試驗、13,766 人）
- 更可能存活且住在自己家中（RR ~1.06）；進機構較少（RR ~0.80）
- 對死亡率本身影響小 → CGA 的價值在**功能與獨立**

---

# CGA 進入結構性心臟病：2014 → 2026

| 年 | 研究 | 重點 |
|---|---|---|
| 2014 | Afilalo, JACC review | Frailty 概念系統性進入心血管照護 |
| 2017 | **FRAILTY-AVR** (n=1,020, 7 種量表) | **EFT**（椅子起立 ×5、Mini-Cog、Hb、albumin）1 年死亡 aOR **3.72**；ΔC 0.071 |
| 2018 | FRAILTY-AVR 營養次分析 (n=1,158) | MNA-SF 與 1 年死亡獨立相關，**獨立於衰弱** |
| 2026 | **GASS-TAVR** (n=562, 中位 83 歲) | **MNA-SF + BADL + eGFR + PASP**；AUC 0.92 / 驗證 0.87，**優於 STS** |

> EFT = 把 CGA 濃縮成 4 項的結構性心臟病版本；GASS-TAVR = 老年工具比外科分數更能預測「治療是否有意義」

---

# 功能量表：Katz ADL (1963) 與 Lawton IADL (1969)

## Katz Index of ADL — JAMA 1963
- Cleveland Benjamin Rose Hospital；觀察髖部骨折老人**復原順序**
- 六項：洗澡、穿衣、如廁、移位、大小便控制、進食（0–6 分）
- **世界第一個標準化功能量表**；GASS-TAVR 以「loss of ≥2 BADL」定義功能下降

## Lawton–Brody IADL — Gerontologist 1969
- 八項：電話、購物、備餐、家務、洗衣、交通、**服藥**、理財
- 比 ADL 更早退化；Katz 6/6 的病人可能已無法自行管理 DOAC

> 術前記錄基線、術後 1 年重測；「功能未惡化」應與「MR/TR ≤2+」並列品質指標

---

<!-- _class: divider -->
# Part 2
## MNA 與 MNA-SF
### Mini Nutritional Assessment

---

# 為什麼 TEER 病人要篩營養

右心衰竭 → 腸道 / 肝鬱血 → 蛋白流失 → 惡病質

| 研究 | 族群 | 營養不良盛行率 | 結果 |
|---|---|---|---|
| Besler 2020, EJHF | T-TEER n=86 (MNA) | **94%** 不良或有風險 | 74% 術後 MNA 改善；僅改善者 NT-proBNP ↓、QoL ↑ |
| Scotti 2023, JACC (COAPT) | M-TEER n=552 (GNRI) | 17% | 4 年死亡 68.3% vs 52.8%，aHR 1.37；TEER 獲益一致 |
| Pagnesi 2025, EJHF (EuroTR) | T-TEER n=1,034 (GNRI) | 20.4% | 2 年死亡 45.9% vs 28.2%，**aHR 1.53** |
| Shibata 2025, JACC Adv (OCEAN) | M-TEER n=1,909 | — | 1 個月 GNRI 改善 54.8%；**與手術成功連動**、預測存活 |

> 營養不良是**可逆的**，且與 TEER 技術成功連動

---

# MNA 發展史 (1)：Nestlé–Toulouse–New Mexico

## 1991–1994 — 三方合作誕生
- **Nestlé** 研究中心 (Guigoz)、**Toulouse** 老年醫學 (Vellas)、**New Mexico** Aging Process Study (Garry)
- **第一篇**：Guigoz Y, Vellas B, Garry PJ. *Facts Res Gerontol* **1994**;4(Suppl 2):15–59 — **未收錄 PubMed**
- 1996 Nutr Rev：第一篇可查版本，標題即「…as part of the geriatric evaluation」

## 1999 — Vellas，Nutrition：完整 MNA 驗證
- **18 題、30 分**：人體測量、整體、飲食、主觀四部分
- ≥24 正常；17–23.5 有風險；<17 營養不良
- 對照臨床營養狀態：敏感度 ~96%、特異度 ~98%

---

# MNA 發展史 (2)：MNA-SF 的兩次里程碑

## 2001 — Rubenstein，J Gerontol A：MNA-SF 誕生
- 重新分析 **881 人**（法 151、西 400、新墨西哥 330；平均 76.4 歲）
- 依相關性、內部一致性、完成率、施測難易挑題 → **6 題、0–14 分**
- 與完整 MNA **r = 0.945**；≥11 為正常 → **敏感度 97.9%、特異度 100%**
- 提出**兩階段篩檢**：SF 陽性再做完整 MNA

## 2009 — Kaiser，J Nutr Health Aging：修訂版
- 27 資料集 (n=6,257) → 12 資料集 **2,032 人（平均 82.3 歲）**
- **小腿圍 (CC ≥31 cm) 可取代 BMI**（臥床、水腫時）
- 改為**三分類**：12–14 正常 / 8–11 有風險 / **0–7 營養不良**
- 2010 JAGS：24 研究 4,507 人；復健 ~50%、醫院 ~39%、機構 ~14%、社區 ~6%

---

# MNA-SF 六題（現行版）與 GNRI

```text
A. 3 個月食量減少？       0 嚴重 / 1 中度 / 2 無
B. 3 個月體重減輕？       0 >3kg / 1 不知 / 2 1-3kg / 3 無
C. 行動能力？             0 臥床/輪椅 / 1 可下床不出門 / 2 可外出
D. 3 個月心理壓力或急性病？ 0 有 / 2 無
E. 神經心理問題？         0 重度失智或憂鬱 / 1 輕度失智 / 2 無
F1. BMI                   0 <19 / 1 19-21 / 2 21-23 / 3 ≥23
F2. 小腿圍（BMI 不可得時） 0 <31cm / 3 ≥31cm
────────────────────────────────────────────
0-14：12-14 正常 | 8-11 有風險 | 0-7 營養不良    ≈3 分鐘、免抽血
```

**GNRI**（Bouillanne 2005, AJCN）= 1.489 × albumin (g/L) + 41.7 × (體重/理想體重)；**≤98 有風險**
→ 登錄研究回溯用 GNRI；門診前瞻用 MNA-SF；**兩者互補**（行為 vs 生化）

---

<!-- _class: divider -->
# Part 3
## KCCQ
### Kansas City Cardiomyopathy Questionnaire

---

# 為什麼 TEER 特別需要 KCCQ

- TEER 的核心價值是**症狀與生活品質**，不只是壽命
  - MITRA-FR 中性；TRILUMINATE 死亡 / HFH 無差異，**KCCQ 顯著改善**
- 沒有可靠的 PRO，T-TEER 幾乎無法證明自己的價值
- **FDA 認證為 Clinical Outcome Assessment (COA)**；ACC/AHA 品質績效指標

| KCCQ-OS | 對應 |
|---|---|
| <25 | ≈ NYHA IV |
| 25–49 | 差 |
| 50–74 | 尚可 |
| 75–100 | 良好 |

**MCID：5 分**；10 分中度；20 分大幅（Spertus 2020, JACC review）

---

# KCCQ 發展史 (1)：2000 → 2005

## 2000 — Green, Porter, Bresnahan, Spertus，JACC：第一篇
- Kansas City Mid America Heart Institute；**23 題、自填**
- 五領域：身體限制、症狀（頻率/嚴重/穩定）、自我效能、社會干擾、QoL
- 驗證：**70 穩定 + 59 失代償**、EF <40%；對照 MLHFQ、SF-36，3 個月重測
- 穩定者變化 0.8–4.0 分；改善者 15.4–40.4 分 → **敏感度優於 MLHFQ 與 SF-36**

## 2005 — Spertus，Am Heart J：MCID
- 14 中心 476 人，盲化心臟科醫師判定 6 週臨床變化
- 小 / 中 / 大改善：**+5.7 / +10.5 / +22.3 分** → **5 分 = MCID**
- 監測個別病人變化的 C 統計量 > NYHA > 6MWT

---

# KCCQ 發展史 (2)：2013 → 2020

| 年 | 文獻 | 貢獻 |
|---|---|---|
| 2013 | Arnold, Circ Heart Fail (**PARTNER** n=955) | 在**主動脈瓣狹窄**驗證：ICC 0.65–0.76、TAVR 後 +13–30 分、基線低 → 死亡高 |
| 2015 | Spertus & Jones, Circ CV Qual Outcomes | **KCCQ-12**：3 研究 4,168 人；與原版相關 >0.93；重測 >0.76；~3 分鐘 |
| 2020 | Spertus, JACC State-of-the-Art | FDA COA；分數對照；試驗分析建議（mean Δ、responder、alive & well） |

> 2013 年的 PARTNER 驗證是關鍵一步：**心衰竭量表可用於瓣膜病** → 為 COAPT / TRILUMINATE 鋪路

---

# KCCQ 在 TEER：COAPT 與 TRILUMINATE

| 試驗 / 分析 | 結果 |
|---|---|
| **COAPT** (Arnold, JACC 2019) | 基線 OS 52.4；1 個月組間差 **+15.9**；24 個月 +12.8；「存活且 ≥10 分改善」36.4% vs 16.6%，**NNT 5.1** |
| COAPT 年齡 (Song, JCI 2022) | ≥74 歲 aHR 0.58；QoL 改善不分年齡，年長者 HFH 降幅較小 |
| COAPT (Arnold, JACC HF 2021) | KCCQ 預後價值**獨立於 NYHA 與 6MWT** |
| **TRILUMINATE** (Sorajja, NEJM 2023) | Win ratio 1.48；**由 KCCQ ≥15 分改善驅動**（49.7% vs 26.4%）；死亡/HFH 無差異 |
| TRILUMINATE (Arnold, JACC 2024) | 1 年組間差 +10.4；「alive & well」74.8% vs 45.9%，**NNT 3.5**；**基線越高獲益越小** |
| TRILUMINATE 2 年 (Kar, Circ 2025) | 健康狀態改善持續 |

> 開放標籤的安慰劑效應爭議存在，但 >10 分改善遠超典型安慰劑；**T-TEER 不量 KCCQ 等於沒有主要終點**

---

<!-- _class: divider -->
# Part 4
## 認知篩檢
### MMSE (1975) · Mini-Cog (2000) · MoCA (2005)

---

# 為什麼要篩認知：TEER 的雙向證據

## 失智 → 結果差（Elzeneini 2024, NIS 2016–19, n=24,550）
- 3.6% 有失智；院內死亡 **OR 4.31** (2.65–6.99)
- 譫妄 OR 5.88、急性中風 OR 8.87、出院至機構 OR 2.71

## 但低灌流性認知障礙可逆（海德堡團隊）
- Nikendei 2016 (Psychosom Med)：MitraClip 後圖形記憶 (p=.003)、執行功能 (p<.001) 改善
- Terhoeven 2019：**基線越差改善越大**「the sicker the better」

## 手術本身的腦部風險
- Blazek 2015 (EuroIntervention)：MitraClip 後 DW-MRI 新發栓塞病灶常見
- Braemswig 2023 (JAHA)：結構介入後新發腦微出血

> 篩檢是為了**照護計畫與譫妄預防**，不是為了拒絕

---

# 三個工具的歷史

| 工具 | 第一篇 | 設計背景 | 特性 |
|---|---|---|---|
| **MMSE** | Folstein, J Psychiatr Res **1975** | Johns Hopkins 精神科住院病人 | 30 分 11 題；史上引用最多；**對 MCI 不敏感**、天花板效應、2001 起版權收費 |
| **Mini-Cog** | Borson, Int J Geriatr Psychiatry **2000** | Univ. Washington，多語言低教育族群 | **3 詞回憶 + 畫鐘**；3 分鐘、免費；**EFT 選用** |
| **MoCA** | Nasreddine, JAGS **2005** | Montréal，補 MMSE 對 MCI 的盲點 | 30 分 10 分鐘；94 MCI + 93 AD + 90 對照；切點 26；**MCI 敏感度 90% vs MMSE 18%**；需認證 |

> 門診第一線用 **Mini-Cog**；陽性 → 老年科 / 神經科做 MoCA；**術前務必留基線**以判讀術後譫妄

---

<!-- _class: divider -->
# Part 5
## 衰弱 Frailty
### 串起所有工具的軸線

---

# Frailty 三個經典工具

## Fried 表型 — J Gerontol A 2001
- Cardiovascular Health Study **n=5,317**；五項：體重減輕、疲憊、握力弱、步速慢、低活動
- ≥3 = frail；首次操作型定義；獨立預測跌倒、失能、住院、死亡

## Clinical Frailty Scale — Rockwood, CMAJ 2005
- Canadian Study of Health and Aging n=2,305；**1（非常健康）–9（末期）**；1 分鐘
- 每升 1 級，5 年死亡率約 +20%；Heart Team 的共通語言

## Essential Frailty Toolset — Afilalo, JACC 2017
- 椅子起立 ×5、Mini-Cog、Hb、albumin；FRAILTY-AVR 中最強預測因子

---

# TEER 專屬的衰弱資料

| 研究 | 設計 | 結果 |
|---|---|---|
| **Metze 2017**, JACC CV Interv (Köln) | n=213 前瞻 Fried | **45.5% frail**；器械成功相同 (81 vs 85%)；症狀改善相同；**6 週死亡 8.3% vs 1.7%**；長期 HR 3.06 |
| Arnold 2017 社論 | — | 「Frail Elderly, the Ideal Patients for MitraClip」 |
| **Kundi 2019**, EHJ (Medicare) | TMVr n=3,746, HFRS | 1 年死亡 低/中/高 **12.8 / 29.7 / 40.9%** |
| Rios 2022, AJC (NIS) | 行政資料 | frailty 與 M-TEER 不良結果相關 |
| **Metze 2025**, J Cachexia Sarcopenia Muscle | n=524 | 疲憊 HR 2.24、步速 2.74 預測死亡；**體重減輕不預測**；**S-frailty (疲憊+步速)** 使 MitraScore C 0.645→**0.700** |

> 一致訊息：衰弱**不降低成功率與症狀改善，但死亡率 2–3 倍** → 不是「不做」的理由，而是「怎麼做、做完怎麼照顧」的理由

---

<!-- _class: divider -->
# Part 6
## 放進你的 TEER Program

---

# 門診第一線篩檢包（≈15 分鐘，護理師 / 個管師）

```text
┌─ TEER Geriatric Screening Bundle ──────────────────────────┐
│ 1. Katz ADL (6) + Lawton IADL (8)                  2 min   │
│ 2. MNA-SF (6 題；BMI 或小腿圍)                     3 min   │
│ 3. Mini-Cog (3 詞 + 畫鐘)                          3 min   │
│ 4. KCCQ-12 (自填)                                  3 min   │
│ 5. 步速 5 m 或椅子起立 ×5 + CFS (1-9)              2 min   │
│ 6. 多重用藥 (≥5) + 照顧者 / 居住                   2 min   │
│ 7. 抽血 albumin、Hb → GNRI、EFT                    —       │
└────────────────────────────────────────────────────────────┘
紅旗：MNA-SF ≤7 | Mini-Cog <3 | CFS ≥6 | ADL 依賴 ≥2 | KCCQ-OS <25
  → 轉老年科完整 CGA，並在 Heart Team 提出
```

---

# Heart Team 決策：從「能不能做」到「做了會不會好」

- 把 **KCCQ-OS、MNA-SF、CFS、Mini-Cog** 四個數字與 TEE 解剖、EuroSCORE / MitraScore **並列在會議簡報上**
- 老年科醫師**參與決策**（Stuck 1993：只寫會診單無效）
- 明確討論**治療目標**：延壽？減住院？改善 KCCQ？減利尿劑？→ 不同目標對應不同可接受風險
- CFS ≥7、重度失智、MNA-SF ≤7 且無可逆因素 → 坦誠討論 futility 與緩和照護

> GASS-TAVR 的啟示：老年工具比 STS 更能預測「1 年後是否活著且功能未惡化」

---

# 圍術期照護：術前優化 → 術中 → 術後 72 小時

| 時期 | 措施 | 依據 |
|---|---|---|
| 術前 2–4 週 | 蛋白質 1.2–1.5 g/kg/d、口服營養補充；利尿劑最佳化減少腸道鬱血 | Besler 2020、Goldfarb 2018 |
| 術前 | 用藥整合（抗膽鹼、BZD 減量）、視聽輔具、家屬譫妄衛教 | HELP 原則 |
| 術中 | 減少鎮靜深度、sedation-sparing 策略、縮短時間 | Rawish 2026 RCT（視聽分心減鎮靜） |
| 術後 24–72 h | CAM-ICU 譫妄篩檢、早期下床、當日拔導尿管、定向刺激、睡眠保護 | Elzeneini 2024 |
| 出院前 | 重測 Katz ADL；營養與復健轉介；照顧者參與出院計畫 | Alkhatib 2026 |

---

# 追蹤與品質指標

## 1、6、12 個月：KCCQ-12 + Katz ADL + MNA-SF
- 三者皆可**電話或 App** 完成

## Program 儀表板新增
- **1 年 alive & well**：KCCQ-OS ≥60 且未下降 >10（TRILUMINATE 定義）
- **1 年 ADL 未惡化比例**（GASS-TAVR 定義）
- 除了「MR/TR ≤2+」「30 天死亡」

> 前瞻性收集這些數據，就是**建立台灣 TEER 版 EFT / GASS 的基礎**——正是 Alkhatib 等人指出的最大研究缺口

---

# Take-Home Messages

1. **CGA 不是問卷而是流程**——Warren 1943 → Rubenstein NEJM 1984 → Stuck Lancet 1993 → Cochrane 2017：**評估必須連結管理權與長期追蹤**才有效
2. **MNA-SF 是 Nestlé–Toulouse–New Mexico 30 年的產物**：1994 首刊 → 1999 完整版 → 2001 Rubenstein 縮 6 題 (r=0.945) → 2009 Kaiser 小腿圍 + 三分類；在 TAVR 已證明**優於 STS**
3. **KCCQ 由 Spertus 團隊 2000 年 JACC 發表**：2005 MCID 5 分 → 2013 PARTNER 驗證瓣膜病 → 2015 KCCQ-12 → FDA COA；**T-TEER 的主要終點**
4. **認知篩檢用 Mini-Cog 起步**（EFT 內建、免費、3 分鐘）；失智 → M-TEER 院內死亡 OR 4.3，但低灌流性認知障礙**可逆**
5. 衰弱、營養不良、認知障礙**不降低 TEER 成功率與症狀改善，但死亡率 2–3 倍**——TEER 版 EFT 正在成形，**現在開始前瞻收集**

---

<!-- _class: ref -->
# 參考文獻 (1/3)

1. Alkhatib R, et al. TEER in Older Adults With Mitral and Tricuspid Valve Disease. [Circ Cardiovasc Interv 2026:e017207.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.017207) PMID 42723624
2. Esser R, et al. T-TEER in frail older adults: a cardiogeriatric framework. [Aging Clin Exp Res 2026;38:34.](https://doi.org/10.1007/s40520-025-03291-2) PMID 41442111
3. Solomon DH, et al. NIH Consensus: Geriatric assessment methods for clinical decision-making. [JAMA 1988;259:2450.](https://pubmed.ncbi.nlm.nih.gov/3280847/)
4. Warren MW. Care of Chronic Sick. [Br Med J 1943;2:822.](https://pubmed.ncbi.nlm.nih.gov/20785199/)
5. Rubenstein LZ, et al. Effectiveness of a geriatric evaluation unit: RCT. [N Engl J Med 1984;311:1664.](https://doi.org/10.1056/NEJM198412273112604) PMID 6390207
6. Stuck AE, et al. CGA: a meta-analysis of controlled trials. [Lancet 1993;342:1032.](https://doi.org/10.1016/0140-6736(93)92884-v) PMID 8105269
7. Ellis G, et al. CGA for older adults admitted to hospital. [Cochrane 2017;9:CD006211.](https://doi.org/10.1002/14651858.CD006211.pub3) PMID 28898390
8. Afilalo J, et al. Frailty assessment in the cardiovascular care of older adults. [JACC 2014;63:747.](https://doi.org/10.1016/j.jacc.2013.09.070) PMID 24291279
9. Afilalo J, et al. FRAILTY-AVR. [JACC 2017;70:689.](https://doi.org/10.1016/j.jacc.2017.06.024) PMID 28693934
10. Fumagalli C, et al. GASS-TAVR. [JACC Cardiovasc Interv 2026;19:813.](https://doi.org/10.1016/j.jcin.2025.12.018) PMID 41986031
11. Katz S, et al. The Index of ADL. [JAMA 1963;185:914.](https://pubmed.ncbi.nlm.nih.gov/14044222/)
12. Lawton MP, Brody EM. Self-maintaining and instrumental ADL. [Gerontologist 1969;9:179.](https://pubmed.ncbi.nlm.nih.gov/5349366/)
13. Besler C, et al. Nutritional status in TR: implications of transcatheter repair. [Eur J Heart Fail 2020;22:1826.](https://doi.org/10.1002/ejhf.1752) PMID 32100930
14. Scotti A, et al. Malnutrition in HF and SMR: COAPT. [JACC 2023;82:128.](https://doi.org/10.1016/j.jacc.2023.04.047) PMID 37306651
15. Pagnesi M, et al. Malnutrition and outcomes in T-TEER (EuroTR). [Eur J Heart Fail 2025;27:1304.](https://doi.org/10.1002/ejhf.3623) PMID 39980251
16. Guigoz Y, Vellas B, Garry PJ. MNA as part of the geriatric evaluation. [Nutr Rev 1996;54:S59.](https://pubmed.ncbi.nlm.nih.gov/8919685/) ※原始版：Facts Res Gerontol 1994;4(Suppl 2):15-59（非 PubMed）
17. Vellas B, et al. The MNA and its use in grading the nutritional state of elderly patients. [Nutrition 1999;15:116.](https://doi.org/10.1016/s0899-9007(98)00171-3) PMID 9990575
18. Rubenstein LZ, et al. Developing the MNA-SF. [J Gerontol A 2001;56:M366.](https://doi.org/10.1093/gerona/56.6.m366) PMID 11382797

---

<!-- _class: ref -->
# 參考文獻 (2/3)

19. Kaiser MJ, et al. Validation of the MNA-SF. [J Nutr Health Aging 2009;13:782.](https://doi.org/10.1007/s12603-009-0214-7) PMID 19812868
20. Kaiser MJ, et al. Frequency of malnutrition in older adults: multinational MNA. [JAGS 2010;58:1734.](https://doi.org/10.1111/j.1532-5415.2010.03016.x) PMID 20863332
21. Guigoz Y. The MNA review of the literature. [J Nutr Health Aging 2006;10:466.](https://pubmed.ncbi.nlm.nih.gov/17183419/)
22. Bouillanne O, et al. Geriatric Nutritional Risk Index. [Am J Clin Nutr 2005;82:777.](https://doi.org/10.1093/ajcn/82.4.777) PMID 16210706
23. Shibata K, et al. Early nutritional reversibility after M-TEER (OCEAN-Mitral). [JACC Adv 2025;4:102142.](https://doi.org/10.1016/j.jacadv.2025.102142) PMID 40967169
24. Goldfarb M, et al. Malnutrition and mortality in AVR (FRAILTY-AVR). [Circulation 2018;138:2202.](https://doi.org/10.1161/CIRCULATIONAHA.118.033887) PMID 29976568
25. Spertus JA, et al. Interpreting the KCCQ: JACC State-of-the-Art. [JACC 2020;76:2379.](https://doi.org/10.1016/j.jacc.2020.09.542) PMID 33183512
26. Green CP, Porter CB, Bresnahan DR, Spertus JA. Development and evaluation of the KCCQ. [JACC 2000;35:1245.](https://doi.org/10.1016/s0735-1097(00)00531-3) PMID 10758967
27. Spertus J, et al. Monitoring clinical changes in HF: a comparison of methods. [Am Heart J 2005;150:707.](https://doi.org/10.1016/j.ahj.2004.12.010) PMID 16209970
28. Arnold SV, et al. KCCQ in aortic stenosis (PARTNER). [Circ Heart Fail 2013;6:61.](https://doi.org/10.1161/CIRCHEARTFAILURE.112.970053) PMID 23230306
29. Spertus JA, Jones PG. KCCQ-12. [Circ Cardiovasc Qual Outcomes 2015;8:469.](https://doi.org/10.1161/CIRCOUTCOMES.115.001958) PMID 26307129
30. Arnold SV, et al. Health status after TMVr: COAPT. [JACC 2019;73:2123.](https://doi.org/10.1016/j.jacc.2019.02.010) PMID 30894288
31. Song C, et al. Age-related outcomes after TMVr: COAPT. [JACC Cardiovasc Interv 2022;15:397.](https://doi.org/10.1016/j.jcin.2021.11.037) PMID 35093278
32. Arnold SV, et al. Health status vs functional status in HF and SMR. [JACC Heart Fail 2021;9:684.](https://doi.org/10.1016/j.jchf.2021.04.012) PMID 34391740
33. Sorajja P, et al. TRILUMINATE Pivotal. [N Engl J Med 2023;388:1833.](https://doi.org/10.1056/NEJMoa2300525) PMID 36876753
34. Arnold SV, et al. Health status after T-TEER (TRILUMINATE). [JACC 2024;83:1.](https://doi.org/10.1016/j.jacc.2023.10.008) PMID 37898329
35. Kar S, et al. TRILUMINATE 2-year outcomes. [Circulation 2025;151:1630.](https://doi.org/10.1161/CIRCULATIONAHA.125.074536) PMID 40159089
36. Elzeneini M, et al. Dementia and outcomes after M-TEER. [Cardiovasc Revasc Med 2024;66:1.](https://doi.org/10.1016/j.carrev.2024.03.031) PMID 38604834

---

<!-- _class: ref -->
# 參考文獻 (3/3)

37. Nikendei C, et al. Mitral valve repair and memory / executive function. [Psychosom Med 2016;78:432.](https://doi.org/10.1097/PSY.0000000000000284) PMID 26705072
38. Terhoeven V, et al. MitraClip and cognitive function: the sicker the better. [Eur J Med Res 2019;24:14.](https://doi.org/10.1186/s40001-019-0371-z) PMID 30791961
39. Blazek S, et al. Cerebral embolic lesions after MitraClip. [EuroIntervention 2015;10:1195.](https://doi.org/10.4244/EIJY14M05_10) PMID 24831647
40. Braemswig TB, et al. New cerebral microbleeds after structural heart interventions. [J Am Heart Assoc 2023;12:e027284.](https://doi.org/10.1161/JAHA.122.027284) PMID 36734351
41. Folstein MF, et al. "Mini-mental state". [J Psychiatr Res 1975;12:189.](https://doi.org/10.1016/0022-3956(75)90026-6) PMID 1202204
42. Borson S, et al. The Mini-Cog. [Int J Geriatr Psychiatry 2000;15:1021.](https://pubmed.ncbi.nlm.nih.gov/11113982/) PMID 11113982
43. Nasreddine ZS, et al. The MoCA. [JAGS 2005;53:695.](https://doi.org/10.1111/j.1532-5415.2005.53221.x) PMID 15817019
44. Fried LP, et al. Frailty in older adults: evidence for a phenotype. [J Gerontol A 2001;56:M146.](https://doi.org/10.1093/gerona/56.3.m146) PMID 11253156
45. Rockwood K, et al. Clinical Frailty Scale. [CMAJ 2005;173:489.](https://doi.org/10.1503/cmaj.050051) PMID 16129869
46. Metze C, et al. Impact of frailty on outcomes in PMVR. [JACC Cardiovasc Interv 2017;10:1920.](https://doi.org/10.1016/j.jcin.2017.07.042) PMID 28917516
47. Arnold SV. Frail Elderly, the Ideal Patients for MitraClip. [JACC Cardiovasc Interv 2017;10:1930.](https://doi.org/10.1016/j.jcin.2017.08.029) PMID 28917513
48. Kundi H, et al. Frailty in transcatheter valve therapies: nationwide cohort. [Eur Heart J 2019;40:2231.](https://doi.org/10.1093/eurheartj/ehz187) PMID 30977798
49. Rios S, et al. Frailty and M-TEER outcomes (NIS). [Am J Cardiol 2022;179:58.](https://doi.org/10.1016/j.amjcard.2022.06.019) PMID 35870989
50. Metze C, et al. A simplified frailty measure in PMVR. [J Cachexia Sarcopenia Muscle 2025;16:e70138.](https://doi.org/10.1002/jcsm.70138) PMID 41327510
51. Thangavelu V, et al. Preoperative frailty in major cardiac procedures: meta-analysis. [Anesth Analg 2025.](https://doi.org/10.1213/ANE.0000000000007887) PMID 41442636
52. Kundi H, et al. Trends and late outcomes in elderly mitral interventions. [JACC Cardiovasc Interv 2025;18:2241.](https://doi.org/10.1016/j.jcin.2025.06.041) PMID 40992805
53. Rawish E, et al. Audiovisual distraction during M-TEER: sedation-sparing RCT. [JACC Adv 2026;5:102835.](https://doi.org/10.1016/j.jacadv.2026.102835) PMID 42167101

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
本文件僅供醫療專業人員教學參考
