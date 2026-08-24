# O014 Unit 036 admission and reader QA

Date: 2026-08-24  
Status: admitted local source-order checkpoint; the complete corpus, mastery
layer, semantic reader, and final release set remain in production.

## Authority and exact scope

- Work: Wen-Wei Li, *Methods of Algebra, Volume 2: Linear Algebra*.
- Authority: author-controlled Gitee `master` commit
  `9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
  `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.
- Unit: `o014.aljabr2.chapter3.double-complexes`, *Bikompleks*.
- Exact authority boundary: `chapter3.tex` lines 700--945, including the blank
  separator at line 945 and stopping before `sec:Abel-cplx` at line 946.
- Frozen normalized-LF slice: `tmp/unit036-source-slice.tex`, 20,674 bytes,
  SHA-256
  `0d532ff079384d4437ed82abf21c828fe392f79f48db27f57a5af62069ed1c8c`.
- Ordered stable map: `tmp/unit036-segment-map.jsonl`, 76 records, 20,892
  bytes, SHA-256
  `f2a147d9be45c91a2ccd292e843b830237636743b43616eb1437453479edcada`.
- Target: `source/id-ID/chapter3-unit-036.tex`, 28,124 bytes, SHA-256
  `d36274b3f84495b1a28608b9f95f7e2d173afe73e84b38f408b265819c9bcc3f`.

The complete section has 13 labels, 12 source reference tokens over eleven
unique targets, citation `Li1`, one source-reference comment, 30 top-level
source displays, ten TikZ-CD diagrams, three lists with six items, 14 index
commands, four definitions, four propositions, four proofs, one remark, one
convention, one definition--proposition, one example, and one informal reader
prompt. It has no formal exercise, hint, solution, or external asset.

## Translation, topology, and mathematical review

The target preserves all 76 stable markers in exact map order, all 13 labels,
all 12 semantic reference relationships, citation, 14 indexes, ten diagrams,
six items, environments, arrows, formulas, signs, and degrees. The forward
reference to `def:Cf-Supp` uses the established `sourcecrossref` fallback so
the partial reader is warning-free while preserving the source target. All 37
environment starts and ends and all braces are balanced. No Han-script prose,
replacement character, or malformed encoding remains.

An independent final audit found no defect. It verified that the map covers
all 209 nonblank source lines, that eight diagrams are structurally identical
and the remaining two differ only in translated text labels, and that the
core macro counts match (`dhori` 39, `dvert` 40, totalization macros 64, and
diagram arrows 51).

Two deterministic source corrections are recorded and disclosed at point of
use:

- O014-C038 restores omitted `F` arguments in the definition and shifted
  isomorphisms for `C_oplus F`, `C_Pi F`, `K_oplus F`, and `K_Pi F`. Without
  `F`, the printed final terms are undefined and break the parallel typing.
- O014-C039 reconciles the source's named strict inverse `sigma^{-1}` with its
  copied coefficient `(-1)^(q+1)`. The true inverse has vertical coefficient
  `(-1)^q`; the target then supplies the canonical coordinate isomorphism
  multiplying bidegree `(p,q)` by `(-1)^q`, which changes only the vertical
  sign and yields the standard Hom-complex differential.

The corrections ledger has 40 unique rows through O014-C039. No upstream
contact occurred. One presentation-only change moves a long Hom-totalization
isomorphism out of prose into a display; this removes the only overfull line
without changing mathematics.

## Indonesian field-terminology QA and provenance

The requested arXiv-first terminology check was repeated at this boundary.
Exact searches for representative Indonesian category/homological-algebra
phrases produced no same-field Indonesian record with a downloadable TeX
source package. The bounded negative result and exact search terms are recorded
in `controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`; it is not generalized into a
claim that no such item exists.

The permitted fallback directly inspected relevant pages from four official
Indonesian institutional PDFs: the ITB U-complex abstract, the UNDIP paper on
contravariant functors and Abelian categories, the UNY/UNDIP paper on tensor
products, and UGM's category-theory course description. They attest field
forms including `fungtor`, `transformasi natural`, `hasil kali tensor`,
`aljabar homologi`, `rantai kompleks`, `kategori homotopi`, and `kategori
aditif`. They do not attest an Indonesian compound for bicomplex, Hom
bicomplex, or the Koszul sign rule.

The evidence refines glossary variants and notes but does not justify a
corpus-wide replacement. Coordinated preferred forms `funktor`, `transformasi
alami`, `hasil kali tensor`, `pelengkapan`, and `aljabar homologis` remain;
the transparent Unit 036 forms `bikompleks`, `bikompleks Hom`, `aturan tanda
Koszul`, and `homotopi bikompleks` remain provisional where direct field
attestation is absent. No Unit 001--036 prose requires propagation.

The terminology report is 14,089 bytes, SHA-256
`0d3cc71e0e7eb1a837de69cbc4e570575df8efd63090927495899ed78e19b3fc`.
The control and backend stores contain the same 427 concept IDs and preferred
forms:

- `controls/TERMINOLOGY_O013_O014.csv`: 69,146 bytes, SHA-256
  `c148e22d102db93b359ef7d4d7341dc5953cf0747fc34af4e587e3c60ca7e4f4`.
- `backend/terms.csv`: 28,724 bytes, SHA-256
  `fd71fe300455b1a24b2a2a059fb1ad39c0771245cd8c97af9284e16faabe3bd4`.

The witness PDFs are local terminology evidence only and are excluded from
public payloads because redistribution rights were not established. Edition,
reader, and release metadata retain the exact production identification
`OpenAI Codex gpt-5.6-sol, Ultra`, all source and witness-author credits,
CC BY 4.0 attribution/change notice, and non-endorsement.

## Backend and cumulative source closure

- `backend/units.jsonl`: 36 unique IDs and sequences, 26,483 bytes, SHA-256
  `9ed6ad3dcfe91aebff97cd5e427fdbb9f511de760e0741515ecebb4cf619053c`.
- `backend/segments.jsonl`: 1,869 unique IDs, including the exact 76 Unit 036
  IDs and sequences, 543,445 bytes, SHA-256
  `dfdcfc54ac38ec99399c2406f5e96b75e17e802522114a06851209f8c1a31778`.
- Snapshot and stable wrappers are byte-identical: 8,719 bytes, SHA-256
  `9a0e61ae42f3fb7e2a0d081b60e82f3a00e504eea85a7f1cdaa7a93af9ca1f75`,
  with 36 exact ordered inputs and truthful coverage through Section 3.5.
- Snapshot and stable bibliographies are byte-identical: 6,649 bytes,
  SHA-256
  `a7ec7fa3df2ad91a8d13f8ed552e51e5c79ed64896e07dd68d4bd58b90ad2019`.

## Reproducible build and PDF inspection

The admitted shell-escape-disabled build is
`build/cumulative-unit-036-finalB-20260824`. It used XeLaTeX (MiKTeX 26.5),
Biber 2.21, both MakeIndex passes, and four XeLaTeX passes. Biber resolves all
19 citekeys with no warning or error. MakeIndex accepts 165 term entries and
70 symbol entries with zero rejection or warning.

The final 79,529-byte log has SHA-256
`b4b884d331045167ca903e11b920f776ddfaecc617c91c1ae2086bfb64dfdddb`
and zero TeX/package error, undefined reference or citation, rerun request,
overfull box, missing character, fatal error, or emergency stop. It contains
15 non-fatal underfull horizontal boxes, seven underfull vertical boxes, four
inherited LaTeX release-availability notices, one known biblatex
footnote-patching warning, and two expected shell-escape-disabled imakeidx
advisories.

The checkpoint and promoted cumulative PDF are byte-identical: PDF 1.7, 219
pages, 1,107,313 bytes, SHA-256
`a720761eeab43f504f22af1214259c3481e377f5de3ecd3287b7aee9e71c8d2b`.
It is `id-ID`, unencrypted, and untagged. It has 43 outline entries, 950 named
destinations, 724 internal GoTo links, and 12 URI links, with no form,
JavaScript, embedded file, structure tree, or MarkInfo. All 52 fonts are
embedded; 11 mathematical fonts lack ToUnicode maps. Therefore this PDF is not
claimed to be an accessible semantic reader.

Physical pages 198--219 were rendered at 120 dpi. Both contact sheets and
full-size pages 205, 206, and 209--212 were inspected locally; an independent
audit inspected pages 205--212. Section 3.5, all diagrams, the reflowed Hom
display, translator notes, bibliography, and indexes are centered, legible,
unclipped, and free of overlap or truncation. Physical page 216 is an
intentional separator. Contact-sheet hashes:

- `contact-198-208.png`: 1,128,369 bytes, SHA-256
  `d81e894ee100b2e20c81556b089de5d3ffde7a51ab404010e8cf4fa042a9bb8b`.
- `contact-209-219.png`: 947,435 bytes, SHA-256
  `d5b010de06d28180b0babcd74749cf6abc5c6aa044f87cb577442df21283c4e1`.

Static evidence `tmp/unit036-qa.txt` is 4,510 bytes, SHA-256
`f5495558902d1bb1efa6c3349d84e8c75b94548e057790beb644e7b5780e6500`.

## Admission decision

Admit Unit 036 and the cumulative reader through Section 3.5. The next exact
source cursor is Unit 037, `o014.aljabr2.chapter3.abelian-category-complexes`,
`chapter3.tex` lines 946--1060, stopping before `sec:cone-vs-long-exact-sequence`
at line 1061. Its frozen normalized-LF slice is 8,933 bytes, SHA-256
`6adf88af700b26dac31c81724d991fbefcedab64f6ccd08849e532a75e04410e`;
its 30-record map is 9,537 bytes, SHA-256
`e08be8d6d9372550bcfa2680c6f3d1b02fbaa4f9886d35ff7b293fc82aaa30c2`.
This admission is a worthwhile partial checkpoint, not completion of the
pursuit.
