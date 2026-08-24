# O014 Unit 033 admission and reader QA

Date: 2026-08-24  
Unit: `o014.aljabr2.chapter3.hom-complex-and-homotopy`  
Title: *Kompleks Hom dan Homotopi*  
Result: **PASS — translated, independently reviewed, built, rendered, and admitted**

## Authority and exact scope

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled Gitee `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 033 is
exactly Section 3.2, `chapter3.tex` lines 163--345 inclusive. The next
unadmitted source is line 346,
`\section{映射锥}\label{sec:mapping-cone}`.

The normalized-LF authority slice is `tmp/unit033-source-slice.tex`, 12,347
bytes, SHA-256
`30e6afb74eae4ea7aa78d610a2806c713faa3d0e7f893e16f0565a0ce379e59c`.
It is byte-equal to the frozen authority range. The 56-record stable-ID map is
`tmp/unit033-segment-map.jsonl`, 16,810 bytes, SHA-256
`0798cc52a5cf5e9c49c9132039d58e74f95e7d653348d6e4367708214a2d11c2`.

## Translation, topology, and mathematical review

The admitted target is `source/id-ID/chapter3-unit-033.tex`, 18,841 bytes,
SHA-256
`deb48c356cc78ad8fc5f4d730be640d5a60fde0c3b90d7a45c21330bcbd337d2`.
It translates the complete section without abridgment. The source range has no
exercise, hint, answer, solution, citation, external figure, or external asset.

All 56 stable markers are unique and occur in exact map order. The Unit-033
backend has 56 rows in exact map parity. Source/target topology passes for all
15 labels, all 20 reference occurrences, four definitions (including the
definition--proposition), four lemmas, two propositions, six proofs, one
remark, the two-item list, all 8 index commands, and all four TikZ-CD diagrams
with their 12 arrows. All environments and braces balance. The source's 22
block displays and one inline TikZ diagram are preserved; three long inline
formulas were moved to bracket displays solely to prevent overfull lines in the
Indonesian reader. Their mathematics is unchanged.

Independent review rechecked every formula, sign, degree, mapping direction,
diagram label, and naturality component after the final reflow. No Han residue,
NUL, replacement character, stray patch marker, duplicate marker, malformed
environment, mathematical mismatch, or residual language defect remains.

Three deterministic source defects are corrected and disclosed in translator
notes and `controls/SOURCE_CORRECTIONS.csv`:

- `O014-C033`: the upper horizontal diagram label is typed as
  `\Hom^n(u,v)`, matching the source and target degrees.
- `O014-C034`: the previously unbound homotopy variable is explicitly typed as
  `h\in\Hom^{n-1}(X,Y)`, equivalently `\Hom^{-1}(X,Y[n])`.
- `O014-C035`: the adjunction isomorphism is applied degreewise as
  `\varphi_{X^k,Y^{k+r}}(f^k)`.

The source spelling `eqn:homotopy-cat-cmposition` remains unchanged because it
is a functional identifier. A reused source summation index is made
type-explicit in prose but is not recorded as a formal correction.

## Indonesian terminology and provenance

The bounded arXiv-first field-terminology check was completed before this unit
was scaled. No suitable Indonesian same-field arXiv TeX source existed in the
bounded official searches, so the prescribed fallback used the official
nine-page Universitas Diponegoro article “Fungtor Kontravarian dan Kategori
Abelian.” Its PDF is 429,219 bytes, SHA-256
`d22cf3c40242359a2d00eb726697e08b6ad29c647a0309cbcd98914484b5f9b6`;
all pages were rendered and inspected. The evidence and decisions are recorded
in `controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`, 10,335 bytes, SHA-256
`0c6e739d72941399bb388ef470fc36c2a36bcf3d9781848e46d4056caf5d36fd`.

The preferred forms remain `funktor`, `objek`, `morfisme`, and
`homomorfisme`; witnessed older spellings are recognition variants only. Unit
033 adds four synchronized concepts: `aturan Leibniz`, `morfisme homotopik`,
`morfisme homotopik nol`, and `kategori homotopi`. Both terminology surfaces
contain 420 valid, unique, matching concept IDs: control 66,830 bytes, SHA-256
`1c8f524b524790d4eaf5228a53163e7ca59308e78ae3088080c019e3067e4612`;
backend 28,240 bytes, SHA-256
`da6059ea5e6e7c49a549e0d57c45c220b7d1e13d5230104728237f835f8bc52a`.

The edition provenance identifies the production model exactly as **OpenAI
Codex gpt-5.6-sol, Ultra**, without displacing Wen-Wei Li's authorship or any
source, witness-author, component, or human-contributor credit.

## Backend and cumulative source closure

The modular backend now has 33 sequential units and 1,689 unique segments.
`backend/units.jsonl` is 24,379 bytes, SHA-256
`46ab1bb22f4738b7609de4c659a6dbd463bcbe6d5bc24e54f8344b8f77984d62`;
`backend/segments.jsonl` is 493,965 bytes, SHA-256
`01ab5504c591b89b034f65ebfb64c5cf29559bf2a0b54fcfe267225933dc26d0`.
Unit 033 has status `translated_built_qa_passed`, and its backend target hash
equals the admitted target hash.

The cumulative wrapper through Unit 033 is 8,641 bytes, SHA-256
`30b1d26eb64bfc05989fa7b1715feab759c1205c4e9fcf705ded0f0cc240f3a3`.
It inputs Units 001--033 in exact source order and retains the exact model,
attribution, modification, license, and non-endorsement notices. The stable
cumulative wrapper is byte-identical. The bibliography snapshot remains 6,649
bytes, SHA-256
`a7ec7fa3df2ad91a8d13f8ed552e51e5c79ed64896e07dd68d4bd58b90ad2019`;
the stable bibliography is byte-identical.

## Reproducible build and PDF inspection

The admitted shell-escape-disabled build is
`build/cumulative-unit-033-finalC-20260824`. It used XeLaTeX, Biber 2.21, both
MakeIndex passes, three convergence XeLaTeX passes after bibliography and index
generation, and one final punctuation-only XeLaTeX pass. Biber resolved all 19
citekeys with no warning or error. MakeIndex accepted 155 term entries and 55
symbol entries with zero rejection or warning.

The final TeX log is 79,160 bytes, SHA-256
`a9f4627dcaee573db4dd4454a196e33c1e3ef91f5616ba9fbdbd5f558abc49d5`.
It has no TeX or package error, undefined control sequence, unresolved
reference or citation, cross-reference/Biber rerun request, overfull box,
missing character, fatal error, or emergency stop. Twenty non-fatal underfull
warnings remain: 14 horizontal and 6 vertical. The log also retains four
non-fatal LaTeX kernel-release notices, one biblatex footnote-patching warning,
and two imakeidx advisories even though the indexes were regenerated and all
final passes completed.

The checkpoint and promoted cumulative reader are byte-identical: PDF 1.7,
201 pages, 1,023,423 bytes, SHA-256
`b621a25b3fe7032885680eea75fae0096cab5bafd95818cd1cf88fad9e6e40a3`.
The PDF has `id-ID` metadata, is unencrypted and untagged, and has 40 outline
entries, 875 named destinations, 680 internal GoTo links, and 12 URI links. It
has no form, JavaScript, embedded file, structure tree, or MarkInfo and is not
claimed to be fully accessible.

Physical pages 181--201 were rendered at 120 dpi. Both contact sheets and
full-size pages 188--194 were inspected. Section 3.2, definitions, proofs,
footnotes, formulas, four TikZ-CD diagrams, bibliography, symbol index, and term
index are centered and legible. Physical page 198 is an intentional blank
recto/verso separator. No clipping, overlap, broken diagram, black square,
off-page content, or unreadable glyph was visible. Contact-sheet SHA-256 values
are `fd1822137f705341947eb45f87ec19225cc77c6a212f32854526ef30ffbf2bcf`
and `d440de3e86c8c024f76ae068190ff2adbf2171b0e6b45130e3072c4d841602e5`.

## Admission decision

Unit 033 is admitted through `chapter3.tex` line 345. The next production
cursor is line 346, `sec:mapping-cone`. This remains a partial working edition
and does not complete the full-corpus pursuit.
