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
