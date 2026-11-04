import os
D=os.path.dirname(os.path.abspath(__file__))
exec(open(D+"/common.py").read()); exec(open(D+"/icons.py").read())
KC=((232,236,252,255),BL)
jobs=[(f"keycap_{n}",f_label(str(n),KC[0],KC[1],200,BL)) for n in range(1,9)]
jobs+=[("fast_forward",f_media(m_ff)),("rewind",f_media(m_ff,180)),("next_track_button",f_media(m_next)),("double_vertical_bar",f_media(m_pause)),
("recycling_symbol",f_recycle),("repeat_button",f_repeat),("leftwards_arrow_with_hook",f_hook),
("clock_face_three_oclock",f_clockf(90)),("clock_face_one_oclock",f_clockf(30)),("stopwatch",f_stopw),
("full_moon_symbol",f_fullmoon),("new_moon_symbol",f_newmoon),("black_sun_with_rays",f_sun),
("calendar",f_cal),("tear_off_calendar",f_tear),("radio_button",f_radio),
("squared_id",f_label("ID",BL,BLD,150)),("input_numbers",f_label("1234",BL,BLD,72)),("input_latin_letters",f_label("abc",BL,BLD,105)),("squared_new",f_label("NEW",(46,204,113,255),(30,160,86,255),88)),
("a_button_blood_type",f_label("A",(231,60,60,255),(185,40,40,255),260)),("b_button_blood_type",f_label("B",(231,60,60,255),(185,40,40,255),260)),
("broken_heart",f_broken),("sparkling_heart",f_sparkheart),("heart_with_arrow",f_heartarrow),("heart_with_ribbon",f_heartribbon),("revolving_hearts",f_revolve),
("party_popper",f_popper),("confetti_ball",f_confball),("collision_symbol",f_boom),("dizzy_symbol",f_dizzy),("police_car_light",f_siren),
("incoming_envelope",f_env('in')),("e_mail_symbol",f_env('at')),("envelope_with_arrow",f_env('arrow')),("blue_book",f_bbook),("scroll",f_scroll),("page_facing_up",f_page),
("inbox_tray",f_tray(True)),("outbox_tray",f_tray(False)),("open_file_folder",f_folder),
("crossed_swords",f_swords),("scales",f_scales),("hourglass",f_hourb),("musical_note",f_note),("multiple_musical_notes",f_notes),("four_leaf_clover",f_clover),
("chequered_flag",f_flag),("rainbow",f_rainbow),("banknote_with_dollar_sign",f_banknote),("european_castle",f_castle),("busts_in_silhouette",f_bust(2)),("bust_in_silhouette",f_bust(1))]
for n,fn in jobs: save(n,fn)
