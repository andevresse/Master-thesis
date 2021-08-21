## This script delete all main.run ##
## Author : Anthony Devresse ##
from LHS_Test_1 import num
import os

n_design = num

for i in range (0,n_design) :
    #os.remove(r"D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_"+str(i)+".run")
    os.remove(r"D:\Mémoire\LHS_Test\EnergyScope\output"+str(i))
