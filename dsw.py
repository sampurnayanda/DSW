#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add(a,b):
    return a+b
n1=10
n2=20
print(add(n1,n2))


# In[ ]:


def add(a,b):
    return a+b
def subtract(a,b):
    if(a>b):
        return a-b
    else:
        return b-a
def multiply(a,b):
    return a*b
def divide(a,b):
    while(b!=0):
        return a/b
def getpower(a,b):
    P=1
    for i in range(1, b+1):
        P=P*a
        return P
def getIntegerDivison(a,b):
    return a//b
def getModularDivison(a,b):
    return a%b
def getSquareRoot(n):
    math.sqrt(n)
def getQuadraticRoots(a,b,c):
    d = b * b - 4 * a * c 
    val = math.sqrt(abs(d)) 
    if d > 0: 
        print("real and different roots") 
        r1=((-b + val)/(2 * a)) 
        r2=((-b - val)/(2 * a)) 
        return(r1,r2)
     
    elif d == 0: 
        print("real and same roots") 
        r=(-b / (2 * a)) 
        return(r)
    else:
        print("Complex Roots") 
        r1=(- b / (2 * a), + i, val) 
        r2=(- b / (2 * a), - i, val) 
        return(r1,r2)
def getMean(list1):
    s=0;
    for i in list1:
        s=s+i
    return(s/len(list1))    
def getmedian(list1):
    list1.sort()
    l=len(list1)
    if l%2==0:
        return((list1[l//2 - 1]+list1[l//2])/2)
    else:
         return(list1[l//2])
def getMode(d1):
    m=0
    t=0
    for i in d1:
        if m<d1[i]:
            m=d1[i]
            t=i;

            return t    
def main():       
    a1=int(input("enter a number"))
    b1=int(input("enter another number"))
    c1=int(input("enter another number"))
    n1=int(input("enter a number for square root"))
    list2=list(input("enter a list"))
    
    print(add(a1,b1))
    print(subtract(a1,b1))
    print(multiply(a1,b1))
    print(divide(a1,b1))
    print(getPower(a1,b1))
    print(getIntegerDivison(a1,b1))
    print(getModularDivison(a1,b1))
    print(getSquareRoot(a1,b1))
    print(getQuadraticRoots(a1,b1))
    print(getMean(a1,b1))
    print(getmedian(a1,b1))
    print(getMode(a1,b1))
    
main()    


# In[28]:


def getMode(d1):
    m=0
    t=0
    for i in d1:
        if m<d1[i]:
            m=d1[i]
            t=i;
        return t    
d2={1:10,2:7,3:3}
print(getMode(d2))


# In[24]:


def getmedian(list1):
    list1.sort()
    l=len(list1)
    if l%2==0:
        return((list1[l//2 - 1]+list1[l//2])/2)
    else:
         return(list1[l//2])
        
list2=list(input("enter a list"))
print(getmedian(list2))


# In[ ]:





# In[ ]:




