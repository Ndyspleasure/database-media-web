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

## Membuat gambar dengan GPT

Satu gambar per soal, lalu `tools/tebakgambar_build.py` membuat 3 varian petunjuk otomatis.

Prompt dasar (ganti isi dalam kurung):

> Ilustrasi digital bersih dari [OBJEK ATAU TEMPAT], satu subjek utama di tengah, latar sederhana,
> warna jelas, gaya kartun semi-realistis konsisten, tanpa teks, tanpa huruf, tanpa watermark,
> tanpa logo, tanpa orang nyata yang dikenali, rasio 4:3.

Tips: sebut satu subjek saja; minta gaya yang SAMA untuk semua soal supaya tidak ada soal yang
"kelihatan beda"; tolak hasil yang memuat tulisan karena bisa membocorkan jawaban; simpan nama
berkas sumber bebas (mis. `borobudur.png`), nama itu tidak ikut ke repo.

## Membangun berkas

```bash
python3 tools/tebakgambar_build.py <folder-gambar-sumber>
```

- Hasil: `tebak-gambar/<id>-1.webp`, `-2.webp`, `-3.webp` (id acak, 40 sampai 100 KB).
- Pemetaan nama sumber ke id ada di `tebakgambar-map.local.json` (di `.gitignore`, JANGAN di-commit).
- Tulis jawaban tiap id di `content/tebakgambar.json` repo bot, lalu commit, beri tag (`tg-v1`, ...),
  dan perbarui `baseUrl` di repo bot.
