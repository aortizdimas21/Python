def rsaThreePrimes(p,q,r,e,c):
    modulo=(p*q*r)
    modulo_1=(p-1)*(r-1)*(q-1)
    d=modinv(e,modulo_1)
    
    if d<=0:
        d=d*-1
        c_inv=modinv(c,modulo) #finding the inverse of the function so that I can raise to a negative power. Ex - (7)^-15 is the same as (7^-1)^15
        m=pow(c_inv,d,modulo)
    else:
        m=pow(c,d,modulo)
        

        
        
        
    # your code here
    return m

def modinv(a,b):
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