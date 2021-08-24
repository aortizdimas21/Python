def relatedkeys(g,p,A,c11,c12,m1,c21,c22):
    o=uv(c11,c21,g,p)
    u=o[0]
    v=o[1]
    Av=(pow(A,v,p))
    Ak_inv=pow(m1*bezouts(c12,p),1,p)
    Av_inv=(bezouts(Av,p))%p
    m2=pow(c22*(pow(Ak_inv,u))*Av_inv,1,p)
    
    return m2
    # your code here
    

def uv(c11,c21,g,p):
        u=1
        v=1
        while c21!=(pow(c11,u,p)*pow(g,v,p))%p:
            v+=1
            if v==100:
                u+=1
                v=1
            if c21==(pow(c11,u,p)*pow(g,v,p))%p:
                return u,v

def decipherElgamal(p,g,a,c1,c2):
    
    w = pow(c1,a,p)
    w = bezout(w,p)
    m = (c2*w)%p
    
    return m

def analyzeElgamal(g,p,A,c11,c12,m1,c21,c22):
    y=bezouts(c12,p)
        
    m2 =(y*m1*c22)%p
    

    return m2

def bezouts(a,b):
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

