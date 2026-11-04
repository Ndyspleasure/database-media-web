import os
D=os.path.dirname(os.path.abspath(__file__))
exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read())
jobs=[("smiling_face_smiling_eyes",f_face('smile_eyes')),("pensive_face",f_face('pensive')),("pouting_face",f_face('angry')),("anxious_face_with_sweat",f_face('anxious')),("grinning_smiling_eyes",f_face('grin')),
("neutral_face",f_face('neutral')),("flushed_face",f_face('flushed')),("grinning_face_sweat",f_face('sweat')),("thinking_face",f_face('think')),("loudly_crying_face",f_face('cry')),("confounded_face",f_face('confound')),
("smiling_face_with_halo",f_face('halo')),("face_with_cowboy_hat",f_face('cowboy')),("sleeping_face",f_face('sleep')),("shushing_face",f_face('shush')),("dark_sunglasses",f_shades),("eyes",f_eyes),("ghost",f_ghost),
("dog_face",f_dog),("cat_face",f_cat),("mouse_face",f_mouse),("rabbit_face",f_rabbit),("fox_face",f_fox),("bear_face",f_bear),("panda_face",f_panda),("frog_face",f_frog),("monkey_face",f_monkey),("penguin",f_penguin),("tropical_fish",f_fish),("butterfly",f_butter),
("red_apple",f_apple),("banana",f_banana),("watermelon",f_melon),("strawberry",f_straw),("cherries",f_cherry),("lemon",f_lemon),("carrot",f_carrot),("mushroom",f_mush),("slice_of_pizza",f_pizza),("hamburger",f_burger),("doughnut",f_donut),("soft_ice_cream",f_icecream),("cookie",f_cookie),("birthday_cake",f_cake),
("skull_and_crossbones",f_skullx),("microphone",f_mic),("television",f_tv),("camera",f_camera),("telephone_receiver",f_receiver),("test_tube",f_tube),("crystal_ball",f_ball2),("candle",f_candle),("ring",f_ring),("rose",f_rose),("seedling",f_seedling),("cherry_blossom",f_blossom),("soccer_ball",f_soccer),("balloon",f_balloon)]
for n,fn in jobs: save(n,fn)
