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


# #BAR GRAPH 

# #Plotting  figure for Rural population (% of total population)

# In[5]:


# set fount size (18)
mat_plot.rcParams.update({'font.size': 18}) 
df_bar1= df_ag1[df_ag1['Indicator Name'] == 'Rural population (% of total population)']
df_bar=df_bar1.pivot_table(index=['Country Name'], values=['1962', '1972', '1982', '1992', '2002']) 
mat_plot.rcParams['figure.figsize']=(21,7) 
df_bar1= df_bar.head(25)
df_bar1.plot.bar(color=['DarkOrange', 'Chartreuse', 'green',  'Blue', '#ff8080'])
mat_plot.xlabel('Country Name')

mat_plot.ylabel('Comparision')

mat_plot.title('Rural population (% of total population)') 
mat_plot.show();


# Rural data was gathered from a number of nations between 1962 and 2002, and a bar graph was created to represent this information. According to the chart, investigation has shown that the population distribution is most concentrated in Bangladesh, and that this concentration decreases as the year count rises.
# Another country has its people concentrated in the fewest feasible places.

# #Plotting figure for Arable land (% of land area)

# In[4]:


df_ag2.head(8)#visualizaing dataset 

# #BAR GRAPH 

# #Plotting  figure for Rural population (% of total population)

# In[5]:


# set fount size (18)
mat_plot.rcParams.update({'font.size': 18}) 
df_bar1= df_ag1[df_ag1['Indicator Name'] == 'Rural population (% of total population)']
df_bar=df_bar1.pivot_table(index=['Country Name'], values=['1962', '1972', '1982', '1992', '2002']) 
mat_plot.rcParams['figure.figsize']=(21,7) 
df_bar1= df_bar.head(25)
df_bar1.plot.bar(color=['DarkOrange', 'Chartreuse', 'green',  'Blue', '#ff8080'])
mat_plot.xlabel('Country Name')

mat_plot.ylabel('Comparision')

mat_plot.title('Rural population (% of total population)') 
mat_plot.show();


# Rural data was gathered from a number of nations between 1962 and 2002, and a bar graph was created to represent this information. According to the chart, investigation has shown that the population distribution is most concentrated in Bangladesh, and that this concentration decreases as the year count rises.
# Another country has its people concentrated in the fewest feasible places.

# #Plotting figure for Arable land (% of land area)
# In[6]:


df_bar2= df_ag1[df_ag1['Indicator Name'] == 'Arable land (% of land area)']
df_bar3=df_bar2.pivot_table(index=['Country Name'], values=['1962', '1972', '1982', '1992', '2002']) 
mat_plot.rcParams['figure.figsize']=(21,7) 
df_bar1= df_bar3.head(25)
df_bar1.plot.bar(color=['GoldenRod', 'red', 'green', 'Blue', 'DeepPink'])
mat_plot.xlabel('Country Name')
mat_plot.ylabel('Comparision')
mat_plot.title('Arable land (% of land area)') 
mat_plot.show();


# A bar graph shows arable land statistics from several nations between 1962 and 2002. These years' data were collected. Analyzing the figure shows that Bangladesh had the most people in 1972.
# The Bahamas, Belarus, Azerbaijan, and others have small populations, and data for certain years is missing.

# # Showing  correlation 

# In[7]:


dataset_corr = df_ag1[df_ag1['Indicator Name']=='Rural population']  
dataset_corr_1 = dataset_corr.pivot_table(index=['Country Name'], values = ['2001', '2006', '2020','2021'])  
dataset_corr_1.head(15)
