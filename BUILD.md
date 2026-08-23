# Reproducible PDF build

## Toolchain baseline

The admitted Unit 029 artifact was built on Windows with XeLaTeX, Biber 2.21,
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

Expected admitted boundary: 175 pages, 902,840 bytes, SHA-256
`bfda39c9f834643f024dd2c7d9c16e341c8736b40f3bfa6dcc9d1646b6d6bd25`.
Toolchain and platform metadata can change PDF bytes even when the mathematical
content is unchanged; compare the build log, page count, links, fonts, and
rendered pages as well as the byte hash. A clean replay may differ in raw PDF
bytes because of platform job-name and metadata variation; it must still match
the admitted page count, links, fonts, and visual checks.

The full build and visual-QA receipt is
[`provenance/UNIT_029_QA.md`](provenance/UNIT_029_QA.md).
