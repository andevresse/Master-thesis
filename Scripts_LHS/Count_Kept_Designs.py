## This script counts the number of suboptimums
## Author : Anthony Devresse

from Call_Distance_Criteria import criterias
from LHS_Test_1 import num

n_design = num
count = 0
for i in range (0,n_design) :
    if criterias[i] != 0 :
        count +=1
print ('The number of kept designs is '+str(count))
print('The max of suboptimums criteria is ' + str(max(criterias)))