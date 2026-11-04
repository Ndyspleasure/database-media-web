import os
D=os.path.dirname(os.path.abspath(__file__))
exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read())
jobs=[("frame_with_picture",f_frame),("factory",f_factory),("personal_computer",f_laptop),("hotel",f_hotel),("hospital",f_hospital),("passenger_ship",f_ship),("steam_locomotive",f_train),("snow_capped_mountain",f_mountain),
("slot_machine",f_slot),("microscope",f_micro),("dna_double_helix",f_dna),("movie_camera",f_moviecam),("ballpoint_pen",f_pen),("mantelpiece_clock",f_mantel),("flashlight",f_flash),("pager",f_pager),("billed_cap",f_cap),
("love_letter",f_loveletter),("gloves",f_gloves),("receipt",f_receipt),("smoking_symbol",f_cig),("window",f_window),("closed_umbrella",f_umbrella),("small_red_triangle_down",f_tridown),("keyboard",f_keyboard),
("cup_with_straw",f_cupstraw),("cooked_rice",f_rice),("bread",f_bread),("glass_of_milk",f_milk),("steaming_bowl",f_noodle),("pot_of_food",f_pot),("curry_and_rice",f_curry),("cut_of_meat",f_meat),("chocolate_bar",f_choco),
("teddy_bear",f_teddy),("toolbox",f_toolbox),("antenna_with_bars",f_antbars),("basket",f_basket),("bridge_at_night",f_bridge),("mosque",f_mosque),("sailboat",f_sailboat),("tokyo_tower",f_tokyo),("motor_scooter",f_scooter),
("department_store",f_dept),("airplane",f_plane),("newspaper",f_news),("radio",f_radiodev),("three_button_mouse",f_mouse3),("nazar_amulet",f_nazar),("brick",f_brick),("church",f_church),("mouse_trap",f_mousetrap),
("cyclone",f_cyclone),("black_nib",f_nib),("dash_symbol",f_dash),("safety_vest",f_vest),("latin_cross",f_latin),("microbe",f_microbe),("horse_face",f_horse),("waving_black_flag",f_blackflag),("dove_of_peace",f_dove),
("biohazard_sign",f_bio),("joystick",f_joy),("label",f_tag),("pineapple",f_pine),("mango",f_mango),("peach",f_peach),("ear_of_maize",f_corn),("turtle",f_turtle),("octopus",f_octopus),("honeybee",f_bee),
("sunflower",f_sunflower),("cactus",f_cactus),("guitar",f_guitar),("automobile",f_car)]
for n,fn in jobs:
    try: save(n,fn)
    except Exception as e: print("GAGAL",n,repr(e))
