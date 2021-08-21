## This script writes the LHS value in the main.run for one technology
##Author : Anthony Devresse


import fileinput
import shutil
import random
import numpy as np
from LHS import x,num,n_LHS,df



filename_ref = r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\technologies.txt'
techs = np.genfromtxt(filename_ref,dtype = 'str', delimiter = '\t', skip_header = 2,usecols = 0)

n_design = 500
index_tech = 1 #Technology always modified in every suboptimums
myList = list(np.nonzero(df[:53,1])[0]) # List of technologies installed in optimum, without freight


original = open(r'D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_ref_cluster.run','r')
original_lines = original.readlines()
filename = r'D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_cluster.run'
run_new = open(filename,'w')


for j in range(0,n_design) :
    n_LHS = random.randint(1,9)
    List_LHS = random.sample(myList,n_LHS)
    if List_LHS.count(index_tech)>0 :
        List_LHS.remove(index_tech)
    run_new.writelines(original_lines[0:45])
    run_new.writelines('param PathName symbolic default "output'+str(j)+'\"; #place where outputs are print'+'\n')
    run_new.writelines('print "model number ' + str(j) +'";'+'\n')
    run_new.writelines(original_lines[46:51])
    run_new.writelines('\n' + 'let f_max'+'['+ '\'' + techs[index_tech]+ '\'' + ']'+ ':=' + str(x[j][index_tech]) + ';' + '\n' + 'let f_min'+'['+ '\'' + techs[index_tech]+ '\'' + ']'+ ':=' + str(x[j][index_tech])+ ';' + '\n' + 'let fmax_perc[' + '\'' + techs[index_tech] + '\'' + '] := 1.0;' + '\n' + 'let fmin_perc[' + '\'' +  techs[index_tech] + '\'' + '] := 0.0;'+'\n')
    for i in List_LHS :
        run_new.writelines('\n' + 'let f_max'+'['+ '\'' + techs[i]+ '\'' + ']'+ ':=' + str(x[j][i]) + ';' + '\n' + 'let f_min'+'['+ '\'' + techs[i]+ '\'' + ']'+ ':=' + str(x[j][i])+ ';' + '\n' + 'let fmax_perc[' + '\'' + techs[i] + '\'' + '] := 1.0;' + '\n' + 'let fmin_perc[' + '\'' +  techs[i] + '\'' + '] := 0.0;'+'\n')
    run_new.writelines(original_lines[51:len(original_lines)])
    
original.close()
run_new.close()
            

