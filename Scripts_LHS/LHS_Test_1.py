## This script creates a matrix with 104 values for each technology imposed by the LHS
## Author : Anthony Devresse


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from smt.sampling_methods import LHS



df = pd.read_csv(r'D:\Mémoire\LHS_Test\EnergyScope\output_pareto10000\technologies.txt',sep = "\t",header = None,skiprows = [0,1],index_col = 0)


limits = np.zeros((len(df),2))

for i in range (0,len(df)):
    for j in range (0,2):
         if j==0 : #Lower bound
             limits[i][j] = 0.1*df[2][i]
         if j==1 : #Upper bound
            if df[2][i] == 0 :
                if df[3][i] == 1000 or df[3][i] == 10000 : 
                    limits[i][j] = 0.01*df[3][i] # if f = 1e3 or 1e4 takes 1% of f_max so 10 or 100 for DHN_Seasonal_Storage
                else :
                    limits[i][j] = df[3][i] #Otherwise just take f_max
            elif (1.9*df[2][i]>df[3][i]) :
                limits[i][j] = df[3][i] #if upper bound > f_max put f_max as upper bound
            else :
                limits[i][j] = 1.9*df[2][i]
    



sampling = LHS(xlimits=limits) #LHS with the bounds
num = 500
x = sampling(num) #x is the matrice with the number num of random designs


# plt.plot(x[:,4],x[:,5],'.')
# plt.show()

# print(x[0][1])
# print(x.shape)


