# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:40:57 2023

@author: Ameni
"""
import numpy as np 
import random  

# 1ére question

def random_mat(N):
    M = 5 + 5 * np.random.randn(N,2)
    M[:,1] = 2 * M[:,0]
    
    return M

def build_m(M, N, n=3):
    
    for i in range(n+1):
        
        indexL = np.random.randint(N-1)
        indexC = np.random.randint(1)
        M[indexL , indexC] = np.nan
        
    return M

def nettoyage(M):
    
    medcolonnes = np.nanmedian(M, axis = 0)
    print("medcolonnes : ",medcolonnes)
    for l in range(M.shape[0]):
        for c in range(M.shape[1]):
            if np.isnan(M[l,c]):
                M[l,c] = medcolonnes[c]
            
    return M
    
#PP
mat = random_mat(6)
print("matrice M= ",mat)
mat = build_m(mat, 6)
print("matrice_nan M= ",mat)
mat = nettoyage(mat)
print("matrice_median M= ",mat)
