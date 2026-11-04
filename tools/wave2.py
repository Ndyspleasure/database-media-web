import os
D=os.path.dirname(os.path.abspath(__file__))
exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read())
Y=((253,203,50,255),(200,150,20,255),(255,235,150,255)); B=((52,120,246,255),(30,80,200,255),(130,180,255,255)); O=((255,140,40,255),(200,100,20,255),(255,190,120,255))
PU=((155,89,182,255),(115,60,150,255),(200,150,225,255)); W=((240,242,245,255),(170,175,185,255),(255,255,255,255)); BK=((45,48,55,255),(20,22,26,255),(100,105,115,255)); G=((46,204,113,255),(30,160,86,255),(130,232,170,255))
GOLD=((255,193,7,255),(200,140,0,255),(255,224,100,255)); SIL=((190,198,210,255),(130,140,155,255),(225,230,238,255)); BRZ=((205,127,50,255),(150,85,30,255),(230,165,100,255))
jobs=[("large_yellow_circle",f_ball(*Y)),("large_blue_circle",f_ball(*B)),("large_orange_circle",f_ball(*O)),("large_purple_circle",f_ball(*PU)),("medium_white_circle",f_ball(*W)),("medium_black_circle",f_ball(*BK)),
("large_yellow_square",f_sq(*Y)),("large_blue_square",f_sq(*B)),("large_purple_square",f_sq(*PU)),("large_green_square",f_sq(*G)),("white_large_square",f_sq(*W)),("black_large_square",f_sq(*BK)),
("first_place_medal",f_medal(*GOLD,1)),("second_place_medal",f_medal(*SIL,2)),("third_place_medal",f_medal(*BRZ,3)),("sports_medal",f_medal(*GOLD,0)),
("black_rightwards_arrow",f_arrow(0)),("leftwards_black_arrow",f_arrow(180)),("upwards_black_arrow",f_arrow(90)),("black_left_pointing_triangle",f_playl),
("direct_hit",f_target),("crescent_moon",f_moon),("electric_light_bulb",f_bulb),("high_voltage_sign",f_bolt),("alarm_clock",f_alarm),("white_medium_star",f_star),("glowing_star",f_gstar),("sparkles",f_sparkles),
("coin",f_coin),("speech_balloon",f_speech),("wrapped_present",f_gift),("open_book",f_book),("black_question_mark_ornament",f_q((231,60,60,255))),("white_question_mark_ornament",f_q((205,210,222,255))),
("anticlockwise_arrows_button",f_cycle),("growing_heart",f_heartc((247,110,160,255),(210,70,120,255),(255,175,205,255))),("green_heart",f_heartc((46,204,113,255),(30,160,86,255),(150,235,180,255))),
("black_heart",f_heartc((45,48,55,255),(20,22,26,255),(95,100,112,255))),("no_entry_sign",f_nosign),("no_entry",f_noentry)]
for n,fn in jobs: save(n,fn)
