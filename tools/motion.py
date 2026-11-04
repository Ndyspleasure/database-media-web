# ===== sistem animasi v2: intro/outro "pop", gerak berbasis fisika, aksi khas =====
def tf(im,sx=1,sy=1,rot=0,dx=0,dy=0,piv=(0,0),anc=(0,.5)):
    if rot: im=im.rotate(rot,resample=Image.BICUBIC,center=(S/2+piv[0]*K,S/2+piv[1]*K))
    if abs(sx-1)>1e-3 or abs(sy-1)>1e-3:
        w,h=max(1,int(S*sx)),max(1,int(S*sy)); sm=im.resize((w,h),Image.LANCZOS); ax,ay=S/2+anc[0]*K,S/2+anc[1]*K
        out=Image.new("RGBA",(S,S),(0,0,0,0)); out.paste(sm,(int(ax*(1-sx)),int(ay*(1-sy))),sm); im=out
    if dx or dy:
        out=Image.new("RGBA",(S,S),(0,0,0,0)); out.paste(im,(int(dx*K),int(dy*K)),im); im=out
    return im
def gb(u,c,w): return math.exp(-((u-c)/w)**2)
def staged(fn,a0=.12,a1=.88):
    def f(t):
        im=fn(clamp((t-a0)/(a1-a0)))
        if t<a0:
            p=t/a0; s=.15+.85*ease_out_back(p); k=1-p; return tf(im,s*(1-.14*k),s*(1+.14*k),-9*k,0,0)
        if t>a1:
            p=(t-a1)/(1-a1); s=1-.85*ease_in(p); return tf(im,s*(1+.12*p),s*(1-.12*p),6*p)
        return im
    return f
def add_glint(im,u,t0=.55,t1=.85,w=.3,a=170):
    if not(t0<u<t1): return im
    x0=-1.4+2.8*(u-t0)/(t1-t0); g,d=layer(); d.polygon([P(x0,-1.3),P(x0+w,-1.3),P(x0+w-.7,1.3),P(x0-.7,1.3)],fill=(255,255,255,a))
    g.putalpha(ImageChops.multiply(g.getchannel("A"),im.getchannel("A"))); out=im.copy(); out.alpha_composite(g); return out
def add_spark(im,u,x,y,st=.5,r=.2):
    p=clamp((u-st)/.22)
    if p<=0 or p>=1: return im
    out=im.copy(); d=ImageDraw.Draw(out); star4(d,x,y,r*math.sin(math.pi*p),W); return out
# --- motions: art(RGBA), u(0..1) -> RGBA ---
def m_hop(art,u,h=.25):
    sq=.13*gb(u,.1,.05)+.15*gb(u,.6,.045); air=math.sin(math.pi*clamp((u-.15)/.4)); st=.09*air
    return tf(art,1+sq-st,1-sq+st,0,0,-h*air)
def m_jelly(art,u):
    s=math.exp(-5*(u-.1))*math.sin(2*math.pi*3.2*(u-.1)) if u>.1 else 0; return tf(art,1+.17*s,1-.17*s)
def m_spiny(art,u):
    a=2*math.pi*ease_io(clamp((u-.1)/.6)); return tf(art,max(.05,abs(math.cos(a))),1,0,0,0,anc=(0,0))
def m_swing(art,u,piv=(0,-.6),amp=26):
    return tf(art,rot=amp*math.exp(-2.8*u)*math.cos(2*math.pi*2.2*u),piv=piv)
def m_tada(art,u):
    w=math.exp(-4*max(0,u-.3))*math.sin(2*math.pi*4*max(0,u-.3)) if u>.3 else 0
    s=1+.15*gb(u,.3,.1)-.07*gb(u,.15,.08); return tf(art,s,s,10*w,0,0,anc=(0,0))
def m_wave(art,u,piv=(0,.55),amp=24): return tf(art,rot=amp*math.sin(2*math.pi*3*u)*math.sin(math.pi*u)**.5,piv=piv)
def m_alert(art,u,amp=11,n=5):
    env=ease_io(clamp((u-.08)/.1))*(1-ease_io(clamp((u-.5)/.12))); return tf(art,1+.05*env,1+.05*env,amp*env*math.sin(2*math.pi*n*u),0,0,anc=(0,0))
def m_spin(art,u,deg=360,eased=True,mode=1): 
    p=ease_io(clamp((u-.05)/.6)) if eased else u; return tf(art,rot=deg*p,anc=(0,0))
def m_float(art,u): return tf(art,1,1,3*math.sin(2*math.pi*u+1),0,-.07*math.sin(2*math.pi*u))
def m_stamp(art,u):
    p=clamp(u/.2); s=1+.8*(1-ease_out_back(p)*0-p**2*0)*(1-ease_io(p)); sq=.14*gb(u,.22,.04)
    out=tf(art,s+sq,s-sq,0,0,0,anc=(0,0))
    if .2<u<.5: f=(u-.2)/.3; g,d=layer(); ring(d,.58+.5*f,(255,255,255,int(200*(1-f))),.06); out.alpha_composite(g)
    return m_alert(out,max(0,u-.45)*1.4,9,4) if u>.5 else out
def make_motion(fn,m,kw=None,g=True,sp=None):
    art=fn(0); kw=kw or {}
    def f(u):
        im=m(art,u,**kw)
        if g: im=add_glint(im,u)
        if sp: im=add_spark(im,u,*sp)
        return im
    return f
# --- ikon dengan aksi khas ---
def f_chev(ang,kind):
    def f(u):
        im,d=layer(); circle(d,.58,BL,BLD); l,e=layer()
        for k in range(3):
            x=-.75+1.5*((2*u+k/3)%1)
            if kind=='chev': thick_line(e,[(x-.12,-.24),(x+.1,0),(x-.12,.24)],.12,W)
            else: poly(e,[(x-.14,-.22),(x-.14,.22),(x+.16,0)],W,W,.05)
        mk=Image.new("L",(S,S),0); ImageDraw.Draw(mk).ellipse([S/2-.5*K,S/2-.5*K,S/2+.5*K,S/2+.5*K],fill=255); l.putalpha(ImageChops.multiply(l.getchannel("A"),mk)); im.alpha_composite(l)
        return tf(im,rot=ang,anc=(0,0)) if ang else im
    return f
def f_pm2(plus,col,dk):
    def f(u):
        im,d=layer(); circle(d,.58,col,dk); L=.3*ease_out_back(clamp((u-.05)/.3)); rr(d,-L,-.07,L,.07,.03,W)
        if plus: L2=.3*ease_out_back(clamp((u-.2)/.3)); rr(d,-.07,-L2,.07,L2,.03,W)
        if .6<u<1: f2=(u-.6)/.4; ring(d,.58+.25*f2,col[:3]+(int(255*(1-f2)),),.05)
        return tf(im,1+.04*gb(u,.55,.06),1+.04*gb(u,.55,.06),0,0,0,anc=(0,0))
    return f
def f_boom2(u):
    im,d=layer(); s=(.25+.9*ease_out_back(clamp(u/.3))) if u<.3 else 1.15-.2*clamp((u-.3)/.5); p1=[];p2=[]
    for i in range(16):
        a=math.radians(i*22.5-90); r=(.66 if i%2==0 else .34)*(1+.12*math.sin(i*2.3+u*9)); p1.append((s*r*math.cos(a),s*r*math.sin(a))); p2.append((s*r*.55*math.cos(a),s*r*.55*math.sin(a)))
    poly(d,p1,(255,110,30,255),(220,60,10,255),.03); poly(d,p2,(255,226,100,255))
    f=clamp((u-.1)/.55)
    if 0<f<1:
        ring(d,.3+.75*f,(255,200,80,255),.06*(1-f)+.01)
        for k in range(8): a=math.radians(k*45+10); r=.55+.6*f; ell(d,r*math.cos(a),r*math.sin(a),.05*(1-f)+.01,.05*(1-f)+.01,(255,230,120,255))
    return im
def f_note2(u):
    art=f_note(0); im=m_hop(art,u,.2); d=ImageDraw.Draw(im)
    for k in range(3):
        f=(u*1.2+k/3)%1; x=.45+.12*k+.06*math.sin(6*f+k); y=-.1-.6*f; r=.07*(1-.6*f)
        if f<.85: ell(d,x,y,r*1.3,r,BL); thick_line(d,[(x+r*1.2,y),(x+r*1.2,y-.2*(1-.5*f))],.025,BL)
    return im
def f_ghost2(u):
    im,d=layer(); dy=-.06*math.sin(2*math.pi*u); pts=[(.45*math.cos(math.radians(a)),-.05+.45*math.sin(math.radians(a))) for a in range(180,361,10)]
    pts+=[(.45-.9*i/8,.5+.07*math.sin(2*math.pi*u*2+i*1.3)) for i in range(9)]
    poly(d,pts,(245,247,252,255),(170,175,195,255),.03); b=bl(u,.4); [ell(d,x,-.1,.06,.08*b,DK) for x in(-.17,.17)]; m=.07+.03*math.sin(2*math.pi*u*2); ell(d,0,.1,m,m*1.3,DK)
    ell(d,-.3,.02,.07,.04,(255,200,210,255)); ell(d,.3,.02,.07,.04,(255,200,210,255)); return tf(im,1,1,4*math.sin(2*math.pi*u),.03*math.sin(2*math.pi*u),dy)
def _gear(d,cx,cy,r,n,ang,col,dk):
    pts=[]; st=2*math.pi/n
    for i in range(n):
        a=ang+i*st
        for off,rad in((-.32,r),(-.2,r*1.28),(.2,r*1.28),(.32,r)): pts.append((cx+rad*math.cos(a+off*st),cy+rad*math.sin(a+off*st)))
    poly(d,pts,col,dk,.03); ell(d,cx,cy,r*.95,r*.95,col,dk,.03); ell(d,cx,cy,r*.4,r*.4,(0,0,0,0))
def f_gear2(u):
    im,d=layer(); a=math.radians(90*u)
    _gear(d,-.2,.15,.36,8,a,(150,160,175,255),GRD); _gear(d,.33,-.3,.22,6,-a*8/6+math.radians(30),(88,101,242,255),BLD); return im
def f_wrench2(u):
    im,d=layer(); a=45*ease_io(clamp(u/.4)) if u<.4 else 45*(1-ease_io(clamp((u-.4)/.1)))
    l,e=layer(); rr(e,-.07,0,.07,.7,.07,GR,GRD,.03); ell(e,0,0,.26,.26,GR,GRD,.03); rr(e,-.11,-.4,.11,-.08,0,(0,0,0,0)); poly(e,[(.13*math.cos(math.radians(60*k)),.13*math.sin(math.radians(60*k))) for k in range(6)],(255,193,7,255),(200,140,0,255),.02)
    out=tf(l,rot=a-35,dy=-.2,dx=.1)
    if .36<u<.5: d2=ImageDraw.Draw(out); star4(d2,.1,-.2,.2*math.sin(math.pi*(u-.36)/.14),W)
    return tf(out,1.3,1.3,anc=(0,0))
def f_hammer2(u):
    if u<.3: a=60*ease_io(u/.3)
    elif u<.36: a=60+6*(u-.3)/.06
    elif u<.45: a=66-92*ease_in((u-.36)/.09)
    else: a=-26+6*ease_io(clamp((u-.45)/.2))
    l,e=layer(); rr(e,-.05,-.7,.05,0,.03,BR,BRD,.02); rr(e,-.3,-.82,.3,-.56,.06,GR,GRD,.03); rr(e,-.24,-.78,-.1,-.6,.03,(210,218,228,255))
    out=tf(l,rot=a); g,d=layer(); rr(d,.3,-.5,.78,-.36,.03,(90,95,110,255),GRD,.02); out.alpha_composite(g)
    if .44<u<.62: d2=ImageDraw.Draw(out); f=(u-.44)/.18; star4(d2,.45,-.6,.35*math.sin(math.pi*f),(255,230,120,255)); ell(d2,.45,-.6,.06*(1-f),.06*(1-f),W)
    return tf(tf(out,dx=-.15,dy=.3),1.3,1.3,anc=(0,0))
CUSTOM={"gear":f_gear2,"wrench":f_wrench2,"hammer":f_hammer2,"collision_symbol":f_boom2,"musical_note":f_note2,"ghost":f_ghost2,
"heavy_plus_sign":f_pm2(True,(46,204,113,255),(30,160,86,255)),"heavy_minus_sign":f_pm2(False,(231,60,60,255),(185,40,40,255)),
"black_right_pointing_triangle":f_chev(0,'tri'),"black_left_pointing_triangle":f_chev(180,'tri'),"black_rightwards_arrow":f_chev(0,'chev'),"leftwards_black_arrow":f_chev(180,'chev'),"upwards_black_arrow":f_chev(90,'chev')}
RAW={"check","cross_mark","bar_chart","chart_with_upwards_trend","chart_with_downwards_trend","seedling","rainbow","direct_hit","memo","page_facing_up","scroll","door","incoming_envelope","ballot_box_with_ballot","inbox_tray","outbox_tray","bow_and_arrow","sunrise","collision_symbol","heavy_plus_sign","heavy_minus_sign","hammer","wrench"}
def _M(m,kw=None,g=True,sp=None): return (m,kw or {},g,sp)
MAP={}
for n in ("large_yellow_square","large_blue_square","large_purple_square","large_green_square","white_large_square","black_large_square","large_blue_diamond","playing_card_black_joker","flower_playing_cards","identification_card","squared_id","squared_new","a_button_blood_type","b_button_blood_type","input_numbers","input_latin_letters","ticket","banknote_with_dollar_sign"): MAP[n]=_M(m_spiny)
for n in [f"keycap_{i}" for i in range(1,9)]+["black_question_mark_ornament","white_question_mark_ornament","money_bag","jigsaw_puzzle_piece","japanese_ogre","cactus","file_cabinet","hole","house_building","house_with_garden","house_buildings","bank","classical_building","church","convenience_store","brick","vampire"]: MAP[n]=_M(m_jelly,sp=(.4,-.5,.55))
for n in ("package","briefcase","luggage","school_satchel","toolbox","basket","bread","cookie","red_apple","banana","watermelon","strawberry","lemon","carrot","mushroom","slice_of_pizza","grapes","pineapple","peach","ear_of_maize","doughnut","baby_bottle","chair","baby","adult","man_office_worker","woman_office_worker","man_cooking","man_with_turban","farmer","shopping_trolley","womans_boots"): MAP[n]=_M(m_hop,sp=(.42,-.5,.62))
for n in ("red_gift_envelope","heart_with_ribbon","fork_and_knife_with_plate","newspaper","billed_cap"): MAP[n]=_M(m_tada,sp=(.45,-.5,.5))
MAP["tear_off_calendar"]=_M(m_swing,{"piv":(0,-.6)}); MAP["label"]=_M(m_swing,{"piv":(-.25,0),"amp":30}); MAP["closed_umbrella"]=_M(m_wave,{"piv":(0,.6),"amp":14}); MAP["rose"]=_M(m_wave,{"piv":(0,.65),"amp":10}); MAP["coffin"]=_M(m_wave,{"piv":(0,.68),"amp":8})
MAP["waving_hand_sign"]=_M(m_wave,{"amp":28},g=False); MAP["broom"]=_M(m_wave,{"piv":(0,-.7),"amp":16})
MAP["cyclone"]=_M(m_spin,{"deg":360,"eased":False},g=False); MAP["recycling_symbol"]=_M(m_spin,{"deg":120}); MAP["anticlockwise_arrows_button"]=_M(m_spin,{"deg":360},g=False); MAP["dotted_six_pointed_star"]=_M(m_spin,{"deg":60}); MAP["ring_buoy"]=_M(m_spin,{"deg":90})
MAP["telephone_receiver"]=_M(m_alert,{"amp":14,"n":7},g=False); MAP["octagonal_sign"]=_M(m_alert); MAP["no_entry"]=_M(m_stamp); MAP["no_entry_sign"]=_M(m_stamp)
MAP["small_red_triangle_down"]=_M(m_hop,{"h":-.12},g=False)
