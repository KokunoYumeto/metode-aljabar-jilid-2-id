# Unit 045 admission QA

Date: 2026-08-26  
Course/role: O014 / D80  
Unit: `o014.aljabr2.chapter3.ext-tor`  
Result: **PASS**

## Frozen source boundary

Unit 045 is the complete Section 3.14, `sec:Ext-Tor`, from the frozen Wen-Wei
Li authority `chapter3.tex` lines 2714--2935 inclusive, with substantive
content through line 2934 and the terminal blank separator at line 2935. It
stops before `sec:K-injectives` at line 2936. The authority remains branch
`master`, commit `9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.

The normalized-LF source witness `tmp/unit045-source-slice.tex` is 20,416
bytes, 222 LF lines / 178 nonblank lines, SHA-256
`b257f061a7a3f56f8878d1815ac430417c033ef7ff93b214abe13eccb0b1d15a`.
The ordered map `tmp/unit045-segment-map.jsonl` has 60 records (40 top-level,
20 nested), is 15,479 bytes, and has SHA-256
`ffcb362491af688b95c07bd0b15a75bbde5d278028795b0098387c60d0a95278`.
Its top-level spans are nonoverlapping and cover every nonblank authority line;
all nested spans lie within their parent ranges.

## Translation and independent review

The admitted Indonesian target `source/id-ID/chapter3-unit-045.tex` is 26,060
bytes / 580 LF lines, SHA-256
`348fbb2121a37a54795a0e68b6fe3c76004294f10ee6a84201e4815abb62db6d`.
Its 60 stable segment markers exactly match map order. Independent
segment-by-segment and formula-by-formula review verifies all 12 labels, 26
reference targets, eight citation keys, eleven index entries, two footnotes,
two TikZ-CD blocks, formulas, quantifiers, signs, degrees, objects, morphism
orientations, Ext/Tor conventions, and proof implications. Twenty-nine LaTeX
environments are balanced. No Han character, U+FFFD, or U+2011 remains.

The sole reference beyond this partial reader, `sec:Hom-Ext`, is represented as
`\sourcecrossref{sec:Hom-Ext}{4.5}` rather than a broken internal link. Review
also normalized the established terms `kompleks total`, `hasil kali tensor`,
`funktor pelupa`, `kategori abelian k-linear`, `lapangan`, and module-side word
order; restored the source's “before Proposition 6.8.6” direction; and fixed
the proof phrase defining `B_p` and `Z_p` as submodules of `C_p`. These are
translation fidelity/polish changes, not changes to the authority mathematics.
No Unit 045 source-correction candidate remains.

## Cumulative integration

The frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-045.tex` and mutable alias
are byte-identical at 8,994 bytes, SHA-256
`8ee79862e9c4e10320a8f9fd2925303ad42bbe9079d9a2d40f4db28cace80977`.
They contain exactly the contiguous inputs 001--045 and truthfully identify
Chapter 3 through Section 3.14 / authority content line 2934. The referenced
bibliography `references-cumulative-through-unit-045.bib` and mutable alias are
byte-identical at 8,115 bytes, SHA-256
`9cab4a4c93359dd8b833bcc3fa57da1493782b6f5d34a5cea00b203d25ee63a8`;
Unit 045 introduces no new citekey beyond the existing `Li1` entry.

The modular backend now has 45 unique units and 2,438 unique segments. The
unit file is 33,800 bytes, SHA-256
`0e441fc4257935faec0a392b7c743d79adcefdad2bc62270fd02d7ab3e4fc6bf`;
the segment file is 718,432 bytes, SHA-256
`23c8f65c060ce384eaf757ed768dbe365f0d4a43ff6520b5e948d73e949be0f9`.
Removing the Unit 045 unit/segment suffix reconstructs the exact admitted Unit
044 hashes. The synchronized terminology stores each contain 477 unique
concepts and agree on every preferred form. `backend/terms.csv` is 32,449
bytes, SHA-256
`515358d2f6279e836655f0716fa5ec3d823d98d66fa62c6b0c9b3c30eddd20ba`;
`controls/TERMINOLOGY_O013_O014.csv` is 81,016 bytes, SHA-256
`f84a44360f61d749faafdf44af57f9e97ad8c89178e449eef6c39c93fcdc54c1`.
The four new first-use concepts are `ext_functor`, `tor_functor`,
`flat_resolution`, and `kunneth_theorem`.

## Reproducible build

The admitted clean build is `build/cumulative-unit-045-finalA-20260826`.
XeLaTeX 26.5 ran with shell escape disabled, Biber 2.21 ran with the bounded
source directory supplied explicitly, both MakeIndex jobs ran in the build
directory, and four further XeLaTeX passes followed. The byte-identical pass 4
and pass 5 console transcripts are each 28,698 bytes, SHA-256
`6acb1c062494fa55ba4e1364f63927f12201e4bfc179fa95d1441efc908089e5`,
which proves convergence of the final replay surface.

Biber resolves all 22 citekeys with zero error or warning. Its 30,421-byte BBL
has SHA-256
`586c340f7b1bcd7382e3b1cd9808f1ac5d553c7e2c76c8e59db6a851a7d2f35f`.
MakeIndex accepts 203 terminology entries and 103 symbol entries with zero
rejection or warning. The terminology index is 9,121 bytes / SHA-256
`de818bfd9aa1a429f7c056410480752a2a4e546c8cd52f7dea236f4e2c31f32c`;
the symbol index is 3,867 bytes / SHA-256
`ddd5c27995115d22a8e4ecde7e4e7215a67912c6d87fac858d882614437aef98`.

The final 81,765-byte log, SHA-256
`333449a38efbe6ab8d8544e4fe931c80cb551ccec20c5e9052447f50edcefb4d`,
contains no TeX/package error, undefined reference or citation, missing
character, emergency stop, or fatal error. Three overfull horizontal boxes
remain: two inherited Unit 044 cases (8.65707 pt and 42.92992 pt) and one
0.62685-pt Unit 045 paragraph. There is no overfull vertical box. Twenty
underfull horizontal and seven underfull vertical boxes are nonfatal. The two
generic imakeidx reminders are expected in the shell-escape-disabled external
index workflow; both generated indexes are loaded and the last two XeLaTeX
transcripts are identical.

## PDF structure and page-image inspection

The build PDF, checkpoint PDF, and promoted cumulative PDF are byte-identical:
PDF 1.7, 290 pages, 1,427,097 bytes, SHA-256
`39eee75436b826cac1e82fe5d3eb051212625f194bc32b81f2afab5350f95405`.
All pages are 498.9 by 708.66 points with zero rotation. The file is
unencrypted and untagged. Strict parsing verifies 52 outline entries, 1,254
named destinations, 1,006 internal links, and sixteen URI links. All 1,022
link rectangles lie within page bounds; every internal name resolves. There
is no malformed destination, form, widget, JavaScript, embedded file,
additional action, structure tree, `MarkInfo`, or metadata stream. The opening
action is the ordinary page-destination array.

All 54 font rows are embedded and subsetted. Forty-two have ToUnicode maps;
twelve inherited mathematical fonts do not. Therefore neither tagged-PDF nor
fully semantic accessibility is claimed.

Fresh 120-dpi inspection covers physical pages 1--6, the transition and all
content on physical pages 268--280, and every bibliography/index page through
physical page 290. Unit 045 itself occupies physical pages 272--280. Formulas,
the two diagrams, the wide inherited Unit 044 displays, theorem heads,
footnotes, bibliography, and both indexes are centered within the text block,
legible, and unclipped. Physical pages 2, 4, and 284 are intentional blank
transitions. The combined page 268--290 contact sheet is 2,944,791 bytes,
SHA-256
`13d9b005f8b5972540290d20610dd4f364610db0d35b2a443d19d97362ab3aa5`.

The author's official 650-page Linux/TeX Live/xindy PDF remains the reference
pagination. This 290-page Windows/MiKTeX/MakeIndex artifact is a valid partial
Indonesian reader and makes no pagination-identity claim. Unit 045 is admitted
locally; this checkpoint does not complete the corpus pursuit.
