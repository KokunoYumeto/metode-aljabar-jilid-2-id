# O014 Unit 026 QA receipt

Date: 2026-08-23
Unit: `o014.aljabr2.chapter2.subobjects-and-isomorphism-theorems`
Title: `Subobjek dan Teorema Isomorfisme`
Authority span: `chapter2.tex` lines 911--1132 inclusive
Decision: admitted as a translated, built, and QA-passed cumulative boundary

This is a partial production checkpoint, not completion of the corpus-level
pursuit.

## Authority, map, and target identity

- Frozen authority commit:
  `9a5803ff77dd3257484cb177f851a73770a59dd3`; tree:
  `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`.
- The normalized-LF authority slice
  `tmp/unit026-source-slice.tex` is 15,939 bytes, SHA-256
  `85f25b07bbf35565c56e1f64ddb33c0a00ae79b1f60e3bb0aeb39ca982cccda8`.
  It is the exact source span through line 1132; line 1133 begins the next
  section, `单性和半单性`.
- `tmp/unit026-segment-map.jsonl` contains 62 unique, source-ordered
  records, 21,112 bytes, SHA-256
  `79144b8d751fc35c6c177f4b24595388fe1f117239277431eb0d2310483a08bb`.
- The admitted translation is `source/id-ID/chapter2-unit-026.tex`, 24,624
  bytes, SHA-256
  `52e87d044ba6a645a5c98329832fdb06272ce15106422c13ac402c75a67e200c`.
  It is UTF-8 without BOM, LF-only, with no NUL, replacement character, Han
  residue, or mojibake.

## Mathematical and structural fidelity

The independent source audit found one section, two definitions, one convention,
two propositions, one lemma, two corollaries, two theorems, seven proofs,
three lists with seven items, eight non-diagram display units, eighteen
TikZ-CD blocks with 98 arrows, eleven labels, 28 source reference occurrences
over nineteen unique keys, two citations, six index entries, and no exercise or
hint. The target preserves all of those counts and the exact source order.

All 62 map records have one unique target marker in map order; the target and
map ID sets are identical. Labels, citations, diagrams, arrows, lists, and
index commands are preserved. The target has one additional reference
occurrence in a translator footnote that documents O014-C026; all source
references remain present.

Two source defects are corrected and visibly disclosed:

1. O014-C025: source lines 987--988 declare `(X_i)` and `(Y_i)` but use
   `(X'_i)` and `(Y'_i)` in the formulas. The target primes the declaration
   (lines 169--174) and records the minimal notation repair.
2. O014-C026: source line 998 calls `f(X')` a coimage even though the
   definition at line 975 makes it `\Image[ X'\to X\to Y ]`, a subobject of
   `Y`. The target uses `citra` and discloses the type/definition repair at
   lines 189--194.

The independent target-fidelity audit also repaired three target-only issues
before admission: source-absent emphasis around `gabungan naik`, omitted
explicit `\Delta\to\Delta^-` notation and delimiters, and the antecedent
of the final pullback statement (the outer frame, not the upper-left square).
The final target contains no CJK residue or placeholder text.

## Terminology and external field-use check

The bounded official arXiv search found no admissible Indonesian same-field
source with downloadable TeX. The instructed fallback used two official ITB
PDF witnesses; all sixteen pages were rendered and inspected directly. They
remain restricted local witnesses and are excluded from public payloads. The
full method, identities, hashes, and decisions are in
`controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`, SHA-256
`8f112facd6d58c728d9e18d7b34a050064b62a8b0a2c2645d49682d4dbe98cd1`.

The control glossary now has 366 rows (including the Unit 026 terms
`irisan subobjek`, `jumlah subobjek`, `gabungan naik`, `prabayang
subobjek`, `isomorfisme kanonik`, `morfisme antidiagonal`,
`bijeksi pembalik urutan`, and `teorema isomorfisme`). Its current
control hash is
`5ec2c7be6b48a0272a169fe6ff4b0b1b426c9e627fa9be1b5588257fadc2ac97`;
the matching modular backend hash is
`65ee12e5df18726eea287d2135b718f85d2d65ccf0599de7146b6c7258beb935`.
Edition provenance identifies the production model exactly as **OpenAI Codex
gpt-5.6-sol, Ultra**. This does not displace Wen-Wei Li, witness authors,
component credits, human direction, CC BY 4.0 obligations, or
non-endorsement.

## Backend admission

- `backend/units.jsonl`: 26 unique sequential units, 19,337 bytes, SHA-256
  `1f7ab70854830c6ebc415a9345469514f5e4ec8bd4b68b400ccbe483aff93e01`.
- `backend/segments.jsonl`: 1,236 unique segments, 349,612 bytes, SHA-256
  `484ca4d97d0532cb0fb110f2a4748572d614ded21ced4b13287d6cea932523fc`.

The 62 Unit 026 backend records exactly equal the frozen segment map.
Unit IDs and segment IDs are unique; per-unit segment sequences are
contiguous.

## Reproducible cumulative build

The frozen wrapper is
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-026.tex`, 8,413 bytes,
SHA-256
`7730354f2ecf40e4e9a0ffd6d78dc1818419471b9537156d3c4eeccb9201ada9`.
The existing eighteen-entry bibliography remains byte-identical to the
validated prior boundary. The clean build ran in
`build/cumulative-unit-026-finalB-20260823` with shell escape disabled:
XeLaTeX, Biber 2.21 with `source/id-ID` in `BIBINPUTS`, both MakeIndex
passes, and three final XeLaTeX passes. Biber found all eighteen cited keys;
MakeIndex accepted 116 term entries and 43 symbol entries with zero
rejection or warning.

The final log has no TeX/package error, undefined control sequence, unresolved
reference or citation, rerun request, overfull box, fatal error, or emergency
stop. Ten underfull hboxes and six underfull vboxes remain. MiKTeX also
reports its known release-date mismatch, a biblatex footnote-patching warning,
and imakeidx's reminder about rerunning XeLaTeX; these are non-fatal and are
recorded rather than hidden.

- PDF: 152 pages, 807,443 bytes, SHA-256
  `1895b07aad71009c4c1d6594120d6f8f47694b751551aff3c1e1cbb3b4c31ed9`.
- Final log: 77,957 bytes, SHA-256
  `3bb583ec79afc9ea1f52f0212f7cf2c5a5420380ca76749deb684ceadeceb589`.
- Resolved BBL: 24,833 bytes, SHA-256
  `308229e58134e11c6947ec59b712bf0b45e30a4bd235795fdc35ca2d9aca7128`.
- Term index: 5,022 bytes, SHA-256
  `8e080c7cecbf1d6895acfc8b131cf4f243959911173dc3f5dc80d4d2182c9c3a`.
- Symbol index: 1,499 bytes, SHA-256
  `b6c45736464e5047d6bc8eac3b3ccf31bb0e5686d5a75a235dd8e9ac4675d627`.

The checkpoint PDF and promoted cumulative PDF are byte-identical at the
hash above.

## Structural, accessibility, and visual PDF QA

The PDF is PDF 1.7, `id-ID`, unencrypted, uniform 498.9 x 708.66 point
pages, and untagged. It has 152 pages, 32 outline entries, 489 link
annotations (477 internal/destination links and 12 URI actions), 49 resolved
fonts, and no forms, JavaScript, embedded files, remote actions, or other
active content. No link rectangle is malformed. Mathematical font extraction
remains incomplete; the PDF is not claimed to be tagged or fully accessible.

Physical pages 139--152 (the Unit 026 boundary, bibliography, and indexes)
were rendered at 150 dpi and visually inspected as a contact sheet and at
detail. The diagrams, theorem boxes, long formulas, correction notes,
bibliography, and indexes are centered, readable, and unclipped. The
high-detail render contact sheet is
`tmp/pdfs/unit026-finalB-pages/contact-sheet.png`, 481,082 bytes, SHA-256
`9d1f68c6e4129f45b8938bbda016cf07058b9ffb766a4f514ddb7bda6a3eed91`.
No visual defect was found.

## Admission and continuation

Admit Unit 026 and the 152-page cumulative boundary. Continue contiguously
with the next exact source span after line 1132. This is a production
checkpoint, not pursuit completion.
