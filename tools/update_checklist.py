"""Bangun CHECKLIST.md dari tools/emojis.txt + file di gifs/. Jalankan: python3 tools/update_checklist.py"""
import os, json
D=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(D,"..")
rows=[l.split() for l in open(D+"/emojis.txt",encoding="utf-8").read().splitlines() if l.strip()]
ids={}
if os.path.exists(R+"/emoji_ids.json"): ids=json.load(open(R+"/emoji_ids.json"))
done={f[:-4] for f in os.listdir(R+"/gifs") if f.endswith(".gif")}
tot=len(rows); uni=sum(1 for r in rows if len(r)>2); target=tot-uni
nd=sum(1 for r in rows if r[1] in done)
out=["# Checklist Emoji Animasi (Discord Application Emojis)\n",
"File ini dibuat otomatis oleh `tools/update_checklist.py` — jangan edit manual.\n",
f"**Progres: {nd} / {tot} GIF selesai** ({tot-nd} tersisa).\n",
"Legenda: ✅ GIF sudah dibuat · ⬜ belum.\n",
"Spesifikasi: GIF 128×128 px, transparan, < 256 KB, nama 2–32 karakter (a-z, 0-9, _).\n",
"## Berikutnya (20 teratas yang belum dikerjakan)\n"]
pend=[(i+1,r) for i,r in enumerate(rows) if r[1] not in done ][:20]
out+= [f"- #{i} {r[0]} `{r[1]}`" for i,r in pend]
out+=["\n## Semua emoji\n","| Status | # | Emoji | Nama | ID Emoji |","|---|---|---|---|---|"]
for i,r in enumerate(rows,1):
    st="✅" if r[1] in done else "⬜"
    out.append(f"| {st} | {i} | {r[0]} | `{r[1]}` | {ids.get(r[1],'')} |")
open(R+"/CHECKLIST.md","w",encoding="utf-8").write("\n".join(out)+"\n")
print(f"{nd}/{tot} selesai, {tot-nd} GIF tersisa")
