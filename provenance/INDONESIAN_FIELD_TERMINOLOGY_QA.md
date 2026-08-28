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

## Supplemental same-field journal witness at the Unit 031/032 boundary

The arXiv-first search was bounded again before Unit 032 admission. Searches
combining Indonesian category-theory terms such as `kategori`, `funktor`,
`kategori abelian`, `aljabar homologis`, and `kategori monoidal` did not locate
an Indonesian-language same-field arXiv record with downloadable TeX. The result
remains a bounded negative finding, not a proof of absence. The instructed PDF
fallback was therefore applied to an official Indonesian mathematics-journal
source:

Agus Suryanto, Nikken Prima Puspita, and Robertus Heri S. U., “Fungtor
Kontravarian dan Kategori Abelian,” *Jurnal Matematika* 5(2), October 2016,
Jurusan Matematika, Universitas Diponegoro.

- Official article record:
  <https://ejournal3.undip.ac.id/index.php/matematika/article/view/13930>
- Official PDF:
  <https://ejournal3.undip.ac.id/index.php/matematika/article/download/13930/13466>
- Local evidence copy:
  `references/terminology-qa/Suryanto-Puspita-Heri-2016-Fungtor-Kontravarian-dan-Kategori-Abelian.pdf`
- Identity: 9 pages, 429,219 bytes, SHA-256
  `d22cf3c40242359a2d00eb726697e08b6ad29c647a0309cbcd98914484b5f9b6`.
- Layout-preserving extracted text: 15,691 bytes, SHA-256
  `fe8fcf391a4dc16edca2643e96b3a312ed1ecfb5b627c079ef314ddd3f6b8443`.
- All nine pages were rendered with MuPDF and visually inspected; the 3-by-3
  contact sheet is 922,354 bytes, SHA-256
  `1fd4a03e0f49111e8f4fa99991e73e0ff6bb503d5c623d66b4a78bce11976718`.
  Poppler emitted font-substitution warnings because several legacy Microsoft
  fonts are not embedded, so the MuPDF render—not the degraded Poppler render—
  is the visual witness.

The paper repeatedly attests `kategori abelian`, `kernel`, `kokernel`, `produk`,
and `koproduk`, exactly matching this edition. It uses the older spellings
`fungtor`, `obyek`, `morfisma`, and `homomorfisma`; these are useful search and
recognition variants but do not justify replacing the coordinated preferred
forms `funktor`, `objek`, `morfisme`, and `homomorfisme`. The glossary therefore
adds only the missing variants `obyek`, `homomorfisma modul`, `obyek terminal`,
`obyek inisial`, `obyek nol`, and `morfisma nol`. No translated prose or formula
requires propagation. The PDF is retained only as local QA evidence and is not
an edition component or public-release payload.

## Unit 036 arXiv-first reconfirmation and focused term decision

At the safe boundary before admitting Unit 036, the requested arXiv-first check
was repeated specifically for the terminology introduced by the double-complex
section. Exact all-field searches for `"kategori abelian"`, `"aljabar
homologi"`, `"transformasi natural"`, and `"hasil kali tensor"` each returned
zero arXiv records. Related bounded searches for Indonesian category theory,
`bikompleks`, `kompleks ganda`, and a Koszul sign term likewise produced no
Indonesian-language same-field record with a downloadable TeX source package.
There was therefore no source archive to unpack. This remains a bounded
negative result rather than a universal absence claim.

The fallback comparison directly inspected the previously recorded 2020 ITB
U-complex abstract and 2016 UNDIP category-theory paper, plus two official
institutional documents:

- Nikken Prima Puspita, “Pengaruh Kenon-Unitalan Modul terhadap Hasil Kali
  Tensor,” Seminar Nasional Matematika dan Pendidikan Matematika, 2010,
  official UNY record <https://eprints.uny.ac.id/10473/>. The local PDF is
  `references/terminology-qa/Puspita-2010-Pengaruh-Kenon-Unitalan-Modul-terhadap-Hasil-Kali-Tensor.pdf`,
  450,227 bytes, SHA-256
  `767e89f16a31f952ad4a5c3df74f7422f49abf5a4a4af1e1d1506654b0ad02f6`;
  its layout-preserving text witness is 22,175 bytes, SHA-256
  `4b230c6b5f268216231d474a3db69fed2551726760a5f7c1551ab3f4d120d609`.
- FMIPA Universitas Gadjah Mada, *Dokumen Kurikulum 2022 Program Magister*,
  course MMM 6203 “Teori Kategori dan Fungtor,” printed page 106 / PDF page
  122, official PDF
  <https://mkom.ugm.ac.id/wp-content/uploads/sites/690/2026/01/Dokumen-Kurikulum-Progam-Magister-FMIPA-UGM-tahun-2022.pdf>.
  The local PDF is
  `references/terminology-qa/UGM-2022-Dokumen-Kurikulum-Program-Magister-FMIPA.pdf`,
  4,213,305 bytes, SHA-256
  `aab71b299cf141c63069f3b2a061d23be1d6b06abac7c9dd912c321cbe362bc7`;
  the extracted page witness is 2,943 bytes, SHA-256
  `8a6932560f20abd9cbef781f50f729176df7e70ca9651114e5beb5b00d84edc3`.

The four relevant PDF pages were rendered and visually inspected rather than
accepted from search snippets alone. Puspita repeatedly uses `hasil kali
tensor`. The UGM course repeatedly uses `fungtor` and `transformasi natural`.
Suryanto et al. likewise use `fungtor`, while Elfiyanti directly attests
`aljabar homologi`, `rantai kompleks`, `kategori homotopi`, and `kategori
aditif`.

These observations refine evidence notes and variants but do not justify a
corpus-wide preferred-term replacement. This edition retains the coordinated
O013/O014 preferred `funktor` and `transformasi alami`, while registering the
genuinely attested `fungtor` and `transformasi natural`; retains the strongly
attested `hasil kali tensor` and `pelengkapan`; and retains `aljabar homologis`
with `aljabar homologi` as a field-attested variant for grammatical and
cross-corpus consistency. No witness used `bikompleks`, `kompleks ganda`,
`bikompleks Hom`, or either Indonesian form of “Koszul sign rule.” Accordingly,
Unit 036 keeps the transparent provisional forms `bikompleks`, `bikompleks
Hom`, `aturan tanda Koszul`, and `homotopi bikompleks`. The simple component
`homotopi` is strongly attested. No translated Unit 001--036 prose requires a
replacement; the terminology ledger notes were propagated instead.

The new PDFs and text extracts are local QA witnesses only. They are excluded
from edition and public-release payloads because their redistribution rights
were not established. The edition and reader metadata already carry the exact
production identification **OpenAI Codex gpt-5.6-sol, Ultra** while preserving
all source-author and human-contributor credits.

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

