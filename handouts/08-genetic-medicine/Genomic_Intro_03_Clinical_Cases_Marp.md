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
  section.lead { background-color: #1a2740; color: #ffffff; }
  section.lead h1 { color: #ffffff; font-size: 2.1em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.divider {
    background-color: #0072bc; color: white;
    display: flex; justify-content: center; align-items: center;
  }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.4em; text-align: center; }
  section.divider h2 { color: #ffe169; }
  section.divider h3 { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.70em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b; background-color: #fff5f5;
    padding: 0.5em 1em; font-size: 0.86em;
  }
  pre {
    background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1;
    border-radius: 8px; padding: 0.8em; font-size: 0.64em;
  }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.82em; }
footer: '謝慕揚 MD, PhD, FESC | 基因體醫學入門 第三課：臨床案例應用 | 2026'
---

<!-- _class: lead -->
# 基因體醫學入門 · 第三課
## 臨床實際案例應用
### Clinical Case Applications in Cardiology
**讀書會共筆整理** | 心臟科取向入門 | 2026
講者：謝慕揚／新育／凱鈞（擇一）｜審稿：洛嘉

---

# 這一課怎麼走

- 把前兩課的**字彙**與**檢測方法**用在 4 個真實常見的心臟情境
- 每個案例固定五步：
  **表型 → 選擇檢測 → 判讀 → 家族篩檢 → 治療/諮詢**
- 貫穿主題：**基因診斷會改變我們對病人與「整個家族」的處置**

> 共筆性質：案例為教學示意，臨床決策請依最新指引與個別病情。

---

# 一個核心心法：心肌肥厚不一定是 HCM

> 同一個「表型」可能由不同基因造成 (**phenocopy**)，其中有些是**可治療**的。

| 看到 LVH，要想到 | 基因 | 為何重要 |
|------------------|------|----------|
| 肥厚性心肌病 HCM | `MYH7`/`MYBPC3` | 最常見、需風險分層 |
| Fabry 氏症 | `GLA` (X-linked) | **可酵素替代治療** |
| ATTR 類澱粉沉積 | `TTR` | **可用 tafamidis** |
| Noonan 等 RAS 病變 | `PTPN11`… | 症候群線索 |

> 這就是 NGS panel 的價值：一次把「會偽裝成 HCM」的可治療病因一起釐清。

---

<!-- _class: divider -->
# 案例 1
## 年輕 HCM 先證者與家族篩檢

---

# 案例 1：表型 → 檢測

- 28 歲男性，運動時呼吸困難；心超：**非對稱性中膈肥厚 18 mm**，臨床診斷 HCM
- 家族史：**父親 40 歲猝死**（未明原因）
- **選擇檢測**：心肌病 **NGS panel**（表型明確 → 用窄 panel，少 VUS）

> ESC 2023 cardiomyopathy 指引：基因檢測 + 遺傳諮詢為臨床工作的 **Class I** 一環。

---

# 案例 1：判讀 → 家族篩檢

- 報告：`MYBPC3` frameshift 變異，**ACMG = Pathogenic (P)**，heterozygous
- 判讀：與診斷相符；frameshift/截短是 `MYBPC3` 常見致病機轉
- **家族 cascade 篩檢**（AD，子代/一等親各 **50%**）：
  - 先證者確認 P 變異 → 一等親做**單點**檢測（便宜、明確）
  - 帶變異者：臨床追蹤（心超/ECG）＋風險分層
  - **不帶**變異者：可從專科追蹤**畢業**（節省資源、解除焦慮）

> 若報告是 **VUS** 而非 P：**不可**用來啟動 cascade，僅臨床追蹤先證者本人。

---

# 案例 1：基因陽性、表型陰性怎麼辦

- 先證者 16 歲弟弟：帶 `MYBPC3` P 變異，但目前心超**正常**
- 這是 **genotype-positive / phenotype-negative**
- 處置：**不是沒事**——因 HCM **不完全外顯**且可延遲發病
  - 定期影像/ECG 追蹤（依年齡與指引調整間隔）
  - 衛教警訊症狀、避免極限競技運動的個別化討論

> 教學點：**外顯率 (penetrance)** 與**追蹤**的臨床落地。

---

<!-- _class: divider -->
# 案例 2
## 猝死後的分子解剖 (Molecular Autopsy)

---

# 案例 2：LQTS / channelopathy

- 19 歲女性游泳後猝死，解剖**心臟結構正常** → 疑離子通道病 (channelopathy)
- **分子解剖 (molecular autopsy)**：對保存檢體做心律不整基因 panel
- 結果：`KCNQ1` **Pathogenic** → **LQT1**（典型誘因：運動、游泳）

家族意義：
- 父母/手足做**單點**檢測；帶變異者 → 心臟科評估
- **LQT1 對 beta-blocker 反應佳**；基因型可指導誘因衛教與治療

> 與悲痛家屬溝通需格外謹慎（見內部講義情境 10）：先安頓情緒，再談對在世家人的保護價值。

---

# 案例 2：基因型如何指導 LQTS 處置

| 亞型 | 基因 | 典型誘因 | 治療重點 |
|------|------|----------|----------|
| LQT1 | `KCNQ1` | 運動、游泳 | beta-blocker 反應佳 |
| LQT2 | `KCNH2` | 情緒、聲響、產後 | beta-blocker、避免聲音驚嚇/低血鉀 |
| LQT3 | `SCN5A` | 睡眠/休息 | beta-blocker 效果較有限 |

> **基因型 → 表型 → 治療**的經典範例：同樣是 LQTS，誘因與用藥考量隨基因而不同。

---

<!-- _class: divider -->
# 案例 3
## 可治療的「假 HCM」：Fabry 與 ATTR

---

# 案例 3a：Fabry 氏症（別漏掉，可治療）

- 45 歲男性，向心性 LVH，伴**神經痛、蛋白尿、角膜渦狀混濁**
- `GLA` 變異（**X-linked**，男性半合子）→ α-galactosidase A 缺乏 → Fabry
- 為何關鍵：**有疾病特異治療**（酵素替代、口服 chaperone）
- 家族：X-linked → 女性帶因者也可能受影響；母系/姊妹篩檢

> 線索在「**心臟以外**」：把表型擴展到全身（見內部講義《從外觀看見心臟病》）。

---

# 案例 3b：遺傳型 ATTR 類澱粉沉積

- 70 歲男性，LVH + 低電壓 + 多發性神經病變；骨掃描攝取陽性
- `TTR` 基因檢測：區分**遺傳型 (variant ATTR)** vs 野生型 (wild-type)
  - 例：`TTR` p.Val142Ile（V122I）等變異
- 為何關鍵：**tafamidis 可治療**；遺傳型需**家族諮詢**（AD）
- 流程：影像/骨掃描定型 + **基因檢測定性**（遺傳 vs 野生）

> 教學點：**檢測「定性」改變家族處置**——野生型不遺傳、遺傳型要 cascade。

---

<!-- _class: divider -->
# 案例 4
## 家族性高膽固醇 (FH) 與基因治療前沿

---

# 案例 4：FH 的診斷與 cascade

- 35 歲男性，LDL-C 260 mg/dL，**跟腱黃色瘤**，父親 45 歲心肌梗塞
- FH panel：`LDLR` / `APOB` / `PCSK9`（AD）
- 注意**盲點**：**WES／NGS panel 偵測不到 CNV**——臨床上「LDL 很高但 NGS 點變異陰性」的病人確實存在，可能是 `LDLR` 大段缺失/重複
- 追加 **MLPA（Multiplex Ligation-dependent Probe Amplification，多重連接探針擴增）** 偵測 CNV；實務上可把 **MLPA 與 FH panel 一起設計檢測**
- **家族 cascade**：FH 是 cascade 篩檢效益最高的疾病之一——早找出、早積極降脂

---

# 案例 4：從「診斷基因」到「編輯基因」

- 傳統：診斷後**長期**降脂（statin / ezetimibe / PCSK9 抑制劑）
- 前沿：**體內鹼基編輯**單次輸注**永久降 PCSK9** → **VERVE-102 (Heart-2)**
  - phase 1：單次給藥達 PCSK9 −88%、LDL −62%（1.0 mg/kg），效果持久
- 把第一課的字彙串起來：base editing 改的就是 **PCSK9** 基因的單一鹼基

> 詳見內部講義《VERVE-102 PCSK9 鹼基編輯》。**仍為早期試驗，非現行常規治療。**

---

# 跨案例的諮詢通則 (Counseling Pearls)

> 1. **P/LP** 才啟動 cascade；**VUS** 只追蹤先證者、不擴大、可重新分類。
> 2. **未成年預測性檢測**：除非「兒童期即需處置」（如 LQTS、FH 早期治療），否則多**延後**至可自主決定。
> 3. **基因陽性/表型陰性**：持續追蹤，因不完全外顯。
> 4. **可治療的偽 HCM**（Fabry、ATTR）別漏——基因檢測直接改變治療。
> 5. 壞消息/猝死後溝通：**先情緒、後資訊**；強調對在世家人的保護價值。

---

# Take-home（第三課）

> - 基因診斷的價值不只在病人本人，而在**改變整個家族的處置**（cascade）。
> - **同一表型、不同基因**：心肌肥厚要想到 Fabry/ATTR 等**可治療**病因。
> - **基因型指導治療**：LQTS 亞型、ATTR 定性、FH 積極降脂、PCSK9 編輯。
> - 把前兩課接起來：**字彙 → 方法 → 真實決策**。

下一步：**總院莊教授線上演講**（30 min 演講 + 30 min 討論）為本系列壓軸。

---

<!-- _class: small-text -->
# 延伸資源（已查證）

- Arbelo E, et al. 2023 ESC Guidelines for the management of cardiomyopathies. *Eur Heart J*. 2023;44:3503-3626. [DOI](https://doi.org/10.1093/eurheartj/ehad194)
- Vafai SB, et al. In Vivo Base Editing of PCSK9 with VERVE-102. *N Engl J Med*. 2026. [DOI](https://doi.org/10.1056/NEJMoa2601283)
- British Heart Foundation — Inherited heart conditions：<https://www.bhf.org.uk/informationsupport/conditions/inherited-heart-conditions>
- 內部講義：《基因醫學心臟病學：範例臨床情境分析》（10 情境）、《從外觀看見心臟病》、《基因精準醫學與心臟病》

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**讀書會共筆整理** · 審稿：洛嘉
僅供醫療專業人員教學參考｜壓軸：莊教授線上演講
