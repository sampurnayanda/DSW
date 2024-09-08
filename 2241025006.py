#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("enter a list")
L[]=int(input("enter 10 numbers"))


# In[13]:


L=[]
L=[17,20,40,33,50,70,87,90,32]
i=0

while(i<10):
     if(L[i]%2==0):
        L1=[]
        L1=L1+L
     else:
        L2=[]
        L2=L2+L

print("even no.s"+L1)
print("odd no.s"+L2)


# In[18]:


L=[]
L=[17,20,40,33,50,70,87,90,32]
i=0

while(i<10):
    if(L[i]%2==0):
            L1=[]
            L1=L1+L
    else:
            L2=[]
            L2=L2+L

print("even no.s"+L1)
print("odd no.s"+L2)


# In[21]:


L=[]
L=[17,20,40,33,50,70,87,90,32]
i=0

while(i<10):
    if(L[i]%2==0):
            L1=[]
            L1=L1+L
    else:
            L2=[]
            L2=L2+L

print("even no.s"+L1)
print("odd no.s"+L2)


# In[36]:


list=[]
list2=[]
list3=[]
n=int(input("enter the size of the list"))
for i in range (0,n):
    j=int(input())
    list.append(j)
print(list)
for i in list:
    if(i%2==0):
        list2.append(i)
    else:
        list3.append(i)
        
print(list2)
print(list3)


# In[33]:


list=[]
sum=0
pro=1
n=int(input("enter size"))
for i in range (0,n):
    j=int(input())
    list.append(j)
    
print(list)
for i in list:
    sum=sum+i
    pro=pro*i
print(sum)
print(pro)


# In[47]:


lst=[]
list1=[]
list2=[]
n=int(input("enter size"))
for i in range (0,n):
    j=input()
    list.append(j)
print(lst)
for i in list:
    if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E'or i=='O' or i=='I'or i=='U' ):
        list1=list1.append(i)
    else:
        list2=list2.append(i)
print(list1)
print(list2)


# In[46]:


tt=(['first','second',2067,100,[1,2,3]])
type(x)
tt[4][1]="modified"
print(tt)


# In[50]:


l=(2241025006,'sampurna','cse',9876543210,9.1)
l1=[]
for i in range (0,4):
    
    roll=int(input("enter your roll no."))
    name=input("enter your name")
    branch=input("enter your branch")
    mob=int(input("enter your mobile number"))
    cgpa=int(input("enter your cgpa"))
    t1=(roll,name,branch,mob,cgpa)


# In[ ]:




