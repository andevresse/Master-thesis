import numpy as np
import matplotlib.pyplot as plt

path_ref = r'C:\Users\devre\Desktop\UCL\Q9\Optimization\EnergyScope\EnergyScope\Sens_Analysis\Wind_cinv_1000\resources.txt'
resources_ref = np.genfromtxt(path_ref,skip_header = 1,usecols=1)

path_cheap = r'C:\Users\devre\Desktop\UCL\Q9\Optimization\EnergyScope\EnergyScope\Sens_Analysis\Wind_cinv_800\resources.txt'
resources_cheap = np.genfromtxt(path_cheap,skip_header = 1,usecols=1)

path_expensive = r'C:\Users\devre\Desktop\UCL\Q9\Optimization\EnergyScope\EnergyScope\Sens_Analysis\Wind_cinv_4000\resources.txt'
resources_expensive = np.genfromtxt(path_expensive,skip_header = 1,usecols=1)





N=3
ind = np.arange(N)
width = 0.40

elec = [resources_cheap[0],resources_ref[0],resources_expensive[0]]
gasoline = [resources_cheap[1],resources_ref[1],resources_expensive[1]]
diesel = [resources_cheap[2],resources_ref[2],resources_expensive[2]]
bioethanol = [resources_cheap[3],resources_ref[3],resources_expensive[3]]
biodiesel = [resources_cheap[4],resources_ref[4],resources_expensive[4]]
LFO = [resources_cheap[5],resources_ref[5],resources_expensive[5]]  
NG = [resources_cheap[6],resources_ref[6],resources_expensive[6]]
SLF = [resources_cheap[7],resources_ref[7],resources_expensive[7]]
SNG = [resources_cheap[8],resources_ref[8],resources_expensive[8]]
wood = [resources_cheap[9],resources_ref[9],resources_expensive[9]]
wet_biomass = [resources_cheap[10],resources_ref[10],resources_expensive[10]]
coal = [resources_cheap[11],resources_ref[11],resources_expensive[11]]
uranium = [resources_cheap[12],resources_ref[12],resources_expensive[12]]
waste = [resources_cheap[13],resources_ref[13],resources_expensive[13]]
H2 = [resources_cheap[14],resources_ref[14],resources_expensive[14]]
Wind = [resources_cheap[17],resources_ref[17],resources_expensive[17]]
Solar = [resources_cheap[18],resources_ref[18],resources_expensive[18]]
Hydro = [resources_cheap[19],resources_ref[19],resources_expensive[19]]
Geo = [resources_cheap[19],resources_ref[19],resources_expensive[19]]

p1 = plt.bar(ind,elec)
p2 = plt.bar(ind,gasoline)
p3 = plt.bar(ind,diesel)
p4 = plt.bar(ind,bioethanol)
p5 = plt.bar(ind,biodiesel)
p6 = plt.bar(ind,LFO)
p7 = plt.bar(ind,NG)
p8 = plt.bar(ind,SLF)
p9 = plt.bar(ind,SNG)
p10 = plt.bar(ind,wood)
p11 = plt.bar(ind,wet_biomass)
p12 = plt.bar(ind,coal)
p13 = plt.bar(ind,uranium)
p14 = plt.bar(ind,waste)
p15 = plt.bar(ind,H2)
p16 = plt.bar(ind,Wind)
p17 = plt.bar(ind,Solar)
p18 = plt.bar(ind,Hydro)
p19 = plt.bar(ind,Geo)
 

plt.ylabel('Primary energy supply [GWh]')
plt.xticks(ind,('Cheap','Reference','Expensive'))
plt.legend((p1[0],p7[0],p12[0],p11[0],p16[0]),('Imported','NG','Coal','waste','Wind'))
                                            
      
plt.show()
    



           