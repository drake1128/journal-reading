# Longtable Examples Reference

## Basic Two-Column Table

```latex
\begin{longtable}{p{4cm}p{10cm}}
\caption{基本雙欄表格} \\
\toprule
\textbf{項目} & \textbf{說明} \\
\midrule
\endfirsthead

\multicolumn{2}{c}{\textbf{表格續接}} \\
\toprule
\textbf{項目} & \textbf{說明} \\
\midrule
\endhead

\bottomrule
\endfoot

項目一 & 說明內容 \\
\midrule
項目二 & 多行內容第一行\newline
多行內容第二行 \\
\bottomrule
\end{longtable}
```

## Clinical Trial Results Table

```latex
\begin{longtable}{lccc}
\caption{臨床試驗結果比較} \\
\toprule
\textbf{結果指標} & \textbf{治療組} & \textbf{對照組} & \textbf{P值} \\
\midrule
\endfirsthead

\multicolumn{4}{c}{\textbf{表格續接}} \\
\toprule
\textbf{結果指標} & \textbf{治療組} & \textbf{對照組} & \textbf{P值} \\
\midrule
\endhead

\bottomrule
\endfoot

主要終點事件 & 12 (8.5\%) & 24 (17.1\%) & 0.032 \\
心血管死亡 & 5 (3.5\%) & 12 (8.6\%) & 0.045 \\
全因死亡 & 8 (5.7\%) & 15 (10.7\%) & 0.089 \\
\bottomrule
\end{longtable}
```

## Patient Characteristics Table

```latex
\begin{longtable}{lcc}
\caption{基線患者特徵} \\
\toprule
\textbf{特徵} & \textbf{治療組 (n=200)} & \textbf{對照組 (n=200)} \\
\midrule
\endfirsthead

\multicolumn{3}{c}{\textbf{表格續接}} \\
\toprule
\textbf{特徵} & \textbf{治療組} & \textbf{對照組} \\
\midrule
\endhead

\bottomrule
\endfoot

年齡 (歲) & 65.2±10.3 & 64.8±9.8 \\
男性 & 142 (71\%) & 138 (69\%) \\
BMI (kg/m²) & 26.5±4.2 & 26.8±4.5 \\
\midrule
\multicolumn{3}{l}{\textbf{病史}} \\
糖尿病 & 68 (34\%) & 72 (36\%) \\
高血壓 & 156 (78\%) & 148 (74\%) \\
心房顫動 & 45 (22.5\%) & 48 (24\%) \\
\midrule
\multicolumn{3}{l}{\textbf{心臟超音波}} \\
LVEF (\%) & 58.2±8.5 & 57.8±9.1 \\
LVESD (mm) & 35.2±4.8 & 35.8±5.2 \\
\bottomrule
\end{longtable}
```

## Hazard Ratio Forest-Style Table

```latex
\begin{longtable}{p{5cm}ccc}
\caption{Cox比例風險迴歸分析} \\
\toprule
\textbf{終點} & \textbf{HR} & \textbf{95\% CI} & \textbf{P值} \\
\midrule
\endfirsthead

\toprule
\textbf{終點} & \textbf{HR} & \textbf{95\% CI} & \textbf{P值} \\
\midrule
\endhead

\bottomrule
\endfoot

\textbf{主要複合終點} & 0.72 & 0.52-0.99 & 0.018 \\
心血管死亡 & 0.17 & 0.07-0.40 & <0.001 \\
全因死亡 & 0.66 & 0.47-0.93 & 0.015 \\
心衰竭住院 & 0.32 & 0.17-0.58 & <0.001 \\
中風 & 0.83 & 0.45-1.53 & 0.55 \\
\bottomrule
\end{longtable}
```

## Subgroup Analysis Table

```latex
\begin{longtable}{p{4cm}cccc}
\caption{亞組分析結果} \\
\toprule
\textbf{亞組} & \textbf{事件數} & \textbf{HR (95\% CI)} & \textbf{P值} & \textbf{交互作用P} \\
\midrule
\endfirsthead

\toprule
\textbf{亞組} & \textbf{事件數} & \textbf{HR (95\% CI)} & \textbf{P值} & \textbf{交互作用P} \\
\midrule
\endhead

\bottomrule
\endfoot

\textbf{年齡} & & & & 0.35 \\
<65歲 & 45/180 & 0.72 (0.44-1.18) & 0.19 & \\
≥65歲 & 83/220 & 0.68 (0.45-1.02) & 0.06 & \\
\midrule
\textbf{性別} & & & & 0.82 \\
男性 & 92/280 & 0.70 (0.48-1.02) & 0.07 & \\
女性 & 36/120 & 0.73 (0.42-1.28) & 0.27 & \\
\midrule
\textbf{糖尿病} & & & & 0.56 \\
有 & 58/140 & 0.75 (0.48-1.18) & 0.21 & \\
無 & 70/260 & 0.67 (0.44-1.02) & 0.06 & \\
\bottomrule
\end{longtable}
```

## Inclusion/Exclusion Criteria Table

```latex
\begin{longtable}{p{3cm}p{11cm}}
\toprule
\textbf{類型} & \textbf{標準} \\
\midrule
\endfirsthead

\toprule
\textbf{類型} & \textbf{標準} \\
\midrule
\endhead

\bottomrule
\endfoot

\textbf{納入條件} & 
• 年齡 20-85 歲\newline
• 重度退化性二尖瓣逆流\newline
• 左室射血分數 (LVEF) >60\%\newline
• 左室收縮末期直徑 (LVESD) <40mm\newline
• 有效逆流孔面積 (EROA) >0.4 cm² \\
\midrule
\textbf{排除條件} & 
• 運動性呼吸困難或心絞痛\newline
• LVEF ≤60\%\newline
• LVESD ≥40mm\newline
• 因二尖瓣逆流導致的新發持續性心房顫動\newline
• 明顯主動脈瓣疾病 \\
\bottomrule
\end{longtable}
```
