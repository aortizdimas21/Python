import math

def pollardRSA(N,e,c):
    p=PollAlgo(N)
    q=N//p
    d=modinv(e,((p-1)*(q-1)))
    if d>=1:
        m=pow(c,d,N)
    else: 
        o=-1*d
        k=modinv(c,N)
        m=pow(k,o,N)
  
    return m


def PollAlgo (n):
    l=2
    k=1
    while math.gcd(l-1,n)==1:
        k+=1
        l=pow(l,k,n)
        w=math.gcd(l-1,n) #faster to just use math.gcd instead of my own gcd function
        if w!=1:
            return w


def linearCong(m,b,N):
    
    l=bezout(m,N)
    if l[0]==1:
        r=(b*modinv(m,N))%N
        M=N
        return r
    if l[0]!=1:
        m_new=m//l[0]
        b_new=b//l[0]
        N_new=N//l[0]
        
        #if b_new.is_integer()==False:
            #return None
        
        p=bezout(m_new,N_new)
        
        
        if p[0]!=1:
            return None
        
        if p[0]==1: 
            r=(b_new*modinv(m_new,N_new))%N_new
            M=N_new
           
            return r
        
        return r        
    
def bezout(a,b):
    f0=a
    f1=b
    u0=1
    v0=0
    u1=0
    v1=1
    while f0%f1!=0:
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
    return f1,u1,v1
       
def gcd(a,b):
    f0=a
    f1=b
    u0=1
    v0=0
    u1=0
    v1=1
    while f0%f1!=0:
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
    return f1

def modinv(a,b):
    r0=a
    r1=b
    u0=1
    v0=0
    u1=0
    v1=1
    while r1!=0:
        q=r0//r1
        r2=r0-q*r1
        u2=u0-q*u1
        v2=v0-q*r1
        u0=u1
        u1=u2
        v1=v2
        r0=r1
        r1=r2
    return u0 