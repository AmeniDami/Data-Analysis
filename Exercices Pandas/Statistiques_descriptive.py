# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:33:17 2023

@author: Ameni
"""

import pandas as pd
from numpy import around
df=pd.read_csv('salaries.csv',header=0,sep=';')
print(df)

#block1- des stat simples
mean1 = df['Salary'].mean()
print('Moyenne des salaires:',around(mean1,2))

sum1 = df['Salary'].sum()
print('la sommes des salaires:',sum1)

max1 = df['Salary'].max()
print('Max des salaires:',max1)

min1 = df['Salary'].min()
print('Min des salaires:',min1)

print('Nombres des salaries: ',len(df))

median1 = df['Salary'].median()
print('Median des salaries: ',around(median1,2))

std1 = df['Salary'].std()
print('Ecart-type des salaries: ',around(std1,2))

var1 = df['Salary'].var()
print('Variance des salaries: ',around(var1,2))

#bloc2 - group by

groupby_sum1 = df.groupby(['Country'])['Salary'].sum()
print('Sommes des salaries par pays: \n', groupby_sum1)

groupby_count1 = df.groupby(['Country'])['Salary'].count()
print('Nombres des salaries par pays: \n', groupby_count1)

#Groupby sur 2 ou plusieurs colonnes
groupby_count1 = df.groupby(['Country','Age'])['Salary'].mean().round(decimals=2)
print('La moyennes  des salaries par pays et par age: \n', groupby_count1)

stat= df['Salary'].describe()
print('Statistique descriptive:\n', stat)

#inputez(remplacez) les valeurs manquantes de la colonne "salary" par la médiane des salaires
median=df['Salary'].median()
df.loc[df['Salary'].isnull(),'Salary']=median
print(df)

















