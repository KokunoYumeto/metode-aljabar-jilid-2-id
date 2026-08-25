# Unit 040 QA - Funktor pemenggalan

Date: 2026-08-25  
Course / role: O014 / D80  
Unit ID: `o014.aljabr2.chapter3.truncation-functors`  
Status: admitted cumulative checkpoint; the complete-corpus pursuit remains active

## Authority, boundary, and source identity

The authority remains Wen-Wei Li, *Methods of Algebra, Volume 2: Linear
Algebra*, author-controlled `master` commit
`9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
`23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, licensed CC BY 4.0. Unit 040 is
the complete Section 3.9, `chapter3.tex` lines 1587--1709 inclusive, with
substantive content through line 1708 and the terminal blank separator at line
1709. It stops before `sec:double-cplx-coh` at line 1710.

The normalized-LF source witness `tmp/unit040-source-slice.tex` is 10,217
bytes, SHA-256
`7954b37ef2279d82e9ce3d8e56f6ce218ccd839970a684189b6315a3f67a48be`.
The 33-record stable map `tmp/unit040-segment-map.jsonl` is 9,187 bytes,
SHA-256
`d2488a8f085baec85fbfc199198db009f9b85f0da996533ec12dde64dd2e62a2`.
All source lines through the last substantive line are covered in order.

## Translation, structure, and independent review

The final Indonesian target `source/id-ID/chapter3-unit-040.tex` is 14,865
bytes / 268 LF lines, SHA-256
`073c9ddbc20430ecb37ee80658f73f5b20756919ec38ffe7807c77130291c9b0`.
Two independent read-only reviews and a final delta audit pass. All 33 stable
markers occur once and in exact map order. The target preserves nine labels,
six cross-references, 22 balanced environment pairs, all source formulas and
sign/index directions, both TikZ-CD diagrams with 58 arrow commands, and all
eight index writes. It contains no active Han residue, omitted segment, citation,
item, asset dependency, or unbalanced brace/environment.

The source has nine mathematical display blocks. The target adds one
semantics-neutral display delimiter around the long `sigma` object-category
identity to prevent overflow; the identity itself is unchanged. The boundedness
table locally uses `\small` and three-point column separation. Exact render
inspection confirms that both presentation changes improve fit without
clipping or changing mathematical content.

The reviews verified the bounded-above/bounded-below directions, shift by
`[a-n,b-n]`, all four truncation complexes, the five short exact sequences,
the `[-n]` and `[-n-1]` shifts, duality under `n` to `-n`, both adjunction
directions, both truncated homotopy formulas, and the double-truncation
identities. Indonesian terminology and prose pass after replacing an ambiguous
adjunction calque, spelling `dualitas` correctly, and writing the two homotopy
compositions in explicit order.

## Disclosed source corrections

The derivative records and discloses four localized source repairs:

- O014-C050 adds the missing Abelian-category hypothesis to the assertion that
  the bounded complex subcategories are Abelian;
- O014-C051 names the two vertical comparison maps that actually induce the
  displayed cohomology isomorphisms, rather than the different-cutoff transition
  maps in the immediately preceding paragraph;
- O014-C052 types the degree-`n` component as
  `Coim(d^{n-1})` canonically isomorphic to `Image(d^{n-1})` before inclusion
  into `Ker(d^n)`;
- O014-C053 changes `X in Obj(A)` to `X in Obj(C(A))` in the iterated-truncation
  proposition.

`controls/SOURCE_CORRECTIONS.csv` now has 54 unique correction rows, is 36,165
bytes, and has SHA-256
`34108f8a41b02859012ba6cb222542db85ce4cd6a2407d61c5435bc698c5e3c0`.
Each of C050--C053 appears once in the target and once in the ledger. No
upstream contact occurs at this boundary.

## Terminology and modular backend

The controlled forms include `funktor pemenggalan`, `kompleks terbatas`,
`kompleks terbatas bawah`, `kompleks terbatas atas`, `kategori homotopi`,
`adjungsi`, `unit`, `kounit`, `kernel`, `kokernel`, `citra`, and `kocitra`.
Three bounded-complex concepts are added. Both terminology surfaces contain
451 unique, exact-matching concept IDs:

- `controls/TERMINOLOGY_O013_O014.csv`: 74,766 bytes, SHA-256
  `543615287d2d06a01dae41119ebb7267c7fa01e1c6ce51c66bf1fe13fd018adb`;
- `backend/terms.csv`: 30,385 bytes, SHA-256
  `78ec6bfe4b277df464f88bba208195ed503f9106ea72c54625214314fb28b36e`.

The backend contains 40 unique units and 2,077 unique segments. Its final 33
segment rows are line-identical to the frozen Unit 040 map:

- `backend/units.jsonl`: 30,107 bytes, SHA-256
  `7c3534c6955fa74aff5adb0adfc57a5c554dc5f3f57f642debf92d38f2acc139`;
- `backend/segments.jsonl`: 613,339 bytes, SHA-256
  `62cd5765fadc9c534753a010b542b9139b99fbffaf9bb92d347b4601eb860dd9`.

## Editable closure and reproducible build

The 40-input frozen wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-040.tex` is 8,824 bytes,
SHA-256
`c0039cb6018e040ea34b94ef8c4ea9c21cebc5ff478e5bc2fd57b9ab2a9b29cf`.
Its mutable alias is byte-identical. The 21-entry bibliography
`source/id-ID/references-cumulative-through-unit-040.bib` is 7,631 bytes,
SHA-256
`b882ae8225e57e383d85b4a5a8f69a0bddc688f20157365d8513b47f612ee597`;
its mutable alias is byte-identical. Cover, PDF subject, and attribution page
truthfully state coverage through Chapter 3 Section 3.9 and source line 1708.

The admitted clean build is
`build/cumulative-unit-040-finalD-20260825`. XeLaTeX (MiKTeX 26.5) ran with
shell escape disabled, followed by Biber 2.21, bounded MakeIndex passes for
both indexes, and three further XeLaTeX passes. Biber resolves all 21 citekeys
with zero warning/error. MakeIndex accepts 182 terminology entries and 88
symbol entries with zero rejection/warning.

The final 84,754-byte log has SHA-256
`b4db8044402b586ffda28843af48326fd5c5a7bbc2cbab611d2c9146f1e220cc`.
It contains zero TeX/package error, undefined control/reference/citation, rerun
request, overfull box, missing character, fatal error, or emergency stop.
Seventeen non-fatal underfull horizontal boxes and seven underfull vertical
boxes remain. The generic imakeidx advisories and optional biblatex
configuration-file notice are informational; both indexes are incorporated.

Resolved build artifacts include:

- BBL: 29,093 bytes, SHA-256
  `aedae96a05b2b62b7728ef815f287b2ef9eb4b6459a1901f08e5bad004543103`;
- term index: 7,954 bytes, SHA-256
  `090c12f3285e0937c8c2721e3658aeff3358119afd46dde8f0a10d63d20544da`;
- symbol index: 3,291 bytes, SHA-256
  `2b89a93b91e94877e6862568512c049ba43601fb9dc91578b072dff210cb2c1c`.

## PDF structure, accessibility qualification, and visual QA

The build PDF, frozen checkpoint, and promoted cumulative reader are
byte-identical: PDF 1.7, 247 pages, 1,230,437 bytes, SHA-256
`15976f12f8a401766cfeca2d446abd780ced1ddeedf812b2e65204d346b73ebf`.
It is unencrypted and untagged. Every page has zero rotation and the same
498.9 by 708.66-point geometry. Strict parsing finds 47 outline entries, 1,070
named destinations, 829 internal actions whose destinations all resolve, and
fourteen HTTPS URI actions. All 843 annotations parse; none is malformed.

There is no AcroForm, widget, JavaScript, embedded file, additional action,
structure tree, or `MarkInfo`; the opening action is the ordinary first-page
`/Fit` view and `/Lang` is `id-ID`. All 52 Poppler font rows are embedded and
subsetted; forty have ToUnicode maps and twelve mathematical fonts do not.
No extracted page contains U+FFFD. The PDF is therefore a searchable,
navigable, visually verified reader, not a tagged or fully semantic
accessibility artifact. Poppler reports its local missing `Adobe-GB1` mapping
pack while inventorying five inherited font mappings; strict parsing and fresh
rendering succeed, so this is recorded as a tool-environment limitation rather
than a missing reader resource.

Fresh renders cover physical pages 1--5, all Unit 040 pages 234--238, and all
backmatter pages 239--247. Full-size inspection covers the boundedness table,
both large truncation/homotopy diagrams, the reflowed duality identity, all four
correction notes, and the final proposition. Text blocks, displays, rules,
diagrams, theorem heads, footnotes, bibliography, and indexes are centered,
legible, and free of clipping, collision, truncation, detached punctuation,
black boxes, or missing visible glyphs. Physical page 238 is the intentional
blank inserted before backmatter. Contact sheets:

- `tmp/pdfs/unit040-finalD/contact-front-1-5.png`: 818,289 bytes, SHA-256
  `50e509841efa9789e32eacefde812f0c80dafb7167783ca3b1538343ae6fde1d`;
- `tmp/pdfs/unit040-finalD/contact-unit-234-238.png`: 2,851,085 bytes,
  SHA-256
  `2bae126d5c9a5c7e3b63b5e9666a32c9734a3fd582b579ebddd26f5fc7734a6e`;
- `tmp/pdfs/unit040-finalD/contact-tail-239-247.png`: 2,832,415 bytes,
  SHA-256
  `7ebccdbd391c6500819a8ca769611ee7ccbc4e7800c3770289ec5a3d71318e47`.

## Admission decision and next cursor

Admit Unit 040 and the cumulative reader through Chapter 3 Section 3.9. The
next exact source-order boundary is Unit 041,
`o014.aljabr2.chapter3.double-complex-cohomology`, *Kohomologi bikompleks*,
the complete `sec:double-cplx-coh`, `chapter3.tex` lines 1710--1881 inclusive,
stopping before `sec:resolutions` at line 1882. Freeze its normalized-LF
source witness and stable segment map before translation.

As throughout this lane, the author's official 650-page Linux/TeX Live/xindy
PDF remains authoritative. This 247-page Windows/MiKTeX/MakeIndex artifact is
a valid partial Indonesian reader and makes no pagination-identity claim. This
checkpoint does not complete the full corpus goal.
