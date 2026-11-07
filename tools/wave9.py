import os
D=os.path.dirname(os.path.abspath(__file__))
exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read())
jobs=[("streak_amber",f_streak_amber),("streak_crimson",f_streak_crimson),("streak_emerald",f_streak_emerald),
("streak_azure",f_streak_azure),("streak_phantom",f_streak_phantom),("streak_eternal",f_streak_eternal)]
for n,fn in jobs: save(n,fn,60,40,True)
