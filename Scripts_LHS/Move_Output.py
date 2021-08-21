## Move all output to the Results folder ##
## Author : Anthony Devresse ##

from LHS_Test_1 import num
import os
import shutil

n_design = 500

#shutil.move(r"D:\Mémoire\LHS_Test\EnergyScope\Comparison_file.txt",r"D:\Mémoire\LHS_Test\Results\LHS_Point_DD_1\Comparison_file.txt")
for i in range (0,n_design) :
    shutil.move(r"D:\Mémoire\LHS_Test\EnergyScope\output"+str(i),r"D:\Mémoire\LHS_Test\Results\Elec_1000_80\GWP1000\output"+str(i))


