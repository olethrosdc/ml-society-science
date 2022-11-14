#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlalchemy


# In[2]:


engine = sqlalchemy.create_engine('sqlite:///../../data/COMPAS/compas.db')


# In[3]:


inspector = sqlalchemy.inspect(engine)


# In[4]:


inspector.get_table_names()


# In[5]:


cursor = engine.execute('SELECT * FROM compas LIMIT 10')


# In[6]:


cursor.fetchall()


# In[7]:


import pandas


# In[8]:


people = pandas.read_sql('people', engine)


# In[9]:


people.head()


# In[10]:


people.columns


# In[11]:


compas = pandas.read_sql('compas', engine)


# In[12]:


compas.head()


# In[13]:


compas.columns


# In[14]:


# In this setting we are interested mainly in whether the score $a$ we have given indidivuals is fair with respect to their sensitive attribute $z$ and their underlying quality $y$, i.e. whether or not recidivism occurred.
df = pandas.read_sql('''SELECT race,
                        is_violent_recid,
                        agency_text,
                        compas.decile_score FROM people JOIN compas ON person_id = people.id''', engine)


# In[15]:


df.head()


# In[16]:


all_counts = df.decile_score.value_counts()


# In[17]:


all_counts


# In[18]:


import matplotlib.pyplot as plt
import numpy as np
counts = df.groupby(['race']).decile_score.value_counts()
X = 1 + np.arange(10)
plt.bar(X, counts['Caucasian'][0:10] / sum(counts['Caucasian'][0:10]), width=0.3)
plt.bar(X+0.3, all_counts[0:10] / sum(all_counts[0:10]), width=0.3)
plt.bar(X+0.6, counts['African-American'][0:10] / sum(counts['African-American'][0:10]), width=0.3)
plt.legend(["Caucasian",  "General", "African-American"])
plt.xlabel("Score")
plt.savefig("Scores-by-race.pdf")


# In[19]:


counts = df.groupby(['race']).decile_score.value_counts()
AA = df[df['race']=="African-American"][["is_violent_recid", "decile_score"]]
CC = df[df['race']=="Caucasian"][["is_violent_recid", "decile_score"]]
GG = df[["is_violent_recid", "decile_score"]]


# In[ ]:





# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')
AA_recidivism = np.zeros(10)
CC_recidivism = np.zeros(10)
GG_recidivism = np.zeros(10)

for score in range(10):
    AA_recidivism[score] = np.mean(AA[AA["decile_score"]==score]["is_violent_recid"])
    CC_recidivism[score] = np.mean(CC[CC["decile_score"]==score]["is_violent_recid"])
    GG_recidivism[score] = np.mean(GG[GG["decile_score"]==score]["is_violent_recid"])
    

plt.plot(CC_recidivism)
plt.plot(GG_recidivism)
plt.plot(AA_recidivism)
plt.legend(["Caucasian",  "General", "African-American"])
plt.xlabel("Score")
plt.ylabel("Recidivism")
plt.savefig("calibration-compas.pdf")


# In[21]:


xcounts = df.groupby(['race', 'is_violent_recid']).decile_score.value_counts()
total_counts = df.groupby(['is_violent_recid']).decile_score.value_counts()
plt.bar(X, xcounts[('Caucasian',0)][0:10]/ sum(xcounts[('Caucasian',0)][0:10]), width=0.3)
plt.bar(X+0.3, total_counts[0][0:10]/ sum(total_counts[0][0:10]), width=0.3)
plt.bar(X+0.6, xcounts[('African-American',0)][0:10]/ sum(xcounts[('African-American',0)][0:10]), width=0.3)
plt.legend(["Caucasian",  "General", "African-American"])
plt.xlabel("Score")
plt.savefig("balance-non-recidivism-compas.pdf")


# In[22]:


xcounts = df.groupby(['race', 'is_violent_recid']).decile_score.value_counts()
plt.bar(X, xcounts[('Caucasian',1)][0:10]/ sum(xcounts[('Caucasian',1)][0:10]), width=0.3)
plt.bar(X+0.3, total_counts[1][0:10]/ sum(total_counts[1][0:10]), width=0.3)
plt.bar(X+0.6, xcounts[('African-American',1)][0:10]/ sum(xcounts[('African-American',1)][0:10]), width=0.3)
plt.legend(["Caucasian",  "General", "African-American"])
plt.xlabel("Score")
plt.savefig("balance-recidivism-compas.pdf")


# # Conditional independence
# 
# Here you should try and measure the conditional independence of your model $P$ with respect to the sensitive variable (race). In particular, we wish to calculate the dependence of the risk classification $a$ on race $z$ given their recidivism $y$:
# $$D(P(a \mid y, z), P(a \mid y)),$$
# which corresponds to the policy for selecting the scores being balanced. We also wish to calculate the dependence of recidivism $y$ on race $z$ given the risk $a$:
# $$D(P(y \mid a, z), P(y \mid a)),$$
# which corresponds to the policy for selecting the scores being calibrated.
# 
# Here $D$ is some appropriate distance or divergence between distributions. It is suggested to use one of:
# 
# 1. Total variation https://en.wikipedia.org/wiki/Total_variation_distance_of_probability_measures 
# 2. KL divergence https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence or 
# 3. $1/2$-Renyi-divergence https://en.wikipedia.org/wiki/R%C3%A9nyi_entropy#R%C3%A9nyi_divergence
# 
# Does the policy look fair with respect to either one of those metrics?
# 

# In[ ]:





# In[ ]:




