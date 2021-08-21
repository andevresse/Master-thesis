## This script plots the D_criteria versus the total cost
## Author : Anthony Devresse ##
## Optimal cost = 37596.05916 ##



from Call_Distance_Criteria import criterias,total_cost,pareto_cost,tech,ct_diff
from R import R
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plot = 'R-Ct'

criterias = criterias[total_cost!=0]
total_cost = total_cost[total_cost!=0]

design_number = np.arange(0,len(criterias))


x =  np.linspace(0,60,1000)

if plot == 'DeltaC-Ct' :
    plt.plot(100*criterias/pareto_cost[8],100*(total_cost-pareto_cost[8])/pareto_cost[8],'.',label = 'Suboptimums' )
    plt.plot(x,x,'black',label = r'$\Delta C = C_T$')
    plt.xlabel(r'$C_T/C_{opt} [\%]$')
    plt.ylabel(r'$\Delta C/C_{opt} [\%]$')
    legend = plt.legend(loc='upper right', shadow=False, fontsize='x-large')
    for i, txt in enumerate(design_number):
        plt.annotate(txt, (100*criterias[i]/pareto_cost[8], 100*(total_cost[i]-pareto_cost[8])/pareto_cost[8]))
    plt.show()
    
if plot == 'Ct_diff-n_design' :
    plt.plot(design_number,100*ct_diff[0]/pareto_cost[8],'.',label = 'Suboptimums')
    plt.xlabel(r'Design number')
    plt.ylabel(r'Transition costs with suboptimum 0')
    legend = plt.legend(loc='upper right', shadow=False, fontsize='x-large')
    for i, txt in enumerate(design_number):
        plt.annotate(txt,(design_number[i],ct_diff[0][i]))
    plt.show()

if plot == 'DeltaC-tech' :
    plt.plot(tech,100*(total_cost-pareto_cost[8])/pareto_cost[8],'.',label = r'Suboptimums')
    plt.xlabel('CCGT installed capacity [GW]')
    plt.ylabel('r$\Delta C/C_{opt} [\%]$')
    legend = plt.legend(loc='upper right', shadow=False, fontsize='x-large')
    for i, txt in enumerate(design_number):
        plt.annotate(txt, (tech[i], 100*(total_cost[i]-pareto_cost[8])/pareto_cost[8]))
    plt.show()

if plot == 'R-Ct' :
    plt.plot(100*criterias/pareto_cost[8],100*R,'.',label = r'Suboptimums')
    plt.xlabel(r'$C_T/C_{opt} [\%]$')
    plt.ylabel('$R [\%]$')
    legend = plt.legend(loc='upper right', shadow=False, fontsize='x-large')
    for i, txt in enumerate(design_number):
        plt.annotate(txt, (100*criterias[i]/pareto_cost[8], 100*R[i]))
    plt.show()
    
    
    
    
    
    
    
    
