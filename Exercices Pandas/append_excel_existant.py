# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:19:39 2023

@author: Ameni
"""

import pandas as pd
from openpyxl import load_workbook

writer = pd.ExcelWriter('E:\Bureau\MRDS\Analyse de données pour entreprise\cours python exemple\mydata_exp.xlsx', engine='openpyxl')

writer.book = load_workbook('E:\Bureau\MRDS\Analyse de données pour entreprise\cours python exemple\mydata_exp.xlsx')

dataF = pd.read_csv ('export1.csv', sep=';',header = 0, encoding='Latin-1')

dataF.toexcel(writer, "Nombres", index=None)
writer.save()                            