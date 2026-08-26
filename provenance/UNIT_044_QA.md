# Unit 044 QA - Contoh: lim^1

Date: 2026-08-26  
Course / role: O014 / D80  
Unit ID: `o014.aljabr2.chapter3.example-lim1`  
Status: admitted cumulative checkpoint; the complete-corpus pursuit remains active

## Authority, boundary, and source identity

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 044 is
the complete Section 3.13, `chapter3.tex` lines 2553--2713 inclusive, with
substantive content through line 2712 and the terminal blank separator at line
2713. It stops before `sec:Ext-Tor` at line 2714.

The normalized-LF source witness `tmp/unit044-source-slice.tex` is 13,478
bytes / 161 LF lines, SHA-256
`2b8a923963fba1f31a9c5f7bfd98e5381a4a1b194f70cd3b7d002fa05a68298e`.
It has a terminal line ending and is byte-identical to the normalized
authority slice. The 51-record map `tmp/unit044-segment-map.jsonl` is 14,076
bytes, SHA-256
`2c376228ea8f711b06db359ab6890b6cf866ed0af222d0ba8adcd1a039aa943f`.
Its 35 top-level and 16 nested records have consecutive sequences, unique
stable IDs, valid `nested_in` parents, and contained ranges. Their union
covers all 128 nonblank authority lines with no omission, and top-level
ownership covers each one exactly once.

## Translation, structure, and corrections

The final Indonesian target `source/id-ID/chapter3-unit-044.tex` is 19,317
bytes / 397 LF lines, SHA-256
`550f7c1d4f7ad08721132b59932d09e5d3eecf0203551b4e0ffcb84702e3d9fc`.
All 51 stable markers occur once and match the map in exact order. The target
preserves the authority's fourteen labels, 21 ordinary `ref`/`eqref` targets
plus two explicit `sourcecrossref` targets, five index writes, two TikZ-CD
environments with sixteen arrows, one Roo06 citation, and balanced localized
environment pairs. The source unit contains no exercises, hints, answers,
solutions, or external assets; it therefore adds none. The target adds only
one disclosed translator footnote for O014-C063. The cumulative wrapper
preserves all previously admitted reader surfaces.

The target is UTF-8 LF-only, with no Han residue, replacement character,
U+2011 nonbreaking hyphen, placeholder token, or unbalanced environment. The
forward reference to `sec:K-injectives` is intentionally rendered as
`\sourcecrossref{sec:K-injectives}{3.15}` because that section is beyond this
partial reader boundary. The new bibliography snapshot contains 22 entries
and adds the cited Roos (2006) source.

One high-confidence source notation repair is disclosed as O014-C063. The
source prints the inverse-system object `C` as `(C_n,h_n)` without its family
subscript; the target restores `(C_n,h_n)_n` and identifies the repair in a
translator footnote. The correction is recorded once in
`controls/SOURCE_CORRECTIONS.csv` and does not alter the mathematical claim.

Six controlled concepts are added or stabilized in
`controls/TERMINOLOGY_O013_O014.csv`: inverse system, countable product,
countable coproduct, exact countable product, shift morphism, and stable
image. The preferred forms agree with the modular backend terminology
surface.

## Backend and editable closure

The backend contains 44 unique units and 2,378 unique segment records after
admission. Current hashes are:

- `backend/units.jsonl`: 33,049 bytes, SHA-256
  `5343e136e2676b06e57b1d3f6eab96b687d6f5da26ff210f0320e5be600d0d0c`;
- `backend/segments.jsonl`: 702,953 bytes, SHA-256
  `18f597ec96d1f8f9394b998df7f3679c71b5581323692d99de664df71b87749a`;
- `backend/terms.csv`: 32,197 bytes, SHA-256
  `0ddf325c2736c1e5393a5984c7650106e08cec8f982aedaac7736e061e93252c`;
- `controls/TERMINOLOGY_O013_O014.csv`: 80,242 bytes, SHA-256
  `f86979f255a4418dc84691941fb24cfcb0318a043fefb21e89be6a95cd5ee478`;
- `controls/SOURCE_CORRECTIONS.csv`: 42,461 bytes, SHA-256
  `48af2431d8a6a02855856da097f9812f91f06aed531fe4dab34fb95e6a09f9f2`.

The through-Unit-044 wrapper and mutable alias are byte-identical, each 8,968
bytes, SHA-256
`307979c8406b4c9eb9c70ed0d4f5a72a7520914fcbc9c124dec214db55dedbfa`.
Both state Chapter 3 through Section 3.13 and source coverage through line
2712. The through-Unit-044 bibliography and both mutable bibliography aliases
are byte-identical, each 8,115 bytes, SHA-256
`9cab4a4c93359dd8b833bcc3fa57da1493782b6f5d34a5cea00b203d25ee63a8`.

## Reproducible build

The admitted clean build is `build/cumulative-unit-044-finalB-20260826`.
XeLaTeX (MiKTeX 26.5) ran with shell escape disabled, followed by Biber 2.21,
bounded MakeIndex passes for both indexes, and four further XeLaTeX passes.
Biber found all 22 citekeys with no error. MakeIndex accepted 197 term-index
entries and 98 symbol-index entries, with zero rejection or warning.

The final 86,374-byte log has SHA-256
`4f181259ff748dea5317d4bfae5ae8db2d8911aa5d4697a6e0cb4b89141839a0`.
There are no TeX errors, undefined or multiply-defined references, undefined
citations, rerun requests, missing characters, fatal errors, or emergency
stops. Two non-fatal overfull horizontal boxes, one overfull vertical box,
nineteen underfull horizontal boxes, and seven underfull vertical boxes remain
inherited/layout warnings; none clips visible content in the inspected pages.
Resolved artifacts are:

- BBL: 30,421 bytes, SHA-256
  `586c340f7b1bcd7382e3b1cd9808f1ac5d553c7e2c76c8e59db6a851a7d2f35f`;
- term index: 8,804 bytes, SHA-256
  `dc3ac907de3a8e23fe68babb4b2ef00f97a228f6860e64e61f9c761efa2e2e4e`;
- symbol index: 3,706 bytes, SHA-256
  `5a14897342c1134aee7bfec841565353537394c0f3627feaf76c45f21728e9c8`.

## PDF structure and visual QA

The build PDF is PDF 1.7, unencrypted, 282 pages, 1,389,564 bytes, SHA-256
`e225bfc588268d4da9bb64978ef4f00ef316e52516c8b4427ca0d838d79d6b05`, with
498.9 by 708.66-point pages and `/Lang` `id-ID`. Strict parsing finds 51
outline entries and 1,224 named destinations. It has 982 annotations: 966
internal GoTo actions and 16 URI actions; all 966 internal destinations resolve
and all 982 rectangles lie within their pages. There is no form, widget,
JavaScript, embedded file, additional action, structure tree, or MarkInfo.
All 52 Poppler font rows are embedded and subsetted; 40 have ToUnicode maps
and twelve inherited mathematical fonts do not. This is a searchable,
navigable, visually verified reader, not a tagged or fully semantic PDF
accessibility artifact.

Fresh 100-dpi renders cover physical pages 258--282, including the transition
from Unit 043, every Unit 044 page (269--272), bibliography, both indexes, and
the intentional blank transition page. A 25-page contact sheet and full-size
inspection confirm centered/legible text, formulas, diagrams, theorem heads,
the O014-C063 note, bibliography, and index entries with no clipping,
collision, truncation, detached note, black box, or missing visible glyph.
The inspected contact sheet is
`qa/render/unit-044-finalB/contact.png`, 1,797,388 bytes, SHA-256
`3ffb867b9e09ea3ad456a4cf06f40ad4f8384b6916b083a3a128bf859db01e00`.

## Admission decision and next cursor

Admit Unit 044 and the cumulative reader through Chapter 3 Section 3.13.
The corresponding `qa/CUMULATIVE_UNIT_044_FILE_MANIFEST.csv` contains 95
unique paths and re-verifies every listed path with zero missing, duplicate,
byte-count, or hash mismatch. The next exact source-order boundary is Unit
045, beginning at
`chapter3.tex` line 2714 (`sec:Ext-Tor`);
the cursor must freeze that slice before translation and must not cross it.

As throughout this lane, the author's official 650-page Linux/TeX Live/xindy
PDF remains authoritative. This 282-page Windows/MiKTeX/MakeIndex artifact is
a valid partial Indonesian reader and makes no pagination-identity claim.
Wen-Wei Li and the upstream project do not endorse this independent
translation. This checkpoint does not complete the full corpus goal.
