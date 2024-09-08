#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def password(s):
    c=0
    c1=0
    c2=0
    c3=0
    if len(s)>=8:
        
        for i in s:
            if(i.isupper()):
                c+=1
            elif(i.islower()):
                c1+=1
            elif(i.isdigit()):
                c2+=1
            else:
                c3+=1
        if(c>=1 and c1>=1 and c2>=1 and c3>=1):
        print("good password")
        else:
        print("bad password")
    else:
        print("bad password")
        
                    
str1=input("enter the password")
password(str1)
        


# In[7]:


a=0
def one():
    b=0
    print(a)
    print(b)
def two():
    b=5
    print(a)
    print(b)
    
one()
two()
one()


# In[9]:


def abc():
    a=0
    b=0
    c=5
    c+=3
    b=c
    a=a+c+b
    return a,b,c


# In[14]:


x,y,z=abc()
print(x,y,z)
type(x)
type(y)
type(z)


# In[ ]:


x


# In[15]:


myFunc=lambda x: x**(1/2)


# In[16]:


x=myFunc(25)
x
type(x)


# In[17]:


print(x)


# In[18]:


x


# In[31]:


myFunc=lambda n,p: round(n**(1/p))
myFunc(25,2)


# In[21]:


myFunc(8,3)


# In[22]:


myFunc(16,4)


# In[37]:



def myTest(i,anyname):
             return anyname(i,3)
x=[8,27,64,125,216]
r=[]
for i in x:
    r.append(myTest(i,myFunc))    
r    


# In[27]:


round(1.99)


# In[28]:


round(1.99,1)


# In[30]:


round(1.993,2)


# In[ ]:




