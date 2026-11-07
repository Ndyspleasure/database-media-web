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

# ===== gelombang 5 =====
SK=(255,204,77,255); SKD=(230,160,30,255); DK=(70,45,20,255); PK=(255,140,120,255)
def lt(c,a=40): return tuple(min(255,v+a) for v in c[:3])+(255,)
def dk_(c,m=.7): return tuple(int(v*m) for v in c[:3])+(255,)
def bl(t,c=.72): return .12 if abs(t-c)<.04 else 1
def _eyes(d,t,y=-.08,dx=.2,r=.065,col=DK): b=bl(t); [ell(d,x,y,r,r*b,col) for x in (-dx,dx)]
def f_face(kind):
    def f(t):
        im,d=layer(); col=(240,95,60,255) if kind=='angry' else SK; b=bl(t)
        circle(d,.58,col,dk_(col,.82)); ell(d,-.28,-.38,.14,.06,lt(col))
        dots=lambda y=-.1,r=.07:[ell(d,x,y,r,r*b,DK) for x in (-.2,.2)]
        arcs=lambda y=-.06:[d.arc([P(x-.12,y-.1),P(x+.12,y+.1)],200,340,fill=DK,width=int(.05*K)) for x in (-.2,.2)]
        smile=lambda y=.12,w=.28,h=.2:d.arc([P(-w,y-h),P(w,y+h)],20,160,fill=DK,width=int(.05*K))
        frown=lambda y=.36,w=.2,h=.12:d.arc([P(-w,y-h),P(w,y+h)],200,340,fill=DK,width=int(.05*K))
        cheeks=lambda:[ell(d,x,.12,.1,.06,PK) for x in (-.4,.4)]
        def openm(y=.1,w=.28,h=.3,tg=False):
            d.pieslice([P(-w,y-h),P(w,y+h)],0,180,fill=(110,30,40,255))
            if tg: ell(d,0,y+h*.6,w*.5,h*.28,(240,100,110,255))
        if kind=='smile_eyes': arcs(); smile(); cheeks()
        elif kind=='pensive':
            for x in (-.2,.2): thick_line(d,[(x-.1,-.08),(x+.1,-.04)],.05,DK)
            frown(.34); thick_line(d,[(-.32,-.22),(-.1,-.2)],.03,DK); thick_line(d,[(.32,-.22),(.1,-.2)],.03,DK)
        elif kind=='angry':
            dots(-.05,.06); thick_line(d,[(-.32,-.25),(-.1,-.15)],.06,DK); thick_line(d,[(.32,-.25),(.1,-.15)],.06,DK); frown(.4,.22,.15)
        elif kind=='grin': arcs(); openm(.04,.34,.34,True)
        elif kind=='neutral': dots(); thick_line(d,[(-.18,.28),(.18,.28)],.05,DK)
        elif kind=='flushed':
            for x in (-.2,.2): ell(d,x,-.08,.13,.13,W,GRD,.02); ell(d,x,-.08,.05,.05,DK)
            cheeks(); thick_line(d,[(-.1,.3),(.1,.3)],.04,DK)
        elif kind in ('sweat','anxious'):
            dots()
            if kind=='sweat': smile(.1,.24,.16)
            else: frown(.38,.2,.14); thick_line(d,[(-.32,-.26),(-.1,-.32)],.04,DK); thick_line(d,[(.32,-.26),(.1,-.32)],.04,DK)
            dy=.05*sg(t); poly(d,[(.46,-.58+dy),(.38,-.42+dy),(.54,-.42+dy)],(90,170,255,255)); ell(d,.46,-.38+dy,.08,.08,(90,170,255,255))
        elif kind=='think':
            dots(); thick_line(d,[(.1,-.28),(.32,-.32)],.05,DK); thick_line(d,[(-.12,.3),(.1,.26)],.04,DK)
            rr(d,.02,.15,.15,.5,.05,SK,SKD,.03); ell(d,-.02,.5,.17,.11,SK,SKD,.03)
        elif kind=='cry':
            arcs(); openm(.14,.3,.26)
            for x,ph in ((-.2,0),(.2,.3)): f2=(t+ph)%1; ell(d,x,.0+.5*f2,.05,.08,(90,170,255,255))
        elif kind=='confound':
            for x in (-.2,.2): thick_line(d,[(x-.08,-.16),(x+.06,-.08)],.04,DK); thick_line(d,[(x-.08,0),(x+.06,-.08)],.04,DK)
            thick_line(d,[(-.2,.32),(-.1,.26),(0,.32),(.1,.26),(.2,.32)],.04,DK)
        elif kind=='halo': dots(); smile(); ell(d,0,-.7+.02*sg(t),.3,.08,None,(255,214,0,255),.05)
        elif kind=='cowboy':
            dots(); smile(); hc=(160,100,50,255); hd=(110,65,30,255); ell(d,0,-.42,.72,.13,hc,hd,.03); rr(d,-.34,-.88,.34,-.42,.12,hc,hd,.03); rr(d,-.34,-.56,.34,-.46,0,hd)
        elif kind=='sleep':
            for x in (-.2,.2): thick_line(d,[(x-.1,-.05),(x+.1,-.05)],.05,DK)
            ell(d,0,.26,.06,.05,DK)
            for ph in (0,.5): f2=(t+ph)%1; txt(d,"z",.5+.1*f2,-.35-.2*f2,int(60+60*f2),BLD)
        elif kind=='shush': dots(); rr(d,-.07,.0,.07,.42,.07,SK,SKD,.03)
        return xform(im,1,0 if kind=='sleep' else 3*sg(t))
    return f
def f_shades(t):
    im,d=layer(); c=(35,38,48,255); rr(d,-.55,-.14,-.04,.16,.1,c,(150,160,185,255),.03); rr(d,.04,-.14,.55,.16,.1,c,(150,160,185,255),.03); thick_line(d,[(-.06,-.08),(.06,-.08)],.05,c); thick_line(d,[(-.55,-.08),(-.65,-.2)],.04,c); thick_line(d,[(.55,-.08),(.65,-.2)],.04,c)
    star4(d,-.4,-.05,.12*twinkle(t),W); return xform(im,1,0,0,-.03*abs(sg(t)))
def f_eyes(t):
    im,d=layer(); a=2*math.pi*t
    for x in (-.27,.27): ell(d,x,0,.22,.3,W,GRD,.03); ell(d,x+.1*math.cos(a),.1*math.sin(a),.09,.12,(45,48,55,255)); ell(d,x+.1*math.cos(a)-.03,.1*math.sin(a)-.04,.025,.025,W)
    return im
def f_ghost(t):
    im,d=layer(); pts=[(.45*math.cos(math.radians(a)),-.05+.45*math.sin(math.radians(a))) for a in range(180,361,10)]
    pts+= [(.45-.9*i/8,.5+(.07 if i%2==0 else -.04)) for i in range(9)]
    poly(d,pts,(245,247,252,255),(170,175,195,255),.03); ell(d,-.17,-.1,.06,.08,DK); ell(d,.17,-.1,.06,.08,DK); ell(d,0,.08,.07,.09,DK); return xform(im,1,4*sg(t),0,-.05*sg(t))
def f_dog(t):
    im,d=layer(); br=(205,150,90,255); db=(125,80,40,255); ell(d,-.5,0,.15,.32,db); ell(d,.5,0,.15,.32,db); ell(d,0,.05,.5,.48,br,dk_(br)); ell(d,0,.22,.26,.2,(240,215,180,255))
    ell(d,0,.12,.09,.06,(40,30,25,255)); _eyes(d,t); thick_line(d,[(0,.18),(0,.26)],.02,DK); ell(d,0,.36,.06,.08,(240,100,110,255)); return xform(im,1,4*sg(t))
def f_cat(t):
    im,d=layer(); o=(255,175,80,255); poly(d,[(-.48,-.1),(-.42,-.58),(-.1,-.32)],o,dk_(o)); poly(d,[(.48,-.1),(.42,-.58),(.1,-.32)],o,dk_(o)); poly(d,[(-.4,-.2),(-.38,-.45),(-.2,-.3)],(255,170,170,255)); poly(d,[(.4,-.2),(.38,-.45),(.2,-.3)],(255,170,170,255))
    ell(d,0,.08,.5,.44,o,dk_(o)); _eyes(d,t,-.05,.2,.07,(60,160,80,255)); poly(d,[(-.05,.1),(.05,.1),(0,.17)],(255,120,140,255))
    for s in (-1,1):
        thick_line(d,[(s*.3,.15),(s*.6,.1)],.015,DK); thick_line(d,[(s*.3,.2),(s*.6,.24)],.015,DK)
    d.arc([P(-.1,.15),P(0,.3)],20,160,fill=DK,width=int(.025*K)); d.arc([P(0,.15),P(.1,.3)],20,160,fill=DK,width=int(.025*K)); return xform(im,1,4*sg(t))
def f_mouse(t):
    im,d=layer(); g=(190,190,205,255)
    for s in (-1,1): ell(d,s*.4,-.3,.2,.2,g,dk_(g)); ell(d,s*.4,-.3,.11,.11,(255,170,190,255))
    ell(d,0,.1,.45,.42,g,dk_(g)); _eyes(d,t,-.02); ell(d,0,.18,.06,.05,(255,130,160,255)); rr(d,-.05,.3,.05,.38,.01,W,GR,.01)
    for s in (-1,1): thick_line(d,[(s*.2,.2),(s*.58,.14)],.015,DK); thick_line(d,[(s*.2,.25),(s*.58,.3)],.015,DK)
    return xform(im,1,4*sg(t))
def f_rabbit(t):
    im,d=layer(); dx=.03*sg(t)
    for s in (-1,1): ell(d,s*.18+dx*s,-.4,.12,.42,W,GR,.03); ell(d,s*.18+dx*s,-.4,.06,.3,(255,170,190,255))
    ell(d,0,.2,.4,.37,W,GR,.03); _eyes(d,t,.12,.17); ell(d,0,.26,.05,.04,(255,130,160,255)); d.arc([P(-.1,.26),P(0,.4)],20,160,fill=DK,width=int(.025*K)); d.arc([P(0,.26),P(.1,.4)],20,160,fill=DK,width=int(.025*K)); return im
def f_fox(t):
    im,d=layer(); o=(255,130,40,255); poly(d,[(-.58,-.05),(-.52,-.62),(-.2,-.28),(.2,-.28),(.52,-.62),(.58,-.05),(0,.6)],o,dk_(o),.03)
    poly(d,[(-.55,.0),(-.2,.15),(0,.6),(.2,.15),(.55,.0),(0,.55)],W); poly(d,[(-.52,-.5),(-.36,-.3),(-.46,-.2)],DK); poly(d,[(.52,-.5),(.36,-.3),(.46,-.2)],DK)
    _eyes(d,t,-.05,.22); ell(d,0,.5,.07,.05,DK); return xform(im,1,4*sg(t))
def f_bear(t):
    im,d=layer(); br=(150,100,60,255)
    for s in (-1,1): ell(d,s*.38,-.38,.17,.17,br,dk_(br)); ell(d,s*.38,-.38,.09,.09,(210,170,130,255))
    ell(d,0,.05,.5,.47,br,dk_(br)); ell(d,0,.2,.22,.17,(220,190,150,255)); ell(d,0,.14,.07,.05,DK); _eyes(d,t,-.07); d.arc([P(-.1,.16),P(0,.3)],20,160,fill=DK,width=int(.025*K)); d.arc([P(0,.16),P(.1,.3)],20,160,fill=DK,width=int(.025*K)); return xform(im,1,4*sg(t))
def f_panda(t):
    im,d=layer(); k=(40,42,50,255)
    for s in (-1,1): ell(d,s*.4,-.38,.18,.18,k)
    ell(d,0,.05,.5,.47,W,GR,.03)
    for s in (-1,1): ell(d,s*.2,-.05,.12,.16,k)
    b=bl(t); [ell(d,x,-.05,.04,.05*b,W) for x in (-.2,.2)]; ell(d,0,.15,.07,.05,k); d.arc([P(-.1,.17),P(0,.3)],20,160,fill=k,width=int(.025*K)); d.arc([P(0,.17),P(.1,.3)],20,160,fill=k,width=int(.025*K)); return xform(im,1,4*sg(t))
def f_frog(t):
    im,d=layer(); g=(90,190,80,255); ell(d,0,.1,.52,.4,g,dk_(g),.03); b=bl(t)
    for s in (-1,1): ell(d,s*.27,-.3,.2,.2,g,dk_(g),.03); ell(d,s*.27,-.3,.13,.13*b,W); ell(d,s*.27,-.3,.06,.06*b,DK)
    d.arc([P(-.35,-.05),P(.35,.4)],20,160,fill=dk_(g,.5),width=int(.04*K)); ell(d,-.08,.0,.02,.02,dk_(g,.5)); ell(d,.08,.0,.02,.02,dk_(g,.5)); return xform(im,1,0,0,-.03*abs(sg(t)))
def f_monkey(t):
    im,d=layer(); br=(150,95,55,255); tan=(240,205,160,255)
    for s in (-1,1): ell(d,s*.5,0,.14,.14,br,dk_(br)); ell(d,s*.5,0,.08,.08,tan)
    ell(d,0,.05,.45,.45,br,dk_(br)); ell(d,-.14,-.02,.2,.2,tan); ell(d,.14,-.02,.2,.2,tan); ell(d,0,.2,.3,.22,tan); _eyes(d,t,-.05,.14,.055); ell(d,-.04,.12,.02,.02,DK); ell(d,.04,.12,.02,.02,DK); d.arc([P(-.14,.14),P(.14,.34)],20,160,fill=DK,width=int(.03*K)); return xform(im,1,4*sg(t))
def f_penguin(t):
    im,d=layer(); k=(45,50,65,255); o=(255,160,30,255); ell(d,-.18,.58,.15,.07,o); ell(d,.18,.58,.15,.07,o)
    ell(d,-.38,.1,.1,.3,k); ell(d,.38,.1,.1,.3,k); ell(d,0,.08,.4,.52,k); ell(d,0,.2,.27,.38,W)
    b=bl(t); ell(d,-.14,-.2,.08,.09*b,W); ell(d,.14,-.2,.08,.09*b,W); ell(d,-.14,-.2,.035,.04*b,DK); ell(d,.14,-.2,.035,.04*b,DK); poly(d,[(-.08,-.08),(.08,-.08),(0,.02)],o); return xform(im,1,6*sg(t))
def f_fish(t):
    im,d=layer(); poly(d,[(.3,0),(.65,-.3),(.65,.3)],(255,120,30,255)); poly(d,[(-.1,-.25),(.15,-.25),(.25,-.5),(-.15,-.4)],(255,120,30,255)); ell(d,-.05,0,.45,.3,(255,170,40,255),(220,110,10,255),.03)
    for x in (.0,.18): thick_line(d,[(x,-.2),(x,.2)],.05,W)
    ell(d,-.3,-.07,.06,.06,W); ell(d,-.3,-.07,.03,.03,DK)
    for k in range(3): f2=(t+k/3)%1; ell(d,-.55-.04*k,-.1-.5*f2,.04,.04,(190,225,255,255))
    return xform(im,1,6*sg(t))
def f_butter(t):
    im,d=layer(); s=.45+.55*abs(math.cos(2*math.pi*t))
    for sgn in (-1,1): ell(d,sgn*.3*s,-.2,.3*s,.28,(255,140,40,255),(200,90,10,255),.03); ell(d,sgn*.22*s,.25,.2*s,.22,(255,200,60,255),(200,140,10,255),.03); ell(d,sgn*.3*s,-.2,.08*s,.08,W)
    bc=(60,45,35,255); rr(d,-.04,-.3,.04,.4,.04,bc); thick_line(d,[(0,-.3),(-.12,-.5)],.02,bc); thick_line(d,[(0,-.3),(.12,-.5)],.02,bc); return xform(im,1,0,0,-.04*sg(t))
def f_apple(t):
    im,d=layer(); rd=(231,60,60,255); ell(d,-.2,.1,.32,.42,rd); ell(d,.2,.1,.32,.42,rd); ell(d,-.25,-.0,.08,.14,(255,150,140,255)); rr(d,-.03,-.45,.04,-.2,.02,(110,70,30,255)); poly(d,[(.04,-.35),(.35,-.5),(.25,-.28)],(60,180,80,255)); return xform(im,1,5*sg(t))
def f_banana(t):
    im,d=layer(); y=(255,225,60,255); d.arc([P(-.7,-.95),P(.7,.5)],25,155,fill=y,width=int(.3*K)); d.arc([P(-.7,-.95),P(.7,.5)],40,140,fill=(255,240,140,255),width=int(.08*K))
    for a in (25,155): ell(d,.7*math.cos(math.radians(a)),-.225+.725*math.sin(math.radians(a)),.08,.08,(110,70,30,255))
    return xform(im,1,-20+6*sg(t),0,-.1)
def f_melon(t):
    im,d=layer(); d.pieslice([P(-.62,-.9),P(.62,.34)],0,180,fill=(46,160,70,255)); d.pieslice([P(-.55,-.83),P(.55,.27)],0,180,fill=(240,250,225,255)); d.pieslice([P(-.5,-.78),P(.5,.22)],0,180,fill=(240,70,80,255))
    for x,y in [(-.25,-.05),(0,.05),(.25,-.05),(-.1,-.2),(.12,-.22)]: ell(d,x,y,.03,.05,DK)
    return xform(im,1,6*sg(t))
def f_straw(t):
    im,d=layer(); poly(d,hpts(.9,0,0,.05),(235,50,75,255),(190,30,55,255))
    for x,y in [(-.2,-.1),(.15,-.15),(0,.1),(-.1,.3),(.2,.15)]: ell(d,x,y,.025,.035,(255,230,120,255))
    star5(d,0,-.34,.3,.1,(60,180,80,255)); return xform(im,1,4*sg(t),0,-.03*abs(sg(t)))
def f_cherry(t):
    im,d=layer(); s=.05*sg(t); thick_line(d,[(-.25+s,.28),(-.12,-.1),(0,-.45)],.03,(90,130,50,255)); thick_line(d,[(.25+s,.36),(.12,-.1),(0,-.45)],.03,(90,130,50,255))
    ell(d,-.25+s,.35,.22,.22,(200,30,60,255),(150,20,40,255)); ell(d,.25+s,.43,.22,.22,(200,30,60,255),(150,20,40,255)); ell(d,-.32+s,.28,.05,.07,(255,140,150,255)); ell(d,.18+s,.36,.05,.07,(255,140,150,255)); poly(d,[(0,-.45),(.3,-.55),(.15,-.35)],(60,180,80,255)); return im
def f_lemon(t):
    im,d=layer(); y=(255,225,60,255); ell(d,0,0,.5,.36,y,(230,185,20,255),.03); ell(d,-.52,0,.08,.06,y,(230,185,20,255),.02); ell(d,.52,0,.08,.06,y,(230,185,20,255),.02); ell(d,-.18,-.12,.1,.05,(255,245,170,255)); poly(d,[(.2,-.3),(.5,-.5),(.4,-.25)],(60,180,80,255)); return xform(im,1,-25+6*sg(t))
def f_carrot(t):
    im,d=layer(); o=(255,140,30,255); poly(d,[(-.22,-.2),(.22,-.2),(0,.72)],o,dk_(o))
    for y,w in ((-.0,.14),(.2,.1),(.4,.06)): thick_line(d,[(-w,y),(w*.2,y+.03)],.025,dk_(o,.8))
    for a in (-25,0,25): thick_line(d,[(0,-.2),(.28*math.sin(math.radians(a)),-.2-.4*math.cos(math.radians(a)))],.07,(60,180,80,255))
    return xform(im,1,25+5*sg(t))
def f_mush(t):
    im,d=layer(); rr(d,-.18,-.15,.18,.5,.08,(250,235,210,255),(200,185,160,255),.03); d.pieslice([P(-.55,-.7),P(.55,.4)],180,360,fill=(231,60,60,255),outline=(170,35,35,255),width=int(.03*K))
    for x,y,r in [(-.28,-.4,.09),(.2,-.5,.08),(0,-.25,.07),(.35,-.25,.06)]: ell(d,x,y,r,r*.8,W)
    return xform(im,1+.04*sg(t))
def f_pizza(t):
    im,d=layer(); poly(d,[(-.55,-.4),(.55,-.4),(0,.62)],(255,200,60,255),(210,140,30,255),.03); rr(d,-.58,-.52,.58,-.34,.08,(205,140,70,255),(150,95,40,255),.03)
    for x,y in [(-.2,-.2),(.2,-.2),(0,.08),(-.05,.35)]: ell(d,x,y,.09,.09,(210,50,50,255))
    ell(d,.05,-.05,.025,.025,(60,160,60,255)); return xform(im,1,6*sg(t))
def f_burger(t):
    im,d=layer(); b=.02*sg(t); tan=(230,160,70,255)
    rr(d,-.55,.25,.55,.45,.1,tan,dk_(tan),.03); rr(d,-.55,.05-b,.55,.25-b,.04,(110,60,35,255)); rr(d,-.5,-.02-2*b,.5,.08-2*b,.03,(231,60,60,255)); thick_line(d,[(-.55,-.03-3*b),(-.35,.02-3*b),(-.15,-.03-3*b),(.05,.02-3*b),(.25,-.03-3*b),(.45,.02-3*b),(.55,-.03-3*b)],.06,(90,190,80,255))
    d.pieslice([P(-.55,-.55-4*b),P(.55,.45-4*b)],180,360,fill=tan,outline=dk_(tan),width=int(.03*K))
    for x,y in [(-.25,-.3),(0,-.4),(.25,-.3),(-.1,-.2),(.15,-.18)]: ell(d,x,y-4*b,.035,.02,(255,245,210,255))
    return im
def f_donut(t):
    rl,rd=layer(); ell(rd,0,0,.56,.56,(225,170,100,255),(180,120,60,255),.03); ell(rd,0,0,.5,.5,(255,140,190,255)); ell(rd,0,0,.18,.18,(0,0,0,0))
    for i,c in enumerate([(255,255,255),(255,230,80),(80,200,255),(120,230,120),(255,255,255),(255,230,80),(80,200,255),(120,230,120)]):
        a=i*math.pi/4+.3; r=.34; thick_line(rd,[(r*math.cos(a),r*math.sin(a)),(r*math.cos(a)+.07*math.cos(a+1),r*math.sin(a)+.07*math.sin(a+1))],.035,c+(255,))
    return xform(rl,1,360*t)
def f_icecream(t):
    im,d=layer(); c=(210,150,70,255); poly(d,[(-.28,0),(.28,0),(0,.68)],c,dk_(c),.03)
    for a,b in ((-.15,.15),(.15,.15)): thick_line(d,[(a,.0),(0,.4+.0*b)],.02,dk_(c,.8))
    ell(d,0,-.02,.34,.14,W,GR,.02); ell(d,0,-.2,.27,.14,(255,170,200,255)); ell(d,0,-.36,.19,.12,W,GR,.02); poly(d,[(-.06,-.45),(.06,-.45),(.0,-.62)],W)
    dy=.06*((t*2)%1); ell(d,.3,.06+dy,.04,.06,(255,170,200,255)); return xform(im,1,4*sg(t))
def f_cookie(t):
    im,d=layer(); circle(d,.55,(220,170,100,255),(170,115,50,255)); ell(d,.5,-.4,.22,.22,(0,0,0,0))
    for x,y in [(-.2,-.2),(.15,.0),(-.1,.2),(.25,.3),(-.35,.1),(0,-.35)]: ell(d,x,y,.07,.06,(90,50,30,255))
    return xform(im,1,6*sg(t),0,-.03*abs(sg(t)))
def f_cake(t):
    im,d=layer(); rr(d,-.58,.08,.58,.5,.05,(255,200,215,255),(220,140,170,255),.03); rr(d,-.58,.02,.58,.14,.05,W,GR,.02); rr(d,-.4,-.25,.4,.05,.05,(255,230,240,255),(230,170,190,255),.03); rr(d,-.04,-.5,.04,-.25,.01,(231,60,60,255))
    flame(d,.14,.08,(255,150,30,255),.03*sg(t),-.56,t); flame(d,.08,.04,(255,235,110,255),.02*sg(t),-.52,t)
    for x in (-.4,-.15,.15,.4): ell(d,x,.3,.04,.04,(255,120,160,255))
    return im
def f_skullx(t):
    im,d=layer()
    for ang in (45,-45):
        a=math.radians(ang); e=[(-.55*math.cos(a),-.55*math.sin(a)),(.55*math.cos(a),.55*math.sin(a))]
        thick_line(d,e,.15,GRD); thick_line(d,e,.1,(245,245,240,255))
        for p in e: ell(d,p[0],p[1],.09,.09,(245,245,240,255),GRD,.02)
    im.alpha_composite(xform(f_skull(t),.8,0,0,-.05)); return im
def f_mic(t):
    im,d=layer(); poly(d,[(-.1,-.05),(.1,-.05),(.07,.6),(-.07,.6)],(70,75,90,255)); rr(d,-.12,.0,.12,.1,.02,GR,GRD,.02); ell(d,0,-.3,.28,.28,GR,GRD,.03)
    for i in (-1,0,1): thick_line(d,[(i*.12,-.55),(i*.1,-.1)],.015,GRD)
    thick_line(d,[(-.26,-.3),(.26,-.3)],.015,GRD); im=xform(im,1,-35+4*sg(t)); d=ImageDraw.Draw(im)
    for k in range(2):
        f2=(t+k/2)%1; r=.2+.3*f2
        if f2<.7: d.arc([P(-.2-r,-.5-r),P(-.2+r,-.5+r)],200,250,fill=(110,120,135,255),width=int(.05*K))
    return im
def f_tv(t):
    im,d=layer(); thick_line(d,[(-.08,-.45),(-.3,-.7)],.03,GRD); thick_line(d,[(.08,-.45),(.3,-.7)],.03,GRD)
    rr(d,-.6,-.45,.6,.5,.1,(120,85,55,255),(80,55,30,255),.03); cols=[(255,255,255),(255,230,80),(80,230,230),(120,230,120),(230,100,230),(231,76,60),(80,100,240)]
    k=int(t*7)%7; rr(d,-.5,-.35,.3,.4,.06,cols[k]+(255,)); ell(d,.43,-.15,.06,.06,(60,50,40,255)); ell(d,.43,.05,.06,.06,(60,50,40,255)); return im
def f_camera(t):
    im,d=layer(); c=(60,64,78,255); rr(d,-.25,-.5,.15,-.3,.04,c); rr(d,-.6,-.32,.6,.45,.1,c,(35,38,48,255),.03); rr(d,.3,-.42,.5,-.32,.03,(231,76,60,255))
    ell(d,0,.07,.3,.3,(35,38,48,255)); ell(d,0,.07,.22,.22,(88,150,246,255)); ell(d,-.07,0,.07,.05,W)
    if .72<t<.85: star4(d,.4,-.55,.3,W); ell(d,0,.07,.22,.22,(255,255,255,255))
    return im
def f_receiver(t):
    im,d=layer(); c=(231,60,60,255); d.arc([P(-.6,-.4),P(.6,.8)],205,335,fill=c,width=int(.2*K))
    for a in (205,335): ell(d,.6*math.cos(math.radians(a)),.2+.6*math.sin(math.radians(a)),.17,.17,c,(170,35,35,255),.03)
    return xform(im,1,-20+(12*math.sin(8*math.pi*t) if t<.5 else 0))
def f_tube(t):
    im,d=layer(); rr(d,-.15,-.55,.15,.5,.15,(215,238,252,255),(130,170,200,255),.03); rr(d,-.12,-.0,.12,.47,.12,(60,200,120,255)); rr(d,-.2,-.6,.2,-.52,.03,(130,170,200,255))
    for k in range(3): f2=(t+k/3)%1; ell(d,-.04+.05*k,.4-.4*f2,.025,.025,(200,255,220,255))
    return xform(im,1,20+8*sg(t))
def f_ball2(t):
    im,d=layer(); rr(d,-.3,.38,.3,.5,.03,(190,150,40,255)); poly(d,[(-.32,.5),(.32,.5),(.22,.3),(-.22,.3)],(255,193,7,255),(200,140,0,255),.02)
    ell(d,0,-.1,.45,.45,(155,89,182,255),(110,60,150,255),.03); ell(d,-.15,-.25,.12,.08,(220,180,245,255))
    a=math.radians(360*t); d.arc([P(-.28,-.38),P(.28,.18)],360*t,360*t+120,fill=(210,160,240,255),width=int(.04*K))
    for x,y,ph in [(.15,-.1,0),(-.15,.0,.33),(.05,-.3,.66)]: star4(d,x,y,.12*twinkle(t,ph),(255,240,150,255))
    return im
def f_candle(t):
    im,d=layer(); rr(d,-.17,-.1,.17,.6,.04,(255,245,220,255),(220,205,170,255),.03); ell(d,.1,-.1,.05,.1,(255,245,220,255)); thick_line(d,[(0,-.1),(0,-.2)],.02,DK)
    flame(d,.28,.14,(255,150,30,255),.04*sg(t),-.4,t); flame(d,.16,.07,(255,235,110,255),.03*sg(t+.2),-.36,t); return im
def f_ring(t):
    im,d=layer(); ell(d,0,.15,.36,.36,None,(255,193,7,255),.12); poly(d,[(-.2,-.2),(.2,-.2),(.28,-.35),(.1,-.55),(-.1,-.55),(-.28,-.35)],(120,220,255,255),(50,150,200,255),.03)
    thick_line(d,[(-.2,-.2),(-.1,-.55)],.015,(50,150,200,255)); thick_line(d,[(.2,-.2),(.1,-.55)],.015,(50,150,200,255)); star4(d,.3,-.55,.2*twinkle(t),W); return xform(im,1,5*sg(t))
def f_rose(t):
    im,d=layer(); g=(60,160,70,255); thick_line(d,[(0,-.0),(0,.65)],.07,g); poly(d,[(0,.35),(.3,.2),(.12,.5)],g); poly(d,[(0,.5),(-.28,.38),(-.1,.62)],g)
    r=(220,40,60,255); rd=(160,20,40,255); ell(d,0,-.25,.32,.3,r,rd,.03); ell(d,-.18,-.22,.16,.22,(240,70,90,255),rd,.02); ell(d,.18,-.22,.16,.22,(240,70,90,255),rd,.02); ell(d,0,-.3,.12,.15,(200,30,50,255),rd,.02)
    return xform(im,1,5*sg(t))
def f_seedling(t):
    im,d=layer(); gr=ease_out_back(t/.5) if t<.85 else 1-ease_in((t-.85)/.15); h=.65*max(0,gr); ell(d,0,.55,.5,.12,(130,90,50,255)); g=(60,180,80,255)
    if h>.02: thick_line(d,[(0,.55),(0,.55-h)],.07,(60,150,70,255))
    s=max(0,gr-.3)
    if s>0: y=.55-h*.85; poly(d,[(0,y),(.4*s,y-.2*s),(.15*s,y+.1*s)],g,(40,140,60,255),.02); poly(d,[(0,y+.05),(-.38*s,y-.15*s),(-.14*s,y+.15*s)],g,(40,140,60,255),.02)
    return im
def f_blossom(t):
    rl,rd=layer()
    for k in range(5): a=math.radians(k*72); ell(rd,.3*math.sin(a),-.3*math.cos(a),.22,.22,(255,170,200,255),(230,120,160,255),.025)
    im=xform(rl,1,72*t); d=ImageDraw.Draw(im); ell(d,0,0,.1,.1,(255,214,0,255))
    for k in range(5): a=math.radians(k*72+36); ell(d,.17*math.sin(a),-.17*math.cos(a),.025,.025,(200,120,0,255))
    return im
def f_soccer(t):
    rl,rd=layer(); circle(rd,.58,W,(60,64,78,255)); c=(45,48,60,255)
    poly(rd,[(.2*math.sin(math.radians(k*72)),-.2*math.cos(math.radians(k*72))) for k in range(5)],c)
    for k in range(5):
        a=math.radians(k*72); thick_line(rd,[(.2*math.sin(a),-.2*math.cos(a)),(.4*math.sin(a),-.4*math.cos(a))],.03,c)
        ell(rd,.47*math.sin(a),-.47*math.cos(a),.09,.09,c)
    im=xform(rl,1,72*t); d=ImageDraw.Draw(im); ring(d,.58,(60,64,78,255),.04); return im
def f_balloon(t):
    im,d=layer(); s=.06*sg(t); ell(d,0,-.15,.38,.46,(231,60,60,255),(180,35,35,255),.03); ell(d,-.14,-.3,.07,.12,(255,150,150,255)); poly(d,[(-.07,.3),(.07,.3),(0,.4)],(180,35,35,255)); thick_line(d,[(0,.4),(.06+s,.52),(-.06-s,.64),(0,.75)],.02,(120,125,140,255)); return xform(im,1,5*sg(t),0,-.05*sg(t))

# ===== gelombang 6 =====
BR=(150,95,50,255); BRD=(100,60,30,255); RE=(231,60,60,255); RED_=(170,35,35,255); GN2=(60,180,80,255); WD=(190,140,80,255)
def person(d,x=0,y=0,s=1,shirt=BL,pants=(60,64,90,255),skin=SK,hair=DK,legs=1,arms=1):
    if legs: rr(d,x-.15*s,y+.18*s,x-.02*s,y+.58*s,.04*s,pants); rr(d,x+.02*s,y+.18*s,x+.15*s,y+.58*s,.04*s,pants)
    rr(d,x-.18*s,y-.2*s,x+.18*s,y+.24*s,.07*s,shirt)
    if arms: rr(d,x-.28*s,y-.18*s,x-.17*s,y+.14*s,.05*s,shirt); rr(d,x+.17*s,y-.18*s,x+.28*s,y+.14*s,.05*s,shirt)
    ell(d,x,y-.38*s,.17*s,.18*s,skin,dk_(skin,.85),.012)
    if hair: d.pieslice([P(x-.18*s,y-.57*s),P(x+.18*s,y-.19*s)],180,360,fill=hair)
    ell(d,x-.06*s,y-.35*s,.02*s,.025*s,DK); ell(d,x+.06*s,y-.35*s,.02*s,.025*s,DK)
def _scene(fn,rot=0,bob=0):
    def f(t):
        im,d=layer(); fn(d,t); return xform(im,1,rot*sg(t),0,bob*sg(t))
    return f
def wins(d,x0,y0,cols,rows,dx,dy,w,h,t,on=(255,230,120,255),off=(90,100,130,255)):
    for i in range(cols):
        for j in range(rows): rr(d,x0+i*dx,y0+j*dy,x0+i*dx+w,y0+j*dy+h,.01,on if ((i*7+j*3+int(t*4))%3)!=0 else off)
# --- tangan ---
def _h_thumb(d,t):
    rr(d,-.6,-.0,-.4,.52,.04,BL); rr(d,-.4,.0,.35,.52,.1,SK,SKD,.02)
    for k in range(3): thick_line(d,[(.0,.12+.12*k),(.3,.12+.12*k)],.02,SKD)
    rr(d,-.35,-.5,-.1,.05,.1,SK,SKD,.02)
def _h_point(d,t):
    rr(d,-.35,-.0,.35,.62,.1,SK,SKD,.02); rr(d,-.12,-.6,.08,.08,.09,SK,SKD,.02); rr(d,-.35,.55,.35,.7,.03,BL)
    for k in range(2): thick_line(d,[(.1+.1*k,.05),(.1+.1*k,.15)],.02,SKD)
def _h_ok(d,t):
    rr(d,-.6,.05,-.4,.55,.04,BL); rr(d,-.4,.05,.2,.55,.1,SK,SKD,.02); ell(d,.15,-.12,.2,.2,None,SK,.1); ell(d,.15,-.12,.2,.2,None,SKD,.02)
    for i,a in enumerate((-.15,-.35,-.55)): rr(d,.05+.15*i+.1,a-.3+.15*i,.17+.15*i+.1,.15,.05,SK,SKD,.02)
def f_wave(t):
    im,d=layer(); rr(d,-.25,-.05,.25,.5,.1,SK,SKD,.02)
    for i,hgt in enumerate((.45,.55,.5,.4)): rr(d,-.25+.12*i,-.05-hgt,-.15+.12*i,-.0,.05,SK,SKD,.02)
    rr(d,-.45,.1,-.2,.3,.08,SK,SKD,.02); return xform(im,1,18*sg(t)+10,0,.03)
# --- orang ---
def _p_stand(d,t): person(d,0,.05,1.5)
def f_ped(t):
    im,d=layer(); w=.08*sg(t); s=1.4; rr(d,-.15*s*.1-.15,.18*s+.05-w*0,-.02,.6,.04,(60,64,90,255)); person(d,0,.0,1.4,legs=0); a=.12*sg(t)
    rr(d,-.16,.28,-.04,.7,.05,(60,64,90,255)); rr(d,.04+a,.28,.16+a,.7,.05,(60,64,90,255)); return im
def f_run(t):
    im,d=layer(); a=.2*sg(t); person(d,0,-.05,1.3,legs=0); rr(d,-.15-a,.25,-.03-a,.64,.05,(60,64,90,255)); rr(d,.03+a,.25,.15+a,.64,.05,(60,64,90,255)); return xform(im,1,-10,0,-.03*abs(sg(2*t)))
def f_adult(t):
    im,d=layer(); person(d,0,.05,1.5,(46,204,113,255)); return xform(im,1,0,0,-.03*abs(sg(t)))
def f_baby(t):
    im,d=layer(); ell(d,0,.0,.5,.5,SK,SKD,.03); d.arc([P(-.1,-.65),P(.1,-.4)],200,340,fill=DK,width=int(.05*K)); ell(d,-.18,-.05,.05,.07,DK); ell(d,.18,-.05,.05,.07,DK); ell(d,-.3,.12,.09,.06,PK); ell(d,.3,.12,.09,.06,PK); d.arc([P(-.12,.1),P(.12,.28)],20,160,fill=DK,width=int(.04*K)); return xform(im,1,4*sg(t))
def f_judge(t):
    im,d=layer(); person(d,-.1,.05,1.5,(40,42,55,255),hair=DK); a=40*abs(sg(2*t)); rr(d,.15,-.1,.55,.0,.03,BR,BRD,.02); rr(d,.4,-.2,.5,.1,.03,BR,BRD,.02); return im
def f_office(woman):
    def f(t):
        im,d=layer(); person(d,0,.05,1.5,(70,75,95,255),(60,64,90,255),hair=(110,60,30,255) if woman else DK); poly(d,[(-.03,-.15),(.03,-.15),(.05,.1),(0,.15),(-.05,.1)],(231,60,60,255)); rr(d,.28,.2,.5,.42,.03,BR,BRD,.02)
        if woman: ell(d,-.2,-.45,.08,.2,(110,60,30,255)); ell(d,.2,-.45,.08,.2,(110,60,30,255))
        return xform(im,1,3*sg(t))
    return f
def f_cook(t):
    im,d=layer(); person(d,0,.1,1.4,W); rr(d,-.28,-.82,.28,-.65,.04,W,GR,.02); ell(d,0,-.9,.3,.2,W,GR,.02); ell(d,.38,.15,.18,.06,(60,64,78,255)); rr(d,.5,.12,.7,.18,.02,(60,64,78,255)); return xform(im,1,3*sg(t))
def f_turban(t):
    im,d=layer(); person(d,0,.1,1.5,(150,70,170,255)); ell(d,0,-.62,.27,.18,W,GR,.02); ell(d,0,-.62,.05,.05,(231,60,60,255)); return xform(im,1,3*sg(t))
def f_farmer(t):
    im,d=layer(); person(d,0,.1,1.5,(60,130,200,255),(150,110,60,255)); ell(d,0,-.68,.38,.08,(240,200,90,255),(190,150,40,255),.02); ell(d,0,-.76,.2,.12,(240,200,90,255),(190,150,40,255),.02); return xform(im,1,3*sg(t))
def f_spy(t):
    im,d=layer(); person(d,0,.1,1.5,(150,120,80,255),(110,85,55,255)); ell(d,0,-.62,.36,.07,(90,70,45,255)); rr(d,-.22,-.8,.22,-.62,.06,(90,70,45,255)); rr(d,-.14,-.42,.14,-.35,.02,(35,38,48,255)); ell(d,.45,.0+.03*sg(t),.12,.12,None,(95,105,125,255),.04); thick_line(d,[(.53,.09),(.62,.2)],.05,BR); return im
def f_mage(t):
    im,d=layer(); person(d,0,.1,1.4,(110,70,170,255)); poly(d,[(-.25,-.6),(.25,-.6),(.03,-1.0)],(110,70,170,255),(70,40,130,255),.02); ell(d,0,-.6,.35,.07,(110,70,170,255),(70,40,130,255),.02); star4(d,.03,-.8,.1+.04*twinkle(t),(255,235,100,255)); poly(d,[(-.12,-.25),(.12,-.25),(0,.05)],W,GR,.015); return xform(im,1,3*sg(t))
def f_vamp(t):
    im,d=layer(); poly(d,[(-.45,-.3),(.45,-.3),(.55,.65),(-.55,.65)],(40,25,55,255)); person(d,0,.1,1.4,(30,30,40,255),skin=(235,225,235,255),hair=(40,30,45,255)); poly(d,[(-.1,-.27),(-.07,-.2),(-.03,-.27)],W); poly(d,[(.1,-.27),(.07,-.2),(.03,-.27)],W); return xform(im,1,3*sg(t))
def f_hand_up(t):
    im,d=layer(); person(d,0,.15,1.4,(88,160,246,255)); rr(d,.2,-.6+.04*sg(2*t),.36,-.1,.06,(88,160,246,255)); ell(d,.28,-.68+.04*sg(2*t),.1,.1,SK,SKD,.02); return xform(im,1,3*sg(t))
def f_speakhead(t):
    im,d=layer(); person(d,-.2,.15,1.5,(150,160,175,255),legs=0,arms=0)
    for k in range(3):
        f=(t+k/3)%1; r=.15+.3*f
        if f<.8: d.arc([P(.2-r,-.4-r),P(.2+r,-.4+r)],-50,50,fill=BL,width=int(.05*K))
    return im
def f_family(n):
    def f(t):
        im,d=layer(); cols=[(88,101,242,255),(231,100,140,255),(255,170,40,255),(46,204,113,255)]
        pos=[(-.35,.0,1.0),(.0,-.0,1.0),(.33,.2,.7)] if n==3 else [(-.42,.0,.95),(-.12,.0,.95),(.2,.15,.75),(.5,.2,.65)]
        for i,(x,y,s) in enumerate(pos): person(d,x,y+.1-.03*max(0,sg(t+i*.25)),s,cols[i],arms=0)
        return im
    return f
def f_foot(t):
    im,d=layer()
    for k,(x,y,ph) in enumerate([(-.2,.25,0),(.2,-.25,.5)]):
        a=ease_io(clamp(1-abs(((t+ph)%1)-.3)*3)) ; c=(120,85,55,255)
        ell(d,x,y,.17,.28,c); ell(d,x,y-.33,.15,.14,c)
        for i in range(3): ell(d,x-.1+.1*i,y-.52,.035,.035,c)
        pass
    return im
def f_bed(t):
    im,d=layer(); rr(d,-.6,.05,.6,.35,.05,(150,100,60,255)); rr(d,-.6,.3,-.5,.55,.02,BRD); rr(d,.5,.3,.6,.55,.02,BRD); rr(d,-.55,-.1,-.15,.1,.06,W,GR,.02); ell(d,-.35,-.15,.14,.14,SK,SKD,.02)
    rr(d,-.2,-.05,.55,.15,.06,(88,101,242,255))
    for ph in (0,.5): f2=(t+ph)%1; txt(d,"z",.3+.2*f2,-.3-.3*f2,int(60+50*f2),BL)
    return im
# --- benda & tempat (gelombang 6, bagian 2) ---
def f_ballot(t):
    im,d=layer(); y=-.65+.5*ease_io(clamp(t/.6)) if t<.85 else -.65
    rr(d,-.2,y,.2,y+.5,.02,W,GR,.02); thick_line(d,[(-.1,y+.2),(-.03,y+.28),(.1,y+.1)],.04,BL)
    rr(d,-.55,-.05,.55,.55,.06,GR,GRD,.03); rr(d,-.3,-.08,.3,.0,0,(40,42,55,255)); return im
def f_masks(t):
    im,d=layer(); a=4*sg(t)
    def mask(x,y,col,dkc,smile,rot):
        l,e=layer(); ell(e,0,0,.34,.42,col,dkc,.03); [ell(e,s*.14,-.1,.07,.05,(50,35,20,255)) for s in(-1,1)]
        e.arc([P(-.17,-.0 if smile else .12),P(.17,.28 if smile else .4)],20 if smile else 200,160 if smile else 340,fill=(50,35,20,255),width=int(.05*K))
        return xform(l,1,rot,x,y)
    im.alpha_composite(mask(-.18,-.06,(255,200,60,255),(210,150,20,255),True,12+a)); im.alpha_composite(mask(.22,.1,(150,110,210,255),(100,70,160,255),False,-12-a)); return im
def f_wolf(t):
    im,d=layer(); g=(150,158,175,255); poly(d,[(-.55,-.05),(-.5,-.68),(-.2,-.3),(.2,-.3),(.5,-.68),(.55,-.05),(.3,.35),(0,.62),(-.3,.35)],g,dk_(g),.03)
    poly(d,[(-.28,.05),(.28,.05),(0,.6)],(235,238,245,255)); poly(d,[(-.5,-.55),(-.36,-.3),(-.46,-.15)],(110,115,130,255)); poly(d,[(.5,-.55),(.36,-.3),(.46,-.15)],(110,115,130,255))
    b=bl(t); [ell(d,x,-.08,.06,.05*b,(255,200,60,255)) for x in(-.2,.2)]; ell(d,0,.55,.07,.05,DK); return xform(im,1,5*sg(t))
def f_brain(t):
    im,d=layer(); ripple(d,t,(255,150,170,255)); p=(255,150,170,255); pd=(210,90,120,255)
    ell(d,-.2,-.05,.38,.4,p,pd,.03); ell(d,.2,-.05,.38,.4,p,pd,.03); ell(d,0,.32,.1,.2,p,pd,.03)
    for pts in ([(0,-.4),(0,.2)],[(-.45,-.1),(-.3,-.15),(-.25,.0)],[(.45,-.1),(.3,-.15),(.25,.0)],[(-.35,.15),(-.2,.1),(-.15,.2)],[(.35,.15),(.2,.1),(.15,.2)]): thick_line(d,pts,.025,pd)
    return xform(im,1+.05*sg(t))
def f_sunrise(t):
    im,d=layer(); y=.3-.35*ease_io(clamp(t/.5)) if t<.5 else (-.05+.35*ease_io(clamp((t-.7)/.3)) if t>.7 else -.05)
    d.pieslice([P(-.45,y-.45),P(.45,y+.45)],180,360,fill=(255,200,40,255))
    for i in range(1,8):
        a=math.radians(180+i*22.5); thick_line(d,[(.55*math.cos(a),y+.55*math.sin(a)),(.7*math.cos(a),y+.7*math.sin(a))],.06,(255,190,40,255))
    rr(d,-.65,.3,.65,.6,.04,(60,70,110,255)); rr(d,-.65,.3,.65,.36,0,(255,140,60,255)); return im
def f_dumpling(t):
    im,d=layer(); d.pieslice([P(-.6,-.55),P(.6,.65)],180,360,fill=(252,244,225,255),outline=(200,180,140,255),width=int(.03*K)); rr(d,-.6,.05,.6,.12,.0,(200,180,140,255))
    for i in range(6): x=-.45+.18*i; thick_line(d,[(x,.05),(x+.03,-.12)],.025,(200,180,140,255))
    for k in range(2):
        f2=(t+k/2)%1
        if f2<.7: ell(d,-.1+.2*k+.04*math.sin(6*f2),-.5-.3*f2,.05,.05,(220,225,235,255))
    return im
def f_sunset(t):
    im,d=layer(); y=.1+.15*sg(t); d.pieslice([P(-.4,y-.4),P(.4,y+.4)],180,360,fill=(255,140,60,255))
    for x,h,w in [(-.6,.5,.25),(-.3,.7,.22),(0,.45,.26),(.28,.8,.22),(.55,.55,.25)]:
        rr(d,x-w/2,.55-h,x+w/2,.6,.0,(60,70,110,255)); wins(d,x-w/2+.04,.55-h+.06,2,max(1,int(h/.2)),.1,.17,.05,.07,t)
    return im
def f_luggage(t):
    im,d=layer(); d.arc([P(-.2,-.5),P(.2,-.1)],180,360,fill=BRD,width=int(.06*K)); rr(d,-.5,-.25,.5,.5,.08,BR,BRD,.03)
    for x in(-.3,.3): rr(d,x-.05,-.25,x+.05,.5,0,BRD)
    rr(d,-.08,0,.08,.14,.02,(255,193,7,255)); ell(d,-.3,.56,.06,.06,(60,64,78,255)); ell(d,.3,.56,.06,.06,(60,64,78,255)); return xform(im,1,3*sg(t),0,-.03*abs(sg(t)))
def f_truck(t):
    im,d=layer(); rr(d,-.65,-.35,.15,.3,.04,W,GR,.03); rr(d,.15,-.15,.6,.3,.06,(52,120,246,255),(30,80,200,255),.03); rr(d,.3,-.08,.5,.08,.02,(190,225,255,255))
    for x in(-.4,.35):
        ell(d,x,.36,.16,.16,(45,48,55,255)); ell(d,x,.36,.06,.06,GR)
        for k in range(2): a=math.radians(360*t*.5+k*90); thick_line(d,[(x-.14*math.cos(a),.36-.14*math.sin(a)),(x+.14*math.cos(a),.36+.14*math.sin(a))],.02,GR)
    for k in range(3): thick_line(d,[(-.7-.1*k,.55),(-.6-.1*k,.55)],.03,(190,195,205,255))
    return xform(im,1,0,0,-.015*sg(4*t))
def f_city(t):
    im,d=layer()
    for x,h,w,c in [(-.55,.5,.28,(88,101,242,255)),(-.25,.9,.28,(60,70,200,255)),(.05,.65,.3,(88,101,242,255)),(.36,.8,.28,(60,70,200,255)),(.62,.4,.22,(88,101,242,255))]:
        rr(d,x-w/2,.55-h,x+w/2,.6,0,c); wins(d,x-w/2+.04,.55-h+.06,2,max(1,int((h-.08)/.15)),.11,.15,.06,.08,t)
    return im
def f_hamwr(t):
    a=6*sg(t); h,e=layer(); rr(e,-.06,-.3,.06,.62,.03,BR,BRD,.02); rr(e,-.4,-.55,.4,-.22,.06,GR,GRD,.03)
    w,g=layer(); rr(g,-.08,-.12,.08,.62,.08,(150,160,175,255),GRD,.03); ell(g,0,-.34,.24,.24,(150,160,175,255),GRD,.03); rr(g,-.1,-.66,.1,-.36,0,(0,0,0,0))
    im=xform(h,1,40+a); im.alpha_composite(xform(w,1,-40-a)); return im
def f_bow(t):
    im,d=layer(); pull=ease_io(clamp(t/.45)) if t<.55 else 0; fly=clamp((t-.55)/.3) if t>=.55 else 0
    px=-.3*pull; d.arc([P(-.8,-.6),P(.4,.6)],-70,70,fill=BR,width=int(.08*K))
    thick_line(d,[(0,-.56),(px,0),(0,.56)],.015,(220,220,225,255))
    if fly<1:
        x0=px+1.6*fly; poly(d,[(x0+.9,0),(x0+.78,-.07),(x0+.78,.07)],GR); thick_line(d,[(x0,0),(x0+.8,0)],.03,(190,150,90,255)); poly(d,[(x0,0),(x0-.1,-.08),(x0+.1,0)],RE); poly(d,[(x0,0),(x0-.1,.08),(x0+.1,0)],RE)
    return im
def f_mailbox(raised):
    def f(t):
        im,d=layer(); rr(d,-.06,.2,.06,.65,.01,GR,GRD,.02); rr(d,-.5,-.3,.5,.22,.22,BL,BLD,.03); ell(d,.4,-.04,.11,.2,(40,42,60,255)); rr(d,.2,-.15,.5,-.1,0,W)
        o=0 if raised else .35; w=.03*sg(t) if raised else 0
        thick_line(d,[(-.3,-.3),(-.3,-.62+o)],.04,GR); rr(d,-.3,-.64+o+w,-.1,-.5+o+w,.02,RE)
        return im
    return f
def f_cards(t):
    im,d=layer(); rr(d,-.38,-.55,.38,.55,.07,W,GR,.03)
    for k in range(5): a=math.radians(k*72); ell(d,.17*math.sin(a),-.17*math.cos(a),.1,.1,(255,110,150,255))
    ell(d,0,0,.07,.07,(255,214,0,255)); return xform(im,1,-10+5*sg(t))
def f_joker(t):
    im,d=layer(); rr(d,-.4,-.58,.4,.58,.07,W,GR,.03); ell(d,0,.0,.2,.2,SK,SKD,.02); poly(d,[(-.2,-.1),(-.32,-.42),(-.05,-.2)],RE); poly(d,[(.2,-.1),(.32,-.42),(.05,-.2)],(52,120,246,255)); poly(d,[(-.2,-.1),(.2,-.1),(0,-.3)],(46,204,113,255))
    ell(d,-.32,-.44,.04,.04,(255,214,0,255)); ell(d,.32,-.44,.04,.04,(255,214,0,255)); ell(d,-.07,.0,.025,.03,DK); ell(d,.07,.0,.025,.03,DK); d.arc([P(-.1,.02),P(.1,.14)],20,160,fill=DK,width=int(.03*K)); return xform(im,1,5*sg(t))
def f_buoy(t):
    rl,rd=layer()
    for i in range(8): rd.arc([P(-.45,-.45),P(.45,.45)],i*45,i*45+45,fill=W if i%2 else RE,width=int(.24*K))
    ring(rd,.57,GRD,.02); ring(rd,.33,GRD,.02); return xform(rl,1,90*t,0,-.03*sg(t))
def f_bank(dollar):
    def f(t):
        im,d=layer(); st=(235,225,200,255); so=(170,155,120,255)
        poly(d,[(-.65,-.2),(0,-.65),(.65,-.2)],st,so,.03); rr(d,-.65,.45,.65,.58,.02,st,so,.03); rr(d,-.58,.35,.58,.45,.0,st,so,.02)
        for x in(-.45,-.15,.15,.45): rr(d,x-.07,-.15,x+.07,.35,.02,st,so,.02)
        rr(d,-.65,-.2,.65,-.12,0,st,so,.02)
        if dollar: txt(d,"$",0,-.34,70,(60,130,70,255))
        return xform(im,1+.03*sg(t))
    return f
def f_studiomic(t):
    im,d=layer(); ripple(d,t,(110,120,135,255)); d.arc([P(-.4,-.3),P(.4,.4)],20,160,fill=GRD,width=int(.05*K)); rr(d,-.03,.35,.03,.58,0,GRD); rr(d,-.25,.56,.25,.64,.03,GRD)
    rr(d,-.18,-.5,.18,.12,.18,GR,GRD,.03)
    for y in(-.4,-.3,-.2,-.1): thick_line(d,[(-.14,y),(.14,y)],.015,GRD)
    return im
def f_coffin(t):
    im,d=layer(); poly(d,[(-.2,-.68),(.2,-.68),(.4,-.15),(.24,.68),(-.24,.68),(-.4,-.15)],(130,85,50,255),(85,50,25,255),.04); rr(d,-.05,-.45,.05,.3,.01,(255,193,7,255)); rr(d,-.2,-.25,.2,-.15,.01,(255,193,7,255)); return xform(im,1,6*sg(t))
def f_dish(t):
    im,d=layer(); d.pieslice([P(-.45,-.45),P(.45,.45)],0,180,fill=(215,220,232,255),outline=GRD,width=int(.03*K)); thick_line(d,[(0,.0),(0,-.35)],.03,GRD); ell(d,0,-.38,.06,.06,RE)
    im=xform(im,1,-35); d=ImageDraw.Draw(im); rr(d,-.05,.15,.05,.5,0,GRD); rr(d,-.25,.48,.25,.58,.03,GRD)
    for k in range(3):
        f2=(t+k/3)%1; r=.2+.35*f2
        if f2<.75: d.arc([P(.2-r,-.45-r),P(.2+r,-.45+r)],-60,20,fill=BL,width=int(.05*K))
    return im
def f_salt(t):
    im,d=layer(); rr(d,-.28,-.1,.28,.55,.12,(225,240,252,255),GR,.03); rr(d,-.3,-.35,.3,-.08,.1,GR,GRD,.03)
    for x in(-.12,0,.12): ell(d,x,-.22,.015,.015,GRD)
    im2=xform(im,1,170+10*sg(2*t),0,0); d2=ImageDraw.Draw(im2)
    for k in range(6): f2=(t*2+k/6)%1; ell(d2,-.2+.08*k,-.45+.8*f2,.015,.015,W)
    return im2
def f_tickets(t):
    im,d=layer()
    for rot,col in ((-14,(255,159,28,255)),(10,(88,101,242,255))):
        l,e=layer(); rr(e,-.55,-.28,.55,.28,.06,col,dk_(col),.03); ell(e,-.55,0,.09,.09,(0,0,0,0)); ell(e,.55,0,.09,.09,(0,0,0,0)); star4(e,-.1,0,.18,W); im.alpha_composite(xform(l,1,rot+3*sg(t)))
    return im
def f_fork(t):
    im,d=layer(); circle(d,.42,W,GR); ring(d,.28,(210,215,225,255),.02)
    for x in(-.68,-.62,-.56): thick_line(d,[(x,-.4),(x,-.05)],.025,GR)
    thick_line(d,[(-.68,-.05),(-.56,-.05)],.03,GR); thick_line(d,[(-.62,-.05),(-.62,.55)],.05,GR); poly(d,[(.6,-.4),(.68,-.4),(.68,.1),(.6,.1)],GR); thick_line(d,[(.64,.1),(.64,.55)],.05,GR); return xform(im,1,3*sg(t))
def f_chicken(t):
    im,d=layer(); circle(d,.5,W,GR); [ell(d,x,-.55,.1,.12,RE) for x in(-.12,0,.12)]; b=bl(t); ell(d,-.17,-.1,.05,.06*b,DK); ell(d,.17,-.1,.05,.06*b,DK); poly(d,[(-.1,.05),(.1,.05),(0,.22)],(255,160,30,255)); ell(d,0,.3,.06,.1,RE); return xform(im,1,0,0,.04*abs(sg(2*t)))
def f_broom(t):
    im,d=layer(); thick_line(d,[(0,-.7),(0,.2)],.06,BR); poly(d,[(-.2,.2),(.2,.2),(.28,.7),(-.28,.7)],(240,200,90,255),(190,150,40,255),.03)
    for x in(-.12,0,.12): thick_line(d,[(x,.3),(x*1.5,.68)],.015,(190,150,40,255))
    rr(d,-.2,.15,.2,.25,.02,(110,70,30,255)); return xform(im,1,25+18*sg(t))
def f_ogre(t):
    im,d=layer(); r=(220,50,50,255); poly(d,[(-.4,-.4),(-.28,-.78),(-.12,-.4)],(255,230,200,255)); poly(d,[(.4,-.4),(.28,-.78),(.12,-.4)],(255,230,200,255)); ell(d,0,0,.55,.52,r,RED_,.03)
    thick_line(d,[(-.4,-.25),(-.1,-.12)],.06,DK); thick_line(d,[(.4,-.25),(.1,-.12)],.06,DK); ell(d,-.2,-.05,.07,.07,(255,230,100,255)); ell(d,.2,-.05,.07,.07,(255,230,100,255)); d.arc([P(-.3,.0),P(.3,.45)],20,160,fill=(80,15,15,255),width=int(.08*K))
    poly(d,[(-.2,.3),(-.13,.3),(-.17,.4)],W); poly(d,[(.2,.3),(.13,.3),(.17,.4)],W); return xform(im,1,4*sg(t))
def f_cart(t):
    im,d=layer(); thick_line(d,[(-.65,-.5),(-.45,-.5),(-.3,.3),(.45,.3)],.05,GRD); poly(d,[(-.42,-.3),(.6,-.3),(.5,.2),(-.3,.2)],GR,GRD,.03)
    for k in range(3): thick_line(d,[(-.2+.25*k,-.3),(-.17+.25*k,.2)],.015,GRD)
    for x in(-.2,.4): ell(d,x,.5,.07,.07,GRD)
    return xform(im,1,0,.02*sg(2*t),-.02*sg(4*t))
def f_steth(t):
    im,d=layer(); c=(60,64,78,255); thick_line(d,[(-.35,-.55),(-.35,-.1),(-.1,.25),(.0,.25)],.05,c); thick_line(d,[(.35,-.55),(.35,-.1),(.1,.25),(0,.25)],.05,c); thick_line(d,[(0,.25),(0,.4),(.2,.5)],.05,c)
    q=.09*(1+.3*max(0,sg(2*t))); ell(d,.3,.52,.2,.2,GR,GRD,.04); ell(d,.3,.52,q,q,RE); ell(d,-.35,-.58,.05,.05,GR); ell(d,.35,-.58,.05,.05,GR); return im
def f_dropc(col,hl):
    def f(t):
        im,d=layer(); flame(d,.5,.34,col,0,.05,t); ell(d,-.12,.12,.06,.1,hl); return xform(im,1+.05*sg(t),0,0,-.03*sg(t))
    return f
def f_satchel(t):
    im,d=layer(); rr(d,-.4,-.4,.4,.55,.15,RE,RED_,.03); rr(d,-.3,.05,.3,.45,.08,(200,40,40,255),RED_,.03); d.arc([P(-.2,-.62),P(.2,-.3)],180,360,fill=RED_,width=int(.06*K)); rr(d,-.06,.1,.06,.2,.02,(255,193,7,255)); thick_line(d,[(-.4,-.1),(-.4,.35)],.04,RED_); return xform(im,1,4*sg(t),0,-.03*abs(sg(t)))
def f_bags(t):
    im,d=layer()
    for x,col,ph in((-.2,RE,0),(.2,(52,120,246,255),.3)):
        a=4*math.sin(2*math.pi*(t+ph)); l,e=layer(); rr(e,-.28,-.25,.28,.45,.04,col,dk_(col),.03); e.arc([P(-.14,-.55),P(.14,-.1)],180,360,fill=dk_(col),width=int(.04*K)); im.alpha_composite(xform(l,1,a,x,0))
    return im
def f_housebs(t):
    im,d=layer()
    for x,y,c,s in((-.4,.1,(231,100,100,255),.9),(.35,.15,(88,150,246,255),.85),(0,-.05,(255,193,7,255),1.0)):
        rr(d,x-.28*s,y-.05*s,x+.28*s,y+.4*s,.0,c,dk_(c),.02); poly(d,[(x-.34*s,y-.05*s),(x,y-.4*s),(x+.34*s,y-.05*s)],(160,70,50,255),(110,45,30,255),.02); rr(d,x-.06*s,y+.15*s,x+.06*s,y+.4*s,0,BRD)
    return im
def f_spool(t):
    im,d=layer(); rr(d,-.3,-.55,.3,-.42,.03,WD,BRD,.02); rr(d,-.3,.42,.3,.55,.03,WD,BRD,.02); rr(d,-.22,-.42,.22,.42,.01,(231,100,140,255))
    for i in range(7): thick_line(d,[(-.22,-.36+.12*i),(.22,-.3+.12*i)],.015,(190,60,100,255))
    thick_line(d,[(.22,.3),(.4,.4),(.5,.3+.04*sg(t)),(.65,.45)],.02,(231,100,140,255)); return xform(im,1,3*sg(t))
def f_speaker(t):
    im,d=layer(); poly(d,[(-.55,-.15),(-.3,-.15),(.0,-.4),(.0,.4),(-.3,.15),(-.55,.15)],GR,GRD,.03)
    for k in range(3):
        f2=(t+k/3)%1; r=.2+.35*f2
        if f2<.8: d.arc([P(-r,-r),P(r,r)],-45,45,fill=BL,width=int(.06*(1-f2*.5)*K))
    return im
def f_dagger(t):
    im,d=layer(); poly(d,[(0,-.7),(.09,-.4),(.09,.1),(-.09,.1),(-.09,-.4)],(215,222,232,255),GRD,.02); thick_line(d,[(0,-.5),(0,.05)],.02,(160,170,185,255)); rr(d,-.22,.1,.22,.18,.02,(190,150,40,255)); rr(d,-.05,.18,.05,.5,.02,BR); ell(d,0,.55,.06,.06,(190,150,40,255)); star4(d,0,-.45,.15*twinkle(t),W); return xform(im,1,-35+4*sg(t))
def f_flagid(t):
    im,d=layer(); rr(d,-.56,-.68,-.48,.66,.02,GR,GRD,.02); dy=lambda x:.06*math.sin(2*math.pi*t-5*x)
    for j,c in enumerate(((231,40,50,255),(250,250,252,255))):
        for i in range(4):
            x0=-.48+i*.25; x1=x0+.25; y0=-.5+j*.3; y1=y0+.3; poly(d,[(x0,y0+dy(x0)),(x1,y0+dy(x1)),(x1,y1+dy(x1)),(x0,y1+dy(x0))],c)
    return im
def f_satellite(t):
    im,d=layer()
    for s in(-1,1):
        for i in range(3):
            x0=s*(.2+.17*i); x1=x0+s*.14; rr(d,min(x0,x1),-.18,max(x0,x1),.18,.01,(52,120,246,255),(30,80,200,255),.02)
    rr(d,-.2,-.22,.2,.22,.05,(190,198,210,255),GRD,.03); ell(d,0,-.3,.05,.05,RE if sg(2*t)>0 else (120,30,30,255)); thick_line(d,[(0,-.22),(0,-.38)],.02,GRD); return xform(im,1,-25+6*sg(t),0,-.03*sg(t))
def f_store(t):
    im,d=layer(); rr(d,-.55,-.2,.55,.55,.02,(250,250,252,255),GR,.03)
    for i in range(6): rr(d,-.55+.183*i,-.45,-.55+.183*(i+1),-.15,.0,(46,170,90,255) if i%2==0 else W,GR,.015)
    rr(d,-.45,.0,-.05,.35,.02,(190,225,255,255),GR,.02); rr(d,.1,.0,.4,.55,.02,(90,100,130,255)); ell(d,.17,.28,.025,.025,(255,193,7,255)); rr(d,-.35,-.7,.35,-.5,.04,(46,170,90,255)); return im
def f_fishrod(t):
    im,d=layer(); thick_line(d,[(-.6,.6),(.3,-.55)],.05,BR); thick_line(d,[(.3,-.55),(.55+.04*sg(t),.1)],.015,GR)
    ell(d,.55,.2+.1*sg(t),.2,.12,(255,170,40,255),(220,110,10,255),.02); poly(d,[(.72,.12+.1*sg(t)),(.88,.0+.1*sg(t)),(.88,.24+.1*sg(t))],(255,120,30,255)); ell(d,.48,.17+.1*sg(t),.025,.025,DK); return im
def f_boot(t):
    im,d=layer(); poly(d,[(-.2,-.55),(.15,-.55),(.15,.0),(.55,.2),(.55,.5),(-.2,.5)],(150,70,50,255),(100,40,25,255),.04); rr(d,-.2,.45,.2,.58,.02,(60,35,25,255)); rr(d,.3,.45,.58,.52,.02,(60,35,25,255)); thick_line(d,[(-.2,-.4),(.15,-.4)],.03,(100,40,25,255)); return xform(im,1,5*sg(t))
def f_chains(t):
    im,d=layer(); s=.05*sg(t); rr(d,-.55-s,-.17,.1-s,.17,.17,None,(150,155,170,255),.1); rr(d,-.1+s,-.17,.55+s,.17,.17,None,(110,115,130,255),.1); return xform(im,1,45+4*sg(t))
def f_desktop(t):
    im,d=layer(); rr(d,-.6,-.5,.6,.25,.06,(60,64,78,255),(40,42,55,255),.03); rr(d,-.52,-.42,.52,.17,.03,(60,130,200,255)); rr(d,-.08,.25,.08,.45,0,GR); rr(d,-.3,.45,.3,.55,.03,GR,GRD,.02)
    for k in range(3): thick_line(d,[(-.4,-.3+.15*k),(-.3+.5*((t*3+k*.4)%1),-.3+.15*k)],.04,W)
    return im
def f_office_b(t):
    im,d=layer(); rr(d,-.4,-.7,.4,.6,0,(110,125,160,255),(70,80,110,255),.03); wins(d,-.3,-.58,3,7,.2,.17,.12,.1,t); rr(d,-.08,.42,.08,.6,0,(60,50,40,255)); return im
def f_grapes(t):
    im,d=layer(); p=(140,70,180,255)
    for (x,y) in [(-.3,-.2),(0,-.2),(.3,-.2),(-.15,0),(.15,0),(0,.2),(-.15,.2),(.15,.2),(0,.4)]: ell(d,x,y,.16,.16,p,dk_(p),.02); ell(d,x-.05,y-.05,.04,.03,(200,150,225,255))
    thick_line(d,[(0,-.4),(0,-.65)],.05,BRD); poly(d,[(0,-.55),(.4,-.7),(.3,-.45)],GN2); return xform(im,1,5*sg(t))
def f_knife(t):
    im,d=layer(); poly(d,[(-.08,-.7),(.09,-.7),(.09,.1),(-.08,.1)],(215,222,232,255),GRD,.02); rr(d,-.06,.1,.08,.55,.04,BR,BRD,.02); star4(d,0,-.45,.15*twinkle(t),W); return xform(im,1,-40+4*sg(t))
def _paw(d,x,y,s,c):
    ell(d,x,y+.1*s,.2*s,.17*s,c)
    for dx,dy,r in((-.22,-.12,.08),(-.08,-.26,.08),(.08,-.26,.08),(.22,-.12,.08)): ell(d,x+dx*s,y+dy*s+.1*s,r*s,r*1.2*s,c)
def f_paw(t):
    im,d=layer(); c=(120,85,55,255); _paw(d,-.25,.2,1.0+.2*max(0,sg(t)),c); _paw(d,.3,-.2,1.0+.2*max(0,-sg(t)),c); return im
def f_idcard(t):
    im,d=layer(); rr(d,-.6,-.4,.6,.4,.06,W,GR,.03); rr(d,-.6,-.4,.6,-.22,.06,BL); rr(d,-.5,-.12,-.15,.28,.03,(190,210,240,255)); ell(d,-.32,-.03,.07,.07,GR); d.pieslice([P(-.45,.05),P(-.19,.35)],180,360,fill=GR)
    for k in range(3): thick_line(d,[(-.05,-.05+.12*k),(.45,-.05+.12*k)],.03,(190,195,205,255))
    return xform(im,1,4*sg(t))
def f_chair(t):
    im,d=layer(); rr(d,-.3,-.65,.3,.0,.04,WD,BRD,.03); rr(d,-.4,.0,.4,.15,.03,WD,BRD,.03)
    for x in(-.35,.35): rr(d,x-.04,.15,x+.04,.62,.01,BRD)
    for y in(-.5,-.35,-.2): thick_line(d,[(-.22,y),(.22,y)],.025,BRD)
    return xform(im,1,3*sg(t))
def f_coffee(t):
    im,d=layer(); ell(d,0,.45,.55,.1,W,GR,.03); rr(d,-.35,-.1,.35,.42,.12,W,GR,.03); ell(d,.4,.15,.15,.15,None,GR,.05); ell(d,0,-.1,.35,.08,(110,70,40,255))
    for k in range(3):
        x=-.15+.15*k; ph=(t+k/3)%1
        if ph<.85: thick_line(d,[(x+.04*math.sin(6*(ph+i*.2)),-.2-.1*i-.15*ph) for i in range(4)],.03,(210,215,225,255))
    return im
def f_clink(t):
    im,d=layer(); a=10+6*max(0,sg(2*t))
    for s in(-1,1):
        l,e=layer(); poly(e,[(-.2,-.5),(.2,-.5),(.12,.1),(-.12,.1)],(220,235,250,255),GR,.03); poly(e,[(-.17,-.3),(.17,-.3),(.12,.05),(-.12,.05)],(255,225,100,255)); rr(e,-.02,.1,.02,.45,0,GR); rr(e,-.15,.45,.15,.52,.02,GR)
        for k in range(3): ell(e,-.06+.06*k,-.1-.05*((k+int(t*4))%3),.015,.015,W)
        im.alpha_composite(xform(l,1,-s*a,s*.28,0))
    star4(d,0,-.5,.2*max(0,sg(2*t)),W); return im
def f_bottle(t):
    im,d=layer(); rr(d,-.2,-.2,.2,.55,.07,(220,235,250,255),GR,.03); rr(d,-.17,.1,.17,.52,.05,W); poly(d,[(-.1,-.2),(.1,-.2),(.06,-.45),(-.06,-.45)],(255,200,160,255),(210,150,110,255),.02); rr(d,-.24,-.28,.24,-.2,.03,(255,130,170,255)); thick_line(d,[(-.2,0),(-.1,0)],.02,GR); return xform(im,1,6*sg(t),0,-.02*sg(2*t))
def f_redenv(t):
    im,d=layer(); rr(d,-.38,-.58,.38,.58,.05,RE,RED_,.03); poly(d,[(-.38,-.58),(0,-.1),(.38,-.58)],(200,40,40,255),RED_,.02); ell(d,0,-.08,.12,.12,(255,214,0,255),(200,150,0,255),.02); return xform(im,1,5*sg(t))
def f_house(garden):
    def f(t):
        im,d=layer(); rr(d,-.45,-.05,.45,.55,.0,(250,235,200,255),(190,160,110,255),.03); poly(d,[(-.55,-.05),(0,-.55),(.55,-.05)],(200,70,50,255),(140,40,30,255),.03); rr(d,-.08,.2,.1,.55,0,BR); rr(d,-.35,.05,-.17,.22,0,(190,225,255,255),GR,.02); rr(d,.17,.05,.35,.22,0,(190,225,255,255),GR,.02)
        if garden:
            ell(d,.65,.35,.18,.2,(60,160,70,255)); rr(d,.62,.4,.68,.58,0,BRD)
            for x,c in((-.6,(255,110,150,255)),(-.5,(255,214,0,255))): thick_line(d,[(x,.58),(x,.45)],.02,GN2); ell(d,x,.42,.05,.05,c)
        return xform(im,.9,2*sg(t))
    return f
def f_pan(t):
    im,d=layer(); dy=-.12*abs(sg(t)); ell(d,-.1,.1,.55,.4,(60,64,78,255),(35,38,50,255),.04); rr(d,.4,.05,.85,.15,.04,(60,64,78,255)); l,e=layer(); ell(e,0,0,.3,.22,W,GR,.02); ell(e,0,0,.1,.1,(255,200,40,255)); im.alpha_composite(xform(l,1,0,-.1,.05+dy)); return im
def f_inf(t):
    f=lambda u:(.6*math.cos(u)/(1+math.sin(u)**2),.6*math.sin(u)*math.cos(u)/(1+math.sin(u)**2)*1.4)
    im,d=layer(); thick_line(d,[f(i/60*2*math.pi) for i in range(61)],.1,BL); x,y=f(2*math.pi*t); ell(d,x,y,.09,.09,(255,214,0,255)); return im
def f_pistol(t):
    im,d=layer(); poly(d,[(-.55,-.25),(.5,-.25),(.5,0),(.1,0),(.05,.55),(-.2,.55),(-.2,.05),(-.55,.05)],(255,140,40,255),(200,90,10,255),.03); rr(d,.4,-.2,.6,-.05,.02,(88,101,242,255)); rr(d,-.35,-.35,.15,-.25,.03,(88,101,242,255))
    for k in range(3):
        f2=(t+k/3)%1
        if f2<.8: ell(d,.65+.3*f2,-.12+.05*f2,.04,.04,(90,170,255,255))
    return im
def f_puzzle(t):
    im,d=layer(); c=(60,170,230,255); dc=(30,120,180,255); rr(d,-.4,-.4,.4,.4,.04,c,dc,.03); ell(d,0,-.4,.12,.12,c,dc,.03); ell(d,.4,0,.12,.12,c,dc,.03); ell(d,-.4,0,.12,.12,(0,0,0,0)); ell(d,0,.4,.12,.12,(0,0,0,0)); return xform(im,1,6*sg(t))
def f_bug(t):
    im,d=layer(); hy=.1+.1*math.sin(2*math.pi*(t-.5))
    for i in range(5): ell(d,-.5+.22*i,.1+.1*math.sin(2*math.pi*(t-i*.1)),.15,.15,(110,200,70,255) if i%2 else (80,170,60,255),(50,120,40,255),.02)
    ell(d,.5,hy,.2,.2,(110,200,70,255),(50,120,40,255),.02); ell(d,.55,hy-.05,.04,.04,DK); thick_line(d,[(.5,hy-.18),(.55,hy-.4)],.02,DK); return im
def f_syringe(t):
    im,d=layer(); p=.07*sg(t)+.1; rr(d,-.45,-.15,.35,.15,.04,(225,240,252,255),GR,.03); rr(d,-.4+p,-.1,.2,.1,.02,(231,60,60,255)); rr(d,-.55+p,-.2,-.45+p,.2,.02,GR); thick_line(d,[(-.75+p,0),(-.5+p,0)],.04,GR)
    rr(d,.35,-.04,.7,.04,0,(190,198,210,255)); return xform(im,1,-35)
def f_dividers(t):
    im,d=layer(); rr(d,-.5,-.1,.5,.55,.05,(190,150,90,255),BRD,.03)
    for i,c in enumerate(((231,100,100,255),(255,193,7,255),(88,150,246,255))): rr(d,-.45+.3*i,-.3-.05*max(0,sg(t+i*.2)),-.2+.3*i,-.05,.03,c,dk_(c),.02)
    return im
def f_clapper(t):
    im,d=layer(); rr(d,-.55,-.15,.55,.55,.04,(45,48,55,255),(20,22,26,255),.03)
    for i in range(4): rr(d,-.5+.27*i,.05,-.4+.27*i,.12,0,W)
    a=math.radians(-25*ease_io(1-abs(2*t-1))); px,py=-.55,-.15
    def R(x,y): return (px+(x-px)*math.cos(a)+(y-py)*math.sin(a), py-(x-px)*math.sin(a)+(y-py)*math.cos(a))
    poly(d,[R(-.55,-.15),R(.55,-.15),R(.55,-.38),R(-.55,-.38)],(60,64,78,255),(20,22,26,255),.03)
    for i in range(4): poly(d,[R(-.5+.27*i,-.15),R(-.4+.27*i,-.15),R(-.34+.27*i,-.38),R(-.44+.27*i,-.38)],W)
    return im
def f_hole(t):
    im,d=layer(); ell(d,0,.1,.55,.25,(150,100,60,255),BRD,.03); ell(d,0,.12,.45,.19,(45,32,25,255))
    for x,y in((-.5,.3),(.45,.35),(-.2,.38)): ell(d,x,y,.04,.025,BRD)
    ell(d,.6,0,.08,.05,GN2); return xform(im,1+.03*sg(t))
def f_moneywing(t):
    im,d=layer()
    for s in(-1,1): l,e=layer(); ell(e,0,0,.28,.12,W,GR,.02); im.alpha_composite(xform(l,1,s*(25+20*sg(t)),s*.6,-.25))
    d=ImageDraw.Draw(im); rr(d,-.4,-.15,.4,.3,.04,(120,200,130,255),(60,140,80,255),.03); ell(d,0,.08,.14,.14,(150,220,160,255),(60,140,80,255),.02); txt(d,"$",0,.09,60,(40,110,60,255)); return im
def f_cabinet(t):
    im,d=layer(); rr(d,-.4,-.6,.4,.6,.04,GR,GRD,.03)
    for i in range(3): rr(d,-.34,-.5+.38*i,.34,-.15+.38*i,.02,(190,198,210,255),GRD,.02); rr(d,-.1,-.36+.38*i,.1,-.3+.38*i,.02,GRD)
    return xform(im,1,0,0,-.02*abs(sg(t)))
def f_point(t):
    im,d=layer(); _h_point(d,t); return xform(im,1,0,0,-.03*abs(sg(t)))
def f_handw(fn,rot=4):
    def f(t):
        im,d=layer(); fn(d,t); return xform(im,1,rot*sg(t),0,-.02*abs(sg(2*t)))
    return f
# --- perbaikan tangan & bintang ---
def _finger_hand(d,x0,x1,top,bot,n=4,col=SK):
    rr(d,x0,top,x1,bot,.1,col,SKD,.02)
    for i in range(1,n): x=x0+(x1-x0)*i/n; thick_line(d,[(x,top+.02),(x,top+.2)],.02,SKD)
def _h_handshake(d,t):
    s=.04*sg(2*t); rr(d,-.74,-.28+s,-.5,.28+s,.04,BL); rr(d,.5,-.28+s,.74,.28+s,.04,(60,64,90,255))
    rr(d,-.5,-.18+s,.12,.2+s,.12,SK,SKD,.02); rr(d,-.12,-.22+s,.5,.16+s,.12,(255,222,120,255),SKD,.02)
    for i in range(4): ell(d,-.05+.1*i,-.2+s,.055,.07,(255,222,120,255),SKD,.015)
    ell(d,-.38,-.12+s,.09,.07,SK,SKD,.015)
def f_pray(t):
    im,d=layer(); rr(d,-.4,.55,.4,.72,.03,BL); s=.02*sg(2*t)
    for sgn,col in ((-1,SK),(1,(255,222,120,255))):
        l,e=layer(); _finger_hand(e,-.14,.14,-.62,.45,3,col); im.alpha_composite(xform(l,1,sgn*9,sgn*.13,s))
    return xform(im,1,3*sg(t))
def f_flex(t):
    im,d=layer(); b=.25+.03*sg(2*t); rr(d,-.68,.12,.2,.52,.2,SK,SKD,.03); rr(d,-.12,-.48,.3,.42,.18,SK,SKD,.03); ell(d,-.22,.0,b,.22,SK,SKD,.03); ell(d,.1,-.52,.26,.22,SK,SKD,.03)
    for i in range(3): thick_line(d,[(.0+.1*i,-.62),(.0+.1*i,-.5)],.02,SKD)
    rr(d,-.75,.15,-.58,.5,.04,BL); return xform(im,1,3*sg(t))
def f_dstar(t):
    im,d=layer(); poly(d,[(0,-.62),(.54,.31),(-.54,.31)],BL,BLD,.03); poly(d,[(0,.62),(.54,-.31),(-.54,-.31)],(120,135,255,255),BLD,.03); ell(d,0,0,.07,.07,W); return xform(im,1+.05*sg(t),60*t)

# ===== gelombang 7 (terakhir) =====
def puffs(d,x,y,t,n=3,col=(215,220,230,255)):
    for k in range(n):
        f=(t+k/n)%1
        if f<.9: r=.05+.07*f; ell(d,x+.06*math.sin(6*f+k),y-.55*f,r,r,col)
def spokes(d,x,y,r,deg,n=4,col=GR,w=.02):
    for k in range(n): a=math.radians(deg+k*360/n); thick_line(d,[(x-r*math.cos(a),y-r*math.sin(a)),(x+r*math.cos(a),y+r*math.sin(a))],w,col)
def f_frame(t):
    im,d=layer(); rr(d,-.55,-.55,.55,.55,.04,(190,140,50,255),(130,90,20,255),.04); rr(d,-.42,-.42,.42,.42,.02,(135,200,250,255)); ell(d,.2,-.2,.1,.1,(255,214,0,255)); poly(d,[(-.42,.42),(-.42,.1),(-.1,-.05),(.15,.2),(.42,0),(.42,.42)],(70,170,90,255)); star4(d,-.25,-.28,.12*twinkle(t),W); return xform(im,1,4*sg(t))
def f_factory(t):
    im,d=layer(); rr(d,-.6,0,.6,.55,0,(150,155,170,255),GRD,.03)
    for i in range(3): poly(d,[(-.6+.4*i,0),(-.6+.4*i,-.25),(-.2+.4*i,0)],(200,70,60,255),(140,40,35,255),.02)
    rr(d,.32,-.55,.5,0,0,(120,125,140,255),GRD,.03); puffs(d,.41,-.55,t); wins(d,-.5,.12,4,2,.28,.2,.15,.12,t); return im
def f_laptop(t):
    im,d=layer(); rr(d,-.5,-.5,.5,.2,.05,(60,64,78,255),(40,42,55,255),.03); rr(d,-.43,-.43,.43,.13,.02,(60,130,200,255)); poly(d,[(-.6,.25),(.6,.25),(.72,.45),(-.72,.45)],GR,GRD,.03)
    for k in range(3): thick_line(d,[(-.33,-.32+.14*k),(-.33+.5*((t*3+k*.4)%1),-.32+.14*k)],.04,W)
    return im
def f_hotel(t):
    im,d=layer(); rr(d,-.45,-.62,.45,.6,0,(255,190,120,255),(190,130,70,255),.03); rr(d,-.28,-.55,.28,-.25,.04,RE,RED_,.02); txt(d,"H",0,-.4,85,W); wins(d,-.33,-.12,3,3,.25,.2,.14,.12,t); rr(d,-.08,.38,.08,.6,0,BRD); return im
def f_hospital(t):
    im,d=layer(); c=RE if sg(2*t)>0 else (255,150,150,255); rr(d,-.55,-.5,.55,.6,0,W,GR,.03); rr(d,-.1,-.4,.1,-.0,.01,c); rr(d,-.2,-.3,.2,-.1,.01,c); wins(d,-.45,.12,3,2,.35,.2,.18,.12,t,(190,225,255,255),(150,170,200,255)); rr(d,-.08,.4,.08,.6,0,(120,130,150,255)); return im
def f_ship(t):
    im,d=layer(); poly(d,[(-.65,.1),(.65,.1),(.45,.4),(-.45,.4)],(40,70,150,255),(25,45,100,255),.03); rr(d,-.45,-.15,.45,.1,0,W,GR,.02); rr(d,-.28,-.35,.28,-.15,0,W,GR,.02)
    for x in(-.12,.08): rr(d,x,-.58,x+.1,-.35,0,RE)
    for i in range(5): ell(d,-.5+.25*i,-.2,.025,.025,(88,150,246,255))
    im=xform(im,1,3*sg(t),0,.03*sg(t)); d=ImageDraw.Draw(im); thick_line(d,[(-.7+.05*i,.5+.04*math.sin(2*math.pi*t+i)) for i in range(29)],.04,(120,190,250,255)); return im
def f_train(t):
    im,d=layer(); rr(d,-.1,-.15,.6,.3,.1,(45,48,60,255)); rr(d,-.6,-.45,-.15,.35,.03,RE,RED_,.03); rr(d,-.55,-.38,-.2,-.15,.01,(190,225,255,255)); rr(d,.4,-.42,.55,-.12,0,(45,48,60,255)); puffs(d,.47,-.42,t); poly(d,[(.6,.3),(.72,.45),(.55,.45)],GRD)
    for x,r in((-.4,.2),(.1,.17),(.4,.17)): ell(d,x,.4,r,r,(60,64,78,255),GRD,.02); spokes(d,x,.4,r*.85,90*t,4,GR,.02)
    return xform(im,1,0,0,-.01*sg(4*t))
def f_mountain(t):
    im,d=layer(); poly(d,[(-.65,.45),(-.15,-.45),(.35,.45)],(110,125,160,255)); poly(d,[(-.15,-.45),(-.3,-.15),(-.2,-.2),(-.12,-.1),(0,-.2),(.05,-.15)],W)
    poly(d,[(-.2,.45),(.3,-.25),(.7,.45)],(80,100,140,255)); poly(d,[(.3,-.25),(.2,-.05),(.28,-.1),(.34,0),(.42,-.08),(.45,-.08)],W); ell(d,.5,-.5,.1,.1,(255,214,0,255))
    cx=-.8+1.6*t; ell(d,cx,-.3,.18,.08,W); ell(d,cx+.12,-.34,.12,.07,W); return im
def f_slot(t):
    im,d=layer(); rr(d,-.5,-.6,.5,.6,.08,RE,RED_,.03); rr(d,-.4,-.25,.4,.2,.03,W,GR,.03); cols=[RE,(255,214,0,255),(46,204,113,255),BL]
    for i in range(3): ell(d,-.25+.25*i,-.03,.09,.09,cols[int(t*8+i*2)%4])
    ell(d,0,-.45,.08,.08,(255,214,0,255) if sg(3*t)>0 else (150,120,0,255)); pull=.25*ease_io(clamp(t/.3)) if t<.5 else .25*(1-ease_io(clamp((t-.5)/.3)))
    thick_line(d,[(.5,-.1),(.68,-.1+pull*.2),(.68,-.4+pull)],.05,GR); ell(d,.68,-.42+pull,.08,.08,RE); return im
def f_micro(t):
    l,e=layer(); rr(e,-.1,-.6,.1,.05,.03,GR,GRD,.03); rr(e,-.06,.05,.06,.2,.01,GRD); ell(e,0,-.6,.12,.05,(60,64,78,255)); im=xform(l,1,-25)
    d=ImageDraw.Draw(im); d.arc([P(-.2,-.2),P(.6,.55)],270,450,fill=GRD,width=int(.1*K)); rr(d,-.35,.1,.15,.17,.02,GRD); rr(d,-.5,.52,.5,.62,.03,GR,GRD,.02); star4(d,-.3,-.45,.14*twinkle(t),W); return im
def f_dna(t):
    im,d=layer(); ph=2*math.pi*t
    for i in range(0,25):
        y=-.6+1.2*i/24; x=.26*math.sin(4*math.pi*(i/24)+ph); x2=-x
        if i%2==0: thick_line(d,[(x,y),(x2,y)],.025,(190,195,210,255))
    for sgn,c in((1,BL),(-1,(231,100,140,255))): thick_line(d,[(sgn*.26*math.sin(4*math.pi*(i/24)+ph),-.6+1.2*i/24) for i in range(25)],.07,c)
    return im
def f_moviecam(t):
    im,d=layer(); rr(d,-.5,-.05,.3,.45,.05,(60,64,78,255),(35,38,50,255),.03); poly(d,[(.3,.05),(.62,-.05),(.62,.45),(.3,.35)],GR,GRD,.03)
    for x,r in((-.28,.24),(.08,.2)): ell(d,x,-.3,r,r,(80,85,100,255),(35,38,50,255),.03); spokes(d,x,-.3,r*.8,120*t,3,GR,.025); ell(d,x,-.3,.04,.04,GR)
    ell(d,-.3,.2,.06,.06,RE if sg(2*t)>0 else (120,30,30,255)); return im
def f_pen(t):
    pts=[(-.55,.52),(-.4,.38),(-.28,.55),(-.12,.38),(0,.55),(.15,.4),(.3,.55),(.45,.4)]; p=ease_io(clamp(t/.8)); q=partial(pts,max(p,.001))
    l,e=layer(); rr(e,-.07,-.55,.07,.3,.04,BL,BLD,.02); poly(e,[(-.07,.3),(.07,.3),(0,.52)],GRD); rr(e,.07,-.5,.1,-.1,.01,GR)
    th=math.radians(35); tx,ty=.52*math.sin(th),.52*math.cos(th); pen=xform(l,1,35,q[-1][0]-tx,q[-1][1]-ty)
    im,d=layer(); thick_line(d,q,.04,BLD); im.alpha_composite(pen); return im
def f_mantel(t):
    im,d=layer(); rr(d,-.35,-.62,.35,.58,.2,WD,BRD,.03); circle_=None; ell(d,0,-.28,.23,.23,W,BRD,.03)
    for k in range(4): a=math.radians(k*90); ell(d,.17*math.sin(a),-.28-.17*math.cos(a),.02,.02,GRD)
    a=2*math.pi*t; thick_line(d,[(0,-.28),(.14*math.sin(a),-.28-.14*math.cos(a))],.03,DK); thick_line(d,[(0,-.28),(.09*math.sin(2.5),-.28-.09*math.cos(2.5))],.04,DK)
    rr(d,-.2,.0,.2,.45,.05,(60,45,35,255)); px=.1*math.sin(2*math.pi*t); thick_line(d,[(0,.02),(px,.35)],.02,(255,193,7,255)); ell(d,px,.35,.06,.06,(255,193,7,255)); return im
def f_flash(t):
    l,e=layer(); on=sg(2*t)>-.3; 
    if on: poly(e,[(-.22,-.3),(.22,-.3),(.55,-.8),(-.55,-.8)],(255,245,170,255))
    rr(e,-.12,-.1,.12,.6,.05,(60,64,78,255),(35,38,50,255),.02); poly(e,[(-.12,-.1),(.12,-.1),(.22,-.3),(-.22,-.3)],GR,GRD,.02); rr(e,-.05,.15,.05,.3,.02,RE); return xform(l,1,-25,0,.15)
def f_pager(t):
    im,d=layer(); rr(d,-.4,-.4,.4,.4,.08,(60,64,78,255),(35,38,50,255),.03); rr(d,-.3,-.3,.3,0,.03,(150,220,150,255))
    for k in range(2): thick_line(d,[(-.22,-.22+.1*k),(-.22+.4*((t*2+k*.3)%1),-.22+.1*k)],.04,(40,90,40,255))
    for x in(-.2,0,.2): ell(d,x,.22,.05,.05,GR)
    for k in range(2):
        f2=(t+k/2)%1
        if f2<.7: r=.1+.25*f2; d.arc([P(.4-r,-.4-r),P(.4+r,-.4+r)],270,360,fill=BL,width=int(.04*K))
    return im
def f_cap(t):
    im,d=layer(); c=(60,100,200,255); d.pieslice([P(-.45,-.5),P(.45,.4)],180,360,fill=c,outline=dk_(c),width=int(.03*K)); ell(d,.3,-.03,.4,.09,dk_(c),dk_(c,.5),.02); ell(d,0,-.5,.05,.05,dk_(c)); thick_line(d,[(0,-.5),(0,-.05)],.02,dk_(c)); thick_line(d,[(-.25,-.4),(-.2,-.05)],.02,dk_(c)); return xform(im,1,-8+4*sg(t))
def f_loveletter(t):
    im,d=layer(); rr(d,-.55,-.2,.55,.4,.06,(250,250,252,255),(230,100,140,255),.04); thick_line(d,[(-.55,-.2),(0,.15),(.55,-.2)],.04,(230,100,140,255)); poly(d,hpts(.22,0,0,.12),RE,RED_,.01)
    for k in range(3):
        f2=(t+k/3)%1
        if f2<.9: poly(d,hpts(.12+.04*f2,0,-.3+.3*k+.05*math.sin(6*f2),-.3-.4*f2),(255,110,150,255))
    return im
def f_gloves(t):
    im,d=layer()
    for sgn,col in((-1,(255,160,50,255)),(1,(255,190,90,255))):
        l,e=layer(); _finger_hand(e,-.2,.2,-.45,.3,4,col); rr(e,-.24,.3,.24,.52,.04,(88,101,242,255)); rr(e,-.32,-.1,-.18,.15,.07,col,SKD,.02) if False else None; im.alpha_composite(xform(l,1,sgn*12+4*sg(t),sgn*.3,0))
    return im
def f_receipt(t):
    im,d=layer(); pts=[(-.35,-.6),(.35,-.6),(.35,.55)]
    for i in range(7): pts.append((.35-.7*(i+1)/7,.55+(.08 if i%2==0 else 0)))
    poly(d,pts,W,GR,.03)
    for k in range(5): y=-.45+.17*k+.17*(t%1)*0; thick_line(d,[(-.25,y),(-.25+.35*(1 if k%2 else .7),y)],.04,(190,195,205,255))
    txt(d,"$",.18,.28,55,(60,130,70,255)); return xform(im,1,3*sg(t))
def f_cig(t):
    l,e=layer(); rr(e,-.5,-.06,.3,.06,.02,W,GR,.02); rr(e,.3,-.06,.55,.06,.02,(255,150,50,255)); ell(e,-.5,0,.06,.07,RE if sg(2*t)>-.2 else (255,150,80,255)); im=xform(l,1,20); d=ImageDraw.Draw(im)
    for k in range(3):
        f2=(t+k/3)%1
        if f2<.85: thick_line(d,[(-.45+.04*math.sin(8*(f2+i*.2)),-.2-.12*i-.2*f2) for i in range(4)],.03,(205,210,222,255))
    return im
def f_window(t):
    im,d=layer(); rr(d,-.5,-.6,.5,.6,.03,W,GR,.04); 
    for x0,y0 in((-.42,-.52),(.02,-.52),(-.42,.02),(.02,.02)): rr(d,x0,y0,x0+.4,y0+.5,0,(160,215,250,255))
    s=.03*sg(t); poly(d,[(-.5,-.6),(-.25+s,-.6),(-.3+s,.5),(-.5,.5)],(231,100,140,255)); poly(d,[(.5,-.6),(.25-s,-.6),(.3-s,.5),(.5,.5)],(231,100,140,255)); star4(d,.15,-.3,.14*twinkle(t),W); return im
def f_umbrella(t):
    im,d=layer(); poly(d,[(0,-.7),(.18,-.2),(.12,.35),(-.12,.35),(-.18,-.2)],(88,101,242,255),BLD,.03)
    for x in(-.06,.06): thick_line(d,[(x*.3,-.55),(x,.3)],.015,BLD)
    thick_line(d,[(0,.35),(0,.6)],.04,BR); d.arc([P(0,.5),P(.2,.72)],90,270,fill=BR,width=int(.04*K)); return xform(im,1,20+8*sg(t))
def f_tridown(t):
    im,d=layer(); poly(d,[(-.5,-.4),(.5,-.4),(0,.5)],RE,RED_,.04); poly(d,[(-.35,-.32),(-.1,-.32),(-.2,-.1)],(255,140,140,255)); return xform(im,1,0,0,.05*abs(sg(2*t)))
def f_keyboard(t):
    im,d=layer(); rr(d,-.65,-.35,.65,.35,.06,GR,GRD,.03); act=int(t*15)%15
    for r in range(3):
        for c in range(5): rr(d,-.55+.22*c,-.25+.2*r,-.37+.22*c,-.1+.2*r,.02,BL if r*5+c==act else (225,230,240,255),GRD,.01)
    rr(d,-.4,.18,.4,.28,.02,(225,230,240,255)) if False else None; return im
def f_cupstraw(t):
    im,d=layer(); thick_line(d,[(0,-.28),(.05,-.6),(.18,-.72)],.05,(88,201,150,255)); poly(d,[(-.28,-.2),(.28,-.2),(.2,.55),(-.2,.55)],RE,RED_,.03); poly(d,[(-.25,0),(.25,0),(.23,.2),(-.23,.2)],W); rr(d,-.32,-.28,.32,-.18,.03,(240,240,245,255),GR,.02)
    for k in range(3):
        f2=(t+k/3)%1; ell(d,-.1+.1*k,.4-.55*f2,.03,.03,(255,200,200,255))
    return xform(im,1,3*sg(t))
def f_rice(t):
    im,d=layer(); d.pieslice([P(-.55,-.35),P(.55,.75)],0,180,fill=(88,150,246,255),outline=(60,110,200,255),width=int(.03*K)); d.pieslice([P(-.5,-.15),P(.5,.25)],180,360,fill=W,outline=GR,width=int(.02*K)); rr(d,-.55,.17,.55,.23,.03,(70,120,210,255))
    for x,y in((-.2,-.05),(0,-.1),(.2,-.03),(.1,.05)): ell(d,x,y,.02,.015,GR)
    puffs(d,0,-.2,t,2); return d and im
def f_bread(t):
    im,d=layer(); c=(230,170,80,255); rr(d,-.5,-.05,.5,.5,.1,c,dk_(c),.03); ell(d,0,-.08,.5,.3,c,dk_(c),.03); rr(d,-.46,-.06,.46,.08,0,c)
    for x in(-.25,0,.25): thick_line(d,[(x-.05,-.3),(x+.05,-.15)],.04,(255,215,140,255))
    return xform(im,1,3*sg(t),0,-.03*abs(sg(t)))
def f_milk(t):
    im,d=layer(); poly(d,[(-.3,-.55),(.3,-.55),(.24,.55),(-.24,.55)],(225,240,252,255),(130,170,200,255),.03); y=-.05+.025*sg(t); w=.3-.06*((y+.55)/1.1)
    poly(d,[(-w,y),(w,y),(.23,.53),(-.23,.53)],W); thick_line(d,[(-w,y),(-w*.5,y-.02),(0,y+.02),(w*.5,y-.02),(w,y)],.03,(235,240,250,255)); return im
def f_noodle(t):
    im,d=layer(); thick_line(d,[(.1,-.7),(.35,-.2)],.03,BR); thick_line(d,[(.2,-.7),(.42,-.2)],.03,BR)
    d.pieslice([P(-.55,-.35),P(.55,.75)],0,180,fill=(231,100,100,255),outline=RED_,width=int(.03*K))
    for k in range(4): thick_line(d,[(-.4+.2*k,-.05),(-.3+.2*k,.0),(-.2+.2*k,-.05)],.04,(255,225,120,255))
    ell(d,-.2,-.08,.08,.06,(255,150,170,255)); puffs(d,-.1,-.2,t,2); return im
def f_pot(t):
    im,d=layer(); rr(d,-.5,-.05,.5,.5,.1,GR,GRD,.03); rr(d,-.62,.05,-.5,.15,.03,GRD); rr(d,.5,.05,.62,.15,.03,GRD); ell(d,0,-.05,.5,.12,(210,100,50,255),GRD,.03)
    for k in range(3): f2=(t+k/3)%1; ell(d,-.25+.25*k,-.05-.04*f2,.04*(1-f2*.3),.03,(255,160,90,255))
    puffs(d,0,-.2,t,3); return im
def f_curry(t):
    im,d=layer(); ell(d,0,.3,.65,.2,W,GR,.03); ell(d,-.2,.12,.3,.2,W,GR,.02); ell(d,.25,.15,.3,.2,(190,120,40,255),(140,80,20,255),.02)
    for x,y in((.15,.1),(.35,.18),(.28,.05)): ell(d,x,y,.04,.04,(240,180,90,255))
    puffs(d,0,-.1,t,2); return im
def f_meat(t):
    im,d=layer(); ell(d,0,0,.58,.42,(255,190,190,255),(190,90,100,255),.03); ell(d,0,0,.48,.33,(220,80,95,255)); ell(d,.2,.02,.1,.08,W,GR,.02)
    for pts in([(-.3,-.1),(-.1,-.15)],[(-.2,.1),(0,.05)],[(-.4,.0),(-.25,-.02)]): thick_line(d,pts,.025,(255,200,200,255))
    star4(d,-.4,-.35,.12*twinkle(t),(255,230,150,255)); return xform(im,1,-10+4*sg(t))
def f_choco(t):
    im,d=layer(); rr(d,-.4,-.5,.4,.6,.03,(190,198,210,255),GRD,.03); rr(d,-.35,-.55,.35,.2,.03,(120,70,40,255),(80,45,25,255),.03)
    for i in range(1,3): thick_line(d,[(-.35+.233*i,-.55),(-.35+.233*i,.2)],.02,(80,45,25,255))
    for j in range(1,4): thick_line(d,[(-.35,-.55+.19*j),(.35,-.55+.19*j)],.02,(80,45,25,255))
    star4(d,.3,-.5,.14*twinkle(t),W); return xform(im,1,4*sg(t))
def f_teddy(t):
    im,d=layer(); br=(170,115,70,255); ell(d,0,.4,.38,.3,br,dk_(br),.03)
    for s in(-1,1): ell(d,s*.32,-.4,.14,.14,br,dk_(br)); ell(d,s*.32,-.4,.07,.07,(220,180,140,255))
    ell(d,0,-.12,.42,.4,br,dk_(br)); ell(d,0,.0,.17,.13,(230,200,160,255)); ell(d,0,-.03,.05,.04,DK); _eyes(d,t,-.2,.17,.05); poly(d,[(-.2,.22),(0,.2),(-.2,.3)],RE); poly(d,[(.2,.22),(0,.2),(.2,.3)],RE); ell(d,0,.22,.05,.05,RED_); return xform(im,1,4*sg(t))
def f_toolbox(t):
    im,d=layer(); thick_line(d,[(-.3,-.1),(-.35,-.4)],.06,GR); thick_line(d,[(.3,-.1),(.5,-.5)],.04,(255,193,7,255)); rr(d,.44,-.6,.56,-.45,.02,RE)
    d.arc([P(-.25,-.5),P(.25,.0)],180,360,fill=GRD,width=int(.06*K)); rr(d,-.6,-.1,.6,.5,.06,RE,RED_,.03); thick_line(d,[(-.6,.15),(.6,.15)],.025,RED_); rr(d,-.08,.1,.08,.22,.02,(255,193,7,255)); return xform(im,1,3*sg(t),0,-.02*abs(sg(t)))
def f_antbars(t):
    im,d=layer(); n=1+int(t*5)%4
    for i in range(4): rr(d,-.5+.27*i,.5-.25*(i+1),-.3+.27*i,.5,.03,(46,204,113,255) if i<n else (190,195,205,255))
    return im
def f_basket(t):
    im,d=layer(); d.arc([P(-.45,-.55),P(.45,.35)],180,360,fill=(160,110,50,255),width=int(.07*K)); d.pieslice([P(-.55,-.35),P(.55,.75)],0,180,fill=(205,150,80,255),outline=(160,110,50,255),width=int(.03*K)); rr(d,-.58,.1,.58,.2,.04,(160,110,50,255))
    for i in range(5): thick_line(d,[(-.4+.2*i,.2),(-.3+.15*i,.6)],.02,(160,110,50,255))
    return xform(im,1,3*sg(t))
def f_bridge(t):
    im,d=layer(); rr(d,-.65,-.6,.65,.6,.1,(30,35,75,255)); ell(d,.35,-.35,.12,.12,(255,240,170,255)); ell(d,.4,-.4,.1,.1,(30,35,75,255))
    for x,y,ph in((-.4,-.4,0),(-.1,-.5,.3),(.1,-.2,.6)): star4(d,x,y,.07+.05*twinkle(t,ph),W)
    rr(d,-.65,.15,.65,.25,0,(150,160,200,255)); 
    for x in(-.35,.35): rr(d,x-.05,-.2,x+.05,.25,0,(150,160,200,255)); thick_line(d,[(x,-.2),(x-.3,.15)],.02,(150,160,200,255)); thick_line(d,[(x,-.2),(x+.3,.15)],.02,(150,160,200,255))
    for i in range(7): ell(d,-.55+.18*i,.12,.025,.025,(255,214,0,255) if (i+int(t*4))%2 else (150,120,40,255))
    return im
def f_mosque(t):
    im,d=layer(); c=(235,225,200,255); so=(170,155,120,255)
    for x in(-.5,.5): rr(d,x-.07,-.3,x+.07,.55,0,c,so,.03); poly(d,[(x-.1,-.3),(x,-.6),(x+.1,-.3)],(70,170,150,255),so,.02)
    rr(d,-.35,.05,.35,.55,0,c,so,.03); d.pieslice([P(-.35,-.35),P(.35,.35)],180,360,fill=(70,170,150,255),outline=so,width=int(.03*K)); thick_line(d,[(0,-.35),(0,-.5)],.025,(255,193,7,255)); ell(d,0,-.55,.06,.06,None,(255,193,7,255),.025)
    d.pieslice([P(-.1,.15),P(.1,.55)],180,360,fill=(60,45,35,255)); rr(d,-.1,.35,.1,.55,0,(60,45,35,255)); star4(d,.3,-.5,.12*twinkle(t),(255,240,150,255)); return im
def f_sailboat(t):
    im,d=layer(); thick_line(d,[(0,-.65),(0,.2)],.04,BR); poly(d,[(.04,-.6),(.5,.1),(.04,.1)],W,GR,.02); poly(d,[(-.04,-.45),(-.4,.1),(-.04,.1)],(255,230,200,255),GR,.02); poly(d,[(-.55,.15),(.55,.15),(.4,.4),(-.4,.4)],RE,RED_,.03)
    im=xform(im,1,4*sg(t),0,.03*sg(t)); d=ImageDraw.Draw(im); thick_line(d,[(-.7+.05*i,.5+.04*math.sin(2*math.pi*t+i)) for i in range(29)],.04,(120,190,250,255)); return im
def f_tokyo(t):
    im,d=layer(); poly(d,[(0,-.75),(.07,-.4),(.3,.1),(.4,.6),(-.4,.6),(-.3,.1),(-.07,-.4)],(231,70,50,255),(170,40,30,255),.03); rr(d,-.2,-.1,.2,0,0,W); rr(d,-.28,.2,.28,.28,0,W); thick_line(d,[(0,-.75),(0,-.95)],.025,GRD)
    ell(d,0,-.95,.03,.03,RE if sg(2*t)>0 else (120,30,30,255)); thick_line(d,[(-.1,.6),(0,.3),(.1,.6)],.02,(170,40,30,255)); return im
def f_scooter(t):
    im,d=layer(); poly(d,[(-.45,.0),(-.1,.0),(.0,.25),(.35,.25),(.35,.1),(-.45,.1)],(88,201,150,255),(40,140,100,255),.03); rr(d,-.55,-.1,-.15,.0,.03,(60,64,78,255)); thick_line(d,[(.35,.25),(.3,-.35),(.15,-.45)],.05,GR); rr(d,.05,-.5,.3,-.42,.02,GRD)
    for x in(-.4,.4): ell(d,x,.45,.16,.16,(45,48,55,255)); spokes(d,x,.45,.13,90*t,4,GR,.02)
    return xform(im,1,0,0,-.012*sg(4*t))
def f_dept(t):
    im,d=layer(); rr(d,-.6,-.4,.6,.6,0,(235,225,205,255),(170,155,120,255),.03); rr(d,-.5,-.65,.5,-.4,.04,(88,101,242,255),BLD,.03)
    for i in range(6): rr(d,-.6+.2*i,-.15,-.4+.2*i,.05,0,RE if i%2==0 else W,GR,.01)
    wins(d,-.5,.12,4,2,.28,.22,.16,.14,t,(190,225,255,255),(140,160,190,255)); rr(d,-.1,.4,.1,.6,0,BRD); return im
def f_plane(t):
    l,e=layer(); ell(e,0,0,.6,.1,W,GR,.03); poly(e,[(-.05,0),(.2,0),(.0,-.5),(-.2,-.5)],(190,200,220,255),GR,.02); poly(e,[(-.05,0),(.2,0),(.0,.5),(-.2,.5)],(190,200,220,255),GR,.02); poly(e,[(-.5,0),(-.6,-.2),(-.4,-.0)],(190,200,220,255),GR,.02); ell(e,.35,-.02,.05,.03,(88,150,246,255))
    im=xform(l,1,-30,0,.04*sg(t)); d=ImageDraw.Draw(im)
    for k in range(2): cx=.8-1.6*((t+k/2)%1); ell(d,cx,.45-.3*k,.2,.07,(225,235,250,255)); ell(d,cx+.1,.4-.3*k,.13,.06,(225,235,250,255))
    return im
def f_news(t):
    im,d=layer(); rr(d,-.55,-.45,.55,.45,.03,W,GR,.03); rr(d,-.45,-.38,.45,-.22,0,(60,64,78,255)); rr(d,-.45,-.1,-.05,.2,0,(190,195,205,255)); 
    for k in range(4): thick_line(d,[(.05,-.08+.1*k),(.45,-.08+.1*k)],.03,(190,195,205,255))
    for k in range(2): thick_line(d,[(-.45,.28+.08*k),(.45,.28+.08*k)],.03,(190,195,205,255))
    return xform(im,1,3*sg(t))
def f_radiodev(t):
    im,d=layer(); thick_line(d,[(.3,-.3),(.5,-.65)],.03,GR); rr(d,-.6,-.3,.6,.4,.08,(150,95,60,255),(100,60,35,255),.03); ell(d,-.28,.05,.22,.22,(60,45,35,255)); ell(d,-.28,.05,.14,.14,(100,80,60,255))
    rr(d,.0,-.2,.5,-.05,.02,(255,230,160,255)); thick_line(d,[(.05+.4*(.5+.5*sg(t)),-.2),(.05+.4*(.5+.5*sg(t)),-.05)],.02,RE); ell(d,.15,.2,.06,.06,GR); ell(d,.35,.2,.06,.06,GR)
    f2=t%1; ell(d,.7,-.4-.3*f2,.04,.03,BL); return im
def f_mouse3(t):
    im,d=layer(); ell(d,0,.05,.36,.55,GR,GRD,.03); on=sg(3*t)>0; rr(d,-.34,-.45,-.12,-.05,.0,(190,198,210,255) if not on else BL); rr(d,.12,-.45,.34,-.05,.0,(190,198,210,255)); rr(d,-.05,-.4,.05,-.15,.03,GRD)
    thick_line(d,[(-.34,-.05),(.34,-.05)],.02,GRD); thick_line(d,[(0,.5),(0,.7),(.2,.75)],.02,GRD); return im
def f_nazar(t):
    im,d=layer(); ripple(d,t,(60,130,220,255)); circle(d,.58,(20,60,140,255)); circle(d,.44,W); circle(d,.3,(80,170,240,255)); circle(d,.16,(20,20,35,255)); return xform(im,1+.04*sg(t))
def f_brick(t):
    im,d=layer(); c=(205,90,60,255); dc=(140,50,30,255)
    for r in range(4):
        off=.0 if r%2==0 else .25
        for i in range(-1,3):
            x0=-.5+.5*i+off; x1=x0+.5
            if x1>-.6 and x0<.6: rr(d,max(-.6,x0)+.01,-.55+.28*r,min(.6,x1)-.01,-.3+.28*r,.02,c,dc,.02)
    return xform(im,1,3*sg(t))
def f_church(t):
    im,d=layer(); rr(d,-.4,-.05,.4,.55,0,(250,245,235,255),GR,.03); poly(d,[(-.45,-.05),(0,-.4),(.45,-.05)],(150,95,70,255),(100,60,40,255),.03); rr(d,-.12,-.55,.12,-.3,0,(250,245,235,255),GR,.02); poly(d,[(-.15,-.55),(0,-.8),(.15,-.55)],(150,95,70,255)); rr(d,-.02,-.98,.02,-.78,0,(255,193,7,255)); rr(d,-.08,-.92,.08,-.88,0,(255,193,7,255))
    d.pieslice([P(-.12,.15),P(.12,.55)],180,360,fill=(100,60,40,255)); rr(d,-.12,.35,.12,.55,0,(100,60,40,255)); ell(d,0,-.42,.04,.04,(255,193,7,255)); return im
def f_mousetrap(t):
    im,d=layer(); rr(d,-.55,-.1,.55,.45,.04,WD,BRD,.03); a=-70 if t<.7 else -70*(1-clamp((t-.7)/.06)) if t<.76 else 0
    if t>.9: a=0
    ar=math.radians(a); px,py=-.4,.1; x2=px+.8*math.cos(ar); y2=py+.8*math.sin(ar); thick_line(d,[(px,py),(x2,y2)],.04,GR); poly(d,[(.35,.0),(.5,.0),(.5,.3),(.35,.3)],(255,214,0,255)); ell(d,.42,.1,.025,.025,(200,150,0,255)); return im
def f_cyclone(t):
    rl,rd=layer(); c=(120,140,190,255)
    for i,r in enumerate((.55,.42,.3,.18)): rd.arc([P(-r,-r),P(r,r)],20+40*i,250+40*i,fill=c,width=int(.09*K))
    return xform(rl,1,360*t)
def f_nib(t):
    im,d=layer(); poly(d,[(-.2,-.5),(.2,-.5),(.28,.0),(0,.55),(-.28,.0)],(45,48,60,255),(20,22,26,255),.03); thick_line(d,[(0,.15),(0,.55)],.025,GR); ell(d,0,.1,.05,.05,GR); rr(d,-.2,-.62,.2,-.48,.03,(45,48,60,255)); f2=t%1
    if f2<.8: ell(d,0,.62+.15*f2,.04,.06,(40,60,150,255))
    return im
def f_dash(t):
    im,d=layer()
    for y,ph,c in((-.3,0,(150,200,250,255)),(0,.3,(190,225,255,255)),(.3,.6,(150,200,250,255))):
        x0=-.7+1.4*((t+ph)%1)-.3; pts=[(x0+.6*i/10,y+.06*math.sin(6*(i/10))) for i in range(11)]; thick_line(d,[(max(-.7,min(.7,x)),yy) for x,yy in pts],.06,c)
    return im
def f_vest(t):
    im,d=layer(); poly(d,[(-.4,-.55),(-.15,-.55),(0,-.25),(.15,-.55),(.4,-.55),(.5,.55),(-.5,.55)],(255,140,30,255),(200,90,10,255),.03); rr(d,-.47,.0,.47,.12,0,(220,225,232,255)); rr(d,-.49,.3,.49,.42,0,(220,225,232,255)); thick_line(d,[(0,-.25),(0,.55)],.03,(200,90,10,255)); star4(d,-.3,.06,.15*twinkle(t),W); return xform(im,1,3*sg(t))
def f_latin(t):
    im,d=layer(); ripple(d,t,(255,214,0,255)); rr(d,-.12,-.65,.12,.65,.02,(255,193,7,255),(200,140,0,255),.03); rr(d,-.4,-.35,.4,-.12,.02,(255,193,7,255),(200,140,0,255),.03); rr(d,-.1,-.63,.1,.63,0,(255,193,7,255)); return xform(im,1+.03*sg(t))
def f_microbe(t):
    rl,rd=layer()
    for i in range(8): a=math.radians(i*45); thick_line(rd,[(.4*math.cos(a),.4*math.sin(a)),(.58*math.cos(a),.58*math.sin(a))],.04,(90,170,70,255)); ell(rd,.62*math.cos(a),.62*math.sin(a),.06,.06,(150,220,100,255))
    im=xform(rl,1,45*t); d=ImageDraw.Draw(im); ell(d,0,0,.42,.42,(120,200,90,255),(70,140,50,255),.03)
    for x,y,r in((-.15,-.1,.08),(.15,.1,.1),(.0,.2,.05)): ell(d,x,y,r,r,(80,150,60,255))
    ell(d,-.1,-.12,.05,.05,W); ell(d,.1,-.12,.05,.05,W); return xform(im,1+.04*sg(2*t))
def f_horse(t):
    im,d=layer(); br=(170,110,60,255); poly(d,[(-.3,-.35),(-.22,-.75),(-.08,-.4)],br,dk_(br)); poly(d,[(.3,-.35),(.22,-.75),(.08,-.4)],br,dk_(br)); rr(d,-.1,-.65,.1,.1,.05,(70,45,25,255)); ell(d,0,.05,.36,.52,br,dk_(br),.03); ell(d,0,.4,.26,.18,(230,200,160,255),dk_(br),.02)
    ell(d,-.09,.4,.03,.04,DK); ell(d,.09,.4,.03,.04,DK); _eyes(d,t,-.1,.2,.06); return xform(im,1,4*sg(t))
def f_blackflag(t):
    im,d=layer(); rr(d,-.56,-.68,-.48,.66,.02,GR,GRD,.02); dy=lambda x:.07*math.sin(2*math.pi*t-5*x)
    for i in range(4):
        x0=-.48+i*.25; x1=x0+.25; poly(d,[(x0,-.6+dy(x0)),(x1,-.6+dy(x1)),(x1,.0+dy(x1)),(x0,.0+dy(x0))],(35,38,48,255))
    return im
def f_dove(t):
    im,d=layer(); ell(d,0,.1,.45,.25,W,GR,.03); ell(d,.4,-.1,.17,.17,W,GR,.03); poly(d,[(.55,-.1),(.72,-.05),(.55,0)],(255,160,30,255)); ell(d,.45,-.13,.03,.03,DK); poly(d,[(-.4,.1),(-.65,.0),(-.5,.25)],W,GR,.02)
    a=25*sg(t); l,e=layer(); poly(e,[(0,.05),(-.2,-.5),(.15,-.45),(.3,.05)],W,GR,.03); im.alpha_composite(xform(l,1,a,0,0)); thick_line(d,[(.7,-.05),(.5,.35),(.2,.45)],.03,GN2); ell(d,.45,.38,.07,.04,GN2); return xform(im,1,0,0,-.03*sg(t))
def f_bio(t):
    rl,rd=layer()
    for k in range(3):
        a=math.radians(k*120); ell(rd,.26*math.sin(a),-.26*math.cos(a),.24,.24,None,(60,40,20,255),.1)
    im=xform(rl,1,120*t); d=ImageDraw.Draw(im); ell(d,0,0,.07,.07,(60,40,20,255)); return im
def f_joy(t):
    im,d=layer(); rr(d,-.55,.25,.55,.55,.06,GR,GRD,.03); sx=.22*sg(t); thick_line(d,[(0,.25),(sx,-.3)],.08,GRD); ell(d,sx,-.38,.17,.17,RE,RED_,.03); ell(d,sx-.06,-.44,.05,.04,(255,150,150,255)); ell(d,-.38,.4,.06,.06,RE); ell(d,.38,.4,.06,.06,BL); return im
def f_tag(t):
    im,d=layer(); poly(d,[(-.5,0),(-.25,-.4),(.5,-.4),(.5,.4),(-.25,.4)],(255,230,150,255),(200,160,60,255),.03); ell(d,-.25,0,.07,.07,(0,0,0,0)); thick_line(d,[(-.25,0),(-.55,-.2),(-.7,-.1)],.02,GRD)
    for k in range(3): thick_line(d,[(-.05,-.2+.2*k),(.35,-.2+.2*k)],.03,(190,150,60,255))
    return xform(im,1,-20+10*sg(t))
def f_pine(t):
    im,d=layer(); y=(255,200,40,255); ell(d,0,.15,.35,.45,y,(200,140,10,255),.03)
    for i in range(-3,4): thick_line(d,[(.1*i-.2,.15-.4),(.1*i+.25,.15+.4)],.015,(200,140,10,255)); thick_line(d,[(.1*i+.2,.15-.4),(.1*i-.25,.15+.4)],.015,(200,140,10,255))
    for a in (-30,-12,0,12,30): thick_line(d,[(0,-.25),(.4*math.sin(math.radians(a)),-.25-.45*math.cos(math.radians(a)))],.09,(60,170,80,255))
    return xform(im,1,4*sg(t))
def f_mango(t):
    l,e=layer(); ell(e,0,0,.42,.52,(255,170,50,255),(220,110,20,255),.03); ell(e,.15,.1,.2,.3,(240,90,60,255)); ell(e,-.18,-.2,.06,.14,(255,230,150,255)); im=xform(l,1,30+4*sg(t)); d=ImageDraw.Draw(im); poly(d,[(.1,-.5),(.45,-.6),(.3,-.35)],(60,170,80,255)); return im
def f_peach(t):
    im,d=layer(); ell(d,0,.05,.48,.46,(255,170,140,255),(220,110,90,255),.03); ell(d,.15,.1,.25,.3,(255,130,120,255)); thick_line(d,[(0,-.35),(.05,.1),(0,.4)],.02,(220,110,90,255)); ell(d,-.2,-.1,.06,.12,(255,225,210,255)); poly(d,[(0,-.4),(.4,-.55),(.25,-.3)],(60,170,80,255)); return xform(im,1,5*sg(t))
def f_corn(t):
    l,e=layer(); ell(e,0,0,.26,.58,(255,214,60,255),(220,170,20,255),.03)
    for i in range(5):
        for j in range(3): ell(e,-.12+.12*j,-.4+.17*i,.04,.05,(255,240,150,255))
    poly(e,[(-.05,.1),(-.35,.55),(.0,.5)],(70,170,80,255),(40,120,50,255),.02); poly(e,[(.05,.1),(.35,.55),(0,.5)],(90,190,100,255),(40,120,50,255),.02); return xform(l,1,25+5*sg(t))
def f_turtle(t):
    im,d=layer(); g=(70,170,80,255); gd=(40,120,50,255); w=.04*sg(t)
    for x,y in((-.4,-.3+w),(.4,-.3-w),(-.4,.3-w),(.4,.3+w)): ell(d,x,y,.14,.1,(120,200,110,255),gd,.02)
    ell(d,0,-.55,.14,.16,(120,200,110,255),gd,.02); ell(d,-.05,-.58,.02,.02,DK); ell(d,.05,-.58,.02,.02,DK); ell(d,0,0,.42,.45,g,gd,.03)
    for p in([(0,-.25),(.18,-.1),(.12,.12),(-.12,.12),(-.18,-.1)],): poly(d,p,(110,200,110,255),gd,.02)
    for a in range(5): thick_line(d,[p for p in [(0,0)]]+[(.4*math.sin(math.radians(a*72)),-.4*math.cos(math.radians(a*72)))],.015,gd) if False else None
    return xform(im,1,0,0,.0)
def f_octopus(t):
    im,d=layer(); p=(170,90,200,255); pd=(120,55,150,255)
    for i in range(6):
        x=-.4+.16*i; thick_line(d,[(x,.15)]+[(x+.05*math.sin(2*math.pi*t-j*1.2+i),.15+.14*j) for j in range(1,5)],.09,p)
    ell(d,0,-.15,.45,.42,p,pd,.03); _eyes(d,t,-.15,.18,.08,W); [ell(d,x,-.14,.035,.045,DK) for x in(-.18,.18)]; d.arc([P(-.1,-.05),P(.1,.12)],20,160,fill=pd,width=int(.03*K)); return xform(im,1,0,0,-.03*sg(t))
def f_bee(t):
    im,d=layer(); w=.6+.4*abs(math.cos(2*math.pi*t*2)); 
    for s in(-1,1): ell(d,s*.15,-.4,.12*w,.25,(220,240,255,255),(150,190,230,255),.02)
    ell(d,0,.05,.4,.32,(255,200,40,255),(200,140,10,255),.03)
    for x in(-.12,.1): thick_line(d,[(x,-.22),(x,.3)],.1,(45,40,35,255))
    ell(d,-.4,.05,.14,.14,(255,200,40,255),(200,140,10,255),.03); ell(d,-.44,.02,.03,.03,DK); poly(d,[(.4,.05),(.6,.08),(.4,.15)],(60,50,40,255)); return xform(im,1,0,0,-.04*sg(t))
def f_sunflower(t):
    rl,rd=layer()
    for i in range(12): a=math.radians(i*30); thick_line(rd,[(.3*math.cos(a),.3*math.sin(a)),(.58*math.cos(a),.58*math.sin(a))],.15,(255,214,0,255))
    im=xform(rl,1,30*t); d=ImageDraw.Draw(im); ell(d,0,0,.3,.3,(110,70,30,255),(70,40,15,255),.03)
    for i in range(6): a=math.radians(i*60); ell(d,.15*math.cos(a),.15*math.sin(a),.025,.025,(160,110,50,255))
    return im
def f_cactus(t):
    im,d=layer(); g=(60,160,80,255); gd=(35,110,55,255); rr(d,-.28,.35,.28,.6,.04,(190,100,60,255),(130,60,30,255),.03); rr(d,-.14,-.5,.14,.4,.12,g,gd,.03); rr(d,-.4,-.15,-.14,0,.06,g,gd,.02); rr(d,-.4,-.35,-.28,-.1,.06,g,gd,.02); rr(d,.14,-.05,.4,.1,.06,g,gd,.02); rr(d,.28,-.28,.4,0,.06,g,gd,.02)
    ell(d,0,-.52,.07,.06,(255,110,150,255)); return xform(im,1,4*sg(t))
def f_guitar(t):
    l,e=layer(); b=(190,120,60,255); bd=(120,70,30,255); ell(e,0,.32,.3,.28,b,bd,.03); ell(e,0,.0,.22,.2,b,bd,.03); ell(e,0,.2,.08,.08,(40,25,15,255)); rr(e,-.05,-.7,.05,.1,0,(90,55,30,255)); rr(e,-.1,-.85,.1,-.65,.02,(60,40,25,255))
    for i,x in enumerate((-.03,0,.03)): thick_line(e,[(x,-.7),(x+.02*math.sin(2*math.pi*t*3+i)*(1 if i==1 else .5),.5)],.008,(230,230,235,255))
    return xform(l,1,-35+3*sg(t))
def f_car(t):
    im,d=layer(); poly(d,[(-.6,.1),(-.55,-.05),(-.3,-.1),(-.15,-.35),(.3,-.35),(.45,-.1),(.62,0),(.65,.1),(.6,.3),(-.6,.3)],RE,RED_,.03); poly(d,[(-.1,-.1),(0,-.28),(.28,-.28),(.38,-.1)],(190,225,255,255)); thick_line(d,[(.1,-.28),(.1,-.1)],.02,RED_)
    for x in(-.35,.35): ell(d,x,.32,.17,.17,(45,48,55,255)); ell(d,x,.32,.08,.08,GR); spokes(d,x,.32,.14,120*t,3,GR,.02)
    for k in range(3): thick_line(d,[(-.75-.1*k+.3*((t+k/3)%1),.55),(-.65-.1*k+.3*((t+k/3)%1),.55)],.03,(190,195,205,255))
    return xform(im,1,0,0,-.012*sg(4*t))

# ===== gelombang 8 =====
def f_flagpost(t):
    im,d=layer(); ell(d,0,.58,.5,.1,(150,100,60,255)); thick_line(d,[(-.1,.58),(-.1,-.72)],.06,GR); top=[];bot=[]
    for i in range(9):
        u=i/8; x=-.1+.72*u; w=.06*math.sin(2*math.pi*t-5*u)*u; top.append((x,-.68+.22*u+w)); bot.append((x,-.22-.22*u+w))
    poly(d,top+bot[::-1],RE,RED_,.03); ell(d,-.1,-.74,.06,.06,(255,193,7,255)); return im
def f_nomouth(t):
    im,d=layer(); circle(d,.58,SK,SKD); ell(d,-.28,-.38,.14,.06,lt(SK)); b=bl(t,.8); lk=.06*math.sin(2*math.pi*t)
    for x in(-.2,.2): ell(d,x,-.05,.1,.12*b,W,GRD,.015); ell(d,x+lk,-.05,.05,.06*b,DK)
    thick_line(d,[(-.32,-.25),(-.1,-.23)],.035,DK); thick_line(d,[(.32,-.25),(.1,-.23)],.035,DK)
    f=(t*2)%1; ell(d,.46,-.4+.3*f,.05,.07,(90,170,255,255)) if f<.8 else None; return im
def f_camflash(t):
    im,d=layer(); c=(60,64,78,255); rr(d,-.25,-.5,.15,-.3,.04,c); rr(d,-.6,-.32,.6,.45,.1,c,(35,38,48,255),.03); rr(d,.28,-.45,.5,-.32,.03,(255,240,150,255),GRD,.02)
    ell(d,0,.07,.3,.3,(35,38,48,255)); ell(d,0,.07,.22,.22,(88,150,246,255)); ell(d,-.07,0,.07,.05,W)
    f=clamp((t-.2)/.4)
    if 0<f<1:
        e=math.sin(math.pi*f)
        for k in range(8): a=math.radians(k*45+10); thick_line(d,[(.39+.14*math.cos(a),-.38+.14*math.sin(a)),(.39+(.18+.5*e)*math.cos(a),-.38+(.18+.5*e)*math.sin(a))],.05,(255,240,150,255))
        star4(d,.39,-.38,.5*e,W)
    return im
def f_palette(t):
    im,d=layer(); wd=(205,150,90,255); ell(d,0,0,.62,.5,wd,dk_(wd),.03); ell(d,.28,.2,.1,.08,(0,0,0,0)); ell(d,-.12,.52,.2,.12,(0,0,0,0))
    cols=[RE,(255,214,0,255),(46,204,113,255),(52,120,246,255)]; pos=[(-.38,-.1),(-.15,-.3),(.15,-.3),(.4,-.1)]
    for i,(c,p) in enumerate(zip(cols,pos)): ell(d,p[0],p[1],.11*ease_out_back(clamp((t*1.0-.06*i)/.2)),.11*ease_out_back(clamp((t-.06*i)/.2)),c)
    k=t*4; j=int(k)%4; f=ease_io(k-int(k)); a=pos[j]; b=pos[(j+1)%4]; tip=(a[0]+(b[0]-a[0])*f,a[1]+(b[1]-a[1])*f-.05*math.sin(math.pi*f))
    thick_line(d,[(tip[0]+.05,tip[1]-.05),(tip[0]+.5,tip[1]-.55)],.06,BR); ell(d,tip[0],tip[1],.06,.06,cols[j]); return im
def f_bin(t):
    im,d=layer(); gr=(150,160,175,255); op=ease_io(clamp((t-.05)/.2))-ease_io(clamp((t-.62)/.2)); p=clamp((t-.25)/.3)
    if 0<p<1: x=.7-.7*p; y=-.7+.65*p-.4*math.sin(math.pi*p); ell(d,x,y,.11,.11,(235,235,240,255),GR,.02); thick_line(d,[(x-.05,y-.03),(x+.04,y+.04)],.015,GR)
    poly(d,[(-.35,-.1),(.35,-.1),(.28,.62),(-.28,.62)],gr,GRD,.03)
    for x in(-.15,0,.15): thick_line(d,[(x*1.1,0),(x,.55)],.03,GRD)
    l,e=layer(); rr(e,-.42,-.26,.42,-.12,.04,gr,GRD,.03); rr(e,-.08,-.34,.08,-.26,.02,GRD); lid=l.rotate(55*op,resample=Image.BICUBIC,center=(S/2-.4*K,S/2-.12*K)); im.alpha_composite(lid); return im
def f_serious(t):
    im,d=layer(); circle(d,.58,SK,SKD); ell(d,-.28,-.38,.14,.06,lt(SK)); [ell(d,x,-.1,.06,.06,DK) for x in(-.2,.2)]
    thick_line(d,[(-.34,-.27),(-.1,-.17)],.06,DK); thick_line(d,[(.34,-.27),(.1,-.17)],.06,DK); rr(d,-.34,.08,.34,.34,.07,(150,155,170,255),GRD,.025)
    for i,ch in enumerate("#@!%"): txt(d,ch,-.21+.14*i,.21+.03*math.sin(2*math.pi*(t*3+i*.25)),62,(40,44,56,255))
    return xform(im,1,3*math.sin(2*math.pi*6*t)*(1 if .2<t<.7 else 0))
def f_writing(t):
    pts=[(-.5,.5),(-.35,.33),(-.22,.52),(-.08,.33),(.06,.52),(.2,.33),(.34,.5)]; p=ease_io(clamp(t/.8)); q=partial(pts,max(p,.001)); tip=q[-1]
    im,d=layer(); thick_line(d,q,.045,BLD); l,e=layer(); thick_line(e,[(0,0),(.25,-.32)],.08,BL); ell(e,.34,-.4,.2,.18,SK,SKD,.03); ell(e,.2,-.25,.07,.09,SK,SKD,.02); rr(e,.45,-.62,.72,-.4,.04,BL)
    im.alpha_composite(xform(l,1,0,tip[0]-.1,tip[1]+.05)); return xform(xform(im,1.1),1,0,-.1,.0)
def f_smallsq(t):
    im,d=layer(); rr(d,-.3,-.3,.3,.3,.08,(240,242,245,255),(170,175,185,255),.04); rr(d,-.2,-.24,-.02,-.17,.03,W); return im
_ALIEN=["00100000100","00010001000","00111111100","01101110110","11111111111","10111111101","10100000101"]
def f_alien(t):
    im,d=layer(); c=.1; x0=-.55+.08*math.sin(2*math.pi*t); y0=-.4; col=(150,90,220,255); B=(t*4)%2<1
    rows=_ALIEN+(["00011011000"] if B else ["00110001100"])
    if not B: rows=[r for r in rows]; rows[6]="01000000010"
    for j,r in enumerate(rows):
        for i,ch in enumerate(r):
            if ch=="1": rr(d,x0+i*c,y0+j*c,x0+(i+1)*c,y0+(j+1)*c,.01,col)
    for i in(2,8): rr(d,x0+i*c+.01,y0+3*c+.01,x0+(i+1)*c-.01,y0+4*c-.01,.01,(255,255,255,255)) if False else None
    return xform(im,1,0,0,-.03*abs(math.sin(2*math.pi*t*2)))
def f_ladybug(t):
    im,d=layer(); w=math.sin(2*math.pi*t*3)
    for s in(-1,1):
        for k,y in enumerate((-.1,.1,.3)): thick_line(d,[(s*.3,y),(s*(.52+.04*w*(1 if k%2 else -1)),y+.1+.03*w)],.04,DK)
        thick_line(d,[(s*.08,-.55),(s*(.22+.03*w),-.72)],.025,DK)
    ell(d,0,-.42,.2,.15,DK); ell(d,0,.1,.42,.48,RE,RED_,.03); thick_line(d,[(0,-.35),(0,.57)],.025+.015*max(0,w),DK)
    for x,y,r in((-.22,-.1,.08),(.22,-.1,.08),(-.2,.2,.07),(.2,.2,.07),(-.1,.4,.05),(.1,.4,.05)): ell(d,x,y,r,r,DK)
    ell(d,-.1,-.45,.04,.04,W); ell(d,.1,-.45,.04,.04,W); return xform(im,1,4*math.sin(2*math.pi*t*1.5),0,-.02*abs(w))
def f_pointdown(t):
    l,e=layer(); _h_point(e,t); art=xform(l,1,180); dy=.13*(gb(t,.25,.06)+gb(t,.5,.06)); return xform(art,1,0,0,dy)

# ===== gelombang 9: api streak 6 tier (Amber, Crimson, Emerald, Azure, Phantom, Eternal) =====
# Semua gerak memakai frekuensi bilangan bulat terhadap t (0..1) agar loop mulus; "acak" dibuat deterministik (_hs).
from PIL import ImageFilter
def _hs(i,k=0):
    v=math.sin(i*12.9898+k*78.233)*43758.5453; return v-math.floor(v)
def _c(c,a=255): return (c[0],c[1],c[2],int(max(0,min(255,a))))
def _gbell(t,c,w): return math.exp(-(((t-c+.5)%1-.5)/w)**2)
def _bloom(im,cx,cy,r,col,a,blur=.5):
    g=Image.new("RGBA",(S,S),(col[0],col[1],col[2],0)); d=ImageDraw.Draw(g); x,y=P(cx,cy)
    d.ellipse([x-r*K,y-r*K,x+r*K,y+r*K],fill=_c(col,a)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(max(1,r*K*blur))))
def _sk_flame(t,cols,sc=1.0,dy=.06,amp=1.):
    im,d=layer(); hf=1+.07*amp*sg(t)
    flame(d,.62*hf,.42,_c(cols[0]),.10*amp*sg(t),-.02,t)
    flame(d,.46*hf,.30,_c(cols[1]),.07*amp*sg(t+.2),.14,t)
    flame(d,.28*hf,.18,_c(cols[2]),.05*amp*sg(2*t),.28,t)
    return xform(im,sc,0,0,dy)
def _embers(d,t,n,col,spread=.5,y0=.5,y1=-.95,size=.05,seed=0,sway=.1):
    for i in range(n):
        ph=(t+_hs(i,seed))%1
        x=(_hs(i,seed+1)*2-1)*spread*(1-.3*ph)+sway*math.sin(2*math.pi*(ph+_hs(i,seed+3)))
        r=size*(1-.55*ph)*(.6+.8*_hs(i,seed+2)); a=255*math.sin(math.pi*ph)**.6
        ell(d,x,y0+(y1-y0)*ph,r,r,_c(col,a))
def _sparks(d,t,n,col,r0=.5,r1=.92,seed=0,ln=.14,w=.032):
    for i in range(n):
        ph=(t+_hs(i,seed))%1; a=2*math.pi*_hs(i,seed+1); q0=r0+(r1-r0)*ph; q1=q0+ln*(1-ph)
        al=255*(1-ph)**.8*min(1,ph*8)
        d.line([P(q0*math.cos(a),q0*math.sin(a)*.9),P(q1*math.cos(a),q1*math.sin(a)*.9)],fill=_c(col,al),width=int(w*K))
def _pulse(d,t,col,n=2,r0=.55,r1=.95,w=.035):
    for i in range(n):
        f=(t+i/n)%1; ring(d,r0+(r1-r0)*f,_c(col,210*(1-f)**1.2*min(1,f*10)),w)
def _orbit(im,t,rx,ry,tilt,n,col,dirn=1,size=.07,side=1,ring_a=110,w=.022,ph0=0,star=False):
    g,d=layer(); ct,st=math.cos(tilt),math.sin(tilt)
    def pt(a): x=rx*math.cos(a); y=ry*math.sin(a); return (x*ct-y*st,x*st+y*ct)
    if ring_a>0:
        for k in range(40):
            a0=2*math.pi*k/40; a1=2*math.pi*(k+1)/40
            if side*math.sin((a0+a1)/2)>=0: d.line([P(*pt(a0)),P(*pt(a1))],fill=_c(col,ring_a),width=int(w*K))
    for j in range(n):
        a=2*math.pi*(dirn*t+j/n+ph0); s=math.sin(a)
        if side*s<0: continue
        x,y=pt(a); sz=size*(.75+.35*s*side)
        if star: star4(d,x,y,sz*1.7,_c(col))
        else: ell(d,x,y,sz,sz,_c(col))
    im.alpha_composite(g)
def _crystals(d,t,n,col,hi,rad=.8,size=.11,seed=0,dirn=1):
    for j in range(n):
        a=2*math.pi*(dirn*t+j/n); x=rad*math.cos(a)*(1+.08*_hs(j,seed)); y=rad*.78*math.sin(a)+.05*sg(2*t+_hs(j,seed+1))
        w=abs(math.cos(2*math.pi*(2*t+_hs(j,seed+2))))*.6+.35; sz=size*(.8+.4*_hs(j,seed+3))
        poly(d,[(x,y-sz),(x+sz*.6*w,y),(x,y+sz*1.1),(x-sz*.6*w,y)],_c(col))
        poly(d,[(x,y-sz),(x+sz*.6*w,y),(x,y)],_c(hi))
def _smoke(im,t,n,col,a=120,blur=14,y0=.35,rise=1.0,spread=.45):
    g=Image.new("RGBA",(S,S),(col[0],col[1],col[2],0)); d=ImageDraw.Draw(g)
    for i in range(n):
        ph=(t+_hs(i,9))%1; x=(_hs(i,10)*2-1)*spread+.08*math.sin(2*math.pi*(ph+_hs(i,11))); r=.14+.16*ph
        ell(d,x,y0-rise*ph,r,r,_c(col,a*math.sin(math.pi*ph)))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(blur)))
def _bolts(im,t,n,col,core=(255,255,255),dur=.22):
    g,d=layer()
    for s in range(n):
        u=(t-_hs(s,5)+1)%1
        if u>=dur: continue
        f=1-u/dur; ang=2*math.pi*_hs(s,6); step=int(u*14); pts=[]
        for k in range(6):
            r=.34+.12*k; off=0 if k in (0,5) else (_hs(s*7+k,7+step)-.5)*.2
            pts.append((r*math.cos(ang)-off*math.sin(ang),r*math.sin(ang)+off*math.cos(ang)))
        thick_line(d,pts,.075,_c(col,150*f)); thick_line(d,pts,.032,_c(core,255*f))
    im.alpha_composite(g)
def _arcs(d,t,n,r,col,span=40,w=.04,dirn=1,off=0):
    x,y=P(0,0)
    for k in range(n):
        a=360*(dirn*t+k/n+off); d.arc([x-r*K,y-r*K,x+r*K,y+r*K],a,a+span,fill=_c(col),width=int(w*K))
def _twink(d,t,pts,col,r=.12):
    for i,(x,y) in enumerate(pts): star4(d,x,y,r*twinkle(t,i*.27),_c(col))

def f_streak_amber(t):
    im,_=layer(); _bloom(im,0,.05,.5,(255,150,30),120+40*sg(t))
    g,d=layer(); _pulse(d,t,(255,190,70),2,.55,.92,.03); im.alpha_composite(g)
    im.alpha_composite(_sk_flame(t,[(255,95,15),(255,160,30),(255,236,120)]))
    g,d=layer(); _embers(d,t,9,(255,190,60),seed=1); _sparks(d,t,5,(255,230,130),seed=2); im.alpha_composite(g); return im
def f_streak_crimson(t):
    im,_=layer(); _smoke(im,t,5,(60,10,20),140,12)
    fl=_gbell(t,.3,.04); _bloom(im,0,.05,.55,(255,40,60),110+30*sg(t)+90*fl)
    _orbit(im,t,.78,.3,.3,5,(255,90,90),1,.055,side=-1,ring_a=0)
    im.alpha_composite(_sk_flame(t,[(190,12,35),(250,60,50),(255,190,180)],amp=1.2))
    _orbit(im,t,.78,.3,.3,5,(255,110,110),1,.055,side=1,ring_a=0)
    g,d=layer(); _embers(d,t,8,(255,80,80),seed=3,sway=.14); _sparks(d,t,6,(255,130,175),seed=4,r0=.45)
    if fl>.05:
        for k in range(4):
            a=2*math.pi*(k/4+.1); thick_line(d,[(.5*math.cos(a),.5*math.sin(a)),(.95*math.cos(a),.95*math.sin(a))],.05,_c((255,235,235),255*fl))
    im.alpha_composite(g); return im
def f_streak_emerald(t):
    im,_=layer(); _bloom(im,0,.05,.55,(40,220,130),120+40*sg(t))
    g,d=layer(); _arcs(d,t,3,.84,(120,255,185),60,.045); im.alpha_composite(g)
    im.alpha_composite(_sk_flame(t,[(20,170,95),(70,225,140),(215,255,230)]))
    g,d=layer(); _crystals(d,t,4,(40,200,120),(190,255,215),.78,.11,seed=2)
    _embers(d,t,6,(150,255,200),seed=5,size=.045); _twink(d,t,[(-.5,-.55),(.55,-.4),(.0,.75)],(220,255,235),.13)
    _pulse(d,t,(110,245,175),1,.6,.95,.03); im.alpha_composite(g); return im
def f_streak_azure(t):
    im,_=layer(); _bloom(im,0,.05,.55,(40,170,255),120+40*sg(t))
    g,d=layer(); _pulse(d,t,(120,220,255),2,.55,.96,.04); _arcs(d,t,8,.88,(190,240,255),22,.035,-1); im.alpha_composite(g)
    im.alpha_composite(_sk_flame(t,[(35,110,245),(70,200,255),(225,250,255)]))
    _bolts(im,t,4,(80,200,255))
    g,d=layer(); _crystals(d,t,5,(150,225,255),(235,250,255),.8,.085,seed=7,dirn=-1); _embers(d,t,6,(170,235,255),seed=8,size=.04)
    im.alpha_composite(g); return im
def f_streak_phantom(t):
    im,_=layer()
    g=Image.new("RGBA",(S,S),(0,0,0,0))
    for i in range(4):
        a=2*math.pi*(t+i/4); _bloom(g,.45*math.cos(a),.34*math.sin(a)+.05,.26,(150,60,230),90)
    im.alpha_composite(g); _bloom(im,0,.05,.5,(170,90,255),110+30*sg(t))
    _orbit(im,t,.9,.34,.55,3,(215,170,255),1,.06,side=-1,star=True); _orbit(im,t,.9,.34,-.55,3,(150,190,255),-1,.06,side=-1,star=True,ph0=.17)
    im.alpha_composite(_sk_flame(t,[(120,50,215),(185,110,255),(245,230,255)],sc=.92))
    _orbit(im,t,.9,.34,.55,3,(225,185,255),1,.06,side=1,star=True); _orbit(im,t,.9,.34,-.55,3,(170,205,255),-1,.06,side=1,star=True,ph0=.17)
    g,d=layer(); _crystals(d,t,4,(160,90,245),(225,190,255),.62,.095,seed=9,dirn=-1)
    _twink(d,t,[(-.65,-.6),(.62,-.62),(-.7,.45),(.68,.5),(0,-.85)],(255,255,255),.14); _embers(d,t,5,(215,170,255),seed=11,size=.04)
    im.alpha_composite(g); return im
def f_streak_eternal(t):
    im,_=layer(); _bloom(im,0,.0,.62,(255,205,70),115+35*sg(t))
    g,d=layer(); _pulse(d,t,(255,225,120),1,.62,1.0,.04); im.alpha_composite(g)
    _orbit(im,t,.92,.3,.4,4,(255,225,120),1,.055,side=-1,star=True,ring_a=90); _orbit(im,t,.92,.3,-.4,4,(255,245,200),-1,.055,side=-1,star=True,ring_a=90,ph0=.12)
    g,d=layer(); pu=.8+.2*sg(t)
    for k in range(7):
        c=k-3; a=math.radians(-90+c*15); L=(.34+.2*(1-abs(c)/3))*pu; x0,y0=.0+c*.06,-.7
        x1,y1=x0+L*math.cos(a),y0+L*math.sin(a); nx,ny=-math.sin(a)*.035,math.cos(a)*.035
        poly(d,[(x0+nx,y0+ny),(x1,y1),(x0-nx,y0-ny)],_c((255,230,130),230)); ell(d,x1,y1,.03,.03,(255,255,255,255))
    im.alpha_composite(g)
    im.alpha_composite(_sk_flame(t,[(255,185,40),(255,235,150),(255,255,255)],sc=.86,dy=.1))
    _orbit(im,t,.92,.3,.4,4,(255,235,140),1,.055,side=1,star=True,ring_a=110); _orbit(im,t,.92,.3,-.4,4,(255,250,215),-1,.055,side=1,star=True,ring_a=110,ph0=.12)
    g,d=layer(); b=t%1
    if b<.4:
        p=b/.4
        for k in range(10): a=2*math.pi*(k/10+.03); star4(d,(.3+.62*p)*math.cos(a),(.3+.62*p)*math.sin(a)*.9,.13*(1-p),_c((255,240,170)))
    _twink(d,t,[(-.7,-.35),(.72,-.2),(-.5,.62),(.55,.66)],(255,255,255),.14); _embers(d,t,6,(255,225,120),seed=13,size=.04)
    im.alpha_composite(g); return im
