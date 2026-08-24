# O014 Unit 038 admission and reader QA

Date: 2026-08-24

Result: **PASS — admit after the exact checks recorded below.**

## Authority and exact scope

- Frozen authority: Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
  Algebra*, author-controlled Gitee `master` commit
  `9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
  `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.
- Unit: `o014.aljabr2.chapter3.mapping-cone-and-long-exact-sequences`,
  *Kerucut pemetaan: barisan eksak panjang*.
- Exact authority boundary: `chapter3.tex` lines 1061--1292, including the
  terminal blank separator at line 1292 and stopping before `sec:HH` at line
  1293.
- Frozen normalized-LF slice: `tmp/unit038-source-slice.tex`, 17,739 bytes,
  SHA-256
  `161c303deb0ff9f7d7a6dbd8341a1dae0e11086d794e68d812b6d3db334fe43e`.
- Stable map: `tmp/unit038-segment-map.jsonl`, 63 records, 22,648 bytes,
  SHA-256
  `56322e9fc22c7dc1ef8eb5fac6a9b09913011cf451f05f6cd5922ddd450e1ad8`.
- Target: `source/id-ID/chapter3-unit-038.tex`, 454 LF-terminated UTF-8
  lines, 25,357 bytes, SHA-256
  `85971b03546ce646f434602b3af499be7244fab17fa5944ed5987618a06ee2d1`.

This section contains three propositions, three corollaries, six proofs, one
lemma, 16 TikZ-CD diagrams with 139 arrows, twelve list items, thirteen labels,
43 references, and two citations. It has no exercise, hint, answer, solution,
external asset, or source comment. No mathematical source defect was
demonstrated, so the correction ledger remains at 44 rows through O014-C043.

## Translation, topology, and mathematical review

Independent structural and semantic audits pass all 63 mapped segments. Every
stable segment marker is unique and appears in exact map order. The target
preserves all thirteen labels, 43 reference occurrences over 22 targets as 42
ordinary references plus one established `\sourcecrossref` fallback, both
citation keys (`KS06`, `Li1`), all 16 diagrams and 139 arrows, and all twelve
list items. The target has 52 balanced environment pairs; the two pairs beyond
the source topology are the layout-only `multlined` and `aligned` wrappers
described below. UTF-8, BOM, NUL, CR/LF, terminal-newline, active Han-residue,
and stable-ID checks pass.

The semantic audit reports no omission, duplication, polarity reversal,
quantifier error, degree/index/sign error, mistranslation, or terminology
conflict. `Aksioma rotasi` is the sole new settled term. The title uses a colon
instead of a literal conjunction to fit the class's section heading while
preserving the source relation. Four source-neutral reflows remove line
overflow without changing mathematics:

- the item containing
  `\Hm^{n+1}(X)=\Hm^n(X[1])\to\Hm^{n+1}(Y)` is an unnumbered display;
- the long composition in mapped segment `q009` uses `multlined`;
- the two compared compositions in proof `pf003` use an `aligned` display;
- the map `\xi^n:\Hm^n(X[1])\to\Hm^{n+1}(Y)` is an unnumbered display.

Independent normalized comparison confirms that the maps, factors,
compositions, signs, arrows, labels, citations, and logical claims are exact
after removing only those wrappers and line breaks. The forward Bab 4
reference to `prop:ses-vs-triangle` remains explicit and printable without an
unresolved PDF link.

## Backend and cumulative source closure

`backend/units.jsonl` contains 38 unique unit IDs with unique sequences 1--38,
28,564 bytes, SHA-256
`c6d57531805acfb61275ead07455afd7a27c4d448ecd7c4b440abfa4dee72d51`.
Units 1--37 point to their materialized successor; Unit 038 is marked
`translated_built_qa_passed` and points to the declared next cursor
`o014.aljabr2.chapter3.exercises-hochschild-homology-and-cohomology`, which is
not yet admitted.

`backend/segments.jsonl` contains 1,962 unique segment IDs, 575,630 bytes,
SHA-256
`3f09a22da6f742859bbaba24721f78d1deb88f0bc3a7ad909820dc326148bbc5`.
Its 63 Unit 038 records are byte-for-byte equal to the frozen map; their
sequences are unique and contiguous, and every `nested_in` target resolves.
The backend is structural metadata and contains no duplicated target-LaTeX
field requiring reflow synchronization.

The terminology surfaces contain 428 unique matching concept IDs:

- `controls/TERMINOLOGY_O013_O014.csv`: 69,366 bytes, SHA-256
  `4799050de5c570966da2d7ce778a4f3e78c607d9fcfb9a1773793bf1214dd0b1`;
- `backend/terms.csv`: 28,789 bytes, SHA-256
  `4b87f1e360ad63ed58c973b60ef7720f5b1e07ac37505f329d8a7268fa0c2970`.

The cumulative wrapper has 38 unique, resolving inputs and 310 unique labels
with no duplicate. Its nineteen cited keys are all supplied by the nineteen
bibliography entries and resolve in Biber. Frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-038.tex` is 8,772 bytes,
SHA-256
`f78784261bd3171b73c6bf8beed8454b11b4adcf84990f64693e1ec75aa25ea7`.
The current wrapper is byte-identical. The bibliography is 6,649 bytes,
SHA-256
`a7ec7fa3df2ad91a8d13f8ed552e51e5c79ed64896e07dd68d4bd58b90ad2019`;
the frozen and current copies are byte-identical.

## Reproducible build and PDF inspection

The admitted shell-escape-disabled build is
`build/cumulative-unit-038-finalD-20260824`. It uses XeLaTeX (MiKTeX 26.5),
Biber 2.21, both bounded MakeIndex passes, and converged final XeLaTeX passes.
Biber reports no warning or error. MakeIndex accepts 167 terminology entries
and 71 symbol entries, with zero rejection and zero warning.

The final 79,553-byte log has SHA-256
`d6648d30b969f1c515910e594f9b91ff397c631edfecd10dad1d69489d6e1aff`.
It has zero TeX/package error, undefined control, unresolved reference or
citation, rerun request, overfull horizontal or vertical box, missing
character, missing included file, fatal error, or emergency stop. Sixteen
non-fatal underfull horizontal boxes and seven underfull vertical boxes remain.
The informational absence of optional `biblatex-dm.cfg`, inherited LaTeX
release notices, the known biblatex footnote-patching warning, and generic
imakeidx advisories are not failed resources; both indexes are present in the
final PDF.

Resolved build artifacts include:

- BBL: 26,186 bytes, SHA-256
  `3e3e7ac0feb83d090c693fff1dd531021c7f576c1519646c67ef33203c048742`;
- term index: 7,159 bytes, SHA-256
  `31a02123f93d8c9789f2d6d20836cac06b2a353f466bad3b79bb8e80fafb42bf`;
- symbol index: 2,440 bytes, SHA-256
  `191362f17604e60af593407fa8ba7dbe0c55db494a67eb4a95fc88d7a602c546`.

The build PDF, frozen checkpoint, and promoted cumulative reader are
byte-identical: PDF 1.7, 231 pages, 1,162,756 bytes, SHA-256
`71293cdd594e6df12ddf7ea0c1ca74518e1a0ca5da530f91934a562426702a07`.
It is unencrypted and untagged, with one 498.9 x 708.66-point page size, 45
outline items, 1,007 named destinations, and 808 link annotations: 796 valid
internal actions and twelve HTTPS actions. No internal target is unresolved or
malformed. The sole catalog open action is the ordinary first-page `/Fit`
view; there is no JavaScript, form, widget, embedded file, additional action,
structure tree, or `MarkInfo`.

`pdffonts` reports 52 embedded/subset font rows. Forty-one have ToUnicode maps;
eleven legacy mathematical fonts do not. Pypdf extracts 422,419 characters
without replacement characters, but mathematical font extraction still
contains NUL placeholders. The Unit 038 stable destination resolves and its
eight physical pages yield 11,048 extracted characters. This is therefore a
searchable, navigable, visually verified PDF reader, not a tagged or fully
semantic accessibility artifact. The accessible offline HTML reader remains a
later full-corpus obligation.

The cover, attribution, contents, physical pages 217--224 containing all of
Section 3.7, and physical pages 225--231 containing bibliography and indexes
were freshly rendered at 120 dpi and inspected both as contact sheets and at
full size. Text blocks fill the page normally with the intended small
book-layout offset. All diagrams, equation numbers, theorem heads, footnotes,
links, bibliography entries, and indexes are centered, legible, and free of
clipping, collision, truncation, detached punctuation, or missing visible
glyph. Physical page 224 has intentional lower whitespace because the section
ends there. Contact sheets:

- `tmp/pdfs/unit038-finalD/contact-front-1-5.png`: 362,671 bytes, SHA-256
  `ac1690702b445e0a5efd5006ccbdb3a12fbed6adde7cf72ac18e059a94827d27`;
- `tmp/pdfs/unit038-finalD/contact-unit-217-224.png`: 1,601,980 bytes,
  SHA-256
  `abe2f0d68169956cef56161ee7181a78b823ed683a0582080cf498049323d662`;
- `tmp/pdfs/unit038-finalD/contact-tail-225-231.png`: 1,165,499 bytes,
  SHA-256
  `350b988908b90a9ce2dcb61d8656567902baedf709ffbd85aa81d9e5aaf888a0`.

The metadata and attribution page truthfully identify coverage through
`chapter3.tex` line 1291 / Section 3.7, preserve Wen-Wei Li's authorship and CC
BY 4.0 source relationship, state non-endorsement, and disclose the production
model exactly as `OpenAI Codex gpt-5.6-sol, Ultra`.

## Admission decision

Admit Unit 038 and the cumulative reader through Section 3.7. The next exact
source boundary is Unit 039,
`o014.aljabr2.chapter3.exercises-hochschild-homology-and-cohomology`, the
complete `sec:HH`, `chapter3.tex` lines 1293--1586, with substantive content
through line 1585 and a terminal blank separator at line 1586. Stop before
`sec:truncation-functors` at line 1587. Unit 038 adds no source exercise, hint,
answer, or solution, so cumulative source counts remain 37 exercises, 23
active hints, one intentionally commented hint, and zero source answers or
solutions. This is a partial checkpoint and does not complete the corpus
pursuit.
