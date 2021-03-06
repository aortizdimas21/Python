#In one of the written problems (3.13 in the 2nd edition, 3.12 in the 1st), you saw that it is unsafe to use the same modulus  π  in two different RSA public keys. In this problem, you will implement the algorithm that Eve could use to exploit that situation, in a more general context.

#Suppose that you know a modulus  π , two relatively prime integers  π,π , and two powers  ππ(modπ)  and  ππ(modπ)  of an unknown integer  π . You may assume that  π  is a unit modulo  π . Write a function  ππ΅ππππΏππ πππ(π½,π,π,ππ,ππ)  that computes and returns the unknown integer  π  (you should return  π  reduced modulo  π , i.e.  0β€π<π ). The integer  π  will be  1000  bits long in the largest test cases, but a naive approach will earn partial credit.


def mFromPowers(N,e,f,me,mf):
    c1=me #these are both already reduced mod N
    c2=mf
    
    b=bezout(e,f)
    u=b[0]
    v=b[1]
   
    if u>=1:
        yy=pow(c1,u,N)
    else: 
        o=-1*u
        k=modinv(c1,N)
        yy=pow(k,o,N)
        
    if v>=1:
        d=pow(c2,v,N)
    else: 
        v=-1*v
        w=modinv(c2,N)
        d=pow(w,v,N)
        
        
    m=(yy*d)%N
       
  
    # Your code here
    
    return m

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
    return u1,v1

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

