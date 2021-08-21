## Compare two designs in terms of technologies ##
## Author : Anthony Devresse
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')

def compare_tech(reffile,filename) :
    f = open(reffile, "r")
    lines = f.readlines()
    tech = [None]*104
    for i in range (0,len(lines)-2) :
        line = lines[i+2].split()
        tech[i] = line[0]
        
    #print(tech)
    f.close()

    filename_ref = reffile
    filename_sub = filename
    df_ref = pd.read_csv(filename_ref,sep = "\t",header = None,skiprows = [0,1],index_col = 0)
    try :
        df_sub = pd.read_csv(filename_sub,sep = "\t",header = None,skiprows = [0,1],index_col = 0)
        #output = open(r'D:\Mémoire\LHS_Test\EnergyScope\Comparison_file.txt','a')
        
        bins = 0
        j = 0
        techs_opt = np.zeros(104)
        techs_sub = np.zeros(104)
        index_tech = list(range(0,104))
        for i in range (0,104) :
            
            if df_ref[2][i] - df_sub[2][i] != 0 :
                bins +=1
                output = open(r'Comparison_file.txt','a')
                output.write(tech[i] + '\t' + 'ref = ' + str(df_ref[2][i]) + '\t' + 'sub = ' + str(df_sub[2][i]) + '\t' + 'diff = ' + str(df_sub[2][i] - df_ref[2][i])+'\n')
                techs_opt[j] = df_ref[2][i]
                techs_sub[j] = df_sub[2][i]
                index_tech[j] = i
                j+=1
                
        techs_opt = techs_opt[:bins]
        techs_sub = techs_sub[:bins]
        index_tech = index_tech[:bins]
        
        plt.bar(np.arange(0,bins,1)-0.15,techs_opt,width=0.3,label = 'Optimum')
        plt.bar(np.arange(0,bins,1)+0.15,techs_sub,width=0.3,label = 'Suboptimum')
        plt.xticks(np.arange(0,bins,1),[tech[i] for i in index_tech],rotation = 45)
        plt.show()
        
        
        output.close()
    except Exception as x :
        #print ('Empty file ! Count is '+str(count))
        print(x)
    
