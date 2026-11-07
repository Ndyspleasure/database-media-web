# Prompt & panduan pembuatan GIF emoji

Dokumen ini merangkum cara GIF di repo ini dibuat, supaya bisa diulang, diperbaiki, atau ditambah
(oleh manusia maupun oleh Claude di sesi baru). Skrip pembuatnya ada di `tools/`.

## 1. Tujuan

Mengganti emoji unicode yang dipakai bot Discord dengan **emoji animasi (GIF)** yang diunggah ke
**Application Emojis** (Discord Developer Portal → aplikasi → Emojis). Daftar emoji ada di
`tools/emojis.txt` (satu baris per emoji: `emoji nama_file`). Status pengerjaan ada di `CHECKLIST.md`.

## 2. Spesifikasi teknis (wajib)

| Hal | Aturan |
|---|---|
| Ukuran | 128×128 px |
| Latar | transparan |
| Berat file | < 256 KB (hasil saat ini ≤ ~111 KB) |
| Nama | 2–32 karakter, hanya `a-z 0-9 _`, unik per aplikasi |
| Loop | berulang tanpa putus (`loop=0`) |
| Frame | 36 frame × 40 ms (± 1,4 detik) |
| **Frame pertama** | harus **pose penuh** — Discord memakai frame pertama sebagai gambar statis di daftar emoji |

Nama yang lebih dari 32 karakter harus dipersingkat (mis. `serious_face_with_symbols_covering_mouth`
→ `serious_face_symbols_mouth`). Unggahan dengan nama yang sudah ada **ditolak** Discord
("An emoji named … already exists"): hapus yang lama dulu di Portal, atau pakai nama baru.

## 3. Gaya visual

- Flat/geometris, warna cerah dan konsisten, outline tipis lebih gelap dari warna isi.
- Satu objek utama di tengah kanvas, kontras baik di tema gelap maupun terang.
- Dirender 4× (512 px) lalu diperkecil ke 128 px agar halus; palet GIF 255 warna + 1 indeks transparan.
- Ikon sederhana (simbol, benda) paling bagus; tangan/orang paling lemah — itu keterbatasan gaya geometris.

## 4. Prinsip animasi (versi 2)

Animasi jangan sekadar menggoyang gambar yang sama. Setiap emoji punya "busur cerita":

1. **Intro** — muncul dengan efek pop memantul (overshoot + squash/stretch).
2. **Aksi utama** — gerak yang bermakna untuk objeknya (palu memukul, kunci inggris memutar baut,
   gigi saling berputar, kertas suara masuk kotak, pena menulis, dst.).
3. **Outro** — mengecil, lalu loop.

Gerak generik berbasis fisika (di `tools/motion.py`): `m_hop` (lompat + gepeng saat mendarat),
`m_jelly` (bergetar seperti agar-agar), `m_spiny` (membalik), `m_swing` (bandul dengan pivot),
`m_tada`, `m_wave`, `m_alert` (mengocok), `m_spin`, `m_stamp`. Ditambah kilau yang menyapu
(`add_glint`) dan bintang berkelip (`add_spark`).
Emoji yang sudah punya intro sendiri (mis. ✅ yang menggambar centang) masuk daftar `RAW`
agar tidak mendapat pop ganda. Timeline digeser supaya frame pertama = pose penuh.

## 5. Struktur repo

```
gifs/                  hasil GIF (nama file = nama emoji)
tools/emojis.txt       daftar emoji (urutan = nomor di CHECKLIST.md)
tools/common.py        kanvas, helper gambar, easing, penyimpan GIF (save)
tools/icons.py         fungsi gambar tiap emoji: f_xxx(t) -> gambar RGBA, t = 0..1
tools/motion.py        sistem animasi v2 + tabel MAP/CUSTOM/RAW
tools/wave1..8.py      daftar `jobs = [(nama_emoji, fungsi), ...]` per gelombang
tools/build_all.py     bangun ulang semua / sebagian GIF
tools/update_checklist.py   perbarui CHECKLIST.md
tools/preview.py       contact sheet semua GIF -> preview.png
```

## 6. Perintah

```bash
pip install pillow                      # satu-satunya dependensi (font DejaVu Sans Bold dipakai untuk teks)
python3 tools/build_all.py              # bangun ulang SEMUA GIF (± 6 menit)
python3 tools/build_all.py fire check   # hanya emoji tertentu
python3 tools/update_checklist.py       # perbarui CHECKLIST.md
python3 tools/preview.py                # buat preview.png
```

## 7. Menambah emoji baru

1. Tambah baris `emoji nama_file` di `tools/emojis.txt` (nama ≤ 32 karakter, unik).
2. Tulis fungsi `f_nama(t)` di `tools/icons.py` (gambar di kanvas via helper `layer()`, `rr`, `ell`, `poly`,
   `thick_line`, dst.; `t` berjalan 0..1 dan harus berulang mulus). **Jangan memakai nama fungsi yang sudah ada.**
3. Daftarkan di wave baru (`tools/waveN.py`, salin pola wave8) dan tambah `N` ke `range(1, N+1)` di `build_all.py`.
4. Opsional: beri gerak khas lewat `MAP`/`CUSTOM` di `tools/motion.py`.
5. Jalankan `python3 tools/build_all.py nama_file`, lihat hasilnya, lalu `python3 tools/update_checklist.py`.

## 8. Jebakan yang pernah terjadi

- **Nama variabel menimpa konstanta/fungsi** (`W` putih, `txt()` penggambar teks) oleh skrip wave →
  gambar rusak. Pakai nama unik; `build_all.py` sudah mengamankan konstanta dasar.
- **Nama fungsi ganda** di `icons.py` saling menimpa (mis. `f_cross`, `f_bars`, `f_label`). Cek duplikat
  sebelum commit.
- **Frame pertama kecil** (karena intro pop) membuat pratinjau Discord tampak kosong → timeline digeser.
- Pillow menggabungkan frame yang identik, jadi jumlah frame di file bisa < 36; durasi total tetap sama.

## 9. Contoh prompt untuk Claude (sesi baru)

> Repo ini berisi generator GIF emoji animasi untuk Discord Application Emojis. Baca `PROMPT.md` dan
> `tools/`. Tambahkan GIF untuk emoji berikut: `<emoji> <nama_maks_32_karakter>`, ….
> Ikuti spesifikasi (128×128, transparan, < 256 KB, 36 frame, frame pertama pose penuh) dan prinsip
> animasi v2 (pop intro, aksi khas yang bermakna, outro). Perbarui `CHECKLIST.md`, lalu commit dan push.
> Tunjukkan potongan frame sebagai bukti hasilnya.

Prompt untuk memperbaiki animasi tertentu:

> Animasi `<nama>` hanya bergerak-gerak. Buat aksi khas yang sesuai maknanya (bukan sekadar goyang), pakai
> sistem di `tools/motion.py`, bangun ulang hanya GIF itu, dan tunjukkan potongan framenya.

## 10. Emoji streak per tier (`streak_amber` … `streak_eternal`)

Enam api untuk tier Streak Harian Vanillate.ID (hari 1-6 Amber, 7-29 Crimson, 30-89 Emerald, 90-179 Azure,
180-364 Phantom, 365+ Eternal). Fungsinya `f_streak_*` di akhir `tools/icons.py`, didaftarkan di `tools/wave9.py`.

- **60 frame × 40 ms** (2,4 detik), bukan 36 frame, supaya orbit dan kilatan terasa natural. Diatur lewat
  `STREAK_SAVE` di `build_all.py` (`save(nama, fn, 60, 40, True)`). Tanpa intro pop (loop sudah lengkap).
- **Alpha dither** (`save(..., dither=True)`): GIF hanya punya transparansi 1 bit, jadi glow lembut dibuat dengan
  ordered dither supaya tidak jadi cakram solid. Berat file jauh lebih kecil dibanding glow penuh, tapi tetap
  diukur: semua < 256.000 byte (169-223 KB). Bila menambah efek, cek ukuran lagi.
- Loop mulus: semua gerak memakai frekuensi bilangan bulat terhadap `t`; "acak" (partikel, kilat) deterministik
  lewat `_hs()`, tidak memakai `random`.
- **Api hidup, bukan gambar diam:** `_fire()`/`_tongue()` menggambar api dari beberapa lidah dengan tepi halus (tanpa gerigi,
  supaya terbaca api, bukan kristal): dasar bulat lebar, mengecil cekung ke ujung yang melengkung, ujung berkedip,
  bergoyang, meliuk, dan berdenyut dengan fase berbeda. Tier dibedakan oleh warna, tinggi, jumlah lidah, kecepatan kedip,
  dan efek sekeliling (bukan bentuk geometris aneh).
- Setiap tier punya identitas: Amber bara+percikan, Crimson asap+kilatan merah, Emerald aura+kristal,
  Azure listrik+cincin energi, Phantom dua orbit+kristal+bintang, Eternal mahkota cahaya+orbit emas+ledakan bintang.
