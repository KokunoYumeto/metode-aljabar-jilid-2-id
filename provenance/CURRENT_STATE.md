# O014 current state

Status: active source-order Indonesian production. Units 001--028 are complete,
admitted, built, and QA-passed without a source gap through
`chapter2.tex` line 1563. This remains a partial working edition; do not
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
seventeen exercises, and ten hints. Units 020--028 translate `chapter2.tex`
lines 9--1563: the overview, Abelian-category definition, first look at
complexes, diagram lemmas, lattice-theory overview, direct-sum decomposition,
Subobjek dan Teorema Isomorfisme, and Objek Sederhana dan Semisederhana.

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

The backend contains 28 sequential units and 1,387 unique segments.
`backend/units.jsonl` is 20,820 bytes, SHA-256
`f1dd95c50b2cde67c216df17a209aa6287bf26fd9dc6bb118bed79dc98ec7ae4`;
`backend/segments.jsonl` is 400,163 bytes, SHA-256
`91abf38aa24cbbe8104cbb61a118b443bc840baf3274e44c6386d56adc46de04`.
Both terminology surfaces now contain 382 unique, matching IDs:
control `controls/TERMINOLOGY_O013_O014.csv` SHA-256
`8aff5bad2fb43e8319426e54df1ff0ba48abf580ce5f8a3ceeb378a176cea8e3`;
backend `backend/terms.csv` SHA-256
`eee2687340596e47610add6920f5a60982bdeba56d6cb91eba2cf93020f5a7f0`.

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
from public payloads. The report is
`controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`, 7,965 bytes, SHA-256
`8f112facd6d58c728d9e18d7b34a050064b62a8b0a2c2645d49682d4dbe98cd1`.
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

## Latest admitted reader (Unit 028)

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

## Exact continuation

The next source cursor is `chapter2.tex` line 1564, where the authority begins
the section labeled `sec:Serre-subcat` (`Serre 子范畴和
\texorpdfstring{$\mathrm{K}_0$}{K0} 群`). Before translation, freeze that
section's exact source slice, topology, map, and terminology in the same
bounded manner. Continue in source order without skipping exercises or hints;
the next executable action is the Unit 029 source audit and map.

## Public preservation

GitHub remains the existing edition repository
<https://github.com/KokunoYumeto/metode-aljabar-jilid-2-id>, branch `main`,
public through Unit 027 at commit
`3b0ec2283199f58fd5078c8cbb07410c34077329`, tree
`3d0554f2ebb37663124c4f8c68844c3179a41048`; anonymous archive/readback passed
with zero missing, unexpected, or hash-mismatched files. Unit 028 is built and
ready for the next authorized advancement of this same lineage; never create a
duplicate.

Zenodo is one concept lineage: Unit 027 is public as record 22071108, DOI
`10.5281/zenodo.22071108`, concept 22059751,
`10.5281/zenodo.22059751`, version `unit-027`, with seven files and zero
anonymous byte/hash mismatches; receipt:
`release/zenodo/unit-027/ZENODO_PUBLICATION_RECEIPT.json`. An intermediate
same-lineage record 22071092 was published with inherited files during the
transaction and cannot be deleted through the deposit API; the receipt records
its residual state and the clean latest seven-file record.

Figshare remains one work-level item, article 33314775, public version 3,
DOI `10.6084/m9.figshare.33314775.v3`, CC BY 4.0, in project 280296 and
collection 8668413. A reader-first Unit 027 seven-file payload (1,130,394
bytes) is prepared locally but no mutation occurred: the account endpoint
returned 403 `InactiveAccount`, the article endpoint returned 404, and the web
surface returned 502/202. Blocker receipt:
`release/figshare/unit-027/FIGSHARE_PUBLICATION_RECEIPT.json`.

Continue contiguous source-order production. This checkpoint does not complete
the pursuit.
