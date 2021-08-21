## This script calls the distance_criteria function for every designs and give a matrix with all criterias
## Author : Anthony Devresse

import numpy as np
import pandas as pd
from Distance_Criteria import Price_Criteria



##Initialisation##
n_design = 14
n_pareto = 9
tech = np.zeros(n_design)
criterias = np.zeros(n_design)
total_cost = np.zeros(n_design)
total_gwp = np.zeros(n_design)
pareto_cost = np.zeros(n_pareto)
pareto_gwp = np.zeros(n_pareto)
ct_diff = np.zeros((n_design,n_design))
path_ref = r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_ref'
path = r'D:\Memoire\Other_Methods\MGA\results\MGA_Slack5_Tech\output'
path_pareto = r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_pareto'

##Pareto_Computation##
for i in range (0,n_pareto) :
    df_pareto_cost = np.genfromtxt(path_pareto + str((i+1)*10000) + '\\cost_breakdown.txt',dtype = 'float' , delimiter = '\t', skip_header = 1,usecols = (1,2,3))
    df_pareto_gwp = np.genfromtxt(path_pareto + str((i+1)*10000) + '\\cost_breakdown.txt',dtype = 'float', delimiter = '\t', skip_header = 1, usecols = (1))

    pareto_cost[i] = sum(sum(df_pareto_cost))
    pareto_gwp[i] = sum(df_pareto_gwp)


##Suboptimums computation##
for i in range (0,n_design) :

    try :
        techs = np.genfromtxt(path+str(i)+'\\technologies.txt',dtype = 'float', delimiter = '\t', skip_header = 2, usecols = 2)
        tech[i] = techs[1]
        criterias[i] = Price_Criteria(path_ref + '\\cost_breakdown.txt',path+str(i)+'\\cost_breakdown.txt',128)
        df_cost = np.genfromtxt(path + str(i) + '\\cost_breakdown.txt',dtype = 'float',delimiter = '\t', skip_header = 1, usecols = (1,2,3))
        df_gwp = np.genfromtxt(path + str(i) + '\\gwp_breakdown.txt',dtype = 'float',delimiter = '\t', skip_header = 1, usecols = (1))
        total_cost[i] = sum(sum(df_cost))
        total_gwp[i] = sum(df_gwp)
        
        

    except Exception as x :
        print(x)

    
## C_t computation between suboptimums ##
for i in range (0,n_design) :
    for j in range (0,n_design) :
        ct_diff[i][j] = Price_Criteria(path+str(i)+'\\cost_breakdown.txt', path+str(j)+'\\cost_breakdown.txt',128)

## Compute R criteria ##
R = 1 - np.divide((total_cost-pareto_cost[8]),criterias)
        




