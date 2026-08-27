# Decision log

## D001 - Primary corpus admitted

Admit Wen-Wei Li Volume 2 at commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`. The author-controlled Gitee
repository is primary; GitHub is the exact official mirror.

## D002 - Course extent

Use Prelude plus Chapters 1-5 as the integrated core. Preserve Chapters 6-9
and both appendices as source-order extensions. Do not market all 650 pages as
a one-semester course.

## D003 - Bounded alternative disposition

Reject Leinster plus Stacks as the primary course. Retain Leinster as a gentle
donor and Stacks as a semantic/reference verifier only.

## D004 - First production boundary

Unit 001 is `prelude.tex` lines 9-29 inclusive: the opening of the Introduction
through `何谓线性代数`, ending immediately before `同调简史`. It is the first
canonical content in source order. `pre-prelude.tex` is inactive and excluded.

## D005 - O013 terminology link

Use locale-neutral concept IDs shared with O013. Preferred forms currently
include `gelanggang`, `modul`, `lapangan`, `kategori`, `funktor`, `modul
kuosien`, `kernel`, `kokernel`, and `citra`. O013 now has its own separate
local production lane at `04_mirrors/id/metode-aljabar-jilid-1-id`. The
identities here are coordinated terms only; this O014 file neither mutates
that lane nor claims its glossary is already published.

For explicit O013 coordination, use: `kategori monoidal`, `funktor`,
`transformasi alami`, `limit`, `keterwakilan`, `pengayaan kategori`, `hasil
kali tensor`, and `pelengkapan`; retain `kompletisasi` only as a searchable
variant.

## D006 - Mastery bridge

Do not invent or relocate exercises into the Prelude. Preserve the 194
chapter/appendix exercises and 117 hints in their source positions. Any worked
solutions or diagram-chasing bridge must be newly authored and separately
labeled.

## D007 - Accessibility bridge

The upstream PDF is untagged and has no HTML/EPUB/MathML surface. Treat the
editable LaTeX and source-native TikZ as inputs for a later semantic reader;
do not call the current PDF accessible merely because its text is selectable.

## D008 - Portable build profile

The upstream `font-setup-open.tex` and cover still hard-code Noto CJK families.
For local derivative builds, use `font-setup-id.tex`, which substitutes bundled
Fandol fonts without changing mathematical content. Keep the authority capture
byte-exact and record this as a build/typography modification.

## D009 - Unit 002 production boundary

Unit 002 is `prelude.tex` lines 30--103 inclusive, from `同调简史` through
the end of its homotopical-algebra subsection, stopping before `本书旨趣`.
Its stable ID is `o014.aljabr2.prelude.homology-history`. Preserve the one
section, five subsections, three lists with ten items, three displays, one
TikZ-CD diagram, and citation sequence `CE56`, `CE56`, `CE56`, `Gr57`.

## D010 - Disclosed source correction O014-C001

Source line 49 says that the degree-one Hochschild term classifies all
derivations. Correct the Indonesian reader to the standard statement that
first Hochschild cohomology classifies derivations modulo inner derivations.
Mark the intervention with an explicit translator's footnote and maintain its
exact evidence and pointers in `SOURCE_CORRECTIONS.csv`; do not silently alter
the claim.

## D011 - Clickable license notice

Naming CC BY 4.0 without its URI is insufficient for the reader surface.
Retain the bundled `LICENSE` file and place the exact
`https://creativecommons.org/licenses/by/4.0/` link on every standalone and
cumulative attribution page. Unit 001 was rebuilt to satisfy this rule.

## D012 - Unit 003 production boundary

Unit 003 is `prelude.tex` lines 104--126 inclusive, from `本书旨趣` through
its `路径与取舍` subsection, stopping before `使用指南`. Its stable ID is
`o014.aljabr2.prelude.book-purpose`. Preserve the one section, two
subsections, ten narrative segments, seven bibliography keys, nLab link, and
Freyd--Mitchell forward reference.

## D013 - Source-forward references in partial readers

Do not emit broken links merely because a source label points beyond the
current cumulative boundary. `\sourcecrossref{label}{designation}` prints the
verified source designation as plain text while the target is absent and
becomes a normal `\ref` when the source label enters the cumulative build.
Unit 003 therefore shows Appendix B.6 now and will resolve `sec:FM` normally
in the complete edition.

## D014 - Unit 004 production boundary

Unit 004 is `prelude.tex` lines 127--153 inclusive, from `使用指南` through
the category-size convention, stopping before `结构总览`. Its stable ID is
`o014.aljabr2.prelude.reader-guide`. Preserve its three subsections, ten
narrative paragraphs, two-item list, universe math, Li1 citation locators,
exercise policy, and teaching-use qualifications.

## D015 - Strongly inaccessible cardinal terminology

Use `kardinal tak terjangkau kuat` with the first-use English gloss
`strongly inaccessible cardinal`. Keep `kardinal tak terakses kuat` only as a
searchable variant; attested Indonesian mathematical usage and naturalness
favor `tak terjangkau`. Evidence retained at
`https://ejournal.unisba.ac.id/index.php/matematika/article/download/3376/2059`.

## D016 - Unit 005 production boundary

Unit 005 is `prelude.tex` lines 154--183 inclusive, from `结构总览` through
the author-page and errata invitation, stopping before `鸣谢`. Its stable ID
is `o014.aljabr2.prelude.structure-overview`. Preserve the three description
lists and eleven labeled items, the exact seven-run math sequence, every
chapter/appendix scope qualification, and the distinction between flat descent
as a named subject and faithful-flat hypotheses used later in the book.

## D017 - Unit 006 production boundary and personal names

Unit 006 is `prelude.tex` lines 185--205 inclusive, from `鸣谢` through the
author's signature, date, and place, stopping before `凡例`. Its stable ID is
`o014.aljabr2.prelude.acknowledgments`. Preserve all roles, institutions,
funding details, hedges, and the complete literary closing. The frozen source
itself attests `Wen-Wei Li`; keep the other eleven thanked names and editor
name in their exact Han forms until preferred Latin spellings are proven from
primary authority. Disclose that choice rather than guessing identity-specific
romanizations. The historical NSFC English program name is `Excellent Young
Scientists Fund`.

## D018 - Localize inherited bibliography strings

`AJbook2.cls` overrides the English biblatex connector `in` with Chinese
`刊于`. Do not modify the exact upstream support file. Override reader-facing
bibliography strings in the Indonesian wrapper, including `in={dalam}`, so
strict active-language residue checks do not pass Chinese interface text into
the derivative bibliography. Intentional Han personal names remain a separate,
documented exception.

## D019 - Unit 007 closes the Prelude

Unit 007 is `prelude.tex` lines 207--495 inclusive, the complete `凡例`
section through EOF. Its stable ID is
`o014.aljabr2.prelude.conventions`. Preserve nine subsections, 20 active
TikZ-CD diagrams, four notation tables, 19 list items, 15 citations, three
source-forward references, 45 index commands, and the inactive commented
diagram. Its 114 locale-neutral segment IDs are the backend closure for the
unit.

## D020 - Disclosed convention-section source corrections

Register and disclose three narrowly proven interventions. O014-C002 changes
the `A^{opp}` symbol-index typo at source line 335 to the paragraph's defined
`R^{opp}`. O014-C003 changes the canonical coproduct injection target at
source line 444 from a product to the coproduct and adds an adjacent translator
note. O014-C004 removes the syntactically extraneous backslash after the second
TikZ-CD opener at source line 483 without changing the diagram. None is a
silent repair.

## D021 - Indonesian dual indexes and table reflow

Retain separate term and symbol indexes in the derivative reader. Use English
glosses alongside Indonesian term entries and keep the cross-course
terminology ledger separate from the reader index. Reflow the two wide
universal-property tables by reducing intercolumn padding while preserving
mathematical content and readable type; do not shrink them into an unreadable
facsimile. The resulting term index uses two footnote-sized columns on one
page, and the symbol index uses three columns.

## D022 - Unit 008 Chapter 1 overview and localized chapter chrome

Unit 008 is `chapter1.tex` lines 9--31 inclusive, from the Chapter 1 heading
through the complete reader-tip box, stopping before `子商`. Its stable ID is
`o014.aljabr2.chapter1.overview`. Preserve its six-item roadmap, all 25 source
references with verified partial-reader fallbacks, and citations `Li1`,
`KS06`, and `Rie16`. Localize the inherited Chinese chapter label, running
header, contents entry, and reader-tip title without modifying upstream
support files. Reflow the chapter title as a centered near-text-width box so
the Indonesian title is readable and page-filling rather than constrained by
the source-language geometry.

## D023 - Unit 009 production boundary

Unit 009 is the complete section `子商`, `chapter1.tex` lines 33--139
inclusive, stopping before `像, 余像和严格态射` at line 140. Its stable ID is
`o014.aljabr2.chapter1.subquotients`, with provisional Indonesian title
`Subkuosien`. Preserve the monomorphism/epimorphism recap, all definitions,
propositions, lemmas, proofs, diagrams, equations, index entries, and forward
reference to the later abelian-category corollary. The normalized-LF source
slice is 8,860 bytes, SHA-256
`3c1bcab75bb9b58f9b3d8c1ff3cf9ac84ecd77d75389f39c48d40dd8a76b5f8d`.

## D024 - Unit 009 admission and section-scoped counters

Admit Unit 009 on target SHA-256
`ede78ab615ad672a6655780041c70c07d9bfcc34ce54d7044e004c5437728a11`
and frozen 45-page checkpoint SHA-256
`bcdebbae4fc2f81a042c3732344811ba00b3ae347529fb68e3998d8379c450c1`.
The initial derivative wrapper omitted the upstream
`\numberwithin{equation}{section}` and `\numberwithin{figure}{section}` rules,
which would have rendered equation `eqn:coprod-prod-delta` as `(1.1)` instead
of `(1.1.1)`. Restore those rules in the derivative wrapper and localize all
reader-facing theorem/proof names without modifying the exact upstream class.
The final topology, numbering, build, structural PDF checks, and 45-page
visual inspection pass are recorded in `qa/UNIT_009_QA.md`.

## D025 - Unit 010 production boundary and strictness terminology

Unit 010 is the complete section `像, 余像和严格态射`, `chapter1.tex` lines
140--266 inclusive, stopping before `加性范畴: 核, 余核` at line 267. Its
stable ID is `o014.aljabr2.chapter1.images-coimages-strict`, with Indonesian
title `Citra, Kocitra, dan Morfisme Ketat`. The normalized-LF source slice is
8,700 bytes, ends in LF, and has SHA-256
`31b9d3e83fbad15efb4f5e9524afb1154ec50a0778498fa0deaa773cf18381bc`.
Preserve all definitions, lemmas, propositions, six proofs, nine diagrams,
eleven labels, references, indexes, and the epi--mono factorization category.
Use `penyama/kopenyama` for `\Ker/\Coker` of parallel pairs here, retain
`citra`, `kocitra`, `morfisme ketat`, and `faktorisasi epi--mono`, and do not
conflate the statement that every morphism is strict with the weaker notion
of a balanced category. The factorization category comes from a preorder, not
necessarily a partial order.

## D026 - Unit 010 admission and final-diagram reflow

Admit Unit 010 on target SHA-256
`a9ac206d5588dd9b23b1fc5216fd42dc5893f6d899488b25069668f8d55d73df`
and frozen 49-page checkpoint SHA-256
`365c17817b41cc17567698279abe942e5eacf3ae738743ea33244f86fc784e2f`.
The source encloses its final multiline TikZ-CD in inline math. Reflow that
unchanged diagram body as an unnumbered centered display: this removes the
tall baseline box, aligns it with the section's other diagrams, and changes no
arrow, formula, label, or counter. Independent mathematical/naturalness and
topology audits pass on the exact admitted target. Register source proof-clarity
observation O014-O001 without changing the source's construction or contacting
upstream.

## D027 - Unit 011 production boundary

Unit 011 is the complete section `加性范畴: 核, 余核`, `chapter1.tex` lines
267--567 inclusive, stopping before `推广: 交换环上的线性范畴` at line 568.
Its stable ID is
`o014.aljabr2.chapter1.additive-categories-kernels-cokernels`, with provisional
Indonesian title `Kategori Aditif: Kernel dan Kokernel`. The normalized-LF
source slice is 20,965 bytes, ends in LF, and has SHA-256
`55916070ed2f33eb3af08b01b589608d1344785c8e259aae77599dfc43ea2170`.
Translate the section contiguously and preserve every theorem-like block,
proof, diagram, formula, label, reference, index entry, and any exercise or
hint at its source position.

## D028 - Unit 011 disclosed corrections and presentation changes

Register two narrowly proven source corrections. O014-C005 changes the prose
description of `Z \dsqcup{Y} \Coker(f)` from an ordinary coproduct to the
fiber coproduct actually displayed and used by the dual proof. O014-C006
restores the missing hypotheses `fg=0` and `hf=0` in the kernel and cokernel
universal properties. Both corrections are disclosed in translator footnotes
and in `SOURCE_CORRECTIONS.csv`.

Reflow the two multiline adjunction TikZ-CD environments at source lines
284--286 and 376--378 from inline math to centered unnumbered displays. Their
diagram bodies and punctuation remain unchanged. Expand the source's five bare
MakeIndex shorthands (`\oplus`, image/coimage, and their symbols) to the
complete established display entries so the Windows fallback does not emit
literal or split index keys.

## D029 - Unit 011 admission and first use of myarrows

Admit Unit 011 on target SHA-256
`735277e6e0e469bee4929b2153f6931864d86609237344b7da217c77d724005e`
and frozen 58-page checkpoint SHA-256
`e72c2f71668b84382a24e57fd5001bd7b3cb5415229f82d9a45c9bd0f7b1b4f0`.
This is the first derivative unit that needs the upstream `myarrows.sty`, for
the source-native `\xlongequal`. Preserve its CC BY 4.0 header and borrowed-code
attribution, but save and restore the standard extendable-arrow commands after
loading it so earlier units do not undergo a retroactive layout change.

Independent mathematical, language, and topology audits pass. The final
reader has no error, unresolved reference, missing citation, or overfull box;
all 58 rendered pages pass visual inspection. The terminology and backend term
surfaces now agree on 238 unique concept IDs. Continue at `chapter1.tex` line
568 with the complete section on linear categories over a commutative ring.

## D030 - Unit 012 production boundary and exact slice witness

Unit 012 is the complete section `推广: 交换环上的线性范畴`,
`chapter1.tex` lines 568--629 inclusive, stopping before
`由函子观极限` at line 630. Its stable ID is
`o014.aljabr2.chapter1.linear-categories-over-commutative-rings`, with
Indonesian title `Perumuman: Kategori Linear atas Gelanggang Komutatif`.

The exact source witness joins the 62 selected line elements with LF. Because
line 629 is blank, that join already has a terminal LF: 5,540 bytes, SHA-256
`7dda28b5a53a9ff4568ffb3efe2edf927261f383b1b8b91b9ce2543aca948b0f`.
Discard the provisional 5,541-byte witness, which incorrectly appended a
second LF after the already terminal blank element. This is a provenance
correction made before admission, not a source-content change.

## D031 - Unit 012 admission and readable display reflow

Admit Unit 012 on target SHA-256
`b01b3d4582b4cf8db87a5bf4b11aea4abd01599df05fe10f59f69f4ab4f3bcc6`
and frozen 60-page checkpoint SHA-256
`b07c52b279c4a8e3da9be5331103e2f949396690f063ac9de9615137afaf841c`.
Preserve the distinction between a category enriched over
`$\Bbbk\dcate{Mod}$` and an additive `$\Bbbk$`-linear category, and
state the existence condition in Proposition 1.4.3(ii) specifically for
`$\varinjlim\alpha$`.

Reflow the source's inline adjunction diagram and its long inline equality in
the final proof as centered unnumbered displays. Introduce the first displayed
composition diagram with a colon so no punctuation is detached from the
sentence. These are presentation-only changes: every mathematical token,
arrow, label, and counter is preserved. Independent mathematical, topology,
language, frozen-build, structural-PDF, and 60-page visual checks pass. The
terminology surfaces agree on 247 unique concept IDs.

The stricter whole-backend containment pass exposed one inherited metadata
range in Unit 011: paragraph segment `p007` introduces and owns the
`compactitem` at source lines 332--335 but had been recorded as ending at
line 331. Extend only that parent segment's source end to line 335. The source,
translation, marker order, child ranges, and Unit 011 artifact hashes do not
change.

## D032 - Unit 013 production boundary

Unit 013 is the complete section `由函子观极限`, `chapter1.tex` lines
630--762 inclusive, stopping before `滤过归纳极限` at line 763. Its stable
ID is `o014.aljabr2.chapter1.limits-through-functors`, with provisional
Indonesian title `Meninjau Limit melalui Funktor`. Joining the 133 selected
line elements with LF already ends in LF because line 762 is blank; the exact
slice is 11,614 bytes, SHA-256
`01a42e16505d061567248e6b52a46e2f212a418065ee57f131087ef173e76561`.

The pinned source has two independently confirmed local defects in this
boundary: line 714 sends the constructed group homomorphism to
`$\varinjlim\beta$` although the entire construction and universal
property require `$\varprojlim\beta$`; line 724 duplicates `对` in
`对对每个`. Correct and disclose both in the derivative, then register exact
target locations in `SOURCE_CORRECTIONS.csv` before admission.

## D033 - Unit 013 third source correction and partial-reader reference

Independent audit finds a third mathematical codomain typo at source line
760. Proposition 1.5.7(i) concerns the forgetful functor
`$\mathcal{F}:\mathcal{C}^J\to\mathcal{C}^{\Obj(J)}$`; it therefore creates
`$\varinjlim\alpha$` in its domain `$\mathcal{C}^J$`, not in
`$\mathcal{C}$`. The proof itself constructs `$X:J\to\mathcal{C}$`, confirming
that the resulting object lies in the functor category. Register and disclose
this as O014-C009 alongside O014-C007 at line 714 and textual correction
O014-C008 at line 724.

The source's reference from Section 1.5 to the later comma-category example
at line 801 is verified as Example 1.6.3. Use
`\sourcecrossref{eg:comma-vs-cone}{1.6.3}` so this partial checkpoint contains
no broken forward link and the complete reader later resolves it normally.

## D034 - Unit 013 admission

Admit Unit 013 on target SHA-256
`d1e0f66183b95cf57bb092a2c40956fd7ce2374f860ab14d68e8dbca929bae57`
and frozen 66-page checkpoint SHA-256
`693a52fe0a54b14deac526b271381389a280c362a07c4e40e7f2664322dd59d2`.
The target preserves 50 stable segments, six lists with fourteen items, five
ordinary displays, three TikZ-CD diagrams, nine labels, three citations, four
index commands, and the exact comparison-arrow and naturality directions.

Independent mathematical, topology, and language audits pass. The final
frozen build has no error, unresolved reference, missing citation, overfull
box, or missing character; all 66 rendered pages pass visual inspection and
match the settled mutable build pixel for pixel. The backend now has thirteen
units and 467 segments. Both terminology surfaces contain the same 262 unique
concept IDs.

## D035 - Unit 014 production boundary

Unit 014 is the complete section `滤过归纳极限`, `chapter1.tex` lines
763--925 inclusive, stopping before `Kan 延拓` at line 926. Its stable ID is
`o014.aljabr2.chapter1.filtered-inductive-limits`, with provisional Indonesian
title `Limit Induktif Terfilter`. Joining the 163 selected logical line
elements with LF already ends in LF because line 925 is blank; the exact slice
is 13,190 bytes, SHA-256
`1d53f52915d245c2ef2e10da1aa15525f4341c3400be5585ae40eba08e451f8d`.

Translate and audit this section contiguously. Preserve every theorem-like
block, proof, diagram, equation, list, label, reference, citation, index entry,
exercise, and hint at its exact source position. Do not silently repair a
suspected source defect; register any proven correction before admission.

## D036 - Unit 014 source corrections and partial-reader references

Independent mathematical review confirms four defects in the pinned source.
Register and disclose O014-C010 through O014-C013. Require the object set of a
filtered category to be nonempty and consequently qualify the total-order
example as nonempty; type `k` as an object rather than a morphism; compose the
cofinality cospan through `k_0 -> k` so its apex actually lies in the full
subcategory `J`; and replace the erroneous outer inductive limit in the dual
finite-subcategory approximation by the projective limit indexed by
`OFin_I^opp`.

Use verified `\sourcecrossref` fallbacks for the later or out-of-order targets
Remark A.2.3, Appendix A, and Section 1.9. Reflow one long equality with
`aligned`, replace the diagram label `1:1` by the semantic isomorphism label
`\sim`, and use `\enlargethispage{2\baselineskip}` at the local section start
to eliminate a 21.13144pt overfull vbox. These presentation changes preserve
all mathematical tokens and have no counter or topology effect.

## D037 - Unit 014 admission

Admit Unit 014 on target SHA-256
`eba8da89fb2f1146ed3b881ac0099377f68e929d2c2f6a0ef6efd0a8aa8147f7`
and frozen 72-page checkpoint SHA-256
`24fef5c26c5877f7454fa90365bbca23ca09c51e841340310680bb13eb030daa`.
Independent mathematical, topology, language, and structural-readiness audits
pass. The final frozen build has no error, unresolved reference, missing
citation, rerun request, overfull box, or missing character; all 72 rendered
pages pass visual inspection and are pixel-identical to the settled mutable
build. The backend now has fourteen units and 518 segments. Both terminology
surfaces contain the same 274 unique concept IDs. The 35-row exact cumulative
manifest verifies every byte count and hash with zero mismatch.

## D038 - Unit 015 production boundary

Unit 015 is the complete section `Kan 延拓`, `chapter1.tex` lines 926--1140
inclusive, stopping before `以极限构造 Kan 延拓` at line 1141. Its stable ID
is `o014.aljabr2.chapter1.kan-extensions`, with Indonesian title `Ekstensi
Kan`. Joining the 215 selected logical line elements with LF already ends in
LF because line 1140 is blank; the exact slice is 20,013 bytes, SHA-256
`e522e1efc9a4103b701fafd4c0e2e2d7fa4a7c269f29296d67b7a68a5e64e7b9`.

The bounded audit finds two independently confirmed correction candidates:
line 1022 must conclude with `Ran_G(identity_D)`, matching the typed statement
at line 1016, rather than `Ran_F(identity_C)`; and the absolute-extension
definition must declare the category `F` before quantifying over a functor
`M:E->F`. Correct, disclose, and register both before admission. Preserve the
theorem label `prop:Quillen-adjunction-gen` literally. Preserve the ordinary
reference to `sec:limit-functor`, which already resolves live to admitted Unit
013; no partial-reader fallback is needed.

## D039 - Unit 015 corrections, terminology, and readable diagram reflow

Register and disclose O014-C014 and O014-C015. For an adjunction
`F:C->D`, `G:D->C`, the right-extension identification in the final sentence
of Example 1.7.5 must be `Ran_G(identity_D)`, as already typed correctly in
the same example, rather than the source's `Ran_F(identity_C)`. In Definition
1.7.6, quantify over category `F` before using it as the codomain of
`M:E->F`. Both interventions are local, independently checked, and recorded
with exact source and target locations in `SOURCE_CORRECTIONS.csv`.

Reflow the two source-inline multiline adjunction diagrams as centered
unnumbered displays. Preserve every TikZ-CD token, arrow, label, and
punctuation mark; this is a presentation-only change that prevents tall
baseline boxes. At first use, explain `funktor tarik balik` as the
precomposition functor. Add nine shared terminology concepts: natural
isomorphism, left and right Kan extension, precomposition functor, 2-category,
vertical and horizontal composition, pointwise Kan extension, and preservation
of a Kan extension.

## D040 - Unit 015 admission

Admit Unit 015 on target SHA-256
`37961cdf22d89b79c4e5a27405747c31bcc1a88149b7ed042c077a63b58550f0`
and frozen 78-page checkpoint SHA-256
`bc5f86b276f199d68f2a78e38067a19997dabafa97028fdd47c35dcf83a26459`.
The target preserves 67 stable segments, two definitions, two examples, one
proposition, one theorem, one remark, two proofs, eleven list items, thirty
TikZ-CD diagrams with 173 arrows, seven labels, six references, five citation
commands, four index commands, and three footnotes. The two new translator
notes disclose O014-C014 and O014-C015.

Independent mathematical, topology, Indonesian-language, and final
structural-readiness audits pass. The frozen build has no error, unresolved
reference, missing citation, rerun request, overfull box, or missing character;
all 78 rendered pages pass visual inspection and are pixel-identical to the
settled mutable build. The backend now has fifteen units and 585 segments.
Both terminology surfaces contain the same 283 unique concept IDs.

## D041 - Unit 016 production boundary

Unit 016 is the complete section `以极限构造 Kan 延拓`, `chapter1.tex`
lines 1141--1229 inclusive, stopping before `Gabriel--Zisman 局部化` at line
1230. Its stable ID is
`o014.aljabr2.chapter1.kan-extensions-as-limits`, with Indonesian title
`Konstruksi Ekstensi Kan melalui Limit`. Joining the 89 selected logical line
elements with LF already ends in LF because line 1229 is blank; the exact
slice is 8,131 bytes, SHA-256
`7553fbbc9b8c8d899344c94ea6e584d0ff5748a93ac4d4653fdebe9ff47a89b3`.

Translate and audit this section contiguously. Preserve its theorem, proof,
remark, example, two lists with six items, nine display blocks, six TikZ-CD
diagrams, five labels, all references and the `Li1` citation. Verify and, if
confirmed, disclose the locator typo at source line 1156, `Lemma 2.7,4`, as
`Lema 2.7.4` before admission. No exercise, hint, or external asset occurs in
this boundary.

## D042 - Unit 016 correction, segmentation, and final line repair

Register and disclose O014-C016: the pinned source's locator `Lemma 2.7,4`
is the local punctuation typo `Lema 2.7.4`. Preserve the draft's 35 coherent
segment markers rather than the earlier 26-record provisional map. The shorter
map conflated equation identities and omitted seven independently reusable
proof paragraphs; the canonical 35-record map restores exact marker order,
source ranges, equation wrappers, diagram nesting, and parent containment.

Independent comparison found two source-inline `\varinjlim` spans that the
first draft had rendered only as prose. Restore both literal mathematical
spans while retaining the Indonesian explanation. The first mutable build then
reported one 2.10254pt overfull hbox in the final proof paragraph. Shorten
`Bagian persegi ... bagian segitiga` to the equivalent `Persegi itu ...
segitiganya`; this changes no mathematical claim and produces a final build
with zero overfull box.

## D043 - Unit 016 admission

Admit Unit 016 on target SHA-256
`3840e35aa8ca85af05020b1134b7045d4f02420d3b0193951f67a4ead6837df7`
and frozen 82-page checkpoint SHA-256
`c7c78c481d1bd10964bb6f2d4dbb8dad70d869389f881eb9f12cc0f81e8307ba`.
The target preserves one theorem, one proof, one remark, one example, six list
items, three numbered equations, five bracket displays, one gathered display,
six TikZ-CD diagrams with 28 arrows, five labels, sixteen references, the
`Li1` citation, and one index command. All 35 stable segments have exact
target/backend parity and valid nested containment.

Independent mathematical, topology, Indonesian-language, final structural,
and full-size visual audits pass. The final build has no error, unresolved
reference, missing citation, rerun request, overfull box, or missing character;
all 82 rendered pages are pixel-identical between mutable and frozen builds.
The backend now has sixteen units and 620 segments, and both terminology
surfaces contain the same 286 unique concept IDs.

## D044 - Unit 017 production boundary

Unit 017 is the complete section `Gabriel--Zisman 局部化`, `chapter1.tex`
lines 1230--1582 inclusive, stopping before `沿局部化作 Kan 延拓` at line
1583. Its stable ID is
`o014.aljabr2.chapter1.gabriel-zisman-localization`, with Indonesian title
`Lokalisasi Gabriel--Zisman`. Joining the 353 selected logical line elements
with LF already ends in LF because line 1582 is blank; the exact slice is
28,032 bytes, SHA-256
`8d6063a530350e4dfda51c965c404983d53d469ca320b08e96b2b098970af9e0`.

Translate and audit the section contiguously. Preserve all 21 theorem-like
blocks, twelve proofs, five lists with thirteen items, 27 explicit displays,
26 TikZ-CD diagrams with 134 arrows, nineteen labels, all references, five
citation commands over four keys, eight index commands, one source footnote,
and both informal reader tasks. No formal exercise or hint occurs here.

Verify and, if confirmed, disclose two correction candidates. At source line
1255, `GG'` is the endofunctor on the primed localization and its identity must
therefore be `identity_{C[S^-1]'}`. At source line 1493, because `F` maps
`X,Y` to `FX,FY`, the fraction `(Fa)(Fs)^{-1}` lies in
`Hom_D(FX,FY)`, not `Hom_D(X,Y)`. The validated provisional backend map has
101 unique, source-ordered records and exact coverage of every label, unique
reference target, citation key, and diagram.

## D045 - Unit 017 corrections, link closure, and layout reflow

Register and disclose O014-C017 and O014-C018. In the uniqueness proof,
`GG'` is an endofunctor of the primed localization, so its identity is
`identity_{C[S^-1]'}`; the proposition immediately preceding the proof already
has this correct type. For the induced functor, `(Fa)(Fs)^{-1}:FX->FY` lies in
`Hom_D(FX,FY)`, not `Hom_D(X,Y)`. Both source repairs are minimal, mathematically
forced, and visible in translator notes.

The partial reader does not yet include Appendix A, so replace the otherwise
unresolved forward link `\\S\\ref{sec:GP}` by the exact static locator `Lampiran
\\S~A.3`. Preserve `sec:GP` as `source_xrefs` in the backend and restore a live
link when Appendix A enters the cumulative reader.

Move the two source-inline fraction diagrams and the wide additive Hom-set
formula into centered display wrappers. The diagram and formula bodies remain
unchanged. This removes all three mutable-build overfull boxes. Independent
review verifies exact source mathematics and topology modulo these disclosed
reflows, translated `text{...}` spans, and O014-C017/C018.

## D046 - Unit 017 admission

Admit Unit 017 on target SHA-256
`eb711edd0842ae6c2e1199d9d541f44f8a3ddc56a152c4f09d3671edabba52af`
and frozen 94-page checkpoint SHA-256
`6e99e9333bdac7df99c0d496231cfd352d41f6989e2e3dc3a899c54bb2209f30`.
The target preserves all 101 stable segments, 21 theorem-like blocks, twelve
proofs, thirteen items, 26 diagrams with 134 arrows, nineteen labels, five
citation calls over four keys, eight index commands, the source footnote, and
both informal reader tasks.

The clean frozen build exposed one stale term-index page reference in the
intermediate mutable PDF. Re-running the complete mutable index cycle corrects
it; all 94 final frozen and mutable renders are pixel-identical. The final log
has no error, unresolved reference, missing citation, overfull box, or missing
character. Full contact-sheet and full-size Section 1.9, bibliography, and
index inspection pass. The backend now has seventeen units and 721 segments.
At admission, the two terminology surfaces had exact parity over 296 concept
IDs; Unit 018 preparation immediately afterward raises the live count to 298.

## D047 - Unit 018 production boundary

Unit 018 is the complete section `沿局部化作 Kan 延拓`, `chapter1.tex` lines
1583--1707 inclusive, stopping before the next same-level section at line
1708. Its stable ID is
`o014.aljabr2.chapter1.kan-extensions-along-localization`, with Indonesian
title `Ekstensi Kan sepanjang Lokalisasi`. Joining the 125 selected logical
line elements with LF already ends in LF because line 1707 is blank; the exact
slice is 12,061 bytes, SHA-256
`5f229d0ba8c2ea8059f8d5146ff0cab31c7723692cda8f23123e72b94714de9f`.

Translate and audit this section contiguously. Preserve its three propositions,
one lemma, four proofs, two enumerations with five items, ten displays, eight
TikZ-CD diagrams with 42 arrows, five labels, 24 reference calls, and one
source footnote. There is no formal citation, index entry, exercise, hint,
figure file, or external asset in the boundary. The exact 33-record map is
`tmp/unit018-segment-map.jsonl`.

Verify and, if confirmed, disclose O014-C019 at source line 1599: the right
branch must target `C[S^-1]^r`, not `C[T^-1]^r`, because `T` is the induced
system on the subcategory `I`, while `S` is the localized system on `C`; the
left branch and the universal-property proof confirm the type.

## D048 - Unit 018 correction, forward link, and wording

Register and disclose O014-C019. The right branch of the induced localized
functor has codomain `C[S^{-1}]^r`, not `C[T^{-1}]^r`: `T` is defined on the
full subcategory `I`, whereas `S` is the multiplicative system on `C`. The
left branch and the following universal-property proof confirm this type.

The partial reader does not yet contain Chapter 4. Replace the otherwise
unresolved forward link `sec:triangulated-functor-localization` by the exact
static locator `\S~4.6`, retain the source xref in the backend, and restore the
live link when Chapter 4 enters the reader. Independent language review also
clarifies that the term `FX` in the relevant indexing category corresponds to
its identity object; this is an explicit Indonesian rendering of the source
relation, not an added mathematical claim.

## D049 - Unit 018 admission

Admit Unit 018 on target SHA-256
`64d032ac5b7a4ed02812aeb3addfba68177019f16e55dad046cbf2eba1f86d61`
and frozen 98-page checkpoint SHA-256
`1a724cd76acba0c1569456c443466cd8fb070721225bec8a1387d7c33147434e`.
The target preserves all 33 stable segments, three propositions, one lemma,
four proofs, five list items, ten displays, eight diagrams with 42 arrows,
five labels, 23 live reference calls, and the source footnote.

Independent mathematical, topology, Indonesian-language, final structural,
and visual audits pass. The final build has no error, unresolved reference,
missing citation, overfull box, or missing character; all 98 rendered pages
are pixel-identical between mutable and frozen builds. The backend now has
eighteen units and 754 segments, and both terminology surfaces contain the
same 298 unique concept IDs. The corrected 40-row manifest has zero file,
byte-count, or hash mismatches and SHA-256
`ffea232269edfa4910a773784b4ffe5fc77c385b859377045cd38ed7abe18872`.

## D050 - Unit 019 production boundary

Unit 019 is the complete section `伴随函子定理`, `chapter1.tex` lines
1708--2079 inclusive, ending exactly at the pinned Chapter 1 file boundary.
Its stable ID is `o014.aljabr2.chapter1.adjoint-functor-theorem`, with
Indonesian title `Teorema Funktor Adjoin`. Joining the 372 selected logical
line elements with LF does not add a terminal LF; the exact slice is 31,323
bytes, SHA-256
`98db944bbfa82a570cac62b57d4f30e262ff70bdc0daf5024d0535399360fed4`.

Translate and audit this section contiguously. Preserve three definitions,
five lemmas, one proposition, two theorems, two corollaries, three examples,
ten proofs, 44 list items including all seventeen chapter-end exercises and
ten hints, nineteen displays, fifteen TikZ-CD diagrams with 62 arrows,
seventeen labels, all references, thirteen citation calls, and six index
commands. The exact provisional map has 126 unique source-ordered records at
`tmp/unit019-segment-map.jsonl`.

Verify and, if confirmed, disclose O014-C020 at source line 1747: the
definition introduces category `E`, so the morphism test must use
`Hom_E(e,e')`, not `Hom_C(e,e')`. Until their targets enter the cumulative
reader, render the forward references at lines 1829, 1859, and 1929 as exact
descriptive static locators while preserving their source xrefs in the
backend.

## D051 - Unit 019 terminology and bibliography preparation

Add seventeen first-use terms to both terminology surfaces, with exact
preferred-form parity: weakly initial/terminal families and objects, solution
and cosolution set conditions, general and special adjoint functor theorems,
generating and cogenerating families, well-powered and well-copowered
categories, representable functors, Stone--Čech compactification, free groups,
free products, and amalgamated free products. Retain `well-powered` and
`well-copowered` as provisional international modifiers and define them
immediately in Indonesian at first use. The two surfaces now contain 315
unique concept IDs with zero duplicate or parity error.

Add the exact upstream `Xiong` bibliographic record needed by this boundary to
the mutable cumulative bibliography, preserving the Chinese author and title
and recording the fourth edition. The prepared bibliography has fifteen
entries, 4,622 bytes, SHA-256
`17226b63467faae7e7307d527f4277a5377fa8e0f3c2ff8458cbf3473118e2e0`.

## D052 - Unit 019 correction, partial-link closure, and admission

Register and disclose O014-C020. The weakly initial family definition has
introduced category `E` and objects `e,e'` of `E`; its morphism test therefore
uses `Hom_E(e,e')`, not the pinned source's undefined `Hom_C(e,e')`. The
Indonesian target makes the minimal correction and carries an explicit
translator note.

The three not-yet-live references are rendered as exact descriptive static
locators: the future Grothendieck-category section and the Yoneda density and
representable-functor material in Appendix A.1. Preserve their source xrefs in
the backend and restore live links when those targets enter the cumulative
reader. Reflow one long morphism and one two-diagram display into narrower
centered displays without changing their mathematical content. Localize the
byte-exact class's chapter-end exercise heading/bookmark and hint label to
`Latihan` and `Petunjuk` in the wrapper rather than editing `AJbook2.cls`.

Admit Unit 019 on target SHA-256
`a04c24934e745370ee6362215e7fe12ec449bc5c3adec3082212f7990b434afd`
and frozen 112-page checkpoint SHA-256
`256d59b339def9786edf72c15b45559a45f1c61d76f5d92950996f4eccffac43`.
Independent fidelity and topology reaudits pass over all 126 segments, 23
theorem-like blocks, ten proofs, 44 list items, seventeen exercises, ten
hints, nineteen source displays, fifteen diagrams with 62 arrows, seventeen
labels, 51 references, thirteen citations, and six index commands. The build
and visual audits pass with zero error, unresolved link, overfull box, or
missing glyph. The backend has nineteen units and 880 segments; both
terminology surfaces have exact parity over 315 concept IDs. The 41-row
manifest has zero mismatch and SHA-256
`1c1a750b64c232d82796612a7c322e83bca65329e0f24ce40d5972f8770177be`.

## D053 - Unit 020 boundary and terminology

Unit 020 is the Chapter 2 heading and complete overview, `chapter2.tex` lines
9--32 inclusive, stopping before `Abel 范畴的定义` at line 35. Its stable ID is
`o014.aljabr2.chapter2.overview`, with Indonesian title `Kategori Abelian`.
Joining the 24 selected logical source-line elements with LF does not add a
terminal LF; the exact slice is 4,921 bytes, SHA-256
`fe8aad79bbfe634abd2ae5680059f7ae714b8f890403aeec3acfe3a6cf5e986a`.

Preserve the overview's sixteen inline math spans, two ordered items, reading
tip, 21 cross-reference calls, two citations, one index command, and eleven
stable segments. Keep only the already-present `sec:cat-localization` target
as a live link; render the other twenty calls through exact static locators
until their targets enter the cumulative reader. Add fourteen exact-parity
first-use terms, including injective/projective objects, the snake and five
lemmas, Serre subcategories, composition series, `K_0`, exact categories, and
the Krull--Remak--Schmidt theorem. Both terminology surfaces then contain 329
unique concept IDs. Add the exact upstream `Bu10` bibliography record.

## D054 - Unit 020 corrections and admission

The first Unit 020 draft accidentally retained the upstream reading-tip
environment name and used the non-settled phrase `teknik Indisasi`. Correct
these before promotion to `petunjukbacaan` and `konstruksi Ind`. The first
build also exposed two accidental Unicode capital sharp-S characters in
section locators; replace them with the intended TeX `\SS`. These are
derivative-production repairs, not corrections to Li's source.

Admit Unit 020 on target SHA-256
`b53b2dfa38264ed51e46a1004864cd36d7ec7d5b4f0fbd9f215dad40a76f285c`
and frozen 116-page checkpoint SHA-256
`e080e4d6d912b36f3dbb2b0c3d5f00c00f97cbcef8eb550d2694b91ae90d99fc`.
Independent semantic, topology, structural-PDF, and visual audits pass. All
307 internal PDF links resolve, all 48 font rows are embedded, and all 116
mutable/frozen page renders are byte-identical. The backend has twenty unique
units and 891 unique segments; Unit 020's eleven target/map/backend records
match exactly. The 42-row manifest has zero mismatch, lists 14,718,229 bytes,
and has SHA-256
`d923cc32543b013417726a9a94f88128881d134cd688d40264158a52c8f8227b`.

## D055 - Unit 021 production boundary

Unit 021 is the complete section `Abel 范畴的定义`, `chapter2.tex` lines
35--115 inclusive, stopping before `初识复形` at line 116. Its stable ID is
`o014.aljabr2.chapter2.abelian-category-definition`, with Indonesian title
`Definisi Kategori Abelian`. Line 115 is blank, so the normalized slice ends
in LF: 81 logical source lines, 5,858 bytes, SHA-256
`52d5af389a06909c9c6d725827b29913affc73da22027b0e39ff138844ce5738`.

Translate and audit this section contiguously. Preserve one definition, two
remarks, three propositions, one corollary, four proofs, one compact list with
two items, one footnote, three display wrappers, three TikZ-CD diagrams with
arrow vector `2,4,4`, seven labels, sixteen reference calls, the `Li1`
citation, and one index command. All references resolve backward or within
the unit. The exact 25-record map is
`tmp/unit021-segment-map.jsonl`, SHA-256
`23151c734ea87cd8b08766dc4afc5388630ec2b5ebdf51fd6cc606c25425259a`.

## D056 - Unit 021 admission

Admit Unit 021 on target SHA-256
`5afd761701f6a28323e5ae4d39a2c1a47238eedf95d2afe0319ec1b705f1fbb8`
and frozen 118-page checkpoint SHA-256
`4a7fa3afa68ea77db4c570528e65f1fdb2ddbfbb52653517c12bb694e6e674af`.
The target is the independently audited draft plus the lane-standard terminal
LF. It preserves all 25 stable segments, 79 math spans, seven labels, sixteen
references, one citation, one index command, one footnote, three diagrams with
ten arrows, and the complete definition/proposition/proof structure. No source
correction or new unsettled term is required.

Independent semantic, topology, structural-PDF, and visual audits pass. All
328 internal PDF links resolve, all 48 font rows are embedded, and all 118
mutable/frozen page renders are byte-identical. The backend now has 21 unique
units and 916 unique segments; Unit 021's target/map/backend records match
exactly. The 43-row manifest has zero mismatch, lists 12,741,831 bytes, and has
SHA-256
`630823e1615bc3fb80e780d80f38ca9a7567ceae4b306a3ae768954c65159a71`.

## D057 - Unit 022 production boundary

Unit 022 is the complete section `初识复形`, `chapter2.tex` lines 116--292
inclusive, stopping immediately before `若干图表引理` at line 293. Its stable
ID is `o014.aljabr2.chapter2.first-look-at-complexes`, with Indonesian title
`Mengenal Kompleks`. The normalized-LF source witness is 13,796 bytes,
SHA-256
`f2ea791a1f33d1f3cc75d2a31041d56c1c80675b48201324b2401b4463cdd76c`.

Translate and audit this section contiguously. Preserve one lemma, three
propositions, four proofs, two definitions, one remark, one enumerate, one
itemize, one description list, one compact list, eleven list items, nineteen
display wrappers, ten TikZ-CD diagrams with arrow vector
`4,4,5,7,7,5,7,7,7,4` and 57 arrows total, ten labels, thirty reference
occurrences, and twelve index commands. There are no citations, footnotes,
exercises, hints, or external assets in this boundary.

The exact 58-record source-ordered map is
`tmp/unit022-segment-map.jsonl`, 17,714 bytes, SHA-256
`3374f78e7c7b6b5d8aa9e48afd41ce47e03361ef69a033d57252a14a0e6f1f99`.
Independent pre-admission review found that the provisional map had preserved
but failed to segment the display at source line 248. Add that display as
`q009`, shift the later local display IDs and sequences consistently, and
correct the remark topology from four to five displays before admission.
All references are backward or internal except `sec:Abel-cplx`, whose source
target is Chapter 3 line 946, and `prop:split-ses`, whose source target is
Chapter 2 line 786. Until those two targets enter the cumulative reader,
render exact descriptive static locators while retaining their source xrefs
in the backend; restore live links when the targets are admitted.

## D058 - Partial-release preservation routing and Unit 021 Zenodo lineage

On 2026-08-22 the user reported that GitHub had suspended the account after VPN
use and that a support ticket was open. Defer all GitHub publication attempts
until the account is restored; continue local production and use Zenodo as the
live preservation channel for verified partial boundaries.

Bounded anonymous and authenticated searches found neither a public O014
record nor a private O014 draft. Establish one non-duplicative lineage with
the clean title `Metode dalam Aljabar, Jilid 2: Aljabar Linear — Edisi Bahasa
Indonesia`, version `unit-021`, record 22059752, concept record 22059751, and
DOI `10.5281/zenodo.22059752`. The description leads with the work and exact
partial scope, explicitly says this is not the complete 650-page edition,
preserves CC BY 4.0 attribution and non-endorsement, and states the untagged
PDF accessibility boundary.

Publish six files: the byte-exact 118-page checkpoint; editable source/backend
ZIP; QA/provenance ZIP with private build-host paths removed from the public
log; README; release manifest; and SHA-256 sums. Both ZIP inventories were
verified entry-by-entry before upload. After publication, anonymously download
all six public files; every filename, byte count, Zenodo MD5, and SHA-256
matches local bytes. The DOI resolves with HTTP 200. Persist the sanitized
receipt at `release/zenodo/unit-021/ZENODO_PUBLICATION_RECEIPT.json`, SHA-256
`6d37e01c0b26d961cd3a2c8f760513768d433d878d243652ee8a03d08a8f9cb5`.
Future verified checkpoints must version this concept lineage rather than
creating duplicate records.

## D059 - Unit 022 admission

Admit Unit 022 on target SHA-256
`0e93c197b9d43bfa0afe67991dc24545e6109b745be743dd42ef6eca61618f01`
and frozen 124-page checkpoint SHA-256
`1d3a337ea9acd8b55bd8760206e964b467b9330c320db737c9fd93a4a7bbb5a2`.
The complete target preserves all 58 stable segments, 133 inline mathematical
spans, nineteen display wrappers, ten diagrams with 57 arrows, ten labels,
thirty source reference occurrences, twelve index commands, and the complete
lemma/proposition/definition/proof/list structure. The decreasing-index chain
complex notation `$(X_\bullet,d_\bullet)$` is explicitly present in the
admitted bytes. Two future source references render exact descriptive static
locators while retaining their source labels for later live-link restoration.

Independent semantic, topology, structural-PDF, and visual audits pass. The
provisional omission of a segment row for the source-line-248 display was
corrected before admission. All 357 internal PDF links resolve, all 50 unique
fonts are embedded and subset, and all 124 mutable/frozen page renders are
byte-identical. The backend now has 22 unique units and 974 unique segments;
Unit 022's target, corrected map, and backend records match exactly. The
45-row manifest has zero mismatch, lists 13,714,312 bytes, and has SHA-256
`60447cfce6739b5c46f1f47e6aaa06e8a2d03f824e862c9033677f53de4a8cc4`.

## D060 - Unit 022 dual-preservation checkpoint and metadata repair

Advance the existing Zenodo concept lineage, without creating a competing
concept, to record 22060130 and DOI `10.5281/zenodo.22060130`, version
`unit-022`. Its six-file payload includes the exact admitted 124-page reader,
editable source/backend, QA/provenance, README, manifest, and checksums. All
six public files were anonymously read back with exact filename, byte, MD5,
and SHA-256 parity. The metadata discloses the partial boundary, CC BY 4.0,
independent modification, non-endorsement, and untagged-PDF accessibility
limit.

An independent public audit found that the `isDerivedFrom` relation used the
nonexistent Gitee account slug `wenweili`. Correct it in place to the frozen
authority slug `wen-wei-li`; republish the metadata edit on the same record,
leave all six files unchanged, and anonymously prove that the old relation is
absent and the corrected link responds. Do not mint another Zenodo version for
this metadata-only repair.

Maintain one work-level Figshare item, article 33314775, in project 280296 and
the Indonesian collection. The first publication carried the full Zenodo
preservation payload; the corrected reader-first version 2 removes the bulky
QA/provenance archive from the latest surface and uses a compact six-file,
899,423-byte payload: PDF first, editable source/backend, standalone LICENSE,
README, manifest, and checksums. It retains exact CC BY 4.0, a truthful
Unit-022 partial-status statement, and links to the Zenodo version and concept.
The public article DOI is `10.6084/m9.figshare.33314775.v2`; the containing
collection was republished as `10.6084/m9.figshare.c.8668413.v21`. Anonymous
readback of every public file passes, and the whole 22-article project totals
21,007,790 bytes, far below its 20,000,000,000-byte cap.

## D061 - Unit 023 admission

Admit Unit 023 as the complete `若干图表引理` section, `chapter2.tex` lines
293--518, stable ID `o014.aljabr2.chapter2.diagram-lemmas`, on target SHA-256
`fc4111560e37ca303539416a84ab98504fd9168a50c040d9a998ac68d0e9bf34`.
Its exact 69-record map has SHA-256
`b8e5d95b5ec5465824aa84f624c987adb9b1beae0c44102ef2fc2a11356b641d`.
Independent semantic and topology audits pass all labels, references,
citations, indexes, equations, displays, list items, 21 TikZ-CD diagrams with
199 arrows, and both inline TikZ drawings. The only inline-math-span count
difference is a deliberate explicit composite
`S' \to X' \xrightarrow{\alpha} S`, not an omission.

The 132-page frozen checkpoint and promoted reader are byte-identical at
722,835 bytes, SHA-256
`43cb2ea687be2b8c40fd96c10d7863a0e89297452584b50b816517520cc92360`.
Biber resolves all seventeen keys; both indexes accept all entries; the final
log has no TeX error, unresolved citation/reference, rerun request, overfull
box, or missing character. All 397 internal links resolve. Every font is
embedded/subset. Full-page and detailed rendered inspection passes. The
backend now contains 23 units and 1,043 segments, with exact map/target parity.
The 51-row cumulative manifest has zero mismatch and SHA-256
`30d9cffd774e25effdc665adc3637796fd56b54eb5b5c82a248888d2c87eafac`.

## D062 - Restore GitHub publication and prove public bytes

After the user reported GitHub reinstated, create the corpus-specific public
repository `KokunoYumeto/metode-aljabar-jilid-2-id`. Publish a reader-first
Unit-023 boundary: the admitted PDF, all 23 unit sources and required XeLaTeX
support, cumulative bibliography, modular backend, CC BY 4.0 license, source
authority/component rights, terminology/corrections, build baseline, QA,
manifest, and checksums. Exclude build trees, renders, caches, superseded
wrappers/bibliographies, raw authority dumps, private task controls, and
credentials. Mark the scope as partial and the PDF as untagged; preserve exact
attribution, modification notice, and non-endorsement.

The first credential-free commit-archive audit detected Git line-ending
normalization in the root license and checksum files. Add canonical LF
attributes and regenerate the manifest/checksums rather than accepting a
content-equivalent hash mismatch. Final branch `main` commit
`936a95c60610e9f03cebfb5f08fc38e1721617ac`, tree
`58db1c00aa1a8f67dbf5e7c87a3daaaee31e5a65`, passes a second anonymous audit:
repository page, raw README, and raw PDF return HTTP 200; all 50 files and
1,680,574 bytes match the public commit archive; all 48 manifest payload rows
match; the PDF retains admitted SHA-256
`43cb2ea687be2b8c40fd96c10d7863a0e89297452584b50b816517520cc92360`.
GitHub detects CC BY 4.0 and exposes the intended discovery topics. Persist the
sanitized receipt at `release/github/GITHUB_PUBLICATION_RECEIPT.json`, SHA-256
`162fbf59d4e5401f59c1bd673ccbe83e00d44ee7815efd48f929d8acf2a8ac7c`.
Do not create a Release or Pages deployment merely to duplicate the committed
reader; keep the repository current at materially verified boundaries.

## D063 - Unit 024 admission and three disclosed order corrections

Admit Unit 024 as the complete `格论一瞥` section, `chapter2.tex` lines
519--720, stable ID `o014.aljabr2.chapter2.glimpse-of-lattice-theory`, on
target SHA-256
`e532e2e0f674b97d69fb5d94127d41b51273ffd35e555fcb6e1a8391b0f8cf3c`.
Independent semantic and structural audits pass all 64 segments, sixteen
labels, sixteen references, two citations, seventeen indexes, five diagrams
with fifteen arrows, seven list items, and the complete environment/display
topology.

Correct and visibly disclose three internally proven source inconsistencies:
O014-C021 restricts the Schreier-factor permutation to `{0,...,r-1}` and
`0<=i<r`; O014-C022 weakens `a<b` to `a<=b` in the composition-series
definition so its asserted zero-length case exists; O014-C023 reverses the
interval/end assignments for a descending pair to `[y_{i+1},y_i]`,
`y_{i+1}=a`, `y_i=b`. Reverse-applying only these three disclosed blocks
recovers the pre-correction target byte-for-byte, proving no unrelated
translation change.

The final clean build is 140 pages and 754,103 bytes, SHA-256
`f7633cfd5783af30c464d2a04008cd5d1881f6ad2a375fce8aae3a53e74fcf97`.
A source-neutral line break after the full Schreier theorem header eliminates
the only provisional overfull box. The final log has no error, unresolved
reference/citation, rerun request, overfull box, or missing character. All 420
internal links resolve; all fifty fonts are embedded/subset. Full renders and
original-resolution inspection pass. The backend now contains 24 units and
1,107 segments; both terminology surfaces contain 347 matching IDs. The
54-row exact manifest lists 18,198,242 bytes, has zero mismatch, and SHA-256
`36bdbb60ea2ba62e6fe3bd833f4cf360ab78da47eca99718fc1233ca1ac59953`.

## D064 - Advance the public GitHub edition through Unit 024

Advance the existing repository rather than creating a duplicate. Commit
`598ca94f8772d7eb1598dbd9748f5c61d2d8fd8f`, tree
`455640771ca6229899f208df7475b2d4d57a80c4`, replaces the public reader with
the admitted 140-page Unit-024 PDF, adds Unit 024 and the updated backend,
corrections, terminology, build baseline, QA, and cumulative manifest, and
keeps the payload compact by replacing the current-surface Unit-023 QA files
(which remain available in Git history).

Credential-free page, raw README, and raw PDF reads return HTTP 200. The
public commit archive contains 51 files and 1,762,578 bytes; every file matches
the local committed byte stream, all 49 payload-manifest rows pass, and the raw
PDF has exact admitted SHA-256
`f7633cfd5783af30c464d2a04008cd5d1881f6ad2a375fce8aae3a53e74fcf97`.
Persist the sanitized receipt at
`release/github/GITHUB_PUBLICATION_RECEIPT.json`, 2,507 bytes, SHA-256
`0b3fac71615ef0d4550054318a9e49a0461b4ce69d43ecfa74294ade37aae7a2`.

## D065 - External Indonesian field-terminology QA and model disclosure

At the Unit-024 safe boundary, run the requested bounded terminology check
before admitting more translation. The official arXiv exact search for
`"Bahasa Indonesia"` returns seventeen records, none in the relevant
mathematical field; exact searches for `"aljabar homologi"` and `"kategori
abel"` return none, and bounded target-term probes yield no admissible
Indonesian category/module/homological-algebra source with downloadable TeX.
Use the instructed non-arXiv fallback rather than extending the search loop.

Inspect all four pages of Gustina Elfiyanti's 2020 ITB doctoral front matter
for *Kajian Kategori U-Kompleks dan Kategori U-Kompleks Lemah* (126,507
bytes, SHA-256
`8e56993c4abcac3d7f89c9bb948e9d9925de6eef8b3102121c530e43ed8f19be`)
and all twelve pages of Ryan Kasyfil Aziz's 2012 ITB Chapter 2, “Aljabar,
Modul, dan Kategori” (435,907 bytes, SHA-256
`196d921577e7ba9f2508d8e1cc5be434061a8e1f40c71f8f7adcf643f00c2c1c`).
Treat both as restricted local terminology evidence only; never include their
PDF bytes in a public payload.

The witnesses confirm `gelanggang`, `modul`, `jumlah langsung`, `dekomposisi
jumlah langsung`, `modul projektif`, `barisan eksak`, `kategori aditif`, and
`Lema Ular`. They attest alternatives `aljabar homologi`, `rantai kompleks`,
`kategori abel`, `kategori tersegitigakan`, `kategori bentukan`,
`homomorfisma penghubung`, `morfisma`, `fungtor`, and `tak terdekomposisi`.
Retain the current preferred forms because they are mathematically precise,
coordinated with O013, and internally consistent; register the attested
alternatives as variants. Do not identify the witness's `segitiga eksak` with
this edition's `segitiga terbedakan` without stronger conceptual evidence.
No prose replacement in admitted Units 001--024 is justified.

Persist the complete audit at
`controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`. Add the exact production-model
disclosure **OpenAI Codex gpt-5.6-sol, Ultra** to edition/repository provenance
without displacing Wen-Wei Li's authorship, the user's human direction, witness
authors/supervisors, component credits, license obligations, or
non-endorsement.

Publish only the audit, glossary refinements, rights note, and model disclosure
to the existing GitHub edition; do not publish either restricted witness PDF.
Final branch `main` commit
`d60c9d1ffb50244915e370d68208368700c10363`, tree
`b246a436b1cdbfce5b4f8355ca7a526af6c40005`, passes credential-free readback:
all 52 tracked files and 1,772,058 bytes match the commit archive, all 50
manifest rows pass, the terminology audit and model identification are public,
and the unchanged 140-page reader retains SHA-256
`f7633cfd5783af30c464d2a04008cd5d1881f6ad2a375fce8aae3a53e74fcf97`.
The sanitized receipt is `release/github/GITHUB_PUBLICATION_RECEIPT.json`,
3,137 bytes, SHA-256
`ede8d23766cb7fbf6742e6a22f7db6ebf4e42e669f0732a62d19f8a0ffc3b2cb`.

## D066 - Unit 025 admission, portable bibliography, and public-name hygiene

Admit Unit 025 as the complete `直和分解` section, `chapter2.tex` lines
721--910, stable ID
`o014.aljabr2.chapter2.direct-sum-decomposition`, on target SHA-256
`1d03a870340625913fedd6b399c7ceeef5cf7819ee7c454856e0102dcedf0dc4`.
Independent semantic and structural audits pass all 67 segments, ten labels,
ten references, nine citations, nine indexes, five diagrams with 24 arrows,
fifteen list items, and the complete theorem/proof/display topology. The two
additional display blocks are source-faithful layout reflows of long formulas.

Correct and visibly disclose O014-C024: source line 800 reverses the direction
of `r` despite condition (ii), the equation `rf=identity`, and the subsequent
factorization all requiring `r:X\to X'`. The correction ledger and target note
now share the exact target locator, lines 182--185. No upstream contact is
made.

For portable visual output, retain exact Chinese bibliography metadata in
source comments and render verified Hanyu Pinyin fields where local Adobe-GB1
maps are unavailable. This changes presentation only, not cited-work identity.
Replace the awkward provenance-page URL break with two centered clickable
labels. Remove the directing person's personal-name token from every current
public-facing edition surface while retaining the role as `the user`/`pengguna`
and preserving all source, witness, component, and human-contributor credits.

The final 146-page checkpoint and promoted cumulative reader are byte-identical
at 771,201 bytes, SHA-256
`71f099e10d84e7d4f8c28756aba81c8ec82ca68a7f2d07df6cc168456efb5709`.
The clean build has no TeX error, unresolved reference/citation, rerun request,
overfull box, or missing character. All 444 internal links resolve; every font
is embedded/subset. Fresh full-document renders and detailed Unit 025,
provenance, and bibliography inspection pass. The backend now contains 25
units and 1,174 segments; both terminology surfaces contain 358 matching IDs.
The exact 56-row manifest lists 22,830,302 bytes with zero mismatch and has
SHA-256
`c253a6af5d63f7c2ba8c455affdf81060c90bee77dfd7eae7bb269bc8539aad4`.

Freeze Unit 026 at `chapter2.tex` lines 911--1132, stable ID
`o014.aljabr2.chapter2.subobjects-and-isomorphism-theorems`, and continue in
source order. This is a production checkpoint, not pursuit completion.

## D067 - Advance and verify the public GitHub edition through Unit 025

Advance the existing reader-first repository rather than creating a duplicate.
Commit `8f5333773e6103f917a4afaf93f84cf80a241630`, tree
`f64bb86429407be4193b433136da619d12828a62`, publishes the admitted 146-page
reader, Unit 025 source, 25-unit/1,174-segment backend, 358-row terminology,
O014-C024 disclosure, current external terminology audit, portable
bibliography, exact model note, build baseline, Unit 025 QA, and checksums.
The obsolete current-surface Unit 024 QA/manifest remain recoverable in Git
history and are replaced by their Unit 025 successors.

Before commit, rebuild the public source with XeLaTeX/Biber/MakeIndex. It
produces 146 pages with no error, unresolved reference/citation, overfull box,
or missing character; all 146 pages are pixel-identical to the admitted reader
at 50 dpi. Normalize every public text file to LF so the working bytes, Git
index blobs, manifest, and archive agree exactly.

Credential-free repository-page, raw README, raw PDF, GitHub API, and immutable
commit-archive reads pass. The archive contains all 53 tracked files and
1,841,205 bytes with zero mismatch; all 51 manifest/checksum payload rows pass;
the PDF is exactly 771,201 bytes with SHA-256
`71f099e10d84e7d4f8c28756aba81c8ec82ca68a7f2d07df6cc168456efb5709`.
GitHub identifies CC BY 4.0. The restricted terminology witnesses, prohibited
personal-name token, umbrella-project prose, private paths, and credentials are
absent. Persist the sanitized receipt at
`release/github/GITHUB_PUBLICATION_RECEIPT.json`, 3,490 bytes, SHA-256
`cd97ac2f86f5584f8cdfffb589f1abf7ea3f91a0eef6b00ded3b7839495d3bc1`.

## D068 - Unit 026 admission and cumulative reader

Admit Unit 026 as the complete `Subobjek dan Teorema Isomorfisme` section,
`chapter2.tex` lines 911--1132, stable ID
`o014.aljabr2.chapter2.subobjects-and-isomorphism-theorems`. The normalized
authority slice is 15,939 bytes, SHA-256
`85f25b07bbf35565c56e1f64ddb33c0a00ae79b1f60e3bb0aeb39ca982cccda8`; the
62-record map is 21,112 bytes, SHA-256
`79144b8d751fc35c6c177f4b24595388fe1f117239277431eb0d2310483a08bb`.
The target is 24,624 bytes, SHA-256
`52e87d044ba6a645a5c98329832fdb06272ce15106422c13ac402c75a67e200c`.

The source audit identified O014-C025 (unprimed family declarations used with
primed formulas) and O014-C026 (the source calls an `Image` object a
coimage); both are corrected and disclosed in the target and
`controls/SOURCE_CORRECTIONS.csv`. The target-fidelity audit additionally
repaired three markup/antecedent slips before admission. Structural parity
passes: 62 markers, 11 labels, 28 source references, two citations, six
indexes, 18 TikZ-CD diagrams/98 arrows, seven list items, and seven proofs;
there are no exercises or hints.

The clean shell-escape-disabled XeLaTeX/Biber/MakeIndex replay in
`build/cumulative-unit-026-finalB-20260823` produces a 152-page PDF,
807,443 bytes, SHA-256
`1895b07aad71009c4c1d6594120d6f8f47694b751551aff3c1e1cbb3b4c31ed9`.
There are no fatal, TeX, unresolved-reference, citation, rerun, overfull-box,
or missing-character errors; ten underfull hboxes and six underfull vboxes,
plus the known MiKTeX/biblatex/imakeidx non-fatal warnings, remain recorded.
All affected pages 139--152 were rendered and visually inspected. The
checkpoint and cumulative PDFs are byte-identical. QA receipt:
`qa/UNIT_026_QA.md`, 7,491 bytes, SHA-256
`2bb2a8d1c3a352ba68f5adb9d5f02a7ca9a4de5352c6ff724b2aff33db0c2abf`.
The 53-row exact manifest is
`qa/CUMULATIVE_UNIT_026_FILE_MANIFEST.csv`, 7,076 bytes, SHA-256
`f78c35eea3f2a52ecc9d64a5f7310d158377774d30d8d2b8fcd33a65411c096d`.

Continue source-order production; this is not corpus completion.

## D069 - Figshare Unit 025 public mirror verification

The existing work-level Figshare item (article 33314775) was advanced to
public version 3 without creating a duplicate. DOI:
`10.6084/m9.figshare.33314775.v3`; license: CC BY 4.0. The reader-first
payload has seven public files totaling 1,034,298 bytes, with the PDF first.
A bounded anonymous public-API/download check passed for all seven filenames,
sizes, and SHA-256 values; project 280296 and Indonesian collection 8668413
both publicly contain the article. The exact file inventory and hashes are
recorded in the sanitized release receipt to be updated at the next release
boundary. No credentials or signed-in browser state were used for the
readback.

## D070 - Unit 027 admission and checkpoint readiness (2026-08-23)

Admit `o014.aljabr2.chapter2.simplicity-and-semisimplicity` as the complete
source-order section `chapter2.tex` lines 1133--1244. The normalized authority
slice is 8,321 bytes, SHA-256
`e2f435c542379cd0f924343bd552514be261d8827dfa53afd107e20722ec213b`; its
38-record segment map is 11,184 bytes, SHA-256
`5d821f28602c5c7f40bfcb6569ccdf68f6aaac14bc9a5161a333d08f420d4fe6`. The
translated target is 13,458 bytes, SHA-256
`bcf83b6829f1ea4fcd4a712e19f4c7f1402ed0990565aad2b6c5055fbe97cf66`.

Structural review preserved all 38 stable markers, six labels, thirteen
references, two citations, eleven index commands, one footnote, six proofs,
and all display/environment topology. The section has no exercises, hints,
figures, or assets. Terminology uses the settled forms `objek sederhana`,
`objek semisederhana`, `objek terbelah`, `faktor komposisi`, `multiplicitas`,
and `gelanggang pembagian`; no new upstream correction was confirmed. A
sourcecrossref fallback was retained for the intentional forward reference to
`sec:Grothendieck-cat`. The Jordan--Hölder heading was shortened for fit and a
local line-breaking adjustment was limited to presentation.

The clean shell-escape-disabled XeLaTeX/Biber/MakeIndex replay in
`build/cumulative-unit-027-final-20260823` produced the byte-identical
checkpoint and cumulative reader: 157 pages, 823,894 bytes, SHA-256
`04af446ade23411da0a59a5f6a9f526b0267ddfe104c24e8fdedc0ad0583a6e0`.
There are no fatal, TeX, unresolved-reference, citation, rerun, overfull-box,
or missing-character errors; sixteen underfull boxes and known non-fatal
MiKTeX/biblatex/imakeidx warnings remain recorded. Physical pages 147--150
were rendered at 180 dpi and visually inspected. QA receipt:
`qa/UNIT_027_QA.md`, 7,019 bytes, SHA-256
`165ca2cb47cc6670c76154743e91b94a5323eb9d4ba8a3a01ea816b2d1ba2145`.

The backend now has 27 units and 1,274 segments; both terminology surfaces
have 375 matching rows. The next exact cursor is `chapter2.tex` line 1245,
`sec:inj-proj` (`正合函子, 内射对象和投射对象`); freeze its source slice and
map before translation. Unit 026 remains the latest public GitHub and Zenodo
boundary (GitHub commit `ba61089654d8df894111cd8ac9699d3ea280bf52`; Zenodo
record `22070867`, DOI `10.5281/zenodo.22070867`). Unit 027 is ready for the
next authorized advancement of those existing lineages; no duplicate record
or upstream contact is permitted.

## D071 - Unit 027 GitHub preservation (2026-08-23)

The existing edition repository was advanced, not duplicated, through the
Unit 027 boundary. Public `main` commit is
`3b0ec2283199f58fd5078c8cbb07410c34077329`, tree
`3d0554f2ebb37663124c4f8c68844c3179a41048`. The anonymous commit/archive
readback passed: 64 files, 62 manifest rows, archive 1,147,288 bytes,
SHA-256 `e81e8a7c1e3eaab4ada0bbc610dedd1e77f8d1e8dc7a8e7881adf3dad1cbd282`,
zero missing/unexpected/hash mismatches. The public reader is 157 pages,
823,894 bytes, SHA-256
`04af446ade23411da0a59a5f6a9f526b0267ddfe104c24e8fdedc0ad0583a6e0`.
Receipt: `release/github/GITHUB_PUBLICATION_RECEIPT.json`. Zenodo and
Figshare Unit 027 advancement remain pending their anonymous readbacks.

## D072 - Unit 027 public preservation (2026-08-23)

The existing GitHub edition lineage now contains Unit 027 at commit
`3b0ec2283199f58fd5078c8cbb07410c34077329`, tree
`3d0554f2ebb37663124c4f8c68844c3179a41048`; the anonymous archive/readback
passed with 64 files, 62 manifest rows, and zero mismatches. The existing
Zenodo concept lineage now has clean latest record 22071108,
`https://doi.org/10.5281/zenodo.22071108`, version `unit-027`, exactly seven
files totaling 1,130,179 bytes; every public byte/hash readback passed. The
correct PDF is 157 pages, 823,894 bytes, SHA-256
`04af446ade23411da0a59a5f6a9f526b0267ddfe104c24e8fdedc0ad0583a6e0`.
Receipts are `release/github/GITHUB_PUBLICATION_RECEIPT.json` and
`release/zenodo/unit-027/ZENODO_PUBLICATION_RECEIPT.json`.

An intermediate same-lineage Zenodo record 22071092 was accidentally
published with ten inherited files. One bounded deletion-request attempt was
made; Zenodo left it `done` and does not permit deletion through the deposit
API. It is explicitly marked residual/superseded in the Zenodo receipt; no
further retries are authorized. Figshare was not mutated: its account API
returned 403 `InactiveAccount`, article lookup returned 404, and the web
surface was degraded. The verified seven-file local payload and blocker
receipt are retained at `release/figshare/unit-027/FIGSHARE_PUBLICATION_RECEIPT.json`
(3,245 bytes, SHA-256
`7e6e3dd7f14fc2bb6960608edcc135cf5806292f08994c6de313a593fdac1044`).

## D073 - Unit 028 admission and reader checkpoint (2026-08-23)

Admit `o014.aljabr2.chapter2.exact-functors-injective-projective-objects` as
the complete source-order section `chapter2.tex` lines 1245--1563. The
normalized authority slice is 24,797 bytes, SHA-256
`e6e50b76ae9dcd59f739e00b89347c0a0a05c303a6fff56934018301cd275d63`; its
113-record segment map is 39,367 bytes, SHA-256
`0dfbfa43a29313cd1b3a57a9b72b64c2d668889e369605dd2709164688c6b9d8`. The
translated target is 37,694 bytes, SHA-256
`cd2f4bc1d7c2d4912650db33a934f9571f7a018d409a617fef4e61033d293a85`.

Structural review preserved the 113 stable markers, 19 labels, six citations,
six index commands, 17 TikZ-CD environments, and 21 display environments.
The sole conventional-reference difference is intentional: the source's
forward `sec:derived-primer` reference is represented by the local
`sourcecrossref` fallback to printed section 3.12. O014-C027 is disclosed in a
translator footnote. No exercises or hints occur in this section. The backend
now has 28 units and 1,387 segments; terminology has 382 matching rows.

The clean shell-escape-disabled XeLaTeX/Biber/MakeIndex replay in
`build/cumulative-unit-028-final-20260823` produced the byte-identical
checkpoint and cumulative reader: 167 pages, 868,564 bytes, SHA-256
`78c1ec3db75a97f3593d91412a8fbd19057d821df200cbc2893641dff5c48a43`.
There are no fatal, TeX, unresolved-reference, citation, rerun, overfull-box,
or missing-character errors; seventeen underfull boxes and known non-fatal
MiKTeX/fontspec/biblatex/imakeidx warnings remain recorded. Physical pages
153--167 were rendered and visually inspected. QA receipt:
`qa/UNIT_028_QA.md`, 5,070 bytes, SHA-256
`df6282afeae47aa0f3cb81be82b88a9a9a47fedcad6c223b131e637b0b7e8faf`.

The 67-row exact checkpoint manifest
`qa/CUMULATIVE_UNIT_028_FILE_MANIFEST.csv` lists 6,395,650 bytes, is 8,554
bytes, and has SHA-256
`4594c6510d46ab84568945035b503436624786d4df49ad2340d3cd0986b424e`; the
verification pass found zero missing or byte/hash mismatches. Mutable pursuit
controls are excluded from this snapshot and remain durable in their own
hashed control files.

## D074 - Unit 028 public lineage advancement (2026-08-23)

The existing GitHub edition repository was advanced, not duplicated, through
Unit 028 at public `main` commit
`c24ae8b406ef6b12ffd30275779c6ee293516888`, tree
`046d93c76ac12e2b84a66ae1db90636ea34dece1`. The reader is 167 pages, 868,564
bytes, SHA-256
`78c1ec3db75a97f3593d91412a8fbd19057d821df200cbc2893641dff5c48a43`.
Anonymous archive/readback passed with zero missing, unexpected, or hash
mismatches; the sanitized receipt is
`release/github/GITHUB_PUBLICATION_RECEIPT.json`, 3,015 bytes, SHA-256
`1aacb7327f4fdd23f0a0be6c79ef739b514602ac8ee87e4a58b763a77ada642d`.

The same Zenodo concept lineage (`22059751`) now has clean latest record
22071584, DOI `10.5281/zenodo.22071584`, version `unit-028-corrected-2`.
Its seven reader-first files total 1,187,667 bytes; anonymous downloads match
every local byte and SHA-256, and the DOI resolves with HTTP 200. The README
contains the exact upstream commit/tree, `Funktor`, and 382 terminology rows;
the sanitized receipt is
`release/zenodo/unit-028/ZENODO_PUBLICATION_RECEIPT.json`, 6,192 bytes,
SHA-256 `0600974fedb5091dcec687aa60e20b260b9474b8238a9715d35394d04476cca3`.
Same-concept records 22071302 and 22071377 remain documented as superseded
residuals; no deletion attempt or competing concept was made. Figshare was not
mutated.

The next exact cursor is `chapter2.tex` line 1564, `sec:Serre-subcat`
(`Serre 子范畴和 \texorpdfstring{$\mathrm{K}_0$}{K0} 群`). Its exact slice
and segment map are now frozen, and Unit 029 translation is in progress. This
checkpoint does not complete the corpus.

## D075 - Unit 029 admission and reader checkpoint (2026-08-23)

Admit `o014.aljabr2.chapter2.serre-subcategories-and-k0-groups` as the complete
source-order section `chapter2.tex` lines 1564--1754. The normalized authority
slice is 17,301 bytes, SHA-256
`45f958e6627cb4cef919dbd1fd5bc478b68c5d6c706dac47b69dd4d6dbd40aba`;
the translated target is 25,425 bytes, SHA-256
`6cfc81b8d1dc52ed685971c9dd4d81471e8978b58d8c682be60a5ef1f97d2b81`;
and its 61-record map is 19,962 bytes, SHA-256
`ec804f816cde5005f626110f65bf4dd7db928c6fc2ab040cfc36ad809f7ae4e2`.
Two independent reviews passed marker/order, mathematical, reference,
citation, environment, display, diagram, index, encoding, and naturalness
checks. O014-C028 and O014-C029 are accepted and disclosed at point of use.

The pre-existing Indonesian field-terminology gate remains satisfied by the
bounded arXiv negative result and the two directly inspected ITB fallback
witnesses in `controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`. No bulk replacement
was justified. Unit 029 registers `subkategori Serre lemah`, `kerangka kecil`,
and `modul torsi-S`, bringing both terminology surfaces to 385 matching rows.
The edition and repository retain the exact production-model disclosure
`OpenAI Codex gpt-5.6-sol, Ultra` without displacing source or human credits.

The first build exposed a missing cumulative bibliography record for `Lai19`.
Older snapshots were preserved; the new Unit-029 snapshot adds the exact
source identity in readable Hanyu Pinyin display form. Final Biber resolves all
19 citekeys. The shell-escape-disabled XeLaTeX/Biber/MakeIndex replay in
`build/cumulative-unit-029-finalB-20260823` produces a 175-page, 902,840-byte
PDF, SHA-256
`bfda39c9f834643f024dd2c7d9c16e341c8736b40f3bfa6dcc9d1646b6d6bd25`.
Final logs have no TeX, citation, reference, rerun, overfull, or missing-glyph
error; seventeen underfull warnings remain. Physical pages 160--175 passed
visual inspection. QA receipt `qa/UNIT_029_QA.md` is 7,276 bytes, SHA-256
`60006df36bb0e8622870886fcf2286f4e776d7894a9772d22ec99e9590333d55`.

The 64-row manifest `qa/CUMULATIVE_UNIT_029_FILE_MANIFEST.csv` lists 5,609,913
bytes, is 8,042 bytes, SHA-256
`ec69439286262800cd2ec6dd830ae21fd968508ccd67c703f3e6798715ccb40d`,
and verifies with zero missing or mismatched entries. The next source cursor is
`chapter2.tex` line 1756, `sec:Grothendieck-cat`; its exact section boundary is
under source audit. This checkpoint does not complete the corpus.

## D076 - Unit 029 public lineage advancement (2026-08-23)

Advance the existing GitHub edition repository, not a new repository, through
Unit 029 at public `main` commit
`7c99d2a6af0b55e00aa3b42959ce014db482ab62`, tree
`6884cf2df9d9fb45e2186201f59837ee3dc6fb32`. The immutable 71-file archive is
1,270,661 bytes, SHA-256
`cdf937fccf1c1e102203784363625cf5d27382664a886cb5ce7e2616ef4cf793`.
Anonymous repository, commit, raw-file, archive, manifest, checksum, source
closure, and 175-page reader verification passed with zero mismatch. The
sanitized receipt is `release/github/GITHUB_PUBLICATION_RECEIPT.json`, 4,669
bytes, SHA-256
`c3a612a1b14338f0dd7db60ac399befe6251981cd23ebd76ab1906a458a1872f`.

Advance the same Zenodo concept lineage 22059751 from prior record 22071584 to
record 22071903, DOI `10.5281/zenodo.22071903`, version `unit-029`. The
reader-first seven-file payload totals 1,237,689 bytes. Every anonymous file
download matches local bytes and SHA-256; record, DOI, API, and concept-latest
readbacks all return HTTP 200. The 45-entry source/backend ZIP includes all 29
source inputs, 1,448 segments, 385 terms, and the exact referenced bibliography;
the 14-entry QA/provenance ZIP contains no restricted witness. Metadata retains
the exact title, CC BY 4.0, Indonesian language, source/non-endorsement credits,
one organization contributor entry, and the exact production-model note,
without organization branding in title or descriptive prose. Receipt
`release/zenodo/unit-029/ZENODO_PUBLICATION_RECEIPT.json` is 5,910 bytes,
SHA-256
`9d0aa36d98979cf5cb02838ac35fd0005987252e496a2fbe562b449ca60acdbe`.
No duplicate concept or unpublished draft remains. Unit 030 production is
already underway; Unit 029 publication does not complete the corpus.

## D077 - Unit 030 admission and complete Chapter 2 reader (2026-08-23)

Admit `o014.aljabr2.chapter2.grothendieck-categories` as the exact final
Chapter 2 section and chapter-level exercise closure, `chapter2.tex` lines
1756--2132. The normalized authority slice is 30,150 bytes, SHA-256
`4b3ed0e1d7676d37d3bf465a241df0116fbb0e28cf39cd1b313a9f9f19225b7e`;
the translated target is 43,836 bytes, SHA-256
`a7fec40262a70c2f7fe253a97cf21558acc3c0b32272e3bcdb24a04e58c96697`;
and its 133-record stable map is 41,437 bytes, SHA-256
`dff9eaedeaaaad88c10b68d40fd4683f0e27f88164985b1824aef5bfb71b85b7`.
Independent review passed marker order, labels, 46 references over 35 targets,
citations, localized environments, mathematics, all nine TikZ-CD diagrams,
all 20 exercises, 13 active hints, the single commented hint, encoding, and
naturalness. No new source correction is admitted.

Retain two presentation decisions. The Appendix-A forward reference
`eqn:I-small-gen` uses a printed `sourcecrossref` fallback `A.2.1` until the
appendix enters the cumulative reader. A long inline Hom map is reflowed as an
unnumbered display to remove an overfull line; this is the sole display-count
difference and preserves the formula and numbering. The pre-existing bounded
Indonesian terminology QA remains satisfied. Ten new concept entries are
synchronized and the existing `kategori co-well-powered` form is reused,
bringing both terminology surfaces to 395 matching IDs. The exact production
model disclosure remains `OpenAI Codex gpt-5.6-sol, Ultra` without displacing
source or human credits.

The backend now contains 30 sequential units and 1,581 segments. The admitted
shell-escape-disabled XeLaTeX/Biber/MakeIndex replay is
`build/cumulative-unit-030-finalD-20260823`. Biber resolves 19 citekeys;
MakeIndex accepts 144 term and 47 symbol entries. Three final XeLaTeX passes
are stable. The final log has zero TeX, fatal, unresolved, rerun, overfull, or
missing-character finding and 19 non-fatal underfull boxes.

The checkpoint and promoted cumulative reader are byte-identical: 187 pages,
963,655 bytes, SHA-256
`e74feecbbcc1dc2b4538b182215b1c3210ad32f4d90fa933c43cbd27293823bf`.
The PDF is unencrypted and untagged, with 37 resolving outline entries, 51
embedded/subset font names, 636 resolving internal links, 12 HTTPS links, and
no forms, JavaScript, embedded files, or additional actions. Physical pages
167--187 and three contact sheets passed visual inspection. Blank pages 180
and 184 are intentional verso separators. QA receipt `qa/UNIT_030_QA.md` is
8,288 bytes, SHA-256
`ccc38fc3565f4628704e3ef5572cb5e96d5dd2dbcbb22de4829193000b76b26d`.

The 66-row exact manifest `qa/CUMULATIVE_UNIT_030_FILE_MANIFEST.csv` lists
5,562,324 bytes, is 8,318 bytes, SHA-256
`4dc90363c8af66e305689da41c465d083a9b2c09c393537d6c93633ff4f345b2`,
and verifies with zero missing or mismatch. The next exact source cursor is
`chapter3.tex` line 9, `sec:cplx`; its first unit boundary is under bounded
audit. This checkpoint completes Chapter 2 but does not complete the corpus.

## D078 - Unit 030 public lineage advancement (2026-08-23)

Advance the existing GitHub edition repository through Unit 030 at public
`main` commit `12fffac4cae9d30c0e01a842af2a17d97bc11fab`, tree
`915f707640eaf69772629aaa1ebe74244e4a5a47`. The immutable 75-file archive is
1,361,188 bytes, SHA-256
`e7e31d77704180f33b7151e1751c4fb9a015c500840cfb048285f9c7aca58c9d`.
Anonymous repository, commit, raw, archive, manifest, checksum, and reader
readback passed with zero mismatch. The sanitized receipt is
`release/github/GITHUB_PUBLICATION_RECEIPT.json`, 4,730 bytes, SHA-256
`84e960f2da5566437005743036cfdf08e83c1c62ce5da0b9d18a7770b043bea7`.

Advance the same Zenodo concept lineage 22059751 from record 22071903 to
record 22072361, DOI `10.5281/zenodo.22072361`, version `unit-030`. Its seven
reader-first files total 1,315,841 bytes. Every anonymous file download matches
the local bytes and SHA-256; record API/page, DOI, and concept-latest readbacks
all return HTTP 200. The source/backend ZIP is frozen at exactly 30 units,
1,581 segments, 395 terms, and source through `chapter2-unit-030`; no concurrent
Unit 031 material or restricted terminology witness is present. Metadata
retains the exact work title, CC BY 4.0, Indonesian language, attribution,
non-endorsement, single organization contributor entry, and exact production
model note without organization branding in title or descriptive prose. The
sanitized receipt is
`release/zenodo/unit-030/ZENODO_PUBLICATION_RECEIPT.json`, 7,226 bytes,
SHA-256
`5ba4a68170d9b6b67ddf05578db694b81a126fb37177d2bfb132e9c933dbac75`.
No competing concept or unpublished draft was created. Publication does not
complete the corpus.

## D079 - Unit 031 admission and Chapter 3 overview reader (2026-08-23)

Admit `o014.aljabr2.chapter3.overview` as the exact Chapter 3 overview,
`chapter3.tex` lines 9--55. The normalized authority slice is 8,019 bytes,
SHA-256
`6b4b4806e0d9885580547cb103d93e59f0a094ff08d93abdd2781287b71040ec`;
the translated target is 13,031 bytes, SHA-256
`65e3dd7e5c5a0a4512c9c90efd727b32fc7d8c1397d8117f29a492ca080c4e65`;
and its 19-record stable map is 5,258 bytes, SHA-256
`0c70f75800fa91ed0d1ebf97642237d576118746dcc60de1ef43521f4e43731f`.
Independent review passed all markers, 39 references over 30 targets, citation
`KS06`, three displays, the TikZ-CD diagram, reader-tip topology, mathematics,
encoding, and naturalness after one minor bimodule-phrase repair.

Admit and disclose O014-C030--C032: restore the malformed transition as
`Sebaliknya`; restore the skipped `I^1` in the injective resolution; and
replace the ill-typed cohomology denominator `Image(d^{n+1})` with
`Image(d^{n-1})`, verified against three earlier admitted definitions. Add 16
synchronized terminology concepts. Retain the three weakly attested forms for
hyperderived, effaceable, and co-effaceable functors as explicitly provisional,
without a human-dependent hold. Both terminology surfaces now contain 411
matching IDs.

The admitted shell-escape-disabled build is
`build/cumulative-unit-031-finalC-20260823`: Biber resolves 19 citekeys;
MakeIndex accepts 144 term and 47 symbol entries; three final XeLaTeX passes
are clean. The final log has zero TeX, fatal, unresolved, rerun, overfull, or
missing-character finding and 19 non-fatal underfull boxes. The checkpoint and
promoted cumulative reader are byte-identical: 191 pages, 979,643 bytes,
SHA-256
`0834eaa525fb64f3f2f13665238429fd3e4db9e3679b8c71e781ce2fdf333330`.
Physical pages 179--191 passed rendered inspection. The PDF remains untagged
and is not described as fully accessible.

QA receipt `qa/UNIT_031_QA.md` is 8,237 bytes, SHA-256
`eb6dda5f6ebef8776e44981bdf1dd05006fe11476e96d48714d0b0feb1baaf16`.
The 66-row manifest `qa/CUMULATIVE_UNIT_031_FILE_MANIFEST.csv` lists 5,061,256
bytes, is 8,285 bytes, SHA-256
`1578225fc37b67bb44a036fcb384cfc63c00f331a55dad29b825d23cd8b2cd2c`,
and verified with zero mismatch at admission. The next frozen unit is
`chapter3.tex` lines 57--162, `sec:additive-cplx`; this checkpoint does not
complete the corpus.

## D080 - Unit 031 public lineage advancement (2026-08-23)

Advance the existing GitHub edition repository through Unit 031 at public
`main` commit `b194a5ff973e53790564860c9054e5b8736bb2f2`, tree
`1d3728351c64dab3cee68784986aae89ca7db377`. The immutable 80-file archive is
1,401,778 bytes, SHA-256
`a875a5c1c118d0a0545934aea16b9402a355f74411190bb6080598637bdd4da0`.
Its 78 manifest payload rows list 2,600,853 bytes. Anonymous repository,
commit, raw-file, archive, manifest, checksum, README, and reader readback all
passed with zero mismatch. The sanitized receipt is
`release/github/GITHUB_PUBLICATION_RECEIPT.json`, 4,740 bytes, SHA-256
`82d393ca2ca3998c11cd6055cfdc63c2270254a5b6d0f19b0bc3ca14b5394f66`.

Advance the same Zenodo concept lineage 22059751 from record 22072361 to
record 22072584, DOI `10.5281/zenodo.22072584`, version `unit-031`. Its seven
reader-first files total 1,340,041 bytes. Every anonymous file download matches
the local bytes and SHA-256; record API/page, DOI, and concept-latest readbacks
all return HTTP 200. The source/backend and QA/provenance packages freeze
exactly 31 units, 1,600 segments, 411 terms, and source through Unit 031, with
no Unit 032 material or restricted terminology witness. Metadata preserves the
exact title, CC BY 4.0, Indonesian language, author/source credit,
non-endorsement, one organization contributor entry, and exact model note,
without organization branding in the title or descriptive prose. The sanitized
receipt is `release/zenodo/unit-031/ZENODO_PUBLICATION_RECEIPT.json`, 7,232
bytes, SHA-256
`0aa083c4a4789d8ebe30e7b8873fc71c904e4552aaa9e3d203c4b0902c387d7d`.
No competing concept or unpublished draft was created. Publication does not
complete the corpus.

## D081 - Supplemental Indonesian category-theory terminology QA (2026-08-24)

Reaffirm the earlier bounded arXiv-first result before admitting Unit 032:
official arXiv searches did not locate an Indonesian-language category theory,
homological algebra, or adjacent algebra paper with downloadable TeX. This is
a bounded negative result, not a claim of exhaustive absence. Apply the
instructed fallback to the official Universitas Diponegoro journal PDF by Agus
Suryanto, Nikken Prima Puspita, and Robertus Heri S. U., “Fungtor Kontravarian
dan Kategori Abelian,” *Jurnal Matematika* 5(2), 2016. The nine-page PDF is
429,219 bytes, SHA-256
`d22cf3c40242359a2d00eb726697e08b6ad29c647a0309cbcd98914484b5f9b6`.
All pages were rendered with MuPDF and visually inspected; the contact sheet is
922,354 bytes, SHA-256
`1fd4a03e0f49111e8f4fa99991e73e0ff6bb503d5c623d66b4a78bce11976718`.

The witness exactly supports `kategori abelian`, `kernel`, `kokernel`,
`produk`, and `koproduk`. Its older spellings `fungtor`, `obyek`, `morfisma`,
and `homomorfisma` are registered only as recognition/search variants. Retain
the coordinated preferred forms `funktor`, `objek`, `morfisme`, and
`homomorfisme`; no translated prose or formula needs propagation. The complete
evidence and rationale are in `controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`.
The witness remains local QA evidence and is excluded from release payloads.
The edition and public provenance already identify the production model
exactly as `OpenAI Codex gpt-5.6-sol, Ultra` without displacing any source,
author, witness-author, or human-contributor credit.

## D082 - Unit 032 admission: complexes over additive categories (2026-08-24)

Admit `o014.aljabr2.chapter3.complexes-over-additive-categories` as the exact
Section 3.1 range, `chapter3.tex` lines 57--162. The normalized authority slice
is 8,995 bytes, SHA-256
`2f928e1ca88a032bec9c270d65604e25a38bd00ec62874562ae95a55be0ee8b5`;
the translated target is 13,677 bytes, SHA-256
`0ac6def5c534f07ceacfb80f29fff71b0174fffb944c0759fce1392510e3b500`;
and its 33-record stable map is 10,336 bytes, SHA-256
`7100b28797cf67adb12b11dc400a54d980671957bd491a053ba16702fc3c2e1f`.
Independent review passed all 33 markers, 9 labels, 7 references, 4
definitions, 1 lemma, 2 propositions, 2 proofs, the convention, the remark,
all 5 displays, both TikZ-CD diagrams, both lists and all 6 items, 2 footnotes,
11 indexes, mathematics, encoding, and naturalness. The target explicitly
types the DG-morphism identity as `(Tf)d_X=d_Yf`. This range has no exercise,
hint, answer, solution, citation, external figure, or external asset. No new
source correction is required.

Synchronize five newly defined concepts for graded objects, differential graded
objects, bigraded objects, the complex category, and concentrated complexes.
After repairing an initially detected control/backend count mismatch, both
terminology surfaces contain exactly 416 unique matching concept IDs. The
control ledger is 65,903 bytes, SHA-256
`cf88447b578262f044d15ebaecd5b505b051599f90068e88099ca073c12ad777`;
the backend terminology is 27,955 bytes, SHA-256
`f37a93c0ad714999de14697f31b549746f52fac116aa128b600e5e4e3bbcd96a`.
Retain the supplemental UNDIP spellings only as variants; no bulk prose change
is warranted.

The modular backend now contains 32 sequential units and 1,633 segments.
`backend/units.jsonl` is 23,665 bytes, SHA-256
`0212ad5888b3153a14679d27a149b518e3a9396084643228d15a6b4b2c9365e0`;
`backend/segments.jsonl` is 477,156 bytes, SHA-256
`8906b0d5204e12187eb198e361b91358145aee5d464b9fafb69d23a3bf049406`.
The Unit-032 row is `translated_built_qa_passed` and has target-hash parity.

The admitted shell-escape-disabled build is
`build/cumulative-unit-032-finalA-20260823`. Biber resolves 19 citekeys;
MakeIndex accepts 151 term and 51 symbol entries with zero rejection or
warning; three convergence XeLaTeX passes are complete. The final log has zero
TeX/package error, unresolved reference or citation, rerun request, overfull
box, missing character, fatal error, or emergency stop, and 19 non-fatal
underfull boxes. The corrected Biber invocation is recorded because an initial
working-directory invocation could not resolve the relative bibliography; the
final `.blg` is clean.

The checkpoint and promoted cumulative reader are byte-identical: PDF 1.7,
195 pages, 999,106 bytes, SHA-256
`f28977200909076af2a30ea82de30985a917a5e3d62cb2f2d478502b51314ef3`.
It is `id-ID`, unencrypted, untagged, and has 39 outline entries, 843 named
destinations, 654 internal links, 12 HTTPS links, and 52 embedded font
programs, with no forms, JavaScript, embedded files, structure tree, or
MarkInfo. Physical pages 178--195, both contact sheets, and full-size pages
185--188 passed visual inspection; blank physical pages 180 and 192 are
intentional separators.

QA receipt `qa/UNIT_032_QA.md` is 7,699 bytes, SHA-256
`dbb770de4c12b1f884e6a487d48a2725a0e428e923951fc07c478022e579d51c`.
The 67-row exact manifest `qa/CUMULATIVE_UNIT_032_FILE_MANIFEST.csv` lists
5,896,555 bytes, is 8,476 bytes, SHA-256
`d05def8f5bcff64f85a71373ecb125027baeb3892fed2e3621b592336ade913a`,
and verifies with zero missing file, byte-count mismatch, or hash mismatch.
The next exact cursor is `chapter3.tex` line 163, `sec:Hom-cplx`. This
checkpoint remains partial and does not complete the corpus.

## D083 - Unit 032 public lineage advancement (2026-08-24)

Advance the existing GitHub edition repository `main` through Unit 032 at
commit `86e859ef869195aec41d69f8a2aa45362a37f7a0`, tree
`64f1ecea3c0da6af2f5c54677013c8821f86b67f`. Its anonymous immutable archive
contains 85 files, 1,446,288 bytes, SHA-256
`cddc7e994de983926566f76cb21814af147bff257fc6fadf6cc6d44036076f72`;
the 83-row manifest and checksums have SHA-256
`b501226a4db96aa547329564b379673608c73b1724f7541fe714089470b69004`
and `304ae56e3a864c246adf60d6e922640bb3fc7b4298ee07e88427d3e810a43545`,
with zero mismatch. The 999,106-byte reader has SHA-256
`f28977200909076af2a30ea82de30985a917a5e3d62cb2f2d478502b51314ef3`.
Receipt: `release/github/GITHUB_PUBLICATION_RECEIPT.json`, 4,959 bytes,
SHA-256 `ef60848a9545356ab99bc379dcbbf0186d5de591e345a03a82c290256b904e1d`.

Advance only the existing Zenodo concept 22059751 from record 22072584 to
record 22073972, DOI `10.5281/zenodo.22073972`, version `unit-032`. Its seven
public files total 1,367,262 bytes: PDF 999,106 bytes / SHA-256
`f28977200909076af2a30ea82de30985a917a5e3d62cb2f2d478502b51314ef3`;
source/backend ZIP 274,681 bytes /
`d2ad4f7c13c90d04a3acda6cc6870de3d38e9afc0fd45e4685fe787b0f619932`;
QA/provenance ZIP 66,327 bytes /
`7d7c685f3f6ea3ec12fbc6192e3bfcdfc63ebe75812f7ea4c0db365378e47cce`;
LICENSE 19,045 bytes /
`48a83a6e39f7b2f166763b30776132c9a99aa816f17cb06f87ad5b8542a7b71f`;
README 2,972 bytes /
`1c550d081c714133bbea1e11eed91388ee5d51e2e4a56439173c2827f0abf16f`;
release manifest 4,528 bytes /
`e06f82587665d091bf652c5485508726e4bfc237dff3d56e835b482d0889ecd9`;
and checksums 603 bytes /
`f25168c782490269741898a9153831714262bb64261d1d64e9d625130488e760`.
Anonymous record, DOI, concept-latest, and every-file readback pass. The payload
freezes exactly 32 units, 1,633 segments, and 416 terms; no Unit 033 target or
C033--C035 correction artifact is present. Exact model provenance remains
`OpenAI Codex gpt-5.6-sol, Ultra`; title, CC BY 4.0, `ind`, attribution,
non-endorsement, and the single established organization contributor are
preserved. Receipt: `release/zenodo/unit-032/ZENODO_PUBLICATION_RECEIPT.json`,
7,200 bytes, SHA-256
`aca04167d54526bcc81ad63c7b4bb9da3c61e1a581e7015679e5e906517ae8ca`.
Publication remains partial and does not complete the corpus.

## D091 - Explicit task-local cleanup before continuation (2026-08-24)

Pause production for the user's cleanup gate and inspect only exact O014 paths
already known to this lane. Preserve canonical and live sources, the admitted
Unit 036 finalB build, current PDFs, frozen release staging, contact sheets,
authority and terminology evidence, receipts, controls, manifests, credentials,
and the active Unit 037 source slice and map.

Archive 51 exact superseded or reproducible artifacts: the 15-file obsolete
`build/cumulative-unit-036-finalA-20260824` tree; the 12-file transient
`tmp/terminology-field-qa` tree; 22 loose rendered `page-*.png` files and the
extracted text file in `tmp/pdfs/unit036-finalB-pages-198-219`; and
`tmp/unit036-full-pdftotext.txt`. The verified no-overwrite archive is
`old stuff/O014-unit036-superseded-build-and-QA-scratch-20260824.zip`, 51
entries and 10,910,003 uncompressed bytes, 9,617,936 compressed bytes,
SHA-256
`af8056e178442db4223655000956e69d944aa64a667e7f7ddfa3b45832356742`.
Every entry name, byte count, and SHA-256 reverified before deletion; delete
only those exact archived loose originals. This cleanup changes no canonical
source, admitted artifact, release payload, or reproducibility evidence.

## D092 - Unit 036 public lineage advancement (2026-08-24)

Advance the existing GitHub edition repository
`KokunoYumeto/metode-aljabar-jilid-2-id` on `main` through Unit 036. Commit
`51db528789c176d8a906a55b5c2a7ee40dc27ccc` carries the admitted content;
inventory-only commit `9abf7c2861bb08e0d09d919ce2e242699ae4e657`, tree
`b1d951c2244694e5f8b8f2a102ab8184dec9dc7c`, corrects two manifest and
checksum rows that had described CRLF working-tree bytes instead of the
canonical LF blobs. No payload content changes in the follow-up commit. The
105-file immutable public archive is 1,658,586 bytes, SHA-256
`6b2ee1c75911a2143c6ec2a73a599e78d1214b7a6088083d64398a2893910da9`;
all 103 manifest rows, all 103 checksum rows, repository and commit pages, and
the 1,107,313-byte PDF pass anonymous readback with zero mismatch. Sanitized
receipt `release/github/GITHUB_PUBLICATION_RECEIPT.json` is 5,829 bytes,
SHA-256
`e7663b8ce5ff43b7c9d11fb06d145c22fa00f1d30e3259a20b1739feb9080327`.

Advance only existing Zenodo concept 22059751 from record 22074617 to public
record 22075083, DOI `10.5281/zenodo.22075083`, version `unit-036`. Its seven
public files total 1,499,086 bytes: reader PDF 1,107,313 /
`a720761eeab43f504f22af1214259c3481e377f5de3ecd3287b7aee9e71c8d2b`;
source/backend ZIP 304,935 /
`4c979019f554de4082029a5b192edad3508a5396d529993d8b13159aa28dfb37`;
QA/provenance ZIP 59,453 /
`726c5c08e43a01034b5aaf5e842f4b53e5c280c12ba72574d1afaf022bf802bd`;
LICENSE 19,045 /
`48a83a6e39f7b2f166763b30776132c9a99aa816f17cb06f87ad5b8542a7b71f`;
README 3,006 /
`c56c10d6e4bf84608da7cbbe7c264498a9796d9180a2fe6eb1a7c54e8440ed4f`;
release manifest 4,731 /
`8304e25e0d6b1c03591df101c2a72357de0e792370d4f34c23ac89427dbbcbfb`;
and checksums 603 /
`c4b769fb7df26e1ffe26f2c5778d69118ed02a714f5c63cb61557130ac70f6ff`.
Anonymous record API/page, DOI resolution, concept-latest, and every-file
byte/hash readback pass with zero mismatch. Metadata preserves exact title,
`ind`, CC BY 4.0, source attribution and non-endorsement; the established
organization contributor appears exactly once and nowhere in the title or
description. Model disclosure remains `OpenAI Codex gpt-5.6-sol, Ultra`.
Receipt `release/zenodo/unit-036/ZENODO_PUBLICATION_RECEIPT.json` is 6,743
bytes, SHA-256
`38d64d268f1a3828ab29c7b3be083030300642e811474877adfc9e811659d290`.
No competing concept or residual unpublished draft exists. This worthwhile
partial checkpoint is preserved but does not complete the corpus.

## D093 - Unit 037 admission: complexes in an abelian category (2026-08-24)

Admit `o014.aljabr2.chapter3.abelian-category-complexes`, exactly frozen
`chapter3.tex` lines 946--1060. The 8,933-byte LF-normalized slice has SHA-256
`6adf88af700b26dac31c81724d991fbefcedab64f6ccd08849e532a75e04410e`;
the exhaustive 30-record map is 9,537 bytes, SHA-256
`e08be8d6d9372550bcfa2680c6f3d1b02fbaa4f9886d35ff7b293fc82aaa30c2`.
The complete Indonesian target is 262 LF-terminated lines, 13,925 bytes,
SHA-256
`e6078b3d29464c49f90f9586aa44448da806efc41017b610bf2e2f3715583065`.

Independent full-unit structural and semantic reviews pass all 30 segments,
eight labels, 18 xrefs, 23 balanced environment pairs, eight display
constructs, six TikZ-CD diagrams with 62 arrows, three indexes, and both list
items. No omitted content, mistranslation, polarity, quantifier, degree,
encoding, active-language-residue, or stop-boundary defect remains. Accept and
disclose O014-C040--C043: component families must be identities of complexes;
the induced three-term-diagram differential requires `d_Z^n`; the proof
concludes `C(A)` rather than its already-assumed-abelian input `A`; and the
cokernels must use `d^(n-1)` to type the displayed degree-`n-1` to degree-`n`
vertical maps. The correction ledger has 44 unique rows through O014-C043.
Unit 037 adds no exercise, hint, answer, solution, citation, or external asset.

Repair the stale backend adjacency metadata discovered during the independent
build audit: sequences 26--36 now point to their exact successor, all 36
nonterminal records match the following unit ID, and sequence 37 is marked
`translated_built_qa_passed`. The synchronized backend has 37 unique units,
1,899 unique segments, and 427 terminology concepts with zero missing nested
target or terminology mismatch.

Admit `build/cumulative-unit-037-finalA-20260824`. Biber resolves 19 citekeys;
MakeIndex accepts 167 term and 71 symbol entries with zero rejection or
warning. The final 79,650-byte log, SHA-256
`bcff49d344c09a3b34a68ac64b676fe6981bf1fa3526aa4cb46404f329065d84`,
has zero TeX/package error, undefined control/reference/citation, rerun request,
overfull box, missing character/file, fatal error, or emergency stop. Sixteen
underfull horizontal and seven underfull vertical boxes are non-fatal.

Promote the byte-identical 223-page PDF to the Unit 037 checkpoint and current
cumulative reader: 1,127,663 bytes, SHA-256
`27e07599542a5994f99c6a43c4a8cebdfec4c2f2d3415e186fa79dea108facb0`.
It is unencrypted and untagged, with 44 outlines, 974 named destinations, 749
resolved internal actions, 12 URI actions, and all 52 fonts embedded; 11
mathematical fonts lack ToUnicode. Local and independent visual inspection of
pages 1--8 and 209--223 finds no clipping, overlap, malformed diagram, or
non-centered-reader regression. QA receipt `qa/UNIT_037_QA.md` is 8,548 bytes,
SHA-256
`7ea0827f6b28949cccda14231ff6217be51f10c1c766ba3743e37426e7bd6315`.
The 75-row exact manifest lists 10,497,235 bytes, is 9,483 bytes, SHA-256
`46d35857206375e14e1810289633b74fa52031132d7a115c4783c59ef8d894d0`,
and re-verifies with zero mismatch. Advance next to the complete Section 3.7,
`chapter3.tex` lines 1061--1292, without crossing `sec:HH` at line 1293. This
is an admitted partial boundary and does not complete the full corpus.

## D090 - Unit 036 admission: double complexes (2026-08-24)

Admit Unit 036, `o014.aljabr2.chapter3.double-complexes`, exactly
`chapter3.tex` lines 700--945. The normalized 20,674-byte authority slice has
SHA-256
`0d532ff079384d4437ed82abf21c828fe392f79f48db27f57a5af62069ed1c8c`;
the translated 28,124-byte target has SHA-256
`d36274b3f84495b1a28608b9f95f7e2d173afe73e84b38f408b265819c9bcc3f`;
and the 76-record stable map has SHA-256
`f2a147d9be45c91a2ccd292e843b830237636743b43616eb1437453479edcada`.
Two independent reviews pass exact marker order, all 13 labels, 12 semantic
reference relationships, one citation, 14 indexes, ten TikZ-CD diagrams, six
items, 37 balanced environments, formulas, signs, degrees, encoding, and
natural Indonesian prose. One long Hom-totalization isomorphism is reflowed as
a display to remove an overfull line without mathematical change.

Apply and disclose two deterministic source corrections. O014-C038 restores
the omitted bifunctor `F` in the functor equality and both rightmost shifted
isomorphism terms. O014-C039 uses vertical coefficient `(-1)^q` for the strict
inverse `sigma^{-1}` and supplies the coordinate isomorphism `(-1)^q` that
changes only the vertical sign and recovers the standard Hom differential.
The corrections ledger has 40 unique rows through O014-C039. No upstream
contact occurred.

Complete the requested arXiv-first terminology recheck before admission. No
Indonesian same-field arXiv source with downloadable TeX was found in the
bounded exact-phrase search, so four official institutional PDF witnesses were
directly inspected. They refine field variants and evidence notes but do not
justify changing coordinated preferred prose. The exact report is 14,089
bytes, SHA-256
`0d3cc71e0e7eb1a837de69cbc4e570575df8efd63090927495899ed78e19b3fc`.
The control and backend stores contain the same 427 terminology concepts. The
exact model identification `OpenAI Codex gpt-5.6-sol, Ultra` remains in reader,
edition, and release metadata with source and human credits preserved.

Admit the shell-escape-disabled build
`build/cumulative-unit-036-finalB-20260824`. Biber resolves 19 citekeys;
MakeIndex accepts 165 term and 70 symbol entries with zero rejection or
warning. The final 79,529-byte log has SHA-256
`b4b884d331045167ca903e11b920f776ddfaecc617c91c1ae2086bfb64dfdddb`
and zero TeX/package error, unresolved reference or citation, rerun request,
overfull box, missing character, fatal error, or emergency stop. Fifteen
non-fatal underfull horizontal boxes and seven underfull vertical boxes remain.

The checkpoint and promoted reader are byte-identical: PDF 1.7, 219 pages,
1,107,313 bytes, SHA-256
`a720761eeab43f504f22af1214259c3481e377f5de3ecd3287b7aee9e71c8d2b`.
Physical pages 198--219, both contact sheets, and full-size pages 205--212 pass
visual inspection; physical page 216 is an intentional separator. QA receipt
`qa/UNIT_036_QA.md` is 9,198 bytes, SHA-256
`126ff3267e7dd55b943a6277d72525dde3b5abe51cbf0279229de8063cf7859b`.
The 73-row manifest `qa/CUMULATIVE_UNIT_036_FILE_MANIFEST.csv` lists 7,144,999
bytes, is 9,283 bytes, SHA-256
`e069f9a83d36952473d5dc7ff18b4ba371a16523c6c971fee7d9731dd1642a9c`,
and independently verifies with zero missing file, duplicate path, byte-count
mismatch, or hash mismatch.

Advance the exact cursor to Unit 037,
`o014.aljabr2.chapter3.abelian-category-complexes`, `chapter3.tex` lines
946--1060, stopping before `sec:cone-vs-long-exact-sequence` at line 1061. Its
frozen 8,933-byte slice has SHA-256
`6adf88af700b26dac31c81724d991fbefcedab64f6ccd08849e532a75e04410e`;
its 30-record map has SHA-256
`e08be8d6d9372550bcfa2680c6f3d1b02fbaa4f9886d35ff7b293fc82aaa30c2`.
This checkpoint remains partial and does not complete the corpus.

## D084 - Unit 033 admission: Hom complexes and homotopy (2026-08-24)

Admit Unit 033, `o014.aljabr2.chapter3.hom-complex-and-homotopy`, exactly
`chapter3.tex` lines 163--345. The frozen 12,347-byte source slice has SHA-256
`30e6afb74eae4ea7aa78d610a2806c713faa3d0e7f893e16f0565a0ce379e59c`;
the translated 18,841-byte target has SHA-256
`deb48c356cc78ad8fc5f4d730be640d5a60fde0c3b90d7a45c21330bcbd337d2`;
and the 56-record stable map has SHA-256
`0798cc52a5cf5e9c49c9132039d58e74f95e7d653348d6e4367708214a2d11c2`.
Independent final review passes exact marker order, all 15 labels, all 20
references, all 8 indexes, four TikZ-CD diagrams and 12 arrows, all formula
signs and degrees, balanced environments, encoding, and Indonesian
naturalness. Three overly long inline formulas were moved into displays to
remove overfull lines without changing their mathematical content.

Apply and disclose three deterministic source corrections: O014-C033 types
the upper horizontal diagram map as `\Hom^n(u,v)`; O014-C034 binds the
homotopy variable in degree `n-1`; O014-C035 types the adjunction component
degreewise. Preserve the functional source label spelling
`eqn:homotopy-cat-cmposition`. Synchronize four new terminology concepts:
`aturan Leibniz`, `morfisme homotopik`, `morfisme homotopik nol`, and
`kategori homotopi`. The backend now contains 33 units, 1,689 segments, and
420 exact matching terminology concepts.

Admit the shell-escape-disabled build
`build/cumulative-unit-033-finalC-20260824`. Biber resolves 19 citekeys;
MakeIndex accepts 155 term and 55 symbol entries with zero rejection or
warning. The final 79,160-byte log has SHA-256
`a9f4627dcaee573db4dd4454a196e33c1e3ef91f5616ba9fbdbd5f558abc49d5`
and zero TeX/package error, unresolved reference or citation, rerun request,
overfull box, missing character, fatal error, or emergency stop. Twenty
non-fatal underfull boxes remain.

The checkpoint and promoted cumulative reader are byte-identical: 201 pages,
1,023,423 bytes, SHA-256
`b621a25b3fe7032885680eea75fae0096cab5bafd95818cd1cf88fad9e6e40a3`.
Physical pages 181--201 and full-size pages 188--194 pass visual inspection.
QA receipt `qa/UNIT_033_QA.md` is 7,765 bytes, SHA-256
`be60e4a4db0b7831942fbd420cdf15cc1fb3fb011dbe974b3b2b595140e13e62`.
The 70-row manifest `qa/CUMULATIVE_UNIT_033_FILE_MANIFEST.csv` lists 7,264,804
bytes, is 8,844 bytes, SHA-256
`2f2af339423f49c2bb9bfe90ebe2d8af199b84e43bb59c5adec5a30b34054b2c`,
and verifies with zero missing file, duplicate path, byte mismatch, or hash
mismatch. The next exact cursor is Unit 034, `chapter3.tex` line 346,
`sec:mapping-cone`, stopping before line 622. This remains partial and does
not complete the corpus.

## D085 - Unit 033 public lineage advancement (2026-08-24)

Advance the existing GitHub edition repository `KokunoYumeto/metode-aljabar-jilid-2-id`
on `main` to commit `45eb6b8975c1ddc8b94f2c42cd669c2a0ad972c7`, tree
`7e10077278642d2cdfabfb92b1b7023a19655668`. Anonymous repository, commit,
archive, raw manifest, checksums, and PDF readback pass. The 90-file public
archive is 1,493,833 bytes, SHA-256
`fbe766c4cbfb1a496a89305d2a28c5435c544180968f5365533224acaac984c0`;
its 88-row manifest covers 2,786,609 payload bytes with zero mismatch and has
SHA-256 `5489da053ff9ca1988b8b2f73015a9da09e5617c59bf8a00af83b73d07f8943c`;
checksums have SHA-256
`0d1d9801ff95f26158c8e7859926411577664a8862860e841f3683b1bac9dc48`.
The reader is 1,023,423 bytes, SHA-256
`b621a25b3fe7032885680eea75fae0096cab5bafd95818cd1cf88fad9e6e40a3`.
Sanitized receipt `release/github/GITHUB_PUBLICATION_RECEIPT.json` is 5,157
bytes, SHA-256
`e79f8cfe56a4d950b11d191310de9083bdec72762f6f952dbfbaf81d22f4a0c5`.

Advance only existing Zenodo concept 22059751 from record 22073972 to record
22074221, DOI `10.5281/zenodo.22074221`, version `unit-033`. Its seven public
files total 1,399,828 bytes: PDF 1,023,423 /
`b621a25b3fe7032885680eea75fae0096cab5bafd95818cd1cf88fad9e6e40a3`;
source/backend ZIP 281,854 /
`39a30bc43a8a409cd130fff8bb7cebcd2db8e2842691e289a84bef083740f082`;
QA/provenance ZIP 67,315 /
`ab92f9253bada89ee70284e14d4552f23afd7cf92b4ad81310b7a1ddea27fab8`;
LICENSE 19,045 /
`48a83a6e39f7b2f166763b30776132c9a99aa816f17cb06f87ad5b8542a7b71f`;
README 2,967 /
`887bdc3d21516f93cb40cc3681d58f56ff15ef8d4460d1e2e0c83d91e101f650`;
release manifest 4,621 /
`9346e52473a63b2dddb80de939487bf62d90947e6a918a212c4a70593911f881`;
and checksums 603 /
`bbbdde73c9d3417d10ca14ce20b5d5084c0a55f4af341ef32b9a34534302aca2`.
Anonymous record, DOI, concept-latest, and every-file readback pass. Sanitized
receipt `release/zenodo/unit-033/ZENODO_PUBLICATION_RECEIPT.json` is 7,477
bytes, SHA-256
`ff888a23baf443fad48b42ce91f7e984ed4d0f8ad878f07a9b16699fcf3f48ff`.

The exact public snapshot freezes 33 units, 1,689 segments, and 420 terms,
with corrections through O014-C035 and zero Unit 034 leakage. Preserve the
exact title, CC BY 4.0, `ind`, attribution, non-endorsement, one established
organization contributor, and model note `OpenAI Codex gpt-5.6-sol, Ultra`.
A bounded Figshare retry made no mutation: account and project endpoints return
403 `Inactive/disabled account`, article 33314775 returns 404, and collection
8668413 remains publicly readable. Sanitized receipt
`release/figshare/unit-033/FIGSHARE_PUBLICATION_RECEIPT.json` is 4,010 bytes,
SHA-256 `02b14573b71222ce451d0ead95c4a9db22d536c94717eb3975129731184098a4`.
Publication remains partial and does not complete the corpus.

## D086 - Unit 034 admission: mapping cone (2026-08-24)

Admit Unit 034, `o014.aljabr2.chapter3.mapping-cone`, exactly
`chapter3.tex` lines 346--621. The normalized 18,021-byte authority slice has
SHA-256
`0640f89fb580226e49e7663880d487fea235d21fbe5e510e842bc782b9eafa35`;
the translated 24,865-byte target has SHA-256
`8cd871b192324139083c3a3bd206418b37b0d9bceede23db6279c223f0b6da03`;
and the 80-record stable map has SHA-256
`d2cf4ff2a6a8ce6da91171bfce6df365cdf58b8ef33421273e5b15185d77052b`.
Two independent final reviews pass exact marker order, all 13 labels, 15
references, nine indexes, seven TikZ-CD diagrams plus one embedded TikZ
matrix, 30 source displays plus one presentation-only tuple reflow, all signs,
degrees, maps, balanced environments, encoding, and natural Indonesian prose.
No Chinese prose remains and no source correction is required. Synchronize
three new terminology concepts: `kokernel homotopi`, `kernel homotopi`, and
`kocitra homotopi`. The backend now contains 34 units, 1,769 segments, and 423
exact matching terminology concepts.

Admit the shell-escape-disabled build
`build/cumulative-unit-034-finalC-20260824`. Biber resolves 19 citekeys;
MakeIndex accepts 160 term and 59 symbol entries with zero rejection or
warning. The final 79,349-byte log has SHA-256
`4385fd0e3d80884dcbc157dbe512010d02b852ea0500235cec64d54c6ac13f97`
and zero TeX/package error, unresolved reference or citation, rerun request,
overfull box, missing character, fatal error, or emergency stop. Fifteen
non-fatal underfull horizontal boxes and six underfull vertical boxes remain.

The checkpoint and promoted cumulative reader are byte-identical: 209 pages,
1,056,839 bytes, SHA-256
`c49a6a7fd01659cc2fdaf7304b7a0576f48cfbb35c3106446bd21db78e509aac`.
Physical pages 188--209, both contact sheets, and full-size pages 194--202 pass
visual inspection; physical page 206 is an intentional separator. QA receipt
`qa/UNIT_034_QA.md` is 7,387 bytes, SHA-256
`db34ae09be27c2a6173ba0966df3a72e8002a89235ed5305e8d1b0eb24f822aa`.
The 71-row manifest `qa/CUMULATIVE_UNIT_034_FILE_MANIFEST.csv` lists 7,308,710
bytes, is 8,966 bytes, SHA-256
`edad5e9ff4ad53da1f7d73564639d964b1213f87632368c15c2b92507d4494a8`,
and verifies with zero missing file, duplicate path, byte mismatch, or hash
mismatch.

Advance the exact cursor to Unit 035,
`o014.aljabr2.chapter3.opposite-category-complexes`, `chapter3.tex`
lines 622--699, stopping before `sec:double-cplx` at line 700. Freeze its
6,688-byte slice at SHA-256
`2fb37ee63cd53f2ac6de01c3aef3bc9fab1da286ee4ad989e7e9f38fd07108ba`
and its 24-record map at SHA-256
`238672a25609198890fec47d1a06490b15ae4e388e18f1ddd9fa7c311671a2af`.
Authority line 645 has the proven O014-C036 candidate: the printed strict
involutivity claim overlooks that `\sigma^2X` has differential `-d`; preserve
the valid natural isomorphism to `X` by degree-`n` component
`(-1)^n\identity_{X^n}` and disclose the correction. This checkpoint remains
partial and does not complete the corpus.

## D087 - Unit 034 public lineage advancement (2026-08-24)

Advance the existing GitHub edition repository
`KokunoYumeto/metode-aljabar-jilid-2-id` on `main` to commit
`e1cc1e0f81471da54726dff4c2086e4102725312`, tree
`fd16fcc220af6af56fd9ae9e4734d6fca712b418`. Anonymous repository, commit,
archive, manifest, checksum, and reader readback pass. The 95-file archive is
1,550,775 bytes, SHA-256
`75ca202ad604ad447e69eb1c888cdd9773edb70ac96f60e7158e2ab5ed98e807`;
the 93-row manifest covers 2,899,523 bytes with zero mismatch and has SHA-256
`f238d6fcdb4e087483a2c8de631188bfb639344a0e5b2feee021246be21cf8bf`;
checksums have SHA-256
`543959151ee38230c53bda26a8863556388538deb96bd183f694b3357a5b00b1`.
Sanitized receipt `release/github/GITHUB_PUBLICATION_RECEIPT.json` is 5,600
bytes, SHA-256
`9437c2f5d239d946331dd2eda1073ab9fe4c02e00588aca8bf15b7004ede4756`.

Advance only existing Zenodo concept 22059751 from record 22074221 to record
22074495, DOI `10.5281/zenodo.22074495`, version `unit-034`. Its seven public
files total 1,429,702 bytes. The reader is 1,056,839 bytes, SHA-256
`c49a6a7fd01659cc2fdaf7304b7a0576f48cfbb35c3106446bd21db78e509aac`;
the source/backend ZIP is 290,677 bytes, SHA-256
`7f528be372db582837c08f2de2433b7f84137348ed6dab1ac11a04e931b330a5`;
and the QA/provenance ZIP is 54,931 bytes, SHA-256
`08ea62ee4756e2fcca79080e1f5e02f46dcf2ef533c219a864fa3b01104e6bd0`.
All seven files pass anonymous byte/hash readback; no residual draft or
competing concept remains. Sanitized receipt
`release/zenodo/unit-034/ZENODO_PUBLICATION_RECEIPT.json` is 7,531 bytes,
SHA-256
`0dcaad52bb26ab65150fe1d8c3395febaf65b18889a5a133fdc48fcd46db6fef`.

The public snapshot freezes exactly 34 units, 1,769 segments, and 423 terms,
with corrections through O014-C035 and zero Unit 035 leakage. Preserve the
exact title, CC BY 4.0, `ind`, attribution, non-endorsement, one established
organization contributor, and model note `OpenAI Codex gpt-5.6-sol, Ultra`.
A bounded Figshare retry made no mutation because the account remains inactive;
its receipt is `release/figshare/unit-034/FIGSHARE_PUBLICATION_RECEIPT.json`,
4,010 bytes, SHA-256
`357d5df10851b62d73c4117f0cbea8d608f8ecf3ffa75f019291dc5e28c2ed86`.
Publication remains partial and does not complete the corpus.

## D088 - Unit 035 admission: complexes over the opposite category (2026-08-24)

Admit Unit 035, `o014.aljabr2.chapter3.opposite-category-complexes`, exactly
`chapter3.tex` lines 622--699. The normalized 6,688-byte authority slice has
SHA-256
`2fb37ee63cd53f2ac6de01c3aef3bc9fab1da286ee4ad989e7e9f38fd07108ba`;
the translated 10,449-byte target has SHA-256
`e0b892cb1be0a68e67a7e88dcb3b1c9fe6346a26811feb426b540a0be98c804f`;
and the 24-record stable map has SHA-256
`238672a25609198890fec47d1a06490b15ae4e388e18f1ddd9fa7c311671a2af`.
Two independent reviews pass exact marker order, all six labels, five
reference relationships, two indexes, three TikZ-CD diagrams, environments,
formulas, signs, degrees, balanced structure, encoding, and natural Indonesian
prose. A forward reference to `prop:derived-cat-op` uses the established
`sourcecrossref` fallback. Local table spacing and one aligned-display reflow
remove two overfull lines without mathematical change.

Apply and disclose two deterministic source corrections. O014-C036 replaces
the printed strict-involutivity claim: applying the displayed
`(-1)^{n+1}` construction twice gives `(X,-d_X)`, naturally isomorphic to
`X` by degree-`n` component `(-1)^n\identity_{X^n}`, while coefficient
`(-1)^n` defines the true strict inverse. O014-C037 replaces a reversed
left/right prose locator by side-neutral wording. The corrections ledger has
38 unique rows through O014-C037. No new terminology concept is required; the
control and backend terminology ledgers remain exact 423-concept matches. The
backend now contains 35 units and 1,793 segments.

Admit the shell-escape-disabled build
`build/cumulative-unit-035-finalC-20260824`. Biber resolves 19 citekeys;
MakeIndex accepts 160 term and 61 symbol entries with zero rejection or
warning. The final 79,457-byte log has SHA-256
`c18387a776347a26f88660d8ac768079fba0050691599c78229b35c3b9263050`
and zero TeX/package error, unresolved reference or citation, rerun request,
overfull box, missing character, fatal error, or emergency stop. Fifteen
non-fatal underfull horizontal boxes and seven underfull vertical boxes remain.

The checkpoint and promoted reader are byte-identical: PDF 1.7, 211 pages,
1,070,845 bytes, SHA-256
`1f6cc9abf330f9d25604bfe9b5862bb39114069973256bcb11f6be23cf0c8b4c`.
Physical pages 195--211 and full-size pages 201--204 pass visual inspection.
QA receipt `qa/UNIT_035_QA.md` is 7,537 bytes, SHA-256
`8970a0179ec41cc94ed10dea56557f777e31d909e44bdae2bcd4067d3cc8391a`.
The 72-row manifest `qa/CUMULATIVE_UNIT_035_FILE_MANIFEST.csv` lists 8,327,986
bytes, is 9,086 bytes, SHA-256
`0f439079634f08549d4ec6e124683469e09c4bf1392b0279f6f8b216d10794fe`,
and independently re-verifies with zero missing file, duplicate path,
byte-count mismatch, or hash mismatch.

Advance the exact cursor to Unit 036,
`o014.aljabr2.chapter3.double-complexes`, `chapter3.tex` lines 700--945,
stopping before `sec:Abel-cplx` at line 946. Its frozen 20,674-byte slice has
SHA-256
`0d532ff079384d4437ed82abf21c828fe392f79f48db27f57a5af62069ed1c8c`;
its 76-record map is 20,892 bytes, SHA-256
`f2a147d9be45c91a2ccd292e843b830237636743b43616eb1437453479edcada`.
During translation, resolve and disclose only if proven the apparent omitted
`F` in lines 907--908 and the strict-inverse versus same-form
`\sigma^{-1}` sign/notation conflict in lines 915--932. This checkpoint
remains partial and does not complete the corpus.

## D089 - Unit 035 public lineage advancement (2026-08-24)

Advance the existing GitHub edition repository
`KokunoYumeto/metode-aljabar-jilid-2-id` on `main` to commit
`372e9cbcb6b04181e0b6c6bc4a0cdf3fe16728a4`, tree
`388fef9e48dd30c052c8c39494a7367fa400f7c6`. Anonymous repository, commit,
archive, manifest, checksum, and reader readback pass. The 100-file immutable
archive is 1,585,097 bytes, SHA-256
`85b53e213feb49b56db2e4c18053f49f26b0ec3be3aa31d6a9cb25a8562a927f`;
the 98-row manifest covers 2,965,413 payload bytes with zero mismatch and has
SHA-256 `1450b5db5f268bd5e7831209d1aca39d3e58921f720cf82af7666df64a468aca`;
checksums have SHA-256
`5fbb1cba6107da3c30a385c4447e08ac34e6db08baee3e527d073ab4cf004a07`.
The reader is 1,070,845 bytes, SHA-256
`1f6cc9abf330f9d25604bfe9b5862bb39114069973256bcb11f6be23cf0c8b4c`.
Sanitized receipt `release/github/GITHUB_PUBLICATION_RECEIPT.json` is 5,603
bytes, SHA-256
`417a1c013f497cabff2b99553201a8b63033cfe7d59b8a77fa5f697007b53994`.

Advance only existing Zenodo concept 22059751 from record 22074495 to record
22074617, DOI `10.5281/zenodo.22074617`, version `unit-035`. Its seven public
files total 1,448,692 bytes: PDF 1,070,845 /
`1f6cc9abf330f9d25604bfe9b5862bb39114069973256bcb11f6be23cf0c8b4c`;
source/backend ZIP 295,163 /
`b81a4e3ac6486e5da92f39ae4c8b4ee56715f3696f85e58ef1a21bb49db34104`;
QA/provenance ZIP 55,452 /
`7940cee1b0df5511b2f1369f786cba4525a60e07f7ebb2408284030627c17001`;
LICENSE 19,045 /
`48a83a6e39f7b2f166763b30776132c9a99aa816f17cb06f87ad5b8542a7b71f`;
README 2,964 /
`c5252f5e17f94d7c60e31c4720620ea67955f57be70e3ddbd6f9ec307d64b391`;
release manifest 4,620 /
`33842dd560b7d3f7ed7d60b477ddb5cbf7ffd7ecfe433691c47374a37671d7e6`;
and checksums 603 /
`afb0ab31ec83f1c6e974af4bea3122503113a1ecafa657f1f6059743e0bdbf8c`.
Anonymous record API/page, DOI resolution, concept-latest, and every-file
byte/hash readback pass independently; no residual draft or competing concept
exists. Sanitized receipt
`release/zenodo/unit-035/ZENODO_PUBLICATION_RECEIPT.json` is 7,529 bytes,
SHA-256 `087d33f0a572472ce38591b22d128d39c0a9fbcc042238e6fa1845abb4ed2dc2`.

The exact public snapshot freezes 35 units, 1,793 segments, 423 terms, and
corrections through O014-C037, with zero Unit 036 leakage. Preserve the exact
work title, CC BY 4.0, `ind`, attribution, non-endorsement, one established
organization contributor, and model note `OpenAI Codex gpt-5.6-sol, Ultra`.
The bounded Figshare retry made no mutation because the account remains
inactive; receipt `release/figshare/unit-035/FIGSHARE_PUBLICATION_RECEIPT.json`
is 4,010 bytes, SHA-256
`a430dcbb7dd6e2e16cf74129ee2b3cff0d45c0f8ad1aff48f4255c2734e502ea`.
Publication remains partial and does not complete the corpus.

## D094 - Freeze Unit 038 after admitting Unit 037 (2026-08-24)

Advance the durable production cursor from admitted Unit 037 to
`o014.aljabr2.chapter3.mapping-cone-and-long-exact-sequences`. Freeze exactly
`chapter3.tex` lines 1061--1292, including the terminal blank line, and stop
before `sec:HH` at line 1293. The 17,739-byte LF-normalized slice has SHA-256
`161c303deb0ff9f7d7a6dbd8341a1dae0e11086d794e68d812b6d3db334fe43e`
and independently matches the authority source. Its 63-record map is 22,724
bytes, SHA-256
`2d258bb98975a650dc395a3b355da041d8d9dcb12719a7701037fc300d7e8794`;
sequences and identifiers are unique, mapped bounds are monotone, all 43
source-reference occurrences over 22 unique targets and both citation keys
resolve, and no correction
candidate or missing component is demonstrated by the bounded static audit.
Translate this unit next while Unit 037 is advanced through the already
authorized GitHub and Zenodo publication lineages.

## D095 - Publish the admitted Unit 037 boundary (2026-08-24)

Advance the existing GitHub edition repository, without creating another
repository or contacting upstream, to commit
`1c75e6d7691e460b8bb1a8c23888674e93dce18c`, tree
`6b47e4fda674de204cc116470d8e6b184daf97ca`. Accept only after anonymous
readback of the 1,701,722-byte immutable archive (SHA-256
`b12bd4b67b67303f794180db2f63aaec1470eb7cfaa5dccdcbcb6516f93f288f`),
all 108 canonical manifest/checksum rows, and the 223-page reader reports zero
mismatch.

Advance only Zenodo concept 22059751 from record 22075083 to published record
22086560, DOI `10.5281/zenodo.22086560`, version `unit-037`. The seven files
total 1,517,978 bytes and anonymously match the local PDF, source/backend ZIP,
QA/provenance ZIP, license, README, release manifest, and checksums with zero
mismatch. Preserve CC BY 4.0, author attribution, exact partial scope,
non-endorsement, model disclosure, and the established single organization
contributor; keep the organization label out of title and descriptive prose.
No residual draft or duplicate concept is permitted. Public preservation is
complete for Unit 037, but the overall goal remains active at Unit 038.

## D096 - Admit the reviewed Unit 038 translation draft to integration (2026-08-24)

Accept all 63 translated segments as mathematically faithful after independent
structural and semantic comparison. The final pre-build target is 25,223 bytes,
SHA-256
`391faa18feede781394efefe0808ed3729650a5f014d2217efac05e4d2b35f08`.
It preserves 13 labels, 43 source references as 42 ordinary references plus
one established forward-reference fallback, two citations, 50 balanced
environment pairs, 16 TikZ-CD diagrams with 139 arrows, 12 list items, all
formula signs/degrees/indices, and all 63 stable IDs; no Han prose remains.

Repair two segment-map annotations that attributed references outside their
mapped ranges, yielding a 22,648-byte map with SHA-256
`56322e9fc22c7dc1ef8eb5fac6a9b09913011cf451f05f6cd5922ddd450e1ad8`.
Use `saling berlawanan tanda` for the one awkward phrase and
`\sourcecrossref{prop:ses-vs-triangle}{...}` for the sole Bab 4 label that is
not yet in the cumulative wrapper. Add `rotation axiom` / `aksioma rotasi` as
the only new term, bringing both terminology ledgers to 428 rows. These are
translation/backend presentation repairs, not corrections to the mathematical
source; the source-correction ledger remains at O014-C043. Proceed to backend
integration and a clean cumulative build.

## D097 - Bound the Unit 037 Figshare retry (2026-08-24)

Perform one authenticated preflight against the existing Figshare article,
project, and collection only. Stop before mutation because the account and
project endpoints both return `403 Inactive/disabled account`; do not create a
replacement article or misstate the public boundary. Preserve the exact Unit
037 bytes on the already verified GitHub and Zenodo surfaces. Receipt
`release/figshare/unit-037/FIGSHARE_PUBLICATION_RECEIPT.json` records zero
uploads, zero metadata mutations, and zero new or competing items.

## D098 - Archive only confirmed-disposable O014 artifacts (2026-08-24)

Pause Unit 038 production and archive only task-owned artifacts already
superseded by canonical sources, admitted QA evidence, and public release
receipts: reproducible Unit 001--037 build trees, the stray duplicate Unit 028
build tree under `source/id-ID/build`, completed release staging/readback trees,
temporary Zenodo transaction responses for Units 028--029, and superseded draft
fragments or one-off QA scripts. Preserve the active
`build/cumulative-unit-038-finalA-20260824` tree, `build/upstream-replay`, all
canonical translated sources, source slices, segment maps, terminology and
backend ledgers, controls, receipts, final release artifacts, and credentials.

The no-overwrite archive is
`C:/Users/the user/Documents/interlanguage/old stuff/o014_methods_of_algebra_v2_obsolete_builds_readbacks_01a02164_20260824-222605.zip`:
692,700,671 bytes, SHA-256
`dfccec87a0f8bc71767709969803649cc795ef2b47276de49a4812aa7098cf34`.
Its `_cleanup_roots.txt` gives the exact 150 archived/deleted roots and
`_cleanup_manifest.csv` gives every one of the 5,287 source-relative paths,
byte counts, and SHA-256 hashes. Independent post-write verification reopened
all 5,289 ZIP entries and found zero missing, extra, size-mismatched, or
hash-mismatched payload entries. Only then were the 150 exact loose roots
deleted. Loose bytes removed: 762,133,538; net disk recovery after retaining
the archive: 69,432,867 bytes; surviving selected roots: zero.

## D099 - Admit Unit 038 and advance the exact source cursor (2026-08-24)

Admit `o014.aljabr2.chapter3.mapping-cone-and-long-exact-sequences` after
independent structural and semantic passes plus the clean finalD reader build.
The final target is 25,357 bytes, SHA-256
`85971b03546ce646f434602b3af499be7244fab17fa5944ed5987618a06ee2d1`.
It preserves all 63 stable segments, thirteen labels, 43 reference occurrences,
two citations, sixteen TikZ-CD diagrams with 139 arrows, and twelve list items.
The colon heading and four display reflows are presentation-only changes that
remove all overfull lines; independent normalized comparison proves that no
map, composition, factor, sign, label, citation, or logical claim changed. No
source correction is added.

Update Unit 038 in `backend/units.jsonl` to the final target hash and status
`translated_built_qa_passed`, and declare the exact Unit 039 successor. The
resulting 38-row unit backend is 28,564 bytes, SHA-256
`c6d57531805acfb61275ead07455afd7a27c4d448ecd7c4b440abfa4dee72d51`.
The 1,962-row segment backend is 575,630 bytes, SHA-256
`3f09a22da6f742859bbaba24721f78d1deb88f0bc3a7ad909820dc326148bbc5`;
its 63 Unit 038 rows exactly equal the frozen map. Both terminology surfaces
hold 428 matching concepts.

Admit `build/cumulative-unit-038-finalD-20260824`. The converged log has no
TeX/package error, unresolved control/reference/citation, rerun request,
overfull box, missing character/included file, fatal error, or emergency stop.
The build, checkpoint, and promoted cumulative PDF are byte-identical: 231
pages, 1,162,756 bytes, SHA-256
`71293cdd594e6df12ddf7ea0c1ca74518e1a0ca5da530f91934a562426702a07`.
All 808 links are classified and all 796 internal targets resolve. The reader
is untagged; eleven of 52 embedded mathematical font rows lack ToUnicode, so
full semantic accessibility is not claimed. Fresh visual inspection of cover,
attribution, all Unit 038 pages, bibliography, and indexes passes with normal
page fill and no clipping or collision.

QA receipt `qa/UNIT_038_QA.md` is 9,568 bytes, SHA-256
`b012592ff91252b1dbb8fdbc880f3d8197170afcbe3a6c40e16cb5042e10c02e`.
The exact 75-row manifest
`qa/CUMULATIVE_UNIT_038_FILE_MANIFEST.csv` lists 8,443,225 bytes, is 9,470
bytes, SHA-256
`ca514d36eeea7489242ffc2b3aab685858c9805bcaa0ab5b8a103cd3be399b34`,
and verifies with zero missing, duplicate, byte-count, or hash defect.

Advance the production cursor to Unit 039,
`o014.aljabr2.chapter3.exercises-hochschild-homology-and-cohomology`, exactly
`chapter3.tex` lines 1293--1586, stopping before
`sec:truncation-functors` at line 1587. The source witness and stable map remain
the next production action. Public preservation remains truthfully at Unit 037
until the already authorized Unit 038 GitHub and Zenodo transactions complete.
This admission remains partial and does not complete the corpus pursuit.

## D100 - Publish and anonymously verify the Unit 038 boundary (2026-08-24)

Advance the existing GitHub edition repository without creating a replacement
repository or contacting upstream. The initial content commit
`b101791b45e96e6aa033ade7e7e71c908820c7cc` published the reader and exact
Unit 038 source/backend/provenance closure. Its first anonymous archive audit
correctly rejected four inventory rows derived from CRLF checkout bytes rather
than Git's LF-normalized canonical blobs. Correct only those rows and accept
final commit `e129fc737546c3778eba6a96f975309fbe14c57b`, tree
`c033468e6edb1af5cc40d47c1a738f2e71020f45`, after a complete second readback.
The 1,771,050-byte archive has SHA-256
`c23ec8c757b6a8a86d5ec0749179ca8f526a16a3a0afd91125410f383b259f4d`,
contains exactly 115 expected files, and verifies all 113 manifest/checksum
payload rows with zero defect. The raw 231-page reader matches the admitted
1,162,756 bytes and SHA-256
`71293cdd594e6df12ddf7ea0c1ca74518e1a0ca5da530f91934a562426702a07`.
Sanitized receipt hash:
`a9b240310577020f9eb2d9dfd2b7ba0cca9c2b364e91dc9a22d59b68e6d7c817`.

Advance only existing Zenodo concept 22059751 from record 22086560 to
published record 22087331, DOI `10.5281/zenodo.22087331`, version `unit-038`.
The seven reader-first files total 1,562,324 bytes: PDF 1,162,756 /
`71293cdd594e6df12ddf7ea0c1ca74518e1a0ca5da530f91934a562426702a07`;
source/backend ZIP 318,266 /
`3872d931085130d8a379c6a6c0314e7b4947c1c9dd8a8a96738a03c92348bdea`;
QA/provenance ZIP 55,888 /
`e82355b12d38d945d395a1f1b7b819eef969bc4a252e89200155fe337a7ffc8c`;
LICENSE 19,045 /
`48a83a6e39f7b2f166763b30776132c9a99aa816f17cb06f87ad5b8542a7b71f`;
README 3,081 /
`9d8de19fe144a9e203e397773749305f67f9f5c10cd866d4291b5a9173ad19d1`;
release manifest 2,686 /
`5780098d447dcad2c801977c02a372ec443137ccd6140adc5d1ff76c62138e90`;
and checksums 602 /
`b3cc27a06959d94ee7ddc02a0935070cbdbda93316a5d6ac58bd8c716fe8242d`.
Anonymous record API/page, record DOI, concept DOI/latest API, and every-file
byte/hash readback pass. Metadata preserves the exact title, author, license,
language, one established organization contributor, non-endorsement, and
model disclosure without placing the organization label in the title or
description. No residual draft or competing concept exists. Sanitized receipt
hash: `ab21198f8c86c6d377d5afcb710ebe076c764a1cce36e84d5e312341f709ec3a`.

Perform one bounded Figshare preflight after both successful publications.
Stop before mutation because authenticated account and project endpoints both
return `403 Inactive/disabled account`; do not duplicate the existing article.
Receipt hash:
`22fbf23546b7602739202cc14ffa38934afffd18bccd8dbcf785662bf7c6dc68`.
GitHub and Zenodo now preserve the exact Unit 038 boundary. Continue at Unit
039; the overall corpus pursuit remains active.

## D101 - Remove recreatable post-release transaction/render transients (2026-08-24)

After both public readbacks and sanitized receipts passed, remove only five
exact task-owned transient targets that are fully recreatable and excluded from
the canonical admission/release manifests: the temporary GitHub archive/raw
readback directory (2,976,910 bytes), the temporary Zenodo seven-file readback
directory (1,562,324 bytes), the superseded 328-byte Zenodo transaction-state
file, and the finalD individual-page render directories (3,408,834 and 306,938
bytes). Total transient bytes removed: 8,255,334. Preserve the finalD build,
promoted PDFs, three admitted contact sheets, source/backend packages, public
receipts, manifests, controls, and all canonical production files.

## D102 - Archive the escaped literal-dollar-out failed build log (2026-08-24)

The bounded task-root check found one additional obsolete artifact: the
literal directory `$out`, containing only the 1,111-byte failed Unit 025 log
`Al-jabr-2-id-cumulative-through-unit-025.log` (SHA-256
`2d1eaf4ef111bd8647c8e788baff24971fe99f1c3ea2cc1318628f81439556eb`).
Archive that exact file, without overwrite, as
`[workspace]\old stuff\o014_literal-dollar-out_failed-unit025-log_01a02164_20260824.zip`.
The ZIP is 824 bytes with SHA-256
`f6aad85381e98388d129b63bdb2c7a1263447216105141beaddb2212f0ebc7db`.
Its sole entry has the expected name, 1,111 bytes, and the exact source hash;
after this byte/hash verification, delete only the archived log and its now
empty literal `$out` directory. Canonical sources, builds, readers, manifests,
receipts, controls, and Unit 039 work remain untouched.

## D103 - Admit Unit 039 and advance to truncation functors (2026-08-25)

Admit `o014.aljabr2.chapter3.exercises-hochschild-homology-and-cohomology`,
the complete `chapter3.tex` lines 1293--1586 / Section 3.8. The frozen
22,932-byte slice has SHA-256
`d94462e5d3d2868d7f6de812d6b888c927eb5c8611d52dcfb3a6b9104550325c`;
the 82-record map has SHA-256
`e7fe543ff2f5165924a3dd4fe99e6d6bb00417e9f76e3dbca4ef2b1195c9ad08`;
and the audited 35,023-byte Indonesian target has SHA-256
`641c391d6a11b0d5276070b14253278a194ab820e2850d3be8223a6bf953d254`.
Independent fidelity, mathematical, structural, and post-layout audits pass
all 82 segments, the complete formula/diagram topology, twelve labels,
thirteen references, three citation keys, 24 index commands, and zero active
Han residue. Replace seven Unicode smart-quote pairs with TeX-native quoting
to remove CJK glue without changing semantics.

Disclose and admit source repairs O014-C044--C049: the surplus tensor factor,
dual-boundary index, undeclared two-argument Hochschild notation, reversed
complex arguments, chain-homology wording, and `R^vee` coefficient in the
cohomological SBI sequence. No upstream contact occurs. Add twenty first-use
terminology concepts, bringing both exact-matching terminology surfaces to
448 rows. Admit the 39-unit / 2,044-segment backend at SHA-256
`96d4bce4db97ba7cb737300eecdbb75ded1c4de974e54d1f501e2d046c57ccce`
and
`688d32abdc574c69c82c83f9b03ef9e2679ab7e70fc22f01df4d0083b5d8a0fa`.

The first invocation of the newly named finalC directory omitted the required
source search path and stopped before producing pages; delete that exact
2,281-byte recreatable failed directory, then replay in a fresh finalC
directory with `TEXINPUTS` and `BIBINPUTS` bound to `source/id-ID`. Admit the
shell-escape-disabled finalC build after Biber, both MakeIndex passes, and
converged XeLaTeX passes. The final log has zero error, undefined
reference/citation, rerun request, overflow, missing character, or fatal stop.
The 243-page, 1,210,711-byte PDF has SHA-256
`11cabff2db7b4bdb1abaaf29be78a37fd5e16b4dd08b30f6debf88742f026f6a`;
all 1,049 destinations and 831 links validate, all 52 fonts are embedded, and
fresh exact renders pass. The finalC rebuild corrects the stale cover claim
from Section 3.7 to Section 3.8; pages 2--243 retain identical decompressed
content streams to the otherwise valid finalB candidate.

QA receipt `qa/UNIT_039_QA.md` is 9,656 bytes, SHA-256
`53a9b5b309ecc0ba1648781e1bf858a26d835414a01ab165aff3dbd8ec2f4bcf`.
The exact 76-row manifest lists 7,592,101 bytes, is 9,591 bytes, SHA-256
`6c74c75ecbab1a4465b9cd65be2670fbc68bf9c3382242cc9503b26a121de972`,
and re-verifies with zero mismatch. Advance to Unit 040,
`o014.aljabr2.chapter3.truncation-functors`, exactly lines 1587--1709,
stopping before `sec:double-cplx-coh` at line 1710. This admission remains a
partial corpus checkpoint.

## D104 - Archive superseded Unit 039 build and render transients (2026-08-25)

After finalC admission, archive 136 exact task-owned files from the superseded
preflight, finalA, and finalB build directories; the finalA and finalB render
trees; the finalC individual-page render directories; and the finalC console
captures. Their total loose size is 17,918,924 bytes. The no-overwrite archive
is
`[workspace]\old stuff\o014_unit039_superseded_builds_and_render_transients_01a02164_20260825-004808.zip`,
15,908,977 bytes, SHA-256
`3d180c3baea9e3a266159b41867dcf70e666350b5f225e0d93e91b8e3558bbf4`.
Its 136 payload entries plus `_cleanup_manifest.csv` open successfully; every
entry name, byte count, and SHA-256 re-verifies with zero mismatch. Delete only
the eighteen exact archived roots/files after verification. Retain the finalC
canonical build artifacts, all three finalC contact sheets, Unit 039 source
witness/map/translation, backend, controls, QA/manifest, and both promoted
PDFs.

## D105 - Publish and anonymously verify the Unit 039 boundary (2026-08-25)

Advance the existing corpus-specific GitHub edition repository from commit
`e129fc737546c3778eba6a96f975309fbe14c57b` to commit
`37ead420edf108b4974a6a040812406fc12df039`, tree
`459b2f6c28e84ffab9f22a0aa153d2e058d9f67a`; create neither a replacement
repository nor an upstream message. Before commit, validate all 118 canonical
payload blobs against `MANIFEST.csv` and `SHA256SUMS.txt`, and reject any
credential pattern, private user path, personal name, future-unit byte, or
stray organization-label prose. The immutable public archive contains 120
files, is 1,856,390 bytes, SHA-256
`3f196257bca21fd76662998e16bedb0ba288c302e310d4d00988ba0cda1361df`.
Credential-free repository, commit, archive, raw manifest, raw sums, README,
and reader requests all return HTTP 200; all 118 payload bytes/hashes and the
API tree match. The public PDF is the admitted 243-page, 1,210,711-byte reader
with SHA-256
`11cabff2db7b4bdb1abaaf29be78a37fd5e16b4dd08b30f6debf88742f026f6a`.
Sanitized GitHub receipt hash:
`797663d6c3a7e4ddab4295ce565d0a46d23da2645a72ca52ebdc4ba71ef80095`.

Advance only existing Zenodo concept 22059751 from record 22087331 to
published record 22088565, DOI `10.5281/zenodo.22088565`, version `unit-039`.
Its seven reader-first files total 1,627,091 bytes: PDF 1,210,711 /
`11cabff2db7b4bdb1abaaf29be78a37fd5e16b4dd08b30f6debf88742f026f6a`;
source/backend ZIP 331,518 /
`9efecda69ff29161d56e1a8655af1a374b10870c2bee98a4e716ff5a42bf70c0`;
QA/provenance ZIP 59,438 /
`fef149ff3a832faa225700a41840229a0f413ed90a60124da5a5dd21ee1dfc6a`;
LICENSE 19,045 /
`48a83a6e39f7b2f166763b30776132c9a99aa816f17cb06f87ad5b8542a7b71f`;
README 3,074 /
`c06c8d5e95f777566210234b9288e019511ade7b2b8f114a165b6eb60f5730eb`;
release manifest 2,703 /
`40a80e6f883d1331be8cae1d032fd91bcdf12e79916a8acc76eb5700446d2251`;
and checksums 602 /
`c23d7aaed1956a80e89d769a609e011c1502c31532f36023bb9ac8f77c1d70a0`.
Anonymous record API/page, record DOI, concept DOI/latest API, and every-file
byte/hash readback pass. Metadata preserves the exact title, source author,
license, language, one established organization contributor,
non-endorsement, and exact model disclosure without placing the organization
label in the title or description. No residual draft or competing concept
exists. Sanitized Zenodo receipt hash:
`f842947a29c953bcbeff661f4d5681403b867735bac09064e65eb7528e31531b`.

After both sanitized receipts exist, remove only the exact credential-free
GitHub and Zenodo readback directories (122 files / 5,419,007 bytes and eight
files / 1,636,472 bytes respectively). These are recreatable transaction
transients; preserve the public releases, local release packages, receipts,
canonical build, source/backend, QA, and contact sheets. Do not repeat the
known inactive-account Figshare mutation attempt. Continue at Unit 040; the
overall corpus pursuit remains active.

## D106 - Archive the failed literal-output Unit 040 build (2026-08-25)

The first Unit 040 build invocation passed PowerShell's `-output-directory`
argument in an expansion-unsafe form, so XeLaTeX wrote its incomplete first
pass to the literal task-local directory `$out`; the intended finalA directory
contained only console captures. Stop the process before Biber or later passes
can mutate either root. Archive exactly those two disposable roots as eleven
files / 1,651,491 bytes in
`[workspace]\old stuff\o014_unit040_failed_literal-output-build_01a02164_20260825-034221.zip`,
1,208,059 bytes, SHA-256
`3b98158aeb8ad61ad818d352f340f7d8145a6fc2a8199ca7cd2cbf5bfddb83f7`.
The ZIP contains an internal cleanup manifest and re-verifies every entry name,
uncompressed byte count, and SHA-256 with zero mismatch. Delete only the exact
loose roots after verification. Replay the build in a fresh directory with
`-output-directory` and its path supplied as separate command tokens.

## D107 - Admit Unit 040 and advance to double-complex cohomology (2026-08-25)

Admit `o014.aljabr2.chapter3.truncation-functors`, the complete Section 3.9,
`chapter3.tex` lines 1587--1709. The frozen 10,217-byte source slice has
SHA-256
`7954b37ef2279d82e9ce3d8e56f6ce218ccd839970a684189b6315a3f67a48be`;
the 33-record map has SHA-256
`d2488a8f085baec85fbfc199198db009f9b85f0da996533ec12dde64dd2e62a2`;
and the final 14,865-byte Indonesian target has SHA-256
`073c9ddbc20430ecb37ee80658f73f5b20756919ec38ffe7807c77130291c9b0`.
Independent mathematical, fidelity, language, and final-delta reviews pass all
segments, formulas, labels, references, environment topology, diagram arrows,
and indexes.

Disclose O014-C050--C053 for the missing Abelian hypothesis, ambiguous
comparison-map antecedent, Coim/Image component typing, and wrong object
category. Add three bounded-complex terminology concepts, producing 451
exact-matching terminology rows. Admit the 40-unit / 2,077-segment backend at
SHA-256
`7c3534c6955fa74aff5adb0adfc57a5c554dc5f3f57f642debf92d38f2acc139`
and
`62cd5765fadc9c534753a010b542b9139b99fbffaf9bb92d347b4601eb860dd9`.

The finalB build exposed a 21.86-point overflow in the four-column boundedness
table and a 0.67-point overflow in the long duality identity. Apply only local
presentation changes: smaller table spacing and a display treatment for the
unchanged duality identity. FinalC confirms the table repair but retains the
duality overflow; finalD is a fresh complete replay and has zero overflow.
Admit finalD after Biber, both MakeIndex passes, and converged XeLaTeX passes.
Its final log has zero error, undefined reference/citation, rerun request,
overflow, missing character, or fatal stop. The 247-page PDF is 1,230,437
bytes, SHA-256
`15976f12f8a401766cfeca2d446abd780ced1ddeedf812b2e65204d346b73ebf`;
all 1,070 named destinations and 843 actions resolve/parse, all 52 font rows
are embedded, and fresh full-size renders pass.

QA receipt `qa/UNIT_040_QA.md` is 9,489 bytes, SHA-256
`e7eab8020a62d6a1994212742e73b573de6520f92ffed8ec1c412e8e49171705`.
The exact 77-row manifest lists 12,119,914 bytes, is 9,716 bytes, SHA-256
`70afa2bf1a259fd69333bb61ca9e863e0b95b47341b2924515d6d6b27cc95a88`,
and re-verifies with zero mismatch. Advance to Unit 041,
`o014.aljabr2.chapter3.double-complex-cohomology`, exactly lines 1710--1881,
stopping before `sec:resolutions` at line 1882. This remains a partial corpus
checkpoint; publish it through the existing GitHub and Zenodo lineages before
continuing production.

## D108 - Archive superseded Unit 040 builds and inspected render transients (2026-08-25)

After finalD admission and full-size visual inspection, archive exactly the
superseded finalB and finalC build trees, the 19 individual rendered page PNGs,
and seven redundant finalD console captures. The 70 task-owned files total
5,984,538 loose bytes. The no-overwrite archive is
`[workspace]\old stuff\o014_unit040_superseded_builds_and_render_transients_01a02164_20260825-041115.zip`,
4,665,068 bytes, SHA-256
`3762c561607547799ab7ac1a86f48342ca2dc59bf1c0e94a9ccf2f477727b732`.
Its 70 payload entries plus internal cleanup manifest open successfully; every
entry name, uncompressed byte count, and SHA-256 re-verifies with zero
mismatch. Delete only the exact archived loose roots/files after verification.
Retain the complete finalD canonical build artifacts, three contact sheets,
source witness/map/translation, backend, controls, QA/manifest, promoted PDFs,
and publication materials.

## D109 - Archive superseded Unit 038 candidate builds (2026-08-25)

At the explicit cleanup boundary, archive only the three superseded Unit 038
candidate build trees `cumulative-unit-038-finalA-20260824`,
`cumulative-unit-038-finalB-20260824`, and
`cumulative-unit-038-finalC-20260824`. Their 45 files total 6,086,501 loose
bytes. The no-overwrite archive is
`old stuff/o014_unit038_superseded_candidate_builds_01a02164_20260825-041840.zip`,
5,028,153 bytes, SHA-256
`7db65aee4716316fa7dab0528db6c6ca8dea97cfc424a3500e51a71f2df948ea`.
The archive opened successfully and every entry name, uncompressed byte count,
and SHA-256 matched the pre-archive inventory before deletion. Retain the
successful Unit 038 finalD build, successful Unit 039 finalC build, current
Unit 040 finalD build, all source witnesses/maps, QA contacts, canonical
outputs, release packages, receipts, and the active publication worktree.

## D110 - Publish and anonymously verify Unit 040 (2026-08-25)

Advance the existing GitHub repository and Zenodo concept with the admitted
Unit 040 snapshot; do not create a competing lineage. The first GitHub commit
`4a2e1e28ab2668173b8a6fce8c241f146808293b` preserved the correct reader and
content bytes, but anonymous archive readback exposed three checksum rows that
described CRLF worktree bytes instead of Git's LF-normalized public blobs.
Correct only those inventory rows and publish final commit
`cd61ef96eda025a072deffbe98de451ef236dc05`, tree
`fb94b4915b3f8920ef1b47f4eac5a2aa9dae31bb`. Its 1,903,798-byte immutable
archive has SHA-256
`adb26734ceaae10a01af0f292e682671b2e561331507385f345eb275dd3d301f`;
all 123 payloads then pass anonymous manifest/checksum readback with zero
mismatch, and the public PDF remains byte-identical to the admitted reader.

Advance Zenodo concept record `22059751` from immutable Unit 039 record
`22088565` to published Unit 040 record `22096566`, DOI
`10.5281/zenodo.22096566`. Publish exactly seven reader-first files totaling
1,658,212 bytes: the 247-page PDF, compact 40-unit source/backend ZIP, compact
QA/provenance ZIP including the exact Unit 040 slice and map, CC BY 4.0
license, README, release manifest, and checksum list. Anonymous readback of
the public API, page, both DOI routes, all seven files, both ZIP internal
manifests, and PDF properties passes with zero mismatch. Keep the complete
corpus pursuit active and continue at Unit 041, `chapter3.tex` line 1710.

## D111 - Archive redundant Unit 040 public readbacks (2026-08-25)

Once the sanitized GitHub and Zenodo receipts independently captured the full
public identities, archive the two task-local GitHub readback directories and
the task-local Zenodo readback directory as redundant loose evidence. Their 13
files total 7,932,488 bytes. The no-overwrite archive is
`old stuff/o014_unit040_public_readbacks_01a02164_20260825-151616.zip`,
7,685,984 bytes, SHA-256
`18eaaafbc65c8e7b7c7526641621f6b85bcea4d866b14b35bb94296dbc430358`.
The archive opens and every entry name, uncompressed byte count, and SHA-256
matches before exact-root deletion. Retain both local release packages,
sanitized receipts, canonical source/backend/controls, and the public records.

## D112 - Archive superseded Unit 038--039 builds and renders (2026-08-25)

At the explicit cleanup boundary, archive only the admitted-but-now-superseded
Unit 038 finalD and Unit 039 finalC build trees and their rendered-page sets.
The four exact task-local directories contain 36 files / 8,287,867 loose bytes.
The no-overwrite archive is
`[workspace]\old stuff\o014_superseded_unit038-039_builds_and_renders_01a02164_20260825-154253.zip`,
7,290,676 bytes, SHA-256
`833bccd43e990ddf2ad967c0a08cfc84277f5614c665b60c03c00409ceb702d2`.
The archive opens and every entry name, uncompressed byte count, and SHA-256
matches the pre-archive inventory before deletion. Delete only
`build/cumulative-unit-038-finalD-20260824`,
`build/cumulative-unit-039-finalC-20260825`, `tmp/pdfs/unit038-finalD`, and
`tmp/pdfs/unit039-finalC`. Retain the canonical Unit 040 finalD build, its
render evidence, all Unit 041 work, source witnesses and maps, controls,
backend, QA records, release packages, receipts, and upstream replay.

## D113 - Archive superseded Unit 041 candidates and renders (2026-08-25)

After finalD admission, archive the three superseded Unit 041 build candidates
finalA, finalB, and finalC together with the obsolete finalC render set. The
four exact task-local directories contain 100 files / 10,539,388 loose bytes.
The no-overwrite archive is
`[workspace]\old stuff\o014_unit041_superseded_builds_and_renders_01a02164_20260825-161628.zip`,
8,798,871 bytes, SHA-256
`f2cf861907e647d9177784ca0f045fcff8f077a1552ad007a91f02c3422f30ed`.
The archive opens and every entry name, uncompressed byte count, and SHA-256
matches before exact-root deletion. Retain the finalD build, finalD render
evidence, promoted PDFs, sources, backend, controls, QA, and release materials.

## D114 - Admit Unit 041 and advance the local cumulative reader (2026-08-25)

Admit `o014.aljabr2.chapter3.double-complex-cohomology`, the complete
`chapter3.tex` lines 1710--1881. Preserve the 43-record stable map, all formulas,
ten labels, 24 cross-reference commands, `KS06`, five symbol indexes, seven
TikZ-CD diagrams, and 36 arrows. Disclose O014-C054 for the missing evaluation
at `X` and O014-C055 for the source's overstrong isomorphism symbol. Reflow the
long cone-object formula and move crowded quasi-isomorphism properties from
two diagrams into adjacent prose after full-size render inspection; independent
delta review confirms no semantic or topological change.

Admit `build/cumulative-unit-041-finalD-20260825`: Biber resolves 21 citekeys,
MakeIndex accepts 182 terminology and 93 symbol entries, and the final log has
zero error, unresolved reference/citation, rerun request, overfull box, missing
character, or fatal stop. Promote the byte-identical 253-page PDF, 1,255,777
bytes, SHA-256
`f364d2c3b6839a14b89f77313f9e3117dc9b7b5e5ad920d27637924513d5a29f`.
The 78-row manifest re-verifies with zero mismatch. Advance the next cursor to
Unit 042, `sec:resolutions`, lines 1882--2214, but keep the corpus pursuit
active and publish this worthwhile boundary through the existing GitHub and
Zenodo lineages before continuing.

## D115 - Publish and anonymously verify Unit 041 (2026-08-25)

Advance the existing GitHub repository and Zenodo concept with the admitted
Unit 041 snapshot; create no competing lineage. The first Unit 041 GitHub
commit exposed task-local absolute archive paths in two provenance files.
Because the PDF and mathematical sources were unaffected, sanitize those
provenance-only strings, repair the mutable cursor's Unit 041 QA pointer,
regenerate the public manifest and checksum inventory, amend the Unit 041
commit, and replace the branch head with force-with-lease.

The final GitHub head is commit
`98bc2fec01c8e7a1e987f46cfaf519e9b9ee2e6c`, tree
`ad28c286f4e07ffc847fff339d2c509f49ed099e`. Its 1,957,201-byte immutable
archive has SHA-256
`3badbdddb20a602a208ddce629fb17a6d96d0850bb616b8a3761fd9a261a7b2e`.
Anonymous readback proves 128 manifest payloads and 128 checksum rows with
zero missing, unlisted, duplicate, byte, or hash mismatch; it also proves zero
private-path/name match and exact identity of the 1,255,777-byte reader.

Advance Zenodo concept record `22059751` from immutable Unit 040 record
`22096566` to published Unit 041 record `22098141`, DOI
`10.5281/zenodo.22098141`. Publish exactly seven files totaling 1,693,098
bytes: the 253-page reader, compact 41-unit source/backend ZIP, compact
QA/provenance ZIP with the exact Unit 041 slice and segment map, CC BY 4.0
license, README, release manifest, and checksums. Preserve the exact title,
single organization-contributor entry, source attribution, modification
notice, non-endorsement, partial-status claim, and precise model disclosure.
Anonymous per-file, record, DOI, concept-DOI, and concept-latest readback passes
with zero mismatch.

## D116 - Archive redundant Unit 041 public readbacks (2026-08-25)

Once both sanitized receipts captured the final public identities, archive
only the two GitHub readback directories and one Zenodo readback directory.
Their 274 files total 15,679,484 loose bytes. The no-overwrite archive is
`old stuff/o014_unit041_public_readbacks_01a02164_20260825-165331.zip`,
11,796,299 bytes, SHA-256
`4c7e83208853f83e14e7a7b2dfc65395171a6b2a540c939dc9eefb11979a4a87`.
The ZIP opens and every entry name, uncompressed byte count, and SHA-256
matches before deletion of the three exact task-local roots. Retain the
canonical Unit 041 packages, sanitized receipts, finalD build/render evidence,
source witnesses and maps, controls, backend, QA, and promoted PDF.

## D117 - Admit Unit 042 and freeze the Unit 043 boundary (2026-08-25)

Admit `o014.aljabr2.chapter3.resolutions`, the complete
`chapter3.tex` lines 1882--2214. Preserve its 102-record stable map, 15
labels, 31 live cross-references plus two explicit source-number forward
references, seven equation references, five symbol-index entries, 21 item
nodes, thirteen diagrams, and 90 arrows. Disclose O014-C056 through O014-C059
for the undefined base-step cokernel, wrong diagram object, ill-typed matrix
entry, and repeated vertical arrow. Independent semantic and delta review
confirms these repairs and the natural Indonesian text.

Admit `build/cumulative-unit-042-finalD-20260825`: Biber resolves 21
citekeys, MakeIndex accepts 187 terminology and 93 symbol entries, and the
final log has zero error, unresolved reference/citation, rerun request,
overfull box, missing character, or fatal stop. Promote the byte-identical
265-page PDF, 1,309,971 bytes, SHA-256
`11037fbd52c9bdea1b18a449fbf8395f89ad6716b4c080035565ffc71f2d7491`.
Fresh full-size page inspection passes, with the untagged/ToUnicode
accessibility limitation stated explicitly. The final 79-row manifest,
9,947 bytes, SHA-256
`829961cb5e76ad4a031d06240b14084acccbea50092eaded5cf1f7709197ffae`,
re-verifies 10,952,634 listed bytes with zero mismatch.

Freeze the next source-order boundary as Unit 043,
`o014.aljabr2.chapter3.classical-derived-functors`,
`chapter3.tex` lines 2215--2552, stopping before `sec:lim1` at line
2553. Reserve O014-C060 and O014-C061 for the two typed source anomalies
identified at lines 2345--2346 and 2538--2539. Keep the full corpus pursuit
active and publish Unit 042 through the existing GitHub and Zenodo lineages
before translating this next unit.

## D118 - Publish and anonymously verify Unit 042 (2026-08-25)

Advance the existing GitHub repository and Zenodo concept with the admitted
Unit 042 snapshot; create no competing lineage and expose no Unit 043 source
or correction beyond O014-C059. Fast-forward GitHub `main` from
`98bc2fec01c8e7a1e987f46cfaf519e9b9ee2e6c` to commit
`3a8062fb77b60c456f560523508885445db57c3a`, tree
`147809a3a936e447a20d4287dcd818a8be2610e0`. The immutable 2,044,848-byte
codeload archive has SHA-256
`c576bbc934cfe7a387aff1e5140023a28f6fe838ef04e0d6b503ad84ce35dd48`.
Anonymous HTML, raw, and archive readback verifies all 133 payload manifest
rows and 133 checksum rows with zero mismatch; the 265-page public PDF remains
byte-identical to the admitted reader.

Advance Zenodo concept record `22059751` from immutable Unit 041 record
`22098141` to published Unit 042 record `22102326`, DOI
`10.5281/zenodo.22102326`. Publish exactly seven files totaling 1,774,270
bytes: the reader, 60-entry source/backend ZIP, 11-entry QA/provenance ZIP,
CC BY 4.0 license, README, release manifest, and checksum list. Preserve the
exact title, one organization-contributor entry, source attribution,
modification notice, non-endorsement, partial-status claim, and exact model
disclosure; keep the organization label out of title and descriptive prose.
Anonymous record, page, both DOI routes, concept-latest, every file, both ZIP
manifests, and PDF properties pass with zero mismatch. Keep the full corpus
pursuit active and begin Unit 043 at `chapter3.tex` line 2215.

## D119 - Admit Unit 043 and freeze the Unit 044 boundary (2026-08-26)

Admit `o014.aljabr2.chapter3.classical-derived-functors` as the complete
Section 3.12, `chapter3.tex` lines 2215--2552, stopping before
`sec:lim1` at line 2553. Freeze the normalized 338-line authority witness at
27,132 bytes / SHA-256
`ac95a737c3df39dff8ece789057d2ad3ce93474b258476245b2fcc67d074dbb9`,
the 105-record map at 32,475 bytes / SHA-256
`2712c57d9a9066fb1a119037857552c0c331abd20d91c86a3c41c56de1a542cd`,
and the final Indonesian target at 40,571 bytes / SHA-256
`80d7ba5a71f45c418ac8278ac03ee6409d23bc7bc48dcf52310096d0ae153d54`.
Independent block review and the final deterministic replay pass. Disclose
O014-C060 through O014-C062 exactly once each; these restore two diagram
objects, two connecting-morphism degrees, and the intended `n >= 1`
zero-extension boundary.

Synchronize the terminology stores at 467 exact-matching concepts and the
backend at 43 unique units / 2,327 unique segments. Keep effaceable and
coeffaceable active, but retain hyperderived as provisional because this
source-internal recurrence is not external Indonesian field attestation.

Admit `build/cumulative-unit-043-finalD-20260825`. Biber resolves 21
citekeys, MakeIndex accepts 195 terminology and 95 symbol entries, and the
final log has zero TeX/package error, undefined reference/citation, rerun
request, overfull box, missing character, or fatal stop. Promote the
byte-identical 275-page reader, 1,361,656 bytes, SHA-256
`15a22aa8f55fefd7ba0d10840e3719bd3718d6af6ceda63eedf919db24250ac1`.
Strict PDF checks and full-size inspection of every new page and the complete
backmatter pass, with the untagged/ToUnicode limitation stated explicitly.

The final 80-row manifest lists 8,342,643 bytes, is 10,069 bytes, SHA-256
`ea52868bcecc97dabd75ac6a0935f1bbefb5ffe2f07fca7aec3cabc23fe2822c`,
and re-verifies with zero mismatch. Freeze Unit 044,
`o014.aljabr2.chapter3.example-lim1`, as complete `chapter3.tex` lines
2553--2713, content through line 2712, stopping before `sec:Ext-Tor` at line
2714. Its normalized 161-line authority slice is 13,478 bytes, SHA-256
`2b8a923963fba1f31a9c5f7bfd98e5381a4a1b194f70cd3b7d002fa05a68298e`.
Keep the full corpus pursuit active and publish Unit 043 through the existing
GitHub and Zenodo lineages before scaling Unit 044 production.

## D120 - Publish and anonymously verify Unit 043 (2026-08-26)

Advance the existing GitHub repository and Zenodo concept with the admitted
Unit 043 snapshot; create no competing lineage and publish no Unit 044 source
or correction beyond O014-C062. GitHub `main` is immutable commit
`16da6a2d73cae5b53decb49a58b4af684ed42756`, tree
`5df51ebd754ea81c3638f6f443a81107b8b7e3ec`. Anonymous repository, commit,
raw-reader, raw-README, branch-head, and codeload checks pass. The 2,129,606-
byte codeload archive, SHA-256
`de2ae149a3fe4eaa126c15f13ba592fa11a66f72bac8cf7ceedc203245749482`,
contains all 138 manifest payload rows plus the two inventories with zero
missing, extra, size, or hash mismatch.

Advance Zenodo concept `22059751` from record `22102326` to published record
`22103241`, DOI `10.5281/zenodo.22103241`, version `unit-043`. Publish exactly
seven reader-first files totaling 1,832,410 bytes: the 275-page reader, the
61-entry source/backend ZIP, the 11-entry QA/provenance ZIP, CC BY 4.0
license, README, release manifest, and checksums. Preserve the exact work
title, source authorship, derivative notice, non-endorsement, partial status,
untagged-PDF limitation, exact model disclosure, and the single inherited
organization contributor without placing the organization label in the title
or description. Anonymous record API, record page, assigned DOI, concept DOI,
concept-latest endpoint, immutable predecessor, every public file, both ZIP
manifests, and PDF properties pass with zero mismatch. The sanitized receipt
is `release/zenodo/unit-043/ZENODO_PUBLICATION_RECEIPT.json`, 7,933 bytes,
SHA-256
`7758fba3e2cd59385437a75aed57b10378ae29f0e22b146ede3c935588b2626b`.

Close the Unit 043 release boundary and immediately resume source-order
production at Unit 044, `chapter3.tex` lines 2553--2713. This publication is
a partial preservation checkpoint and does not complete the corpus pursuit.

## D121 - Admit Unit 044 and freeze Unit 045 (2026-08-26)

Admit `o014.aljabr2.chapter3.example-lim1` as complete Section 3.13,
`chapter3.tex` lines 2553--2713, stopping before `sec:Ext-Tor` at line 2714.
The normalized 161-line witness is 13,478 bytes / SHA-256
`2b8a923963fba1f31a9c5f7bfd98e5381a4a1b194f70cd3b7d002fa05a68298e`;
the 51-record map is 14,076 bytes / SHA-256
`2c376228ea8f711b06db359ab6890b6cf866ed0af222d0ba8adcd1a039aa943f`;
the final Indonesian target is 19,317 bytes / SHA-256
`550f7c1d4f7ad08721132b59932d09e5d3eecf0203551b4e0ffcb84702e3d9fc`.
The target preserves all labels, formulas, references, indexes, and diagrams;
the sole high-confidence notation repair is O014-C063, disclosed once.

Admit `build/cumulative-unit-044-finalB-20260826`: Biber resolves 22 citekeys,
MakeIndex accepts 197 term and 98 symbol entries with zero rejection or
warning, and the final log has no undefined reference/citation or TeX error.
Promote the byte-identical 282-page reader, 1,389,564 bytes, SHA-256
`e225bfc588268d4da9bb64978ef4f00ef316e52516c8b4427ca0d838d79d6b05`.
Strict PDF checks and full-size inspection of physical pages 258--282 pass;
the untagged/ToUnicode limitation is stated explicitly. The 95-row manifest
revalidates with zero missing, duplicate, size, or hash mismatch.

Freeze Unit 045, `o014.aljabr2.chapter3.ext-tor`, as the complete next source
boundary `chapter3.tex` lines 2714--2935, content through line 2934, stopping
before `sec:K-injectives` at line 2936. Keep the full corpus pursuit active and
publish Unit 044 through the existing GitHub and Zenodo lineages before
advancing the next boundary's build.

## D122 - Publish and anonymously verify Unit 044; activate Unit 045 (2026-08-26)

Advance the existing GitHub repository and Zenodo concept with the admitted
Unit 044 snapshot; create no competing lineage and publish no Unit 045 source.
GitHub `main` is immutable commit
`e0b8335594526f773fc97d41f8916061815758a2`, tree
`71d46cf1ee43ffe2ac1ed84a5f195f5e1b1d5edd`. Its 2,185,980-byte immutable
codeload archive, SHA-256
`7561c4c91708645bab6c4fbca5e2a4b246a77ce616abd71a5e20a006febca013`,
passes anonymous repository, commit, raw-reader, raw-README, manifest,
checksum, and archive verification. The sanitized GitHub receipt is 5,881
bytes, SHA-256
`e487b1b6f51d7ca652d9521e032e36ba169b4c3e0a160bab185538db3ee8f4f9`.

Advance Zenodo concept `22059751` from immutable record `22103241` to record
`22104088`, DOI `10.5281/zenodo.22104088`, version `unit-044`. Publish exactly
seven files totaling 2,110,664 bytes: the 282-page reader, source/backend ZIP,
QA/provenance ZIP, CC BY 4.0 license, README, release manifest, and checksums.
Preserve the exact work title, source authorship, derivative notice,
non-endorsement, partial status, untagged-PDF limitation, exact model
disclosure, and single inherited organization contributor. Anonymous record,
page, version DOI, concept DOI, concept-latest, predecessor, every file, both
ZIP manifests, and the exact PDF properties pass with zero mismatch. The
sanitized Zenodo receipt is
`release/zenodo/unit-044/ZENODO_PUBLICATION_RECEIPT.json`, 5,480 bytes,
SHA-256
`65e6fb9070e698f2c225036bd4d5b177a19a1c2dc829b7df09a65ba2341365b2`.

Close the Unit 044 release boundary and activate Unit 045,
`o014.aljabr2.chapter3.ext-tor`, exactly at `chapter3.tex` lines 2714--2935.
Its target has passed independent structural preflight and its future Chapter
4 reference uses `\sourcecrossref{sec:Hom-Ext}{4.5}`. Continue integration,
build, and QA without crossing into `sec:K-injectives` at line 2936. This
publication is a partial preservation checkpoint and does not complete the
corpus pursuit.

## D123 - Admit Unit 045 and freeze Unit 046 (2026-08-26)

Admit `o014.aljabr2.chapter3.ext-tor` as complete Section 3.14,
`chapter3.tex` lines 2714--2935, stopping before `sec:K-injectives` at line
2936. The normalized 222-line witness is 20,416 bytes / SHA-256
`b257f061a7a3f56f8878d1815ac430417c033ef7ff93b214abe13eccb0b1d15a`;
the 60-record map is 15,479 bytes / SHA-256
`ffcb362491af688b95c07bd0b15a75bbde5d278028795b0098387c60d0a95278`;
the final Indonesian target is 26,060 bytes / SHA-256
`348fbb2121a37a54795a0e68b6fe3c76004294f10ee6a84201e4815abb62db6d`.
Independent structural and formula-by-formula review passes. Preserve all
source mathematics and represent the sole future Chapter 4 reference using
`\sourcecrossref{sec:Hom-Ext}{4.5}`. No source-correction ledger row is needed
for this unit.

Synchronize the backend at 45 unique units / 2,438 unique segments and the
terminology stores at 477 exact-matching concepts. Admit
`build/cumulative-unit-045-finalA-20260826`: Biber resolves 22 citekeys,
MakeIndex accepts 203 terminology and 103 symbol entries, the last two
XeLaTeX transcripts are byte-identical, and the final log has no undefined
reference/citation, missing character, TeX error, or fatal stop. Promote the
byte-identical 290-page reader, 1,427,097 bytes, SHA-256
`39eee75436b826cac1e82fe5d3eb051212625f194bc32b81f2afab5350f95405`.
Strict PDF validation and full-size inspection of physical pages 1--6 and
268--290 pass, with the untagged/ToUnicode limitation stated explicitly. The
95-row manifest revalidates with zero missing, duplicate, size, or hash
mismatch.

Freeze Unit 046,
`o014.aljabr2.chapter3.k-injectives`, as complete
Section 3.15 at `chapter3.tex` lines 2936--3200, stopping before Exercises at
line 3201. Its exact witness, segment map, and initial Indonesian target are
materialized, but semantic review and three possible notation repairs remain
to be adjudicated before integration. Keep the full corpus pursuit active and
publish Unit 045 through the existing GitHub and Zenodo lineages before its
next cumulative build.

## D124 - Publish and anonymously verify Unit 045; admit the reviewed Unit 046 target (2026-08-26)

Advance the existing GitHub repository from Unit 044 commit
`e0b8335594526f773fc97d41f8916061815758a2` by one fast-forward commit only.
The Unit 045 public boundary is commit
`e072d5949d8ce0c1768c0c0e631b259db444fa8a`, tree
`ec57f1a58263ec43128be9fd20fe140e31e06295`. Its 2,252,498-byte immutable
codeload archive has SHA-256
`295232cd9d545f783fc36eeb6f4952d6590c0950dfd7b10dfe32d2a0f09b5c7f`.
Anonymous HTML, raw-file, manifest, checksum, reader, and archive verification
passes across exactly 150 files and 148 payload rows with zero mismatch and no
Unit 046 leakage. Preserve the sanitized 6,118-byte GitHub receipt, SHA-256
`01cf9e7096d98e81b50425da15a3e9068c79626eb123ded6d7338eb950c836b6`.

Advance Zenodo concept `22059751` from record `22104088` to record `22104808`,
DOI `10.5281/zenodo.22104808`, version `unit-045`, without creating a competing
concept. Publish exactly seven files totaling 2,163,607 bytes, with the exact
290-page reader first. Anonymous record, page, version DOI, concept DOI,
predecessor, every public file, both ZIP manifests, and PDF properties pass.
Preserve the exact title, Li as sole creator, CC BY 4.0, the independent
derivative/non-endorsement statement, exact model disclosure, and the one
inherited organization contributor. Preserve the sanitized 5,331-byte receipt,
SHA-256
`266e8ec7032015cbb363cd5b1f5527a53b123c27b050ae9e23241745cfd99531`.

Accept the independent Unit 046 review and disclose three inherited source
repairs as O014-C064--O014-C066. Restore `\varprojlim_k` at source line 3063,
restore `\Delta_{\tau A}` at line 3137, and normalize the undefined
`\Delta_{\tau_A}` to `\Delta_{\tau A}` at line 3145. Also enforce the settled
`homotopik` and `barisan` terminology. The reviewed target is 28,931 bytes /
SHA-256
`15f84671182c59ac6779a61968b9d03ca8f43d8625fd81399e4a44dacddbf496`.
Integrate/build/QA the exact complete Section 3.15 boundary through line 3200,
without crossing into Exercises at line 3201. This public checkpoint and target
review do not complete the corpus pursuit.

## D125 - Admit Unit 046 and freeze the Unit 047 exercise closure (2026-08-26)

Admit `o014.aljabr2.chapter3.k-injectives` as complete Section 3.15,
`chapter3.tex` lines 2936--3200, stopping before Exercises at line 3201. Freeze
the 20,086-byte authority witness at SHA-256
`5a56872f1fbdd507618130c9def1445e5689dba76d94189676a97e2a677a72e6`,
the 83-record map at 24,432 bytes / SHA-256
`64dcb930ff3a0327d9b15e6cc34764f9f41d458a25e9b5857dffdf6c322e3a1a`,
and the reviewed Indonesian target at 28,931 bytes / SHA-256
`15f84671182c59ac6779a61968b9d03ca8f43d8625fd81399e4a44dacddbf496`.
Preserve all source topology and disclose O014-C064--O014-C066 exactly once
each. Synchronize the backend at 46 units / 2,521 segments and the terminology
stores at 479 exact-matching concepts.

Admit `build/cumulative-unit-046-finalA-20260826`. Biber resolves all 25
citekeys, MakeIndex accepts 207 terminology and 103 symbol entries, and the
final log has no TeX/package error, undefined reference/citation, rerun request,
missing character, or fatal stop. Retain the seven measured overfull hboxes as
honestly recorded non-fatal warnings because full-size page-image inspection
proves that no content clips or crosses the page. Promote the byte-identical
302-page reader, 1,468,650 bytes, SHA-256
`4edebacd5d8a2f8fd62da9d9553b3b8ad3699fcd523311bae04759c7c1176bc9`.
Strict PDF validation and inspection of the front matter, every new page, and
complete backmatter pass; retain the explicit untagged/ToUnicode accessibility
limitation.

Freeze the 97-row manifest at 12,441 bytes / SHA-256
`bbad03aedeff6c06ce0e72f3fc092dc9c94a2ac50dc23f1e69dc27b0a9b78f05`;
it replays 15,977,340 listed bytes with zero mismatch and no Unit 047 payload.
Freeze Unit 047, `o014.aljabr2.chapter3.exercises`, as the complete Exercises
environment at `chapter3.tex` lines 3201--3425 and the end of the file. Its
18,004-byte normalized witness has SHA-256
`831dd2a9e3ddacc3ece25aaae474487678f93aa4731660ae07e81aa69e5cb4a0`.
Reserve O014-C067--O014-C069 for independent target review; do not treat them
as admitted corrections before that review. Package and publish Unit 046
through the existing GitHub and Zenodo lineages while Unit 047 translation
continues. This checkpoint remains partial and does not complete the pursuit.

## D126 - Publish Unit 046 and admit the independently reviewed Unit 047 target (2026-08-26)

Advance GitHub `main` by one fast-forward commit from Unit 045
`e072d5949d8ce0c1768c0c0e631b259db444fa8a` to Unit 046 commit
`61affa077df97bfc7a3e6643f5884a4efc852eab`, tree
`625de9517a635d957228d0ce0db2ee21c0bb7147`. Anonymous repository, commit,
raw-file, reader, manifest, checksum, and immutable codeload checks pass. The
2,326,794-byte archive, SHA-256
`fe90811614aee58e7af1fef8d87728ed92498f0fc4b0cd48f3037004c20a90d0`,
contains exactly 155 files and replays the 153-row inventory with zero mismatch.

Advance the existing Zenodo concept `22059751` from immutable Unit 045 record
`22104808` to Unit 046 record `22105465`, DOI
`10.5281/zenodo.22105465`; create no competing concept. Publish seven
reader-first files totaling 2,227,171 bytes. Preserve the exact work title,
Li as sole creator, CC BY 4.0, independent-derivative and non-endorsement
statements, exact model disclosure, and the single inherited organization
contributor without placing that organization in the title or description.
Anonymous record, DOI, concept-latest, predecessor, every file, both ZIP
manifests, and the 302-page PDF properties pass with zero mismatch.

Accept the independent Unit 047 review. Freeze the 18,004-byte authority
witness at SHA-256
`831dd2a9e3ddacc3ece25aaae474487678f93aa4731660ae07e81aa69e5cb4a0`,
the 95-record map at 27,644 bytes / SHA-256
`c227c6a7a13fba436af6ece633816ef5eb1f54af5d0d2d253f4baf09f459cf8c`,
and the final 26,722-byte Indonesian target after its layout-only display
reflow at SHA-256
`18f1639f9800e751f60418c018770b50eae69067b4f4b39384446443931ac91f`.
Admit O014-C067--O014-C069 as disclosed corrections for the missing inverse-
limit index, incorrect coefficient ring, and omitted application of `F`.
Preserve all 26 exercises, seventeen hints, 29 references, four diagrams, and
the two explicit Chapter 8 source-section fallbacks. Integrate and build Unit
047 before opening Unit 048, `chapter4.tex` lines 9--60. Neither this public
checkpoint nor the reviewed target completes the corpus pursuit.

## D127 - Admit the complete Chapter 3 exercise reader and open Unit 048 (2026-08-26)

Admit Unit 047 as `chapter3.tex` lines 3201--3425 and the complete end-of-file
exercise closure. Preserve the 18,004-byte authority witness at SHA-256
`831dd2a9e3ddacc3ece25aaae474487678f93aa4731660ae07e81aa69e5cb4a0`,
the 95-record map at 27,644 bytes / SHA-256
`c227c6a7a13fba436af6ece633816ef5eb1f54af5d0d2d253f4baf09f459cf8c`,
and the reviewed target at 26,722 bytes / SHA-256
`18f1639f9800e751f60418c018770b50eae69067b4f4b39384446443931ac91f`.
The 26 exercises, seventeen hints, four diagrams, two citations, 29 references,
and corrections O014-C067--O014-C069 pass.

Reject finalB only as a release artifact because its title, attribution page,
and PDF Subject retained the prior line-3200 scope. Admit
`build/cumulative-unit-047-finalC-20260826`, which corrects the visible scope
to complete Chapter 3 / line 3425 and anchors the `Latihan` outline on its
physical heading page. Its final three XeLaTeX transcripts are byte-identical;
Biber and both indexes pass; the log has no fatal, unresolved, glyph, or rerun
failure; and all seven overfull hboxes are inherited and visibly benign.

Promote the 308-page, 1,510,819-byte reader at SHA-256
`ad728f05e2069ca0bcaabcba8de5bdf8fcda311b1a022125f46c2c817c16cfec`.
Strict PDF validation passes every destination and link rectangle, and fresh
inspection of the front matter, every Unit 047 page, bibliography, and both
indexes finds no visual defect. Freeze the 98-row manifest at 12,575 bytes /
SHA-256
`02aacb9aa99e6fa09dd30723269483808f64dfd7cfe206531ce7e6d4271346a5`,
listing 16,306,822 bytes with zero mismatch. Publish this checkpoint through
the existing GitHub and Zenodo lineages and continue at Unit 048,
`chapter4.tex` lines 9--60. This admission does not complete the corpus goal.

## D128 - Close Unit 047 public lineages and accept Unit 048 review (2026-08-27)

Close the Unit 047 GitHub boundary at final immutable commit
`b085f39d2cc933572015a1bdfa4fbd6f516d8982`, tree
`3a8da8615671109f152dafe1145d15f76795b17c`. Preserve the truthful two-commit
sequence: content commit `bcb4bbc6453c1cfa7790e9d8b9cbb9ba7447ff22`,
then one manifest/checksum integrity correction for published LF bytes. Use
only the final codeload archive, 2,401,830 bytes / SHA-256
`5170a25e7aae589a81ca342ba16c4795858b7313db31153443c37a6a13fb3f2a`;
the superseded content-commit archive is not release evidence. Anonymous
HTML/raw/archive readback and the 158-row manifest replay pass. Preserve the
sanitized receipt at `release/github/GITHUB_PUBLICATION_RECEIPT.json`, 7,072
bytes / SHA-256
`f961f51d0066e0d3a807e0693df9351ae6bb5ca827162412807eb58584729eb7`.

Close the corresponding Zenodo boundary at existing-concept record `22105841`,
DOI `10.5281/zenodo.22105841`, version `unit-047`. Credential-free download of
all seven files, both package inventories, the outer manifest/checksums, DOI
redirects, and latest-version resolution pass with zero mismatch. The visible
record page actively previews the 308-page PDF and lists it first. Preserve the
sanitized receipt at
`release/zenodo/unit-047/ZENODO_PUBLICATION_RECEIPT.json`, 7,254 bytes /
SHA-256
`98441fdbdf738f1a28a97ea34245230000cb5618c0627ab2b41f935bada41183`.

Accept the independent Unit 048 comparison after one final wording correction
to `sifat keterhapusan`. The provisional reviewed target was 13,746 bytes /
SHA-256
`c61ac97f8d771b427ea75fbf1b0b363b552c9e9b02fd1491117b40cc64abee17`
and its 27-record map at 7,141 bytes / SHA-256
`41dcd96e597d7824fd10e19ff49b5beecd014d5bf1e02eb96a240d08a598481c`.
Admit O014-C070 for the incorrect right-hand localization label and O014-C071
for the over-broad complex scope in the classical Ext formula. Proceed through
backend, terminology, cumulative build, structural/visual QA, and publication
without crossing the frozen line-60 boundary. This decision does not complete
the corpus pursuit.

## D129 - Admit the Chapter 4 overview reader (2026-08-27)

Supersede only the provisional target bytes in D128 after the
meaning-preserving layout shortening. Admit Unit 048 at 13,727 bytes / SHA-256
`b987c6d3b29c0853a128b8fa73eede0a769c38deea7ee9392ad5d8beb4f206b7`,
with the same 8,677-byte authority witness at SHA-256
`800e4d6242edc127ed4db7fa45f98259cea386773d9333055ad170e9b9d971ed`
and the same 27-record segment map at SHA-256
`41dcd96e597d7824fd10e19ff49b5beecd014d5bf1e02eb96a240d08a598481c`.
Preserve all formulas, two diagrams and ten arrows, all source-reference
targets, and corrections O014-C070--O014-C071. The unit has no citation,
exercise, hint, answer, or solution.

Admit `build/cumulative-unit-048-finalD-20260827` after the clean converged
XeLaTeX/Biber/MakeIndex replay. The final log has no fatal, unresolved,
missing-character, or rerun failure; the seven overfull horizontal boxes are
inherited and visibly benign. Promote the byte-identical build, checkpoint,
and cumulative PDF at 314 pages, 1,526,462 bytes / SHA-256
`8eaf326be418d06f8c75dd4ea255073327a25a267d4be1813417c456a5a19d60`.
Strict PDF validation and fresh page-image inspection pass, while the inherited
untagged/ToUnicode limitations remain disclosed.

Freeze `qa/UNIT_048_QA.md` at 8,493 bytes / SHA-256
`22220a80fdb078d34b728706b9b717f21fb661070cd841b47c2b555417be47ee`
and the 115-row manifest at 15,051 bytes / SHA-256
`ca6251302aff86604203e658ac2dd53d7dbe93c279260d681363e8872631bd69`,
listing 24,929,784 bytes with zero replay mismatch. Publish this checkpoint in
the existing GitHub and Zenodo lineages, then continue in source order at
`chapter4.tex` line 62. This admission does not complete the corpus goal.
