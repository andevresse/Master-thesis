## This script works with the R criteria ##
## Author : Anthony Devresse ##

from Call_Distance_Criteria import n_design,criterias,total_cost,total_gwp,pareto_cost,pareto_gwp
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


criterias = criterias[total_cost!=0]
total_cost = total_cost[total_cost!=0]


R = np.zeros(n_design)


R = 1 - np.divide((total_cost-pareto_cost[8]),criterias)


# plt.hist([R_nogwp,R_gwp10000,R_gwp20000,R_gwp30000,R_gwp40000,R_gwp50000], bins=50, label = ['No GWP limit','GWP = 10000','GWP = 20000','GWP = 30000','GWP = 40000','GWP = 50000', 'GWP = 60000'])
# #plt.hist(R_gwp10000,bins = 'auto',rwidth = 0.85)
# plt.legend(loc='upper right')
# plt.xlabel('R [/]')
# plt.ylabel('Occurences [/]')
# plt.show()


# gwp = np.array([pareto_gwp[0],pareto_gwp[1],pareto_gwp[2],pareto_gwp[3],pareto_gwp[4],pareto_gwp[8]])
# Robustness = np.array([np.mean(R_gwp10000),np.mean(R_gwp20000),np.mean(R_gwp30000),np.mean(R_gwp40000),np.mean(R_gwp50000),np.mean(R_nogwp)])


# plt.plot(pareto_gwp[8]/1000,np.mean(R_nogwp),'o-b')
# plt.plot(pareto_gwp[0]/1000,np.mean(R_gwp10000),'o-b')
# plt.plot(pareto_gwp[1]/1000,np.mean(R_gwp20000),'o-b')
# plt.plot(pareto_gwp[2]/1000,np.mean(R_gwp30000),'o-b')
# plt.plot(pareto_gwp[3]/1000,np.mean(R_gwp40000),'o-b')
# plt.plot(pareto_gwp[4]/1000,np.mean(R_gwp50000),'o-b')
# plt.plot(gwp,Robustness,'o-')
# plt.xlabel('CO2 emissions [MtCO2eq]')
# plt.ylabel('Robustness [/]')
# plt.show()






