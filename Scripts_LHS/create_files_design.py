## This script creates the main.run to run EnergyScope
## It does so by copying a reference .run for the number num (in LHS_Test_1) times
## /!\ It does not impose any LHS value for certain technologies, this is done in Write_in_file script /!\
## Author : Anthony Devresse

import numpy as np
import os
import shutil
from LHS_Test_1 import num

n_design = 500
design=list(range(0,n_design))
print(design)
for i in range (0,n_design):
    file = open(r"D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_"+str(design[i])+".run", "x")
    
    # If only close suboptimums saved 
    original_sub = r'D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_LHS.run'
    # If all suboptimums saved
    original_all = r'D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_ref.run'
    
    target = r'D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_'+str(design[i])+'.run'
    shutil.copyfile(original_all, target)
    file.close()
