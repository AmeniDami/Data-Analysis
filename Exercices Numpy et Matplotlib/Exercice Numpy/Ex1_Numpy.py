# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:40:35 2023

@author: Ameni
"""
import numpy as np

def MAD(M, axis=None):
   mad = np.median(M, axis , keepdims= True)
   mad = np.abs(M - mad)
   mad = np.median(mad, axis)
   return mad


#PP
M = np.random.randint(10,100,size=(2,3))  # des valeurs entre 10 et 100 dans 2 ligne et 3 colonne

# calcluer MAD par ligne et colonne (axis = None)
mad1 = MAD(M, 0)
print("le MAD par ligne et colonne: ",mad1)

# calcluer MAD par  colonne (axis = 0)
mad2 = MAD(M, 0)
print("le MAD par colonne: ",mad2)

# calcluer MAD par ligne  (axis = 1)
mad3 = MAD(M, 1)
print("le MAD par ligne: ",mad3) 