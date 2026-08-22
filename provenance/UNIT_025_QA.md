# O014 Unit 025 QA receipt

Date: 2026-08-22
Unit: `o014.aljabr2.chapter2.direct-sum-decomposition`
Title: `Dekomposisi Jumlah Langsung`
Authority span: `chapter2.tex` lines 721--910 inclusive
Decision: admitted as a translated, built, and QA-passed cumulative boundary

This is a partial production checkpoint, not completion of the corpus-level
pursuit.

## Authority, map, and target identity

- Frozen authority commit:
  `9a5803ff77dd3257484cb177f851a73770a59dd3`; tree:
  `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`.
- The authoritative `chapter2.tex` is 168,436 bytes, SHA-256
  `440c4c9e6b3bffbae4525d67ae1cabbca137b63e042cf82517b682e06fda6a79`.
- `tmp/unit025-source-slice.tex` is exactly the normalized-LF byte range for
  lines 721--910, including its terminal LF: 14,844 bytes, SHA-256
  `ad29667287d9332cbbbfb6218b05287edb0131ef1ab0d54b4a1cc322a010b857`.
- `tmp/unit025-segment-map.jsonl` contains 67 unique, sequential records:
  19,602 bytes, SHA-256
  `6567bda1d5ea871fda5e9c4f1617b5934fc6de5a43e265c047545a13e0426760`.
- The admitted translation is `source/id-ID/chapter2-unit-025.tex`, 22,660
  bytes, SHA-256
  `1d03a870340625913fedd6b399c7ceeef5cf7819ee7c454856e0102dcedf0dc4`.
  It is UTF-8 without BOM, LF-only, and contains no NUL, replacement
  character, Han residue, or mojibake.

Two independent read-only reviews found no admission-blocking defect. Every
map record is represented by one target marker in exact order, and the Unit
025 backend records are literal copies of the admitted map records. A complete
target reading found natural, faithful Indonesian with no substantive
omission.

## Mathematical and structural fidelity

The target preserves two definitions, two lemmas, three propositions, two
corollaries, one theorem, eight proofs, five lists with fifteen items, one
`align*`, three matrices, five TikZ-CD diagrams with 24 arrows, ten labels,
ten references, nine citations, and nine index commands. Label, reference,
and citation-key order is exact. There is no exercise or hint in this source
span.

The target has eleven display-math blocks where the source has ten. This is a
deliberate layout-only reflow: the long image-chain expression corresponding
to source line 896 moved from inline math to a display. Its mathematical
content is unchanged. A second layout-only reflow splits an overlong set of
bijections using `gathered`; neither change alters notation or meaning.

O014-C024 corrects the source prose at line 800 from the ill-typed
`r:X'\to X` to `r:X\to X'`. Condition (ii) already defines this direction,
requires `rf=\identity_{X'}`, and the later factorization requires the same
typing. Target lines 182--185 disclose the correction in a translator note,
and the exact evidence is registered in `controls/SOURCE_CORRECTIONS.csv`,
14,943 bytes, SHA-256
`0034cdb7e899113e787107497697793977830511904cb562eb7fee907c091164`.
No upstream contact occurred.

## Terminology and external field-use check

Before admitting this unit, the requested bounded official arXiv check found
no admissible Indonesian same-field source with downloadable TeX. The honest
fallback used two official ITB PDFs, all sixteen pages of which were rendered
and inspected directly. They are restricted local terminology witnesses and
are excluded from every public payload.

The witnesses confirm, among other forms, `jumlah langsung`, `dekomposisi
jumlah langsung`, `gelanggang`, `modul projektif`, `barisan eksak`, and
`kategori aditif`. Nine attested variants were added to the glossary notes.
No preferred-form replacement or retroactive prose change was justified. The
full bounded method, source identities, hashes, comparison, and decisions are
in `controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`, 7,965 bytes, SHA-256
`8f112facd6d58c728d9e18d7b34a050064b62a8b0a2c2645d49682d4dbe98cd1`.

Both terminology surfaces contain 358 unique concept IDs with exact
ID/preferred-form parity. The control ledger is 53,058 bytes, SHA-256
`bffb07f625a2a6c0327750e00d038fc451096fd32b0f23489fa8f853bd147717`;
the modular terminology backend is 23,774 bytes, SHA-256
`fd6358bc06cc6ce730723119e46fc85655381746e6a8fb6237aeb51a1d7ec28f`.
Unit 025 adds or settles `idempoten`, `kategori Karoubi`, `kategori
pseudoabelian`, `barisan eksak pendek terbelah`, `penampang`, `retraksi`,
`rantai ganda`, `syarat rantai ganda`, `nilpoten`, `gelanggang lokal`, and
`Lema Fitting`.

Edition provenance explicitly identifies the production model as **OpenAI
Codex gpt-5.6-sol, Ultra**. This does not displace the source author,
terminology-witness authors or supervisors, component credits, human
direction, CC BY 4.0 obligations, or non-endorsement.

## Backend admission

- `backend/units.jsonl`: 25 unique sequential units, 18,601 bytes, SHA-256
  `a9844fb07ed8320e83779dfd284be1bc2381bdb83b7bec43406c31ca92ddbc92`.
- `backend/segments.jsonl`: 1,174 unique segments, 328,500 bytes, SHA-256
  `5146ce4ea127bc458e52c6e6a972a31f55931bd67b9bd8000d0122d103e98bb5`.

The Unit 025 row contains the current target hash and the admitted status.
Unit IDs and segment IDs are unique, sequences are contiguous, and the 67
Unit 025 records have exact map/backend/marker parity.

## Reproducible cumulative build

The final frozen wrapper is
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-025.tex`, 8,623 bytes,
SHA-256
`ef028e191a5a36965fc9bf2d72923adbae84089f4d5f78eeb22c53e0aae863a3`.
The eighteen-entry frozen bibliography is 6,196 bytes, SHA-256
`0328bfd3515f737f7cbabfa5e3bacf8e4e983f1088b279ef7d09116bdf9c6918`.
Two Chinese-language bibliography records preserve exact original-script
metadata in source comments while using verified Hanyu Pinyin in visible
fields, avoiding a reader-visible defect on systems without Adobe-GB1 maps.

The final clean build ran in `build/cumulative-unit-025-final2-20260822` with
shell escape disabled: XeLaTeX, Biber 2.21 with `source/id-ID` in
`BIBINPUTS`, both MakeIndex passes, and three final XeLaTeX passes. Biber
resolved all eighteen cited keys. MakeIndex accepted 115 term entries and 38
symbol entries with zero rejection or warning. The final log has no TeX or
package error, undefined control sequence, unresolved reference or citation,
rerun request, overfull box, missing character, fatal error, or emergency
stop. Ten underfull hboxes and six visually benign underfull vboxes remain.

- PDF: 146 pages, 771,201 bytes, SHA-256
  `71f099e10d84e7d4f8c28756aba81c8ec82ca68a7f2d07df6cc168456efb5709`.
- Final log: 81,066 bytes, SHA-256
  `198f43e8276cf3d90256d9fcda80a156204faac4ff6364bbae43cb058162469a`.
- Resolved BBL: 24,833 bytes, SHA-256
  `308229e58134e11c6947ec59b712bf0b45e30a4bd235795fdc35ca2d9aca7128`.
- Term index: 4,990 bytes, SHA-256
  `e65ff77ccd6e143c7ce2c32e951e4d0097072bfeda9f317810a4cbb0d9786569`.
- Symbol index: 1,346 bytes, SHA-256
  `98f6367ea38dde5461be69127c4620a4c35e2d309d0f3686f36ab89cbeb7d6ec`.

The frozen checkpoint and promoted cumulative reader are byte-identical.

## Structural, accessibility, and visual PDF QA

Strict parsing reports PDF 1.7, `id-ID`, unencrypted, uniform
498.9-by-708.66-point pages, and zero rotation. The reader has 31 valid
outline entries, 580 valid named destinations, and 456 link annotations: 444
resolved internal links and 12 URI actions over ten unique HTTPS URLs. Every
link rectangle is positive-area and contained within its page. There is no
form, field, widget, JavaScript, additional action, embedded or associated
file, portfolio, launch, remote-GoTo, or media action. The catalog open action
is only a fit-to-page view of physical page 1.

All 49 recursively discovered fonts are embedded and subset; 41 have
ToUnicode maps. The eight without ToUnicode are mathematical/symbol fonts and
FandolSong. Pypdf extracts 266,590 characters with zero U+FFFD but 670 NULs
from incompletely mapped mathematics. MuPDF retains 178 private-use delimiter
pieces and exposes additional replacement characters from the same mapping
limitations. These are genuine semantic/accessibility limits: the PDF is
untagged and is not represented as fully accessible. They are not visible
corruption. The personal-name token prohibited for public output is absent
from extracted text, metadata, and raw token checks.

All 146 pages were freshly rendered at 70 dpi and reviewed as a full contact
sheet. Physical pages 129--146 were also reviewed at higher detail; physical
page 3 was rerendered at 140 dpi after replacing an awkward URL wrap with two
centered, human-readable links; bibliography page 142 was independently
inspected. The five blank physical pages are 2, 4, 106, 140, and 144 and are
intentional recto/front-matter transitions. Unit 025, its five diagrams,
matrices, long reflowed formulas, correction note, bibliography, and both
indexes are centered, legible, and free of clipping, overlap, detached
punctuation, off-page material, or missing visible glyphs.

## Admission and continuation

Admit Unit 025 and the 146-page cumulative boundary. Resume contiguously at
Unit 026, `chapter2.tex` lines 911--1132, stable ID
`o014.aljabr2.chapter2.subobjects-and-isomorphism-theorems`, Indonesian title
`Subobjek dan Teorema Isomorfisme`. Line 1133 starts the following section.
