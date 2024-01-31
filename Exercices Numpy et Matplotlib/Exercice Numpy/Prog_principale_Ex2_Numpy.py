# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:00:49 2023

@author: Ameni
"""

import Ex2_Numpy as an

N= 5
M = an.random_mat(N)
print("matrice M: ", M)

modified_matrix = an.build_m(M, N, n=3)
print("matrice modifié est : ",modified_matrix )

matrice_nettoyé = an.nettoyage(modified_matrix)
print("matrice nettoyé est : ",matrice_nettoyé )