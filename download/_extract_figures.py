"""
Extract figures from all downloaded TAVI complication case-report PDFs into
mainz-2024/images/tavi-complications/<PMID>_<Author>/fig-N.<ext>

Heuristics:
- Skip embedded images smaller than 200 px on the shorter side (logos, journal headers, icons).
- Sort images by page, then by their image rectangle area (largest first within page).
- For pages with several embedded images that are panels of one composite figure,
  ALSO render the full page at 200 dpi as a reference.
- Output a manifest JSON per paper listing extracted files plus their page+bbox metadata.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

DOWNLOAD = Path(__file__).parent
OUT_ROOT = DOWNLOAD.parent / "handouts" / "04-valvular-disease" / "mainz-2024" / "images" / "tavi-complications"
MIN_SIDE = 200  # px


def slug(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")


def extract_one(pdf_path: Path) -> dict:
    stem = pdf_path.stem  # e.g. 39822806_Sturla_2025
    out_dir = OUT_ROOT / slug(stem)
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    manifest = {"pdf": pdf_path.name, "pages": len(doc), "figures": []}

    fig_idx = 0
    for pno in range(len(doc)):
        page = doc[pno]
        infos = page.get_images(full=True)
        if not infos:
            continue
        # de-duplicate by xref
        seen = set()
        page_imgs = []
        for info in infos:
            xref = info[0]
            if xref in seen:
                continue
            seen.add(xref)
            try:
                ext = doc.extract_image(xref)
            except Exception:
                continue
            w, h = ext["width"], ext["height"]
            if min(w, h) < MIN_SIDE:
                continue
            page_imgs.append((xref, ext, w * h))
        page_imgs.sort(key=lambda t: -t[2])
        for xref, ext, _ in page_imgs:
            fig_idx += 1
            ext_name = ext["ext"]
            fname = f"fig-{fig_idx:02d}_p{pno+1}.{ext_name}"
            (out_dir / fname).write_bytes(ext["image"])
            manifest["figures"].append({
                "file": fname,
                "page": pno + 1,
                "width": ext["width"],
                "height": ext["height"],
                "ext": ext_name,
                "bytes": len(ext["image"]),
            })

    # Save text snapshot for the paper (used later when writing case summaries)
    text_path = out_dir / "_text.txt"
    if not text_path.exists():
        with text_path.open("w", encoding="utf-8") as f:
            for pno in range(len(doc)):
                f.write(f"\n=== PAGE {pno+1} ===\n")
                f.write(doc[pno].get_text("text"))

    (out_dir / "_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    doc.close()
    return manifest


def main():
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    pdfs = sorted(DOWNLOAD.glob("*.pdf"))
    print(f"[i] {len(pdfs)} PDFs to process")
    summary = []
    for pdf in pdfs:
        try:
            m = extract_one(pdf)
            summary.append({"pdf": pdf.name, "figures": len(m["figures"]), "pages": m["pages"]})
            print(f"  {pdf.name}: {len(m['figures'])} figs / {m['pages']} pages")
        except Exception as e:
            print(f"  {pdf.name}: ERROR {e}")
            summary.append({"pdf": pdf.name, "error": str(e)})
    (OUT_ROOT / "_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[i] Wrote summary to {OUT_ROOT / '_summary.json'}")


if __name__ == "__main__":
    main()
