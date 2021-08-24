#Write a function  𝚎𝚌𝙳𝙻𝙿(𝙿,𝚀,𝙰,𝙱,𝚙,𝚚)  to solve the elliptic curve discrete logarithm problem, in cases where the prime  𝑝  is up to 28 bits. Here,  𝑃,𝑄  are points on the curve  𝑌2≡𝑋3+𝐴𝑋+𝐵(mod𝑝) , and you are given, for convenience, the number  𝑞  of points on the curve (which you may assume to be prime). The function should return the minimum nonnegative  𝑛  such that  𝑛⋅𝑃=𝑄 . Note that if you find any such solution  𝑛′ , then you can find the minimum solution by computing  𝑛′(mod𝑞) . Note: one issue you may encounter is that it is not possible to place a “list” (e.g. [2,3]) into a Python dict. To resolve this, make sure all of your elliptic curve points (besides O) are represented as “tuples” instead (e.g. (2,3), with parentheses instead of brackets).

import math

def ecDLP(P,Q,A,B,p,q):
    N=q
    n=int(math.sqrt(N))+1
    nP=ecMult(n,P,A,B,p)
    nj=nP[0],(-1*nP[-1])%p
    k=0
    h=0
    bstep=[0]
    gstep=[Q]

    for i in range (1,n):
        h=ecAdd(h,P,A,B,p)
        bstep.append(ecAdd(h,P,A,B,p)) #i*P
        k=ecAdd(k,nj,A,B,p)     
        gstep.append(ecAdd(Q,k,A,B,p)) #Q-njP
     
       
    coll=collision(bstep,gstep)
    if coll==None:
        return None
    else:
        return (coll [0]+ n*coll[1]+1)%q
    # Your code here
    
    
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


def ecMult(n,P,A,B,p):
    res=0
    if n==0:
        return 0
    if n==2:
        res=ecAdd(P,P,A,B,p)
        return res
    k=P
    l=n
    if k==0:
        return 0
    
    while l>0:
        if l%2==1:
            res=ecAdd(res,k,A,B,p)
        k=ecAdd(k,k,A,B,p)
        l=l//2
    return res
    # Your code here
    
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
def ecSubtract(P,Q,A,B,p): #works for making values from scratch but not for recursive methods bc of way it is written
    if Q==0:
        return P
    if P==0:
        return Q
    x1=P[0]
    y1=P[1]
    x2=Q[0]
    y2=(-1*Q[1])%p
    
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



     
                  
                     
