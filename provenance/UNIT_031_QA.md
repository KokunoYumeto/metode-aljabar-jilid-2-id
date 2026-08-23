# O014 Unit 031 admission and reader QA

Date: 2026-08-23  
Unit: `o014.aljabr2.chapter3.overview`  
Title: *Kompleks*  
Result: **PASS — translated, independently reviewed, built, rendered, and admitted**

## Authority and exact scope

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled Gitee `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 031 is
exactly the Chapter 3 overview, `chapter3.tex` lines 9--55 inclusive. The
next unadmitted source is line 57,
`\section{加性范畴上的复形}\label{sec:additive-cplx}`.

The normalized-LF authority slice is `tmp/unit031-source-slice.tex`, 8,019
bytes, SHA-256
`6b4b4806e0d9885580547cb103d93e59f0a094ff08d93abdd2781287b71040ec`.
It is byte-equal to the frozen authority range. The 19-record stable-ID map is
`tmp/unit031-segment-map.jsonl`, 5,258 bytes, SHA-256
`0c70f75800fa91ed0d1ebf97642237d576118746dcc60de1ef43521f4e43731f`.

## Translation, topology, and mathematical review

The admitted target is `source/id-ID/chapter3-unit-031.tex`, 13,031 bytes,
SHA-256
`65e3dd7e5c5a0a4512c9c90efd727b32fc7d8c1397d8117f29a492ca080c4e65`.
It translates the complete overview without abridgment. The source contains no
exercises, hints, answers, solutions, figures, external assets, or index
commands in this range.

All 19 stable markers are unique and occur in exact map order. The Unit-031
backend has 19 rows in raw-line exact map parity. Source/target topology passes
for the chapter label, all 39 reference occurrences in identical source order
over the same 30 targets, citation `KS06`, three unnumbered displays, one
TikZ-CD diagram, and the reader-tip enclosure. Three already admitted targets
remain live internal references. Thirty-six forward occurrences use
`sourcecrossref` with human-readable section fallbacks; the underlying labels
are retained and will become live links as their units enter the cumulative
reader.

No Han residue, NUL, replacement character, stray patch marker, duplicate
marker, or malformed environment remains. Mathematical content and variance,
complex/cochain conventions, Hom complexes, mapping cones, bicomplex
totalization, long exact sequences, injective/projective resolutions, derived
and delta functors, balanced bifunctors, inverse-limit derivation, and
K-injective/K-projective resolutions were reviewed against the authority.
Fallback section numbers were checked against the pinned source structure.

An independent naturalness review found one minor expression:
`dari suatu bimodul-(R,R), M`. The admitted target uses the idiomatic and
ledger-consistent `dari M, suatu bimodul (R,R)`. The same review otherwise
passed the complete translation and all topology.

## Transparent source corrections

The official errata contains no item for this overview. Three unlisted
authority defects have deterministic corrections, each recorded in
`controls/SOURCE_CORRECTIONS.csv` and disclosed at point of use:

- **O014-C030:** source line 10 has a malformed transition after a full stop.
  The target restores the intended `Sebaliknya`.
- **O014-C031:** source line 27 prints
  `0 -> X -> I^0 -> I^2 -> ...`, skipping `I^1`. The immediately following
  diagram has `I^0 -> I^1 -> I^2`; the target restores that sequence.
- **O014-C032:** source line 10 defines
  `H^n(X)=Ker(d^n)/Image(d^{n+1})`. Under the book's cochain convention,
  `Image(d^{n+1})` lies in `X^{n+2}` and cannot be a subobject of
  `Ker(d^n)` in `X^n`. The target uses `Image(d^{n-1})`, confirmed by
  the admitted definitions in the Prelude and Chapter 2.

The corrections ledger is 20,300 bytes, SHA-256
`a26625348170c5e2ea8fd0afb89bef2b3bdecfa8257af039455ce17b03b8b4dc`.
All correction IDs are unique and have status `accepted_disclosed`.

## Indonesian terminology and provenance

Unit 031 adds 16 synchronized concepts, including `homotopi kompleks`,
`kompleks Hom`, `kompleks total`, `barisan eksak panjang`, `resolusi`,
`funktor pemenggalan`, `resolusi Cartan--Eilenberg`, `bifunktor`,
`bifunktor seimbang`, `syarat Mittag--Leffler`, `kompleks K-injektif`,
`kompleks K-projektif`, and `silinder pemetaan`.

The independently reviewed forms `funktor hiperturunan`, `funktor yang
dapat dihapus`, and `funktor yang dapat dihapus secara dual` are coherent
but weakly attested. They remain usable and explicitly `provisional` pending
the later definition-level evidence; this is not a hold on production or
publication. Both terminology surfaces contain 411 valid, unique, matching
concept IDs: control 64,017 bytes, SHA-256
`cb6232573c951f8e588fc16255039d580cc793770ac8a693c5c6296ebcb049b9`;
backend 27,586 bytes, SHA-256
`422f6637dcff729f48fb0daae845e4c6641381c21b1b860ae071e2847d862277`.

The existing bounded Indonesian field-usage report remains the external
terminology evidence. Restricted witnesses remain local and outside public
payloads. The edition provenance continues to identify the production model
exactly as **OpenAI Codex gpt-5.6-sol, Ultra**, without displacing Wen-Wei Li's
authorship or any human, source, or component credit.

## Backend and cumulative source closure

The modular backend now has 31 sequential units and 1,600 unique segments.
`backend/units.jsonl` is 22,938 bytes, SHA-256
`c6ea4d27b82e631d945d2524454cdd07a961621fe3eb41d81bcf463f0fe323f0`;
`backend/segments.jsonl` is 466,820 bytes, SHA-256
`74aa4cb3354af3dd42cd99f0f82beaef303e10486eb1938bec5ae2b05070a88e`.
Unit 031 has status `translated_built_qa_passed`, and its backend target hash
equals the admitted target hash.

The cumulative wrapper through Unit 031 is 8,571 bytes, SHA-256
`7367d1ed75cab76e4d73fab776289dc59d0b89c33d35ff3d7a6553825714050b`.
It inputs Units 001--031 in exact source order and retains the exact model,
attribution, modification, license, and non-endorsement notices. The
bibliography snapshot remains 6,649 bytes, SHA-256
`a7ec7fa3df2ad91a8d13f8ed552e51e5c79ed64896e07dd68d4bd58b90ad2019`;
its existing `KS06` record closes the new citation. Stable cumulative source
files are byte-identical to these snapshots.

## Reproducible build and PDF inspection

The admitted clean build is
`build/cumulative-unit-031-finalC-20260823`. It used shell-escape-disabled
XeLaTeX, Biber 2.21, both MakeIndex passes, and three final XeLaTeX passes.
Biber resolved all 19 citekeys with no warning or error. MakeIndex accepted
144 term entries and 47 symbol entries with zero rejection or warning.

The final TeX log is 82,693 bytes, SHA-256
`e817b71f2a03a0fafea1da0388b53f79018077bc36e9e792cdeff8d91136be5e`.
The final log has no TeX error, undefined control sequence, unresolved
reference or citation, rerun request, overfull box, missing character, fatal
error, or emergency stop. Nineteen non-fatal underfull-box warnings remain.

The checkpoint and promoted cumulative reader are byte-identical: PDF 1.7,
191 pages, 979,643 bytes, SHA-256
`0834eaa525fb64f3f2f13665238429fd3e4db9e3679b8c71e781ce2fdf333330`.
The PDF is unencrypted and has `id-ID` metadata, 38 outline entries, 824 named
destinations, 51 embedded or subset font names, 644 internal GoTo links, and 12
HTTPS links. It has no form, JavaScript, embedded files, additional actions,
structure tree, or MarkInfo. It is untagged and is not claimed to be fully
accessible.

Physical pages 179--191 were rendered at 120 dpi. Both contact sheets and
full-size Chapter 3 pages 181--184 were inspected. The chapter opening, three
correction footnotes, long exact sequence, injective-resolution display,
TikZ-CD diagram, forward-reference fallbacks, reader-tip box, bibliography, and
indexes are centered and legible. Blank pages 180 and 188 are intentional
recto/verso separators. No clipping, overlap, broken diagram, black square,
off-page content, or unreadable glyph was visible. Contact-sheet SHA-256 values
are
`4a2b6818f605a0882527c654b9c90f67c179ad1327f9992fcf29b1df4c1ea172`
and
`b1dae49083ab66921ff15d5b46ebc0be42a66a0bb1c058b4ecd48a850187793e`.

## Admission decision

Unit 031 is admitted through `chapter3.tex` line 55. The next production
cursor is line 57, `sec:additive-cplx`. This remains a partial working edition
and does not complete the full-corpus pursuit.

