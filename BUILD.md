# Reproducible builds

## PDF

Master edisi lengkap ialah
`source/Al-jabr-2-id-complete-draft.tex`. Walaupun nama berkas tersebut
mempertahankan nama kerja produksi, isi yang dirilis mencakup seluruh 146 unit
dan judul publiknya tetap *Metode dalam Aljabar, Jilid 2: Aljabar Linear —
Edisi Bahasa Indonesia*.

Distribusi TeX lengkap harus menyediakan XeLaTeX, Biber, SplitIndex,
MakeIndex/xindy, serta paket yang diminta oleh `AJbook2.cls`, `mycommand.sty`,
dan `myarrows.sty`. Fon portabel menggunakan TeX Gyre Heros dan fon Fandol yang
tersedia dalam TeX Live/MiKTeX. Shell escape tidak diperlukan.

Contoh alur Windows/MiKTeX dengan MakeIndex sebagai fallback:

```powershell
New-Item -ItemType Directory -Path build -Force | Out-Null
Push-Location source
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape `
  -output-directory=../build Al-jabr-2-id-complete-draft.tex
Pop-Location

Push-Location build
$oldBibInputs = $env:BIBINPUTS
$env:BIBINPUTS = "../source;"
biber Al-jabr-2-id-complete-draft
splitindex Al-jabr-2-id-complete-draft.idx
Pop-Location

Push-Location source
1..2 | ForEach-Object {
  xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape `
    -output-directory=../build Al-jabr-2-id-complete-draft.tex
}
Pop-Location
$env:BIBINPUTS = $oldBibInputs
```

Pada Linux/TeX Live, gunakan konfigurasi xindy yang tertanam dalam master;
alur penulis (`latexmk`/xindy) tetap menjadi baseline platform sumber.

PDF resmi penulis berjumlah 650 halaman pada Linux/TeX Live/xindy. Sumber yang
sama menghasilkan fallback Windows/MiKTeX/MakeIndex 653 halaman yang sah.
Jumlah halaman edisi Bahasa Indonesia tidak diharapkan sama karena perbedaan
bahasa, pelokalan, dan materi jembatan independen. Perbandingan build harus
mencakup log, jumlah halaman, fon, pranala, indeks, dan inspeksi visual—bukan
hanya kesamaan byte PDF.

## Pembaca HTML offline

Sumber pembangunan berada di `reader-source/`. Jalankan
`reader-source/build-reader.ps1` dari salinan repositori lengkap. Hasil build
berada di `reader-source/dist/`; distribusi yang diterima disalin ke `reader/`
dan harus dapat dibuka melalui `reader/index.html` tanpa jaringan. Jangan
menganggap hasil antara dalam direktori build sebagai distribusi yang siap
dirilis.

## Penutupan rilis

Skrip staging di luar repositori menyalin ulang sumber/backend/pembaca dari
lane kanonis. Mode final menolak penutupan jika backend belum memuat 146 unit
atau pembaca offline belum memiliki `index.html`; barulah manifes, checksum,
dan ZIP deterministik dibuat.
