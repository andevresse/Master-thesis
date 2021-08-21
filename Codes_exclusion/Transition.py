# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:55:46 2021

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt

c_path = 'Ref\cost_breakdown.txt'
c_ref = np.genfromtxt(c_path,skip_header = 1,usecols = (1,2,3))
Ref_cost = np.sum(c_ref)

def T_to_ref(n):
    c=np.genfromtxt('Results_sans_nuk\Results_max\output_'+str(int(n))+'\cost_breakdown.txt',skip_header = 1,usecols = (1,2,3))
    cost = 0
    for i in range (0,len(c)):
        cost = cost + max(0,c[i][0]-c_ref[i][0])
        cost = cost + c[i][1] + c[i][2] - c_ref[i][1] - c_ref[i][2]
    return cost

def D_to_ref(n):
    c=np.genfromtxt('Results_sans_nuk\Results_max\output_'+str(int(n))+'\cost_breakdown.txt',skip_header = 1,usecols = (1,2,3))
    D = 0
    for i in range (0,len(c)):
        for j in range (0,3):
            D = D+abs(c_ref[i][j]-c[i][j])
    return D


Transit = np.zeros(500)
Total_cost = np.zeros(500)
Diff=np.zeros(500)
for i in range (0,500):
    Transit[i] = T_to_ref(i+1)
    Diff[i] = D_to_ref(i+1)
    Total_cost[i] = np.sum(np.sum(np.genfromtxt('Results_sans_nuk\Results_max\output_'+str(int(i+1))+'\cost_breakdown.txt',skip_header = 1,usecols = (1,2,3))))
    
Total_cost_rel = Total_cost - Ref_cost

plt.plot(Transit,Total_cost_rel,'.')
plt.show()

plt.plot(Diff,Total_cost_rel,'.')
plt.show()

Rt = 1-np.divide(Total_cost_rel,Transit)
plt.plot(Transit,Rt,'.')
plt.show()

plt.plot(Diff,1-np.divide(Total_cost_rel,Diff),'.')
plt.show()