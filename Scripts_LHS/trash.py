import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
from Distance_Criteria import Price_Criteria

# def myfunction(x) :
#     #output = abs(2*np.arctan(x)-math.pi/2)
#     output = abs(x-1)/(abs(x)+1)
#     return output
# 
# x = np.linspace(0,10,1000)
# toPlot = myfunction(x)
# plt.plot(x,toPlot)
# plt.xlabel('f_sub/f_opt')
# plt.ylabel('ds')
# plt.show()

Price_Diff = Price_Criteria(r'D:\Mémoire\LHS_Test\EnergyScope\output1\\cost_breakdown.txt',128)
print(Price_Diff)