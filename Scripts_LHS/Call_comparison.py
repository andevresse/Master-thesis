## Call comparison for every suboptimums##
## Author : Anthony Devresse ##



import numpy as np
from Comparison import compare_tech
from Call_Distance_Criteria import criterias,total_cost,pareto_cost
import matplotlib
import matplotlib.pyplot as plt
from LHS_Test_1 import num


n_design = 500
R = np.zeros(n_design)
R = 1 - np.divide((total_cost-pareto_cost[8]),criterias) #Avant suppression des 0 pour pas décaler

output = open(r'D:\Mémoire\LHS_Test\EnergyScope\Comparison_file.txt','w')
for count in range (0,n_design) :
    print ('count is ' +str(count))
    output = open(r'D:\Mémoire\LHS_Test\EnergyScope\Comparison_file.txt','a')
    output.write('\n' + '-----------------------------------------------------'+'\n')
    output.write('The design number is '+ str(count) + '\n' + 'its relative distance criteria is ' + str(100*(criterias[count]/pareto_cost[8])) + '\n' + 'Its R criteria is ' + str(R[count])+ '\n' + 'Its price is '+ str(total_cost[count]) + '\n' )
    output.close() 
    compare_tech(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\technologies.txt',r'D:\Mémoire\LHS_Test\Results\New_LHS_Random9_90\1st\New_LHS_1\output'+str(count)+'\\technologies.txt') # Open and close the file 