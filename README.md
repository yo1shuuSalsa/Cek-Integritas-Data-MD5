# Program Pengecek Integritas Data Profil (MD5)

[cite_start]Tugas mata kuliah Keamanan Jaringan untuk **Mahasiswa No Urut 16-Selesai**.

## Deskripsi
[cite_start]Program ini mensimulasikan bagaimana **Admin** dapat mengetahui apakah data profil user (Nama, Email, HP) pernah dimodifikasi atau tidak. 
[cite_start]Kami menggunakan algoritma **MD5** untuk membuat *checksum*[cite: 22, 105]. [cite_start]Jika ada satu karakter saja yang berubah, nilai hash MD5 (32 karakter hexadecimal) akan berubah total.

## Cara Kerja
1. [cite_start]Input data profil awal.
2. [cite_start]Sistem men-generate dan menyimpan hash MD5 awal.
3. [cite_start]Input data baru untuk perbandingan.
4. [cite_start]Sistem membandingkan hash lama vs hash baru dan menampilkan status perubahan.
