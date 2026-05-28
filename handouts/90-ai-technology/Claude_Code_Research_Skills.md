# Claude Code × Scientific Research
## 介入心臟科 & 透析研究推薦 GitHub Skills 組合

> 作者備註：本文件由 Claude 生成，供搭配 Claude Code 本地端安裝使用。

---

## 📊 統計分析 & 數據處理

### 1. Anthropic Quickstarts
- **GitHub**：https://github.com/anthropics/anthropic-quickstarts
- 快速搭建互動式數據分析 agent
- 結合 Python（pandas、scipy、statsmodels）做臨床數據清理、描述統計、回歸分析
- 適合處理透析病患 cohort 資料

### 2. DuckDB MCP Server
- **GitHub**：https://github.com/motherduckdb/mcp-server-duckdb
- 直接對大型 CSV / Parquet 臨床資料庫下 SQL query
- 不需要預先建立資料庫，查詢速度極快
- 適合分析 ESRD registry、導管室數據庫

---

## 📄 文獻整理 & 知識管理

### 3. Zotero MCP（選用）
- **GitHub**：https://github.com/adhikasp/mcp-zotero
- 讓 Claude Code 直接讀取 Zotero 文獻庫
- 可自動生成摘要、比較研究方法、產出 related works 段落
- 搭配 PubMed MCP 效果加倍
- ⚠️ 需要安裝 Zotero 本地端軟體；若繼續使用 EndNote 可略過此項

### 4. arXiv MCP Server
- **GitHub**：https://github.com/blazickjp/arxiv-mcp-server
- 直接搜尋 arXiv preprint
- 適合追蹤最新 AKI / CKD / dialysis 相關研究

---

## 🔬 研究寫作 & 統計報告

### 5. mcp-pandoc
- **GitHub**：https://github.com/vivekVells/mcp-pandoc
- 讓 Claude Code 直接生成 LaTeX / Word / Markdown 格式研究報告
- 適合搭配 journal-reading-latex skill
- 可自動排版 Table 1、Figure legend、References

### 6. Sequential Thinking MCP
- **GitHub**：https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
- 強化 Claude Code 的多步驟邏輯推理能力
- 適合設計複雜的統計分析流程（如 propensity score matching、survival analysis pipeline）
- 幫助規劃 research protocol

---

## 🏥 醫學特化工具

### 7. Filesystem MCP + pydicom（自定義 DICOM skill）
- **GitHub**：https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- 搭配 `pydicom` 讓 Claude Code 分析心導管影像 metadata
- 可批次整理 cath lab 的 DICOM header 資料

### 8. PostgreSQL MCP
- **GitHub**：https://github.com/modelcontextprotocol/servers/tree/main/src/postgres
- 若醫院有 PostgreSQL 臨床資料庫，可讓 Claude Code 直接下 query
- 適合從 HIS 抽取透析 + 心血管事件資料

---

## 💡 建議整體工作流程

```
PubMed MCP   ──► 文獻搜尋
EndNote      ──► 文獻管理（匯出 .bib）
DuckDB MCP   ──► 臨床資料分析
Pandoc MCP   ──► 論文寫作輸出
     │
     ▼
Claude Code 整合串接，一鍵完成從數據到論文
```

---

## 🖥️ 本地端安裝 Claude Code 步驟

### 前置需求
- Node.js v18 以上：https://nodejs.org/
- Git：https://git-scm.com/

### 安裝指令
```bash
# 安裝 Claude Code
npm install -g @anthropic-ai/claude-code

# 確認安裝成功
claude --version

# 進入您的研究專案資料夾後啟動
cd your-research-project
claude
```

### 設定 MCP Servers（以 PubMed 為例）
在專案根目錄建立 `.mcp.json`：
```json
{
  "mcpServers": {
    "pubmed": {
      "url": "https://pubmed.mcp.claude.com/mcp"
    },
    "duckdb": {
      "command": "npx",
      "args": ["-y", "mcp-server-duckdb"]
    }
  }
}
```

---

## 📦 您目前已具備的工具清單

| 工具 | 用途 | 狀態 |
|------|------|------|
| Claude Code | 核心 AI agent | ✅ 待安裝（本地端） |
| Cursor | LaTeX / 程式碼編輯器 | ✅ 使用中 |
| PubMed MCP | 文獻搜尋 | ✅ 已連接 |
| EndNote | 文獻管理 | ✅ 使用中 |
| LaTeX / BibTeX | 論文排版 | ✅ 建議安裝 |
| DuckDB MCP | 臨床資料分析 | 🔜 建議下一步安裝 |
| Zotero MCP | 文獻庫整合 | ⏸️ 選用（需裝 Zotero） |

---

*文件生成日期：2026年4月*
