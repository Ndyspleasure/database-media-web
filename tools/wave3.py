import os
D=os.path.dirname(os.path.abspath(__file__))
exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read())
GN=(46,204,113,255); GND=(30,160,86,255); RD=(231,60,60,255); RDD=(185,40,40,255)
jobs=[("wrench",f_wrench),("hammer",f_hammer),("gear",f_gear),("package",f_package),("door",f_door),("mobile_phone",f_phone),("briefcase",f_brief),("clipboard",f_clip),("money_bag",f_money),
("graduation_cap",f_grad),("game_die",f_die),("memo",f_memo),
("chart_with_upwards_trend",f_chart([(-.38,.3),(-.15,.05),(.05,.18),(.28,-.12),(.42,-.3)],GN)),("chart_with_downwards_trend",f_chart([(-.38,-.3),(-.15,-.05),(.05,-.18),(.28,.1),(.42,.28)],RD)),
("globe_with_meridians",f_globe),("video_game",f_game),("old_key",f_key((190,135,55,255),(125,80,25,255))),("key",f_key((255,193,7,255),(200,140,0,255))),
("loudspeaker",f_mega((231,76,60,255),(170,40,35,255))),("cheering_megaphone",f_mega((255,159,28,255),(200,110,10,255))),("skull",f_skull),("rocket",f_rocket),
("bell",f_bell((255,193,7,255),(200,140,0,255),False)),("bell_with_cancellation_stroke",f_bell((150,155,165,255),(100,105,118,255),True)),("gem_stone",f_gem),("large_blue_diamond",f_diamond),
("heavy_plus_sign",f_pm(True,GN,GND)),("heavy_minus_sign",f_pm(False,RD,RDD)),("heavy_large_circle",f_bigring),("open_lock",f_openlock),("droplet",f_drop),("bomb",f_bomb),("ticket",f_ticket),
("compass",f_compass),("floppy_disk",f_floppy),("headphone",f_phones),("magnifying_glass_left",f_mag(False)),("magnifying_glass_right",f_mag(True)),("books",f_books),("pushpin",f_pushpin),("round_pushpin",f_mappin),("link_symbol",f_link)]
for n,fn in jobs: save(n,fn)
