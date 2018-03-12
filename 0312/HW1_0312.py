
# coding: utf-8

# # HW1 0312

# In[29]:


import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding = "big5"
soup = BeautifulSoup(response.text, 'html.parser')
s = soup.text


# In[40]:


s[:]=0


# In[33]:


s[0:]


# In[34]:


s[:10]


# In[35]:


s[2:50]


# In[36]:


s[0:100:2]


# In[37]:


s[:1200:4]


# In[38]:


s[22::4]


# In[39]:


s[::7]

