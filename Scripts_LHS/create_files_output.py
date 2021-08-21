# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:45:44 2020

@author: User
"""
import numpy as np
import os
from LHS_Test_1 import num
n_design = num
for i in range (0,500):
    try:
        os.mkdir(r'D:\Mémoire\LHS_Test\Dossier_Output\output' + str(i))
    except :
        pass
    try:
        os.mkdir(r'D:\Mémoire\LHS_Test\Dossier_Output\output' + str(i) +'\\sankey')
    except :
        pass
    try:
        os.mkdir(r'D:\Mémoire\LHS_Test\Dossier_Output\output' + str(i) +'\\hourly_data')
    except :
        pass