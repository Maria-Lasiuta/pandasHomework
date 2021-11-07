#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[15]:


teams = pd.read_csv('teams.csv',sep=',')


# In[23]:


teams.head(16)


# ### Who was a winner?

# In[40]:


teams.Team.loc[(teams.Goals == teams.Goals.max())]


# ### How many red cards there were and which team got it?

# In[75]:


teams['Red Cards'].sum()


# In[76]:


teams[teams['Red Cards'] == 1].Team


# ### Which teams have shooting accurancy more than 50 % and saves-to-shots ratio are more than 80%?

# In[53]:


teams[(teams['Shooting Accuracy'] > '50%') & (teams['Saves-to-shots ratio'] > '80%')]


# In[ ]:





# In[ ]:




