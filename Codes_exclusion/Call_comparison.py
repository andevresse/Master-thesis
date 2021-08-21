## Call comparison for every suboptimums
## Author : Anthony Devresse

from Comparison import compare_tech
from Call_Distance_Criteria import criterias_tot,total_cost,total_gwp
from plot_Cost_CO2 import total_ref_cost
import matplotlib
import matplotlib.pyplot as plt
from LHS_Test_1 import num

n_design = 550
output = open(r'D:\Mémoire\LHS_Test\EnergyScope\Comparison_file.txt','w')
for count in range (0,n_design) :
    output = open(r'D:\Mémoire\LHS_Test\EnergyScope\Comparison_file.txt','a')
    output.write('\n' + '-----------------------------------------------------'+'\n')
    output.write('The design number is '+ str(count)+'\t' + 'and its distance criteria is ' + str(criterias_tot[count]) + '\n' + 'Its price is '+ str(total_cost[count]) + 'and its gwp is '+ str(total_gwp[count]) + '\n' )
    output.close() 
    compare_tech(r'D:\Mémoire\LHS_Test\Results\Elec_1000_80\GWP1000\output'+str(count)+'\\technologies.txt') # Open and close the file 