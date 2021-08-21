from Comparison import compare_tech
from Comparison_Costs import compare_costs
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# compare_tech(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\technologies.txt',r'D:\Mémoire\LHS_Test\Results\Elec_500_90\gwp_10e6\Thesis\output226\\technologies.txt') # Open and close the file
# plt.show()

v1 = compare_costs(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\cost_breakdown.txt',r'D:\Mémoire\LHS_Test\Results\New_LHS_Random9_90\1st\New_LHS_1\output484\\cost_breakdown.txt') # Open and close the file
v2 = compare_costs(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\cost_breakdown.txt',r'D:\Mémoire\LHS_Test\Results\New_LHS_Random9_90\1st\New_LHS_1\\output376\\cost_breakdown.txt') # Open and close the file

list1 = v1[2]
list2 = v2[2]
index = np.unique(np.append(list1,list2))
tech = v1[3]
bins = len(index)


costs_sub_1 = v1[1]
costs_opt_1 = v1[0]
costs_sub_2 = v2[1]
costs_opt_2 = v2[0]

cs1 = np.zeros(len(index))
cs2= np.zeros(len(index))
co1= np.zeros(len(index))
co2= np.zeros(len(index))
for i in range (0,len(index)):
    if index[i] in list1:
        cs1[i] = costs_sub_1[list1.index(index[i])]
        co1[i] = costs_opt_1[list1.index(index[i])]
    else:
        cs1[i]=0
        co1[i]=0
    if index[i] in list2:
        cs2[i] = costs_sub_2[list2.index(index[i])]
        co2[i] = costs_opt_2[list2.index(index[i])]
    else:
        cs2[i]=0
        co2[i]=0
        
    

plt.bar(np.arange(0,bins,1)-0.15,cs1-co1,width=0.3,label = 'R = 0.86')
plt.bar(np.arange(0,bins,1)+0.15,cs2-co2,width=0.3,label = 'R = 0.15')
plt.xticks(np.arange(0,bins,1),[tech[i] for i in index],rotation = 45)
plt.ylabel('Technologies costs differences with optimum [b€]')
plt.legend(loc = 'upper right')


plt.show()