各位同仁 您好：

跟各位報告一下這兩週（2026-10-02 ～ 2026-10-15）的 Critical Care 期刊回顧。這期復甦（resuscitation）的文章特別多，所以就以復甦為主軸，另外補上呼吸、神經、腎臟、循環與重症後照護幾篇值得一讀的研究。先講結論：這一期沒有改寫指引的大型試驗，多半是觀察性資料與統合分析，但方向都滿實用的，給各位做個參考。

本期涵蓋 Resuscitation、Critical Care、Critical Care Medicine、Chest、Intensive Care Medicine、Shock。內容為讀書會內部共筆，僅供教學討論。完整講義與投影片已 commit 並 push 到 repo 的 `handouts/10-icu-general/`。

🎯 **本期主題：復甦為主，兼顧呼吸、腎臟、循環與重症後照護**

---

### 🫁 本期 5 個重點 (Top 5 Pearls)

1. **CPR 期間用「機械式呼吸器」給氣，比徒手 bag-valve 有較高自發循環恢復（ROSC）。** 8 篇研究、6,847 人的貝氏統合分析，ROSC 的 risk ratio (RR) 1.20，益處後驗機率 99%。不過存活與神經學預後的訊號還不精確，指引目前也還沒建議取代徒手。重點還是避免過度通氣。
2. **院外心臟驟停（OHCA）由不可電擊轉成可電擊後，給 amiodarone 與較高存活相關。** 德國登錄配對分析，出院存活 6.5% vs 4.2%（odds ratio, OR 1.58）。倒是神經學預後沒有達到統計顯著，不要過度解讀。
3. **體外 CPR（ECPR）的節律若惡化成心搏停止（asystole），預後極差。** 良好神經學預後的 RR 只有 0.20。簡單來說，CPR 過程「往 asystole 走」是很強的壞訊號，可以納入上機與否的判斷。
4. **肺切除術後預防性 high-flow nasal cannula (HFNC) 能降低術後肺部併發症。** 中-重度併發症 23.1% vs 39.6%。但作者講得很清楚，不建議對所有人常規使用，而是給年長或高風險的人。
5. **敗血症存活者「家屬」的心理後遺症一年都不太退。** 家屬的心理型 PICS-F 三個月 43%、一年 42%，而且跟病人本身的「心理」問題最相關。說穿了，重症後追蹤不能只顧病人。

---

### 💓 心臟驟停與復甦 (Resuscitation)

| 主題 | 設計 / 人數 | 關鍵結果 | 連結 |
|------|------------|----------|------|
| 機械式 vs 徒手 bag-valve 給氣 | Bayesian 統合，8 篇 / 6,847 人 | ROSC RR 1.20（CrI 1.04–1.42，益處機率 99%）；存活/神經學不精確 | [doi](https://doi.org/10.1016/j.resuscitation.2026.111345) · [PMID 42863592](https://pubmed.ncbi.nlm.nih.gov/42863592/) |
| 不可電擊→可電擊後給 amiodarone | 德國登錄配對，各 1,843 | 出院存活 6.5% vs 4.2%（OR 1.58）；神經學預後 NS | [doi](https://doi.org/10.1016/j.resuscitation.2026.111349) · [PMID 42838501](https://pubmed.ncbi.nlm.nih.gov/42838501/) |
| ECPR 的節律動態 | 統合，10 篇 / 5,183 人 | 惡化成 asystole 良好神經學預後 RR 0.20；節律改善 RR 3.12 | [doi](https://doi.org/10.1016/j.resuscitation.2026.111348) · [PMID 42838500](https://pubmed.ncbi.nlm.nih.gov/42838500/) |
| Post-ROSC 早期實驗室表型 | 新加坡全國 1,514 人（LCA） | 分 MOD/HOM/IMD 三型；HOM、IMD 死亡與不良預後較 MOD 低 | [doi](https://doi.org/10.1016/j.resuscitation.2026.111351) · [PMID 42855036](https://pubmed.ncbi.nlm.nih.gov/42855036/) |

---

### 🫁 呼吸支持 (Ventilation)

| 主題 | 設計 / 人數 | 關鍵結果 | 連結 |
|------|------------|----------|------|
| 肺切除術後預防性 HFNC | 單中心 RCT，210 人 | 中-重度術後肺併發症 23.1% vs 39.6%（OR 0.50）；不建議全面常規化 | [doi](https://doi.org/10.1186/s13054-026-06205-4) · [PMID 42864673](https://pubmed.ncbi.nlm.nih.gov/42864673/) |
| 高頻胸壁震盪（HFCWO）治痰液滯留 | 單中心 RCT，88 人 | 支氣管鏡需求校正後 OR 0.336（p=0.055，不顯著）；住院縮短屬探索性 | [doi](https://doi.org/10.1016/j.chest.2026.10.007) · [PMID 42874912](https://pubmed.ncbi.nlm.nih.gov/42874912/) |

---

### 🧠 神經重症 · 腎臟 · 循環 (Neuro / Renal / Hemodynamics)

| 主題 | 設計 / 人數 | 關鍵結果 | 連結 |
|------|------------|----------|------|
| 自動瞳孔量測 NPi vs QPi（LYNX） | 前瞻多中心，108 人 | 相關 r=0.717，但 QPi 對 propofol 敏感 → 鎮靜病人兩者不可互換 | [doi](https://doi.org/10.1186/s13054-026-06360-8) · [PMID 42839269](https://pubmed.ncbi.nlm.nih.gov/42839269/) |
| 少尿（oliguria）最佳閾值 | 瑞典回顧，4,999 人 | 死亡/CKD 風險在比 0.5 mL/kg/hr 更低的尿量即上升 | [doi](https://doi.org/10.1097/CCM.0000000000007370) · [PMID 42872921](https://pubmed.ncbi.nlm.nih.gov/42872921/) |
| VA ECMO 累積 inotrope 暴露 | 荷蘭 6 中心，440 人 | 暴露越高，脫機失敗、30 天死亡、心律不整皆增加（HR ~1.04） | [doi](https://doi.org/10.1097/CCM.0000000000007338) · [PMID 42809661](https://pubmed.ncbi.nlm.nih.gov/42809661/) |

---

### 👪 重症後照護 (Survivorship)

| 主題 | 設計 / 人數 | 關鍵結果 | 連結 |
|------|------------|----------|------|
| 敗血症存活者家屬 PICS-F | 日本 21 ICU，94 對 | PICS-F 一年仍 42% 不退；與病人「心理」PICS 最相關（aOR 3.71） | [doi](https://doi.org/10.1097/CCM.0000000000007378) · [PMID 42872916](https://pubmed.ncbi.nlm.nih.gov/42872916/) |
| 種族/族裔與 ICU 存活者身體障礙 | 單中心，4,370 人 | 黑人、西班牙裔功能障礙與後續醫療利用皆較高 | [doi](https://doi.org/10.1097/CCM.0000000000007373) · [PMID 42841714](https://pubmed.ncbi.nlm.nih.gov/42841714/) |

---

### 📌 Take Home Message

這一期的共同主題，說穿了就是「別把單一數字當唯一依據」。CPR 的節律要看動態、少尿的閾值可能比我們習慣的更嚴、瞳孔指數要看是哪一種、鎮靜藥會干擾判讀。另外 VA ECMO 下的 inotrope、肺切除後的 HFNC，都提醒我們「能減則減、該用才用」。總結一句：這些多半是觀察性證據，方向可參考，但還不到改寫常規的程度。只是提出來供各位參考。

---

**讀書會共筆整理人：謝慕揚 MD, PhD, FESC**

本文件為讀書會內部共筆，僅供醫療專業人員教學討論參考。
