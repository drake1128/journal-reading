# Table Examples Reference (Markdown + Marp)

## Basic Two-Column Table

```markdown
| 項目 | 說明 |
|------|------|
| 項目一 | 說明內容 |
| 項目二 | 另一項說明 |
| **粗體項目** | 多行用分號分隔：第一點；第二點；第三點 |
```

## Clinical Trial Results Table

```markdown
| 結果指標 | 治療組 | 對照組 | P 值 |
|----------|--------|--------|------|
| 主要終點事件 | 12 (8.5%) | 24 (17.1%) | 0.032 |
| 心血管死亡 | 5 (3.5%) | 12 (8.6%) | 0.045 |
| 全因死亡 | 8 (5.7%) | 15 (10.7%) | 0.089 |
```

## Patient Characteristics Table

```markdown
| 特徵 | 治療組 (n=200) | 對照組 (n=200) |
|------|---------------|---------------|
| 年齡 (歲) | 65.2 ± 10.3 | 64.8 ± 9.8 |
| 男性 | 142 (71%) | 138 (69%) |
| BMI (kg/m2) | 26.5 ± 4.2 | 26.8 ± 4.5 |
| **病史** | | |
| 糖尿病 | 68 (34%) | 72 (36%) |
| 高血壓 | 156 (78%) | 148 (74%) |
| 心房顫動 | 45 (22.5%) | 48 (24%) |
| **心臟超音波** | | |
| LVEF (%) | 58.2 ± 8.5 | 57.8 ± 9.1 |
```

## Hazard Ratio Table

```markdown
| 終點 | HR | 95% CI | P 值 |
|------|-----|--------|------|
| **主要複合終點** | 0.72 | 0.52-0.99 | 0.018 |
| 心血管死亡 | 0.17 | 0.07-0.40 | < 0.001 |
| 全因死亡 | 0.66 | 0.47-0.93 | 0.015 |
| 心衰竭住院 | 0.32 | 0.17-0.58 | < 0.001 |
| 中風 | 0.83 | 0.45-1.53 | 0.55 |
```

## Subgroup Analysis Table

```markdown
| 亞組 | 事件數 | HR (95% CI) | P 值 | 交互作用 P |
|------|--------|-------------|------|-----------|
| **年齡** | | | | 0.35 |
| < 65 歲 | 45/180 | 0.72 (0.44-1.18) | 0.19 | |
| >= 65 歲 | 83/220 | 0.68 (0.45-1.02) | 0.06 | |
| **性別** | | | | 0.82 |
| 男性 | 92/280 | 0.70 (0.48-1.02) | 0.07 | |
| 女性 | 36/120 | 0.73 (0.42-1.28) | 0.27 | |
```

## Inclusion/Exclusion Criteria Table

```markdown
| 類型 | 標準 |
|------|------|
| **納入條件** | 年齡 20-85 歲；重度退化性二尖瓣逆流；LVEF > 60%；LVESD < 40mm |
| **排除條件** | 運動性呼吸困難；LVEF <= 60%；LVESD >= 40mm；新發持續性 AF |
```

## Drug Comparison Table

```markdown
| 特性 | **Drug A** | **Drug B** | **Drug C** |
|------|:---:|:---:|:---:|
| 半衰期 | **Short** | Long | Medium |
| 給藥途徑 | IV only | IV + PO | PO only |
| 代謝 | RBC | 肝臟 | 肝臟 |
| 劑量調整 | **不需要** | 需要 | 需要 |
```

## Marp Table Sizing Note

In Marp slides, tables use `font-size: 0.72em` by default (set in CSS). For tables with many columns, the content auto-wraps. If a table is too wide, reduce columns or abbreviate content — do NOT try to use HTML to resize.
