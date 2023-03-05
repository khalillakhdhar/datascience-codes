# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:21:49 2023

@author: khali
"""
#lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# lecture
df = pd.read_csv('./datas/countries.csv')
print(df.head())
"""df.plot(x='Country',y='salary average',kind='bar')
plt.xlabel('Pays')
plt.ylabel('Salaires moyenne')
plt.title("Moyenne des salaires par pays")
"""
#partie 2
"""df.groupby('Country')['salary average'].mean().plot(kind='line')
plt.title("moyenne salaire par pays")
plt.xlabel("Pays")
plt.ylabel("Salaire moyenne")
plt.show()
"""
"""
salariesavg = df['salary average'].tolist()
countries = df['Country'].tolist()
working = df['Working Hours'].tolist()
workpower= df['working power'].tolist()
plt.bar(countries,salariesavg,width=0.25, label='moyenne des salaire', align='edge')
plt.bar(countries,working,width=-0.25, label='horaires du travail', align='edge')
plt.xlabel("Pays")
plt.ylabel("Travail")
plt.legend(loc='upper left')
plt.grid(True,linewidth=1 , linestyle="--")
plt.show()
"""
plt.plot(workpower, working, label = 'working hours and power',
color='g', marker='o', markerfacecolor='k',
linestyle='--', linewidth=3)
plt.xlabel('force de travail (en million)')
plt.ylabel('heures du travail ')
plt.title('Rapport horaire employées (Million)')
#plt.yticks([10000, 20000, 30000, 40000, 50000, 60000])
plt.show()