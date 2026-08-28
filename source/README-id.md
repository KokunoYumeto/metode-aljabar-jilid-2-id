> **Catatan penerjemah:** Ini adalah terjemahan id-ID dari README sumber beku pada commit `9a5803ff77dd3257484cb177f851a73770a59dd3`. Provenans model: `OpenAI Codex gpt-5.6-sol, Ultra`.

Ini adalah sumber LaTeX untuk buku teks **Methods of Algebra** (dalam bahasa Tionghoa: 代数学方法), Jilid 2.

Buku ini mula-mula diterbitkan pada tahun 2024 oleh Higher Education Press (Beijing), ISBN 978-7-04-062754-1.

Versi PDF dan daftar ralat tersedia di laman penulis. Kesalahan yang ditemukan akan diperbaiki dalam revisi berikutnya.

Berkas-berkas ini diharapkan dapat membantu para dosen, mahasiswa, serta peminat yang ingin menulis buku matematika atau fisika berbahasa Tionghoa secara serius tanpa terlalu banyak kerepotan TeXnis.

# Cara mengompilasi

## Persyaratan sistem
Berkas-berkas ini harus dikompilasi menggunakan XeLaTeX dengan paket xeCJK. Petunjuk berikut mengasumsikan lingkungan UN*X.

Petunjuk berikut dapat disesuaikan untuk Windows, tetapi cara ini tidak dianjurkan. Pilihan termudah ialah beralih ke sistem sumber terbuka.

Kita hanya memerlukan paket dan fon standar, seperti
- [TeX Live](https://tug.org/texlive), termasuk program latexmk, xindy, dan biber.
- Fon standar yang disertakan dalam TeX Live, khususnya fon Fandol. Entah mengapa, saya menggunakan dan memasang fon TeX Gyre Heros pada sistem. Jika muncul pesan galat yang berkaitan dengan fon ini, carilah berkas OTF dalam direktori fon TeX yang namanya diawali dengan **texgyreheros**, lalu pasang berkas-berkas tersebut secara manual pada sistem Anda.
- Fon **Noto Sans CJK SC** dari [Noto CJK](https://github.com/googlei18n/noto-cjk), yang juga harus dipasang untuk seluruh sistem.

Pastikan semua paket/program yang relevan telah terpasang. Sebagai rujukan, penulis melakukan kompilasi menggunakan distribusi Linux berbasis Arch dengan TeX Live 2024; paket **biber** dan **texlive-science** diperlukan.

## Mengkloning berkas
Pastikan [Git](https://git-scm.com/) telah terpasang pada komputer Anda. Untuk menyiapkan proses kompilasi, klon repositori ke `~/AlJabr-2` di dalam direktori home. Pada baris perintah, ketik
```
cd ~
git clone https://github.com/wenweili/AlJabr-2
```

Semua berkas sumber menggunakan pengodean UTF-8, yang merupakan standar de facto untuk menyimpan teks multibahasa. Jika Anda mengalami masalah saat membuka berkas sumber di Windows, cobalah mengonfigurasi ulang editor Anda atau mengonversi pengodeannya secara manual.

## Mengompilasi sumber TeX

Masuk ke direktori
```
cd ~/AlJabr-2
```
Kemudian, ketik
```
latexmk -pdf -pdflatex="xelatex -shell-escape -interaction=nonstopmode %O %S" Al-jabr-2
```
atau, secara lebih sederhana,
```
make
```

Nikmati secangkir kopi karena proses ini akan memakan waktu beberapa menit. Berkas PDF yang dihasilkan seharusnya muncul sebagai **Al-jabr-2.pdf** dalam direktori yang sama. Perhatikan bahwa berkas utamanya ialah **Al-jabr-2.tex**.

Untuk membersihkan direktori kerja dari semua berkas hasil kompilasi selain PDF, ketik
```
make clean
```

# Kelas dokumen AJbook
Buku ini ditulis menggunakan kelas **AJbook2** (AJbook2.cls). Ini merupakan kelas dokumen serbaguna yang dikembangkan dari pendahulunya, AJbook.cls, yang digunakan untuk Jilid 1. Contoh penggunaan dasarnya tersedia dalam Template-AJbook.tex; ketik
```
latexmk -pdf -pdflatex="xelatex -shell-escape -interaction=nonstopmode %O %S" Template-AJbook
```
atau, secara lebih sederhana,
```
make template
```
untuk mengompilasi templat tersebut.

Fon dan unsur tampilan lainnya dapat disesuaikan melalui beberapa berkas konfigurasi; bacalah berkas-berkas sumber dengan saksama untuk keterangan lebih lanjut. Berkas Template-AJbook.tex mengikuti konfigurasi asli buku ini.

# Daftar ralat
Daftar ralat dihasilkan dari **Errata-Al-jabr-2.tex**, yang didasarkan pada berkas kelas dokumen yang sangat sederhana, **AJerrata.cls**. Selain fon standar yang dibundel bersama TeX, berkas ini juga bergantung pada **Noto Serif CJK SC** dan **Noto Sans CJK SC**; Anda dapat memasangnya dari [fon Noto CJK](https://github.com/googlei18n/noto-cjk).

Untuk mengompilasi daftar ralat, ketik
```
xelatex Errata-Al-jabr-2
```
atau
```
make errata
```
dalam direktori yang sama.

# Umpan balik
Jika Anda mengalami masalah kompilasi, mohon laporkan kepada penulis. Pastikan semua persyaratan sistem di atas telah dipenuhi dan sertakan pesan galat yang terperinci. Saran lainnya juga diterima dengan senang hati.

# Lisensi
Seluruh basis kode dilisensikan berdasarkan [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

# Riwayat Star

[![Bagan Riwayat Star](https://api.star-history.com/svg?repos=wenweili/AlJabr-2&type=Date)](https://star-history.com/#wenweili/AlJabr-2&Date)
