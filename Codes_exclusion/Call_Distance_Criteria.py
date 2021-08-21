## This script calls the distance_criteria function for every designs and give a matrix with all criterias
## Author : Anthony Devresse

import numpy as np
import pandas as pd
from Distance_Criteria import Price_Criteria,Emiss_Criteria


nFr = 500
nDD = 500

EmissCrit_Fr_100 = np.zeros(nFr)
criterias_Fr_100 = np.zeros(nFr)
# criterias_Fr_50 = np.zeros(nFr)
# criterias_Fr_40 = np.zeros(nFr)
# criterias_Fr_30 = np.zeros(nFr)
# criterias_Fr_10 = np.zeros(nFr)

EmissCrit_DD_100 = np.zeros(nDD)
criterias_DD_100 = np.zeros(nDD)
# criterias_DD_50 = np.zeros(nDD)
# criterias_DD_40 = np.zeros(nDD)
# criterias_DD_30 = np.zeros(nDD)
# criterias_DD_10 = np.zeros(nDD)

total_cost_Fr_100 = np.zeros(nFr)
total_emis_Fr_100 = np.zeros(nFr)
# total_cost_Fr_50 = np.zeros(nFr)
# total_cost_Fr_40 = np.zeros(nFr)
# total_cost_Fr_30 = np.zeros(nFr)
# total_cost_Fr_10 = np.zeros(nFr)

total_cost_DD_100 = np.zeros(nDD)
total_emis_DD_100 = np.zeros(nDD)
# total_cost_DD_50 = np.zeros(nDD)
# total_cost_DD_40 = np.zeros(nDD)
# total_cost_DD_30 = np.zeros(nDD)
# total_cost_DD_10 = np.zeros(nDD)

for i in range (0,nDD) :
    criterias_DD_100[i] = Price_Criteria(r'Ref\cost_breakdown.txt',r'Results_sans_nuk\Results_max\output_'+str(i+1)+'\cost_breakdown.txt',128)
    EmissCrit_DD_100[i] = Emiss_Criteria(r'Ref\gwp_breakdown.txt',r'Results_sans_nuk\Results_max\output_'+str(i+1)+'\gwp_breakdown.txt',24)    
    # criterias_DD_50[i] = Price_Criteria(r'pareto\CO2emissions50000\cost_breakdown.txt',r'Results_sans_nuk\Results_50\output_'+str(i+1)+'\\cost_breakdown.txt',128)
    # criterias_DD_40[i] = Price_Criteria(r'pareto\CO2emissions40000\cost_breakdown.txt',r'Results_sans_nuk\Results_40\output_'+str(i+1)+'\\cost_breakdown.txt',128)
    # criterias_DD_30[i] = Price_Criteria(r'pareto\CO2emissions30000\cost_breakdown.txt',r'Results_sans_nuk\Results_30\output_'+str(i+1)+'\\cost_breakdown.txt',128)
    # criterias_DD_10[i] = Price_Criteria(r'pareto\CO2emissions10000\cost_breakdown.txt',r'Results_sans_nuk\Results_10\output_'+str(i+1)+'\\cost_breakdown.txt',128)

    total_cost_DD_100[i] = np.sum(np.sum(np.genfromtxt(r'Results_sans_nuk\Results_max\output_'+str(i+1)+'\cost_breakdown.txt',usecols = (1,2,3),skip_header=1)))
    total_emis_DD_100[i] = np.sum(np.genfromtxt(r'Results_sans_nuk\Results_max\output_'+str(i+1)+'\gwp_breakdown.txt',usecols = 1,skip_header=1))

    
    
for i in range (0,nFr) :
    criterias_Fr_100[i] = Price_Criteria(r'Ref\cost_breakdown.txt',r'ResultsA\gwp100\output'+str(i)+'\cost_breakdown.txt',128)
    EmissCrit_Fr_100[i] = Emiss_Criteria(r'Ref\gwp_breakdown.txt',r'ResultsA\gwp100\output'+str(i)+'\gwp_breakdown.txt',24)
    # criterias_Fr_50[i] = Price_Criteria(r'pareto\CO2emissions50000\cost_breakdown.txt',r'ResultsA\gwp50\output'+str(i)+'\\cost_breakdown.txt',128)
    # criterias_Fr_40[i] = Price_Criteria(r'pareto\CO2emissions40000\cost_breakdown.txt',r'ResultsA\gwp40\output'+str(i)+'\\cost_breakdown.txt',128)
    # criterias_Fr_30[i] = Price_Criteria(r'pareto\CO2emissions30000\cost_breakdown.txt',r'ResultsA\gwp30\output'+str(i)+'\\cost_breakdown.txt',128)
    # criterias_Fr_10[i] = Price_Criteria(r'pareto\CO2emissions10000\cost_breakdown.txt',r'ResultsA\gwp10\output'+str(i)+'\\cost_breakdown.txt',128)
    try : 
       total_cost_Fr_100[i] = np.sum(np.sum(np.genfromtxt(r'ResultsA\gwp100\output'+str(i)+'\cost_breakdown.txt',usecols = (1,2,3),skip_header=1)))
       total_emis_Fr_100[i] = np.sum(np.genfromtxt(r'ResultsA\gwp100\output'+str(i)+'\gwp_breakdown.txt',usecols = 1,skip_header=1))

    except :
        pass
criterias_100 = np.append(criterias_DD_100,criterias_Fr_100)
# criterias_50 = np.append(criterias_DD_50,criterias_Fr_50)    
# criterias_40 = np.append(criterias_DD_40,criterias_Fr_40)    
# criterias_30 = np.append(criterias_DD_30,criterias_Fr_30)    
# criterias_10 = np.append(criterias_DD_10,criterias_Fr_10)        

total_cost_100 = np.append(total_cost_DD_100,total_cost_Fr_100)
# total_cost_50 = np.append(total_cost_DD_50,total_cost_Fr_50)
# total_cost_40 = np.append(total_cost_DD_40,total_cost_Fr_40)
# total_cost_30 = np.append(total_cost_DD_30,total_cost_Fr_30)
# total_cost_10 = np.append(total_cost_DD_10,total_cost_Fr_10)

