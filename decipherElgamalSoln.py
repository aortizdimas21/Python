import math #makes it so that I am able to use the power function

def decipherElgamal(p,g,a,c1,c2):
    
    w = pow(c1,a,p)
    w = bezout(w,p)
    m = (c2*w)%p
    
    return m

#reusing code from the other problem set
def bezout(a,b):
    f0=a
    f1=b
    u0=1
    v0=0
    u1=0
    v1=1
    while f1!=0:
        r=f0//f1
        f2=f0 - r*f1
        u2=u0 - r*u1
        v2=v0 - r*v1
        u0=u1
        u1=u2
        v0=v1
        v1=v2
        f0=f1
        f1=f2
    return u0
   
        