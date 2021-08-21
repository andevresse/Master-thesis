## Generates full random ESTD technologies designs using LHS ##

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from smt.sampling_methods import LHS


df = pd.read_csv(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\technologies.txt',sep = "\t",header = None,skiprows = [0,1],index_col = 0)

limits = np.zeros((len(df),2))

for i in range (0,len(df)):
    for j in range (0,2):
         if j==0 : #Lower bound
             limits[i][j] = df[1][i] #Usually 0
         if j==1 : #Upper bound
             if df[3][i] == 1000 or df[3][i] == 10000 :
                 limits[i][j] = 0.02*df[3][i]
             else :
                 limits[i][j] = df[3][i]
                   
sampling = LHS(xlimits=limits) #LHS with the bounds
num = 1000
x = sampling(num) #x is the matrice with the number num of random designs

# print(x)
# print(x.shape)









