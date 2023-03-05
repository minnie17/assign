#!/usr/bin/env python
# coding: utf-8

# In[25]:


from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


# In[32]:


data = pd.read_excel(r"C:\Users\Jalaluddin Shaik\OneDrive\Desktop\scoccer.xlsx", index_col=1)


# In[42]:


data.head()
data = data.head()
data


# In[50]:


import pandas as pd
import matplotlib.pyplot as plt

# import the data and clean it
data = pd.read_excel(r"C:\Users\Jalaluddin Shaik\OneDrive\Desktop\scoccer.xlsx")
data = data[['name', 'age', 'nationality', 'club']]
data['age'] = pd.to_numeric(data['age'], errors='coerce')

# Calculate the overall average age
avg_age = data['age'].mean()

# Group the data by club and calculate the average age for each group
grouped_data = data.groupby('club')['age'].mean()

# Create a horizontal bar plot of the average ages by club
grouped_data.plot(kind='barh')
plt.axvline(avg_age, color='red', linestyle='--')
plt.xlabel('Average Age')
plt.ylabel('club')
plt.title('Average Age of Football Players by club')
plt.show()


# 
