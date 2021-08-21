## Call clustering function ##
## Author : Anthony Devresse ##
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from clustering_function import clustering
from Call_Distance_Criteria import criterias
from R import R,n_design


## Test ##
# output = clustering(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref','D:\Mémoire\LHS_Test\Results\Elec_500_90\gwp_10e6\Thesis\output4')





rels = np.zeros(n_design)

for i in range (0,n_design) :
    rels[i] = clustering(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref','D:\Mémoire\LHS_Test\Results\Results_DD\Results_3\Results_max\output_'+str(i+1))


nan_array = np.isnan(rels)
not_nan_array =~ nan_array
rels = rels[not_nan_array]

var_NG = np.zeros(len(rels))
for i in range(0,len(rels)) :
    var_NG[i] = rels[i] - 48.59794852



plt.plot(criterias,rels,'.')
plt.show()