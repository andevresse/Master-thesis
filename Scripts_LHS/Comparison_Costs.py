## Plots in bar charts the differences of costs between 2 designs##
## Author : Anthony Devresse ##

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')

def compare_costs(file_ref,filename) :
    f = open(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\cost_breakdown.txt', "r")
    lines = f.readlines()
    tech = [None]*128
    for i in range (0,len(lines)-1) :
        line = lines[i+1].split()
        tech[i] = line[0]
        
    #print(tech)
    f.close()

    filename_ref = file_ref
    filename_sub = filename
    df_ref = np.genfromtxt(filename_ref, dtype = 'float',delimiter = '\t', skip_header = 1,usecols = (1,2,3))
    print('df_ref is' + str(df_ref[1][0]))
    try :
        df_sub = np.genfromtxt(filename_sub,dtype = 'float' , delimiter = '\t', skip_header = 1,usecols = (1,2,3))
        #output = open(r'D:\Mémoire\LHS_Test\EnergyScope\Comparison_file.txt','a')
        
        bins = 0
        j = 0
        costs_opt = np.zeros(128)
        costs_sub = np.zeros(128)
        index_cost = list(range(0,128))
        cost_ref_tech = np.zeros(128)
        cost_sub_tech = np.zeros(128)
        difference_costs = np.zeros(128)
        for i in range (0,128) :
            cost_ref_tech[i] +=df_ref[i][0] + df_ref[i][1] + df_ref[i][2]
            cost_sub_tech[i] +=df_sub[i][0] + df_sub[i][1] + df_sub[i][2]
            
            if cost_ref_tech[i] - cost_sub_tech[i] != 0 :
                output = open(r'D:\Mémoire\LHS_Test\EnergyScope\Comparison_file_cost.txt','a')
                #if tech[i] != 'TS_DHN_SEASONAL' :
                bins +=1
                output.write(tech[i] + '\t' + 'ref = ' + str(cost_ref_tech[i]) + '\t' + 'sub = ' + str(cost_sub_tech[i]) + '\t' + 'diff = ' + str(cost_sub_tech[i] - cost_ref_tech[i])+'\n')
                output.close()
                costs_opt[j] = cost_ref_tech[i] 
                costs_sub[j] = cost_sub_tech[i]
                index_cost[j] = i
                difference_costs[j] = cost_sub_tech[i] - cost_ref_tech[i]
                j+=1
                output.close()
                
        costs_opt = costs_opt[:bins]/1000
        costs_sub = costs_sub[:bins]/1000
        index_cost = index_cost[:bins]
        difference_costs = difference_costs[:bins]
        toreturn = [costs_opt,costs_sub,index_cost,tech,bins]
        return toreturn
        
#         plt.bar(np.arange(0,bins,1)-0.15,costs_opt,width=0.3,label = 'Optimum cost')
#         plt.bar(np.arange(0,bins,1)+0.15,costs_sub,width=0.3,label = 'Suboptimum cost')
#         plt.xticks(np.arange(0,bins,1),[tech[i] for i in index_cost],rotation = 45)
#         plt.ylabel('Technologies costs [b€]')
#         print('Difference of price is ' + str(sum(difference_costs)))

#         plt.bar(np.arange(0,bins,1)-shift,costs_sub-costs_opt,width=0.3,label = label)
#         plt.xticks(np.arange(0,bins,1),[tech[i] for i in index_cost],rotation = 45)
#         plt.ylabel('Technologies costs differences with optimum [b€]')
#         plt.legend(loc = 'upper right')
        
    except Exception as x :
        #print ('Empty file ! Count is '+str(count))
        print(x)
    
