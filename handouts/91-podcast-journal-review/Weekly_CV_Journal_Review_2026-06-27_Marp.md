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
  section.lead blockquote { color: #2d3436; }
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
  section.abbr { font-size: 0.62em; }
  .qr {
    position: absolute;
    right: 40px;
    bottom: 80px;
    text-align: center;
    font-size: 0.65em;
    color: #555;
  }
  .qr img { width: 110px; height: 110px; border: 1px solid #dcdde1; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-06-20 ~ 2026-06-27'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-06-20 ~ 2026-06-27

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每篇 Pick / 文章附 QR Code，可掃描跳轉原文

> 本期已與上一期（2026-06-20）交叉去重，全為新刊出或未收錄之文獻。

---

# 🎯 本週主題與固定欄目

## 瓣膜介入的「精算與救援」週

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 本週 TAVI 重要文獻
3. 🔧 **TEER Section** — PASCAL / MitraClip / TriClip 進展
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — 結構介入救援 × 5
6. 📖 **參考文獻 + 縮寫對照**

---

# ⭐ Top 5 Picks

| 試驗／研究 | 期刊 | 關鍵數字 |
|------------|------|----------|
| **Ross 手術現代成人結局** | *JACC* | 12 年存活≈一般人口；自體瓣再介入 **1.1%** |
| **ABC 雙葉瓣破裂演算法** | *Circ CV Interv* | 敏感度 **100%**、特異度 89.1% |
| **REPAIR：PASCAL M-TEER 小瓣口** | *JACC Adv* | <4 cm² 仍可行；1 年死亡 13.0% vs 13.6% |
| **FINEARTS-HF 睡眠呼吸中止** | *JACC HF* | 睡眠呼吸中止 → 主要終點 **↑43%** |
| **SGLT2i 與 TAVI 後結局** | *JACC Adv* | MACE **HR 0.65**；HF 住院 HR 0.58 |

---

<!-- _class: divider -->
# Pick #1
## Ross 手術
### 現代成人的長期結局標竿

---

# Ross 手術 — 設計與結果

**Contemporary Outcomes of the Ross Procedure in Adults.** *J Am Coll Cardiol* 2026 Jun 23.
🔗 [DOI: 10.1016/j.jacc.2026.03.173](https://doi.org/10.1016/j.jacc.2026.03.173)

- 單中心 **455** 例成人（47±12 歲、73% 男）；中位追蹤 **9.0 年**，追蹤完整度 98%
- 手術死亡率 **0.4%**；無病人—人工瓣不匹配；永久節律器置入僅 **0.8%**
- 12 年存活與年齡／性別配對一般人口**相當**
- 12 年平均主動脈瓣壓差僅 **4.0 mmHg**

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAACYUlEQVR4nO2bQWrkMBBFX0WCLGXoA+Qo8g3mSGFuZh8lBwhYy4DNn4VkdyeL0D3QaUFKC9NGb/GhqNJXldvElWt+upYERx119AmKtTUCZhZh3h/7VuxEq6MESVItiZr2HXtdgCxJWu4rwNGb0JY9bEZeANKHQVqpmTfeXYCj/4XaCJCXIP2tEfxhAY5+s+KXd80DpvnPeyQvpx8Q4OjN0Wo2vpxEFhgJmIcAJAHlfgIcvRHdqu8DwMYSIb89q55gs5mZDfcV4OiVK7bsqevD1DKquYzLu/PDtTqKtARpSmvzFlqgOnotoCm1F00P1+po3I16rAYDCGvbS2u0vGxRlNPagVZHI5QBSO/RssDyBMAWIb1XxmpAH67V0Vb1prSyF8G1dTAmgoAgSF4Ju0D3GC1BZK3Uwph1+dBE8Gj1gLZoTTSDQV6Cqt+YkuQuoyuU1tBNuqx6WvZOb20bem71gTYHfxxZrd+ejl/sNt6j1Qe6mdnLio0Emb1I5LfWPzyPUjrR+rvRi4yqdrCm1dcs80rYC1qe1XKrPEtTiUCJ2FiJIObhrgIcvXrtZuLwhLu32NtPQe7ge0Ejta3U2rgR2KLqDKUMAAHL6kKro3sKHW3clmDrYRZbQ8Nzqw/0/M1Turx52Ugb/NcOfRdafznK15vwkVZw9Dc8tzpB673K6pyknltBBpgow6cBysO1OvoJLRFNJbbDa35Zod6dhx8S4OgNaFqB9FFPMHs9u/o3/1a3C/TTN0+1CAZZnUaW02ok7Vn2cK2ORmCz9lJO63mnDf6L7bF8uFZHzf8R5Kijd0H/AcZwoig0edXxAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# 1.1%
## 12 年自體移植瓣 (autograft) 再介入率
### 術前 AR vs AS 無差異（1.2% vs 1.1%，p=0.39）

任何心臟再介入 12 年僅 **3.5%**

---

# Ross 手術 — 臨床啟示

> 💡 當代技術下，Ross 手術於合適年輕成人（含 >50 歲、含術前 AR）展現**接近正常人口的存活與極低再介入率**。

- 對不願終生抗凝、重視耐久度的年輕主動脈瓣病人是強力選項
- 為 TAVI / SAVR / Ross 三方決策提供重要對照標竿
- 高度選擇之單中心經驗，外推需審慎

---

<!-- _class: divider -->
# Pick #2
## ABC Sizing 演算法
### 雙葉瓣 TAVR 主動脈根部破裂預測

---

# ABC 雙葉瓣破裂演算法 — 設計與結果

**ABC Sizing Algorithm for SAPIEN 3.** *Circ Cardiovasc Interv* 2026 Jun 25.
🔗 [DOI: 10.1161/CIRCINTERVENTIONS.126.016918](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016918)

- 15 國多中心病例對照，170 例（**23 破裂** vs 147 對照），CT 盲化判讀
- 三大驅動因子：**鈣化體積、竇部狹窄、瓣環過度撐大**

| 指標 | 數值 |
|------|------|
| 任一高風險條件 **敏感度** | **100%**（85.7–100） |
| **特異度** | 89.1%（83.1–93.2） |
| 診斷勝算比 (DOR) | **374.5** |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAACbElEQVR4nO2bQWrkMBBFX8WCLG3IAXIU+WY509zAPkoOEJCWDTI1i5LahoGhe+FY0KWFcVtv8UGU6ldJLcqDY317lARHHXX0DbLUMeeAzPZ9EwDaVDhTgKPPoIOqqiqMN9Eli8jMoDIDRFVVTecKcPQptEYPIPOoqgvAKgGLvPl0AY4+j+Z3ZRURVgmoavltAY4+g26iy6hKTLTY+l0Bjv532II0Gz8UyKEI4000pg9gVCCfJ8DRJ9HNfB8A8pWA+P1eXcYqIiLTuQIcfXCEGj0A5E0UCjAWFArH2vlyrY6imgZVTYMCw311BiU2l2HIcrlWR5uD/yyYb48JdGETs4g2O50twNHHhoVVTABWag3tcf/psdUJijUqom2H+1vtb6gmqIt3uVZHaU2n5i0WS1mq+2yNssu1OrrXW1pfxh9R8gSMP0HinwkglA60OvoGOcA6bbI3C1k/VVW/AxZ0ltV60PriKC09tUS10Lx8dYd303G5VkcttmQeSzPqY4GoN2GdoBZdY+lE64ujde9bp5+gsNXHOiUVGIoAKNnzVi/oWFsWh7wV0yZ2YhLToNY77ELri6MHB197Gbq/tYTmeasT1KpjW7Joj9KqrAPiq9UFeujB1yoLEMaExPRRIH+0E+TLtTpaO08Ae7Nwbz/Zt+ix1QcasBNjQOo5cSi6ToNNK3ko2JnX5VodNbTaQau8biJfCWRmE5Fpk3pDoxOtr4xyOIg0O2j9Xf1n+E7YH1prqyxid9XqrQ2PrY7Qw93BVYJ1B207lIlafvWi9dXR+52nHGxl5Ctt1ifUJbdGfB9aXxsV/0eQo46egv4FzzqOcjQRym4AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# ABC 演算法 — 臨床啟示

> 💡 雙葉瓣 TAVR 主動脈根部破裂罕見卻致命；ABC 演算法提供**接近 100% 敏感度的 rule-out 篩檢**。

- 無任一高風險條件 → 破裂風險極低
- 有條件 → 重新考慮瓣徑、改用自膨式瓣 (SEV)、保守撐大或外科
- 仍須外部前瞻驗證

---

<!-- _class: divider -->
# Pick #3
## REPAIR Study
### PASCAL M-TEER 小三維瓣口面積

---

# REPAIR — 設計與結果

**Small MVOA in M-TEER: The REPAIR Study.** *JACC Adv* 2026;5(6):103014.
🔗 [DOI: 10.1016/j.jacadv.2026.103014](https://doi.org/10.1016/j.jacadv.2026.103014)

- PASCAL 二尖瓣經導管緣對緣修復 (M-TEER)；依基線三維瓣口面積 (3D-MVOA) 分層
- n=**1,189**；<4 cm²（28%）vs ≥4 cm²（72%）

| 指標 | <4 cm² | ≥4 cm² |
|------|--------|--------|
| 技術成功 | 95.9% | 98.2%（p=0.028） |
| MR ≤1+ | 72% | 72%（NS） |
| **1 年死亡** | **13.0%** | **13.6%**（p=0.76） |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAACz0lEQVR4nO2cS4qkQBCGvxiFXuqN0psNfaS5gXWUOsBAumxQ/lnkQ7thpmjGtishciFqfYuAn8h4pWXiM+v241M4OO+881/KL5bXxGY2ATYBsPSJKb/319jj/Ml8J0kSLD16HTeDxQyGtyQ3QZIUr7LH+bP57Jx0IkTQPKzYRCe9jpBcfLrQHue/ireJTkAnzcC+SX+TPc6fyA9rvrmNYBObEeI32uP8f/PJOw9F0s26lXDvV1jG8nIQsFxhj/Pn81tKj9NeHGLNn+mU7m5mZjZeZY/z5/F9dk4Als10GztgWBHsl8vscf5cHimW+ihEkLSSInGIOZ0mpHeS5mez3/kHK9e1w5qUhkHKWpIfC+L6tseTWxupKiruPNdKOHl37JSaHK5vY3zSV9Kat+ZQtUzCDyupEg6xc32b48v+zPtYW1fQyi6369saf0ioNKeoS/bVFI4h6UvqaT2b/c4/WCX+QulfdSIoy13cuVNW/9nsd/7BkiIpwuYiqUpbU+estMffBvnU37AQRwxKpzLErYelL6F4MeT9yUb5NOvNBa9NS1/GhcObcRs72U+t2HSVPc6fyKf8qmRV+aKZXARrHko7y/OrFvlDQyNnUEOueg+/KuL1b5t89t+9FkrHdWKd75eayfPnJvkqbVc6GGm0APto3/uT7fJ1qlAnRIMOneg9HPt8oWU+3F8k3ctZq6A9CBf1kzs/qf3O/22lDkaeJeQhMJT8uVB19342+51/yO8b8t2MOim0qQz5pViP0D6h/c7/a5X5Ee925aF2KtNgyeNvw3z9fgFyJJ4BzctLduyZzQh399/2+EN9lPw3pEl/vYuF8/q3Rf69vnUqGI+F075Ju76t8f2HZ2PYerF0q4VfmxHmDaAenH02+51/sI7nY+uF8hHS4SSl969a5Htgs/ywjAi2njDnd2IxYPhtuo3xAnucP5c3/38G551vlv8DSb5QN2CLT50AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# REPAIR — 臨床啟示

> 💡 小瓣口面積非 PASCAL M-TEER 絕對禁忌：審慎選擇下 MR 降幅與 1 年結局相當。

- 校正後 HR（<4 vs ≥4 cm²）= **1.05**（0.67–1.63）
- 須以三維影像精算殘餘瓣口、術中監測跨瓣壓差
- 防範**醫源性二尖瓣狹窄 (iatrogenic mitral stenosis)**

---

<!-- _class: divider -->
# Pick #4
## FINEARTS-HF
### 睡眠呼吸中止次族群分析

---

# FINEARTS-HF 睡眠呼吸中止 — 結果

**Sleep Apnea in HFmrEF/HFpEF: FINEARTS-HF.** *JACC Heart Fail* 2026 Jun 23.
🔗 [DOI: 10.1016/j.jchf.2026.103187](https://doi.org/10.1016/j.jchf.2026.103187)

- FINEARTS-HF（finerenone vs placebo，n=**6,001**，LVEF ≥40%）預設次族群
- 合併**睡眠呼吸中止**者 → 主要終點（總 HF 事件＋CV 死亡）風險 **↑約 43%**
- finerenone 整體降低主要終點約 **16%**；**益處不因睡眠呼吸中止而打折**

> 💡 睡眠呼吸中止是 HFpEF/HFmrEF 被低估的高風險共病 → 應主動篩檢，且高風險者反而是 finerenone 治療的優先對象

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAACP0lEQVR4nO2bQYrjQAxFn9qGLMvQB8hR7BvMkZq5mesofYABexmo8GehcuI0DNOZIZ2Clham4noLgVDpS+WY+KTll8+SEGiggb7AatUmwGwAmwDyANtW/0gHAv20SUsnSRKjCr6cU/ENRkmOzE/3NVBHa/asva/s7f0gm1LBM296uAOB/hs6LmfTnE4Ga/8MBwL9s/UffguEjTOQj+ULHAj07mhdZbxBV5SHX9u7JGB9nAOB3qkytuW4dPr4qBYqowm0ikC3BYBOV524s4hWE6grQTObkiTpZOThbPuNZnz95mhtq2pGAePWeUEqcE21yK3no163NNOJcQFIBc2pbGUsTsKG0F20bnJre9TgRbSaQGu/NS6DuVrPBsoGsL4WwRnzpHu6r4FuCj5Jmv1Nd6lbchkfdasVFOlWUfipl4pveATHqFttoDValxSqPXFSbYw9UFG32kB3VyTb0YdnlMfIYxm51Qa63W8tl/As8KHf8syLaDWF2gSQj5J+DtTTsSZd+QoHAv2bVQWff5RerFYn7+OCDMBIoDwsD3Mg0PsnT9dOuDbL1+H8NpeKk/D5aO8xAhDrQZCEjao3XbAO1oqvgd7cb10arL3AIDRhM+jNN09LFfS7CYaPMeIkbAN1lVFPvW0lOJngbECHPdKBQP8DrZ87AWbHgl9OfqUDgd6B2rQeRB5qyaofGka/1RK6jXbrIN7e3nvIdtgNoprx9TujPbU8AayvXryUjyfzPjkPXYn7rVZQi38EBRroQ9DfCX3GkBXJGf8AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# Pick #5
## SGLT2i 與 TAVI 後結局
### 統合分析

---

# SGLT2i 與 TAVI 後結局 — 結果

**SGLT-2i and Outcomes After TAVI (Meta-Analysis).** *JACC Adv* 2026;5(6):102884.
🔗 [DOI: 10.1016/j.jacadv.2026.102884](https://doi.org/10.1016/j.jacadv.2026.102884)

- 6 研究（1 RCT + 5 世代），共 **35,075** 例 TAVI

| 結局 | 效應量 |
|------|--------|
| MACE | **HR 0.65**（0.44–0.95） |
| 心衰竭住院 | HR 0.58（0.40–0.86） |
| 全因死亡 | HR 0.71（0.55–0.91） |
| 心血管死亡 | RR 0.55（0.34–0.89） |

> 💡 GRADE 確定性**低**（觀察性為主）→ 屬假說生成，非因果

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAAC/klEQVR4nO2cTYrcMBBGX0WCXsowB+ij2DfIkUJuZh9lDhCwlg0yXxaS3dMJmWGgp9OC0qLB8lsUiPr7Sm4Tn1nLt0/h4Lzzzn8pn62tic1Yhs0gm7EMYDbA/j4+xh7n78wHSZKAUKO12QCM6/EjSVofZY/z9+abc+aI/VhBUsEmQD8HqC4+PdAe5+/Fx5unzUR+kVVPzgNALI+0x/mv5IPMzgXNqWBTKrSo/L/scf4+vKQCsFlNuOQI5NPePCVJ8wPtcf6e/FbLY1pUbkkYAJsAFjOrNddT2u/8O0tv1hrqT3VYqdy8laT52ex3/kM+x9bhTuliLOeLAZvZlE+y6fr2UfY4f0c+UqtmtqjW/wbV1LucL6blXID0K7JYKM9nv/MfrFZaJak9rkGaCWJc90etQVXk8PjcGR+BIJYpluukwUgrghKNdDHBZpBf3H975LMZpMuuMp8Lmmmlc/VkOJSsJ7Tf+fdWjc+j2qlCKlA16fWAUlOnPT73xu8d0Ar1aMeaawuak9TkDoI0J8+//fFNgTz8V/NxyMAxRPL6qlM+QhJGHrBxHeqm4GJAKCwDaBkweX3VI/+mP7p2RS0qH3tH4Hb/7Y2njfZT4VpaQWrSZIvKeHzul88R6fV066tt5q85R2j9r9/P6Y+PVAUjFYx0bOcXsUyb7T4NTal8Nvud/2DtrVEbGO2tUWEPze2t598uefaB4K5qzDdKdBWhW+D2/NstP76eJOlibTtJkC5t5j+q7DX1k9rv/L/WPiECmioZpHmvn1t8pjmx+29v/J/3N5pWtd50vTWE+/l2yL+9ITnWTlgtCTfN8nrcnn/74/f4LOmqNe97N5Mk1zd65Ov9doNQ+1xBU7JsnEHkodZcWob1AfY4/5V8kE1QL8RqzpE67tcaZD9eXb/qj//r+5TFQrFRWzRSiVq+Bxmp7I79bPY7//6q59uGvalEI61QP0LKsWqWIsdi4/wIe5y/L1/vx7aHPCDY4iFtFMix1Et2nn975M3/n8F557vlfwPjSClK5qMv5AAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 本週 TAVI 相關文獻
### Drake 主要臨床方向

---

# TAVI #1 — ABC 雙葉瓣破裂演算法（見 Pick #2）

**ABC Sizing Algorithm for SAPIEN 3.** *Circ Cardiovasc Interv* 2026 Jun 25.
🔗 [DOI: 10.1161/CIRCINTERVENTIONS.126.016918](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016918)

- 15 國、170 例；任一高風險條件對主動脈根部破裂**敏感度 100%**、特異度 89.1%
- 三大驅動：**鈣化體積、竇部狹窄、瓣環過度撐大**

> 💡 BAV-TAVR 術前以 CT 套用 ABC 演算法作為破裂「rule-out」；高風險者考慮 SEV、保守撐大或外科

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAACbElEQVR4nO2bQWrkMBBFX8WCLG3IAXIU+WY509zAPkoOEJCWDTI1i5LahoGhe+FY0KWFcVtv8UGU6ldJLcqDY317lARHHXX0DbLUMeeAzPZ9EwDaVDhTgKPPoIOqqiqMN9Eli8jMoDIDRFVVTecKcPQptEYPIPOoqgvAKgGLvPl0AY4+j+Z3ZRURVgmoavltAY4+g26iy6hKTLTY+l0Bjv532II0Gz8UyKEI4000pg9gVCCfJ8DRJ9HNfB8A8pWA+P1eXcYqIiLTuQIcfXCEGj0A5E0UCjAWFArH2vlyrY6imgZVTYMCw311BiU2l2HIcrlWR5uD/yyYb48JdGETs4g2O50twNHHhoVVTABWag3tcf/psdUJijUqom2H+1vtb6gmqIt3uVZHaU2n5i0WS1mq+2yNssu1OrrXW1pfxh9R8gSMP0HinwkglA60OvoGOcA6bbI3C1k/VVW/AxZ0ltV60PriKC09tUS10Lx8dYd303G5VkcttmQeSzPqY4GoN2GdoBZdY+lE64ujde9bp5+gsNXHOiUVGIoAKNnzVi/oWFsWh7wV0yZ2YhLToNY77ELri6MHB197Gbq/tYTmeasT1KpjW7Joj9KqrAPiq9UFeujB1yoLEMaExPRRIH+0E+TLtTpaO08Ae7Nwbz/Zt+ix1QcasBNjQOo5cSi6ToNNK3ko2JnX5VodNbTaQau8biJfCWRmE5Fpk3pDoxOtr4xyOIg0O2j9Xf1n+E7YH1prqyxid9XqrQ2PrY7Qw93BVYJ1B207lIlafvWi9dXR+52nHGxl5Ctt1ifUJbdGfB9aXxsV/0eQo46egv4FzzqOcjQRym4AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TAVI #2 — Redo-TAVR（TAV-in-TAV）最佳實務共識

**Redo-TAVR Best Practices Part 1 & 2 — Heart and Valve Collaboratory.** *JACC Cardiovasc Interv* 2026 Jun 24.
🔗 [Part 1 DOI: 10.1016/j.jcin.2026.06.003](https://doi.org/10.1016/j.jcin.2026.06.003)

- 依**首植瓣與第二瓣高度（short/tall）組合**系統化 redo-TAVR 規劃
- 核心：**冠狀動脈阻塞風險**、瓣葉外推、對位、未來冠狀動脈通路、植入深度

> 💡 第一代 TAVR 進入退化期 → **首次植入就要為再介入鋪路**（瓣膜選擇、對位、冠狀動脈高度）= lifetime management

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAACT0lEQVR4nO2bQYrrMAyGP9WGLh3oAeYozg3emeZmzVF6gIFkWXDQW8hu8roYZniEGiovSpN+ix/Eb0m2KsoP13T6KQmOOuroCRapa2wv7ds0QPspHinA0d+gQVVVFVgFAP0cViHfImRVVZ270eooVPcsERkB8u2sMqaCOW88XICjP1rxn6dQmIavqKS7wHIpxwtw9D9QGQkqI8D0Ub5FjxHg6DfLvLWV8QprZBq+2rukwHKcAEd/ia5W9wEg43LWmreWCJOIiAzdaH1vFN2tGbAScQ76vK4v1+roySpB67dSAViFaVhl/0M3Wt8cpbZaSVWvBIVUUNUCWPCa1dxbr0dpu16BPIdWbqT2mH0n7AhtPiKYt7aURTbTFfSaPFpdoNTaIqnZSq/tg7yZzr3VB9pqwhmzkDkqW95SrSHzvNUH2rz1eLwSVK+t1Kguc2/1gVqVQZ5r3GpF0TbGGijPW32gbJlpux2pySup562+0AjLYKeDOkkoTH8UybpGIa0RCCp2Gv9yrY7WfuvRGLetr+w2QfdWL+g+b1nIeOq3PG/1g9Zo1Wp9329th7xY7/xyrY5GO60AUBaQPF+KZAWBUGAZpBetjp72M0+pjtLYFA206SdrlnvQ+uZoxCwEWOk3fSiSb2eF5YKyhMIkwWvCHlC76ZdHyABQuIvWgbWAHCnA0V9Ha1vKIpbGhFSiPmYMO9Dq6DMqYyqIDLWqr4OGyfNWR2i7LL4L1m/dIvop511V343Wd0b3Z/AWmVRvTOoIAMHPMrpBxf8R5Kijh6B/AbPExXogDsX2AAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TAVI #3 — TAVR 後冠狀動脈疾病進展（QCA + QFR）

**Progression of CAD After TAVR: QCA & QFR.** *Catheter Cardiovasc Interv* 2026 Jun 25.
🔗 [DOI: 10.1002/ccd.70704](https://doi.org/10.1002/ccd.70704)

- 92 例 TAVR，術前後皆有侵入性冠狀動脈攝影
- 以定量冠狀動脈攝影 (QCA) + 定量血流比 (QFR) 評估 CAD 解剖與血流動力學進展
- 比較自膨式 (SEV) vs 球囊擴張 (BEV)

> 💡 以 QFR 追蹤 TAVR 後冠狀動脈，有助釐清「併存穩定 CAD 是否／何時處理」並呼應 redo 時代的冠狀動脈通路考量

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAACZUlEQVR4nO2bO27rMBBFz4QEUlI7yFKknQXZmbQU70AsA1C4ryBpO68I7MIxAQ8LQxZPcQGC85eJG9f2disJjjrq6Btka2vJZvXtZhG2CfpWHESrowRJ0pVJtCUVmE8RZknS/lgBjt6FttuTSr1MdWv7KNSbtzxcgKP3ozmiNUnSycw+T/GvBTj6+/pxIEkY6YgiCbYp/IEAR+9GJRWAw5j3IFs4rDovkqT14QIcvRk9rHmr/C7Ikfo0nyJsZmY2DaP1tdEI6RwN5sO0TRik7xpqXOfOT9fqKNIeBNXq9Z95ByCIWQWtBGl9ulZHkfZ2ZFqT1B3V+QQJartP1+pot4TV9MUicixG2hEclbF6bk/X6ugb5IjZFCTthwFHdVlmE2gFpJNXnoZAr43gXD2YJKm0Dam08pNbwqHQmlbNp3PlaTrMbAqqRd6htL4umr7NPncw+/g2SJItOQJJ+g99jABH70BrOmxWfdSazfQ1BUE2Y95Bq0cZY6D0Zkno9yhJLQejRxlrcr81EjpfwoqTGdt0PsZUsOXxAhy9Ec2x2r9Wxr1KjGl/a2ljBK0vjp6vkHq03uP22jGe9yCP4EdBe7MklWYO11Tqu9YnAc+3hkHr3Wprh8u50UqEtCc/rSHQy8xT91Fa83uNCW3BI/ix0MvM09FakttH6cE70FKyIbS+NlrnMgxCgVSiyGBgMO+TAaGW5AfQ6ugPNEf6NEaBbQrSymFegx8TDdKXxTb4SZ+iseXPBDj6++qNEbW0qgX0vYHc6oQewQ+DXmaezGzJsbUf5/2w60L8EFpfGzX/IshRRx+C/gMnkIm3U4zMzAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## PASCAL × MitraClip × TriClip
### Drake 的 TEER 操作面向

---

# TEER #1 — REPAIR：PASCAL 小瓣口（見 Pick #3）

**REPAIR Study.** *JACC Adv* 2026;5(6):103014.
🔗 [DOI: 10.1016/j.jacadv.2026.103014](https://doi.org/10.1016/j.jacadv.2026.103014)

- n=**1,189**；3D-MVOA <4 cm²（28%）vs ≥4 cm²
- 技術成功 95.9% vs 98.2%；**1 年死亡 13.0% vs 13.6%（NS）**

> 💡 小三維瓣口非絕對禁忌，但須精算殘餘瓣口、監測跨瓣壓差以防醫源性二尖瓣狹窄

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAACz0lEQVR4nO2cS4qkQBCGvxiFXuqN0psNfaS5gXWUOsBAumxQ/lnkQ7thpmjGtishciFqfYuAn8h4pWXiM+v241M4OO+881/KL5bXxGY2ATYBsPSJKb/319jj/Ml8J0kSLD16HTeDxQyGtyQ3QZIUr7LH+bP57Jx0IkTQPKzYRCe9jpBcfLrQHue/ireJTkAnzcC+SX+TPc6fyA9rvrmNYBObEeI32uP8f/PJOw9F0s26lXDvV1jG8nIQsFxhj/Pn81tKj9NeHGLNn+mU7m5mZjZeZY/z5/F9dk4Als10GztgWBHsl8vscf5cHimW+ihEkLSSInGIOZ0mpHeS5mez3/kHK9e1w5qUhkHKWpIfC+L6tseTWxupKiruPNdKOHl37JSaHK5vY3zSV9Kat+ZQtUzCDyupEg6xc32b48v+zPtYW1fQyi6369saf0ioNKeoS/bVFI4h6UvqaT2b/c4/WCX+QulfdSIoy13cuVNW/9nsd/7BkiIpwuYiqUpbU+estMffBvnU37AQRwxKpzLErYelL6F4MeT9yUb5NOvNBa9NS1/GhcObcRs72U+t2HSVPc6fyKf8qmRV+aKZXARrHko7y/OrFvlDQyNnUEOueg+/KuL1b5t89t+9FkrHdWKd75eayfPnJvkqbVc6GGm0APto3/uT7fJ1qlAnRIMOneg9HPt8oWU+3F8k3ctZq6A9CBf1kzs/qf3O/22lDkaeJeQhMJT8uVB19342+51/yO8b8t2MOim0qQz5pViP0D6h/c7/a5X5Ee925aF2KtNgyeNvw3z9fgFyJJ4BzctLduyZzQh399/2+EN9lPw3pEl/vYuF8/q3Rf69vnUqGI+F075Ju76t8f2HZ2PYerF0q4VfmxHmDaAenH02+51/sI7nY+uF8hHS4SSl969a5Htgs/ywjAi2njDnd2IxYPhtuo3xAnucP5c3/38G551vlv8DSb5QN2CLT50AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TEER #2 — TR 的 CMR 右心室—肺動脈耦合預後

**RV-Arterial Coupling by CMR in Tricuspid Regurgitation.** *Circ Cardiovasc Imaging* 2026 Jun 25.
🔗 [DOI: 10.1161/CIRCIMAGING.126.019717](https://doi.org/10.1161/CIRCIMAGING.126.019717)

- 631 例三尖瓣逆流 (TR)；CMR 計算 f-RVSV/ESV 耦合指標
- 截點 **≤0.57** → 校正後 **HR 2.36**（1.27–4.37，p=0.004）
- 在輕、中、重度 TR 各亞群皆能分層長期預後

> 💡 TR 預後不只看逆流嚴重度，更看**右心室能否代償** → 為 TriClip／T-TEER 時機選擇提供生理依據（趁耦合 >0.57 前介入）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAACaElEQVR4nO2bTWrkMBCFv4oEWcrgA8k3y5lyA/sofYABaxlQ82YhuX+yGNKLnhaktDAt/C0eFFV+VVKb+OHa3n5KgqOOOvoGxfpa2q+ILcUMgONVHESrowRJkiCp1UWtSbIFIEuS9ucKcPQhtGcPZ5NUMZuAzSIt85anC3D0cbRE2CaQThFJ9X8LcPTfK37bGxhAgG0Jd+F6uVZHG3rNI61JkvRl5B0gSVqfLsDRH6Pn5vuAIPs4RWwp791lbGbWPmNjaP3dqN12x2VuGWZwXwTBu+NB0BKBEjGbzsZmZmRVbLkmXfF+awg0QvpqCSbKhGWBbdOfCGWWQUu1EbQ62gyG1tS7494JE9T8xkqQtAdpfblWR+mhSBWt0B83a4cWMo/W69Heb+VTbN7C8j4BZa4GIJKAtD9NgKMP5hbQS1+9bAFSpTddnlvjoEFaOZt97EG2tG2QdIrchmwIrb8bPTxh2mGbdiDVNnuy/AnaLIhtck84BNpcBrk9usto2/ZWOtzhy7U62j1ht/H13iIeIXNPOAhKP4iEllFX00GWLknn0RoCPaKVah/Et3KY6uXY+DAdHq3XoxHKBPnzXQahjZqAILb+25T3+WkCHH3QEwqgIsqMoEbLO1je53qdyw+g1dHbdjjvV9PRi2Brtfy7NQgauZxlGalGy2vF2qgJECVUoD5NgKMPo/3OU3lXO9+i3Sc823Hm5edb46Hpy64m0JbUKyJZnltDoPd3noKulVCbgeB8FMuXa3W0od/vDuZTj6LZdEyjRtH6m9EInI8mq8xVlIk22s0CtiXi51ujoOb/CHLU0aegfwFnCIEvozz8jwAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# TEER #3 — 重度 LV 功能不全的「保護式」M-TEER

**Protected M-TEER With Temporary MCS.** *JACC Case Rep* 2026 Jun 24.
🔗 [DOI: 10.1016/j.jaccas.2026.108783](https://doi.org/10.1016/j.jaccas.2026.108783)

- 46 歲缺血性心肌病、LVEF **26%**、重度次發性 MR
- 擇期 **Impella 5.0** 支持下計畫性 M-TEER（2 枚 XTW clip），術後逐步脫離
- **3.5 年**追蹤 NYHA I–II、無 HF 住院、移出移植名單

> 💡 重度 LV 功能不全 M-TEER 的風險是**後負荷不匹配**；暫時性 MCS 護航可緩衝並爭取 GDMT 上調時間（單一案例）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAADC0lEQVR4nO2cwY3bMBBF34QE9igBW4BLkTpISUFK2g6sUrYD8WiAws9hKNkbJHGCOI4EzBwEy3yHD3A55Pyh18SfxPTpj3AIPvjg/ylfrMXI4h+gmDH1YNbDOp6foyf4B/NJkuSJWueu+qwyzNtDkjQ/S0/wj+bb4iwZhveMpIqNgL724Et8fKKe4B/F5w9vqRqdMEiC0gPk+kw9wf9LfjGGeU3SY1dpWfl/6Qn+b3lfv2uRlCqwZFFyhfIq6CrQCSjP0BP84/nt1AzYWF5kX+Y2bGPJMJmZn7l2qT/4n0duixOAsvgkM50qgotp6hO3Fsje9Ad/J6Q5tQkcpC0hVxjmJH9sozrvTX/wd8JPUIOuZ6kkaU7Suavo3G1zTor5PRy/rt9tBn1qSfKTtOb2XazfQ/IZuovvugKw4VwxuhlBzUZ3McFiUF7r/vQHfyfUwssgX7qelQe1/CzN0Ab2pj/4X0debaokYMnQzRjkKkqPgUHztJ6hJ/jH80nSvJiNJOnMYgy6GNNJvglDye5p7VN/8D8P96+MTjBZqlBeZJRXtaULMLy9Yj7Te9Mf/J3wzVVrrXstl/CCCPCHH6z3pj/4u3wnmfWL6QxuXXmncKuZbOxau3CX+oP/RbT+wvR5xiABJDGdam7lkkDT+CIj9t8D8mt9tBpW63ff2R2018jPB+MzrSqq2PCegW7GW4PTuNiapLcW4t70B38nVn9Sq6sxt/5+MyQB8IFYv8fjbx3mLSFfB5qJxfYnsDf9wd+JtTS6rZSaK7l5lpKiv3BM/mOHqLIm5LodvFYu/Ocj8lt/QbrpFA4fPt1k75jfg/G3NyRbw6hl5Zutd5hj/z0on2m3JsEoPTa8v8iGt1zd3wDQ9WLW7vQH/zt8+/0CwNSDl8Mj4I0l67d1vk/9wf8u772Er2amc8mYnaofwfym7O71B/8x8nfvNmgxDVqy0dWs6XNy61kQ/vPx+LU+0g8OVMDVuor695B8xi/PAbQLObDeuUsVSq6aThfT1M9P0BP8Y3mL/88QfPCH5b8BALoh9hEOSrAAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

<!-- _class: small-text -->
# 其他值得一讀（1/2）

| 研究 | 期刊 | 重點 | DOI |
|------|------|------|-----|
| **HF + CKD 疾病序列與 GDMT** | *JACC HF* | 最常見 **CKD-first（58–61%）**；腎臟科就診僅 4–8%；GDMT 偏低 | [10.1016/j.jchf.2026.103179](https://doi.org/10.1016/j.jchf.2026.103179) |
| **淋巴瘤存活者 CVD 負擔** | *JACC Adv* | n=36,334；CVD 住院 **HR 1.58**；持續 ≥10 年 | [10.1016/j.jacadv.2026.102860](https://doi.org/10.1016/j.jacadv.2026.102860) |
| **孕產婦女性 CVH（LE8）** | *JACC Adv* | 孕婦 LE8 最低（62）、hsCRP 最高（4.68） | [10.1016/j.jacadv.2026.102934](https://doi.org/10.1016/j.jacadv.2026.102934) |

---

<!-- _class: small-text -->
# 其他值得一讀（2/2）

| 研究 | 期刊 | 重點 | DOI |
|------|------|------|-----|
| **Medicare GLP-1 可近性** | *NEJM* | 政策觀點：給付 GLP-1 的「通往無處的橋」 | [10.1056/NEJMp2605694](https://doi.org/10.1056/NEJMp2605694) |
| **智利食品標示法與幼兒過重** | *Lancet* | n=321,597；女童 −2.85%、男童 −2.40% | [10.1016/S0140-6736(26)00651-3](https://doi.org/10.1016/S0140-6736(26)00651-3) |
| **經導管二尖瓣 Valve-in-Valve** | *Circ CV Interv* | 編輯評論：尺寸選擇與充分擴張很重要 | [10.1161/CIRCINTERVENTIONS.126.016982](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016982) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構介入救援 × 5
### TAVR / TEER 疑難情境

---

# Case #1 — 重度 AS + 急性髖部骨折：TAVR-First

**Expedited TAVR-First Pathway.** *JACC Case Rep* 2026 Jun 25.
🔗 [DOI: 10.1016/j.jaccas.2026.108988](https://doi.org/10.1016/j.jaccas.2026.108988)

高齡男性重度症狀性 AS + 急性髖臼骨折。Day 1 經股動脈微創 TAVR（清醒鎮靜）→ Day 2 髖部修補 → Day 4 出院，1 年完全獨立。

> **為什麼值得讀**：重度 AS 病人非心臟手術麻醉風險極高；**多科協作 TAVR-First** 先穩定血流動力學再修補骨折，提供可複製路徑

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAAC50lEQVR4nO2cTW7cMAxGH2sDXcpADpCj2DcreqTeYHyU3MBaDqDB14Xon7RIgqCTqQVQi8GM/RYECFLkJ2pMfGbN3z6FQ/DBB/+lfDZfE2BmZpDNmAcwG/yZmfWPsSf4O/OdJEnAzSCV6lXGZfuQJC2Psif4e/MenLmH8aVHUsEmQD8HqCE+PdCe4O/F938+mIeuGHSCPAD05ZH2BP+1vKSCLqlgUyp4Vv5/9gT/b3yN37VJ6grkAZH7AvlpfZ4E5EfYE/z9+Zt51QzYRCf7sfhrmwBmM6s11yntD/6dpcNagLr1Jqlmai3dkbiczf7gP+Rz7x3ulCRGXQ24mU35uw797/Qoe4K/I+8V1LjAHr81ai+poEuSIBV/EfHbGM8qbXTyn0snXei0+tzdXUWO8G9j/KH/9WI5FYy0ICi9ka6mKmzlp3I++4P/kM890nJbVeYBdMFL5xrJsClZJ7Q/+PeWtLgb6zctXU3XR2kjeQqP/Nwav+2wsHdFjFpLq3EBqmtT7L/t8kmSXnqYh06Qv8um7JoH4wKueZzV/uDfWGt/9Corj9oaInw79sL6bPYH/yGfJObhZtJyM+ZnqZ4Ubl2vTcmPC09pf/DvLa+v9gpqFTRqY1y7XqL/bZQ/KBi6pPWod8/PLnfgP8O/jfE9PpVzNcaXHkgLRn4S8+TjOsCmfpzN/uA/WIfWqHZAqVC96qnZ3zJGfdUg74LGuH4cBCtXncsqYkX/2yC/CVbUqRw/5t2VjvX8N+qrJvlj/LIPXO2e3rhL1FcN8n/Pb6TC7m6P3039CP82xh8nJMd1dNKl523rdXdHfm6PP0xY7bG6PtubYAj/Nsz7/QWA+flquyDpB8PDFufntD/4t9br+ws3g9SJ2UDkASOVXuSnYuOvmN9ojz8c6O8Xyjw1H+brYj62Uf7V/ns41e/2qwur+hH+bZBf9WcA8oCNL32pcrRfV+mL5ueraR6WB9gT/H15i/9nCD74ZvnfSqdeJYUwD78AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #2 — TAVI for AR 後平臥呼吸困難—直立性低血氧

**Platypnea-Orthodeoxia After TAVI for AR.** *JACC Case Rep* 2026 Jun 24.
🔗 [DOI: 10.1016/j.jaccas.2026.108397](https://doi.org/10.1016/j.jaccas.2026.108397)

82 歲女性因重度 AR 接受 TAVI（JenaValve Trilogy）。術後頑固低血氧 = 平臥呼吸困難—直立性低血氧，經卵圓孔未閉 (PFO) 右至左分流。經皮 PFO 關閉後血氧恢復。

> **為什麼值得讀**：矯正 AR 降低左側充填壓 → **揭露潛伏的心房間右至左分流**；新發姿勢性低血氧應評估 PFO（可逆）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAAC80lEQVR4nO2cQY7bMAxFPysDWcrAHGCOIt+gZ+0NrKPkAANYywAyfhcibU/RmXRQ17UBahVHb0GAIUV+yhHiKyt/+xIOOO+88/+UL6JraJ86iIiIbvSA7XfH2OP8znwgSRKIJBAryAlA7gGkCUAi2b47pf3OP+M1ODELR8wCIBCJJFA6tEgeDrTH+b34bvtQeiBNoCA+BOlHDwL1UHuc/5d8oAxFBGkKRO6Dxe//ssf5v+Wb96xJmoUAISgvFYhvQsQKIBJAOcIe5/fnZ9GCucWvBWy63/Qxi1bS57Tf+Y9Xp8EJACizML9WIPcQID4EwBrdR9jj/L48yCmQnIJ6sfVCrABi1f5o5caz2e/8k9XcOQLgGLmEqvqcY6xo7k6k+/dyPDR049IGRZpXJ3skq/0Ozma/80+WSVcaphyxZmp1cnOt5+cr86WDDOXGVlUlkshyI/JrNTk61gPtcX4f3vIzAjm2U3eppdpxbOq0n79X5C35mgfbl6mdyVp4wUQO9+9l+SLCsXSwIdJDOBbLymkCfH50SX6Tn1tBNUK7ovWx+Xf0+L0g36GpzqUX5v4NQJxgU8EeuovaCeIR9ji/L69icx5CFeBGSXcBgFBFhctQkb+/mUh5Nvudf7JWfbJl4E2vi6XIapWW97/X402XWnoh1TfWOztWX7l/r8hv9EmVmadg8wWYV5fbWe7fC/ImPYv0gci9fWpNMGZB7mfRTviE9jv/2dqIUzoVNFUjLVOFVYT2+L0Yb7rFeupafm4zQ911/16U3+iTdhJrrdzyc1qm/64/X5HfRKjeZbebHGu55frVdfkOQGgFVhM08msF0jh3kkaAKABRgo3/z2a/83/C6/sLRd86alefs9xa/SzSz6Ka5Tntd/7D9W6+8F7QiMs7SauSdTb7nf8KPwt575ZLOrMg3fXFJL1JeW77nf89vwpWMiBQhvhoCXnTCY8H2uP8XnybD+pDeaEAc5sUSuL8y249n/3Of77E/5/Beecvy/8Eiw9Sd1JmgK8AAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #3 — 原生瓣 TAVR 的改良 UNICORN 瓣葉撕裂

**Modified UNICORN Leaflet Laceration in Native Valve TAVR.** *JACC Case Rep* 2026 Jun 24.
🔗 [DOI: 10.1016/j.jaccas.2026.108902](https://doi.org/10.1016/j.jaccas.2026.108902)

電燒穿越目標瓣葉 → 球囊瓣膜成形 → 大型非順應性球囊撕裂瓣葉 → 植入球囊擴張瓣，預防冠狀動脈阻塞。

> **為什麼值得讀**：將電燒瓣葉撕裂從 valve-in-valve **延伸到原生瓣 TAVR**；高風險冠狀動脈解剖的主動式保護新選項（影像導引至關重要）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAAC30lEQVR4nO2cTY7bMAxGH2sDXdpADjBHcW5W9Ei9gX2UuYG0DKDg60I/cRbTdNBMagHkwrCjtyBAkCIpKiY+I9u3T+HgvPPOfykfrciZa36BaMY2g9kMdX18jT7OP5kfJEnKb+uUslVZQntIksKr9HH+2XxxzmjG8j4iKWFnQD9n8oKdX6iP88/ix7uvIbGdh2QwCOIMMKZX6uP8V/JXgymRg/R5SpSo/L/0cf5f+ey/tUgaEkRDxDFBPNXfJwHxFfo4/1x+JHttFVvCKdkSTvXzF7BlYHiBPs4/l0c7CUDeeidJUkJrza6zrEfT3/kHIoWhhOFFEkyJ/FjCoPxoq27f3vhcC7GEm6UHSaFUwlqnZnMGt293/M6q+bGEQVrzW1nNiPtvj/xYnbMk0YKEMQUEaTSmiymnYPGUjqe/8w/5aCaF0sQysxGtgJ0h51dA62QdUH/n/yRlr2WQVqAmVIP2rY2pdaePpr/zD6RsrgFKVRSARTW1ygv54MH33/74ml9NqhbkvioK1ErJ86sO+dxhrk487PyXFqS10uL40fR3/oGUo996lrCPys2dW7vD7dsbz62XQWtNFnNLNSrj8blTPvevSq+5Omzuae06WRl1/+2VN5sH2Y9wNZguZuf4XVq5mtlb7X5kmx9Tf+c/lF2vOQfkAGXDzaEZcsz2/bdHftffKAbNvYyWU9dDwpJuHU1/5x/IbYetO3GthMvBUp2u9PyqR35X+lZfhVv+XFOr0ol2+/bG389v7GvdXdV7Oxh2+3bG7yckS9e5tZ7b1rsE33875Ufy1CRgxJNY3kdseR+T8m+AiG0E72j6O/83fLm/ALDNJTTbGZDC1czm5ufH1N/5j+T+/sLVYApoMxBxxpjSKOIp2fLL5zf64/fzV+1CWelV7ebrfD62U75O0KklVLVXVdbbp9e/PfJ39xfinFMrmC5Gua4yJm1vF9M2hxfo4/xzefP/Z3De+W7530Pjec6Ado/wAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case #4 — 退化 ACURATE Neo2 + 高風險冠狀動脈的 Redo-TAVR

**Redo TAVR With High-Risk Coronary Anatomy.** *JACC Case Rep* 2026 Jun 24.
🔗 [DOI: 10.1016/j.jaccas.2026.108611](https://doi.org/10.1016/j.jaccas.2026.108611)

76 歲男性曾植入 27 mm ACURATE Neo2，因人工瓣 AR 就醫；RCA 開口位於上下冠之間 = 極高阻塞風險。以 26 mm SAPIEN 3 行 redo-TAVR，CT 精算避免阻塞。

> **為什麼值得讀**：呼應 redo-TAVR 共識 —**首植瓣設計決定再介入冠狀動脈風險**。注意 **ACURATE Neo2／Prime 已於 2025/5 停售**，但既有植入者仍需 redo 規劃

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAAC3UlEQVR4nO2cQY6kMAxFnwekXoJUB+ijhBvMmeZIcwM4St2ALEsK8iwcAvRIjVpTXUMke4GgeAtLlhP7O5QoX7Hpx5dwcN5557+Vj5JtYBGILTIAEFtj1vfta/xx/sl8o6qqCvFNmd4fAlEEuofIABBUVXV+lT/OP5vPyQkQ7i06dgkZaFR/9WApPrzQH+efxbeHp0WgU4Bmrbtim17pj/PfyHcJW4anHmRgEcL8H/1x/p95y999kxR7NNzbBLEHukTO6fgKf5x/Pr9YeQzxTWWgURnsZaMyxBYmERHpX+WP88/j23XDBcvQqW+wlRoSSjxm99X8d/6UL23uAED3EKZ+ERmsE16sMfb8rZK3gkpHwLrgkUahO9xZ69up6ng1/50/MVVNsDVEYW5yaMMMqnOjqnOjJnJ4fCvjW4g3lfD7Ztus0CUkKCgoQvcQnQYE4i1dz3/nT2xLzjVhD6+DplWf9PytkC8BbVTHTpUwN3axwAMW34xczX/nT8x22NEe1rugiRzudXfW0eurCvmiPzcJYi8EBaZ+VqEDJfbo9HNGTNO6mv/Of24tmMx8Q9YgQ5iXdj9aiGJKx/X8d/7EbPQbNK0rdVfmRV0id0qa1sbpav47f2J5tF/22rCKHPli84WyCV/Nf+dPbKuvttTd3WV9A/D41shn/Wrrf0uTlGtqUyqLenk1/50/sYP+nHa/baN91yfr5Q8K81xO2lGiOsN+5nA1/50/sQ9h/GA5qlZ9eXzr49e1WEtXtJXO2yG7EniPb2U8+2ydG916odwz7ZRor5/r4/cDo6I6b9LzOgn2/bdSvsVUSUAAJNzFJsFKvOVKi2gfrrj+XB3PtvjmTbhLR82ycL7/Vs83+SMkooiO8U1F3vMibSdlL+6/85/zi+gISD4EvX2/sEj+Euna/jv/l2V9Q0uHy7pcb0V0Xr19fa6PP9TPM+TzOeXURpkZ+vmNKnnx/2dw3vlq+T8B9U+zL3if6wAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #5 — 鏡像右位心的退化性 MR TEER

**TEER in Mirror-Image Dextrocardia.** *JACC Case Rep* 2026 Jun 24.
🔗 [DOI: 10.1016/j.jaccas.2026.108347](https://doi.org/10.1016/j.jaccas.2026.108347)

76 歲鏡像右位心女性，前葉連枷致重度退化性 MR。以 2 枚 **MitraClip XTR** 行 TEER，採**修改的跨房中隔穿刺與反向導管操作**；術後 MR 微量、無狹窄。

> **為什麼值得讀**：罕見鏡像解剖下 TEER 仰賴術前規劃與反向操作的心智轉換；證實 dextrocardia 退化性 MR 的 TEER 可行性

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAAC30lEQVR4nO2cS27jMAyGf461lwEfoEeRbzbokXoD+yg9wADSsoCMfxakH5lFg6KJaw3IRRBH34IAQfHpCPEVmX99CQecd975p/JFTEYAIiICFBHMPSDS228iEs7Rx/kH8x1Jcr2oY1WrIuXtgySZz9LH+Ufz5pxFhHwPIFkhIwC+9tADGU/Ux/lH8eGfZ0EkBOgIlB4AQj1TH+efy6v/TrFCxlhht/LP6eP893j13zX2dhXAIkQJFSgDgVgBRAIoZ+jj/OP5RSxrBiAjOsrvbMcylgDMIqI51yX1d/4T4UEyAA29kSRZwSkeAU5X09/5O0Lmzq7nRBKJFXorp9xRP7ZTt29rvGVQKe+W7kjmjpyi+a8FYXRu3+b42wzZHJaTfjObq+Hdf1vkAxBrAOKfQGAR7V8hZhCoQRA/xA7KUK+nv/N3ZPVQAJpaoaPeymnPrzLAye/nBvlj/J1gZoQF4Q2KXA1/Nf2dvyPH/FlDL7C7rs4XNp92+7bG3/SvCoCUhyooAwUQaHRObwNELX01/Z3/XAKsITlUSW8ALMn6EGi7svTg3EOR6+nv/B3ZR7971Wu3cqRVSlu7w+/n1njrT05xmwJqV6Oa4bXqhde/jfI6y7cKSB0WsCbl3slS1P23PV7zK0lTDZZBxQwdDc6jtTsAbCnY1fR3/o5Y/XtTEFkQ5urO0AP33/b4NavapoI6UFgPzPD76dX0d/6OmBmzea21Idf5L/btSs+vWuRvJ0TbwtWaP+9NSu8/N8nf7m/YNWxT/a3q3QfDbt/G+OP8N9Fm+cf5EbYlDo+/DfIBtjUJCMpQkd4CkN5Dpf4GgCiLnKSP88/g7f0FLMLXvqOMcX1/gXnR1Ul/P6VJ/rB1ZQs5a9V7zLRy5/Xv/8HLiEWQWCHyYvHXvsX6A/o4/z1+rY/W1djdV+18S6e9/m2R1/mvPZQeNgQ+zH9D5fzyIZz7fII+zj+WF/9/Buedb5b/Cx7fXmk9f2QcAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: lead -->
# 💎 Take Home Message

### 1. **Ross 手術現代標竿** — 12 年存活≈一般人口、自體瓣再介入 1.1%、PPM 0.8%
### 2. **雙葉瓣 TAVR 破裂可預測** — ABC 演算法敏感度 100%、特異度 89%
### 3. **PASCAL M-TEER 小瓣口可行** — REPAIR：<4 cm² 與 ≥4 cm² 結局相當（防狹窄）
### 4. **TR 看右心室耦合** — CMR f-RVSV/ESV ≤0.57，HR 2.36；為 TriClip 時機選擇依據
### 5. **重度 LV 的保護式 M-TEER** — 暫時性 MCS（Impella）防後負荷不匹配
### 6. **再介入時代** — Redo-TAVR 共識：首植瓣選擇決定未來；ACURATE Neo2 已停售
### 7. **藥物／族群** — 睡眠呼吸中止↑43%（finerenone 益處一致）；SGLT2i 或利 TAVI 後（HR 0.65，確定性低）

---

<!-- _class: small-text -->
# 完整參考文獻 (1/2)

**Top 5 Picks**
1. Contemporary Outcomes of the Ross Procedure in Adults. [*JACC* 2026 Jun 23.](https://doi.org/10.1016/j.jacc.2026.03.173)
2. ABC Sizing Algorithm for Aortic Root Rupture in Bicuspid AS (SAPIEN 3). [*Circ Cardiovasc Interv* 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016918)
3. Small MVOA in M-TEER: The REPAIR Study. [*JACC Adv* 2026;5(6):103014.](https://doi.org/10.1016/j.jacadv.2026.103014)
4. Sleep Apnea in HFmrEF/HFpEF: FINEARTS-HF. [*JACC Heart Fail* 2026.](https://doi.org/10.1016/j.jchf.2026.103187)
5. SGLT-2i and Outcomes After TAVI (Meta-Analysis). [*JACC Adv* 2026;5(6):102884.](https://doi.org/10.1016/j.jacadv.2026.102884)

**TAVI Section**
6–7. Redo-TAVR (TAV-in-TAV) Best Practices Part 1 & 2. [*JACC Cardiovasc Interv* 2026.](https://doi.org/10.1016/j.jcin.2026.06.003)
8. CAD Progression After TAVR (QCA/QFR). [*Catheter Cardiovasc Interv* 2026.](https://doi.org/10.1002/ccd.70704)

---

<!-- _class: small-text -->
# 完整參考文獻 (2/2)

**TEER Section**
9. RV-Arterial Coupling by CMR in TR. [*Circ Cardiovasc Imaging* 2026.](https://doi.org/10.1161/CIRCIMAGING.126.019717)
10. Protected M-TEER With Temporary MCS. [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.108783)

**Honorable Mentions**
11. Cardiorenal Pathways in HF + CKD. [*JACC HF* 2026.](https://doi.org/10.1016/j.jchf.2026.103179)
12. CVD Burden in Lymphoma Survivors. [*JACC Adv* 2026;5(6):102860.](https://doi.org/10.1016/j.jacadv.2026.102860)
13. CVH in Reproductive-Aged Women (LE8). [*JACC Adv* 2026;5(6):102934.](https://doi.org/10.1016/j.jacadv.2026.102934)
14. Access to GLP-1s for Medicare Beneficiaries. [*NEJM* 2026;394(24).](https://doi.org/10.1056/NEJMp2605694)
15. Chile Food Labelling Law and Childhood Excess Weight. [*Lancet* 2026;407(10548).](https://doi.org/10.1016/S0140-6736(26)00651-3)
16. Transcatheter Mitral Valve-in-Valve: Sizing Matters. [*Circ CV Interv* 2026.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016982)

**Case Reports**
17–21. TAVR-First (108988) · Platypnea-Orthodeoxia (108397) · UNICORN (108902) · Redo-TAVR (108611) · Dextrocardia TEER (108347). [*JACC Case Rep* 2026.](https://doi.org/10.1016/j.jaccas.2026.108988)

---

<!-- _class: abbr -->
# 縮寫對照表 (1/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| AS / AR | Aortic Stenosis / Regurgitation | 主動脈瓣狹窄／逆流 |
| BAV | Bicuspid Aortic Valve | 雙葉式主動脈瓣 |
| TAVR / TAVI | Transcatheter Aortic Valve Replacement / Implantation | 經導管主動脈瓣置換／植入 |
| SAVR | Surgical Aortic Valve Replacement | 外科主動脈瓣置換 |
| BEV / SEV | Balloon-Expandable / Self-Expanding Valve | 球囊擴張瓣／自膨式瓣 |
| TAV-in-TAV | Transcatheter Valve-in-Transcatheter Valve | 經導管瓣中瓣（redo-TAVR） |
| TMViV | Transcatheter Mitral Valve-in-Valve | 經導管二尖瓣瓣中瓣 |
| PPM | Patient-Prosthesis Mismatch / Permanent Pacemaker | 病人—人工瓣不匹配／永久節律器 |
| CAD / RCA | Coronary Artery Disease / Right Coronary Artery | 冠狀動脈疾病／右冠狀動脈 |
| QCA / QFR | Quantitative Coronary Angiography / Flow Ratio | 定量冠狀動脈攝影／血流比 |
| MR | Mitral Regurgitation | 二尖瓣逆流 |
| TR | Tricuspid Regurgitation | 三尖瓣逆流 |

---

<!-- _class: abbr -->
# 縮寫對照表 (2/2)

| 縮寫 | 全名 (英文) | 中文 |
|------|------------|------|
| (M/T-)TEER | (Mitral/Tricuspid) Transcatheter Edge-to-Edge Repair | （二尖瓣／三尖瓣）經導管緣對緣修復 |
| 3D-MVOA | Three-Dimensional Mitral Valve Orifice Area | 三維二尖瓣瓣口面積 |
| RV–PA coupling | Right Ventricular–Pulmonary Arterial Coupling | 右心室—肺動脈耦合 |
| CMR | Cardiac Magnetic Resonance Imaging | 心臟磁振造影 |
| LVEF | Left Ventricular Ejection Fraction | 左心室射出分數 |
| HFpEF / HFmrEF | HF with Preserved / Mildly Reduced EF | 射出分數保留／輕度降低型心衰竭 |
| GDMT | Guideline-Directed Medical Therapy | 指引導向藥物治療 |
| MCS | Mechanical Circulatory Support | 機械循環支持 |
| SGLT2i | Sodium-Glucose Co-transporter 2 Inhibitor | 鈉—葡萄糖協同轉運蛋白 2 抑制劑 |
| MACE | Major Adverse Cardiovascular Events | 主要不良心血管事件 |
| CKD | Chronic Kidney Disease | 慢性腎臟病 |
| PFO | Patent Foramen Ovale | 卵圓孔未閉 |
| UNICORN | Undermining iatrogenic Coronary Obstruction w/ Radiofrequency Needle | 射頻針電燒瓣葉撕裂 |
| LE8 | Life's Essential 8 | 美國心臟協會「生命八要素」 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**
心臟內科｜結構性心臟病介入

*本文件為讀書會共筆之教學整理，*
*僅供醫療專業同仁臨床教學交流參考。*
