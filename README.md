# database-media-web

Emoji animasi (GIF 128×128, transparan, < 256 KB) untuk Discord Application Emojis.

- `CHECKLIST.md` — status tiap emoji (✅ selesai / ⬜ belum / 🔤 unicode saja). Dibuat otomatis.
- `gifs/` — hasil GIF, nama file = nama emoji.
- `tools/emojis.txt` — daftar 388 emoji (urutan = nomor di tabel asli). Akhiran `u` = disarankan tetap unicode.
- `tools/wave1.py`, `tools/wave2.py` — generator GIF per gelombang (`python3 tools/waveN.py`, butuh Pillow).
- `tools/update_checklist.py` — perbarui `CHECKLIST.md` setelah menambah GIF.
- `tools/preview.py` — buat `preview.png` (contact sheet semua GIF).
