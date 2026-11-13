# Aturan penamaan media Vanillate Story

Tujuannya: nama berkas di Google Drive **sama persis** dengan nama yang nanti dipakai bot,
jadi tinggal diunggah tanpa diganti nama lagi.

## 1. Pola nama berkas

`<jenis>_<id>.webp`, huruf kecil, hanya `a-z 0-9 _`, tanpa spasi dan tanpa tanda pisah.

| Jenis | Pola | Contoh | ID berasal dari |
|---|---|---|---|
| Latar lokasi | `loc_<id lokasi>.webp` | `loc_warung.webp` | `locations.json` |
| Potret NPC | `npc_<npcId>.webp` | `npc_alya.webp` | `npcs.json` (`npcId`) |
| Adegan cerita | `scene_<id adegan>.webp` | `scene_b1_01.webp` | naskah `content/story/*.json` |
| Halaman pembuka | `page_00_<slug>.webp` | `page_00_kedatangan.webp` | `story-pages.json` |
| Peta dan banner | `map_…` / `banner_…` | `map_vanillate_city.webp` | manual |

Variasi ekspresi (opsional, nanti): tambahkan akhiran, mis. `npc_alya_senang.webp`, `npc_alya_sedih.webp`.
Versi ulang (revisi): tambahkan `_v2`, mis. `scene_b1_01_v2.webp`. Jangan menimpa berkas yang sudah dipakai bot.

## 2. Struktur folder di Google Drive

```
Vanillate Story/
  01_Lokasi/            (39 berkas, loc_*.webp)
  02_Potret_NPC/        (40 berkas, npc_*.webp)
  03_Adegan_Cerita/     (65 berkas, scene_*.webp)
  04_Halaman_Pembuka/   (7 berkas, page_*.webp)
  05_Peta_Banner/       (2 berkas, map_*.webp dan banner_*.webp)
  _asli_png/            (hasil mentah dari ChatGPT sebelum dikonversi, opsional)
```

Awalan angka pada nama folder hanya untuk mengurutkan di Drive. Nama berkas tidak memakai angka.

## 3. Ukuran dan format

ChatGPT hanya menghasilkan rasio 1:1, 3:2 (1536x1024), dan 2:3 (1024x1536). Prompt sudah meminta semua subjek penting
berada di bagian tengah, jadi hasilnya tinggal **dipotong** ke ukuran akhir.

| Jenis | Minta di ChatGPT | Potong ke (akhir) | Berat |
|---|---|---|---|
| Lokasi, adegan, halaman pembuka | 3:2 (1536x1024) | 16:9, lalu perkecil ke 1280x720 | di bawah 300 KB |
| Potret NPC | 2:3 (1024x1536) | 3:4, lalu perkecil ke 768x1024 | di bawah 250 KB |
| Peta dan banner | 3:2 (1536x1024) | peta: pita tengah 8:3 (1920x720 setelah diperbesar), banner: 16:9 | di bawah 500 KB |

ChatGPT menghasilkan PNG. Ubah ke WebP (kualitas 80) lalu cek ukurannya, mis. dengan `cwebp -q 80 in.png -o out.webp`
atau situs konversi. Simpan PNG asli di `_asli_png/` dengan nama yang sama.

## 4. Alur kerja per gambar

1. Buka `manifest.csv` (bisa diimpor ke Google Sheets) atau berkas `.txt` di folder `prompts/`.
2. Salin teks di antara `===== TEMPEL KE CHATGPT =====` dan `===== SELESAI =====`.
3. Tempel ke ChatGPT, lalu atur ukuran sesuai baris `BUAT DI GPT` (atau tulis "buat dalam rasio 3:2"). Untuk konsistensi gaya,
   lampirkan 3 gambar acuan gaya (peta pixel, potret, adegan) yang sudah kamu setujui dan tulis "ikuti gaya gambar terlampir persis".
4. Pilih hasil terbaik, ubah ke WebP, **beri nama persis seperti `NAMA BERKAS`** di berkas prompt.
5. Unggah ke folder Drive yang tertulis di baris `NAMA BERKAS`.
6. Centang di Sheets (kolom `status`) supaya tidak dobel.

## 5. Catatan konsistensi

- Kerjakan per kategori: semua lokasi dahulu, lalu potret, lalu adegan.
- Pakai **satu percakapan ChatGPT per kategori** supaya gayanya tetap sama. Percakapan yang terlalu panjang bisa melenceng,
  jadi buka percakapan baru tiap sekitar 15 gambar dan lampirkan lagi gambar acuan gayanya.
- Kalau wajah tokoh berubah, minta "ubah gambar ini, pertahankan wajah dan pakaian tokoh seperti gambar terlampir".
- ChatGPT bisa memolakan tulisan di gambar. Prompt sudah melarang teks, tapi kalau muncul, minta "hapus semua tulisan".
- Potret NPC dibuat **sebelum** adegan. Lampirkan potretnya saat membuat adegan yang memuat tokoh itu agar wajah konsisten.
- Tokoh pemain tidak pernah digambar dari depan (jenis kelamin bebas). Prompt sudah menetapkannya.
- Jenis kelamin dan usia NPC adalah **asumsi** dari gelar dan peran di naskah. Ubah bagian deskripsi di `.txt` bila berbeda dari maksudmu.
- Semua tokoh dewasa kecuali tiga murid SD, dan tidak ada pakaian atau pose yang seksual.
- Tanpa logo atau merek nyata. Referensi gaya hanya acuan visual.
