
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
                     
          
                      
        
        
   

        
    #k=(((a2-a1)%m2)*(modinv(m1,m2)))%m2 #instead of m2, it is the last entry in m_list once I removed all the other entries
                    
    
    #a=(a1+m1*k)%(m1*m2) #instead of (m1*m2) it would be the product of every entry 
    # Your code here
    #return (a,m)

    
def crt(a1,m1,a2,m2):
    
    k=(((a2-a1)%m2)*(modinv(m1,m2)))%m2
                    
    a=(a1+m1*k)%(m1*m2)
    
    return a
      
    
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

