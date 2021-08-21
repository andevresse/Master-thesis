## This function computes the distance criteria (+-= transition price)
##Author : Anthony Devresse

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import math




def Distance_Criteria(filename,n_tech) :
    
    n_LHS_not_null = 0     
    criteria = 0
    distance = np.zeros(n_tech)
    
    try :
        df_ref = pd.read_csv(r'Ref\technologies.txt',sep = "\t",header = None,skiprows = [0,1],index_col = 0)
        df_LHS = pd.read_csv(filename,sep = "\t",header = None,skiprows = [0,1],index_col = 0)
        for i in range (0,n_tech) :
            if df_ref[2][i] == 0 and df_LHS[2][i] == 0:
                distance[i] = 0
#             elif df_ref[2][i] == 0 and df_LHS[2][i] != 0:
#                 distance[i] = 1
#                 n_LHS_not_null +=1
            else :
                #distance[i] = abs(df_ref[2][i]-df_LHS[2][i])/(abs(df_ref[2][i]-0.3*df_ref[2][i]))
                distance[i] = (abs(df_ref[2][i] - df_LHS[2][i]))/(abs(df_ref[2][i])+abs(df_LHS[2][i]))
                #distance[i] = abs(2*np.arctan(df_ref[2][i]/df_LHS[2][i])-(math.pi)/2)
                n_LHS_not_null +=1
        criteria = sum(distance)#/n_LHS_not_null    
        return criteria
    except Exception as x:
        return 0
    
def Price_Criteria(reffile,filename,n_tech) :
    
    criteria = 0
    distance = np.zeros(n_tech)
    total_row = np.zeros(n_tech)
    
    try :
        df_ref = pd.read_csv(reffile,sep = "\t",header = None,skiprows = [0],index_col = 0)
        df_LHS = pd.read_csv(filename,sep = "\t",header = None,skiprows = [0],index_col = 0)
        for i in range (0,n_tech) :
            for j in range (1,4) :
                distance[i] += abs(df_ref[j][i] - df_LHS[j][i])
        criteria = sum(distance)
        return criteria
    except Exception as x :
        print(x)
        return 0

def Emiss_Criteria(reffile,filename,n_ress) :
    
    criteria = 0
    distance = np.zeros(n_ress)
    total_row = np.zeros(n_ress)
    
    try :
        df_ref = pd.read_csv(reffile,sep = "\t",header = None,skiprows = [0],index_col = 0)
        df_LHS = pd.read_csv(filename,sep = "\t",header = None,skiprows = [0],index_col = 0)
        for i in range (0,n_ress) :
            distance[i] += abs(df_ref[1][i] - df_LHS[1][i])
        criteria = sum(distance)
        return criteria
    except Exception as x :
        print(x)
        return 0
    
# def Price_Criteria_gwp(filename,n_tech) :
    
#     criteria = 0
#     distance = np.zeros(n_tech)
#     total_row = np.zeros(n_tech)
    
#     try :
#         df_ref = pd.read_csv(r'Ref\cost_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
#         df_LHS = pd.read_csv(filename,sep = "\t",header = None,skiprows = [0],index_col = 0)
#         for i in range (0,n_tech) :
#             for j in range (1,4) :
#                 distance[i] += abs(df_ref[j][i] - df_LHS[j][i])
#         criteria = sum(distance)
#         return criteria
#     except Exception as x :
#         print(x)
#         return 0
    
# def Price_Criteria_Elec(filename,n_tech) :
#     #Tech from 0 to 9 -> range from 0 to 9
    
#     criteria = 0
#     distance = np.zeros(n_tech)
#     total_row = np.zeros(n_tech)
    
#     try :
#         df_ref = pd.read_csv(r'Ref\cost_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
#         df_LHS = pd.read_csv(filename,sep = "\t",header = None,skiprows = [0],index_col = 0)
#         for i in range (0,n_tech) :
#             for j in range (1,4) :
#                 distance[i] += abs(df_ref[j][i] - df_LHS[j][i])
#         criteria = sum(distance)
#         return criteria
#     except Exception as x :
#         #print(x)
#         return 0
    
# def Price_Criteria_Heating(filename,n_tech) :
#     #Tech from 10 to 40 -> range from 10 to 41
#     criteria = 0
#     distance = np.zeros(n_tech)
#     total_row = np.zeros(n_tech)
    
#     try :
#         df_ref = pd.read_csv(r'Ref\cost_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
#         df_LHS = pd.read_csv(filename,sep = "\t",header = None,skiprows = [0],index_col = 0)
#         for i in range (10,n_tech) :
#             for j in range (1,4) :
#                 distance[i] += abs(df_ref[j][i] - df_LHS[j][i])
#         criteria = sum(distance)
#         return criteria
#     except Exception as x :
#         #print(x)
#         return 0
    
# def Price_Criteria_Mobility(reffile,filename,n_tech) :
#     #Tech from 41 to 60 -> range from 41 to 61
#     criteria = 0
#     distance = np.zeros(n_tech)
#     total_row = np.zeros(n_tech)
    
#     try :
#         df_ref = pd.read_csv(reffile,sep = "\t",header = None,skiprows = [0],index_col = 0)
#         df_LHS = pd.read_csv(filename,sep = "\t",header = None,skiprows = [0],index_col = 0)
#         for i in range (41,n_tech) :
#             for j in range (1,4) :
#                 distance[i] += abs(df_ref[j][i] - df_LHS[j][i])
#         criteria = sum(distance)
#         return criteria
#     except Exception as x :
#         #print(x)
#         return 0
    
# def Price_Criteria_Storage(filename,n_tech) :
    #Tech from 63 to 82 -> range from 63 to 83
    criteria = 0
    distance = np.zeros(n_tech)
    total_row = np.zeros(n_tech)
    
    try :
        df_ref = pd.read_csv(r'Ref\cost_breakdown.txt',sep = "\t",header = None,skiprows = [0],index_col = 0)
        df_LHS = pd.read_csv(filename,sep = "\t",header = None,skiprows = [0],index_col = 0)
        for i in range (63,n_tech) :
            for j in range (1,4) :
                distance[i] += abs(df_ref[j][i] - df_LHS[j][i])
        criteria = sum(distance)
        return criteria
    except Exception as x :
        #print(x)
        return 0
    
