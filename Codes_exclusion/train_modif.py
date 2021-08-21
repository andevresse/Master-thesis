# -*- coding: utf-8 -*-
"""
Created on Sun May 30 09:54:38 2021

@author: User
"""

import numpy as np

path_tech_ref = 'Ref\\technologies.txt'
path_cost_ref = 'Ref\\cost_breakdown.txt'
cost_ref = open (path_cost_ref,'r')
tech_ref = open (path_tech_ref,'r')
n_tech = tech_ref.readlines()[28]
n_cost = cost_ref.readlines()[27]

for n in range (1,551):
    tech_old = open('Results_sans_nuk\Results_max\output_'+str(int(n))+'\\technologies.txt','r')
    lignes = tech_old.readlines()
    lignes[28] = n_tech
    tech_new = open('Results_sans_nuk\Results_max\output_'+str(int(n))+'\\technologies.txt','w')
    tech_new.writelines(lignes)
    tech_new.close()
    
    cost_old = open('Results_sans_nuk\Results_max\output_'+str(int(n))+'\\cost_breakdown.txt','r')
    lignes = cost_old.readlines()
    lignes[27] = n_cost
    cost_new = open('Results_sans_nuk\Results_max\output_'+str(int(n))+'\\cost_breakdown.txt','w')
    cost_new.writelines(lignes)
    cost_new.close()
    