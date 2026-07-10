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
  section.lead h1 { color: #ffffff; font-size: 2.2em; }
  section.lead h2 { color: #b0c4de; }
  section.lead p, section.lead strong { color: #dfe6e9; }
  section.lead a { color: #74b9ff; }
  section.lead blockquote { color: #2d3436; }
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
  section.divider h2 { color: #ffe066; }
  section.divider h3 { color: #ffffff; }
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
  code { background-color: #f1f2f6; color: #2d3436; padding: 2px 6px; border-radius: 4px; }
  strong { color: #ba181b; }
  footer { color: #787878; font-size: 0.6em; }
  section.small-text { font-size: 0.85em; }
footer: '謝慕揚 MD, PhD, FESC | Venus Flytrap Snap Mechanism | 2026'
---

<!-- _class: lead -->
# 捕蠅草如何瞬間閉合？
## 細胞壁瞬間軟化之謎 — Nature News / Science 2026
**謝慕揚 MD, PhD, FESC（讀書會共筆整理）** | 2026-06-15
[Nature News 原文](https://doi.org/10.1038/d41586-026-01857-2) ｜ [Science 原始研究](https://doi.org/10.1126/science.aed5051)

---

# 一句話總結

> 捕蠅草 (_Dionaea muscipula_) 在 **< 1 秒** 內閉合，靠的不是「水分快速灌注撐脹」，而是葉片**外表皮細胞壁在約一秒內「瞬間軟化」**，釋放儲存的**彈性能**，使外凸葉瓣瞬間翻轉內凹。

- 科學界**首次**觀察到植物細胞壁在如此短時間內力學性質劇變
- 研究團隊：Yoël Forterre（Aix-Marseille University）
- 發表：**_Science_ 2026;392:1183–1187**

---

<!-- _class: divider -->
# 背景：150 年的謎題

---

# 從達爾文到今天

| 年代 | 里程碑 |
|------|--------|
| **1875** | 達爾文稱捕蠅草為「最奇妙的植物」，驚嘆其「快速」 |
| **2005** | Forterre：葉瓣為外凸**預張構型**，閉合是 **snap-buckling**（最快 1/10 秒） |
| **2019** | Scherzer：感覺毛 (trigger hairs) → **動作電位**橫越葉面 → 觸發 |
| **2026** | **本研究：解開「張力如何瞬間釋放」的最後一塊拼圖** |

> **核心懸案**：葉片像被扳彎、隨時要彈回的彈片——但「扳機」如何被扣下？

---

<!-- _class: divider -->
# 兩個競爭假說

---

# 灌水撐脹 vs. 鬆開煞車

| 假說 | 機制 | 速度決定因素 |
|------|------|------------|
| **A. 水分快速移動** | 水由內側流向外表皮細胞 → 膨脹 → 驅動翻轉 | 跨葉水分傳輸時間 |
| **B. 細胞壁瞬間軟化** | 剛性細胞壁突然變軟 → 釋放彈性能 → 翻轉 | 細胞壁力學變化（可極快） |

**核心問題：是「灌水撐脹」，還是「鬆開煞車」讓捕蠅草閉合？**

---

<!-- _class: divider -->
# 關鍵實驗與證據

---

# 兩個實驗，一個結論

**> 100 株捕蠅草、歷時多年 → 明確支持「假說 B：細胞壁軟化」**

| 實驗 | 做法 | 結果 |
|------|------|------|
| **① 量測細胞壁硬度** | 探測外表皮細胞 stiffness | 觸發後細胞**明顯軟化** |
| **② 計算水分傳輸時間** | 量測 + 計算跨葉水分傳輸 | 需 **30–150 秒**，遠慢於閉合的 < 1 秒 → **排除假說 A** |

> **時間尺度排除法**：即使機制存在，太慢就不可能是瞬間動作的元兇。

---

# 專家評論

> 「這是一篇令人屏息、非常優雅的論文。植物能放鬆細胞剛性外壁以利生長，但那是**遠比捕蠅草閉合慢得多**的時間尺度。**像捕蠅草這種速度的細胞軟化，是科學家前所未見的現象。**」

**— Simon Poppinga**，生物力學學者
達姆施塔特工業大學 (Technical University of Darmstadt) 植物園主任（未參與本研究）

---

# 機制圖解

```text
[1] 靜止：葉瓣外凸、預張，彈性能儲存於剛性細胞壁
        │  昆蟲觸碰 trigger hairs
        ▼
[2] 動作電位 (action potential) 橫越葉面
        │  （新發現的關鍵步驟）
        ▼
[3] 外表皮細胞壁「瞬間軟化」(~1 秒)
        │
        ▼
[4] 釋放彈性能 → snap-buckling（彈跳挫曲）
        │
        ▼
[5] 葉瓣外凸翻轉為內凹 → 陷阱閉合 (< 1 秒)
```

---

<!-- _class: divider -->
# 尚未解開的謎題

---

# 故事還沒結束

1. **究竟是什麼讓細胞壁變軟？**
   - 細胞壁 = 柔軟**凝膠基質** + 剛性**纖維網**
   - 假說：昆蟲到來後釋放**酵素混合物**，削弱纖維-基質的連結 → 軟化
2. **捕到大型獵物時，葉瓣如何「攤平」形成消化腔？**

> 「這些未解的問題，正是我們每天早上走進實驗室的理由。」— Poppinga

---

# 跨領域延伸：軟體機器人

- 啟發**軟體機器人 (soft robotics)** 設計
- 概念：平時**儲存彈性能**，當材料**剛性改變**時瞬間啟動
- 以「材料軟化」取代馬達驅動 → 快速、低耗能的彈跳式動作
- 捕蠅草給工程界的**仿生 (bio-inspired)** 啟示

---

# 給臨床讀者的類比聯想（趣味發想）

| 捕蠅草機制 | 心血管／臨床類比 |
|-----------|----------------|
| 預張、儲能的細胞壁 | 主動脈彈性回縮、心室舒張儲能 |
| 細胞壁剛性主動調控 | 血管硬化 (arterial stiffness)、壁重塑 |
| snap-buckling 失穩 | 裝置自膨張／球囊擴張的力學 |
| 觸發毛→電位→機械反應 | 機械-電氣偶聯 (mechano-electrical coupling) |

> 僅供發想：「力學儲能-釋能」是橫跨植物與心血管的共通語言。

---

<!-- _class: small-text -->
# 參考文獻

1. Wolf L. Revealed: how Venus flytraps snap shut with astonishing speed. [*Nature* (News). 2026 Jun 11.](https://doi.org/10.1038/d41586-026-01857-2)
2. Ryu J, Colombani M, Mollier M, Marthelot J, Forterre Y. Fast cell wall softening causes Venus flytrap closure. [*Science*. 2026;392:1183–1187.](https://doi.org/10.1126/science.aed5051)
3. Forterre Y, Skotheim JM, Dumais J, Mahadevan L. How the Venus flytrap snaps. [*Nature*. 2005;433:421–425.](https://doi.org/10.1038/nature03185)
4. Scherzer S, Federle W, Al-Rasheid KAS, Hedrich R. Venus flytrap trigger hairs are micronewton mechano-sensors that can detect small insect prey. [*Nature Plants*. 2019;5:670–675.](https://doi.org/10.1038/s41477-019-0465-1)

---

<!-- _class: lead -->
# 謝謝聆聽
## Q & A
**謝慕揚 MD, PhD, FESC** ｜ 讀書會共筆整理
[Science — Fast cell wall softening causes Venus flytrap closure](https://doi.org/10.1126/science.aed5051)
