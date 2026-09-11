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
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.68em; }
  pre code { background-color: transparent; color: #2d3436; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.74em; }
  section.abbr { font-size: 0.62em; }
  .qr { position: absolute; right: 40px; bottom: 80px; text-align: center; font-size: 0.65em; color: #555; }
  .qr img { width: 110px; height: 110px; border: 1px solid #dcdde1; }
footer: '謝慕揚 MD, PhD, FESC | Weekly CV Journal Review | 2026-09-04 ~ 2026-09-11'
---

<!-- _class: lead -->
# 每週心血管期刊文獻回顧
## Weekly Cardiovascular Journal Review
### 2026-09-04 ~ 2026-09-11

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期刊：NEJM｜Lancet｜EHJ｜JACC 系列｜Circulation 系列｜EuroIntervention

📱 每張重點投影片附 QR Code，可掃描跳轉原文（DOI）

> 本週主題：**介入與結構的「真實世界細節週」——把上週的大方向，落實到導管室的每個決策**

---

# 🎯 本週主題與固定欄目

## 沒有大 RCT，但滿滿是導管室的實作問題

**上週** ESC/NEJM/Lancet 一次倒出七個大型 RCT；**本週**回到臨床實作面——

- 🫀 **TAVR 瓣膜壞了怎麼再處理？**（EXPLANTORREDO-TAVR）
- 🫀 **純主動脈瓣逆流 (AR) 有了專屬瓣膜表現如何？**（JenaValve Trilogy）
- 🔧 **MitraClip 到底對乳突肌做了什麼？**（力學代價）
- 🩺 **HFpEF 用運動超音波怎麼判讀？**（+ LA strain 雙切點）
- 💊 **左心耳封堵後要吃什麼抗栓？**（減量 DOAC vs 抗血小板）

> **本週六大固定欄目**：⭐ Top 5 Picks｜🫀 TAVI｜🔧 TEER｜📚 Honorable Mentions｜🔬 Case Reports｜📖 參考文獻＋縮寫

---

# ⭐ Top 5 Picks 一覽

| # | 研究 | 期刊 | 方向 | 關鍵數字 |
|---|------|------|------|---------|
| 1 | **EXPLANTORREDO-TAVR** | *Circ Interv* | 💡 | n=553；1 年死亡 BEV 24.3% vs SEV 21.5%（P=0.65）；策略/存活與初始瓣種無關 |
| 2 | **JenaValve Trilogy 純 AR** | *Circ Interv* | ✅ | n=363；技術成功 98%、院內死亡 0.3%、**PPM 22%** |
| 3 | **運動超音波+LA strain 診斷 HFpEF** | *EHJ* | 💡 | n=482；雙切點敏感度 95–99%；侵入性檢查 60%→30% |
| 4 | **FIELD-PULSE 焦點式 PFA (FIH)** | *JACC EP* | ➰ | n=35；急性 PVI 100%、中位 13 min；12 個月免復發 73.9% |
| 5 | **Lancet 妊娠×心血管三部曲** | *Lancet* | 💡 | 不良妊娠結局 = 女性心血管風險早期指標 |

> **Pearl of the Week**：把上週的大方向**落地到導管室**——TAVR 進年輕族群「壞了怎麼辦」、純 AR 有專屬瓣膜、MitraClip 有力學代價、HFpEF 門診可分流、LAAO 後別再開雙抗。

---

<!-- _class: divider -->
# ⭐ Top 5 Picks
## 逐篇設計與結果

---

# Top 1｜EXPLANTORREDO-TAVR

## [Zaid S, et al. *Circ Cardiovasc Interv* 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016705)

| 項目 | 內容 |
|------|------|
| **設計** | 國際登錄，29 中心（2009–2022）；TAVR 失敗後 redo-TAVR 或外科取出；**n=553** |
| **失敗機轉** | BEV 結構退化 **73.4%** vs SEV 瓣周漏 **41.1%**；SEV 更早失敗（19.7 vs 41.8 月） |
| **策略** | redo-TAVR ≈54%、explant ≈46%（兩瓣種相近）；**跨平台**再植入為主流 |
| **存活** | 30 天死亡 8.7% vs 8.0%（P=0.85）；1 年 24.3% vs 21.5%（**P=0.65**）；3 年校正後無差異 |

> 💡 **初始瓣種決定「失敗機轉與時序」，但不決定再介入策略與存活**。第一次 TAVR 就要為未來再介入預留冠脈可近性（lifetime management）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACAUlEQVR4nO2aTWrkMBCFX40bslTDHGCO4twgR5qryUfJAQLqZcDNy6JUZXmGQCBMxfGUVlb0QVo86l9CfGTdf3wIA5L7HAdW/9LVJrJiImaudlTWo9/jLBxYC0lydWUmYm4TWcvaNaqpRyR3F5Er0A2ivAoAQH43AIuIfPXv+5+4y7i5/SQAUFDWP7ij3+Ms3KjH8vQqAKZVVVmuL//u/yb3zhriB9VfjduMH/HcTURELsByBVhxFyxX6FZEROTxW9zjFJxludtq3WYwD39M+wjioGntltuSa8+0ZnVVJObUI4qDFoAaJjCRFR5Tmp1m/AjjsBmESrGvDC3Gpx5BHDYzUFHcXLpG6a9COQ0dQFmx81duLm1i2kccZ/7Ku4i6CgkUP0g9orh91Jg8iptQQNpHJGdeqniq24Cx1d4770e/x1m4rSNi22Y2U5HxI5wbXBXmZqMPTbeay5N6RHE9o9UvjeeW+VZAi/S0jzjOSw/aQLBhCCI+uT36Pc7Ceeuqh3JrkJC9SC/ZT4zkxv5uLVvS66KU7JdEcvv3JZbv6oHJk3qEcl564PZALL/66EMerVxn/Rb3OAW371+hf3F4epX9xK/idAr1/EDgdvH0957vfQK5nX14kV7LaqUHsp8Yyf31vmS20Qd6ZZj+KpIb86sKwIZSflCyPo/kJN+3H4p7AwhCHYVr57LhAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Top 2｜JenaValve Trilogy（純 AR 專屬瓣膜）

## [Wienemann H, et al. *Circ Cardiovasc Interv* 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016851)

| 項目 | 內容 |
|------|------|
| **設計** | 8 家歐洲中心真實世界（2021–2025）；症狀性純 AR、經股 Trilogy；**n=363** |
| **族群** | 中位 81 歲、45% 女性、EuroSCORE II 3.4%、LVEF 50% |
| **程序** | 技術成功 **98%**、瓣周漏 none/trace **86%**、平均壓差 4 mmHg |
| **結果** | 院內死亡 **0.3%**、**PPM 22%**、3 年死亡 25.9% |

> ✅ **全球第一個純 AR 專屬瓣膜**（2026-03 FDA 核准，ALIGN-AR）。過去只能開刀/保守的純 AR 有了經導管選項；但 **PPM 22% 偏高**須納入諮商。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACKklEQVR4nO2aUa7bIBBFzxSkfOIdkR10y/ZSsoBI5PNJtm4/AMeuWulJrYjjwIdFzJHMBF2YYcbEd9ry41sYdO7fODTuehqDBEGSNNehMB/djrNwHkICWDzgZgNDsHgBZPVMPw9vx5m4xcyG8ltKTvC4iGkAJjN79fw+lYtpMaahPpp9t3N/5qbBiZic7IrT37n//d3OPZuH/N8vEJ9rEBIW0+bd0e04C7fzr8L8+6O07l+14tCmpbJflaHwHOnr0YirAQcAYUYjLoceuZdF0vXRikNKAEEiJiCq9siR4Qyx66MVl/WRZRBVT42orIryru9Xzbj1PHfK9yVSUYWUXD5TNPb9qhW3W4CihTqU9aG+Hg25fGzDeopnQQDEtKqnr0crrjpUCYjJZe+2nOdA8bn6erTifO242aYBg5DQNLh111peOr9P42rWY/eonpZUNdP10Yhbwz6tp0aJz/PWNfb4oymX96uahXKzAYjHgBHuXvF2EdNwP7odZ+HYqCLqmaqtdygx0ePBxly+b7fnTe8zXcg0gF3fw44zcNv73RyJhHpVQijvuj5acpOVBpQsrZRAI5uk7fHtOA23q+2RbrWUgSoXu76FHafgPLnUJ9wB3Mx0xYg3DzwMwM964fw+jfPbH+FuxDQAQbt0+vHtOCOXVYFTKfoxj9mQq7OOML9P4ep9YkkIfpnGx0VEfZnGh0fje9hxBm5fX6KNv1sTh72eoSVnvb79UNwvvxmZP2u8hAUAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Top 3｜運動超音波 + LA strain 診斷 HFpEF

## [Harada T, et al. *Eur Heart J* 2026](https://doi.org/10.1093/eurheartj/ehag716)

| 項目 | 內容 |
|------|------|
| **設計** | 侵入性運動血流動力學 + 同步運動超音波；多中心驗證；**n=482** |
| **現況** | 單用分數 + 運動超音波，敏感度僅 **55–60%** |
| **改良** | 加靜息 LA compliance（LA strain÷E/e'）+ 雙切點 rule-in/out |
| **成效** | 明確分類者敏感度 **95–99%**；侵入性檢查需求 ~60% → **~30%** |

> 💡 **運動超音波無法完全取代侵入性檢查**，但加 LA strain + 雙切點，門診即可分流大多數病人，僅 ~1/3 需轉侵入性。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACJElEQVR4nO2aUarcMAxFj+rA+3R20KV4ttadJUt5Cyh4Pgdsbj/sOJlC4UGpJ83YHyEkBxJFRNKVZeIrK3/7EgaD+zsOLc9nQZIWLxGUtls+nd2OC3Feksq3dwKyEWJ1jyRJy39hx2W4bGYzECLAfYJ1zmY3gNXMXv1+78qtc7YatD4nWOdOzx3cvqbDeVCewKfJ8ML+6XMH92fOSYoA949SbUmfVpIIQdKr3++duKf6yqffD3WN+qoXNxF2BXL/kIWISlKv5RYw9Ec3rv4GJTZFp1bgAj4hRafxf/TjqNJjEyGHUFXKXy9pGf7oxRXFt2lxJ8CpSsEI4BMEDX904tCC0x6qysWgVMLX+D86c5s/mgOKZ6IrTSwplpB2djuuwrWw1IKWl2rqALZrwx+duC2BA3tBVfO50vBHb+6QP+pBiT2TtGx/djuuwpX+ldYZA7JpNbCw5AlwycClV77f+3FBD6NWue6QOoowCTGPfntH7kn70TYJ41GYjPqqH7d99q3ALQ5Ymihc/PBHT+65oFIJWrUG3pHhj15c3SFXm2Jo/ZIqzcvZ8Ec3brW6gLZfG7fJBmqOP78d1+Am8BEgT2X/Ax8x/N5eBNb559ntuAq3bQP61CJXdcWu2Ue8eg232oTd7nXEwW5egvvHmL96GZdNP75Lkh5tnuEx9GBHjtpWr7KvtnvLVIlPezf+7HZchXueL9lr33SYFx3+6MfZmG8/FfcLmWXDKZSAijcAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Top 4｜FIELD-PULSE（焦點式 PFA，首次人體）

## [Reddy VY, et al. *JACC Clin Electrophysiol* 2026](https://doi.org/10.1016/j.jacep.2026.09.001)

| 項目 | 內容 |
|------|------|
| **設計** | First-in-human pilot；次秒級高壓（≥10 kV、<200 ms）QRS 同步焦點式 PFA；**n=35** |
| **急性** | 急性 PVI **100%**；每人中位 39 次脈衝、消融時間 **13 min** |
| **耐久/安全** | 波形 C 每肺靜脈耐久 **94.2%**；腦 MRI 無 DWI+/FLAIR+；無溶血/AKI |
| **療效** | 12 個月免於房性心律不整 **73.9%（60.6–90.2）** |

> ➰ **早期可行性佳**：兼顧「彈性病灶設計」與「不需長時間導管穩定」；仍需大型 RCT。理解 PFA 技術世代演進的好教材。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV4AAAFeAQAAAADlUEq3AAACoklEQVR4nO2bTW4bMQyFHzsDeCnfwEeRb9Az9WbSUXKAApplgBm8LkjNaJwGSF0kZQFyEdjRtyDwQIl/FuLDtn37OAsE/DUwWI5PaQUySZZEIjcAmWs/T6sTnwN+gBNJqlATAWwCLDP440aiXgGSJIsnnwM+TCMPaQXJFWSDfkUmqQfFOCc+B/weXOVC1JtdoCzL/E/cCPiP4FGkzE2YG8AqAJBe5avcCPiv4Il2dy4XooqI3BMJLDN6OkN+vhsBPwU/5qK/+2MW76BLeEY+V4S5gQLMkNxAWH4KIOpBn3CvAhv2UtDqChZMRNb8dGLEoFO4lw+7ZADQxaMqqPqGgj5haP8FMC3JNmkgqrSWxOj/nPgc8MlMqNZvzJLYL9AGANpfi1vULWyPXG57DHKFdtoKsH+aSDIU9AjD5NEo467l1NvbpJ3mUNAlPPZFy0NzFP1FLNb8duJzwCfrkk3cG9joNUSv9/VrKOgSHoPuSGd43J0NR3A68Tngkx21n76Iw+vXS8F+EAp6hMeejA0JOXRijnFhxKBvuF4n64HWq83o5Z5edUqxN2t8+Ryw2hGDlnfC6oph86KfOvE54NFswltvhOSXC0VHFcu8on7/CejaTFrnz3Uj4Kfhnotq1jK92VCzTAaIrppTuCcsutVkq01Dh9TaMYxc1Cs8voPsq6KjbkpFNeEW7tV7rweBnsnYeXS23cNVzHQ5LbdNWBYRmylZJgO5O/I54MNmIDUA2Gbd1K43zTtBYN/jXgT8VDcCfho+7WwfTRjsk0IA++TCic8BvwfXKyB3WCNU7gBsZvhyodxd+hzwabE+NbBep1WATVhlouSyzRqDsW3oEz7Gt+Om07HuNCwfxi3qEj7tbAO9mN/3DofVtagmXMISv+H9z+Ff1rR0ux4ktAEAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Top 5｜Lancet 妊娠 × 心血管三部曲

## [Brazile TL, et al. *Lancet* 2026（Series 第一篇）](https://doi.org/10.1016/S0140-6736(26)01234-1)

- **三部曲 Series**：①孕前生理與全球負擔、風險分層 ②妊娠高血壓（最常見）③不良妊娠結局 (APO) 與終身心血管風險
- **核心概念**：妊娠是心血管的「生理壓力測試」；**妊娠高血壓、妊娠糖尿病、早產**揭露潛在易感性
- **臨床行動**：把**妊娠史**納入標準心血管風險問診——把預防「上移」到年輕女性

> 💡 一位 40 多歲女性若有子癇前症/妊娠糖尿病病史，其心血管風險常被系統性低估。呼應建立**產科—心臟科銜接門診**。（第三篇：[DOI](https://doi.org/10.1016/S0140-6736(26)01235-3)）

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV4AAAFeAQAAAADlUEq3AAACkElEQVR4nO2bS4rcMBCG/4oMvZQhB+ijyDcLuZl9lD5AQF4OSPxZ6OlmCJMJPVSgamGkmW9RUNRbLcSHJX/7OAsY/DUwuPcT4/ibY/mQqf3fJyU6G3wR7p7FUOU0rlXaaTcLqoWziKwAcIrIhiyywbFdARwi8no1DP532CcgRIA/1yw47ulP8OvUMPhv4GU6h8cCHAIIvCNw3ijH+usr1DD40/ACwBFABgCXAOQFYc8LQvwOAhkIfLUaBn8anmvR3ad3P1WsklEJ95JzLkMBTwKeVzEL6oSPFQCQBUAW2c4buZ9SryIivSpVo7PBk5DREYArPoiaFl1NfYFkCbTBfFAljBI2Qxu9VGtFx5YHWU8WRXXCZYJWXI0kq/HQnDOQbXJqlYxKuFpwNPPFbu1TbUnSLKgUnlytxtPopmloQwCzoFL4mgdd3zX1PIjmg1bJ6ISLD9Yy1JMllI4iht0lbTehFT7WXDo+hEdZQUC2s81LjxUQWYtzqtHZ4EnI+FTOOJagGmr9YnlQNTxveGtvj1KVTqdyNQuqhNsCHsPz0mgf+nsLwCyoFz4XAP5NgPNG4FwgG7IgPG6UH0yQDY4IUZHOBg+Zp6Ge0zjmaWBqUzWlcN0A9sQ3GS+M3OiTTbbVwzXdyebfROSeWiNxn+yrTWeDgXcaiTi6/LGetyiqFr7u6FMPqq5PZ9hsabWoSnjBsdUjw+NGCTHXK5AWgc8L69Ve3WuEF8BHAMhljsZDHHGsEB4bgFKk1iGbEp0NvkgPkb2P59xX7IVytpvQCl8sGHs30QczoXUTtptQCl99sD00LPO1OL+DskpGKfw82a6OOFb2Y0FhUVQlfH2zzelp09RItI2TEp0NnkXsN7z/OfwbLrd10B7MJ+gAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🫀 TAVI Section
## 結構性主動脈瓣方向
### TAVR 失敗再介入 × 純 AR 專屬瓣膜 × 瓣外損害

---

# TAVI #1｜TAVR 失敗再介入（EXPLANTORREDO）

## [Zaid S, et al. *Circ Cardiovasc Interv* 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016705)

- n=553；BEV 失敗多為**晚期結構退化**、SEV 多為**早期瓣周漏**（且更早失敗）
- 再介入策略（redo vs explant）與 1–3 年存活**與初始瓣種無關**
- 「跨平台」redo-TAVR（換另一種瓣膜）為兩組主流

> **對 Drake**：TAVR-in-TAVR 與外科取出並行；**第一次 TAVR 就要為未來再介入預留冠脈可近性**（lifetime management 思維）。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACAUlEQVR4nO2aTWrkMBCFX40bslTDHGCO4twgR5qryUfJAQLqZcDNy6JUZXmGQCBMxfGUVlb0QVo86l9CfGTdf3wIA5L7HAdW/9LVJrJiImaudlTWo9/jLBxYC0lydWUmYm4TWcvaNaqpRyR3F5Er0A2ivAoAQH43AIuIfPXv+5+4y7i5/SQAUFDWP7ij3+Ms3KjH8vQqAKZVVVmuL//u/yb3zhriB9VfjduMH/HcTURELsByBVhxFyxX6FZEROTxW9zjFJxludtq3WYwD39M+wjioGntltuSa8+0ZnVVJObUI4qDFoAaJjCRFR5Tmp1m/AjjsBmESrGvDC3Gpx5BHDYzUFHcXLpG6a9COQ0dQFmx81duLm1i2kccZ/7Ku4i6CgkUP0g9orh91Jg8iptQQNpHJGdeqniq24Cx1d4770e/x1m4rSNi22Y2U5HxI5wbXBXmZqMPTbeay5N6RHE9o9UvjeeW+VZAi/S0jzjOSw/aQLBhCCI+uT36Pc7Ceeuqh3JrkJC9SC/ZT4zkxv5uLVvS66KU7JdEcvv3JZbv6oHJk3qEcl564PZALL/66EMerVxn/Rb3OAW371+hf3F4epX9xK/idAr1/EDgdvH0957vfQK5nX14kV7LaqUHsp8Yyf31vmS20Qd6ZZj+KpIb86sKwIZSflCyPo/kJN+3H4p7AwhCHYVr57LhAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# TAVI #2｜JenaValve Trilogy 純 AR 真實世界

## [Wienemann H, et al. *Circ Cardiovasc Interv* 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016851)

- 純 AR（無鈣化）過去是 TAVR 禁區——沒有鈣化就沒有錨定
- Trilogy 用**三個直接夾住原生瓣葉的定位器**解決錨定；2026-03 FDA 核准
- 真實世界 n=363：技術成功 98%、院內死亡 0.3%、殘餘漏極低

> **對 Drake**：開啟過去只能開刀/保守的純 AR 介入大門；務必納入 **PPM 22%** 的術前諮商與無鈣化錨定的解剖評估。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACKklEQVR4nO2aUa7bIBBFzxSkfOIdkR10y/ZSsoBI5PNJtm4/AMeuWulJrYjjwIdFzJHMBF2YYcbEd9ry41sYdO7fODTuehqDBEGSNNehMB/djrNwHkICWDzgZgNDsHgBZPVMPw9vx5m4xcyG8ltKTvC4iGkAJjN79fw+lYtpMaahPpp9t3N/5qbBiZic7IrT37n//d3OPZuH/N8vEJ9rEBIW0+bd0e04C7fzr8L8+6O07l+14tCmpbJflaHwHOnr0YirAQcAYUYjLoceuZdF0vXRikNKAEEiJiCq9siR4Qyx66MVl/WRZRBVT42orIryru9Xzbj1PHfK9yVSUYWUXD5TNPb9qhW3W4CihTqU9aG+Hg25fGzDeopnQQDEtKqnr0crrjpUCYjJZe+2nOdA8bn6erTifO242aYBg5DQNLh111peOr9P42rWY/eonpZUNdP10Yhbwz6tp0aJz/PWNfb4oymX96uahXKzAYjHgBHuXvF2EdNwP7odZ+HYqCLqmaqtdygx0ePBxly+b7fnTe8zXcg0gF3fw44zcNv73RyJhHpVQijvuj5acpOVBpQsrZRAI5uk7fHtOA23q+2RbrWUgSoXu76FHafgPLnUJ9wB3Mx0xYg3DzwMwM964fw+jfPbH+FuxDQAQbt0+vHtOCOXVYFTKfoxj9mQq7OOML9P4ep9YkkIfpnGx0VEfZnGh0fje9hxBm5fX6KNv1sTh72eoSVnvb79UNwvvxmZP2u8hAUAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TAVI #3｜瓣外心臟損害 (CD) 與 AS 嚴重度

## [Coisne A, et al. *JACC Adv* 2026（VALVENOR）](https://doi.org/10.1016/j.jacadv.2026.103227)

- 法國 VALVENOR 世代，n=1,747，追蹤 5 年
- CD 分期 >0 者峰值主動脈流速較高；**更高流速獨立與 CD >0 相關**
- **CD >0：全因死亡 HR 1.75（1.44–2.11）、心血管死亡 HR 2.52（1.79–3.55）**（跨所有 AS 嚴重度）

> **對 Drake**：AS 預後不只看瓣膜，更看「連帶損害」。**CD 分期可能是『何時該處理 AS』的一塊拼圖**（呼應 early-TAVR 辯論），值得系統性納入術前評估。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV4AAAFeAQAAAADlUEq3AAACpUlEQVR4nO2bQYrcQAxFv1KGXpYhB+ijVN9gjhT6Zq4blZcNNj8LqVx2yGIyYSYKSAvTjd9CIKTSl8pCvNv2b+9ngYC/BgaX4xdJorRELkhE4QZ9qOXNic8Bn20CcgOAfQLWGQB2AQDw+kB98+JzwL/Cu4jMAOps6Ue2XQAkygMAqoh8vhsB/z2cX4J6f4nIndS41fnr3Qj443CiPkrbpZ+I/8CNgP/EuGSS5GY9TSEJ5O38giS5RCfjFV5FRGSCxu0579Izb9cqKiIi8vDkc8DDOGzJln4oJMmWaL/UIgc9wuCSTfGRLZFsAEqzF+e3EUGXsMVNNQRpSbdk0/Ym6xsQit4p3LOsP0Yp1aguWZuYyEGvMOy4a+k4DMc5CAxJEb2oU3hCfdsAnaXlBikNFGCfCKRNNDn1lxefA76Y9S+kinkTEplnMa/j7chBlzB68LoVbr2yHiofmUSJc9AlrDHSkAGmJoaGMCQ6Gb9wH5kB6GuJLgqtlPbQRifjE4a1nL2Umo4HThPSQ+A78Tngi5304BHGLi62fkpGFXUNr7deLFc5dkq7iMyJth9cJ6DOjnwOeFifqgHQ1eCYcQNHXqboRb3CvdFsiWM6owffkBmqK+IcdAnbOWiz69669OYTVl71lIwIeoTRZ9fXZcQxF8VpUR8R9AyvIqj3DXzOidq6qB7UDf6NItHJuIQvO3pc9rqmAvu+IuaiPuHLne3RyRzDUYyARhV1CZ/vbNdHAusMYZ0bYbe3rajyU90I+MPwaSbTr1po1/IboRg56B7OL/1kQkRuRJ13kR8tkUt+CZ/RybiEp/Of9WbjbayzoLTvmyC/BKWBKC2+PvMIX65mN1gBHfvB0u/OhB50Cp97Uf1qsPWN07hq0ftTJz4HfDaJb3j/c/gnIwhx35kl1loAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 🔧 TEER Section
## 二尖瓣與三尖瓣緣對緣
### MitraClip 力學 × 高齡評估 × MCS

---

# TEER #1｜MitraClip 對乳突肌的力學代價

## [Park MH, et al. *Circ Cardiovasc Interv* 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016161)

- 體外左心模擬器 + 力感測，豬二尖瓣 n=8 隨機配對
- **MitraClip 降逆流，但乳突肌 (PM) 峰值受力較基線增加約 23%**
- **外科 neochordal 修復可把 PM 受力還原到近生理值**（各法皆將 MR 降至 <15%）

> **對 Drake**：**TEER 不是「零成本」**。對較年輕、可外科修復（degenerative prolapse）者，neochordal 在瓣下力學上更「生理」；為 M-TEER 後長期瓣下重塑/殘餘 MR 提供機轉。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACHUlEQVR4nO2aTYrjMBBGX40NvVRukKMoNxvmZvZRcoABeRmw+GYhyXGaXgSGUSee0iJY8gNHEvXzlWTimZZ/PIWBc3/HoWn3NEhK24/W9iqsrz6Po3BoCiprL0l66N7HfD86ctnMTgBkg8UMgDI2W+m+wzyOwI275/kyyACMkATkf/dd557gws2IkjTR7KPLd5174AZJ6T6UzX5exxroo6Tv/n//EzfCYru+5tNvNJ9vJoD6Krz8PI7C1QyqpFEM+0xr3zy/6sTVfHcKKxB2goPmwwbPdztyaArVIEo/pkH3F7X5fvTiquybwgox0XYmSDWUB9eDPbnir8qyK93d1z6muH305bJpIhswCMhGTNnMbISoYjjvMI8jcLSyYUutJgZV6ZG2aqPbRy+urHgJ6hMgpUF3kd58mO9HJ65pjbTZR8t8W+iQx4+OXMuv2GyhPVF9mER0PdiLa6nuZiQT1Che5aHnVz25duL0aezBfXn86MfV849YNHketyqiqaa/g8zrid24z/lVVYZb+cTrV325h/pu2IpYxVU1pe770ZGbrTaKUg+Sfp2aUm/H6a8/j2NwI4QEkEfi9UMWr+NqBKCmVgli8vtXHbl2v2Q+35qRNNOwyzJidnqLeRyB2wvyehWOJkf8fPCbuXAz5vMKs42U+i6LmdtHX+7xfsnyIQi34rTsUkTIW8zjCNzX93frWNWDXr/qx5nfb38p7g/NwdcS0WRZ7gAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# TEER #2｜高齡族群的 M-TEER / T-TEER

## [Alkhatib B, et al. *Circ Cardiovasc Interv* 2026](https://doi.org/10.1161/CIRCINTERVENTIONS.126.017207)

- TEER 病人絕大多數高齡衰弱，但試驗對衰弱/認知描述不一致
- 應納入**老年心臟學工具**：CGA、MNA-SF、Katz ADL、KCCQ、認知篩檢
- 術後結構化復健、早期活動、譫妄預防、照護者參與

> **對 Drake**：建立 MitraClip/TriClip program 時，除影像與技術外，**術前加做衰弱/認知/營養篩檢**，把「有意義的餘命與功能獨立」納入 shared decision-making。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACA0lEQVR4nO2aTYrjMBCFvxoFslRu0EexbzbMzeQDDSjLBpvXC/1gZxhoGEZJu0sLY0kfxKJQvdKLTHymbT8+hYFz/8ah1N+kFSkHKRHEpLVNxfXV13EWDqUolVCkuFJDkYNKV5KUPB4juc3MbsCUAeK7AWA/M7CY2bO/7ztxl4e+TRkZcX0Yf/V1nIXbx2OZg2yxsApAy+33//td5/7SdvqhHNTa2uTd9WMot6+vip4fHrV5PEZxaNdyG0tRYtrNeDwGcfsNIUkQV8rRYyqpSmLyeIziqkwkQheRrimZdjz0fDWOW+wCxHczs6tsjitwNzO7BZWJ+Sus4xxc04ocqmDUnVKyFJ6vBnNUFW9WiRJdU6j5yuurcVw1rGgFVR2NXdldP4ZyTcCh+1ddyou/6/tjJNfPg62+erTaa/fV13EWrirElOl+SZOOhOvHcK6fAotNVU+B+xgVeX/1dZyF29tURT+AWuqWN/n+GMjVenfKQYcuPSiuHyO5bl0drJLyAGq55fEYxe393VRGgppr1TTF89VAbrHaqqubNzO7bQZsBvernvt9345r/w8CoF9vtciymaYp6Uus4xQcPSMdTPfd1Sv3E5/FTRlsvl8F90szttj8vs9A7s/90a7CNXvR/cSR3PF+CfQEBdW68nw1kjveL1G7JZr7RPTz+UjO/H77S3EfNrYIjUH1tlAAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# TEER #3｜Impella 支撐下重度 MR 的經導管策略

## [Isawa T, et al. *Circ Rep* 2026](https://doi.org/10.1253/circrep.CR-26-0155)

- 日本仙台厚生：重度 MR + 進階心衰、需 Impella 支撐（n=33）
- 經導管策略（M-TEER，n=17）vs 保守（n=16）
- **院內死亡 HR 0.13（0.03–0.52，P=0.004）**，favoring 經導管

> **對 Drake**：「**TEER × 機械循環支持 (MCS)**」的真實世界佐證——用 MCS 穩住血流動力、再以 TEER 消除急性重度 MR 的救援/橋接路徑。務實界限：單中心、小樣本、回溯。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACDUlEQVR4nO2aTWrDMBCF31SGLlXoAXIU5Wq9mX2U3kBeFmReF5qRlXYTKFUdd7QQif2BLR6an2cJcc/Ynu7CAOd+xoFz+8UcSJIEIgnEYrdiOfo6TsRFkmQBgE2AVQSAClX1mR9iHafhNhF5AQAEilxIYJ30/iJVnkdYxxm46ct/TScxQxB/8bnO3cHFDwGwCdK7yJ5Yfv25zu2Ds+UPzghEysFKrlgsf3g+H8X19dUcy9dJh+sxitMdoMNUSBlA6m8cfR1n4Wq8Qsq2U2q8iqSGL9djKNfCkmWNlFtn2H55/hjGgcxA7cVbKq/XVBkAyffHQK7FJuBGnuVSIHIpf/1+/4qziIQ9f3yLV15fjeO0tiVZW4/qZCWS++T5fByn/WAVJbf2MAPWIwK+P8ZxsFDVatsMU6YCgZ7Px3ETEgFRq/21ALFMAEKx6W/f7x9yq8he6sp1fabIRZ1Fua4T+PbyCOs4BdcbJIB+H+zLrfq50OPVIM78qxxaQVW6L7fVTXE9hnHmX7G0rnz3rwAz3V2PQVzv7/ZNeuBeCPv+GMktokNd9prZN7EpECk/wDpOw7XzJYt6VZBrLJArAmv1tXh9NYpDi0i7t955Wk2to6/jLFyvh+YPtRKtBob77QO52/1xc7yh60Q8n4/ibgUo0KOi0MjVepKjr+Ms3LfzJbR+0C67nziSEz/ffijuE+Uc83cWdKHFAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 📚 Honorable Mentions
## 其他值得一讀

---

# 📚 Honorable Mentions（1/2）

| 主題 | 重點 | 連結 |
|------|------|------|
| **LAAO 後減量 DOAC vs 抗血小板** | 減量 DOAC 優於 DAPT（降死亡 HR 0.79、大出血 HR 0.87）；與單抗相當——**別再開雙抗** | [DOI](https://doi.org/10.4244/EIJ-D-26-00102) |
| **CT-FFR 性別差異（TARGET 次分析）** | 男性減少不必要 ICA；女性 2 年 MACE 較低（adjHR 0.48）但交互作用未達顯著（探索性） | [DOI](https://doi.org/10.4244/EIJ-D-25-01383) |
| **ELAACC LAAO 多模態影像共識** | LAAO 術前/術中/術後影像整合地圖（CT、TEE、ICE） | [DOI](https://doi.org/10.4244/EIJ-D-25-01372) |
| **心衰預測新型風險分數** | 評述近年 HF 預測分數的定位——協助分流、非取代臨床判斷 | [DOI](https://doi.org/10.1093/eurheartj/ehag644) |

---

# 📚 Honorable Mentions（2/2）

| 主題 | 重點 | 連結 |
|------|------|------|
| **CAR-T 心血管毒性分層（CART-8）** | 從 CART-7 到 CART-8 更新風險分層——「告知、而非限制」CAR-T | [DOI](https://doi.org/10.1093/eurheartj/ehag710) |
| **LBBAP 後急性 TR 惡化** | n=239；約 1/10（11.3%）出現急性 TR 惡化；AF 與導線-三尖瓣距離短為獨立危險因子 | [DOI](https://doi.org/10.1253/circrep.CR-26-0148) |
| **美國 ISR 治療趨勢 2009–2024** | 支架內再狹窄當代處理型態演變——ISR 仍是未解難題 | [DOI](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016533) |
| **心衰與神經認知障礙（回顧）** | 心衰與認知障礙雙向關係、機轉與照護意涵 | [DOI](https://doi.org/10.1161/CIRCHEARTFAILURE.126.014265) |

---

<!-- _class: divider -->
# 🔬 Case Reports
## 結構／冠脈介入 × 5

---

# Case #1｜緊急 TAVR 橋接活動性 AV 心內膜炎

## [Attumalil TV, et al. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.110231)

- 73 歲男、雙葉瓣 AS + *Gemella* AV 心內膜炎、大贅生物、根部假瘤、重度 AR、心因性休克、外科禁區
- **緊急經股 TAVR** 穩定血流動力；3 週後行外科根部修補與換瓣，完全康復

> **教訓**：心內膜炎向來是 TAVR 禁忌，本例（文獻首例）示範在極端情境以 TAVR **橋接到手術**的救命暫時措施——高度個體化例外，且務必規劃後續確定性外科。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV4AAAFeAQAAAADlUEq3AAACpElEQVR4nO2bTYrcQAyFP8WGXpYhB5ijuG+QI4XczD5KblBeNti8LFTln0kWkw49VEC1GHq6v4VASHp6ZZv48Nm+fJyFgD8HRtP+SRmATproxKgV/+MnrY3EHPDlaEqSpBVJK4wZgO70nSRJU2SwWXgzswGY7Sb9GDpJeTOgk90BZjN7fRgB/zucVuy7Hmb2Jnne5uHzwwj4aXgxKyMwb8aYOx1T8hPDCPhv4U5FxCTJzHq88ua3OhZHSa8PI+Bn4cXM8wabaUoPq5W3eRc1MzO7txRzwMfRcSYA0upFJ+VOVam6XG0k5oCv8DxsXmSMWpF+9sBixvz2MFyphhZtF/Y9vtbbCiR55THmfa3PEBt9o/DuxMApeaQVTdQuOiXf7RuJOeDL8QyOuhozPgfhWCnCk2kY7nx7N7Meu9MJKJ6MC5vqzjQUc8D78RY5ed7q4PN+ujPlu6jBFmHK4KufvGOqiphj1WeMOdgkTJUp0p4oiip9j0QGW4TZZcq5GvfKO9prKJl24bRi9+VWLutHrcUXHTPYPT3Mje5XhxHwczCn+/jSRcsyf1zu+noYXbRNuNgxUk2eZyvDpYtCaNFGYQ4/u67wZ31aL5a6cLZbhYvuHGshntIo6TQbQ8k0Cu8ytHhp9eG0YnSXLuq/RgZbhH/zZHY5cxqG1TBtJOaA/wSnh/k907SYwdJTlIzf4N9kNrQWc8DA9Y6+NMt9Nu5OWwpftFn48sy2zsPQzVFOUzIy2CLcQ8oAW8/8LYt5yGge8uWKaelfHEbAT8PsLfK6V6z1yQunYh9sFr5ksO4QlNdfqHf0KfbBZuH+8t9mYrkJlsEY89fVcGcbMeZ4+6xF+PLu0rneys9jFanRRRuFz1rUP71zts/PHTYSc8DnY/EO738O/wLeRXMBORnq8wAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #2｜AngioVac 抽吸橫跨 PFO 的移行血栓

## [Nallapati CS, et al. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.110222)

- 19 歲男、何杰金氏淋巴瘤、大量 PE + 心包填塞 + 心因性休克、需 VA-V ECMO
- 橫跨 PFO 的雙心房移行血栓；外科風險過高 → **AngioVac 真空抽吸**
- 加**雙側腦保護 + 暫時主動脈血流阻斷 + 中隔封堵器圈住血栓**，無中風

> **教訓**：跨 PFO 移行血栓有**肺+體循環雙重栓塞風險**。經皮真空抽吸可行，關鍵在**防範系統性栓塞的「組合拳」**。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV4AAAFeAQAAAADlUEq3AAACpklEQVR4nO2bTWrkQAxGn6YMWZZhDpCjVN8gRwpzM/tAA9XLBptvFvVjm5lFJiGhAtIitOO3EIiS9EllE2+2/cfbWXD4a2C09F/KAARpIYikjfKnWNwG8dnhi2mJkqQNSRIpAxD6/+oLLR7BYeHdzGZgtQn9moOkvBsQZDeA1cw+3w2HPw7Hh9mrHmb2LJW4rfPXu+Hwu+H7k/RrDiLl3Ug56KiSX+iGw/8DT0AQsAMxYzBtrPNvWF9aE5P02W44/BH4bmZmE8BuWuLD2snbDQAzM7PbSD47fJgOWwAtcYMkScpBEI/33ouOCNeQAUU5FDWRcn1xfTuIzw5fTMog5aAarShpiRIpd1mfwRX9oHBPmxuUcUyUIG5oaY/lNPoZHBPuU7Wgehp11EE4JIXPZAaG6xDG7FmyWxUXZSYDsR5Ouw3ls8PdWq9yOYOlGHam5Fg/g0PCreWk6YryqzUxNYxRInkdHBI+C8BjS9E1xIF4JzMo3FvOre6ZFvqmsDwGUZtUj+CIcCt8XUgcuTOp6oou8Afx2eGL1eFZt6Lj87HhbfLQs+iYcNvR9/lLiVaGSxYF70UHhWu0UrtR0TKmatxKKq2XLgbx2eGL1V60pM0+Dc20BAo1vl4Hx4Sbcjh60Xg0NnU4WtsZP4NDwl1DhFIM60Hsc1FON9k8gqPCu0F8nPbxcJ+onUzZ4D/JbB7JZ4e7nXf0bc/UaiOXzOp1cEj4rzvbZUevrQnFvqj3OjgmPEHMAPvE+iJYZ9A658uK6T59shsOvxu+9KLAuXU53Rd1PfhN4CoFzexJrPNu9lou0DyM1TuZIeHp8rSbVgubuM9Gyj83Iz6MlBEp+9dnI8KXb5f6PPvYD6bWpHoWHRQ+96ILfZub4R/3Dgfx2eGzmX/D+83hP7MxfJ9pBQCpAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

# Case #3｜LAAO 術中「復律後左心耳滯流」

## [Ivanov A, et al. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.110205)

- 三名 LAAO 病人，電復律恢復竇律數分鐘內出現新的左心耳 SEC/sludge/疑似血栓
- 以**超音波顯影劑**區分「緩慢完全顯影 vs 持續充填缺損」，據以個體化**部署或中止**

> **教訓**：**復律後數分鐘可能出現新的左心耳滯流甚至疑似血栓**，貿然部署可能封住血栓或誤判。顯影劑能區分慢速血流與真血栓——可立即改變術中判讀習慣。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV4AAAFeAQAAAADlUEq3AAACq0lEQVR4nO2bS4rkMAyGP40DvUygD1BHSd1s6CPNDeIDNbiWBQn/LPxIUsyiaaYKN0iLkMe3EAhb+iXHxJdt+/V1Fhx+DYyWdqcEQJAWgpi1ki/ZxrUTnx0+mZZRkrQiaYU5ARAO7yRJWjyC3cKbmU1AtAF9TEFS2gwIsitANLPnu+Hwt+Dh9BRWm7UZjIJ4BeL0+Qo3HP6fcBBz2ow5Be1Z8uVuOPx1OKgUMeMK3AaIExAvNS3Okp7vhsPfhW9mZjYAbKaPy93qytuMOIGZmdm1J58d3k27LflxzYtOSkEn81q0RxgtY1F8RTkk8t6pZVwfvnbis8MnkxJoIahEa5S0jBJzarI+gSv6TuGyymqMssAvdzmqWcz7GuwVbttmaIlvz4P1w0KOdCc+O/wIBxEvdzO7rNiVIKD0ZIrCKN2Zjnx2uFlVDkFV+7Vk2Jjyztdgj3BNfLQedwKpFjEljKPE7HmwW3iz1nXBruMK8XI3opWmqRY209KVzw4324VEqTtpk8L8GAQF6cRnh0+Wi8/zXDfvnXldVq3hEewULjmvlZxVwu8T3ioPXQ/2CbcBvFRlfZWCx10UvBbtFKY1XEpVOreAAm2wFLyz3StMyX77HCIVZVg2UKDkRl+DXcKnRmg98wR7fdoaM64H+4TZA7UPBA99UY4n2Trx2eFHOAjGu+UX+VzabaBUMnmC/yazqSefHW52nNEftV+7qx+8Fu0TPp3ZrhtoLl2aUCwB9V20S3iAMQFsA/EKitPnoDil04jpNjzZDYe/DdO2yMOcqZ6Y2c+Luh78MbCkFTN7E3HazH6nIC3j3YheyXQJDw/PNv95X8VtMub0vhrj3ZgTYk7+91mP8OnfpdbPbmcMa5PN9WC38LEWXWht0gT/OHfYic8OH838H94fDv8F3Sp8qcplnccAAAAASUVORK5CYII="><br>📱 Scan DOI</div>

---

# Case #4｜瀰漫性冠狀動脈擴張症合併 ACS

## [Gonnah AR, et al. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.110203)

- 72 歲女、瀰漫多支冠狀動脈擴張症 (CAE)、下壁 STEMI、8 mm 擴張 RCA 血栓阻塞
- 抽吸血栓恢復部分血流後，**因瀰漫擴張、持續血栓、貼壁不良而放棄置放支架**
- 改以 DOAC + 單抗出院

> **教訓**：**不是每個 STEMI 都該（能）放支架**——擴張血管內置放支架的 malapposition 與再血栓風險必須權衡。抗栓需個體化 + 長期影像追蹤。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV4AAAFeAQAAAADlUEq3AAACnklEQVR4nO2bTW6mMAyGHw9IXYYbfEeBq/Vm5ChzgJHC8pNA7yzyA7SbqppWqcZeRECehSXL8U+MiQ/L8evjLDj8XXC0IvlDnI72BMBR96d+dHb4IlqDJGnPT8wJtDJISpA3JElr2DvR2eG38GFmE8A2otdpEHM6DIJkC0AsHtqRzg5XGW9vh0FIQKjhMU5/vkMNh/8JPKchG84WDssuuX6/Gg5/Og4qDcrLGvYaDD0O9g9vZmY2Qnw8LS9ZwtOIE+RUdOlJZ4dP0Slr2GFuTidJEM4X98E+4Vb2AaB1G7FlMyNOh2ndzLKbLh3p7PApI2zjbjCIOSEj7CMEYQSwWUBcvloNhz8NIyVgTgAMymU9LZNZQzle/RTtFKbknddwx/l0Vhiei3YKt75ZNeP6ZjedyY5bsEe4HpYMymno6ZJr2Asi7YD7YJdw6WcDMEu1n52aQQEIErP7YLfwYcXpNjPiQ7IlPA0YRElSD9Pr1JPODl/gbQQ4svFgM9O6je1+EIj2oi9Xw+HPwTWTSS0YprqT09Cwl3TGc9E+4VIP5qdbL61Ev0StFt2CXcL1Zl51AW4Ffl7ALdgpPALHqGigOCXyDW98CIPDmAUGw45POvUNB4n5d+lil3QGINqI1pya9qazw0CrB/PFUu2llQ5paY7WXT9Fe4SprZdB72WnFfPe2e4VvkwWFglnLrpfvrkFO4Xf39EnaMfmrUPquWiX8GUaLZeCs9qoRavoV4+DXcOhxbxtRK+5gzaI+CgBMjfeovdFu4RpR2T1wdRmDFMr5svcYSc6O3yTmwXbbGitJi7NUe+L/gB4e1H5dyk8bzPb24ts6VPn/x6+zWxfqsC65F6pTzr1C19z0ZU6+JTLw1xIlNjouWinsPk/vD8c/guIhnTqnBh8ZwAAAABJRU5ErkJggg=="><br>📱 Scan DOI</div>

---

# Case #5｜MCS「上機前先想好退場」

## [Mackey R, et al. *JACC Case Rep* 2026](https://doi.org/10.1016/j.jaccas.2026.110245)

- 58 歲男、下壁 STEMI + 心因性休克；主動脈開口血栓無法血運重建、既存嚴重心肌病
- VA-ECMO 作「橋接到決策」；**上機後才發現每日古柯鹼/酒精** → 排除移植、家屬撤除維生

> **教訓（作者明言）**：不成比例的雙心室功能不良應觸發心肌病評估；**啟動 MCS 前必須先建立明確的『退場策略』(bridge to what)**——避免「上得去、下不來」。

<div class="qr"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV4AAAFeAQAAAADlUEq3AAACiElEQVR4nO2bTYrcQAxGn2LvbcgBcpTqG+RMuZl9oIGa5YDNl0X9uNzJYhgygwLSoml3v4VAlEqfJJt4t53f3s9CwF8Do61/kw6ASdqYRNJB+Si2HE58Dvhm2hZJ0oGUJ5EyAFP7rXxI2iKCbuHTzFZgX0G/1klSPg2YZA+A3cw+342APwTPT8+WdBosgv0B7OvLV7gR8L+EJ5HyaaQ86bolv9yNgN9pwz24LRIwCZbjdkHGPegafjUzsxngNG3Lm7WTdxr7CmZmZg9PPgd8mS7bAFgOSJKkPOlmcQY9wmhbquIrejBlyoe2kkqHf534HPDNpEyRgjVai1RuxJS7rM8Qit4pXHsy6WrHLGqVTHsspzHOoE+45sk0Xnf9HoRLUkQt6hSuvTRaAiVJJXfWJlspcQrixOeAb9aUw6SnWA5ivuTYiKBLeKg2yxkE+vE7WnzL4YwIeoSHe7BmzCcNkZuuiErGJ9xLzjF3liKmPk6l0xaVjFO46/g+182Xwqi6ogt8Jz4HfDOpB4pLx+drwtvkYWRRn3AbPPS1ilqVwi2LQtSiTuF751MaumpAS6V16cKJzwHfrFQytS96dWJ6QIGqK+IMuoSHEcQ10qUVn/R2DKEHncI9i9ZatI4lel+UYVAfEfQIj2PAlFvVkvpwdys/RF/ULfzHjL4Pd9s3db0fEfQI33e2VTd+r9kE1wmNLOoSnmHJAOfM/vNl1v7jmLWvWUBd+4XX+ZPdCPjDMD1Ftl7a1Y4Z9kVDD7qF7xGcbmoCWsN0CT3oFr5v3Z+m/TEJXlcj5e+HsbwZKSNSjrfPPMLP7y6pbm+3qe81M4ws6hMea9GNPs3N8Je9Qyc+BzyaxTu8/zn8G3F9qkU7FCXjAAAAAElFTkSuQmCC"><br>📱 Scan DOI</div>

---

<!-- _class: divider -->
# 💎 整合 Take Home
## 本週 7 大臨床啟示

---

# 💎 本週 Take Home Message（1/2）

1. **EXPLANTORREDO-TAVR 💡**：TAVR 失敗——BEV 晚期結構退化、SEV 早期瓣周漏；**初始瓣種不影響再介入策略與存活**。第一次 TAVR 就為未來預留冠脈可近性。
2. **JenaValve Trilogy ✅**：純 AR 專屬瓣膜真實世界表現佳（成功 98%、院內死亡 0.3%），但 **PPM 22% 偏高**；2026-03 已 FDA 核准。
3. **MitraClip 力學代價 💡**：降逆流但乳突肌受力 +23%；neochordal 還原生理受力。**TEER 不是零成本**；可外科修復者外科更「生理」。
4. **HFpEF 診斷 💡**：運動超音波 + LA strain + 雙切點 → 敏感度 95–99%、侵入性檢查 60%→30%。

---

# 💎 本週 Take Home Message（2/2）

5. **LAAO 抗栓 💡**：減量 DOAC 優於 DAPT、與單抗相當——**別再開雙抗**；搭配 ELAACC 影像共識與「復律後左心耳滯流」術中判讀。
6. **FIELD-PULSE ➰／CT-FFR 性別 💡**：焦點式 PFA first-in-human 可行（早期）；CT-FFR 男性減少不必要 ICA、女性效益待前瞻驗證。
7. **結構＋重症「退路思維」（Drake 主力）**：緊急 TAVR 橋接心內膜炎（例外）、AngioVac 處理跨 PFO 血栓、**MCS 上機前先想好退場**、Impella 平台上做 M-TEER。另：**把妊娠史納入女性心血管風險問診**。

---

<!-- _class: small-text -->
# 📖 參考文獻（1/2）

**Top 5 Picks**
1. Zaid S, et al. EXPLANTORREDO-TAVR. [*Circ Cardiovasc Interv* 2026:e016705.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016705) PMID [42723622](https://pubmed.ncbi.nlm.nih.gov/42723622/)
2. Wienemann H, et al. Dedicated TAVR for Native AR (Trilogy). [*Circ Cardiovasc Interv* 2026:e016851.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.016851) PMID [42717919](https://pubmed.ncbi.nlm.nih.gov/42717919/)
3. Harada T, et al. Exercise stress echo for HFpEF. [*Eur Heart J* 2026:ehag716.](https://doi.org/10.1093/eurheartj/ehag716) PMID [42720269](https://pubmed.ncbi.nlm.nih.gov/42720269/)
4. Reddy VY, et al. FIELD-PULSE (focal PFA). [*JACC Clin Electrophysiol* 2026.](https://doi.org/10.1016/j.jacep.2026.09.001) PMID [42714369](https://pubmed.ncbi.nlm.nih.gov/42714369/)
5. Brazile TL, et al. CVD in pregnancy (Series). [*Lancet* 2026.](https://doi.org/10.1016/S0140-6736(26)01234-1) PMID [42669306](https://pubmed.ncbi.nlm.nih.gov/42669306/)

**TAVI / TEER**
6. Coisne A, et al. Extravalvular Cardiac Damage & AS. [*JACC Adv* 2026:103227.](https://doi.org/10.1016/j.jacadv.2026.103227) PMID [42721604](https://pubmed.ncbi.nlm.nih.gov/42721604/)
7. Park MH, et al. PM forces: MitraClip vs neochordal. [*Circ Cardiovasc Interv* 2026:e016161.](https://doi.org/10.1161/CIRCINTERVENTIONS.125.016161) PMID [42723623](https://pubmed.ncbi.nlm.nih.gov/42723623/)
8. Alkhatib B, et al. TEER in Older Adults. [*Circ Cardiovasc Interv* 2026:e017207.](https://doi.org/10.1161/CIRCINTERVENTIONS.126.017207) PMID [42723624](https://pubmed.ncbi.nlm.nih.gov/42723624/)
9. Isawa T, et al. Transcatheter strategy for MR w/ Impella. [*Circ Rep* 2026;8(9):1570-2.](https://doi.org/10.1253/circrep.CR-26-0155) PMID [42724097](https://pubmed.ncbi.nlm.nih.gov/42724097/)

---

<!-- _class: small-text -->
# 📖 參考文獻（2/2）

**Honorable Mentions**
10. Fauchier L, et al. Reduced-dose DOAC vs antiplatelet after LAAO. [*EuroIntervention* 2026.](https://doi.org/10.4244/EIJ-D-26-00102) PMID [42703763](https://pubmed.ncbi.nlm.nih.gov/42703763/)
11. Ding D, et al. Sex differences in CT-FFR (TARGET). [*EuroIntervention* 2026.](https://doi.org/10.4244/EIJ-D-25-01383) PMID [42703765](https://pubmed.ncbi.nlm.nih.gov/42703765/)
12. ELAACC. Multimodality imaging for LAAO (consensus). [*EuroIntervention* 2026.](https://doi.org/10.4244/EIJ-D-25-01372) PMID [42703764](https://pubmed.ncbi.nlm.nih.gov/42703764/)
13. Novel risk scores for HF prediction. [*Eur Heart J* 2026:ehag644.](https://doi.org/10.1093/eurheartj/ehag644) PMID [42705643](https://pubmed.ncbi.nlm.nih.gov/42705643/)
14. CAR-T CV toxicity: CART-7 to CART-8. [*Eur Heart J* 2026:ehag710.](https://doi.org/10.1093/eurheartj/ehag710) PMID [42717801](https://pubmed.ncbi.nlm.nih.gov/42717801/)
15. Miyajima K, et al. Acute TR worsening after LBBAP. [*Circ Rep* 2026;8(9):1387-95.](https://doi.org/10.1253/circrep.CR-26-0148) PMID [42723984](https://pubmed.ncbi.nlm.nih.gov/42723984/)

**Case Reports**
16. Attumalil TV, et al. Emergency TAVR bridge for AV endocarditis. [*JACC Case Rep* 2026:110231.](https://doi.org/10.1016/j.jaccas.2026.110231) PMID [42726041](https://pubmed.ncbi.nlm.nih.gov/42726041/)
17. Nallapati CS, et al. AngioVac thrombectomy across PFO. [*JACC Case Rep* 2026:110222.](https://doi.org/10.1016/j.jaccas.2026.110222) PMID [42726037](https://pubmed.ncbi.nlm.nih.gov/42726037/)
18. Ivanov A, et al. Postcardioversion LAA stasis during LAAC. [*JACC Case Rep* 2026:110205.](https://doi.org/10.1016/j.jaccas.2026.110205) PMID [42726038](https://pubmed.ncbi.nlm.nih.gov/42726038/)
19. Gonnah AR, et al. ACS in diffuse coronary ectasia. [*JACC Case Rep* 2026:110203.](https://doi.org/10.1016/j.jaccas.2026.110203) PMID [42726045](https://pubmed.ncbi.nlm.nih.gov/42726045/)
20. Mackey R, et al. Occult cocaine CM + MCS exit strategy. [*JACC Case Rep* 2026:110245.](https://doi.org/10.1016/j.jaccas.2026.110245) PMID [42726043](https://pubmed.ncbi.nlm.nih.gov/42726043/)

---

<!-- _class: abbr -->
# 縮寫對照（1/2）

| 縮寫 | 全名 (英文) / 中文 |
|------|------|
| TAVR/TAVI | Transcatheter Aortic Valve Replacement/Implantation 經導管主動脈瓣置換/植入 |
| BEV / SEV | Balloon-Expandable / Self-Expanding Valve 球囊擴張瓣／自膨瓣 |
| redo-TAVR / explant | 再次瓣中瓣／失敗 TAVR 外科取出 |
| AS / AR / ssAR | Aortic Stenosis / (symptomatic severe) Aortic Regurgitation 主動脈瓣狹窄／（症狀性重度）逆流 |
| PPM / PVL | Permanent Pacemaker / Paravalvular Leak 永久節律器／瓣周漏 |
| VARC-3 | Valve Academic Research Consortium-3 瓣膜學術研究聯盟第三版 |
| CD | (extravalvular) Cardiac Damage （瓣外）心臟損害分期 |
| TEER / M-TEER / T-TEER | (Mitral/Tricuspid) Transcatheter Edge-to-Edge Repair 經導管緣對緣修復 |
| MR / TR | Mitral / Tricuspid Regurgitation 二尖瓣／三尖瓣逆流 |
| PM | Papillary Muscle 乳突肌 |
| HFpEF | HF with preserved Ejection Fraction 射血分數保留型心衰竭 |
| LA / LVEF | Left Atrium 左心房／左心室射血分數 |

---

<!-- _class: abbr -->
# 縮寫對照（2/2）

| 縮寫 | 全名 (英文) / 中文 |
|------|------|
| CGA / MNA-SF / KCCQ | 綜合老年評估／簡易營養評估／堪薩斯城心肌病問卷 |
| PFA / PVI / AF | Pulsed-Field Ablation / Pulmonary Vein Isolation / Atrial Fibrillation 脈衝場消融／肺靜脈隔離／心房顫動 |
| LBBAP | Left Bundle Branch Area Pacing 左束支區起搏 |
| LAAO / LAAC | Left Atrial Appendage Occlusion / Closure 左心耳封堵 |
| DAPT / SAPT / DOAC | 雙抗／單抗血小板／直接口服抗凝劑 |
| CT-FFR / ICA / CCTA | 電腦斷層血流儲備分數／侵入性冠脈攝影／冠脈電腦斷層 |
| ISR / CAE / STEMI | 支架內再狹窄／冠狀動脈擴張症／ST 段上升心肌梗塞 |
| CAR-T | Chimeric Antigen Receptor T-cell 嵌合抗原受體 T 細胞療法 |
| APO / HDP | Adverse Pregnancy Outcomes / Hypertensive Disorders of Pregnancy 不良妊娠結局／妊娠高血壓疾病 |
| MCS / VA-ECMO | Mechanical Circulatory Support / Venoarterial ECMO 機械循環支持／靜脈-動脈體外膜氧合 |
| PFO / SEC | Patent Foramen Ovale / Spontaneous Echo Contrast 卵圓孔未閉／自發性回音顯影 |
| MACE / NCB | Major Adverse CV Events / Net Clinical Benefit 主要不良心血管事件／淨臨床效益 |

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

涵蓋期間：2026-09-04 ~ 2026-09-11

> 本講義為讀書會共筆之教學整理，僅供醫療專業同仁臨床教學交流參考，不作為個案診療依據。臨床決策請依各病人實際情況並參考最新指南。
