# O014 Unit 037 admission and reader QA

Date: 2026-08-24

Result: **PASS — admit after the exact checks recorded below.**

## Authority and exact scope

- Frozen authority: Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
  Algebra*, Gitee `master` commit
  `9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
  `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.
- Unit: `o014.aljabr2.chapter3.abelian-category-complexes`, *Kompleks pada
  kategori abelian*.
- Exact authority boundary: `chapter3.tex` lines 946--1060, including the
  two blank terminal separators at lines 1059--1060 and stopping before
  `sec:cone-vs-long-exact-sequence` at line 1061.
- Frozen normalized-LF slice: `tmp/unit037-source-slice.tex`, 8,933 bytes,
  SHA-256
  `6adf88af700b26dac31c81724d991fbefcedab64f6ccd08849e532a75e04410e`.
- Stable map: `tmp/unit037-segment-map.jsonl`, 30 records, 9,537 bytes,
  SHA-256
  `e08be8d6d9372550bcfa2680c6f3d1b02fbaa4f9886d35ff7b293fc82aaa30c2`.
- Target: `source/id-ID/chapter3-unit-037.tex`, 262 LF-terminated lines,
  13,925 bytes, SHA-256
  `e6078b3d29464c49f90f9586aa44448da806efc41017b610bf2e2f3715583065`.

The source closure contains four propositions, five proofs, one remark, one
definition, one corollary, eight display constructs including six TikZ-CD
diagrams, three index commands, and one two-item list. It has no citation,
exercise, hint, answer, solution, external asset, or source comment. Four
target footnotes disclose source corrections; they are not represented as
upstream content.

## Translation, topology, and mathematical review

Two independent read-only audits cover all 30 mapped segments. Every stable
segment marker is unique and appears in map order. All 11 nesting links
resolve. The eight labels and 18 reference tokens over 14 unique targets have
the exact source multiset and order. Twenty-three environment pairs are
balanced with zero nesting error and zero brace delta. The localized theorem
types correspond exactly to the source's four propositions, five proofs, one
remark, one definition, and one corollary. Four bracket displays, two
`equation` environments, one `equation*`, one `gather*`, all six TikZ-CD
diagrams, all 62 diagram arrows, three indexes, and both list items are
preserved. Formula comparison passes after excluding translator-note formulas
and applying only the four disclosed repairs. The source's isolated inline
`$0$` at line 1050 is rendered naturally as Indonesian *nol* without semantic
loss. UTF-8, BOM, NUL, CJK-residue, CR/LF, and final-newline checks pass.

Full semantic comparison finds no omission, polarity reversal, quantifier or
degree error, mistranslation, or terminology conflict. Settled forms include
`kategori abelian`, `funktor`, `morfisme`, `citra`, `barisan eksak panjang`,
`kuasi-isomorfisme`, and `morfisme homotopik nol`.

Four mathematical source repairs are justified, implemented, disclosed once,
and registered in `controls/SOURCE_CORRECTIONS.csv`:

- O014-C040 changes the left sides of the degreewise kernel, cokernel, image,
  and coimage formulas from mistyped components to the complexes themselves.
- O014-C041 restores the omitted `d_Z^n` needed for the morphism of
  three-term diagrams that induces `d_H^n`.
- O014-C042 names `C(A)`, rather than the already-assumed-abelian `A`, as the
  category proved abelian.
- O014-C043 uses cokernels of `d^(n-1)` to match the displayed vertical maps
  from degree `n-1` to degree `n`, followed by the explicit reindexing used in
  the auxiliary diagram.

The correction ledger now has 44 unique rows through O014-C043, 28,407 bytes,
SHA-256
`505dbaf4a3a719facf0ff0986a1fe1e284414aefd0c6b0769c841ad081f94db9`.

## Backend and cumulative source closure

`backend/units.jsonl` contains 37 unique unit IDs with unique sequences 1--37.
A discovered stale adjacency defect from sequences 26--36 was repaired: every
unit through sequence 36 now points to the actual following unit, sequence 37
is the only current terminal record, and it is marked
`translated_built_qa_passed`. The resulting file is 27,700 bytes, SHA-256
`904f3923b84594d80ea904a21476b5dd0ab18384814966661866c8f969ecdce8`.

`backend/segments.jsonl` contains 1,899 unique segment IDs; its 30 Unit 037
records are byte-for-byte equal to the frozen map and have sequences 1--30.
All nested targets resolve. The file is 552,982 bytes, SHA-256
`4f4997e219bd1813fb6bf36331497ad4eab6dee63e8e3582d0e857f437013606`.
The terminology control and backend remain exact 427-concept matches with no
missing, extra, duplicate, blank, or preferred-form mismatch:

- `controls/TERMINOLOGY_O013_O014.csv`: 69,146 bytes, SHA-256
  `c148e22d102db93b359ef7d4d7341dc5953cf0747fc34af4e587e3c60ca7e4f4`.
- `backend/terms.csv`: 28,724 bytes, SHA-256
  `fd71fe300455b1a24b2a2a059fb1ad39c0771245cd8c97af9284e16faabe3bd4`.

The cumulative wrapper has 37 unique inputs and zero missing input. Its single
bibliography resource is present; 19 unique cited keys equal the 19 included
bibliography entries. Across the cumulative source, 297 unique labels have no
duplicate. Frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-037.tex` is 8,746 bytes,
SHA-256
`76229abbc9650f0d453a95b120b55e45406abdce8a4847ae02aa6ee20a311584`.
Its bibliography is 6,649 bytes, SHA-256
`a7ec7fa3df2ad91a8d13f8ed552e51e5c79ed64896e07dd68d4bd58b90ad2019`.
The current wrapper and bibliography are byte-identical to these frozen files.

## Reproducible build and PDF inspection

The admitted shell-escape-disabled build is
`build/cumulative-unit-037-finalA-20260824`. It uses XeLaTeX (MiKTeX 26.5),
Biber 2.21, both MakeIndex passes, and four XeLaTeX passes. Biber resolves all
19 citekeys with no warning or error. MakeIndex accepts 167 term entries and
71 symbol entries with zero rejection or warning.

The final 79,650-byte log has SHA-256
`bcff49d344c09a3b34a68ac64b676fe6981bf1fa3526aa4cb46404f329065d84`
and zero TeX/package error, undefined control, unresolved reference or
citation, rerun request, overfull box, missing character or file, fatal error,
or emergency stop. It contains 16 non-fatal underfull horizontal boxes, seven
underfull vertical boxes, four inherited LaTeX release-availability notices,
one known biblatex footnote-patching warning, and two generic imakeidx
advisories despite the completed final index-bearing passes.

The build, checkpoint, and promoted cumulative reader are byte-identical: PDF
1.7, 223 pages, 1,127,663 bytes, SHA-256
`27e07599542a5994f99c6a43c4a8cebdfec4c2f2d3415e186fa79dea108facb0`.
It is `id-ID`, unencrypted, and untagged. It has 44 outline entries, 974 named
destinations, 761 link annotations comprising 749 resolved internal GoTo
actions and 12 URI actions, and no form, JavaScript, embedded file, catalog
additional action, structure tree, or MarkInfo. All 52 fonts are embedded and
subsetted; 11 mathematical fonts lack ToUnicode maps. Consequently the PDF is
not claimed as a fully accessible semantic reader.

Physical pages 1--8 and 209--223 were rendered at 120 dpi. Contact sheets and
full-size pages 213--216 were inspected locally and independently. The title,
attribution, contents, Section 3.6, footnotes, all six diagram groups,
bibliography, and indexes are centered, legible, unclipped, and free of
collision or truncation. Physical pages 2, 4, and 220 are intentional verso
pages. The earlier narrow/non-centered-reader defect does not recur: the text
block fills the page normally with the expected small book-layout offset.
Contact-sheet hashes:

- `contact-1-8.png`: 1,342,904 bytes, SHA-256
  `5a4625b758392e0ff44aa92f502a5187a62509f6de0d3f8bfb4c246c2ea84c0f`.
- `contact-209-216.png`: 2,514,149 bytes, SHA-256
  `2b0b99f4c65d46c06e9b651b3f75bf2b5d54b81cd7dae8133a57bce7494eb768`.
- `contact-217-223.png`: 1,502,205 bytes, SHA-256
  `7e11b31151d630a0bc503d739958e059d11a0feb2ae6451c035bf75585816f00`.

Static evidence `tmp/unit037-qa.txt` is 3,809 bytes, SHA-256
`cfbbdfc1f9aef78cfeebf07f52c99ca5fa7d32bc2158b7e31257dba57af9b8ec`.

## Admission decision

Admit Unit 037 and the cumulative reader through Section 3.6. The next exact
source cursor is Unit 038, the complete section
`sec:cone-vs-long-exact-sequence`, `chapter3.tex` lines 1061--1292, stopping
before `sec:HH` at line 1293. Unit 037 adds no source exercise, hint, answer,
solution, citation, or external asset, so cumulative reader counts remain 37
exercises, 23 active hints, one intentionally commented hint, and zero source
answers or solutions. This remains a partial checkpoint and does not complete
the corpus pursuit.
