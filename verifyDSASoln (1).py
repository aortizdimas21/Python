
import math
def verifyDSA(p,q,g,A,d,s1,s2):
    v1=linearCong(s2,d,q)
    v2= linearCong(s2,s1,q)
    x=pow(g,v1,p)
    y=pow(A,v2,p)
    z=(x*y)%p
   
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