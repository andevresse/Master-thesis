## This script works with the R criteria ##
## Author : Anthony Devresse ##

from Call_Distance_Criteria import criterias_DD_100,criterias_DD_50,criterias_DD_40,criterias_DD_30,criterias_DD_10,total_cost_DD_100,total_cost_DD_50,total_cost_DD_40,total_cost_DD_30,total_cost_DD_10,criterias_Fr_100,criterias_Fr_50,criterias_Fr_40,criterias_Fr_30,criterias_Fr_10,total_cost_Fr_100,total_cost_Fr_50,total_cost_Fr_40,total_cost_Fr_30,total_cost_Fr_10
from plot_Cost_CO2 import n_design,total_ref_cost,total_ref_gwp,pareto_cost,pareto_gwp
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

criterias_DD_100 = criterias_DD_100[total_cost_DD_100!=0]
criterias_DD_50 = criterias_DD_50[total_cost_DD_50!=0]
criterias_DD_40 = criterias_DD_40[total_cost_DD_40!=0]
criterias_DD_30 = criterias_DD_30[total_cost_DD_30!=0]
criterias_DD_10 = criterias_DD_10[total_cost_DD_10!=0]
criterias_Fr_100 = criterias_Fr_100[total_cost_Fr_100!=0]
criterias_Fr_50 = criterias_Fr_50[total_cost_Fr_50!=0]
criterias_Fr_40 = criterias_Fr_40[total_cost_Fr_40!=0]
criterias_Fr_30 = criterias_Fr_30[total_cost_Fr_30!=0]
criterias_Fr_10 = criterias_Fr_10[total_cost_Fr_10!=0]

total_cost_DD_100 = total_cost_DD_100[total_cost_DD_100!=0]
total_cost_DD_50 = total_cost_DD_50[total_cost_DD_50!=0]
total_cost_DD_40 = total_cost_DD_40[total_cost_DD_40!=0]
total_cost_DD_30 = total_cost_DD_30[total_cost_DD_30!=0]
total_cost_DD_10 = total_cost_DD_10[total_cost_DD_10!=0]
total_cost_Fr_100 = total_cost_Fr_100[total_cost_Fr_100!=0]
total_cost_Fr_50 = total_cost_Fr_50[total_cost_Fr_50!=0]
total_cost_Fr_40 = total_cost_Fr_40[total_cost_Fr_40!=0]
total_cost_Fr_30 = total_cost_Fr_30[total_cost_Fr_30!=0]
total_cost_Fr_10 = total_cost_Fr_10[total_cost_Fr_10!=0]



gwp = [total_ref_gwp,pareto_gwp[45],pareto_gwp[35],pareto_gwp[25],pareto_gwp[5]]


R_nogwp = 1 - np.divide((total_cost_DD_100-total_ref_cost),criterias_DD_100)
R_gwp10000 = 1 - np.divide((total_cost_DD_10-pareto_cost[5]),criterias_DD_10)
R_gwp30000 = 1 - np.divide((total_cost_DD_30-pareto_cost[25]),criterias_DD_30)
R_gwp40000 = 1 - np.divide((total_cost_DD_40-pareto_cost[35]),criterias_DD_40)
R_gwp50000 = 1 - np.divide((total_cost_DD_50-pareto_cost[45]),criterias_DD_50)  

# plt.hist([R_nogwp,R_gwp50000,R_gwp40000,R_gwp30000,R_gwp10000], bins='auto', label = ['GWP = 74e3','GWP = 50e3','GWP = 40e3','GWP = 30e3','GWP = 10e3'])
# legend = plt.legend(loc='upper left', shadow=False, fontsize='x-large')
# plt.show()
# print('Rnogwp mean is '+str(np.mean(R_nogwp)) + '\n' + 'R_gwp50000 mean is '+str(np.mean(R_gwp50000)) + '\n' +'R_gwp40000 mean is '+str(np.mean(R_gwp40000)) + '\n' +'R_gwp30000 mean is '+str(np.mean(R_gwp30000)) + 'Rgwp10000 mean is '+str(np.mean(R_gwp10000)))

R_DD = [np.mean(R_nogwp),np.mean(R_gwp50000),np.mean(R_gwp40000),np.mean(R_gwp30000),np.mean(R_gwp10000)]
V_DD = [np.var(R_nogwp),np.var(R_gwp50000),np.var(R_gwp40000),np.var(R_gwp30000),np.var(R_gwp10000)]

R_nogwp = 1 - np.divide((total_cost_Fr_100-total_ref_cost),criterias_Fr_100)
R_gwp10000 = 1 - np.divide((total_cost_Fr_10-pareto_cost[5]),criterias_Fr_10)
R_gwp30000 = 1 - np.divide((total_cost_Fr_30-pareto_cost[25]),criterias_Fr_30)
R_gwp40000 = 1 - np.divide((total_cost_Fr_40-pareto_cost[35]),criterias_Fr_40)
R_gwp50000 = 1 - np.divide((total_cost_Fr_50-pareto_cost[45]),criterias_Fr_50)  

# plt.hist([R_nogwp,R_gwp50000,R_gwp40000,R_gwp30000,R_gwp10000], bins='auto', label = ['GWP = 74e3','GWP = 50e3','GWP = 40e3','GWP = 30e3','GWP = 10e3'])
# legend = plt.legend(loc='upper left', shadow=False, fontsize='x-large')
# plt.show()
# print('Rnogwp mean is '+str(np.mean(R_nogwp)) + '\n' + 'R_gwp50000 mean is '+str(np.mean(R_gwp50000)) + '\n' +'R_gwp40000 mean is '+str(np.mean(R_gwp40000)) + '\n' +'R_gwp30000 mean is '+str(np.mean(R_gwp30000)) + 'Rgwp10000 mean is '+str(np.mean(R_gwp10000)))

R_Fr = [np.mean(R_nogwp),np.mean(R_gwp50000),np.mean(R_gwp40000),np.mean(R_gwp30000),np.mean(R_gwp10000)]
V_Fr = [np.var(R_nogwp),np.var(R_gwp50000),np.var(R_gwp40000),np.var(R_gwp30000),np.var(R_gwp10000)]


plt.plot(gwp,R_DD,'o-b',label = 'Exclusion method')
plt.plot(gwp,R_Fr,'o-g',label = 'LHS method')
plt.title('Evolution of the R criteria mean with gwp')
plt.xlabel('gwp emissions [kT-eq CO2]')
plt.ylabel('R criteria mean[-]')
legend = plt.legend(loc='upper left', shadow=False, fontsize='large')
plt.show()

plt.plot(gwp,V_DD,'o-b',label = 'Exclusion method')
plt.plot(gwp,V_Fr,'o-g',label = 'LHS method')
plt.title('Evolution of the R criteria variance with gwp')
plt.xlabel('gwp emissions [kT-eq CO2]')
plt.ylabel('R criteria variance [-]')
legend = plt.legend(loc='upper right', shadow=False, fontsize='large')
plt.show()