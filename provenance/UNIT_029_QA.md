# O014 Unit 029 admission and reader QA

Date: 2026-08-23  
Unit: `o014.aljabr2.chapter2.serre-subcategories-and-k0-groups`  
Title: *Subkategori Serre dan Grup K0*  
Result: **PASS — translated, structurally audited, built, rendered, and admitted**

## Authority and exact scope

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled Gitee `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 029 is
exactly `chapter2.tex` lines 1564--1754 inclusive. The next unadmitted heading
is line 1756, label `sec:Grothendieck-cat`.

The normalized-LF authority slice is `tmp/unit029-source-slice.tex`, 17,301
bytes, SHA-256
`45f958e6627cb4cef919dbd1fd5bc478b68c5d6c706dac47b69dd4d6dbd40aba`.
The 61-record stable-ID map is `tmp/unit029-segment-map.jsonl`, 19,962 bytes,
SHA-256
`ec804f816cde5005f626110f65bf4dd7db928c6fc2ab040cfc36ad809f7ae4e2`.

## Translation, topology, and mathematical review

The admitted target is `source/id-ID/chapter2-unit-029.tex`, 25,425 bytes and
506 lines, SHA-256
`6cfc81b8d1dc52ed685971c9dd4d81471e8978b58d8c682be60a5ef1f97d2b81`.
Two independent bounded reviews found no remaining actionable translation or
mathematical defect.

All 61 stable markers are unique and occur in exact map order. The Unit-029
backend has 61 rows in byte-exact map parity. Source/target parity passed for
11 labels, 20 conventional or frozen-source references, one citation group,
three `eqref` commands, eight index commands, 30 begin/end environments, ten
display blocks, two `tikzcd` environments, three `gather*` environments, and
two `equation` environments. Braces and math delimiters are balanced. No Han
residue, NUL, replacement character, stray patch marker, duplicate marker, or
bare command line remains. The source range contains no exercises or hints.

Two source defects are corrected transparently and registered in
`controls/SOURCE_CORRECTIONS.csv`:

- O014-C028 changes the source's inconsistent `K_0(f)` to `K_0(F)`, because
  `F` is the exact functor inducing `[X] -> [FX]`.
- O014-C029 replaces a non-well-defined restriction in the fullness proof by
  the canonical fiber product
  `M_0 = M_1 x_{M_2[S^{-1}]} M_2` and its projections. Its kernel and cokernel
  over `M_1` are S-torsion, so the resulting roof represents the required
  localized morphism.

Both repairs have translator footnotes at the point of use. The corrections
ledger has 30 valid, uniquely identified records; O014-C028 and O014-C029 are
`accepted_disclosed`.

## Indonesian terminology gate

The required external field-usage check was already completed at the Unit-024
boundary and remains applicable here. A bounded search of official arXiv
records found no admissible Indonesian same-field item with downloadable TeX.
The documented fallback directly inspected two official ITB mathematical
documents: Gustina Elfiyanti's 2020 category/homological-algebra dissertation
front matter and Ryan Kasyfil Aziz's 2012 algebra/modules/categories chapter.
The exact sources, hashes, page-by-page inspection, attested variants, rights
restrictions, and decisions are recorded in
`controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`, 7,965 bytes, SHA-256
`8f112facd6d58c728d9e18d7b34a050064b62a8b0a2c2645d49682d4dbe98cd1`.
The restricted witnesses remain local and are excluded from release payloads.

The evidence supported existing forms such as `barisan eksak`, `funktor`,
`morfisme`, and `kuosien`, while preserving attested variants rather than
forcing mathematically misleading substitutions. Unit 029 adds synchronized
entries `subkategori Serre lemah`, `kerangka kecil`, and `modul torsi-S`.
Both terminology surfaces contain 385 valid unique records: control SHA-256
`9ff8508a6754dc57667835686cd93f192271e38b28c6c457870826f2c2048eb3`;
backend SHA-256
`b46b8f431952d9b9a7f73e9f60d0143611e1bfd34b2deb9d3f9b8d82d8554c1f`.

The edition and repository provenance note identifies the production model
exactly as **OpenAI Codex gpt-5.6-sol, Ultra**, without displacing Wen-Wei Li's
authorship or any human/source/component credits.

## Backend and bibliography closure

The modular backend now has 29 sequential units and 1,448 unique segments.
`backend/units.jsonl` is 21,549 bytes, SHA-256
`1f2234f737ed8dcca5e35e01d23472cf5fd13709741ff1ccdb654617fad6382d`;
`backend/segments.jsonl` is 420,125 bytes, SHA-256
`2567cf14ca54017d462fb8dc015a4545fda3d071242dd280843c91522c35a01f`.
The Unit-029 backend target hash equals the admitted target hash and its status
is `translated_built_qa_passed`.

The initial build correctly exposed that the earlier cumulative bibliography
snapshot did not yet contain Unit 029's `Lai19` citation. Older snapshots were
left untouched. `references-cumulative-through-unit-029.bib` adds the exact
source record in readable Hanyu Pinyin display form while retaining the
source-script identity in a non-rendered comment. It is 6,649 bytes, SHA-256
`a7ec7fa3df2ad91a8d13f8ed552e51e5c79ed64896e07dd68d4bd58b90ad2019`.
The stable cumulative bibliography is byte-identical. The final Biber run
resolved all 19 citekeys with no warning or error.

## Reproducible build and PDF inspection

The admitted clean build is
`build/cumulative-unit-029-finalB-20260823`. It used shell-escape-disabled
XeLaTeX, Biber 2.21, MakeIndex for both indexes, and three final XeLaTeX
passes. MakeIndex accepted 139 term entries and 47 symbol entries with zero
rejections or warnings. The final TeX log is 78,488 bytes, SHA-256
`f5a36e23b4624bbc3da5542208d0c0bf474c983d0d7b148b5f00bd572abd9ea9`;
the Biber log is 1,769 bytes, SHA-256
`9eb0d8bb428ced702513b82d4fe0bd9467dee9bd419f3cf56b1c38b0f499758f`.

The final log has no TeX error, undefined control sequence, unresolved
reference or citation, rerun request, overfull box, missing character, fatal
error, or emergency stop. Seventeen non-fatal underfull-box warnings remain.

The checkpoint and promoted cumulative reader are byte-identical: PDF 1.7,
175 pages, 902,840 bytes, SHA-256
`bfda39c9f834643f024dd2c7d9c16e341c8736b40f3bfa6dcc9d1646b6d6bd25`.
The PDF is unencrypted, has `id-ID` metadata, 35 outline entries, 51 embedded
or subset font names, 591 link annotations including 12 URI links, no form
widgets, and no JavaScript. It is untagged and is not claimed to be fully
accessible.

Physical pages 160--175 were rendered at 120 dpi. Sixteen page images and two
contact sheets were inspected, including the section opening, definitions,
proofs, displayed equations, both correction footnotes, bibliography entry
`Lai19`, and both indexes. No clipping, overlap, broken diagram, black square,
or unreadable glyph was visible. Poppler emitted non-fatal Adobe-GB1/F41 text
mapping diagnostics during rendering; XeLaTeX reported no missing character,
and the rendered pages were visually intact. Contact-sheet SHA-256 values are
`64da8b5b31802438965de25c5b8a4b52caece4f3eded66b6ccab55cc72613996`
and `eb0ef7b98c4169ef4425d43acbac6b80c40fd282e2400a15d03636edfc47661e`.

## Admission decision

Unit 029 is admitted through `chapter2.tex` line 1754. The next production
cursor is line 1756, `sec:Grothendieck-cat`. This boundary is a partial public
checkpoint and does not complete the full-corpus pursuit.
