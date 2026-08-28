# Rights and component disposition

## Governing license

The repository README declares the entire codebase licensed under Creative
Commons Attribution 4.0 International. The root license, main source, chapter
and appendix headers, classes, styles, configurations, cover, template, and
errata carry matching CC BY 4.0 notices. Translation, modification,
redistribution, and commercial publication are permitted.

Every public derivative must retain creator attribution, identify the pinned
source, link or reproduce the CC BY 4.0 license, and clearly mark translation
and other changes. Neither Wen-Wei Li nor Higher Education Press may be
presented as endorsing this independent Indonesian edition.

## Component table

| Component | Role | Rights/disposition |
|---|---|---|
| `Al-jabr-2.tex`, `prelude.tex`, chapters, appendices | authored reader source | CC BY 4.0; translate with attribution and modification notice |
| `AJbook2.cls`, `mycommand.sty`, font/title configs | reader build support | CC BY 4.0 headers; retained in editable derivative closure |
| `myarrows.sty` | custom arrow support | Header says CC BY 4.0 and attributes borrowed arrow code to Antal Spector-Zabusky. Both notices are preserved. Unit 011 is the first derivative unit that requires it, for the source-native `\xlongequal` construction. |
| `ccby.png` | license badge | In main upstream closure; retained as frozen support but not rendered by Unit 001 |
| `Lanzhou.png`, `Template-AJbook.*` | separate class template | Not included by the main book and excluded from the Indonesian reader closure |
| Noto/Fandol/TeX Gyre fonts | external build dependencies | Not source-repository content. Do not redistribute standalone font files here; embedded PDF subsets remain subject to their font licenses. |
| TeX packages/toolchain | external build dependencies | Not relicensed by this project; retain their own licenses |
| Indonesian translation, metadata, stable-ID exports | derivative/new material | Released under CC BY 4.0 with the upstream work; changes are explicitly identified |

Mathematical facts and stable concept identifiers are not asserted as
copyrightable expression. Whenever wording or diagrams are adapted, the
upstream CC BY attribution remains attached at the smallest practical unit.

## Production provenance

The Indonesian translation, terminology work, metadata, modular backend, and
QA were produced with **OpenAI Codex gpt-5.6-sol, Ultra**, at the user's
direction. This disclosure does not replace or diminish Wen-Wei Li's source
authorship, the user's human direction, or any component-specific credit above.
