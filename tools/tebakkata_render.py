#!/usr/bin/env python3
"""Render gambar soal game Tebak Kata dari berkas spesifikasi PRIVAT.

Pemakaian:
    python3 tools/tebakkata_render.py --spec <spesifikasi.json> [--icons tebak-gambar] [--out tebak-kata]

Repo ini PUBLIK. Spesifikasi (berisi jawaban dan rumus) disimpan di repo bot yang privat dan hanya dibaca
alat ini lewat --spec. Alat ini TIDAK menulis jawaban ke mana pun dan nama berkas keluaran = id acak soal.

Bentuk spesifikasi (daftar soal):
  {"id": "ab12cd", "words": [ [tile, tile, ...], [tile, ...] ]}   # satu daftar ubin per kata
  tile:
    {"k": "ikon",   "i": "<id ikon>"}                       gambar benda (varian -3)
    {"k": "ganti",  "i": "<id ikon>", "a": "c", "b": "n"}   gambar + gelembung "C = N" (huruf A dicoret, diganti B)
    {"k": "hapus",  "i": "<id ikon>", "x": "g"}             gambar + gelembung "- G" (hapus huruf itu)
    {"k": "potong", "i": "<id ikon>", "x": "kam"}           gambar + gelembung "- KAM" (buang awalan atau akhiran)
    {"k": "huruf",  "s": "gi"}                              ubin huruf
Ubin dalam satu kata digabung "+", kata dipisah panel sendiri, diakhiri "= ?".
"""
import argparse
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
W, H = 1280, 720
BG = (244, 251, 247)
INK = (38, 50, 56)
LINE = (200, 222, 210)
PANEL = (231, 243, 250)
PANEL_LINE = (176, 208, 226)
AMBER = (255, 193, 7)
ROSE = (255, 171, 145)
TEAL = (0, 105, 92)
RED = (200, 30, 30)
MARGIN = 48


def font(size):
    return ImageFont.truetype(FONT, max(10, int(size)))


class Layout:
    """Menghitung ukuran ubin terbesar yang muat dan penempatan tiap kelompok."""

    def __init__(self, words):
        self.words = words
        self.best = None
        fallback = None
        for s in range(240, 60, -6):
            rows = self._rows(s)
            if rows is None:
                continue
            total_h = len(rows) * (s * 1.34) + (len(rows) - 1) * s * 0.12
            if total_h > H - 2 * MARGIN:
                continue
            if fallback is None:
                fallback = (s, rows)
            # hindari baris terakhir yang hanya berisi "= ?" (terlempar sendirian)
            if len(rows) > 1 and all(it[0] == "tanya" for it in rows[-1]):
                continue
            self.best = (s, rows)
            break
        if self.best is None:
            self.best = fallback
        if not self.best:
            raise ValueError("soal terlalu panjang untuk satu gambar")
        self.s, self.rows = self.best

    def gwidth(self, n, s):
        return n * s + (n - 1) * s * 0.30 + s * 0.16

    def _rows(self, s):
        gap = s * 0.22
        items = [("kata", i, self.gwidth(len(w), s)) for i, w in enumerate(self.words)]
        items.append(("tanya", 0, s * 0.34 + s))
        rows, cur, cw = [], [], 0
        for it in items:
            need = it[2] + (gap if cur else 0)
            if it[2] > W - 2 * MARGIN:
                return None
            if cur and cw + need > W - 2 * MARGIN:
                rows.append(cur)
                cur, cw = [], 0
                need = it[2]
            cur.append(it)
            cw += need
        rows.append(cur)
        return rows


def card(im, x, y, w, h, radius):
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((x + 3, y + 6, x + w + 3, y + h + 6), radius, fill=(214, 232, 222))
    d.rounded_rectangle((x, y, x + w, y + h), radius, fill="white", outline=LINE, width=3)


def badge(im, x, y, s, kind, a, b=None):
    """Gelembung di atas ubin gambar. ganti: 'A = B' dengan A dicoret. hapus/potong: '- X'."""
    d = ImageDraw.Draw(im)
    f = font(s * 0.17)
    text = f"{a.upper()} = {b.upper()}" if kind == "ganti" else f"- {a.upper()}"
    tw = d.textlength(text, font=f)
    bw, bh = tw + s * 0.22, s * 0.27
    bx, by = x + s - bw + s * 0.04, y - bh * 0.62
    d.rounded_rectangle((bx, by, bx + bw, by + bh), bh * 0.32, fill=AMBER if kind == "ganti" else ROSE,
                        outline=INK, width=3)
    tx, ty = bx + (bw - tw) / 2, by + bh * 0.16
    d.text((tx, ty), text, font=f, fill=INK)
    if kind == "ganti":
        aw = d.textlength(a.upper(), font=f)
        d.line((tx - 2, by + bh - 7, tx + aw + 2, by + 7), fill=RED, width=max(3, int(s * 0.03)))


def icon_tile(im, icons_dir, t, x, y, s):
    card(im, x, y, s, s, s * 0.11)
    path = os.path.join(icons_dir, f"{t['i']}-3.webp")
    g = Image.open(path).convert("RGB")
    iw = int(s - s * 0.12)
    g = g.resize((iw, int(iw * 0.75)))
    mask = Image.new("L", g.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0) + g.size, int(s * 0.07), fill=255)
    im.paste(g, (x + int(s * 0.06), y + int((s - g.size[1]) / 2)), mask)
    if t["k"] in ("ganti", "hapus", "potong"):
        if t["k"] == "ganti":
            badge(im, x, y, s, "ganti", t["a"], t["b"])
        else:
            badge(im, x, y, s, t["k"], t["x"])


def text_tile(im, t, x, y, s):
    card(im, x, y, s, s, s * 0.11)
    d = ImageDraw.Draw(im)
    txt = t["s"].upper()
    size = s * 0.5
    f = font(size)
    while d.textlength(txt, font=f) > s * 0.84 and size > 12:   # muat dengan lebar sebenarnya
        size -= 2
        f = font(size)
    tw = d.textlength(txt, font=f)
    d.text((x + (s - tw) / 2, y + s / 2 - size * 0.62), txt, font=f, fill=TEAL)


def plus(im, x, y, s, w, ch="+"):
    d = ImageDraw.Draw(im)
    f = font(s * 0.36)
    tw = d.textlength(ch, font=f)
    d.text((x + (w - tw) / 2, y + s / 2 - s * 0.24), ch, font=f, fill=INK)


def render(puzzle, icons_dir, out_path):
    words = puzzle["words"]
    lay = Layout(words)
    s = int(lay.s)
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    gap = s * 0.22
    row_h = s * 1.34
    block_h = len(lay.rows) * row_h + (len(lay.rows) - 1) * s * 0.12
    y0 = (H - block_h) / 2 + s * 0.30
    for r, row in enumerate(lay.rows):
        rw = sum(it[2] for it in row) + gap * (len(row) - 1)
        x = (W - rw) / 2
        y = int(y0 + r * (row_h + s * 0.12))
        for kind, idx, width in row:
            if kind == "kata":
                gx, gy = int(x), int(y - s * 0.10)
                d.rounded_rectangle((gx, gy, gx + width, gy + s * 1.20), s * 0.16, fill=PANEL, outline=PANEL_LINE, width=3)
                tx = x + s * 0.08
                tiles = words[idx]
                for n, t in enumerate(tiles):
                    if t["k"] == "huruf":
                        text_tile(im, t, int(tx), y, s)
                    else:
                        icon_tile(im, icons_dir, t, int(tx), y, s)
                    tx += s
                    if n < len(tiles) - 1:
                        plus(im, int(tx), y, s, s * 0.30)
                        tx += s * 0.30
            else:
                plus(im, int(x), y, s, s * 0.34, "=")
                tx = x + s * 0.34
                card(im, int(tx), y, s, s, s * 0.11)
                f = font(s * 0.62)
                tw = d.textlength("?", font=f)
                d.text((tx + (s - tw) / 2, y + s * 0.10), "?", font=f, fill=(150, 160, 165))
            x += width + gap
    im.save(out_path, "WEBP", quality=82, method=6)
    return os.path.getsize(out_path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spec", required=True, help="berkas spesifikasi soal (PRIVAT, jangan di-commit)")
    ap.add_argument("--icons", default="tebak-gambar", help="folder ikon WebP (bawaan tebak-gambar)")
    ap.add_argument("--out", default="tebak-kata", help="folder keluaran (bawaan tebak-kata)")
    a = ap.parse_args()
    puzzles = json.load(open(a.spec, encoding="utf-8"))
    os.makedirs(a.out, exist_ok=True)
    biggest = 0
    for p in puzzles:
        out = os.path.join(a.out, f"{p['id']}.webp")
        size = render(p, a.icons, out)
        biggest = max(biggest, size)
    print(f"{len(puzzles)} gambar dibuat di {a.out}, terbesar {biggest / 1024:.1f} KB")
    if biggest > 150 * 1024:
        sys.exit("ada gambar di atas 150 KB")


if __name__ == "__main__":
    main()
