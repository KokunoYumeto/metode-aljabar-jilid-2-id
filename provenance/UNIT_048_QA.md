# Unit 048 admission QA

Date: 2026-08-27
Course/role: O014 / D80
Unit: `o014.aljabr2.chapter4.overview`
Result: **PASS**

## Frozen source boundary

Unit 048 is the complete Chapter 4 overview and reading-tip enclosure from the
frozen Wen-Wei Li authority `chapter4.tex` lines 9--60 inclusive. It stops at
the blank line 61 before Section 4.1 (`sec:triangular-def`) begins on line 62.
The authority remains branch `master`, commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.

The normalized-LF witness `tmp/unit048-source-slice.tex` is 8,677 bytes / 52
LF lines, SHA-256
`800e4d6242edc127ed4db7fa45f98259cea386773d9333055ad170e9b9d971ed`.
The ordered map `tmp/unit048-segment-map.jsonl` has 27 records, is 7,141
bytes, and has SHA-256
`41dcd96e597d7824fd10e19ff49b5beecd014d5bf1e02eb96a240d08a598481c`.
Sequences 1--27 and segment IDs are unique, ordered, and exactly match the 27
stable markers in the target and the 27 Unit 048 backend rows.

## Translation and independent review

The admitted Indonesian target `source/id-ID/chapter4-unit-048.tex` is 13,727
bytes / 248 LF lines, SHA-256
`b987c6d3b29c0853a128b8fa73eede0a769c38deea7ee9392ad5d8beb4f206b7`.
Independent comparison verifies the chapter heading and label, two enumerate
enclosures and five items, five display blocks, two TikZ-CD diagrams and all
ten arrows, every formula/sign/superscript, and every source cross-reference.
The segment map has 24 unique source reference targets; the target preserves
all of them through `\sourcecrossref`, `\ref`, or the existing `\CHref`
surface. The unit has no citation, exercise, hint, answer, or solution.

Two high-confidence inherited defects are corrected and disclosed at point of
use and in `controls/SOURCE_CORRECTIONS.csv` as O014-C070--O014-C071. The
target restores the right-hand localization functor label `Q'` in the second
diagram and restricts the classical Ext formula to objects of
`\mathcal{A}` viewed as degree-zero complexes. The final language review also
uses the established nominal form `sifat keterhapusan`. One layout-only prose
shortening around the first mapping-cone paragraph removes a new 3.73564-point
overfull line without changing mathematical content. No Han character, U+FFFD
replacement character, or U+2011 remains in the target.

## Cumulative integration

The frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-048.tex` and mutable alias
are byte-identical at 9,146 bytes, SHA-256
`0b79115969e927dc0dbe395405cb17a97a0d05749ced4bca6ccf8c3153c181f6`.
They contain exactly 48 unique contiguous inputs and truthfully identify the
new boundary as complete Chapter 3 plus the Chapter 4 overview through line
60. The PDF Subject and visible title-page scope state the same boundary.

Unit 048 introduces no citation. The 26-entry bibliography
`source/id-ID/references-cumulative-through-unit-048.bib` and mutable alias
remain byte-identical to the Unit 047 bibliography at 9,881 bytes, SHA-256
`45d10bddaacbc2272a62c15c6d58e46f2bd769e4f32455c8a8cfd525fd33f0f6`.
All 26 cumulative citekeys resolve.

The modular backend has 48 unique units and 2,643 unique segments.
`backend/units.jsonl` is 35,994 bytes, SHA-256
`bb09febf697093493504cc882d7e62361a111000cff90c1f6c8b2ea02779c61a`;
`backend/segments.jsonl` is 777,649 bytes, SHA-256
`011be5aa08001e9ffcf33800b52bdfb257adc981d252e3b32382996ff872dab0`.
The Unit 048 row records `translated_built_qa_passed`.

Terminology review adds 24 genuinely new first-use concepts and records three
variants without changing the established preferred forms `kategori
bertriangulasi`, `kategori turunan`, and `segitiga terbedakan`. Both
terminology surfaces contain 506 unique concepts with identical IDs and
preferred Indonesian forms. `backend/terms.csv` is 34,810 bytes / SHA-256
`4ac8c93b4f0afd9e90594381634aa2552aecc420097ab36a19dc109de9fb831b`;
`controls/TERMINOLOGY_O013_O014.csv` is 87,271 bytes / SHA-256
`1f7a6f175c071a0964e297b5edb26f99ba43e1f09dc6629d6d5996344dcdb364`.
The correction ledger has 72 rows and no duplicate ID; it is 48,064 bytes /
SHA-256
`a8ba3f1f6aea2f9e259a4958cbd9279346498625c53e768acdfdc954c884347e`.

## Reproducible build

The admitted build is `build/cumulative-unit-048-finalD-20260827`. FinalA
proved the first integrated reader but was rejected because it exposed one new
3.73564-point overfull line. FinalB and finalC were interrupted mid-pass and
are rejected incomplete candidates. FinalD starts from a fresh empty output
directory after the layout-only wording correction.

FinalD ran XeLaTeX 26.5 with shell escape disabled, Biber 2.21, both bounded
MakeIndex jobs, and four further shell-escape-disabled XeLaTeX passes. Passes
3, 4, and 5 are byte-identical at 30,807 bytes, SHA-256
`6e209ee2bc9d6c6d90475d9e9a95a2d7c06b17eb81a528e4c5ad7cc6d62aea76`.
Biber resolves all 26 citekeys with no Biber warning or error. Its 36,087-byte
BBL has SHA-256
`fd45e12d4dd985d632994c9b4ba5377310cd3e178399ffb7ab2ab1c86b9f782e`.
MakeIndex accepts 209 terminology entries and 103 symbol entries with zero
rejection or warning. The terminology index is 9,522 bytes / SHA-256
`29e96ef7fb0d4de580ad0e857c6cdaab33f824d64403a179205f8baa4ae2fce5`;
the symbol index is 3,867 bytes / SHA-256
`ddd5c27995115d22a8e4ecde7e4e7215a67912c6d87fac858d882614437aef98`.

The final 83,923-byte log, SHA-256
`bba64de5ba2db7d262cd534d33b9ab53477c525e3dfb0a44394ba4541ba06662`,
has no TeX/package error, undefined control sequence, undefined reference or
citation, missing character, rerun request, emergency stop, or fatal error.
Seven overfull horizontal boxes remain, exactly the seven inherited from Unit
047 at 8.65707, 42.92992, 0.62685, 4.2665, 2.0793, 6.06439, and 14.60446
points. There is no overfull vertical box. Twenty-four underfull horizontal
and eight underfull vertical boxes remain nonfatal. The inherited LaTeX release
notices and biblatex footnote-patching warning are not reference, citation,
content, or build failures. Full-size page inspection confirms that none of
these cases clips or crosses the page.

## PDF structure and page-image inspection

The build PDF, checkpoint PDF, and promoted cumulative PDF are byte-identical:
PDF 1.7, 314 pages, 1,526,462 bytes, SHA-256
`8eaf326be418d06f8c75dd4ea255073327a25a267d4be1813417c456a5a19d60`.
All pages are 498.9 by 708.66 points at zero rotation. The reader is
unencrypted, untagged, and has `/Lang id-ID`. Its Subject truthfully says
`Pendahuluan lengkap, Bab 1 lengkap, Bab 2 lengkap, Bab 3 lengkap, dan
ikhtisar Bab 4`.

Strict parsing verifies 1,377 named destinations, 55 outline destinations,
1,115 resolved internal links, and 22 nonempty URI links. The stable Unit 048
destination and Chapter 4 outline both resolve to physical page 299. All
destinations and coordinates resolve in bounds; all 1,137 link rectangles are
positive and in bounds. There is no malformed or targetless action, AcroForm,
field, widget, JavaScript, embedded file, additional action, structure tree,
`MarkInfo`, or metadata stream.

All 56 Poppler font rows are embedded and subsetted; 41 have ToUnicode maps
and fifteen inherited mathematical/CJK font rows do not. Poppler text
extraction yields 613,378 characters with zero replacement, NUL, or Han
character. Tagged or fully semantic PDF accessibility is therefore not
claimed.

Fresh 120-dpi inspection covers physical pages 1--6 and 296--314. Unit 048
occupies pages 299--303. Bibliography pages begin at 305, the symbol index at
309, and the terminology index at 311. Physical pages 2, 4, 298, 304, and 308
are intentional blank transitions. The front contact sheet
`qa/render/unit-048-finalD/front-contact.png` is 893,925 bytes / SHA-256
`ce4eef600c44ee152df5182423ba8a4817fe15854a4fce7074f822fbaaf357c9`;
the tail contact sheet `qa/render/unit-048-finalD/tail-contact.png` is
4,447,100 bytes / SHA-256
`b8db8be25409e6aa301637a272eb8ad22644ba03eac48c1171ef19fb62fdbf23`.
The updated title/attribution/contents scope, Chapter 4 opener, all five new
pages, both diagrams, correction footnotes, reading-tip box, bibliography, and
both indexes are legible and unclipped, with no overlap, missing glyph, or
margin defect.

The author's official 650-page Linux/TeX Live/xindy PDF remains the reference
pagination. This 314-page Windows/MiKTeX/MakeIndex artifact is a valid partial
Indonesian reader and makes no pagination-identity claim. Unit 048 is admitted
locally; this checkpoint does not complete the corpus pursuit.
