# Unit 024 admission and cumulative QA

Date: 2026-08-22. Result: **PASS**. Unit 024 is admitted as the complete
`格论一瞥` section and the cumulative reader is admitted through
`chapter2.tex` line 720.

## Authority and translation boundary

- Stable unit ID: `o014.aljabr2.chapter2.glimpse-of-lattice-theory`.
- Indonesian title: `Sekilas tentang Teori Kisi`.
- Authority: pinned commit `9a5803ff77dd3257484cb177f851a73770a59dd3`,
  tree `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`, CC BY 4.0.
- Exact source range: `chapter2.tex` lines 519--720; line 720 is blank and
  line 721 begins `\section{直和分解}\label{sec:direct-sum}`.
- Normalized-LF witness: `tmp/unit024-source-slice.tex`, 14,567 bytes,
  SHA-256
  `acac220f78e67338b5db1b324c64b005ab70ca6cf57d2a644e33b79bbfcc2090`.
- Source-ordered map: `tmp/unit024-segment-map.jsonl`, 64 records, 18,850
  bytes, SHA-256
  `c8c46a101eeab8ffb0430acecb5d053a3c4a494a44728ec57022dba434ec0109`.
- Admitted target: `source/id-ID/chapter2-unit-024.tex`, 23,072 bytes,
  435 LF lines, SHA-256
  `e532e2e0f674b97d69fb5d94127d41b51273ffd35e555fcb6e1a8391b0f8cf3c`.

Two independent read-only audits pass. All 64 unique segment markers occur in
exact map order and cover every nonblank authority line. The localized
environment stream has the exact 66-token topology, closes in source order,
and leaves balanced braces. Exact parity is preserved for sixteen labels,
sixteen references (twelve `\ref` and four `\eqref` over nine targets), two
`Li1` citations, seventeen index entries, five TikZ-CD diagrams with arrow
vector `3,7,1,2,2`, two itemize environments with `2,3` items, one enumerate
with two items, eleven bracketed displays, two `equation`, two `equation*`,
and one `multline*`. There are no exercises or hints in this boundary. The
target has no CR, NUL, replacement character, or Han residue.

The inline-math count is 221 authority spans versus 233 target spans. The
complete difference is confined to the three disclosed source corrections
below; the sole source-only `$i$` is deliberately strengthened to the typed
range `$0\leq i<r$`. Reverse-applying those three blocks reconstructs the
pre-correction target byte-for-byte at its known SHA-256, proving there is no
unintended translation change.

## Disclosed source corrections

- O014-C021: source line 648 lets `sigma` permute `{0,...,r}` and then uses
  `x'_{sigma(i)+1}`. The target uses the `r` adjacent-factor indices
  `{0,...,r-1}` and quantifies `0<=i<r`; otherwise the final index is
  undefined.
- O014-C022: source lines 670--673 assume `a<b` but immediately assert that
  `r=0` exactly when `a=b`. The definition now uses `a<=b`, preserving the
  stated zero-length and singleton cases.
- O014-C023: for the descending chain `y_i>y_{i+1}`, source line 710 reverses
  both the interval endpoints and their assignments to `a<b`. The target uses
  `[y_{i+1},y_i]`, `y_{i+1}=a`, and `y_i=b`.

Each change has a visible `Catatan penerjemah` and an exact row in
`controls/SOURCE_CORRECTIONS.csv`. No upstream contact was made.

## Backend and terminology

- `backend/units.jsonl`: 24 unique sequential units, 17,830 bytes, SHA-256
  `77769f680d3c04dae958d8cd9e69e059ecf560a9487073fe61265230156055d4`.
- `backend/segments.jsonl`: 1,107 unique segments, 308,898 bytes, SHA-256
  `1e67811633be9a3ec5e540e4b4e55dc07281ba7194149d0babb7626535eb74a7`.
  Its 64 Unit-024 rows are byte-derived from the admitted map and match the
  target marker order exactly.
- Both terminology surfaces contain 347 unique concept IDs and have exact
  ID/preferred-form parity. The control ledger is 50,331 bytes, SHA-256
  `90c99eec762cae6e72a86579825a95fdd15b274e8d1d335c16532cc413561e50`;
  the backend is 23,081 bytes, SHA-256
  `1d8f60f87dbe9776f0214e542cd1729b8ebbb001cc561ca990780aeb8dff829c`.
  Unit 024 settles `kisi`, `kisi terbatas`, `kisi modular`, `komplemen`,
  `isomorfisme standar`, `penghalusan`, `penghalusan sejati`, `rantai naik`,
  `rantai menurun`, `Noetherian`, `Artinian`, and `berpanjang hingga`.

## Reproducible cumulative build

The frozen wrapper is
`source/id-ID/Al-jabr-2-id-cumulative-through-unit-024.tex`, 7,886 bytes,
SHA-256
`718f1f44db16d9991597b8e6ac5dc3dcfdadbf82515371a000384b140c50ccca`.
The frozen seventeen-entry bibliography is 5,356 bytes, SHA-256
`f915e4b1035df018391679d82a901dd825bd36ef6a27714618c4d47e6dab4c7f`.
The mutable wrapper is logically byte-identical after normalizing only the
mutable bibliography filename.

The final clean build ran in `build/cumulative-unit-024-frozen-final` with
XeLaTeX, Biber 2.21, MakeIndex for both indexes, and three final XeLaTeX
passes; shell escape remained disabled. The first visual build revealed one
9.88 pt overfull theorem-header line. A source-neutral `\mbox{}\par` places
the preserved full Schreier theorem title on its own line. The fresh final
build has no error, undefined control sequence, unresolved citation/reference,
rerun request, overfull box, or missing character. Ten underfull hboxes and six
visually benign underfull vboxes remain.

- PDF: 140 pages, 754,103 bytes, SHA-256
  `f7633cfd5783af30c464d2a04008cd5d1881f6ad2a375fce8aae3a53e74fcf97`.
- Final log: 77,766 bytes, SHA-256
  `beb3d03e4a7743e5d50168efb9246d6806d2cb584713361c69c9d60dcc96c52a`.
- Resolved BBL: 23,044 bytes, SHA-256
  `1ff14837ea986ec409b9851749d6dc83b4a9170ccc98e7303aea23e560476d87`.
- Term index: 106 accepted, zero rejected/warned; `.ind` 4,549 bytes,
  SHA-256
  `b4451e3e30700a50d29d5a69c7f2bd0a83833e9d6a340f2367ce0600bafc6b99`;
  `.ilg` 440 bytes, SHA-256
  `aa8f95fd7298e6a2182366d402ef1b3328544f3e56e20a7f1f0c73f04940afbb`.
- Symbol index: 38 accepted, zero rejected/warned; `.ind` 1,346 bytes,
  SHA-256
  `98f6367ea38dde5461be69127c4620a4c35e2d309d0f3686f36ab89cbeb7d6ec`;
  `.ilg` 294 bytes, SHA-256
  `8356719d3a5bacf93cc2b2266e2d0740ec036dd2dacd6178d9b81880ae6f3af5`.

The checkpoint and promoted cumulative PDF are byte-identical to the build.

## Structural and visual PDF QA

Strict parsing reports PDF 1.7, `id-ID`, unencrypted and untagged, with thirty
outline entries, 540 named destinations, and 430 links. All 420 internal links
resolve; ten URI links cover eight unique nonempty HTTPS URLs. There are no
other link actions, forms, AcroForm, JavaScript, embedded/associated files, or
additional actions. All fifty unique fonts are embedded and subset; 42 carry
ToUnicode maps.

Pypdf extracts 252,690 characters with zero replacement characters, 503 NULs
around mathematical content, and zero Han. MuPDF extracts 252,866 characters
with zero replacement characters and zero NULs; its 77 Han occurrences over 66
characters are intentional author names and exact bibliography metadata. The
PDF is not represented as tagged or fully accessible.

All 140 pages were rendered at 120 dpi, totaling 24,299,336 bytes. Intentional
blank versos are physical pages 2, 4, 106, 134, and 138. The full contact sheet
is 3,305,273 bytes, SHA-256
`d6a989a7a0df920e8eb6be36377ced6a395acfbef90dd32f9f2a6ba96df9c8c7`;
the detailed physical-pages-123--140 sheet is 2,292,689 bytes, SHA-256
`c26e34296ac024ae1894857a74c0a6fb737a678cc8fba2d2458e8bbe1172728e`.
Physical pages 126--133 were inspected individually at original resolution.
The section heading, five diagrams, theorem header, all three disclosure
footnotes, formulas, lists, bibliography, and indexes are centered and legible
with no clipping, overlap, detached punctuation, off-page content, or missing
glyph.

Poppler lacks this host's Adobe-GB1 mapping and warns only on the intentional
Chinese bibliography metadata. Independent MuPDF witnesses for pages 135 and
136 render it correctly: 118,672 bytes / SHA-256
`0f613055318889b8bab96fd92c207f7d60a5f1db391f84a9be9fa2b9dcebe81d`
and 128,409 bytes / SHA-256
`fcee597817abd3d02beeb74a5a1b559d3b726287f42e1c82c47d21256f37028b`.

## Admission decision

Admit Unit 024 and the 140-page cumulative boundary. Resume at Unit 025,
`chapter2.tex` line 721, section `直和分解`, stable ID
`o014.aljabr2.chapter2.direct-sum-decomposition`. This admission is a
production checkpoint, not pursuit completion.
