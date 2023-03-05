#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[27]:


# Import the data and clean it
data = pd.read_excel(r"C:\Users\Jalaluddin Shaik\OneDrive\Desktop\scoccer.xlsx")


# In[28]:


data.head()
data = data.head()
data


# In[44]:


import pandas as pd
import matplotlib.pyplot as plt

# Import the data and clean it
data = pd.read_excel(r"C:\Users\Jalaluddin Shaik\OneDrive\Desktop\scoccer.xlsx")
data = data[['name', 'nationality', 'club']]
data['nationality'] = data['nationality'].str.upper()
data['club'] = data['club'].str.title()

# Group the data by nationality and club
grouped_data = data.groupby(['nationality', 'club'])['name'].count()

# Create a pie plot for each club
clubs = data['club'].unique()
for club in clubs:
    club_data = grouped_data.loc[:, club]
    club_data.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(f'Players by Nationality in {club}')
    plt.legend(labels=club_data.index, bbox_to_anchor =(1, 0.7), ncol = 2)
    plt.show()


# In[ ]:




