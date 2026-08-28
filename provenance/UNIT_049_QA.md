# Unit 049 admission QA

Date: 2026-08-28  
Course/role: O014 / D80  
Unit: `o014.aljabr2.chapter4.triangulated-category-definition`  
Result: **PASS**

## Frozen source boundary

Unit 049 is the complete Section 4.1 definition cluster from the frozen
Wen-Wei Li authority `chapter4.tex` lines 62--208 inclusive. It begins with
the definition of a category with translation, includes the definition and
axioms of triangulated categories, all nine TikZ-CD diagrams, the octahedral
remark and the duality remark, and ends with the closing pointer to
`def:triangulated-subcat`. It stops at blank line 209 before the lemma at line
210. The authority remains branch `master`, commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.

The normalized-LF witness `tmp/unit049-source-slice.tex` is 11,491 bytes / 147
LF lines, SHA-256
`e61a3898512072a4df18f5c7e3255fb009d274fd327dd91b781c22fea58e2516`.
The ordered map `tmp/unit049-segment-map.jsonl` has 47 records, is 15,759
bytes, and has SHA-256
`2523adc49a09f1665e024c82afdfd9d300b71245a7adb9aa6c5bacb72c36eb8c`.
Sequences 1--47 and segment IDs are unique, ordered, and exactly match the 47
stable markers in the target and the 47 Unit 049 backend rows. Each of the
nine diagrams has its own stable diagram ID `g001`--`g009`.

## Translation and independent review

The admitted Indonesian target `source/id-ID/chapter4-unit-049.tex` is 17,618
bytes / 357 LF lines, SHA-256
`66361f2b64908293cc507d34d74089e1a51b4d3697becdabab75cae07e4000db`.
Independent source comparison verifies one section, four definitions, one
example, three remarks, the three-item category-with-translation list, the
six-item TR0--TR5 axiom list, one substantive footnote, eleven index entries,
eight labels, twelve reference occurrences, one citation, six non-diagram
display blocks, and every arrow, sign, dashed style and crossing in all nine
TikZ-CD diagrams. The unit has no theorem, proposition, lemma, proof,
exercise, hint, answer, solution, or external asset.

The translation preserves the established forms `kategori bertriangulasi`,
`segitiga terbedakan`, `funktor pergeseran`, and `aksioma oktahedral`. It
introduces `kategori dengan pergeseran`, `morfisme berderajat`, `segitiga`,
and the provisional form `kategori prabertriangulasi`. The source's distinction
between an equivalence and a strict automorphism is preserved. The theorem
title uses layout-only nonbreaking groups, and one long multivariable sentence
is split without changing its mathematics; these edits prevent new overfull
lines. No high-confidence source defect was found, so Unit 049 adds no row to
`controls/SOURCE_CORRECTIONS.csv`. No Han character, U+FFFD replacement
character, or U+2011 remains in the target.

## Cumulative integration

The frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-049.tex` and mutable alias
are byte-identical at 9,268 bytes, SHA-256
`8aca09ac5931e9a7b0a8c12183f6a4a321c378492df2fc261f3962774f113f54`.
They contain exactly 49 unique contiguous inputs and truthfully identify the
new boundary as complete Chapter 3 plus Chapter 4 through line 208 and the
duality note. The PDF Subject and visible title-page scope state the same
boundary.

Unit 049 cites only `Li1`, already present. The 26-entry bibliography
`source/id-ID/references-cumulative-through-unit-049.bib` and mutable alias
remain byte-identical to the Unit 048 bibliography at 9,881 bytes, SHA-256
`45d10bddaacbc2272a62c15c6d58e46f2bd769e4f32455c8a8cfd525fd33f0f6`.
All 26 cumulative citekeys resolve.

The modular backend has 49 unique units and 2,690 unique segments.
`backend/units.jsonl` is 36,764 bytes, SHA-256
`2fc9a6112a461e56d5de5f3072df455fedfb1cb665b2069d0d7969af6161052c`;
`backend/segments.jsonl` is 793,361 bytes, SHA-256
`40bb301546ef6c064b470c8a4d7995e564d92c0f19f1cc64c2d62f84614ca048`.
The Unit 049 row records `translated_built_qa_passed` and points to the next
source-order unit `o014.aljabr2.chapter4.cohomological-functors`.

Terminology review adds five genuinely new concepts. Both terminology
surfaces contain 511 unique concept IDs with identical preferred Indonesian
forms. `backend/terms.csv` is 35,189 bytes / SHA-256
`1dd7b0cadac2962d99d7b4267cb703634a78d39b3c60c4f4efe08fa5698c7cb6`;
`controls/TERMINOLOGY_O013_O014.csv` is 88,637 bytes / SHA-256
`260de6a5b70f039bec88d7fe2e5616d7112bd57f52f4c51319d21282aeccd7bc`.
The correction ledger remains at 72 rows, 48,064 bytes / SHA-256
`a8ba3f1f6aea2f9e259a4958cbd9279346498625c53e768acdfdc954c884347e`.

## Reproducible build

The admitted clean build is
`build/cumulative-unit-049-finalC-20260828`. FinalA exposed one new
21.3441-point overfull line in the multivariable definition and was rejected.
FinalB verified the prose reflow but preceded the final theorem-title and
fidelity micro-edits. FinalC starts from a fresh output directory and contains
the final admitted source.

FinalC ran XeLaTeX 26.5 with shell escape disabled, Biber 2.21, both bounded
MakeIndex jobs, and four further shell-escape-disabled XeLaTeX passes. Passes
3, 4, and 5 have byte-identical 31,366-byte console transcripts, SHA-256
`a1daa6934f405b4c80f8a4fdf2c0f7af90c4733668bee6ec1beafeb3b3885e9b`;
their logs differ only in the first-line run timestamp. Biber resolves all 26
citekeys with no Biber error. Its 36,087-byte BBL has SHA-256
`fd45e12d4dd985d632994c9b4ba5377310cd3e178399ffb7ab2ab1c86b9f782e`.
MakeIndex accepts 219 terminology entries and 104 symbol entries with zero
rejection or warning. The terminology index is 9,977 bytes / SHA-256
`f72550cc8b4fef5b4afc0379a27172bf0d6c85c87465cf1ce5a3a2a117526628`;
the symbol index is 3,903 bytes / SHA-256
`a98a95cccec64166b5dbc891e18aaf29bc667eb41edc23d3c18b1935d3335204`.

The final 84,585-byte log, SHA-256
`a6b5d4e1bc17d880dc553284bb624c4edcf601316cb5a3a03fa14cdaea5d7f2f`,
has no TeX/package error, undefined control sequence, undefined reference or
citation, missing character, unresolved LaTeX/biblatex rerun request,
emergency stop, or fatal error.
Seven overfull horizontal boxes remain, exactly the inherited Unit 048 set;
Unit 049 adds none. There is no overfull vertical box. Twenty-six underfull
horizontal and ten underfull vertical boxes remain nonfatal, respectively two
and two more than Unit 048. The inherited LaTeX release notices, biblatex
footnote-patching warning and imakeidx generic reminder are not reference,
citation, content, or build failures. Full-size inspection confirms that none
of these cases clips or crosses the page.

## PDF structure and page-image inspection

The build PDF, checkpoint PDF, and promoted cumulative PDF are byte-identical:
PDF 1.7, 318 pages, 1,549,628 bytes, SHA-256
`e76f5d2f3184fba979d525673963cc85453202d199243f6532beae21eaaec04c`.
All pages are 498.9 by 708.66 points at zero rotation. The reader is
unencrypted, untagged, and has `/Lang id-ID`. Its Subject truthfully says
`Pendahuluan lengkap, Bab 1 lengkap, Bab 2 lengkap, Bab 3 lengkap, dan Bab 4
sampai catatan dualitas kategori bertriangulasi`.

Strict parsing verifies 1,399 named destinations, 56 outline destinations,
1,130 resolved internal links, and 22 nonempty URI links. The stable Unit 049
destination resolves to physical page 303; the Chapter 4 destination resolves
to physical page 299. All destinations and coordinates resolve in bounds; all
1,152 link rectangles are positive and in bounds. There is no malformed or
targetless action, AcroForm, field, widget, JavaScript, embedded file,
additional action, structure tree, `MarkInfo`, or metadata stream.

All 55 Poppler font rows are embedded and subsetted; 41 have ToUnicode maps
and fourteen inherited mathematical/CJK font rows do not. Poppler text
extraction yields 623,651 characters with zero replacement, NUL, or Han
character. Tagged or fully semantic PDF accessibility is therefore not
claimed.

Fresh 120-dpi inspection covers physical pages 1--6 and 299--318. Unit 049
occupies pages 303--308. Bibliography pages occupy 309--311, physical page 312
is an intentional blank transition, the symbol index occupies 313--314, and
the terminology index occupies 315--318. The front contact sheet
`qa/render/unit-049-finalC/front-contact.png` is 245,253 bytes / SHA-256
`e55fa5cce3b273d2c937a121aa8cc89233c26d3cc7b43856ea56cf1c5f95ddcd`;
the tail contact sheet `qa/render/unit-049-finalC/tail-contact.png` is
1,449,326 bytes / SHA-256
`dfdf9b589b4f2e612e66c2db463aed53d39daca9254355546cef49520b2ffdc3`.
The updated title, attribution and contents scope; all six Unit 049 pages;
every diagram, formula, axiom, footnote and internal link; bibliography; and
both indexes are legible and unclipped, with no overlap, missing glyph, or
margin defect.

The author's official 650-page Linux/TeX Live/xindy PDF remains the reference
pagination. This 318-page Windows/MiKTeX/MakeIndex artifact is a valid partial
Indonesian reader and makes no pagination-identity claim. Unit 049 is admitted
locally; this checkpoint does not complete the corpus pursuit.
