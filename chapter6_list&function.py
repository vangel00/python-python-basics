#!/usr/bin/env python
# coding: utf-8

# In[19]:


st = [1,300,5,7,9]
num = len(st)
print(num)
print("minValue: ", min(st))
print("maxValue: ", max(st))

st.remove(300) #3을 찾아서 제거하는 부분.
st

st.append(500)
st

st.extend([600, 700])
st


# In[30]:


st.insert(2, 700)
st

st.clear()
st


# In[31]:


st.append(100)
st.append(200)
st
print(st)
print(type(st))


# In[32]:


st.pop(0)
st

st.remove(200)
st


# In[39]:


st = [1,300,5,7,9, 1,1,1,1,]
print(st)

st.count(1)
st.index(300)


# In[42]:


st = [ ]
st.append(1)
st.append(2)
st.append(3)
st

st.remove(1)
st.remove(2)
st.remove(3)
st


# In[45]:


st = [ ]
st.append(1)
st.append(2)
st.append(3)
st

st.pop(-1)
st.pop(-1)
st.pop(-1)
st


# In[3]:


st = [1,2,3,4]
st.clear()
st


# In[4]:


st = [1,2,3,4]
st[:] = []
st


# In[8]:


st = [1,2,3,4]
st.pop(-1)
st.pop(-1)
st.pop(-1)
st.pop(-1)
st


# In[15]:


st = []
for i in range(10):
    st.append(i + 1)

print(st)

for i in range(10):
    st.pop(-1)
    
st    


# In[16]:


st = [1,2]
st.extend([3,4,5])
st


# In[28]:


#      0    1
st = [100,200]
st[2: ] = [300,400,500,600,700]
#st.append([300,400,500,600,700])
print(st)

print(len(st))
print("가장 작은 값: ", min(st))
print("가장 큰 값: ", max(st))


# In[40]:


str = "Pythooooon"
print(len(str))
print(min(str))
print(max(str))

print(str.count("o"))
str.count("oo")
str.lower()
str.upper()
str


# In[49]:


str = " Hyun dae bin "
cp1 = str.lstrip()
cp2 = str.rstrip()
print(cp1)
print(cp2)
print(cp1 + cp2)
print(str.strip())


# In[51]:


str = "Hyun Dae Bin"
rps = str.replace("in", "un")
print(rps)
str


# In[66]:


str = "YoonSungWooBooHoo"
rps = str.replace("oo", "ee",3)
print(rps)
str


# In[73]:


str = "Hyun Dae Bin"
ret = str.split()
print(ret)
print(ret[0])
print(ret[1])
print(ret[2])


# In[79]:


str = "Hyun\r\nDae\r\nBin"
ret = str.split('\r\n') #Enter 역할 , escape 문자
print(ret)
print(ret[0])
print(ret[1])
print(ret[2])


# In[80]:


#연습문제 6-2

#1.
str = "The Espresso Spirit"
print(str.upper())
print(str.lower())
print(str)


# In[ ]:


def birth_only(pn):

    birth = pn.split("-")
    return birth[0]

p1 = "070609-2011xxx"
p1 = birth_only(p1)
print(p1) # 070609

p2 = "090716-1012xxx"
p2 = birth_only(p2)
print(p2) # 090716


# In[84]:


str = "Hyun is Dae is Bin is"
a = str.find("is")
print("index value: ", a)

b = str.rfind("is")
print("index value: ", b)

c = str.find("aa")
print("index value: ", c)


# In[106]:


#제어문자열(escape control character)
print('\b\b\b')
print('\\')
print("Hello" + '\t' + "world" + "\t" + "hyun dae bin")
print("hyun\ndae\nbin")
print("hyun\"dae")


# In[107]:


#del command
st = [1,2,3,4,5]
del st[:]
st


# In[109]:


#      0     1     2     3     4
st = [1000, 2000, 3000, 4000, 5000]
del st[3:] #부분 삭제 
st


# In[112]:


#      0     1     2     3     4
st = [1000, 2000, 3000, 4000, 5000]
del st[0] #부분 삭제 
st


# In[113]:


#      0     1     2     3     4
st = [1000, 2000, 3000, 4000, 5000]
del st[2] #부분 삭제 
st


# In[114]:


#      0     1     2     3     4
#            0     1      2    3
st = [1000, 2000, 3000, 4000, 5000]
del st[0] #부분 삭제 
del st[1]
st


# In[118]:


st = [1000, 2000, 3000, 4000, 5000]
print(st)

del st # sql에서 본다면 drop table st 
print(st) #NameError: name 'st' is not defined


# In[ ]:




