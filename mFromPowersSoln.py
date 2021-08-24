#In one of the written problems (3.13 in the 2nd edition, 3.12 in the 1st), you saw that it is unsafe to use the same modulus  𝑁  in two different RSA public keys. In this problem, you will implement the algorithm that Eve could use to exploit that situation, in a more general context.

#Suppose that you know a modulus  𝑁 , two relatively prime integers  𝑒,𝑓 , and two powers  𝑚𝑒(mod𝑁)  and  𝑚𝑓(mod𝑁)  of an unknown integer  𝑚 . You may assume that  𝑚  is a unit modulo  𝑁 . Write a function  𝚖𝙵𝚛𝚘𝚖𝙿𝚘𝚠𝚎𝚛𝚜(𝙽,𝚎,𝚏,𝚖𝚎,𝚖𝚏)  that computes and returns the unknown integer  𝑚  (you should return  𝑚  reduced modulo  𝑁 , i.e.  0≤𝑚<𝑁 ). The integer  𝑁  will be  1000  bits long in the largest test cases, but a naive approach will earn partial credit.


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

