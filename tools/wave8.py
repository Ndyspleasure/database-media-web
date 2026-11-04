import os
D=os.path.dirname(os.path.abspath(__file__))
exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read())
jobs=[("triangular_flag_on_post",f_flagpost),("face_without_mouth",f_nomouth),("camera_with_flash",f_camflash),("artist_palette",f_palette),("wastebasket",f_bin),("serious_face_symbols_mouth",f_serious),
("writing_hand",f_writing),("white_small_square",f_smallsq),("alien_monster",f_alien),("lady_beetle",f_ladybug),("backhand_index_pointing_down",f_pointdown)]
for n,fn in jobs: save(n,fn)
