## This function computes the distance criteria (+-= transition price)
##Author : Anthony Devresse

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import math


    
def Price_Criteria(ref_file,filename,n_tech) :
    
    criteria = 0
    distance = np.zeros(n_tech)
    tech_cost_ref = np.zeros(n_tech)
    tech_cost_sub = np.zeros(n_tech)
    
    try :
        df_ref = np.genfromtxt(ref_file,dtype = 'float' , delimiter = '\t', skip_header = 1,usecols = (1,2,3))
        df_LHS = np.genfromtxt(filename,dtype = 'float' , delimiter = '\t', skip_header = 1,usecols = (1,2,3))
        for i in range (0,n_tech) :
            tech_cost_ref[i] = df_ref[i][0] + df_ref[i][1] + df_ref[i][2]
            tech_cost_sub[i] = df_LHS[i][0] + df_LHS[i][1] + df_LHS[i][2]
            #distance[i] = abs(tech_cost_ref[i] - tech_cost_sub[i])
            distance [i] = max(df_LHS[i][0] - df_ref[i][0],0) + (df_LHS[i][1]-df_ref[i][1]) + (df_LHS[i][2] - df_ref[i][2])
        criteria = sum(distance)
        return criteria
    except Exception as x :
        print('Error'+str(x))
        return 0
    
