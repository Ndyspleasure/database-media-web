def f_bars(t):
    im,d=layer(); rr(d,-.66,.52,.66,.58,.03,(150,155,165,255))
    for i,(x,h,c) in enumerate([(-.4,.55,(88,101,242,255)),(0,.95,(46,204,113,255)),(.4,.72,(255,159,28,255))]):
        g=ease_out_back((t-.08*i)/.35); 
        if t>.85: g*=1-ease_in((t-.85)/.15)
        hh=max(.02,h*g); rr(d,x-.13,.52-hh,x+.13,.52,.05,c)
    return im
def f_trophy(t):
    im,d=layer(); gold=(255,193,7,255); dk=(200,140,0,255)
    d.arc([P(-.6,-.45),P(-.26,-.0)],90,270,fill=dk,width=int(.07*K)); d.arc([P(.26,-.45),P(.6,-.0)],270,450,fill=dk,width=int(.07*K))
    poly(d,[(-.38,-.52),(.38,-.52),(.36,-.15),(.22,.07),(-.22,.07),(-.36,-.15)],gold,dk)
    rr(d,-.07,.05,.07,.32,.02,dk); rr(d,-.28,.3,.28,.46,.05,(160,100,30,255))
    poly(d,[(-.28,-.44),(-.17,-.44),(-.2,-.1),(-.28,-.14)],(255,226,120,255))
    star4(d,.42,-.5,.2*twinkle(t),(255,255,255,255)); star4(d,-.5,.1,.14*twinkle(t,.5),(255,240,150,255))
    return xform(im,1+.04*sg(t),3*sg(t))
def f_shield(t):
    im,d=layer(); ripple(d,t,(88,140,250,255))
    def sh(k):
        pts=[(-.5*k,-.45*k),(0,-.6*k),(.5*k,-.45*k)]
        for i in range(0,13): a=i/12*math.pi/2; pts.append((.5*k*math.cos(a),.68*k*math.sin(a)))
        pts+= [(-x,y) for x,y in reversed(pts[3:])]
        return pts
    poly(d,sh(1),(52,101,214,255),(30,70,170,255)); poly(d,sh(.8),(88,140,250,255))
    thick_line(d,partial([(-.2,.0),(-.05,.17),(.22,-.15)],ease_io((t-.1)/.3)),.12,(255,255,255,255))
    return xform(im,1+.05*sg(t))
def f_robot(t):
    im,d=layer(); on=(t%.5)<.25
    thick_line(d,[(0,-.3),(0,-.48)],.05,(90,100,115,255)); ell(d,0,-.54,.08,.08,(255,80,80,255) if on else (120,40,40,255))
    rr(d,-.56,-.06,-.42,.22,.04,(110,120,135,255)); rr(d,.42,-.06,.56,.22,.04,(110,120,135,255))
    rr(d,-.45,-.3,.45,.4,.12,(160,170,185,255),(90,100,115,255)); rr(d,-.35,-.2,.35,.25,.07,(40,48,62,255))
    ry=.1*(.12 if abs(t-.7)<.05 else 1)
    ell(d,-.18,0,.09,ry,(80,230,255,255)); ell(d,.18,0,.09,ry,(80,230,255,255)); rr(d,-.14,.11,.14,.16,.02,(80,230,255,255))
    return xform(im,1,4*sg(t),0,.03*sg(2*t))
def f_stop(t):
    im,d=layer()
    poly(d,[(.68*math.cos(math.radians(i*45+22.5)),.68*math.sin(math.radians(i*45+22.5))) for i in range(8)],(255,255,255,255))
    poly(d,[(.6*math.cos(math.radians(i*45+22.5)),.6*math.sin(math.radians(i*45+22.5))) for i in range(8)],(220,40,40,255))
    rr(d,-.3,-.07,.3,.07,.04,(255,255,255,255)); return xform(im,1+.06*sg(t))
def f_lock(t):
    im,d=layer()
    off=.16*(1-ease_io(t/.25)) if t<.25 else (.16*ease_io((t-.85)/.15) if t>.85 else 0)
    sc=(170,178,190,255); d.arc([P(-.25,-.5-off),P(.25,0-off)],180,360,fill=sc,width=int(.09*K))
    for x in (-.25,.25): d.line([P(x,-.25-off),P(x,-.02)],fill=sc,width=int(.09*K))
    rr(d,-.38,-.05,.38,.5,.1,(255,193,7,255),(200,140,0,255)); ell(d,0,.18,.07,.07,(60,40,10,255)); rr(d,-.03,.18,.03,.34,.01,(60,40,10,255))
    shake=7*math.sin((t-.3)*30)*clamp(1-(t-.3)*5) if .3<t<.5 else 0
    return xform(im,1,shake)
def f_play(t):
    im,d=layer(); ripple(d,t,(88,101,242,255)); circle(d,.55,(88,101,242,255),(60,70,200,255))
    poly(d,[(-.12,-.26),(.28,0),(-.12,.26)],(255,255,255,255),(255,255,255,255),.07)
    return xform(im,1+.04*sg(t),0,.02*sg(t))
def f_info(t):
    im,d=layer(); ripple(d,t,(52,152,219,255)); circle(d,.55,(52,152,219,255),(30,110,170,255))
    ell(d,0,-.24,.075,.075,(255,255,255,255)); rr(d,-.07,-.08,.07,.3,.04,(255,255,255,255))
    return xform(im,1+.05*sg(t))
def flame(d,h,w,col,sway,oy,t):
    R=[];L=[]
    for i in range(25):
        u=i/24; y=oy-h+u*1.9*h; wp=w*1.6*u*(1-u**4)**.5; xo=sway*(1-u)**2
        R.append((xo+wp,y)); L.append((xo-wp,y))
    poly(d,R+L[::-1],col)
def f_fire(t):
    im,d=layer(); hf=1+.06*sg(2*t)
    flame(d,.62*hf,.42,(255,100,20,255),.1*sg(t),-.02,t); flame(d,.46*hf,.3,(255,170,30,255),.07*sg(t+.2),.14,t); flame(d,.28*hf,.18,(255,235,110,255),.05*sg(2*t),.28,t)
    return im
def f_crown(t):
    im,d=layer(); gold=(255,193,7,255); dk=(200,140,0,255)
    poly(d,[(-.5,.34),(-.58,-.32),(-.22,-.02),(0,-.5),(.22,-.02),(.58,-.32),(.5,.34)],gold,dk)
    rr(d,-.5,.34,.5,.5,.05,(230,165,0,255),dk)
    for x,y,c in [(-.58,-.34,(231,76,60,255)),(0,-.52,(52,152,219,255)),(.58,-.34,(46,204,113,255))]: ell(d,x,y,.07,.07,c)
    for x,c in [(-.25,(231,76,60,255)),(0,(52,152,219,255)),(.25,(46,204,113,255))]: ell(d,x,.42,.05,.05,c)
    star4(d,.3,-.2,.2*twinkle(t),(255,255,255,255)); return xform(im,1+.04*sg(t),3*sg(t))
def f_heart(t):
    a=lambda c,w: math.exp(-((t-c)/w)**2); s=1+.14*a(.15,.06)+.1*a(.35,.06)
    im,d=layer(); pts=[]
    for i in range(80):
        u=i/80*2*math.pi; pts.append((.034*16*math.sin(u)**3*1.0, -.034*(13*math.cos(u)-5*math.cos(2*u)-2*math.cos(3*u)-math.cos(4*u))+.05))
    poly(d,pts,(235,50,75,255),(190,30,55,255)); ell(d,-.26,-.22,.12,.07,(255,130,150,255))
    return xform(im,s)
def f_ball(col,dk,hl):
    def f(t):
        im,d=layer(); ripple(d,t,col); circle(d,.55,col,dk); ell(d,-.2,-.25,.17,.09,hl); return xform(im,1+.05*sg(t))
    return f

# ===== gelombang 2 =====
def f_sq(col,dk,hl):
    def f(t):
        im,d=layer(); rr(d,-.55,-.55,.55,.55,.14,col,dk,.04); rr(d,-.42,-.46,-.12,-.36,.05,hl); return xform(im,1+.05*sg(t),3*sg(t))
    return f
def f_medal(col,dk,hi,num):
    def f(t):
        im,d=layer()
        poly(d,[(-.3,-.62),(-.08,-.62),(.1,-.05),(-.12,-.05)],(52,120,246,255)); poly(d,[(.3,-.62),(.08,-.62),(-.1,-.05),(.12,-.05)],(231,76,60,255))
        ell(d,0,.22,.4,.4,col,dk,.05); ell(d,0,.22,.29,.29,hi)
        pts={1:[(-.07,.12),(.05,.05),(.05,.38)],2:[(-.1,.1),(0,.04),(.1,.1),(.08,.2),(-.1,.38),(.1,.38)],3:[(-.1,.08),(.09,.08),(-.01,.2),(.1,.27),(.08,.37),(-.1,.36)]}
        if num: thick_line(d,pts[num],.08,dk)
        else: star4(d,0,.22,.25,(255,255,255,255))
        star4(d,.38,-.02,.18*twinkle(t),(255,255,255,255))
        return xform(im,1,5*sg(t))
    return f
def f_arrow(ang):
    def f(t):
        im,d=layer(); circle(d,.58,(88,101,242,255),(60,70,200,255)); dx=.05*sg(t)
        poly(d,[(-.3+dx,-.1),(.05+dx,-.1),(.05+dx,-.28),(.38+dx,0),(.05+dx,.28),(.05+dx,.1),(-.3+dx,.1)],(255,255,255,255),(255,255,255,255),.05)
        return xform(im,1,ang)
    return f
def f_playl(t): return xform(f_play(t),1,180)
def f_target(t):
    im,d=layer()
    for r,c in [(.58,(231,60,60,255)),(.44,(255,255,255,255)),(.31,(231,60,60,255)),(.18,(255,255,255,255)),(.07,(231,60,60,255))]: circle(d,r,c)
    f=1-ease_io(t/.2) if t<.2 else (ease_io((t-.85)/.15) if t>.85 else 0)
    ox,oy=.9*f,-.9*f
    thick_line(d,[(ox,oy),(ox+.5,oy-.5)],.05,(60,64,75,255)); poly(d,[(ox+.38,oy-.38),(ox+.66,oy-.46),(ox+.46,oy-.66)],(88,101,242,255))
    return xform(im,1+(.06*math.sin(math.pi*(t-.2)/.1) if .2<t<.3 else 0))
def f_moon(t):
    im,d=layer(); ell(d,-.05,0,.55,.55,(255,213,79,255)); ell(d,.25,-.14,.48,.48,(0,0,0,0))
    star4(d,.42,-.45,.17*twinkle(t),(255,240,150,255)); star4(d,.5,.25,.12*twinkle(t,.5),(255,240,150,255)); return xform(im,1,6*sg(t))
def f_bulb(t):
    im,d=layer(); p=sg(t); k=p*.5+.5
    for i in range(7):
        a=math.radians(-180+i*30); r0=.58+.03*p; r1=r0+.12+.05*p
        thick_line(d,[(r0*math.cos(a),r0*math.sin(a)-.12),(r1*math.cos(a),r1*math.sin(a)-.12)],.05,(255,213,40,255))
    col=(255,int(215+20*k),int(60+30*k),255); ell(d,0,-.12,.38,.38,col); poly(d,[(-.2,.1),(.2,.1),(.15,.38),(-.15,.38)],col)
    rr(d,-.17,.36,.17,.46,.03,(150,155,165,255)); rr(d,-.12,.46,.12,.55,.03,(100,105,115,255))
    thick_line(d,[(-.1,0),(-.05,-.15),(0,-.05),(.05,-.15),(.1,0)],.03,(200,140,0,255)); ell(d,-.17,-.26,.06,.1,(255,250,200,255)); return im
def f_bolt(t):
    im,d=layer(); c=(255,250,190,255) if twinkle(t)>.5 else (255,214,0,255)
    poly(d,[(.12,-.65),(-.38,.08),(-.05,.08),(-.18,.65),(.38,-.12),(.05,-.12)],c,(230,150,0,255),.04); return xform(im,1+.07*sg(2*t),4*sg(t))
def f_alarm(t):
    im,d=layer()
    for x in (-1,1): ell(d,x*.38,-.45,.17,.17,(220,50,50,255),(170,30,30,255)); thick_line(d,[(x*.3,.45),(x*.42,.62)],.07,(90,95,105,255))
    ell(d,0,.04,.5,.5,(255,255,255,255),(220,50,50,255),.08)
    for i in range(12):
        a=i*math.pi/6; thick_line(d,[(.4*math.sin(a),.04-.4*math.cos(a)),(.45*math.sin(a),.04-.45*math.cos(a))],.025,(90,95,105,255))
    a=2*math.pi*t; thick_line(d,[(0,.04),(.34*math.sin(a),.04-.34*math.cos(a))],.04,(60,64,75,255))
    thick_line(d,[(0,.04),(.22*math.sin(2.2),.04-.22*math.cos(2.2))],.06,(60,64,75,255)); ell(d,0,.04,.05,.05,(220,50,50,255))
    return xform(im,1,4*math.sin(2*math.pi*6*t))
def star5(d,cx,cy,R,r,fill,outline=None):
    poly(d,[(cx+(R if i%2==0 else r)*math.cos(math.radians(-90+36*i)),cy+(R if i%2==0 else r)*math.sin(math.radians(-90+36*i))) for i in range(10)],fill,outline,.04)
def f_star(t):
    im,d=layer(); star5(d,0,.04,.66,.28,(255,214,0,255),(230,150,0,255)); star4(d,-.18,-.12,.16*twinkle(t),(255,255,255,255)); return xform(im,1+.07*sg(t),12*sg(t))
def f_gstar(t):
    im,d=layer(); star5(d,0,.04,.52,.23,(255,225,60,255),(240,160,0,255))
    star4(d,.55,-.5,.22*twinkle(t),(255,240,120,255)); star4(d,-.58,.3,.18*twinkle(t,.35),(255,240,120,255)); star4(d,.5,.52,.15*twinkle(t,.7),(255,240,120,255)); return xform(im,1+.05*sg(t),8*sg(t))
def f_sparkles(t):
    im,d=layer(); c=(255,214,0,255)
    star4(d,-.2,.1,.5*(.7+.3*sg(t)),c); star4(d,.38,-.35,.3*(.7+.3*sg(t+.33)),c); star4(d,.34,.45,.22*(.7+.3*sg(t+.66)),c); return im
def f_coin(t):
    im,d=layer(); rx=max(.06,.55*abs(math.cos(2*math.pi*t))); ell(d,0,0,rx,.55,(255,193,7,255),(200,140,0,255),.05)
    if rx>.15: ell(d,0,0,rx*.78,.43,None,(230,165,0,255),.03)
    rr(d,-.06*rx/.55,-.2,.06*rx/.55,.2,0,(230,165,0,255)); return im
def f_speech(t):
    im,d=layer(); poly(d,[(-.32,.2),(-.08,.2),(-.38,.52)],(88,101,242,255),(60,70,200,255)); rr(d,-.6,-.48,.6,.26,.26,(88,101,242,255),(60,70,200,255),.04)
    for i,x in enumerate((-.28,0,.28)): ell(d,x,-.11-.1*max(0,math.sin(2*math.pi*(t-i*.12))),.075,.075,(255,255,255,255))
    return im
def f_gift(t):
    im,d=layer(); h=.1*abs(math.sin(4*math.pi*t)) if t<.5 else 0; y=(255,214,0,255)
    rr(d,-.5,-.02,.5,.55,.05,(231,76,60,255),(185,50,40,255)); rr(d,-.07,-.02,.07,.55,0,y)
    rr(d,-.56,-.25-h,.56,-h,.04,(210,60,50,255),(170,40,35,255)); rr(d,-.07,-.25-h,.07,-h,0,y)
    ell(d,-.15,-.36-h,.15,.1,None,y,.05); ell(d,.15,-.36-h,.15,.1,None,y,.05); ell(d,0,-.32-h,.06,.06,y); return im
def f_book(t):
    im,d=layer(); poly(d,[(0,-.4),(-.6,-.5),(-.6,.4),(0,.5),(.6,.4),(.6,-.5)],(120,80,50,255))
    poly(d,[(0,-.35),(-.55,-.45),(-.55,.35),(0,.45)],(250,245,230,255)); poly(d,[(0,-.35),(.55,-.45),(.55,.35),(0,.45)],(245,238,215,255))
    for k in range(4):
        y=-.2+.15*k; thick_line(d,[(-.45,y-.03),(-.1,y)],.03,(170,160,140,255)); thick_line(d,[(.1,y),(.45,y-.03)],.03,(170,160,140,255))
    p=ease_io((t-.1)/.3) if t<.5 else 1-ease_io((t-.6)/.3); xo=.55*math.cos(math.pi*p)
    poly(d,[(0,-.35),(xo,-.45),(xo,.35),(0,.45)],(255,252,240,255),(200,190,170,255),.02); return im
def f_q(col):
    def f(t):
        im,d=layer(); d.arc([P(-.3,-.58),P(.3,.02)],180,450,fill=col,width=int(.15*K)); thick_line(d,[(0,.02),(0,.14)],.15,col); ell(d,0,.4,.085,.085,col)
        return xform(im,1+.04*sg(t),8*sg(t))
    return f
def f_cycle(t):
    im,d=layer(); col=(88,101,242,255)
    for s0 in (20,200):
        d.arc([P(-.45,-.45),P(.45,.45)],s0+30,s0+150,fill=col,width=int(.12*K)); a=math.radians(s0+30); c=(.45*math.cos(a),.45*math.sin(a)); tt=(math.sin(a),-math.cos(a)); n=(math.cos(a),math.sin(a))
        poly(d,[(c[0]+tt[0]*.22,c[1]+tt[1]*.22),(c[0]+n[0]*.17,c[1]+n[1]*.17),(c[0]-n[0]*.17,c[1]-n[1]*.17)],col)
    return xform(im,1,360*t)
def f_heartc(fill,outline,hl):
    def f(t):
        a=lambda c,w: math.exp(-((t-c)/w)**2); s=1+.14*a(.15,.06)+.1*a(.35,.06); im,d=layer(); pts=[]
        for i in range(80):
            u=i/80*2*math.pi; pts.append((.034*16*math.sin(u)**3,-.034*(13*math.cos(u)-5*math.cos(2*u)-2*math.cos(3*u)-math.cos(4*u))+.05))
        poly(d,pts,fill,outline); ell(d,-.26,-.22,.12,.07,hl); return xform(im,s)
    return f
def f_nosign(t):
    im,d=layer(); ring(d,.55,(231,60,60,255),.13); thick_line(d,[(-.39,-.39),(.39,.39)],.13,(231,60,60,255)); return xform(im,1+.05*sg(t))
def f_noentry(t):
    im,d=layer(); circle(d,.6,(231,60,60,255),(185,40,40,255)); rr(d,-.35,-.08,.35,.08,.04,(255,255,255,255)); return xform(im,1+.05*sg(t))

# ===== gelombang 3 =====
from PIL import ImageChops, ImageFont
try: FONT=ImageFont.truetype("DejaVuSans-Bold.ttf",190)
except Exception: FONT=None
GR=(150,160,175,255); GRD=(95,105,120,255)
def f_wrench(t):
    im,d=layer(); rr(d,-.08,-.12,.08,.62,.08,GR,GRD,.03); ell(d,0,-.34,.24,.24,GR,GRD,.03); rr(d,-.1,-.66,.1,-.36,0,(0,0,0,0)); return xform(im,1,45+14*sg(t))
def f_hammer(t):
    im,d=layer(); rr(d,-.06,-.3,.06,.62,.03,(160,100,50,255),(110,65,30,255)); rr(d,-.4,-.55,.4,-.22,.06,GR,GRD,.03); rr(d,-.34,-.5,-.18,-.27,.03,(210,218,228,255)); return xform(im,1,15+25*sg(t))
def f_gear(t):
    im,d=layer()
    for i in range(8):
        a=i*math.pi/4; thick_line(d,[(.36*math.cos(a),.36*math.sin(a)),(.54*math.cos(a),.54*math.sin(a))],.2,GR)
    ell(d,0,0,.45,.45,GR,GRD,.03); ell(d,0,0,.18,.18,(0,0,0,0)); return xform(im,1,45*t)
def f_package(t):
    im,d=layer(); rr(d,-.5,-.25,.5,.5,.04,(205,150,90,255),(150,100,50,255)); rr(d,-.58,-.45,.58,-.2,.04,(185,130,70,255),(140,90,45,255)); rr(d,-.1,-.45,.1,.5,0,(235,210,150,255)); rr(d,.18,.08,.42,.36,.02,(255,255,255,255),(200,200,200,255),.02)
    return xform(im,1,0,0,-.08*abs(math.sin(2*math.pi*t)))
def f_door(t):
    im,d=layer(); a=math.radians(75*(ease_io((t-.1)/.25) if t<.5 else 1-ease_io((t-.7)/.2)))
    rr(d,-.42,-.62,.42,.62,.04,(100,65,35,255)); rr(d,-.34,-.54,.34,.62,0,(255,226,120,255)); w=.68*math.cos(a); ph=.08*math.sin(a)
    poly(d,[(-.34,-.54),(-.34+w,-.54+ph*2),(-.34+w,.62-ph*2),(-.34,.62)],(170,110,60,255),(120,75,40,255),.02); ell(d,-.34+w-.08*math.cos(a),.05,.04,.04,(255,214,0,255)); return im
def f_phone(t):
    im,d=layer(); dx=.03*math.sin(16*math.pi*t) if t<.5 else 0
    rr(d,-.3,-.58,.3,.58,.08,(45,48,55,255),(20,22,26,255)); rr(d,-.24,-.46,.24,.42,.03,(88,101,242,255)); rr(d,-.15,-.3,.15,-.12,.05,(255,255,255,255)); rr(d,-.15,-.06,.1,.12,.05,(255,255,255,255)); ell(d,0,.5,.035,.035,(130,135,145,255)); return xform(im,1,0,dx)
def f_brief(t):
    im,d=layer(); hc=(95,60,30,255); d.arc([P(-.22,-.5),P(.22,-.05)],180,360,fill=hc,width=int(.07*K))
    for x in (-.22,.22): d.line([P(x,-.28),P(x,-.05)],fill=hc,width=int(.07*K))
    rr(d,-.58,-.22,.58,.5,.08,(150,95,50,255),hc); thick_line(d,[(-.55,.1),(.55,.1)],.03,hc); rr(d,-.07,0,.07,.2,.02,(255,193,7,255)); return xform(im,1,4*sg(t),0,-.03*abs(sg(t)))
def f_clip(t):
    im,d=layer(); rr(d,-.44,-.56,.44,.6,.06,(190,130,70,255),(140,90,45,255)); rr(d,-.35,-.45,.35,.5,.03,(255,255,255,255)); rr(d,-.17,-.66,.17,-.42,.05,GR,GRD)
    fade=1-ease_in((t-.88)/.12) if t>.88 else 1
    for k in range(3):
        y=-.2+.27*k; thick_line(d,[(-.1,y),(.25,y)],.05,(190,195,205,255)); p=ease_io((t-.1-k*.22)/.2)*fade
        if p>0: thick_line(d,partial([(-.28,y),(-.22,y+.07),(-.12,y-.07)],p),.06,(46,204,113,255))
    return im
def f_money(t):
    im,d=layer(); bag=(205,160,90,255); dk=(150,105,50,255)
    poly(d,[(-.2,-.38),(.2,-.38),(.1,-.2),(-.1,-.2)],bag,dk); ell(d,0,.18,.5,.45,bag,dk,.04); rr(d,-.22,-.45,.22,-.34,.04,(185,60,50,255))
    if FONT: d.text(P(0,.2),"$",font=FONT,fill=(70,110,40,255),anchor="mm")
    else: rr(d,-.04,0,.04,.4,.02,(70,110,40,255))
    return xform(im,1,6*sg(t))
def f_grad(t):
    im,d=layer(); poly(d,[(-.35,.05),(-.35,.35),(0,.5),(.35,.35),(.35,.05),(0,.22)],(70,75,88,255)); poly(d,[(0,-.4),(.68,-.08),(0,.24),(-.68,-.08)],(45,48,55,255),(20,22,26,255),.03)
    sx=.04*sg(t); thick_line(d,[(.5,-.05),(.52+sx,.28)],.04,(255,193,7,255)); ell(d,.52+sx,.32,.06,.06,(255,193,7,255)); return xform(im,1,5*sg(t),0,-.1*abs(math.sin(2*math.pi*t)))
PIPS={1:[(0,0)],2:[(-.2,-.2),(.2,.2)],3:[(-.2,-.2),(0,0),(.2,.2)],4:[(-.2,-.2),(.2,-.2),(-.2,.2),(.2,.2)],5:[(-.2,-.2),(.2,-.2),(0,0),(-.2,.2),(.2,.2)],6:[(-.2,-.22),(.2,-.22),(-.2,0),(.2,0),(-.2,.22),(.2,.22)]}
def f_die(t):
    im,d=layer(); n=1+int(t*6)%6; rr(d,-.46,-.46,.46,.46,.14,(250,250,252,255),(110,115,128,255),.05)
    for x,y in PIPS[n]: ell(d,x,y,.07,.07,(45,48,55,255))
    return xform(im,1,360*t,0,-.12*abs(math.sin(6*math.pi*t)))
def f_memo(t):
    im,d=layer(); rr(d,-.4,-.58,.4,.58,.05,(255,248,225,255),(200,185,140,255)); rr(d,-.4,-.58,.4,-.42,.05,(231,76,60,255))
    fade=1-ease_in((t-.88)/.12) if t>.88 else 1; tip=(0,0)
    for k in range(4):
        y=-.25+.2*k; p=clamp((t-.05-k*.2)/.2)*fade; x1=-.28+.56*p
        if p>0: thick_line(d,[(-.28,y),(x1,y)],.045,(120,125,140,255))
        if 0<p<1: tip=(x1,y)
    if .05<t<.85: x,y=tip; thick_line(d,[(x+.04,y-.04),(x+.34,y-.34)],.1,(255,193,7,255)); poly(d,[(x,y),(x,y-.1),(x+.1,y)],(60,50,40,255))
    return im
def f_chart(pts,col):
    def f(t):
        s=ease_out_back(t/.12) if t<.12 else (1-ease_in((t-.9)/.1) if t>.9 else 1)
        im,d=layer(); rr(d,-.6,-.55,.6,.55,.08,(245,246,250,255),(190,195,205,255),.03); thick_line(d,[(-.45,-.4),(-.45,.4),(.5,.4)],.04,(150,155,165,255))
        p=ease_io((t-.15)/.55)
        if p>0:
            thick_line(d,partial(pts,p),.09,col)
            if p>=.99:
                a,b=pts[-1],pts[-2]; L=math.dist(a,b); v=((a[0]-b[0])/L,(a[1]-b[1])/L); n=(-v[1],v[0])
                poly(d,[(a[0]+v[0]*.14,a[1]+v[1]*.14),(a[0]-v[0]*.05+n[0]*.12,a[1]-v[1]*.05+n[1]*.12),(a[0]-v[0]*.05-n[0]*.12,a[1]-v[1]*.05-n[1]*.12)],col)
        return xform(im,s)
    return f
def f_globe(t):
    im,d=layer(); circle(d,.58,(52,120,246,255)); land=Image.new("RGBA",(S,S),(0,0,0,0)); ld=ImageDraw.Draw(land); Pd=1.4
    for off in (-Pd,0,Pd):
        sx=off-Pd*t
        for cx,cy,rx,ry in [(-.3,-.2,.3,.2),(.2,.15,.25,.22),(0,.42,.18,.08),(-.1,-.5,.22,.08),(.5,-.25,.12,.1)]:
            x,y=P(cx+sx,cy); ld.ellipse([x-rx*K,y-ry*K,x+rx*K,y+ry*K],fill=(60,180,90,255))
    mask=Image.new("L",(S,S),0); ImageDraw.Draw(mask).ellipse([S/2-.58*K,S/2-.58*K,S/2+.58*K,S/2+.58*K],fill=255)
    land.putalpha(ImageChops.multiply(land.getchannel("A"),mask)); im.alpha_composite(land); ring(d,.58,(30,80,180,255),.04); return im
def f_game(t):
    im,d=layer(); c=(95,100,118,255); o=(55,58,70,255); ell(d,-.42,.18,.2,.26,c,o,.03); ell(d,.42,.18,.2,.26,c,o,.03); rr(d,-.6,-.28,.6,.22,.2,c,o,.03)
    rr(d,-.45,-.08,-.15,.02,0,(240,240,245,255)); rr(d,-.35,-.18,-.25,.12,0,(240,240,245,255)); act=int(t*4)%4
    for i,((x,y),col) in enumerate(zip([(.38,-.15),(.5,-.03),(.38,.09),(.26,-.03)],[(231,76,60,255),(46,204,113,255),(52,120,246,255),(255,193,7,255)])): ell(d,x,y,.06 if i!=act else .045,.06 if i!=act else .045,col)
    return xform(im,1,4*sg(t))
def f_key(col,dk):
    def f(t):
        im,d=layer(); ell(d,0,-.36,.22,.22,col,dk,.04); ell(d,0,-.36,.09,.09,(0,0,0,0)); rr(d,-.055,-.16,.055,.6,.03,col,dk,.03); rr(d,.05,.3,.2,.38,.02,col,dk,.03); rr(d,.05,.44,.15,.52,.02,col,dk,.03)
        star4(d,-.12,-.46,.12*twinkle(t),(255,255,255,255)); return xform(im,1,-45+6*sg(t))
    return f
def f_mega(col,dk):
    def f(t):
        im,d=layer()
        for k in range(3):
            fr=(t+k/3)%1; r=.2+.35*fr
            if fr<.75: d.arc([P(.25-r,-r),P(.25+r,r)],-40,40,fill=(110,120,135,255),width=int(.07*(1-fr*.5)*K))
        poly(d,[(-.55,-.15),(-.2,-.15),(.3,-.5),(.3,.5),(-.2,.15),(-.55,.15)],col,dk,.03); rr(d,-.4,.12,-.22,.4,.04,dk); return xform(im,1+.04*sg(2*t),3*sg(t))
    return f
def f_skull(t):
    im,d=layer(); w=(240,242,246,255); o=(150,155,170,255); j=.05*abs(math.sin(4*math.pi*t)); rr(d,-.26,.12+j,.26,.46+j,.08,w,o,.03); ell(d,0,-.1,.46,.42,w,o,.03)
    for x in (-.17,.17): ell(d,x,-.05,.13,.14,(35,38,48,255))
    poly(d,[(0,.06),(-.05,.17),(.05,.17)],(35,38,48,255))
    for x in (-.12,0,.12): thick_line(d,[(x,.33+j),(x,.42+j)],.02,o)
    return xform(im,1,4*sg(t))
def f_rocket(t):
    im,d=layer(); fl=.3+.1*sg(4*t)
    poly(d,[(-.14,.3),(.14,.3),(0,.3+fl+.15)],(255,130,30,255)); poly(d,[(-.07,.3),(.07,.3),(0,.3+fl*.7)],(255,226,100,255))
    poly(d,[(-.2,.05),(-.42,.4),(-.2,.3)],(231,76,60,255)); poly(d,[(.2,.05),(.42,.4),(.2,.3)],(231,76,60,255))
    rr(d,-.2,-.35,.2,.32,.1,(240,242,248,255),(170,178,192,255),.03); poly(d,[(0,-.65),(.2,-.3),(-.2,-.3)],(231,76,60,255)); ell(d,0,-.12,.1,.1,(88,170,246,255),(60,90,150,255),.03)
    return xform(im,1,-45,.02*sg(2*t),.03*sg(t))
def f_bell(col,dk,slash):
    def f(t):
        im,d=layer(); sw=math.sin(2*math.pi*t); ell(d,0,-.52,.06,.06,dk); ell(d,0,-.15,.33,.36,col); poly(d,[(-.32,-.08),(.32,-.08),(.5,.3),(-.5,.3)],col); rr(d,-.5,.27,.5,.34,.03,col); ell(d,-.1*sw,.4,.1,.1,dk)
        if slash: thick_line(d,[(-.5,-.5),(.5,.5)],.1,(231,60,60,255))
        return xform(im,1,18*sw)
    return f
def f_gem(t):
    im,d=layer(); poly(d,[(-.5,-.2),(-.3,-.5),(.3,-.5),(.5,-.2),(0,.55)],(60,180,235,255),(30,120,190,255),.04); poly(d,[(-.3,-.5),(.3,-.5),(.5,-.2),(-.5,-.2)],(130,220,255,255))
    for s in (-1,1): thick_line(d,[(s*.15,-.5),(s*.28,-.2),(0,.5)],.025,(30,120,190,255))
    star4(d,.3,-.35,.2*twinkle(t),(255,255,255,255)); return xform(im,1+.05*sg(t))
def f_diamond(t):
    im,d=layer(); poly(d,[(0,-.62),(.44,0),(0,.62),(-.44,0)],(52,120,246,255),(30,80,200,255),.04); poly(d,[(0,-.55),(.37,0),(0,0)],(110,165,255,255)); return xform(im,1+.05*sg(t),6*sg(t))
def f_pm(plus,col,dk):
    def f(t):
        im,d=layer(); circle(d,.58,col,dk); rr(d,-.3,-.07,.3,.07,.03,(255,255,255,255))
        if plus: rr(d,-.07,-.3,.07,.3,.03,(255,255,255,255))
        return xform(im,1+.06*sg(t))
    return f
def f_bigring(t):
    im,d=layer(); ripple(d,t,(231,60,60,255)); ring(d,.5,(231,60,60,255),.14); return xform(im,1+.05*sg(t))
def f_openlock(t):
    im,d=layer(); off=.16; sc=(170,178,190,255); d.arc([P(-.25,-.5-off),P(.25,-off)],180,360,fill=sc,width=int(.09*K))
    d.line([P(-.25,-.25-off),P(-.25,-.02)],fill=sc,width=int(.09*K)); d.line([P(.25,-.25-off),P(.25,-.22)],fill=sc,width=int(.09*K))
    rr(d,-.38,-.05,.38,.5,.1,(255,193,7,255),(200,140,0,255)); ell(d,0,.18,.07,.07,(60,40,10,255)); rr(d,-.03,.18,.03,.34,.01,(60,40,10,255)); return xform(im,1,6*sg(t))
def f_drop(t):
    im,d=layer(); flame(d,.5,.34,(52,160,246,255),0,.05,t); ell(d,-.12,.12,.06,.1,(170,215,255,255)); return xform(im,1+.05*sg(t),0,0,-.03*sg(t))
def f_bomb(t):
    im,d=layer(); ell(d,-.05,.1,.42,.42,(45,48,55,255),(20,22,26,255)); ell(d,-.2,-.05,.1,.07,(110,115,128,255)); rr(d,.1,-.4,.28,-.22,.03,(150,155,165,255))
    thick_line(d,[(.2,-.4),(.28,-.5),(.4,-.52)],.04,(190,150,90,255)); star4(d,.45,-.55,.16*(.8+.2*sg(4*t)),(255,170,30,255)); star4(d,.45,-.55,.09,(255,240,120,255)); return xform(im,1+.04*sg(2*t))
def f_ticket(t):
    im,d=layer(); rr(d,-.58,-.3,.58,.3,.06,(255,159,28,255),(200,110,10,255),.03); ell(d,-.58,0,.1,.1,(0,0,0,0)); ell(d,.58,0,.1,.1,(0,0,0,0))
    for k in range(4): thick_line(d,[(.3,-.2+.13*k),(.3,-.14+.13*k)],.03,(255,255,255,255))
    star4(d,-.12,0,.2,(255,255,255,255)); return xform(im,1,-15+5*sg(t))
def f_compass(t):
    im,d=layer(); circle(d,.58,(240,242,246,255),(88,101,242,255))
    for a in (0,90,180,270): ell(d,.46*math.sin(math.radians(a)),-.46*math.cos(math.radians(a)),.03,.03,(90,95,105,255))
    th=math.radians(40*sg(t)); tip=(.38*math.sin(th),-.38*math.cos(th)); nx,ny=math.cos(th)*.09,math.sin(th)*.09
    poly(d,[tip,(nx,ny),(-nx,-ny)],(231,60,60,255)); poly(d,[(-tip[0],-tip[1]),(nx,ny),(-nx,-ny)],(150,155,165,255)); ell(d,0,0,.04,.04,(60,64,75,255)); return im
def f_floppy(t):
    im,d=layer(); rr(d,-.5,-.5,.5,.5,.06,(52,120,246,255),(30,80,200,255),.03); rr(d,-.28,-.5,.28,-.15,.02,(190,198,210,255)); rr(d,.1,-.45,.2,-.2,.01,(60,64,75,255)); rr(d,-.35,.05,.35,.5,.02,(255,255,255,255))
    for k in range(3): thick_line(d,[(-.25,.15+.12*k),(.25,.15+.12*k)],.025,(190,195,205,255))
    ell(d,.4,-.38,.04,.04,(46,204,113,255) if sg(t)>0 else (30,100,60,255)); return xform(im,1+.04*sg(t))
def f_phones(t):
    im,d=layer(); b=.03*max(0,math.sin(4*math.pi*t)); d.arc([P(-.48,-.56),P(.48,.4)],180,360,fill=(60,64,78,255),width=int(.1*K))
    for s in (-1,1): rr(d,s*.5-.13-b,-.04,s*.5+.13+b,.42,.1,(88,101,242,255),(60,70,200,255),.03)
    return xform(im,1,0,0,-.02*abs(sg(2*t)))
def f_mag(flip):
    def f(t):
        im,d=layer(); thick_line(d,[(.18,.18),(.52,.52)],.13,(120,80,45,255)); ell(d,-.12,-.12,.36,.36,(205,232,255,255),(95,105,125,255),.08); ell(d,-.25,-.25,.09,.06,(255,255,255,255))
        im=xform(im,1,0,.06*math.cos(2*math.pi*t),.06*math.sin(2*math.pi*t)); return im.transpose(Image.FLIP_LEFT_RIGHT) if flip else im
    return f
def f_books(t):
    im,d=layer()
    for i,(y0,y1,c,w,ox) in enumerate([(.2,.5,(231,76,60),.55,0),(-.1,.2,(52,120,246),.5,.04),(-.4,-.1,(46,204,113),.45,-.03)]):
        dy=-.1*max(0,math.sin(2*math.pi*(t-i*.18))); dk=tuple(int(v*.7) for v in c)+(255,); rr(d,-w+ox,y0+dy,w+ox,y1+dy,.04,c+(255,),dk,.03)
        for x in (-w+.1+ox,-w+.16+ox): thick_line(d,[(x,y0+dy+.05),(x,y1+dy-.05)],.02,(255,255,255,255))
    return im
def f_pushpin(t):
    im,d=layer(); dy=.05*max(0,math.sin(2*math.pi*t)); rd=(231,60,60,255); dr=(170,35,35,255)
    thick_line(d,[(0,.1+dy),(0,.62)],.05,(150,155,165,255)); rr(d,-.2,-.6+dy,.2,-.2+dy,.08,rd,dr,.03); poly(d,[(-.14,-.2+dy),(.14,-.2+dy),(.28,0+dy),(-.28,0+dy)],rd); rr(d,-.34,-.02+dy,.34,.1+dy,.04,dr); return xform(im,1,35)
def f_mappin(t):
    im,d=layer(); flame(d,.5,.34,(231,60,60,255),0,-.05,t); im=im.rotate(180); d=ImageDraw.Draw(im); ell(d,0,-.2,.12,.12,(255,255,255,255)); return xform(im,1,0,0,-.1*abs(math.sin(2*math.pi*t)))
def f_link(t):
    im,d=layer(); s=.06*sg(t); rr(d,-.55-s,-.17,.1-s,.17,.17,None,(88,101,242,255),.1); rr(d,-.1+s,-.17,.55+s,.17,.17,None,(150,160,250,255),.1); return xform(im,1,-45)

# ===== gelombang 4 =====
_F={}
def fnt(sz):
    if sz not in _F:
        try: _F[sz]=ImageFont.truetype("DejaVuSans-Bold.ttf",sz)
        except Exception: _F[sz]=None
    return _F[sz]
def txt(d,s,x,y,sz,col):
    f=fnt(sz)
    if f: d.text(P(x,y),s,font=f,fill=col,anchor="mm")
W=(255,255,255,255); BL=(88,101,242,255); BLD=(60,70,200,255)
def hpts(s=1,rot=0,cx=0,cy=0):
    c,sn=math.cos(math.radians(rot)),math.sin(math.radians(rot)); out=[]
    for i in range(80):
        u=i/80*2*math.pi; x=.034*16*math.sin(u)**3*s; y=(-.034*(13*math.cos(u)-5*math.cos(2*u)-2*math.cos(3*u)-math.cos(4*u))+.05)*s
        out.append((cx+x*c-y*sn,cy+x*sn+y*c))
    return out
def f_label(s,bg,dk,sz,fg=W):
    def f(t):
        im,d=layer(); rr(d,-.55,-.55,.55,.55,.14,bg,dk,.05); txt(d,s,0,.03,sz,fg); return xform(im,1+.05*sg(t),3*sg(t))
    return f
def f_media(fn,rot=0):
    def f(t):
        im,d=layer(); circle(d,.58,BL,BLD); fn(d,.04*sg(t),t); return xform(im,1,rot)
    return f
def m_ff(d,dx,t): poly(d,[(-.3+dx,-.24),(-.3+dx,.24),(dx,0)],W,W,.05); poly(d,[(dx,-.24),(dx,.24),(.3+dx,0)],W,W,.05)
def m_next(d,dx,t): poly(d,[(-.3+dx,-.24),(-.3+dx,.24),(.1+dx,0)],W,W,.05); rr(d,.14+dx,-.24,.28+dx,.24,.03,W)
def m_pause(d,dx,t):
    s=1+.15*sg(t); rr(d,-.22,-.25*s,-.06,.25*s,.03,W); rr(d,.06,-.25*s,.22,.25*s,.03,W)
def _arrowhead(d,deg,r,col,sz=.22):
    a=math.radians(deg); c=(r*math.cos(a),r*math.sin(a)); tt=(math.sin(a),-math.cos(a)); n=(math.cos(a),math.sin(a))
    poly(d,[(c[0]+tt[0]*sz,c[1]+tt[1]*sz),(c[0]+n[0]*sz*.85,c[1]+n[1]*sz*.85),(c[0]-n[0]*sz*.85,c[1]-n[1]*sz*.85)],col)
def f_recycle(t):
    im,d=layer(); col=(46,204,113,255)
    for s0 in (0,120,240): d.arc([P(-.42,-.42),P(.42,.42)],s0+25,s0+95,fill=col,width=int(.13*K)); _arrowhead(d,s0+25,.42,col,.24)
    return xform(im,1,120*t)
def f_repeat(t):
    bg,d=layer(); rr(d,-.58,-.58,.58,.58,.16,BL,BLD,.04); fg,e=layer()
    for s0 in (20,200): e.arc([P(-.3,-.3),P(.3,.3)],s0+30,s0+150,fill=W,width=int(.1*K)); _arrowhead(e,s0+30,.3,W,.17)
    bg.alpha_composite(xform(fg,1,180*t)); return bg
def f_hook(t):
    im,d=layer(); circle(d,.58,BL,BLD); dx=.04*sg(t); thick_line(d,[(.2,.28),(.2,-.08),(-.14+dx,-.08)],.1,W); poly(d,[(-.3+dx,-.08),(-.1+dx,-.24),(-.1+dx,.08)],W); return im
def f_clockf(hdeg,mdeg=0):
    def f(t):
        im,d=layer(); circle(d,.58,(250,250,252,255),BL); ring(d,.58,BL,.06)
        for i in range(12): a=math.radians(i*30); r=.46; q=.03 if i%3==0 else .02; ell(d,r*math.sin(a),-r*math.cos(a),q,q,(90,95,105,255))
        for deg,L,w in ((hdeg,.25,.07),(mdeg,.38,.05)): a=math.radians(deg); thick_line(d,[(0,0),(L*math.sin(a),-L*math.cos(a))],w,(45,48,55,255))
        a=2*math.pi*t; thick_line(d,[(0,0),(.4*math.sin(a),-.4*math.cos(a))],.025,(231,60,60,255)); ell(d,0,0,.05,.05,(231,60,60,255)); return xform(im,1+.03*sg(t))
    return f
def f_stopw(t):
    im,d=layer(); rr(d,-.08,-.68,.08,-.48,.02,GR,GRD); circle(d,.5,(250,250,252,255),GRD)
    for i in range(12): a=math.radians(i*30); ell(d,.4*math.sin(a),-.4*math.cos(a),.02,.02,(90,95,105,255))
    d.arc([P(-.44,-.44),P(.44,.44)],-90,-90+360*t,fill=BL,width=int(.06*K)) if t>.01 else None
    a=2*math.pi*t; thick_line(d,[(0,0),(.34*math.sin(a),-.34*math.cos(a))],.04,(231,60,60,255)); ell(d,0,0,.05,.05,(45,48,55,255)); return im
def f_fullmoon(t):
    im,d=layer(); ripple(d,t,(255,236,160,255)); circle(d,.5,(255,236,160,255),(230,200,100,255))
    for x,y,rx,ry in [(-.2,-.15,.12,.1),(.2,.1,.15,.12),(-.05,.3,.08,.07),(.22,-.25,.07,.06)]: ell(d,x,y,rx,ry,(240,215,125,255))
    star4(d,.62,-.55,.15*twinkle(t),(255,255,255,255)); star4(d,-.62,.5,.12*twinkle(t,.5),(255,255,255,255)); return xform(im,1+.03*sg(t))
def f_newmoon(t):
    im,d=layer(); circle(d,.5,(60,66,90,255),(40,44,65,255)); d.arc([P(-.46,-.46),P(.46,.46)],200,290,fill=(130,140,185,255),width=int(.04*K))
    for x,y,rx,ry in [(-.2,-.15,.12,.1),(.2,.1,.15,.12),(-.05,.3,.08,.07)]: ell(d,x,y,rx,ry,(50,55,78,255))
    star4(d,.62,-.55,.15*twinkle(t),W); star4(d,-.62,.5,.12*twinkle(t,.5),W); star4(d,-.55,-.5,.1*twinkle(t,.25),W); return im
def f_sun(t):
    rl,rd=layer()
    for i in range(12): a=math.radians(i*30); thick_line(rd,[(.54*math.cos(a),.54*math.sin(a)),(.7*math.cos(a),.7*math.sin(a))],.09,(255,170,30,255))
    im=xform(rl,1,30*t); d=ImageDraw.Draw(im); circle(d,.42,(255,200,40,255),(240,150,10,255)); ell(d,-.14,-.16,.12,.07,(255,235,150,255)); return xform(im,1+.04*sg(t))
def _calbody(d,hd):
    rr(d,-.55,-.5,.55,.6,.08,(250,250,252,255),(150,155,170,255),.04); rr(d,-.55,-.5,.55,-.2,.08,hd); rr(d,-.55,-.3,.55,-.2,0,hd)
    for x in (-.3,.3): rr(d,x-.04,-.62,x+.04,-.38,.03,(90,95,105,255))
def f_cal(t):
    im,d=layer(); _calbody(d,(231,60,60,255)); act=int(t*8)%8
    for r in range(2):
        for c in range(4): x=-.37+c*.25; y=0+r*.3; rr(d,x-.09,y-.09,x+.09,y+.09,.03,BL if r*4+c==act else (215,220,232,255))
    return xform(im,1,2*sg(t))
def f_tear(t):
    im,d=layer(); _calbody(d,(255,140,40,255)); txt(d,"17",0,.18,170,(45,48,55,255)); poly(d,[(.55,.35),(.55,.6),(.3,.6)],(215,220,232,255)); return xform(im,1,3*sg(t),0,-.02*abs(sg(t)))
def f_radio(t):
    im,d=layer(); circle(d,.55,(235,238,245,255),(150,155,170,255)); r=.28*(1+.12*sg(t)); ell(d,0,0,r,r,BL); ell(d,-.08,-.08,.07,.05,(150,165,255,255)); return im
def f_broken(t):
    im,d=layer(); poly(d,hpts(1),(235,50,75,255),(190,30,55,255)); w=.035+.03*max(0,sg(t)); thick_line(d,[(0,-.4),(-.08,-.15),(.08,.05),(-.06,.25),(0,.58)],w*2,(0,0,0,0)); return xform(im,1,4*sg(2*t))
def f_sparkheart(t):
    im,d=layer(); poly(d,hpts(.85,0,0,.05),(247,110,160,255),(210,70,120,255)); ell(d,-.22,-.17,.1,.06,(255,175,205,255))
    for x,y,r,ph in [(.5,-.5,.22,0),(-.55,-.35,.17,.33),(.55,.3,.14,.66)]: star4(d,x,y,r*twinkle(t,ph)+.02,(255,220,70,255))
    return xform(im,1+.05*sg(t))
def f_heartarrow(t):
    im,d=layer(); a=.05*sg(t); poly(d,hpts(1),(255,75,110,255),(200,40,70,255)); ell(d,-.26,-.22,.12,.07,(255,150,170,255))
    ox,oy=a,-a; thick_line(d,[(-.55+ox,.55+oy),(.45+ox,-.45+oy)],.05,(120,80,45,255)); poly(d,[(.65+ox,-.65+oy),(.4+ox,-.5+oy),(.5+ox,-.4+oy)],(150,155,165,255))
    poly(d,[(-.55+ox,.55+oy),(-.45+ox,.4+oy),(-.65+ox,.45+oy)],(255,255,255,255)); poly(d,[(-.55+ox,.55+oy),(-.4+ox,.45+oy),(-.45+ox,.65+oy)],(231,60,60,255)); return xform(im,1+.05*sg(2*t))
def f_heartribbon(t):
    im,d=layer(); y=(255,214,0,255); poly(d,hpts(1),(250,100,150,255),(205,60,110,255)); thick_line(d,[(-.48,.02),(.48,.02)],.09,y); thick_line(d,[(0,-.3),(0,.55)],.09,y)
    poly(d,[(0,-.3),(-.28,-.5),(-.3,-.2)],y); poly(d,[(0,-.3),(.28,-.5),(.3,-.2)],y); ell(d,0,-.3,.07,.07,(230,170,0,255)); return xform(im,1+.05*sg(t),3*sg(t))
def f_revolve(t):
    im,d=layer(); a=2*math.pi*t; cols=[((255,105,160,255),(210,70,120,255)),((190,110,240,255),(140,70,190,255))]
    for k in range(2): b=a+k*math.pi; poly(d,hpts(.5,0,.25*math.cos(b),.25*math.sin(b)),*cols[k],.02)
    return im
def f_popper(t):
    cone,cd=layer(); poly(cd,[(0,.62),(-.3,-.12),(.3,-.12)],(255,193,7,255),(200,140,0,255),.03); ell(cd,0,-.12,.3,.09,(230,150,0,255)); thick_line(cd,[(-.14,.18),(.14,.02)],.04,(231,76,60,255)); thick_line(cd,[(-.08,.4),(.08,.3)],.04,(231,76,60,255))
    im=xform(cone,1,-45); d=ImageDraw.Draw(im); cols=[(231,76,60),(52,170,246),(46,204,113),(255,193,7),(190,110,240),(255,105,160)]
    for k in range(14):
        f=(t+k/14)%1; ang=math.radians(-45+((k*53)%100-50)*.9); r=.15+.85*f; x=.1+r*math.cos(ang); y=-.1+r*math.sin(ang)+.5*f*f; s=.055*(1-.5*f); col=cols[k%6]+(255,)
        (ell(d,x,y,s,s,col) if k%2 else rr(d,x-s,y-s,x+s,y+s,0,col))
    return im
def f_confball(t):
    im,d=layer(); cc=[(255,193,7),(46,204,113),(52,170,246),(231,76,60),(255,255,255)]; ell(d,0,.1,.38,.38,(155,89,182,255),(115,60,150,255),.03)
    for k,(x,y) in enumerate([(-.2,0),(.15,-.1),(0,.2),(-.18,.28),(.22,.2),(.05,-.2)]): ell(d,x,.1+y,.04,.04,cc[k%5]+(255,))
    for k in range(10):
        f=(t+k/10)%1; x=-.6+1.2*((k*37%10)/10)+.05*math.sin(2*math.pi*(t*2+k)); y=-.7+1.4*f; rr(d,x-.04,y-.025,x+.04,y+.025,.01,cc[k%5]+(255,))
    return im
def f_boom(t):
    im,d=layer(); p1=[];p2=[]
    for i in range(16): a=math.radians(i*22.5-90); r=.66 if i%2==0 else .34; p1.append((r*math.cos(a),r*math.sin(a))); p2.append((r*.55*math.cos(a),r*.55*math.sin(a)))
    poly(d,p1,(255,110,30,255),(220,60,10,255),.03); poly(d,p2,(255,226,100,255)); return xform(im,1+.1*sg(2*t),45*t)
def f_dizzy(t):
    im,d=layer(); star5(d,0,0,.3,.13,(255,214,0,255),(230,150,0,255))
    for k in range(3): a=2*math.pi*t+k*2*math.pi/3; star4(d,.5*math.cos(a),.5*math.sin(a),.2,(255,235,100,255))
    return im
def f_siren(t):
    im,d=layer(); on=sg(t)>0; col=(231,60,60,255) if on else (255,140,140,255); rr(d,-.5,.2,.5,.42,.05,(70,75,90,255),(40,42,55,255))
    d.pieslice([P(-.36,-.16),P(.36,.56)],180,360,fill=col,outline=(170,30,30,255),width=int(.03*K)); s=-1 if on else 1
    for dy in (-.0,.14,-.14): thick_line(d,[(s*.5,-.1+dy-.1),(s*.7,-.1+dy-.18)],.05,(255,193,7,255))
    return im
def f_env(kind):
    def f(t):
        im,d=layer(); y={'in':0,'arrow':.2,'at':0}[kind]
        if kind=='in': y+=-.7*(1-ease_out_back(t/.35)) if t<.35 else (-.7*ease_in((t-.85)/.15) if t>.85 else 0)
        rr(d,-.55,-.3+y,.55,.3+y,.06,(250,250,252,255),(130,140,190,255),.04); thick_line(d,[(-.55,-.3+y),(0,.08+y),(.55,-.3+y)],.04,(130,140,190,255))
        if kind=='arrow': b=.04*sg(t); poly(d,[(-.09,-.72+b),(.09,-.72+b),(.09,-.52+b),(.2,-.52+b),(0,-.35+b),(-.2,-.52+b),(-.09,-.52+b)],BL)
        if kind=='at': ell(d,.34,.2,.2,.2,(231,60,60,255)); txt(d,"@",.34,.2,95,W)
        return xform(im,1,3*sg(t)) if kind=='at' else im
    return f
def f_bbook(t):
    im,d=layer(); rr(d,-.42,-.58,.42,.58,.05,(52,120,246,255),(30,80,200,255),.03); rr(d,-.42,-.58,-.3,.58,.03,(30,80,200,255)); rr(d,.38,-.5,.46,.5,.02,(250,250,245,255),(200,200,190,255),.02)
    star4(d,.05,-.05,.2*(.8+.2*sg(t)),W); thick_line(d,[(-.1,.3),(.2,.3)],.04,(130,175,255,255)); return xform(im,1,4*sg(t),0,-.03*abs(sg(t)))
def f_scroll(t):
    h=.35+.2*ease_io(1-abs(2*t-1)); im,d=layer(); rr(d,-.4,-h,.4,h,.02,(250,240,215,255),(200,180,130,255),.03)
    for y in (-h,h): rr(d,-.5,y-.1,.5,y+.1,.1,(235,215,170,255),(190,160,100,255),.03)
    for k in range(4): y=-h+.2+k*(2*h-.4)/3; thick_line(d,[(-.28,y),(.28,y)],.03,(170,150,110,255))
    return im
def f_page(t):
    im,d=layer(); poly(d,[(-.4,-.58),(.18,-.58),(.4,-.36),(.4,.58),(-.4,.58)],W,(150,155,170,255),.04); poly(d,[(.18,-.58),(.18,-.36),(.4,-.36)],(215,220,232,255),(150,155,170,255),.03)
    fade=1-ease_in((t-.88)/.12) if t>.88 else 1
    for k in range(5):
        y=-.2+.15*k; p=ease_io((t-.05-k*.15)/.2)*fade
        if p>0: thick_line(d,[(-.26,y),(-.26+.52*p*(1 if k<4 else .6),y)],.04,(130,135,150,255))
    return im
def f_tray(down):
    def f(t):
        im,d=layer(); y=(-.45+.5*ease_io(t)) if down else (.05-.5*ease_io(t))
        if down: poly(d,[(-.08,y-.2),(.08,y-.2),(.08,y),(.2,y),(0,y+.2),(-.2,y),(-.08,y)],BL)
        else: poly(d,[(-.08,y+.2),(.08,y+.2),(.08,y),(.2,y),(0,y-.2),(-.2,y),(-.08,y)],BL)
        poly(d,[(-.55,.05),(-.55,.5),(.55,.5),(.55,.05),(.35,.05),(.3,.25),(-.3,.25),(-.35,.05)],GR,GRD,.03); return im
    return f
def f_folder(t):
    im,d=layer(); poly(d,[(-.55,-.4),(-.2,-.4),(-.1,-.28),(.5,-.28),(.5,.5),(-.55,.5)],(222,165,40,255),(170,120,20,255),.03)
    rr(d,-.4,-.35-.08*abs(sg(t)),.35,.15,.02,W,(200,200,210,255),.02); poly(d,[(-.45,-.05),(.6,-.05),(.5,.5),(-.55,.5)],(255,203,70,255),(200,150,30,255),.03); return im
def _sword():
    im,d=layer(); poly(d,[(0,-.68),(.07,-.5),(.07,.15),(-.07,.15),(-.07,-.5)],(215,222,232,255),GRD,.02); thick_line(d,[(0,-.5),(0,.1)],.02,(160,170,185,255))
    rr(d,-.2,.15,.2,.22,.02,(255,193,7,255),(200,140,0,255),.02); rr(d,-.04,.22,.04,.45,.01,(150,95,50,255)); ell(d,0,.5,.06,.06,(255,193,7,255)); return im
def f_swords(t):
    a=3*sg(2*t); im=xform(_sword(),1,45+a); im.alpha_composite(xform(_sword(),1,-45-a)); d=ImageDraw.Draw(im); star4(d,0,-.05,.2*twinkle(t),W); return im
def f_scales(t):
    im,d=layer(); th=math.radians(12*sg(t)); pv=(0,-.42); rr(d,-.03,-.5,.03,.5,.01,(190,150,40,255)); rr(d,-.28,.45,.28,.53,.03,(190,150,40,255),(150,110,20,255),.02)
    L=(-.5*math.cos(th),pv[1]-.5*math.sin(th)); R=(.5*math.cos(th),pv[1]+.5*math.sin(th)); thick_line(d,[L,R],.05,(255,193,7,255))
    for (x,y) in (L,R):
        thick_line(d,[(x,y),(x-.15,y+.3)],.015,(150,110,20,255)); thick_line(d,[(x,y),(x+.15,y+.3)],.015,(150,110,20,255)); poly(d,[(x-.22,y+.3),(x+.22,y+.3),(x+.14,y+.42),(x-.14,y+.42)],(255,193,7,255),(200,140,0,255),.02)
    ell(d,0,-.5,.07,.07,(255,193,7,255)); return im
def f_hourb(t):
    drain=clamp(t/.78); ang=180*ease_io((t-.78)/.22) if t>.78 else 0; im,d=layer(); glass=(190,225,255,255); line=(120,150,200,255); sand=(255,120,170,255)
    top=[P(-.3,-.4),P(.3,-.4),P(0,0)]; bot=[P(0,0),P(.3,.4),P(-.3,.4)]; d.polygon(top,fill=glass); d.polygon(bot,fill=glass); f=1-drain; ys=-.4+.4*(1-f)
    if f>.01: w=-.75*ys; poly(d,[(-w,ys),(w,ys),(0,0)],sand)
    yb=.4-.4*drain
    if drain>.01: w=.75*yb; poly(d,[(-w,yb),(w,yb),(.3,.4),(-.3,.4)],sand)
    d.line(top+[top[0]],fill=line,width=int(.03*K)); d.line(bot+[bot[0]],fill=line,width=int(.03*K))
    for y in (-.48,.4): rr(d,-.38,y,.38,y+.08,.03,(120,70,170,255))
    return xform(im,1,ang)
def f_note(t):
    im,d=layer(); ell(d,-.15,.35,.2,.15,BL); rr(d,.01,-.5,.09,.35,.02,BL); poly(d,[(.09,-.5),(.4,-.3),(.4,-.1),(.09,-.3)],BL); return xform(im,1,6*sg(t),0,-.05*abs(sg(t)))
def f_notes(t):
    im,d=layer(); b1=.06*max(0,sg(t)); b2=.06*max(0,-sg(t))
    ell(d,-.3,.35-b1,.17,.13,BL); ell(d,.3,.25-b2,.17,.13,BL); rr(d,-.15,-.4-b1,-.07,.35-b1,.02,BL); rr(d,.45,-.5-b2,.53,.25-b2,.02,BL); poly(d,[(-.15,-.4-b1),(.53,-.5-b2),(.53,-.3-b2),(-.15,-.2-b1)],BL); return im
def f_clover(t):
    im,d=layer(); g=(46,180,90,255); gd=(30,130,60,255); thick_line(d,[(0,.1),(.08,.4),(.2,.62)],.07,gd)
    for k in range(4): a=k*90; poly(d,hpts(.45,a,.27*math.sin(math.radians(a)),-.27*math.cos(math.radians(a))),g,gd,.02)
    star4(d,.5,-.5,.18*twinkle(t),(255,255,255,255)); return xform(im,1,8*sg(t))
def f_flag(t):
    im,d=layer(); rr(d,-.56,-.68,-.48,.66,.02,GR,GRD,.02); dy=lambda x:.06*math.sin(2*math.pi*t-5*x)
    for i in range(4):
        for j in range(3):
            x0=-.48+i*.25; x1=x0+.25; y0=-.62+j*.2; y1=y0+.2
            poly(d,[(x0,y0+dy(x0)),(x1,y0+dy(x1)),(x1,y1+dy(x1)),(x0,y1+dy(x0))],(30,32,38,255) if (i+j)%2==0 else (250,250,252,255))
    return im
def f_rainbow(t):
    im,d=layer(); cols=[(231,60,60),(255,140,40),(255,213,50),(46,204,113),(52,120,246),(155,89,182)]
    for i,c in enumerate(cols):
        p=ease_io((t-.05-i*.05)/.3) if t<.7 else 1-ease_io((t-.78-i*.03)/.15); r=.62-i*.085
        if p>0: d.arc([P(-r,.3-r),P(r,.3+r)],180,180+180*clamp(p),fill=c+(255,),width=int(.1*K))
    for x in (-.55,.55): ell(d,x,.38,.2,.12,W); ell(d,x*.85,.28,.14,.1,W)
    return im
def f_banknote(t):
    im,d=layer(); gd=(60,140,80,255); rr(d,-.62,-.32,.62,.32,.05,(120,200,130,255),gd,.04); rr(d,-.54,-.24,.54,.24,.03,None,gd,.02); ell(d,0,0,.2,.2,(150,220,160,255),gd,.025); txt(d,"$",0,.01,70,(40,110,60,255))
    for x in (-.4,.4): ell(d,x,0,.05,.05,gd)
    return xform(im,1,6*sg(t),0,-.04*sg(2*t))
def f_castle(t):
    im,d=layer(); st=(190,195,208,255); so=(120,125,140,255); rd=(210,60,60,255)
    rr(d,-.6,-.2,-.26,.5,0,st,so,.03); rr(d,.26,-.2,.6,.5,0,st,so,.03); rr(d,-.26,-.05,.26,.5,0,st,so,.03); rr(d,-.2,-.5,.2,.5,0,st,so,.03)
    poly(d,[(-.66,-.2),(-.43,-.5),(-.2,-.2)],rd,(150,35,35,255),.02); poly(d,[(.2,-.2),(.43,-.5),(.66,-.2)],rd,(150,35,35,255),.02); poly(d,[(-.26,-.5),(0,-.82),(.26,-.5)],rd,(150,35,35,255),.02)
    ell(d,0,.28,.1,.1,(70,50,35,255)); rr(d,-.1,.28,.1,.5,0,(70,50,35,255)); rr(d,-.05,-.35,.05,-.15,.04,(80,90,120,255))
    for x in (-.43,.43): rr(d,x-.04,0,x+.04,.18,.04,(80,90,120,255))
    thick_line(d,[(0,-.82),(0,-.98)],.025,so); w=.05*sg(t); poly(d,[(0,-.98),(.28,-.92+w),(0,-.82)],(231,76,60,255)); return xform(im,.85,3*sg(t))
def f_bust(n):
    def f(t):
        im,d=layer(); col=(120,130,150,255); dk=(80,90,110,255)
        def person(x,y,s,c): ell(d,x,y-.18*s,.17*s,.17*s,c); d.pieslice([P(x-.3*s,y),P(x+.3*s,y+.7*s)],180,360,fill=c)
        if n==1: person(0,.1-.04*abs(sg(t)),1.4,col)
        else: person(.22,-.02-.03*max(0,-sg(t)),1.0,dk); person(-.17,.15-.04*max(0,sg(t)),1.2,col)
        return im
    return f
