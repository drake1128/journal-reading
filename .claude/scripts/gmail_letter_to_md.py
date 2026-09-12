#!/usr/bin/env python3
"""Convert a Gmail HTML 導讀信 (as saved htmlBody) into clean Markdown for Quarto.

Usage: gmail_letter_to_md.py letter.html > letter.md

Steps: unwrap Google redirect links → strip presentational attributes →
collapse single-cell layout tables into headings/paragraphs → pandoc → tidy.
"""
import re, sys, subprocess
from urllib.parse import unquote
from lxml import html as LH, etree

SRC = sys.argv[1]
raw = open(SRC, encoding="utf-8").read()

# 1. Google redirect links → original URL
raw = re.sub(r'https://www\.google\.com/url\?q=(https?://[^&"\s]+)[^"\s]*',
             lambda m: unquote(m.group(1)), raw)

doc = LH.fromstring(raw)

# 2. strip presentational attributes (keep href / src / alt)
KEEP = {"href", "src", "alt"}
for el in doc.iter():
    if not isinstance(el.tag, str):
        continue
    for a in list(el.attrib):
        if a not in KEEP:
            del el.attrib[a]

# 3. collapse layout tables (one direct row × one direct cell), outermost first, repeat
def direct_rows(t):
    return t.xpath("./tbody/tr|./thead/tr|./tr")
changed = True
while changed:
    changed = False
    for tbl in list(doc.iter("table")):
        rows = direct_rows(tbl)
        if len(rows) != 1:
            continue
        cells = rows[0].xpath("./td|./th")
        if len(cells) != 1:
            continue
        td = cells[0]
        txt = "".join(td.itertext()).strip()
        has_block = any(isinstance(c.tag, str) and c.tag in ("p","ol","ul","table","div","h1","h2","h3","pre") for c in td)
        if len(txt) <= 60 and not has_block and "\n" not in txt:
            new = LH.Element("h3"); new.text = txt
        else:
            new = LH.Element("div"); new.text = td.text
            for c in list(td):
                new.append(c)
        tbl.getparent().replace(tbl, new)
        changed = True
        break

# 4. two-cell side-by-side comparison tables (one <tr> with 2 <td>, no <th>) → sequential blocks
for tbl in list(doc.iter("table")):
    rows = tbl.findall(".//tr")
    if len(rows) == 1 and not tbl.findall(".//th") and len(rows[0].findall("td")) == 2:
        wrap = LH.Element("div")
        for td in rows[0].findall("td"):
            p = etree.SubElement(wrap, "p")
            p.text = td.text
            for c in td:
                p.append(c)
        tbl.getparent().replace(tbl, wrap)

# 4b. ensure first row with <th> lives in <thead> so pandoc emits a real header
for tbl in list(doc.iter("table")):
    rows = tbl.findall(".//tr")
    if rows and rows[0].findall("th") and tbl.find("thead") is None:
        thead = LH.Element("thead"); thead.append(rows[0]); tbl.insert(0, thead)
    elif rows and not tbl.findall(".//th"):
        # no header at all → synthesize an empty-ish header from column count
        n = len(rows[0].findall("td"))
        thead = LH.Element("thead"); tr = etree.SubElement(thead, "tr")
        for i in range(n):
            th = etree.SubElement(tr, "th"); th.text = "　"
        tbl.insert(0, thead)

# 5. <br> inside table cells → " / " so pipe tables stay single-line
for br in list(doc.iter("br")):
    if br.xpath("ancestor::td|ancestor::th"):
        br.tail = " · " + (br.tail or "")
        br.drop_tree()

cleaned = etree.tostring(doc, encoding="unicode", method="html")

md = subprocess.run(
    ["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"],
    input=cleaned, capture_output=True, text=True, check=True).stdout

# 6. tidy: remove leftover Gmail signature / blank lines
md = re.sub(r"\n{3,}", "\n\n", md)
md = md.replace("\\<", "<").replace("\\>", ">")
# headings: promote h1 (letter title) to h2 so page has a single H1
md = re.sub(r"^# ", "## ", md, flags=re.M)
print(md.strip() + "\n")
