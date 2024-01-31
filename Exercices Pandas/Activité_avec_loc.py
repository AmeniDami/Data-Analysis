# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:34:30 2023

@author: Ameni
"""
from pandas import DataFrame 
from numpy import nan 
#Creation du DataFrame
Boxes = {'color': ['green','green','blue','blue','red','red','red','red'],
         'shape': ['rectangle','rectangle','square','rectangle','square','square','square','rectangle'],
         'price': [10,15,nan,5,10,nan,15,5]
         }
#print(Boxes)
df = DataFrame(Boxes, columns= ['color','shape','price'])
print(df)

#1 Appliquez un filtrage filtrage par colonnes colonnes Color, Shape
df.loc[:,['color','shape']]

#Sélectionnez seulement les lignes dont:

#2) a) Color=Green (affichez seulement les colonnes Shape et Price en résultat)
df.loc[df['color']=='green',['price','shape']]

#b) Price < 15
df1= df.loc[df['price']<15]
print("question b\n", df1)

#c) Color =Green et Shape = Rectangle (affichezseulement la colonne Price en résultat)
df.loc[(df['color']=='green')& (df['shape']=='rectangle'),['price']]

#d)Color est dans cette Liste [‘Red’, ‘Blue’] 
l=['red','blue']
df.loc[df['color'].isin(l)]

#e) Les valeurs de la colonne Price ne sont pas nulles.
df.loc[df['price'].notnull()]

#f) Les valeurs de la colonne Price sont nulles (affichezseulement les colonnes Color et Shape en résultat)
df.loc[df['price'].isnull(),['color','shape'] ]