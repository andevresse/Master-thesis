## This script writes the LHS value in the main.run created by create_files_design script
##Author : Anthony Devresse


import fileinput
import shutil
from LHS import num,n_LHS,df,x,gwp_limit
import random
import numpy as np


#Change to keep only some suboptimums close or not from optimum in term of cost
select = False

#print(x)

f = open(r'D:\Memoire\LHS_Test\EnergyScope\output_pareto10000\technologies.txt', "r")
lines = f.readlines()
tech = [None]*104
for i in range (0,len(lines)-2) :
    line = lines[i+2].split()
    tech[i] = line[0]
    
print(tech)
f.close()
n_design = num
n_tech = n_LHS

if select == True :
    original = open(r'D:\Memoire\LHS_Test\EnergyScope\ESTD_main_cluster_select','r')
    original_lines = original_readlines()
elif select == False :
    original = open(r'D:\Memoire\LHS_Test\EnergyScope\ESTD_main_ref_cluster.run','r')
    original_lines = original.readlines()

filename = r'D:\Memoire\LHS_Test\EnergyScope\ESTD_main_cluster.run'
run_new = open(filename,'w')

myList = list(np.nonzero(df[:60,1])[0]) # List of technologies indexes installed in optimum
myList.remove(53) #Vire le train freight


for j in range(0,n_design) :
    List_LHS = random.sample(myList,n_LHS)
    run_new.writelines(original_lines[0:45])
    run_new.writelines('param PathName symbolic default "output'+str(j)+'\"; #place where outputs are print'+'\n')
    run_new.writelines('print "model number ' + str(j) +'";'+'\n')
    run_new.writelines(original_lines[46:50])
    run_new.writelines('let gwp_limit := ' + gwp_limit + ';' + '\n')
    for i in List_LHS :
        run_new.writelines('\n' + 'let f_max'+'['+ '\'' + tech[i]+ '\'' + ']'+ ':=' + str(x[j][i]) + ';' + '\n' + 'let f_min'+'['+ '\'' + tech[i]+ '\'' + ']'+ ':=' + str(x[j][i])+ ';' + '\n' + 'let fmax_perc[' + '\'' + tech[i] + '\'' + '] := 1.0;' + '\n' + 'let fmin_perc[' + '\'' +  tech[i] + '\'' + '] := 0.0;'+'\n')
    run_new.writelines(original_lines[51:len(original_lines)])
    
original.close()
run_new.close()
            

