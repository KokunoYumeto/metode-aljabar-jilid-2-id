# Metode dalam Aljabar, Jilid 2 — Bahasa Indonesia

Edisi Bahasa Indonesia independen dari *Methods of Algebra, Volume 2: Linear
Algebra* karya Wen-Wei Li. Repositori ini menyediakan pembaca PDF, sumber
XeLaTeX yang dapat disunting, dan ekspor semantik ber-ID stabil.

[Baca PDF kumulatif saat ini](artifacts/metode-dalam-aljabar-jilid-2-id-cumulative.pdf)

## Status

Ini adalah **edisi kerja parsial**, bukan terjemahan lengkap. Batas publik ini
mencakup Unit 001–039: seluruh Pendahuluan, seluruh Bab 1, seluruh Bab 2,
serta Bab 3 sampai Bagian 3.8 (`chapter3.tex` upstream baris 9–1586). Pembaca
saat ini berjumlah 243 halaman. Produksi berikutnya dimulai pada `chapter3.tex`
baris 1587, bagian funktor pemenggalan (`sec:truncation-functors`), dan
berlanjut dalam urutan sumber menuju keseluruhan buku resmi 650 halaman.

PDF memiliki teks yang dapat dipilih, daftar isi, markah, dan pranala internal
yang telah diperiksa, tetapi **belum merupakan PDF bertag** dan tidak diklaim
sepenuhnya aksesibel. Pembaca HTML semantik/offline masih dalam pengembangan.

## Otoritas sumber

- Karya: Wen-Wei Li, *Methods of Algebra, Volume 2: Linear Algebra*.
- Repositori utama penulis: <https://gitee.com/wen-wei-li/AlJabr-2>.
- Cermin resmi: <https://github.com/wenweili/AlJabr-2>.
- Edisi daring yang dibekukan: branch `master`, commit
  `9a5803ff77dd3257484cb177f851a73770a59dd3`, tree
  `23bd05c2fb8434278df4fdfb636559a6a2b0d2ff`.
- Lisensi sumber dan turunan ini: [CC BY 4.0](LICENSE).

Terjemahan dan perubahan penyajian ditandai sebagai karya turunan. Wen-Wei Li
dan Higher Education Press tidak mendukung atau mengesahkan edisi independen
ini. Rincian otoritas, komponen, dan perubahan tersedia di
[`provenance/`](provenance/).

## Isi repositori

- `artifacts/`: PDF pembaca terbaik pada batas publik saat ini.
- `source/`: penutup kumulatif, 39 unit terjemahan, bibliografi, kelas, gaya,
  konfigurasi font/judul, dan aset lisensi yang diperlukan untuk membangun PDF.
- `backend/`: 39 unit, 2.044 segmen, dan 448 istilah dalam bentuk modular
  (`JSONL`/`CSV`).
- `provenance/`: pembekuan sumber, hak komponen, koreksi, terminologi, baseline
  build, audit terminologi Indonesia, QA Unit 039, serta manifes.

Lihat [BUILD.md](BUILD.md) untuk cara membangun ulang. `MANIFEST.csv` dan
`SHA256SUMS.txt` mencatat ukuran dan SHA-256 setiap berkas publik.

## Kredit

Teks, matematika, struktur, notasi, sitasi, dan diagram sumber: Wen-Wei Li.
Terjemahan Bahasa Indonesia, metadata, dan backend: Codex, atas instruksi
pengguna. Semua perubahan dirilis di bawah CC BY 4.0 dengan atribusi kepada
sumber.

Provenans produksi: terjemahan Bahasa Indonesia, rekonsiliasi terminologi,
metadata, backend modular, dan QA diproduksi dengan **OpenAI Codex gpt-5.6-sol, Ultra**,
atas arahan pengguna. Pengungkapan ini tidak menggantikan kredit Wen-Wei Li
sebagai penulis karya sumber atau kredit komponen lain.
