# Pembaca luring HTML5

Direktori ini membangun master terjemahan lengkap
<code>source/Al-jabr-2-id-complete-draft.tex</code> menjadi HTML5 dengan
matematika TeX yang dibentuk oleh bundel MathJax 3.2.2 lokal menjadi CHTML dan
lapisan semantik untuk teknologi asistif. Hasil berada di <code>reader-source/dist/</code>, dengan
<code>index.html</code> sebagai titik masuk dan seluruh stylesheet serta aset
konversi berada secara lokal di direktori yang sama. Tidak ada CDN atau path
privat; JavaScript yang dipakai hanya bundel MathJax lokal berlisensi Apache 2.0.

Konfigurasi mempertahankan jangkar dan tautan rujukan silang yang dibuat
TeX4ht dari <code>\label</code>/<code>\ref</code>, memakai heading HTML
semantik bawaan TeX4ht, menyediakan daftar isi bertaut, metadata
<code>id-ID</code>, tautan lewati-konten, chrome pembaca berbahasa Indonesia,
tata letak responsif terpusat, serta fokus keyboard yang terlihat.

## Prasyarat

- PowerShell 7.4 atau lebih baru.
- Pandoc dan Python 3 dengan <code>lxml</code>.
- Bundel lokal MathJax 3.2.2 yang sudah disertakan pada
  <code>reader/vendor/mathjax-3.2.2/</code>.

Master meminta program indeks bernama <code>truexindy</code>; MiKTeX
menyediakan <code>texindy</code>. Script menambahkan
<code>reader/tools/truexindy.cmd</code> ke <code>PATH</code> proses build saja
sebagai shim deterministik ke <code>texindy</code>.

Kelas juga memuat <code>pdfpages</code> untuk sampul PDF opsional. Master aktif
memakai sampul TeX, sehingga <code>reader-driver.tex</code> men-stub paket yang
tidak dipakai itu sebelum menginput master lengkap, untuk menghindari konflik
driver XeTeX/DVI milik TeX4ht.

Paket <code>zhlineskip</code> hanya mengatur spasi baris cetak dan tidak
dipanggil oleh unit. Driver men-stubnya karena versi MiKTeX 2026 berkonflik
dengan hook <code>mathtools</code> TeX4ht 2023 di tengah pemuatan
<code>expl3</code>; pengaturan tersebut tidak mempunyai semantik dalam HTML.

Sampul cetak asli memakai gambar TikZ bertumpuk dan tabel tata letak. Pada
TeX4ht, kombinasi itu tidak berhenti menghasilkan halaman saat mencapai tabel
lisensi. Driver karena itu mengarahkan hanya opsi sampul kelas ke
<code>reader-cover.tex</code>, padanan HTML semantik yang mempertahankan judul,
penulis, data edisi, ISBN, laman penulis, dan lisensi. Isi master, diagram
matematis, label, dan urutan bab tidak diganti.

## Build produksi

Dari akar proyek:

~~~powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\reader-source\build-offline-reader.ps1
~~~

Script membaca tepat 148 <code>\input</code> aktif dari master, mengonversi
setiap unit secara paralel dengan pembaca LaTeX Pandoc, mempertahankan sumber
TeX matematika untuk MathJax lokal, menyematkan semua 829 deskripsi diagram
dari ledger, membangun bibliografi, lalu menjalankan satu pemeriksaan
deterministik atas urutan unit, jangkar, fragmen, aset lokal, matematika,
diagram, dan path privat. Manifest <code>SHA256SUMS.txt</code> dibuat di
<code>reader-source/dist/</code>.

Backend TeX4ht yang terdokumentasi pada <code>build-reader.ps1</code> dan
<code>reader-driver.tex</code> dipertahankan sebagai bukti diagnosis, bukan
jalur produksi: implementasi MiKTeX 2026 yang tersedia gagal secara
deterministik pada list/array kelas dan kemudian pada pemindai matematika
multi-kolom. Jalur Pandoc–MathJax menghindari kegagalan tersebut tanpa
mengubah sumber terjemahan.

Pada fallback HTML, diagram TikZ dinyatakan sebagai deskripsi tekstual lengkap
dari ledger dan bukan visual. PDF edisi mempertahankan visual asli; batasan ini
juga dinyatakan pada <code>accessibility.html</code> dan laporan build.

