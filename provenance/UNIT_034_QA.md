# O014 Unit 034 admission and reader QA

Date: 2026-08-24  
Unit: `o014.aljabr2.chapter3.mapping-cone`  
Title: *Kerucut pemetaan*  
Result: **PASS — translated, independently reviewed, built, rendered, and admitted**

## Authority and exact scope

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled Gitee `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 034 is
exactly Section 3.3, `chapter3.tex` lines 346--621 inclusive. The next
unadmitted source is line 622,
`\section{相反范畴上的复形}\label{sec:opposite-cplx}`.

The normalized-LF authority slice is `tmp/unit034-source-slice.tex`, 18,021
bytes, SHA-256
`0640f89fb580226e49e7663880d487fea235d21fbe5e510e842bc782b9eafa35`.
It is byte-equal to the frozen authority range. The 80-record stable-ID map is
`tmp/unit034-segment-map.jsonl`, 21,373 bytes, SHA-256
`d2cf4ff2a6a8ce6da91171bfce6df365cdf58b8ef33421273e5b15185d77052b`.

## Translation, topology, and mathematical review

The admitted target is `source/id-ID/chapter3-unit-034.tex`, 24,865 bytes,
SHA-256
`8cd871b192324139083c3a3bd206418b37b0d9bceede23db6279c223f0b6da03`.
It translates the complete section without abridgment. The source range has no
exercise, hint, answer, solution, citation, footnote, external figure, or
external asset.

All 80 stable markers are unique and occur in exact map order. The Unit-034
backend has 80 rows in exact map parity. Source/target topology passes for all
13 labels, 15 references, three definitions, five propositions, two lemmas,
five proofs, two remarks, one example, five lists with 13 items, 9 index
commands, seven TikZ-CD diagrams, and the embedded TikZ matrix. The functional
lemma labels `prop:cone-alpha` and `prop:cone-beta`, and all source uses of the
mixed `\Cyl`/`\mathrm{Cyl}` notation, remain authority-faithful.

Independent review checked all 30 source displays, the seven TikZ-CD bodies,
the five translated mathematical text strings, and the normalized multiset of
211 inline-math spans. Signs, shifts, degrees, matrix entries, map directions,
cone and cylinder definitions, homotopies, and chain-complex versions are
preserved. One long inline tuple was moved to an equivalent bracket display
to prevent an overfull line. A `\enlargethispage{2pt}` adjustment removes a
1.14674-point overfull first-page box without altering content, and two
awkward suffix constructions were rephrased as natural `... dari f`
definitions. Final deterministic rechecks preserve every marker, identifier,
formula, and environment. No Han residue, NUL, replacement character, stray
patch marker, duplicate marker, or malformed environment remains.

The official errata contains no item for this range, and no deterministic
source defect was found. No source correction was added.

## Indonesian terminology and provenance

The previously completed bounded Indonesian field-terminology check remains
the controlling external-language evidence. No suitable Indonesian
same-field arXiv TeX source was found, so the official nine-page Universitas
Diponegoro article “Fungtor Kontravarian dan Kategori Abelian” was used as the
documented fallback. Its identity and inspection are recorded in
`controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`, 10,335 bytes, SHA-256
`0c6e739d72941399bb388ef470fc36c2a36bcf3d9781848e46d4056caf5d36fd`.

The already established terms `kerucut pemetaan`, `silinder pemetaan`,
`kocitra`, and `morfisme homotopik nol` are retained. Unit 034 adds three
synchronized concepts: `kokernel homotopi`, `kernel homotopi`, and `kocitra
homotopi`. Both terminology surfaces contain 423 valid, unique, matching
concept IDs: control 67,477 bytes, SHA-256
`811ebc6201c4262418c2d34b939b9d2dd8493442359b4cc4094f365ef1f683c8`;
backend 28,447 bytes, SHA-256
`d77d374e6ce2e4d231fbea5b96424df5a8269cc9493a432d39eb91699db61d89`.

The edition provenance identifies the production model exactly as **OpenAI
Codex gpt-5.6-sol, Ultra**, without displacing Wen-Wei Li's authorship or any
source, witness-author, component, or human-contributor credit.

## Backend and cumulative source closure

The modular backend now has 34 sequential units and 1,769 unique segments.
`backend/units.jsonl` is 25,072 bytes, SHA-256
`5582d0d813195708e72975cd9820d1b5583a55caca6f8150f6455c97f85a952d`;
`backend/segments.jsonl` is 515,338 bytes, SHA-256
`f20625ae1228d95037a12f120384abeefd30a2505d7d9e3a93d53442c4e0a1eb`.
Unit 034 has status `translated_built_qa_passed`, and its backend target hash
equals the admitted target hash.

The cumulative wrapper through Unit 034 is 8,667 bytes, SHA-256
`5c7838c25c23943f5d6832588535fd1e73d38c0d89db3dd79a284b4ff0dc310f`.
It inputs Units 001--034 in exact source order and retains the exact model,
attribution, modification, license, and non-endorsement notices. The stable
cumulative wrapper is byte-identical. The bibliography snapshot remains 6,649
bytes, SHA-256
`a7ec7fa3df2ad91a8d13f8ed552e51e5c79ed64896e07dd68d4bd58b90ad2019`;
the stable bibliography is byte-identical.

## Reproducible build and PDF inspection

The admitted shell-escape-disabled build is
`build/cumulative-unit-034-finalC-20260824`. It used XeLaTeX, Biber 2.21, both
MakeIndex passes, three convergence XeLaTeX passes after bibliography and index
generation, and one final prose-only XeLaTeX pass. Biber resolved all 19
citekeys with no warning or error. MakeIndex accepted 160 term entries and 59
symbol entries with zero rejection or warning.

The final TeX log is 79,349 bytes, SHA-256
`4385fd0e3d80884dcbc157dbe512010d02b852ea0500235cec64d54c6ac13f97`.
It has no TeX or package error, undefined control sequence, unresolved
reference or citation, cross-reference/Biber rerun request, overfull box,
missing character, fatal error, or emergency stop. Twenty-one non-fatal
underfull warnings remain: 15 horizontal and 6 vertical. The log also retains
four non-fatal LaTeX kernel-release notices, one biblatex footnote-patching
warning, and two imakeidx advisories even though the indexes were regenerated
and all final passes completed.

The checkpoint and promoted cumulative reader are byte-identical: PDF 1.7,
209 pages, 1,056,839 bytes, SHA-256
`c49a6a7fd01659cc2fdaf7304b7a0576f48cfbb35c3106446bd21db78e509aac`.
The PDF has `id-ID` metadata, is unencrypted and untagged, and has 41 outline
entries, 907 named destinations, 698 internal GoTo links, and 12 URI links. It
has no form, JavaScript, embedded file, structure tree, or MarkInfo and is not
claimed to be fully accessible.

Physical pages 188--209 were rendered at 120 dpi. Both contact sheets and
full-size pages 194--202 were inspected. Section 3.3, definitions, proofs,
matrices, all diagrams, bibliography, symbol index, and term index are centered
and legible. Physical page 206 is an intentional recto/verso separator. No
clipping, overlap, broken diagram, black square, off-page content, or unreadable
glyph was visible. Contact-sheet SHA-256 values are
`ba9e5f73c4a6458635cc6e56f6e7f656a1c276770b1fe0ed1d7099949ce844d6`
and `d3afd055174598ab3b6a273ac7e9237370b0e96bc2e79f26e53e724a82e75866`.

## Admission decision

Unit 034 is admitted through `chapter3.tex` line 621. The next production
cursor is line 622, `sec:opposite-cplx`. This remains a partial working edition
and does not complete the full-corpus pursuit.
