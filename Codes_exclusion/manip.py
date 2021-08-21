# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:16:05 2021

@author: User
"""
import numpy as np
import os
import shutil
cost_10k = np.sum(np.sum(np.genfromtxt('pareto\\CO2emissions40000\\cost_breakdown.txt',skip_header=1,usecols=[1,2,3])))

cmin=cost_10k
cmax=cost_10k*1.1
n=0
for i in range (0,500):
    if os.path.isfile('ResultsA\\Nouveau_dossier\\gwp40\\output'+str(int(i))+'\\cost_breakdown.txt'):
        cost = np.sum(np.sum(np.genfromtxt('ResultsA\\Nouveau_dossier\\gwp40\\output'+str(int(i))+'\\cost_breakdown.txt',skip_header=1,usecols=[1,2,3])))
        if cost<cmax and cost>cmin:
            shutil.copytree('ResultsA\\Nouveau_dossier\\gwp40\\output'+str(int(i)), 'ResultsA\\Nouveau_dossier\\Final\\output'+str(int(n)))
            n=n+1        
for i in range (0,500):
    if os.path.isfile('ResultsA\\Nouveau_dossier\\LHS_DD_40k\\output'+str(int(i))+'\\cost_breakdown.txt'):
        cost = np.sum(np.sum(np.genfromtxt('ResultsA\\Nouveau_dossier\\LHS_DD_40k\\output'+str(int(i))+'\\cost_breakdown.txt',skip_header=1,usecols=[1,2,3])))
        if cost<cmax and cost>cmin:
            shutil.copytree('ResultsA\\Nouveau_dossier\\LHS_DD_40k\\output'+str(int(i)), 'ResultsA\\Nouveau_dossier\\Final\\output'+str(int(n)))
            n=n+1     
for i in range (0,500):
    if os.path.isfile('ResultsA\\Nouveau_dossier\\LHS_DD_40k_2\\output'+str(int(i))+'\\cost_breakdown.txt'):
        cost = np.sum(np.sum(np.genfromtxt('ResultsA\\Nouveau_dossier\\LHS_DD_40k_2\\output'+str(int(i))+'\\cost_breakdown.txt',skip_header=1,usecols=[1,2,3])))
        if cost<cmax and cost>cmin:
            shutil.copytree('ResultsA\\Nouveau_dossier\\LHS_DD_40k_2\\output'+str(int(i)), 'ResultsA\\Nouveau_dossier\\Final\\output'+str(int(n)))
            n=n+1   
shutil.copytree('ResultsA\\Nouveau_dossier\\Final','ResultsA\\gwp40')
