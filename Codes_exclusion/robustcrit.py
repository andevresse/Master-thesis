# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:55:43 2021

@author: User
"""
import numpy as np
import pandas as pd

co2=100
if co2==100:
    path_asset='ref\\technologies.txt'
    path_cost='ref\\cost_breakdown.txt'
    n=1500
else:        
    path_asset = 'pareto\\CO2emissions'+str(int(co2))+'000\\technologies.txt'
    path_cost = 'pareto\\CO2emissions'+str(int(co2))+'000\\cost_breakdown.txt'
    n=700
fref=np.genfromtxt(path_asset,skip_header=2,usecols=2)[0:60]
cpref=np.genfromtxt(path_asset,skip_header=2,usecols=7)[0:60]
eref=np.multiply(fref,cpref)
cref=np.sum(np.sum(np.genfromtxt(path_cost,skip_header = 1,usecols = [1,2,3])))
tech_names=np.genfromtxt(path_asset,skip_header=2,usecols=0,dtype=str)[0:60]

tn=np.array(tech_names)
Master=[]
cr=[]
for n in range(0,n):
    if co2 == 100:
        if n<550:
            path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
        elif n<1050:
            path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
        else:
            path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
    else:   
        if n > 199:
            n=n-200
            path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
        else:
            path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
    
    try:
        f=np.genfromtxt(path+'\\technologies.txt',skip_header=2,usecols=2)[0:60]
        cp=np.genfromtxt(path+'\\technologies.txt',skip_header=2,usecols=7)[0:60]
        e=np.multiply(f,cp)
        e2=e.tolist()
        Master.append(e2)
        cr.append((np.sum(np.sum(np.genfromtxt(path+'\\cost_breakdown.txt',skip_header = 1,usecols = [1,2,3])))-cref)/cref)
    except:
        pass
    
Master2=np.array([np.array(xi) for xi in Master])
for i in range(0,60):
    Master2[:,i]=(Master2[:,i]-eref[i])/np.max(Master2[:,i])
cr=np.array(cr)
tn=tn[np.logical_not(np.isnan(Master2[1,:]))]
Master2=np.absolute(Master2[:, ~np.isnan(Master2).any(axis=0)])
Crit = Master2/cr[:,None]

n=np.array([np.count_nonzero(x) for x in zip(*Master2)])
s=np.array([sum(x) for x in zip(*Master2)])
mcrit = 100*s/n
    

df=pd.DataFrame(Crit,columns=tn)
