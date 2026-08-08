---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  /* ===== 台灣高血壓學會 Taiwan Hypertension Society — coral/rose identity ===== */
  section {
    font-family: 'Microsoft JhengHei', 'PingFang TC', sans-serif;
    background-color: #fff9fa;
    color: #3d2d30;
    border-top: 10px solid #c4304a;
    padding-top: 44px;
  }
  /* ---- Lead / title (coral hero) ---- */
  section.lead {
    background-color: #c4304a;
    color: #ffffff;
    border-top: 10px solid #7f1d30;
  }
  section.lead h1 { color: #ffffff; font-size: 2.0em; border-bottom: none; }
  section.lead h2 { color: #ffdbe2; }
  section.lead p, section.lead strong { color: #ffeef1; }
  section.lead a { color: #ffd9df; text-decoration: underline; }
  section.lead blockquote,
  section.lead blockquote p,
  section.lead blockquote strong {
    color: #3d2d30; background-color: #ffffff; border-left-color: #f0a9b5;
  }
  /* ---- Section dividers (coral) ---- */
  section.divider {
    background-color: #c4304a;
    color: #ffffff;
    border-top: 10px solid #7f1d30;
    display: flex; justify-content: center; align-items: center;
  }
  section.divider h1 { color: #ffffff; border-bottom: none; font-size: 2.3em; text-align: center; }
  section.divider h2 { color: #ffe08a; }
  section.divider h3 { color: #ffffff; }
  /* ---- Headings ---- */
  h1 { color: #c4304a; border-bottom: 3px solid #e6828f; padding-bottom: 0.18em; font-size: 1.45em; }
  h2 { color: #d23c50; font-size: 1.02em; }
  h3 { color: #9a5560; }
  /* ---- Tables ---- */
  table { font-size: 0.62em; width: 100%; border-collapse: collapse; }
  th { background-color: #c4304a; color: #ffffff; padding: 6px 9px; }
  td { padding: 4px 8px; border-bottom: 1px solid #f3d6dc; }
  tr:nth-child(even) { background-color: #fbe9ec; }
  /* ---- Blockquote (soft pink card) ---- */
  blockquote {
    border-left: 5px solid #c4304a;
    background-color: #fdeef0;
    padding: 0.45em 0.95em; font-size: 0.82em; border-radius: 0 10px 10px 0;
  }
  /* ---- Code ---- */
  pre { background-color: #fdf3f5; color: #3d2d30; border: 1px solid #f0cdd4; border-radius: 10px; padding: 0.6em; font-size: 0.6em; }
  pre code { background-color: transparent; color: #3d2d30; }
  code { background-color: #fbe4e8; color: #c4304a; padding: 2px 6px; border-radius: 4px; }
  strong { color: #c4304a; }
  a { color: #c4304a; }
  footer { color: #b07b83; font-size: 0.55em; }
  section.small-text { font-size: 0.8em; }
  section.ref { font-size: 0.68em; }
  img[alt~="qr"] { border: 3px solid #ffffff; box-shadow: 0 0 0 1px #f0cdd4; border-radius: 8px; }
footer: '謝慕揚 MD, PhD, FESC | 高血壓期刊回顧 Hypertension Biweekly Review | 2026-07-28'
---

<!-- _class: lead -->

# 🫀 每雙週高血壓期刊文獻回顧

## 2026-07-14 ~ 2026-07-28

**謝慕揚 MD, PhD, FESC** | 2026-07-28
NEJM · Lancet · BMJ · JAMA family · Hypertension · J Hypertens · Hypertens Res · Circulation · EHJ · JACC

> 本文件為讀書會共筆整理，僅供醫療專業人員教學參考；非個人精選推薦。

---

# 本期主題

**從「偵測」→「風險」→「器官損害表型」→「精準藥物」**

- 🔍 **偵測**：社區血壓篩檢、兒童血壓計驗證、遠距監測落地
- ⚠️ **風險**：GBD 2023 — **高收縮壓仍是缺血性心臟病死亡的頭號可改變風險（47.2%）**
- 🧠 **器官損害表型**：Circulation AI **HyperScore** 把血壓分級抓不到的預後差異揪出來
- 💊 **精準藥物**：finerenone 在**亞洲人為主**的非糖尿病 CKD 顯著護腎；β-blocker 第一線降壓角色再被質疑

> **一句話**：血壓數字本身不足以分層——要看**器官損害表型**與**病因**。

---

# Top 5 Picks 一覽

| # | 主題 | 期刊 | 方向 | 關鍵數字 |
|---|------|------|:--:|------|
| 1 | **FIND-CKD** 腎絲球亞組 finerenone | JAMA | ✅ | eGFR slope 差 **0.73**（0.22–1.24）；蛋白尿 **−42%**；亞洲人 62% |
| 2 | **HyperScore** 器官損害 AI 表型 | Circulation | 💡 | 重度器官損害 AUC **0.964**；分層贏過血壓；6 種表型 |
| 3 | **GBD 2023** 風險與 IHD 死亡 | JAMA Cardiol | 💡 | 高 SBP = 頭號可改變風險，佔 **47.2%** IHD 死亡 |
| 4 | **β-blocker 角色再定位** | JACC | 💡 | 質疑第一線降壓／HFpEF／穩定 CAD 常規使用 |
| 5 | **社區血壓篩檢** | Lancet | 💡 | 低成本提升偵測、觸及弱勢；須連結後續照護 |

> **Pearl**：用血壓數字分層不夠——看**器官損害表型（HyperScore）**與**病因（腎絲球病、內分泌性）**。

---

# ① FIND-CKD 腎絲球疾病亞組：finerenone

## [Neuen BL, et al. JAMA 2026;336(3):224-235](https://doi.org/10.1001/jama.2026.9923)

| 項目 | 內容 |
|------|------|
| 設計 | Phase 3 RCT（FIND-CKD，非糖尿病 CKD）之**腎絲球疾病亞組**；24 國 |
| 族群 | 903 人（IgA 腎病 46%、FSGS 24%、膜性腎病 10%）；**亞洲人 61.9%** |
| 介入 | finerenone 10/20 mg vs placebo（加在標準治療上） |
| 主要 | 32 個月 eGFR total slope：**−3.50 vs −4.23**（差 **0.73** mL/min/1.73m²/年，95% CI 0.22–1.24） |
| 次要 | 蛋白尿 12 個月 **−42%**（35–48%）；腎衰竭/≥40% eGFR 下降風險降低 |
| 母試驗 | 整體 eGFR slope 差 0.7（0.3–1.1，p<0.001）；複合 CV-腎 HR **0.77**（0.60–0.99） |

> ✅ 亞洲族群外推性佳（IgA 為大宗，貼近台灣 CKD 病因）；非類固醇 MRA 為非糖尿病 CKD 再添一根支柱。

![qr w:150](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABlUlEQVRYhd2YvZWEMAyEx4+AcEugFJeGS6MUSiAk4KGbkQ3L3l2+T3awP/qcCEkjCeAL52U6J8YdmKzQMuzVZuHgyv/pHEymBTiHA69NTgaE2SzRTzNem2EHbdtkVqJC+ekw9Q2BkZYFFhrW1NzHTVXW4K+8DQKrYAhOaxb8qyY9wMdhPFWCw/6f3AeA7lPSx+2nbcxX3osGgaxu5e3KhdEOaqTU3jqDNKkBMCFXQty9DNEg1WQu/PZelmtp8VoLdixINfc4ebu64sRrpS/o3ydqL+MzkJqwly133saBUpOSPuZbqomMCAdX+Ull3KvGSxhNVTaHgzrzu/P6fPvIvm6gquzyt83xrvG5WDgoYfT51qrGw4OMXBASnlx03WI4PVLrlbcdQeUjK3C8tsjBPJ51t48E2/Eqc42XrmD6GNWDwMfW8X7j4osi+oKMIlSCdSXx7Yo/l+eKGQZmf01xa3w9lzAGhfLVF60NbdLtEMrz1YuxPYaIENd7TW9giW15q0NVOOg+KWTVzcQFhPPtkktf8AvnBw5MTtQ4ow48AAAAAElFTkSuQmCC)

---

# ② HyperScore：高血壓器官損害 AI 表型

## [Alkhodari M, et al. Circulation 2026;154(4):316-333](https://doi.org/10.1161/CIRCULATIONAHA.125.077394)

| 項目 | 內容 |
|------|------|
| 方法 | 半監督式對比軌跡推論 (cTI)；整合 **566 項**多模態變數（心/腦/腎/血管/肺/肝/代謝） |
| 資料 | UK Biobank **27,099** 人開發；ARIC **5,507** 人外部驗證 |
| 結果 | 重度器官損害辨識 **AUC 0.964**；HyperScore 分層存活**顯著**，而血壓分層**不顯著** |
| 表型 | 找出 **6 種** HyperTrajectory：心臟、脂蛋白、動脈血栓、腦、心腎、肝主導 |

> 💡 **概念翻轉**：同樣血壓、器官損害可以天差地別——AI 器官損害評分比血壓數字更能預測 7 年存活與器官疾病。

![qr w:150](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABoElEQVRYhd2YsZGEMAxF5SEgpARKoTRTGqVQAiEBw7//JczdzRawIytYvDwSWV+yZLMv2ATZbTYe827V7gFnvEM6uNOfcg/neHBRrYBQS0sIF6Dc+jcDK9zPw5dJ4QAwZFzi4rt+oY0nd2GrkVxZYUhTuRVZdtmHbpPAKBjKMoZsRbmGj2rSA2w2AvuM1STND8sB3SdWQ8aTMJYH9eoqzQWZWvwpaCFjxaDL2FyaPUFb1qo98LOMr9BS0LLBCVuF/IyzzKXJutKCnQ3yMGaWRbNUIssWftcV1BO3b4J2gZswqP14pZkMroWp1c4yG1hNgNfPTJAmP0cyFYxLfZOp1U0HeUZVTR3ea1T8V18/0LNMw9XJzzbzOUs1fvGmMBfkGVUlTQZxbnqcFFrLCPkYvMZvT/CwhzS7gtLjM9vHd/B4PrN9IvhYKyE+EHu1zwd/pw6oxkPRi0HR+oJUoflA7HmHR6Xb3xEzDVzimuL0Gm8IewtjShg3S7LDOyjrE8YBgGe6Qkpoca8ZNV7XMeMRy3TQfWr3fWtMHZOk2Rf8gv0A2armfbuZ0FYAAAAASUVORK5CYII=)

---

# ③ GBD 2023：高收縮壓是 IHD 死亡頭號可改變風險

## [Benziger CP, et al. JAMA Cardiol 2026](https://doi.org/10.1001/jamacardio.2026.2435)

- 2023 全美 **473,000** 例 IHD 死亡；年齡標準化死亡率較 1990 下降 **58.7%**
- **高收縮壓 (SBP)** = 頭號可改變風險，佔 **47.2%**（36.4–57.0）IHD 死亡
- 其次：飲食風險 38.6%、高 LDL-C 28.5%
- 逆勢上升：高空腹血糖（+38.8%）、高 BMI（+54.5%，自 1990）
- 大幅下降：吸菸（−33.3%）、細懸浮微粒污染（−74.9%）

> **政策啟示**：控制**收縮壓**仍是降低缺血性心臟病死亡 CP 值最高的單一介入。

![qr w:150](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABmElEQVRYhd2YPa6EMAyEJ9qCco/AUThacjSOwhEoKRCzYzuL9v30K8cFQvkq48nYBvhCPGlxYTqAeQWBxxFnTAc35VOuB3W0LQ3X48RztyQTwoUsypPclCd46myfyZYVWp6WMcrYEJj2eUPNDUOax2R6fMNfuk0CwzAMzrplLOdfNxkBfoTV043xP7tPAD2nYo+QpiB36XWt6aDHJdrbFXnKI7m6NEeC81qbfQTrZXZy9zLkg2xWuuhllaHIdz1TQTPG+tGueixsg0Gp0D/G5A1M44eMcfdBJBu0q+W9LLJjuAnpeeaCKlRtl07CGK1d6RVAzQetZMUMz2DMtz/VNwq0WcKcMTIXdI9fGtNBTUiVvoj4duWhIi8hzVxQ2V3lnOR9s02AXqnt1u04UCr0OV69LIyRXk8yG+wRo7rchDE2uWCTwffWQTd5n2+PWBQxFpQKYQuxrSR9u4oGx3xw8d8UUU+AEbcx5oTwW0Z3+7hkA8JYSaoNUj0SQvSh0N1e0oRnfK8kiWA3jCOalP2inTTfrksbC34hXkcnR8kGsEBDAAAAAElFTkSuQmCC)

---

# ④ β-blocker 角色再定位

## [Sperry BW, et al. J Am Coll Cardiol 2026](https://doi.org/10.1016/j.jacc.2026.06.015)

| 仍是基石 | 角色被質疑 |
|---|---|
| HFrEF（EF 下降心衰） | **第一線降壓**（無強制適應症時） |
| 心絞痛 (angina) | EF 保留的 MI 後常規使用 |
| | 穩定 CAD |
| | HFpEF |
| | 圍手術期常規使用 |

> 💡 綜論主張：β-blocker 的效益比過去認知更**細緻**，需依病理、心室功能與症狀**個別化**；並點出何處該**去處方 (deprescribing)**。對高血壓 = **不應作為未合併強制適應症者的第一線用藥**。

![qr w:150](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABm0lEQVRYhd2YTa6DMAyEHWXBkiNwlBwtHI2jcASWLBB+M3bCq9ruK8dS//zBwrE7thH5gc1Ku2U6+avilU/3aTi443e6s8K1A9q3gxcGhEU1IU4Fk6p6wXcsqmtUyOj2BZ6kjHNYKDLBs1VJ304oCvTSPKdDEGeDb3UbBLpgEC57QcquTzUZAb6Y5VMBv8l9AGgxJb5ZnPBkPVCvWw0HZdlE7nT1dgVlhEbqZqU5EhSX/Ym9rMCRr/YXlHiwrPW2hO4+YTDHPZ+h4IzsVLJzfiDvgEaOBXc7BNRj72WZbXnrk1Qs6G3ZUyuuJoi7xRkIWmnywycMDO0ZGik9e5Eg41y5dVDj5bGn+saB0EWegTdjzvGm8aUNhaEgQrLS5HbVDHeU5xACQcb5aLy127nL/VCwHcLUzyCr5VM1Gmxmo7rNt2hcHHU1HnzZOuiy63xRlLEgs5hcGNkAkq0kT1uOBa0tt0VRRd3+hTEkZIkaOdiuVMaE4g8DXUxoAaH4c01qPK9DWz58zQ8HLSZ/3sec3fmaMN9uZR0L/sD+ALQDT+sTtffSAAAAAElFTkSuQmCC)

---

# ⑤ 社區血壓篩檢的角色

## [Poulter NR, et al. Lancet 2026;408(10551):289-292](https://doi.org/10.1016/S0140-6736(26)00379-X)

- 反駁「大規模篩檢排擠照護資源」的觀點
- **機會式社區篩檢**可低成本提升高血壓**偵測**，觸及不易接觸醫療的族群
- 需搭配**經驗證血壓計**與標準化流程；確診與長期管理仍須連結醫療院所
- 提升偵測是改善**族群層級**血壓控制的必要條件

> **台灣意涵**：社區/職場機會式量測 + 基層連結，是提高高血壓知曉率的務實策略。

![qr w:150](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABnklEQVRYhd2YsZXDMAxDqefCZUbwKB7NGk2jZASVLvKMI0Ald7kMkEepSaxf0SRB0GZfODfwXGZr3+522LXgjDukg3ePp1zLuXazHeaX560zyIRwB8rFpw3tMDz8rm9AzQoXwFO2K1XnxNDWk+/hgJorK4zSZG+xy4ry+a9uk8AQDHaZp6yiPJYPNZkBPs8K3Lfm78Phh9bngIqpqLeYWUJ0r1cXlmzQ5dAzVnCOcVXw8JDRVJqTwQqX/TX6jn+jBS0b9HxWu4z1yFkGqQl+k50KNkUX46pqLBu9Rp0OHu4JfQDwjvZj4VhuYwBkgryp1HhmUY9UE0BxpoN2qDQpjHQY9E0KOR2k9sn3RZhv1TcRlCl0ZR9qYpcmNNr+coyJILN4RRJ9u6Iw8nKPOHPBHUMwNsog9yz12zEhlK3ogmpB5hPIBscZpjY+U0TrpYPPrUM/chjL2HltLuhVaEUaMupRpqr9XTHTwF0af66KNHzTm2omhPriYi+JhE0Jn1+WRpEiJbTxOcYUJzWyx4ROBxVTpIwrY+z2LM254BfOD3LiDzOBAaI+AAAAAElFTkSuQmCC)

---

<!-- _class: divider -->

# 🎯 頑固型 & 次發性高血壓

---

# JAMA 頑固型高血壓綜論 + 次發性三案例

## [Juraschek SP, et al. JAMA 2026 (Resistant Hypertension review)](https://doi.org/10.1001/jama.2026.9409)

- JAMA 本期刊出**頑固型高血壓診斷與處置綜論**，與本中心 **TSOC 頑固型高血壓指引**題目高度相關
- ⚠️ **誠實註記**：檢索當下摘要**尚未釋出**；為免杜撰，僅列出處與連結，下一期補重點

**次發性高血壓——本期以 3 例呈現（見 🔬 Case Reports）**

- 原發性醛固酮增多症（adrenocortical oncocytoma，CYP11B2+）
- 嗜鉻細胞瘤兒茶酚胺危象 → 心因性休克（可逆）
- 子癇前症 → 出血性 PRES 併橋腦梗塞

> 對**年輕、嚴重、低血鉀、陣發性**高血壓，先想**次發病因**、完成 RAAS 與 metanephrine 評估——正確分流，而非直接標「頑固」。

---

<!-- _class: divider -->

# 💊 藥物治療 ／ 🔧 器械

---

# 藥物與器械焦點

| 主題 | 重點 | 連結 |
|------|------|------|
| **finerenone（非類固醇 MRA）** | 非糖尿病 CKD／腎絲球病護腎（見 Top ①）；RAAS 藥理，合併蛋白尿高血壓具實務意義 | [DOI](https://doi.org/10.1001/jama.2026.9923) |
| **ARB 的 P-gp 抑制 × DOAC 出血** | 部分 ARB 抑制 P-glycoprotein，恐增併用 DOAC 出血風險；HTN+AF 選藥留意 | [DOI](https://doi.org/10.1038/s41440-026-02733-2) |
| **RDN 中樞抗發炎機轉（動物）** | SHR：RDN 使 SBP **210→143 mmHg**；經 P2X7R/PI3K/Akt 降下視丘神經發炎 | [DOI](https://doi.org/10.1161/HYPERTENSIONAHA.126.26793) |

> 本期無新的 RDN **人體隨機試驗**；判讀 RDN 療效仍須回到**服藥順從性**與 sham-control 議題（呼應 TSOC 頑固型高血壓題目）。

---

<!-- _class: divider -->

# 👥 特殊族群 & 亞洲/台灣資料

---

# 特殊族群焦點

| 主題 | 重點 | 連結 |
|------|------|------|
| **高動脈硬化者強化降壓（中國 RCT 事後）** | baPWV 最高分位者，強化降壓後 eGFR 下降較大（腎功能異常 0%/4.8%/6.4%）；降壓需個別化 | [DOI](https://doi.org/10.1093/ajh/hpag088) |
| **STRIDE BP 兒童血壓計驗證** | 628 篇僅 22 篇通過；兒童專用經驗證裝置**嚴重不足**；選機查 STRIDE BP 清單 | [DOI](https://doi.org/10.1161/HYPERTENSIONAHA.125.26206) |
| **含鋅 polaprezinc 輔助減鹽（日本社區）** | 改善老年味覺、促進減鹽；亞洲高鹽飲食族群可參考 | [DOI](https://doi.org/10.1038/s41440-026-02740-3) |

> **亞洲相關性最高**：FIND-CKD 腎絲球亞組 **62% 為亞洲人、46% IgA 腎病**——與台灣 CKD 病因結構相近。

---

<!-- _class: divider -->

# 🔬 Case Reports

---

# 三例次發性 / 急性高血壓

| 案例 | 教學點 | 連結 |
|------|------|------|
| **原發性醛固酮增多症**（adrenocortical oncocytoma）| 44M 嚴重 HTN+低血鉀；AVS 右側優勢；CYP11B2+；oncocytoma 也可分泌醛固酮、具惡性風險 | [DOI](https://doi.org/10.1080/08037051.2026.2680794) |
| **嗜鉻細胞瘤兒茶酚胺危象**（心因性休克）| 30F 以休克/心跳停止首發；α-/β-阻斷後手術；兒茶酚胺心肌病**可逆** | [DOI](https://doi.org/10.1210/jcemcr/luag199) |
| **子癇前症出血性 PRES**（併橋腦梗塞）| 26 週初產婦 190/110、抽搐；MRI 腦幹梗塞+點狀出血；及早控壓與影像診斷 | [DOI](https://doi.org/10.1016/j.radcr.2026.06.142) |

> 三例都提醒：**次發性高血壓與高血壓急症**在年輕、嚴重、合併特徵時要優先排查。

---

<!-- _class: divider -->

# 整合 Take Home

---

# 本期 5 大臨床啟示

1. **血壓數字分層不夠**——器官損害表型（AI HyperScore）比血壓更能預測預後（Circulation）。
2. **控制收縮壓仍是 CP 值最高的介入**——GBD 2023：高 SBP 佔 IHD 死亡 47.2%（JAMA Cardiol）。
3. **finerenone 為非糖尿病 CKD／腎絲球病護腎添新支柱**，且**亞洲外推性佳**（JAMA / FIND-CKD）。
4. **β-blocker 非高血壓第一線**（無強制適應症時），需個別化與去處方（JACC）。
5. **次發性高血壓要主動排查**——原發性醛固酮增多症、嗜鉻細胞瘤、子癇前症急症，別直接標「頑固」。

---

<!-- _class: small-text -->

# 縮寫對照

| 縮寫 | 全名 | | 縮寫 | 全名 |
|---|---|---|---|---|
| CKD | Chronic Kidney Disease | | RDN | Renal Denervation |
| eGFR | est. Glomerular Filtration Rate | | SHR | Spontaneously Hypertensive Rat |
| MRA | Mineralocorticoid Receptor Antagonist | | baPWV | brachial-ankle Pulse Wave Velocity |
| IHD | Ischemic Heart Disease | | CCB | Calcium-Channel Blocker |
| SBP/DBP | Systolic/Diastolic BP | | ARB | Angiotensin Receptor Blocker |
| GBD | Global Burden of Disease | | DOAC | Direct Oral Anticoagulant |
| ML | Machine Learning | | AF | Atrial Fibrillation |
| ARIC | Atherosclerosis Risk in Communities | | AVS | Adrenal Venous Sampling |
| CKM | Cardiovascular-Kidney-Metabolic | | CYP11B2 | Aldosterone Synthase |
| PVN | Paraventricular Nucleus | | PRES | Posterior Reversible Encephalopathy Syndrome |

---

<!-- _class: ref -->

# 參考文獻（1/2）

1. Neuen BL, et al. Finerenone in CKD Due to Glomerular Diseases: RCT. [*JAMA*. 2026;336(3):224-235.](https://doi.org/10.1001/jama.2026.9923)
2. Alkhodari M, et al. Contrastive ML to Quantify Hypertensive Multiorgan Damage. [*Circulation*. 2026;154(4):316-333.](https://doi.org/10.1161/CIRCULATIONAHA.125.077394)
3. Benziger CP, et al. Modifiable Risk Factors & IHD Mortality: GBD 2023. [*JAMA Cardiol*. 2026.](https://doi.org/10.1001/jamacardio.2026.2435)
4. Sperry BW, et al. Refining the Role of Beta-Blockers. [*J Am Coll Cardiol*. 2026.](https://doi.org/10.1016/j.jacc.2026.06.015)
5. Poulter NR, et al. Community-based blood pressure screening. [*Lancet*. 2026;408(10551):289-292.](https://doi.org/10.1016/S0140-6736(26)00379-X)
6. Juraschek SP, et al. Review of Diagnosis and Management of Resistant Hypertension. [*JAMA*. 2026.](https://doi.org/10.1001/jama.2026.9409)
7. Liang W, et al. RDN Modulates Hypothalamic Neuroinflammation via P2X7R/PI3K/Akt. [*Hypertension*. 2026.](https://doi.org/10.1161/HYPERTENSIONAHA.126.26793)
8. Akasaki Y. ARB P-gp inhibition and DOAC bleeding risk. [*Hypertens Res*. 2026.](https://doi.org/10.1038/s41440-026-02733-2)

| Finerenone | HyperScore | GBD 2023 | β-blocker | Lancet 篩檢 |
|:--:|:--:|:--:|:--:|:--:|
| ![qr w:95](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABlUlEQVRYhd2YvZWEMAyEx4+AcEugFJeGS6MUSiAk4KGbkQ3L3l2+T3awP/qcCEkjCeAL52U6J8YdmKzQMuzVZuHgyv/pHEymBTiHA69NTgaE2SzRTzNem2EHbdtkVqJC+ekw9Q2BkZYFFhrW1NzHTVXW4K+8DQKrYAhOaxb8qyY9wMdhPFWCw/6f3AeA7lPSx+2nbcxX3osGgaxu5e3KhdEOaqTU3jqDNKkBMCFXQty9DNEg1WQu/PZelmtp8VoLdixINfc4ebu64sRrpS/o3ydqL+MzkJqwly133saBUpOSPuZbqomMCAdX+Ull3KvGSxhNVTaHgzrzu/P6fPvIvm6gquzyt83xrvG5WDgoYfT51qrGw4OMXBASnlx03WI4PVLrlbcdQeUjK3C8tsjBPJ51t48E2/Eqc42XrmD6GNWDwMfW8X7j4osi+oKMIlSCdSXx7Yo/l+eKGQZmf01xa3w9lzAGhfLVF60NbdLtEMrz1YuxPYaIENd7TW9giW15q0NVOOg+KWTVzcQFhPPtkktf8AvnBw5MTtQ4ow48AAAAAElFTkSuQmCC) | ![qr w:95](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABoElEQVRYhd2YsZGEMAxF5SEgpARKoTRTGqVQAiEBw7//JczdzRawIytYvDwSWV+yZLMv2ATZbTYe827V7gFnvEM6uNOfcg/neHBRrYBQS0sIF6Dc+jcDK9zPw5dJ4QAwZFzi4rt+oY0nd2GrkVxZYUhTuRVZdtmHbpPAKBjKMoZsRbmGj2rSA2w2AvuM1STND8sB3SdWQ8aTMJYH9eoqzQWZWvwpaCFjxaDL2FyaPUFb1qo98LOMr9BS0LLBCVuF/IyzzKXJutKCnQ3yMGaWRbNUIssWftcV1BO3b4J2gZswqP14pZkMroWp1c4yG1hNgNfPTJAmP0cyFYxLfZOp1U0HeUZVTR3ea1T8V18/0LNMw9XJzzbzOUs1fvGmMBfkGVUlTQZxbnqcFFrLCPkYvMZvT/CwhzS7gtLjM9vHd/B4PrN9IvhYKyE+EHu1zwd/pw6oxkPRi0HR+oJUoflA7HmHR6Xb3xEzDVzimuL0Gm8IewtjShg3S7LDOyjrE8YBgGe6Qkpoca8ZNV7XMeMRy3TQfWr3fWtMHZOk2Rf8gv0A2armfbuZ0FYAAAAASUVORK5CYII=) | ![qr w:95](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABmElEQVRYhd2YPa6EMAyEJ9qCco/AUThacjSOwhEoKRCzYzuL9v30K8cFQvkq48nYBvhCPGlxYTqAeQWBxxFnTAc35VOuB3W0LQ3X48RztyQTwoUsypPclCd46myfyZYVWp6WMcrYEJj2eUPNDUOax2R6fMNfuk0CwzAMzrplLOdfNxkBfoTV043xP7tPAD2nYo+QpiB36XWt6aDHJdrbFXnKI7m6NEeC81qbfQTrZXZy9zLkg2xWuuhllaHIdz1TQTPG+tGueixsg0Gp0D/G5A1M44eMcfdBJBu0q+W9LLJjuAnpeeaCKlRtl07CGK1d6RVAzQetZMUMz2DMtz/VNwq0WcKcMTIXdI9fGtNBTUiVvoj4duWhIi8hzVxQ2V3lnOR9s02AXqnt1u04UCr0OV69LIyRXk8yG+wRo7rchDE2uWCTwffWQTd5n2+PWBQxFpQKYQuxrSR9u4oGx3xw8d8UUU+AEbcx5oTwW0Z3+7hkA8JYSaoNUj0SQvSh0N1e0oRnfK8kiWA3jCOalP2inTTfrksbC34hXkcnR8kGsEBDAAAAAElFTkSuQmCC) | ![qr w:95](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABm0lEQVRYhd2YTa6DMAyEHWXBkiNwlBwtHI2jcASWLBB+M3bCq9ruK8dS//zBwrE7thH5gc1Ku2U6+avilU/3aTi443e6s8K1A9q3gxcGhEU1IU4Fk6p6wXcsqmtUyOj2BZ6kjHNYKDLBs1VJ304oCvTSPKdDEGeDb3UbBLpgEC57QcquTzUZAb6Y5VMBv8l9AGgxJb5ZnPBkPVCvWw0HZdlE7nT1dgVlhEbqZqU5EhSX/Ym9rMCRr/YXlHiwrPW2hO4+YTDHPZ+h4IzsVLJzfiDvgEaOBXc7BNRj72WZbXnrk1Qs6G3ZUyuuJoi7xRkIWmnywycMDO0ZGik9e5Eg41y5dVDj5bGn+saB0EWegTdjzvGm8aUNhaEgQrLS5HbVDHeU5xACQcb5aLy127nL/VCwHcLUzyCr5VM1Gmxmo7rNt2hcHHU1HnzZOuiy63xRlLEgs5hcGNkAkq0kT1uOBa0tt0VRRd3+hTEkZIkaOdiuVMaE4g8DXUxoAaH4c01qPK9DWz58zQ8HLSZ/3sec3fmaMN9uZR0L/sD+ALQDT+sTtffSAAAAAElFTkSuQmCC) | ![qr w:95](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAADcAQMAAAAhlF3CAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABnklEQVRYhd2YsZXDMAxDqefCZUbwKB7NGk2jZASVLvKMI0Ald7kMkEepSaxf0SRB0GZfODfwXGZr3+522LXgjDukg3ePp1zLuXazHeaX560zyIRwB8rFpw3tMDz8rm9AzQoXwFO2K1XnxNDWk+/hgJorK4zSZG+xy4ry+a9uk8AQDHaZp6yiPJYPNZkBPs8K3Lfm78Phh9bngIqpqLeYWUJ0r1cXlmzQ5dAzVnCOcVXw8JDRVJqTwQqX/TX6jn+jBS0b9HxWu4z1yFkGqQl+k50KNkUX46pqLBu9Rp0OHu4JfQDwjvZj4VhuYwBkgryp1HhmUY9UE0BxpoN2qDQpjHQY9E0KOR2k9sn3RZhv1TcRlCl0ZR9qYpcmNNr+coyJILN4RRJ9u6Iw8nKPOHPBHUMwNsog9yz12zEhlK3ogmpB5hPIBscZpjY+U0TrpYPPrUM/chjL2HltLuhVaEUaMupRpqr9XTHTwF0af66KNHzTm2omhPriYi+JhE0Jn1+WRpEiJbTxOcYUJzWyx4ROBxVTpIwrY+z2LM254BfOD3LiDzOBAaI+AAAAAElFTkSuQmCC) |

---

<!-- _class: ref -->

# 參考文獻（2/2）

9. Wang Y, et al. Intensive BP lowering & kidney decline in high arterial stiffness. [*Am J Hypertens*. 2026.](https://doi.org/10.1093/ajh/hpag088)
10. Stergiou GS, et al. Validated Automated Cuff BP Devices for Children: STRIDE BP. [*Hypertension*. 2026.](https://doi.org/10.1161/HYPERTENSIONAHA.125.26206)
11. Kudo H, et al. Zinc-containing polaprezinc for salt reduction in older HTN. [*Hypertens Res*. 2026.](https://doi.org/10.1038/s41440-026-02740-3)
12. Lloyd-Jones DM. Cardiovascular-Kidney-Metabolic Syndrome. [*Circulation*. 2026;154(4):416-419.](https://doi.org/10.1161/CIRCULATIONAHA.126.080905)
13. Marcus GM, et al. Caffeine and CVD: AHA Scientific Statement. [*Circulation*. 2026.](https://doi.org/10.1161/CIR.0000000000001454)
14. Nolan T. Long term benefits of blood pressure lowering. [*BMJ*. 2026;394:e100266.](https://doi.org/10.1136/bmj-2026-100266)
15. Feigenblum N, et al. Challenges Implementing Remote Patient Monitoring for HTN. [*JAMA Cardiol*. 2026.](https://doi.org/10.1001/jamacardio.2026.2095)
16. Facility-based blood pressure measurement and treatment. [*Lancet*. 2026;408(10551).](https://doi.org/10.1016/S0140-6736(26)01230-4)
17. Ji Q, et al. Adrenocortical oncocytoma manifesting as primary aldosteronism. [*Blood Press*. 2026;35(1):2680794.](https://doi.org/10.1080/08037051.2026.2680794)
18. van der Linden T, et al. Cardiogenic shock due to pheochromocytoma crisis. [*JCEM Case Rep*. 2026;4(8):luag199.](https://doi.org/10.1210/jcemcr/luag199)
19. Nalla S, et al. Hemorrhagic PRES with pontine infarction in early-onset eclampsia. [*Radiol Case Rep*. 2026;21(10):4715-4720.](https://doi.org/10.1016/j.radcr.2026.06.142)

---

<!-- _class: lead -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
每雙週高血壓期刊文獻回顧 · 2026-07-28

> 本文件為讀書會共筆整理，僅供醫療專業人員教學參考；資料經 PubMed 檢索與 WebSearch 交叉驗證。
