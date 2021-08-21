## This script creates a matrix with 104 values for each technology imposed by the LHS
## Author : Anthony Devresse


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from smt.sampling_methods import LHS


# A changer en fonction de l'optimum !
gwp_limit = '40000'
filename = r'D:\Memoire\LHS_Test\EnergyScope\output_pareto' + gwp_limit + '\\technologies.txt'
n_LHS = 3

df = np.genfromtxt(filename,dtype = 'float' , delimiter = '\t', skip_header = 2,usecols = (1,2,3))
limits = np.zeros((len(df),2))



for i in range (0,len(df)):
    for j in range (0,2):
         if j==0 : #Lower bound
             limits[i][j] = 0.6*df[i][1]
         if j==1 : #Upper bound
            if df[i][1] == 0 :
                if df[i][2] == 1000 or df[i][2] == 10000 : 
                    limits[i][j] = 0.01*df[i][2] # if f = 1e3 or 1e4 takes 1% of f_max so 10 or 100 for DHN_Seasonal_Storage
                else :
                    limits[i][j] = df[i][2] #Otherwise just take f_max
            elif (1.9*df[i][1]>df[i][2]) :
                limits[i][j] = df[i][2] #if upper bound > f_max put f_max as upper bound
            else :
                limits[i][j] = 1.4*df[i][1]
    



sampling = LHS(xlimits=limits) #LHS with the bounds
num = 500
x = sampling(num) #x is the matrice with the number num of random designs

# plt.plot(x[:,1],x[:,6],'.')
# plt.show()

# print(x[0][1])
# print(x.shape)



