# O014 Unit 032 admission and reader QA

Date: 2026-08-24  
Unit: `o014.aljabr2.chapter3.complexes-over-additive-categories`  
Title: *Kompleks pada Kategori Aditif*  
Result: **PASS — translated, independently reviewed, built, rendered, and admitted**

## Authority and exact scope

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled Gitee `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 032 is
exactly Section 3.1, `chapter3.tex` lines 57--162 inclusive. The next
unadmitted source is line 163,
`\section{复形之间的态射复形}\label{sec:Hom-cplx}`.

The normalized-LF authority slice is `tmp/unit032-source-slice.tex`, 8,995
bytes, SHA-256
`2f928e1ca88a032bec9c270d65604e25a38bd00ec62874562ae95a55be0ee8b5`.
It is byte-equal to the frozen authority range. The 33-record stable-ID map is
`tmp/unit032-segment-map.jsonl`, 10,336 bytes, SHA-256
`7100b28797cf67adb12b11dc400a54d980671957bd491a053ba16702fc3c2e1f`.

## Translation, topology, and mathematical review

The admitted target is `source/id-ID/chapter3-unit-032.tex`, 13,677 bytes,
SHA-256
`0ac6def5c534f07ceacfb80f29fff71b0174fffb944c0759fce1392510e3b500`.
It translates the complete section without abridgment. The source range has no
exercise, hint, answer, solution, citation, external figure, or external asset.

All 33 stable markers are unique and occur in exact map order. The Unit-032
backend has 33 rows in exact map parity. Source/target topology passes for all
9 labels, all 7 reference occurrences, 4 definitions, 1 lemma, 2 propositions,
2 proofs, 1 convention, 1 remark, 5 displayed-mathematics blocks, both TikZ-CD
diagrams, 2 lists with 6 items, 2 footnotes, and 11 index commands. Six
references are live; the later spectral-sequence reference retains a printed
source-section fallback through `sourcecrossref`.

All five displays and both TikZ-CD bodies preserve the source mathematics after
whitespace normalization. Review specifically checked the unsigned graded
shift `T`, the signed complex shift `[n]`, the typed DG-morphism identity
`(Tf)d_X=d_Yf`, the fact that `U` creates rather than merely preserves the
displayed limits, the degree of `S[-n]`, and the reversal between chain and
cochain shifts. No Han residue, NUL, replacement character, stray patch marker,
duplicate marker, or malformed environment remains. Independent naturalness
review required only the typed DG-morphism clarification and one cleaner proof
sentence; both are in the admitted target.

The official errata contains no item for this range, and no new deterministic
source defect was found. No source correction was added.

## Indonesian terminology and provenance

The bounded arXiv-first field-terminology check was repeated before admission.
No suitable Indonesian same-field arXiv TeX source was found, so the prescribed
fallback used the official nine-page Universitas Diponegoro journal article
“Fungtor Kontravarian dan Kategori Abelian.” Its PDF is 429,219 bytes,
SHA-256
`d22cf3c40242359a2d00eb726697e08b6ad29c647a0309cbcd98914484b5f9b6`;
all pages were rendered and inspected. The evidence and decisions are recorded
in `controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`, 10,335 bytes, SHA-256
`0c6e739d72941399bb388ef470fc36c2a36bcf3d9781848e46d4056caf5d36fd`.

The preferred prose remains `funktor`, `objek`, `morfisme`, and
`homomorfisme`; the witnessed older spellings are recognition variants only.
Unit 032 adds five synchronized concepts: `objek bergradasi`, `objek
diferensial bergradasi`, `objek bergradasi ganda`, `kategori kompleks`, and
`kompleks terkonsentrasi`. Both terminology surfaces contain 416 valid, unique,
matching concept IDs: control 65,903 bytes, SHA-256
`cf88447b578262f044d15ebaecd5b505b051599f90068e88099ca073c12ad777`;
backend 27,955 bytes, SHA-256
`f37a93c0ad714999de14697f31b549746f52fac116aa128b600e5e4e3bbcd96a`.

The edition provenance identifies the production model exactly as **OpenAI
Codex gpt-5.6-sol, Ultra**, without displacing Wen-Wei Li's authorship or any
source, witness-author, component, or human-contributor credit.

## Backend and cumulative source closure

The modular backend now has 32 sequential units and 1,633 unique segments.
`backend/units.jsonl` is 23,665 bytes, SHA-256
`0212ad5888b3153a14679d27a149b518e3a9396084643228d15a6b4b2c9365e0`;
`backend/segments.jsonl` is 477,156 bytes, SHA-256
`8906b0d5204e12187eb198e361b91358145aee5d464b9fafb69d23a3bf049406`.
Unit 032 has status `translated_built_qa_passed`, and its backend target hash
equals the admitted target hash.

The cumulative wrapper through Unit 032 is 8,615 bytes, SHA-256
`986c92fa9072265b48d37fe5a13ab6510b37ea0b5f72d91642723cd751c1924c`.
It inputs Units 001--032 in exact source order and retains the exact model,
attribution, modification, license, and non-endorsement notices. The stable
cumulative wrapper is byte-identical. The bibliography snapshot remains 6,649
bytes, SHA-256
`a7ec7fa3df2ad91a8d13f8ed552e51e5c79ed64896e07dd68d4bd58b90ad2019`;
the stable bibliography is byte-identical.

## Reproducible build and PDF inspection

The admitted shell-escape-disabled build is
`build/cumulative-unit-032-finalA-20260823`. It used XeLaTeX, Biber 2.21,
both MakeIndex passes, and three convergence XeLaTeX passes after bibliography
and index generation. A first Biber invocation from the build directory could
not resolve the relative bibliography path; the corrected invocation ran from
the source directory with explicit build input/output directories and produced
the clean final `.blg`. Biber resolved all 19 citekeys with no warning or
error. MakeIndex accepted 151 term entries and 51 symbol entries with zero
rejection or warning.

The final TeX log is 79,020 bytes, SHA-256
`c3edcb705ec3a48b37b3cfd7ab35381a6a27ca27814487859bc83ad86418bb21`.
It has no TeX or package error, undefined control sequence, unresolved
reference or citation, cross-reference/Biber rerun request, overfull box,
missing character, fatal error, or emergency stop. Nineteen non-fatal
underfull warnings remain: 13 horizontal and 6 vertical. The log also retains
four non-fatal LaTeX kernel-release notices, one biblatex footnote-patching
warning, and two imakeidx advisories even though the indexes were regenerated
and all final passes completed.

The checkpoint and promoted cumulative reader are byte-identical: PDF 1.7,
195 pages, 999,106 bytes, SHA-256
`f28977200909076af2a30ea82de30985a917a5e3d62cb2f2d478502b51314ef3`.
The PDF has `id-ID` metadata, is unencrypted and untagged, and has 39 outline
entries, 843 named destinations, 654 internal GoTo links, 12 HTTPS links, and
52 embedded font-resource programs. It has no form, widget, JavaScript,
embedded file, structure tree, or MarkInfo and is not claimed to be fully
accessible.

Physical pages 178--195 were rendered at 120 dpi. Both contact sheets and
full-size pages 185--188 were inspected. The Section 3.1 heading, definitions,
lists, footnotes, formulas, both TikZ-CD diagrams, bibliography, symbol index,
and term index are centered and legible. Blank physical pages 180 and 192 are
intentional recto/verso separators. No clipping, overlap, broken diagram,
black square, off-page content, or unreadable glyph was visible. Contact-sheet
SHA-256 values are
`313a8ee3105befa2db2e293c471d4492afbd063a460af8bd66b6ca36b3ef2f5d`
and
`82b5af7145897c8c97c14d0ee6a1142450efb9c5030ac7cd30833c704f0d6238`.

## Admission decision

Unit 032 is admitted through `chapter3.tex` line 162. The next production
cursor is line 163, `sec:Hom-cplx`. This remains a partial working edition and
does not complete the full-corpus pursuit.
