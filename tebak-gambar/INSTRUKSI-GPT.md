# Panduan agen: membuat gambar Tebak Gambar

Catatan serah terima untuk agen (GPT, Codex, atau Claude) yang membuat gambar game **Tebak Gambar** bot Vanillate.ID. Baca juga `tebak-gambar/README.md` (aturan berkas dan rilis) dan `gpt.md` (alur umum membuat dan mengunggah gambar di repo ini).

## Tujuan

150 gambar, satu per nomor 001 sampai 150. Pemain menebak apa isi gambar yang mula-mula diburamkan. Jawaban tiap nomor TIDAK ada di repo ini dan jangan ditanyakan ke pengguna; tugasmu hanya menggambar subjeknya.

## Gaya (wajib sama untuk semua gambar)

- Ilustrasi digital datar (flat illustration) yang bersih, garis tepi tipis, warna cerah dan jenuh, bayangan lembut sederhana.
- SATU subjek utama di tengah, memenuhi sekitar 70 persen bingkai, latar polos atau gradasi lembut satu warna.
- Format lanskap, rasio sekitar 4:3.
- DILARANG: teks, huruf, angka, tanda air, logo atau merek, orang nyata atau wajah yang dikenali, konten dewasa atau menakutkan, dan objek tambahan yang membocorkan jawaban (papan nama, label).
- Subjek bangunan atau tempat harus khas dan mudah dikenali, tidak perlu persis.

## Alur

1. Ambil subjek tiap nomor dari daftar di bawah. Buat SATU gambar per nomor dengan alat image generation.
2. LIHAT hasilnya. Ulangi bila ada tulisan atau huruf di gambar, ada lebih dari satu subjek, subjek tidak jelas, atau gayanya berbeda dari yang lain. Kirim ulang blok gaya di atas tiap sekitar 25 gambar supaya gaya tidak melenceng.
3. Simpan lokal sebagai `001.png` sampai `150.png` (nama = nomor, jangan memakai nama subjek). Jangan mengunggah PNG sumber ke repo.
4. Jalankan `python3 tools/tebakgambar_build.py <folder-png> --out tebak-gambar --map <jalur-di-luar-repo>/tebakgambar-map.local.json`. Alat ini membuat 3 WebP per gambar (`<id>-1.webp` buram berat, `-2.webp` buram ringan, `-3.webp` jelas) dengan id acak, dan menulis pemetaan nomor ke id.
5. Unggah HANYA berkas `tebak-gambar/*.webp` ke `main`, bertahap (mis. 10 gambar per commit). Jangan menimpa berkas yang sudah ada.
6. **JANGAN mengunggah `tebakgambar-map.local.json`** dan jangan menempelkan isinya di komentar atau issue publik. Berkas itu menghubungkan id ke nomor, dan itulah yang membuka jawaban. Serahkan kepada pengguna lewat chat pribadi.
7. Laporkan ke pengguna: jumlah gambar jadi, nomor yang gagal atau diulang, dan serahkan berkas pemetaan.

Pemberian tag rilis (`tg-v1`) dan penulisan jawaban dilakukan pengguna atau agen bot, bukan di sini.

## Daftar subjek

Nomor ini hanya urutan kerja. Urutan di repo bot diatur terpisah.

```
001: seekor kucing duduk
002: seekor anjing berdiri
003: seekor gajah dengan belalai terangkat
004: seekor jerapah berleher panjang
005: seekor singa jantan berambut lebat
006: seekor ikan berenang
007: seekor burung kecil hinggap di ranting
008: kupu-kupu bersayap lebar
009: seekor sapi berdiri di padang rumput
010: seekor ayam jago
011: seekor bebek di air
012: seekor kelinci bertelinga panjang
013: sebuah apel merah
014: setandan pisang
015: sebuah jeruk bulat
016: irisan semangka
017: sebuah nanas utuh
018: sebuah buah mangga
019: sebuah tomat merah
020: sebatang wortel
021: pizza dengan keju meleleh
022: hamburger bersusun
023: es krim cone dua scoop
024: kue ulang tahun dengan lilin
025: sepiring nasi goreng dengan telur mata sapi
026: rumah sederhana beratap segitiga
027: mobil keluarga
028: sepeda dengan dua roda
029: pesawat terbang di langit
030: kapal besar di laut
031: kereta api di rel
032: bus kota
033: matahari bersinar
034: bulan purnama di malam hari
035: langit malam penuh bintang
036: pelangi di atas bukit
037: awan putih di langit biru
038: hujan turun dari awan gelap
039: pohon besar berdaun lebat
040: setangkai bunga mekar
041: gunung menjulang
042: pantai berpasir dengan ombak
043: payung terbuka
044: kursi kayu
045: meja makan kayu
046: tempat tidur dengan bantal
047: jam dinding bulat
048: sebuah kunci logam lama
049: buku tebal terbuka
050: sepasang sepatu olahraga
051: kura-kura dengan tempurung bermotif
052: penguin berdiri di es
053: flamingo merah muda berdiri satu kaki
054: kuda nil muncul dari air
055: bunglon di dahan
056: kepiting merah dengan capit
057: ubur-ubur bercahaya di laut
058: gurita dengan delapan tentakel
059: burung hantu bermata besar
060: lebah di bunga
061: sate ayam dengan bumbu kacang
062: semangkuk soto ayam
063: sepiring rendang daging
064: semangkuk bakso
065: martabak manis dipotong
066: segelas es cendol
067: klepon bertabur kelapa parut
068: secangkir kopi panas beruap
069: kamera foto klasik
070: teleskop di tripod
071: kompas navigasi
072: jam pasir
073: gitar akustik
074: piano klasik
075: set drum
076: biola dengan busur
077: angklung bambu
078: wayang kulit bayangan
079: becak di jalan
080: delman ditarik kuda
081: perahu layar di laut
082: mercusuar di tepi karang
083: jembatan gantung
084: menara tinggi
085: tenda kemah di hutan
086: api unggun di malam hari
087: kincir angin di padang
088: candi bertingkat bergaya Borobudur
089: tugu tinggi dengan api emas di puncak
090: rumah adat bertanduk atap melengkung
091: komodo besar
092: orangutan bergelantung
093: harimau belang
094: badak bercula
095: beruang coklat
096: kangguru membawa anak di kantong
097: paus melompat dari air
098: hiu dengan sirip menonjol
099: tupai memegang kacang
100: unta berpunuk di gurun
101: axolotl dengan insang berumbai
102: trenggiling bersisik menggulung
103: tapir berbelalai pendek
104: dugong di dasar laut
105: babirusa bertaring melengkung
106: musang berbulu belang
107: kuskus bermata bulat di dahan
108: burung cenderawasih berbulu indah
109: kasuari berjambul
110: bunga raksasa berbintik merah
111: papeda dengan kuah ikan kuning
112: semangkuk rawon hitam
113: pempek dengan cuko
114: gethuk berwarna warni
115: kue lumpur hangat
116: dodol dibungkus
117: potongan tempe
118: tape singkong dalam daun
119: menara jam besar dengan atap khas
120: gedung dengan tusuk sate di atap
121: candi menjulang runcing bergaya Prambanan
122: topeng reog dengan bulu merak besar
123: rumah joglo beratap tumpang
124: tugu putih dengan puncak runcing
125: kapal pinisi berlayar tinggi
126: sekstan navigasi
127: stetoskop dokter
128: mikroskop laboratorium
129: kincir air dari kayu
130: gramofon dengan corong
131: mesin ketik antik
132: lentera minyak tua
133: astrolab kuningan
134: obeng dengan gagang kuning
135: tang logam
136: gergaji tangan
137: palu dengan gagang kayu
138: kunci inggris
139: sikat gigi
140: gunting logam
141: peniti
142: gerhana matahari total dengan korona
143: cahaya aurora di langit kutub
144: tornado di dataran
145: terumbu karang warna warni
146: stalaktit di dalam gua
147: geyser menyembur
148: air terjun bertingkat
149: danau di antara gunung
150: bekantan berhidung panjang
```
