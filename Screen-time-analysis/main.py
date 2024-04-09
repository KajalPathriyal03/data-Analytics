# print("Hello World");
#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[8]:


import plotly.express as px
import plotly.graph_objects as go


# In[10]:


data = pd.read_csv("Screentime-App-Details.csv")


# In[12]:


data.head()


# In[14]:


data.isnull().sum()


# In[15]:


data.describe()


# In[17]:


figure=px.bar(data_frame=data,
             x='Date',
             y='Usage',
             color='App',
            title='Usage')


# In[18]:


figure.show()


# In[20]:


figure=px.bar(data_frame=data,
             x='Date',
             y='Notifications',
             color='App',
             title='Notifications')
figure.show()


# In[21]:


figure=px.bar(data_frame=data,
             x='Date',
             y='Times opened',
             color='App',
             title='Times opened')
figure.show()


# In[28]:


figure=px.scatter(data_frame=data,
                 x='Notifications',
                 y='Usage',
                  trendline='ols',
                 size='Notifications',
                 title='Relationship between Notification and Usage')
figure.show()


# There’s a linear relationship between the number of notifications and the amount of usage. It means that more notifications result in more use of smartphones.
# 
# In this way we can analyze the screen time of a user

# In[ ]:




