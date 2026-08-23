# O014 Unit 027 QA receipt

Date: 2026-08-23  
Unit: `o014.aljabr2.chapter2.simplicity-and-semisimplicity`  
Title: `Objek Sederhana dan Semisederhana`  
Authority span: `chapter2.tex` lines 1133--1244 inclusive  
Decision: admitted as a translated, built, visually inspected cumulative boundary

This is a partial production checkpoint, not completion of the corpus-level
pursuit.

## Authority, map, and target identity

- Frozen authority commit: `9a5803ff77dd3257484cb177f851a73770a59dd3`; tree:
  `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`; license: CC BY 4.0.
- The normalized-LF authority slice `tmp/unit027-source-slice.tex` is 8,321
  bytes, SHA-256
  `e2f435c542379cd0f924343bd552514be261d8827dfa53afd107e20722ec213b`.
  It is byte-identical to the frozen source span; line 1245 begins the next
  section, `正合函子, 内射对象和投射对象`.
- `tmp/unit027-segment-map.jsonl` contains 38 unique source-ordered records,
  11,184 bytes, SHA-256
  `5d821f28602c5c7f40bfcb6569ccdf68f6aaac14bc9a5161a333d08f420d4fe6`.
- The admitted translation is `source/id-ID/chapter2-unit-027.tex`, 13,458
  bytes, SHA-256
  `bcf83b6829f1ea4fcd4a712e19f4c7f1402ed0990565aad2b6c5055fbe97cf66`.
  It is UTF-8 without BOM, LF-only, with no NUL, replacement character,
  Han/CJK residue, or mojibake.

## Mathematical and structural fidelity

The independent source audit found one section, one convention, two
definitions plus one definition--theorem, three lemmas, two propositions, two
remarks, six proofs, one two-item itemize, one three-item enumerate, five list
items, five display-math blocks, six labels, thirteen source-reference
occurrences over eleven unique keys, two citations, eleven index commands, one
footnote, and no exercises, hints, solutions, figures, TikZ, or external
assets. No confirmed mathematical defect was found.

All 38 map records have one unique target marker in exact map order; target and
map ID sets are identical. Labels, formulas, source xrefs, citations, index
commands, list structure, and theorem/proof boundaries are preserved. The
forward reference to `sec:Grothendieck-cat` uses the existing
`sourcecrossref` fallback so this partial reader has no unresolved reference;
the source section identity and future section number remain explicit.

Two presentational adaptations are disclosed: the Jordan--Hölder optional
heading is shortened to fit the localized theorem chrome, and a local sloppy
paragraph setting prevents a theorem-header overfull box. Neither changes the
mathematical statement. The target contains no source-language residue.

## Terminology and external field-use check

The bounded official arXiv search found no admissible Indonesian same-field
source with downloadable TeX. The instructed fallback used two official ITB
PDF witnesses; all sixteen pages were rendered and inspected directly. They
remain restricted local witnesses and are excluded from public payloads. The
method, identities, hashes, and decisions are recorded in
`controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md` (SHA-256
`8f112facd6d58c728d9e18d7b34a050064b62a8b0a2c2645d49682d4dbe98cd1`).

Unit 027 settles `semisederhana`, `objek terbelah`, `faktor komposisi`,
`multiplicitas`, `gelanggang pembagian`, and `kategori abelian
semisederhana/terbelah`, while retaining the established `objek sederhana`,
`deret komposisi`, `subkuosien`, `Noetherian`, `Artinian`, and `berpanjang
hingga`. The control glossary has 375 rows, 56,234 bytes, SHA-256
`f7da2827f72eb138de719321d7cc99914441b4ad41679538b262dffd747fca61`; the
modular backend has 375 rows, 24,887 bytes, SHA-256
`c39537a5ea87198b3d0311c5a10821edfa1142d799b3ab5a79a2704da748864f`.
Edition provenance identifies the production model exactly as **OpenAI Codex
gpt-5.6-sol, Ultra**. This does not displace Wen-Wei Li, component authors,
human direction, CC BY 4.0 obligations, or non-endorsement.

## Backend admission

- `backend/units.jsonl`: 27 unique sequential units, 20,066 bytes, SHA-256
  `87a7322bae33b27c1fc953d3bedf32d8346165cce4a672e2c4e0fd8ac3d0fb93`.
- `backend/segments.jsonl`: 1,274 unique segments, 360,796 bytes, SHA-256
  `c959e28face3800d41ec03b698f969b45a131028fe185732e800b189edae7ae8`.

The 38 Unit 027 backend records exactly equal the frozen segment map; unit IDs
and segment IDs are unique and every per-unit sequence is contiguous.

## Reproducible cumulative build

The wrapper is `source/id-ID/Al-jabr-2-id-cumulative-through-unit-027.tex`,
8,441 bytes, SHA-256
`682584a5b012055aea67be78799bb639d3529038961cfb589bd1af249755539c`.
The clean build ran in `build/cumulative-unit-027-final-20260823` with shell
escape disabled: XeLaTeX, Biber 2.21 with `source/id-ID` in `BIBINPUTS`, both
MakeIndex passes, and three final XeLaTeX passes. Biber resolved all eighteen
cited keys; MakeIndex accepted 125 terminology entries and 45 symbol entries
with zero rejection or warning.

The final log has no TeX/package error, undefined control sequence, unresolved
reference or citation, rerun request, overfull box, fatal error, or emergency
stop. Sixteen underfull boxes remain; MiKTeX's known release-date mismatch,
biblatex footnote-patching warning, and imakeidx rerun reminder are non-fatal
and retained in the build logs rather than hidden.

- PDF: 157 pages, 823,894 bytes, SHA-256
  `04af446ade23411da0a59a5f6a9f526b0267ddfe104c24e8fdedc0ad0583a6e0`.
- Final log: 78,003 bytes, SHA-256
  `90452dc2b32e3fa1c630d6d3ac2d886a0a21ca9b5f090738cf14a09f2265f866`.
- Resolved BBL: 24,833 bytes, SHA-256
  `308229e58134e11c6947ec59b712bf0b45e30a4bd235795fdc35ca2d9aca7128`.
- Term index: 5,318 bytes, SHA-256
  `725269a9abe882d5b9fe106c391224fd6283ba278a24ac48b7b1e19ac8f132d6`.
- Symbol index: 1,568 bytes, SHA-256
  `9cb539234abc1853507143cb820bc843324c31087efe0ea1bfc5b67c03d973f8`.

The checkpoint PDF and promoted cumulative PDF are byte-identical at the hash
above.

## Structural, accessibility, and visual PDF QA

The PDF is PDF 1.7, `id-ID`, unencrypted, uniform 498.9 x 708.66 point pages,
and untagged. It has 157 pages, 49 resolved fonts, 506 link annotations (494
internal/destination and 12 URI actions), and no forms, JavaScript, embedded
files, remote actions, or other active content. Mathematical font extraction
remains incomplete; the PDF is not claimed to be tagged or fully accessible.

Physical pages 147--150 (the complete Unit 027 section) were rendered at 180
dpi and visually inspected as a contact sheet and at high detail. The section
heading, theorem/proof transitions, list items, formulas, footnote, and final
remark are centered, readable, and unclipped. The contact sheet is
`tmp/pdfs/unit027-final-pages-147-150/contact-sheet.png`, 600,827 bytes,
SHA-256
`48e82f741f0678181c3ef2fa2635c4adb69b654eb69ddacc735ada1464c775e1`.
No visual defect was found.

## Admission and continuation

Admit Unit 027 and the 157-page cumulative boundary. Continue contiguously at
the next exact source span after line 1244 (`sec:inj-proj`, line 1245). This is
a production checkpoint, not pursuit completion.
