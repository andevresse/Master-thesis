## Compare two designs in terms of technologies ##
## Author : Anthony Devresse
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')

## Call comparison for one design ##
###


def compare_tech(ref_file,filename) :
    f = open(ref_file, "r")
    lines = f.readlines()
    tech = [None]*104
    for i in range (0,len(lines)-2) :
        line = lines[i+2].split()
        tech[i] = line[0]
        
    #print(tech)
    f.close()

    filename_ref = r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\technologies.txt'
    filename_sub = filename
    df_ref = np.genfromtxt(filename_ref,dtype = 'float' , delimiter = '\t', skip_header = 2,usecols = (2))
    try :
        df_sub = np.genfromtxt(filename_sub,dtype = 'float' , delimiter = '\t', skip_header = 2,usecols = (2))
        #output = open(r'D:\Mémoire\LHS_Test\EnergyScope\Comparison_file.txt','a')
        
        bins = 0
        j = 0
        techs_opt = np.zeros(104)
        techs_sub = np.zeros(104)
        index_tech = list(range(0,104))
        for i in range (0,104) :
            if df_ref[i] - df_sub[i] != 0 :
                output = open(r'D:\Mémoire\LHS_Test\EnergyScope\Comparison_file.txt','a')
                if tech[i] != 'TS_DHN_SEASONAL' :
                    bins +=1
                    output.write(tech[i] + '\t' + 'ref = ' + str(df_ref[i]) + '\t' + 'sub = ' + str(df_sub[i]) + '\t' + 'diff = ' + str(df_sub[i] - df_ref[i])+'\n')
                    techs_opt[j] = df_ref[i]
                    techs_sub[j] = df_sub[i]
                    index_tech[j] = i
                    j+=1
                
        techs_opt = techs_opt[:bins]
        techs_sub = techs_sub[:bins]
        index_tech = index_tech[:bins]
        
        plt.bar(np.arange(0,bins,1)-0.15,techs_opt,width=0.3,label = 'Optimum')
        plt.bar(np.arange(0,bins,1)+0.15,techs_sub,width=0.3,label = 'Suboptimum')
        plt.xticks(np.arange(0,bins,1),[tech[i] for i in index_tech],rotation = 45)
        plt.ylabel('Technologies sizing [GW]')

        
        
        output.close()
    except Exception as x :
        #print ('Empty file ! Count is '+str(count))
        print(x)
    
