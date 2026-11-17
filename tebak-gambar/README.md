# tebak-gambar

Gambar untuk game Tebak Gambar bot Vanillate.ID. Repo ini PUBLIK, jadi **jangan menaruh
jawaban atau nama yang membocorkan jawaban di sini**. Pasangan gambar dan jawaban ada di
`content/tebakgambar.json` repo bot. Rancangan: `docs/tebak-gambar.md` di repo bot.

## Aturan berkas

- Nama acak 6 karakter huruf kecil dan angka: `k7q2m9-1.webp`, `k7q2m9-2.webp`, `k7q2m9-3.webp`.
- Tiga varian per soal: `-1` buram berat, `-2` buram ringan atau terpotong, `-3` jelas.
- WebP, sisi terpanjang 640 px, 40 sampai 100 KB (maks. 150 KB).
- Hanya gambar milik sendiri atau bebas hak cipta, tanpa wajah orang nyata yang dikenali, tanpa konten dewasa.

## Rilis

Setiap penambahan soal diberi TAG git baru (`tg-v1`, `tg-v2`, ...). Bot memakai URL
`https://cdn.jsdelivr.net/gh/Ndyspleasure/database-media-web@<tag>/tebak-gambar/<berkas>`.
Jangan memakai `@main` karena cache CDN bisa berubah diam diam. Jangan menghapus atau
mengganti isi berkas pada tag yang sudah dipakai bot; tambah berkas baru saja.
