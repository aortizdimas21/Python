import random

def makeQP(qbits,pbits):
    o=pbits
    m=qbits
    q=random.randint(pow(2,m-1),pow(2,m)-1)
    while isPrime(q)!= True:
        q=random.randint(pow(2,m-1),pow(2,m)-1)
    
    while True:
        b=random.randint(pow(2,(o-m)-1),pow(2,o-m)-1)
        p=q*b+1
        if isPrime(p)==True and p.bit_length()==o:
            break
                 
    return q,p 
  
       
        
           
           
            
            
           
       

# This function can be used to test whether your function is working.
# You can use this function as-is to make sure you have the right bit lengths.
# Once you provide an ``isPrime'' function, uncomment the last 8 lines, which will check that your output is prime.
def checkQP(q,p,qbits,pbits):
    if q.bit_length() == qbits:
        print('q has the correct number of bits.')
    else:
        print('q is %d bits long, but should be %d bits long'%(q.bit_length(),qbits))

    if p.bit_length() == pbits:
        print('p has the correct number of bits.')
    else:
        print('p is %d bits long, but should be %d bits long'%(p.bit_length(),pbits))

    if p%q == 1:
        print('p is 1 mod q, as desired.')
    else:
        print('p is not 1 mod q.')

import random
def isPrime(n):
    x=1
    p=n-1
    m=p
    if (n%2==0):
        return False
    if (n==2):
        return False
  
    while (m% 2 == 0): 
        m //= 2
    q=p//m
    k=1
    while k in (1,q):
        if (2**k)*m==p:
            break
        else: 
            k+=1
            
    a = random.randint(1,p)      
    b_0=pow(a,m,n)
        
    if b_0 ==1 or b_0==-1:
        return True  
    if (b_0 == n-1):  #moved this out of my while loop and seemed to fix the problem of it not running....()'s matter!!
            return True
        
    while (m!= n - 1): 
        b_0= (b_0 * b_0) % n 
        m *= 2
        if (b_0 == 1): 
            return False 
        if (b_0 == n-1): #checking to see if making it p was making the code not run - when I used p, it failed some tests 
            return True
        
    return False
        
        
        
#def isPrime(n): #naive approach
    #x=1
    #factors_n=[]
    #while x < n: 
        #if n%x ==0:
            #factors_n.append(x)
            #x+=1
        #else:
            #x+=1    
    #if len(factors_n)==1:
        #return True 
    #else:
         #return False      

   
    #Uncomment these lines once you provide an isPrime function.
    #

