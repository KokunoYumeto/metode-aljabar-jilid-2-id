# Unit 028 QA — exact functors, injective and projective objects

Date: 2026-08-23  
Course/role: O014 / D80  
Unit: `o014.aljabr2.chapter2.exact-functors-injective-projective-objects`  
Locale: `id-ID`  
Authority: Wen-Wei Li, *Methods in Algebra, Volume 2: Linear Algebra*, Gitee
`master`, commit `9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.

## Scope and fidelity

The admitted source section is `chapter2.tex` lines 1245–1563, label
`sec:inj-proj`, beginning `正合函子, 内射对象和投射对象` and ending immediately
before `sec:Serre-subcat`. The normalized source slice is
`tmp/unit028-source-slice.tex` (24,797 bytes, SHA-256
`e6e50b76ae9dcd59f739e00b89347c0a0a05c303a6fff56934018301cd275d63`).
The Indonesian target is
`source/id-ID/chapter2-unit-028.tex` (37,694 bytes, SHA-256
`cd2f4bc1d7c2d4912650db33a934f9571f7a018d409a617fef4e61033d293a85`).
The 113-record stable segment map is
`tmp/unit028-segment-map.jsonl` (39,367 bytes, SHA-256
`0dfbfa43a29313cd1b3a57a9b72b64c2d668889e369605dd2709164688c6b9d8`).

Structural audit passed: 113 markers and map IDs are unique and in source
order; source/target begin/end markers are 57/57; labels 19/19; citations
6/6; `eqref` 2/2; index commands 6/6; TikZ-CD environments 17/17; display
environments 21/21; dollar delimiters are balanced. No Han characters, NULs,
replacement characters, private paths, stray leading `+`, or bare command
residue remain. The one source reference to `sec:derived-primer` is an
intentional forward reference and uses the local `\sourcecrossref` fallback
to the printed section number `3.12`; all labels and all remaining references
are preserved. No exercises or hints occur in this source section.

The target includes the disclosed O014-C027 source correction in a translator
footnote: the source's `H:X` assignment is rendered as `H:X\mapsto[X
\xrightarrow{\mathrm{id}_X}X]` so the displayed map has the intended object
assignment. This is a transparent correction, not a silent alteration.

## Backend and terminology

`backend/units.jsonl`: 28 records, 20,820 bytes, SHA-256
`f1dd95c50b2cde67c216df17a209aa6287bf26fd9dc6bb118bed79dc98ec7ae4`; the
Unit 028 record covers lines 1245–1563 and points to the target hash above.
`backend/segments.jsonl`: 1,387 records, 400,163 bytes, SHA-256
`91abf38aa24cbbe8104cbb61a118b443bc840baf3274e44c6386d56adc46de04`.
`backend/terms.csv`: 383 lines (382 terminology rows), 25,632 bytes, SHA-256
`eee2687340596e47610add6920f5a60982bdeba56d6cb91eba2cf93020f5a7f0`.
The coordinated terminology ledger has 382 rows, 57,895 bytes, SHA-256
`8aff5bad2fb43e8319426e54df1ff0ba48abf580ce5f8a3ceeb378a176cea8e3`.
Unit 028 adds the settled forms `funktor eksak`, `funktor eksak kiri/kanan`,
`funktor eksak setia`, `cukup banyak objek injektif/projektif`, `kategori
panah`, and `keeksakan lokalisasi`.

## Reproducible build and PDF checks

The shell-escape-disabled XeLaTeX/Biber/MakeIndex replay is
`build/cumulative-unit-028-final-20260823`. Biber completed with 18 citekeys;
MakeIndex completed with 131 term entries and 45 symbol entries; three final
XeLaTeX passes exited 0 and produced a 167-page PDF. The build log
`Al-jabr-2-id-cumulative-through-unit-028.log` is 78,367 bytes, SHA-256
`44f30cad450155076987d84ea4a6a7cd64e8b35bd768740f1be3ef6f47c1b7cd`.
The PDF is 167 pages, 868,564 bytes, SHA-256
`78c1ec3db75a97f3593d91412a8fbd19057d821df200cbc2893641dff5c48a43`.
The checkpoint and promoted cumulative output are byte-identical at:

- `output/pdf/checkpoints/metode-dalam-aljabar-jilid-2-id-through-unit-028.pdf`
- `output/pdf/metode-dalam-aljabar-jilid-2-id-cumulative.pdf`

The PDF is PDF 1.7, unencrypted and untagged. It has selectable text and
working internal/URI links, but it is not claimed to be a tagged accessible
PDF; accessible-reader work remains part of the full-corpus goal. No fatal
TeX errors, unresolved labels/citations, rerun requests, overfull boxes, or
missing-character diagnostics remain. Seventeen underfull-box diagnostics and
the known non-fatal MiKTeX release-date, fontspec, biblatex footnote, and
imakeidx warnings are retained as build notes.

Physical pages 153–167 were rendered with Poppler at 120 dpi and inspected.
Text, formulas, TikZ-CD diagrams, footnote placement, headers/footers, page
transitions, bibliography, and index divider pages are legible with no
clipping, overlap, black-square glyphs, or broken diagrams. Contact sheet:
`tmp/pdfs/unit028-final-pages-153-167/contact-sheet.png`, 825,266 bytes,
SHA-256 `912c627cebd05472f10bae56b5ba5922ce95a7ddc52b103b7df2361f070b4e6e`.

## Provenance and continuation

The edition metadata preserves Wen-Wei Li's attribution, CC BY 4.0 terms,
change notice, component provenance, non-endorsement, and the exact production
model note `OpenAI Codex gpt-5.6-sol, Ultra`. The next exact source cursor is
`chapter2.tex` line 1564, label `sec:Serre-subcat` (`Serre 子范畴和
\texorpdfstring{$\mathrm{K}_0$}{K0} 群`). This checkpoint admits Unit 028 but
does not complete the corpus.
