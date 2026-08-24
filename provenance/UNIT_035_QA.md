# O014 Unit 035 admission and reader QA

Date: 2026-08-24  
Status: admitted local source-order checkpoint; the complete corpus, mastery
layer, semantic reader, and final release set remain in production.

## Authority and exact scope

- Work: Wen-Wei Li, *Methods of Algebra, Volume 2: Linear Algebra*.
- Authority: author-controlled Gitee `master` commit
  `9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
  `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.
- Unit: `o014.aljabr2.chapter3.opposite-category-complexes`, *Kompleks pada
  kategori lawan*.
- Exact authority boundary: `chapter3.tex` lines 622--699, including the blank
  separator at line 699 and stopping before `sec:double-cplx` at line 700.
- Frozen normalized-LF slice: `tmp/unit035-source-slice.tex`, 6,688 bytes,
  SHA-256
  `2fb37ee63cd53f2ac6de01c3aef3bc9fab1da286ee4ad989e7e9f38fd07108ba`.
- Ordered stable map: `tmp/unit035-segment-map.jsonl`, 24 records, 7,215
  bytes, SHA-256
  `238672a25609198890fec47d1a06490b15ae4e388e18f1ddd9fa7c311671a2af`.
- Target: `source/id-ID/chapter3-unit-035.tex`, 10,449 bytes, SHA-256
  `e0b892cb1be0a68e67a7e88dcb3b1c9fe6346a26811feb426b540a0be98c804f`.

The section contains six labels, four ordinary source references plus one
equation reference, one definition--proposition, two propositions, three
proofs, one remark, ten source displays, three TikZ-CD diagrams, two index
commands, and one source footnote. It contains no citation, list, exercise,
hint, solution, or external asset.

## Translation, topology, and mathematical review

The target has all 24 stable markers in exact map order and preserves all six
labels, five reference relationships, two indexes, three TikZ-CD diagrams,
environments, formulas, arrows, signs, and degrees. The forward reference to
`prop:derived-cat-op` uses the existing `sourcecrossref` fallback so the
partial reader remains warning-free while retaining the live label for the
eventual full corpus. Environment nesting is balanced. No Han-script prose,
replacement character, or malformed punctuation remains.

Two independent reviews checked the construction on objects and morphisms,
the shift isomorphism `s_m`, the degree-minus-one Hom dictionary, and every
mapping-cone comparison. The final review confirms the signs in all three
TikZ-CD diagrams and the matrix entry `-\sigma(f)^n`.

The reader build exposed two presentation-only width problems. The target
reduces `arraycolsep` locally to 4 pt for the source table and moves the long
three-term Hom identity into an aligned display. These changes preserve the
mathematics and remove both overfull boxes.

Two deterministic source corrections are recorded in
`controls/SOURCE_CORRECTIONS.csv`:

- O014-C036: authority line 645 incorrectly claims that applying the same
  `(-1)^{n+1}` construction twice strictly returns `X`. Direct substitution
  gives `(X,-d_X)`. The target discloses the natural isomorphism to `X` whose
  degree-`n` component is `(-1)^n\identity_{X^n}`, and the reverse coefficient
  `(-1)^n` that gives a strict inverse in both orders.
- O014-C037: authority line 635 calls `[-m]` part of the left side even though
  the immediately preceding display places it on the right. The target uses
  side-neutral wording and records this nonmathematical locator repair.

The corrections ledger now has 38 unique rows and ends at O014-C037. No
upstream contact occurred.

## Indonesian terminology and provenance

No genuinely new terminology concept is required. Existing settled forms
cover `kategori lawan`, `kompleks`, `kategori homotopi`, `kerucut pemetaan`,
`kategori turunan`, `kohomologi`, and `kompleks rantai`. The control and
backend ledgers remain exact 423-concept matches:

- `controls/TERMINOLOGY_O013_O014.csv`: 67,477 bytes, SHA-256
  `811ebc6201c4262418c2d34b939b9d2dd8493442359b4cc4094f365ef1f683c8`.
- `backend/terms.csv`: 28,447 bytes, SHA-256
  `d77d374e6ce2e4d231fbea5b96424df5a8269cc9493a432d39eb91699db61d89`.

The completed supplemental Indonesian field-usage review remains documented
at `controls/INDONESIAN_FIELD_TERMINOLOGY_QA.md`; no restricted witness is in
the reader or release payload. Exact source/author credits, CC BY 4.0 change
notice, component rights, non-endorsement, and the model identification
`OpenAI Codex gpt-5.6-sol, Ultra` remain in the edition metadata and rights
controls.

## Backend and cumulative source closure

- `backend/units.jsonl`: 35 unique IDs and sequences, 25,792 bytes, SHA-256
  `909e49066c27f4e1bfa7dc5d6a739d79a49d7d5f69e7f08279b4ecb0064ded3f`.
- `backend/segments.jsonl`: 1,793 unique IDs, including the exact 24 Unit 035
  IDs and sequences, 522,553 bytes, SHA-256
  `b70e3b93bb92e6890e78bcac9af2dcd1c88427a84ec7d7f12ec1e121e6d9e417`.
- Snapshot and stable wrappers are byte-identical: 8,693 bytes, SHA-256
  `2bfde7d988b5dc4c0c21f44e19c1386eaa891c6d7301d7685b6570edd2f17361`,
  with 35 exact ordered inputs and truthful coverage through Section 3.4.
- Snapshot and stable bibliographies are byte-identical: 6,649 bytes,
  SHA-256
  `a7ec7fa3df2ad91a8d13f8ed552e51e5c79ed64896e07dd68d4bd58b90ad2019`.

## Reproducible build and PDF inspection

The admitted shell-escape-disabled build is
`build/cumulative-unit-035-finalC-20260824`. It used XeLaTeX (MiKTeX 26.5),
Biber 2.21, both MakeIndex passes, and four XeLaTeX passes. Passes 3 and 4
differ only in the timestamp line. Biber resolves all 19 citekeys with no
warning or error. MakeIndex accepts 160 term entries and 61 symbol entries
with zero rejection or warning.

The final 79,457-byte log has SHA-256
`c18387a776347a26f88660d8ac768079fba0050691599c78229b35c3b9263050`
and zero TeX/package error, undefined reference or citation, rerun request,
overfull box, missing character, fatal error, or emergency stop. It contains
15 non-fatal underfull horizontal boxes and seven underfull vertical boxes,
four inherited LaTeX release-availability notices, one known biblatex
footnote-patching warning, and two expected shell-escape-disabled imakeidx
advisories.

The checkpoint and promoted cumulative PDF are byte-identical: PDF 1.7,
211 pages, 1,070,845 bytes, SHA-256
`1f6cc9abf330f9d25604bfe9b5862bb39114069973256bcb11f6be23cf0c8b4c`.
The file is `id-ID`, unencrypted, and untagged. It has 42 outline entries, 921
named destinations, 707 internal GoTo links, and 12 URI links, with no form,
JavaScript, embedded file, structure tree, or MarkInfo. All 51 fonts are
embedded; 11 mathematical fonts lack ToUnicode maps. Therefore this PDF is not
claimed to be an accessible semantic reader.

Physical pages 195--211 were rendered at 120 dpi. Both contact sheets and
full-size physical pages 201--204 were inspected. Section 3.4, its table,
translator note, three diagrams, bibliography, and indexes are centered,
legible, unclipped, and free of overlap or truncation. Contact-sheet hashes:

- `contact-195-203.png`: 2,111,714 bytes, SHA-256
  `89b7edf6e3641e1bc08548f9eacef4db57e9081e7285026ff1fab4360791878c`.
- `contact-204-211.png`: 1,344,048 bytes, SHA-256
  `124060a90c09db797aea14135bfd3131b389c032728f43863a06b0485c0f957f`.

Static evidence `tmp/unit035-qa.txt` is 3,888 bytes, SHA-256
`adcbb214b58e0748e1371bbd2acc612d35c51ad93b29020319fdea9ce62fd6ad`.

## Admission decision

Admit Unit 035 and the cumulative reader through Section 3.4. The next exact
source cursor begins at `chapter3.tex` line 700, `sec:double-cplx`; its complete
frozen boundary is recorded in `controls/CURRENT_CURSOR.json`. This admission
is a worthwhile partial checkpoint, not completion of the pursuit.
