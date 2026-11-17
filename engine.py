from random import getrandbits as gb
import json,os,urllib.request,zlib
VL=(0,82,337,365,477,1025,0)
EL=(0,94,281,297,512,936,0)
NM=[chr(97+(s%8))+str(s//16+1)for s in range(128)]
NJ=(-33,-31,-18,-14,14,18,31,33)
GJ=(-17,-16,-15,-1,1,15,16,17)
DJ=(-17,-15,15,17)
RJ=(-16,-1,1,16)
QJ=DJ+RJ
MV=(0,0,0,DJ,RJ,QJ)
CL={7:14,0:13,119:11,112:7}
MT=100000
PP='KKKKKKKKcmZc\\kSHIMQS[YQFGNMPQNOEDKJNOMMEEJJILLSHBKFEGQUEKKKKKKKK'
PN='!5C?Z3G09A]TQ[MG?ZT[`k]VIOPXT\\OQHLONRPPIEINMPOQGD>HJKOGF1F=CGDFE'
PB='DL7BEAMIEOGHSZO?GTVUTWTKJLPWTTMKINNQSNMLKOOOOROMLOOKMPSKCJGFHHAF'
PK=';QOG=CKNRKFIIJADIQKGFMQEGFHDCEGB?KDA?@C>GGE?@CGDKMI;@GMMGTN=MDQO'
PG=PE=(None,PP,PN,PB,None,None,PK)
ZB=[[gb(64)for _ in range(128)]for _ in range(13)]
def tv(u,sq,fl=0):
 return (ord(u[sq])-75)*4 if u else 0
class St:
 __slots__=("s","t","c","e","h","w","k","o")
def load(f):
 st=St()
 st.s=[0]*128
 st.o=[]
 w=f.split()
 sq=112
 for c in w[0]:
  if c=="/":
   sq=sq-24
  elif c.isdigit():
   sq=sq+int(c)
  else:
   pc="PNBRQK".index(c.upper())+1
   if c>"Z":
    pc=-pc
   st.s[sq]=pc
   st.o.append(sq)
   if 6==pc:
    st.w=sq
   elif -6==pc:
    st.k=sq
   sq=sq+1
 if "w"==w[1]:
  st.t=1
 else:
  st.t=-1
 cs=w[2] if len(w)>2 else "-"
 st.c=0
 for b,c in ((1,"K"),(2,"Q"),(4,"k"),(8,"q")):
  if c in cs:
   st.c=st.c+b
 st.e=-1
 if len(w)>3 and "-"!=w[3]:
  st.e=int(w[3][1])-1
  st.e=st.e*16+ord(w[3][0])-97
 st.h=0
 i=0
 while i<len(st.o):
  sq=st.o[i]
  st.h=st.h^ZB[st.s[sq]+6][sq]
  i=i+1
 return st
def hit(st,sq,wt):
 b=st.s
 d0=-15 if wt else 15
 d1=-17 if wt else 17
 for d in (d0,d1):
  t=sq+d
  if t<0 or t>127 or t%16>7:
   continue
  if b[t]==(1 if wt else -1):
   return True
 for ds,pc in ((NJ,2),(GJ,6)):
  i=0
  while i<len(ds):
   t=sq+ds[i]
   i=i+1
   if t<0 or t>127 or t%16>7:
    continue
   if b[t]==(pc if wt else -pc):
    return True
 for ds,ps in ((DJ,(3,5)),(RJ,(4,5))):
  for d in ds:
   t=sq+d
   while t>=0 and t<=127 and t%16<=7:
    pc=b[t]
    if pc:
     if abs(pc) in ps and (pc>0)==wt:
      return True
     break
    t=t+d
 return False
def bad(st):
 if st.t>0:
  return hit(st,st.k,True)
 return hit(st,st.w,False)
def gen(st,co=False):
 b=st.s
 y=st.t
 ms=[]
 for f in st.o:
  pc=b[f]
  if (pc>0)!=(y>0):
   continue
  ap=abs(pc)
  if 1==ap:
   pawn(st,f,ms,co)
  elif 2==ap or 6==ap:
   ds=NJ if 2==ap else GJ
   for d in ds:
    t=f+d
    if t<0 or t>127 or t%16>7:
     continue
    q=b[t]
    if 0==q:
     if not co:
      ms.append(f+t*128)
    elif (q>0)!=(y>0):
     ms.append(f+t*128)
   if 6==ap and not co:
    castle(st,f,ms)
  else:
   for d in MV[ap]:
    t=f+d
    while t>=0 and t<=127 and t%16<=7:
     q=b[t]
     if 0==q:
      if not co:
       ms.append(f+t*128)
     else:
      if (q>0)!=(y>0):
       ms.append(f+t*128)
      break
     t=t+d
 return ms
def pawn(st,f,ms,co):
 b=st.s
 y=st.t
 if y>0:
  step=16
  sr=1
  pr=7
 else:
  step=-16
  sr=6
  pr=0
 for d in (step-1,step+1):
  t=f+d
  if t<0 or t>127 or t%16>7:
   continue
  q=b[t]
  if q and (q>0)!=(y>0):
   pp(st,f,t,ms,pr)
  elif t==st.e:
   ms.append(f+t*128)
 if co:
  return
 t=f+step
 if t>=0 and t<=127 and t%16<=7 and 0==b[t]:
  pp(st,f,t,ms,pr)
  if f//16==sr:
   t2=f+2*step
   if 0==b[t2]:
    ms.append(f+t2*128)
def pp(st,f,t,ms,pr):
 if pr==t//16:
  for z in (5,4,3,2):
   ms.append(f+t*128+z*16384)
 else:
  ms.append(f+t*128)
def castle(st,f,ms):
 b=st.s
 wt=st.t>0
 ks=4 if wt else 116
 if f!=ks:
  return
 rk=4 if wt else -4
 bs=0 if wt else 112
 kb=1 if wt else 4
 qb=2 if wt else 8
 for bit,t,rf,rt,em,sf in ((kb,bs+6,bs+7,bs+5,(bs+5,bs+6),(bs+4,bs+5,bs+6)),(qb,bs+2,bs,bs+3,(bs+3,bs+2,bs+1),(bs+4,bs+3,bs+2))):
  if st.c&bit and b[rf]==rk and all(0==b[s] for s in em) and all(not hit(st,s,not wt) for s in sf):
   ms.append(f+t*128)
def do(st,m):
 b=st.s
 f=m%128
 t=m//128%128
 z=m//16384%8
 pc=b[f]
 v=b[t]
 q=-1
 if 1==abs(pc) and t==st.e and 0==v:
  q=t-16 if st.t>0 else t+16
  v=b[q]
 u=(m,v,q,st.c,st.e,st.h,st.w,st.k)
 h=st.h
 h=h^ZB[pc+6][f]
 if v:
  h=h^ZB[v+6][t if q<0 else q]
 b[f]=0
 npc=pc
 if z:
  npc=z if st.t>0 else -z
 b[t]=npc
 if q>=0:
  b[q]=0
 if v:
  st.o.remove(t if q<0 else q)
 st.o[st.o.index(f)]=t
 if 6==abs(pc) and 2==abs(t-f):
  rf=t+1 if t%16>4 else t-2
  rt=t-1 if t%16>4 else t+1
  rk(st,rf,rt)
  rk2=4 if t<64 else -4
  h=h^ZB[rk2+6][rf]^ZB[rk2+6][rt]
 if 6==pc:
  st.w=t
 elif -6==pc:
  st.k=t
 k=st.c
 if 6==pc:
  k=k&12
 elif -6==pc:
  k=k&3
 for s in (f,t):
  k=k&CL.get(s,15)
 e=-1
 if 1==abs(pc) and 32==abs(t-f):
  e=(f+t)//2
 h=h^ZB[npc+6][t]
 st.c=k
 st.e=e
 st.h=h
 st.t=-st.t
 return u
def rk(st,f,t):
 b=st.s
 pc=b[f]
 b[f]=0
 b[t]=pc
 st.o[st.o.index(f)]=t
def undo(st,u):
 m,v,q,k,e,h,wk,bk=u
 f=m%128
 t=m//128%128
 z=m//16384%8
 pc=st.s[t]
 if z:
  pc=1 if st.t<0 else -1
 b=st.s
 if 6==abs(pc) and 2==abs(t-f):
  rf=t-1 if t%16>4 else t+1
  rt=t+1 if t%16>4 else t-2
  rk(st,rf,rt)
 st.o[st.o.index(t)]=f
 b[t]=0
 b[f]=pc
 if v:
  cs=t if q<0 else q
  b[cs]=v
  st.o.append(cs)
 st.c=k
 st.e=e
 st.h=h
 st.w=wk
 st.k=bk
 st.t=-st.t
def ev(st):
 b=st.s
 mg=0
 eg=0
 ph=0
 nb=0
 i=0
 while i<len(st.o):
  sq=st.o[i]
  i=i+1
  pc=b[sq]
  ap=abs(pc)
  s64=(7-sq//16)*8+sq%8
  if pc<0:
   s64=sq//16*8+sq%8
  sg=1 if pc>0 else -1
  mg=mg+sg*(VL[ap]+tv(PG[ap],s64))
  eg=eg+sg*(EL[ap]+tv(PE[ap],s64))
  ph=ph+(0,0,1,1,2,4,0)[ap]
  if 3==ap:
   nb=nb+sg
 sc=(mg*ph+eg*(24-ph))//24
 if 2==nb:
  sc=sc+30
 elif -2==nb:
  sc=sc-30
 return sc if st.t>0 else -sc
class TO(Exception):
 pass
def sc(z,st,m,tm,pl):
 b=st.s
 v=b[m//128%128]
 if m==tm:
  return -1000000
 if v:
  return -900000-10*VL[abs(v)]+VL[abs(b[m%128])]//10
 if m//16384%8:
  return -800000-VL[m//16384%8]
 k0,k1=z.k[pl] if pl<128 else (0,0)
 if m==k0:
  return -50000
 if m==k1:
  return -40000
 return 0
class Eng:
 def __init__(z,bd=90000):
  z.b=bd
  z.n=0
  z.t={}
  z.k=[[0,0]for _ in range(128)]
  z.S=set()
 def cnt(z):
  z.n=z.n+1
  if z.n>z.b:
   raise TO()
 def srt(z,st,ms,tm,pl):
  ms.sort(key=lambda m:sc(z,st,m,tm,pl))
  return ms
 def q(z,st,a,be,pl):
  z.cnt()
  ks=st.w if st.t>0 else st.k
  ck=hit(st,ks,st.t<0)
  if not ck:
   sd=ev(st)
   if sd>=be:
    return be
   if sd>a:
    a=sd
  ms=z.srt(st,gen(st,co=not ck),0,pl)
  lg=0
  for m in ms:
   u=do(st,m)
   if bad(st):
    undo(st,u)
    continue
   lg=lg+1
   s2=-z.q(st,-be,-a,pl+1)
   undo(st,u)
   if s2>=be:
    return be
   if s2>a:
    a=s2
  if ck and 0==lg:
   return -MT+pl
  return a
 def s(z,st,d,a,be,pl):
  z.cnt()
  key=(st.h,st.t,st.c,st.e)
  if pl>0 and key in z.S:
   return 0
  if d<=0:
   return z.q(st,a,be,pl)
  te=z.t.get(key)
  tm=0
  if te:
   dd,fl,v,tm=te
   if dd>=d:
    if 0==fl:
     return v
    if 1==fl:
     a=max(a,v)
    else:
     be=min(be,v)
    if a>=be:
     return v
  ks=st.w if st.t>0 else st.k
  ck=hit(st,ks,st.t<0)
  if d>=3 and not ck and pl>0:
   e2=ev(st)
   if e2>=be:
    sv=st.t
    ep=st.e
    st.t=-st.t
    st.e=-1
    s2=-z.s(st,d-3,-be,-be+1,pl+1)
    st.t=sv
    st.e=ep
    if s2>=be:
     return be
  ao=a
  z.S.add(key)
  ms=z.srt(st,gen(st),tm,pl)
  bt=-MT
  bm=0
  lg=0
  for i,m in enumerate(ms):
   u=do(st,m)
   if bad(st):
    undo(st,u)
    continue
   lg=lg+1
   cp=0!=u[1]
   pr=0!=(m//16384%8)
   if 1==lg:
    s2=-z.s(st,d-1,-be,-a,pl+1)
   else:
    rd=d-1
    if d>=3 and i>=3 and not cp and not pr and not ck and m!=z.k[pl][0] and m!=z.k[pl][1]:
     rd=d-2
    s2=-z.s(st,rd,-a-1,-a,pl+1)
    if s2>a:
     s2=-z.s(st,d-1,-be,-a,pl+1)
   undo(st,u)
   if s2>bt:
    bt=s2
    bm=m
   if s2>a:
    a=s2
    if a>=be:
     if not cp and not pr:
      kk=z.k[pl]
      if kk[0]!=m:
       kk[1]=kk[0]
       kk[0]=m
     break
  z.S.discard(key)
  if 0==lg:
   return -MT+pl if ck else 0
  if bt<=ao:
   fl=2
  elif bt>=be:
   fl=1
  else:
   fl=0
  z.t[key]=(d,fl,bt,bm)
  return bt
 def go(z,st,hs=None):
  z.S=set(hs) if hs else set()
  lg=[]
  for m in gen(st):
   u=do(st,m)
   if not bad(st):
    lg.append(m)
   undo(st,u)
  rm=z.srt(st,lg,0,0)
  z.n=0
  bt=rm[0]
  try:
   d=1
   while d<64:
    a=-MT
    for i,m in enumerate(rm):
     u=do(st,m)
     if 0==i:
      s2=-z.s(st,d-1,-MT,-a,0)
     else:
      s2=-z.s(st,d-1,-a-1,-a,0)
      if s2>a:
       s2=-z.s(st,d-1,-MT,-a,0)
     undo(st,u)
     if s2>a:
      a=s2
      bt=m
    rm.remove(bt)
    rm.insert(0,bt)
    if a>=MT-200:
     break
    d=d+1
  except TO:
   pass
  m=bt
  return NM[m%128]+NM[m//128%128]+("nbrq"[(m//16384%8)-2] if (m//16384%8) else "")
SV=os.environ["MAKEFUN_ENV_URL"]
E=Eng()
OB='\x1bL\x03\x82\x1a\x83X\x06!\x19\x8a\x9f\x09\xe4\x1bs\xbb\x11\xb2!\xc5\xe9\x18\x93\x19\xe0E\x1b\xa5\x19ew\x1c\xc7\x1at0 5\x0b\x02k!\x82\x08\x9e\xa4"D\x19\xe7\x1b#\xa2\x18\x14<&b!\xf3\x871\x91\x10\xba\xef1u2\x9b\x04;%#\x0d\xa5<\x90\x10H\xde<"\x18\x0c\xccB3"?sW\x85\x136\x19Y\xb0(OV\\\x91\x18\xeasd\x008|N\x8c\xf4:\xe3b\x90\xf2\x13a\x17\x94\xd5#\xc1\xa0\x9d\xb2)bS\xa8\xc6\x12\x11\xf6\xac\xf08\xf1\xc7\xbeC\x08\x04\xbb\xc6S"\x82S\xd5c"N=\xe3%"\xfe\x9b\xf2\x16\x13\xf5\xe0\xfa\xb5\x09'
def key(f):
 return zlib.crc32(" ".join(f.split()[:4]).encode())&16777215
Bk={}
for _i in range(0,len(OB),5):
 _b=OB[_i:_i+5].encode("latin-1")
 _v=_b[3]|_b[4]<<8
 Bk[_b[0]|_b[1]<<8|_b[2]<<16]=NM[_v%128]+NM[_v//128%128]+("nbrq"[(_v//16384%8)-2] if _v//16384%8 else "")
def io(p,b):
 q=urllib.request.Request(SV+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 return json.load(urllib.request.urlopen(q))
hs=[]
while 1:
 o=io("/game",{})
 if o["status"]=="done":
  break
 hs=[]
 while o["status"]=="your_move":
  pos=load(o["fen"])
  hs.append((pos.h,pos.t,pos.c,pos.e))
  m=Bk.get(key(o["fen"]))
  if m is None or m not in o["legal_moves"]:
   try:
    m=E.go(pos,hs)
   except Exception:
    m=o["legal_moves"][0]
   if m not in o["legal_moves"]:
    m=o["legal_moves"][0]
  o=io("/move",{"game":o["game"],"move":m})
