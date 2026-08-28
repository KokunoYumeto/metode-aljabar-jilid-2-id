# Unit 051 admission QA

Date: 2026-08-28
Course/role: O014 / D80
Unit: `o014.aljabr2.chapter4.triangulated-basics`
Result: **PASS**

## Frozen source boundary

Unit 051 is the complete Section 4.2 of the frozen Wen-Wei Li authority,
`chapter4.tex` lines 260--560 inclusive. It begins with the heading and label
for the basic properties of triangulated categories, contains the closure of
results through the nine-lemma construction and Brown-representability remark,
and stops at the blank line 560 before Section 4.3 on line 561. The authority
remains branch `master`, commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.

The normalized-LF witness `tmp/unit051-source-slice.tex` is 25,193 bytes / 301
LF lines, SHA-256
`020f161ea22eacc84e0e37471baf36dffe891ff73e8cbf7ae7afa066a192e1ef`.
The ordered map `tmp/unit051-segment-map.jsonl` has 82 records, is 24,970
bytes, and has SHA-256
`d25de133ce9082e919a032880721c1aeca75f8ddbfbf21c1a42dc29217bfa461`.
Sequences 1--82 and stable IDs are unique and ordered; all nonblank source
content is covered once at the top level, nested ranges are valid, and the map
exactly matches the 82 target markers and Unit 051 backend rows.

## Translation and independent review

The admitted Indonesian target `source/id-ID/chapter4-unit-051.tex` is 35,946
bytes / 656 LF lines, SHA-256
`053ec43d8c63dedfe76be48e81384191fb41516aae7ab0a56250017c6a961d96`.
The draft initially displaced the source blocks for lines 420--560 ahead of
lines 280--419; review restored exact authority order before integration. A
second independent comparison also corrected `struktur bertriangulasi` to the
mathematically exact `struktur prabertriangulasi` in the existence clause and
added the three omitted source-xref keys to map segment `q010`.

Final independent review verifies all 82 segments; twenty labels, 46 source
references, four citations, seven index entries, 22 TikZ-CD displays, and 245
arrows occur in exact source sequence. All TikZ blocks are
whitespace-normalized byte-equivalent to the authority. Displayed and gathered
formulas, signs, morphisms, labels, citations, nesting, and the sixty matched
environment opens/closes pass. The unit contains no exercise, hint, answer,
solution, external asset, Han character, replacement character, placeholder,
duplication, omission, or Section 4.3 content.

The Indonesian is natural and mathematically faithful. Registered terminology
uses the active forms, including `kategori prabertriangulasi`, `kategori
bertriangulasi`, `segitiga terbedakan`, `adjungsi`, `subkategori penuh`,
`subkategori jenuh`, `funktor kohomologis`, `objek kompak`, and
`keterwakilan`. No new terminology row or source correction is required.

## Cumulative integration

The frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-051.tex` and mutable alias
are byte-identical at 9,372 bytes, SHA-256
`869646bc1cb66dc908483c577fcef13e846db0bb7261d3da219536408657e323`.
They contain exactly 51 unique contiguous unit inputs and truthfully state
complete Chapter 3 plus Chapter 4 through line 560 / the end of Section 4.2.
Visible title-page scope, attribution scope, PDF Subject, and bibliography
selection agree.

The four citations use already-resolved keys `Li1` and `stacks`. The 26-entry
bibliography `source/id-ID/references-cumulative-through-unit-051.bib` and
mutable alias are byte-identical at 9,881 bytes, SHA-256
`45d10bddaacbc2272a62c15c6d58e46f2bd769e4f32455c8a8cfd525fd33f0f6`.
Biber resolves all 26 cumulative citekeys.

The modular backend contains 51 unique units and 2,786 unique segments.
`backend/units.jsonl` is 38,305 bytes, SHA-256
`d1952bf1409dc37fd18d1c49af45f724e6064b7479695f9471d3e3e57263d3bd`;
`backend/segments.jsonl` is 822,546 bytes, SHA-256
`6723da200c763b8daf5bc2b91752873d7f4fc28d4621b8c5335e8eac000cedb5`.
Both JSONL files parse, all identifiers are unique, and Unit 051 points to the
next source-order localization unit. Both terminology surfaces retain 511
unique, exact-matching concept IDs.

## Reproducible build

Reject `build/cumulative-unit-051-finalA-20260828`. Although it produced a
330-page PDF, its final log retained three undefined references to not-yet
translated source destinations: Section 4.3, Definition A.2.2, and Section
A.2. The corrected reader preserves those exact designations with
`\sourcecrossref` fallbacks (`4.3`, `A.2.2`, and `A.2`) rather than emitting
broken partial-reader links.

Admit the fresh build `build/cumulative-unit-051-finalB-20260828`. It ran
XeLaTeX 26.5 with shell escape disabled, Biber 2.21, both bounded MakeIndex
jobs, and four further shell-escape-disabled XeLaTeX passes. Passes 3--5 have
byte-identical 36,701-byte console transcripts, SHA-256
`b57b7ee27ae5c13ee20aa03c9bb454c3ef90eaee65d226f1f57d0e86ecfa0c6b`.
Biber resolves 26 citekeys. Its 36,087-byte BBL has SHA-256
`fd45e12d4dd985d632994c9b4ba5377310cd3e178399ffb7ab2ab1c86b9f782e`.
MakeIndex accepts 227 terminology and 105 symbol entries with zero rejection or
warning. Their output indexes are respectively 10,465 bytes / SHA-256
`476b2ff024b93a5d0b0f5bf82f1116907297ca1dc9bf2a18e38f667096a9e66d`
and 3,948 bytes / SHA-256
`f8480ef2005af9cac6406b6adac3d6f5b373d1b20aad64c290a04f97d8fa53e0`.

The final 90,531-byte log, SHA-256
`47360109e7aaacb361a14f70988d6567e003323b2291fbc7c1a2285d9e2bd4c1`,
has no TeX/package error, undefined control sequence, undefined reference or
citation, missing character, rerun request, emergency stop, or fatal error.
Seven overfull horizontal boxes remain exactly the inherited Unit 050 set, and
there is no overfull vertical box. Twenty-seven underfull horizontal and eleven
underfull vertical boxes are nonfatal. Full-size page inspection confirms no
clipping, collision, or unintended overflow.

## PDF structure and page-image inspection

The build PDF, frozen checkpoint PDF, and promoted cumulative PDF are
byte-identical: PDF 1.7, 330 pages, 1,606,437 bytes, SHA-256
`a34260d5cbb051c4209b7b7e8189ab794fe7656f10ed0bfa4b3491868b936945`.
All pages are 498.9 by 708.66 points at zero rotation. The reader is
unencrypted, untagged, and has `/Lang id-ID`; its Subject truthfully states the
line-560 / Section-4.2 scope.

Strict parsing resolves all 1,463 named destinations, 57 outline destinations,
1,184 internal links, 22 nonempty URI links, and 1,206 in-bounds annotations.
The Unit 051 opening theorem resolves to physical page 310; Chapter 4 resolves
to physical page 299. There is no failed destination, malformed or targetless
action, bad rectangle, AcroForm, field, widget, JavaScript, embedded file,
additional action, structure tree, `MarkInfo`, or metadata stream. The inherited
document open action is the benign page-fit array `[page, /Fit]`.

All 55 Poppler font rows are embedded and subsetted; 41 have ToUnicode maps and
fourteen inherited mathematical rows do not. Text extraction succeeds with
648,044 characters and zero replacement, NUL, or Han character. The extractor
emits inherited font-mapping diagnostics but exits successfully and yields a
legible Indonesian text layer. Tagged or fully semantic PDF accessibility is
therefore not claimed.

Fresh 120-dpi inspection covers physical pages 1--6 and 299--330. Unit 051
occupies physical pages 310--320. The title, attribution, contents, all new
definitions, propositions, proofs, formulas, arrow labels, 22 diagrams,
forward-reference fallbacks, bibliography, both indexes, and section boundary
are legible, centered, and unclipped. Intentional whitespace on the final
Section-4.2 page preserves the source-order boundary and introduces no layout
defect. Contact sheets are:

- `qa/render/unit-051-finalB/front-contact.png`, 457,340 bytes / SHA-256
  `3341b5ef2e7ee767ded6e50249bd216e7cb3c0d97b19a7c396417da6225326cc`;
- `qa/render/unit-051-finalB/chapter4-contact.png`, 2,198,840 bytes / SHA-256
  `e14825e3c2d897cd5b8175dcba4c1f768c4029f947e795709bdf69bdabcf4766`;
- `qa/render/unit-051-finalB/unit051-a-contact.png`, 1,259,605 bytes / SHA-256
  `71b1ed63098c4d7b65e6851bce17a2551698822d5bdef5bba4556f5afb1ae74c`;
- `qa/render/unit-051-finalB/unit051-b-contact.png`, 1,122,318 bytes / SHA-256
  `286eeec7be6d7b2335bcfbe37399f992661c96363fd5bc886d113170130bb7c0`;
- `qa/render/unit-051-finalB/tail-contact.png`, 1,448,014 bytes / SHA-256
  `3144c17f9727b2e6b720d8dc162921bba1e0837adde5bf4126c709046b402054`.

The author's official 650-page Linux/TeX Live/xindy PDF remains the reference
pagination. This 330-page Windows/MiKTeX/MakeIndex artifact is a valid partial
Indonesian reader and makes no pagination-identity claim. Unit 051 is admitted;
this checkpoint does not complete the corpus pursuit.
