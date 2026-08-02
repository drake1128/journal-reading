/**
 * 問卷產生器 · Google Form Generator (可重用範本)
 * ------------------------------------------------------------
 * 用途：開會 / 帶團隊時，一鍵產生「Google 表單 + 連動回覆試算表」，
 *       組員手機掃 QR 即可匿名填寫，回覆自動彙整到 Google Sheet。
 *
 * 使用方式（一次性，約 1 分鐘）：
 *   1. 到 https://script.google.com → 「新專案」
 *   2. 把本檔全部內容貼進去，覆蓋預設的 myFunction
 *   3. 上方選函式 buildForm → 按「執行」
 *   4. 第一次會要求授權（同一個 Google 帳號按同意即可）
 *   5. 執行完，下方「執行紀錄 (Ctrl+Enter)」會印出三個網址：
 *        · 填寫網址 (Published URL) ← 這個拿去做 QR / 給組員
 *        · 編輯網址 (Edit URL)      ← 你之後要改題目用
 *        · 回覆試算表 (Sheet URL)   ← 你看彙整結果用
 *   6. 把「填寫網址」貼給我，我在網站管理頁加一張「點我填寫」QR 卡。
 *
 * 下次要做別的問卷：只改下面 CONFIG 的 title/description 與 QUESTIONS，
 *   再執行一次 buildForm 就會生出一份新的表單，互不影響。
 * ============================================================
 */

// ========================== CONFIG ==========================
var CONFIG = {
  title: "制度診斷 · 團隊感知快篩",
  description:
    "這是一份匿名問卷，目的是「診斷制度，不是診斷人」。\n" +
    "請依你在單位裡的實際感受作答，沒有標準答案，越誠實越有用。\n" +
    "填答不會記錄你是誰。約需 3–5 分鐘。",
  collectEmail: false,      // false = 匿名（建議）；true = 記錄填答者 Email
  limitOneResponse: false,  // true = 每個 Google 帳號只能填一次（會強制登入）
  shuffle: false            // true = 選項順序隨機
};

/**
 * 題型：
 *   {type:"section", title, help}                         區段標題
 *   {type:"scale", title, low, high, min, max, required}  李克特量表（預設 1–5）
 *   {type:"mc", title, choices:[...], required}           單選
 *   {type:"checkbox", title, choices:[...], required}     複選
 *   {type:"short", title, required}                       簡答
 *   {type:"paragraph", title, required}                   長答
 */
var LIKERT = { low: "非常不同意", high: "非常同意", min: 1, max: 5 };

var QUESTIONS = [
  { type: "section", title: "A · 基本背景（選填）",
    help: "只用來分群比較，不會拿來對號入座。不想填可留白。" },
  { type: "mc", title: "你的角色", required: false,
    choices: ["醫師", "護理 / 專師", "醫事技術（放射師、技術員等）", "行政 / 管理", "其他"] },
  { type: "mc", title: "在這個單位的年資", required: false,
    choices: ["未滿 1 年", "1–3 年", "3–5 年", "5 年以上"] },

  { type: "section", title: "B · 資訊與心理安全",
    help: "壞消息傳不上去的組織，制度永遠不會被修正。" },
  { type: "scale", title: "壞消息（問題、風險、失誤）能很快傳到「能做決定的人」那裡。", required: true, low: LIKERT.low, high: LIKERT.high, min: LIKERT.min, max: LIKERT.max },
  { type: "scale", title: "在會議上，我可以安全地說出不同意見或壞消息，不會因此被針對。", required: true, low: LIKERT.low, high: LIKERT.high, min: LIKERT.min, max: LIKERT.max },
  { type: "scale", title: "遇到問題時，這裡會去「檢討並修改制度」，而不是只找一個人負責。", required: true, low: LIKERT.low, high: LIKERT.high, min: LIKERT.min, max: LIKERT.max },

  { type: "section", title: "C · 誘因、權限、資源、資訊",
    help: "同樣是「事情推不動」，病因不同，用錯藥完全無效。" },
  { type: "scale", title: "我很清楚我的工作「怎樣算做好」，而且會得到回饋。（資訊）", required: true, low: LIKERT.low, high: LIKERT.high, min: LIKERT.min, max: LIKERT.max },
  { type: "scale", title: "把事情做好，對我個人是有好處的；不做也會有相應後果。（誘因）", required: true, low: LIKERT.low, high: LIKERT.high, min: LIKERT.min, max: LIKERT.max },
  { type: "scale", title: "想把事情做好時，我有足夠的「權限」可以自己決定。（權限）", required: true, low: LIKERT.low, high: LIKERT.high, min: LIKERT.min, max: LIKERT.max },
  { type: "scale", title: "我有足夠的「時間、人力、預算」完成被交付的工作。（資源）", required: true, low: LIKERT.low, high: LIKERT.high, min: LIKERT.min, max: LIKERT.max },

  { type: "section", title: "D · 均衡與退場訊號",
    help: "均衡點才是制度的真實輸出；沒有人抱怨不代表沒問題。" },
  { type: "scale", title: "表面上大家都遵守規定，但私下常有一套「繞過去」的做法。", required: true, low: LIKERT.low, high: LIKERT.high, min: LIKERT.min, max: LIKERT.max },
  { type: "scale", title: "最近我有認真想過「乾脆自己來 / 繞過這個系統」。（Exit 訊號）", required: true, low: LIKERT.low, high: LIKERT.high, min: LIKERT.min, max: LIKERT.max },

  { type: "section", title: "E · 開放意見（最有價值的一段）" },
  { type: "paragraph", title: "如果只能改「一件」制度上的事，你會改什麼？為什麼？", required: false },
  { type: "paragraph", title: "有沒有你觀察到、但一直沒被拿上檯面談的問題？", required: false }
];
// ======================== /CONFIG ===========================


function buildForm() {
  var form = FormApp.create(CONFIG.title);
  form.setDescription(CONFIG.description);
  form.setCollectEmail(CONFIG.collectEmail);
  form.setLimitOneResponsePerUser(CONFIG.limitOneResponse);
  form.setAllowResponseEdits(false);
  form.setShuffleQuestions(CONFIG.shuffle);
  form.setProgressBar(true);

  QUESTIONS.forEach(function (q) {
    switch (q.type) {
      case "section":
        form.addSectionHeaderItem().setTitle(q.title).setHelpText(q.help || "");
        break;
      case "scale":
        form.addScaleItem()
          .setTitle(q.title)
          .setBounds(q.min || 1, q.max || 5)
          .setLabels(q.low || "", q.high || "")
          .setRequired(!!q.required);
        break;
      case "mc":
        form.addMultipleChoiceItem()
          .setTitle(q.title)
          .setChoiceValues(q.choices)
          .setRequired(!!q.required);
        break;
      case "checkbox":
        form.addCheckboxItem()
          .setTitle(q.title)
          .setChoiceValues(q.choices)
          .setRequired(!!q.required);
        break;
      case "short":
        form.addTextItem().setTitle(q.title).setRequired(!!q.required);
        break;
      case "paragraph":
        form.addParagraphTextItem().setTitle(q.title).setRequired(!!q.required);
        break;
    }
  });

  // 建立並連動回覆試算表
  var ss = SpreadsheetApp.create(CONFIG.title + "（回覆）");
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  Logger.log("========================================");
  Logger.log("✅ 表單已建立：" + CONFIG.title);
  Logger.log("① 填寫網址（做 QR / 給組員）: " + form.getPublishedUrl());
  Logger.log("② 編輯網址（改題目用）      : " + form.getEditUrl());
  Logger.log("③ 回覆試算表（看彙整結果）  : " + ss.getUrl());
  Logger.log("========================================");
}
