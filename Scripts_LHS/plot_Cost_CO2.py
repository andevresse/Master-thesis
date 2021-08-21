## This script plots the total cost versus the CO2 emissions
## Author : Anthony Devresse

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from LHS_Test_1 import num

n_design = num
n_pareto = 9

##Reference cost&gwp (Optimal design)##

df_ref_cost = pd.read_csv(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\cost_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
df_ref_cost_gwp = pd.read_csv(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref_gwp1000\cost_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
df_ref_gwp = pd.read_csv(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\gwp_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
df_ref_gwp_1000 = pd.read_csv(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref_gwp1000\gwp_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
#df c'est d'abord colonne puis ligne, à l'inverse d'un array


total_ref_cost = 0
total_ref_gwp = 0
total_ref_cost_gwp = 0
total_ref_gwp_gwp = 0

for i in range (0,len(df_ref_cost)) : #lines
    for j in range (1,4) : #columns
        total_ref_cost = total_ref_cost + df_ref_cost[j][i]
        total_ref_cost_gwp = total_ref_cost_gwp + df_ref_cost_gwp[j][i]
        
for i in range (0,len(df_ref_gwp)) :
    total_ref_gwp = total_ref_gwp + df_ref_gwp[1][i]
    total_ref_gwp_gwp = total_ref_gwp_gwp + df_ref_gwp_1000[1][i]
        
#print(total_ref_cost)
#print(total_ref_gwp)
    
    

##Suboptimums cost & gwp##


total_cost = np.zeros((n_design,1))
total_gwp = np.zeros((n_design,1))
for design in range (0,n_design) :
    try :
        df_cost = pd.read_csv(r'D:\Mémoire\LHS_Test\Results\Results_DD\Results_3\Results_max\output_'+str(design)+'\cost_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
        df_gwp = pd.read_csv(r'D:\Mémoire\LHS_Test\Results\Elec_1000_80\1000_LHS_ELEC_80\output'+str(design)+'\gwp_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
        
        for i in range (0,len(df_cost)) :
            for j in range (1,4) :
                total_cost[design] = total_cost[design] + df_cost[j][i]
            
        for i in range (0,len(df_gwp)) :
            total_gwp[design] = total_gwp[design] + df_gwp[1][i]

    except Exception as x :
        print(x)
    




#print(total_cost_plot)
##Pareto front##


pareto_cost = np.zeros(n_pareto)
pareto_gwp = np.zeros(n_pareto)

for pareto_design in range(0,n_pareto) :
    df_pareto_cost = pd.read_csv(r'D:\Mémoire\LHS_Test\EnergyScope\output_pareto'+str(10000*(pareto_design+1))+'\cost_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
    df_pareto_gwp = pd.read_csv(r'D:\Mémoire\LHS_Test\EnergyScope\output_pareto'+str(10000*(pareto_design+1))+'\gwp_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
    
    for i in range (0,len(df_pareto_cost)) :
        for j in range (1,4) :
            pareto_cost[pareto_design] = pareto_cost[pareto_design] + df_pareto_cost[j][i]
            
    for i in range (0,len(df_pareto_gwp)) :
        pareto_gwp[pareto_design] = pareto_gwp[pareto_design] + df_pareto_gwp[1][i]



            
# # plt.plot(total_ref_gwp/1000,total_ref_cost/1000,'.r')
# # plt.plot(total_gwp/1000,total_cost/1000,'.g')
# plt.plot(pareto_gwp/1000,pareto_cost/1000,'o-g')
# plt.xlabel('CO2 emissions [MTCO2eq]')
# plt.ylabel('Total cost [b€]')
# # matplotlib.rc('xtick', labelsize=40) 
# # matplotlib.rc('ytick', labelsize=40) 
# plt.show()

