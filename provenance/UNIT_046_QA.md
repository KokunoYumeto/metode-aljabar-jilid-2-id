# Unit 046 admission QA

Date: 2026-08-26  
Course/role: O014 / D80  
Unit: `o014.aljabr2.chapter3.k-injectives`  
Result: **PASS**

## Frozen source boundary

Unit 046 is the complete Section 3.15, `sec:K-injectives`, from the frozen
Wen-Wei Li authority `chapter3.tex` lines 2936--3200 inclusive. Substantive
content ends at line 3199 and line 3200 is the terminal blank separator. The
unit stops before the chapter exercise block at line 3201. The authority
remains branch `master`, commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.

The normalized-LF source witness `tmp/unit046-source-slice.tex` is 20,086
bytes, 265 LF lines / 232 nonblank lines, SHA-256
`5a56872f1fbdd507618130c9def1445e5689dba76d94189676a97e2a677a72e6`.
The ordered map `tmp/unit046-segment-map.jsonl` has 83 records (35 top-level,
48 nested), is 24,432 bytes, and has SHA-256
`64dcb930ff3a0327d9b15e6cc34764f9f41d458a25e9b5857dffdf6c322e3a1a`.
Sequences 1--83, segment IDs, and ordering are unique. The top-level spans are
nonoverlapping and cover every nonblank authority line; all nested spans lie
within their declared parents.

## Translation and independent review

The admitted Indonesian target `source/id-ID/chapter3-unit-046.tex` is 28,931
bytes / 651 LF lines / 607 nonblank lines, SHA-256
`15f84671182c59ac6779a61968b9d03ca8f43d8625fd81399e4a44dacddbf496`.
Its 83 unique stable segment markers exactly match map order and the 83 Unit
046 backend segment rows. Independent post-patch segment and formula review
verifies all 18 labels, 50 reference targets (43 `ref`, six `eqref`, and one
future-target `sourcecrossref`), six citation occurrences / five unique keys,
four index entries, four footnotes, fifteen TikZ-CD blocks, 74 diagram arrows,
and 50 balanced LaTeX environments. No Han character, U+FFFD, or U+2011
remains.

The sole reference beyond this partial reader, `prop:cplx-triangulated`, is
represented with `\sourcecrossref` and its frozen source designation rather
than as a broken internal link. Review also enforces the settled forms
`homotopik` and `barisan` and confirms all degrees, inverse limits, products,
truncations, cones, morphism directions, and proof implications against the
authority.

Three high-confidence inherited defects are corrected and visibly disclosed
in translator footnotes and in `controls/SOURCE_CORRECTIONS.csv` as
O014-C064--O014-C066. The target restores `\varprojlim_k` at authority line
3063, restores `\Delta_{\tau A}` in the lower natural-cone diagram at line
3137, and normalizes the undefined `\Delta_{\tau_A}` to the established
`\Delta_{\tau A}` at line 3145. The authority has one footnote in this
boundary; the target has that footnote plus these three disclosures.

## Cumulative integration

The frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-046.tex` and mutable wrapper
alias are byte-identical at 9,020 bytes, SHA-256
`8fea814e7776b2170fef6cc07f8aece3aa0053e6e239cb4f024f8b8f51174775`.
They contain exactly 46 unique contiguous inputs, Units 001--046, and
truthfully identify Chapter 3 through Section 3.15 / authority line 3200. The
25-entry bibliography `references-cumulative-through-unit-046.bib` and both
legacy/current aliases are byte-identical at 9,435 bytes, SHA-256
`e7696fffa125a2381dc8d8ede47b4741127caad4fb47d5716a378c7e06e21098`.
Unit 046 adds the source entries `Spa88`, `BN93`, and `Serp03`; all five unique
Unit 046 citation keys resolve.

The modular backend now has 46 unique units and 2,521 unique segments.
`backend/units.jsonl` is 34,517 bytes, SHA-256
`af7ab6f34da9dff08d553ff650bedf089a9b217c655886a50e4d71a3467f0972`;
`backend/segments.jsonl` is 742,864 bytes, SHA-256
`369b4482de9464d549b69043c660cf361d299ff9efcf21c000430004680591ab`.
The Unit 046 row records status `translated_built_qa_passed`, and its 83
segment rows exactly match the source map. The synchronized terminology stores
each contain 479 unique concepts and agree on every preferred form.
`backend/terms.csv` is 32,645 bytes, SHA-256
`48bf9b975b8f20ef95f155850421cc8620877e56f4b8b0b22adf5f5969f34632`;
`controls/TERMINOLOGY_O013_O014.csv` is 81,555 bytes, SHA-256
`04bf0f2217adbb15dba375db669d698d0050a7e40a51ac505e2cf9ddd30ad5bd`.
The two new first-use concepts are `enough_k_injective_complexes` and
`enough_k_projective_complexes`.

## Reproducible build

The admitted clean build is `build/cumulative-unit-046-finalA-20260826`.
XeLaTeX 26.5 ran with shell escape disabled, Biber 2.21 ran with the bounded
source directory supplied explicitly, both MakeIndex jobs ran in the build
directory, and four further XeLaTeX passes followed. Passes 3, 4, and 5 have
byte-identical 30,603-byte console transcripts, SHA-256
`85e6d970a6a093f458fd5ba2017832d1db59e1cf136aec7a755a5420976eaa8f`,
which proves convergence of the final replay surface.

Biber resolves all 25 citekeys with zero error or warning. Its 34,776-byte BBL
has SHA-256
`daefbe3f540602377da896eeac0b1fe39de056e8b54202c5e8ff5a0dfcc550e0`.
MakeIndex accepts 207 terminology entries and 103 symbol entries with zero
rejection or warning. The terminology index is 9,399 bytes / SHA-256
`66495955ef2773ea75b8621357585e487c1da71eb8d22b87d05f7f0387f26364`;
the symbol index is 3,867 bytes / SHA-256
`ddd5c27995115d22a8e4ecde7e4e7215a67912c6d87fac858d882614437aef98`.

The final 83,717-byte log, SHA-256
`65dbe5357362499d8671057a21cf1b5f62a0a7028644a6eca331c4bcd8ee1d05`,
contains no TeX/package error, undefined reference or citation, missing
character, emergency stop, or fatal error. Seven overfull horizontal boxes
remain: three inherited cases (8.65707 pt, 42.92992 pt, and 0.62685 pt) and
four Unit 046 cases (4.2665 pt, 2.0793 pt, 6.06439 pt, and 14.60446 pt).
There is no overfull vertical box. Twenty-four underfull horizontal and seven
underfull vertical boxes are nonfatal. The generic imakeidx reminders are
expected in the shell-escape-disabled external-index workflow; both indexes
are loaded, and the final three XeLaTeX transcripts are identical. Full-size
page-image inspection confirms that the four new overfull cases are visually
benign and do not cross the text block or clip.

## PDF structure and page-image inspection

The build PDF, checkpoint PDF, and promoted cumulative PDF are byte-identical:
PDF 1.7, 302 pages, 1,468,650 bytes, SHA-256
`4edebacd5d8a2f8fd62da9d9553b3b8ad3699fcd523311bae04759c7c1176bc9`.
All pages are 498.9 by 708.66 points with zero rotation. The file is
unencrypted and untagged. Strict parsing verifies 53 outline entries, 1,299
named destinations, 1,073 internal GoTo links, and twenty URI links. All 1,093
link rectangles lie within page bounds; every internal name resolves. There
is no malformed destination, form, widget, JavaScript, embedded file,
additional action, structure tree, `MarkInfo`, or metadata stream. The opening
action is the ordinary page-destination array.

All 54 `pdffonts` rows are embedded and subsetted. Forty-two have ToUnicode
maps; twelve inherited mathematical fonts do not. Therefore neither tagged-
PDF nor fully semantic accessibility is claimed.

Fresh 120-dpi inspection covers physical pages 1--6 and the contiguous tail
range 276--302. Unit 046 occupies physical pages 282--291; bibliography and
both indexes occupy pages 293--302. Formulas, all fifteen diagrams, theorem
heads, correction footnotes, bibliography, and both indexes are centered
within the text block, legible, and unclipped, with no overlap or missing
glyph. Physical pages 2, 4, 292, and 296 are intentional blank transitions.
The page 276--302 contact sheet is 3,270,870 bytes, SHA-256
`59d7327eb3659675487087dc1033a46e37cacab1dbfde04676bda116223ede72`.

The author's official 650-page Linux/TeX Live/xindy PDF remains the reference
pagination. This 302-page Windows/MiKTeX/MakeIndex artifact is a valid partial
Indonesian reader and makes no pagination-identity claim. Unit 046 is admitted
locally; this checkpoint does not complete the corpus pursuit.
