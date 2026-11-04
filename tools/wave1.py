import os
D=os.path.dirname(os.path.abspath(__file__))
exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read())
jobs=[("bar_chart",f_bars),("trophy",f_trophy),("shield",f_shield),("robot_face",f_robot),("octagonal_sign",f_stop),("lock",f_lock),
("black_right_pointing_triangle",f_play),("information_source",f_info),("fire",f_fire),("crown",f_crown),("heavy_black_heart",f_heart),
("large_green_circle",f_ball((46,204,113,255),(30,160,86,255),(130,232,170,255))),("large_red_circle",f_ball((231,76,60,255),(185,50,40,255),(246,150,140,255)))]
jobs+=[("check",f_check),("cross_mark",f_cross),("warning_sign",f_warn),("hourglass_with_flowing_sand",f_hour)]
for n,fn in jobs: save(n,fn)
