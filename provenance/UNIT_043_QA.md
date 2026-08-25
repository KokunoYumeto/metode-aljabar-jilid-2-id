# Unit 043 QA - Funktor turunan klasik

Date: 2026-08-26  
Course / role: O014 / D80  
Unit ID: `o014.aljabr2.chapter3.classical-derived-functors`  
Status: admitted cumulative checkpoint; the complete-corpus pursuit remains active

## Authority, boundary, and source identity

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 043 is
the complete Section 3.12, `chapter3.tex` lines 2215--2552 inclusive, with
substantive content through line 2551 and the terminal blank separator at line
2552. It stops before `sec:lim1` at line 2553.

The normalized-LF source witness `tmp/unit043-source-slice.tex` is 27,132
bytes / 338 LF lines, SHA-256
`ac95a737c3df39dff8ece789057d2ad3ce93474b258476245b2fcc67d074dbb9`.
It is byte-identical to the normalized authority slice. The 105-record map
`tmp/unit043-segment-map.jsonl` is 32,475 bytes, SHA-256
`2712c57d9a9066fb1a119037857552c0c331abd20d91c86a3c41c56de1a542cd`.
Its 41 top-level and 64 nested records have consecutive sequences, unique
stable IDs, valid parents, and contained ranges. Their union covers all 295
nonblank authority lines with no omission, and top-level ownership covers each
one exactly once. Source line 2286 intentionally belongs to both adjacent
nested diagram records because that single physical line closes the
right-derived diagram and opens the left-derived diagram; no other nonblank
line is shared between sibling records.

## Translation, structure, and independent review

The final Indonesian target `source/id-ID/chapter3-unit-043.tex` is 40,571
bytes / 458 LF lines, SHA-256
`80d7ba5a71f45c418ac8278ac03ee6409d23bc7bc48dcf52310096d0ae153d54`.
Independent block reviews checked mathematical fidelity, natural Indonesian,
terminology, formulas, and diagrams; a final deterministic check then
revalidated the complete target. All 105 stable markers occur once and match
the map in exact order.

The target preserves the authority's seventeen labels, 23 `ref`/`eqref`
targets, ten index writes, nineteen list items, 151 TikZ-CD arrows, seventeen
TikZ-CD environments, and 57 balanced environment pairs. The cumulative build
resolves every reference. The source unit has no citations, exercises, hints,
answers, solutions, or external assets, and the target introduces none.

Active text contains no Han residue, English theorem environment, replacement
character, U+2011 nonbreaking hyphen, placeholder token, or unbalanced
environment. Three added footnotes disclose the three source repairs below.
The reviews specifically checked the long exact sequences, naturality
squares, cohomological and homological delta-functor conventions, acyclic
resolution formulas, dimension shifting, universal-property recursion, and
every connecting-morphism degree.

## Disclosed source corrections

Three localized repairs are independently type-checked and disclosed:

- O014-C060 changes the left objects in the morphism-of-delta-functors square
  from `G^{n-1}(X)` and `F^{n-1}(X)` to `G^{n-1}(Z)` and
  `F^{n-1}(Z)`. The connecting maps printed in the same definition have
  domain at `Z`, so the repaired square is the well-typed one.
- O014-C061 changes the two connecting-arrow labels in the terminal comparison
  square from superscript `n` to `n-1`. Their degree-`n-1` domains and
  degree-`n` codomains require precisely those labels.
- O014-C062 restricts the zero-extension convention `A^{-n}=0` or
  `A_{-n}=0` to `n >= 1`. Applying the unqualified source statement at
  `n=0` would force the arbitrary degree-zero resolution term to be zero.

Each correction identifier occurs exactly once in the target and once in
`controls/SOURCE_CORRECTIONS.csv`. The notes appear at target lines 184,
325, and 441 and render on physical pages 259, 262, and 266. The ledger has 63
unique records, 41,728 bytes, SHA-256
`c89b908142e17e8e014459c2d379bce90e48415f1cd248acb245dbcae20e70de`.
No upstream contact occurs at this boundary.

## Terminology and modular backend

Ten controlled concepts are added at first use: classical, right, left, and
higher derived functor; cohomological and homological delta-functor;
`F`-acyclic object; dimension shifting; and the universal cohomological and
homological delta-functors. `funktor yang dapat dihapus` and `funktor yang
dapat dihapus secara dual` are promoted to active forms after their formal
definitions. `funktor hiperturunan` remains provisional because recurrence
inside the source is not external Indonesian field attestation. The index sort
key for all delta-functor entries is unified.

Both terminology surfaces contain 467 unique concept IDs with exact preferred
form agreement:

- `controls/TERMINOLOGY_O013_O014.csv`: 79,025 bytes, SHA-256
  `4630565f6da21b39bdd490c60e19e954b18ba7cedaa09cf8a2aa4e12feac1f13`;
- `backend/terms.csv`: 31,788 bytes, SHA-256
  `1b3edf201ecb8ad8e25fe65a04a733995df11dd0232b1edfcaca1cf180ea1f37`.

The backend contains 43 unique units and 2,327 unique segments. Its final 105
segment rows are line-identical to the frozen Unit 043 map:

- `backend/units.jsonl`: 32,330 bytes, SHA-256
  `7cdd8ca9aba94faf9bddfc30d23d1c42e9774dc02b25e796b5cfc3af1b140425`;
- `backend/segments.jsonl`: 688,877 bytes, SHA-256
  `a89f850daa4dc3e39051d7f47b95d9297203271575fb5bb34f117a831a17bef6`.

The Unit 043 backend record points to the exact witness and target hashes and
names `o014.aljabr2.chapter3.example-lim1` as the next stable unit.

## Editable closure and reproducible build

The 43-input frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-043.tex` is 8,942 bytes,
SHA-256
`ba0f8dcfc44e74567ca9a35963a821071f7070f0d69b5dcc8fe5fa6c460df7a3`;
its mutable alias is byte-identical. The 21-entry bibliography
`source/id-ID/references-cumulative-through-unit-043.bib` is 7,631 bytes,
SHA-256
`b882ae8225e57e383d85b4a5a8f69a0bddc688f20157365d8513b47f612ee597`;
its mutable alias is byte-identical. Cover, PDF subject, and attribution page
truthfully state Chapter 3 through Section 3.12 and source coverage through
line 2551.

The admitted clean build is
`build/cumulative-unit-043-finalD-20260825`. XeLaTeX (MiKTeX 26.5) ran with
shell escape disabled, followed by Biber 2.21, bounded MakeIndex passes for
both indexes, and three further XeLaTeX passes. Biber resolves all 21 citekeys
with zero warning or error. MakeIndex accepts 195 terminology entries and 95
symbol entries with zero rejection or warning.

The final 80,536-byte log has SHA-256
`e96f51b93b205e06f432e19ada8f0bb9e16569944caa2d46008e4fcfdd4b8e58`.
It has zero TeX/package error, undefined control/reference/citation, rerun
request, overfull box, missing character, fatal error, or emergency stop.
Eighteen non-fatal underfull horizontal boxes and seven underfull vertical
boxes remain. Resolved artifacts include:

- BBL: 29,093 bytes, SHA-256
  `aedae96a05b2b62b7728ef815f287b2ef9eb4b6459a1901f08e5bad004543103`;
- term index: 8,628 bytes, SHA-256
  `db0b751b72510338ac6147931611079309f16f18fe9bed2865ffabb5a7563654`;
- symbol index: 3,622 bytes, SHA-256
  `153d99f626e68123973100db559106356837930a77a0414acd4aaf40959a7743`.

## PDF structure, accessibility qualification, and visual QA

The build PDF, frozen checkpoint, and promoted cumulative reader are
byte-identical: PDF 1.7, 275 pages, 1,361,656 bytes, SHA-256
`15a22aa8f55fefd7ba0d10840e3719bd3718d6af6ceda63eedf919db24250ac1`.
It is unencrypted and untagged. Every page has zero rotation and 498.9 by
708.66-point geometry. Strict parsing finds 50 outline entries, 1,189 named
destinations, 937 resolved internal links, and fourteen URI links. All 951
link rectangles lie within their pages; none is malformed or unresolved.

There is no form, widget, JavaScript, embedded file, additional action,
structure tree, `MarkInfo`, or metadata stream; the opening action is the
ordinary first-page `/Fit` view. All 52 Poppler font rows are embedded and
subsetted; twelve mathematical fonts lack ToUnicode maps. The PDF is therefore
a searchable, navigable, visually verified reader, not a tagged or fully
semantic accessibility artifact.

Fresh 120-dpi renders cover physical pages 1--5, every Unit 043 page 255--266,
and every backmatter page 267--275. Contact sheets and full-size inspection
confirm that cover/attribution scope, all formulas, seventeen diagrams, three
translator notes, theorem heads, bibliography, and both indexes are centered,
legible, and free of clipping, collision, truncation, detached notes, black
boxes, or missing visible glyphs. The terminology-index leading was adjusted
to 9.3 points at an unchanged 8-point glyph size to remove the earlier minor
final-page vertical overflow without reducing legibility. Physical pages 2,
4, and 270 are intentional blank transitions. The three contact sheets are:

- `qa/render-unit043-finalD/contact-front.png`: 159,675 bytes, SHA-256
  `c890f8315884c055f84acdfa29bbf28393a85bc272e9ac60057ff0754f4da4e5`;
- `qa/render-unit043-finalD/contact-unit043.png`: 1,333,994 bytes, SHA-256
  `85ad34822d0872ca5856a31ca02c09c52f60bba3f877f524ace24d04d6e921b0`;
- `qa/render-unit043-finalD/contact-tail.png`: 601,498 bytes, SHA-256
  `3708255a80ed15158e19e7797ecbfc8eeb024a846857f37a5befbee71db01126`.

## Admission decision and next cursor

Admit Unit 043 and the cumulative reader through Chapter 3 Section 3.12. The
80-row admission manifest `qa/CUMULATIVE_UNIT_043_FILE_MANIFEST.csv` contains
80 unique paths and re-verifies with zero missing, duplicate, byte-count, or
hash mismatch. The
next exact source-order boundary is Unit 044,
`o014.aljabr2.chapter3.example-lim1`, *Contoh: lim1*, the complete
`chapter3.tex` lines 2553--2713 inclusive, with substantive content through
line 2712 and the terminal blank separator at line 2713. It stops before
`sec:Ext-Tor` at line 2714.

As throughout this lane, the author's official 650-page Linux/TeX Live/xindy
PDF remains authoritative. This 275-page Windows/MiKTeX/MakeIndex artifact is
a valid partial Indonesian reader and makes no pagination-identity claim.
This checkpoint does not complete the full corpus goal.
