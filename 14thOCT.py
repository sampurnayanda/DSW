#!/usr/bin/env python
# coding: utf-8

# In[27]:


def pattern(n):
    for i in range(1,11):
        print(i,end=" ")
    print(end='\n')    
    for i in range(1,n+1):
        for j in range(1,n+1):
            k=i*j
            print(k,end=" ")    
        print()
        
n1=int(input("enter row"))
pattern(n1)
        


# In[40]:


import math
def armstrong(n):
    num=str(n)
    l=len(num)
    s=0
    m=n
    while(n>0):
        r=n%10
        s=s+math.pow(r,l)
        n=n//10
    if s==m:
        print("armstrong")
    else:
        print("not")

n1=int(input("enter a number"))
armstrong(n1)


# In[47]:


def fibonacci():
    n1=0
    n2=1
    x=n2
    c=0
    print(n1,end=" ")
    print(n2,end=" ")
    while(c<9):
        c=c+1
        print(x,end=" ")
        n1=n2
        n2=x
        x=n1+n2
    print() 

fibonacci()


# In[4]:


def password(str):
    for i in str:
        if(len(str)>8):
            if(ord(i)>=65 and ord(i)<=90):
                if(ord(i)>=97 and ord(i)<=122):
                    if(ord(i)>=48 and ord(i)<=57):
                        print("good password")
                        
            
        
                        
            
str1=input("enter the password")            
password(str1)            


# In[21]:


def password(s):
    c=0
    c1=0
    c2=0
    c3=0
    for i in s:
        if(len(s)>=8):
            if(i.isupper()):
                c+=1
            elif(i.islower()):
                c1+=1
            elif(i.isdigit()):
                c2+=1
            else:
                c3+=1
    if(c>=1 and c1>=1 and c2>=1 and c3>=1):
        return("good password")
    else:
        return("bad password")
                    
str1=input("enter the password")
password(str1)
        


# In[ ]:





# In[ ]:




