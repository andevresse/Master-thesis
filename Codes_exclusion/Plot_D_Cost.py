## This script plots the D_criteria versus the total cost
## Author : Anthony Devresse ##
## Optimal cost = 37596.05916 ##



from Call_Distance_Criteria import criterias_DD_100,total_cost_DD_100,criterias_Fr_100,total_cost_Fr_100,EmissCrit_DD_100,total_emis_DD_100,EmissCrit_Fr_100,total_emis_Fr_100
from plot_Cost_CO2 import n_design,total_ref_cost,total_ref_gwp,total_ref_cost_gwp #,pareto_cost
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# for i in range (0,500) :
#     if(total_cost[i]<total_ref_cost) :
#         print('Cheaper than optimum design : '+ str(i))
# for i in range (0,1000) :
#     if (total_gwp[i]<total_ref_gwp) :
#         print('Less polluting than optimum design : '+ str(i))


EmissCrit_Fr_100 = EmissCrit_Fr_100[total_cost_Fr_100!=0]
total_emis_Fr_100 = total_emis_Fr_100[total_cost_Fr_100!=0]
criterias_DD_100 = criterias_DD_100[total_cost_DD_100!=0]
criterias_Fr_100 = criterias_Fr_100[total_cost_Fr_100!=0]
total_cost_Fr_100 = total_cost_Fr_100[total_cost_Fr_100!=0]
total_cost_DD_100 = total_cost_DD_100[total_cost_DD_100!=0]



x =  np.linspace(0,30,1000)
y = 37.596 + x # Droite telle que la différence de couts entre les 2 designs est égale au D -> droite impossible à dépasser ? 

R = np.zeros(500)
R = 1 - np.divide((total_cost_DD_100-total_ref_cost),criterias_DD_100)
Total_Robustness = 100*np.mean(R)
print('Total_Robustness of this optimum is ' + str(Total_Robustness))

R2 = np.zeros(500)
R2 = 1 - np.divide((total_cost_Fr_100-total_ref_cost),criterias_Fr_100)
Total_Robustness = 100*np.mean(R2)
print('Total_Robustness of this optimum is ' + str(Total_Robustness))

R3 = np.zeros(500)
R3 = 1 - np.divide((total_emis_Fr_100-total_ref_gwp),EmissCrit_Fr_100)
Total_Robustness = 100*np.mean(R3)
print('Total_Robustness of this optimum is ' + str(Total_Robustness))

R4 = np.zeros(500)
R4 = 1 - np.divide((total_emis_DD_100-total_ref_gwp),EmissCrit_DD_100)
Total_Robustness = 100*np.mean(R4)
print('Total_Robustness of this optimum is ' + str(Total_Robustness))

# R_bis = np.zeros(n_design)
# R_bis = 1 - np.divide((total_cost_bis-pareto_cost[5]),criterias_tot_bis)
# Total_Robustness = 100*np.mean(R_bis)
# print('Total_Robustness of this optimum is ' + str(Total_Robustness))

plt.plot(criterias_DD_100/1000,R*100,'.b',label = 'Exclusion')
plt.plot(criterias_Fr_100/1000,R2*100,'.g',label = 'LHS')
# plt.plot(criterias_tot/1000,(total_cost-pareto_cost[0])/1000,'.g',label = 'Suboptimums with GWP limit 10e4')
# plt.plot(criterias_tot_bis/1000,(total_cost_bis-total_ref_cost)/1000,'.y',label = 'Suboptimums with GWP limit 10e6')
#plt.plot(0,pareto_cost[0]/1000,'.r',label = 'Optimum')
#plt.plot(x,y,'black',label = 'theoretical limit')

plt.xlabel('D [B€]')
plt.ylabel('R criteria [%]')
legend = plt.legend(loc='upper right', shadow=False, fontsize='x-large')
plt.show()

plt.plot(EmissCrit_DD_100/1000,R4*100,'.b',label = 'Exclusion')
plt.plot(EmissCrit_Fr_100/1000,R3*100,'.g',label = 'LHS')
# plt.plot(criterias_tot/1000,(total_cost-pareto_cost[0])/1000,'.g',label = 'Suboptimums with GWP limit 10e4')
# plt.plot(criterias_tot_bis/1000,(total_cost_bis-total_ref_cost)/1000,'.y',label = 'Suboptimums with GWP limit 10e6')
#plt.plot(0,pareto_cost[0]/1000,'.r',label = 'Optimum')
#plt.plot(x,y,'black',label = 'theoretical limit')

plt.xlabel('D-GWP [B€]')
plt.ylabel('R-GWP criteria [%]')
legend = plt.legend(loc='upper right', shadow=False, fontsize='x-large')
plt.show()

plt.plot(criterias_DD_100/1000,total_cost_DD_100-total_ref_cost,'.b',label = 'Exclusion')
plt.plot(criterias_Fr_100/1000,total_cost_Fr_100-total_ref_cost,'.g',label = 'LHS')
plt.xlabel('D [B€]')
plt.ylabel('ΔC [M€]')
legend = plt.legend(loc='lower right', shadow=False, fontsize='x-large')
plt.show()

plt.plot(EmissCrit_DD_100,total_emis_DD_100-total_ref_gwp,'.b',label = 'Exclusion')
plt.plot(EmissCrit_Fr_100,total_emis_Fr_100-total_ref_gwp,'.g',label = 'LHS')
plt.xlabel('D-GWP [B€]')
plt.ylabel('ΔGWP [M€]')
legend = plt.legend(loc='lower right', shadow=False, fontsize='x-large')
plt.show()

plt.plot(criterias_DD_100,total_emis_DD_100-total_ref_gwp,'.b',label = 'Exclusion')
plt.plot(criterias_Fr_100,total_emis_Fr_100-total_ref_gwp,'.g',label = 'LHS')
plt.xlabel('D [B€]')
plt.ylabel('ΔGWP [kT-eq CO2]')
legend = plt.legend(loc='lower right', shadow=False, fontsize='x-large')
plt.show()



















