# Unit 041 QA - Kohomologi bikompleks

Date: 2026-08-25  
Course / role: O014 / D80  
Unit ID: `o014.aljabr2.chapter3.double-complex-cohomology`  
Status: admitted cumulative checkpoint; the complete-corpus pursuit remains active

## Authority, boundary, and source identity

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 041 is
the complete Section 3.10, `chapter3.tex` lines 1710--1881 inclusive, with
substantive content through line 1880 and the terminal blank separator at line
1881. It stops before `sec:resolutions` at line 1882.

The normalized-LF source witness `tmp/unit041-source-slice.tex` is 14,167
bytes / 172 LF lines, SHA-256
`fac229cb4d731ecac5486304c8f4f172d0f8522adede60034b5060616d04ccfa`.
It is byte-identical to the normalized authority slice. The 43-record stable
map `tmp/unit041-segment-map.jsonl` is 13,693 bytes, SHA-256
`ef38bad8dc30390e2b8057c17ee5d113e5f7b4c7eba3d08a6d111b08decd444b`.
Its 21 top-level and 22 nested records cover every nonblank authority line in
order; all parent relations and ranges validate.

## Translation, structure, and independent review

The final Indonesian target `source/id-ID/chapter3-unit-041.tex` is 20,059
bytes / 364 LF lines, SHA-256
`8ad7d65cc4681252b6ff4e71f8bd4e3cbdcbfca6416cd538f3fa75c31b1f1367`.
Independent structural and semantic reviews, followed by focused delta audits
of each reflow, pass. All 43 stable markers occur once and in exact map order.
The target preserves 33 balanced environment pairs, ten labels, twenty
`\ref` commands, four `\eqref` commands, the `KS06` citation, five symbol-index
writes, four list items, seven TikZ-CD diagrams, and 36 arrows. It contains no
active Han residue, omitted nonblank source line, unbalanced brace/environment,
external asset dependency, exercise, hint, answer, or solution.

Review explicitly checked every formula, sign, shift, horizontal/vertical
differential, alpha/beta index, truncation direction, total-complex map, and
quasi-isomorphism claim. The long cone-object definition was reflowed into
display math without changing its equality or category. The forward reference
to `eg:double-cplx-tot-ss` uses a partial-reader-safe fallback to Section 5.6;
the authority defines that example at `chapter5.tex` line 794 in Section 5.6.
On the final visual pass, long quasi-isomorphism labels were moved from two
crowded diagrams into their immediately adjacent prose. Arrow topology and all
mathematical information remain unchanged.

## Disclosed source corrections

The derivative records and discloses two localized source repairs:

- O014-C054 evaluates the two composite functors at the bikomplex `X`, because
  the left sides and following displays define objects `H_I^p(X)` and
  `H_II^q(X)`, not unapplied functors;
- O014-C055 names the right vertical morphism as `H_I^q(f)[-q]` and states
  that it is a quasi-isomorphism. The source's isomorphism symbol overstates
  the theorem hypothesis, which gives only a quasi-isomorphism of complexes.

Both corrections appear once in the target and once in
`controls/SOURCE_CORRECTIONS.csv`. C054 is at target lines 34--49; after the
final display reflow, C055 is accurately recorded at lines 298--307. The
ledger contains 56 unique rows, is 37,580 bytes, and has SHA-256
`6c7cacaa608c628b83fed8a4c371edc7c21312832a081af49e66164a584c18a3`.
No upstream contact occurs at this boundary.

## Terminology and modular backend

The controlled forms include `bikompleks`, `kohomologi bikompleks`,
`kompleks total`, `kuasi-isomorfisme`, `eksak pada baris`, `eksak pada kolom`,
and `bikompleks berhingga pada setiap diagonal`. Three Unit 041 concepts were
added. Both terminology surfaces contain 454 unique, exact-matching concept
IDs:

- `controls/TERMINOLOGY_O013_O014.csv`: 75,517 bytes, SHA-256
  `efca167060180bc6ef33227877c717e5e3d8919414ac8a47f8eacde859b7e5c3`;
- `backend/terms.csv`: 30,659 bytes, SHA-256
  `f0c036e9d359154f3b705af96b870f9cb0365ef27fc03282b5ecb4c0bb7a37f7`.

The backend contains 41 unique units and 2,120 unique segments. Its final 43
segment rows are line-identical to the frozen Unit 041 map:

- `backend/units.jsonl`: 30,851 bytes, SHA-256
  `ed0de373c9b193956d61dd08420a358a93d194742ba8c094e108dec5a3aafb37`;
- `backend/segments.jsonl`: 627,032 bytes, SHA-256
  `19038eddc540bb95fb6ba568aac04b8940110cbc2781e1c436afde5d47160d8e`.

The Unit 041 backend row records the exact source/target hashes and the honest
status `translated_built_qa_passed`.

## Editable closure and reproducible build

The 41-input frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-041.tex` is 8,875 bytes,
SHA-256
`d3176291b3f2162016a14686908fe1076263398565ef3ba13aaa99f449630e54`.
Its mutable alias is byte-identical. The 21-entry bibliography
`source/id-ID/references-cumulative-through-unit-041.bib` is 7,631 bytes,
SHA-256
`b882ae8225e57e383d85b4a5a8f69a0bddc688f20157365d8513b47f612ee597`;
its mutable alias is byte-identical. Cover, PDF subject, and attribution page
truthfully state coverage through Chapter 3 Section 3.10 and source line 1880.

The admitted clean build is
`build/cumulative-unit-041-finalD-20260825`. XeLaTeX (MiKTeX 26.5) ran with
shell escape disabled, followed by Biber 2.21, bounded MakeIndex passes for
both indexes, and three further XeLaTeX passes. Biber resolves all 21 citekeys
with zero warning/error. MakeIndex accepts 182 terminology entries and 93
symbol entries with zero rejection/warning.

The final 80,161-byte log has SHA-256
`08bc57c1c7f48755fa79d00da4d06ccba12c8e1355fdf7d39f5fd02df02c4f17`.
It contains zero TeX/package error, undefined control/reference/citation,
rerun request, overfull box, missing character, fatal error, or emergency
stop. Seventeen non-fatal underfull horizontal boxes and seven underfull
vertical boxes remain. The generic imakeidx advisories are informational; both
indexes are incorporated.

Resolved build artifacts include:

- BBL: 29,093 bytes, SHA-256
  `aedae96a05b2b62b7728ef815f287b2ef9eb4b6459a1901f08e5bad004543103`;
- term index: 7,954 bytes, SHA-256
  `090c12f3285e0937c8c2721e3658aeff3358119afd46dde8f0a10d63d20544da`;
- symbol index: 3,562 bytes, SHA-256
  `32cfe879a5aaa893a4b9da15d5e54cf0255ba9da54369225786f3ea0fb75d02e`.

## PDF structure, accessibility qualification, and visual QA

The build PDF, frozen checkpoint, and promoted cumulative reader are
byte-identical: PDF 1.7, 253 pages, 1,255,777 bytes, SHA-256
`f364d2c3b6839a14b89f77313f9e3117dc9b7b5e5ad920d27637924513d5a29f`.
It is `id-ID`, unencrypted, and untagged. Every page has zero rotation and the
same 498.9 by 708.66-point geometry. Strict parsing finds 48 outline entries,
1,097 named destinations, 858 internal actions whose destinations all
resolve, and fourteen URI actions. All 872 link annotations parse; none is
malformed.

There is no AcroForm, widget, JavaScript, embedded file, additional action,
structure tree, or `MarkInfo`; the opening action is the ordinary first-page
`/Fit` view. All 52 Poppler font rows are embedded and subsetted; forty have
ToUnicode maps and twelve mathematical fonts do not. The PDF is therefore a
searchable, navigable, visually verified reader, not a tagged or fully semantic
accessibility artifact. Poppler reports its local missing `Adobe-GB1` mapping
pack while inventorying inherited mappings; strict parsing and fresh rendering
succeed, so this remains a tool-environment limitation rather than a missing
reader resource.

Fresh renders cover physical pages 1--5, all Unit 041 pages 238--243, and all
backmatter pages 244--253. Full-size inspection covers every new diagram, the
reflowed cone object, both correction notes, the final corollary, bibliography,
and indexes. Text blocks, displays, rules, theorem heads, footnotes, and
diagrams are centered, legible, and free of clipping, collision, truncation,
detached punctuation, black boxes, or missing visible glyphs. The crowded
labels found in the first admitted-candidate render are absent from finalD.
Physical page 244 is the intentional blank inserted before backmatter. Contact
sheets:

- `tmp/pdfs/unit041-finalD/contact-front.png`: 159,191 bytes, SHA-256
  `cb118e6f525bccef15ea7ab78bce588e6e9b009d1add588e496cc9e429bf4df8`;
- `tmp/pdfs/unit041-finalD/contact-unit041.png`: 579,240 bytes, SHA-256
  `459306f6190518f5d0f09055d5478b9e08caab24d8c7ee04959cfa6b3f02cd91`;
- `tmp/pdfs/unit041-finalD/contact-tail.png`: 373,586 bytes, SHA-256
  `9551974f0699de7d27a3d4acd6729b496231c49dba75d8adae97f1016eeffb0e`.

## Admission decision and next cursor

Admit Unit 041 and the cumulative reader through Chapter 3 Section 3.10. The
exact 78-row admission manifest
`qa/CUMULATIVE_UNIT_041_FILE_MANIFEST.csv` re-verifies with zero missing,
duplicate, byte-count, or hash mismatch. The
next exact source-order boundary is Unit 042,
`o014.aljabr2.chapter3.resolutions`, *Resolusi*, the complete
`sec:resolutions`, `chapter3.tex` lines 1882--2214 inclusive, stopping before
`sec:derived-primer` at line 2215. Its proposed normalized-LF source slice is
27,644 bytes / 333 LF lines, SHA-256
`75da0a5963f8e3bf2cec5fbe6a4007fea1c1b27faca6bd54528ac8957547ebfa`;
freeze and map it independently before translation.

As throughout this lane, the author's official 650-page Linux/TeX Live/xindy
PDF remains authoritative. This 253-page Windows/MiKTeX/MakeIndex artifact is
a valid partial Indonesian reader and makes no pagination-identity claim. This
checkpoint does not complete the full corpus goal.
