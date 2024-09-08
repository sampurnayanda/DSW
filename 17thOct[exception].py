#!/usr/bin/env python
# coding: utf-8

# In[5]:


def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisonError:
        return "Zero Divison Occurs"
    except:
        return "either of the arguement you have given non-integer value"


# In[2]:


divide(10,0)


# In[4]:


divide(10,0)


# In[6]:


x=input('enter the first value:')
y=input('enter the second value:')
divide(x,y)


# In[7]:


divide(x,y)


# In[8]:


x=input('enter the first value:')
y=input('enter the second value:')
divide(x,y)


# In[ ]:




