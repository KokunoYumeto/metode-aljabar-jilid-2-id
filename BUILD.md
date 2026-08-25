# Reproducible PDF build

## Toolchain baseline

The admitted Unit 041 artifact was built on Windows with XeLaTeX, Biber 2.21,
and MakeIndex. A complete TeX distribution must provide the packages named by
`source/AJbook2.cls`, `source/mycommand.sty`, `source/myarrows.sty`, and the
wrapper. The portable configuration uses TeX Gyre Heros and the Fandol fonts
distributed with TeX Live/MiKTeX. Shell escape is not required and was disabled.

The author's 650-page reference PDF is the Linux/TeX Live/xindy baseline. The
authoritative source can also produce a valid 653-page Windows/MiKTeX/MakeIndex
fallback. That pagination difference is documented and is not a corpus change.

## PowerShell build

Run from the repository root:

```powershell
New-Item -ItemType Directory -Path build -Force | Out-Null
Push-Location source
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory=../build Al-jabr-2-id-cumulative.tex
Pop-Location

Push-Location build
$oldBibInputs = $env:BIBINPUTS
$env:BIBINPUTS = "../source;"
biber Al-jabr-2-id-cumulative
makeindex Al-jabr-2-id-cumulative.idx
makeindex sym1.idx
Pop-Location

Push-Location source
1..3 | ForEach-Object {
  xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory=../build Al-jabr-2-id-cumulative.tex
}
Pop-Location
$env:BIBINPUTS = $oldBibInputs
```

Expected admitted boundary: 253 pages, 1,255,777 bytes, SHA-256
`f364d2c3b6839a14b89f77313f9e3117dc9b7b5e5ad920d27637924513d5a29f`.
Toolchain and platform metadata can change PDF bytes even when the mathematical
content is unchanged; compare the build log, page count, links, fonts, and
rendered pages as well as the byte hash. A clean replay may differ in raw PDF
bytes because of platform job-name and metadata variation; it must still match
the admitted page count, links, fonts, and visual checks.

The full build and visual-QA receipt is
[`provenance/UNIT_041_QA.md`](provenance/UNIT_041_QA.md).
