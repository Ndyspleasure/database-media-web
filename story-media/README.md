# story-media: prompt gambar Vanillate Story

Kumpulan prompt siap tempel ke Google Gemini untuk membuat media game **Vanillate Story** (hub `/game` bot Vanillate).
Berisi 153 prompt, satu berkas per gambar.

| Isi | Jumlah |
|---|---|
| Latar lokasi pixel | 39 |
| Potret karakter gaya novel | 40 (36 NPC + Bang Jul, Ibu, Bapak, Sari) |
| Adegan cerita | 65 |
| Halaman pembuka Bab 0 dan Cara Bermain | 7 |
| Peta kota dan banner | 2 |

- `manifest.csv`: daftar semua gambar (kode, nama berkas, folder Drive, ukuran, prompt). Impor ke Google Sheets untuk pelacak kerja.
- `prompts/<folder>/<nama>.txt`: satu prompt per gambar. Bagian di antara `TEMPEL KE GEMINI` dan `SELESAI` disalin utuh.
- `PENAMAAN.md`: aturan nama berkas, struktur folder Drive, ukuran, alur kerja.
- `00_STYLE_PROMPT.md`: prompt induk gaya (pixel untuk peta, novel untuk karakter).

Sumber data: `src/game/story/content/*.json` di repo `Vanillate.ID`. Bila ID adegan, lokasi, atau NPC berubah di sana,
prompt dan nama berkas di sini perlu disesuaikan.
