# Unit 050 admission QA

Date: 2026-08-28
Course/role: O014 / D80
Unit: `o014.aljabr2.chapter4.cohomological-functors`
Result: **PASS**

## Frozen source boundary

Unit 050 is the remaining lemma-through-corollary closure of Section 4.1 in
the frozen Wen-Wei Li authority, `chapter4.tex` lines 210--258 inclusive. It
begins with the lemma that consecutive morphisms in a distinguished triangle
compose to zero, contains the definition and long exact sequence of a
cohomological functor and the representable-Hom proposition, and ends with the
corollary for a triangle `X -> Y -> 0 -> +1`. It stops at blank line 259 before
Section 4.2 at line 260. The authority remains branch `master`, commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.

The normalized-LF witness `tmp/unit050-source-slice.tex` is 3,170 bytes / 49
LF lines, SHA-256
`62fa567b35e1544072e5983e982bc8f87e2c606428496b69f99e165fb7548cdc`.
The ordered map `tmp/unit050-segment-map.jsonl` has fourteen records, is 4,215
bytes, and has SHA-256
`d331af8ffc006ecfd6b64410cbcf28ca93f7c25e6279db572d5d8d7d780ac393`.
Sequences 1--14 and segment IDs are unique and ordered, exactly match the
fourteen target markers, and exactly match the fourteen Unit 050 backend rows.

## Translation and independent review

The admitted Indonesian target `source/id-ID/chapter4-unit-050.tex` is 5,270
bytes / 107 LF lines, SHA-256
`dc196a7e89676da7899160d554a42f2ceefe2592de705fdadb332c41f57067f0`.
Independent source comparison verifies one lemma, three proofs, one
definition, one remark, one proposition, one corollary, five labels, three
references, two index entries, five display blocks, two TikZ-CD diagrams, and
all formulas and arrow labels. The target contains no exercise, hint, answer,
solution, citation, external asset, Han character, replacement character, or
Section 4.2 content.

The translation uses the registered forms `kategori prabertriangulasi`,
`segitiga terbedakan`, `kategori abelian`, `funktor kohomologis`, and `barisan
eksak panjang`. The draft's capitalized `kategori Abelian` was normalized to
the active ledger form, and the source `corollary` uses the reader's defined
`korolari` environment. Naturalness and mathematical fidelity otherwise pass
without qualification.

One high-confidence source defect is corrected and disclosed as O014-C072.
At `chapter4.tex` line 245, the `TS` node carries two coincident dashed arrows
to `TX`, one unlabeled and one labeled `Tk`. A morphism between the displayed
triangles has one fourth vertical component, namely `Tk`; the target removes
only the redundant unlabeled arrow and preserves the labeled component. The
target therefore contains twenty arrows rather than the source's twenty-one
commands. `controls/SOURCE_CORRECTIONS.csv` now contains 73 accepted rows, is
48,773 bytes, and has SHA-256
`843ea89738b027afbb07b283e9b039c8e645bb21bb1884bc1437f5d5916c10a0`.

## Cumulative integration

The frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-050.tex` and mutable alias
are byte-identical at 9,330 bytes, SHA-256
`21a30f962a4b750f7d6347d1966a29b6372ddb7dca801a814edf971a86fa1e3e`.
They contain exactly fifty unique contiguous unit inputs and truthfully state
complete Chapter 3 plus Chapter 4 through line 258. The visible title-page
scope, attribution page, and PDF Subject agree.

No new citation is introduced. The 26-entry bibliography
`source/id-ID/references-cumulative-through-unit-050.bib` and mutable alias are
byte-identical at 9,881 bytes, SHA-256
`45d10bddaacbc2272a62c15c6d58e46f2bd769e4f32455c8a8cfd525fd33f0f6`.
All 26 cumulative citekeys resolve.

The modular backend contains fifty unique units and 2,704 unique segments.
`backend/units.jsonl` is 37,535 bytes, SHA-256
`db5b0cd2939b24f88ba2328682de9e7a3b4dd8a6964b7c2f903343cde2eda596`;
`backend/segments.jsonl` is 797,576 bytes, SHA-256
`73d9d46748512010936a49e0db6818af67c00340b0d839f8435a375f30c548dc`.
Both JSONL files parse, all identifiers are unique, and the Unit 050 row points
to the next source-order unit. No new terminology concept is required: both
terminology surfaces retain 511 unique, exact-matching concept IDs.

## Reproducible build

The admitted clean build is
`build/cumulative-unit-050-finalB-20260828`. FinalA is rejected because it
exposed the draft's undefined `akibat` theorem environment and stopped after a
non-admissible 306-page partial output. FinalB starts from a fresh directory
after normalizing that environment to `korolari`.

FinalB ran XeLaTeX 26.5 with shell escape disabled, Biber 2.21, both bounded
MakeIndex jobs, and four further shell-escape-disabled XeLaTeX passes. Passes
3, 4, and 5 have byte-identical 31,400-byte console transcripts, SHA-256
`711ef4ef42da880b512a0249f4c56cc344d1cdf9f39773b95a4ac232ac709810`.
Biber resolves all 26 citekeys. Its 36,087-byte BBL has SHA-256
`fd45e12d4dd985d632994c9b4ba5377310cd3e178399ffb7ab2ab1c86b9f782e`.
MakeIndex accepts 221 terminology and 104 symbol entries with zero rejection
or warning. The terminology index is 10,036 bytes / SHA-256
`fd4a4666f1de8b2545426b3c77770783c2de39e5198a2dfa7f370bac12f135b5`;
the symbol index is 3,903 bytes / SHA-256
`a98a95cccec64166b5dbc891e18aaf29bc667eb41edc23d3c18b1935d3335204`.

The final 84,579-byte log, SHA-256
`343b3f6923c87d955ba3ed8f33ae06e7e2a8d89ef3aaafc46a75c7a110f3048a`,
has no TeX/package error, undefined control sequence, undefined reference or
citation, missing character, rerun request, emergency stop, or fatal error.
Seven overfull horizontal boxes remain, exactly the inherited Unit 049 set;
Unit 050 adds none. There is no overfull vertical box. Twenty-six underfull
horizontal and ten underfull vertical boxes remain nonfatal and unchanged.
Full-size inspection confirms that none clips or crosses the page.

## PDF structure and page-image inspection

The build PDF, checkpoint PDF, and promoted cumulative PDF are byte-identical:
PDF 1.7, 320 pages, 1,557,019 bytes, SHA-256
`8bd85bfe55752a3c22e6e4f366cd198b760c1b78d6ac960e8fae818a52e18285`.
All pages are 498.9 by 708.66 points at zero rotation. The reader is
unencrypted, untagged, and has `/Lang id-ID`; its Subject truthfully states the
line-258 scope.

Strict parsing verifies 1,410 named destinations, 56 outline destinations,
1,134 resolved internal links, 22 nonempty URI links, and 1,156 in-bounds
annotations. The Unit 050 opening theorem resolves to physical page 308 and
Chapter 4 to physical page 299. There is no failed destination, malformed or
targetless action, bad rectangle, AcroForm, field, widget, JavaScript,
embedded file, additional action, structure tree, `MarkInfo`, or metadata
stream. The inherited document open action is a benign initial-view
destination, not executable content.

All 55 Poppler font rows are embedded and subsetted; 41 have ToUnicode maps
and fourteen inherited mathematical/CJK font rows do not. Poppler text
extraction succeeds with 626,571 characters and zero replacement, NUL, or Han
character. Tagged or fully semantic PDF accessibility is therefore not
claimed.

Fresh 120-dpi inspection covers physical pages 1--6 and 299--320. Unit 050
occupies physical pages 308--309. The title, attribution, contents, every new
formula and diagram, the O014-C072 footnote, bibliography, both indexes, and
blank transitions are legible and unclipped. Contact sheets are:

- `qa/render/unit-050-finalB/front-contact.png`, 680,616 bytes, SHA-256
  `125c64692abbbf7877d1a644c474be92ff12f5f5a40d0e6bd3808ea5147be8f6`;
- `qa/render/unit-050-finalB/unit050-contact.png`, 1,245,451 bytes, SHA-256
  `cc84861d10010e166163490180aa4756789201bdd80e2e9a9a4d9e186f6a7424`;
- `qa/render/unit-050-finalB/tail-contact.png`, 2,676,122 bytes, SHA-256
  `a80e848ea17004e7581fb916f2d5f281541a288def688bb8028cc3278d8dc764`.

The author's official 650-page Linux/TeX Live/xindy PDF remains the reference
pagination. This 320-page Windows/MiKTeX/MakeIndex artifact is a valid partial
Indonesian reader and makes no pagination-identity claim. Unit 050 is admitted
locally; this checkpoint does not complete the corpus pursuit.
