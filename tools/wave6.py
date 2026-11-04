import os
D=os.path.dirname(os.path.abspath(__file__))
exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read())
jobs=[("handshake",f_handw(_h_handshake,3)),("ballot_box_with_ballot",f_ballot),("performing_arts",f_masks),("wolf_face",f_wolf),("brain",f_brain),("sunrise",f_sunrise),("dumpling",f_dumpling),
("waving_hand_sign",f_wave),("sunset_over_buildings",f_sunset),("luggage",f_luggage),("delivery_truck",f_truck),("cityscape",f_city),("hammer_and_wrench",f_hamwr),("bow_and_arrow",f_bow),
("open_mailbox_raised_flag",f_mailbox(True)),("open_mailbox_lowered_flag",f_mailbox(False)),("flower_playing_cards",f_cards),("playing_card_black_joker",f_joker),("ring_buoy",f_buoy),
("bank",f_bank(True)),("classical_building",f_bank(False)),("studio_microphone",f_studiomic),("baby",f_baby),("coffin",f_coffin),("satellite_antenna",f_dish),("salt_shaker",f_salt),
("admission_tickets",f_tickets),("fork_and_knife_with_plate",f_fork),("pedestrian",f_ped),("chicken",f_chicken),("broom",f_broom),("folded_hands",f_pray),("japanese_ogre",f_ogre),
("shopping_trolley",f_cart),("stethoscope",f_steth),("drop_of_blood",f_dropc((200,30,45,255),(255,130,140,255))),("school_satchel",f_satchel),("flexed_biceps",f_flex),("shopping_bags",f_bags),
("vampire",f_vamp),("house_buildings",f_housebs),("spool_of_thread",f_spool),("speaker_three_sound_waves",f_speaker),("dagger_knife",f_dagger),("flag_indonesia",f_flagid),("satellite",f_satellite),
("convenience_store",f_store),("fishing_pole_and_fish",f_fishrod),("speaking_head",f_speakhead),("farmer",f_farmer),("womans_boots",f_boot),("chains",f_chains),("sleeping_accommodation",f_bed),
("desktop_computer",f_desktop),("office_building",f_office_b),("grapes",f_grapes),("hocho",f_knife),("paw_prints",f_paw),("identification_card",f_idcard),("man_judge",f_judge),
("man_office_worker",f_office(False)),("woman_office_worker",f_office(True)),("chair",f_chair),("hot_beverage",f_coffee),("clinking_glasses",f_clink),("baby_bottle",f_bottle),("red_gift_envelope",f_redenv),
("house_building",f_house(False)),("house_with_garden",f_house(True)),("cooking",f_pan),("infinity",f_inf),("pistol",f_pistol),("jigsaw_puzzle_piece",f_puzzle),("bug",f_bug),("syringe",f_syringe),
("man_with_turban",f_turban),("card_index_dividers",f_dividers),("person_raising_hand",f_hand_up),("family_man_woman_boy",f_family(3)),("family_man_woman_girl_boy",f_family(4)),
("clapper_board",f_clapper),("hole",f_hole),("money_with_wings",f_moneywing),("index_pointing_up",f_point),("file_cabinet",f_cabinet),
("thumbs_up_sign",f_handw(_h_thumb)),("ok_hand_sign",f_handw(_h_ok)),("runner",f_run),("standing_person",_scene(_p_stand,3)),("adult",f_adult),("footprints",f_foot),("sleuth_or_spy",f_spy),("mage",f_mage),("man_cooking",f_cook),
("standing_man",_scene(lambda d,t:person(d,0,.05,1.5,(88,101,242,255)),3)),("dotted_six_pointed_star",f_dstar)]
for n,fn in jobs:
    try: save(n,fn)
    except Exception as e: print("GAGAL",n,repr(e))
