#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


f0=pd.read_csv("Downloads/MiniProject/F0.csv")
f0


# In[3]:


f1=pd.read_csv("Downloads/MiniProject/F1.csv")
f2=pd.read_csv("Downloads/MiniProject/F2.csv")
f3=pd.read_csv("Downloads/MiniProject/F3.csv")
f4=pd.read_csv("Downloads/MiniProject/F4.csv")
f5=pd.read_csv("Downloads/MiniProject/F5.csv")
f6=pd.read_csv("Downloads/MiniProject/F6.csv")
f7=pd.read_csv("Downloads/MiniProject/F7.csv")
f8=pd.read_csv("Downloads/MiniProject/F8.csv")
print("F1\n",f1)
print("F2\n",f2)
print("F3\n",f3)
print("F4\n",f4)
print("F5\n",f5)
print("F6\n",f6)
print("F7\n",f7)
print("F8\n",f8)


# In[5]:


mca=pd.read_csv("Downloads/MiniProject/Monte Carlo_200.csv")
mca.head(12)


# In[6]:


mca.columns


# In[7]:


df = pd.read_csv("Downloads/MiniProject/Monte Carlo_200.csv")
df.columns = df.columns.str.strip()
df_selected = df.iloc[:, 1:]
print(df_selected.head())


# In[9]:


#  real and imaginary parts 
real_columns = [col for col in df.columns if 'V(V0)' in col and 'IMG' not in col]
imaginary_columns = [col for col in df.columns if 'V(V0)' in col and 'IMG' in col]


# In[10]:


# real values
df_real = df[['Frequency'] + real_columns]
df_real.plot(x='Frequency', y=real_columns, figsize=(10, 6))
plt.xlabel('Frequency')
plt.ylabel('Real Amplitude')
plt.title('Real Values')

plt.show()


# In[11]:


# imaginary values
df_imaginary = df[['Frequency'] + imaginary_columns]
df_imaginary.plot(x='Frequency', y=imaginary_columns, figsize=(10, 6))
plt.xlabel('Frequency')
plt.ylabel('Imaginary Amplitude')
plt.title('Imaginary Values')

plt.show()


# In[ ]:




