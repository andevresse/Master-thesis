# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:42:30 2020

@author: User
"""
import os
import shutil
import subprocess

for x in range (0,9):
    co2=(x+1)*10000
    os.mkdir('D:\Mémoire\LHS_Test\EnergyScope\output_pareto'+str(co2))
    os.mkdir('D:\Mémoire\LHS_Test\EnergyScope\output_pareto'+str(co2)+'\sankey')
    os.mkdir('D:\Mémoire\LHS_Test\EnergyScope\output_pareto'+str(co2)+'\hourly_data')

    
