# O014 current state

Status: active source-order Indonesian production. Units 001--032 are complete,
admitted, built, and QA-passed without a source gap through `chapter3.tex`
line 162. This remains a partial working edition; do not
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

## Latest admitted reader (Unit 032)

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

## Exact continuation

The next frozen source unit is Unit 033,
`o014.aljabr2.chapter3.hom-complex-and-homotopy`, exactly `chapter3.tex`
lines 163--345, section `sec:Hom-cplx`; substantive content ends at line 344
and line 345 is its blank separator. Its normalized 12,347-byte slice has
SHA-256
`30e6afb74eae4ea7aa78d610a2806c713faa3d0e7f893e16f0565a0ce379e59c`;
the 56-record, 16,810-byte stable map has SHA-256
`0798cc52a5cf5e9c49c9132039d58e74f95e7d653348d6e4367708214a2d11c2`.
It contains 15 labels, 20 reference/equation-reference occurrences, three
definitions plus one definition-proposition, four lemmas, two propositions,
six proofs, one remark, 19 mapped display blocks including four TikZ-CD
environments, one two-item list, and eight index commands. It has no citations,
footnotes, exercises, hints, solutions, or external assets. Translation must
stop before line 346, `sec:mapping-cone`.

## Public preservation

GitHub remains the existing edition repository
<https://github.com/KokunoYumeto/metode-aljabar-jilid-2-id>, branch `main`,
public through Unit 031 at commit
`b194a5ff973e53790564860c9054e5b8736bb2f2`, tree
`1d3728351c64dab3cee68784986aae89ca7db377`. The immutable anonymous archive
has 80 files, 1,401,778 bytes, SHA-256
`a875a5c1c118d0a0545934aea16b9402a355f74411190bb6080598637bdd4da0`;
repository, commit, raw, archive, manifest, checksum, and 191-page reader
readback passed with zero mismatch. Receipt
`release/github/GITHUB_PUBLICATION_RECEIPT.json` is 4,740 bytes, SHA-256
`82d393ca2ca3998c11cd6055cfdc63c2270254a5b6d0f19b0bc3ca14b5394f66`.

Zenodo remains one concept lineage, 22059751. The clean latest Unit 031 record
is 22072584, DOI `10.5281/zenodo.22072584`, version `unit-031`: seven files
totaling 1,340,041 bytes. Every anonymous file download matches local bytes
and SHA-256; the record API/page, DOI, and concept-latest readbacks all return
HTTP 200. The reader-first payload freezes exactly 31 units, 1,600 segments,
and 411 terms. No Unit 032 material or restricted terminology witness leaked
into the release. Receipt
`release/zenodo/unit-031/ZENODO_PUBLICATION_RECEIPT.json` is 7,232 bytes,
SHA-256
`0aa083c4a4789d8ebe30e7b8873fc71c904e4552aaa9e3d203c4b0902c387d7d`.
The prior records remain immutable; no competing concept or
unpublished draft was created.

Figshare remains one work-level item, article 33314775, public version 3,
DOI `10.6084/m9.figshare.33314775.v3`, CC BY 4.0, in project 280296 and
collection 8668413. A reader-first Unit 027 seven-file payload (1,130,394
bytes) is prepared locally but no mutation occurred: the account endpoint
returned 403 `InactiveAccount`, the article endpoint returned 404, and the web
surface returned 502/202. Blocker receipt:
`release/figshare/unit-027/FIGSHARE_PUBLICATION_RECEIPT.json`.

Continue contiguous source-order production. This checkpoint does not complete
the pursuit.
