# Unit 042 QA - Resolusi

Date: 2026-08-25  
Course / role: O014 / D80  
Unit ID: `o014.aljabr2.chapter3.resolutions`  
Status: admitted cumulative checkpoint; the complete-corpus pursuit remains active

## Authority, boundary, and source identity

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 042 is
the complete Section 3.11, `chapter3.tex` lines 1882--2214 inclusive, with
substantive content through line 2213 and the terminal blank separator at line
2214. It stops before `sec:derived-primer` at line 2215.

The normalized-LF source witness `tmp/unit042-source-slice.tex` is 27,644
bytes / 333 LF lines, SHA-256
`75da0a5963f8e3bf2cec5fbe6a4007fea1c1b27faca6bd54528ac8957547ebfa`.
It is byte-identical to the normalized authority slice. The 102-record map
`tmp/unit042-segment-map.jsonl` is 29,370 bytes, SHA-256
`2581b89bc0485cc25e8c6dbbdf72402d16bd6a58b2ba0c24b6d4d2772c88eb7e`.
Its 31 top-level and 71 nested records cover all 292 nonblank authority lines
once and in order; sequence numbers, IDs, ranges, parent containment, fifteen
labels, and all source cross-reference targets validate.

## Translation, structure, and independent review

The final Indonesian target `source/id-ID/chapter3-unit-042.tex` is 39,646
bytes / 463 LF lines, SHA-256
`8d82d95029a29901862007a63ae2311fd215c576811e6b646770798d2968736e`.
Independent structural, terminology/mathematical, and full 333-line semantic
reviews pass. All 102 stable markers occur once and match the map exactly.
The target preserves fifteen labels, seven `\eqref` commands, five index
writes, 21 list items, 90 TikZ-CD arrows, and zero citations or assets. It has
59 balanced environment pairs: the authority's 58 pairs plus one
presentation-only nested `gathered` used to reflow a wide correspondence.

The authority has 33 `\ref` commands; 31 remain live and resolve in the
partial reader. Two forward references whose targets occur in untranslated
Chapters 4 and 5 are preserved as explicit source-number references, with
machine-readable comments: Theorem 4.4.1 for
`prop:cplx-triangulated` and Section 5.6 for `sec:double-cplx-ss`. Thus the
partial reader has no false or unresolved link, and the stable source target is
not lost. The target contains no active Han residue, English theorem
environment, omitted nonblank source line, unbalanced environment, exercise,
hint, answer, or solution.

The review checked all formulas, maps, degrees, dual directions,
monomorphism/epimorphism distinctions, null-homotopy formula, Horseshoe
construction, and Cartan--Eilenberg bidegrees. The wide correspondence in
Lemma 3.11.8 was split into a two-line display after deterministic QA detected
an overfull box; the mathematical set and bijection are unchanged.

## Disclosed source corrections

Four localized repairs are independently type-checked and disclosed:

- O014-C056 treats the base step as `Coker[X -> I^0]` and uses the printed
  `Coker[I^{n-1} -> I^n]` formula only for `n >= 1`, avoiding undefined
  `I^{-1}`;
- O014-C057 restores the diagram node `X^n`, the common domain of
  `d_X^n`, `alpha^n`, and `h^n`;
- O014-C058 restores `d_C^n` in the lower-right entry of the left matrix,
  making the composition on `I^n direct-sum C^n` well typed;
- O014-C059 restores the horizontal map `I^{n,m} -> I^{n+1,m}`, as required
  by the following `d_h^2=0` check, rather than repeating the vertical map.

Each correction occurs once in the reader and once in
`controls/SOURCE_CORRECTIONS.csv`, at target ranges 61--65, 217--221,
353--369, and 431--435 respectively. The ledger has 60 unique records, 39,740
bytes, SHA-256
`6d2600353104019c5fe63d54907617498c304abf20bddf2440401e908cfe914c`.
No upstream contact occurs at this boundary.

## Terminology and modular backend

New controlled forms are `kompleks yang terdiri atas objek-objek injektif`,
`kompleks yang terdiri atas objek-objek projektif`, and
`Lema Tapal Kuda` (with *Horseshoe Lemma* visible at first use).
`resolusi injektif`, `resolusi projektif`, and
`resolusi Cartan--Eilenberg` remain established forms. Both terminology
surfaces contain 457 unique, exact-matching concept IDs:

- `controls/TERMINOLOGY_O013_O014.csv`: 76,616 bytes, SHA-256
  `cda83d98b1f9335617b1cce07fb1e4a45620dd79416d78fab2f8a5686f8a5c0a`;
- `backend/terms.csv`: 30,952 bytes, SHA-256
  `c8a7a7675f4fa9892e3a74f1b44da1c9da031d7a1af8bc6569df4cccabc9e0dd`.

The backend contains 42 unique units and 2,222 unique segments. Its final 102
segment rows are line-identical to the frozen Unit 042 map:

- `backend/units.jsonl`: 31,583 bytes, SHA-256
  `867b9c166fb51f1ac7567d330293d1212a196303902ea68efd1df74dfd6493a4`;
- `backend/segments.jsonl`: 656,402 bytes, SHA-256
  `5463fb6377df8279a2e5696b2f91f6223ac60f7150d29862a854b2c0a438011a`.

## Editable closure and reproducible build

The 42-input frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-042.tex` is 8,901 bytes,
SHA-256
`b5efcfedad4313cba18a70a39eb5fd48a9e38717032bdcc47d11ff6095f44ff8`;
its mutable alias is byte-identical. The 21-entry bibliography
`source/id-ID/references-cumulative-through-unit-042.bib` is 7,631 bytes,
SHA-256
`b882ae8225e57e383d85b4a5a8f69a0bddc688f20157365d8513b47f612ee597`;
its mutable alias is byte-identical. Cover, PDF subject, and attribution page
truthfully state Chapter 3 through Section 3.11 and source coverage through
line 2213.

The admitted clean build is
`build/cumulative-unit-042-finalD-20260825`. XeLaTeX (MiKTeX 26.5) ran with
shell escape disabled, followed by Biber 2.21, bounded MakeIndex passes for
both indexes, and three further XeLaTeX passes. Biber resolves all 21 citekeys
with zero warning/error. MakeIndex accepts 187 terminology entries and 93
symbol entries with zero rejection/warning.

The final 85,262-byte log has SHA-256
`f5d455b64b6cbccc58d55366ad8c4c6ddb8de14e33962692cfbc1660c7c8d480`.
It has zero TeX/package error, undefined control/reference/citation, rerun
request, overfull box, missing character, fatal error, or emergency stop.
Eighteen non-fatal underfull horizontal boxes and seven underfull vertical
boxes remain. Resolved artifacts include:

- BBL: 29,093 bytes, SHA-256
  `aedae96a05b2b62b7728ef815f287b2ef9eb4b6459a1901f08e5bad004543103`;
- term index: 8,169 bytes, SHA-256
  `90a59d56c9d73bc0cd180d207ee9ecacd921a1efaf1e3ee522eb12e585c72b59`;
- symbol index: 3,562 bytes, SHA-256
  `32cfe879a5aaa893a4b9da15d5e54cf0255ba9da54369225786f3ea0fb75d02e`.

## PDF structure, accessibility qualification, and visual QA

The build PDF, frozen checkpoint, and promoted cumulative reader are
byte-identical: PDF 1.7, 265 pages, 1,309,971 bytes, SHA-256
`11037fbd52c9bdea1b18a449fbf8395f89ad6716b4c080035565ffc71f2d7491`.
It is unencrypted and untagged. Every page has zero rotation and 498.9 by
708.66-point geometry. Strict parsing finds 49 outline entries, 1,145 named
destinations, 906 resolved internal links, and fourteen URI links. All 920
link annotations parse; none is malformed or unresolved.

There is no form, widget, JavaScript, embedded file, additional action,
structure tree, `MarkInfo`, or metadata stream; the opening action is the
ordinary first-page `/Fit` view. All 52 Poppler font rows are embedded and
subsetted; twelve mathematical fonts lack ToUnicode maps. The PDF is therefore
a searchable, navigable, visually verified reader, not a tagged or fully
semantic accessibility artifact.

Fresh 120-dpi renders cover physical pages 1--5, every Unit 042 page 243--255,
and every backmatter page 256--265. Contact sheets and full-size inspection
confirm that cover/attribution scope, all formulas, thirteen diagrams, four
translator notes, theorem heads, the reflowed correspondence, bibliography,
and both indexes are centered, legible, and free of clipping, collision,
truncation, detached notes, black boxes, or missing visible glyphs. Physical
pages 2, 4, 256, and 260 are intentional blank transitions. The three contact
sheets are:

- `qa/render-unit042-finalD/contact-front.png`: 363,971 bytes, SHA-256
  `ccca84065e37aa733930d78c40d61715a206c69b740c2703633b5c4191d5bb26`;
- `qa/render-unit042-finalD/contact-unit042.png`: 3,181,477 bytes, SHA-256
  `406d0f08752a43fc9141a9efb6aea31e4c2823441daa24c2d8926e53f15546bb`;
- `qa/render-unit042-finalD/contact-tail.png`: 1,395,921 bytes, SHA-256
  `dbbf7621ed07d5b8bdf2a46e72f3a312f40809b6ed4d70347b0fb0a6cd166a67`.

## Admission decision and next cursor

Admit Unit 042 and the cumulative reader through Chapter 3 Section 3.11. The
79-row admission manifest `qa/CUMULATIVE_UNIT_042_FILE_MANIFEST.csv` contains
79 unique paths and re-verifies with zero missing, duplicate, byte-count, or
hash mismatch. The next exact source-order boundary starts at
`chapter3.tex` line 2215, `sec:derived-primer`, *Funktor Turunan Klasik*.
Its exact endpoint must be frozen from the authority before translation.

As throughout this lane, the author's official 650-page Linux/TeX Live/xindy
PDF remains authoritative. This 265-page Windows/MiKTeX/MakeIndex artifact is
a valid partial Indonesian reader and makes no pagination-identity claim.
This checkpoint does not complete the full corpus goal.
