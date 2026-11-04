# database-media-web

Emoji animasi (GIF 128×128, transparan, < 256 KB) untuk Discord Application Emojis.

- `CHECKLIST.md` — status tiap emoji (✅ selesai / ⬜ belum). Dibuat otomatis.
- `gifs/` — hasil GIF, nama file = nama emoji.
- `tools/emojis.txt` — daftar 399 emoji (urutan = nomor di tabel asli).
- `tools/wave1.py` … `tools/wave8.py` — definisi emoji per gelombang. `tools/motion.py` — sistem animasi v2 (pop intro/outro, gerak fisika, aksi khas).
- `tools/build_all.py` — bangun ulang SEMUA GIF (`python3 tools/build_all.py` atau tambah nama emoji untuk sebagian).
- `tools/update_checklist.py` — perbarui `CHECKLIST.md` setelah menambah GIF.
- `tools/preview.py` — buat `preview.png` (contact sheet semua GIF).
