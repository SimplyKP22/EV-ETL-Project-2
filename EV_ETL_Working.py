#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
from sqlalchemy import create_engine


# In[2]:


# The path to our CSV files. These files contain the data that we exported.
file1 = "Resources/General_EV_data.csv"
file2 = "Resources/EV_Performance_data.csv"

# Read our data into pandas
general_df = pd.read_csv(file1)
performance_df = pd.read_csv(file2)


# In[3]:


# Display and explore data for general_df
general_df


# In[4]:


# Display and explore data for performance_df
performance_df


# ## Data Cleaning

# In[5]:


# split the 'Name' Column in the performance_df so we can have a 'Make' and 'Model' column as we do in the general_df.
# this will allow us to merge the databases based on the model
make_model = performance_df['Name'].str.split(' ', n=1, expand=True)


# In[6]:


make_model


# In[7]:


# merge the two new columns with the performance_df. This will enable us to later merge the performance and general dataframes
# perf_df = pd.concat([make_model, performance_df], axis=1)
perf_df = pd.merge(make_model, performance_df, left_index=True, right_index=True)


# In[8]:


perf_df


# In[9]:


# Remove the 'Name' column as that is no longer needed 
perf_df.drop('Name', axis=1, inplace=True)


# In[10]:


# Rename the 0 and 1 column to Make and Model. This will put the dataframe more in line with the general_df
perf_df = perf_df.rename(columns = {0: 'Make', 1: 'Model'})


# In[11]:


perf_df


# In[12]:


# Merge the perf_df and general_df
merge_df = pd.merge(general_df, perf_df, on='Model', how='outer')
merge_df


# In[13]:


# Display a list of the columns in the new database. This way we can identify the columns that we can remove to cleanp
# the dataframe and remove data the does not bring value to the end user
list(merge_df)


# In[14]:


# Remove the NA values
merge_df = merge_df.dropna()


# In[15]:


# Remove the columns that contain duplicate data and the columns that do not add value to the end user.
merge_df.drop(['Drive','AccelSec','TopSpeed_KmH','Range_Km','PriceEuro','Efficiency_WhKm','FastCharge_KmH','PlugType','Seats','Make','Efficiency','FastChargeSpeed'], axis=1, inplace=True)


# In[16]:


# Reset the index
merge_df.reset_index(drop=True)


# In[17]:


# List the columns to confirm we have the necessary data remains
list(merge_df)


# In[18]:


# Create a connection to postgresql database

protocol = 'postgresql'
username = 'postgres'
password = 'admin'
host = 'localhost'
port = 5432
database_name = 'EV_DB'
rds_connection_string = f'{protocol}://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(rds_connection_string)


# In[19]:


# Import dataframe to SQL database

merge_df.to_sql(name='etl_db', con=engine.connect(), if_exists='replace', index=False)


# In[20]:


# Confirm that table was created 
engine.table_names


# In[21]:


# Print the table where the connection was established

pd.read_sql('select * from etl_db', con=engine.connect())


# # TO DO for Saturday
# Drop AccelSec column and recreate SQL database with one less column.
# Clean up and pseudocode
# Download as .py file: File>Download as>Python (.py)
# Remove notebook file and replace with .py file
# Submit Project
# Finish Web Scraping HW
