#!/usr/bin/env python3
"""One deterministic offline-reader validation and hash manifest."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from lxml import html


UNIT_RE = re.compile(
    r"\\input\{((?:prelude-unit-\d{3}|chapter\d+-unit-\d{3}|"
    r"appendix\d+-unit-\d{3}|mastery-bridge-[^}]+))\}"
)
REMOTE = {"http", "https", "mailto", "tel", "urn", "doi"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", required=True, type=Path)
    parser.add_argument("--master", required=True, type=Path)
    parser.add_argument("--ledger", required=True, type=Path)
    args = parser.parse_args()

    expected = [f"{stem}.tex" for stem in UNIT_RE.findall(args.master.read_text(encoding="utf-8"))]
    with args.ledger.open(encoding="utf-8-sig", newline="") as stream:
        ledger_count = sum(1 for _ in csv.DictReader(stream))
    errors: list[str] = []
    html_files = sorted(args.dist.glob("*.html"))
    if not html_files:
        errors.append("tidak ada berkas HTML")

    parsed: dict[Path, object] = {}
    ids: dict[Path, set[str]] = {}
    math_count = 0
    math_source_count = 0
    image_count = 0
    applied_diagrams: set[str] = set()
    local_refs = 0
    for path in html_files:
        tree = html.parse(str(path), parser=html.HTMLParser(encoding="utf-8"))
        parsed[path] = tree
        id_values = [value for value in tree.xpath("//*[@id]/@id") if value]
        duplicate_ids = sorted({value for value in id_values if id_values.count(value) > 1})
        if duplicate_ids:
            errors.append(f"{path.name}: ID duplikat: {duplicate_ids[:10]}")
        ids[path] = set(id_values)
        if tree.getroot().get("lang") != "id-ID":
            errors.append(f"{path.name}: lang bukan id-ID")
        math_count += len(tree.xpath("//*[local-name()='math']"))
        math_source_count += len(tree.xpath(
            "//*[contains(concat(' ', normalize-space(@class), ' '), ' mathjax-inline ') or "
            "contains(concat(' ', normalize-space(@class), ' '), ' mathjax-display ') or "
            "contains(concat(' ', normalize-space(@class), ' '), ' math ')]"
        ))
        images = tree.xpath("//img")
        image_count += len(images)
        for image in images:
            if not (image.get("alt") or "").strip():
                errors.append(f"{path.name}: gambar tanpa alt: {image.get('src', '')}")
            if image.get("data-diagram-id"):
                applied_diagrams.add(image.get("data-diagram-id"))
        for diagram_id in tree.xpath("//*[@data-diagram-id]/@data-diagram-id"):
            applied_diagrams.add(diagram_id)

    index = args.dist / "index.html"
    if index in parsed:
        tree = parsed[index]
        units = tree.xpath("//section[@data-unit-file]/@data-unit-file")
        if units != expected:
            errors.append(f"index.html: urutan unit {len(units)} tidak sama dengan 148 input master")
        if len(tree.xpath("//nav[@class='reader-unit-index']//a")) != len(expected):
            errors.append("index.html: indeks unit tidak memuat 148 tautan")
        if len(applied_diagrams) != ledger_count:
            errors.append(
                f"index.html: alt ledger diterapkan pada {len(applied_diagrams)}/{ledger_count} diagram"
            )
        mathjax_scripts = tree.xpath("//script[contains(@src, 'mathjax-3.2.2/tex-chtml-full.js')]")
        if math_count == 0 and math_source_count == 0:
            errors.append("index.html: sumber matematika semantik tidak ditemukan")
        if not mathjax_scripts:
            errors.append("index.html: bundel MathJax lokal tidak dirujuk")

    for path, tree in parsed.items():
        for element, attribute in [
            ("a", "href"), ("img", "src"), ("link", "href"),
            ("object", "data"), ("source", "src"), ("script", "src"),
        ]:
            for node in tree.xpath(f"//{element}[@{attribute}]"):
                raw = (node.get(attribute) or "").strip()
                if not raw:
                    continue
                url = urlsplit(raw)
                if url.scheme.lower() in REMOTE:
                    if element != "a":
                        errors.append(f"{path.name}: aset jaringan: {raw}")
                    continue
                if url.scheme or raw.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:[\\/]", raw):
                    errors.append(f"{path.name}: path absolut/privat: {raw}")
                    continue
                target = path if not url.path else (path.parent / unquote(url.path)).resolve()
                try:
                    target.relative_to(args.dist.resolve())
                except ValueError:
                    errors.append(f"{path.name}: rujukan keluar dist: {raw}")
                    continue
                if not target.exists():
                    errors.append(f"{path.name}: target lokal hilang: {raw}")
                    continue
                local_refs += 1
                if url.fragment and target.suffix.lower() in {".html", ".htm"}:
                    if target not in parsed:
                        parsed[target] = html.parse(str(target), parser=html.HTMLParser(encoding="utf-8"))
                        ids[target] = set(parsed[target].xpath("//*[@id]/@id"))
                    if unquote(url.fragment) not in ids[target]:
                        errors.append(f"{path.name}: fragmen hilang: {raw}")

    report_path = args.dist / "validation-report.json"
    report = {
        "status": "pass" if not errors else "fail",
        "html_files": len(html_files),
        "units_and_bridges": len(expected),
        "mathml_elements": math_count,
        "mathjax_source_elements": math_source_count,
        "images": image_count,
        "diagram_alt_texts_applied": len(applied_diagrams),
        "ledger_diagrams": ledger_count,
        "local_references_checked": local_refs,
        "errors": errors,
        "limitations": [
            "MathML pronunciation depends on the browser and assistive technology.",
            "Complex diagram alt text is a summary, not a complete substitute for the visual relation.",
            "No WCAG conformance level or tagged-PDF claim is made.",
        ],
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifest_path = args.dist / "SHA256SUMS.txt"
    files = sorted(path for path in args.dist.rglob("*") if path.is_file() and path != manifest_path)
    lines = [f"{sha256(path)}  {path.relative_to(args.dist).as_posix()}" for path in files]
    manifest_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
