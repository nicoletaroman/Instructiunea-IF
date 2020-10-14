xa=int(input("bile mari albe"))
xr=int(input("bile mari rosii"))
xv=int(input("bile mari verzi"))
ya=int(input("bile mici albe"))
yr=int(input("bile mici rosii"))
yv=int(input("bile mici verzi"))
xt=xa+xr+xv
yt=ya+yr+yv
print("sunt in total",xt+yt,"bile")
if xt>yt:
    print("sunt mai multe bile mari")
if xt==yt:
    print("Nr de bile este egal")
else:
    print("sunt mai multe bile mici")
if xa+ya>xr+yr and xa+ya>xv+yv:
    print("sunt mai multe albe")
if xr+yr>xa+ya and xr+yr>xv+yv:
    print("sunt mai multe rosii")
if xv+yv>xr+yr and xv+yv>xa+ya:
    print("sunt mai multe verzi")
if xa+ya==xr+yr and xa+ya==xv+yv:
    print("sunt nr egale")
if xa+ya>xr+yr and xa+ya==xv+yv:
    print("sunt mai multe verzi si albe")
if xa+ya==xr+yr and xa+ya>xv+yv:
    print("sunt mai multe albe si rosii")
if xv+yv==xr+yr and xv+yv>xa+ya:
    print("sunt mai multe verzi si rosii")
