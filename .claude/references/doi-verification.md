# DOI Verification Reference Guide

## Common Medical Journal DOI Patterns

### NEJM (New England Journal of Medicine)
- Pattern: `10.1056/NEJMoaXXXXXX` or `10.1056/NEJMXXXXXXXX`
- Example: `https://doi.org/10.1056/NEJMoa2107659`

### JACC (Journal of the American College of Cardiology)
- Pattern: `10.1016/j.jacc.XXXX.XX.XXX`
- Example: `https://doi.org/10.1016/j.jacc.2021.01.001`

### JACC Cardiovascular Interventions
- Pattern: `10.1016/j.jcin.XXXX.XX.XXX`
- Example: `https://doi.org/10.1016/j.jcin.2025.07.038`

### Circulation
- Pattern: `10.1161/CIRCULATIONAHA.XXX.XXXXXX`
- Example: `https://doi.org/10.1161/CIRCULATIONAHA.112.099606`

### European Heart Journal
- Pattern: `10.1093/eurheartj/XXXXX`
- Example: `https://doi.org/10.1093/eurheartj/ehab368`

### EuroIntervention
- Pattern: `10.4244/EIJXXX` or `10.4244/EIJ-D-XX-XXXXX`
- Example: `https://doi.org/10.4244/EIJY14M04_11`

### Lancet
- Pattern: `10.1016/S0140-6736(XX)XXXXX-X`
- Example: `https://doi.org/10.1016/S0140-6736(21)00677-2`

### Nature Medicine
- Pattern: `10.1038/s41591-XXX-XXXXX-X`
- Example: `https://doi.org/10.1038/s41591-021-01449-5`

### JAMA
- Pattern: `10.1001/jama.XXXX.XXXXXX`
- Example: `https://doi.org/10.1001/jama.2013.278477`

### CHEST
- Pattern: `10.1016/j.chest.XXXX.XX.XXX`
- Example: `https://doi.org/10.1016/j.chest.2024.08.020`

### Critical Care Medicine
- Pattern: `10.1097/CCM.XXXXXXXXXXXXXXXX`
- Example: `https://doi.org/10.1097/CCM.0000000000006966`

### Intensive Care Medicine
- Pattern: `10.1007/s00134-XXX-XXXXX-X`
- Example: `https://doi.org/10.1007/s00134-021-06506-y`

### Critical Care
- Pattern: `10.1186/s13054-XXX-XXXXX-X`
- Example: `https://doi.org/10.1186/s13054-024-05174-w`

## Verification Search Queries

### Template
```
"[Article Title]" [Journal] [Year] [First Author] DOI
```

### Examples
```
"Effect of heart rate control with esmolol" JAMA 2013 Morelli DOI
"Landiolol and Organ Failure" JAMA 2023 Whitehouse DOI
```

## Citation Format

### Markdown (Primary)
```markdown
1. Author1, Author2, et al. Title. [*Journal*. Year;Vol(Issue):Pages.](https://doi.org/10.xxxx/xxxxxx)
```

### Without DOI (Markdown)
```markdown
1. Author1, et al. Title. *Journal*. Year;Vol:Pages.
```

### LaTeX (Legacy)
```latex
\item Author1, Author2, et al. Title. \href{https://doi.org/DOI}{\textit{Journal}. Year;Vol(Issue):Pages.}
```

## Common DOI Issues

1. **Typos in DOI number** - Verify each digit
2. **Wrong protocol** - Use `https://doi.org/` not `http://` or `dx.doi.org/`
3. **Spaces in DOI** - Remove all spaces
4. **Case sensitivity** - DOIs are case-insensitive but keep original case

## When to Skip Hyperlink

- Cannot find DOI after multiple searches
- DOI resolves to wrong article
- Article is too recent (DOI not yet indexed)
- Preprint without official DOI
