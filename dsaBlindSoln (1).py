import random
import math

def dsaBlind(p,q,g,A):
    i=(random.randint(1,q))%q
    j=1
    while gcd(j,p-1)!=1:
        j+=1
   
    s1=((pow(g,i,p)*pow(A,j,p))%p)%q
    s2=linearCong(j,s1,q)
    d=linearCong(j,s1*i,q)
        
   
  
 

    print(verifyDSA(p,q,g,A,d,s1,s2))
    # Your code here
    return d,s1,s2


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

def verifyDSA(p,q,g,A,d,s1,s2):
    v1=linearCong(s2,d,q)
    v2= linearCong(s2,s1,q)
    x=pow(g,v1,p)
    y=pow(A,v2,p)
    z=(x*y)%p
    print(v1,v2,z%q)
    if (z%q)==s1:
        return True
    else:
        return False
    
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
        
   
    
    # Your code here
    # The function should either "return None" or "return r,M", where the solution is x = r momod M.

    
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


def bsgs(g,h,p):
    
    N=p-1
    n=int(math.sqrt(N))+2
    gn=pow(g,n,p)
    gninv=modinv(gn,p)
    bstep=[1]
    gstep=[h]
    
    for i in range (1,n):
        bstep.append(bstep[-1]*g%p)
        gstep.append (gstep[-1]*gninv%p)
    coll=collision(bstep,gstep)
    if coll==None:
        return None
    else:
        return coll [0] + n*coll[1]
    
    
    
def collision (list1, list2):
    lookup=dict()
    
    for i in range (len(list1)):
        lookup [list1[i]]=i
    for j in range (len(list2)):
        if list2[j] in lookup:
            return (lookup[list2[j]], j)
        
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