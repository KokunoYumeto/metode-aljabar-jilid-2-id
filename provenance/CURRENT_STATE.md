# O014 current state

Status: active source-order Indonesian production. Units 001--043 are complete,
admitted, built, and QA-passed without a source gap through `chapter3.tex`
line 2552. The public lineages currently remain at Unit 042 while Unit 043
release packaging is in progress. This remains a partial working edition; do not
complete the pursuit at this or any later checkpoint short of the entire
corpus, independent mastery layer, semantic reader, and final verified release
set.

## Frozen authority and terminal scope

- Corpus: Wen-Wei Li, *Methods of Algebra, Volume 2: Linear Algebra*.
- Authority: author-controlled Gitee `master` commit
  `9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
  `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.
- The author's 650-page Linux/TeX Live/xindy PDF is the reference pagination.
  The separately valid 653-page Windows/MiKTeX/MakeIndex replay proves editable
  closure and is not a corpus mismatch.
- Li is the integrated spine. Leinster is only an optional introductory donor;
  Stacks is a verification/accessibility reference. The source contains 194
  exercises and 117 hints but no answers or solutions. Any mastery/solution
  bridge is independent, separately labeled work.
- Terminal scope remains the complete source-order translation, exercises and
  hints, independent mastery bridge, semantic/offline reader, modular backend,
  cumulative PDF, full QA, and verified GitHub/Zenodo/Figshare preservation.

## Contiguous admitted production

Units 001--007 translate `prelude.tex` lines 9--495. Units 008--019 translate
`chapter1.tex` lines 9--2079, including all eleven Chapter 1 sections,
seventeen exercises, and ten hints. Units 020--030 translate all of
`chapter2.tex` lines 9--2132: the overview, Abelian-category definition, first look at
complexes, diagram lemmas, lattice-theory overview, direct-sum decomposition,
Subobjek dan Teorema Isomorfisme, Objek Sederhana dan Semisederhana, exact
functors/injective/projective objects, Subkategori Serre dan Grup K0, Kategori
Grothendieck, and the complete 20-exercise/13-active-hint chapter closure.
Unit 031 translates the complete Chapter 3 overview, `chapter3.tex` lines
9--55.

Unit 026, `o014.aljabr2.chapter2.subobjects-and-isomorphism-theorems`, is
admitted at `source/id-ID/chapter2-unit-026.tex`, 24,624 bytes, SHA-256
`52e87d044ba6a645a5c98329832fdb06272ce15106422c13ac402c75a67e200c`.
Its normalized authority slice is lines 911--1132, 15,939 bytes, SHA-256
`85f25b07bbf35565c56e1f64ddb33c0a00ae79b1f60e3bb0aeb39ca982cccda8`; its
62-record map is 21,112 bytes, SHA-256
`79144b8d751fc35c6c177f4b24595388fe1f117239277431eb0d2310483a08bb`.
The section has eleven labels, 28 references over nineteen unique targets, two
citations, two definitions, one convention, two propositions, one lemma, two
corollaries, two theorems, seven proofs, three lists/seven items, eighteen
TikZ-CD diagrams/98 arrows, six indexes, and no exercises or hints.

O014-C025 corrects the source's unprimed family declaration against primed
formulas; O014-C026 corrects the source's `Image`/coimage misidentification.
Both are disclosed in the target and `controls/SOURCE_CORRECTIONS.csv`.
The target-fidelity review also repaired three target-only markup/antecedent
slips before admission. No upstream contact occurred.

Unit 027, `o014.aljabr2.chapter2.simplicity-and-semisimplicity`, is admitted at
`source/id-ID/chapter2-unit-027.tex`, 13,458 bytes, SHA-256
`bcf83b6829f1ea4fcd4a712e19f4c7f1402ed0990565aad2b6c5055fbe97cf66`.
Its normalized authority slice is lines 1133--1244, 8,321 bytes, SHA-256
`e2f435c542379cd0f924343bd552514be261d8827dfa53afd107e20722ec213b`; its
38-record map is 11,184 bytes, SHA-256
`5d821f28602c5c7f40bfcb6569ccdf68f6aaac14bc9a5161a333d08f420d4fe6`.
The section has one convention, two definitions plus one definition-theorem,
three lemmas, two propositions, two remarks, six proofs, five display-math
blocks, six labels, thirteen references, two citations, eleven index commands,
one footnote, no diagrams/assets, and no exercises or hints. No confirmed
mathematical defect was found. The target uses the existing sourcecrossref
fallback for the intentional forward reference to `sec:Grothendieck-cat`.

Unit 028, `o014.aljabr2.chapter2.exact-functors-injective-projective-objects`,
is admitted at `source/id-ID/chapter2-unit-028.tex`, 37,694 bytes, SHA-256
`cd2f4bc1d7c2d4912650db33a934f9571f7a018d409a617fef4e61033d293a85`.
Its normalized authority slice is lines 1245--1563, 24,797 bytes, SHA-256
`e6e50b76ae9dcd59f739e00b89347c0a0a05c303a6fff56934018301cd275d63`; its
113-record map is 39,367 bytes, SHA-256
`0dfbfa43a29313cd1b3a57a9b72b64c2d668889e369605dd2709164688c6b9d8`.
The section has 19 labels, 30 conventional references plus one intentional
`sourcecrossref` fallback for `sec:derived-primer`, six citations, six index
commands, 17 TikZ-CD environments, 21 display environments, and no exercises
or hints. O014-C027 is disclosed in a translator footnote. New settled terms
include `funktor eksak`, `funktor eksak kiri/kanan`, `funktor eksak setia`,
`cukup banyak objek injektif/projektif`, `kategori panah`, and `keeksakan
lokalisasi`.

Unit 029, `o014.aljabr2.chapter2.serre-subcategories-and-k0-groups`, is
admitted at `source/id-ID/chapter2-unit-029.tex`, 25,425 bytes, SHA-256
`6cfc81b8d1dc52ed685971c9dd4d81471e8978b58d8c682be60a5ef1f97d2b81`.
Its normalized authority slice is lines 1564--1754, 17,301 bytes, SHA-256
`45f958e6627cb4cef919dbd1fd5bc478b68c5d6c706dac47b69dd4d6dbd40aba`;
its 61-record map is 19,962 bytes, SHA-256
`ec804f816cde5005f626110f65bf4dd7db928c6fc2ab040cfc36ad809f7ae4e2`.
All labels, references, citations, environments, display blocks, diagrams, and
index entries passed source/target parity. O014-C028 corrects `K_0(f)` to
`K_0(F)`; O014-C029 supplies the canonical fiber-product repair for an
undefined restriction in the fullness proof. Both are disclosed at point of
use. This section contains no exercises or hints.

Unit 030, `o014.aljabr2.chapter2.grothendieck-categories`, is admitted at
`source/id-ID/chapter2-unit-030.tex`, 43,836 bytes, SHA-256
`a7fec40262a70c2f7fe253a97cf21558acc3c0b32272e3bcdb24a04e58c96697`.
Its normalized authority slice is lines 1756--2132, 30,150 bytes, SHA-256
`4b3ed0e1d7676d37d3bf465a241df0116fbb0e28cf39cd1b313a9f9f19225b7e`;
its 133-record map is 41,437 bytes, SHA-256
`dff9eaedeaaaad88c10b68d40fd4683f0e27f88164985b1824aef5bfb71b85b7`.
It preserves 15 labels, 46 references over 35 targets, citations `Gr57` and
`Li1`, nine TikZ-CD diagrams, all 20 exercises, 13 active hints, and the one
commented hint. No new source correction was admitted. A forward Appendix-A
reference uses a printed `sourcecrossref` fallback, and one long inline Hom map
was reflowed to an unnumbered display to remove an overfull line.

Unit 031, `o014.aljabr2.chapter3.overview`, is admitted at
`source/id-ID/chapter3-unit-031.tex`, 13,031 bytes, SHA-256
`65e3dd7e5c5a0a4512c9c90efd727b32fc7d8c1397d8117f29a492ca080c4e65`.
Its normalized 8,019-byte authority slice has SHA-256
`6b4b4806e0d9885580547cb103d93e59f0a094ff08d93abdd2781287b71040ec`;
its 19-record, 5,258-byte map has SHA-256
`0c70f75800fa91ed0d1ebf97642237d576118746dcc60de1ef43521f4e43731f`.
It preserves 39 references over 30 targets, citation `KS06`, three displays,
one TikZ-CD diagram, and the reader-tip enclosure. O014-C030--C032 correct a
malformed transition, a skipped `I^1`, and the ill-typed cohomology denominator;
all are disclosed at point of use.

Unit 032, `o014.aljabr2.chapter3.complexes-over-additive-categories`, is
admitted at `source/id-ID/chapter3-unit-032.tex`, 13,677 bytes, SHA-256
`0ac6def5c534f07ceacfb80f29fff71b0174fffb944c0759fce1392510e3b500`.
Its normalized authority slice is `chapter3.tex` lines 57--162, 8,995 bytes,
SHA-256
`2f928e1ca88a032bec9c270d65604e25a38bd00ec62874562ae95a55be0ee8b5`;
its 33-record, 10,336-byte map has SHA-256
`7100b28797cf67adb12b11dc400a54d980671957bd491a053ba16702fc3c2e1f`.
It preserves 9 labels, 7 references, 4 definitions, 1 lemma, 2 propositions,
2 proofs, 1 convention, 1 remark, 5 displays, both TikZ-CD diagrams, 2 lists
with 6 items, 2 footnotes, and 11 indexes. It has no citations, exercises,
hints, answers, solutions, or external assets. No new source correction was
required.

The backend contains 32 sequential units and 1,633 unique segments.
`backend/units.jsonl` is 23,665 bytes, SHA-256
`0212ad5888b3153a14679d27a149b518e3a9396084643228d15a6b4b2c9365e0`;
`backend/segments.jsonl` is 477,156 bytes, SHA-256
`8906b0d5204e12187eb198e361b91358145aee5d464b9fafb69d23a3bf049406`.
Both terminology surfaces now contain 416 unique, matching IDs:
control `controls/TERMINOLOGY_O013_O014.csv` SHA-256
`cf88447b578262f044d15ebaecd5b505b051599f90068e88099ca073c12ad777`;
backend `backend/terms.csv` SHA-256
`f37a93c0ad714999de14697f31b549746f52fac116aa128b600e5e4e3bbcd96a`.

## External Indonesian terminology QA

The bounded official arXiv check found no admissible Indonesian same-field source
with downloadable TeX. The instructed fallback used two official ITB PDFs:
Gustina Elfiyanti's 2020 U-complex-category front matter, 4 pages /
126,507 bytes / SHA-256
`8e56993c4abcac3d7f89c9bb948e9d9925de6eef8b3102121c530e43ed8f19be`, and
Ryan Kasyfil Aziz's 2012 algebra/modules/categories chapter, 12 pages /
435,907 bytes / SHA-256
`196d921577e7ba9f2508d8e1cc5be434061a8e1f40c71f8f7adcf643f00c2c1c`.
Every page was rendered and inspected; witnesses remain local and excluded
from public payloads. A supplemental nine-page Universitas Diponegoro category-
theory journal PDF is 429,219 bytes, SHA-256
`d22cf3c40242359a2d00eb726697e08b6ad29c647a0309cbcd98914484b5f9b6`;
it confirms the mathematics and contributes older spelling variants only. The
report is `controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`, 10,335 bytes, SHA-256
`0c6e739d72941399bb388ef470fc36c2a36bcf3d9781848e46d4056caf5d36fd`.
Edition/repository provenance identifies the production model exactly as
`OpenAI Codex gpt-5.6-sol, Ultra`.

## Previous admitted reader (Unit 026)

The clean shell-escape-disabled build directory is
`build/cumulative-unit-026-finalB-20260823`: XeLaTeX, Biber 2.21, both
MakeIndex passes, and three final XeLaTeX passes. It has no fatal, TeX,
unresolved-reference, citation, rerun, overfull-box, or missing-character
errors; ten underfull hboxes and six underfull vboxes plus known non-fatal
MiKTeX/biblatex/imakeidx warnings remain recorded.

The frozen checkpoint and promoted cumulative reader are byte-identical:
152 pages, 807,443 bytes, SHA-256
`1895b07aad71009c4c1d6594120d6f8f47694b751551aff3c1e1cbb3b4c31ed9`.
Paths:
`output/pdf/checkpoints/metode-dalam-aljabar-jilid-2-id-through-unit-026.pdf`
and `output/pdf/metode-dalam-aljabar-jilid-2-id-cumulative.pdf`.
The PDF is PDF 1.7, `id-ID`, unencrypted, untagged, with 32 outline entries,
49 embedded/subset fonts, 489 link annotations (477 internal/destination and
12 URI), and no active content. Mathematical font extraction remains
incomplete; accessibility is not overstated. Physical pages 139--152 were
rendered at 150 dpi and visually inspected; contact sheet:
`tmp/pdfs/unit026-finalB-pages/contact-sheet.png`, 481,082 bytes, SHA-256
`9d1f68c6e4129f45b8938bbda016cf07058b9ffb766a4f514ddb7bda6a3eed91`.
QA receipt `qa/UNIT_026_QA.md` is 7,491 bytes, SHA-256
`2bb2a8d1c3a352ba68f5adb9d5f02a7ca9a4de5352c6ff724b2aff33db0c2abf`.
The 53-row exact manifest
`qa/CUMULATIVE_UNIT_026_FILE_MANIFEST.csv` is 7,076 bytes, SHA-256
`f78c35eea3f2a52ecc9d64a5f7310d158377774d30d8d2b8fcd33a65411c096d`.

## Prior admitted reader (Unit 027)

The clean shell-escape-disabled build directory is
`build/cumulative-unit-027-final-20260823`: XeLaTeX, Biber 2.21, both
MakeIndex passes, and three final XeLaTeX passes. It has no fatal, TeX,
unresolved-reference, citation, rerun, overfull-box, or missing-character
errors; sixteen underfull boxes plus known non-fatal MiKTeX/biblatex/imakeidx
warnings remain recorded.

The frozen checkpoint and promoted cumulative reader are byte-identical:
157 pages, 823,894 bytes, SHA-256
`04af446ade23411da0a59a5f6a9f526b0267ddfe104c24e8fdedc0ad0583a6e0`.
Paths:
`output/pdf/checkpoints/metode-dalam-aljabar-jilid-2-id-through-unit-027.pdf`
and `output/pdf/metode-dalam-aljabar-jilid-2-id-cumulative.pdf`.
The PDF is PDF 1.7, `id-ID`, unencrypted, untagged, with 49 embedded/subset
fonts, 506 link annotations (494 internal/destination and 12 URI), and no
active content. Mathematical font extraction remains incomplete; accessibility
is not overstated. Physical pages 147--150 were rendered at 180 dpi and
visually inspected; contact sheet:
`tmp/pdfs/unit027-final-pages-147-150/contact-sheet.png`, 600,827 bytes,
SHA-256 `48e82f741f0678181c3ef2fa2635c4adb69b654eb69ddacc735ada1464c775e1`.
QA receipt `qa/UNIT_027_QA.md` is 7,019 bytes, SHA-256
`165ca2cb47cc6670c76154743e91b94a5323eb9d4ba8a3a01ea816b2d1ba2145`.
The 60-row exact manifest
`qa/CUMULATIVE_UNIT_027_FILE_MANIFEST.csv` is 7,433 bytes, SHA-256
`bd7c0e9309ec2231b1bf2a59acdfd60995906af9d1a9d6a97db901088ef3af45`.

## Prior admitted reader (Unit 028)

The clean shell-escape-disabled build directory is
`build/cumulative-unit-028-final-20260823`: XeLaTeX, Biber 2.21, both
MakeIndex passes, and three final XeLaTeX passes. It has no fatal, TeX,
unresolved-reference, citation, rerun, overfull-box, or missing-character
errors; seventeen underfull boxes plus known non-fatal MiKTeX/fontspec,
biblatex, and imakeidx warnings remain recorded.

The frozen checkpoint and promoted cumulative reader are byte-identical:
167 pages, 868,564 bytes, SHA-256
`78c1ec3db75a97f3593d91412a8fbd19057d821df200cbc2893641dff5c48a43`.
Paths:
`output/pdf/checkpoints/metode-dalam-aljabar-jilid-2-id-through-unit-028.pdf`
and `output/pdf/metode-dalam-aljabar-jilid-2-id-cumulative.pdf`.
The PDF is PDF 1.7, `id-ID`, unencrypted, untagged; accessibility is not
overstated. Physical pages 153--167 were rendered at 120 dpi and visually
inspected; contact sheet:
`tmp/pdfs/unit028-final-pages-153-167/contact-sheet.png`, 825,266 bytes,
SHA-256 `912c627cebd05472f10bae56b5ba5922ce95a7ddc52b103b7df2361f070b4e6e`.
QA receipt `qa/UNIT_028_QA.md` is 5,070 bytes, SHA-256
`df6282afeae47aa0f3cb81be82b88a9a9a47fedcad6c223b131e637b0b7e8faf`.
The 67-row exact Unit 028 manifest
`qa/CUMULATIVE_UNIT_028_FILE_MANIFEST.csv` lists 6,395,650 bytes, is 8,554
bytes, and has SHA-256
`4594c6510d46ab84568945035b503436624786d4df49ad2340d3cd0986b424e`;
verification found zero missing or hash/byte mismatches. Mutable pursuit
controls are intentionally kept outside this release snapshot to avoid a
self-invalidating manifest; their current hashes are recorded in the cursor
and decision log.

## Prior admitted reader (Unit 029)

The clean shell-escape-disabled build directory is
`build/cumulative-unit-029-finalB-20260823`: XeLaTeX, Biber 2.21, both
MakeIndex passes, and three final XeLaTeX passes. Biber resolved all 19
citekeys; MakeIndex accepted 139 term entries and 47 symbol entries. The final
logs have no fatal, TeX, unresolved-reference, citation, rerun, overfull-box,
or missing-character error. Seventeen non-fatal underfull boxes remain.

The checkpoint and promoted cumulative reader are byte-identical: 175 pages,
902,840 bytes, SHA-256
`bfda39c9f834643f024dd2c7d9c16e341c8736b40f3bfa6dcc9d1646b6d6bd25`.
The PDF is PDF 1.7, `id-ID`, unencrypted, untagged, with 35 outline entries, 51
font names, 591 links including 12 URI links, and no form widgets or
JavaScript. Accessibility is not overstated. Physical pages 160--175 were
rendered at 120 dpi and visually inspected; both contact sheets passed. QA
receipt `qa/UNIT_029_QA.md` is 7,276 bytes, SHA-256
`60006df36bb0e8622870886fcf2286f4e776d7894a9772d22ec99e9590333d55`.
The 64-row exact manifest
`qa/CUMULATIVE_UNIT_029_FILE_MANIFEST.csv` lists 5,609,913 bytes, is 8,042
bytes, and has SHA-256
`ec69439286262800cd2ec6dd830ae21fd968508ccd67c703f3e6798715ccb40d`;
verification found zero missing or byte/hash mismatches.

## Prior admitted reader (Unit 030)

The clean shell-escape-disabled build directory is
`build/cumulative-unit-030-finalD-20260823`: XeLaTeX, Biber 2.21, both
MakeIndex passes, and three final XeLaTeX passes. Biber resolved all 19
citekeys; MakeIndex accepted 144 term entries and 47 symbol entries. The final
logs have no fatal, TeX, unresolved-reference, citation, rerun, overfull-box,
or missing-character error. Nineteen non-fatal underfull boxes remain.

The checkpoint and promoted cumulative reader are byte-identical: 187 pages,
963,655 bytes, SHA-256
`e74feecbbcc1dc2b4538b182215b1c3210ad32f4d90fa933c43cbd27293823bf`.
The PDF is PDF 1.7, `id-ID`, unencrypted, untagged, with 37 resolving outline
entries, 51 embedded/subset font names, 636 resolving internal links, 12 HTTPS
links, and no forms, JavaScript, embedded files, or additional actions.
Accessibility is not overstated. Physical pages 167--187 were rendered at 120
dpi and visually inspected; all three contact sheets and representative
full-size pages passed. QA receipt `qa/UNIT_030_QA.md` is 8,288 bytes, SHA-256
`ccc38fc3565f4628704e3ef5572cb5e96d5dd2dbcbb22de4829193000b76b26d`.
The 66-row exact manifest
`qa/CUMULATIVE_UNIT_030_FILE_MANIFEST.csv` lists 5,562,324 bytes, is 8,318
bytes, SHA-256
`4dc90363c8af66e305689da41c465d083a9b2c09c393537d6c93633ff4f345b2`,
and verifies with zero missing or byte/hash mismatches.

## Prior admitted reader (Unit 031)

The clean shell-escape-disabled build directory is
`build/cumulative-unit-031-finalC-20260823`: XeLaTeX, Biber 2.21, both
MakeIndex passes, and three final XeLaTeX passes. Biber resolved all 19
citekeys; MakeIndex accepted 144 term entries and 47 symbol entries. The final
log has no fatal, TeX, unresolved-reference, citation, rerun, overfull-box, or
missing-character error. Nineteen non-fatal underfull boxes remain.

The checkpoint and promoted cumulative reader are byte-identical: 191 pages,
979,643 bytes, SHA-256
`0834eaa525fb64f3f2f13665238429fd3e4db9e3679b8c71e781ce2fdf333330`.
The PDF is PDF 1.7, `id-ID`, unencrypted, untagged, with 38 outline entries,
824 named destinations, 51 embedded/subset font names, 644 internal GoTo
links, 12 HTTPS links, and no forms, JavaScript, embedded files, additional
actions, structure tree, or MarkInfo. Physical pages 179--191 were rendered at
120 dpi; both contact sheets and full-size Chapter 3 pages 181--184 passed
visual inspection. QA receipt `qa/UNIT_031_QA.md` is 8,237 bytes, SHA-256
`eb6dda5f6ebef8776e44981bdf1dd05006fe11476e96d48714d0b0feb1baaf16`.
The 66-row exact manifest
`qa/CUMULATIVE_UNIT_031_FILE_MANIFEST.csv` lists 5,061,256 bytes, is 8,285
bytes, SHA-256
`1578225fc37b67bb44a036fcb384cfc63c00f331a55dad29b825d23cd8b2cd2c`,
and verified with zero missing or byte/hash mismatches at admission.

## Prior admitted reader (Unit 032)

The clean shell-escape-disabled build directory is
`build/cumulative-unit-032-finalA-20260823`: XeLaTeX, Biber 2.21, both
MakeIndex passes, and three final XeLaTeX convergence passes. Biber resolved
all 19 citekeys; MakeIndex accepted 151 term entries and 51 symbol entries
with zero rejection or warning. The final log has no TeX/package error,
unresolved reference or citation, rerun request, overfull box, missing
character, fatal error, or emergency stop. Nineteen non-fatal underfull boxes
remain. The QA receipt records the corrected Biber working-directory
invocation after an initial relative-path failure; the admitted final `.blg`
is clean.

The checkpoint and promoted cumulative reader are byte-identical: PDF 1.7,
195 pages, 999,106 bytes, SHA-256
`f28977200909076af2a30ea82de30985a917a5e3d62cb2f2d478502b51314ef3`.
It is `id-ID`, unencrypted, untagged, and has 39 outline entries, 843 named
destinations, 654 internal links, 12 HTTPS links, and 52 embedded font
programs, with no forms, JavaScript, embedded files, structure tree, or
MarkInfo. Physical pages 178--195, both contact sheets, and full-size pages
185--188 passed visual inspection; blank physical pages 180 and 192 are
intentional separators. QA receipt `qa/UNIT_032_QA.md` is 7,699 bytes,
SHA-256
`dbb770de4c12b1f884e6a487d48a2725a0e428e923951fc07c478022e579d51c`.
The 67-row exact manifest
`qa/CUMULATIVE_UNIT_032_FILE_MANIFEST.csv` lists 5,896,555 bytes, is 8,476
bytes, SHA-256
`d05def8f5bcff64f85a71373ecb125027baeb3892fed2e3621b592336ade913a`,
and verifies with zero missing file, byte-count mismatch, or hash mismatch.

## Latest admitted reader (Unit 036)

Unit 036, *Bikompleks*, is admitted through `chapter3.tex` line 945. The exact
target `source/id-ID/chapter3-unit-036.tex` is 28,124 bytes, SHA-256
`d36274b3f84495b1a28608b9f95f7e2d173afe73e84b38f408b265819c9bcc3f`.
Two independent reviews pass all 76 ordered stable markers, 13 labels, 12
reference relationships, one citation, 14 indexes, ten TikZ-CD diagrams, 37
balanced environments, formulas, signs, degrees, encoding, and natural
Indonesian prose. O014-C038 restores omitted bifunctor arguments; O014-C039
uses the strict inverse sign and a coordinate isomorphism to recover the
standard Hom differential. Both are disclosed at point of use. The requested
arXiv-first terminology check found no admissible Indonesian same-field TeX
source; directly inspected institutional fallbacks refined variants and notes
without requiring a prose replacement. The synchronized backend contains 36
units, 1,869 unique segments, and 427 terminology concepts.

The admitted shell-escape-disabled build is
`build/cumulative-unit-036-finalB-20260824`: XeLaTeX, Biber 2.21, both
MakeIndex passes, and four XeLaTeX passes. Biber resolves 19 citekeys;
MakeIndex accepts 165 term and 70 symbol entries with zero rejection or
warning. The 79,529-byte final log has SHA-256
`b4b884d331045167ca903e11b920f776ddfaecc617c91c1ae2086bfb64dfdddb`
and zero TeX/package error, unresolved reference or citation, rerun request,
overfull box, missing character, fatal error, or emergency stop. Fifteen
non-fatal underfull horizontal boxes and seven underfull vertical boxes remain.

The checkpoint and promoted cumulative reader are byte-identical: PDF 1.7,
219 pages, 1,107,313 bytes, SHA-256
`a720761eeab43f504f22af1214259c3481e377f5de3ecd3287b7aee9e71c8d2b`.
It is `id-ID`, unencrypted, untagged, and has 43 outline entries, 950 named
destinations, 724 internal GoTo links, and 12 URI links, with no form,
JavaScript, embedded file, structure tree, or MarkInfo. All 52 fonts are
embedded, while 11 mathematical fonts lack ToUnicode maps; no semantic-PDF
accessibility claim is made. Physical pages 198--219, both contact sheets, and
full-size pages 205--212 passed visual inspection. QA receipt
`qa/UNIT_036_QA.md` is 9,198 bytes, SHA-256
`126ff3267e7dd55b943a6277d72525dde3b5abe51cbf0279229de8063cf7859b`.
The 73-row exact manifest `qa/CUMULATIVE_UNIT_036_FILE_MANIFEST.csv` lists
7,144,999 bytes, is 9,283 bytes, SHA-256
`e069f9a83d36952473d5dc7ff18b4ba371a16523c6c971fee7d9731dd1642a9c`,
and independently re-verifies with zero missing file, duplicate path,
byte-count mismatch, or hash mismatch.

## Exact continuation

The next frozen source unit is Unit 037,
`o014.aljabr2.chapter3.abelian-category-complexes`, exactly `chapter3.tex`
lines 946--1060, section `sec:Abel-cplx`; substantive content ends at line
1058 and lines 1059--1060 are blank separators. Its normalized 8,933-byte
slice has SHA-256
`6adf88af700b26dac31c81724d991fbefcedab64f6ccd08849e532a75e04410e`;
the 30-record, 9,537-byte stable map has SHA-256
`e08be8d6d9372550bcfa2680c6f3d1b02fbaa4f9886d35ff7b293fc82aaa30c2`.
It contains eight labels, 18 reference tokens over 14 targets, eight display
constructs including six TikZ-CD diagrams, three indexes, four propositions,
five proofs, one remark, one definition, one corollary, and a two-item list.
It has no citation, exercise, hint, solution, external asset, footnote, or
source comment. The first complete Indonesian draft now exists at
`source/id-ID/chapter3-unit-037.tex`: 262 LF-terminated lines, 13,925 bytes,
SHA-256
`e6078b3d29464c49f90f9586aa44448da806efc41017b610bf2e2f3715583065`.
Structural, semantic, integration, build, render, and admission QA remain
pending; Unit 037 is not yet an admitted boundary.

Four source-correction candidates require exact review during translation:
the degreewise kernel/cokernel formulas at lines 957--958 are mistyped as
families; line 964 omits `d_Z`; line 971 names `A` instead of `C(A)`; and the
degree labels in the diagram at lines 1026--1031 do not match the prose's
`d^n`. Translation must stop before line 1061,
`sec:cone-vs-long-exact-sequence`.

## Public preservation

GitHub remains the existing edition repository
<https://github.com/KokunoYumeto/metode-aljabar-jilid-2-id>, branch `main`,
public through Unit 036 at commit
`9abf7c2861bb08e0d09d919ce2e242699ae4e657`, tree
`b1d951c2244694e5f8b8f2a102ab8184dec9dc7c`. The immutable anonymous archive
has 105 files, 1,658,586 bytes, SHA-256
`6b2ee1c75911a2143c6ec2a73a599e78d1214b7a6088083d64398a2893910da9`;
all 103 manifest and checksum rows and the 219-page reader passed byte/hash
readback with zero mismatch. An inventory-only follow-up commit corrected two
CRLF-versus-LF inventory rows without changing payload content. Receipt
`release/github/GITHUB_PUBLICATION_RECEIPT.json` is 5,829 bytes, SHA-256
`e7663b8ce5ff43b7c9d11fb06d145c22fa00f1d30e3259a20b1739feb9080327`.

Zenodo remains one concept lineage, 22059751. The latest Unit 036 record is
22075083, DOI `10.5281/zenodo.22075083`, version `unit-036`: seven files
totaling 1,499,086 bytes. Every anonymous file download matches local bytes
and SHA-256; the record API/page, DOI, and concept-latest readbacks all pass.
The reader-first payload freezes exactly 36 units, 1,869 segments, and 427
terms, with corrections through O014-C039. No Unit 037 or future artifact or
restricted terminology witness entered the release. Receipt
`release/zenodo/unit-036/ZENODO_PUBLICATION_RECEIPT.json` is 6,743 bytes,
SHA-256
`38d64d268f1a3828ab29c7b3be083030300642e811474877adfc9e811659d290`.
Record 22074617 and all earlier versions remain immutable; no competing
concept or unpublished draft was created.

Before this publication, the explicit task-local cleanup archived 51
superseded build, terminology-QA scratch, and rendered-page artifacts into
`old stuff/O014-unit036-superseded-build-and-QA-scratch-20260824.zip`.
The verified ZIP contains 10,910,003 uncompressed bytes, is 9,617,936 bytes,
and has SHA-256
`af8056e178442db4223655000956e69d944aa64a667e7f7ddfa3b45832356742`;
only the exact successfully archived loose originals were deleted. Canonical
sources, the admitted finalB build, current PDFs, release staging, receipts,
and durable evidence remain live.

Figshare remains one work-level item, article 33314775, public version 3,
DOI `10.6084/m9.figshare.33314775.v3`, CC BY 4.0, in project 280296 and
collection 8668413, DOI `10.6084/m9.figshare.c.8668413.v43`. The single bounded
Unit 035 retry made no mutation because the account remains inactive. Blocker
receipt `release/figshare/unit-035/FIGSHARE_PUBLICATION_RECEIPT.json` is 4,010 bytes,
SHA-256
`a430dcbb7dd6e2e16cf74129ee2b3cff0d45c0f8ad1aff48f4255c2734e502ea`.

Continue contiguous source-order production. This checkpoint does not complete
the pursuit.

## Unit 037 admitted checkpoint (2026-08-24)

Units 001--037 now form one contiguous admitted Indonesian reader through all
of `prelude.tex`, all of `chapter1.tex`, all of `chapter2.tex`, and
`chapter3.tex` lines 9--1060 / Section 3.6. Unit 037 is
`o014.aljabr2.chapter3.abelian-category-complexes`, exact lines 946--1060. Its
frozen 8,933-byte source slice has SHA-256
`6adf88af700b26dac31c81724d991fbefcedab64f6ccd08849e532a75e04410e`;
its 30-record, 9,537-byte map has SHA-256
`e08be8d6d9372550bcfa2680c6f3d1b02fbaa4f9886d35ff7b293fc82aaa30c2`.
The complete 262-line Indonesian target is 13,925 bytes, SHA-256
`e6078b3d29464c49f90f9586aa44448da806efc41017b610bf2e2f3715583065`.

Independent structural and semantic audits pass all 30 segments, eight labels,
18 reference tokens, 23 environment pairs, eight display constructs, six
TikZ-CD diagrams with 62 arrows, three index terms, and the two-item list.
There is no omission, mathematical polarity/quantifier/index defect, CJK
residue, encoding defect, exercise, hint, answer, solution, citation, or
external asset. Four proven source corrections O014-C040--C043 repair the
component-family notation, omitted `d_Z^n`, wrong category name, and cokernel
degree mismatch; all are disclosed exactly once and now registered in the
44-row correction ledger. The backend contains 37 unique sequential units,
1,899 unique segments, and 427 exact terminology concepts. A stale
`next_unit_id` chain from Units 026--036 was repaired; all 36 nonterminal units
now point to their actual successor and Unit 037 alone is terminal pending the
Unit 038 freeze.

The admitted shell-escape-disabled build is
`build/cumulative-unit-037-finalA-20260824`: XeLaTeX, Biber 2.21, both
MakeIndex passes, and four XeLaTeX passes. Biber resolves 19 citekeys;
MakeIndex accepts 167 term entries and 71 symbol entries with zero rejection
or warning. The 79,650-byte final log has SHA-256
`bcff49d344c09a3b34a68ac64b676fe6981bf1fa3526aa4cb46404f329065d84`
and zero error, undefined control/reference/citation, rerun request, overfull
box, missing character/file, fatal error, or emergency stop. Sixteen non-fatal
underfull horizontal boxes and seven underfull vertical boxes remain.

The build, checkpoint, and promoted cumulative reader are byte-identical: PDF
1.7, 223 pages, 1,127,663 bytes, SHA-256
`27e07599542a5994f99c6a43c4a8cebdfec4c2f2d3415e186fa79dea108facb0`.
It is `id-ID`, unencrypted, untagged, and has 44 outlines, 974 named
destinations, 749 valid internal actions, and 12 URI actions. All 52 fonts are
embedded; 11 mathematical fonts lack ToUnicode. Physical pages 1--8 and
209--223, including full-size pages 213--216, pass local and independent visual
inspection. The section, six diagram groups, footnotes, bibliography, and
indexes are centered and unclipped; the prior non-centered-reader defect does
not recur. QA receipt `qa/UNIT_037_QA.md` is 8,548 bytes, SHA-256
`7ea0827f6b28949cccda14231ff6217be51f10c1c766ba3743e37426e7bd6315`.

The exact 75-row admission manifest
`qa/CUMULATIVE_UNIT_037_FILE_MANIFEST.csv` lists 10,497,235 bytes, is 9,483
bytes, SHA-256
`46d35857206375e14e1810289633b74fa52031132d7a115c4783c59ef8d894d0`,
and independently re-verifies with zero missing file, duplicate path,
byte-count mismatch, or hash mismatch. The byte-identical frozen staging tree
`release/staging/unit-037-frozen` contains exactly those 75 files. Public
GitHub and Zenodo still correctly identify Unit 036 until the Unit 037 release
transaction completes; no premature public-boundary claim is made.

The next source-order boundary is Unit 038, the complete
`sec:cone-vs-long-exact-sequence`, `chapter3.tex` lines 1061--1292, stopping
before `sec:HH` at line 1293. Continue there without skipping. This admitted
checkpoint remains partial and does not complete the corpus pursuit.

## Unit 038 source freeze (2026-08-24)

The next production unit is now deterministically frozen as
`o014.aljabr2.chapter3.mapping-cone-and-long-exact-sequences`, the complete
Section 3.7 `sec:cone-vs-long-exact-sequence`. The source boundary is exactly
`chapter3.tex` lines 1061--1292, including the terminal blank line, and stops
before `sec:HH` at line 1293. The LF-normalized source witness
`tmp/unit038-source-slice.tex` is 17,739 bytes, SHA-256
`161c303deb0ff9f7d7a6dbd8341a1dae0e11086d794e68d812b6d3db334fe43e`;
an independent byte comparison against the frozen authority tree passes.

The map `tmp/unit038-segment-map.jsonl` has 63 unique, contiguous records.
The source has 13 labels, 43 `\ref`/`\eqref` occurrences over 22 resolved
unique targets, and two resolved citation keys (`KS06` and `Li1`). The map is
22,724 bytes, SHA-256
`2d258bb98975a650dc395a3b355da041d8d9dcb12719a7701037fc300d7e8794`.
All mapped intervals are monotone and remain inside lines 1061--1291. A bounded
static audit found no demonstrable source-correction candidate, no exercise,
hint, solution, external asset, or source comment. Translation must preserve
all labels, references, citations, environments, displays, and TikZ-CD
structure, and must not cross into the Hochschild section. Public preservation
still correctly reports Unit 036 until the admitted Unit 037 release completes.

## Unit 037 public preservation complete (2026-08-24)

The existing corpus-specific GitHub repository is now public through Unit 037
at commit `1c75e6d7691e460b8bb1a8c23888674e93dce18c`, tree
`6b47e4fda674de204cc116470d8e6b184daf97ca`. The immutable anonymous archive
contains 110 files, is 1,701,722 bytes, and has SHA-256
`b12bd4b67b67303f794180db2f63aaec1470eb7cfaa5dccdcbcb6516f93f288f`.
Both the 108-row `MANIFEST.csv` and 108-row `SHA256SUMS.txt` independently
reverify every payload blob with zero mismatch. The public 223-page PDF is
1,127,663 bytes, SHA-256
`27e07599542a5994f99c6a43c4a8cebdfec4c2f2d3415e186fa79dea108facb0`.
Sanitized receipt `release/github/GITHUB_PUBLICATION_RECEIPT.json` is 6,665
bytes, SHA-256
`6c9f3a6d029e853061f144226084951f36c7607c21e2fd194225ebcee11d58f3`.

The same admitted boundary advances only the existing Zenodo concept 22059751
to record 22086560, DOI `10.5281/zenodo.22086560`, version `unit-037`. Its seven
reader-first files total 1,517,978 bytes. Every anonymous public download
matches its local byte count and SHA-256; the record page, DOI, and concept
latest-alias all resolve to the new public version. Metadata preserves the
exact work title, author, `ind`, CC BY 4.0, independent-derivative and
non-endorsement statements, the single organization-contributor entry, and
the exact model disclosure `OpenAI Codex gpt-5.6-sol, Ultra`; the organization
label is absent from the title and description. No duplicate concept or
residual unpublished draft was created. Sanitized receipt
`release/zenodo/unit-037/ZENODO_PUBLICATION_RECEIPT.json` is 6,926 bytes,
SHA-256
`1f191028f01a817543b203b2047306d075f8c8192800341612c13a8dd4cdaa27`.

The public snapshot contains Units 001--037, 1,899 segments, 427 terms, and
corrections through O014-C043, with no Unit 038 byte or future correction.
Unit 038 remains the active local production boundary; this partial release
does not complete the corpus pursuit.

## Unit 038 translation draft (2026-08-24)

The complete draft `source/id-ID/chapter3-unit-038.tex` now covers all 63
mapped segments through source line 1291 and stops before `sec:HH`. After
independent review it is 434 LF-only UTF-8 lines, 25,223 bytes, SHA-256
`391faa18feede781394efefe0808ed3729650a5f014d2217efac05e4d2b35f08`,
with a terminal newline and no BOM. Preliminary deterministic counts match the
source at 13 labels, 43 reference occurrences, two citations, 16 TikZ-CD
environments, and 12 list items; 63 unique stable segment markers are present
in map order and no Han prose remains. Both independent audits now pass after
replacing one unidiomatic phrase, converting the sole not-yet-included Bab 4
reference to the established `\sourcecrossref` fallback, and repairing two
incorrect map annotations. The corrected 63-row map is 22,648 bytes, SHA-256
`56322e9fc22c7dc1ef8eb5fac6a9b09913011cf451f05f6cd5922ddd450e1ad8`.
`Aksioma rotasi` is added as the sole new terminology entry, bringing the
control/backend ledgers to 428 exact concepts. No mathematical source defect
or source correction is demonstrated. Backend and cumulative-build integration
are the next executable actions.

The single bounded Figshare Unit 037 attempt made no mutation: both the
authenticated account and project endpoints still return `403
Inactive/disabled account`, while the Indonesian collection remains publicly
readable. The existing article was not duplicated or modified. Sanitized
receipt `release/figshare/unit-037/FIGSHARE_PUBLICATION_RECEIPT.json` is 4,190
bytes, SHA-256
`67472fb2041d4564343eba6333e5e80a482256873cd98f8ca31c7d5ea182edd2`.
GitHub and Zenodo remain the verified current Unit 037 preservation surfaces.

## Unit 038 admitted checkpoint (2026-08-24)

Units 001--038 now form one contiguous admitted Indonesian reader through all
of `prelude.tex`, `chapter1.tex`, and `chapter2.tex`, plus `chapter3.tex` lines
9--1292 / Section 3.7. Unit 038 is
`o014.aljabr2.chapter3.mapping-cone-and-long-exact-sequences`, exact lines
1061--1292. Its frozen 17,739-byte source slice has SHA-256
`161c303deb0ff9f7d7a6dbd8341a1dae0e11086d794e68d812b6d3db334fe43e`;
its 63-record, 22,648-byte map has SHA-256
`56322e9fc22c7dc1ef8eb5fac6a9b09913011cf451f05f6cd5922ddd450e1ad8`.
The complete 454-line Indonesian target is 25,357 bytes, SHA-256
`85971b03546ce646f434602b3af499be7244fab17fa5944ed5987618a06ee2d1`.

Independent structural and semantic audits pass all 63 stable segments,
thirteen labels, 43 source-reference occurrences, both citations, 52 balanced
target environment pairs, sixteen TikZ-CD diagrams with 139 arrows, and twelve
list items. Four layout-only reflows remove all overfull lines while
preserving the exact maps, compositions, factors, signs, and claims. No source
exercise, hint, answer, solution, asset, or demonstrable correction occurs.
The source-correction ledger remains at 44 rows through O014-C043. The sole new
settled term is `aksioma rotasi`, bringing both terminology surfaces to 428
exact matching concepts.

The backend contains 38 unique sequential units and 1,962 unique segments.
`backend/units.jsonl` is 28,564 bytes, SHA-256
`c6d57531805acfb61275ead07455afd7a27c4d448ecd7c4b440abfa4dee72d51`;
`backend/segments.jsonl` is 575,630 bytes, SHA-256
`3f09a22da6f742859bbaba24721f78d1deb88f0bc3a7ad909820dc326148bbc5`.
All 63 Unit 038 backend rows exactly match the frozen map. The wrapper has 38
resolving inputs and 310 unique labels; all nineteen citations resolve against
the nineteen-entry bibliography.

The admitted shell-escape-disabled build is
`build/cumulative-unit-038-finalD-20260824`: XeLaTeX, Biber 2.21, both bounded
MakeIndex passes, and converged final XeLaTeX passes. Biber and both index
passes have zero warning/error or rejection. The 79,553-byte final log has
SHA-256
`d6648d30b969f1c515910e594f9b91ff397c631edfecd10dad1d69489d6e1aff`
and zero TeX/package error, undefined control/reference/citation, rerun request,
overfull box, missing character/included file, fatal error, or emergency stop.
Sixteen non-fatal underfull horizontal boxes and seven underfull vertical boxes
remain.

The build, checkpoint, and promoted cumulative reader are byte-identical: PDF
1.7, 231 pages, 1,162,756 bytes, SHA-256
`71293cdd594e6df12ddf7ea0c1ca74518e1a0ca5da530f91934a562426702a07`.
It is unencrypted and untagged, with 45 outline items, 1,007 named
destinations, 796 resolved internal links, and twelve HTTPS links. All 52 font
rows are embedded; eleven mathematical fonts lack ToUnicode. Fresh 120-dpi
inspection of the cover, attribution, all Section 3.7 pages, bibliography, and
indexes passes: the page is filled normally, and all prose, displays, diagrams,
equation numbers, footnotes, and indexes are centered, legible, and unclipped.
The complete qualification and contact-sheet hashes are in
`qa/UNIT_038_QA.md`, 9,568 bytes, SHA-256
`b012592ff91252b1dbb8fdbc880f3d8197170afcbe3a6c40e16cb5042e10c02e`.

The exact 75-row admission manifest
`qa/CUMULATIVE_UNIT_038_FILE_MANIFEST.csv` lists 8,443,225 bytes, is 9,470
bytes, SHA-256
`ca514d36eeea7489242ffc2b3aab685858c9805bcaa0ab5b8a103cd3be399b34`,
and re-verifies with zero missing file, duplicate path, byte-count mismatch, or
hash mismatch. Public GitHub and Zenodo still correctly identify Unit 037
until the Unit 038 release transaction completes; no premature public-boundary
claim is made.

The next exact source-order boundary is Unit 039,
`o014.aljabr2.chapter3.exercises-hochschild-homology-and-cohomology`, the
complete `sec:HH`, `chapter3.tex` lines 1293--1586, with substantive content
through line 1585 and a terminal blank separator at line 1586. It stops before
`sec:truncation-functors` at line 1587. Freeze its source witness and segment
map before translation. This admitted checkpoint remains partial and does not
complete the corpus pursuit.

## Unit 038 public preservation complete (2026-08-24)

The existing corpus-specific GitHub repository is public through Unit 038 at
commit `e129fc737546c3778eba6a96f975309fbe14c57b`, tree
`c033468e6edb1af5cc40d47c1a738f2e71020f45`. The immutable anonymous archive
contains 115 files, is 1,771,050 bytes, and has SHA-256
`c23ec8c757b6a8a86d5ec0749179ca8f526a16a3a0afd91125410f383b259f4d`.
The 113-row `MANIFEST.csv` and 113-row `SHA256SUMS.txt` both reverify every
canonical public blob with zero missing, extra, byte, or hash mismatch. The
first readback exposed four CRLF-checkout hashes that did not describe Git's
LF-normalized public blobs; corrective commit `e129fc7` repairs exactly those
inventory rows, and the complete second readback passes. The public 231-page
PDF is 1,162,756 bytes, SHA-256
`71293cdd594e6df12ddf7ea0c1ca74518e1a0ca5da530f91934a562426702a07`.
Sanitized receipt `release/github/GITHUB_PUBLICATION_RECEIPT.json` is 6,979
bytes, SHA-256
`a9b240310577020f9eb2d9dfd2b7ba0cca9c2b364e91dc9a22d59b68e6d7c817`.

The same admitted boundary advances only the existing Zenodo concept 22059751
to record 22087331, DOI `10.5281/zenodo.22087331`, version `unit-038`. Its seven
reader-first files total 1,562,324 bytes. Every anonymous public download
matches its local byte count and SHA-256; the record page, record DOI, concept
DOI, concept API latest alias, metadata, and sorted first PDF all pass. Metadata
preserves the exact work title, Wen-Wei Li creator attribution, `ind`, CC BY
4.0, independent-derivative and non-endorsement statements, the single
organization-contributor entry, and exact model disclosure `OpenAI Codex
gpt-5.6-sol, Ultra`; the organization label is absent from the title and
description. No competing concept or residual unpublished draft was created.
Sanitized receipt
`release/zenodo/unit-038/ZENODO_PUBLICATION_RECEIPT.json` is 6,977 bytes,
SHA-256
`ab21198f8c86c6d377d5afcb710ebe076c764a1cce36e84d5e312341f709ec3a`.

The public snapshot contains Units 001--038, 1,962 segments, 428 terminology
concepts, and corrections through O014-C043, with no Unit 039 byte or future
correction. One bounded Figshare preflight made no mutation because both the
account and project endpoints still return `403 Inactive/disabled account`;
the public collection remains readable, while the prior article endpoint
returns 404. Receipt
`release/figshare/unit-038/FIGSHARE_PUBLICATION_RECEIPT.json` is 4,190 bytes,
SHA-256
`22fbf23546b7602739202cc14ffa38934afffd18bccd8dbcf785662bf7c6dc68`.
GitHub and Zenodo are the verified current Unit 038 preservation surfaces.

## Unit 039 admitted checkpoint (2026-08-25)

Units 001--039 now form one contiguous admitted Indonesian reader through all
of `prelude.tex`, `chapter1.tex`, and `chapter2.tex`, plus `chapter3.tex` lines
9--1586 / Section 3.8. Unit 039 is
`o014.aljabr2.chapter3.exercises-hochschild-homology-and-cohomology`, exact
lines 1293--1586. Its frozen 22,932-byte source slice has SHA-256
`d94462e5d3d2868d7f6de812d6b888c927eb5c8611d52dcfb3a6b9104550325c`;
its 82-record, 28,522-byte map has SHA-256
`e7fe543ff2f5165924a3dd4fe99e6d6bb00417e9f76e3dbca4ef2b1195c9ad08`.
The complete 711-line Indonesian target is 35,023 bytes, SHA-256
`641c391d6a11b0d5276070b14253278a194ab820e2850d3be8223a6bf953d254`.

Independent structural, mathematical, language, and post-layout audits pass
all 82 stable segments, twelve labels, thirteen references, three citation
keys, 46 balanced environment pairs, ten TikZ-CD diagrams/48 arrows, one TikZ
figure, six list items, and 24 index commands. Seven TeX-native quote pairs
replace Unicode smart quotes without semantic change. Six demonstrated source
repairs, O014-C044--C049, correct a surplus tensor factor, a dual-boundary
index, undeclared two-argument Hochschild notation, reversed complex
arguments, a homology/cohomology typo, and the coefficient bimodule in the
cohomological SBI sequence. All are disclosed inline and in the 50-row source
correction ledger; no upstream message was sent.

Twenty first-use concepts bring both terminology surfaces to 448 exact
matching unique concept IDs. The backend contains 39 unique sequential units
and 2,044 unique segments. `backend/units.jsonl` is 29,357 bytes, SHA-256
`96d4bce4db97ba7cb737300eecdbb75ded1c4de974e54d1f501e2d046c57ccce`;
`backend/segments.jsonl` is 604,152 bytes, SHA-256
`688d32abdc574c69c82c83f9b03ef9e2679ab7e70fc22f01df4d0083b5d8a0fa`.
The final 82 backend rows exactly match the frozen Unit 039 map. The 39-input
wrapper and its mutable alias are byte-identical; the 21-entry bibliography
and its mutable alias are also byte-identical.

The admitted shell-escape-disabled build is
`build/cumulative-unit-039-finalC-20260825`: XeLaTeX, Biber 2.21, both bounded
MakeIndex passes, and converged final XeLaTeX passes. Biber and both index
passes have zero warning/error or rejection. The 84,606-byte final log has
SHA-256
`33fb1a38c0fa46dee4ca3fd3012c71b89b1f844ece7a2f66bd418250ed61e1bf`
and zero TeX/package error, undefined control/reference/citation, rerun
request, overfull box, missing character, fatal error, or emergency stop.
Seventeen non-fatal underfull horizontal boxes and seven underfull vertical
boxes remain.

The build, checkpoint, and promoted cumulative reader are byte-identical: PDF
1.7, 243 pages, 1,210,711 bytes, SHA-256
`11cabff2db7b4bdb1abaaf29be78a37fd5e16b4dd08b30f6debf88742f026f6a`.
It is unencrypted and untagged, with 46 valid outline entries, 1,049 valid
named destinations, 817 resolved internal links, fourteen HTTPS links, and 52
embedded/subset font rows. Twelve mathematical fonts lack ToUnicode. Fresh
120-dpi inspection of the corrected 3.8 cover, all Section 3.8 pages,
bibliography, and indexes passes: all prose, displays, diagrams, equation
numbers, footnotes, and indexes are centered, legible, and unclipped.

The complete qualification and contact-sheet hashes are in
`qa/UNIT_039_QA.md`, 9,656 bytes, SHA-256
`53a9b5b309ecc0ba1648781e1bf858a26d835414a01ab165aff3dbd8ec2f4bcf`.
The exact 76-row admission manifest
`qa/CUMULATIVE_UNIT_039_FILE_MANIFEST.csv` lists 7,592,101 bytes, is 9,591
bytes, SHA-256
`6c74c75ecbab1a4465b9cd65be2670fbc68bf9c3382242cc9503b26a121de972`,
and re-verifies with zero missing file, duplicate path, byte-count mismatch, or
hash mismatch.

The next exact source-order boundary is Unit 040,
`o014.aljabr2.chapter3.truncation-functors`, *Funktor pemenggalan*, exact
`chapter3.tex` lines 1587--1709, substantive through line 1708, stopping before
`sec:double-cplx-coh` at line 1710. The Unit 039 public transaction and
readback are recorded immediately below. This admitted checkpoint remains
partial and does not complete the corpus pursuit.

## Unit 039 public preservation complete (2026-08-25)

The existing corpus-specific GitHub repository is public through Unit 039 at
commit `37ead420edf108b4974a6a040812406fc12df039`, tree
`459b2f6c28e84ffab9f22a0aa153d2e058d9f67a`. Its immutable anonymous archive
contains 120 files, is 1,856,390 bytes, and has SHA-256
`3f196257bca21fd76662998e16bedb0ba288c302e310d4d00988ba0cda1361df`.
The 118-row `MANIFEST.csv` and 118-row `SHA256SUMS.txt` both reverify every
canonical public blob with zero missing, extra, byte, or hash mismatch. The
public 243-page PDF is 1,210,711 bytes, SHA-256
`11cabff2db7b4bdb1abaaf29be78a37fd5e16b4dd08b30f6debf88742f026f6a`.
The staged/public blob audit found no credential pattern, private user path,
personal name, or stray organization-label prose. Sanitized receipt
`release/github/GITHUB_PUBLICATION_RECEIPT.json` is 5,879 bytes, SHA-256
`797663d6c3a7e4ddab4295ce565d0a46d23da2645a72ca52ebdc4ba71ef80095`.

The same admitted boundary advances only the existing Zenodo concept 22059751
from record 22087331 to published record 22088565, DOI
`10.5281/zenodo.22088565`, version `unit-039`. Its seven reader-first files
total 1,627,091 bytes. Every credential-free public download matches its local
byte count and SHA-256; the record page, record DOI, concept DOI, concept API
latest alias, metadata, and sorted first PDF all pass. Metadata preserves the
exact work title, Wen-Wei Li creator attribution, `ind`, CC BY 4.0,
independent-derivative and non-endorsement statements, the single established
organization-contributor entry, and exact model disclosure `OpenAI Codex
gpt-5.6-sol, Ultra`; the organization label is absent from the title and
description. No competing concept or residual unpublished draft was created.
Sanitized receipt
`release/zenodo/unit-039/ZENODO_PUBLICATION_RECEIPT.json` is 7,202 bytes,
SHA-256
`f842947a29c953bcbeff661f4d5681403b867735bac09064e65eb7528e31531b`.

The public snapshot contains Units 001--039, 2,044 segments, 448 terminology
concepts, and corrections through O014-C049. It contains no Unit 040 byte or
future correction. Figshare remains truthfully at its last verified public
boundary because the account is inactive; no repeated mutation attempt or
duplicate article occurs. GitHub and Zenodo are the verified current Unit 039
preservation surfaces. Unit 040 is now the active production boundary. This
partial release does not complete the corpus pursuit.

## Unit 040 admitted checkpoint (2026-08-25)

Units 001--040 now form one contiguous admitted Indonesian reader through all
of `prelude.tex`, `chapter1.tex`, and `chapter2.tex`, plus `chapter3.tex` lines
9--1709 / Section 3.9. Unit 040 is
`o014.aljabr2.chapter3.truncation-functors`, *Funktor pemenggalan*. Its exact
10,217-byte normalized-LF source slice has SHA-256
`7954b37ef2279d82e9ce3d8e56f6ce218ccd839970a684189b6315a3f67a48be`;
its 33-record map has SHA-256
`d2488a8f085baec85fbfc199198db009f9b85f0da996533ec12dde64dd2e62a2`;
and its independently audited 14,865-byte Indonesian target has SHA-256
`073c9ddbc20430ecb37ee80658f73f5b20756919ec38ffe7807c77130291c9b0`.

All 33 mapped segments, nine labels, six references, 22 environment pairs,
58 diagram arrows, eight index writes, formulas, signs, shifts, and adjunction
directions pass. Four disclosed source repairs O014-C050--C053 cover the
missing Abelian hypothesis, comparison-map antecedent, Coim/Image component
typing, and wrong object category. Three bounded-complex terms bring both
terminology surfaces to 451 exact-matching concepts. The modular backend now
contains 40 units and 2,077 unique segments; its final 33 rows exactly match
the frozen Unit 040 map.

The admitted build is `build/cumulative-unit-040-finalD-20260825`. Biber
resolves all 21 citations and both MakeIndex passes accept 182 terminology and
88 symbol entries with no warning or rejection. The final log has zero error,
undefined reference/citation, rerun request, overfull box, missing character,
or fatal stop. The build, checkpoint, and promoted cumulative reader are
byte-identical: 247 pages, 1,230,437 bytes, SHA-256
`15976f12f8a401766cfeca2d446abd780ced1ddeedf812b2e65204d346b73ebf`.
Strict PDF and fresh full-size render inspection pass; the reflowed boundedness
table, duality display, diagrams, notes, bibliography, and indexes are centered,
legible, and unclipped. QA receipt `qa/UNIT_040_QA.md` is 9,489 bytes, SHA-256
`e7eab8020a62d6a1994212742e73b573de6520f92ffed8ec1c412e8e49171705`.
The 77-row admission manifest lists 12,119,914 bytes, is 9,716 bytes, SHA-256
`70afa2bf1a259fd69333bb61ca9e863e0b95b47341b2924515d6d6b27cc95a88`,
and re-verifies with zero missing, duplicate, byte-count, or hash mismatch.

The output-argument parsing failure that created a literal `$out` directory is
closed: exactly eleven failed-build files / 1,651,491 bytes were verified in
the no-overwrite archive
`old stuff/o014_unit040_failed_literal-output-build_01a02164_20260825-034221.zip`,
SHA-256
`3b98158aeb8ad61ad818d352f340f7d8145a6fc2a8199ca7cd2cbf5bfddb83f7`,
then both loose failed roots were deleted. The finalD canonical build and QA
surfaces are retained.

After admission, the two superseded overflow-build trees, inspected individual
page renders, and redundant finalD console captures (70 files / 5,984,538
bytes) were likewise verified in the no-overwrite archive
`old stuff/o014_unit040_superseded_builds_and_render_transients_01a02164_20260825-041115.zip`,
SHA-256
`3762c561607547799ab7ac1a86f48342ca2dc59bf1c0e94a9ccf2f477727b732`,
then deleted. Canonical finalD artifacts and the three contact sheets remain.

The later explicit cleanup boundary archived only the three obsolete Unit 038
candidate build trees (finalA/finalB/finalC): 45 files / 6,086,501 bytes into
`old stuff/o014_unit038_superseded_candidate_builds_01a02164_20260825-041840.zip`
(5,028,153 bytes; SHA-256
`7db65aee4716316fa7dab0528db6c6ca8dea97cfc424a3500e51a71f2df948ea`).
Entry names, uncompressed sizes, and hashes verified before exact-root
deletion. Successful final builds, canonical evidence, and publication files
were deliberately retained.

GitHub and Zenodo now publish the admitted Unit 040 boundary. The corrected
GitHub head is commit `cd61ef96eda025a072deffbe98de451ef236dc05`, tree
`fb94b4915b3f8920ef1b47f4eac5a2aa9dae31bb`; its immutable archive is
1,903,798 bytes, SHA-256
`adb26734ceaae10a01af0f292e682671b2e561331507385f345eb275dd3d301f`.
Anonymous readback verifies 123 payloads with zero missing, unlisted,
duplicate, byte, hash, or cross-inventory mismatch; the PDF exactly matches
the admitted 1,230,437-byte reader. Zenodo record `22096566`, DOI
`10.5281/zenodo.22096566`, advances the existing concept `22059751` as
`unit-040`. All seven public files total 1,658,212 bytes and match the local
package byte-for-byte and SHA-256; both DOI routes resolve to this record, and
the concept-latest API returns it. Sanitized receipts are
`release/github/GITHUB_PUBLICATION_RECEIPT.json` and
`release/zenodo/unit-040/ZENODO_PUBLICATION_RECEIPT.json`.

After both sanitized receipts were validated, the two GitHub readback folders
(initial failing inventory and corrected passing inventory) and the passing
Zenodo readback folder became redundant loose copies. Their exact 13 files /
7,932,488 bytes were archived as
`old stuff/o014_unit040_public_readbacks_01a02164_20260825-151616.zip`
(7,685,984 bytes; SHA-256
`18eaaafbc65c8e7b7c7526641621f6b85bcea4d866b14b35bb94296dbc430358`).
Every ZIP entry name, uncompressed byte count, and SHA-256 matched before the
three exact loose directories were deleted. Canonical packages, public files,
and sanitized receipts remain live.

The next exact boundary is Unit 041,
`o014.aljabr2.chapter3.double-complex-cohomology`, *Kohomologi bikompleks*,
the complete `chapter3.tex` lines 1710--1881, stopping before
`sec:resolutions` at line 1882. This published checkpoint remains partial and
does not complete the corpus pursuit.

At the next explicit cleanup boundary, the now-superseded Unit 038 finalD and
Unit 039 finalC build trees and their rendered-page sets (36 files / 8,287,867
bytes) were verified in
`old stuff/o014_superseded_unit038-039_builds_and_renders_01a02164_20260825-154253.zip`
(7,290,676 bytes; SHA-256
`833bccd43e990ddf2ad967c0a08cfc84277f5614c665b60c03c00409ceb702d2`)
before the four exact loose directories were deleted. The Unit 040 canonical
build/render evidence and all active Unit 041, source, control, backend, QA,
and release materials remain live.

Unit 041, `o014.aljabr2.chapter3.double-complex-cohomology`, is now locally
admitted. It covers the complete `chapter3.tex` lines 1710--1881 and stops
before `sec:resolutions` at line 1882. The exact 14,167-byte source witness has
SHA-256
`fac229cb4d731ecac5486304c8f4f172d0f8522adede60034b5060616d04ccfa`;
the 43-record map is 13,693 bytes / SHA-256
`ef38bad8dc30390e2b8057c17ee5d113e5f7b4c7eba3d08a6d111b08decd444b`;
and the final 20,059-byte Indonesian target has SHA-256
`8ad7d65cc4681252b6ff4e71f8bd4e3cbdcbfca6416cd538f3fa75c31b1f1367`.
Independent structural, semantic, and focused delta reviews pass. Disclosed
repairs O014-C054 and O014-C055 cover object/functor typing and the distinction
between a quasi-isomorphism and a chain-level isomorphism. Both ledgers have
454 exact-matching terminology concepts; the backend has 41 unique units and
2,120 unique segments.

The admitted build is `build/cumulative-unit-041-finalD-20260825`. Biber
resolves all 21 citations and both MakeIndex passes accept 182 terminology and
93 symbol entries with no rejection or warning. The final log has zero error,
undefined reference/citation, rerun request, overfull box, missing character,
or fatal stop. The build, Unit 041 checkpoint, and promoted cumulative reader
are byte-identical: 253 pages, 1,255,777 bytes, SHA-256
`f364d2c3b6839a14b89f77313f9e3117dc9b7b5e5ad920d27637924513d5a29f`.
Strict PDF checks and fresh full-size rendering pass after moving two crowded
quasi-isomorphism labels into adjacent prose. QA receipt `qa/UNIT_041_QA.md`
is 9,621 bytes, SHA-256
`d515d3a6e28fe4c25d99f910e5383e8b58bd56bcbce8ba8238a33ce77e52bc71`.
The 78-row admission manifest lists 6,851,782 bytes, is 9,820 bytes, SHA-256
`b7271d4b4e429125dcf474d0b1810933cc559bf17b574c5f8b38830822a843dc`,
and re-verifies with zero mismatch.

After finalD admission, the three superseded Unit 041 build candidates and the
obsolete finalC render set (100 files / 10,539,388 bytes) were verified in
`old stuff/o014_unit041_superseded_builds_and_renders_01a02164_20260825-161628.zip`
(8,798,871 bytes; SHA-256
`f2cf861907e647d9177784ca0f045fcff8f077a1552ad007a91f02c3422f30ed`)
before the four exact loose directories were deleted. The finalD build and
render evidence remain live.

GitHub and Zenodo still expose the earlier Unit 040 boundary while Unit 041
release packaging is in progress. The next exact source cursor is Unit 042,
`o014.aljabr2.chapter3.resolutions`, `chapter3.tex` lines 1882--2214,
stopping before `sec:derived-primer` at line 2215. This partial checkpoint does
not complete the corpus pursuit.

Unit 041 is now public and anonymously verified in both existing lineages.
GitHub `main` is commit
`98bc2fec01c8e7a1e987f46cfaf519e9b9ee2e6c`, tree
`ad28c286f4e07ffc847fff339d2c509f49ed099e`. Its immutable 1,957,201-byte
archive has SHA-256
`3badbdddb20a602a208ddce629fb17a6d96d0850bb616b8a3761fd9a261a7b2e`.
Anonymous codeload, raw-reader, raw-README, repository-page, and commit-page
readback passes: 128 payload rows and 128 checksum rows have zero missing,
unlisted, byte, or hash mismatch, and the public PDF remains the exact
1,255,777-byte admitted reader. An initial Unit 041 commit exposed task-local
absolute archive paths in provenance-only text; it was replaced with
force-with-lease after path sanitization, cursor repair, inventory
regeneration, and a second complete anonymous readback. No private path,
credential-like string, or stale Unit 040 cursor remains in the final head.
The sanitized receipt is
`release/github/GITHUB_PUBLICATION_RECEIPT.json`, 6,683 bytes, SHA-256
`8abb97ec439bbd96cb26b1d9384c6e31d44addd0813bae3864e2cb67baca5196`.

Zenodo record `22098141`, DOI `10.5281/zenodo.22098141`, advances the
existing concept `22059751` as version `unit-041`; it does not create a
competing concept. Seven reader-first files total 1,693,098 bytes. Anonymous
record, page, DOI, concept-DOI, concept-latest, and per-file readback passes
with zero filename, byte, or SHA-256 mismatch. The PDF is first, 253 pages,
unencrypted, and still honestly identified as untagged. The exact work title
is preserved without an organization label in the title or description; the
single organization-contributor metadata entry is preserved. The sanitized
receipt is
`release/zenodo/unit-041/ZENODO_PUBLICATION_RECEIPT.json`, 7,545 bytes,
SHA-256
`5a52ac1af8d25cf06ecdf1d479424160e052b193051b39e4cb798a85fb9ecbca`.

After the receipts passed, three redundant loose public-readback directories
(274 files / 15,679,484 bytes) were verified in the no-overwrite archive
`old stuff/o014_unit041_public_readbacks_01a02164_20260825-165331.zip`
(11,796,299 bytes; SHA-256
`4c7e83208853f83e14e7a7b2dfc65395171a6b2a540c939dc9eefb11979a4a87`)
before the exact loose directories were deleted. Canonical release packages,
sanitized receipts, current source/backend, finalD build/render evidence, and
the promoted reader remain live.

The complete corpus pursuit remains active. Resume next at Unit 042,
`o014.aljabr2.chapter3.resolutions`, by freezing and mapping exactly
`chapter3.tex` lines 1882--2214 and stopping before
`sec:derived-primer` at line 2215.

Unit 042, `o014.aljabr2.chapter3.resolutions`, is now locally admitted. It
covers the complete `chapter3.tex` lines 1882--2214, with substantive content
through line 2213, and stops before `sec:derived-primer` at line 2215. The
333-line normalized-LF source witness is 27,644 bytes, SHA-256
`75da0a5963f8e3bf2cec5fbe6a4007fea1c1b27faca6bd54528ac8957547ebfa`;
the 102-record map is 29,370 bytes, SHA-256
`2581b89bc0485cc25e8c6dbbdf72402d16bd6a58b2ba0c24b6d4d2772c88eb7e`;
and the final Indonesian target is 39,646 bytes, SHA-256
`8d82d95029a29901862007a63ae2311fd215c576811e6b646770798d2968736e`.
Independent structural and semantic review passes after four disclosed,
type-preserving repairs, O014-C056 through O014-C059. The terminology surfaces
have 457 exact-matching concepts; the backend has 42 unique units and 2,222
unique segments, with its final 102 rows line-identical to the frozen map.

The admitted build is `build/cumulative-unit-042-finalD-20260825`. Biber
resolves all 21 citekeys, and the two MakeIndex passes accept 187 terminology
and 93 symbol entries with no rejection or warning. The final log has zero
TeX/package error, undefined reference/citation, rerun request, overfull box,
missing character, fatal error, or emergency stop. The build, checkpoint, and
promoted reader are byte-identical: 265 pages, 1,309,971 bytes, SHA-256
`11037fbd52c9bdea1b18a449fbf8395f89ad6716b4c080035565ffc71f2d7491`.
Strict structural checks and fresh 120-dpi rendering of the front matter, all
Unit 042 pages, and the complete backmatter pass. The PDF is navigable and
searchable but remains untagged; twelve mathematical font rows lack ToUnicode,
so no fully semantic accessibility claim is made.

The 79-row admission manifest
`qa/CUMULATIVE_UNIT_042_FILE_MANIFEST.csv` lists 10,952,634 bytes and
re-verifies 79 unique paths with zero missing, duplicate, byte-count, or hash
mismatch. It is 9,947 bytes, SHA-256
`829961cb5e76ad4a031d06240b14084acccbea50092eaded5cf1f7709197ffae`.
The Unit 042 QA receipt is 9,285 bytes, SHA-256
`9bcc87d3483b439ac4381760241880a3a139671c98660eacb62817a0de787f66`.
GitHub and Zenodo still expose Unit 041 while this admitted boundary is being
packaged, so the local completion status remains publication-pending.

The next exact boundary is Unit 043,
`o014.aljabr2.chapter3.classical-derived-functors`, *Funktor turunan
klasik*, the complete `chapter3.tex` lines 2215--2552. Its 338-line
normalized-LF slice is 27,132 bytes, SHA-256
`ac95a737c3df39dff8ece789057d2ad3ce93474b258476245b2fcc67d074dbb9`,
and it stops before `sec:lim1` at line 2553. Two high-confidence typed source
repairs at lines 2345--2346 and 2538--2539 are reserved as O014-C060 and
O014-C061 for independent verification during translation. This checkpoint is
partial and does not complete the corpus pursuit.

Unit 042 is now public and anonymously verified in both existing lineages.
GitHub `main` is commit
`3a8062fb77b60c456f560523508885445db57c3a`, tree
`147809a3a936e447a20d4287dcd818a8be2610e0`. Its immutable codeload
archive is 2,044,848 bytes, SHA-256
`c576bbc934cfe7a387aff1e5140023a28f6fe838ef04e0d6b503ad84ce35dd48`.
Credential-free repository-page, commit-page, raw-reader, raw-README, and
archive readback pass. The archive has 135 files: 133 manifest/checksum
payload rows plus the two inventories. Every path, byte count, and SHA-256
matches; there is no unlisted payload, private-path/name match, Unit 043
source, or correction identifier beyond O014-C059. The public PDF is the exact
1,309,971-byte admitted reader. Sanitized receipt
`release/github/GITHUB_PUBLICATION_RECEIPT.json` is 6,273 bytes, SHA-256
`7c2eaaa5122ac3dd1c6f556709f60a5c2cbb4c65a1f11ca04bbc3be237379533`.

Zenodo record `22102326`, DOI `10.5281/zenodo.22102326`, advances the
existing concept `22059751` as version `unit-042`; no competing concept was
created. Seven reader-first files total 1,774,270 bytes. Anonymous record,
page, DOI, concept-DOI, concept-latest, and per-file readback pass with zero
filename, byte, or SHA-256 mismatch. The 60-entry source/backend ZIP and
11-entry QA/provenance ZIP independently re-verify their internal manifests.
The PDF is first by filename, 265 pages, unencrypted, and truthfully untagged.
The exact work title contains no organization label; the single inherited
organization-contributor entry is preserved, and the description contains no
repeated organization prose. Sanitized receipt
`release/zenodo/unit-042/ZENODO_PUBLICATION_RECEIPT.json` is 7,588 bytes,
SHA-256
`18bb8cbe7e931c706802337f43902230187395b24e5d766f792791465aec554c`.

The complete corpus pursuit remains active. Resume at the already bounded Unit
043, `o014.aljabr2.chapter3.classical-derived-functors`,
`chapter3.tex` lines 2215--2552, before `sec:lim1` at line 2553.

Unit 043, `o014.aljabr2.chapter3.classical-derived-functors`, is now
locally admitted. It covers complete Section 3.12, `chapter3.tex` lines
2215--2552, with substantive content through line 2551, and stops before
`sec:lim1` at line 2553. The normalized 338-line source witness is 27,132
bytes, SHA-256
`ac95a737c3df39dff8ece789057d2ad3ce93474b258476245b2fcc67d074dbb9`;
the 105-record map is 32,475 bytes, SHA-256
`2712c57d9a9066fb1a119037857552c0c331abd20d91c86a3c41c56de1a542cd`;
and the final Indonesian target is 40,571 bytes, SHA-256
`80d7ba5a71f45c418ac8278ac03ee6409d23bc7bc48dcf52310096d0ae153d54`.
Independent mathematical, terminology, and prose reviews pass, as does the
final topology and residue replay. Three disclosed, type-preserving source
repairs, O014-C060 through O014-C062, correct two diagram objects, two
connecting-map degrees, and the zero-extension boundary at degree zero.

Both terminology surfaces have 467 unique, exact-matching concepts. Ten new
controlled concepts cover the classical/right/left/higher derived functors,
both delta-functor directions and their universal forms, `F`-acyclic
objects, and dimension shifting. Effaceable and coeffaceable are active;
hyperderived remains honestly provisional. The backend has 43 unique units
and 2,327 unique segments, and its last 105 rows are line-identical to the
frozen Unit 043 map.

The admitted build is `build/cumulative-unit-043-finalD-20260825`. Biber
resolves all 21 citekeys, and MakeIndex accepts 195 terminology and 95 symbol
entries with no rejection or warning. The final 80,536-byte log, SHA-256
`e96f51b93b205e06f432e19ada8f0bb9e16569944caa2d46008e4fcfdd4b8e58`,
has zero TeX/package error, undefined reference/citation, rerun request,
overfull box, missing character, fatal error, or emergency stop. Eighteen
underfull hboxes and seven underfull vboxes remain non-fatal.

The build, checkpoint, and promoted reader are byte-identical: PDF 1.7, 275
pages, 1,361,656 bytes, SHA-256
`15a22aa8f55fefd7ba0d10840e3719bd3718d6af6ceda63eedf919db24250ac1`.
Strict parsing verifies 50 outline entries, 1,189 named destinations, 937
internal and fourteen URI links, all resolved and within page bounds. The
reader is unencrypted and untagged; all 52 fonts are embedded/subset, while
twelve mathematical fonts lack ToUnicode maps, so no fully semantic
accessibility claim is made. Full-size inspection covers front pages 1--5,
every Unit 043 page 255--266, and backmatter pages 267--275. All formulas,
seventeen diagrams, three notes, bibliography pages, and both indexes are
centered, legible, and unclipped.

The QA receipt `qa/UNIT_043_QA.md` is 10,181 bytes, SHA-256
`45c438d62bd1b6306e05d60db03599e42a66a4354f3cb22d209ed3630b7fc74b`.
The 80-row admission manifest
`qa/CUMULATIVE_UNIT_043_FILE_MANIFEST.csv` lists 8,342,643 bytes, is 10,069
bytes, SHA-256
`ea52868bcecc97dabd75ac6a0935f1bbefb5ffe2f07fca7aec3cabc23fe2822c`,
and re-verifies 80 unique paths with zero missing, duplicate, byte-count, or
hash mismatch.

GitHub and Zenodo still expose the independently verified Unit 042 boundary
while Unit 043 is packaged into those same lineages. The next exact
source-order boundary is Unit 044,
`o014.aljabr2.chapter3.example-lim1`, complete `sec:lim1`,
`chapter3.tex` lines 2553--2713, with content through line 2712 and a
terminal blank at 2713. Its normalized 161-line authority slice is 13,478
bytes, SHA-256
`2b8a923963fba1f31a9c5f7bfd98e5381a4a1b194f70cd3b7d002fa05a68298e`,
and it stops before `sec:Ext-Tor` at line 2714. This checkpoint remains
partial and does not complete the corpus pursuit.
