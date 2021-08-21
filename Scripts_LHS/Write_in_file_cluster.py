## This script writes the LHS value in the main.run created by create_files_design script
##Author : Anthony Devresse


import fileinput
import shutil
import LHS_Test_1
from LHS import x,num,n_LHS


#print(x)

f = open(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\technologies.txt', "r")
lines = f.readlines()
tech = [None]*104
for i in range (0,len(lines)-2) :
    line = lines[i+2].split()
    tech[i] = line[0]
    
print(tech)
f.close()
n_design = num
n_tech = n_LHS
tech_start = 18

original = open(r'D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_ref_cluster.run','r')
original_lines = original.readlines()
filename = r'D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_cluster.run'
run_new = open(filename,'w')


for j in range(0,n_design) :
    run_new.writelines(original_lines[0:45])
    run_new.writelines('param PathName symbolic default "output'+str(j)+'\"; #place where outputs are print'+'\n')
    run_new.writelines('print "model number ' + str(j) +'";'+'\n')
    run_new.writelines(original_lines[46:51])
    for i in range (tech_start,tech_start + n_tech) :
        run_new.writelines('\n' + 'let f_max'+'['+ '\'' + tech[i]+ '\'' + ']'+ ':=' + str(x[i][j]) + ';' + '\n' + 'let f_min'+'['+ '\'' + tech[i]+ '\'' + ']'+ ':=' + str(x[i][j])+ ';' + '\n' + 'let fmax_perc[' + '\'' + tech[i] + '\'' + '] := 1.0;' + '\n' + 'let fmin_perc[' + '\'' +  tech[i] + '\'' + '] := 0.0;'+'\n')
    run_new.writelines(original_lines[51:len(original_lines)])
    
original.close()
run_new.close()
            
