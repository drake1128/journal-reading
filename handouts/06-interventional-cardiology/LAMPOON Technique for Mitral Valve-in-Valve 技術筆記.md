# LAMPOON Technique for Mitral Valve-in-Valve (MViV) — 技術筆記

**整理：謝慕揚 MD, PhD, FESC**
**最後更新：2026-04-23**
**用途：個人實作參考；本院 MViV 合併 LAMPOON 流程備忘**

> **LAMPOON** = **L**aceration of the **A**nterior **M**itral leaflet to **P**revent **O**utflow **Ob**structio**N**
> 為 BASILICA 的姊妹技術，由 NIH / Emory / MedStar 團隊 (Khan, Lederman, Babaliaros, Greenbaum, Lisko) 發展，使用 **高頻電燒 (electrosurgery)** 將前葉 (anterior mitral leaflet, AML) 從中線劈開，於 TMVR 前預防 neo-LVOT 阻塞

---

## 目錄

1. [今日案例重點（快速參考）](#今日案例重點快速參考)
2. [LAMPOON 技術演進概覽](#lampoon-技術演進概覽)
3. [Antegrade Transseptal LAMPOON — 詳細步驟](#antegrade-transseptal-lampoon--詳細步驟)
4. [Tip-to-Base LAMPOON — ViV/ViR 專用變體](#tip-to-base-lampoon--vivvir-專用變體)
5. [Rendezvous Technique (Taiwan / Cheng Hsin) — 2024 改良版](#rendezvous-technique-taiwan--cheng-hsin--2024-改良版)
6. [關鍵器材與耗材清單](#關鍵器材與耗材清單)
7. [電燒設定 (Bovie / Electrosurgical Settings)](#電燒設定-bovie--electrosurgical-settings)
8. [Pitfalls 與避開方法](#pitfalls-與避開方法)
9. [影像確認與監測](#影像確認與監測)
10. [關鍵文獻](#關鍵文獻)

---

## 今日案例重點（快速參考）

**Setup**：Mitral ViV，採 **Antegrade Transseptal 路徑** 搭配 **AV loop**。

### 關鍵器材配置（今日做法）

| 步驟 | 路徑 | 器材 | 功能 |
|------|------|------|------|
| 1. Transseptal | RA → LA | 單次 TSP + **Agilis steerable sheath** | 提供 LA 操作的穩定平台 |
| 2. 建立 AV loop | LA → LV → Aorta | **Terumo (Glidewire) via Agilis** | 過心室到主動脈 |
| 3. Snare 拉出體外 | Aorta → 體外 | Snare（股動脈） | 創造 through-and-through AV 迴路 |
| 4. **動脈端 insulating catheter** | Aorta → LV | **MP 7F** (arterial) | 保護主動脈、絕緣拉絲 |
| 5. **靜脈端 delivery catheter** | IAS → LA → LV → AV/Aorta | **JR 5F** (transseptal) | 靜脈側遞送 Astato wire 到前葉 |
| 6. 劈裂 leaflet 的 wire | JR 5F → 穿過前葉 | **Asahi Astato 20** hydrophilic stiff wire | 本案首選 cheesewire |

> **Pearl (今日)**：先建立 AV loop（Terumo），再換 Astato wire 進行 leaflet 電燒切斷。**MP 7F 在動脈端 + JR 5F 在靜脈端** 的雙 catheter 平台是 antegrade LAMPOON 的標準配置。

---

## LAMPOON 技術演進概覽

| 年代 | 變體 | 代表論文 | 主要應用 |
|------|------|---------|---------|
| 2017–2019 | **Classic Retrograde (base-to-tip)** | [Khan JM *JACC* 2019](https://doi.org/10.1016/j.jacc.2019.02.076) | NHLBI LAMPOON trial (n=30)；ViR + ViMAC |
| 2020 | **Antegrade Transseptal** | [Lisko JC *Circ CV Interv* 2020](https://doi.org/10.1161/CIRCINTERVENTIONS.119.008903) | 簡化流程（procedure 時間 39 vs 65 min）；**推薦為新標準** |
| 2021 | **Tip-to-Base (for protected annulus)** | [Lisko JC *JACC CVI* 2021](https://doi.org/10.1016/j.jcin.2020.11.034) | ViV / ViR 中年環被 prosthesis 保護；21 例成功率 100% |
| 2021 | **Tip-to-Base for ViV** | [Ben-Dor I *Innovations* 2021](https://doi.org/10.1177/15569845211048899) | Failing mitral bioprosthesis |
| 2022 | **First for Surgical MV Bioprosthesis (真正 ViV)** | [Kamioka N *CRVM* 2023](https://doi.org/10.1016/j.carrev.2022.04.023) | 首例 LAMPOON + mitral ViV 在外科生物瓣 |
| 2024 | **Modified Tip-to-Base + Rendezvous (Taiwan)** | [Lin HC *Acta Cardiol Sin* 2024](https://doi.org/10.6515/ACS.202405_40(3).20240129A) | **13 例 ViV/ViR 全部成功**；RT 3D-TEE 指引 |
| 2024 | **5-Year Outcomes** | [Khan JM *JACC CVI* 2024](https://doi.org/10.1016/j.jcin.2024.05.041) | 5-yr 存活率 25%；LAMPOON 本身無長期併發症 |
| 2026 | **APAC Electrosurgery Review** | [Wong CK *JACC Asia* 2026](https://doi.org/10.1016/j.jacasi.2025.10.025) | 亞太區 electrosurgery 應用全貌 |

---

## Antegrade Transseptal LAMPOON — 詳細步驟

> **基於 Lisko JC et al. (Circ CV Interv 2020, PMID 32513014)**：在 8 例 fixed LVOT obstruction 高風險病人 100% 成功，procedure time 比 retrograde 縮短 26 min，且建議為新標準。

### 前置準備

1. **預先 CT 評估**
   - 量測 **neo-LVOT area**（phase-specific thresholds：早期收縮期 260、peak flow 210、mid-systole 200、end-systole 180 mm²；Kohli et al. *EHJ CVI* 2022）
   - 量測 **skirt neo-LVOT area**（更精確）
   - 評估 **aorto-mitral angle**、**AML 長度**、**basal septum 肥厚**
   - 對於 ViV：確認前瓣葉（先前外科瓣）的 **leaflet length + commissures 位置**
2. **腦部保護**：建議使用 **SENTINEL cerebral embolic protection (CEP)**（Lin 2024 中 85% 病例使用，且 LAMPOON 後 TMVR 栓塞負擔不低）
3. **麻醉與影像**：全身麻醉、**RT 3D-TEE**、透視 + rotational angiography

### 步驟流程（Antegrade LAMPOON）

```text
┌─────────────────────────────────────────────────────┐
│  Step 1: Vascular Access                             │
│  · R femoral vein (14F, TMVR delivery) + 工作 7F    │
│  · R femoral artery (7-8F, insulating MP 7F)        │
│  · L femoral artery (pigtail + CEP 6F)              │
└─────────────────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 2: Transseptal Puncture (TSP)                  │
│  · Mid-posterior IAS，距 MV 約 4-4.5 cm             │
│  · Agilis steerable sheath 進 LA                    │
│  · **兩個獨立通道**：一為 AV loop、一為 leaflet 穿刺 │
└─────────────────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 3: Build Arteriovenous (AV) Loop               │
│  · Agilis 內放 support catheter (MP/AL)              │
│  · **Terumo hydrophilic wire** 越過 MV → LV → Ao    │
│  · 股動脈 snare 拉出 Terumo → **AV loop 建立**      │
│  · AV loop 提供 leaflet 穿刺的軌道與拉力             │
└─────────────────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 4: Position the Two Insulating/Delivery Caths  │
│  · 動脈側：MP 7F 沿 Ao → LV                         │
│    → 覆蓋 wire 在升主動脈的裸露段，絕緣保護         │
│  · 靜脈側：JR 5F 從 IAS → LA → 跨 MV → 準備穿葉    │
│    → JR 5F 導引 Astato wire 指向 AML 中線 (A2)      │
└─────────────────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 5: Leaflet Traversal                          │
│  · 將 Terumo 換成 **Asahi Astato 20 (0.014")**     │
│  · JR 5F 指向 AML 中心（A2），在 RT 3D-TEE 下確認   │
│  · Astato wire **遠端塑形如 "flying V"**（預留切割段）│
│  · **開啟 Bovie** → Astato 前端以 pure-cut mode    │
│    通過 AML 從 atrial → ventricular side            │
│  · 使用 3D-TEE **確認穿葉點在 leaflet 中線 (A2)**  │
└─────────────────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 6: Snare Wire in LV/Ao, Complete Loop         │
│  · Astato 穿葉後進 LV → 過 AV → 到升主動脈           │
│  · MP 7F (arterial) 前端 snare 抓取 Astato          │
│  · 拉出體外 → **Astato 完成 through-and-through**  │
│  · Confirm MP 7F **完全覆蓋 Ao 段** 避免誤燒主動脈   │
└─────────────────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 7: Electrosurgical Laceration                 │
│  · **Cheesewire technique**：雙端張力拉緊 Astato    │
│  · 電燒模式：**Pure Cut 70-80 W**（連續 mode）       │
│  · 確認 5% dextrose 於周邊腔內（降低電阻不均）       │
│  · 同步雙手拉緊 → Astato 裸段以電流劈開 AML       │
│  · 數秒內完成；RT 3D-TEE 可見 AML 被切開成兩半     │
└─────────────────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 8: Confirm + Proceed to TMVR (SAPIEN 3)       │
│  · 3D-TEE 確認 AML 已切開；無 acute MR 惡化          │
│  · 移除 Astato、MP 7F                                │
│  · 沿 Terumo (AV loop 未拆) 植入 SAPIEN 3 TMVR      │
│  · 最終確認：neo-LVOT gradient < 30 mmHg、無 PVL    │
└─────────────────────────────────────────────────────┘
```

---

## Tip-to-Base LAMPOON — ViV/ViR 專用變體

> **核心觀念**：當 mitral annulus 被 prosthesis (surgical valve 或 annuloplasty ring) 保護時，只需切斷 **瓣葉游離段**，從 tip 往 base 方向電燒，避免觸及主動脈根部。

### 為什麼 ViV 特別適合 tip-to-base？

- Base-to-tip 傳統方式需穿過 **aorto-mitral curtain**，ViV 中該區域已被 prosthesis 覆蓋 → 穿葉困難且可能傷及周邊組織
- Tip-to-base 從 **leaflet 游離緣 (tip)** 穿入，保留 prosthesis 作為 **天然絕緣層**
- 更短的 procedure time（平均節省 20–30 min）
- 避免主動脈根部損傷（Lisko 2021 中 2/21 例因 supra-annular ring 導致 AV 損傷，是主要 caveat）

### Tip-to-Base 技術差異

1. **從 LV 側** 開始穿葉：MP 7F 從 Ao 進入 LV，朝 MV 游離緣
2. **從 tip 側 insert Astato**：Astato 從 LV 朝 leaflet 游離緣 → 穿入 atrial 側
3. **Snare in LA**：經 Agilis 端 snare 拉出
4. **Insulating**：以 aortic MP catheter 絕緣 Ao 段
5. **Cheesewire 方向**：從 tip → base，在 prosthesis 內緣停住
6. **3D-TEE 必備**：確認游離緣穿刺點、避免傷及瓣下器具

---

## Rendezvous Technique (Taiwan / Cheng Hsin 振興醫院) — 2024 改良版

> **Lin HC, Lee YT, Tsao TP, Lee KC, Hsiung MC, Yin WH, Wei J.**
> A Modified Tip-to-Base LAMPOON to Prevent LVOTO in ViR or ViV TMVR.
> [*Acta Cardiol Sin*. 2024;40(3):331-339. PMID: 38779166](https://pubmed.ncbi.nlm.nih.gov/38779166/)
> [DOI: 10.6515/ACS.202405_40(3).20240129A](https://doi.org/10.6515/ACS.202405_40(3).20240129A) | [PMC Free Full Text](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11106618/)
>
> **Affiliation**：Heart Center, Cheng Hsin General Hospital (振興醫院心臟中心)
> Taipei, Taiwan（No. 45, Cheng Hsin St., Beitou Dist.）
> **Corresponding author**：Dr. Wei-Hsian Yin (殷偉賢 醫師)
> **CoI disclosure**：本研究為 **亞太地區 ViV/ViR LAMPOON 最重要技術文獻之一**；技術已被 **2026 APAC Electrosurgery Working Group Review（Wong CK et al. JACC Asia 2026）** 正式引用為區域標準。

### 🏆 振興醫院 Cheng Hsin Series 核心數據

| 項目 | 結果 |
|------|:----:|
| **收案期間** | 單一中心連續病例 |
| **病人數** | **13 位**（ViV + ViR） |
| **女性** | 6 人（46%） |
| **平均年齡** | 67.7 歲 |
| **平均 LVEF** | 60% |
| **STS Score 中位數** | 3.2% |
| **介入瓣膜** | SAPIEN 3 (Edwards Lifesciences) |
| **手術路徑** | 單次 Transseptal，**preventive LAMPOON + TMVR 同時完成** |
| **影像引導** | RT 3D-TEE 全程 |
| **技術成功率** | **13/13 = 100%** |
| **LAMPOON 路徑** | **Tip-to-Base** |
| **SENTINEL 腦部保護使用** | **11/13 (85%)** |
| **SENTINEL 捕獲 debris ≥2 mm** | **8/11 (73%) 🩸** |
| **非計畫性主動脈 / AV 損傷** | **0 例** |
| **顯著 LVOTO (術後)** | **0 例** |
| **手術時間** | 較 retrograde 顯著縮短 |
| **透視時間** | 較傳統技術減少 |

### 什麼是 Rendezvous 技術？

**核心概念**：雙側 wire 在 **LV 腔內會合對接**，不需將穿葉 wire 再推進主動脈 snare，縮短流程並避免主動脈刺激。

1. **雙側 wire 在 LV 內會合 (rendezvous)**：
   - 動脈側 MP 推進到 LV，預置 snare
   - 靜脈側 JR 經 IAS → LA → 穿葉 → Astato wire 深入 LV
   - 兩條 wire **在 LV 中央直接相遇** —「一手交錢、一手交貨」
2. **RT 3D-TEE 即時引導 wire 對齊**（振興團隊核心創新）
3. **優點**：
   - 縮短 fluoroscopy 時間
   - 減少主動脈刺激 / 損傷風險
   - 提高 alignment 成功率
   - 對 **亞洲人 anatomy（annulus 較小、LVOT 狹窄）** 特別有利

### 技術細節（Lin 2024）

| 步驟 | 動脈側 (Retrograde limb) | 靜脈側 (Antegrade limb) |
|------|--------------------------|-------------------------|
| 1. Access | 股動脈 7F | 股靜脈 + TSP |
| 2. Guide | **MP 或 AL catheter → 過 AV 到 LV** | **Agilis → LA → JR 5F → 跨 MV** |
| 3. Wire | Snare (GooseNeck) 預置於 LV | **Asahi Astato 20** via JR，穿過 AML |
| 4. Rendezvous 位置 | LV mid-cavity | LV mid-cavity |
| 5. 影像引導 | **RT 3D-TEE en face view of AML** | 同 |
| 6. Wire 對接 | MP 端 snare 抓 Astato | — |
| 7. 外拉 | 拉出股動脈端 | — |
| 8. Cheesewire | 電燒 Pure Cut 70-80 W | — |

### 為什麼 Tip-to-Base + Rendezvous 是 ViV 的最佳解？

- **Tip-to-base**：避開 aorto-mitral curtain（已被外科瓣環覆蓋）
- **Rendezvous**：雙側 wire 在 LV 對接，不需進主動脈 snare
- **3D-TEE 引導**：精準定位 AML 中心 (A2)，避開 commissure
- **SENTINEL 同步**：保護腦部（7 成以上會捕捉到 ≥2 mm debris！）

### 🇹🇼 本院（本次）做法與 Lin 2024 Rendezvous 的對照

| 器材 / 步驟 | Lin 2024 振興 | 本院今日 | 一致性 |
|-------------|:-------------:|:--------:|:------:|
| TSP + Agilis | ✅ | ✅ | 完全一致 |
| **MP 7F (動脈端)** | ✅ | ✅ | 完全一致 |
| **JR 5F (靜脈端)** | ✅ | ✅ | 完全一致 |
| **Asahi Astato 20** | ✅ | ✅ | 完全一致 |
| Terumo Glidewire 建立 AV loop | ✅ | ✅ | 完全一致 |
| RT 3D-TEE 引導 | ✅ | ✅（若有） | 建議標配 |
| Tip-to-Base 方向 | ✅ | ✅ | 完全一致 |
| SENTINEL CEP | 85% | 建議納入 | 強烈建議 |
| SAPIEN 3 TMVR | ✅ | ✅ | 完全一致 |

> **結論**：本院今日 MViV + LAMPOON 流程 **完全符合 Cheng Hsin 2024 Series 的 Rendezvous Tip-to-Base 標準**。這是目前亞太地區 ViV/ViR LAMPOON 的 **reference procedure**。

---

## 關鍵器材與耗材清單

### 穿刺與 Access
| 器材 | 規格 | 部位 |
|------|------|------|
| TSP needle | BRK-1 / NRG RF needle | 股靜脈 |
| Steerable sheath | **Agilis NxT (St. Jude / Abbott)** | 股靜脈 → LA |
| TMVR delivery sheath | Edwards 14F eSheath | 股靜脈 |

### AV Loop 與 Leaflet 穿刺
| 器材 | 規格 | 備註 |
|------|------|------|
| Hydrophilic J-wire | **Terumo Glidewire** 260 cm | AV loop 建立 |
| Leaflet laceration wire | **Asahi Astato 20** 0.014" | 本院首選；遠端預留 **裸露段 6–8 cm** 供電燒 |
| Alternative wire | 0.014" Piggyback wire (Vascular Solutions) | 備選 |
| Snare | **Amplatz GooseNeck 20–30 mm** | 股動脈 snare 拉 wire |

### Insulating / Delivery Catheters
| 器材 | 規格 | 路徑 |
|------|------|------|
| **MP 7F** (arterial) | 多用途 MP guiding | Ao → LV；**絕緣升主動脈段** |
| **JR 5F** (venous/transseptal) | JR 4.0 diagnostic | IAS → LA → 跨 MV → 指向 Ao 側 |
| Backup: AL 1/2 | — | 若 JR 不易對準 |

### 其他
| 器材 | 備註 |
|------|------|
| **Bovie ESU (Electrosurgical Unit)** | ForceFX / Valleylab 等 |
| **5% Dextrose in Water (D5W)** | 降低局部電阻，**必要！** 非生理食鹽水 |
| **Cerebral embolic protection** | SENTINEL（強烈建議） |
| **3D-TEE 機台** | Philips EPIQ 或同級 |

---

## 電燒設定 (Bovie / Electrosurgical Settings)

| 步驟 | Mode | Power | 持續時間 |
|------|------|:-----:|:--------:|
| **Leaflet traversal** (穿葉) | **Pure Cut** | **70 W** | Pulsed 1–2 sec bursts |
| **Cheesewire laceration** | **Pure Cut (continuous)** | **70–80 W** | 持續直到 wire 切斷 leaflet（通常 2–5 sec） |

> **關鍵**：
> - **必須使用 D5W** 沖洗 wire 裸露段；生理食鹽水導電過快會不均勻切割
> - **雙手同步拉張**：wire 需保持張力；鬆弛時電流集中於一點易燒穿結構
> - **Coagulation mode 禁用**：只能用 Pure Cut；coag 會造成 tissue charring 而非清潔切割

---

## Pitfalls 與避開方法

| Pitfall | 機轉 | 預防 / 處理 |
|--------|------|------------|
| **主動脈瓣 / 根部損傷** | MP 7F 絕緣不足；wire 裸段外露於 Ao | **confirm MP catheter fully covers wire in Ao**；tip-to-base 改用較無此風險 |
| **穿葉位置偏離中線** | 未在 A2 中央穿 → 切開不對稱 | **3D-TEE en face view** 確認；Rendezvous 技術幫助對齊 |
| **LVOT 仍阻塞** | skirt neo-LVOT < 180 mm² 的病人仍可能 residual obstruction | CT phase-specific thresholds (Kohli 2022)；考慮 BATMAN 或 alcohol septal ablation |
| **Paravalvular leak (PVL)** | SAPIEN 3 在非圓形 annulus 中 | **LAMPOON IDE trial** 中 10% 額外處置 PVL；影響長期預後 |
| **Wire perforation / 心室穿刺** | Astato stiff wire 前端過深 | 前端塑形，避免過度前推；透視監測 LV 輪廓 |
| **Lacerate 失敗** | 電流不足或 wire 鬆弛 | 重新塑形 wire 裸段；增加張力；確認 grounding pad 接觸良好 |
| **AML 斷端捲曲阻塞** | Leaflet 被切成 2 片但重疊 | SAPIEN 3 植入後 **flaps 貼附新瓣** 一般可解決 |
| **Stroke** | 拉絲過程 debris 栓塞 | **SENTINEL CEP** 強烈建議 (Lin 2024 中 85% 使用) |

---

## 影像確認與監測

### Pre-procedure CT (必做)
- Neo-LVOT area（systolic 各 phase）
- Skirt neo-LVOT area（更精確預測 obstruction 風險）
- Aorto-mitral angle
- AML length & prosthesis sewing ring position
- Septal thickness

### Intra-procedure
- **RT 3D-TEE** 全程：
  - Transseptal 位置（mid-posterior）
  - AV loop wire 路徑
  - Leaflet traversal 位置 (en face A2)
  - Post-LAMPOON：確認 AML 切開
  - TMVR deployment & PVL 評估
- **Fluoro**：rotational angiography confirm LVOT

### Post-procedure
- **Immediate**：LVOT gradient（Doppler TEE）、MR、PVL
- **Discharge TTE**：LVOT gradient < 30 mmHg = optimal；< 50 mmHg = acceptable
- **Post-op CT (1 mo)**：neo-LVOT geometry、skirt LVOT flow area

---

## 長期預後（NHLBI LAMPOON Trial 5-yr）

> **Khan JM et al. JACC CVI 2024 (PMID 39243268)**

| 時間 | 存活率 | 備註 |
|------|:------:|------|
| 30 天 | 97% | LAMPOON 成功率 100% |
| 1 年 | 65% | 6 min walk +60 m；KCCQ +24 |
| 5 年 | 25% | 反映原發病嚴重度而非 LAMPOON |

> **結論**：LAMPOON **本身無長期併發症**；長期存活受原始 inoperable status 主導。

---

## 關鍵文獻

### 原始技術 & 試驗
1. Khan JM, Babaliaros VC, Greenbaum AB, et al. Anterior Leaflet Laceration to Prevent Ventricular Outflow Tract Obstruction During Transcatheter Mitral Valve Replacement (**NHLBI LAMPOON trial**). [*J Am Coll Cardiol*. 2019;73(20):2521-2534.](https://pubmed.ncbi.nlm.nih.gov/31118146/) [DOI: 10.1016/j.jacc.2019.02.076](https://doi.org/10.1016/j.jacc.2019.02.076)

2. Lisko JC, Greenbaum AB, Khan JM, et al. **Antegrade** Intentional Laceration of the Anterior Mitral Leaflet to Prevent LVOT Obstruction: A Simplified Technique. [*Circ Cardiovasc Interv*. 2020;13(6):e008903.](https://pubmed.ncbi.nlm.nih.gov/32513014/) [DOI: 10.1161/CIRCINTERVENTIONS.119.008903](https://doi.org/10.1161/CIRCINTERVENTIONS.119.008903)

3. Lisko JC, Babaliaros VC, Khan JM, et al. **Tip-to-Base LAMPOON** for Transcatheter Mitral Valve Replacement With a Protected Mitral Annulus. [*JACC Cardiovasc Interv*. 2021;14(5):541-550.](https://pubmed.ncbi.nlm.nih.gov/33663781/) [DOI: 10.1016/j.jcin.2020.11.034](https://doi.org/10.1016/j.jcin.2020.11.034)

4. Khan JM, Babaliaros VC, Greenbaum AB, et al. **5-Year Outcomes** of Anterior Mitral Leaflet Laceration to Prevent Outflow Obstruction. [*JACC Cardiovasc Interv*. 2024;17(18):2084-2096.](https://pubmed.ncbi.nlm.nih.gov/39243268/) [DOI: 10.1016/j.jcin.2024.05.041](https://doi.org/10.1016/j.jcin.2024.05.041)

### ViV 專用變體
5. Ben-Dor I, Weissman G, Case BC, et al. **Valve-in-Valve for Failing Mitral Bioprosthesis With Tip-to-Base LAMPOON** to Prevent LVOT Obstruction. [*Innovations (Phila)*. 2021;16(6):558-561.](https://pubmed.ncbi.nlm.nih.gov/34636690/) [DOI: 10.1177/15569845211048899](https://doi.org/10.1177/15569845211048899)

6. Kamioka N, Greenbaum AB, Lederman RJ, et al. **First Application of LAMPOON to a Surgical Mitral Bioprosthesis** (first true MViV LAMPOON). [*Cardiovasc Revasc Med*. 2023;53S:S299-S302.](https://pubmed.ncbi.nlm.nih.gov/35879191/) [DOI: 10.1016/j.carrev.2022.04.023](https://doi.org/10.1016/j.carrev.2022.04.023)

7. Lin HC, Lee YT, Tsao TP, et al. **A Modified Tip-to-Base LAMPOON with Rendezvous Technique** (Taiwan, Cheng Hsin, 13 ViV/ViR cases). [*Acta Cardiol Sin*. 2024;40(3):301-310.](https://pubmed.ncbi.nlm.nih.gov/38779166/) [DOI: 10.6515/ACS.202405_40(3).20240129A](https://doi.org/10.6515/ACS.202405_40(3).20240129A)

### 回顧與影像
8. Case BC, Lisko JC, Babaliaros VC, et al. LAMPOON techniques to prevent or manage LVOT obstruction in TMVR (**Review of all variants**). [*Ann Cardiothorac Surg*. 2021;10(1):115-122.](https://pubmed.ncbi.nlm.nih.gov/33575191/) [DOI: 10.21037/acs-2020-mv-25](https://doi.org/10.21037/acs-2020-mv-25)

9. Khan JM, Rogers T, Greenbaum AB, et al. Use of Electrosurgery in Interventional Cardiology (**BASILICA / LAMPOON / ELASTA-Clip overview**). [*Interv Cardiol Clin*. 2022;11(3):269-280.](https://pubmed.ncbi.nlm.nih.gov/35710281/) [DOI: 10.1016/j.iccl.2022.01.004](https://doi.org/10.1016/j.iccl.2022.01.004)

10. Kohli K, Wei ZA, Sadri V, et al. Dynamic nature of the LVOT following TMVR with LAMPOON: new insights from post-procedure imaging. [*Eur Heart J Cardiovasc Imaging*. 2022;23(5):650-662.](https://pubmed.ncbi.nlm.nih.gov/34009283/) [DOI: 10.1093/ehjci/jeab074](https://doi.org/10.1093/ehjci/jeab074)

11. Kohli K, Wei ZA, Sadri V, et al. Assessing the Hemodynamic Impact of Anterior Leaflet Laceration in TMVR: CFD analysis. [*Front Cardiovasc Med*. 2022;9:869259.](https://pubmed.ncbi.nlm.nih.gov/35811698/) [DOI: 10.3389/fcvm.2022.869259](https://doi.org/10.3389/fcvm.2022.869259)

### TMVR ViV 整體預後
12. Eng MH, Kargoli F, Wang DD, et al. Short- and mid-term outcomes in percutaneous TMVR using balloon-expandable valves (MViV/MViR/ViMAC). [*Catheter Cardiovasc Interv*. 2021;98(6):E868-E876.](https://pubmed.ncbi.nlm.nih.gov/34106514/) [DOI: 10.1002/ccd.29783](https://doi.org/10.1002/ccd.29783)

13. Onishi T, El-Eshmawi A, Lerakis S, et al. Transcatheter mitral valve options for severe mitral annular calcification (LAMPOON + BATMAN + TMVI review). [*Ann Cardiothorac Surg*. 2025;14(6):437-451.](https://pubmed.ncbi.nlm.nih.gov/41383202/) [DOI: 10.21037/acs-2025-mac-11](https://doi.org/10.21037/acs-2025-mac-11)

### 亞太區
14. Wong CK, Poon K, So KC, et al. **Transcatheter Electrosurgery in the Asia-Pacific**: Implementation and Innovations (APAC Electrosurgery Working Group). [*JACC Asia*. 2026;6(1):1-16.](https://pubmed.ncbi.nlm.nih.gov/41498463/) [DOI: 10.1016/j.jacasi.2025.10.025](https://doi.org/10.1016/j.jacasi.2025.10.025)

---

## 本院未來 MViV + LAMPOON 執行 Checklist

### Pre-procedure
- [ ] CT 顯示 neo-LVOT 高風險（area < 200 mm² at peak flow）
- [ ] Heart team 確認 inoperable / extremely high surgical risk
- [ ] Pre-order：Agilis、Astato 20、Terumo、MP 7F、JR 5F、Amplatz GooseNeck snare、D5W、Bovie ESU、SENTINEL CEP
- [ ] Anesthesia：GA、arterial line、central line、temp pacing wire

### Intra-procedure
- [ ] 雙側股動靜脈 access (R vein 14F + 7F；R/L artery 7F + 6F CEP)
- [ ] SENTINEL CEP deploy（procedure 開始前）
- [ ] TSP mid-posterior → Agilis 進 LA
- [ ] Build AV loop: Agilis → Terumo → LV → Ao → snare 拉出
- [ ] 動脈端 MP 7F 進 Ao → LV（insulator）
- [ ] 靜脈端 JR 5F 進 LA → 跨 MV → 指向 AML 中心 (A2)
- [ ] 換 Terumo 為 **Astato 20**（裸段塑 "flying V" 6-8 cm）
- [ ] 3D-TEE 確認 Astato 穿葉在 A2 中線
- [ ] Bovie Pure Cut 70 W → Astato 穿葉 → snare in LV or Ao
- [ ] Confirm MP 7F 完全 cover wire in Ao
- [ ] Bovie Pure Cut 70-80 W continuous → cheesewire laceration
- [ ] 3D-TEE confirm AML 切開
- [ ] Remove Astato + MP；保留 AV loop 準備 TMVR
- [ ] SAPIEN 3 TMVR transseptal 植入
- [ ] Final TEE：LVOT gradient < 30 mmHg、MR absent/trace、PVL 評估

### Post-procedure
- [ ] TTE 24h、30-day、6-mo、1-yr
- [ ] CT 1-mo 確認 neo-LVOT geometry
- [ ] 抗凝/抗血小板依 TMVR ViV protocol

---

*本文件基於 2020–2024 LAMPOON 文獻回顧與本院 2026-04-23 執行案例整理。臨床決策請結合個案情況、最新文獻與 heart team 討論。*

*整理人：謝慕揚 MD, PhD, FESC*
