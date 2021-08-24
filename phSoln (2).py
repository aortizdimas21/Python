# Make sure to include your code for the other three functions on this PSet here!Implement the Pohlig-Hellman algorithm. That #write a funciton ph(g,h,p) that solves
#the discrete logarithm problem 
#g^x ≡ h (mod p) under the assumption that p is a “weak”
#prime, in the sense that p − 1 factors into small prime factors. More specifically: you may
#assume that p − 1 factors into prime powers, all 16 bits or smaller, but p will be 64 bits in
#length.

import math


def ph(g,h,p):
    N=p-1
    q=ppFactor(N) #q is a list of the prime factors
    chinese_remainder=[]
  
    for n in q:
        g_i= pow(int(g),int(N)//n,p)
        h_i= pow(int(h),int(N)//n,p)
        jj=bsgsBoundedOrder(g_i,h_i,p,n)
        chinese_remainder.append([jj,n])
    a=crtList(chinese_remainder)
    
    return a[0]

   
   

def ppFactor(N):
    l=2
    pfactors=[]
    while (l*l<N):
        if N%l!=0:
            l=l+1
        else:
            N= N//l
            pfactors.append(l)
            
    if N>1:
        pfactors.append(N)
    q=pfactors   
    k=[(x,q.count(x)) for x in set(q)]    
    e=[x[1] for x in k]
    m=[(x[0]**x[1]) for x in k] 
    return  m
    
    
def primefactor(n):
    # Your code here. Find p and q with p,q > 1 and pq = n.
    # The order of p and q does not matter (e.g. if n=35, either 3,5 or 5,3 will be accepted)
    x=2
    prime_factors=[]
   
    while (x*x<n):
        if n%x:
            x=x+1
        else:
            n= n//x
            prime_factors.append(x)
    if n>1:
        prime_factors.append(n)        
    return prime_factors
          
                
    p=x
    q=n//p
            

    return p,q
    
def crtList(ls):
    a_list = [x[0] for x in ls] #making a list that only has the a's
    m_list=[x[1] for x in ls] #making a list that only has the m's
    
    #k=(((a_list[1]-a_list[0])%m_list[1])*(modinv(m_list[0],m_list[1])))%m_list[1]
    #a=(a_list[0]+m_list[0]*k)%(m_list[0]*m_list[1])
    #trying to make it so that I reduce it down to only two entries    
                    
    while len(a_list)>2:
        
        k_temp=(((a_list[1]-a_list[0])%m_list[1])*(modinv(m_list[0],m_list[1])))%m_list[1]
        a_temp=(a_list[0]+m_list[0]*k_temp)%(m_list[0]*m_list[1])
        m_temp=m_list[0]*m_list[1]
        a_list.remove(a_list[0])
        a_list.remove(a_list[0])
        a_list.append(a_temp)
        m_temp=m_list[0]*m_list[1]
        m_list.append(m_temp)
        m_list.remove(m_list[0])
        m_list.remove(m_list[0])
            
        if len(a_list)==2:
            break
                  
    k=(((a_list[1]-a_list[0])%m_list[1])*(modinv(m_list[0],m_list[1])))%m_list[1]
    a=(a_list[0]+m_list[0]*k)%(m_list[0]*m_list[1])  
    m=(m_list[1]*m_list[0])
                      
                                     
    return [a,m]              
 
    
def crt(a1,m1,a2,m2):
    
    k=(((a2-a1)%m2)*(modinv(m1,m2)))%m2  #k=(((a2-a1)%m2)*(modinv(m1,m2)))%m2 #instead of m2, it is the last entry in m_list once #I removed all the other entries
                    
    a=(a1+m1*k)%(m1*m2)#a=(a1+m1*k)%(m1*m2) #instead of (m1*m2) it would be the product of every entry 
    
    return a
     

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



def bsgsBoundedOrder(g,h,p,q):
    n=int(math.sqrt(q))+2
    gn=(pow(g,n,p))
    gninv=(modinv(gn,p))
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



     
                  
                    