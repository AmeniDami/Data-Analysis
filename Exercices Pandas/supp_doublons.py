# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:05:13 2023

@author: Ameni
"""

from pandas import DataFrame

data = {'color': ['green','green','blue','blue','red','red','red','red'],
         'shape': ['rectangle','rectangle','square','rectangle','square','square','square','rectangle'],
         'price': [10,15,45,5,10,20,15,5]
         }
df = DataFrame(data, columns=['color','shape'])
print('DataFrame d\'origine:\n',df)

#supprimer les doublons
df2= DataFrame.drop_duplicates(df)
print('DataFrame après suppression des doublons des lignes:\n',df2)

#supprimer les doublons d'une seule colonne
#keep = 'last' ou 'first' 
df3= df.drop_duplicates(subset='color', keep='last')
print('DataFrame après suppression des doublons de la colonne color:\n',df3)

#verifier l'existance des doublons
df.duplicated().sum()