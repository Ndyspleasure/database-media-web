import math, os
from PIL import Image, ImageDraw
OUTDIR=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','gifs'); os.makedirs(OUTDIR,exist_ok=True)
S=512; OUT=128; N=30; K=200
def ease_out_back(t):
    c1=1.70158; c3=c1+1; t=max(0,min(1,t)); return 1+c3*(t-1)**3+c1*(t-1)**2
def ease_io(t):
    t=max(0,min(1,t)); return t*t*(3-2*t)
def clamp(x): return max(0,min(1,x))
def P(x,y): return (S/2+x*K, S/2+y*K)
def layer(): 
    im=Image.new("RGBA",(S,S),(0,0,0,0)); return im, ImageDraw.Draw(im)
def xform(im, scale=1, rot=0, dx=0, dy=0):
    if scale<=0.01: return Image.new("RGBA",(S,S),(0,0,0,0))
    if rot: im=im.rotate(rot, resample=Image.BICUBIC, center=(S/2,S/2))
    if scale!=1:
        n=max(1,int(S*scale)); sm=im.resize((n,n),Image.LANCZOS)
        out=Image.new("RGBA",(S,S),(0,0,0,0)); out.paste(sm,((S-n)//2+int(dx*K),(S-n)//2+int(dy*K)),sm); return out
    if dx or dy:
        out=Image.new("RGBA",(S,S),(0,0,0,0)); out.paste(im,(int(dx*K),int(dy*K)),im); return out
    return im
def thick_line(d,pts,w,col):
    for a,b in zip(pts,pts[1:]):
        d.line([P(*a),P(*b)],fill=col,width=int(w*K))
    for p in pts:
        x,y=P(*p); r=w*K/2; d.ellipse([x-r,y-r,x+r,y+r],fill=col)
def partial(pts,prog):
    segs=[math.dist(a,b) for a,b in zip(pts,pts[1:])]; tot=sum(segs); rem=prog*tot; out=[pts[0]]
    for (a,b),l in zip(zip(pts,pts[1:]),segs):
        if rem>=l: out.append(b); rem-=l
        else:
            f=rem/l; out.append((a[0]+(b[0]-a[0])*f,a[1]+(b[1]-a[1])*f)); break
    return out
def circle(d,r,col,outline=None):
    x,y=P(0,0); d.ellipse([x-r*K,y-r*K,x+r*K,y+r*K],fill=col,outline=outline,width=int(.04*K))

def f_check(t):
    s=ease_out_back(t/0.3) if t<0.8 else 1-ease_in(( t-0.8)/0.2)
    im,d=layer(); circle(d,0.62,(46,204,113,255),(30,160,86,255))
    thick_line(d,partial([(-0.28,0.02),(-0.07,0.24),(0.30,-0.2)],ease_io((t-0.28)/0.3)),0.15,(255,255,255,255)) if t>0.28 else None
    return xform(im,s)
def ease_in(t): t=clamp(t); return t*t
def f_cross(t):
    s=ease_out_back(t/0.3) if t<0.85 else 1-ease_in((t-0.85)/0.15)
    im,d=layer(); circle(d,0.62,(231,76,60,255),(185,50,40,255))
    p=ease_io((t-0.25)/0.25)
    if t>0.25:
        thick_line(d,partial([(-0.24,-0.24),(0.24,0.24)],p),0.15,(255,255,255,255))
        thick_line(d,partial([(0.24,-0.24),(-0.24,0.24)],clamp((p-0.5)*2) if p<1 else 1),0.15,(255,255,255,255))
    dx=0.07*math.sin((t-0.5)*40)*clamp(1-(t-0.5)*4) if 0.5<t<0.75 else 0
    return xform(im,s,0,dx)
def f_warn(t):
    pulse=1+0.07*math.sin(t*2*math.pi); rot=6*math.sin(t*4*math.pi)
    im,d=layer()
    tri=[P(0,-0.62),P(0.68,0.52),P(-0.68,0.52)]
    d.polygon(tri,fill=(255,179,0,255)); d.line(tri+[tri[0]],fill=(200,130,0,255),width=int(.05*K),joint="curve")
    for p in tri: x,y=p; d.ellipse([x-.025*K,y-.025*K,x+.025*K,y+.025*K],fill=(200,130,0,255))
    d.rounded_rectangle([P(-0.07,-0.28),P(0.07,0.12)],radius=int(.06*K),fill=(60,40,10,255))
    x,y=P(0,0.3); d.ellipse([x-.085*K,y-.085*K,x+.085*K,y+.085*K],fill=(60,40,10,255))
    return xform(im,pulse*0.95,rot)
def f_hour(t):
    drain=clamp(t/0.78); f=1-drain; ang=0
    if t>0.78: ang=180*ease_io((t-0.78)/0.22)
    im,d=layer()
    glass=(170,220,255,150); line=(90,150,200,255); sand=(255,196,60,255); wood=(150,95,50,255)
    top=[P(-.3,-.4),P(.3,-.4),P(0,0)]; bot=[P(0,0),P(.3,.4),P(-.3,.4)]
    d.polygon(top,fill=glass); d.polygon(bot,fill=glass)
    ys=-.4+.4*(1-f)
    if f>0.01:
        w=-.75*ys; d.polygon([P(-w,ys),P(w,ys),P(0,0)],fill=sand)
    g=drain; yb=.4-.4*g
    if g>0.01:
        w=.75*yb; d.polygon([P(-w,yb),P(w,yb),P(.3,.4),P(-.3,.4)],fill=sand)
    if 0.01<drain<0.99: d.line([P(0,0),P(0,yb)],fill=sand,width=int(.03*K))
    d.line(top+[top[0]],fill=line,width=int(.03*K),joint="curve"); d.line(bot+[bot[0]],fill=line,width=int(.03*K),joint="curve")
    for y in (-.48,.4): d.rounded_rectangle([P(-.38,y),P(.38,y+.08)],radius=int(.03*K),fill=wood)
    return xform(im,1,ang)

def save(name,fn,n=N,dur=45):
    frames=[]
    for i in range(n):
        im=fn(i/n).resize((OUT,OUT),Image.LANCZOS)
        a=im.getchannel("A"); p=im.convert("RGB").quantize(colors=255,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE)
        p.paste(255,a.point(lambda v:255 if v<128 else 0)); p.info["transparency"]=255; frames.append(p)
    path=os.path.join(OUTDIR,f"{name}.gif")
    frames[0].save(path,save_all=True,append_images=frames[1:],duration=dur,loop=0,disposal=2,transparency=255,optimize=False)
    print(name, os.path.getsize(path)//1024,"KB"); return frames

def poly(d,pts,fill,outline=None,w=.03):
    q=[P(*p) for p in pts]; d.polygon(q,fill=fill)
    if outline: d.line(q+[q[0]],fill=outline,width=int(w*K),joint="curve")
def rr(d,x0,y0,x1,y1,r,fill,outline=None,w=.03):
    d.rounded_rectangle([P(x0,y0),P(x1,y1)],radius=int(r*K),fill=fill,outline=outline,width=int(w*K))
def ell(d,cx,cy,rx,ry,fill,outline=None,w=.03):
    x,y=P(cx,cy); d.ellipse([x-rx*K,y-ry*K,x+rx*K,y+ry*K],fill=fill,outline=outline,width=int(w*K))
def ring(d,r,col,w=.04):
    x,y=P(0,0); d.ellipse([x-r*K,y-r*K,x+r*K,y+r*K],outline=col,width=max(1,int(w*K)))
def star4(d,cx,cy,r,fill):
    if r<=0.01: return
    pts=[]
    for i in range(8):
        a=i*math.pi/4-math.pi/2; rad=r if i%2==0 else r*.28; pts.append((cx+rad*math.cos(a),cy+rad*math.sin(a)))
    poly(d,pts,fill)
def twinkle(t,ph=0):
    f=(t+ph)%1; return math.sin(math.pi*f/0.4) if f<0.4 else 0
def ripple(d,t,col):
    f=t%1; r=.6+.3*f; ring(d,r,col[:3]+(int(170*(1-f)),),.05)
def sg(x): return math.sin(2*math.pi*x)

