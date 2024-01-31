# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 01:22:21 2023

@author: Ameni
"""

import pandas as pd

valeurs = {'color': ['green','green','blue','blue','red','red','red','red'],
         'shape': ['rectangle','rectangle','square','rectangle','square','square','square','rectangle'],
         'price': [10,15,45,5,10,20,15,5]
         }
dataf = pd.DataFrame(valeurs)
print(dataf)

#exporation vers un nouveau fichier csv
dataf.to_csv('export1.csv')
dataf.to_csv('export2.csv',index=False,sep=';')

#exporation vers un nouveau fichier Excel:
dataf.to_excel('E:\Bureau\MRDS\Analyse de données pour entreprise\cours python exemple\mydata_exp.xlsx',sheet_name='data',header=True,index=False)