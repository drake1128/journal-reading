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
  section.divider {
    background-color: #0072bc;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 { color: #ffffff; border-bottom: none; font-size: 2.4em; text-align: center; }
  section.divider h2 { color: #ffffff; font-size: 1.5em; text-align: center; font-weight: bold; }
  section.divider h3 { color: #ffe082; font-size: 1.2em; text-align: center; font-weight: normal; }
  section.divider p, section.divider strong { color: #ffffff; }
  section.bignum { background-color: #1a2740; color: #ffffff; text-align: center; }
  section.bignum h1 { color: #ffffff; font-size: 3.3em; border-bottom: none; }
  section.bignum h2 { color: #b0c4de; font-size: 1.3em; }
  section.bignum p { color: #dfe6e9; font-size: 1.0em; }
  section.bignum strong { color: #ffe082; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  a { color: #0072bc; }
  table { font-size: 0.66em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 5px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.9em;
  }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.68em; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.72em; }
  section.abbr { font-size: 0.6em; }
  .qr { position: absolute; right: 40px; bottom: 70px; text-align: center; font-size: 0.6em; color: #555; }
  .qr img { width: 110px; height: 110px; border: 1px solid #dcdde1; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-08-15 ~ 2026-08-22'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-08-15 ~ 2026-08-22

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每張重點投影片附 QR Code，可掃描跳轉原文 DOI

---

# 🎯 本週主題與固定欄目

## 把治療的「第二層效益」看清楚——抗發炎、護肢、再介入、抗栓個體化

**本週六大固定欄目**：

1. ⭐ **Top 5 Picks** — 跨期刊精選
2. 🫀 **TAVI Section** — 結構性主動脈瓣方向
3. 🔧 **TEER Section** — 二尖瓣與三尖瓣緣對緣
4. 📚 **Honorable Mentions** — 其他值得讀
5. 🔬 **Case Reports** — 結構／冠脈介入 × 5
6. 📖 **參考文獻 + 縮寫對照**

> ⚠️ 本週 *NEJM* 與 *Lancet* 皆無心血管原始研究；主軸落在 Circulation 系列／EHJ／EuroIntervention／JACC 系列。

---

# ⭐ Top 5 Picks

| # | 研究 | 期刊 | 結果 | 關鍵數字 |
|---|------|------|------|----------|
| 1 | **SELECT hsCRP**（semaglutide 抗發炎） | *Circulation* | ✅ | hsCRP **−37.8%**、早於減重、獨立 LDL |
| 2 | **CLEAR PAD 肢體終點**（bempedoic acid） | *Circulation* | ✅ | MALE **HR 0.64**、總 MALE **RR 0.55** |
| 3 | **FINE-HEART**（finerenone × 癌症史） | *Eur Heart J* | ✅ | n=**18,991**；有無癌症史效益一致 |
| 4 | **LAAC vs OAC** RCT 統合 | *Circ EP* | 💡 | 缺血中風 **RR 1.41**、非手術出血 **RR 0.57** |
| 5 | **BETULA**（低劑量短時 CDT 治 PE） | *EuroInterv* | ➰ | RV/LV **−0.17 vs +0.02**、次要中性 |

> **Pearl**：看第二層效益、也看第二層代價——抗發炎、護肢、再介入與抗栓，都要拆到第二層才站得住。

---

<!-- _class: divider -->
# Pick #1
## SELECT hsCRP 次分析
### semaglutide 的心血管效益部分來自抗發炎

---

# Pick #1 — 設計與結果

**Plutzky J, et al.（Lincoff AM 資深）** *Circulation* 2026 Aug 18.
🔗 [DOI: 10.1161/CIRCULATIONAHA.125.074482](https://doi.org/10.1161/CIRCULATIONAHA.125.074482)

- SELECT 預設次分析：**n=17,604**，ASCVD + 過重／肥胖但**非糖尿病**；追蹤 39.8 個月
- 基線高敏 C 反應蛋白 (hsCRP) 具預後價值（MACE 隨 hsCRP 遞增）

| 指標 | 結果 |
|------|------|
| **hsCRP 變化（104 週）** | **−37.8%** |
| **時序** | 早於顯著減重（4–8 週即現），甚至無減重者也降 |
| **獨立性** | 獨立於 LDL、statin、ASCVD 收案條件 |

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAABCklEQVR4nMWWsY1cMQxEHxeXjzrY/sv6HYwqeA7WgX2ZJeDMSCLAATlDkRr52/aL7/aznplZe681m5lZhzgYDdCaaHqc4SxMYZdZd5Xuh/X+56g/7QuAhSHrDkeWM7i65JTncSC/LxvynOqlao39nI51T9KoaHqOA7XF2PS4f7AEFUA5x8GIxJrzul50mG663sNzrDumlFgbrvjRRIJCz3HkI3gKXOjeGDWG9DofDU1zjpM2QCN4kU+JSRrMDT9Rio2Q43f6ouCbgRW5mPPARy+T8/55EYW1maHkYs7PYhFgT3av9kUZImXd7Z15sp8J21OeX2BpIHnwoq49wxtYrLUu9s43x3/+t/wCYWHIT7DJGXkAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: bignum -->
# −37.8%
## semaglutide 把 hsCRP 降低（104 週）
### 早於減重、獨立於 LDL/statin

**MACE 效益部分來自抗發炎**：hsCRP 可作為可追蹤的殘餘發炎風險指標

---

<!-- _class: divider -->
# Pick #2
## CLEAR Outcomes — PAD 肢體終點
### 降 LDL 不只護心、也護肢

---

# Pick #2 — 設計與結果

**Bonaca MP, et al.（Nicholls SJ 資深）** *Circulation* 2026 Aug 18.
🔗 [DOI: 10.1161/CIRCULATIONAHA.125.078469](https://doi.org/10.1161/CIRCULATIONAHA.125.078469)

- CLEAR Outcomes（statin 不耐受，n=13,970）中**周邊動脈疾病 (PAD) 1,624 例**；bempedoic acid vs 安慰劑；MALE 盲判

| 終點（PAD 病人） | 效果 |
|------|------|
| **首次 MALE** | **HR 0.64（0.44–0.93），p=0.018**（↓36%） |
| **總 MALE（含復發）** | **RR 0.55（0.35–0.85），p=0.007**（↓45%） |
| 總 MACE-4 或 MALE | RR 0.71（0.54–0.95） |

> 💡 statin 不耐受的 PAD 病人：bempedoic acid 同時降低 MALE 與 MACE，護心也護肢

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAABD0lEQVR4nM2Wy20cMAxEn4y9DzvY/styB6MKXg4bGIiTQywBhnmSBuCAnxGpJX/afuOzfS+y1prZew2steaYJwohndfxjOcBK+wddoeVu0w7lPmq19/I073oDQ9Go5gaTc94lgvy+7Ih76fxqFZaonoYD6ZAg8Fwmhe2FaWk4TweE2IiwZzz0KqS1B73Cy0hBcJ537GxoZaGizqTgkIhOeV5kFJ2ylOY83dRmhBI2gsdYopU9UY/pASlyU3fKYKh0GMdPmC66CbA/KfXv3gE18g76bqYzwsS2ONrsl7tiz2v8uyLuUqCJQGO9fOBdKN+1esTUvIse8/xPn2ATAamT/bxHkQgiTYxx/VZP+zf8guN475h739j7wAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# Pick #3
## FINE-HEART 統合
### finerenone 在有無癌症史者效益一致

---

# Pick #3 — 設計與結果

**Ruppert M, Vaduganathan M, et al.** *Eur Heart J* 2026 Aug 18.
🔗 [DOI: 10.1093/eurheartj/ehag522](https://doi.org/10.1093/eurheartj/ehag522)

- FINE-HEART（FIDELIO + FIGARO + FINEARTS-HF 個人層級統合）事後分析；**n=18,991**，7.3% 有癌症史
- 有癌症史者：多屬較晚期心腎代謝 (CKM) 分期、**全因死亡與住院風險更高**

> 💡 不論有無癌症史，finerenone **一致降低**全因死亡、心衰、住院、腎臟終點、MACE、新發 AF；安全性一致

**Take home**：共病癌症不阻卻 non-steroidal MRA——腫瘤存活者可放心使用

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAABEUlEQVR4nM2WwWlEMQxEn0Luow5+/2W5g1EFk8PuJWEDiz6E+CQL9Gw0kuwK39d88HP9raequqeq6arqJYcokWX5ae44n1CC0bQe5poDNCVOvx31G0fMcL0f9dITM0fhQLzlVAr03AzobPVKEjlYSZKlXkQRRLINa92JTWwsCdhyPqDpC/UBK3vdlVELgZnZcogSSLCd+EaeSWQ7QXfyM6o2TbXxur9IbFsJYHmvu0BScLiXH8mOrQjW96kwF3i4TAP7/oIE2XkMxi0HAUaYW/2VJEggRWvO472AgUNP7+ehEnwchOUb87nENYaZev/0154TStejqO+9sPLhMHVrbigyIPtO/YBEYgPr/qp/9m/5An75wfxbU2tZAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# Pick #4
## LAAC vs OAC 的 RCT 統合
### 「不輸抗凝」的表象要拆開看

---

# Pick #4 — 設計與結果

**Circ Arrhythm Electrophysiol** 2026 Aug.
🔗 [DOI: 10.1161/CIRCEP.126.015245](https://doi.org/10.1161/CIRCEP.126.015245)

- 6 個 RCT、**n=7,004**（左心耳封堵 LAAC 3,681 vs 口服抗凝 OAC 3,323）

| 終點 | 結果 |
|------|------|
| **缺血性中風** | **RR 1.41（1.04–1.91），p=0.03**（3.2% vs 2.1%） |
| 任何中風 / 複合 | RR 1.08 / 0.99（無差異） |
| **非手術相關大出血** | **RR 0.57（0.43–0.77）**（6.2% vs 10.7%） |

> 💡 **怕出血 → LAAC 有利；怕缺血性中風 → OAC 占上風**。個體化風險權衡，而非一體適用

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAABDUlEQVR4nM2WQW4DMAgEhyj35Qf5/7Pyg+UF20NyaZVIKZaq+mQjMcYLAlf4vubCz/W3lqrqqZ6arqpec5QgozRKDiKsppsuQ/WWcwVgAnNz/+L2lxwK4s+9XlpisJl5bHecSoGehwHdtxyAMnAzrOuQCJQEIVC85TgKyMYoWnOCRBKIkm08F9rcmW6LmdnmiwgLJVHiE30kR8aSzvSxLAvho3xZxraF4j1Hj8KBQ30Ay4lkpL0+CoriJM5BPLIihBSO9MFIsQNi+64rhpQKj1wfer3RWY6JpH39POZFNwYsb+fOFUrAbTyU+rDPDwYynWU/fHJSjalPvd7NCz/6a/BZviA2WOt81T/7t3wB2tK65YpDKloAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# Pick #5
## BETULA 試驗
### 低劑量短時 CDT 治療中高危肺栓塞

---

# Pick #5 — 設計與結果

**Schultz J, et al.** *EuroIntervention* 2026;22(16):903–912.
🔗 [DOI: 10.4244/EIJ-D-26-00292](https://doi.org/10.4244/EIJ-D-26-00292)

- 開放標籤 RCT；中-高危肺栓塞 (PE)，導管溶栓 (CDT，r-tPA **4 mg/2h**)+肝素 vs 單用肝素；n=60

| 終點 | 結果 |
|------|------|
| **24h RV/LV 比變化** | **CDT −0.17 vs UFH +0.02（p=0.01）** |
| 臨床次要終點 | 血栓負荷／死亡／復發 **兩組無差異** |
| 安全性 | **無大出血**（輕微 10% vs 3%） |

> 💡 改善替代指標（RV/LV），但**臨床次要終點全中性、n=60**——概念驗證，需大型硬終點試驗

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAAA/0lEQVR4nM2WQW4EIQwEy1HuPT/Y/z9rf9C8oHKYXLI5LUhRuGGJotuAzcjPsT54HX8bmZlrzQwwM9c2J8qF5SK6q+cTJhAey4vJodN1LVffXfUrYhbkOuNY1iJDsbuccSDfkwV57nFQNaJRtbucaKi0pOxz2tok1eaAkwrVYk58GS2Blh5wWkMbGjT7vkilUZLuc2owxVBykOfESIiafT2UNLezHumxmlYJB3oSGoCkJ+elBYPl6H01kNhw5EsVkEa29dz1p3PXoJVu9q+7bpSq8eQ+h0TaBPZ93ZEl6TP2OuhfAANlzXu7v0QsCXlgyG5fRuBOTWi239f8s3/LFzZB1u5gJnQEAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 結構性主動脈瓣方向
### 再介入 × tapered LVOT × Allegra ViV

---

# TAVI #1 — 瓣中瓣失敗：redo-TAVI vs 外科取出

**Ktenopoulos N, et al.** *J Am Heart Assoc* 2026 Aug 20.（統合分析）
🔗 [DOI: 10.1161/JAHA.125.048885](https://doi.org/10.1161/JAHA.125.048885)

- 8 研究、**n=6,166**（redo-TAVI 3,743 vs 外科取出 2,425）
- redo-TAVI：院內死亡 **OR 0.20**、30 天 **OR 0.28**、1 年 **OR 0.70**；出血更少、住院更短
- **代價：中重度瓣周漏 (PVL) 明顯升高（OR 80.12）**；PPM 相當

> 💡 解剖合適者以 **redo-TAVI 為優選**（更低死亡/出血），但須把 PVL 與冠脈阻塞納入術前 CT 與 heart team

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAABCUlEQVR4nMWWsW0FMQxDn4P0zxvc/mPdBvQETPEvRX4XG0hU2QJEUDIleZSftj54t7/1jDHmnKwJY4y5jWNLGNda03aXzycMGbi4ModnmRZMfhv1xgfABcMDnA9oGBgSml2c0QE+lwXeezi0batg2za7ec3JILfCYu7qh6Y04nPY5ENBsbEm7uOEpKFtYLs+r/iQGGlP+NDGp0b7OAo1SnSbz+i8rxuuJUB25xgtaiCc1iffD0Y50E/AWtAc8GnSNK3BA/1AtIkBcqLDVlqwbPfFa1/QNQPT7M9DW+51cUlYuzhUNPKaigdzDIBbc1vmGR9BpZ70aWvS1jZH+nn2hZGDfn9z/PO/5QsieM7V2vD5EAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# TAVI #2 — tapered LVOT 與自膨瓣移位

**Eckel C, et al.** *Clin Res Cardiol* 2026 Aug 20.（NAVITOR）
🔗 [DOI: 10.1007/s00392-026-02990-8](https://doi.org/10.1007/s00392-026-02990-8)

- 354 例原生重度 AS，自膨瓣環內瓣膜；依左心室流出道 (LVOT) 形態分組
- 技術/裝置成功皆高且相當；但 **不完全術中移位 (IPDM)：tapered 18.9% vs 6.6%（p=0.001）**
- 獨立因子：**tapered LVOT（OR 2.47）**、嚴重瓣膜偏心（OR 2.16）

> 💡 tapered LVOT 者建議**略深植入**以增加錨定穩定；術前 CT 的 LVOT 形態判讀直接影響釋放策略

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAABFElEQVR4nM2WQW4EMQgEi9Xemx/M/581P2he0DnMHpLNaRkpCicbiVJjjHGFnzYP3u1vPVXVDc1QVb3mKIEpOFrJVg8RkuPotbyTaU/PqD+M+u1xm5yfRr15YgBNm3jLqRTotRnQueM8CdCGEuHGPeyaOulh6Jnt/SGxraDYKPu6V3Oc6Dql8loPkrEJ9l4PUUKwkWJlzzGOY1/i1hwwFpFzixM5SAko3ucVgnSdNrc4coil2Gw5D1occ7UG0v4dixUpcZDWdX8yoqDNMNzRk0RGscK67te8GIWGxvv+UiJwgkL29aKa6GA0pRvzC6CH0siznl+XZ3SqbdJbzhNChwrTjLV+n6eKLndryEdZfLf6Z/+WL/z4uvCNfW8kAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TAVI #3 — Allegra 瓣中瓣多中心登記

**Khan H, et al.** *Catheter Cardiovasc Interv* 2026 Aug 21.
🔗 [DOI: 10.1002/ccd.70811](https://doi.org/10.1002/ccd.70811)

- 英國 5 中心、**106 例** Allegra 瓣中瓣 (ViV) TAVI；近半 index 瓣膜 ≤21 mm
- VARC-3：**技術成功 86.8%、裝置成功 75.5%、早期安全 86.8%**
- 植入後平均壓差 **12 mmHg**、瓣口 1.7 cm²；30 天死亡 **0%**

> 💡 小瓣膜 ViV 最怕高殘餘壓差/冠脈阻塞；Allegra（大瓣口設計）血流動力尚佳，是 ViV 選瓣另一選項

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAABEklEQVR4nM2WwW0lMQxDn4Lc6Q7Sf1nTAV3By2H+JckeNh5gsboYFiBaEmlbI19tv/Hd/q1nZhabxV4zsw5xMBr1tabHGc5iD3MtmHVa1/u9ZLuu9ZvT/+jJFa6P30Z9y0fWkGsR5LTP40Bemw25TvlSNS1R9ZAvTJvURPoEp00NxaZP9MNeQ1cHmJ7ruTXBEMJ5XZqAYNOe1oXV0kJ91Oc0SYkxcJ7PrZ20AfqAd4Uiog9wbApE4Vw/7yyu5bp32efvRqGb7kHXX0f9MAMQNZA80aFiojEPeH9lY03ygK9oQGzkQV0haWwDOeb9xkkqFI7v++25uoiRnL7z93/BZLrY7hzOCTdfeMvo/J7Ofza3fALPz9PV1HR9+AAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 二尖瓣與三尖瓣緣對緣
### 大三尖瓣環 × ≤65 歲 M-TEER × FMR 證據脆弱度

---

# TEER #1 — 大三尖瓣環：LuX-Valve Plus (TRINITY)

**De Backer O, et al.** *EuroIntervention* 2026;22(16):891–902.
🔗 [DOI: 10.4244/EIJ-D-26-00062](https://doi.org/10.4244/EIJ-D-26-00062)

- **114 例**大三尖瓣環（55–70 mm）、重度以上三尖瓣逆流 (TR)、外科高風險（STS 9.9%）；經導管三尖瓣置換 (TTVR)
- **術中成功 95.6%**、30 天**臨床成功 91.2%**、殘餘 TR ≤中度 93.7%、僅 6.1% 需 PPM
- KCCQ 57→71 分、NYHA III-IV 由 57%→21%（皆 p<0.001）

> 💡 **大三尖瓣環**過去多被排除；LuX-Valve Plus 補上「解剖不利 TR」的置換選項。屬單臂、30 天短期

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAABEklEQVR4nM2WwW1YMQxDn4Lc6Q2y/1jZgJrg9ZAemhYBUn+gqG42LEIiacsjn2Nf+D3+7c7MHPbs7JmZc40TZQ/xrdEHFc7hyJke5jzrNNDs32b9Gq8A7HT88sw3dyzpYSj2FmccyM/FQt7vcFAVqFG1tziBNKEN5BbnBUiBnizprQ+xQtFi7vt65cSFw5Zdcl9PTesHydf8YEIJaBJzj6OUYui9Xq+87/GULry5t37GSGJonvFDq8Zakgf8NGlSY32ilwpSxT65XxKUQLjt64WKZKbvcb+d9Wc9QBRMcu8fjAaoxns/f8wLyNnZ4Tx753FJj3u8nMsfONnswnw366t50bMEpM/0otTQXOs1/9m/5QfuAsu8/80SpgAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# TEER #2 — ≤65 歲的二尖瓣 TEER

**Guo Y, et al.（Makkar R 資深，Cedars-Sinai）** *J Am Heart Assoc* 2026 Aug 20.
🔗 [DOI: 10.1161/JAHA.125.043262](https://doi.org/10.1161/JAHA.125.043262)

- 1,364 例二尖瓣逆流 (MR) TEER；≤65 歲 247 例（18.1%，中位 58 歲）
- 年輕組心衰更晚期，但 **3 年全因死亡較低（18.5% vs 30.3%，p=0.007）**；配對後仍成立
- **警訊：年輕組若裝置不成功，存活優勢消失**

> 💡 年輕不是護身符——唯有達最佳裝置成功（殘餘 MR ≤mild 且壓差 <5 mmHg）才有存活效益，必要時及早再介入

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAABDElEQVR4nM2WS2oFMQwES4+3b91g7n+suUHrBJ3FZJNAIMgQopVtcKFPy3KFrzYvvtvfnlRVD0MNVdVLDlEiFBQpkXecN5TIlKh0aRvXG4CByfz+1k+cRnAdckKHCqbDNs+VAn1uBnRvOQ+gxTzLbVwN3GgA+tZaPwbHwbG81g/B0QMiYc9JbCzbkZwDf4SkEGQfxBU7sYM4yU8UjIQCa39eQAfd4ynAB3oWwIjRzbXU8xsjaNcNF9e2T4mQCJYgB/WylCSGiAP9yIATAsqekySERIrWffHMi5Bu6PF+7ihhZrjnKd1RvYgE7Pv09QnrcTB9NmEbUyUmZ/M0CGPn5P0ByZYIWuu5/tm/5QMrZsA+qvE7eAAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# TEER #3 — FMR 的 TEER 證據多穩？脆弱度檢視

**Zuin M, Piazza G, et al.** *JACC Adv* 2026;5(9):103164.
🔗 [DOI: 10.1016/j.jacadv.2026.103164](https://doi.org/10.1016/j.jacadv.2026.103164)

- 針對功能性二尖瓣逆流 (FMR) 的 TEER 關鍵 RCT（COAPT／MITRA-FR 等），以**脆弱指數 (Fragility Index)** 檢視結論之統計穩健度
- 主題：改變指引的陽性 RCT，在「改變少數事件」下是否仍站得住

> 💡 用「脆弱度」眼光看待改變指引的試驗，理解證據可靠邊界，避免把單一 RCT 過度外推。屬方法學分析（原文摘要 PubMed 未提供）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJQAAACUAQAAAABdRz15AAABPklEQVR4nM2WsW1EMQxDnw7XUxv8/cfyBtQETPEPKZJU0QGJ4cYETEgULavC1zWPbxD8HVZVXUPVvauXfEpwEwahZB1zNbiQQlP9Dg0a1emyf3H3Z2ykEf0OvhhdpjlAvOOrFOjzOKCziy+JgRnO3IcNH1GEkhgLiLzkA8tGkR0raz4jYgcSZ8tnJyEgh2SdLyBsBdnwlvgkRQ5K9vo5YEnExqzji2KQTdC2Hk8o2qG4jGhr7efEt2lMtvk+OEVBEEHDsp/ejnMUWcR7/xlJcPd9veH9KpEVg5Us9XvibtyuCGbwTr8ncBia0iHUuh4YnJef1++3AtCMLwA3Xs0br/4STCwJb/2shJQvN8bSVj8hKRAU1v/HjZ1GZVdQ7f63FzZBjJpZ5vuE0KQ5dDpbvgdTxYUPlwHYzX/1z+fdDxiq9sZ4x2PoAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

<!-- _class: small-text -->
# 其他值得一讀（1/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **CHIP × AF 腦病灶/認知**（n=1,572） | *Circulation* | CHIP 帶原 22%；微出血 OR 1.45、白質病灶 OR 1.56；7 年認知退化更明顯（MoCA β −0.53） | [DOI](https://doi.org/10.1161/CIRCULATIONAHA.126.079459) ｜ [PMID](https://pubmed.ncbi.nlm.nih.gov/42610248/) |
| **Evolocumab × CABG 移植血管**（Newton-CABG） | *JACC Adv* | 24 個月移植失敗兩組無差異，但 SVG 中度病灶較少（11.5% vs 19.3%，p<0.001） | [DOI](https://doi.org/10.1016/j.jacadv.2026.103162) ｜ [PMID](https://pubmed.ncbi.nlm.nih.gov/42617487/) |
| **AMI 後 β-阻斷劑 × EF 表型**（n=5,557） | *JACC Adv* | HFrEF/HFmrEF **aHR 0.590**、**HFpEF 無效**（交互作用 p=0.034） | [DOI](https://doi.org/10.1016/j.jacadv.2026.103168) ｜ [PMID](https://pubmed.ncbi.nlm.nih.gov/42617486/) |

---

<!-- _class: small-text -->
# 其他值得一讀（2/2）

| 研究 | 期刊 | 重點 | 連結 |
|------|------|------|------|
| **心臟移植：捐贈者 ASCVD vs 冠脈攝影**（n=5,152） | *Eur Heart J* | ASCVD >5% 預測較差結局（HR 1.30）；低風險者常規冠脈攝影無助益 | [DOI](https://doi.org/10.1093/eurheartj/ehag488) ｜ [PMID](https://pubmed.ncbi.nlm.nih.gov/42619250/) |
| **LAD 自發冠脈剝離 (SR-SCAD)**（n=388） | *EuroInterv* | LAD-SCAD 病灶更長/多支；長期 MACCE 獨立升高（**aHR 2.00**） | [DOI](https://doi.org/10.4244/EIJ-D-25-01394) ｜ [PMID](https://pubmed.ncbi.nlm.nih.gov/42610336/) |
| **德國職場 CV 風險：年齡×性別**（n=40,704） | *JACC Adv* | 45–55 歲女性吸菸多、50 歲起女性肥胖多；更年期風險上升 → 性別專屬預防 | [DOI](https://doi.org/10.1016/j.jacadv.2026.103159) ｜ [PMID](https://pubmed.ncbi.nlm.nih.gov/42617493/) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構／冠脈介入方向 × 5

---

# Case #1 — TAVR 後「自殺性左心室」休克

**De la Ossa VL, et al.** *JACC Case Rep* 2026 Aug 21.
🔗 [DOI: 10.1016/j.jaccas.2026.109244](https://doi.org/10.1016/j.jaccas.2026.109244)

77 歲女性 TAVR 後心因性休克。超音波見**小而過度收縮的左心室 + 匕首狀動態心室內壓差**（動態 LVOT 阻塞），非瓣膜功能異常。**停用強心劑、改補液 + 升壓 + β-阻斷**後迅速恢復。

> 💡 TAVR 後不明休克要**立刻超音波**：見「小而高動力 LV + 動態壓差」即為自殺性 LV，**強心劑會火上加油**

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJQAAACUAQAAAABdRz15AAABQ0lEQVR4nM2WMW4EMQwDR4frqR/s/5+1P6BewBQ+pEhwRaAAyXYW4IFoy1xW+PrN41sJ/q5WVd3VVVRRVb3kKcE4DELJuudqYJBCU73jPQFoqdwT+oe9vKvdJY0ObsuLGURzA/GOVynQ53JA94ZHkoQEZJQk3vEUgRJjAdGWZ9uAIjvWtj8jROxA4rXevJjIIVnrtSTbCrJhfx9ghchByfr8QoiQiI3Z8R6gCoTbRYulv5zWbNlyJLyel2DbRphs9T65bjcpREaz10uwZckijrfzh3WQCRZrnhxbkcFKludXYWjB5BgqWv1/SRRbMfJxwuX9lhvcNp360d43eoEecwG48VIvIAUfp9m+j5MP7vHl5mX5+/d7xlqB7fw9XtBJ2RXU/oV8MAYxaka/kQ8o9U37WP6ON1VcqpvLAOzyX/3zvPsBF9L+TWGwABsAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #2 — IVUS 導引 UNICORN 瓣葉切割（redo TAVR）

**Hailan A, et al.** *JACC Case Rep* 2026 Aug 20.
🔗 [DOI: 10.1016/j.jaccas.2026.109805](https://doi.org/10.1016/j.jaccas.2026.109805)

26 mm SAPIEN 3 嚴重衰敗、**左冠脈阻塞高風險（valve-to-coronary 3.4 mm）**。以**血管內超音波 (IVUS) 導引 UNICORN（射頻針瓣葉切割）** 即時評估瓣葉/瓣架/左主幹關係，再植入 23 mm RESILIA，結果良好。

> 💡 TAVR-in-TAVR/ViV 最致命是冠脈阻塞；**首度以 IVUS 導引 UNICORN**，把腔內影像帶進瓣葉切割

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJQAAACUAQAAAABdRz15AAABSklEQVR4nM2WQY4cMQwDy4O5l38w/39W/4B+AXPoxR6ym8NECyR9agkQQZOypVV+/87jSwr+XW6ttWFv2NzBDM+WvS4W18Z2xu8JS3D37Fx3MMQDDsXAfqv2z7mwD/v4N7Vfcg30crMJzQxvdYGf4QGvGR7cuuUTc4JHbZUQFUMzw0vSRhppGeI97x4p2Zzu+Ebt9/xq2ta2JOjwvFK9HTa2U/2oFbWCZcxPtJhUMFN+YsGUlnSo34Mj257XYQMrU3+VkgKJZuwv1DQxJmTsR9I0Euit5JCf8SYJDT/Sf2mKQPUH+kXj7UwcvgcP6LmAliAZzqOPQYQxCo71a1sIUq1zf8FSaqJz/WyhK+QFOcz2jdvfJK0pTPvv3g9kc7pPeG1G8/LOnQPuI5xr/L603tdDyvR+PDkLl3htuvJO7fd4nwtv+fj/n/bdXwgz7bw2CW8xAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case #3 — TAVR-IE 贅生物栓塞表現為 NSTE-ACS

**Lucchese SC, et al.** *JACC Case Rep* 2026 Aug 20.
🔗 [DOI: 10.1016/j.jaccas.2026.109875](https://doi.org/10.1016/j.jaccas.2026.109875)

70 歲男性有 TAVR 病史，以胸悶 + troponin 升高表現。冠脈攝影見 **LAD 阻塞，抽吸物為贅生物**；血培養 *Enterococcus faecalis*，TEE 證實生物瓣贅生物——**TAVR 感染性心內膜炎 (IE) 栓塞至冠脈**。

> 💡 TAVR 病人 ACS 若見抽吸物性狀不尋常/發燒/菌血症，要想到 IE 栓塞；抽吸物送病理與培養

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJQAAACUAQAAAABdRz15AAABSklEQVR4nM2WsW1EMQxDnw6/pzfw/mN5A2oCpviXKxKkCHRA4k4qCMqkKVf4evrxrQV/16uqVVVUU1TVGuIpAYF2sZSMOdfCpPsYqDXDuwDYzZLq91x+6FlLB9ljvAvCagzdG8JMj0qBXmWDzmzeJAb7wLmLCR4RxpEwiWx5xu+I7MLCTbNmehBFxBGJA5nxu+h16N1ShWV66hezG9JajSnP/dyOlgrtxsz0vQDvRgXthdfYL4njSIAlZaRHpVk6gBrY4FE+Ez9jwDEWQz8TOwjbieLpvETEkh3bkTzFi4IwkUzMDO9BgS1oDCXN8o/kNkqkd+nh5L7H2PP7UyQHnBjm/JKE57AKY36AZCQHSZnqq4Te3A/OXeN8RrLAkUGa7g+A3RYFss87/gcNhoMXekP+Kcm9ND3dR5/6GoIShvlykRdunvD/6b/7AbJc/V7SXV9VAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case #4 — 穿越 PFO 的「轉運中血栓」+ PE

**Stewart CJ, et al.** *JACC Case Rep* 2026 Aug 20.
🔗 [DOI: 10.1016/j.jaccas.2026.109873](https://doi.org/10.1016/j.jaccas.2026.109873)

56 歲病人雙側大量肺栓塞 (PE)，經胸超音波見**大量血栓卡在卵圓孔 (PFO)**（thrombus in transit）。多科討論後行**緊急外科取栓 + PFO 關閉**，成功。

> 💡 轉運中血栓同時威脅肺與體循環（矛盾性栓塞→隱源性中風）；低-中手術風險者外科取栓栓塞/死亡率較低

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJQAAACUAQAAAABdRz15AAABQUlEQVR4nMWWQWodMAxEn8LfP9/g3/9YucH4BNPFDy1toNAqEG2MBB6k8UjylD/tvn0KwffFZuYww1zm5ezwbLnJIGK7y+8BI09u78k7jGs84OKYwX+6+9dYctL/vPt7rMFcDk9Cs8ObDh9lAlzwfcdfgZFbLs+y1DMVrCGqYLPDQ/qCTEpwiweoUWrd50fbljakuMvvjXTm3hMOEd53eqHUoNiXu+XPYhOTGsyOvwecXjw8LyDP7OvVYrCEruslJREayfJ9aSOkSWuz158lic2r7b6gPyKpBhq6zs9EIDYvd4kXtYUqka/hr2mj7f491BTSBshaL/1VrPUr5p+hqYlu+ZuecADIPWboen8ooTWFrf4eH6dDh3gOy30JwKF3gtPlvnxAOeF54FAP6/kHgh/zL+v5/PPD24/l+Y1/28/2A6K29l6Ke7XuAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case #5 — NOGA 直視 Trifecta 生物瓣衰敗

**Suzuki J, et al.** *Case Rep Cardiol* 2026;2026:7201873.
🔗 [DOI: 10.1155/cric/7201873](https://doi.org/10.1155/cric/7201873)

Trifecta 是 TAV-in-SAV 最具挑戰的外科瓣。以**非阻塞性全景血管內視鏡 (NOGA)** 於**直視下**觀察瓣葉衰敗形態（CT 難評估），後植入 26 mm Evolut FX。

> 💡 Trifecta 瓣葉外掛設計使 ViV 評估困難；NOGA 直視補足 CT 盲點。屬單一案例，增益價值待驗證

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACEAQAAAAB5P74KAAABDUlEQVR4nMWWQWpEIRBEn2H25Q3m/seaG5QneFn8mUVCAoNCIi6kwcJ+1bYO+TrWB9/H30bGGJO5Futa7ulgNBZioumezg1GGEWAkd28bgBkOsj7u36LrGJXz3Qsuc81ndhdneHglREL8tjVAZgAvbS2fYdI+lxt+o5eJ4mUbNfPVTcUmkSPzmNsVdp9HQJiMPaETxTVmiM+AZqS9sQvSEkQ4gGf9JrUAz7DUQDuj9kZ2LwXGIIpxnrAJ9BIVc74QK8iIuz31SIzyEjHm7t+0hmQwgIm6X7f0NDr2cgJHxJiCeTIrwSTUrvN+RlZjzVlTLr/fsnsnbDuWd31C4FASzzgc+P1cfHZY//33/IJqpzDMZF0ViEAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# 💎 本週 Take Home Message（1/2）

1. **semaglutide 效益部分來自抗發炎（SELECT hsCRP）**：hsCRP −37.8%、早於減重、獨立 LDL/statin。
2. **降 LDL 護心也護肢（CLEAR PAD）**：bempedoic acid 把 MALE 降 36%、總 MALE 降 45%。
3. **共病癌症不阻卻 finerenone（FINE-HEART）**：有無癌症史效益一致。
4. **LAAC「不輸抗凝」要拆開看**：缺血性中風其實較高（RR 1.41）、非手術大出血較低（RR 0.57）。

---

# 💎 本週 Take Home Message（2/2）

5. **TAVI 再介入/大解剖**：瓣中瓣失敗優選 **redo-TAVI**（死亡/出血低、PVL 高）；**tapered LVOT** 宜略深植入；**Allegra ViV** 血流動力尚佳。
6. **TEER 選擇與證據素養**：**大三尖瓣環用 LuX-Valve Plus**（術中成功 95.6%）；**≤65 歲 M-TEER 需達最佳裝置成功才有效益**；以**脆弱度**批判讀 FMR RCT。
7. **五則介入 case**：TAVR 後**自殺性 LV**、**IVUS 導引 UNICORN**、**TAVR-IE 栓塞 ACS**、**PFO 轉運中血栓**、**NOGA 直視** Trifecta。另記：**CHIP 是 AF 新腦/認知風險**、**AMI 後 β-阻斷劑只在 HFrEF/HFmrEF 有效**。

---

<!-- _class: small-text -->
# 完整參考文獻（1/2）

**Top 5 Picks**
1. Plutzky J, et al. Semaglutide & hsCRP in SELECT. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.125.074482) PMID 42610271
2. Bonaca MP, et al. Bempedoic Acid & Limb Outcomes in PAD (CLEAR). [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.125.078469) PMID 42610264
3. Ruppert M, et al. Finerenone in CKM ± cancer (FINE-HEART). [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag522) PMID 42610431
4. LAAC vs OAC in AF: RCT meta-analysis. [*Circ Arrhythm EP* 2026.](https://doi.org/10.1161/CIRCEP.126.015245) PMID 42626769
5. Schultz J, et al. Low-dose CDT for intermediate-high-risk PE (BETULA). [*EuroInterv* 2026;22(16):903–912.](https://doi.org/10.4244/EIJ-D-26-00292) PMID 42610339

**TAVI**
6. Ktenopoulos N, et al. Redo-TAVI vs surgical explantation: meta-analysis. [*JAHA* 2026.](https://doi.org/10.1161/JAHA.125.048885) PMID 42622107
7. Eckel C, et al. Self-expanding THV in tapered LVOT. [*Clin Res Cardiol* 2026.](https://doi.org/10.1007/s00392-026-02990-8) PMID 42622673
8. Khan H, et al. Allegra valve-in-valve registry. [*Catheter Cardiovasc Interv* 2026.](https://doi.org/10.1002/ccd.70811) PMID 42627148

---

<!-- _class: small-text -->
# 完整參考文獻（2/2）

**TEER**
9. De Backer O, et al. LuX-Valve Plus TTVR in large anatomies (TRINITY). [*EuroInterv* 2026;22(16):891–902.](https://doi.org/10.4244/EIJ-D-26-00062) PMID 42610335
10. Guo Y, et al. Mitral TEER in Younger Adults. [*JAHA* 2026.](https://doi.org/10.1161/JAHA.125.043262) PMID 42622086
11. Zuin M, et al. TEER in FMR: robustness of trial evidence. [*JACC Adv* 2026;5(9):103164.](https://doi.org/10.1016/j.jacadv.2026.103164) PMID 42617485

**Honorable Mentions**
12. CHIP & silent brain lesions in AF. [*Circulation* 2026.](https://doi.org/10.1161/CIRCULATIONAHA.126.079459) PMID 42610248
13. Evolocumab on CABG grafts (Newton-CABG). [*JACC Adv* 2026.](https://doi.org/10.1016/j.jacadv.2026.103162) PMID 42617487
14. Gu T, et al. β-blocker after AMI by HF subtype. [*JACC Adv* 2026.](https://doi.org/10.1016/j.jacadv.2026.103168) PMID 42617486
15. Gnesin F, et al. Donor ASCVD risk vs angiography. [*Eur Heart J* 2026.](https://doi.org/10.1093/eurheartj/ehag488) PMID 42619250
16. Marschall A, et al. LAD-SCAD (SR-SCAD). [*EuroInterv* 2026;22(16):874–882.](https://doi.org/10.4244/EIJ-D-25-01394) PMID 42610336
17. Lueg JC, et al. CV risk factors by age & sex (Germany). [*JACC Adv* 2026.](https://doi.org/10.1016/j.jacadv.2026.103159) PMID 42617493

**Case Reports**：18. Suicidal LV after TAVR (PMID 42627316)｜19. IVUS-UNICORN redo TAVR (42622593)｜20. TAVR-IE embolization NSTE-ACS (42622592)｜21. Thrombus-in-transit PFO (42627317)｜22. NOGA Trifecta BVD (42621394)

---

<!-- _class: abbr -->
# 縮寫對照（1/2）

| 縮寫 | 全名 | 縮寫 | 全名 |
|------|------|------|------|
| ASCVD | Atherosclerotic CV Disease | MALE | Major Adverse Limb Event |
| MACE | Major Adverse CV Events | PAD | Peripheral Artery Disease |
| hsCRP | High-Sensitivity CRP | CKM | Cardio-Kidney-Metabolic |
| GLP-1 RA | GLP-1 Receptor Agonist | MRA | Mineralocorticoid Receptor Antagonist |
| LDL-C | Low-Density Lipoprotein Cholesterol | AF | Atrial Fibrillation |
| HR/RR/OR | Hazard/Risk/Odds Ratio | LAAC | Left Atrial Appendage Closure |
| OAC/NOAC | (Non-Vitamin K) Oral Anticoagulant | CHIP | Clonal Hematopoiesis Indeterm. Potential |
| PE | Pulmonary Embolism | CDT | Catheter-Directed Thrombolysis |
| UFH | Unfractionated Heparin | r-tPA | Recombinant Tissue Plasminogen Activator |
| RV/LV | Right/Left Ventricle | MoCA | Montreal Cognitive Assessment |

---

<!-- _class: abbr -->
# 縮寫對照（2/2）

| 縮寫 | 全名 | 縮寫 | 全名 |
|------|------|------|------|
| TAVI/TAVR | Transcatheter Aortic Valve Impl./Repl. | TEER | Transcatheter Edge-to-Edge Repair |
| SAVR | Surgical Aortic Valve Replacement | M-TEER/T-TEER | Mitral/Tricuspid TEER |
| ViV | Valve-in-Valve | TTVR | Transcatheter Tricuspid Valve Replacement |
| AS | Aortic Stenosis | MR/TR | Mitral/Tricuspid Regurgitation |
| PVL | Paravalvular Leak | FMR | Functional Mitral Regurgitation |
| PPM | Permanent Pacemaker | KCCQ | Kansas City Cardiomyopathy Questionnaire |
| LVOT | Left Ventricular Outflow Tract | HFrEF/HFmrEF/HFpEF | HF reduced/mildly-reduced/preserved EF |
| IPDM | Incomplete Periproc. Device Migration | AMI | Acute Myocardial Infarction |
| VARC-3 | Valve Academic Research Consortium-3 | CABG | Coronary Artery Bypass Grafting |
| STS | Society of Thoracic Surgeons score | SVG/IMA | Saphenous Vein Graft / Internal Mammary A. |
| SCAD | Spontaneous Coronary Artery Dissection | LAD | Left Anterior Descending artery |
| MACCE | Major Adverse Cardiac & Cerebrovasc. Events | ACS/NSTE-ACS | (Non-ST-Elevation) Acute Coronary Syndrome |
| IE | Infective Endocarditis | PFO | Patent Foramen Ovale |
| IVUS | Intravascular Ultrasound | NOGA | Nonobstructive General Angioscopy |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**

📱 每張投影片 QR Code 可掃描跳轉原文 DOI

*本講義為讀書會共筆之教學整理，僅供醫療專業同仁臨床教學交流參考，不作為個案診療依據。*
