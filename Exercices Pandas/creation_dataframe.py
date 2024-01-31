# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 00:33:25 2023

@author: Ameni
"""
import pandas as pd
import numpy as np


#create a dataframe a partir d'un dictionnaire of series
d={'Name': pd.Series(['ameni','farah','manel','maysa']),
  'Age': pd.Series([22,25,50,48,15]),
  'Rating':pd.Series([4.23,8.25,6.32,4.6,7.56])}
df= pd.DataFrame(d)
print(df)

#create dataframe a partir d'un dictionnaire
dict = {'color': ['green','green','blue','blue','red','red','red','red'],
         'shape': ['rectangle','rectangle','square','rectangle','square','square','square','rectangle'],
         'price': [10,15,45,5,10,20,15,5]
         }
mydata = pd.DataFrame(dict)
print(mydata)

#create dataframe a partir d'un ndarray 2D
x = np.array([[10,20,30],[100,200,300],[1000,2000,3000]])
dataf = pd.DataFrame(x, columns=['un','deux','trois'])
print(dataf)