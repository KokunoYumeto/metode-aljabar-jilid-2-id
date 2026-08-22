# External Indonesian field-terminology QA

Date: 2026-08-22  
Scope: terminology check at the admitted Unit-024 boundary, before Unit 025 is
admitted  
Edition: independent Indonesian derivative of Wen-Wei Li, *Methods of Algebra,
Volume 2: Linear Algebra*

## Method and bounded arXiv result

The check began with arXiv, as requested. The official arXiv search for the
exact phrase `"Bahasa Indonesia"` returned 17 records. All 17 displayed records
were in computer-science/electrical-engineering categories and none was an
Indonesian-language source in category theory, module theory, or homological
algebra. Exact official searches for `"aljabar homologi"` and `"kategori abel"`
returned no records. Additional bounded probes for `ruang vektor`, `gelanggang`,
`rantai kompleks`, `fungtor`, and `homomorfisme` did not produce an admissible
same-field Indonesian paper with a downloadable TeX source package. This is a
bounded negative result, not a claim that no such arXiv item can exist.

Official search URLs inspected:

- <https://arxiv.org/search/?query=%22Bahasa+Indonesia%22&searchtype=all&abstracts=show&order=-announced_date_first&size=50>
- <https://arxiv.org/search/?query=%22aljabar+homologi%22&searchtype=all&abstracts=show&order=-announced_date_first&size=50>
- <https://arxiv.org/search/?query=%22kategori+abel%22&searchtype=all&abstracts=show&order=-announced_date_first&size=50>

Because no admissible arXiv source package was found, the instructed fallback
was used. Two official Indonesian institutional PDFs were inspected directly.
They are terminology witnesses only and are not donor text or redistributable
edition components.

## Primary fallback witness

Gustina Elfiyanti, *Kajian Kategori U-Kompleks dan Kategori U-Kompleks Lemah*,
doctoral dissertation, Doctoral Program in Mathematics, Institut Teknologi
Bandung, November 2020; approved 20 November 2020. Supervisors: Dr. Muchtadi
Intan Detiena and Ahmad Muchlis, Ph.D.

- Official ITB catalog page:
  <https://digilib.itb.ac.id/gdl/view_data/kajian-kategori-u-kompleks-dan-kategori-u-kompleks-lemah/>
- Official ITB front-matter PDF:
  <https://digilib.itb.ac.id/assets/files/2021/QUJTVFJBSyBHVVNUSU5BIEVMRklZQU5USS5wZGY.pdf>
- Local evidence copy:
  `authority/terminology-qa/itb-2020-gustina-elfiyanti-u-complex-abstract.pdf`
- Identity: 4 pages, 126,507 bytes, SHA-256
  `8e56993c4abcac3d7f89c9bb948e9d9925de6eef8b3102121c530e43ed8f19be`.

All four pages were rendered and visually inspected. The parallel Indonesian
and English abstracts directly support the following mappings: *homological
algebra* / `aljabar homologi`; *chain complex* / `rantai kompleks`;
*connecting homomorphism* / `Homomorfisma Penghubung`; *exact triangle* /
`Segitiga Eksak`; *abelian category* / `kategori abel`; *homotopy category* /
`kategori homotopi`; *additive category* / `kategori aditif`; *triangulated
category* / `kategori tersegitigakan`; *derived category* / `kategori
bentukan`; and *Snake Lemma* / `Lema Ular`.

The PDF itself states an ITB campus-use restriction. It is retained locally only
as the requested QA witness and must not be placed in GitHub, Zenodo, Figshare,
or an edition source package.

## Secondary same-field comparator

Ryan Kasyfil Aziz, *Identifikasi Aljabar Tipe Hingga*, undergraduate final
report, Mathematics, Institut Teknologi Bandung, 2012; supervisor Dr. Muchtadi
Intan Detiena. The directly inspected Chapter 2 PDF is the official repository
segment “Aljabar, Modul, dan Kategori.”

- Official ITB PDF:
  <https://digilib.itb.ac.id/assets/files/disk1/349/jbptitbpp-gdl-ryankasyfi-17418-3-2012ta-2.pdf>
- Local evidence copy:
  `authority/terminology-qa/itb-2012-ryan-kasyfil-aziz-chapter2.pdf`
- Identity: 12 pages, 435,907 bytes, SHA-256
  `196d921577e7ba9f2508d8e1cc5be434061a8e1f40c71f8f7adcf643f00c2c1c`.

All twelve pages were rendered and visually inspected. This chapter independently
uses `gelanggang`, `lapangan`, `ruang vektor`, `modul`, `submodul`, `modul
kuosien`, `jumlah langsung`, `dekomposisi jumlah langsung`, `modul projektif`,
`barisan eksak`, `morfisma`, `homomorfisma modul`, and the older spelling
`fungtor`. It also uses `tak terdekomposisi` where this edition uses `tak
terurai`. The PDF is encrypted and forbids copying/printing in its permissions;
it is therefore also strictly a local terminology witness and is excluded from
all public payloads.

## Comparison and decisions

| Concept | Current preferred form | Witness form | Decision |
|---|---|---|---|
| homological algebra | `aljabar homologis` | `aljabar homologi` | Retain the adjectival current form for grammatical clarity and corpus-wide consistency; preserve the attested witness form as a glossary variant. |
| chain complex | `kompleks rantai` | `rantai kompleks` | Retain the current form, which keeps `kompleks` as the head and distinguishes it symmetrically from `kompleks kokrantai`; add the attested variant. |
| abelian category | `kategori abelian` | `kategori abel` | Retain the coordinated O014 form; record lowercase `kategori abel` and `kategori Abel` as variants. No mathematical distinction is intended. |
| additive category | `kategori aditif` | `kategori aditif` | Exact match; no change. |
| triangulated category | `kategori bertriangulasi` | `kategori tersegitigakan` | Retain the current descriptive form and add the attested alternative. |
| derived category | `kategori turunan` | `kategori bentukan` | Retain `turunan`, which maps the mathematical operation more specifically and matches `funktor turunan`; add `bentukan` as an attested variant. |
| connecting morphism | `morfisme penghubung` | `homomorfisma penghubung` | Retain the category-general `morfisme`; retain both `homomorfisme` and the witnessed `homomorfisma` in module-specific contexts. |
| morphism | `morfisme` | `morfisma` | Retain the coordinated preferred spelling; the witness spelling was already registered as a variant. |
| functor | `funktor` | `fungtor` | Retain the O013-coordinated form; the older witness spelling was already registered as a variant. |
| direct sum / decomposition | `jumlah langsung` / `dekomposisi jumlah langsung` | same | Exact match and especially relevant to Unit 025; no change. |
| indecomposable object | `objek tak terurai` | `tak terdekomposisi` | Retain the concise current form; the literal witness form remains a registered variant. |
| ring / projective module / exact sequence | `gelanggang` / `modul projektif` / `barisan eksak` | same | Exact matches; no change. |
| exact triangle | no current equivalence to `distinguished triangle` | `segitiga eksak` | Do not merge with `segitiga terbedakan`: the witness wording is evidence of local usage, not proof that the two notions are interchangeable. |
| Snake Lemma | `Lema Ular` | `Lema Ular` | Exact match; no change. |

The comparison therefore requires glossary refinement, not a bulk terminology
replacement. The preferred terms already used in Units 001--024 remain
mathematically sound and internally consistent. No translated prose needs
propagation. The glossary variants and notes are updated so later source units
can recognize the attested field forms without silently conflating distinct
concepts.

## Provenance and credit

The Indonesian translation, terminology reconciliation, metadata, modular
backend, and QA were produced with **OpenAI Codex gpt-5.6-sol, Ultra**, at
the user's direction. This model note does not alter authorship or rights: Wen-Wei
Li remains the author of the source work; Gustina Elfiyanti and Ryan Kasyfil
Aziz remain the authors of the terminology witnesses; their supervisors and
institutional records remain credited above; and the user remains the directing
human contributor. Neither the source author, the witness authors, their
institutions, nor Higher Education Press endorses this independent edition.

