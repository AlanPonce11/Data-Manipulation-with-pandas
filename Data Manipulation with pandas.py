#!/usr/bin/env python
# coding: utf-8

# # Data Manipulation with pandas

# ## Course Description
# pandas is the world's most popular Python library, used for everything from data manipulation to data analysis. In this course, you'll learn how to manipulate DataFrames, as you extract, filter, and transform real-world datasets for analysis. Using pandas you’ll explore all the core data science concepts. Using real-world data, including Walmart sales figures and global temperature time series, you’ll learn how to import, clean, calculate statistics, and create visualizations—using pandas to add to the power of Python!
# 
# 

# ### Transforming DataFrames

# In[2]:


import pandas as pd 


# In[4]:


homelessness = pd.read_csv("homelessness.csv")
homelessness.head()


# In[5]:


# Print the head of the homelessness data
print(homelessness.head())

# Print information about `homelessness`
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())


# In[6]:


# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)


# In[9]:


# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])

# Print the top few rows
homelessness_reg_fam.head()


# In[ ]:


# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(ind_state.head())


# In[ ]:


# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)


# In[ ]:


# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)


# In[ ]:


# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of total that are individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]

# See the result
print(homelessness)


# In[ ]:


# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)


# ### Aggregating DataFrames

# In[ ]:





# In[ ]:




