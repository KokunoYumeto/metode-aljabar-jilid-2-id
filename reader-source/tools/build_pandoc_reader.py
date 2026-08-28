#!/usr/bin/env python3
"""Build the complete reflowed reader directly from the admitted LaTeX units.

This is the deterministic fallback for a reproducible TeX4ht failure in the
book's list/array and multi-column math surfaces. Pandoc preserves prose,
lists, headings and raw TeX math; local MathJax renders the mathematics.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import html as html_std
import json
import re
import shutil
import subprocess
from collections import defaultdict
from pathlib import Path

from lxml import etree, html


UNIT_RE = re.compile(
    r"\\input\{((?:prelude-unit-\d{3}|chapter\d+-unit-\d{3}|"
    r"appendix\d+-unit-\d{3}|mastery-bridge-[^}]+))\}"
)
DIAGRAM_RE = re.compile(
    r"\\begin\{(tikzcd|tikzpicture)\}(.*?)\\end\{\1\}", re.DOTALL
)
ENV_NAMES = {
    "theorem": "Teorema", "teorema": "Teorema", "corollary": "Korolari",
    "korolari": "Korolari", "lemma": "Lema", "lema": "Lema",
    "proposition": "Proposisi", "proposisi": "Proposisi",
    "definition": "Definisi", "definisi": "Definisi",
    "definition-theorem": "Definisi–Teorema", "definisiteorema": "Definisi–Teorema",
    "definisi-proposisi": "Definisi–Proposisi", "definisiproposisi": "Definisi–Proposisi",
    "hypothesis": "Hipotesis", "hipotesis": "Hipotesis",
    "conjecture": "Konjektur", "konjektur": "Konjektur",
    "example": "Contoh", "contoh": "Contoh", "remark": "Catatan",
    "catatan": "Catatan", "convention": "Konvensi", "konvensi": "Konvensi",
    "proof": "Bukti", "bukti": "Bukti", "latihan": "Latihan",
}


def macro_preamble(source_dir: Path) -> str:
    """Collect balanced command declarations Pandoc can expand in math."""
    declarations: list[str] = []
    starters = re.compile(
        r"^\s*\\(?:newcommand|renewcommand|providecommand|DeclareMathOperator\*?|"
        r"DeclarePairedDelimiterX?|DeclareRobustCommand|newrobustcmd)"
    )
    for name in ("mycommand.sty", "myarrows.sty"):
        lines = (source_dir / name).read_text(encoding="utf-8").splitlines()
        collecting: list[str] = []
        balance = 0
        for line in lines:
            if not collecting and starters.match(line):
                collecting = [line]
                balance = line.count("{") - line.count("}")
                if balance <= 0:
                    declarations.append("\n".join(collecting))
                    collecting = []
            elif collecting:
                collecting.append(line)
                balance += line.count("{") - line.count("}")
                if balance <= 0:
                    declarations.append("\n".join(collecting))
                    collecting = []
    return "\n".join(declarations) + "\n"


def preprocess(text: str, rows: list[dict[str, str]]) -> tuple[str, list[str]]:
    # Preserve every durable segment and LaTeX label as an HTML anchor.
    text = re.sub(r"(?m)^\s*%\s*segment-id:\s*([^\s]+)\s*$", r"\\hypertarget{\1}{}", text)
    text = re.sub(r"\\label\{([^}]+)\}", r"\\hypertarget{\1}{}", text)
    text = re.sub(
        r"\\sourcecrossref\{([^}]+)\}\{([^}]*)\}",
        r"\\href{#\1}{\2}", text,
    )
    text = re.sub(r"\\eqref\{([^}]+)\}", r"\\href{#\1}{persamaan}", text)
    text = re.sub(r"\\ref\{([^}]+)\}", r"\\href{#\1}{rujukan}", text)
    text = re.sub(
        r"\\cite(?:\[[^]]*\])?\{([^}]+)\}",
        lambda m: "\\href{#ref-" + m.group(1).split(",")[0].strip() + "}{[" + m.group(1) + "]}",
        text,
    )

    for env, label in ENV_NAMES.items():
        pattern = re.compile(r"\\begin\{" + re.escape(env) + r"\}(?:\[([^]]*)\])?")
        text = pattern.sub(lambda m: "\\par\\noindent\\textbf{" + label + (" (" + m.group(1) + ")" if m.group(1) else "") + ".}\\quad ", text)
        text = re.sub(r"\\end\{" + re.escape(env) + r"\}", r"\\par", text)
    text = re.sub(r"\\begin\{Exercises\}", r"\\section*{Latihan}", text)
    text = re.sub(r"\\end\{Exercises\}", "", text)
    text = re.sub(r"\\begin\{hint\}", r"\\textbf{Petunjuk.}\\quad ", text)
    text = re.sub(r"\\end\{hint\}", "", text)
    text = re.sub(r"\\begin\{petunjukbacaan\}", r"\\par\\noindent\\textbf{Petunjuk Bacaan.}\\quad ", text)
    text = re.sub(r"\\end\{petunjukbacaan\}", r"\\par", text)

    tokens: list[str] = []
    index = 0
    def diagram_sub(match: re.Match[str]) -> str:
        nonlocal index
        token = f"READERDIAGRAM{index:04d}"
        tokens.append(token)
        kind = match.group(1)
        index += 1
        return (r"\text{" + token + "}" if kind == "tikzcd" else r"\par\textbf{" + token + r"}\par")
    text = DIAGRAM_RE.sub(diagram_sub, text)
    return text, tokens


def convert_one(args: tuple[int, str, Path, str, list[dict[str, str]], Path]) -> dict[str, object]:
    order, stem, source_path, macros, rows, pandoc = args
    source, tokens = preprocess(source_path.read_text(encoding="utf-8"), rows)
    completed = subprocess.run(
        [str(pandoc), "-f", "latex+raw_tex", "-t", "html5", "--mathjax", "--wrap=none"],
        input=macros + source, text=True, encoding="utf-8", capture_output=True,
        check=False,
    )
    if completed.returncode:
        raise RuntimeError(f"Pandoc gagal pada {source_path.name}: {completed.stderr}")
    wrapper = html.fragment_fromstring("<div></div>")
    for fragment in html.fragments_fromstring(completed.stdout):
        if isinstance(fragment, str):
            if fragment.strip():
                paragraph = etree.SubElement(wrapper, "p")
                paragraph.text = fragment
        else:
            wrapper.append(fragment)

    known_ids = set(re.findall(r"\\hypertarget\{([^}]+)\}", source))
    renamed: dict[str, str] = {}
    for node in wrapper.xpath(".//*[@id]"):
        old = node.get("id")
        if old and old not in known_ids:
            new = f"{stem}--{old}"
            node.set("id", new)
            renamed[old] = new
    for link in wrapper.xpath(".//a[starts-with(@href, '#')]"):
        old = link.get("href")[1:]
        if old in renamed:
            link.set("href", "#" + renamed[old])

    # Pandoc cannot emit a DOM anchor when \label occurred inside display math.
    # Retain those stable targets at the owning unit boundary so every xref is
    # keyboard-navigable even when the exact equation-level placement is lost.
    present_ids = set(wrapper.xpath(".//*[@id]/@id"))
    for missing_id in sorted(known_ids - present_ids):
        wrapper.insert(0, etree.Element("span", {"id": missing_id, "class": "reader-anchor-fallback"}))

    applied = 0
    for token, row in zip(tokens, rows):
        hits = wrapper.xpath(f"//*[contains(string(.), '{token}')]")
        target = None
        if hits:
            # Choose the deepest hit carrying the token.
            target = hits[-1]
            while target.getparent() is not None and target.getparent() is not wrapper and target.tag not in {"p", "span", "div"}:
                target = target.getparent()
        figure = etree.Element(
            "figure", {"class": "reader-diagram", "role": "img",
                       "data-diagram-id": row["diagram_id"],
                       "aria-label": row["alt_text_id"].strip()}
        )
        caption = etree.SubElement(figure, "figcaption")
        strong = etree.SubElement(caption, "strong")
        strong.text = f"Diagram {row['diagram_id']}. "
        strong.tail = row["alt_text_id"].strip()
        if target is not None and target.getparent() is not None:
            target.getparent().replace(target, figure)
        else:
            wrapper.append(figure)
        applied += 1
    # A ledger row is still useful even if Pandoc absorbed its visual wrapper.
    for row in rows[applied:]:
        figure = etree.SubElement(
            wrapper, "figure", {"class": "reader-diagram", "role": "img",
                                "data-diagram-id": row["diagram_id"],
                                "aria-label": row["alt_text_id"].strip()}
        )
        caption = etree.SubElement(figure, "figcaption")
        caption.text = f"Diagram {row['diagram_id']}. {row['alt_text_id'].strip()}"
        applied += 1
    return {"order": order, "stem": stem, "html": html.tostring(wrapper, encoding="unicode"),
            "stderr": completed.stderr, "diagrams": applied}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--reader", required=True, type=Path)
    args = parser.parse_args()
    project = args.project.resolve()
    reader = args.reader.resolve()
    source_dir = project / "source" / "id-ID"
    master = source_dir / "Al-jabr-2-id-complete-draft.tex"
    dist = reader / "dist"
    build = reader / "build"
    dist.mkdir(parents=True, exist_ok=True)
    build.mkdir(parents=True, exist_ok=True)
    pandoc = Path(shutil.which("pandoc") or "")
    if not pandoc:
        raise SystemExit("pandoc tidak ditemukan")

    stems = UNIT_RE.findall(master.read_text(encoding="utf-8"))
    if len(stems) != 148:
        raise SystemExit(f"148 unit/bridge diharapkan; ditemukan {len(stems)}")
    with (project / "backend" / "figure-alt-text-id.csv").open(encoding="utf-8-sig", newline="") as stream:
        ledger_rows = list(csv.DictReader(stream))
    ledger: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in ledger_rows:
        ledger[row["unit_filename"]].append(row)
    for rows in ledger.values():
        rows.sort(key=lambda row: int(row["local_order"]))
    macros = macro_preamble(source_dir)
    jobs = [
        (i, stem, source_dir / f"{stem}.tex", macros, ledger.get(f"{stem}.tex", []), pandoc)
        for i, stem in enumerate(stems)
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(convert_one, jobs))
    results.sort(key=lambda row: row["order"])

    bib = subprocess.run(
        [str(pandoc), "-f", "latex", "-t", "html5", "--citeproc",
         "--bibliography", str(source_dir / "Al-jabr.bib"), "--wrap=none"],
        input=r"\nocite{*}", text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout
    nav_items = "\n".join(
        f'<li><a href="#unit-{r["stem"]}">{html_std.escape(r["stem"].replace("-", " "))}</a></li>'
        for r in results
    )
    sections = "\n".join(
        f'<section id="unit-{r["stem"]}" class="reader-unit" data-unit-file="{r["stem"]}.tex" role="doc-chapter">'
        f'{r["html"]}</section>' for r in results
    )
    document = f'''<!doctype html>
<html lang="id-ID"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="Wen-Wei Li">
<meta name="description" content="Metode dalam Aljabar, Jilid 2 — edisi Bahasa Indonesia lengkap.">
<title>Metode dalam Aljabar, Jilid 2: Aljabar Linear — Edisi Bahasa Indonesia</title>
<link rel="stylesheet" href="reader.css">
<script>window.MathJax={{tex:{{tags:"ams"}},options:{{enableAssistiveMml:true}},chtml:{{fontURL:"vendor/mathjax-3.2.2/output/chtml/fonts/woff-v2"}}}};</script>
<script defer src="vendor/mathjax-3.2.2/tex-chtml-full.js"></script></head><body>
<a class="skip-link" href="#main-content">Lewati ke konten utama</a>
<header class="reader-header"><a class="reader-home" href="index.html">Metode dalam Aljabar II</a><span class="reader-edition">Edisi Bahasa Indonesia</span></header>
<main id="main-content" class="reader-main" tabindex="-1">
<section class="reader-cover" aria-labelledby="book-title"><h1 id="book-title">Metode dalam Aljabar</h1><p class="reader-cover-volume">Jilid 2: Aljabar Linear</p><p class="reader-cover-author">Wen-Wei Li, penulis</p><hr><h2>Tentang edisi ini</h2><p>Edisi Bahasa Indonesia lengkap dari karya sumber 2024.</p><p class="reader-cover-license">CC BY 4.0. Edisi independen; penulis dan penerbit sumber tidak mendukung atau mengesahkannya.</p></section>
<nav class="reader-unit-index" aria-label="Navigasi unit"><details open><summary>Navigasi 146 unit dan 2 jembatan</summary><ol>{nav_items}</ol></details></nav>
{sections}
<section id="bibliography" class="reader-unit"><h1>Daftar Pustaka</h1>{bib}</section>
</main><footer class="reader-footer"><span>Pembaca luring — edisi Bahasa Indonesia</span><a href="accessibility.html">Aksesibilitas, atribusi, dan batasan</a></footer></body></html>'''
    (dist / "index.html").write_text(document, encoding="utf-8")
    shutil.copy2(reader / "reader.css", dist / "reader.css")
    shutil.copy2(reader / "accessibility.html", dist / "accessibility.html")
    shutil.copy2(reader / "LICENSE.txt", dist / "LICENSE.txt")
    shutil.copytree(reader / "vendor" / "mathjax-3.2.2", dist / "vendor" / "mathjax-3.2.2", dirs_exist_ok=True)
    report = {
        "backend": "Pandoc LaTeX reader + local MathJax 3.2.2",
        "units_and_bridges": len(results), "ledger_diagrams": len(ledger_rows),
        "diagram_descriptions_embedded": sum(int(r["diagrams"]) for r in results),
        "pandoc_warnings": [r["stderr"] for r in results if str(r["stderr"]).strip()],
        "explicit_limitation": "Diagram visual TeX/TikZ diganti deskripsi tekstual ledger pada fallback pembaca; PDF mempertahankan visual asli.",
    }
    (build / "reader-build-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
