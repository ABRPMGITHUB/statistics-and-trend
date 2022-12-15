# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 05:39:26 2022

@author: bhargavi
"""

#!/usr/bin/env python
# coding: utf-8

# #Importing library

# In[1]:


import pandas as pd 
import numpy as np 
from matplotlib import pyplot as mat_plot 


# #Make Function 

# In[2]:


def read_df(Data_filename):
    data_ag1=pd.read_csv(Data_filename,skiprows=4)
    #read datset & skip 4 rows 
    data_ag2=data_ag1.drop(['Indicator Code', 'Unnamed: 66', 'Country Code', 'Indicator Name'],axis=1) # unused columns drop
    data_ag3=data_ag2.set_index("Country Name")
    # transpose dataset 
    data_ag4=data_ag3.T
    data_ag4.reset_index(inplace=True)
    data_ag4.rename(columns = {'index':'Year'}, inplace = True) 
    return data_ag1,data_ag4


# In[3]:


Data_filename="/content/API_1_DS2_en_csv_v2_4550063.csv" # dataset path 
df_ag1,df_ag2=read_df(Data_filename)
df_ag1.head(8) # visualizaing dataset 


# In[4]:


df_ag2.head(8)#visualizaing dataset 
