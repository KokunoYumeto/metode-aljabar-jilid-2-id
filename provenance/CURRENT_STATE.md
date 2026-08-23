# O014 current state

Status: active source-order Indonesian production. Units 001--026 are complete,
admitted, built, and QA-passed without a source gap through
`chapter2.tex` line 1132. This remains a partial working edition; do not
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
seventeen exercises, and ten hints. Units 020--026 translate `chapter2.tex`
lines 9--1132: the overview, Abelian-category definition, first look at
complexes, diagram lemmas, lattice-theory overview, direct-sum decomposition,
and Subobjek dan Teorema Isomorfisme.

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

The backend contains 26 sequential units and 1,236 unique segments.
`backend/units.jsonl` is 19,337 bytes, SHA-256
`1f7ab70854830c6ebc415a9345469514f5e4ec8bd4b68b400ccbe483aff93e01`;
`backend/segments.jsonl` is 349,612 bytes, SHA-256
`484ca4d97d0532cb0fb110f2a4748572d614ded21ced4b13287d6cea932523fc`.
Both terminology surfaces now contain 366 unique, matching IDs:
control `controls/TERMINOLOGY_O013_O014.csv` SHA-256
`5ec2c7be6b48a0272a169fe6ff4b0b1b426c9e627fa9be1b5588257fadc2ac97`;
backend `backend/terms.csv` SHA-256
`65ee12e5df18726eea287d2135b718f85d2d65ccf0599de7146b6c7258beb935`.

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

## Latest admitted reader

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

## Exact continuation

The next source section begins at `chapter2.tex` line 1133 and ends at line
1244; line 1245 begins `sec:inj-proj`. The bounded authority slice is
8,321 bytes, SHA-256
`e2f435c542379cd0f924343bd552514be261d8827dfa53afd107e20722ec213b`.
Stable ID: `o014.aljabr2.chapter2.simplicity-and-semisimplicity`; source
label `sec:semisimple`; planned Indonesian title `Objek Sederhana dan
Semisederhana`. The source audit found one convention, two definitions, one
definition-theorem, three lemmas, two propositions, two remarks, six proofs,
five display-math blocks, six labels, thirteen references, two citations,
eleven index commands, one footnote, no diagrams/assets, and no exercises or
hints. The exact segment map is to be frozen before translation. Retain
`objek sederhana`, `objek semisederhana`, `deret komposisi`, `faktor
komposisi`, `teorema Jordan--Hölder`, `Lema Schur`, `gelanggang
pembagian`, `multihimpunan`, `terbelah`, `Noetherian`, and `Artinian`
consistently.

## Public preservation

GitHub remains the existing edition repository
<https://github.com/KokunoYumeto/metode-aljabar-jilid-2-id>, branch `main`,
public through Unit 025 at commit
`8f5333773e6103f917a4afaf93f84cf80a241630`, tree
`f64bb86429407be4193b433136da619d12828a62`; Unit 026 release preparation is
ready and must advance that lineage, never create a duplicate.

Zenodo is one concept lineage: public Unit 025 record 22062526, concept
22059751, DOI `10.5281/zenodo.22062526`; Unit 026 release preparation is
pending in the same concept.

Figshare is one work-level item, article 33314775, public version 3, DOI
`10.6084/m9.figshare.33314775.v3`, CC BY 4.0, in project 280296 and
collection 8668413. The seven-file reader-first Unit 025 payload totals
1,034,298 bytes and passed anonymous filename/byte/hash readback. Receipt:
`release/figshare/unit-022/FIGSHARE_PUBLICATION_RECEIPT.json`, 4,362 bytes,
SHA-256 `f3bbdc670dce089eb53d9118db2164a3fd8aaf4ada57ac7dc351b55f68c108e1`.

Continue contiguous source-order production. This checkpoint does not complete
the pursuit.
