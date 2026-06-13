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
    justify-content: center;
  }
  section.lead h1 { color: #ffffff; font-size: 2.0em; border-bottom: none; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #ffd166; text-decoration: underline; }
  section.divider {
    background-color: #0072bc;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  section.divider h1 { color: white; border-bottom: none; font-size: 2.4em; text-align: center; }
  section.divider h2, section.divider h3 { color: #ffffff; }
  h1 { color: #ba181b; border-bottom: 3px solid #ba181b; padding-bottom: 0.2em; }
  h2 { color: #0072bc; }
  h3 { color: #555555; }
  table { font-size: 0.74em; width: 100%; }
  th { background-color: #0072bc; color: white; padding: 6px 10px; }
  td { padding: 4px 10px; }
  tr:nth-child(even) { background-color: #f0f4f8; }
  blockquote {
    border-left: 4px solid #ba181b;
    background-color: #fff5f5;
    padding: 0.5em 1em;
    font-size: 0.9em;
  }
  /* Disclaimer blockquote on a dark lead slide: force dark text so it stays
     readable on the light box (otherwise inherits section.lead light colour). */
  section.lead blockquote,
  section.lead blockquote p,
  section.lead blockquote strong { color: #2d3436; }
  pre { background-color: #f5f6fa; color: #2d3436; border: 1px solid #dcdde1; border-radius: 8px; padding: 0.8em; font-size: 0.62em; }
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.82em; }
  section.ref { font-size: 0.74em; }
footer: '謝慕揚 MD, PhD, FESC | Door-to-Balloon / Door-to-Needle | 2026'
---

<!-- _class: lead -->
# 如何改善 Door-to-Balloon / Door-to-Needle 時間？
## STEMI 再灌流的系統照護
**謝慕揚 MD, PhD, FESC** ｜ 2026-06-14
[Bradley EH, et al. N Engl J Med. 2006;355:2308–2320 — DOI: 10.1056/NEJMsa063117](https://doi.org/10.1056/NEJMsa063117)

---

# 核心結論 (Bottom Line)

> **縮短 STEMI 再灌流時間，靠的不是新科技，而是「流程與系統」的改造。**

- **Bradley 2006 (NEJM)**：找出 **6 個與更短 D2B 獨立相關的醫院策略**，效果以「分鐘」計，且當年多數醫院都還沒做
- **Menees 2013 (NEJM) 的反思**：全國 D2B 大幅下降，**院內死亡率卻幾乎沒變**
- 時間是**必要但不充分** —— **總缺血時間**與**到院前延遲**才是更大的戰場

---

# 為什麼時間重要？指標與目標

**Time is muscle**：再灌流愈快，挽救心肌愈多。

| 路徑 | 指標 | 指引目標 |
|------|------|---------|
| **primary PCI（導管）** | **Door-to-Balloon (D2B)** = 到院 → 球囊擴張 | **≤ 90 分鐘** |
| **fibrinolysis（溶栓）** | **Door-to-Needle (D2N)** = 到院 → 開始溶栓 | **≤ 30 分鐘** |
| 跨院轉送 PCI | **FMC-to-device** = 首次醫療接觸 → 器械 | **≤ 90–120 分鐘** |

> D2B 只是「**到院後**」那一段；真正影響預後的是 **symptom-to-balloon 的總缺血時間**（含到院前延遲）。

---

# Bradley 2006 — 6 大有效策略

調查 365 家醫院、28 種做法 → 6 個與較短 D2B **獨立相關**（括號＝平均減少分鐘）：

| # | 策略 | D2B 減少 |
|---|------|---------|
| 1 | **急診醫師直接啟動導管室**（不必先等心臟科） | −8.2 min |
| 2 | **單一通電話**給中央呼叫台即可啟動 | −13.8 min |
| 3 | **病人到院途中（en route）就先啟動導管室** | −15.4 min |
| 4 | **導管室團隊承諾 ≤20 分鐘到位**（vs >30） | −19.3 min |
| 5 | **主治級心臟科醫師全時在院** | −14.6 min |
| 6 | **即時數據回饋**給急診與導管室團隊 | −8.6 min |

> 都是**流程/組織**改變、不是新器材；當年**只有少數醫院在做** → 改善空間常「免費」。

---

# 之後：D2B Alliance / Mission Lifeline

- Bradley 2006 成為 **ACC「D2B Alliance」** 與 **AHA「Mission: Lifeline」** 的理論基礎
- 全美推動：**到院前 12 導程 ECG、單一電話啟動、急診啟動導管室、團隊到位時限、定期回饋**
- 成效：全美 D2B 時間在數年內**大幅下降、達標率明顯提升**（見下頁）

---

# Menees 2013 — 時間變快，死亡率卻沒降

CathPCI Registry，2005–2009，**96,738** 例 primary PCI、515 家醫院。

| 指標 | 2005–06 | 2008–09 | P |
|------|---------|---------|---|
| **中位數 D2B** | 83 min | **67 min** | <0.001 |
| **D2B ≤90 min** | 59.7% | **83.1%** | <0.001 |
| 風險校正院內死亡率 | 5.0% | 4.7% | **0.34（無變化）** |
| 30 天死亡率 | — | — | 0.64（無差異） |

> **全國 D2B 顯著縮短，院內死亡率卻幾乎沒變 → 需要「額外」策略才能再降死亡率。**

---

# 為什麼死亡率沒降？（教學重點）

- **天花板效應**：系統已接近最佳，再擠幾分鐘的邊際效益有限
- **總缺血時間才是關鍵**：D2B 只佔「症狀→再灌流」一小段；**到院前延遲**常是更大宗
- **族群選擇 (selection)**：愈衝指標，可能納入愈多預後較差/較不典型病人，稀釋好處
- **啟示**：D2B 是**必要但不充分** → 下一階段往 **symptom-to-FMC、FMC-to-device、休克照護、次級預防** 著力

---

# Door-to-Needle（溶栓）的對應策略

無法及時 primary PCI 時，**溶栓**仍關鍵，目標 **D2N ≤ 30 分鐘**。邏輯與 D2B 相同：

- **到院前 12 導程 ECG**：救護車上判讀、預先通報
- **急診醫師依方案 (protocol) 直接啟動／給藥**
- **單次呼叫 / STEMI 溶栓 checklist**（適應症/禁忌）
- **bolus 型溶栓劑**（如 tenecteplase, TNK）急診即備
- **pharmaco-invasive**：溶栓後常規早期轉送導管室
- **定期稽核與回饋**：把 D2N 當品質指標

> 屬 **AHA/ACC STEMI 指引與 Mission: Lifeline**；核心同 Bradley —— **決策前移、流程標準化、數據回饋。**

---

# 實務落地清單

```text
到院前 (Pre-hospital)
  └─ 救護車 12 導程 ECG → 預先通報 → 病人 en route 即啟動

到院 (Door)
  ├─ 急診醫師可「自行」判讀並啟動（PCI）或依方案給溶栓（lysis）
  ├─ 「單一電話」啟動整組團隊
  └─ STEMI checklist（適應症/禁忌、抗血小板、抗凝）

啟動後 (Activation)
  ├─ 導管室團隊承諾 ≤20 分鐘到位
  ├─ 主治級隨時可到 / 在院
  └─ 溶栓劑（bolus）急診即備

事後 (Feedback)
  └─ 每案記錄 D2B / D2N、定期稽核、即時回饋
```

---

<!-- _class: divider -->
# Take Home

---

# 5 大臨床 Pearls

> **Pearl 1**：縮短 D2B/D2N 主要靠**系統與流程**，不是新科技。

> **Pearl 2**：Bradley 2006 的 6 策略效果以「分鐘」計，且當年多數醫院未採用 —— 改善空間常「免費」。

> **Pearl 3**：Menees 2013 提醒 **D2B 達標 ≠ 死亡率下降**；**總缺血時間**與**到院前延遲**才是下一個戰場。

> **Pearl 4**：溶栓路徑同理 —— D2N ≤30 分鐘，靠到院前 ECG、急診依方案給藥、bolus 溶栓劑與 pharmaco-invasive 轉送。

> **Pearl 5**：把時間指標當**品質工具**，同時兼顧 symptom-to-FMC 衛教、休克照護與次級預防。

---

<!-- _class: small-text -->
# 縮寫對照

| 縮寫 | 全名 (English) | 中文 |
|------|----------------|------|
| STEMI | ST-Elevation Myocardial Infarction | ST 段上升型心肌梗塞 |
| D2B / D2N | Door-to-Balloon / Door-to-Needle time | 到院至球囊 / 至溶栓給藥時間 |
| PCI | Percutaneous Coronary Intervention | 經皮冠狀動脈介入 |
| FMC | First Medical Contact | 首次醫療接觸 |
| ECG / ED | Electrocardiogram / Emergency Department | 心電圖 / 急診 |
| ACC / AHA | American College of Cardiology / American Heart Association | 美國心臟學院 / 協會 |
| TNK | Tenecteplase | 替奈普酶（bolus 型溶栓劑） |

---

<!-- _class: ref -->
# 參考文獻

1. Bradley EH, Herrin J, Wang Y, et al. Strategies for reducing the door-to-balloon time in acute myocardial infarction. [*N Engl J Med*. 2006;355(22):2308–2320.](https://doi.org/10.1056/NEJMsa063117) ｜ PMID [17101617](https://pubmed.ncbi.nlm.nih.gov/17101617/)
2. Menees DS, Peterson ED, Wang Y, et al. Door-to-balloon time and mortality among patients undergoing primary PCI. [*N Engl J Med*. 2013;369(10):901–909.](https://doi.org/10.1056/NEJMoa1208200) ｜ PMID [24004117](https://pubmed.ncbi.nlm.nih.gov/24004117/)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

本案重點：縮短再灌流時間靠系統流程；但 D2B 達標 ≠ 死亡率下降，總缺血時間才是關鍵

> 本投影片為讀書會共筆之教學整理，僅供醫療專業人員教學參考；臨床決策請以原始文獻及醫師個人判斷為依據。
