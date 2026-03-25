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
  section.small-text { font-size: 0.85em; }
footer: 'Drake Hsieh MD, PhD, FESC | AI-Powered Literature Review | 2026'
---

<!-- _class: lead -->

# Leveraging AI for Literature Review

## Practical Approaches and Workflows Using Claude, PubMed & Semantic Scholar

**Drake Hsieh MD, PhD, FESC**
Hsinchu MacKay Memorial Hospital | 2026-03-16

---

# Outline

1. Why AI for Literature Review?
2. The Tool Ecosystem: Claude + MCP
3. PubMed MCP — Searching Biomedical Literature
4. Semantic Scholar MCP — Citation Network Analysis
5. **Live Workflow Demo**: End-to-End Literature Review
6. Practical Tips & Pitfalls
7. Summary & Q&A

---

<!-- _class: divider -->

# Part 1: Why AI for Literature Review?

---

# The Challenge of Modern Literature Review

- **PubMed** alone indexes **over 36 million** biomedical citations
- ~1.5 million new articles added per year
- A systematic review takes **6–18 months** on average
- Traditional workflow: manual search → screen → extract → synthesize

> **Key Problem**: The volume of scientific literature has outpaced human capacity to review it

---

# What AI Brings to the Table

| Traditional Approach | AI-Augmented Approach |
|---------------------|----------------------|
| Manual Boolean query construction | AI suggests & refines queries iteratively |
| Screen titles/abstracts one by one | Batch screening with relevance scoring |
| Manual data extraction into spreadsheets | Automated extraction from full text |
| Weeks to synthesize across papers | Real-time cross-paper synthesis |
| Citation chasing by hand | Automated citation network traversal |

---

# From Passive Search to Active Research Partner

```text
Traditional Workflow:
  Human → formulate query → run search → read abstracts → repeat

AI-Augmented Workflow:
  Human → describe research question
    → AI formulates multiple search strategies
    → AI runs searches across databases
    → AI retrieves & analyzes full text
    → AI synthesizes findings with citations
    → Human validates & refines
```

> **Shift**: The researcher becomes a **strategist and validator**, not a manual searcher

---

<!-- _class: divider -->

# Part 2: The Tool Ecosystem — Claude + MCP

---

# What is MCP (Model Context Protocol)?

- **Open standard** by Anthropic (Nov 2024) for AI ↔ external tool integration
- Allows Claude to **directly query** databases in real time
- No copy-paste, no switching tabs — everything happens in one conversation

### How It Works

```text
You (in Claude) → "Find recent RCTs on SGLT2 inhibitors in HFpEF"
        ↓
Claude → PubMed MCP → PubMed API → returns structured results
        ↓
Claude → analyzes, summarizes, and cites the papers
```

---

# Available MCP Connectors for Research

| MCP Server | What It Does | Best For |
|-----------|-------------|---------|
| **PubMed** | 36M+ biomedical citations, full text via PMC | Clinical literature, systematic reviews |
| **Semantic Scholar** | 200M+ papers, citation graphs, author profiles | Citation analysis, field mapping |
| **bioRxiv** | Preprint search (biology) | Cutting-edge, pre-peer-review findings |
| **Wiley (Scholar Gateway)** | Peer-reviewed Wiley content | Full-text access to Wiley journals |

> All of these are available **inside Claude** — no separate login or software needed

---

# Setting Up MCP Connectors

### For Claude.ai (Web/Team/Enterprise)

1. Go to **Settings → Connectors**
2. Find **PubMed** / **Semantic Scholar** → Click **"Connect"**
3. Start a new conversation — connectors are now active

### For Claude Code (CLI)

```text
Settings → MCP Servers → Add server configuration
  - PubMed: pubmed.mcp.claude.com
  - Semantic Scholar: semantic-scholar MCP server
```

> **No API key needed** for PubMed — it uses the public NCBI E-utilities

---

<!-- _class: divider -->

# Part 3: PubMed MCP — Searching Biomedical Literature

---

# PubMed MCP Capabilities

### What You Can Do

- **Keyword search** — natural language or Boolean queries
- **Author search** — find all papers by a specific author
- **Retrieve full metadata** — abstract, authors, journal, dates, MeSH terms
- **Get full text** — from PubMed Central (~8M articles)
- **Find related articles** — NCBI's related article algorithm
- **Convert IDs** — between PMID, PMC ID, and DOI

---

# Practical Example 1: Finding Recent RCTs

### Your Prompt to Claude:

> *"Search PubMed for randomized controlled trials published in the last 2 years on transcatheter edge-to-edge repair (TEER) for mitral regurgitation. Focus on MitraClip and PASCAL devices."*

### What Claude Does Behind the Scenes:

```text
1. Constructs query: "transcatheter edge-to-edge repair" OR "TEER"
   OR "MitraClip" OR "PASCAL" AND "randomized controlled trial"
   Filters: last 2 years
2. Sends to PubMed MCP → retrieves top results
3. Fetches abstracts and full text (if available in PMC)
4. Summarizes key findings in a structured table
```

---

# Practical Example 1: Sample Output

| Study | N | Device | Primary Endpoint | Result |
|-------|---|--------|-----------------|--------|
| CLASP IID (2024) | 350 | PASCAL vs MitraClip | MR reduction at 2y | Non-inferior |
| RESHAPE-HF2 (2025) | 505 | MitraClip + GDMT vs GDMT | HF hospitalization | Significant reduction |

Claude automatically provides:
- **PMID links** for each paper
- **Key inclusion/exclusion criteria**
- **Statistical details** (HR, CI, p-values)
- **Limitations noted by authors**

---

# Practical Example 2: Building a Search Strategy

### Your Prompt:

> *"Help me build a systematic search strategy for: 'Does AI-assisted ECG interpretation improve diagnostic accuracy for acute MI in the emergency department?' Test it on PubMed."*

### Claude's Approach:

```text
Concept 1: "artificial intelligence" OR "machine learning" OR "deep learning"
Concept 2: "electrocardiography" OR "ECG" OR "EKG"
Concept 3: "myocardial infarction" OR "acute coronary syndrome" OR "STEMI"
Concept 4: "emergency department" OR "emergency service"

Combined: (C1) AND (C2) AND (C3) AND (C4)
```

> Claude then **runs** this query, checks results, and suggests refinements

---

# PubMed MCP: Full-Text Analysis

### When a paper is in PubMed Central (PMC):

> *"Get the full text of PMID 38912345 and summarize the statistical methods used."*

### Claude retrieves and can:

- Extract **specific sections** (Methods, Results, Discussion)
- Compare **methods across multiple papers**
- Identify **statistical tests** used and whether they're appropriate
- Pull **exact numbers** from results tables
- Check for **reporting guideline adherence** (CONSORT, STROBE)

---

<!-- _class: divider -->

# Part 4: Semantic Scholar MCP — Citation Network Analysis

---

# Semantic Scholar MCP Capabilities

### What You Can Do

- **Search papers** — across 200M+ publications (all fields)
- **Get paper details** — abstract, citation count, venue, open access links
- **Citation graph traversal** — who cites this paper? what does it cite?
- **Author profiles** — h-index, publication history, top papers
- **Recommendations** — "papers like this one"
- **Related papers** — find similar work across fields
- **Export BibTeX** — for reference management

---

# Practical Example 3: Citation Network Mapping

### Your Prompt:

> *"Find the paper 'Transcatheter Mitral-Valve Repair in Patients with Heart Failure' (COAPT trial) on Semantic Scholar. Show me the 10 most influential papers that cite it."*

### Claude Does:

```text
1. Search Semantic Scholar → finds paper (Stone et al., NEJM 2018)
2. Get citations → retrieves all citing papers
3. Sorts by citation count + influence score
4. Returns structured summary of top 10 citing papers
5. Identifies key themes: patient selection, imaging, outcomes
```

> This reveals **how a landmark trial shaped the field**

---

# Practical Example 4: Author Impact Analysis

### Your Prompt:

> *"Look up Dr. Paul Sorajja on Semantic Scholar. What are his top 5 most-cited papers? What topics does he publish on most?"*

### Claude Returns:

- **h-index** and total citation count
- **Top papers** ranked by citations with key findings
- **Research theme clustering** — e.g., structural intervention, TAVR, TEER
- **Collaboration network** — frequent co-authors
- **Publication trajectory** — papers per year over time

> Useful for **identifying key opinion leaders** before a conference or collaboration

---

# Practical Example 5: Finding Research Gaps

### Combining PubMed + Semantic Scholar:

> *"Search for papers on AI-guided intraprocedural imaging during TEER. Use both PubMed and Semantic Scholar. Identify what has been studied and what gaps remain."*

### Multi-Database Workflow:

```text
Step 1: PubMed MCP → clinical studies with MeSH indexing
Step 2: Semantic Scholar → broader results including conference papers,
        preprints, and engineering publications
Step 3: Cross-reference → identify unique papers from each source
Step 4: Gap analysis → what questions remain unanswered?
```

---

<!-- _class: divider -->

# Part 5: Live Workflow Demo

---

# End-to-End Literature Review Workflow

### Research Question:
*"What is the current evidence for tricuspid TEER (TriClip) in patients with severe tricuspid regurgitation?"*

### Step-by-Step Workflow:

```text
Step 1: Search PubMed → clinical trials, guidelines, meta-analyses
Step 2: Search Semantic Scholar → expand to conference abstracts, preprints
Step 3: Retrieve full text → for key papers in PMC
Step 4: Synthesize → structured summary with evidence table
Step 5: Citation export → BibTeX for reference manager
Step 6: Identify gaps → what studies are still needed?
```

---

# Step 1: PubMed Search

### Prompt to Claude:

> *"Search PubMed for all studies on TriClip or tricuspid transcatheter edge-to-edge repair published since 2022. Include RCTs, observational studies, and systematic reviews."*

### Claude constructs and runs:

```text
("TriClip" OR "tricuspid edge-to-edge" OR "tricuspid TEER"
 OR "transcatheter tricuspid repair")
AND ("2022"[Date - Publication] : "3000"[Date - Publication])
```

Returns: study type, sample size, key outcomes, PMID links

---

# Step 2: Semantic Scholar Expansion

### Prompt to Claude:

> *"Now search Semantic Scholar for the same topic. Find papers that PubMed may have missed — especially conference abstracts, engineering papers on device design, and imaging studies."*

### Added Value:

| Source | PubMed Finds | Semantic Scholar Adds |
|--------|-------------|----------------------|
| RCTs | TRILUMINATE Pivotal | Early feasibility studies |
| Reviews | Systematic reviews | Narrative reviews from non-indexed journals |
| Imaging | Echo-focused papers | AI/ML imaging papers, conference proceedings |
| Device | Clinical reports | Engineering, bench testing, simulation studies |

---

# Step 3: Full-Text Deep Dive

### Prompt to Claude:

> *"Get the full text of the TRILUMINATE Pivotal trial from PMC. Extract: (1) patient selection criteria, (2) primary and secondary endpoints, (3) safety outcomes at 1 year, (4) subgroup analyses."*

### Claude extracts structured data directly from the paper — no manual reading needed for initial screening.

> **Important**: Always **verify AI-extracted data** against the original paper before citing in your own work.

---

# Step 4: Evidence Synthesis

### Prompt to Claude:

> *"Based on all the papers we found, create an evidence summary table for tricuspid TEER, organized by study design (RCTs, registries, case series). Include: sample size, follow-up, primary endpoint, and key safety data."*

### Claude produces a formatted evidence table ready for:
- **Journal club presentations**
- **Grant applications**
- **Guideline committee review**
- **Teaching handouts**

---

# Step 5: BibTeX Export

### Prompt to Claude:

> *"Export all the papers we discussed as BibTeX entries for my reference manager."*

### Claude uses Semantic Scholar MCP to generate:

```text
@article{sorajja2023triluminate,
  title={Transcatheter Tricuspid-Valve Repair ...},
  author={Sorajja, Paul and ...},
  journal={New England Journal of Medicine},
  year={2023},
  doi={10.1056/NEJMoa2300525}
}
```

> Import directly into **Zotero, Mendeley, or EndNote**

---

<!-- _class: divider -->

# Part 6: Practical Tips & Pitfalls

---

# Tips for Effective AI-Powered Literature Review

### Do's

- **Be specific** with your research question — Claude performs better with focused queries
- **Iterate** — refine searches based on initial results
- **Cross-reference** — use both PubMed AND Semantic Scholar for completeness
- **Verify** — always check AI-extracted data against original papers
- **Use date filters** — narrow to relevant time periods

### Don'ts

- Don't accept AI summaries without verification for **systematic reviews**
- Don't rely solely on abstracts — request **full text** when available
- Don't skip **MeSH terms** — they improve PubMed precision significantly

---

# Common Pitfalls and How to Avoid Them

| Pitfall | Solution |
|---------|----------|
| AI "hallucinates" a citation | Always verify PMID/DOI links are real |
| Search too broad (10,000+ results) | Add filters: study type, date, population |
| Search too narrow (0 results) | Remove outcome terms, broaden population |
| Missing key landmark papers | Ask Claude to check specific known papers |
| Outdated results | Specify date range explicitly |
| Full text not available | Check PMC, request via institutional access |

---

# Prompt Templates for Literature Review

### Template 1: Rapid Topic Overview
> *"Search PubMed and Semantic Scholar for the latest evidence on [TOPIC]. Summarize the top 10 most relevant papers in a table with: authors, year, study design, N, key finding."*

### Template 2: Systematic Search Strategy
> *"Build a Boolean search strategy for the PICO question: P=[population], I=[intervention], C=[comparator], O=[outcome]. Test it on PubMed and report the number of results."*

### Template 3: Citation Analysis
> *"Find [LANDMARK PAPER] on Semantic Scholar. List the 10 most-cited papers that reference it. What new directions has this work inspired?"*

---

# When to Use Which Tool

| Task | Best Tool | Why |
|------|-----------|-----|
| Clinical evidence search | **PubMed MCP** | MeSH indexing, RCT filters, clinical focus |
| Broad literature mapping | **Semantic Scholar MCP** | 200M+ papers, all disciplines |
| Citation network analysis | **Semantic Scholar MCP** | Citation graphs, influence scores |
| Full-text retrieval | **PubMed MCP** | PMC integration, ~8M full-text articles |
| Preprint search | **bioRxiv MCP** | Biology preprints, not yet peer-reviewed |
| Author profiling | **Semantic Scholar MCP** | h-index, co-author networks |

---

<!-- _class: divider -->

# Part 7: Summary & Key Takeaways

---

# The AI-Augmented Literature Review Workflow

```text
1. Define Research Question (PICO framework)
        ↓
2. Search PubMed MCP (clinical, indexed literature)
        ↓
3. Search Semantic Scholar MCP (broader, citation networks)
        ↓
4. Retrieve Full Text (PMC via PubMed MCP)
        ↓
5. Synthesize & Summarize (Claude analysis)
        ↓
6. Verify & Validate (human expert review)
        ↓
7. Export Citations (BibTeX via Semantic Scholar MCP)
        ↓
8. Write & Publish
```

---

# Key Takeaways

> **1.** AI does not replace the researcher — it **amplifies** your capacity to review literature

> **2.** MCP connectors give Claude **real-time access** to PubMed and Semantic Scholar — no copy-paste needed

> **3.** Use **PubMed** for clinical depth, **Semantic Scholar** for breadth and citation analysis

> **4.** Always **verify** AI-generated citations and extracted data

> **5.** The biggest efficiency gain is in **iterative search refinement** — what used to take days now takes minutes

---

<!-- _class: small-text -->

# References & Resources

1. Anthropic. How scientists are using Claude to accelerate research. [anthropic.com/news/accelerating-scientific-research](https://www.anthropic.com/news/accelerating-scientific-research)
2. Anthropic. Claude for Life Sciences. [anthropic.com/news/claude-for-life-sciences](https://www.anthropic.com/news/claude-for-life-sciences)
3. Anthropic. Introducing the Model Context Protocol. [anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol)
4. Tay A. MCP Servers and Academic Search — How Claude can pilot search strategies using PubMed. [aarontay.substack.com](https://aarontay.substack.com/p/mcp-servers-and-academic-search-the)
5. Tay A. The Agentic Researcher — Building custom workflows with Claude & MCP. [aarontay.substack.com](https://aarontay.substack.com/p/creating-your-own-research-assistant)
6. Claude Documentation. Using the PubMed Connector in Claude. [claude.com/resources/tutorials](https://claude.com/resources/tutorials/using-the-pubmed-connector-in-claude)
7. Semantic Scholar API Documentation. [semanticscholar.org](https://www.semanticscholar.org/)

---

<!-- _class: lead -->

# Thank You

## Questions & Discussion

**Drake Hsieh MD, PhD, FESC**

*This presentation was created using Claude Code with MCP integrations*
