## Write in file the LHS values but choose a random number of random technologies ##
## Author : Anthony Devresse ##

import fileinput
import random
from LHS_Test_1 import x,num
import numpy as np


#print(x)

f = open(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\technologies.txt', "r")
lines = f.readlines()
tech = [None]*82
for i in range (0,82) : #Do not take the last 22 technologies 
    line = lines[i+2].split()
    tech[i] = line[0]
# tech.remove('EFFICIENCY')
# tech.remove('DHN')
# tech.remove('GRID')
print(tech)
f.close()

n_design = num

#myList = [i for i, e in enumerate(x[1]) if e != 0]
myList = np.nonzero(x[1])[0]
print(myList)


for j in range(0,n_design) :
    n_LHS = 9 #or  random.randint(1,10) #Random number of technologies that will be LHSed
    myList = range(0,82) #101-3 for the 3 removed technologies
    List_LHS = random.sample(myList,n_LHS)
    print(List_LHS)
    file_name = r'D:\Mémoire\LHS_Test\EnergyScope\ESTD_main_'+str(j)+'.run'
    for line in fileinput.FileInput(file_name,inplace = 1) :
        if 'let re_share_primary := 0.0;' in line :
            line = line.rstrip()
            for i in range (0,n_LHS):
                line = line.replace(line,line + '\n' + 'let f_max'+'['+ '\'' + tech[List_LHS[i]]+ '\'' + ']'+ ':=' + str(x[j][List_LHS[i]]) + ';' + '\n' + 'let f_min'+'['+ '\'' + tech[List_LHS[i]]+ '\'' + ']'+ ':=' + str(x[j][List_LHS[i]])+ ';' + '\n' + 'let fmax_perc[' + '\'' + tech[List_LHS[i]] + '\'' + '] := 1.0;' + '\n' + 'let fmin_perc[' + '\'' +  tech[List_LHS[i]] + '\'' + '] := 0.0;')
        #print(line)
        if 'param PathName symbolic default "output_ref"; #place where outputs are print' in line :
            line.rstrip() 
            line = line.replace(line,'param PathName symbolic default \"output' + str(j) + '\"; #place where outputs are print')
        #print(line)
        if 'let PathName := "output"&; #place where outputs are print' in line :
            line.rstrip()
            line = line.replace(line,'let PathName := "output"&'+str(j)+'; #place where outputs are print')
        print(line)
        