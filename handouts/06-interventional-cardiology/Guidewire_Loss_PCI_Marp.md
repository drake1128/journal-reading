---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'PingFang TC', 'Microsoft JhengHei', sans-serif;
    background-color: #ffffff;
    color: #1a1a1a;
    font-size: 28px;
    padding: 46px 64px 56px 64px;
    justify-content: flex-start;
  }
  h1 { color: #8a1538; font-size: 40px; border-bottom: 3px solid #8a1538; padding-bottom: 0.15em; margin: 0 0 0.35em 0; }
  h2 { color: #1a1a1a; font-size: 32px; margin: 0.2em 0 0.3em 0; }
  h3 { color: #8a1538; font-size: 28px; margin: 0.2em 0; }
  h6 { color: #555555; font-size: 17px; font-weight: normal; position: absolute; left: 64px; right: 64px; bottom: 44px; margin: 0; }
  h6 a { color: #8a1538; }
  ul, ol { margin: 0.2em 0; }
  li { margin: 0.12em 0; }
  strong { color: #8a1538; }
  em { color: #555555; }
  table { font-size: 27px; width: 100%; border-collapse: collapse; }
  th { background-color: #8a1538; color: #ffffff; padding: 6px 12px; }
  td { padding: 5px 12px; border-bottom: 1px solid #e5d3d8; }
  tr:nth-child(even) { background-color: #fbf3f5; }
  blockquote {
    border-left: 6px solid #8a1538;
    background-color: #fbf3f5;
    color: #1a1a1a;
    padding: 0.4em 0.9em;
    margin: 0.4em 0;
    font-size: 28px;
  }
  a { color: #8a1538; }
  footer { color: #777777; font-size: 15px; }
  section::after { font-size: 15px; color: #777777; }
  section.lead { background-color: #8a1538; color: #ffffff; justify-content: center; }
  section.lead h1 { color: #ffffff; border-bottom: 3px solid #ffffff; font-size: 48px; }
  section.lead h2 { color: #f3d9df; }
  section.lead p, section.lead strong, section.lead a, section.lead em { color: #ffffff; }
  section.lead footer, section.lead::after { color: #f3d9df; }
  section.divider { background-color: #1a1a1a; color: #ffffff; justify-content: center; align-items: center; }
  section.divider h1 { color: #ffffff; border-bottom: none; font-size: 52px; text-align: center; }
  section.divider h2 { color: #e8a5b5; text-align: center; }
  section.divider footer, section.divider::after { color: #aaaaaa; }
  section.big h2 { font-size: 34px; }
  section.ref { font-size: 15.3px; }
  section.ref h1 { font-size: 40px; }
  section.ref li { margin: 0.05em 0; }
footer: '謝慕揚 MD, PhD, FESC | 不要再掉 wire：PCI 導線位置的保持 | 2026'
---

<!-- _class: lead -->
<!-- _paginate: false -->

# 不要再掉 wire
## PCI 退器材時的導線位置保持：機轉、證據與練習

**謝慕揚 MD, PhD, FESC** | 2026-10-21

---

# 什麼叫「掉 wire」？

- 推或退器材時，把 0.014" wire **一起帶出**病灶或冠狀動脈
- 代價不只是「再穿一次」
  - Dissection 之後，不一定能再穿回真腔
  - 分叉病灶失去 SB 通路
  - CTO 失去 antegrade／retrograde 位置
- 多花時間、顯影劑、輻射

> 掉 wire 很少寫進併發症，但常常是併發症的起點

---

# 我自己歸納的三個原因

1. **退長的 OTW／雙腔器材**
   - Corsair、SASUKE 退出時最容易掉
2. **分叉病灶，小 guide 退大 NC balloon**
   - 把另一條 SB wire 一起帶出來
3. **太緊張，沒有看螢幕**
   - 低頭看手，沒有踩 fluoro
   - 手照肌肉記憶動作，wire 就被帶走

---

# 現有證據有多少？

| 主題 | 證據等級 |
|---|---|
| OTW 器材交換（hydraulic、trapping） | 病例系列、廠商資料 |
| 分叉 jailed wire 處理 | RCT、EBC 共識 |
| 操作者視線（eye tracking） | 小型研究（神經介入） |
| Fluoro 劑量取捨 | RCT |
| 模擬訓練 | 小型 RCT |
| **掉 wire 的發生率** | **沒有資料** |

---

<!-- _class: divider -->

# 原因一
## 長的 OTW／雙腔器材

---

# 先算長度：為什麼一定會掉？

| 項目 | 長度（約） |
|---|---|
| Guiding catheter | 100 cm |
| Wire 在體內（guide + 冠狀動脈） | 約 110 cm |
| 標準 wire 全長 | 180–190 cm |
| **Corsair（OTW）** | **135／150 cm** |

- 體外只剩約 70–80 cm wire，**比 Corsair 還短**
- 退到一半，手就**沒有地方可以壓住 wire**
- Monorail 的 RX port 離 tip 約 25 cm，不會有這個問題

###### 長度為一般規格的估算值；Corsair 是 OTW microcatheter，SASUKE 是雙腔（RX + OTW）

---

# OTW 器材的四種退法

| 方法 | 原理 | 證據 |
|---|---|---|
| **Trapping balloon** | Guide 內打球囊壓住 wire | 廠商資料、病例 |
| Extension wire | Wire 接長到約 300 cm | 技術描述 |
| 300 cm exchange wire | 一開始就用長 wire | 技術描述 |
| Hydraulic exchange | 加壓推出器材 | 成功率 **96–98%** |

- 目前**沒有**比較這四種方法的研究

###### [Feiring AJ, Olson LE. *Cathet Cardiovasc Diagn* 1997;42:457-66（JEX，n=325 次交換）](https://doi.org/10.1002/(sici)1097-0304(199712)42:4%3C457::aid-ccd29%3E3.0.co;2-f)

---

# Trapping 的實作要點

1. 器材 tip 退到 **guide 內**（看 fluoro 確認）
2. 球囊放在 guide 內、器材 tip 近端
3. 打到 **12 atm**，把 wire 壓在 guide 壁上
4. 退出器材，wire 不動
5. 放掉球囊，再送下一個器材

- TRAPPER（BSC）：6F guide 可退 Corsair、Caravel、Finecross、OTW balloon
- TrapLiner（Teleflex）：guide extension 內建 trapping 球囊

###### [BSC TRAPPER compatibility card（廠商資料）](https://www.bostonscientific.com/content/dam/bostonscientific/Interventional%20Cardiology/portfolio-group/CTO-Systems/Resources/EXT_TRAPPER_Compatibility_Card_A5.pdf) · [TrapLiner IFU](https://irc.teleflex.com/wp-content/uploads/2026/03/107584-rA-IFU-TrapLiner-US-Intl-LLC.pdf)

---

# 雙腔器材（SASUKE 等）

- 第二條 wire 走的是 **OTW lumen**，退出時同樣會被帶走
- 文獻建議：退出「需要 extension wire，**最好用 trapping balloon**」
- 但作者也指出：很多術者**不常用**這兩種方法
- 替代做法：REACH technique
  - 經 guide extension 直接送第二條 wire

> 沒準備好 trapping，就先不要用雙腔器材

###### [Kayaert P, et al. REACH technique. *Catheter Cardiovasc Interv* 2026;107:909-15](https://doi.org/10.1002/ccd.70433)

---

<!-- _class: divider -->

# 原因二
## 分叉病灶：小 guide 退大球囊

---

# 為什麼會連另一條 wire 一起帶出？

- 6F guide 內同時有：**兩條 wire + 一個大 NC balloon**
- 大 NC balloon 放氣後**不會完全收回原形**
  - 翼狀摺邊會勾住旁邊的 wire
- 退到 guide tip、主動脈弓這些轉角時摩擦最大
- 結果：退 MB 球囊，**SB wire 跟著走**

###### 機轉為專家意見；目前沒有找到兩個器材在同一 guide 內摩擦的 bench 研究

---

# Jailed wire 的證據

| 研究 | 發現 |
|---|---|
| Pan 2016 RCT（n=235） | 非 polymer wire 受損 **55%** |
| 同上 | Polymer-coated wire 只有 2 條輕微受損 |
| Kuno 2019（n=850） | Jailed balloon 卡住 **5.9%** |
| Sakamoto 2014（n=28） | 用球囊協助取出，全部成功 |

- 用力硬拉：病例報告有拉出整支支架、支架縱向變形

###### [Pan 2016](https://doi.org/10.1016/j.jcin.2016.06.030) · [Kuno 2019](https://doi.org/10.1016/j.carrev.2019.01.033) · [Sakamoto 2014](https://doi.org/10.1002/ccd.25358) · [Varvarovsky 2007](https://pubmed.ncbi.nlm.nih.gov/17986727/)

---

# EBC 第 17 次共識的提醒

- 避免 jailed 段太長（> 15–20 mm），尤其是鈣化血管
- **Guide 不要碰到近端支架邊緣**
- 取出 jailed wire 時，guide 可能被拉進去
  - Guide 與 SB wire 可以一起退
- 可沿 jailed wire 送球囊，鬆開與 MB 支架的接觸
- **POT 先做，再重新穿 SB**

###### [Pan M, et al. 17th EBC consensus. *EuroIntervention* 2023;19:26-36](https://doi.org/10.4244/EIJ-D-23-00124)

---

# 分叉病灶的實務建議

1. 預期要兩支架或大球囊：**一開始就用 7F guide**
2. 退大 NC balloon 前：**負壓抽到底、等幾秒**
3. 退的時候**踩 fluoro**，同時看兩條 wire 的 tip
4. 左手同時壓住兩條 wire（或交給助手壓 SB wire）
5. 感覺到阻力就停：先看，不要硬拉
6. Jailed wire 用 polymer-jacketed、jailed 段要短

###### 第 1–5 點為專家意見；第 6 點有 RCT 與 EBC 共識支持

---

<!-- _class: divider -->

# 原因三
## 人因：眼睛在哪裡

---

# 專家看螢幕，新手看手

- 神經介入 eye-tracking 研究
  - 模型操作時 **91%** 的注視點在 fluoro 螢幕上
  - 經驗較少的術者「**較常低頭看自己的手**」
  - 漏看重疊 marker 的術者，從沒注視過近端 marker
- 專家在正側位影像之間切換得更頻繁
- 冠狀動脈 PCI 目前**還沒有** eye-tracking 研究

###### [Shojima 2020a](https://doi.org/10.1016/j.wneu.2020.05.012) · [Shojima 2020b](https://doi.org/10.25259/SNI_543_2020) · [Otsuka 2023](https://doi.org/10.18999/nagjms.85.1.50)

---

# 踩 fluoro 的輻射代價：用低 frame rate

- RCT（n=363）：fluoro **7.5 vs 15 fps**
  - 術者劑量下降 **30%**（p < 0.0001）
  - 病人 DAP 下降 **19%**（p = 0.022）
  - Fluoro 時間沒有增加
- 系統性回顧（15 篇 RCT）：7.5 fps 降低術者劑量

> 退器材時踩 fluoro，用 7.5 fps，代價很小

###### [Abdelaal E, et al. *JACC Cardiovasc Interv* 2014;7:567-74](https://doi.org/10.1016/j.jcin.2014.02.005) · [Fernandez R, et al. *JBI Evid Synth* 2021;19:4-33](https://doi.org/10.11124/JBISRIR-D-19-00343)

---

# 緊張是可以量到的

- 介入 fellow 與主治的心率變異（LF/HF）
  - 操作中 **6.2**，休息基準 **4.1**
  - 複雜、出併發症、急診案例更高
  - 到 fellowship 結束時下降
- 壓力一高，注意力變窄，手就回到肌肉記憶

> 緊張不是性格問題，是可以練下來的

###### [Alexandrou M, et al. *J Invasive Cardiol* 2025;37(9)](https://doi.org/10.25270/jic/25.00011)

---

# 手與眼的規則

- **眼睛**：wire 會動的每一個動作，都看螢幕
- **左手**：固定 wire（Y-connector 外或 torquer）
- **右手**：只負責推或退器材
- **嘴巴**：說出來
  - 「退 Corsair，wire 壓住了」
  - 「Trapping 打 12 atm」
- 助手回覆確認（closed-loop communication）

###### 專家意見；目前沒有直接比較的研究

---

<!-- _class: divider -->

# 自我練習
## 把動作練成不必想

---

# 模擬訓練有沒有用？

| 研究 | 設計 | 結果 |
|---|---|---|
| Voelker 2016 | RCT，n=18 | Skills score +5.8 vs −6.7（P=0.003） |
| Bagai 2012 | RCT，n=27 | 技術分數進步 6 vs 1（P=0.04） |
| Jensen 2016 | RCT，n=16（CAG） | 錯誤分數 15 vs 27（p=0.002） |
| Prenner 2018 | 觀察，2,783 例 CAG | 每例 fluoro 少 117 秒 |

- 反面證據：只上課不練習，學習曲線**沒有**變快

###### [Voelker](https://doi.org/10.1111/joic.12257) · [Bagai](https://doi.org/10.1161/CIRCINTERVENTIONS.112.970772) · [Jensen 2016](https://doi.org/10.4244/EIJY15M06_05) · [Prenner](https://doi.org/10.1002/ccd.27203) · [Jensen 2014](https://doi.org/10.1186/1472-6920-14-49)

---

# 自我練習清單（1）：桌上練習

1. **Trapping 乾式練習**
   - 用過期 guide、wire、Corsair，在桌上練 20 次
2. **長度算術**
   - 每次拿到 OTW 器材，先算體外 wire 夠不夠
3. **不看手的退器材**
   - 請助手遮住手，只看模擬螢幕完成退出
4. **雙 wire 退球囊**
   - 6F 與 7F guide 各練一次，感受阻力差別

###### 建議項目為專家意見

---

# 自我練習清單（2）：在導管室

1. **交換前 5 秒停頓**
   - 器材是 RX 還是 OTW？wire 夠長嗎？guide 夠大嗎？
2. **錄影回看**
   - 每月挑一例自己的 cine，看退器材時 wire tip 有沒有動
3. **個人掉 wire 紀錄**
   - 每次掉 wire 寫下：器材、步驟、當時眼睛在哪
4. **看資深術者的手**
   - 觀察左手固定 wire 的位置與時機

###### 建議項目為專家意見

---

# 團隊與 checklist

- 導管室 team brief + WHO 式 checklist
  - 併發症從 **2.0%** 降到 **0.8%**（p ≤ 0.001）
- 國際調查（n=821）
  - **97%** 術者希望有更多併發症處理教學

> 交換器材前，大聲說出計畫，讓整個團隊一起看 wire

###### [Lindsay AC, et al. *BMJ Open Qual* 2018;7:e000074](https://doi.org/10.1136/bmjoq-2017-000074) · [Simsek B, et al. *Catheter Cardiovasc Interv* 2022;99:1733-40](https://doi.org/10.1002/ccd.30173)

---

# 證據的空白

- 沒有「掉 wire」發生率的資料
- 沒有 trapping、extension、hydraulic 的比較研究
- 沒有兩個器材在同一 guide 內摩擦的 bench 研究
- 冠狀動脈 PCI 沒有 eye-tracking 研究
- 沒有針對 wire 操作錯誤的訓練試驗

> 這是值得我們自己做 registry 的題目

---

# Take-home message

1. **OTW／雙腔器材**：先算長度，準備 trapping
2. **分叉病灶**：大球囊、雙 wire，用 7F guide
3. **退器材時**：踩 fluoro（7.5 fps），看兩條 wire tip
4. **左手壓 wire、右手動器材、嘴巴說出來**
5. **桌上練、錄影看、自己記錄**

> 眼睛看螢幕，手才不會把 wire 帶走

---

<!-- _class: ref -->

# 參考文獻（1/2）

1. Feiring AJ, Olson LE. Coronary stent and over-the-wire catheter exchange using standard length guidewires: Jet exchange (JEX). [*Cathet Cardiovasc Diagn*. 1997;42(4):457-66.](https://doi.org/10.1002/(sici)1097-0304(199712)42:4%3C457::aid-ccd29%3E3.0.co;2-f)
2. Boston Scientific. TRAPPER exchange device compatibility card（廠商資料）. [bostonscientific.com](https://www.bostonscientific.com/content/dam/bostonscientific/Interventional%20Cardiology/portfolio-group/CTO-Systems/Resources/EXT_TRAPPER_Compatibility_Card_A5.pdf)
3. Teleflex. TrapLiner instructions for use, rev. A, 2026（廠商資料）. [teleflex.com](https://irc.teleflex.com/wp-content/uploads/2026/03/107584-rA-IFU-TrapLiner-US-Intl-LLC.pdf)
4. Kayaert P, Ungureanu C, Bataille Y, et al. Rapid Entry and Advanced Coronary Handling (REACH) technique. [*Catheter Cardiovasc Interv*. 2026;107(4):909-15.](https://doi.org/10.1002/ccd.70433)
5. Tsujimura T, et al. Successful percutaneous retrieval of a detached microcatheter tip using the guide-extension catheter trapping technique: a case report. [*J Cardiol Cases*. 2019;20(5):168-71.](https://doi.org/10.1016/j.jccase.2019.07.007)
6. Pan M, Ojeda S, Villanueva E, et al. Structural damage of jailed guidewire during the treatment of coronary bifurcation lesions. [*JACC Cardiovasc Interv*. 2016;9(18):1917-24.](https://doi.org/10.1016/j.jcin.2016.06.030)
7. Pan M, Lassen JF, Burzotta F, et al. The 17th expert consensus document of the European Bifurcation Club. [*EuroIntervention*. 2023;19(1):26-36.](https://doi.org/10.4244/EIJ-D-23-00124)
8. Sakamoto S, et al. Clinical and angiographic outcomes of patients undergoing entrapped guidewire retrieval in stent-jailed side branch using a balloon catheter. [*Catheter Cardiovasc Interv*. 2014;84(5):750-6.](https://doi.org/10.1002/ccd.25358)
9. Kuno T, et al. Novel insights of jailed balloon and jailed Corsair technique for PCI of bifurcation lesions. [*Cardiovasc Revasc Med*. 2019;20(12):1065-72.](https://doi.org/10.1016/j.carrev.2019.01.033)
10. Varvarovsky I, Matejka J. Unintended stent extraction from a coronary artery during bifurcation coronary angioplasty. [*J Invasive Cardiol*. 2007;19(11):496-9.](https://pubmed.ncbi.nlm.nih.gov/17986727/)
11. Alexandrou M, Rempakos A, Mutlu D, et al. Equipment entrapment/loss during CTO PCI. [*J Invasive Cardiol*. 2024;36(4).](https://doi.org/10.25270/jic/23.00266)
12. Wu EB, Tsuchikane E. The inherent catastrophic traps in retrograde CTO PCI. [*Catheter Cardiovasc Interv*. 2018;91(6):1101-9.](https://doi.org/10.1002/ccd.27104)

---

<!-- _class: ref -->

# 參考文獻（2/2）

13. Shojima M, Okamoto Y, Ohta M, et al. Preliminary study of eye-tracking during the coil insertion task in a silastic model of intracranial aneurysms. [*World Neurosurg*. 2020;139:e827-35.](https://doi.org/10.1016/j.wneu.2020.05.012)
14. Shojima M, Okamoto Y, Niizuma K, et al. Preliminary study of eye tracking to investigate the differences in gaze behaviors depending on the experience of neuroendovascular therapy. [*Surg Neurol Int*. 2020;11:351.](https://doi.org/10.25259/SNI_543_2020)
15. Otsuka T, et al. Differences in gaze behaviors between trainees and experts during endovascular therapy for cerebral aneurysms. [*Nagoya J Med Sci*. 2023;85(1):50-8.](https://doi.org/10.18999/nagjms.85.1.50)
16. Abdelaal E, Plourde G, MacHaalany J, et al. Effectiveness of low rate fluoroscopy at reducing operator and patient radiation dose during transradial coronary angiography and interventions. [*JACC Cardiovasc Interv*. 2014;7(5):567-74.](https://doi.org/10.1016/j.jcin.2014.02.005)
17. Fernandez R, et al. Safety and effectiveness of strategies to reduce radiation exposure to proceduralists performing cardiac catheterization procedures: a systematic review. [*JBI Evid Synth*. 2021;19(1):4-33.](https://doi.org/10.11124/JBISRIR-D-19-00343)
18. Alexandrou M, Carvalho PEP, Strepkos D, et al. Heart rate variability of interventional cardiology fellows and attendings and changes over time. [*J Invasive Cardiol*. 2025;37(9).](https://doi.org/10.25270/jic/25.00011)
19. Voelker W, Petri N, Tönissen C, et al. Does simulation-based training improve procedural skills of beginners in interventional cardiology? A stratified randomized study. [*J Interv Cardiol*. 2016;29(1):75-82.](https://doi.org/10.1111/joic.12257)
20. Bagai A, O'Brien S, Al Lawati H, et al. Mentored simulation training improves procedural skills in cardiac catheterization: a randomized, controlled pilot study. [*Circ Cardiovasc Interv*. 2012;5(5):672-9.](https://doi.org/10.1161/CIRCINTERVENTIONS.112.970772)
21. Jensen UJ, Jensen J, Ahlberg G, et al. Virtual reality training in coronary angiography and its transfer effect to real-life catheterisation lab. [*EuroIntervention*. 2016;11(13):1503-10.](https://doi.org/10.4244/EIJY15M06_05)
22. Jensen UJ, et al. The role of a simulator-based course in coronary angiography on performance in real life cath lab. [*BMC Med Educ*. 2014;14:49.](https://doi.org/10.1186/1472-6920-14-49)
23. Prenner SB, Wayne DB, Sweis RN, et al. Simulation-based education leads to decreased use of fluoroscopy in diagnostic coronary angiography. [*Catheter Cardiovasc Interv*. 2018;91(6):1054-9.](https://doi.org/10.1002/ccd.27203)
24. Lindsay AC, Bishop J, Harron K, et al. Use of a safe procedure checklist in the cardiac catheterisation laboratory. [*BMJ Open Qual*. 2018;7(3):e000074.](https://doi.org/10.1136/bmjoq-2017-000074)
25. Simsek B, et al. International percutaneous coronary intervention complication survey. [*Catheter Cardiovasc Interv*. 2022;99(6):1733-40.](https://doi.org/10.1002/ccd.30173)

---

<!-- _class: lead -->
<!-- _paginate: false -->

# 謝謝聆聽
## Q & A

**謝慕揚 MD, PhD, FESC**
