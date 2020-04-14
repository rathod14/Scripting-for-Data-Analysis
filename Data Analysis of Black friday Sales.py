#!/usr/bin/env python
# coding: utf-8

# In[37]:


#importing packages
import pandas as pd
import numpy as np


# In[39]:


#importing csv as a pandas dataset
df = pd.read_csv("black_friday.csv")


# In[40]:


#displaying first 5 rows
df.head(5)


# In[41]:


#rename the columns names
df = df.rename(columns={'Product_Category_1': 'Cloths'})
df = df.rename(columns={'Product_Category_2': 'Electronics'})
df=df.rename(columns={'Product_Category_3': 'Home Goods'})
#display all columns names
df.columns


# In[42]:


#display number of rows and columns
#the dataset contains 24k rows and 11 columns
df.shape
#the dataset is too large for this project I will just select the random sample of the dataset
new_df =df.sample(n=2000,replace=True)
new_df.shape


# In[43]:


#dislay concise summary of dataset
new_df.info()


# In[45]:


#Data Cleaning
#handling missing values
#Product Category Cloths and Home goods have large number of null values
new_df.isnull().sum()


# In[46]:


#filling the Null values with fillna() and method backfill
new_df = new_df.fillna(method = 'backfill')
#checking whether all the null values are filled
new_df.isnull().sum()
#HomeGoods column still have null values we will drop the rows
new_df = new_df.dropna()
#again checking whether all the null values are filled
new_df.isnull().sum()


# In[64]:


#Question 1
#Which customer has the largest purchase on black friday? What's their gender and age?

#bf['Gender'].value_counts()
#bf['Purchase'].max()
#bf['Age'].value_counts()

bfmax = new_df.loc[new_df['Purchase'].idxmax()]

print("The customer with the largest purchase on Black Friday is", bfmax[2],"and age group",bfmax[3], 
      ", spending a total of ${:,.2f}".format(bfmax[11]))

bfmax_export = bfmax.to_csv ('BlackFridayMaxPurchase.csv', index= None, header=True)


# In[65]:


#Question 2
#What was the average purchase within each age group?

#df2 = {n: rows[1] for n, rows in enumerate(bf.groupby('Gender'))}
#print(df2[1])

bfage = new_df.groupby(['Age'], as_index=False).mean().groupby('Age').mean()

#print("On average, people within", bfage.index[0],"age group spent:",bfage['Purchase'][0])

count = 0
for line in bfage:
    print ("On average, people within", bfage.index[count],"age group spent ${:,.2f} on Black Friday.".format(bfage['Purchase'][count]))
    count += 1
    
    
bfage_export = bfage.to_csv ('BlackFridayAgeAvg.csv', index= None, header=True)


# In[ ]:




