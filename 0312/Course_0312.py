
# coding: utf-8

# # in Course

# In[11]:


name='xyzasdfg'


# In[8]:


print(name.replace("x","A"))


# In[2]:


name


# In[7]:


print("A"+name[1:])


# In[9]:


name[:3]


# In[12]:


name[1:]


# In[13]:


name[1:4]


# In[14]:


name[::2]


# In[31]:


s = 'book, apple, hi'


# In[17]:


s1 = s.split(',')


# In[18]:


s1


# In[19]:


s1[0]


# In[20]:


s[:4]


# In[25]:


a = ['bbb', 'cccc']


# In[21]:


j = '*'


# In[33]:


j.join(a)


# In[34]:


poem = '''All that doth flow we cannot liquid name
or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''


# In[40]:


poem.rfind('the')


# In[39]:


poem.count('the')


# In[41]:


'中文'.isalnum()


# In[42]:


setup = 'a duck goes into a bar...'
setup.strip('.')


# In[43]:


setup.capitalize()


# In[44]:


setup.title()


# In[52]:


x = ['1', '2']
type(x)


# In[56]:


r = ('1', '2')
type(t)


# In[55]:


list("I love python.")


# In[57]:


list(r)


# In[58]:


x[-1]


# In[59]:


mL = [[['1', 'B10430016'], 'NTUST'], '0']


# In[60]:


mL[0][0][1]


# In[63]:


areas = ['Mon', 'Wenshan', 'Sun']


# In[64]:


areas.index('Wenshan')


# In[65]:


num=[100, 20, 30]


# In[66]:


sorted(num)


# In[67]:


num


# In[70]:


num.sort()
num


# In[71]:


b = num.copy()


# In[72]:


b


# In[73]:


num[0] = 1


# In[74]:


num


# In[75]:


b


# In[78]:


x, y ,z = num


# In[77]:




