# Unit 023 QA

Status: PASS on the exact admitted target, backend records, frozen reader, and
promoted checkpoint hashes recorded below.

## Source boundary and target integrity

- Authority slice: `chapter2.tex` lines 293--518 inclusive, the complete
  section `若干图表引理`, stopping immediately before `格论一瞥` at line 519.
- The normalized-LF source witness is 17,617 bytes, SHA-256
  `3be24467bb3f58a982a52f3bd649453901d3be1f8c84a57e077bcb971c8cacd0`.
  It has a terminal LF and is exactly the pinned-authority range.
- Target: `source/id-ID/chapter2-unit-023.tex`, 25,487 bytes, SHA-256
  `fc4111560e37ca303539416a84ab98504fd9168a50c040d9a998ac68d0e9bf34`.
- The target is strict UTF-8 without BOM, LF-only, and contains no Han
  residue, CR, NUL, replacement character, placeholder, or active
  source-language prose.

## Fidelity, topology, references, and terminology

- Two independent semantic reviews find the Indonesian complete, natural, and
  mathematically faithful. The final review corrected three details before
  admission: module-specific `homomorfisme penghubung`, the source's theorem
  designation before Lema Ular, and settled `bikompleks`; it also replaced one
  calquey composition phrase. A later 17-byte shortening removes a 9.86-pt
  overfull box while preserving exactly the source claim that it suffices to
  prove the first displayed sequence exact.
- The target preserves one section, one lemma, one theorem, one proposition,
  one remark, three proofs, two itemize environments, one compact-item list,
  one enumeration, all thirteen items, six numbered equations, seventeen
  bracketed displays, two inline TikZ pictures with two drawn arrows, and every
  source paragraph.
- All 21 TikZ-CD diagrams preserve their node and arrow topology, with exact
  arrow-count vector `4,5,20,26,24,4,11,6,4,6,10,6,11,9,9,13,4,8,11,4,4`
  and 199 arrows total. Diagram code is source-identical modulo whitespace and
  the intended translation of `\text{natural morphism}` to
  `\text{morfisme alami}`.
- All eleven labels, 32 source references (twelve `\ref` and twenty
  `\eqref` calls), five citations over `KS06`, `Li1`, `stacks`, and `Be12`,
  and four index commands are preserved in exact order. Every reference is
  backward or within the unit; no new partial-reader fallback is required.
- The source has 176 inline-math spans and the target has 175. There is no
  mathematical omission: the only multiset difference combines adjacent
  source spans `$S' \to X'$` and `$\alpha$` into the single explicit
  composite `$S' \to X' \xrightarrow{\alpha} S$`.
- All 69 stable segment markers are unique, source ordered, and exactly equal
  to `tmp/unit023-segment-map.jsonl` and the 69 Unit 023 backend records in ID,
  sequence, source range, kind, references, and nesting. The exact map is
  19,104 bytes, SHA-256
  `b8e5d95b5ec5465824aa84f624c987adb9b1beae0c44102ef2fc2a11356b641d`.
- The full backend has 23 unique sequential units and 1,043 unique segments,
  with zero duplicate ID and zero missing nested parent. The unit backend is
  17,070 bytes, SHA-256
  `e45df4a6642d9c07580a5637dfd0c049a46593ca9ee3d421c55eec2537d68ec4`;
  the segment backend is 290,048 bytes, SHA-256
  `8d5614069fdb389963e1b0aaabf71cbf6881b8b45da4899599de4ab24cfae1e1`.
- Five first-use terms are added with exact parity between the control and
  locale-neutral backend: `kriteria keeksakan`, `morfisme penghubung`, `sifat
  kanonik`, `swa-dual`, and `lema Salamander`. Both terminology surfaces have
  335 unique concept IDs. The control is 48,497 bytes, SHA-256
  `a8d519e3d08319c348f32e9ee6ce63e4dc1f1b84e4f98e5ecef5797ab04d3e4c`;
  the backend is 22,407 bytes, SHA-256
  `318f573be11e85782a2a9a58fbad97aa000581cc118ba92d34e0a1f96ba8899d`.

## Frozen build

- Frozen wrapper:
  `source/id-ID/Al-jabr-2-id-cumulative-through-unit-023.tex`, 7,850 bytes,
  SHA-256
  `0f6e9deceb3478d632f4f06652682cd8628f911df1fe6cff96243222cabec9dc`.
- Frozen bibliography:
  `source/id-ID/references-cumulative-through-unit-023.bib`, 5,356 bytes,
  SHA-256
  `f915e4b1035df018391679d82a901dd825bd36ef6a27714618c4d47e6dab4c7f`.
  It preserves the Unit 022 bibliography and adds the exact upstream `Be12`
  record. Biber 2.21 resolves all seventeen cited keys without warning or
  error.
- The shell-escape-disabled XeLaTeX/Biber/MakeIndex/final-XeLaTeX replay
  produces a 77,498-byte final log, SHA-256
  `4b901bf218c12cad28e9eee4da76673e9103c6690c6041a3eba4b8478447bdf6`.
  It has no LaTeX error, undefined control sequence, unresolved reference,
  missing citation, rerun request, overfull box, or missing character. Nine
  underfull hboxes and six underfull vboxes remain visually benign. The
  inherited LaTeX release notices, biblatex footnote-patching warning, and
  routine imakeidx reminders remain disclosed.
- MakeIndex accepts 90 terminology entries and 37 symbol entries with zero
  rejection or warning. The resolved indexes have SHA-256
  `f37af2eb9bda9c6dd42cddbf2a7439702dd959dd4673b5de0a0f81a8cdc2abb6`
  and
  `e7b12c304abfac39774851ec0ea1f1bc6e5b8ec334fb0032d1e48835768fdf89`.

## Cumulative PDF and accessibility boundary

- Frozen and promoted checkpoint:
  `output/pdf/checkpoints/metode-dalam-aljabar-jilid-2-id-through-unit-023.pdf`.
- 132 pages; 722,835 bytes; SHA-256
  `43cb2ea687be2b8c40fd96c10d7863a0e89297452584b50b816517520cc92360`.
  The frozen build, checkpoint, and current cumulative output are
  byte-identical.
- PDF 1.7, unencrypted, language `id-ID`, and untagged, with no form, field,
  widget, JavaScript, embedded file, attachment, associated file, or additional
  action. This PDF is not represented as a tagged or fully accessible
  artifact.
- All 29 outline entries and 503 named destinations resolve. The PDF has 407
  link annotations: all 397 internal links resolve, and ten URI annotations
  cover eight unique nonempty HTTPS URLs.
- Recursive inspection finds 50 unique fonts, all embedded and subset; 42 have
  Unicode maps. Pypdf extracts 239,133 characters with zero replacement
  characters, 502 NULs around mathematical content, and zero Han. MuPDF
  extracts 239,112 characters with zero replacement characters, zero NULs,
  and 77 intentional Han occurrences over 66 unique code points, confined to
  personal names and exact bibliography metadata. These are disclosed
  extraction/accessibility limits, not visible defects.
- Physical pages 2, 4, 106, and 130 are the four intentional blank pages.

## Visual QA

- All 132 pages were rendered at 120 dpi, totaling 23,031,213 bytes, and
  inspected as a full contact sheet. The full sheet is 3,136,687 bytes,
  SHA-256
  `a1978d6dc14ec54332bb82517c09ea55536f29d30e56bbacb7abbb894a8b9d67`.
- Physical pages 118--126 were inspected individually at original render
  resolution. Section 2.3, all 21 TikZ-CD diagrams, both inline path symbols,
  the Snake/Five/Salamander lemma material, lists, equations, proof endings,
  and cross-reference links are centered, legible, and use the intended full
  text block with no clipping, overlap, detached punctuation, off-page
  content, or missing visible glyph.
- The detailed pages 119--132 sheet is 1,661,816 bytes, SHA-256
  `2dfe9081a2f5720eb31dc1cf5f79a265b553eea608e603fc7c6395bdb1fbb2b0`.
  Separate MuPDF witnesses for bibliography pages 127 and 128 have SHA-256
  `dc7fe6d9ce9f0aed7b72a3a9f0c87ca59f7474ff2dd731ca735b89b977c92354`
  and
  `06995768e7e54619c1b2bcb47bc5f7a75072841f0832929f6e844b277cc34a63`;
  they confirm that the intentional Chinese bibliography metadata hidden by
  this host's incomplete Poppler Adobe-GB1 mapping is embedded, visible, and
  unclipped.
