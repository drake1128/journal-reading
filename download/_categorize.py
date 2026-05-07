"""Categorize 194 TAVI complication case reports by title keywords.

Outputs CATEGORIES.md — a topic-organized index Drake can use to plan
which articles to convert into handouts next.
"""
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

DOWNLOAD_DIR = Path(__file__).parent
STATUS_FILE = DOWNLOAD_DIR / "_download_status.tsv"
OUT_FILE = DOWNLOAD_DIR / "CATEGORIES.md"

# Order matters — first matching category wins. More specific patterns first.
CATEGORIES: list[tuple[str, list[str]]] = [
    ("Coronary obstruction / Anomaly / BASILICA / Spasm", [
        r"coronar(y|ies)", r"left main", r"\bLMCA\b", r"ostia(l|um)",
        r"\bACS\b", r"\bSTEMI\b", r"NSTEMI", r"infarct",
        r"BASILICA", r"chimney", r"snorkel", r"sinus sequest",
        r"anomalous origin", r"vessel spasm", r"multivessel spasm",
        r"cardiac arrest.*spasm",
    ]),
    ("Annular / Aortic root rupture / Dissection / Arch rupture / Calcification", [
        r"annular (rupture|injury|dissection|calcif)", r"annulus rupture",
        r"aortic (rupture|root rupture|root injury|dissection)",
        r"contained rupture", r"sinus rupture", r"sinus of Valsalv",
        r"intramural h[ae]matoma", r"\bIMH\b", r"type [AB] dissection",
        r"device landing zone", r"landing zone.*rupture",
        r"aortic arch rupture", r"aortic annular calcif",
        r"false lumen", r"anastomosis leak", r"Cabrol",
    ]),
    ("Valve embolization / Migration / Dislocation / Malposition", [
        r"\bembol(?!ic)", r"migrat", r"displac", r"dislodg", r"malposit",
        r"dislocat", r"anchoring balloon", r"valve.{0,15}(into|in.the).{0,15}(aorta|left ventricle|ventricle)",
    ]),
    ("Paravalvular leak (PVL) / Regurgitation", [
        r"paraval", r"\bPVL\b", r"\bPVR\b", r"perivalv", r"regurg",
        r"intraprosthetic",
    ]),
    ("Thrombosis / Leaflet / Sinus / Valsalva thrombus / HALT", [
        r"thromb", r"\bHALT\b", r"hypoattenuated",
        r"reduced leaflet motion", r"\bRLM\b",
        r"frozen leaflet", r"stuck leaflet", r"mobile leaflet mass",
        r"leaflet (mass|modification|laceration)",
        r"BABICORN", r"\bROBIN\b", r"radiofrequency guidewire.*leaflet",
        r"contrast retention",
    ]),
    ("Endocarditis / Mycotic / Abscess / Infection", [
        r"endocard", r"infect", r"abscess", r"veget", r"mycotic",
    ]),
    ("Stroke / Cerebral / TIA", [
        r"\bstroke\b", r"cerebr", r"\bTIA\b", r"intracrani", r"cerebrovascular",
        r"silent.*infarct",
    ]),
    ("Vascular access / Bleeding / Iliofemoral / Closure / Carotid / Subclavian", [
        r"vascular (complication|injury|access|closure)", r"access[- ]site",
        r"iliac", r"iliofemoral", r"femor", r"axillary", r"subclavian",
        r"carotid", r"transcaval",
        r"perforat", r"pseudoaneur", r"arteriovenous fistula", r"\bAV fistula\b",
        r"\bbleed", r"hematoma", r"haemorrhage", r"hemorrhage",
        r"closure device", r"ProGlide", r"Manta",
        r"arteriovenous loop", r"aortic.{0,5}aneurysm",
    ]),
    ("Mitral injury / SAM / LVOT obstruction / Suicide LV", [
        r"mitral", r"\bSAM\b", r"systolic anterior motion",
        r"LVOT obstruction", r"left ventricular outflow",
        r"suicide left ventricle", r"chordal",
        r"Mavacamten", r"hypertrophic cardiomyopathy", r"\bHCM\b",
        r"continuous assessment.*LVOT",
    ]),
    ("Cardiac tamponade / Pericardial / Ventricular perforation", [
        r"tamponade", r"pericard", r"hemoperic",
        r"ventricular perforat", r"cardiac perforat",
    ]),
    ("Conduction / AV block / Pacemaker / Bradyarrhythmia", [
        r"conduct", r"pacemaker", r"bundle branch",
        r"atrioventricular", r"AV[- ]block", r"complete heart block",
        r"brady", r"asystole", r"His[- ]bundle",
        r"left bundle branch area pacing", r"\bCSP\b",
    ]),
    ("Iatrogenic VSD / Septal injury / Fistula", [
        r"\bVSDs?\b", r"ventricular septal defect", r"iatrogenic.*septal",
        r"septal (injury|perforat|rupture|defect)",
        r"fistula", r"aorto[- ]right ventricular", r"aorto[- ]left",
        r"LVOT.{0,5}LA fistula",
    ]),
    ("Multi-valve / Concurrent / Combined procedures (TAVR + TEER/PBPV/TEVAR/SAVR)", [
        r"double valve", r"multi[- ]valv", r"multivalv",
        r"\bPBPV\b", r"pulmonary balloon", r"\bTEVAR\b",
        r"rheumatic heart", r"combined.{0,10}TAVR", r"simultaneous TAVR",
        r"left[- ]sided double", r"prosthetic heart valve interaction",
        r"alpha[- ]gal", r"one[- ]stop", r"surgical reintervention",
    ]),
    ("Bicuspid / Special anatomy / Small annulus / Horizontal aorta", [
        r"bicuspid", r"\bBAV\b(?!.*atrioventricular)", r"unicuspid",
        r"low coronar", r"low[- ]lying coronary", r"sievers",
        r"horizontal (aorta|heart)", r"acute aortic angulation",
        r"porcelain aorta", r"narrow sinus", r"narrow STJ",
        r"sinotubular junction", r"small (annul|aortic annul)",
        r"large (annul|aortic annul)", r"extremely large annulus",
        r"aortic coarctation",
    ]),
    ("Valve-in-Valve / Redo TAVR / Explantation", [
        r"valve[- ]in[- ]valve", r"\bViV\b", r"\bredo\b",
        r"repeat TAVR", r"second TAVR", r"failed transcath",
        r"explant", r"reintervent",
    ]),
    ("Heart failure / Cardiogenic shock / ECMO / Pulm HTN", [
        r"cardiogenic shock", r"valvular shock",
        r"heart failure", r"acute heart failure",
        r"\bECMO\b", r"\bMCS\b", r"Impella",
        r"pulmonary hypertension", r"\bPAH\b",
    ]),
    ("Imaging guidance (3D-print / 4D-CT / TEE / ICE / Multi-modality)", [
        r"3D[- ]print", r"3D model", r"three[- ]dimensional",
        r"4D[- ]CT", r"\bMDCT\b", r"computed tomography.*guidance",
        r"\bTEE\b", r"transesophag", r"transoesophag",
        r"intracardiac echo", r"\bICE\b(?![A-Z])", r"ICE[- ]guided",
        r"multimodality imaging", r"image[- ]guided",
        r"fusion imaging",
    ]),
    ("Procedural rescue / Bailout / Snare / Wire loss / Recapture", [
        r"bail.?out", r"\brescue\b", r"\bsalvage\b", r"snare", r"retriev",
        r"crossover", r"buddy wire", r"emergency convers",
        r"wire loss", r"failure to recapture",
        r"antegrade and retrograde",
    ]),
    ("Device malfunction (Delivery system / Balloon / Sheath / Capsule)", [
        r"delivery system (malfunction|failure)", r"buckling",
        r"balloon rupture", r"valve balloon.*rupture", r"rupture of.*valve balloon",
        r"capsule demolition", r"infolded", r"valve.*malfunction",
        r"sheath.*bioprosthesis", r"sheath and self-expanding",
        r"complicated interaction.*balloon",
    ]),
    ("Structural valve deterioration / Bioprosthetic failure", [
        r"structural (valve|deterior)", r"\bSVD\b",
        r"valve degener", r"bioprosth.*(failure|dysfunct|degener)",
        r"valve failure", r"valve dysfunction",
    ]),
    ("Special populations / Comorbidity (Hematologic / Amyloid / Pregnancy / Pediatric)", [
        r"h[ae]matolog", r"amyloid", r"pregnan", r"p[ae]diatric",
        r"Marfan", r"Ehlers-Danlos", r"connective tissue",
        r"safety and feasibility",
    ]),
    ("Bowel / GI / Non-cardiac collateral", [
        r"necrotic bowel", r"bowel ischem", r"mesenteric",
    ]),
]

DEFAULT_CATEGORY = "Other / Miscellaneous"


def categorize(title: str) -> str:
    t = title or ""
    # Normalize whitespace (nbsp, en-space, em-space, etc.) to regular space
    t = re.sub(r"[\s  -​]+", " ", t)
    for cat, patterns in CATEGORIES:
        for pat in patterns:
            if re.search(pat, t, flags=re.I):
                return cat
    return DEFAULT_CATEGORY


def load_status_with_titles():
    rows = []
    with open(STATUS_FILE, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for r in reader:
            rows.append(r)
    return rows


def main():
    rows = load_status_with_titles()
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        cat = categorize(r["title"])
        r["category"] = cat
        by_cat[cat].append(r)

    ordered_keys = [c for c, _ in CATEGORIES] + [DEFAULT_CATEGORY]

    lines = []
    lines.append("# TAVI 併發症 Case Reports — 主題分類索引")
    lines.append("")
    lines.append(f"**194 篇** TAVI complication case reports，以標題關鍵字分至 **{len([k for k in ordered_keys if by_cat.get(k)])}** 個主題類別。")
    lines.append("")
    lines.append("圖示說明：✓ = 已下載 PDF；✗ = 未下載（付費或新文章未索引）")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Top-level summary
    lines.append("## 各類別篇數總覽")
    lines.append("")
    lines.append("| # | 主題類別 | 總計 | 已下載 |")
    lines.append("|---|---------|------|--------|")
    idx = 1
    for cat in ordered_keys:
        items = by_cat.get(cat, [])
        if not items:
            continue
        ok = sum(1 for x in items if x["status"] in ("ok", "exists"))
        anchor = re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")
        lines.append(f"| {idx} | [{cat}](#{idx}-{anchor}) | {len(items)} | {ok} |")
        idx += 1
    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed listing
    idx = 1
    for cat in ordered_keys:
        items = by_cat.get(cat, [])
        if not items:
            continue

        ok_count = sum(1 for x in items if x["status"] in ("ok", "exists"))

        lines.append(f"## {idx}. {cat}")
        lines.append("")
        lines.append(f"**{len(items)} 篇**（{ok_count} 已下載 / {len(items)-ok_count} 未下載）")
        lines.append("")

        items.sort(key=lambda x: (-int(x["year"] or 0), x["author"], x["pmid"]))

        lines.append("| 狀態 | 年 | 期刊 | First Author | 標題 | 檔案 / DOI |")
        lines.append("|------|----|----|-------------|------|-----------|")
        for r in items:
            status_icon = "✓" if r["status"] in ("ok", "exists") else "✗"
            title = r["title"].replace("|", "\\|").rstrip(".")
            if r["status"] in ("ok", "exists"):
                file_link = f"`{r['filename']}`"
            else:
                doi = r["doi"]
                if doi:
                    file_link = f"[DOI](https://doi.org/{doi})"
                else:
                    file_link = f"[PMID](https://pubmed.ncbi.nlm.nih.gov/{r['pmid']}/)"
            jrnl = r["journal"].replace("JACC Cardiovasc Interv", "JACC CV Interv") \
                                .replace("JACC Case Rep", "JACC CR") \
                                .replace("Circ Cardiovasc Interv", "Circ CV Interv") \
                                .replace("Circ Cardiovasc Imaging", "Circ CV Img")
            lines.append(f"| {status_icon} | {r['year']} | {jrnl} | {r['author']} | {title} | {file_link} |")
        lines.append("")
        lines.append("---")
        lines.append("")
        idx += 1

    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {OUT_FILE}")
    print(f"\nCategories with counts (in order):")
    total_ok = 0
    total_all = 0
    for cat in ordered_keys:
        items = by_cat.get(cat, [])
        if items:
            ok = sum(1 for x in items if x["status"] in ("ok", "exists"))
            total_ok += ok
            total_all += len(items)
            print(f"  {cat}: {len(items)} ({ok} dl)")
    print(f"\nTotal: {total_all} ({total_ok} downloaded)")


if __name__ == "__main__":
    main()
