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
  section.lead h1 { color: #ffffff; font-size: 2.1em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #8ecae6; }
  section.lead blockquote, section.lead blockquote strong { color: #2d3436; }
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
  section.small-text { font-size: 0.78em; }
footer: '謝慕揚 MD, PhD, FESC | Disorders of Telomere Length | 2026'
---

<!-- _class: lead -->

# Disorders of Telomere Length

## 端粒長度異常疾病 — 短端粒 vs 長端粒的兩極表型

**謝慕揚 MD, PhD, FESC** ｜ 讀書會共筆整理
資料來源：Schratz KE & Armanios M. *NEJM Evidence* 2026;5(7)
[原文連結 DOI: 10.1056/EVIDra2600012](https://doi.org/10.1056/EVIDra2600012)

---

# 大綱

1. 端粒與端粒酶基礎生物學
2. Haploinsufficiency — 主要致病機轉
3. 端粒長度的臨床測量 (flowFISH)
4. 短端粒症候群 (Short Telomere Syndromes)
5. 長端粒症候群 (Long Telomere Syndromes)
6. **短 vs 長 兩極表型對照**
7. 關鍵基因與機轉
8. 臨床 Pearls 與老化／癌症啟示

---

<!-- _class: divider -->

# 第一部分：端粒生物學基礎

---

# 端粒為何隨老化縮短

- DNA 複製機器無法完整複製染色體末端（end-replication problem）
- 端粒 DNA = **(TTAGGG) 重複序列**，作為基因體完整性的緩衝區
- 縮短至臨界閾值（< 100 bp）→ 觸發 **DNA damage response** → **senescence** 或 **apoptosis**
- 端粒長度 = 體細胞與幹細胞複製潛能的「時鐘 (clock-like)」

> **對比**：短端粒 → 逐步喪失複製潛能；端粒去保護 → 災難性基因體不穩定，體內不容許

---

# 端粒酶 (Telomerase) 與 Shelterin

- **TERT**（催化次單元、速率限制）以 **TR/TERC** 內模板複製 (TTAGGG) 到 3′ 端
- 人類細胞端粒酶延長受**嚴格限制** → 預設隨老化縮短
  - 元件豐度極低；TERT promoter 在體細胞被沉默；僅 S 期窗口可近 3′ overhang
- **Shelterin** 複合體（POT1、TPP1/ACD、TINF2、TERF2IP）保護末端並調控延長
- **Acquired TERT promoter GOF** → 開啟轉錄，是許多癌症的端粒維持機轉，也可作為短端粒病人的血液「救援事件」

---

# Haploinsufficiency 是主要機轉

- 不同於多數 DNA 修復疾病需**雙等位 (biallelic)** 突變（如 ataxia telangiectasia）
- 端粒長度疾病只需**單一等位 (monoallelic)** 突變（TERT、TERC、POT1…）
- 原因：端粒長度調控**無冗餘**，缺陷無法代償
- Haploinsufficiency 僅影響約 10% 人類基因，卻見於**幾乎所有**短/長端粒基因
- 多為**成人期發病** → 臨床並不罕見（估計美國每年合計約 20,000 例）

| 症候群 | 基因座數 | 代表基因 |
|--------|---------|----------|
| 短端粒 | 16 loci | **TERT** (LOF) |
| 長端粒 | 5 loci | **POT1** (LOF → 端粒延長) |

---

<!-- _class: divider -->

# 第二部分：端粒長度測量

---

# flowFISH — 診斷金標準

- 臨床「端粒長度」= 直接測**白血球端粒長度**，以同齡健康對照校正
- **flowFISH** 為金標準；正常範圍已跨國協調
- **Lineage-specific**（淋巴球 vs 顆粒球分開）降低偽陰／偽陽性

| 情境 | 淋巴球 | 顆粒球 | 解讀 |
|------|--------|--------|------|
| 短端粒症候群 | 短 | 短 | 兩系一致縮短 |
| 髓系 clonal (MDS/AML) | 可正常 | 明顯短 | 顆粒球選擇性縮短 |
| 自體免疫／淋巴 clonal | 短 | 正常 | 後天過程 |

> **陷阱**：短端粒非專屬 — RUNX1/GATA2/LIG4 骨髓衰竭也次發性縮短；須合併臨床＋基因判讀

---

<!-- _class: divider -->

# 第三部分：短端粒症候群

---

# 短端粒：自然史（依組織週轉）

| 年齡層 | 表現 |
|--------|------|
| 嬰幼兒（最重端）| SCID (B/NK>T)、enteropathy、cerebellar hypoplasia → **Hoyeraal–Hreidarsson**（1/100 萬）|
| 兒童／年輕成人 | 造血幹細胞衰竭 → aplastic anemia（血小板低下 + macrocytosis）± T 細胞免疫缺陷 |
| 成人 (>40) | **Pulmonary fibrosis（佔 90%）** |

- 淋巴球端粒偏離同齡中位數的**嚴重度 → 預測發病年齡**
- 非後天骨髓衰竭中約 10% 由端粒基因引起（最常見遺傳原因）

---

# 短端粒：肺纖維化（最常見）

- 佔短端粒症候群 **90%**；其中 **IPF 佔 70%**（男性較多）
- 女性較多 NSIP / hypersensitivity pneumonitis；emphysema 與抽菸相關（<65 歲）
- **TERT 突變 + 一等親受影響 → 肺纖維化終生風險 300–500 倍**，近乎完全外顯
- TERT + 8 個基因 → 解釋約 30% familial PF、至少 10% unselected IPF
- 不論亞型皆為**單一、進行性**自然史 → 基因/分子評估或優於影像/病理

> 其他：T 細胞免疫缺陷（herpes/CMV）、非肝硬化肝病 + hepatopulmonary syndrome（10–20%）、早發白髮。**表型為區段性，無血管/代謝/神經認知老化特徵**

---

# 短端粒：病理生理與治療

- **幹細胞 apoptosis + senescence** 驅動進行性器官衰竭
- 慢週轉肺組織需累積 **"second hits"** → senescence → 纖維化/emphysema
- 缺陷為**細胞自主 (cell-autonomous)**

> **治療核心 1**：**避免免疫抑制** — 惡化免疫/骨髓、增加伺機感染；即使無 germline 突變的短端粒 IPF，免疫抑制也增加死亡（呼應 PANTHER-IPF）

> **治療核心 2**：**器官移植**為主軸；早期轉介爭取序列移植（HSCT→肝/肺）；移植前 NGS 評估 MDS/AML 風險

---

# 短端粒：癌症風險（反常抑癌）

- 整體惡性腫瘤**低於預期**（melanoma/肺/腎細胞癌見於「長端粒」基因）
- 僅兩種增加，外顯低、morbidity 有限：

| 癌症 | 終生風險 | 重點 |
|------|---------|------|
| 鱗狀細胞癌（口腔舌）| 5% | Dyskeratosis congenita 男性最易；源於 T 細胞免疫耗竭；醫源性免疫抑制者需監測 |
| MDS/AML | 15% | 幾乎皆 >40 歲；常併肺纖維化（半數死因）|

- 易出現過早 CH（somatic TERT promoter、PPM1D、splicing）→ 周邊血 NGS 可早期分層

---

<!-- _class: divider -->

# 第四部分：長端粒症候群

---

# 長端粒：POT1 為代表

- **過長端粒也會致病** — 較新的認識
- **POT1**（單股端粒結合蛋白）雜合突變 → 現已明確為**長端粒長度**驅動癌症風險
- 症候群式共現：melanoma、glioma、angiosarcoma、**PTC**、**CLL**、MPN
- 另 4 基因（TPP1/ACD、TINF2、TERF2IP、TERT promoter）連結同組癌症；TPP1/TINF2 與 ultra-long 相關
- 初始表現異質 → 幾乎皆 panel **偶然發現**
- 亦有 **genetic anticipation**（後代更早發、癌症更多）；founder mutation 如 POT1 p.I78T

---

# 長端粒：各癌別基因盛行率

| 癌症表型 | Germline 長端粒突變盛行率 |
|----------|------------------|
| Unselected cardiac angiosarcoma | 約 **30%**（POT1）|
| Melanoma + PTC（症候群式）| 約 20% |
| Familial CLL / PTC（4 基因合計）| 3–5% |
| 單一癌別中的 POT1 | 0.5–1% |

- 10,389 名成人癌症：POT1 pathogenic germline variant 盛行率與部分 mismatch repair 基因相當 → **被低估**

---

# 長端粒：自然史

- **年齡為最大風險因子** — 部分個體 70 歲前可達 7 種惡性腫瘤
- 皮膚 melanoma 常伴多發 nevi + **延遲白髮**（melanocyte 長壽）
- 血液惡性腫瘤與 PTC 次常見
- **UK Biobank 210 名 POT1 帶因者：淋巴性惡性腫瘤風險近 8 倍，80 歲前外顯率 45%**
- 其他：MPN/CML、sarcoma、RCC、lung adenocarcinoma、CNS 腫瘤（5–7%）
- 良性：hemangioma、adenoma、hyperplasia；>40 歲女性半數因子宮肌瘤手術

> **鏡像**：長端粒腫瘤組織恰為短端粒退化組織的鏡像；兩者皆與老化相關

---

# 長端粒：CH 與 JAK2 範例

- POT1 突變者 CH 外顯率隨老化達 **100%**（族群 60 歲後僅 10–20%）
- 可早至**嬰兒期**；長端粒維持 clonal longevity → 允許 second hits → 惡性腫瘤

```text
JAK2 內含子 "GGCC" haplotype → 族群 JAK2V617F CH 風險 ×4
        |
帶 "GGCC" 家族：
   |-- POT1 wild-type + 正常縮短 --> 隨老化「熄滅」clone
   |-- POT1 mutant  + 長端粒  --> 獲得大型 JAK2V617F clone → MPN
```

> **矛盾**：長端粒延長「有絲分裂時鐘」，卻**反常促進過早老化**（CH + pan-tissue 腫瘤）

---

# 長端粒：測量、篩檢、治療

- 端粒長度**無明確預後價值**（CH 可遮蔽原生端粒），但可協助判讀 VUS
  - 明確 POT1 突變者：淋巴球端粒 >99 百分位對致病性近 100% 特異、敏感度 60%
- 無症狀篩檢兩難：良性腫瘤高外顯、多癌 indolent 且缺篩檢工具（PTC、CLL）
- >50 歲惡性風險顯著 → 或需部分無症狀評估、**年齡分層**
- 監測策略有歧見：whole-body MRI vs 保守臨床評估
- 放化療須權衡 **second cancer** 風險

---

<!-- _class: divider -->

# 第五部分：兩極對照與總結

---

# 短 vs 長端粒：兩極表型對照

| 面向 | 短端粒 (Short) | 長端粒 (Long) |
|------|----------------|----------------|
| 核心病理 | 退化性、幹細胞耗竭 | 增生／腫瘤性、clonal |
| 代表基因 | **TERT** (LOF) | **POT1** (LOF→延長) |
| 骨髓 | Hypocellular、衰竭 | Hypercellular、MPN、CH(100%) |
| 免疫/淋巴 | T 細胞免疫缺陷 | CLL、淋巴性惡性腫瘤 |
| 肺 | IPF、emphysema | Lung adeno-ca |
| 肝 | 血管 ectasia、NRH | Hemangioma、angiosarcoma |
| 白髮 | **早發** | **延遲**（melanocyte 長壽）|
| 癌症整體 | **抑癌傾向** | **廣泛腫瘤傾向** |

---

# 關鍵基因與機轉

| 基因 | 角色 | 方向 | 代表表型 |
|------|------|------|----------|
| **TERT** | Telomerase 催化次單元 | LOF→短；promoter GOF→長 | IPF、骨髓衰竭 / familial melanoma |
| **TERC/TR** | Telomerase RNA 模板 | LOF→短 | DC、aplastic anemia、PF |
| **POT1** | Shelterin 單股結合 | LOF→**長** | CLL、melanoma、PTC、angiosarcoma |
| **TPP1/ACD** | Shelterin 招募端粒酶 | 長（ultra-long）| Melanoma、PTC、CLL |
| **TINF2** | Shelterin (TIN2) | **雙向**（domain 依賴）| PF / thyroid ca、melanoma |
| **TERF2IP** | Shelterin (RAP1) | 長 | Melanoma、CLL/PTC |

> **判讀陷阱**：至少 3 基因具雙向性 → 須結合端粒長度測量與家族表型

---

# 臨床 Pearls (1)

> **Pearl 1**：IPF + 骨髓衰竭/肝病家族史 → 先想短端粒症候群，**慎用免疫抑制**（細胞自主缺陷，反增死亡率）

> **Pearl 2**：短端粒治療主軸為器官移植；**早期轉介**、移植前 NGS 評估 MDS/AML 風險

> **Pearl 3**：flowFISH 應**分系測量** — 顆粒球選擇性短→髓系 clonal；淋巴球選擇性短→自體免疫/淋巴 clonal

> **Pearl 4**：短端粒非專屬 — RUNX1/GATA2/LIG4 也次發性縮短，須合併判讀

---

# 臨床 Pearls (2)

> **Pearl 5**：多發性/症候群式癌症（melanoma+PTC、CLL、cardiac angiosarcoma、多發子宮肌瘤+延遲白髮）→ 警覺 POT1 等長端粒基因

> **Pearl 6**：POT1 帶因者 CH 外顯率隨老化達 100%，可早至嬰兒期；監測應**年齡分層**（>50 歲風險顯著）

> **Pearl 7**：長端粒放化療須額外考量 **second cancer** 風險

> **Pearl 8**：長端粒延長「時鐘」卻反常促進過早老化；短端粒加速老化卻抑癌 — 不足與過剩皆致病

---

# 對老化與癌症基礎的啟示

- **IPF 典範轉移**：短端粒基因解釋 ≥10% IPF（> BRCA1/2 解釋的 ~5% 乳癌）；指向幹細胞老化中介；ultra-short（<1 百分位）肺移植病人調整 regimen = 新興 precision medicine
- **新致癌典範**：長端粒長度 → 「細胞過度長壽」致癌，有別於 oncogene/tumor suppressor；是癌症**最常見遺傳風險因子**
- **CH 重新理解**：長端粒**同時**預先設定 CH 與癌症，而非 CH 本身「腫瘤前驅」
- **統一觀點**：不足與過剩皆致病 → 解釋端粒延長為何演化出嚴格限制

---

<!-- _class: small-text -->

# 參考文獻 (1)

1. Schratz KE, Armanios M. Disorders of Telomere Length. *NEJM Evid*. 2026;5(7). [doi:10.1056/EVIDra2600012](https://doi.org/10.1056/EVIDra2600012)
2. DeBoy EA, et al. Familial clonal hematopoiesis in a long telomere syndrome. *N Engl J Med*. 2023;388:2422-2433. [doi](https://doi.org/10.1056/NEJMoa2300503)
3. Davidson-Swinton HR, et al. Lymphoid malignancy and clonality in POT1-mediated long telomere syndrome. *Blood*. 2026;147:2226-2237. [doi](https://doi.org/10.1182/blood.2025031287)
4. DeBoy EA, et al. Telomere-lengthening germline variants predispose to syndromic PTC subtype. *Am J Hum Genet*. 2024;111:1114-1124. [doi](https://doi.org/10.1016/j.ajhg.2024.04.006)
5. Schratz KE, et al. Cancer spectrum and outcomes in Mendelian short telomere syndromes. *Blood*. 2020;135:1946-1956. [doi](https://doi.org/10.1182/blood.2019003264)
6. Armanios M. The role of telomeres in human disease. *Annu Rev Genomics Hum Genet*. 2022;23:363-381. [doi](https://doi.org/10.1146/annurev-genom-010422-091101)

---

<!-- _class: small-text -->

# 參考文獻 (2)

7. Armanios MY, et al. Telomerase mutations in families with IPF. *N Engl J Med*. 2007;356:1317-1326. [doi](https://doi.org/10.1056/NEJMoa066157)
8. Alder JK, Armanios M. Telomere-mediated lung disease. *Physiol Rev*. 2022;102:1703-1720. [doi](https://doi.org/10.1152/physrev.00046.2021)
9. Alder JK, et al. Diagnostic utility of telomere length testing. *Proc Natl Acad Sci USA*. 2018;115:E2358-E2365. [doi](https://doi.org/10.1073/pnas.1720427115)
10. Shah PD, Armanios M. Pre-/post-lung transplant considerations for ultra-short telomere length. *Eur Respir J*. 2025;65:2401545. [doi](https://doi.org/10.1183/13993003.01545-2024)
11. Courtwright AM, et al. ISHLT Consensus: short telomere syndrome and lung transplantation. *J Heart Lung Transplant*. 2026;45:e83-e103. [doi](https://doi.org/10.1016/j.healun.2025.10.028)
12. Tsoulaki O, et al. UK guidelines: constitutional POT1 pathogenic variants. *J Med Genet*. 2025;62:559-565. [doi](https://doi.org/10.1136/jmg-2025-110638)

---

<!-- _class: lead -->

# 謝謝聆聽

## Q & A

**謝慕揚 MD, PhD, FESC**

> *本文件僅供醫療專業人員教學參考；整理者為讀書會共筆整理人，非本領域專家。*
