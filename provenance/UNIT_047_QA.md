# Unit 047 admission QA

Date: 2026-08-26  
Course/role: O014 / D80  
Unit: `o014.aljabr2.chapter3.exercises`  
Result: **PASS**

## Frozen source boundary

Unit 047 is the complete Chapter 3 Exercises environment from the frozen
Wen-Wei Li authority `chapter3.tex` lines 3201--3425 inclusive and the end of
that source file. It contains all 26 exercises and all 17 active hints and
stops before `chapter4.tex`. The authority remains branch `master`, commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.

The normalized-LF witness `tmp/unit047-source-slice.tex` is 18,004 bytes / 225
LF lines / 183 nonblank lines, SHA-256
`831dd2a9e3ddacc3ece25aaae474487678f93aa4731660ae07e81aa69e5cb4a0`.
The ordered map `tmp/unit047-segment-map.jsonl` has 95 records, is 27,644
bytes, and has SHA-256
`c227c6a7a13fba436af6ece633816ef5eb1f54af5d0d2d253f4baf09f459cf8c`.
Sequences 1--95 and segment IDs are unique, ordered, and exactly match the 95
stable markers in the target and the 95 Unit 047 backend rows.

## Translation and independent review

The admitted Indonesian target `source/id-ID/chapter3-unit-047.tex` is 26,722
bytes / 657 LF lines / 621 nonblank lines, SHA-256
`18f1639f9800e751f60418c018770b50eae69067b4f4b39384446443931ac91f`.
Independent formula and segment review verifies all 26 top-level exercises,
17 hints, four TikZ-CD diagrams / 25 arrows, 29 reference occurrences over 24
unique targets, the two citations `Lo98` and `Ni09`, two index entries, and
four footnotes. Two Chapter 8 references beyond this partial reader use the
printed `\sourcecrossref` fallback instead of emitting broken links. No Han
character, U+FFFD replacement character, or U+2011 remains.

Three high-confidence inherited defects are corrected and disclosed at point
of use and in `controls/SOURCE_CORRECTIONS.csv` as O014-C067--O014-C069. The
target restores the missing inverse-limit index `\varprojlim_k`, restores the
required coefficient ring `\Bbbk[x,y]/(x^n,y^n)`, and applies the functor `F`
consistently in the final exercise's cohomology morphisms. The final target
also reflows one wide set-bijection display without changing its mathematical
content.

## Cumulative integration

The frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-047.tex` and mutable alias
are byte-identical at 9,043 bytes, SHA-256
`806568a50c4ec6bbfe396f46eeb009337d977d24b7b752cdbb951f6c1f6bf496`.
They contain exactly 47 unique contiguous inputs and truthfully identify
Chapter 3 as complete through authority line 3425. The exercise environment
creates its outline anchor immediately before the `Latihan` entry, so its
bookmark and stable unit destination both land on the exercise heading.

The 26-entry bibliography
`source/id-ID/references-cumulative-through-unit-047.bib` and both current
aliases are byte-identical at 9,881 bytes, SHA-256
`45d10bddaacbc2272a62c15c6d58e46f2bd769e4f32455c8a8cfd525fd33f0f6`.
All 26 cumulative citekeys resolve; Unit 047 adds `Ni09` while reusing `Lo98`.

The modular backend has 47 unique units and 2,616 unique segments.
`backend/units.jsonl` is 35,228 bytes, SHA-256
`cf58a6ebf6fcfd73d429a27b0e392db15d0d18b53d94cc77addfe6584554601e`;
`backend/segments.jsonl` is 770,508 bytes, SHA-256
`1b233c30f7a062c49fdaa981fe32243d541633f4052c799cbcbe8f2fe26575b1`.
The Unit 047 row records `translated_built_qa_passed`. The synchronized
terminology surfaces each contain 482 exact-matching concepts. Backend
`backend/terms.csv` is 32,877 bytes / SHA-256
`3c79ee6e5e1238249d8cc91f0180cb8161e012c9738db24fe39f79da5b59ed60`;
control `controls/TERMINOLOGY_O013_O014.csv` is 82,223 bytes / SHA-256
`f11933a73309775fc7625a202d8d6fc0e5e7ecdf2bc263faaa76b79ca44db84a`.

## Reproducible build

The admitted build is `build/cumulative-unit-047-finalC-20260826`. FinalA was
a pre-QA candidate; finalB proved the layout repair but was rejected because
its title/attribution scope text and PDF Subject still stopped at Section
3.15 / line 3200. FinalC corrects those statements to complete Chapter 3 /
line 3425 and adds the missing exercise bookmark anchor.

FinalC ran XeLaTeX 26.5 with shell escape disabled, Biber 2.21, both bounded
MakeIndex jobs, and four further shell-escape-disabled XeLaTeX passes. Passes
3, 4, and 5 are byte-identical at 34,955 bytes, SHA-256
`e0762d770d4df1ba4a4e9e7db2df9dcbc2df81ed603a75550abc8342033445c3`.
Biber resolves all 26 citekeys with no Biber warning or error. Its 36,087-byte
BBL has SHA-256
`fd45e12d4dd985d632994c9b4ba5377310cd3e178399ffb7ab2ab1c86b9f782e`.
MakeIndex accepts 209 terminology entries and 103 symbol entries with zero
rejection or warning. The terminology index is 9,522 bytes / SHA-256
`29e96ef7fb0d4de580ad0e857c6cdaab33f824d64403a179205f8baa4ae2fce5`;
the symbol index is 3,867 bytes / SHA-256
`ddd5c27995115d22a8e4ecde7e4e7215a67912c6d87fac858d882614437aef98`.

The final 88,221-byte log, SHA-256
`26807b53bf991703a1e0b126c3fc47e327dcb95033e27ad5bb1bb85f15d7b9a0`,
has no TeX/package error, undefined control sequence, undefined reference or
citation, missing character, rerun request, emergency stop, or fatal error.
Seven overfull horizontal boxes remain, exactly the seven inherited from the
Unit 046 reader at 8.65707, 42.92992, 0.62685, 4.2665, 2.0793, 6.06439, and
14.60446 points. There is no overfull vertical box. Twenty-four underfull
horizontal and seven underfull vertical boxes remain nonfatal. Full-size page
inspection confirms that none of these cases clips or crosses the page.

## PDF structure and page-image inspection

The build PDF, checkpoint PDF, and promoted cumulative PDF are byte-identical:
PDF 1.7, 308 pages, 1,510,819 bytes, SHA-256
`ad728f05e2069ca0bcaabcba8de5bdf8fcda311b1a022125f46c2c817c16cfec`.
All pages are 498.9 by 708.66 points at zero rotation. The reader is
unencrypted, untagged, and has `/Lang id-ID`. Its Subject truthfully says
`Pendahuluan lengkap, Bab 1 lengkap, Bab 2 lengkap, dan Bab 3 lengkap`.

Strict parsing verifies 1,362 named destinations, 54 outline destinations,
1,107 resolved internal links, and 22 nonempty URI links. The stable Unit 047
destination and Chapter 3 `Latihan` outline both resolve to physical page 291.
All destinations and coordinates resolve in bounds; all 1,129 link rectangles
are positive and in bounds. There is no malformed or targetless action,
AcroForm, field, widget, JavaScript, embedded file, additional action,
structure tree, `MarkInfo`, or metadata stream. The opening action is the
ordinary first-page `/Fit` array.

All 55 Poppler font rows are embedded and subsetted; 41 have ToUnicode maps
and fourteen inherited mathematical fonts do not. Tagged or fully semantic
PDF accessibility is therefore not claimed.

Fresh 120-dpi inspection covers physical pages 1--6 and 288--308. Unit 047
occupies pages 291--297. Bibliography pages are 299--301, the symbol index is
303--304, and the terminology index is 305--308. Physical pages 2, 4, 298,
and 302 are intentional blank transitions. The contact sheet
`qa/render/unit-047-finalC/unit-047-finalC-contact.png` is 2,981,397 bytes,
SHA-256
`79369f550b60b89792356acc2a9c23aa497613e233677dc2c87eceba23d8e418`.
Every new exercise/hint boundary, all four diagrams, the reflowed bijection,
long formulas, correction footnotes, bibliography, and both indexes are
legible and unclipped, with no overlap, missing glyph, or margin defect.

The author's official 650-page Linux/TeX Live/xindy PDF remains the reference
pagination. This 308-page Windows/MiKTeX/MakeIndex artifact is a valid partial
Indonesian reader and makes no pagination-identity claim. Unit 047 is admitted
locally; this checkpoint does not complete the corpus pursuit.
