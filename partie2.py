# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:22:46 2023

@author: khali
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# lecture
df = pd.read_csv('./datas/stats.csv')
print(df)
#valeur simple
moyenneSalaire= df['salary'].mean()
sommeSalaire=df['salary'].sum()
maxSalaire=df['salary'].max()
minSalaire=df['salary'].min()
nbSalaire=df['salary'].count()
medSalaire=df['salary'].median()
stdSalaire=df['salary'].std()
varSalaire=df['salary'].var()
#groupe by filtres
gbsomme=df.groupby(['country']).sum()
gbcount=df.groupby(['country']).count()
print('moyenne des salaires'+str(moyenneSalaire))
print('somme des salaires'+str(sommeSalaire))
print('salaires min'+str(minSalaire))
print('salaires max'+str(maxSalaire))
print('salaires médianne'+str(medSalaire))
print('std des salaires'+str(stdSalaire))
print('variance des salaires'+str(varSalaire))
print('somme des valeurs par pays'+str(gbsomme))
print('occurence des valeurs par pays'+str(gbcount))