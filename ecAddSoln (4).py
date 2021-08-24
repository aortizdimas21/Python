def ecAdd(P,Q,A,B,p):
    if Q==0:
        return P
    if P==0:
        return Q
    x1=P[0]
    y1=P[1]
    x2=Q[0]
    y2=Q[1]
    
    if x1==x2 and y1==-1*y2:
        return 0
    if x1==x2 and y1!=y2:
        return 0
   
    if P==Q:
        s=((3*pow(x1,2)+A)*modinv(2*y1,p))%p
    if P!=Q:
        s=((y2-y1)%p)*(modinv(x2-x1,p))%p
        
    x=(pow(s,2)-x1-x2)%p
    y=(s*(x1-x)-y1)%p
    
    return x,y
        
    # Your code here
    # Should either return 0 (for point at infinity)
    #   or return (x,y), where x,y are in Z / p Z
    
    
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
    