# Panduan Codex: media gambar Vanillate Story

Dokumen ini adalah catatan serah terima agar Codex pada sesi baru dapat menemukan, **melihat**, membuat, memeriksa, dan mengunggah gambar dengan alur yang sama. Baca dokumen ini bersama prompt masing-masing gambar. Jangan mengandalkan riwayat percakapan, `store()` sesi lama, atau keberadaan file sementara.

## 1. Repository dan status terakhir

- Repository: **`Ndyspleasure/database-media-web`**.
- Cabang hasil yang diminta pengguna: **`main`**. Selalu baca HEAD terbaru sebelum perubahan; jangan menimpa perubahan orang lain.
- Commit terakhir media saat panduan ini ditulis: [`51b8d8266e2b8dbcd7cc39d1c09c818efe81d853`](https://github.com/Ndyspleasure/database-media-web/commit/51b8d8266e2b8dbcd7cc39d1c09c818efe81d853).
- Terverifikasi pada commit tersebut: **39 latar lokasi, 40 potret NPC, dan 65 adegan cerita** sudah berada di repository.
- **65/65 prompt adegan memiliki WebP pasangannya.** Jangan membuat ulang adegan secara otomatis saat pengguna hanya meminta melanjutkan; periksa permintaan dan status terbaru dahulu.
- **7 halaman pembuka dan 2 peta/banner belum memiliki gambar di repository pada pemeriksaan tersebut.** Total 153 prompt bukan berarti 153 gambar telah selesai.
- Pengunggahan sesi ini menuju GitHub, bukan Google Drive. Teks folder Drive pada prompt adalah rencana penamaan, bukan bukti bahwa file sudah diunggah ke Drive.

| Keperluan | Lokasi di repository |
|---|---|
| Daftar seluruh gambar | `story-media/manifest.csv` |
| Gaya induk | `story-media/00_STYLE_PROMPT.md` |
| Ukuran, nama, dan alur awal | `story-media/PENAMAAN.md` |
| Prompt per gambar | `story-media/prompts/<kategori>/<nama>.txt` |
| Referensi latar | `story-media/01_Lokasi/loc_*.webp` |
| Referensi wajah/pakaian NPC | `story-media/02_Potret_NPC/npc_*.webp` |
| Hasil adegan | `story-media/03_Adegan_Cerita/scene_*.webp` |
| Prompt pembuka yang belum dikerjakan | `story-media/prompts/04_Halaman_Pembuka/` |
| Prompt peta/banner yang belum dikerjakan | `story-media/prompts/05_Peta_Banner/` |

Sumber cerita/ID menurut README adalah `src/game/story/content/*.json` di repository `Vanillate.ID`. Untuk produksi gambar biasa, prompt dan manifest di repository media sudah menjadi titik awal; bila diminta mengubah isi cerita, periksa juga sumber ceritanya.

## 2. Dari mana gambar diperoleh

**Gambar baru dibuat dengan alat OpenAI image generation**, bukan hasil pencarian web atau pengambilan gambar dari internet. Potret dan latar yang sudah disetujui di repository digunakan sebagai gambar acuan. Gambar yang dilampirkan pengguna dapat menjadi acuan bila masih dapat diakses alat; jangan mengaku memiliki file lampiran lokal bila path/ID-nya tidak tersedia.

Alur nyata yang dipakai:

1. Baca prompt `.txt`, terutama kode `ST-SCENE`, judul, nama berkas, ukuran, lokasi, tokoh, konteks, dan blok `TEMPEL KE CHATGPT`.
2. Ambil WebP lokasi dan NPC dari GitHub.
3. Simpan referensi ke filesystem lalu **lihat gambarnya** melalui `view_image`.
4. Panggil `image_gen.imagegen` dengan referensi tersebut dan instruksi adegan.
5. Lihat hasilnya. Jika ada masalah isi atau komposisi, edit dengan image generation lagi.
6. Gunakan Pillow hanya untuk crop, resize, dan kompresi WebP.
7. Lihat WebP akhir, unggah ke GitHub, dan verifikasi cabang `main`.

Contoh sumber yang bisa dibuka manusia:

- [Potret Pak Rudi](https://github.com/Ndyspleasure/database-media-web/blob/main/story-media/02_Potret_NPC/npc_pak_rudi.webp)
- [Lokasi sungai](https://github.com/Ndyspleasure/database-media-web/blob/main/story-media/01_Lokasi/loc_river.webp)
- [Prompt Banjir yang Menenggelamkan](https://github.com/Ndyspleasure/database-media-web/blob/main/story-media/prompts/03_Adegan_Cerita/scene_s_sungai_2.txt)
- [Hasil adegannya](https://github.com/Ndyspleasure/database-media-web/blob/main/story-media/03_Adegan_Cerita/scene_s_sungai_2.webp)

URL `github.com/.../blob/main/...` membuka halaman pratinjau. URL `raw.githubusercontent.com/Ndyspleasure/database-media-web/main/<path>` menunjuk isi file, tetapi akses tetap bergantung jaringan/izin. Tautan saja **tidak berarti Codex sudah melihat piksel gambar**; unduh lalu gunakan alat penampil gambar.

## 3. Mulai sesi baru dan temukan pekerjaan yang tersisa

1. Baca instruksi pengguna dan `AGENTS.md` yang berlaku jika ada. Saat sesi produksi ini diperiksa tidak ada `AGENTS.md` di repository; selalu periksa ulang.
2. Temukan alat GitHub yang tersedia. Di sesi ini nama alat adalah `mcp__codex_apps__github_*`, dipanggil melalui `functions.exec`. Nama/paket dapat berubah, jadi periksa metadata alat yang benar-benar tersedia.
3. Baca tree terbaru: `https://api.github.com/repos/Ndyspleasure/database-media-web/git/trees/main?recursive=1` melalui `github_fetch`.
4. Cocokkan setiap prompt dengan target WebP-nya. Contoh: `story-media/prompts/03_Adegan_Cerita/scene_s_maya_3.txt` berpasangan dengan `story-media/03_Adegan_Cerita/scene_s_maya_3.webp`.
5. Untuk urutan produksi, gunakan angka `KODE` pada prompt/manifest, **bukan urutan alfabet nama berkas**.
6. Jika semua target dalam lingkup permintaan sudah ada, laporkan kelengkapannya; untuk kategori baru gunakan ukuran prompt kategori itu.

Contoh pemeriksaan dengan JavaScript setelah tree disimpan sebagai `treeData`:

```js
const files = treeData.tree;
const prompts = files.filter(x =>
  x.path.startsWith('story-media/prompts/03_Adegan_Cerita/') &&
  x.path.endsWith('.txt'));
const missing = prompts.filter(x => !files.some(y =>
  y.path === x.path.replace('/prompts/', '/').replace(/\.txt$/, '.webp')));
// Tampilkan nama file/jumlah saja, jangan tampilkan data base64 gambar.
```

Checkout lokal `/workspace/database-media-web` pada sesi ini ternyata masih berada pada commit lama dan cabang `work`, sedangkan `main` remote jauh lebih baru. **Jangan menganggap checkout lokal sudah mutakhir.** Bila menggunakan Git CLI, periksa status, remote, dan HEAD lalu sinkronkan secara aman. Alur produksi di bawah menggunakan konektor GitHub tanpa mereset checkout lokal.

## 4. Mengunduh dan MELIHAT referensi lewat konektor GitHub

Gunakan `github_fetch_file` untuk file biner dengan `encoding: 'base64'`. `github_fetch` cocok untuk tree, commit, dan teks; pada sesi ini alat tersebut tidak mendukung unduhan biner mentah.

```js
const r = await tools.mcp__codex_apps__github_fetch_file({
  repository_full_name: 'Ndyspleasure/database-media-web',
  path: 'story-media/02_Potret_NPC/npc_pak_rudi.webp',
  ref: 'main',
  encoding: 'base64'
});
if (r.isError || !r.structuredContent?.content) throw Error('Unduhan gagal');
const b64 = r.structuredContent.content.replace(/\s/g, '');
if (!/^[A-Za-z0-9+/=]+$/.test(b64)) throw Error('Base64 tidak valid');
// Jangan text(r), text(b64), atau mencetak isi file biner.
```

Pada sesi ini data dipindahkan ke filesystem dalam potongan 40.000 karakter agar tidak melewati batas panjang argumen shell. Contoh lanjutan, dijalankan di `functions.exec`:

```js
await tools.exec_command({cmd: 'mkdir -p /workspace/work/story-refs'});
const target = '/workspace/work/story-refs/npc_pak_rudi.webp'; // path tetap/tepercaya
for (let i = 0; i < b64.length; i += 40000) {
  const part = b64.slice(i, i + 40000);
  const mode = i === 0 ? 'wb' : 'ab';
  await tools.exec_command({
    cmd: "python -c 'import base64,pathlib; p=pathlib.Path(\"" + target +
      "\"); f=p.open(\"" + mode + "\"); f.write(base64.b64decode(\"" +
      part + "\")); f.close()'",
    max_output_tokens: 50
  });
}
image((await tools.view_image({path: target})).image_url);
```

Contoh shell tersebut aman untuk alfabet base64 yang sudah divalidasi dan path tetap di atas. Jangan interpolasikan nama/path bebas dari pengguna tanpa pengutipan shell yang benar. Bila tool mengembalikan error atau tidak memiliki `structuredContent`, baca error dan ulangi unduhan yang gagal seperlunya; jangan langsung melanjutkan dengan data kosong.

Jika file sudah ada pada checkout yang telah dipastikan benar, cukup `view_image` file lokal itu. Jika referensi hilang dari workspace sesi baru, unduh lagi dari repository. Tidak perlu meminta pengguna mengunggah ulang referensi yang sudah tersedia di sana.

## 5. Membuat ilustrasi dengan image generation

Gunakan kemampuan image generation yang tersedia pada sesi itu. Di sesi produksi ini panggilannya seperti berikut:

```js
// @exec: {"yield_time_ms": 120000, "max_output_tokens": 200}
generatedImage(await tools.image_gen__imagegen({
  referenced_image_paths: [
    '/workspace/work/story-refs/npc_pak_rudi.webp',
    '/workspace/work/story-refs/loc_river.webp'
  ],
  transparent_background: false,
  prompt: 'Isi prompt adegan beserta penjelasan referensi dan komposisi...'
}));
```

- Baca gambar lokal melalui `view_image` sebelum menjadikannya referensi edit/generasi.
- Gunakan referensi wajah/pakaian NPC dan lokasi yang memang disebut dalam prompt. Adegan sebelumnya boleh menjadi acuan kesinambungan properti, pemain, dan suasana.
- Pada sesi ini referensi dibatasi secara konservatif maksimal lima per panggilan. Ikuti batas alat yang aktif. Jika terlalu banyak tokoh, buat lembar acuan gabungan dengan **image generation**, lihat hasilnya, lalu pakai bersama referensi lokasi. Jangan menganggap deskripsi nama saja cukup menjaga wajah.
- Untuk lampiran percakapan tanpa path, mekanisme alat saat ini adalah `num_last_images_to_include`; pilih jumlah paling kecil yang memuat semua target. Jangan gabungkan parameter ini dengan `referenced_image_paths`. Bila gambar tidak bisa diakses dengan kedua mekanisme, barulah minta lampiran ulang.
- Untuk gambar baru tanpa acuan, hilangkan kedua parameter referensi tersebut.
- Semua adegan ini berlatar penuh: `transparent_background: false`. Potongan transparan hanya jika memang diminta.
- Hasil PNG asli muncul di `/workspace/generated_images/exec-<id>.png`. Catat **path yang benar-benar dikembalikan** alat, jangan mengarang nama. Tampilkan hasil menggunakan `generatedImage(result)`, jangan mencetak base64.
- Generasi memerlukan waktu. Jika `functions.exec` mengembalikan ID cell yang masih berjalan, tunggu cell yang sama dengan `functions.wait` sesuai petunjuk alat; jangan membuat panggilan ganda hanya karena belum selesai.
- Simpan PNG asli. PNG mentah sesi ini tidak diunggah ke repository; WebP final yang diunggah.

Susun prompt dengan: kode/judul adegan, gaya, peran setiap referensi, lokasi, aktivitas dan properti utama, ciri NPC, penempatan pemain, komposisi aman untuk crop, dan larangan teks/logo. Pertahankan isi naskah; tambahan instruksi berfungsi memperjelas visual, bukan mengganti cerita.

## 6. Konsistensi dan pemeriksaan visual

- Gaya adegan: anime visual novel, soft cel-shading, mata detail, lineart bersih, latar kota kecil Indonesia bertekstur pixel art yang sedikit dilunakkan. Lokasi murni memakai gaya pixel sesuai prompt induk.
- Pemain dalam rangkaian ini: pria dewasa muda, rambut cokelat acak, kemeja berkerah krem lengan pendek, celana gelap, sepatu sederhana. **Selalu dari belakang, tanpa mata/hidung/pipi atau wajah profil terlihat.** Jangan mengubah kontinuitas ini kecuali diminta pengguna.
- Pengguna pernah menyoroti tubuh Elder Sen yang terpotong. Periksa kepala, badan, tangan, kaki, dan properti utama; jangan crop otomatis sampai tubuh hilang.
- **Seno Suryo (`npc_seno`) berbeda dari Elder Sen/Djoko Seno (`npc_elder_sen`).** Seno guru/penulis40-an berambut cokelat gelap, kacamata bulat, kumis tipis/goatee kecil, kemeja polos. Elder Sen berambut perak, berjanggut putih, batik dan tongkat.
- Shelli: anak SD berkuncir dua; Rara: anak SD dengan kuncir tinggi; Lina: anak SD rambut bob. Pertahankan usia anak, proporsi anak, serta pakaian wajar. NPC lain mengikuti potret dan prompt.
- Nissa pada rangkaian ini memakai hijab krem, bros bunga emas, blus krem, rok panjang cokelat. Tasya memakai vest marun lis emas, blus krem, rambut panjang berponi, pita marun dan jepit bunga.
- Periksa jumlah tokoh, pose, ekspresi, tangan, kaki, benda yang dipegang, arah pandang, perspektif, dan waktu/suasana.
- Periksa detail spesifik: tiga ikan dalam ember, termos kopi, topi yang dilepas, amplop polos, atau lampu hijau sesuai adegannya. Jangan biarkan duplikasi properti yang membingungkan.
- Tanpa logo, merek, watermark, teks terbaca, atau anatomi rusak. Pada adegan warnet simbol undo/komputer generik dipakai tanpa tulisan merek. Jika prompt mengandung contoh tulisan tetapi juga melarang teks, pertahankan fungsi visual lewat simbol generik.

Jika ada kesalahan, minta **edit lewat image generation**: sebut perubahan tepat, bagian yang dipertahankan, dan lampirkan hasil sebelumnya. Contoh revisi nyata: menghapus kertas catatan ganda, membuat wajah pemain sepenuhnya membelakangi kamera, mengganti kipas datar menjadi topi anyaman, melepas topi Pak Hasan, serta memperlebar framing agar kaki tidak terpotong. Jangan mengecat ulang isi gambar memakai Python; Python di sini untuk pengolahan format saja.

## 7. Crop, resize, kompres, lalu lihat hasil akhirnya

Untuk adegan: **1280×720, WebP, ukuran file <300.000 byte**. Batas byte ini sengaja ketat agar juga memenuhi syarat <300 KB. Potret dan peta mempunyai spesifikasi berbeda; baca promptnya.

Prompt awal meminta 3:2 lalu crop16:9. Pada PNG1536×1024, tinggi16:9 adalah864 piksel. Crop tengah default `top=80`, tetapi beberapa hasil perlu `top=110` atau120 demi menjaga kaki. **Pilih setelah melihat gambar**, bukan menyalin angka secara buta. Prompt area aman tidak selalu dipatuhi model. Hasil edit kadang sudah lebar sekitar1672×941; baca ukuran aktual.

Jika seluruh kepala sampai kaki tidak muat dalam crop16:9, edit imagegen: “zoom camera out20–25%, wide16:9, keep complete heads and feet with margins”. Jangan meregangkan gambar untuk memaksanya muat.

Contoh Pillow (ganti sumber, tujuan, dan `top` berdasarkan pemeriksaan):

```python
from pathlib import Path
from PIL import Image

src = Path('/workspace/generated_images/exec-ID-YANG-BENAR.png')
dst = Path('/workspace/work/story-scenes/scene_contoh.webp')
dst.parent.mkdir(parents=True, exist_ok=True)
im = Image.open(src).convert('RGB')
w, h = im.size
crop_h = round(w * 9 / 16)
top = (h - crop_h) // 2  # sesuaikan setelah melihat gambar
assert 0 <= top and top + crop_h <= h
im = im.crop((0, top, w, top + crop_h))
im = im.resize((1280, 720), Image.Resampling.LANCZOS)
for quality in range(88, 39, -3):
    im.save(dst, 'WEBP', quality=quality, method=6)
    if dst.stat().st_size < 300_000:
        break
assert dst.stat().st_size < 300_000
with Image.open(dst) as check:
    assert check.format == 'WEBP' and check.size == (1280, 720)
print(dst.name, dst.stat().st_size)
```

Lalu **`view_image` WebP final**, bukan hanya PNG awal. Pastikan crop tidak menghilangkan kepala/kaki/properti dan kompresi masih layak. Jangan hanya mengandalkan assertion dimensi.

## 8. Memasukkan hasil ke main melalui GitHub

Perubahan sesi produksi memakai objek Git (blob → tree → commit → update ref). Pengguna secara eksplisit meminta masuk `main`. Untuk sesi berikutnya ikuti otorisasi pengguna yang berlaku; jangan menganggap dokumen ini memberi izin publikasi pada repository lain.

1. Ambil HEAD `main` terbaru lewat tree/ref/commit. Ambil detail commit melalui `github_fetch` ke `.../git/commits/<HEAD>`.
2. Simpan `parent.sha` dan **`parent.tree.sha`**. SHA commit berbeda dari SHA tree; jangan menukar keduanya. SHA pada respons tree yang dipakai sesi ini diperlakukan sebagai HEAD setelah dicocokkan dengan endpoint commit; periksa bentuk respons alat aktif.
3. Baca WebP menjadi base64 melalui `exec_command` (`base64 -w0 <path>`), dengan anggaran output cukup (misalnya200000 token untuk satu file). Simpan hasil di variabel dalam `functions.exec`; **jangan cetak base64 ke percakapan**.
4. `github_create_blob({repository_full_name, encoding:'base64', content:base64})` → simpan blob SHA.
5. `github_create_tree({repository_full_name, base_tree_sha:parent.tree.sha, tree_elements:[...]})`. Setiap elemen gambar: `{path:'story-media/03_Adegan_Cerita/<nama>.webp', mode:'100644', type:'blob', sha:blobSha}`. Pakai base tree agar file lain tetap ada.
6. `github_create_commit({repository_full_name, parent_sha:parent.sha, tree_sha:newTreeSha, message:'...judul perubahan...'})`.
7. `github_update_ref({repository_full_name, branch_name:'main', expected_sha:parent.sha, force:false, sha:newCommitSha})`.
8. Jika lease/expected SHA gagal, baca HEAD baru, gabungkan perubahan secara aman ke tree terbaru, lalu buat commit baru. Jangan memakai force untuk melewati perubahan orang lain.
9. Baca ulang tree `main`; periksa HEAD, target path, blob SHA, dan ukuran. Untuk batch, periksa semua file. Cocokkan prompt dengan target lagi.

Selalu periksa `isError` dan `structuredContent` pada setiap hasil alat. Jangan melaporkan “sudah masuk main” hanya karena blob berhasil dibuat; update ref dan verifikasi akhir harus berhasil.

Batch tujuh gambar terakhir memakai satu tree/commit setelah semua blob selesai. Commit tersebut hanya menambah tujuh WebP, bukan PNG mentah, base64 dalam file teks, atau gambar referensi duplikat. Untuk revisi gambar yang sudah dipakai, aturan awal menyarankan akhiran `_v2`; ikuti permintaan pengguna dan aturan repository saat itu, jangan sembarang menimpa.

## 9. Pelaporan dan media yang dibutuhkan

Berikan kabar singkat dalam bahasa Indonesia selama pekerjaan panjang. Jawaban selesai menyebut hasil nyata, tautan GitHub, dimensi/ukuran, dan pekerjaan tersisa bila ada. Bedakan **dibuat**, **diunggah**, **terverifikasi di main**, dan **dipasang di aplikasi**; mengunggah repository media tidak otomatis mengubah bot/website atau Drive.

Jika referensi sudah ada di repository, lanjutkan tanpa meminta media yang sama. Minta bantuan pengguna hanya untuk referensi baru yang belum tersedia/terakses, identitas tokoh atau lokasi baru, atau keputusan isi yang tidak dapat disimpulkan dari prompt. Sebutkan media yang dibutuhkan secara spesifik.

Direktori kerja yang dipakai sesi ini (bisa hilang pada sesi berikutnya):

```text
/workspace/work/story-refs/     # WebP lokasi/NPC yang diunduh untuk dilihat
/workspace/generated_images/   # PNG asli hasil image generation
/workspace/work/story-scenes/  # WebP final sebelum diunggah
```

Repository GitHub adalah sumber persisten untuk WebP final dan prompt. Workspace sementara bukan cadangan permanen. Untuk melanjutkan pekerjaan baru, mulai lagi dari pemeriksaan tree/prompt dan unduh referensi yang diperlukan.
