## This script writes the LHS value in the main.run created by create_files_design script
##Author : Anthony Devresse


import fileinput
import LHS_Test_1
from LHS_Test_1 import x,num


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
design=list(range(0,n_design))
for j in range(0,n_design) :
    
    file_name = r'D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_'+str(design[j])+'.run'
    for line in fileinput.FileInput(file_name,inplace = 1) :
        if 'let re_share_primary := 0.0;' in line :
            line = line.rstrip()
            for i in range (0,10):
                line = line.replace(line,line + '\n' + 'let f_max'+'['+ '\'' + tech[i]+ '\'' + ']'+ ':=' + str(x[j][i]) + ';' + '\n' + 'let f_min'+'['+ '\'' + tech[i]+ '\'' + ']'+ ':=' + str(x[j][i])+ ';' + '\n' + 'let fmax_perc[' + '\'' + tech[i] + '\'' + '] := 1.0;' + '\n' + 'let fmin_perc[' + '\'' +  tech[i] + '\'' + '] := 0.0;')
        #print(line)
        if 'param PathName symbolic default "output_ref"; #place where outputs are print' in line :
            line.rstrip() 
            line = line.replace(line,'param PathName symbolic default \"output' + str(j) + '\"; #place where outputs are print')
        #print(line)
        if 'let PathName := "output"&; #place where outputs are print' in line :
            line.rstrip()
            line = line.replace(line,'let PathName := "output"&'+str(j)+'; #place where outputs are print')
        print(line)
        