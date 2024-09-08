#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=eval("15*20-15/30")


# In[2]:


x


# In[3]:


y=eval(input("enter an expression"))


# In[4]:


y


# In[7]:


z=eval(input("enter an expression"))


# In[6]:


y


# In[8]:


z


# In[12]:


z=eval(input("enter an expression"))


# In[10]:


z


# In[19]:


import math
def SquareRoots(a,b,c):
    d=math.sqrt(b*b-4*a*c)
    if(d>0):
        r1=(-b+d)/2*a
        r2=(-b-d)/2*a
        return(r1,r2)
    elif(d==0):
        r=(-b+d)/2*a
        return r
    elif(d<0):
        r1=a+ib
        r2=a-ib
        return(r1,r2)
 
a1=int(input("enter a"))
b1=int(input("enter b"))
c1=int(input("enter c"))
print(SquareRoots(a1,b1,c1))

    
        


# In[1]:


a1=int(input("enter a"))
b1=int(input("enter b"))
c1=int(input("enter c"))


# In[4]:


a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))

r1=(-b+pow(pow(b,2)-4*a*c,1/2))/2*a
r1


# In[6]:


print("1 ")
print("1 2 ")
print("1 2 3 ")
print("1 2 3 4 ")


# In[8]:


def pattern():
    print("1 ")
    print("1 2 ")
    print("1 2 3 ")
    print("1 2 3 4 ")
    
pattern()    


# In[21]:


def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

n1=int(input("enter the no. of rows"))       
pattern(n1)        


# In[26]:


def pattern(n):
    k = 2*n - 2
 
    
    for i in range(0, n):

        for j in range(0, k):
            print(end=" ")
     
        k = k - 2

        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

n1=int(input("enter the no. of rows"))       
pattern(n1)        


# In[30]:


def pattern(n):
    for i in range(n+1,1):
        for j in range(1,i+1):
            print("#",end=" ")
        print()    

n1=int(input("enter the no. of rows"))       
pattern(n1)        


# In[33]:


def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(" ",end=" ")
        for k in range(i,n+1):
            print("*",end=" ")
        print()
        
n1=int(input("no.of rows"))
pattern(n1)


# In[38]:


lst=[]
n=int(input("enter the no. of list going to be stored:"))
n1=int(input("enter the no. of element in each list"))
for i in range (1,n+1):
    lst.append([])
    for j in range(1,n1+1):
        lst[i].append(j)
        
print(lst)        


# ##### List = []
# for i in range(3):
#     templist=[]
#     for j in range(5):
#         x=input("enter element")
#         templist.append(x)
#     List.append(templist)
# print(List)    

# #### list1=int(input("enter a list"))

# In[ ]:




