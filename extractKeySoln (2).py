#. When using ElGamal digital signatures, it is essential that Samantha always generates her
#ephemeral key at random (much like in ElGamal encryption). In this problem, you will study why it is particularly dangerous to use the same ephemeral key twice. You will be given the public ElGamal parameters p,g, Alice’s public key A, two documents d1,d2, and valid signatures (s11,s12),(s21,s22) for the two documents (respectively). The two signatures were generated using the same ephemeral key. Write a function extractKey(p,g,A,d1,s11,s12,d2,s21,s22)that extracts and returns Alice’s private key a from this information.

def extractKey(p,g,A,d1,s11,s12,d2,s21,s22):
    
   
        N=p-1
        m=s11*(s22-s12)
        b=((s22*d1)-(s12*d2))%N
        lc=linearCong(m,b,N)
        r=lc[0]
        M=lc[1]
       
        while pow(g,r,p)!=A:
            r=r+M
            
           
    # Your code here
        return r




def linearCong(m,b,N):
    
    l=bezout(m,N)
    if l[0]==1:
        r=(b*modinv(m,N))%N
        M=N
        return r,M
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
           
            return r,M
        
        return r,M
        
   
    
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