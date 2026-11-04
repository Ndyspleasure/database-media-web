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
