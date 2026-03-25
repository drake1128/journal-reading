---
name: journal-reading-markdown
description: Create bilingual (Traditional Chinese with English medical terminology) Markdown educational documents from medical literature. Generates both long-form handout (.md) and Marp presentation slides (_Marp.md → .pptx). Use when Drake (謝慕揚醫師) requests document creation from journal articles, podcasts, or research papers. Triggers on "整理", "請幫我整理", "markdown", "marp", "期刊講義", "journal reading", "教學", or references to medical literature from NEJM, JACC, Circulation, EuroIntervention, European Heart Journal.
---

# Journal Reading Markdown Document Skill

Create comprehensive bilingual medical education documents in Markdown format from journal articles and research papers.

## Output Specification

- **Primary output**: Markdown handout (`.md`) + Marp slides (`_Marp.md`)
- **Compiled output**: PowerPoint (`.pptx`) via Marp CLI
- **Optional**: PDF via Marp CLI (`--pdf`)
- **Legacy**: LaTeX (`.tex`) only when explicitly requested

## Build Commands

```bash
# Generate PPTX
marp --no-stdin "Filename_Marp.md" --pptx -o "Filename.pptx" --allow-local-files

# Generate PDF
marp --no-stdin "Filename_Marp.md" --pdf -o "Filename.pdf" --allow-local-files
```

## Author Attribution

Always use: `謝慕揚 MD, PhD, FESC`

## Language Rules

1. Main text in **Traditional Chinese** (繁體中文)
2. Preserve **English** for:
   - Drug names (medications) - NEVER translate
   - Medical terminology
   - Lab tests and procedures
   - Clinical trial names
   - Statistical terms (HR, CI, p-values)
   - Anatomical terms
3. Format: `中文說明 (English term)`

## Handout Markdown Structure

```markdown
# Title / 中文標題

**整理：謝慕揚 MD, PhD, FESC**
**日期：YYYY-MM-DD**

---

## Section

### Subsection

Content with tables, blockquotes, lists...

---

## 參考文獻

1. Author, et al. Title. [*Journal*. Year;Vol:Pages.](https://doi.org/DOI)

---

*本文件僅供醫療專業人員教學參考，臨床決策請結合個案情況。*
```

## Marp Slide Rules (CRITICAL)

### CSS Safety — Avoid Black Blocks
1. **NO** `@import url()` for Google Fonts — use local fonts only
2. **NO** `linear-gradient()` — use flat `background-color` only
3. **NO** custom HTML `<div>` elements — pure Markdown only
4. **NO** dark `pre` backgrounds — use `background-color: #f5f6fa`
5. Use `background-color` not shorthand `background`

### Slide Types
- Title/End: `<!-- _class: lead -->` (dark blue bg `#1a2740`)
- Section divider: `<!-- _class: divider -->` (blue bg `#0072bc`)
- Small text: `<!-- _class: small-text -->` (for references)
- Normal: no class needed (white bg)

### Color Scheme
```
#ba181b  emergency_red   → h1 headers, strong text, blockquote borders
#0072bc  emergency_blue  → h2 headers, table headers, divider slides
#555555  emergency_gray  → h3 headers
#1a2740  lead_bg         → title/end slide backgrounds
#f5f6fa  code_bg         → code block backgrounds
#fff5f5  blockquote_bg   → blockquote backgrounds
```

## Table Formatting

Standard Markdown pipe tables:
```markdown
| Column A | Column B | Column C |
|----------|----------|----------|
| Data     | **Bold** | Data     |
```

## Citation Format (Vancouver Style)

```markdown
1. Author1, Author2, et al. Title. [*Journal*. Year;Vol(Issue):Pages.](https://doi.org/DOI)
```

Without DOI:
```markdown
1. Author1, et al. Title. *Journal*. Year;Vol:Pages.
```

## DOI Verification (CRITICAL)

1. Search: `"article title" + journal + year + DOI`
2. Use `https://doi.org/` prefix
3. **NEVER fabricate DOIs** — cite without link if unverifiable
4. Cross-check DOI resolves to correct article

## Statistics Presentation

- Hazard ratios: `HR 0.72 (95% CI 0.52-0.99)`
- P-values: `P = 0.018` or `P < 0.001`
- Confidence intervals in parentheses

## Drug Information

- Generic names in English only (NEVER translate)
- Dosing in original units
- Include brand names if clinically relevant

## Quality Checklist Before Delivery

- [ ] All DOI links verified via web search
- [ ] Drug names remain in English
- [ ] Author listed as 謝慕揚 MD, PhD, FESC
- [ ] Vancouver citation format used
- [ ] Marp slides: NO Google Fonts import, NO gradients, NO custom divs
- [ ] Marp slides: light code block backgrounds only
- [ ] Marp PPTX generated with `--no-stdin` flag
- [ ] Files moved to appropriate `handouts/` subfolder
