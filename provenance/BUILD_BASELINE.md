# Build baseline

## Upstream recipe

The pinned repository is a modular UTF-8 XeLaTeX project. Its Makefile invokes:

    latexmk -pdf -pdflatex="xelatex -synctex=1 -shell-escape -interaction=nonstopmode %O %S" Al-jabr-2

The declared closure uses the custom class and style files, TikZ/TikZ-CD,
PGFPlots, BibLaTeX/Biber, imakeidx/xindy, TeX Live 2024-era packages, and Noto
CJK/Fandol/TeX Gyre fonts. The committed and author-hosted full PDF are
byte-identical: 4,307,219 bytes, 650 pages, SHA-256
3e1b06656cf794321412b659de4ee5fb0a0177e62f1dc0fc484736c9cf57d58c.

## Independent local replay boundary

The exact authority tree remains byte-for-byte untouched. The original recipe
cannot start locally because the upstream open-font configuration and cover
still require absent Noto CJK families. A disposable build-only copy at
build/upstream-replay substitutes Fandol for those font selections and selects
font-setup-open.tex; it does not change mathematical or reader content.

The full editable closure then compiles through every included chapter,
appendix, bibliography, and index. MiKTeX's Windows xindy launcher was not
usable on this host: the invocation failed at launcher level and produced no
usable xindy output; its original console transcript was not retained. This is
consistent with the upstream README's warning that Windows is not recommended.
The generated split indexes are nevertheless
complete. A bounded MakeIndex fallback accepted all 510 terminology entries
and all 242 symbol entries with zero rejection and zero warning, followed by
two XeLaTeX passes.

Final local replay:

- 653 pages, PDF 1.7, unencrypted and untagged;
- 4,519,957 bytes;
- SHA-256
  20a342fbf91f2aba70e4b96eb6685c6207720f31e96e86579a9728c52b5b773d;
- log 95,853 bytes, SHA-256
  c19cdacda59158243a6eb5b5a0c188521e371ac8366f9001d4be7b8819944ab2;
- no LaTeX error, fatal stop, undefined control sequence, or unresolved
  reference;
- 20 overfull and 21 underfull box reports, retained as layout evidence.

This proves source/build closure but not byte or pagination identity. The
author's Linux/TeX Live/xindy PDF remains authoritative at 650 pages; the
Windows MakeIndex fallback changes index ordering and expands the local result
by three pages.

Representative MuPDF renders of pages 1, 3, 9, and 651--653 confirm the cover,
contents, body mathematics, and both completed indexes have visible Chinese
glyphs and coherent layout. This host's Poppler lacks the Adobe-GB1 language
pack and therefore omits those glyphs; that renderer-local limitation is not a
PDF-content failure and MuPDF is the recorded full-replay visual witness.

## Unit 001 build

The first Indonesian unit uses the same upstream AJbook2.cls,
titles-setup.tex, and mycommand.sty, plus a local font-setup-id.tex that selects
Fandol and does not require Noto. The reproducible sequence is an initial
XeLaTeX pass into build/unit-001, Biber, MakeIndex in that output directory,
then two XeLaTeX passes with the same absolute output directory and shell
escape disabled.

Toolchain observed:

- MiKTeX-XeTeX 4.18 / MiKTeX 26.5;
- Biber 2.21;
- PDF producer: MiKTeX-dvipdfmx 20260404.

After adding the explicit CC BY 4.0 URI, the rebuilt result is 11 pages, 60,387
bytes, SHA-256
b5220a089c5de19e22e46e12377d83f71c1cd86948ee2b35ea2466b4e17c7cb3.
The final log is 67,788 bytes, SHA-256
45f0b66f6d3874cd4db8c7f8792ad4e0a97bcdc6348c6287e0422ad9125cb82b.
It has no LaTeX error, undefined control sequence, unresolved reference,
overfull box, or underfull box. It records two non-fatal toolchain warnings:
the class requests LaTeX release 2026-06-01 while the installed LaTeX2e release
is 2025-11-01, and biblatex reports that footnote patching failed; Unit 001
contains no footnotes. Imakeidx also emits its generic rerun reminder even
though the retained `.ind` is present and the final pass includes it.

## Cumulative build through Unit 002

`source/id-ID/Al-jabr-2-id-cumulative.tex` inputs Units 001 and 002, loads
TikZ-CD, and uses `references-cumulative.bib`. The reproducible sequence is
XeLaTeX, Biber, MakeIndex in `build/cumulative-unit-002`, then two XeLaTeX
passes; shell escape remains disabled.

Final cumulative result:

- 17 pages; PDF 1.7; unencrypted and untagged;
- 97,996 bytes; SHA-256
  0f731bed4a38cfe3e4e2eb6aa75a1d3f85b959648d99ecc25f4ef7f5008bfe28;
- log 68,994 bytes; SHA-256
  2f2bd9628c09cea2a194c7f17e89e8ca6be4378c0f80e45d960a19196d8c5874;
- Biber found all three cited keys and emitted no warning or error;
- MakeIndex accepted the single current index entry with zero rejection and
  zero warning;
- no LaTeX error, undefined control sequence, unresolved reference, missing
  citation, or overfull box;
- one harmless underfull box (badness 1490) at the first subsection opening,
  plus the same class-release and biblatex patching warnings described above.

Strict parsing reports `id-ID`, five outline items, 14 annotations, no form,
JavaScript, attachment, encryption, Han residue, or replacement character. The
URI set contains the exact authority commit and CC BY 4.0 license. All 17 pages
were rendered at 120 dpi and visually inspected; the body, footnote, formulas,
and Dold--Kan diagram are complete with no clipping or overlap. Poppler emits a
host-local Adobe-GB1/F42 warning from dormant upstream CJK font machinery, but
the rendered Indonesian content and mathematical glyphs are visibly complete.

## Frozen cumulative build through Unit 003

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-003.tex` inputs Units
001--003 and uses the frozen nine-entry
`references-cumulative-through-unit-003.bib`. The build sequence is XeLaTeX,
Biber, MakeIndex, then two XeLaTeX passes in
`build/cumulative-unit-003-frozen`; shell escape is disabled.

Final result:

- 19 pages; PDF 1.7; unencrypted and untagged;
- 112,866 bytes; SHA-256
  `7c57d37dfc3de1f8fb17c1562c74604b674a0906d48886b84910e275b3163b66`;
- log 70,165 bytes; SHA-256
  `2064047e26a88f0757b4cf0b06816c31c7cc560b15c82fc1d544a058767b2b9b`;
- Biber resolves all nine bibliography entries without warning or error;
- MakeIndex accepts the current index without rejection;
- no LaTeX error, undefined control sequence, unresolved reference, missing
  citation, or overfull box;
- one inherited underfull hbox (badness 1490), one underfull vbox (badness
  3815), and the previously disclosed toolchain warnings.

Strict parsing reports `id-ID`, six recursive outline items, 26 annotations,
no form, JavaScript, attachment, encryption, Han residue, or replacement
character. The source-forward `sec:FM` reference displays its verified `B.6`
fallback and creates no broken partial link. All fonts are embedded. All 19
pages were rendered at 120 dpi and inspected; the newly added Unit 003 pages
are complete and legible. Poppler retains the documented host-local
Adobe-GB1/F42 warning from dormant CJK machinery.

## Frozen cumulative build through Unit 004

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-004.tex` inputs Units
001--004 and uses the frozen nine-entry bibliography. The same XeLaTeX,
Biber, MakeIndex, two-XeLaTeX sequence runs in
`build/cumulative-unit-004-frozen` with shell escape disabled.

Final result: 21 pages, 120,278 bytes, SHA-256
`cd38967c07f452705351fb7b150daf6b7368a58bef1cc87225446e55b92cb40f`.
The 70,297-byte final log has SHA-256
`31658eae69024844d1bf067398f925638e0686c5af24541f6e2b062be3e27442`.
Biber and MakeIndex complete without warning, error, or rejection. XeLaTeX
has no error, undefined control sequence, unresolved reference, missing
citation, or overfull box; the inherited underfull and toolchain warnings are
unchanged.

Strict parsing reports `id-ID`, seven recursive outline items, 28 annotations,
no form, JavaScript, attachment, encryption, Han residue, or replacement
character. All fonts are embedded. All 21 pages were rendered and inspected;
Unit 004's three pages are legible and complete. Poppler retains the documented
host-local Adobe-GB1/F42 warning from dormant CJK machinery.

## Frozen cumulative build through Unit 005

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-005.tex` inputs Units
001--005 and uses the frozen nine-entry bibliography. The same XeLaTeX,
Biber, MakeIndex, two-XeLaTeX sequence runs in
`build/cumulative-unit-005-frozen` with shell escape disabled.

Final result: 23 pages, 127,435 bytes, SHA-256
`4627d3027c14c4c045f0a62d68fb331e3f08c9ca0d6f91eaf8d632e505b17e85`.
The 70,861-byte final log has SHA-256
`99ab9fb45699bed641bc9df07cfaeaee868a6deab6a72ce47d7b93e944fbdf9d`.
Biber finds all nine entries without warning or error. MakeIndex accepts its
one entry without rejection or warning. XeLaTeX has no error, undefined
control sequence, unresolved reference, missing citation, or overfull box.
The description lists add four underfull hboxes (badness 10000, 4108, 4492,
and 4967); visual inspection confirms that these are spacing diagnostics, not
clipping or overlap.

Strict parsing reports `id-ID`, eight recursive outline items, 29 annotations,
no form, JavaScript, attachment, encryption, Han residue, or replacement
character. All fonts are embedded. All 23 pages were rendered and inspected;
the frozen and mutable-wrapper render sets are pixel-identical. Poppler retains
the documented host-local Adobe-GB1/F43 warning from dormant CJK machinery.

## Frozen cumulative build through Unit 006

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-006.tex` inputs Units
001--006 and uses the frozen nine-entry bibliography. The XeLaTeX, Biber,
MakeIndex, two-XeLaTeX sequence runs in
`build/cumulative-unit-006-frozen` with shell escape disabled.

Final result: 25 pages, 143,888 bytes, SHA-256
`3b187b2a6112ab7851412eb2a347f66ca12ffd7db70e54a5a9c1672c491aea9e`.
The 71,028-byte final log has SHA-256
`1bd014ef046a32985f4780d51f3bab5afff224c2f1e1f5a1e6f5305ac44591e1`.
Biber resolves all nine entries; MakeIndex accepts one entry with zero
rejection and warning. XeLaTeX has no error, undefined control sequence,
unresolved reference, missing citation, or overfull box. The inherited
underfull and toolchain warnings are unchanged.

Strict parsing reports `id-ID`, nine recursive outline items, 30 annotations,
no form, widget, JavaScript, attachment, encryption, or replacement character.
MuPDF extracts exactly the twelve disclosed Han personal names and no other
Han text after the Indonesian bibliography-string override. All fonts are
embedded. All 25 pages were rendered and inspected; Unit 006's two added pages
are complete and legible, and frozen/mutable MuPDF renders are pixel-identical.
Poppler lacks the host Adobe-GB1 mapping for the intentional Han names, so
MuPDF is the authoritative visual and extraction witness for those glyphs.

## Frozen cumulative build through Unit 007

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-007.tex` inputs Units
001--007 and uses the frozen eleven-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in
`build/cumulative-unit-007-frozen` with shell escape disabled.

Final result: 37 pages, 248,863 bytes, SHA-256
`1dea2f047e2617d6e2099a1853843b241100b9fae35d526de22125c031e47258`.
The 71,718-byte final log has SHA-256
`5bb9249f0be90888547e379fca152cda965a21648ff231230c5ab32a811dd8b3`.
Biber emits no warning or error. MakeIndex accepts 29 terminology entries and
17 symbol entries with zero rejection and warning. XeLaTeX has no error,
undefined control sequence, unresolved reference, missing citation, or
overfull box. Six underfull hboxes and one inherited underfull vbox are
retained honestly and have no visible defect.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 12 outline
items, 49 annotations, seven URI annotations over five unique URIs, and no
form, widget, JavaScript, or attachment. All fonts are embedded. All 37 pages
were rendered with MuPDF and inspected; the frozen and mutable page images are
pixel-identical. The centered universal-property tables, diagrams, intentional
Han metadata, bibliography, symbol index, and compact two-column term index
are complete and legible. Poppler's disclosed Adobe-GB1 limitation remains
host-local; MuPDF is the visual witness for intentional Han glyphs.

## Frozen cumulative build through Unit 008

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-008.tex` inputs Units
001--008 and uses the frozen eleven-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run from
a new `build/cumulative-unit-008-frozen` directory with shell escape disabled.

Final result: 41 pages, 256,802 bytes, SHA-256
`864f94329565e7b0094e35f544463440ee3413452408663406132fd300d57ef7`.
The 71,977-byte final log has SHA-256
`0a5b1e5139e924cd9dd524efa3419714fddfaa01d0a5ff67f406bb3c519c13c9`.
Biber emits no warning or error. MakeIndex accepts 29 terminology entries and
17 symbol entries with zero rejection and warning. XeLaTeX has no error,
undefined control sequence, unresolved reference, missing citation, rerun
request, or overfull box. Six inherited underfull hboxes and one inherited
underfull vbox remain visually benign.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 13 outline
items, 66 named destinations, 53 link annotations, seven URI annotations over
five unique URIs, and no form, widget, JavaScript, or attachment. All 46
internal links resolve and all fonts are embedded. Four mathematical fonts
lack Unicode maps; Pypdf and MuPDF therefore retain the documented
mathematical-text extraction limitation. MuPDF extracts exactly the 59
intentional Han glyphs confined to names and exact bibliography metadata.
All 41 pages were rendered and inspected, and the frozen and settled mutable
page images are pixel-identical. The localized, centered Chapter 1 title and
reader-tip chrome are complete and legible.

## Frozen cumulative build through Unit 009

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-009.tex` inputs Units
001--009 and uses the frozen eleven-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run from
a new `build/cumulative-unit-009-frozen` directory with shell escape disabled.

Final result: 45 pages, 276,985 bytes, SHA-256
`bcdebbae4fc2f81a042c3732344811ba00b3ae347529fb68e3998d8379c450c1`.
The 73,371-byte final log has SHA-256
`356a5aac94c7dd1c9560eb2734858fd635d2a64aced7979332ac0646e9b7ee2c`.
Biber emits no warning or error. MakeIndex accepts 34 terminology entries and
19 symbol entries with zero rejection and warning. XeLaTeX has no error,
undefined control sequence, unresolved reference, missing citation, rerun
request, or overfull box. Six inherited underfull hboxes and one inherited
underfull vbox remain visually benign.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 14 outline
items, 86 named destinations, 58 link annotations, seven URI annotations over
five unique URIs, and no form, widget, JavaScript, or attachment. All 51
internal links resolve and all 44 fonts are embedded. Four mathematical fonts
lack Unicode maps; Pypdf and the `mutool draw -F txt` surface therefore retain
the documented mathematical-text extraction limitation. MuPDF extracts
exactly the 59 intentional Han glyphs confined to names and exact bibliography
metadata. All 45 pages were rendered with MuPDF and inspected; the frozen and
mutable page images are pixel-identical. The localized theorem/proof chrome,
three new diagrams, and exact `(1.1.1)` equation numbering are complete and
legible with no clipping or overlap.

## Frozen cumulative build through Unit 010

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-010.tex` inputs Units
001--010 and uses the frozen eleven-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run from
a new `build/cumulative-unit-010-frozen` directory with shell escape disabled.

Final result: 49 pages, 295,848 bytes, SHA-256
`365c17817b41cc17567698279abe942e5eacf3ae738743ea33244f86fc784e2f`.
The 73,311-byte final log has SHA-256
`650c9708eb0e0a7319fcafe632189c490078d878bc55331feed11345ebc0eb0e`.
Biber emits no warning or error. MakeIndex accepts 38 terminology entries and
21 symbol entries with zero rejection and warning. XeLaTeX has no error,
undefined control sequence, unresolved reference, missing citation, rerun
request, or overfull box. Six inherited underfull hboxes and one inherited
underfull vbox remain visually benign.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 15 outline
items, 111 named destinations, 69 link annotations, seven URI annotations over
five unique URIs, and no form, widget, JavaScript, or attachment. All 62
internal links resolve and all 44 fonts are embedded. Four mathematical fonts
lack Unicode maps; Pypdf and the `mutool draw -F txt` surface therefore retain
the documented mathematical-text extraction limitation. MuPDF extracts
exactly the 59 intentional Han glyphs confined to names and exact bibliography
metadata. All 49 pages were rendered with MuPDF and inspected; the frozen and
mutable page images are pixel-identical. The Section 1.2 chrome, all nine new
diagrams, exact `(1.2.1)` equation numbering, and reflowed centered final
factorization diagram are complete and legible with no clipping or overlap.

## Frozen cumulative build through Unit 011

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-011.tex` inputs Units
001--011 and uses the frozen eleven-entry bibliography. Unit 011 first loads
the exact upstream `myarrows.sty` to obtain `\xlongequal`; the wrapper restores
the standard extendable-arrow commands afterward so earlier-unit typography
does not change. XeLaTeX, Biber, the terminology and symbol MakeIndex passes,
and two final XeLaTeX passes run in a new
`build/cumulative-unit-011-frozen` directory with shell escape disabled.

Final result: 58 pages, 343,514 bytes, SHA-256
`e72c2f71668b84382a24e57fd5001bd7b3cb5415229f82d9a45c9bd0f7b1b4f0`.
The 73,679-byte final log has SHA-256
`b2a020add0d1d1d9b71c6bbe1c57cdab155623ac53f94bfb295969622ace9272`.
Biber resolves all eleven entries without warning or error. MakeIndex accepts
47 terminology entries and 26 symbol entries with zero rejection or warning.
XeLaTeX has no error, undefined control sequence, unresolved reference,
missing citation, rerun request, or overfull box. Six inherited underfull
hboxes and one inherited underfull vbox remain visually benign.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 16 recursive
outline items, 158 named destinations, 97 link annotations, seven URI
annotations over five unique URIs, and no form, widget, JavaScript, embedded
file, or attachment. All 90 internal links resolve. All 45 font rows reported
by `pdffonts` are embedded; four mathematical fonts lack Unicode maps. Pypdf
and MuPDF retain the documented mathematical-text extraction limitations, and
MuPDF extracts exactly the 59 intentional Han glyphs confined to names and
exact bibliography metadata.

All 58 pages were rendered with MuPDF and inspected. The frozen and settled
mutable renders are pixel-identical. Full-size inspection of pages 43--52 and
the contents/bibliography/index pages confirms that the Section 1.3 heading,
two centered adjunction diagrams, biproduct identities, dual diagram pairs,
translator notes, wide Hom-set calculation, Banach example, and indexes are
legible with no clipping, overlap, or missing glyph.

## Frozen cumulative build through Unit 012

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-012.tex` inputs Units
001--012 and uses the frozen eleven-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in a
fresh `build/cumulative-unit-012-frozen` directory with shell escape
disabled.

Final result: 60 pages, 353,137 bytes, SHA-256
`b07c52b279c4a8e3da9be5331103e2f949396690f063ac9de9615137afaf841c`.
The 73,797-byte final log has SHA-256
`ee7f308519260ee37547ffaff0ba0dc52a3ae443061e11c8e7d3a32c2f1eead3`.
Biber resolves all eleven entries without warning or error. MakeIndex accepts
51 terminology entries and 27 symbol entries with zero rejection or warning.
XeLaTeX has no error, undefined control sequence, unresolved reference,
missing citation, rerun request, or overfull box. Six inherited underfull
hboxes remain; the inherited underfull vbox plus one new visually benign
underfull vbox are recorded.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, seventeen
recursive outline items, 170 named destinations, 106 link annotations, seven
URI annotations over five unique URIs, and no form, widget, JavaScript,
embedded file, or attachment. All 99 internal links resolve. All 45 font rows
are embedded; four mathematical fonts lack Unicode maps. Pypdf and MuPDF retain
the documented mathematical-text extraction limitations, and MuPDF extracts
exactly the 59 intentional Han glyphs confined to names and exact bibliography
metadata.

All 60 pages were rendered with MuPDF and inspected. Frozen and settled mutable
renders are pixel-identical. Full-size inspection of the new Section 1.4 pages
and the contents, bibliography, and index pages confirms that both reflowed
inline constructions, the two source-native diagrams, theorem numbering, and
localized index entries are legible with no clipping, overlap, detached
punctuation, or missing glyph.

## Frozen cumulative build through Unit 013

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-013.tex` inputs Units
001--013 and uses the frozen eleven-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in a
fresh `build/cumulative-unit-013-frozen` directory with shell escape disabled.

Final result: 66 pages, 379,707 bytes, SHA-256
`693a52fe0a54b14deac526b271381389a280c362a07c4e40e7f2664322dd59d2`.
The 74,038-byte final log has SHA-256
`5244a92a768febc2d00bf14b9fc2e55a232d3187a0c5ed90acabc45e1354a645`.
Biber resolves all eleven entries without warning or error. MakeIndex accepts
54 terminology entries and 28 symbol entries with zero rejection or warning.
XeLaTeX has no error, undefined control sequence, unresolved reference,
missing citation, rerun request, overfull box, or missing character. Six
inherited underfull hboxes and two visually benign underfull vboxes remain.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, eighteen
recursive outline items, 196 named destinations, 120 link annotations, seven
URI annotations over five unique URIs, and no form, JavaScript, embedded file,
or attachment. All 113 internal links resolve. All 48 font resources are
embedded; six lack Unicode maps. Pypdf and MuPDF retain the documented
mathematical-text extraction limitations, and MuPDF extracts exactly the 59
intentional Han glyphs confined to names and exact bibliography metadata.

All 66 pages were rendered at 120 dpi and inspected. Frozen and settled
mutable renders are pixel-identical. Full-size inspection of Section 1.5 pages
and the bibliography/index pages confirms that all three diagrams, comparison
morphisms, compatible-family display, translator notes, and index additions
are legible with no clipping, overlap, detached punctuation, or missing glyph.

## Frozen cumulative build through Unit 014

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-014.tex` inputs Units
001--014 and uses the frozen eleven-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in a
fresh `build/cumulative-unit-014-frozen` directory with shell escape disabled.

Final result: 72 pages, 411,020 bytes, SHA-256
`24fef5c26c5877f7454fa90365bbca23ca09c51e841340310680bb13eb030daa`.
The 75,761-byte final log has SHA-256
`ffe30cff81cdc30cf3e711a464a1902d80e2377b95a8c381ebe0c567d8ed18f5`.
Biber resolves all eleven entries without warning or error. MakeIndex accepts
60 terminology entries and 30 symbol entries with zero rejection or warning.
XeLaTeX has no error, undefined control sequence, unresolved reference,
missing citation, rerun request, overfull box, or missing character. Seven
underfull hboxes and two visually benign underfull vboxes remain.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, nineteen
recursive outline items, 226 named destinations, 135 link annotations, seven
URI annotations over five unique URIs, and no form, JavaScript, embedded file,
or attachment. All 128 internal links resolve. All 48 font resources are
embedded; six lack Unicode maps. Pypdf and MuPDF retain the documented
mathematical-text extraction limitations, and MuPDF extracts exactly the 59
intentional Han glyphs confined to names and exact bibliography metadata.

All 72 pages were rendered at 120 dpi and inspected. Frozen and settled
mutable renders are pixel-identical. Full-size inspection of pages 60--65
confirms that Section 1.6, its seven diagrams, finite-exchange formula, source
correction notes, bibliography, and indexes are legible with no clipping,
overlap, detached punctuation, or missing glyph. The local page enlargement
removes the earlier overfull vbox while retaining a clear lower margin.

## Frozen cumulative build through Unit 015

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-015.tex` inputs Units
001--015 and uses the frozen twelve-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in a
fresh `build/cumulative-unit-015-frozen` directory with shell escape disabled.

Final result: 78 pages, 449,497 bytes, SHA-256
`bc5f86b276f199d68f2a78e38067a19997dabafa97028fdd47c35dcf83a26459`.
The 75,894-byte final log has SHA-256
`75bf36d91e2d7a5ff0e252d1152e4153c28cd3a59cef3f495b64459d1ab5d7f7`.
Biber resolves all twelve cited keys without warning or error. MakeIndex
accepts 62 terminology entries and 32 symbol entries with zero rejection or
warning. XeLaTeX has no error, undefined control sequence, unresolved
reference, missing citation, rerun request, overfull box, or missing character.
Seven underfull hboxes and two visually benign underfull vboxes remain.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, twenty
recursive outline items, 250 named destinations, 154 link annotations, eight
URI annotations over six unique URIs, and no form, JavaScript, embedded file,
or attachment. All 146 internal links resolve. All 46 font rows reported by
`pdffonts` are embedded; four mathematical fonts lack Unicode maps. Pypdf
extracts zero replacement characters, 232 NULs around mathematical content,
and zero Han. MuPDF extracts 37 replacement glyphs, zero NULs, and exactly 59
intentional Han code points (53 unique) confined to names and exact
bibliography metadata. These remain documented extraction/accessibility
limits; the PDF is not tagged.

All 78 pages were rendered at 120 dpi and inspected. Frozen and settled
mutable renders are pixel-identical. Full-size inspection of physical pages
66--72 and the bibliography/index pages 73--78 confirms that Section 1.7, all
thirty new diagrams, both source-correction notes, the Ma07 bibliography
entry, and both indexes are legible with no clipping, overlap, detached
punctuation, or missing visible glyph. Poppler's local Adobe-GB1 mapping
warning affects extraction/rendering of exact Chinese bibliography names, so
a separate MuPDF rendering of page 74 was inspected and confirms those glyphs
are present in the PDF.

## Frozen cumulative build through Unit 016

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-016.tex` inputs Units
001--016 and uses the frozen twelve-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in a
fresh `build/cumulative-unit-016-frozen` directory with shell escape disabled.

Final result: 82 pages, 467,843 bytes, SHA-256
`c7c78c481d1bd10964bb6f2d4dbb8dad70d869389f881eb9f12cc0f81e8307ba`.
The 75,939-byte final log has SHA-256
`daa81cdfadcb72a897716a63a51081a1f1a9ac316a48a8ef07560fa8e008372e`.
Biber resolves all twelve cited keys without warning or error. MakeIndex
accepts 63 terminology entries and 32 symbol entries with zero rejection or
warning. XeLaTeX has no error, undefined control sequence, unresolved
reference, missing citation, rerun request, overfull box, or missing character.
Seven underfull hboxes and two visually benign underfull vboxes remain. The
first mutable attempt's 2.10254pt overfull hbox was eliminated before freezing
by a meaning-preserving Indonesian sentence shortening.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, twenty-one
recursive outline items, 267 named destinations, 174 link annotations, eight
URI annotations over six unique URIs, and no form, JavaScript, embedded file,
or attachment. All 166 internal links resolve. All 46 font rows reported by
`pdffonts` are embedded; four mathematical fonts lack Unicode maps. Pypdf
extracts zero replacement characters, 259 NULs around mathematical content,
and zero Han. MuPDF extracts 39 replacement glyphs, zero NULs, and exactly 59
intentional Han code points (53 unique) confined to names and exact
bibliography metadata. These remain documented extraction/accessibility
limits; the PDF is not tagged.

All 82 pages were rendered at 120 dpi and inspected. Frozen and settled
mutable renders are pixel-identical. Full-size inspection of physical pages
72--76 and bibliography/index pages 77--82 confirms that Section 1.8, all six
new diagrams, three numbered equations, the disclosed source repair, the
bibliography, and both indexes are legible with no clipping, overlap, detached
punctuation, or missing visible glyph. A separate MuPDF rendering of physical
page 78 confirms the exact Chinese bibliography metadata that the local
Poppler installation cannot render without Adobe-GB1 mapping data.

## Frozen cumulative build through Unit 017

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-017.tex` inputs Units
001--017 and uses the frozen fourteen-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in a
fresh `build/cumulative-unit-017-frozen` directory with shell escape disabled.

Final result: 94 pages, 530,120 bytes, SHA-256
`6e99e9333bdac7df99c0d496231cfd352d41f6989e2e3dc3a899c54bb2209f30`.
The 76,790-byte final log has SHA-256
`01391e82dfed4b00482a30b43feabdab0aca3ad057baedb3f5dbf0c7459981e4`.
Biber resolves all fourteen cited keys without warning or error. MakeIndex
accepts 69 terminology entries and 34 symbol entries with zero rejection or
warning. XeLaTeX has no error, undefined control sequence, unresolved
reference, missing citation, overfull box, or missing character. Nine
underfull hboxes and two visually benign underfull vboxes remain. The
inherited LaTeX release, `fontspec`, footnote-patching, and index reminders are
recorded but do not indicate an unresolved reader defect.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, twenty-two
recursive outline items, 329 named destinations, 217 link annotations, nine
URI annotations over seven unique URIs, and no form, widget, JavaScript,
embedded file, or attachment. All 208 internal links resolve. All 47 font rows
are embedded; four mathematical fonts lack Unicode maps. Pypdf and MuPDF
retain the documented mathematical-text extraction limits; MuPDF extracts the
same 59 intentional Han glyph occurrences confined to names and exact
bibliography metadata.

All 94 pages were rendered at 120 dpi and inspected. A clean frozen build
exposed one stale page number in the intermediate mutable term index; the full
mutable XeLaTeX/Biber/MakeIndex cycle was rerun, after which all 94 mutable and
frozen page images are pixel-identical. Full-size inspection of physical pages
76--87, the blank separator page 88, bibliography pages 89--90, and index pages
91--94 confirms that Section 1.9, all 26 new diagrams, the two disclosed source
repairs, bibliography, and indexes are legible with no clipping, overlap,
detached punctuation, off-page content, or missing glyph on the validated
render path. A separate MuPDF page-90 witness confirms the intentional Chinese
bibliography metadata that local Poppler cannot render without Adobe-GB1
mapping data.

## Frozen cumulative build through Unit 018

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-018.tex` inputs Units
001--018 and uses the frozen fourteen-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in a
fresh `build/cumulative-unit-018-frozen` directory with shell escape disabled.

Final result: 98 pages, 555,651 bytes, SHA-256
`1a724cd76acba0c1569456c443466cd8fb070721225bec8a1387d7c33147434e`.
The 76,833-byte final log has SHA-256
`7694b0e17a481a939d0f84bd162ad5dee78ec3ba40cba28e16b5f08391e7ab02`.
Biber resolves all fourteen entries without warning or error. MakeIndex
accepts 69 terminology entries and 34 symbol entries with zero rejection or
warning. XeLaTeX has no error, undefined control sequence, unresolved
reference, missing citation, overfull box, or missing character. Nine
underfull hboxes and two visually benign underfull vboxes remain. The inherited
LaTeX release, `fontspec`, footnote-patching, and index reminders remain
disclosed and do not indicate a reader defect.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, twenty-three
recursive outline items, 350 named destinations, 245 link annotations, nine
URI annotations over seven unique URIs, and no form, widget, JavaScript,
embedded file, or attachment. All 236 internal links resolve. All 47 font rows
are embedded; four mathematical fonts lack Unicode maps. Pypdf extracts zero
replacement characters, 318 NULs around mathematical content, and zero Han.
MuPDF extracts 40 replacement glyphs, zero NULs, and the same 59 intentional
Han occurrences confined to names and exact bibliography metadata. These are
documented extraction/accessibility limits; the PDF is not tagged.

All 98 pages were rendered at 120 dpi and inspected, totaling 16,972,504
bytes. Frozen and settled mutable renders are pixel-identical. Full-size
inspection of physical pages 87--92 and bibliography/index pages 93--98
confirms that Section 1.10, all eight diagrams, the disclosed source repair,
bibliography, and both indexes are legible with no clipping, overlap, detached
punctuation, off-page content, or missing visible glyph. A separate MuPDF
page-94 witness confirms the intentional Chinese bibliography metadata that
the local Poppler installation cannot render without Adobe-GB1 mapping data.

## Frozen cumulative build through Unit 019

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-019.tex` inputs Units
001--019 and uses the frozen fifteen-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in a
fresh `build/cumulative-unit-019-frozen` directory with shell escape disabled.

Final result: 112 pages, 635,782 bytes, SHA-256
`256d59b339def9786edf72c15b45559a45f1c61d76f5d92950996f4eccffac43`.
The 76,936-byte final log has SHA-256
`98affa53e9de79c962dba39ed772194b5948fde55ed979cd744ac7f917162573`.
Biber resolves all fifteen cited keys without warning or error. MakeIndex
accepts 75 terminology entries and 34 symbol entries with zero rejection or
warning. XeLaTeX has no error, undefined control sequence, unresolved
reference, missing citation, rerun request, overfull box, or missing
character. Nine underfull hboxes and two visually benign underfull vboxes
remain.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 25 outline
items, 428 named destinations, 312 link annotations, nine URI annotations over
seven unique URIs, and no form, widget, JavaScript, embedded file, or
attachment. All 303 internal links resolve. All 48 font rows are embedded;
five mathematical fonts lack Unicode maps. Pypdf extracts zero replacement
characters, 371 NULs around mathematical content, and zero Han. MuPDF
extracts 49 replacement glyphs, zero NULs, and 77 intentional Han occurrences
confined to names and exact bibliography metadata.

All 112 pages were rendered at 120 dpi, totaling 19,530,069 bytes. Frozen and
settled mutable renders are byte-identical. The full contact sheet and
physical pages 86--105 and 107--112 were inspected; intentional blank versos
are preserved. The Section 1.11 content, all fifteen diagrams, seventeen
exercises, ten hints, localized exercise/hint chrome, correction note,
bibliography, and indexes are legible with no clipping, overlap, off-page
content, or missing glyph. The MuPDF page-108 witness confirms the intentional
Chinese bibliography metadata hidden by this host's incomplete Poppler
Adobe-GB1 mapping.

## Frozen cumulative build through Unit 020

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-020.tex` inputs Units
001--020 and uses the frozen sixteen-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in a
fresh `build/cumulative-unit-020-frozen` directory with shell escape disabled.

Final result: 116 pages, 645,868 bytes, SHA-256
`e080e4d6d912b36f3dbb2b0c3d5f00c00f97cbcef8eb550d2694b91ae90d99fc`.
The 77,071-byte final log has SHA-256
`c37d62c87fde2d56aef96fb84e6876f79ac6557e962368d410830fd380a790d5`.
Biber 2.21 resolves all sixteen cited keys without warning or error.
MakeIndex accepts 76 terminology entries and 34 symbol entries with zero
rejection or warning. XeLaTeX has no error, undefined control sequence,
unresolved reference, missing citation, rerun request, overfull box, or
missing character. Nine underfull hboxes and three visually benign underfull
vboxes remain.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 26 resolved
outline items, 437 resolved named destinations, and 317 link annotations. All
307 internal links resolve; ten URI annotations cover eight unique URIs.
There is no form, field, widget, JavaScript, embedded file, attachment,
associated file, or collection. All 48 font rows are embedded and subset; 43
have Unicode maps. Pypdf extracts zero replacement characters, 372 NULs
around mathematical content, and zero Han. MuPDF extracts 49 replacement
glyphs, zero NULs, and 77 intentional Han occurrences over 66 unique code
points, confined to names and exact bibliography metadata.

All 116 pages were rendered at 120 dpi, totaling 20,112,560 bytes. Frozen and
settled mutable renders are byte-identical. The full contact sheet and
physical pages 107--109 and 111--116 were inspected; pages 110 and 114 are
intentional blank versos. The Chapter 2 opening, ordered overview, localized
reading-tip box, bibliography, and indexes are legible with no clipping,
overlap, detached punctuation, off-page content, or missing glyph. The MuPDF
page-112 witness confirms the intentional Chinese bibliography metadata hidden
by this host's incomplete Poppler Adobe-GB1 mapping.

## Frozen cumulative build through Unit 021

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-021.tex` inputs Units
001--021 and uses the frozen sixteen-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes run in a
fresh `build/cumulative-unit-021-frozen` directory with shell escape disabled.

Final result: 118 pages, 657,725 bytes, SHA-256
`4a7fa3afa68ea77db4c570528e65f1fdb2ddbfbb52653517c12bb694e6e674af`.
The 77,106-byte final log has SHA-256
`fd7668122039b2577060b9e11bca73baca2320d16a10bbbf60cb2de3148d6efb`.
Biber 2.21 resolves all sixteen cited keys without warning or error.
MakeIndex accepts 77 terminology entries and 34 symbol entries with zero
rejection or warning. XeLaTeX has no error, undefined control sequence,
unresolved reference, missing citation, rerun request, overfull box, or
missing character. Nine underfull hboxes and three visually benign underfull
vboxes remain.

One discarded first invocation passed PowerShell's `$out` name literally to
XeLaTeX. The exact resulting lane-local transient directory and the incomplete
output directory were verified and removed before the clean replay above. In
PowerShell, quote the complete native argument as `"-output-directory=$out"`;
do not pass `-output-directory=$out` as an unquoted native argument.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 27 resolved
outline entries, 453 resolved named destinations, and 338 link annotations.
All 328 internal links resolve; ten URI annotations cover eight unique URLs.
There is no form, field, widget, JavaScript, embedded file, attachment, or
associated file. All 48 font rows are embedded and subset; 43 have Unicode
maps. Pypdf extracts 214,922 characters, zero replacement characters, 409
NULs around mathematical content, and zero Han. MuPDF extracts 230,891
characters, 50 replacement glyphs, zero NULs, and 77 intentional Han
occurrences over 66 unique code points, confined to names and exact
bibliography metadata.

All 118 pages were rendered at 120 dpi, totaling 20,637,664 bytes. Frozen and
settled mutable renders are byte-identical. The full contact sheet and the
title, attribution, contents, Section 2.1, bibliography, and index pages were
inspected at full size. The Section 2.1 hierarchy, all three diagrams,
pullback--pushout proof, footnote, bibliography, and indexes are legible with
no clipping, overlap, detached punctuation, off-page content, or missing
glyph. The MuPDF page-114 witness confirms the intentional Chinese
bibliography metadata hidden by this host's incomplete Poppler Adobe-GB1
mapping.

## Frozen cumulative build through Unit 022

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-022.tex` inputs Units
001--022 and uses the frozen sixteen-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and two final XeLaTeX passes ran in a
fresh `build/cumulative-unit-022-frozen` directory with shell escape disabled.

Final result: 124 pages, 683,385 bytes, SHA-256
`1d3a337ea9acd8b55bd8760206e964b467b9330c320db737c9fd93a4a7bbb5a2`.
The 77,166-byte final log has SHA-256
`ec2c195b2675ca89ac5d389bada8ce4ffca38d31930d12cb6c7d71a3e53b5090`.
Biber 2.21 resolves all sixteen cited keys without warning or error.
MakeIndex accepts 86 terminology entries and 37 symbol entries with zero
rejection or warning. XeLaTeX has no error, undefined control sequence,
unresolved reference, missing citation, rerun request, overfull box, or
missing character. Nine underfull hboxes and three visually benign underfull
vboxes remain.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 28 resolved
outline entries, 476 resolved named destinations, and 367 link annotations.
All 357 internal links resolve; ten URI annotations cover eight unique
nonempty HTTPS URLs. There is no form, field, widget, JavaScript, embedded
file, attachment, associated file, or additional action. All 50 recursively
identified fonts are embedded and subset; 43 have Unicode maps. Pypdf extracts
zero replacement characters, 465 NULs around mathematical content, and zero
Han. MuPDF extracts 59 replacement glyphs, zero NULs, and 77 intentional Han
occurrences over 66 unique code points, confined to names and exact
bibliography metadata.

All 124 pages were rendered at 120 dpi, totaling 21,715,828 bytes. Frozen and
settled mutable renders are byte-identical. The optimized full contact sheet,
the detailed physical-page 107--118 sheet, and the title, chapter, new Section
2.2, bibliography, and index surfaces were inspected. Text uses the intended
centered full-width block; all ten Unit 022 diagrams and the definition/proof
hierarchy are legible with no clipping, overlap, detached punctuation,
off-page content, or missing glyph. The MuPDF page-120 witness confirms the
intentional Chinese bibliography metadata hidden by this host's incomplete
Poppler Adobe-GB1 mapping.

## Frozen cumulative build through Unit 023

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-023.tex` inputs Units
001--023 and uses the frozen seventeen-entry bibliography. XeLaTeX, Biber, the
terminology and symbol MakeIndex passes, and three final XeLaTeX passes ran in
`build/cumulative-unit-023-frozen` with shell escape disabled. Biber must be
given `source/id-ID` in `BIBINPUTS` when invoked from the isolated output
directory; the first Biber invocation omitted that search path and failed
without producing an artifact, after which the corrected invocation and full
final pass sequence succeeded.

Final result: 132 pages, 722,835 bytes, SHA-256
`43cb2ea687be2b8c40fd96c10d7863a0e89297452584b50b816517520cc92360`.
The 77,498-byte final log has SHA-256
`4b901bf218c12cad28e9eee4da76673e9103c6690c6041a3eba4b8478447bdf6`.
Biber 2.21 resolves all seventeen cited keys without warning or error.
MakeIndex accepts 90 terminology entries and 37 symbol entries with zero
rejection or warning. XeLaTeX has no error, undefined control sequence,
unresolved reference, missing citation, rerun request, overfull box, or
missing character. Nine underfull hboxes and six visually benign underfull
vboxes remain.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 29 resolved
outline entries, 503 resolved named destinations, and 407 link annotations.
All 397 internal links resolve; ten URI annotations cover eight unique URLs.
There is no form, field, widget, JavaScript, embedded file, attachment,
associated file, or additional action. All 50 unique fonts are embedded and
subset; 42 have Unicode maps. The documented extraction limits remain, and
the PDF is not represented as tagged or fully accessible.

All 132 pages were rendered at 120 dpi, totaling 23,031,213 bytes, and the
full contact sheet was inspected. Physical pages 118--126 were also inspected
individually at original resolution. Section 2.3, all 21 TikZ-CD diagrams,
both inline path symbols, the Snake/Five/Salamander lemma material, proof and
list hierarchy, bibliography, and indexes are centered and legible with no
clipping, overlap, detached punctuation, off-page content, or missing glyph.
MuPDF witnesses of bibliography pages 127--128 confirm the intentional Chinese
metadata that local Poppler cannot render without Adobe-GB1 mapping data.

## Frozen cumulative build through Unit 024

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-024.tex` inputs Units
001--024 and uses the frozen seventeen-entry bibliography. The admitted clean
build ran in `build/cumulative-unit-024-frozen-final` with shell escape
disabled: XeLaTeX, Biber 2.21 with `source/id-ID` in `BIBINPUTS`, both
MakeIndex passes, and three final XeLaTeX passes.

The first visual build found one 9.88 pt overfull theorem-header line. A
source-neutral `\mbox{}\par` after the Schreier theorem index preserves the
complete title while beginning the statement on the next line. The final
fresh build has no error, undefined control sequence, unresolved
citation/reference, rerun request, overfull box, or missing character. Ten
underfull hboxes and six visually benign underfull vboxes remain. Biber
resolves all seventeen keys. MakeIndex accepts 106 terminology entries and 38
symbol entries with zero rejection or warning.

Final result: 140 pages, 754,103 bytes, SHA-256
`f7633cfd5783af30c464d2a04008cd5d1881f6ad2a375fce8aae3a53e74fcf97`.
The 77,766-byte final log has SHA-256
`beb3d03e4a7743e5d50168efb9246d6806d2cb584713361c69c9d60dcc96c52a`.
The BBL has SHA-256
`1ff14837ea986ec409b9851749d6dc83b4a9170ccc98e7303aea23e560476d87`;
the term and symbol indexes have SHA-256
`b4451e3e30700a50d29d5a69c7f2bd0a83833e9d6a340f2367ce0600bafc6b99`
and
`98f6367ea38dde5461be69127c4620a4c35e2d309d0f3686f36ab89cbeb7d6ec`.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, thirty
outline entries, 540 named destinations, and 430 links. All 420 internal links
resolve; ten URI links cover eight unique HTTPS URLs. There is no form,
JavaScript, embedded/associated file, attachment, other link action, or
additional action. All fifty unique fonts are embedded/subset; 42 have
ToUnicode maps. Pypdf extracts 252,690 characters with zero replacements and
503 mathematical NULs. MuPDF extracts 252,866 characters with zero
replacements/NULs and 77 intentional Han occurrences over 66 characters in
names and exact bibliography metadata.

All 140 pages were rendered at 120 dpi, totaling 24,299,336 bytes. Intentional
blank versos are physical pages 2, 4, 106, 134, and 138. The full contact
sheet and physical pages 126--133 were inspected individually. The complete
Section 2.4, all five diagrams, theorem header, three disclosed correction
notes, formulas, lists, bibliography, and indexes are centered and legible
without clipping, overlap, detached punctuation, off-page material, or
missing glyph. MuPDF witnesses of bibliography pages 135--136 confirm the
intentional Chinese metadata hidden by this host's incomplete Poppler
Adobe-GB1 mapping.

## Frozen cumulative build through Unit 025

`source/id-ID/Al-jabr-2-id-cumulative-through-unit-025.tex` inputs Units
001--025 and the frozen eighteen-entry bibliography. The final clean build ran
in `build/cumulative-unit-025-final2-20260822` with shell escape disabled:
XeLaTeX, Biber 2.21 with `source/id-ID` in `BIBINPUTS`, both MakeIndex passes,
and three final XeLaTeX passes.

The first final build exposed two portability/presentation issues. Visible
Chinese bibliography fields depended on Adobe-GB1 maps that are absent on
some readers, so exact original-script metadata remains in source comments
while verified Hanyu Pinyin appears in the visible fields. The provenance
page's long source URL broke immediately after its scheme, so it was replaced
by two centered human-readable links to the repository and exact commit. The
second clean build has no TeX or package error, undefined control sequence,
unresolved reference/citation, rerun request, overfull box, or missing
character. Ten underfull hboxes and six visually benign underfull vboxes
remain. Biber resolves all eighteen cited keys. MakeIndex accepts 115 term
entries and 38 symbol entries with zero rejection or warning.

Final result: 146 pages, 771,201 bytes, SHA-256
`71f099e10d84e7d4f8c28756aba81c8ec82ca68a7f2d07df6cc168456efb5709`.
The 81,066-byte final log has SHA-256
`198f43e8276cf3d90256d9fcda80a156204faac4ff6364bbae43cb058162469a`.
The BBL has SHA-256
`308229e58134e11c6947ec59b712bf0b45e30a4bd235795fdc35ca2d9aca7128`;
the term and symbol indexes have SHA-256
`e65ff77ccd6e143c7ce2c32e951e4d0097072bfeda9f317810a4cbb0d9786569`
and
`98f6367ea38dde5461be69127c4620a4c35e2d309d0f3686f36ab89cbeb7d6ec`.

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, 31 valid
outline entries, 580 valid named destinations, and 456 link annotations. All
444 internal links resolve; twelve URI actions cover ten unique HTTPS URLs,
and every link rectangle lies within its page. There is no form, JavaScript,
embedded/associated file, launch or remote-GoTo action, media action, or
additional action. All 49 unique fonts are embedded/subset; 41 have ToUnicode
maps. Mathematical font extraction remains incomplete, so the reader is not
represented as tagged or fully accessible.

All 146 pages were freshly rendered at 70 dpi and inspected as a full contact
sheet. Physical pages 129--146 were inspected at higher detail; the corrected
provenance page and bibliography page 142 were rerendered and inspected
individually. Intentional blank versos/transitions are physical pages 2, 4,
106, 140, and 144. Section 2.5, its five diagrams and matrices, the two long
reflowed displays, the disclosed typing correction, bibliography, and indexes
are centered and legible without clipping, overlap, detached punctuation,
off-page material, or missing visible glyph.

## Frozen cumulative build through Unit 037

The admitted Unit 037 build is
`build/cumulative-unit-037-finalA-20260824`. It uses the frozen 37-input
wrapper `source/id-ID/Al-jabr-2-id-cumulative-through-unit-037.tex`, the
byte-identical stable bibliography
`references-cumulative-through-unit-037.bib`, XeLaTeX with shell escape
disabled, Biber 2.21, the bounded MakeIndex fallback for both indexes, and four
XeLaTeX passes. All 37 inputs and the bibliography resource resolve. Biber
processes 19 citekeys without warning or error. MakeIndex accepts 167 term
entries and 71 symbol entries with zero rejection and zero warning.

The final log is 79,650 bytes, SHA-256
`bcff49d344c09a3b34a68ac64b676fe6981bf1fa3526aa4cb46404f329065d84`.
It contains no TeX/package error, undefined control, unresolved reference or
citation, rerun request, overfull box, missing character or file, fatal error,
or emergency stop. Sixteen underfull horizontal boxes and seven underfull
vertical boxes remain non-fatal. Four inherited LaTeX release notices, one
biblatex footnote-patching warning, and two generic imakeidx advisories remain;
the completed final passes incorporate both generated indexes.

The resulting PDF 1.7 is 223 pages and 1,127,663 bytes, SHA-256
`27e07599542a5994f99c6a43c4a8cebdfec4c2f2d3415e186fa79dea108facb0`.
It is `id-ID`, unencrypted, and untagged. All 52 fonts are embedded and
subsetted; 11 mathematical fonts lack ToUnicode maps. It has 44 outlines, 974
named destinations, 749 resolved GoTo actions, and 12 URI actions, with no
form, JavaScript, embedded file, structure tree, or MarkInfo. Visual QA covers
physical pages 1--8 and 209--223, with full-size inspection of pages 213--216;
the section, six diagram groups, footnotes, bibliography, and indexes are
centered and unclipped. Physical pages 2, 4, and 220 are intentional verso
pages. The PDF therefore remains a visually verified reader, not a tagged or
fully semantic accessibility artifact.

As throughout this lane, the author's official 650-page Linux/TeX Live/xindy
PDF is authoritative. This 223-page Windows/MiKTeX/MakeIndex artifact is a
valid partial Indonesian reader and makes no pagination-identity claim.

## Frozen cumulative build through Unit 038

The admitted Unit 038 build is
`build/cumulative-unit-038-finalD-20260824`. It uses the frozen 38-input
wrapper `source/id-ID/Al-jabr-2-id-cumulative-through-unit-038.tex`, the
byte-identical stable bibliography
`references-cumulative-through-unit-038.bib`, XeLaTeX with shell escape
disabled, Biber 2.21, both bounded MakeIndex passes, and converged final
XeLaTeX passes. All 38 inputs and all nineteen cited bibliography keys resolve.
Biber has no warning or error. MakeIndex accepts 167 terminology entries and
71 symbol entries with zero rejection and zero warning.

The final log is 79,553 bytes, SHA-256
`d6648d30b969f1c515910e594f9b91ff397c631edfecd10dad1d69489d6e1aff`.
It contains no TeX/package error, undefined control, unresolved reference or
citation, rerun request, overfull box, missing character or included file,
fatal error, or emergency stop. Sixteen non-fatal underfull horizontal boxes
and seven underfull vertical boxes remain. The informational absence of the
optional `biblatex-dm.cfg`, inherited LaTeX release notices, the known
biblatex footnote-patching warning, and generic imakeidx advisories remain;
both generated indexes are incorporated in the final passes.

The resulting PDF 1.7 is 231 pages and 1,162,756 bytes, SHA-256
`71293cdd594e6df12ddf7ea0c1ca74518e1a0ca5da530f91934a562426702a07`.
It is unencrypted and untagged, with 45 outline items, 1,007 named
destinations, 796 resolved internal actions, and twelve HTTPS actions. All 52
font rows reported by `pdffonts` are embedded/subset; eleven mathematical fonts
lack ToUnicode maps. There is no JavaScript, form, widget, embedded file,
additional action, structure tree, or `MarkInfo`; the sole open action is the
ordinary first-page `/Fit` view. The reader is not represented as tagged or
fully semantic.

Fresh 120-dpi visual QA covers physical pages 1--5, all Unit 038 pages
217--224, and bibliography/index pages 225--231. The cover and attribution
state Section 3.7 and source coverage through `chapter3.tex` line 1291. All
text blocks, long reflowed maps, sixteen diagrams, equation numbers, theorem
heads, footnotes, bibliography, and indexes are centered, legible, and
unclipped. Physical page 224 has intentional lower whitespace because the
section ends there. Exact contact-sheet hashes and the full accessibility
qualification are recorded in `qa/UNIT_038_QA.md`.

As throughout this lane, the author's official 650-page Linux/TeX Live/xindy
PDF is authoritative. This 231-page Windows/MiKTeX/MakeIndex artifact is a
valid partial Indonesian reader and makes no pagination-identity claim.

## Frozen cumulative build through Unit 039

The admitted Unit 039 build is
`build/cumulative-unit-039-finalC-20260825`. It uses the 39-input wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-039.tex`, 8,799 bytes,
SHA-256
`5dc42a8a699bfd2fc0fd25a3bbe6174a2aa7d0fa9210ffc39d41679c4a6c8937`,
and the 21-entry bibliography
`references-cumulative-through-unit-039.bib`, 7,631 bytes, SHA-256
`b882ae8225e57e383d85b4a5a8f69a0bddc688f20157365d8513b47f612ee597`.
The mutable wrapper and bibliography aliases are byte-identical to these
frozen files.

The fresh shell-escape-disabled replay ran XeLaTeX, Biber 2.21, bounded
MakeIndex passes for both indexes, and three further XeLaTeX passes. Biber
resolved all 21 citekeys with zero warning or error. MakeIndex accepted 180
terminology entries and 82 symbol entries with zero rejection or warning.
The 84,606-byte final log has SHA-256
`33fb1a38c0fa46dee4ca3fd3012c71b89b1f844ece7a2f66bd418250ed61e1bf`
and contains zero TeX/package error, undefined control/reference/citation,
rerun request, overfull box, missing character, fatal error, or emergency
stop. Seventeen underfull horizontal boxes and seven underfull vertical boxes
remain non-fatal. The one matched missing-file string is biblatex's
informational absence of optional `biblatex-dm.cfg`, not a missing reader
resource. The resolved BBL is 29,093 bytes, SHA-256
`aedae96a05b2b62b7728ef815f287b2ef9eb4b6459a1901f08e5bad004543103`;
the term index is 7,799 bytes, SHA-256
`5a285a0e77e571a5b48a11b1ea71cdc920f32476f2dde200a331f7b589a8e73b`;
and the symbol index is 2,847 bytes, SHA-256
`039e0f874c2e574719296d2512fa4abce481951069c167cd3cb29bf606ff4d63`.

The build, checkpoint, and promoted cumulative PDF are byte-identical: PDF
1.7, 243 pages, 1,210,711 bytes, SHA-256
`11cabff2db7b4bdb1abaaf29be78a37fd5e16b4dd08b30f6debf88742f026f6a`.
All pages use the same 498.9 x 708.66-point geometry and zero rotation. The
file is unencrypted and untagged, with 46 valid outline entries, 1,049 valid
named destinations, 817 resolved internal links, and fourteen HTTPS links.
There is no form, widget, JavaScript, embedded file, additional action,
structure tree, or `MarkInfo`; the opening action is the ordinary first-page
`/Fit` view. All 52 font rows are embedded/subset; twelve mathematical fonts
lack ToUnicode maps, so a tagged or fully semantic PDF is not claimed.

Fresh 120-dpi visual QA covers physical pages 1--5, all Unit 039 pages
224--234, and bibliography/index pages 235--243. The corrected cover states
Chapter 3 through Section 3.8. All text blocks, formulas, theorem heads,
footnotes, ten TikZ-CD diagrams, the cyclic-complex figure, bibliography, and
indexes are centered, legible, and unclipped. Physical page 234 has
intentional lower whitespace because the section ends there. Exact
contact-sheet hashes and the full accessibility qualification are recorded in
`qa/UNIT_039_QA.md`.

As throughout this lane, the author's official 650-page Linux/TeX Live/xindy
PDF is authoritative. This 243-page Windows/MiKTeX/MakeIndex artifact is a
valid partial Indonesian reader and makes no pagination-identity claim.

## Frozen cumulative build through Unit 040

The admitted Unit 040 build is
`build/cumulative-unit-040-finalD-20260825`. It uses the 40-input wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-040.tex`, 8,824 bytes,
SHA-256
`c0039cb6018e040ea34b94ef8c4ea9c21cebc5ff478e5bc2fd57b9ab2a9b29cf`,
and the 21-entry bibliography
`references-cumulative-through-unit-040.bib`, 7,631 bytes, SHA-256
`b882ae8225e57e383d85b4a5a8f69a0bddc688f20157365d8513b47f612ee597`.
The mutable wrapper and bibliography aliases are byte-identical.

The fresh shell-escape-disabled replay ran XeLaTeX, Biber 2.21, bounded
MakeIndex passes for both indexes, and three further XeLaTeX passes. Biber
resolved all 21 citekeys with zero warning or error. MakeIndex accepted 182
terminology entries and 88 symbol entries with zero rejection or warning. The
84,754-byte final log has SHA-256
`b4db8044402b586ffda28843af48326fd5c5a7bbc2cbab611d2c9146f1e220cc`
and contains zero TeX/package error, undefined control/reference/citation,
rerun request, overfull box, missing character, fatal error, or emergency stop.
Seventeen underfull horizontal boxes and seven underfull vertical boxes remain
non-fatal. The BBL is 29,093 bytes / SHA-256
`aedae96a05b2b62b7728ef815f287b2ef9eb4b6459a1901f08e5bad004543103`;
the term index is 7,954 bytes / SHA-256
`090c12f3285e0937c8c2721e3658aeff3358119afd46dde8f0a10d63d20544da`;
and the symbol index is 3,291 bytes / SHA-256
`2b89a93b91e94877e6862568512c049ba43601fb9dc91578b072dff210cb2c1c`.

The build, checkpoint, and promoted cumulative PDF are byte-identical: PDF
1.7, 247 pages, 1,230,437 bytes, SHA-256
`15976f12f8a401766cfeca2d446abd780ced1ddeedf812b2e65204d346b73ebf`.
All pages use the same 498.9 by 708.66-point geometry and zero rotation. The
file is unencrypted and untagged, with 47 outline entries, 1,070 named
destinations, 829 resolved internal actions, and fourteen HTTPS actions. There
is no form, widget, JavaScript, embedded file, additional action, structure
tree, or `MarkInfo`; the opening action is the ordinary first-page `/Fit` view.
All 52 Poppler font rows are embedded/subset; forty have ToUnicode maps and
twelve mathematical fonts do not, so a tagged or fully semantic PDF is not
claimed.

Fresh visual QA covers physical pages 1--5, Section 3.9 on pages 234--238, and
the complete bibliography/index tail on pages 239--247. Full-size inspection
of pages 234--237 verifies the reflowed boundedness table, both diagrams, the
duality display, all correction notes, and the final proposition. Every text
block, display, diagram, footnote, bibliography entry, and index is centered,
legible, and unclipped; physical page 238 is an intentional pre-backmatter
blank. Exact contact-sheet hashes and the accessibility qualification are in
`qa/UNIT_040_QA.md`, 9,489 bytes, SHA-256
`e7eab8020a62d6a1994212742e73b573de6520f92ffed8ec1c412e8e49171705`.

As throughout this lane, the author's official 650-page Linux/TeX Live/xindy
PDF is authoritative. This 247-page Windows/MiKTeX/MakeIndex artifact is a
valid partial Indonesian reader and makes no pagination-identity claim.

## Frozen cumulative build through Unit 041

The admitted Unit 041 build is
`build/cumulative-unit-041-finalD-20260825`. It uses the 41-input wrapper
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-041.tex`, 8,875 bytes,
SHA-256
`d3176291b3f2162016a14686908fe1076263398565ef3ba13aaa99f449630e54`,
and the 21-entry bibliography
`references-cumulative-through-unit-041.bib`, 7,631 bytes, SHA-256
`b882ae8225e57e383d85b4a5a8f69a0bddc688f20157365d8513b47f612ee597`.
The mutable wrapper and bibliography aliases are byte-identical.

The fresh shell-escape-disabled replay ran XeLaTeX, Biber 2.21, bounded
MakeIndex passes for both indexes, and three further XeLaTeX passes. Biber
resolved all 21 citekeys with zero warning or error. MakeIndex accepted 182
terminology entries and 93 symbol entries with zero rejection or warning. The
80,161-byte final log has SHA-256
`08bc57c1c7f48755fa79d00da4d06ccba12c8e1355fdf7d39f5fd02df02c4f17`
and contains zero TeX/package error, undefined control/reference/citation,
rerun request, overfull box, missing character, fatal error, or emergency
stop. Seventeen underfull horizontal boxes and seven underfull vertical boxes
remain non-fatal. The BBL is 29,093 bytes / SHA-256
`aedae96a05b2b62b7728ef815f287b2ef9eb4b6459a1901f08e5bad004543103`;
the term index is 7,954 bytes / SHA-256
`090c12f3285e0937c8c2721e3658aeff3358119afd46dde8f0a10d63d20544da`;
and the symbol index is 3,562 bytes / SHA-256
`32cfe879a5aaa893a4b9da15d5e54cf0255ba9da54369225786f3ea0fb75d02e`.

The build, checkpoint, and promoted cumulative PDF are byte-identical: PDF
1.7, 253 pages, 1,255,777 bytes, SHA-256
`f364d2c3b6839a14b89f77313f9e3117dc9b7b5e5ad920d27637924513d5a29f`.
All pages use the same 498.9 by 708.66-point geometry and zero rotation. The
file is unencrypted and untagged, with 48 valid outline entries, 1,097 named
destinations, 858 resolved internal links, and fourteen URI links. There is no
form, widget, JavaScript, embedded file, additional action, structure tree, or
`MarkInfo`; the opening action is the ordinary first-page `/Fit` view. All 52
font rows are embedded/subset; twelve mathematical fonts lack ToUnicode maps,
so a tagged or fully semantic PDF is not claimed.

Fresh 120-dpi visual QA covers physical pages 1--5, every Unit 041 page
238--243, and the complete bibliography/index tail on pages 244--253. The
cover and attribution truthfully state Chapter 3 through Section 3.10 and
source coverage through line 1880. The long cone-object definition was
reflowed into display math, and long quasi-isomorphism labels were moved from
two crowded diagrams into adjacent prose. Full-size inspection confirms that
all seven diagrams, formulas, theorem heads, correction notes, bibliography,
and indexes are centered, legible, and unclipped; physical page 244 is the
intentional blank before backmatter.

As throughout this lane, the author's official 650-page Linux/TeX Live/xindy
PDF is authoritative. This 253-page Windows/MiKTeX/MakeIndex artifact is a
valid partial Indonesian reader and makes no pagination-identity claim.
