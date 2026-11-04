"""Kontak sheet semua GIF di gifs/ -> preview.png  (python3 tools/preview.py [out.png])"""
import os,sys
from PIL import Image, ImageSequence, ImageDraw
D=os.path.dirname(os.path.abspath(__file__)); G=D+"/../gifs"; names=sorted(f for f in os.listdir(G) if f.endswith(".gif"))
C=9; O=128; rows=(len(names)+C-1)//C; sh=Image.new("RGBA",(C*O,rows*(O+14)),(54,57,63,255)); dr=ImageDraw.Draw(sh)
for k,n in enumerate(names):
    fr=[f.convert("RGBA") for f in ImageSequence.Iterator(Image.open(f"{G}/{n}"))]; f=fr[int(len(fr)*.55)]
    x,y=(k%C)*O,(k//C)*(O+14); sh.alpha_composite(f,(x,y)); dr.text((x+2,y+O),n[:21],fill=(200,200,200,255))
sh.convert("RGB").save(sys.argv[1] if len(sys.argv)>1 else D+"/../preview.png"); print(len(names),"gif")
