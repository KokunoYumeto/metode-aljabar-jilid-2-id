# O014 Unit 039 admission and reader QA

Date: 2026-08-25

Result: **PASS - admit after the exact checks recorded below.**

## Authority and exact scope

- Frozen authority: Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
  Algebra*, author-controlled Gitee `master` commit
  `9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
  `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.
- Unit: `o014.aljabr2.chapter3.exercises-hochschild-homology-and-cohomology`,
  *Latihan: Homologi dan Kohomologi Hochschild*.
- Exact authority boundary: `chapter3.tex` lines 1293--1586, including the
  terminal blank separator at line 1586 and stopping before
  `sec:truncation-functors` at line 1587.
- Frozen normalized-LF slice: `tmp/unit039-source-slice.tex`, 22,932 bytes,
  SHA-256
  `d94462e5d3d2868d7f6de812d6b888c927eb5c8611d52dcfb3a6b9104550325c`.
- Stable map: `tmp/unit039-segment-map.jsonl`, 82 records, 28,522 bytes,
  SHA-256
  `e7fe543ff2f5165924a3dd4fe99e6d6bb00417e9f76e3dbca4ef2b1195c9ad08`.
- Target: `source/id-ID/chapter3-unit-039.tex`, 711 LF-terminated UTF-8
  lines, 35,023 bytes, SHA-256
  `641c391d6a11b0d5276070b14253278a194ab820e2850d3be8223a6bf953d254`.

The source heading calls this section exercises, but it is an expository
reader section rather than an `Exercises` environment. It contains definitions,
examples, lemmas, theorems, proofs, diagrams, and three embedded reader tasks,
but no top-level source exercise, hint, answer, or solution environment.

## Translation, topology, and mathematical review

Two independent audits, followed by a post-layout differential audit, pass all
82 mapped segments in exact order. Stable IDs are unique. The combined
197-event structural sequence matches the source after normalizing only the
localized Indonesian environment names. The target preserves all twelve
labels, thirteen cross-reference occurrences, three citation keys (`Li1`,
`Lo98`, `Wi19`), 46 balanced environment pairs, ten TikZ-CD diagrams with 48
arrows, one TikZ figure, six list items, 24 index commands including eleven
`sym1` entries, and balanced braces. It has zero active Han residue, Unicode
smart quotes, NUL bytes, or malformed segment markers.

Seven source-neutral TeX-native quote pairs replace Unicode smart quotes so
XeTeX does not insert CJK glue around Indonesian prose. The quoted expressions
are `bar`, `jejak`, `derivasi universal`, `geser dua kolom ke kiri`,
`kohomologi derajat n`, `homologi`, and `geser dua kolom ke kanan`; only the
delimiters changed. Formula, map, degree, sign, coefficient, and diagram
signatures otherwise match the frozen source/map audit exactly.

Six demonstrated source defects are corrected and disclosed both inline and
in `controls/SOURCE_CORRECTIONS.csv`:

- O014-C044 removes a surplus terminal `|1_R` from an image that lies in
  `M tensor R^{tensor n}`;
- O014-C045 uses `b_{n+1}^*` for the cochain differential from degree `n` to
  degree `n+1`;
- O014-C046 declares the previously unbound two-argument Hochschild notation
  `HH_n(R,M)` and `HH^n(R,M)`;
- O014-C047 restores the established argument order `C_*(R,M)` and
  `C^*(R,M)`;
- O014-C048 says degree-`n` homology, rather than cohomology, for the three
  chain total complexes;
- O014-C049 identifies the dual Hochschild column and the cohomological SBI
  term with coefficient bimodule `R^vee`, without assuming an unjustified
  `R^vee` isomorphic to `R`.

The correction ledger now has 50 data rows through O014-C049, 33,247 bytes,
SHA-256
`57a8c18dc49a2b907c4220ef0c71cf5772bc1c77cd842c08722b83b6728e7d35`.
No upstream message was sent.

## Terminology and modular backend

Twenty first-use concepts were reconciled across both terminology surfaces,
including `pangkat tensor`, `kompleks bar`, `kompleks bar teraugmentasi`,
`homomorfisme augmentasi`, `komonad`, `kompleks Hochschild`, `Tor relatif`,
`Ext relatif`, `kopusat`, `diferensial Kahler`, `derivasi universal`,
`bikompleks siklik`, cyclic and periodic cyclic (co)homology, the Connes
periodicity operator, `dual linear`, and provisional `pemenggalan kasar`.
`controls/TERMINOLOGY_O013_O014.csv` and `backend/terms.csv` each contain 448
unique matching concept IDs. Their exact identities are respectively 74,019
bytes / SHA-256
`eccb70db88f3c7bcfe9a3c2e1c79176fb427e2722bc46222adedd355bdb0b6e2`
and 30,155 bytes / SHA-256
`4d666924f60ec395f741e4f0b0c2c6e5599586eb36acf1df370b09d311863689`.

`backend/units.jsonl` contains 39 unique unit IDs and sequences 1--39, 29,357
bytes, SHA-256
`96d4bce4db97ba7cb737300eecdbb75ded1c4de974e54d1f501e2d046c57ccce`.
Unit 039 points to the declared next cursor
`o014.aljabr2.chapter3.truncation-functors`.

`backend/segments.jsonl` contains 2,044 unique segment IDs, 604,152 bytes,
SHA-256
`688d32abdc574c69c82c83f9b03ef9e2679ab7e70fc22f01df4d0083b5d8a0fa`.
Its final 82 rows are line-for-line equal to the frozen Unit 039 map; all
sequences are contiguous and every `nested_in` target resolves.

## Cumulative editable closure and build

The frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-039.tex` has 39 resolving
inputs, 8,799 bytes, SHA-256
`5dc42a8a699bfd2fc0fd25a3bbe6174a2aa7d0fa9210ffc39d41679c4a6c8937`.
Its mutable alias is byte-identical. The 21-entry bibliography
`source/id-ID/references-cumulative-through-unit-039.bib` is 7,631 bytes,
SHA-256
`b882ae8225e57e383d85b4a5a8f69a0bddc688f20157365d8513b47f612ee597`;
its mutable alias is also byte-identical. The title page, PDF subject, and
attribution page all truthfully state coverage through Chapter 3 Section 3.8
and `chapter3.tex` line 1585.

The admitted clean build is
`build/cumulative-unit-039-finalC-20260825`. It uses XeLaTeX (MiKTeX 26.5)
with shell escape disabled, Biber 2.21, bounded MakeIndex passes for both
indexes, and three further XeLaTeX passes. Biber resolves 21 citekeys with
zero warning/error. MakeIndex accepts 180 terminology entries and 82 symbol
entries with zero rejection/warning.

The final 84,606-byte log has SHA-256
`33fb1a38c0fa46dee4ca3fd3012c71b89b1f844ece7a2f66bd418250ed61e1bf`.
It contains zero TeX/package error, undefined control, unresolved reference or
citation, rerun request, overfull box, missing character, fatal error, or
emergency stop. Seventeen underfull horizontal boxes and seven underfull
vertical boxes remain non-fatal. The informational absence of optional
`biblatex-dm.cfg`, inherited LaTeX release notices, the known biblatex
footnote-detection warning, and generic imakeidx advisories are not failed
reader resources; both indexes are present.

Resolved artifacts include:

- BBL: 29,093 bytes, SHA-256
  `aedae96a05b2b62b7728ef815f287b2ef9eb4b6459a1901f08e5bad004543103`;
- term index: 7,799 bytes, SHA-256
  `5a285a0e77e571a5b48a11b1ea71cdc920f32476f2dde200a331f7b589a8e73b`;
- symbol index: 2,847 bytes, SHA-256
  `039e0f874c2e574719296d2512fa4abce481951069c167cd3cb29bf606ff4d63`.

## PDF structure, accessibility qualification, and visual QA

The build PDF, frozen checkpoint, and promoted cumulative reader are
byte-identical: PDF 1.7, 243 pages, 1,210,711 bytes, SHA-256
`11cabff2db7b4bdb1abaaf29be78a37fd5e16b4dd08b30f6debf88742f026f6a`.
The file is unencrypted and every page has zero rotation and the same 498.9 x
708.66-point media/crop/bleed/trim/art geometry. Strict parsing finds 46 valid
outline entries, 1,049 valid named destinations, 817 internal links whose
targets all resolve, fourteen HTTPS links, and no malformed annotation.

There is no AcroForm, widget, JavaScript, embedded file, file attachment,
additional action, structure tree, or `MarkInfo`; the opening action is an
ordinary first-page `/Fit` view and `/Lang` is `id-ID`. All 52 font rows are
embedded/subset. Forty have ToUnicode maps and twelve mathematical fonts do
not. The PDF is therefore a searchable, navigable, visually verified reader,
not a tagged or fully semantic accessibility artifact. The semantic offline
HTML reader remains a full-corpus obligation.

Fresh 120-dpi renders cover physical pages 1--5, all Unit 039 pages 224--234,
and bibliography/index pages 235--243. Contact sheets and representative
full-size pages were inspected. The corrected Section 3.8 cover, text blocks,
equations, diagrams, theorem heads, footnotes, bibliography, and indexes are
centered, legible, and free of clipping, collision, truncation, detached
punctuation, black boxes, or missing visible glyphs. Physical pages 2, 4, and
238 are intentional recto-pagination blanks; page 234 has intentional lower
whitespace because the section ends there. Contact sheets:

- `tmp/pdfs/unit039-finalC/contact-front-1-5.png`: 173,237 bytes, SHA-256
  `932bc3032ef5879ca7fba52e52f7245fd32f28092d423f40f0d760e7f8c9c9e1`;
- `tmp/pdfs/unit039-finalC/contact-unit-224-234.png`: 1,240,759 bytes,
  SHA-256
  `d8235eb6d4abf9f11c0db5089e7f58596ed2e8b2e5f0d2b2262a625514e9bf09`;
- `tmp/pdfs/unit039-finalC/contact-tail-235-243.png`: 619,635 bytes,
  SHA-256
  `d3b6b5d67bfe15a7589eea2bc6955f76cc7544433831512564c897cc7f660e52`.

## Admission decision and next cursor

Admit Unit 039 and the cumulative reader through Chapter 3 Section 3.8. The
next exact source boundary is Unit 040,
`o014.aljabr2.chapter3.truncation-functors`, *Funktor pemenggalan*, exactly
`chapter3.tex` lines 1587--1709, with substantive content through line 1708
and a terminal blank separator at line 1709. Stop before
`sec:double-cplx-coh` at line 1710.

Unit 039 adds no formal source exercise or hint environment, so cumulative
source counts remain 37 top-level exercises, 23 active hints, one intentionally
commented hint, and zero source answers or solutions. This is a partial
checkpoint and does not complete the corpus pursuit.
