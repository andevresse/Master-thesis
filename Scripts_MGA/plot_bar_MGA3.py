# This script plots the histograms for the resources for the MGA runs
# For more informations see : Price, J., & Keppo, I. (2017). Modelling to generate alternatives:
# A technique to explore uncertainty in energy-environment-economy models. Applied Energy,
#195, 356–369. https://doi.org/10.1016/j.apenergy.2017.03.065

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Do not forget to change
gwp_limit = '1000000'

#Model choice
model = 'MGA1' #Choose between MGA1 and MGA2
choice_MGA = 'Resources' #Choose between Activities and Resources
choice_weights = 'Integer' #Choose betweeen Integer and Normalized

#Initialization
if gwp_limit == '1000000' :
    opt_path = r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_MGA_ref'
    path = r'D:\Memoire\Other_Methods\MGA\results' + '\\' + model + '\\73CO2'
elif gwp_limit == '40000' :
    opt_path = r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_MGA_40k'
    path = r'D:\Memoire\Other_Methods\MGA\results' + '\\' + model + '\\40CO2'
elif gwp_limit == '10000' :
    opt_path = r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_MGA_10k'
    path = r'D:\Memoire\Other_Methods\MGA\results' + '\\' + model + '\\10CO2'
    
#Get resources names
resources = np.genfromtxt(opt_path + '\\resources.txt',dtype = 'str', delimiter = '\t', skip_header = 1,usecols = 0)
resources = np.concatenate((resources[0:12],resources[13:15],resources[17:20]))
print(resources)
#Parameters
n_design = 4
slack = np.array([1,2,5,10])



#Optimum computations
opt_res = np.genfromtxt(opt_path + '\\' + 'resources.txt',dtype = 'float',delimiter = '\t',skip_header = 1,usecols = 1)
RES_TOT_opt = sum(opt_res[0:12]) + sum(opt_res[13:15]) + sum(opt_res[17:20])
#opt_res = np.concatenate((opt_res[0:12],opt_res[13:15],opt_res[17:20]))

#Declaration
ELEC = np.zeros((n_design,len(slack)))
GASOLINE = np.zeros((n_design,len(slack)))
DIESEL = np.zeros((n_design,len(slack)))
BIOETHANOL = np.zeros((n_design,len(slack)))
BIODIESEL = np.zeros((n_design,len(slack)))
LFO = np.zeros((n_design,len(slack)))
NG = np.zeros((n_design,len(slack)))
SLF = np.zeros((n_design,len(slack)))
SNG = np.zeros((n_design,len(slack)))
WOOD = np.zeros((n_design,len(slack)))
WET_BIOMASS = np.zeros((n_design,len(slack)))
COAL = np.zeros((n_design,len(slack)))
WASTE = np.zeros((n_design,len(slack)))
H2 = np.zeros((n_design,len(slack)))
RES_WIND = np.zeros((n_design,len(slack)))
RES_SOLAR = np.zeros((n_design,len(slack)))
RES_HYDRO = np.zeros((n_design,len(slack)))
RES_TOT = np.zeros((n_design,len(slack)))
ELEC_TOT = np.zeros((n_design,len(slack)))

#MGA RES computations
for i in range (0,len(slack)) :
    for j in range (0,n_design) :
        try :
            df_res = np.genfromtxt(path + '\\' + choice_MGA+'\\'+choice_weights+ '\slack' + str(slack[i]) + '\output'+str(j)+'\\resources.txt',dtype = 'float', delimiter = '\t', skip_header = 1, usecols = 1)
        except :
            df_res = np.genfromtxt(path + '\\' + choice_MGA+'\\'+choice_weights+ '\slack' + str(slack[i]) + '\output_'+str(j)+'\\resources.txt',dtype = 'float', delimiter = '\t', skip_header = 1, usecols = 1)
        myList_res = list(np.nonzero(np.concatenate((df_res[:15],df_res[17:21])))[0])
        
        ELEC[i,j] = df_res[0]
        ELEC_TOT[i,j] += ELEC[i,j] #Actualise ELEC_TOT avec ELEC importe
        GASOLINE[i,j] = df_res[1]
        DIESEL[i,j] = df_res[2]
        BIOETHANOL[i,j] = df_res[3]
        BIODIESEL[i,j] = df_res[4]
        LFO[i,j] = df_res[5]
        NG[i,j] = df_res[6]
        SLF[i,j] = df_res[7]
        SNG[i,j] = df_res[8]
        WOOD[i,j] = df_res[9]
        WET_BIOMASS[i,j] = df_res[10]
        COAL[i,j] = df_res[11]
        WASTE[i,j] = df_res[13]
        H2[i,j] = df_res[14]
        RES_WIND[i,j] = df_res[17]
        RES_SOLAR[i,j] = df_res[18]
        RES_HYDRO[i,j] = df_res[19]
        RES_TOT[i,j] = sum(df_res[0:12]) + sum(df_res[13:15]) + sum(df_res[17:20])


#x-axis
x_axis = []
x_axis.append('Optimum')
for i in range (0,len(slack)) :
    for j in range (0,n_design) :
        x_axis.append('MGA-'+str(j+1)+'-'+str(slack[i])+'%')

x_axis = ['Optimum','MGA 1%','MGA 2%','MGA 5%','MGA 10%']
x_axis = ['']*17
x_axis[0] = 'Optimum'
x_axis[1] = 'MGA 1%'
x_axis[5] = 'MGA 2%'
x_axis[9] = 'MGA 5%'
x_axis[13] = 'MGA 10%'

x = [1,3,4,5,6,8,9,10,11,13,14,15,16,18,19,20,21]

fig,ax = plt.subplots()
#ax.set_xticks([1,5,15,20],['Optimum','MGA 1%,MGA 2%,MGA 5%,MGA 10%'])

ELEC = np.concatenate(([opt_res[0]],(ELEC.flatten())))
ax.bar(x,ELEC,label = 'ELEC',bottom = 0)

GASOLINE = np.concatenate(([opt_res[1]],(GASOLINE.flatten())))
ax.bar(x,GASOLINE,label = 'GASOLINE',bottom = ELEC)

DIESEL = np.concatenate(([opt_res[2]],(DIESEL.flatten())))
ax.bar(x,DIESEL,label = 'DIESEL',bottom = ELEC+GASOLINE)

BIOETHANOL = np.concatenate(([opt_res[3]],(BIOETHANOL.flatten())))
ax.bar(x,BIOETHANOL,label = 'BIOETHANOL',bottom = ELEC+GASOLINE+DIESEL,color = 'purple')

BIODIESEL = np.concatenate(([opt_res[4]],(BIODIESEL.flatten())))
ax.bar(x,BIODIESEL,label = 'BIODIESEL',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL)

LFO = np.concatenate(([opt_res[5]],(LFO.flatten())))
ax.bar(x,LFO,label = 'LFO',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL)

NG = np.concatenate(([opt_res[6]],(NG.flatten())))
ax.bar(x,NG,label = 'NG',color = 'grey',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO)

SLF = np.concatenate(([opt_res[7]],(SLF.flatten())))
ax.bar(x,SLF,label = 'SLF',bottom =ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO+NG )

SNG = np.concatenate(([opt_res[8]],(SNG.flatten())))
ax.bar(x,SNG,label = 'SNG',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO+NG+SLF,color = 'gainsboro')

WOOD = np.concatenate(([opt_res[9]],(WOOD.flatten())))
ax.bar(x,WOOD,label = 'WOOD',color = 'brown',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO+NG+SLF+SNG)

WET_BIOMASS = np.concatenate(([opt_res[10]],(WET_BIOMASS.flatten())))
ax.bar(x,WET_BIOMASS,label = 'WET_BIOMASS',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO+NG+SLF+SNG+WOOD,color = 'orange')

COAL = np.concatenate(([opt_res[11]],(COAL.flatten())))
ax.bar(x,COAL,label = 'COAL',color = 'black',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO+NG+SLF+SNG+WOOD+WET_BIOMASS)

WASTE = np.concatenate(([opt_res[13]],(WASTE.flatten())))
ax.bar(x,WASTE,label = 'WASTE',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO+NG+SLF+SNG+WOOD+WET_BIOMASS+COAL,color = 'pink')

H2 = np.concatenate(([opt_res[14]],(H2.flatten())))
ax.bar(x,H2,label = 'H2',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO+NG+SLF+SNG+WOOD+WET_BIOMASS+COAL+WASTE)

RES_WIND = np.concatenate(([opt_res[17]],(RES_WIND.flatten())))
ax.bar(x,RES_WIND,label = 'RES_WIND',color = 'green',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO+NG+SLF+SNG+WOOD+WET_BIOMASS+COAL+WASTE+H2)

RES_SOLAR = np.concatenate(([opt_res[18]],(RES_SOLAR.flatten())))
ax.bar(x,RES_SOLAR,label = 'RES_SOLAR',color = 'yellow',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO+NG+SLF+SNG+WOOD+WET_BIOMASS+COAL+WASTE+H2+RES_WIND)

RES_HYDRO = np.concatenate(([opt_res[19]],(RES_HYDRO.flatten())))
ax.bar(x,RES_HYDRO,label = 'RES_HYDRO',bottom = ELEC+GASOLINE+DIESEL+BIOETHANOL+BIODIESEL+LFO+NG+SLF+SNG+WOOD+WET_BIOMASS+COAL+WASTE+H2+RES_WIND+RES_SOLAR,color = 'aqua')

ax.legend(loc = 'upper right')
plt.show()











