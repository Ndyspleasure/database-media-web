# Panduan agen: ikon tambahan untuk game Tebak Kata

Catatan serah terima untuk agen (GPT, Codex, atau Claude) yang membuat ikon benda untuk game **Tebak Kata** bot Vanillate.ID. Baca juga `tebak-gambar/INSTRUKSI-GPT.md` (alur kerja, gaya, dan cara membangun berkas) dan `gpt.md`.

## Tujuan

Soal Tebak Kata adalah teka-teki kata: beberapa gambar benda, potongan huruf, dan huruf yang diganti digabung menjadi satu kata atau frasa. Pemain mengenali benda di tiap gambar dari NAMA BAKUNYA, jadi gambar harus tidak ambigu. Sudah ada 150 ikon (nomor 001 sampai 150, folder `tebak-gambar/`). Panduan ini menambah **23 ikon** bernomor 151 sampai 173.

## Aturan tambahan khusus ikon

- Gambar hanya boleh bisa disebut SATU kata baku. Bila ragu apakah orang akan menyebut nama lain, gambar ulang dengan bentuk yang lebih khas.
- Satu benda, di tengah, latar polos. Tidak ada benda lain, tidak ada teks, huruf, angka, logo, merek, atau orang.
- Gaya, ukuran, dan format sama persis dengan panduan `tebak-gambar/INSTRUKSI-GPT.md` (ilustrasi datar bersih, warna cerah, lanskap 4:3, kirim ulang blok gaya tiap sekitar 25 gambar).

## Alur

1. Buat SATU gambar per nomor dari daftar di bawah. LIHAT hasilnya, ulangi bila ada teks, benda tambahan, atau benda bisa disebut nama lain.
2. Simpan lokal sebagai `151.png` sampai `173.png` (nama = nomor). Jangan unggah PNG sumber ke repo.
3. Jalankan `python3 tools/tebakgambar_build.py <folder-png> --out tebak-gambar --map <jalur-di-luar-repo>/tebakgambar-map-ikon.local.json`. Alat ini membuat 3 WebP per gambar dengan id acak (`<id>-1.webp` sampai `-3.webp`). Game hanya memakai varian `-3`.
4. Unggah HANYA `tebak-gambar/*.webp` ke `main`, bertahap. Jangan menimpa berkas yang ada.
5. **JANGAN mengunggah berkas pemetaan** (`*.local.json`). Serahkan ke pengguna lewat chat pribadi.
6. Laporkan: jumlah gambar jadi, nomor yang diulang, dan serahkan berkas pemetaan.

## Daftar ikon

Format: `NOMOR: nama baku (gambar yang diminta)`.

```
151: api (nyala api oranye dengan inti kuning, satu lidah api besar, tanpa kayu bakar)
152: air (setetes air biru besar yang jernih dan berkilau)
153: tas (tas tangan wanita coklat dengan tali jinjing)
154: laut (hamparan laut biru dengan ombak dan cakrawala, tanpa pantai, kapal, atau pulau)
155: daun (selembar daun hijau besar dengan tulang daun jelas)
156: akar (akar pohon coklat yang menjalar, tanpa batang dan daun)
157: ular (seekor ular hijau melingkar dengan kepala terangkat)
158: roti (sepotong roti tawar putih berbentuk persegi dengan tepi coklat)
159: naga (naga merah panjang bergaya Tiongkok)
160: madu (toples kaca berisi madu kuning dengan sendok kayu penetes madu, tanpa tulisan)
161: kuda (seekor kuda coklat berdiri menyamping)
162: baju (baju biru berlengan pendek, tampak depan)
163: semut (seekor semut hitam besar dilihat dari samping)
164: sapu (sapu ijuk bergagang kayu)
165: lampu (bohlam lampu menyala kuning)
166: handuk (handuk biru terlipat rapi)
167: cermin (cermin tangan bulat berbingkai emas bergagang)
168: roda (satu roda ban hitam dengan pelek perak, bukan kendaraan utuh)
169: mawar (setangkai mawar merah dengan duri dan daun)
170: jagung (satu tongkol jagung kuning dengan kelobot hijau terbuka)
171: gigi (satu gigi geraham putih bersih, tanpa wajah)
172: cabai (dua cabai merah dengan tangkai hijau)
173: bantal (bantal putih persegi yang empuk)
```
