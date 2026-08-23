# O014 Unit 030 admission and reader QA

Date: 2026-08-23  
Unit: `o014.aljabr2.chapter2.grothendieck-categories`  
Title: *Kategori Grothendieck*  
Result: **PASS — translated, structurally audited, built, rendered, and admitted**

## Authority and exact scope

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled Gitee `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 030 is
exactly `chapter2.tex` lines 1756--2132 inclusive: all of
`sec:Grothendieck-cat` followed by the complete Chapter 2 `Exercises` closure.
The next unadmitted source is `chapter3.tex` line 9, label `sec:cplx`.

The normalized-LF authority slice is `tmp/unit030-source-slice.tex`, 30,150
bytes, SHA-256
`4b3ed0e1d7676d37d3bf465a241df0116fbb0e28cf39cd1b313a9f9f19225b7e`.
It is byte-equal to the frozen authority lines after LF normalization and one
terminal LF. The 133-record stable-ID map is
`tmp/unit030-segment-map.jsonl`, 41,437 bytes, SHA-256
`dff9eaedeaaaad88c10b68d40fd4683f0e27f88164985b1824aef5bfb71b85b7`.

## Translation, topology, and mathematical review

The admitted target is `source/id-ID/chapter2-unit-030.tex`, 43,836 bytes and
880 lines, SHA-256
`a7fec40262a70c2f7fe253a97cf21558acc3c0b32272e3bcdb24a04e58c96697`.
The complete section and all 20 chapter exercises are natural id-ID
translations; all 13 active hints and the one intentionally commented hint
remain in their source positions. No answer or solution has been attributed
to the author.

All 133 stable markers are unique and occur in exact map order. The Unit-030
backend has 133 rows in raw-line exact map parity. Source/target parity passes
for 15 labels, 46 reference occurrences over the same 35 targets, eight
citation-key occurrences with exact keys `Gr57` and `Li1`, five index commands,
66 active begin/end environments, nine TikZ-CD diagrams, two `gather*`, one
`multline*`, one `align*`, and the complete exercise/hint closure. The source
and localized target respectively contain three definitions, four
propositions, two lemmas, one theorem, five corollaries, one example, and
twelve proofs; their localized environment names are `definisi`, `proposisi`,
`lema`, `teorema`, `korolari`, `contoh`, and `bukti`.

Braces, environment stacks, and math delimiters are balanced. No Han residue,
NUL, replacement character, stray patch marker, duplicate marker, or bare
command line remains. The core category-theoretic notation and variance,
smallness and universe qualifiers, ordinal recursion, generator/cogenerator
constructions, all diagrams, and the Chapter 2 exercise topology were reviewed
against the source. No independently defensible new source correction was
found, so `controls/SOURCE_CORRECTIONS.csv` remains unchanged at SHA-256
`4bf6f3e68c82f4b6eea6bab4753071ad628d68696d723c9bb526648d74aeb0ef`.

Two target-only presentation adaptations are deliberate and do not change the
mathematics. First, the source's forward `eqref` to `eqn:I-small-gen`, whose
definition occurs in Appendix A outside the current partial reader, uses
`sourcecrossref` with printed fallback `A.2.1`; this keeps the cumulative
reader resolved now and becomes a live internal link when the appendix enters
the full reader. Second, a long Hom-map that overflowed the measure was moved
from inline math to an unnumbered display. This accounts for 22 target bracket
displays versus 21 in the source and was visually checked on physical page 172
(printed page 166).

## Indonesian terminology gate

The directly instructed field-usage check was completed before this unit and
remains applicable. A bounded search of official arXiv records found no
admissible Indonesian same-field item with downloadable TeX. The documented
fallback directly inspected two official ITB mathematical PDFs, page by page.
Their exact identities, hashes, attested forms, rights restrictions, and the
resulting decisions are recorded in
`controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`, 7,965 bytes, SHA-256
`8f112facd6d58c728d9e18d7b34a050064b62a8b0a2c2645d49682d4dbe98cd1`.
Those restricted witnesses remain local and are excluded from public payloads.

Unit 030 adds ten synchronized concept entries, from `generator kuat` through
`Lema Schanuel`, and reuses the pre-existing active form `kategori
co-well-powered`. Other settled forms include `kogenerator injektif`, `argumen
objek kecil`, `objek alpha-kecil relatif terhadap I`, `kardinal kecil regular`,
`rekursi transfinit`, `ordinal penerus`, `ordinal limit`, and `selubung
Karoubi`.
Both terminology surfaces contain 395 valid, unique, matching concept IDs:
control SHA-256
`7c765d8774af9bacbfdc0f4f72b09972cd0d81de5f070bc2cd696ff968b5de5a`;
backend SHA-256
`ea8226ebd96dca7ebcc07a449e099e0e9a96d558724b12abfd0c3e916c20eafc`.

The edition and repository provenance identify the production model exactly
as **OpenAI Codex gpt-5.6-sol, Ultra**, without displacing Wen-Wei Li's
authorship or any human, source, or component credit.

## Backend and cumulative source closure

The modular backend now has 30 sequential units and 1,581 unique segments.
`backend/units.jsonl` is 22,260 bytes, SHA-256
`e26cc16360c1d5d9968e255a11a2c9318e1f4df7f43eda62e74f3428a2b75536`;
`backend/segments.jsonl` is 461,562 bytes, SHA-256
`c1188be50559c39ccfd485b0c62e4e1515a5e908e395ec93c16f4c6095881b46`.
Unit 030 has status `translated_built_qa_passed`, and its backend target hash
equals the admitted target hash.

The cumulative wrapper through Unit 030 is 8,517 bytes, SHA-256
`37dd068fe8f0525fb16edfa245f7c2073bfbd71719a7cfd024fa63550997647f`.
The exact bibliography closure is unchanged from Unit 029: 6,649 bytes,
SHA-256
`a7ec7fa3df2ad91a8d13f8ed552e51e5c79ed64896e07dd68d4bd58b90ad2019`.
Both stable cumulative source files are byte-identical to those versioned
snapshots.

## Reproducible build and PDF inspection

The admitted clean build is
`build/cumulative-unit-030-finalD-20260823`. It used shell-escape-disabled
XeLaTeX, Biber 2.21, MakeIndex for both indexes, and three final XeLaTeX
passes. Biber resolved all 19 citekeys with no warning or error. MakeIndex
accepted 144 term entries and 47 symbol entries, with zero rejection or
warning.

The final TeX log is 78,912 bytes, SHA-256
`a581e395d7e19a646269d98806ed4ccfdf552789e76e672fbca567b03b3d5f3a`;
the Biber log is 1,777 bytes, SHA-256
`3aa8d88750d5951a89803f1e0945ab4e0bf03f523431daf7bad11a7aac5af0ae`.
The final log has no TeX error, undefined control sequence, unresolved
reference or citation, rerun request, overfull box, missing character, fatal
error, or emergency stop. Nineteen non-fatal underfull-box warnings remain.

The checkpoint and promoted cumulative reader are byte-identical: PDF 1.7,
187 pages, 963,655 bytes, SHA-256
`e74feecbbcc1dc2b4538b182215b1c3210ad32f4d90fa933c43cbd27293823bf`.
The PDF is unencrypted and has `id-ID` metadata, 37 resolving outline entries,
815 named destinations, 51 embedded or subset font names, and 648 link
annotations: 636 resolving internal GoTo links and 12 HTTPS links. It has no
form widgets, JavaScript, JavaScript name tree, embedded files, or additional
actions. Its document OpenAction is only a normal page `/Fit` view. The PDF is
untagged and is not claimed to be fully accessible.

Physical pages 167--187 were rendered at 120 dpi. All 21 page images and three
contact sheets were inspected, with individual full-size checks of the
corrected Hom-map page, theorem diagrams, exercise opening, representative
exercise diagrams and hints, the terminal exercise page, bibliography, and
indexes. Blank physical pages 180 and 184 are intentional verso separators.
No clipping, overlap, broken diagram, black square, or unreadable glyph was
visible. Contact-sheet SHA-256 values are
`db10348b59557769798fe7e0762f7f8800cbd4bb3d5949a6b6f5ff4441f115dd`,
`52d7639259990041878c11f8521c55924adfc7bb6a1076e7983724b5f6ca847c`,
and `8028030468c634a6ead368529bce93ea40157fa771419e97c5c80b83a53dbe22`.

## Admission decision

Unit 030 is admitted through the complete end of Chapter 2 at
`chapter2.tex` line 2132. The next production cursor is `chapter3.tex` line 9,
label `sec:cplx`. This remains a partial working and public checkpoint and does
not complete the full-corpus pursuit.
