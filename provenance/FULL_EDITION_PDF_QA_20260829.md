# Full-edition PDF boundary - 2026-08-29

## Admitted artifact

- Reader PDF: `output/pdf/metode-dalam-aljabar-jilid-2-id-cumulative.pdf`
- Build witness: `build/complete-language-finalD-20260829/Al-jabr-2-id-complete-draft.pdf`
- Exact identity: 3,947,598 bytes; SHA-256 `bf6952fac3b4a9b3007853f0271e6fcf5126c4d113912ed591ee73396288a6e3`
- Source master: `source/id-ID/Al-jabr-2-id-complete-draft.tex`; 10,363 bytes; SHA-256 `5edd3a2582982bc02f8c2a98e1b0acd4acd38c9a79f8f6488579bb695b85aa38`
- Translation manifest: `qa/FULL_TRANSLATION_DRAFT_UNIT_MANIFEST.csv`; 146 rows listing 2,717,323 bytes; 16,506 bytes; SHA-256 `2d187091567e0ded4e9676b0918efabbdd16744760204019b6595ff3c9cfdd4c`

The promoted reader and the final build witness are byte-identical. This is the complete Indonesian language-pass boundary: Prelude, Chapters 1-9, Appendices A-B, every source exercise and hint, both independently attributed mastery bridges, bibliography, symbol index, and Indonesian/English terminology index.

## Deterministic build result

The bounded build ran three XeLaTeX passes with Biber and SplitIndex/MakeIndex. The final log is 152,449 bytes with SHA-256 `5a7af67efeef232b747262066a2caffd135465bc1c6f6c036e459551c163d995`.

Final-log counts:

- TeX/package errors, undefined control sequences, unresolved references, unresolved citations, rerun requests, missing characters, emergency stops, and fatal errors: 0
- Overfull horizontal boxes: 105
- Overfull vertical boxes: 0
- Underfull horizontal boxes: 97
- Underfull vertical boxes: 21

The box warnings were treated as inspection locators rather than grounds for repeated rebuilding. Sampled warning pages contain long formulas or diagrams but no visible clipping, collision, or unreadable content.

## PDF structure

`pdfinfo` and strict `pypdf` parsing report:

- PDF 1.7; 864 pages; unencrypted; no forms; no JavaScript
- title `Metode dalam Aljabar, Jilid 2: Aljabar Linear - Edisi Bahasa Indonesia`
- author `Wen-Wei Li`
- 3,810 named destinations
- 146 outline entries
- 3,583 link annotations, including 48 URI links
- 0 widgets

## Visual inspection

Fresh 120-dpi renders were inspected for the cover and attribution pages, table of contents, representative chapter openings across Chapters 1-9, both appendices, both mastery bridges, bibliography, symbol index, terminology index, and pages selected from the largest overfull-box reports. The inspected pages show centered page geometry, readable type, intact formulas and diagrams, working hierarchy, and no clipping, collision, black squares, or missing glyphs.

Final-build pages 1, 827, 836, and 864 were rendered directly from the admitted PDF and inspected after the metadata correction. Contact sheets retained under `tmp/pdfs/complete-language-finalC-20260829/` cover the broader representative and warning-page sample; direct final-build renders are under `tmp/pdfs/complete-language-finalD-20260829/`.

## Accessibility disclosure

The PDF is not tagged and its ToUnicode coverage is incomplete. Selectable text, outlines, and links do not make it a fully accessible PDF. Accessibility claims belong to the separate semantic offline reader, which remains an explicit release deliverable; this PDF is admitted as the complete printable reader only.

## Decision

PASS for complete printable-reader packaging and publication. Do not reopen per-unit translation or repeat the PDF build unless a concrete defect is later demonstrated. Continue directly with full backend reconciliation, semantic-reader completion, package manifests, and publication in the existing GitHub and Zenodo lineages.
