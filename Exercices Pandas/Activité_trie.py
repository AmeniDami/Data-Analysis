# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:57:38 2023

@author: Ameni
"""

from pandas import DataFrame

valeurs = {'color': ['green','green','blue','blue','red','red','red','red'],
         'shape': ['rectangle','rectangle','square','rectangle','square','square','square','rectangle'],
         'price': [10,15,45,5,10,20,15,5]
         }
df = DataFrame(valeurs)
print('Table non triée:\n', df)

df2= df.sort_values(by=['color'])
print('Trie croissant selon le color:\n', df2)

df2= df.sort_values(by=['price'],ascending=False)
print('Trie décroissant selon le price:\n', df2)

df2= df.sort_values(by=['price','color'])
print('Trie croissant selon le prix et le color:\n', df2)

