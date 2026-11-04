"""Bangun ulang SEMUA GIF dengan sistem animasi v2:  python3 tools/build_all.py [nama1 nama2 ...]"""
import os,sys,re
D=os.path.dirname(os.path.abspath(__file__))
exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read()); from PIL import ImageChops; exec(open(D+"/motion.py").read())
_KEEP={k:globals()[k] for k in ('W','BL','BLD','GR','GRD','SK','SKD','DK','RE')}
ALL=[]
for i in range(1,8):
    wtxt=open(f"{D}/wave{i}.py").read().split("for n,fn in jobs")[0].replace('exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read())','')
    exec(wtxt); ALL+=jobs
globals().update(_KEEP)
only=set(sys.argv[1:]); done=0
for name,fn in ALL:
    if only and name not in only: continue
    try:
        if name in CUSTOM: fn=CUSTOM[name]
        elif name in MAP: fn=make_motion(fn,*MAP[name])
        # frame pertama = pose penuh (Discord memakai frame pertama sebagai pratinjau statis)
        if name not in RAW: fn=(lambda f0:(lambda t:f0((t+.14)%1)))(staged(fn))
        else: fn=(lambda f0:(lambda t:f0((t+.42)%1)))(fn)
        save(name,fn); done+=1
    except Exception as e: print("GAGAL",name,repr(e))
print(done,"GIF dibuat")
