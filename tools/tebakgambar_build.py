#!/usr/bin/env python3
"""Bangun berkas game Tebak Gambar dari gambar sumber (mis. hasil GPT).

Pemakaian:
    python3 tools/tebakgambar_build.py <folder-sumber> [--out tebak-gambar] [--map tebakgambar-map.local.json]

Untuk tiap gambar sumber (.png .jpg .jpeg .webp) dibuat 3 varian WebP:
    <id>-1.webp  buram berat   (petunjuk pertama)
    <id>-2.webp  buram ringan  (petunjuk kedua)
    <id>-3.webp  jelas         (petunjuk ketiga dan reveal)
<id> = 6 karakter acak, TIDAK diturunkan dari nama berkas sumber (repo ini publik).

Berkas pemetaan (--map) berisi nama sumber, id, dan ukuran. Nama sumber bisa
membocorkan jawaban, jadi pemetaan itu JANGAN di-commit (sudah di .gitignore).
Dipakai untuk menulis `content/tebakgambar.json` di repo bot.
"""
import argparse
import json
import secrets
import string
import sys
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps

MAX_SIDE = 640
LIMIT_KB = 100          # target per varian
HARD_LIMIT_KB = 150     # batas keras
ALPHABET = string.ascii_lowercase + string.digits
EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def new_id(taken):
    while True:
        i = "".join(secrets.choice(ALPHABET) for _ in range(6))
        if i not in taken:
            taken.add(i)
            return i


def load(path):
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)
    if im.mode not in ("RGB", "L"):
        bg = Image.new("RGB", im.size, (255, 255, 255))
        rgba = im.convert("RGBA")
        bg.paste(rgba, mask=rgba.split()[3])
        im = bg
    else:
        im = im.convert("RGB")
    im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
    return im


def blur_heavy(im):
    """Piksel kasar lalu diburamkan: bentuk umum nyaris tidak terbaca."""
    w, h = im.size
    small = im.resize((max(4, w // 28), max(4, h // 28)), Image.BILINEAR)
    return small.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(radius=max(w, h) / 60))


def blur_light(im):
    """Buram sedang: bentuk dan warna terbaca, detail tidak."""
    w, h = im.size
    small = im.resize((max(8, w // 9), max(8, h // 9)), Image.BILINEAR)
    return small.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(radius=max(w, h) / 150))


def save_webp(im, path):
    """Simpan WebP dengan kualitas turun bertahap sampai <= LIMIT_KB."""
    for q in (82, 74, 66, 58, 50, 42, 34):
        im.save(path, "WEBP", quality=q, method=6)
        if path.stat().st_size <= LIMIT_KB * 1024:
            break
    kb = path.stat().st_size / 1024
    if kb > HARD_LIMIT_KB:
        raise SystemExit(f"{path.name}: {kb:.0f} KB melewati batas keras {HARD_LIMIT_KB} KB, kecilkan gambar sumber")
    return kb


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path, help="folder gambar sumber")
    ap.add_argument("--out", type=Path, default=Path("tebak-gambar"), help="folder keluaran (bawaan tebak-gambar)")
    ap.add_argument("--map", type=Path, default=Path("tebakgambar-map.local.json"), help="berkas pemetaan lokal, jangan di-commit")
    a = ap.parse_args()

    if not a.source.is_dir():
        sys.exit(f"folder sumber tidak ada: {a.source}")
    a.out.mkdir(parents=True, exist_ok=True)

    taken = {p.name.split("-")[0] for p in a.out.glob("*-?.webp")}
    mapping = json.loads(a.map.read_text("utf-8")) if a.map.exists() else {}
    done = {m["source"] for m in mapping.values()}

    files = sorted(p for p in a.source.iterdir() if p.suffix.lower() in EXTS)
    if not files:
        sys.exit("tidak ada gambar (.png .jpg .jpeg .webp) di folder sumber")

    for src in files:
        if src.name in done:
            print(f"lewati (sudah dibuat): {src.name}")
            continue
        im = load(src)
        sid = new_id(taken)
        sizes = [
            save_webp(blur_heavy(im), a.out / f"{sid}-1.webp"),
            save_webp(blur_light(im), a.out / f"{sid}-2.webp"),
            save_webp(im, a.out / f"{sid}-3.webp"),
        ]
        mapping[sid] = {"source": src.name, "size_kb": [round(s) for s in sizes]}
        print(f"{src.name} -> {sid}  ({' / '.join(f'{s:.0f}KB' for s in sizes)})")

    a.map.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print(f"\nPemetaan lokal: {a.map} (jangan di-commit). Tulis jawaban tiap id di content/tebakgambar.json repo bot.")


if __name__ == "__main__":
    main()
