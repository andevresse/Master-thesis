import numpy as np

reference_path = r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_MGA_ref'
output_path = r'D:\Memoire\Other_Methods\MGA\Output'
count = 3
df_res = np.zeros((count,24))
for i in range (0,count) :
    if i == 0 :
        df_res[i] = np.genfromtxt(reference_path + '\\resources.txt',dtype = 'float', delimiter = '\t', skip_header = 1,usecols = 1)
    else :
        df_res[i] = np.genfromtxt(output_path + '\\output' + str(i) + '\\resources.txt',dtype = 'float', delimiter = '\t', skip_header = 1, usecols = 1)

print (df_res)