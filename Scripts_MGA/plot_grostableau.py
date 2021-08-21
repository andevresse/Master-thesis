## This script plots a big table that summarizes the MGA results##
# author : Anthony Devresse
## See DeCarolis, J. F., Babaee, S., Li, B., & Kanungo, S. (2016).
#Modelling to generate alternatives with an energy system optimization model.
#Environmental Modelling and Software, 79, 300–310. https://doi.org/10.1016/j.envsoft.2015.11.019

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#from figures_func import plot_figures


#Do not forget to change
gwp_limit = '1000000'

#model choice
model = 'MGA1' #Choose between MGA1 and MGA2

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


choice_MGA = 'Activities' #Choose between Activities and Resources
choice_weights = 'Normalized' #Choose betweeen Integer and Normalized
plot = 'HT_LAYER'
graduations = True #True if you want y graduations

if choice_MGA == 'Activities' :
    if choice_weights == 'Integer' :
        save_path = r'D:\Memoire\Divers\figures\Gros_Tableau\MGA_Act_Int'
    elif choice_weights == 'Normalized' :
        save_path = r'D:\Memoire\Divers\figures\Gros_Tableau\MGA_Act_Norm'
elif choice_MGA == 'Resources' :
    if choice_weights == 'Integer' :
        save_path = r'D:\Memoire\Divers\figures\Gros_Tableau\MGA_Res_Int'
    elif choice_weights == 'Normalized' :
        save_path = r'D:\Memoire\Divers\figures\Gros_Tableau\MGA_Res_norm'
    


n_design = 4
slack = np.array([1,2,5,10])

emissions = np.zeros((n_design,len(slack)))
costs = np.zeros((n_design,len(slack)))
## ELEC ##
CCGT = np.zeros((n_design,len(slack)))
COAL_US = np.zeros((n_design,len(slack)))
COAL_IGCC = np.zeros((n_design,len(slack)))
PV = np.zeros((n_design,len(slack)))
WIND_ON = np.zeros((n_design,len(slack)))
WIND_OFF = np.zeros((n_design,len(slack)))
WIND = np.zeros((n_design,len(slack)))
HYDRO_RIVER = np.zeros((n_design,len(slack)))
ELEC_CHP = np.zeros((n_design,len(slack)))
ELEC_TOT = np.zeros((n_design,len(slack)))

## HT HEAT ##
HT_CHP_GAS = np.zeros((n_design,len(slack)))
HT_CHP_WOOD = np.zeros((n_design,len(slack)))
HT_CHP_WASTE = np.zeros((n_design,len(slack)))
HT_CHP = np.zeros((n_design,len(slack)))
HT_CHP_OTHER = np.zeros((n_design,len(slack)))
BOILER_GAS = np.zeros((n_design,len(slack)))
BOILER_WOOD = np.zeros((n_design,len(slack)))
BOILER_OIL = np.zeros((n_design,len(slack)))
BOILER_COAL = np.zeros((n_design,len(slack)))
BOILER_WASTE = np.zeros((n_design,len(slack)))
HT_BOILER = np.zeros((n_design,len(slack)))
HT_BOILER_WOOD_WASTE = np.zeros((n_design,len(slack)))
HT_BOILER_OTHER = np.zeros((n_design,len(slack)))
HT_DIRECT_ELEC = np.zeros((n_design,len(slack)))
HT_TOT = np.zeros((n_design,len(slack)))


## LT HEAT##
LT_DHN = np.zeros((n_design,len(slack)))
LT_DEC = np.zeros((n_design,len(slack)))
LT_TOT = np.zeros((n_design,len(slack)))
LT_CHP = np.zeros((n_design,len(slack)))
LT_BOILER = np.zeros((n_design,len(slack)))
LT_OTHER = np.zeros((n_design,len(slack)))
LT_HP = np.zeros((n_design,len(slack)))
LT_DE = np.zeros((n_design,len(slack)))
LT_HP_GAS = np.zeros((n_design,len(slack)))
LT_HP_ELEC = np.zeros((n_design,len(slack)))

## PUBLIC MOBILITY ##
TRAMWAY = np.zeros((n_design,len(slack)))
BUS_DIESEL = np.zeros((n_design,len(slack)))
BUS_HYDIESEL = np.zeros((n_design,len(slack)))
BUS_CNG = np.zeros((n_design,len(slack)))
BUS_FC = np.zeros((n_design,len(slack)))
TRAIN_PUB = np.zeros((n_design,len(slack)))

## PRIVATE MOBILITY ##
CAR_GASOLINE = np.zeros((n_design,len(slack)))
CAR__DIESEL = np.zeros((n_design,len(slack)))
CAR_NG = np.zeros((n_design,len(slack)))
CAR_HEV = np.zeros((n_design,len(slack)))
CAR_PHEV = np.zeros((n_design,len(slack)))
CAR_BEV = np.zeros((n_design,len(slack)))
CAR_FC = np.zeros((n_design,len(slack)))

## Freight ##
TRAIN_FREIGHT = np.zeros((n_design,len(slack)))
BOAT_FREIGHT_DIESEL = np.zeros((n_design,len(slack)))
BOAT_FREIGHT_NG = np.zeros((n_design,len(slack)))
TRUC_DIESEL = np.zeros((n_design,len(slack)))
TRUCK_FC = np.zeros((n_design,len(slack)))
TRUCK_NG = np.zeros((n_design,len(slack)))
TRUCK_ELEC = np.zeros((n_design,len(slack)))




## RES ##
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

## Optimum computations ##

opt_emissions = sum(np.genfromtxt(opt_path + '\\' + 'gwp_breakdown_op.txt',dtype = 'float',delimiter = '\t',skip_header = 1,usecols = 1))
opt_cost = sum(sum(np.genfromtxt(opt_path + '\\' + 'cost_breakdown.txt',dtype = 'float', delimiter = '\t',skip_header = 1,usecols = (1,2,3))))
opt_activities = np.genfromtxt(opt_path + '\\' + 'technologies.txt',dtype = 'float',delimiter = '\t',skip_header = 2,usecols = 9)
opt_res = np.genfromtxt(opt_path + '\\' + 'resources.txt',dtype = 'float',delimiter = '\t',skip_header = 1,usecols = 1)
ELEC_OPT_TOT = sum(opt_activities[1:8]) + 0.9565 * opt_activities[9] + 0.3396 * opt_activities[10] + 0.4444 * opt_activities[11] + 1.25 * opt_activities[19] + 0.3396 * opt_activities[20] + 0.826446281 * opt_activities[21] + 0.758208955 * opt_activities[22] + 0.4444 * opt_activities[23] + 0.9565 * opt_activities[31] + 0.907 * opt_activities[32] + 2.6364*opt_activities[33] + 2.6364*opt_activities[34] + opt_res[0]
HT_OPT_TOT = sum(opt_activities[9:18])
HT_OPT_CHP_GAS = opt_activities[9]
HT_OPT_CHP_OTHER = opt_activities[10] + opt_activities[11]
HT_OPT_BOILER_WOOD_WASTE = opt_activities[13] + opt_activities[16]
HT_OPT_BOILER_OTHER = opt_activities[12] + opt_activities[14] + opt_activities[15]
HT_OPT_DIRECT_ELEC = opt_activities[17]
HT_OPT_WOOD_WASTE = opt_activities[13] + opt_activities[16]
LT_OPT_TOT = sum(opt_activities[18:40])
LT_OPT_CHP = sum(opt_activities[19:24]) + sum(opt_activities[31:35])
LT_OPT_BOILER = sum(opt_activities[24:27]) + sum(opt_activities[35:38])
LT_OPT_HP = opt_activities[18] + opt_activities[29] + opt_activities[30]
LT_OPT_DE = opt_activities[39]
LT_OPT_OTHER = opt_activities[27] + opt_activities[28] + opt_activities[38] 
RES_TOT_opt = sum(opt_res[0:12]) + sum(opt_res[13:15]) + sum(opt_res[17:20])
LT_OPT_HP_ELEC = opt_activities[18] + opt_activities[29]
LT_OPT_HP_GAS = opt_activities[30]

## CO2 computations ##
for i in range (0,len(slack)) :
    for j in range (0,n_design) :
        try :
            emissions[i,j] = sum(np.genfromtxt(path + '\\' + choice_MGA + '\\'+choice_weights+ '\slack' + str(slack[i]) + '\output'+str(j)+'\\gwp_breakdown_op.txt',dtype = 'float',delimiter = '\t',skip_header = 1,usecols = 1))
        except :
            emissions[i,j] = sum(np.genfromtxt(path + '\\' + choice_MGA + '\\'+choice_weights+ '\slack' + str(slack[i]) + '\output_'+str(j)+'\\gwp_breakdown_op.txt',dtype = 'float',delimiter = '\t',skip_header = 1,usecols = 1))
    
## Cost computations ##
for i in range (0,len(slack)) :
    for j in range (0,n_design) :
        try :
            costs[i,j] = sum(sum(np.genfromtxt(path + '\\' + choice_MGA + '\\'+choice_weights+ '\slack' + str(slack[i]) + '\output'+str(j)+'\\cost_breakdown.txt',dtype = 'float',delimiter = '\t',skip_header = 1,usecols = (1,2,3))))
        except :
            costs[i,j] = sum(sum(np.genfromtxt(path + '\\' + choice_MGA + '\\'+choice_weights+ '\slack' + str(slack[i]) + '\output_'+str(j)+'\\cost_breakdown.txt',dtype = 'float',delimiter = '\t',skip_header = 1,usecols = (1,2,3))))
## Activities computations ##
for i in range (0,len(slack)) :
    for j in range (0,n_design) :
        try :
            df_activities = np.genfromtxt(path + '\\' + choice_MGA + '\\' + choice_weights+ '\slack' + str(slack[i]) + '\output'+str(j)+'\\technologies.txt',dtype = 'float' , delimiter = '\t', skip_header = 2,usecols = 9)
        except :
            df_activities = np.genfromtxt(path + '\\' + choice_MGA + '\\' + choice_weights+ '\slack' + str(slack[i]) + '\output_'+str(j)+'\\technologies.txt',dtype = 'float' , delimiter = '\t', skip_header = 2,usecols = 9)
        myList_activities = list(np.nonzero(df_activities[:60])[0]) 
        
        ## ELEC sector ##
        CCGT[i,j] = df_activities[1]
        COAL_US[i,j] = df_activities[2]
        COAL_IGCC[i,j] = df_activities[3]
        PV[i,j] = df_activities[4]
        WIND_ON[i,j] = df_activities[5]
        WIND_OFF[i,j] = df_activities[6]
        WIND[i,j] = df_activities[5] + df_activities[6]
        HYDRO_RIVER[i,j] = df_activities[7]
        ELEC_CHP[i,j] = 0.9565 * df_activities[9] + 0.3396 * df_activities[10] + 0.4444 * df_activities[11] + 1.25 * df_activities[19] + 0.3396 * df_activities[20] + 0.826446281 * df_activities[21] + 0.758208955 * df_activities[22] + 0.4444 * df_activities[23] + 0.9565 * df_activities[31] + 0.907 * df_activities[32] + 2.6364*df_activities[33] + 2.6364*df_activities[34]
        ELEC_TOT[i,j] = sum(df_activities[1:8]) + ELEC_CHP[i,j] 
        
        ## HT heat sector ##
        HT_CHP_GAS[i,j] = df_activities[9]
        HT_CHP_WOOD[i,j] = df_activities[10]
        HT_CHP_WASTE[i,j] = df_activities[11]
        HT_CHP[i,j] = HT_CHP_GAS[i,j] + HT_CHP_WOOD[i,j] + HT_CHP_WASTE[i,j]
        HT_CHP_OTHER[i,j] = HT_CHP[i,j] - HT_CHP_GAS[i,j]
        BOILER_GAS[i,j] = df_activities[12]
        BOILER_WOOD[i,j] = df_activities[13]
        BOILER_OIL[i,j] = df_activities[14]
        BOILER_COAL[i,j] = df_activities[15]
        BOILER_WASTE[i,j] = df_activities[16]
        HT_BOILER[i,j] =  BOILER_GAS[i,j] + BOILER_WOOD[i,j] + BOILER_OIL[i,j] +  BOILER_COAL[i,j] +  BOILER_WASTE[i,j]
        HT_BOILER_WOOD_WASTE[i,j] = BOILER_WOOD[i,j] + BOILER_WASTE[i,j]
        HT_BOILER_OTHER[i,j] = HT_BOILER[i,j] - BOILER_WOOD[i,j] - BOILER_WASTE[i,j] 
        HT_DIRECT_ELEC[i,j] = df_activities[17]
        HT_TOT[i,j] = sum(df_activities[9:18])
        
        ##LT heat sector ##
        LT_DHN[i,j] = sum(df_activities[18:29])
        LT_DEC[i,j] = sum(df_activities[29:40])
        LT_TOT[i,j] = sum(df_activities[18:40])
        LT_CHP[i,j] = sum(df_activities[19:24]) + sum(df_activities[31:35])
        LT_BOILER[i,j] = sum(df_activities[24:27]) + sum(df_activities[35:38])
        LT_HP[i,j] = df_activities[18] + df_activities[29] + df_activities[30]
        LT_DE[i,j] = df_activities[39]
        LT_OTHER[i,j]  = df_activities[27] + df_activities[28] + df_activities[38]
        LT_HP_GAS[i,j] = df_activities[30]
        LT_HP_ELEC[i,j] = df_activities[18] + df_activities[29]

## Resources computations ##
for i in range (0,len(slack)) :
    for j in range (0,n_design) :
        try :
            df_res = np.genfromtxt(path + '\\' + choice_MGA + '\\'+choice_weights+ '\slack' + str(slack[i]) + '\output'+str(j)+'\\resources.txt',dtype = 'float', delimiter = '\t', skip_header = 1, usecols = 1)
        except :
            df_res = np.genfromtxt(path + '\\' + choice_MGA + '\\'+choice_weights+ '\slack' + str(slack[i]) + '\output_'+str(j)+'\\resources.txt',dtype = 'float', delimiter = '\t', skip_header = 1, usecols = 1)
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
        
        
## Plot ##

y_axis = []
y_axis.append('Optimum')
for i in range (0,len(slack)) :
    for j in range (0,n_design) :
        y_axis.append('MGA-'+str(j+1)+'-'+str(slack[i])+'%')
        
#ELEC LAYER

if plot == 'ELEC_LAYER' :
    ELEC_TOT = ELEC_TOT.flatten()
    plt.subplots_adjust(hspace = 0.3)
    
    graduations = True
    
    CCGT = CCGT.flatten()
    fig,((ax0cc,ax0us,ax0pv,ax0wi,ax0ch,ax0im),(ax1cc,ax1us,ax1pv,ax1wi,ax1ch,ax1im),(ax2cc,ax2us,ax2pv,ax2wi,ax2ch,ax2im),(ax3cc,ax3us,ax3pv,ax3wi,ax3ch,ax3im),(ax4cc,ax4us,ax4pv,ax4wi,ax4ch,ax4im),(ax5cc,ax5us,ax5pv,ax5wi,ax5ch,ax5im)) = plt.subplots(6,6,gridspec_kw = {'height_ratios':[1,4,4,4,4,1]},sharex = True)

    ax0cc.plot(100*opt_activities[1]/ELEC_OPT_TOT,y_axis[0],'o')
    ax0cc.set_xlim(-10,110)
    ax0cc.set_title('CCGT')

    ax1cc.plot(100*CCGT[0:4]/ELEC_TOT[0:4],y_axis[1:5],'o--')
    ax1cc.invert_yaxis()
    ax1cc.xaxis.set_label_position('top')

    ax2cc.plot(100*CCGT[4:8]/ELEC_TOT[4:8],y_axis[5:9],'o--')
    ax2cc.invert_yaxis()
    ax2cc.xaxis.set_label_position('top')

    ax3cc.plot(100*CCGT[8:12]/ELEC_TOT[8:12],y_axis[9:13],'o--')
    ax3cc.invert_yaxis()
    ax3cc.xaxis.set_label_position('top')

    ax4cc.plot(100*CCGT[12:16]/ELEC_TOT[12:16],y_axis[13:17],'o--')
    ax4cc.invert_yaxis()
    ax4cc.xaxis.set_label_position('top')
    
    ax5cc.boxplot(100*CCGT[0:16]/ELEC_TOT[0:16],vert = False)
    ax5cc.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0cc.set_yticklabels([])
        ax1cc.set_yticklabels([])
        ax2cc.set_yticklabels([])
        ax3cc.set_yticklabels([])
        ax4cc.set_yticklabels([])
        ax5cc.set_yticklabels([])
        
    
    COAL_US = COAL_US.flatten()
    graduations = False
    
    ax0us.plot(100*opt_activities[2]/ELEC_OPT_TOT,y_axis[0],'o')
    ax0us.set_xlim(-10,110)
    ax0us.set_title('COAL US')
    


    ax1us.plot(100*COAL_US[0:4]/ELEC_TOT[0:4],y_axis[1:5],'o--')
    ax1us.invert_yaxis()
    ax1us.xaxis.set_label_position('top')

    ax2us.plot(100*COAL_US[4:8]/ELEC_TOT[4:8],y_axis[5:9],'o--')
    ax2us.invert_yaxis()
    ax2us.xaxis.set_label_position('top')

    ax3us.plot(100*COAL_US[8:12]/ELEC_TOT[8:12],y_axis[9:13],'o--')
    ax3us.invert_yaxis()
    ax3us.xaxis.set_label_position('top')

    ax4us.plot(100*COAL_US[12:16]/ELEC_TOT[12:16],y_axis[13:17],'o--')
    ax4us.invert_yaxis()
    ax4us.xaxis.set_label_position('top')
    
    ax5us.boxplot(100*COAL_US[0:16]/ELEC_TOT[0:16],vert = False)
    ax5us.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0us.set_yticklabels([])
        ax1us.set_yticklabels([])
        ax2us.set_yticklabels([])
        ax3us.set_yticklabels([])
        ax4us.set_yticklabels([])
        ax5us.set_yticklabels([])


    PV = PV.flatten()
    
    ax0pv.plot(100*opt_activities[4]/ELEC_OPT_TOT,y_axis[0],'o')
    ax0pv.set_xlim(-10,110)
    ax0pv.set_title('PV')


    ax1pv.plot(100*PV[0:4]/ELEC_TOT[0:4],y_axis[1:5],'o--')
    ax1pv.invert_yaxis()
    ax1pv.xaxis.set_label_position('top')

    ax2pv.plot(100*PV[4:8]/ELEC_TOT[4:8],y_axis[5:9],'o--')
    ax2pv.invert_yaxis()
    ax2pv.xaxis.set_label_position('top')

    ax3pv.plot(100*PV[8:12]/ELEC_TOT[8:12],y_axis[9:13],'o--')
    ax3pv.invert_yaxis()
    ax3pv.xaxis.set_label_position('top')

    ax4pv.plot(100*PV[12:16]/ELEC_TOT[12:16],y_axis[13:17],'o--')
    ax4pv.invert_yaxis()
    ax4pv.xaxis.set_label_position('top')
    
    ax5pv.boxplot(100*PV[0:16]/ELEC_TOT[0:16],vert = False)
    ax5pv.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0pv.set_yticklabels([])
        ax1pv.set_yticklabels([])
        ax2pv.set_yticklabels([])
        ax3pv.set_yticklabels([])
        ax4pv.set_yticklabels([])
        ax5pv.set_yticklabels([])
        
        
    WIND = WIND.flatten()

    ax0wi.plot(100*(opt_activities[5]+opt_activities[6])/ELEC_OPT_TOT,y_axis[0],'o')
    ax0wi.set_xlim(-10,110)
    ax0wi.set_title('WIND TURBINES')


    ax1wi.plot(100*WIND[0:4]/ELEC_TOT[0:4],y_axis[1:5],'o--')
    ax1wi.invert_yaxis()
    ax1wi.xaxis.set_label_position('top')

    ax2wi.plot(100*WIND[4:8]/ELEC_TOT[4:8],y_axis[5:9],'o--')
    ax2wi.invert_yaxis()
    ax2wi.xaxis.set_label_position('top')

    ax3wi.plot(100*WIND[8:12]/ELEC_TOT[8:12],y_axis[9:13],'o--')
    ax3wi.invert_yaxis()
    ax3wi.xaxis.set_label_position('top')

    ax4wi.plot(100*WIND[12:16]/ELEC_TOT[12:16],y_axis[13:17],'o--')
    ax4wi.invert_yaxis()
    ax4wi.xaxis.set_label_position('top')
    
    ax5wi.boxplot(100*WIND[0:16]/ELEC_TOT[0:16],vert = False)
    ax5wi.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0wi.set_yticklabels([])
        ax1wi.set_yticklabels([])
        ax2wi.set_yticklabels([])
        ax3wi.set_yticklabels([])
        ax4wi.set_yticklabels([])
        ax5wi.set_yticklabels([])
        
    ELEC_CHP = ELEC_CHP.flatten()
    
    ax0ch.plot(100*sum(opt_activities[9:12])/ELEC_OPT_TOT,y_axis[0],'o')
    ax0ch.set_xlim(-10,110)
    ax0ch.set_title('CHP_ELEC')

    ax1ch.plot(100*ELEC_CHP[0:4]/ELEC_TOT[0:4],y_axis[1:5],'o--')
    ax1ch.invert_yaxis()
    ax1ch.xaxis.set_label_position('top')

    ax2ch.plot(100*ELEC_CHP[4:8]/ELEC_TOT[4:8],y_axis[5:9],'o--')
    ax2ch.invert_yaxis()
    ax2ch.xaxis.set_label_position('top')

    ax3ch.plot(100*ELEC_CHP[8:12]/ELEC_TOT[8:12],y_axis[9:13],'o--')
    ax3ch.invert_yaxis()
    ax3ch.xaxis.set_label_position('top')

    ax4ch.plot(100*ELEC_CHP[12:16]/ELEC_TOT[12:16],y_axis[13:17],'o--')
    ax4ch.invert_yaxis()
    ax4ch.xaxis.set_label_position('top')
    
    ax5ch.boxplot(100*ELEC_CHP[0:16]/ELEC_TOT[0:16],vert = False)
    ax5ch.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0ch.set_yticklabels([])
        ax1ch.set_yticklabels([])
        ax2ch.set_yticklabels([])
        ax3ch.set_yticklabels([])
        ax4ch.set_yticklabels([])
        ax5ch.set_yticklabels([])
        
    ELEC = ELEC.flatten()

    ax0im.plot(100*opt_res[0]/ELEC_OPT_TOT,y_axis[0],'o')
    ax0im.set_xlim(-10,110)
    ax0im.set_title('IMP. ELEC')


    ax1im.plot(100*np.divide(ELEC[0:4],ELEC_TOT[0:4]),y_axis[1:5],'o--')
    ax1im.invert_yaxis()
    ax1im.xaxis.set_label_position('top')

    ax2im.plot(100*ELEC[4:8]/ELEC_TOT[4:8],y_axis[5:9],'o--')
    ax2im.invert_yaxis()
    ax2im.xaxis.set_label_position('top')

    ax3im.plot(100*ELEC[8:12]/ELEC_TOT[8:12],y_axis[9:13],'o--')
    ax3im.invert_yaxis()
    ax3im.xaxis.set_label_position('top')

    ax4im.plot(100*ELEC[12:16]/ELEC_TOT[12:16],y_axis[13:17],'o--')
    ax4im.invert_yaxis()
    ax4im.xaxis.set_label_position('top')
    
    ax5im.boxplot(100*ELEC[0:16]/ELEC_TOT[0:16],vert = False)
    ax5im.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0im.set_yticklabels([])
        ax1im.set_yticklabels([])
        ax2im.set_yticklabels([])
        ax3im.set_yticklabels([])
        ax4im.set_yticklabels([])
        ax5im.set_yticklabels([])
        
    fig.show()            

#HT

if plot == 'HT_LAYER' :
    
    HT_TOT = HT_TOT.flatten()
    plt.subplots_adjust(hspace = 0.3)
    graduations = True
    
    HT_CHP_GAS = HT_CHP_GAS.flatten()
    fig,((ax0ch_g,ax0ch_o,ax0bo_ww,ax0bo_o,ax0de,ax0em),(ax1ch_g,ax1ch_o,ax1bo_ww,ax1bo_o,ax1de,ax1em),(ax2ch_g,ax2ch_o,ax2bo_ww,ax2bo_o,ax2de,ax2em),(ax3ch_g,ax3ch_o,ax3bo_ww,ax3bo_o,ax3de,ax3em),(ax4ch_g,ax4ch_o,ax4bo_ww,ax4bo_o,ax4de,ax4em),(ax5ch_g,ax5ch_o,ax5bo_ww,ax5bo_o,ax5de,ax5em)) = plt.subplots(6,6,gridspec_kw = {'height_ratios':[1,4,4,4,4,1]},sharex = 'col')

    ax0ch_g.plot(100*HT_OPT_CHP_GAS/HT_OPT_TOT,y_axis[0],'o')
    ax0ch_g.set_xlim(-10,110)
    ax0ch_g.set_title('HT_CHP_GAS')


    ax1ch_g.plot(100*HT_CHP_GAS[0:4]/HT_TOT[0:4],y_axis[1:5],'o--')
    ax1ch_g.invert_yaxis()
    ax1ch_g.xaxis.set_label_position('top')

    ax2ch_g.plot(100*HT_CHP_GAS[4:8]/HT_TOT[4:8],y_axis[5:9],'o--')
    ax2ch_g.invert_yaxis()
    ax2ch_g.xaxis.set_label_position('top')

    ax3ch_g.plot(100*HT_CHP_GAS[8:12]/HT_TOT[8:12],y_axis[9:13],'o--')
    ax3ch_g.invert_yaxis()
    ax3ch_g.xaxis.set_label_position('top')

    ax4ch_g.plot(100*HT_CHP_GAS[12:16]/HT_TOT[12:16],y_axis[13:17],'o--')
    ax4ch_g.invert_yaxis()
    ax4ch_g.xaxis.set_label_position('top')
    
    ax5ch_g.boxplot(100*HT_CHP_GAS[0:16]/HT_TOT[0:16],vert = False)
    ax5ch_g.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0ch_g.set_yticklabels([])
        ax1ch_g.set_yticklabels([])
        ax2ch_g.set_yticklabels([])
        ax3ch_g.set_yticklabels([])
        ax4ch_g.set_yticklabels([])
        ax5ch_g.set_yticklabels([])
        
    HT_CHP_OTHER = HT_CHP_OTHER.flatten()
    graduations = False

    ax0ch_o.plot(100*HT_OPT_CHP_OTHER/HT_OPT_TOT,y_axis[0],'o')
    ax0ch_o.set_xlim(-10,110)
    ax0ch_o.set_title('HT_CHP_OTHER')

    ax1ch_o.plot(100*HT_CHP_OTHER[0:4]/HT_TOT[0:4],y_axis[1:5],'o--')
    ax1ch_o.invert_yaxis()
    ax1ch_o.xaxis.set_label_position('top')

    ax2ch_o.plot(100*HT_CHP_OTHER[4:8]/HT_TOT[4:8],y_axis[5:9],'o--')
    ax2ch_o.invert_yaxis()
    ax2ch_o.xaxis.set_label_position('top')

    ax3ch_o.plot(100*HT_CHP_OTHER[8:12]/HT_TOT[8:12],y_axis[9:13],'o--')
    ax3ch_o.invert_yaxis()
    ax3ch_o.xaxis.set_label_position('top')

    ax4ch_o.plot(100*HT_CHP_OTHER[12:16]/HT_TOT[12:16],y_axis[13:17],'o--')
    ax4ch_o.invert_yaxis()
    ax4ch_o.xaxis.set_label_position('top')
    
    ax5ch_o.boxplot(100*HT_CHP_OTHER[0:16]/HT_TOT[0:16],vert = False)
    ax5ch_o.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0ch_o.set_yticklabels([])
        ax1ch_o.set_yticklabels([])
        ax2ch_o.set_yticklabels([])
        ax3ch_o.set_yticklabels([])
        ax4ch_o.set_yticklabels([])
        ax5ch_o.set_yticklabels([])
        
    HT_BOILER_WOOD_WASTE = HT_BOILER_WOOD_WASTE.flatten()

    ax0bo_ww.plot(100*HT_OPT_WOOD_WASTE/HT_OPT_TOT,y_axis[0],'o')
    ax0bo_ww.set_xlim(-10,110)
    ax0bo_ww.set_title('HT_BOILER_WOOD+WASTE')
    
    ax1bo_ww.plot(100*HT_BOILER_WOOD_WASTE[0:4]/HT_TOT[0:4],y_axis[1:5],'o--')
    ax1bo_ww.invert_yaxis()
    ax1bo_ww.xaxis.set_label_position('top')

    ax2bo_ww.plot(100*HT_BOILER_WOOD_WASTE[4:8]/HT_TOT[4:8],y_axis[5:9],'o--')
    ax2bo_ww.invert_yaxis()
    ax2bo_ww.xaxis.set_label_position('top')

    ax3bo_ww.plot(100*HT_BOILER_WOOD_WASTE[8:12]/HT_TOT[8:12],y_axis[9:13],'o--')
    ax3bo_ww.invert_yaxis()
    ax3bo_ww.xaxis.set_label_position('top')

    ax4bo_ww.plot(100*HT_BOILER_WOOD_WASTE[12:16]/HT_TOT[12:16],y_axis[13:17],'o--')
    ax4bo_ww.invert_yaxis()
    ax4bo_ww.xaxis.set_label_position('top')
    
    ax5bo_ww.boxplot(100*HT_BOILER_WOOD_WASTE[0:16]/HT_TOT[0:16],vert = False)
    ax5bo_ww.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0bo_ww.set_yticklabels([])
        ax1bo_ww.set_yticklabels([])
        ax2bo_ww.set_yticklabels([])
        ax3bo_ww.set_yticklabels([])
        ax4bo_ww.set_yticklabels([])
        ax5bo_ww.set_yticklabels([])
        
    HT_BOILER_OTHER = HT_BOILER_OTHER.flatten()

    ax0bo_o.plot(100*HT_OPT_BOILER_OTHER/HT_OPT_TOT,y_axis[0],'o')
    ax0bo_o.set_xlim(-10,110)
    ax0bo_o.set_title('HT_BOILER_OTHER')
    
    ax1bo_o.plot(100*HT_BOILER_OTHER[0:4]/HT_TOT[0:4],y_axis[1:5],'o--')
    ax1bo_o.invert_yaxis()
    ax1bo_o.xaxis.set_label_position('top')

    ax2bo_o.plot(100*HT_BOILER_OTHER[4:8]/HT_TOT[4:8],y_axis[5:9],'o--')
    ax2bo_o.invert_yaxis()
    ax2bo_o.xaxis.set_label_position('top')

    ax3bo_o.plot(100*HT_BOILER_OTHER[8:12]/HT_TOT[8:12],y_axis[9:13],'o--')
    ax3bo_o.invert_yaxis()
    ax3bo_o.xaxis.set_label_position('top')

    ax4bo_o.plot(100*HT_BOILER_OTHER[12:16]/HT_TOT[12:16],y_axis[13:17],'o--')
    ax4bo_o.invert_yaxis()
    ax4bo_o.xaxis.set_label_position('top')
    
    ax5bo_o.boxplot(100*HT_BOILER_OTHER[0:16]/HT_TOT[0:16],vert = False)
    ax5bo_o.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0bo_o.set_yticklabels([])
        ax1bo_o.set_yticklabels([])
        ax2bo_o.set_yticklabels([])
        ax3bo_o.set_yticklabels([])
        ax4bo_o.set_yticklabels([])
        ax5bo_o.set_yticklabels([])
        
    HT_DIRECT_ELEC = HT_DIRECT_ELEC.flatten()

    ax0de.plot(100*HT_OPT_DIRECT_ELEC/HT_OPT_TOT,y_axis[0],'o')
    ax0de.set_xlim(-10,110)
    ax0de.set_title('HT_DIRECT_ELEC')
    
    ax1de.plot(100*HT_DIRECT_ELEC[0:4]/HT_TOT[0:4],y_axis[1:5],'o--')
    ax1de.invert_yaxis()
    ax1de.xaxis.set_label_position('top')

    ax2de.plot(100*HT_DIRECT_ELEC[4:8]/HT_TOT[4:8],y_axis[5:9],'o--')
    ax2de.invert_yaxis()
    ax2de.xaxis.set_label_position('top')

    ax3de.plot(100*HT_DIRECT_ELEC[8:12]/HT_TOT[8:12],y_axis[9:13],'o--')
    ax3de.invert_yaxis()
    ax3de.xaxis.set_label_position('top')

    ax4de.plot(100*HT_DIRECT_ELEC[12:16]/HT_TOT[12:16],y_axis[13:17],'o--')
    ax4de.invert_yaxis()
    ax4de.xaxis.set_label_position('top')
    
    ax5de.boxplot(100*HT_DIRECT_ELEC[0:16]/HT_TOT[0:16],vert = False)
    ax5de.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0de.set_yticklabels([])
        ax1de.set_yticklabels([])
        ax2de.set_yticklabels([])
        ax3de.set_yticklabels([])
        ax4de.set_yticklabels([])
        ax5de.set_yticklabels([])
        
    emissions = np.concatenate(([opt_emissions],emissions.flatten()))

    ax0em.plot(100,y_axis[0],'o')
    ax0em.set_xlim(25,175)
    ax0em.set_title('CO2')


    ax1em.plot(100*emissions[1:5]/opt_emissions,y_axis[1:5],'o--')
    ax1em.invert_yaxis()
    ax1em.xaxis.set_label_position('top')
    

    ax2em.plot(100*emissions[5:9]/opt_emissions,y_axis[5:9],'o--')
    ax2em.invert_yaxis()
    ax2em.xaxis.set_label_position('top')
   

    ax3em.plot(100*emissions[9:13]/opt_emissions,y_axis[9:13],'o--')
    ax3em.invert_yaxis()
    ax3em.xaxis.set_label_position('top')
    

    ax4em.plot(100*emissions[13:17]/opt_emissions,y_axis[13:17],'o--')
    ax4em.invert_yaxis()
    ax4em.xaxis.set_label_position('top')
    
    
    ax5em.boxplot(100*emissions[1:17]/opt_emissions,vert = False)
    ax5em.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0em.set_yticklabels([])
        ax1em.set_yticklabels([])
        ax2em.set_yticklabels([])
        ax3em.set_yticklabels([])
        ax4em.set_yticklabels([])
        ax5em.set_yticklabels([])

    
    fig.show()
    
    
## LT HEAT ##  

if plot == 'LT_LAYER' :
    LT_TOT = LT_TOT.flatten()
    
    LT_CHP = LT_CHP.flatten()
    graduations = True
    figLT,((ax0c,ax0b,ax0hp,ax0hp_el,ax0ot),(ax1c,ax1b,ax1hp,ax1hp_el,ax1ot),(ax2c,ax2b,ax2hp,ax2hp_el,ax2ot),(ax3c,ax3b,ax3hp,ax3hp_el,ax3ot),(ax4c,ax4b,ax4hp,ax4hp_el,ax4ot),(ax5c,ax5b,ax5hp,ax5hp_el,ax5ot)) = plt.subplots(6,5,gridspec_kw = {'height_ratios':[1,4,4,4,4,1]},sharex = 'col',sharey = False)
    plt.subplots_adjust(hspace = 0.3)
    
    ax0c.plot(100*LT_OPT_CHP/LT_OPT_TOT,y_axis[0],'o')
    ax0c.set_xlim(-10,110)
    ax0c.set_title('LT_CHP')
    
    ax1c.plot(100*LT_CHP[0:4]/LT_TOT[0:4],y_axis[1:5],'o--')
    ax1c.invert_yaxis()
    ax1c.xaxis.set_label_position('top')
    

    ax2c.plot(100*LT_CHP[4:8]/LT_TOT[4:8],y_axis[5:9],'o--')
    ax2c.invert_yaxis()
    ax2c.xaxis.set_label_position('top')

    ax3c.plot(100*LT_CHP[8:12]/LT_TOT[8:12],y_axis[9:13],'o--')
    ax3c.invert_yaxis()
    ax3c.xaxis.set_label_position('top')

    ax4c.plot(100*LT_CHP[12:16]/LT_TOT[12:16],y_axis[13:17],'o--')
    ax4c.invert_yaxis()
    ax4c.xaxis.set_label_position('top')
    
    ax5c.boxplot(100*LT_CHP[0:16]/LT_TOT[0:16],vert = False)
    ax5c.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0c.set_yticklabels([])
        ax1c.set_yticklabels([])
        ax2c.set_yticklabels([])
        ax3c.set_yticklabels([])
        ax4c.set_yticklabels([])

    
    LT_BOILER = LT_BOILER.flatten()
    graduations = False
   

    ax0b.plot(100*LT_OPT_BOILER/LT_OPT_TOT,y_axis[0],'o')
    ax0b.set_xlim(-10,110)
    ax0b.set_title('LT_BOILER')
    


    ax1b.plot(100*LT_BOILER[0:4]/LT_TOT[0:4],y_axis[1:5],'o--')
    ax1b.invert_yaxis()
    ax1b.xaxis.set_label_position('top')

    ax2b.plot(100*LT_BOILER[4:8]/LT_TOT[4:8],y_axis[5:9],'o--')
    ax2b.invert_yaxis()
    ax2b.xaxis.set_label_position('top')

    ax3b.plot(100*LT_BOILER[8:12]/LT_TOT[8:12],y_axis[9:13],'o--')
    ax3b.invert_yaxis()
    ax3b.xaxis.set_label_position('top')

    ax4b.plot(100*LT_BOILER[12:16]/LT_TOT[12:16],y_axis[13:17],'o--')
    ax4b.invert_yaxis()
    ax4b.xaxis.set_label_position('top')
    
    ax5b.boxplot(100*LT_BOILER[0:16]/LT_TOT[0:16],vert = False)
    ax5b.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0b.set_yticklabels([])
        ax1b.set_yticklabels([])
        ax2b.set_yticklabels([])
        ax3b.set_yticklabels([])
        ax4b.set_yticklabels([])
        ax5b.set_yticklabels([])
    
    
    LT_HP_GAS = LT_HP_GAS.flatten()

    ax0hp.plot(100*LT_OPT_HP_GAS/LT_OPT_TOT,y_axis[0],'o')
    ax0hp.set_xlim(-10,110)
    ax0hp.set_title('LT_HP_GAS')
    


    ax1hp.plot(100*LT_HP_GAS[0:4]/LT_TOT[0:4],y_axis[1:5],'o--')
    ax1hp.invert_yaxis()
    ax1hp.xaxis.set_label_position('top')

    ax2hp.plot(100*LT_HP_GAS[4:8]/LT_TOT[4:8],y_axis[5:9],'o--')
    ax2hp.invert_yaxis()
    ax2hp.xaxis.set_label_position('top')

    ax3hp.plot(100*LT_HP_GAS[8:12]/LT_TOT[8:12],y_axis[9:13],'o--')
    ax3hp.invert_yaxis()
    ax3hp.xaxis.set_label_position('top')

    ax4hp.plot(100*LT_HP_GAS[12:16]/LT_TOT[12:16],y_axis[13:17],'o--')
    ax4hp.invert_yaxis()
    ax4hp.xaxis.set_label_position('top')
    
    ax5hp.boxplot(100*LT_HP_GAS[0:16]/LT_TOT[0:16],vert=False)
    ax5hp.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0hp.set_yticklabels([])
        ax1hp.set_yticklabels([])
        ax2hp.set_yticklabels([])
        ax3hp.set_yticklabels([])
        ax4hp.set_yticklabels([])
        ax5hp.set_yticklabels([])
        
    
    LT_HP_ELEC = LT_HP_ELEC.flatten()

    ax0hp_el.plot(100*LT_OPT_HP_ELEC/LT_OPT_TOT,y_axis[0],'o')
    ax0hp_el.set_xlim(-10,110)
    ax0hp_el.set_title('LT_HP_ELEC')
    


    ax1hp_el.plot(100*LT_HP_ELEC[0:4]/LT_TOT[0:4],y_axis[1:5],'o--')
    ax1hp_el.invert_yaxis()
    ax1hp_el.xaxis.set_label_position('top')

    ax2hp_el.plot(100*LT_HP_ELEC[4:8]/LT_TOT[4:8],y_axis[5:9],'o--')
    ax2hp_el.invert_yaxis()
    ax2hp_el.xaxis.set_label_position('top')

    ax3hp_el.plot(100*LT_HP_ELEC[8:12]/LT_TOT[8:12],y_axis[9:13],'o--')
    ax3hp_el.invert_yaxis()
    ax3hp_el.xaxis.set_label_position('top')

    ax4hp_el.plot(100*LT_HP_ELEC[12:16]/LT_TOT[12:16],y_axis[13:17],'o--')
    ax4hp_el.invert_yaxis()
    ax4hp_el.xaxis.set_label_position('top')
    
    ax5hp_el.boxplot(100*LT_HP_ELEC[0:16]/LT_TOT[0:16],vert=False)
    ax5hp_el.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0hp_el.set_yticklabels([])
        ax1hp_el.set_yticklabels([])
        ax2hp_el.set_yticklabels([])
        ax3hp_el.set_yticklabels([])
        ax4hp_el.set_yticklabels([])
        ax5hp_el.set_yticklabels([])
        
    LT_OTHER = LT_OTHER.flatten()

    ax0ot.plot(100*LT_OPT_OTHER/LT_OPT_TOT,y_axis[0],'o')
    ax0ot.set_xlim(-10,110)
    ax0ot.set_title('LT_OTHER')

    ax1ot.plot(100*LT_OTHER[0:4]/LT_TOT[0:4],y_axis[1:5],'o--')
    ax1ot.invert_yaxis()
    ax1ot.xaxis.set_label_position('top')

    ax2ot.plot(100*LT_OTHER[4:8]/LT_TOT[4:8],y_axis[5:9],'o--')
    ax2ot.invert_yaxis()
    ax2ot.xaxis.set_label_position('top')

    ax3ot.plot(100*LT_OTHER[8:12]/LT_TOT[8:12],y_axis[9:13],'o--')
    ax3ot.invert_yaxis()
    ax3ot.xaxis.set_label_position('top')

    ax4ot.plot(100*LT_OTHER[12:16]/LT_TOT[12:16],y_axis[13:17],'o--')
    ax4ot.invert_yaxis()
    ax4ot.xaxis.set_label_position('top')
    
    ax5ot.boxplot(100*LT_OTHER[0:16]/LT_TOT[0:16],vert = False)
    ax5ot.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0ot.set_yticklabels([])
        ax1ot.set_yticklabels([])
        ax2ot.set_yticklabels([])
        ax3ot.set_yticklabels([])
        ax4ot.set_yticklabels([])
        ax5ot.set_yticklabels([])
        
    
    figLT.show()
    
#Resources
    
if plot == 'RES_LAYER' :
    
    RES_TOT = RES_TOT.flatten()
    graduations = True
    GASOLINE = GASOLINE.flatten()
    fig,((ax0ga,ax0di,ax0et,ax0bi,ax0lf,ax0ng,ax0wo),(ax1ga,ax1di,ax1et,ax1bi,ax1lf,ax1ng,ax1wo),(ax2ga,ax2di,ax2et,ax2bi,ax2lf,ax2ng,ax2wo),(ax3ga,ax3di,ax3et,ax3bi,ax3lf,ax3ng,ax3wo),(ax4ga,ax4di,ax4et,ax4bi,ax4lf,ax4ng,ax4wo),(ax5ga,ax5di,ax5et,ax5bi,ax5lf,ax5ng,ax5wo)) = plt.subplots(6,7,gridspec_kw = {'height_ratios':[1,4,4,4,4,1]},sharex = True)

    ax0ga.plot(100*opt_res[1]/RES_TOT_opt,y_axis[0],'o')
    ax0ga.set_xlim(-10,110)
    ax0ga.set_title('GASOLINE')


    ax1ga.plot(100*np.divide(GASOLINE[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1ga.invert_yaxis()
    ax1ga.xaxis.set_label_position('top')

    ax2ga.plot(100*GASOLINE[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2ga.invert_yaxis()
    ax2ga.xaxis.set_label_position('top')

    ax3ga.plot(100*GASOLINE[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3ga.invert_yaxis()
    ax3ga.xaxis.set_label_position('top')

    ax4ga.plot(100*GASOLINE[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4ga.invert_yaxis()
    ax4ga.xaxis.set_label_position('top')
    
    ax5ga.boxplot(100*GASOLINE[0:16]/RES_TOT[0:16],vert = False)
    ax5ga.set_yticklabels(['boxplot'])
    
    if graduations == False :
        ax0ga.set_yticklabels([])
        ax1ga.set_yticklabels([])
        ax2ga.set_yticklabels([])
        ax3ga.set_yticklabels([])
        ax4ga.set_yticklabels([])
        ax5ga.set_yticklabels([])
        
    
    DIESEL = DIESEL.flatten()
    graduations = False
    ax0di.plot(100*opt_res[2]/RES_TOT_opt,y_axis[0],'o')
    ax0di.set_xlim(-10,110)
    ax0di.set_title('DIESEL')


    ax1di.plot(100*np.divide(DIESEL[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1di.invert_yaxis()
    ax1di.xaxis.set_label_position('top')

    ax2di.plot(100*DIESEL[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2di.invert_yaxis()
    ax2di.xaxis.set_label_position('top')

    ax3di.plot(100*DIESEL[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3di.invert_yaxis()
    ax3di.xaxis.set_label_position('top')

    ax4di.plot(100*DIESEL[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4di.invert_yaxis()
    ax4di.xaxis.set_label_position('top')
    
    ax5di.boxplot(100*DIESEL[0:16]/RES_TOT[0:16],vert = False)
    
    if graduations == False :
        ax0di.set_yticklabels([])
        ax1di.set_yticklabels([])
        ax2di.set_yticklabels([])
        ax3di.set_yticklabels([])
        ax4di.set_yticklabels([])
        ax5di.set_yticklabels([])
        
    BIOETHANOL = BIOETHANOL.flatten()

    ax0et.plot(100*opt_res[3]/RES_TOT_opt,y_axis[0],'o')
    ax0et.set_xlim(-10,110)
    ax0et.set_title('BIOETHANOL')


    ax1et.plot(100*np.divide(BIOETHANOL[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1et.invert_yaxis()
    ax1et.xaxis.set_label_position('top')

    ax2et.plot(100*BIOETHANOL[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2et.invert_yaxis()
    ax2et.xaxis.set_label_position('top')

    ax3et.plot(100*BIOETHANOL[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3et.invert_yaxis()
    ax3et.xaxis.set_label_position('top')

    ax4et.plot(100*BIOETHANOL[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4et.invert_yaxis()
    ax4et.xaxis.set_label_position('top')
    
    ax5et.boxplot(100*BIOETHANOL[0:16]/RES_TOT[0:16],vert = False)

    
    if graduations == False :
        ax0et.set_yticklabels([])
        ax1et.set_yticklabels([])
        ax2et.set_yticklabels([])
        ax3et.set_yticklabels([])
        ax4et.set_yticklabels([])
        ax5et.set_yticklabels([])
        
    BIODIESEL = BIODIESEL.flatten()

    ax0bi.plot(100*opt_res[4]/RES_TOT_opt,y_axis[0],'o')
    ax0bi.set_xlim(-10,110)
    ax0bi.set_title('BIODIESEL')


    ax1bi.plot(100*np.divide(BIODIESEL[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1bi.invert_yaxis()
    ax1bi.xaxis.set_label_position('top')

    ax2bi.plot(100*BIODIESEL[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2bi.invert_yaxis()
    ax2bi.xaxis.set_label_position('top')

    ax3bi.plot(100*BIODIESEL[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3bi.invert_yaxis()
    ax3bi.xaxis.set_label_position('top')

    ax4bi.plot(100*BIODIESEL[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4bi.invert_yaxis()
    ax4bi.xaxis.set_label_position('top')
    
    ax5bi.boxplot(100*BIODIESEL[0:16]/RES_TOT[0:16],vert = False)

    
    if graduations == False :
        ax0bi.set_yticklabels([])
        ax1bi.set_yticklabels([])
        ax2bi.set_yticklabels([])
        ax3bi.set_yticklabels([])
        ax4bi.set_yticklabels([])
        ax5bi.set_yticklabels([])
        
    LFO = LFO.flatten()

    ax0lf.plot(100*opt_res[5]/RES_TOT_opt,y_axis[0],'o')
    ax0lf.set_xlim(-10,110)
    ax0lf.set_title('LFO')


    ax1lf.plot(100*np.divide(LFO[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1lf.invert_yaxis()
    ax1lf.xaxis.set_label_position('top')

    ax2lf.plot(100*LFO[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2lf.invert_yaxis()
    ax2lf.xaxis.set_label_position('top')

    ax3lf.plot(100*LFO[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3lf.invert_yaxis()
    ax3lf.xaxis.set_label_position('top')

    ax4lf.plot(100*LFO[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4lf.invert_yaxis()
    ax4lf.xaxis.set_label_position('top')
    
    ax5lf.boxplot(100*LFO[0:16]/RES_TOT[0:16],vert = False)
    
    
    if graduations == False :
        ax0lf.set_yticklabels([])
        ax1lf.set_yticklabels([])
        ax2lf.set_yticklabels([])
        ax3lf.set_yticklabels([])
        ax4lf.set_yticklabels([])
        ax5lf.set_yticklabels([])
        
    NG = NG.flatten()

    ax0ng.plot(100*opt_res[6]/RES_TOT_opt,y_axis[0],'o')
    ax0ng.set_xlim(-10,110)
    ax0ng.set_title('NG')


    ax1ng.plot(100*np.divide(NG[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1ng.invert_yaxis()
    ax1ng.xaxis.set_label_position('top')

    ax2ng.plot(100*NG[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2ng.invert_yaxis()
    ax2ng.xaxis.set_label_position('top')

    ax3ng.plot(100*NG[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3ng.invert_yaxis()
    ax3ng.xaxis.set_label_position('top')

    ax4ng.plot(100*NG[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4ng.invert_yaxis()
    ax4ng.xaxis.set_label_position('top')
    
    ax5ng.boxplot(100*NG[0:16]/RES_TOT[0:16],vert = False)
    
    if graduations == False :
        ax0ng.set_yticklabels([])
        ax1ng.set_yticklabels([])
        ax2ng.set_yticklabels([])
        ax3ng.set_yticklabels([])
        ax4ng.set_yticklabels([])
        ax5ng.set_yticklabels([])
        
    WOOD = WOOD.flatten()

    ax0wo.plot(100*opt_res[9]/RES_TOT_opt,y_axis[0],'o')
    ax0wo.set_xlim(-10,110)
    ax0wo.set_title('WOOD')


    ax1wo.plot(100*np.divide(WOOD[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1wo.invert_yaxis()
    ax1wo.xaxis.set_label_position('top')

    ax2wo.plot(100*WOOD[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2wo.invert_yaxis()
    ax2wo.xaxis.set_label_position('top')

    ax3wo.plot(100*WOOD[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3wo.invert_yaxis()
    ax3wo.xaxis.set_label_position('top')

    ax4wo.plot(100*WOOD[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4wo.invert_yaxis()
    ax4wo.xaxis.set_label_position('top')
    
    ax5wo.boxplot(100*WOOD[0:16]/RES_TOT[0:16],vert = False)
    
    if graduations == False :
        ax0wo.set_yticklabels([])
        ax1wo.set_yticklabels([])
        ax2wo.set_yticklabels([])
        ax3wo.set_yticklabels([])
        ax4wo.set_yticklabels([])
        ax5wo.set_yticklabels([])

    fig.show()


    
    
if plot == 'WET_BIOMASS' :
    RES_TOT = RES_TOT.flatten()
    WET_BIOMASS = WET_BIOMASS.flatten()
    fig,(ax0,ax1,ax2,ax3,ax4) = plt.subplots(5,gridspec_kw = {'height_ratios':[1,4,4,4,4]},sharex = True)

    ax0.plot(100*opt_res[10]/RES_TOT_opt,y_axis[0],'o')
    ax0.set_xlim(-10,110)
    ax0.set_xticks(ticks = [0,50,100])


    ax1.plot(100*np.divide(WET_BIOMASS[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1.invert_yaxis()
    ax1.xaxis.set_label_position('top')

    ax2.plot(100*WET_BIOMASS[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2.invert_yaxis()
    ax2.xaxis.set_label_position('top')

    ax3.plot(100*WET_BIOMASS[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3.invert_yaxis()
    ax3.xaxis.set_label_position('top')

    ax4.plot(100*WET_BIOMASS[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4.invert_yaxis()
    ax4.xaxis.set_label_position('top')
    
    if graduations == False :
        ax0.set_yticklabels([])
        ax1.set_yticklabels([])
        ax2.set_yticklabels([])
        ax3.set_yticklabels([])
        ax4.set_yticklabels([])

    fig.suptitle('WET_BIOMASS')
    plt.subplots_adjust(left = 0.46,right = 0.54,hspace = 0.3)
    plt.show()
    
if plot == 'COAL' :
    RES_TOT = RES_TOT.flatten()
    COAL = COAL.flatten()
    fig,(ax0,ax1,ax2,ax3,ax4) = plt.subplots(5,gridspec_kw = {'height_ratios':[1,4,4,4,4]},sharex = True)

    ax0.plot(100*opt_res[11]/RES_TOT_opt,y_axis[0],'o')
    ax0.set_xlim(-10,110)
    ax0.set_xticks(ticks = [0,50,100])


    ax1.plot(100*np.divide(COAL[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1.invert_yaxis()
    ax1.xaxis.set_label_position('top')

    ax2.plot(100*COAL[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2.invert_yaxis()
    ax2.xaxis.set_label_position('top')

    ax3.plot(100*COAL[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3.invert_yaxis()
    ax3.xaxis.set_label_position('top')

    ax4.plot(100*COAL[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4.invert_yaxis()
    ax4.xaxis.set_label_position('top')
    
    if graduations == False :
        ax0.set_yticklabels([])
        ax1.set_yticklabels([])
        ax2.set_yticklabels([])
        ax3.set_yticklabels([])
        ax4.set_yticklabels([])

    fig.suptitle('COAL')
    plt.subplots_adjust(left = 0.46,right = 0.54,hspace = 0.3)
    plt.show() 

if plot == 'WASTE' :
    RES_TOT = RES_TOT.flatten()
    WASTE = WASTE.flatten()
    fig,(ax0,ax1,ax2,ax3,ax4) = plt.subplots(5,gridspec_kw = {'height_ratios':[1,4,4,4,4]},sharex = True)

    ax0.plot(100*opt_res[13]/RES_TOT_opt,y_axis[0],'o')
    ax0.set_xlim(-10,110)
    ax0.set_xticks(ticks = [0,50,100])


    ax1.plot(100*np.divide(WASTE[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1.invert_yaxis()
    ax1.xaxis.set_label_position('top')

    ax2.plot(100*WASTE[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2.invert_yaxis()
    ax2.xaxis.set_label_position('top')

    ax3.plot(100*WASTE[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3.invert_yaxis()
    ax3.xaxis.set_label_position('top')

    ax4.plot(100*WASTE[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4.invert_yaxis()
    ax4.xaxis.set_label_position('top')
    
    if graduations == False :
        ax0.set_yticklabels([])
        ax1.set_yticklabels([])
        ax2.set_yticklabels([])
        ax3.set_yticklabels([])
        ax4.set_yticklabels([])

    fig.suptitle('WASTE')
    plt.subplots_adjust(left = 0.46,right = 0.54,hspace = 0.3)
    plt.show()
    
if plot == 'RES_WIND' :
    RES_TOT = RES_TOT.flatten()
    RES_WIND = RES_WIND.flatten()
    fig,(ax0,ax1,ax2,ax3,ax4) = plt.subplots(5,gridspec_kw = {'height_ratios':[1,4,4,4,4]},sharex = True)

    ax0.plot(100*opt_res[17]/RES_TOT_opt,y_axis[0],'o')
    ax0.set_xlim(-10,110)
    ax0.set_xticks(ticks = [0,50,100])


    ax1.plot(100*np.divide(RES_WIND[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1.invert_yaxis()
    ax1.xaxis.set_label_position('top')

    ax2.plot(100*RES_WIND[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2.invert_yaxis()
    ax2.xaxis.set_label_position('top')

    ax3.plot(100*RES_WIND[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3.invert_yaxis()
    ax3.xaxis.set_label_position('top')

    ax4.plot(100*RES_WIND[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4.invert_yaxis()
    ax4.xaxis.set_label_position('top')
    
    if graduations == False :
        ax0.set_yticklabels([])
        ax1.set_yticklabels([])
        ax2.set_yticklabels([])
        ax3.set_yticklabels([])
        ax4.set_yticklabels([])

    fig.suptitle('RES_WIND')
    plt.subplots_adjust(left = 0.46,right = 0.54,hspace = 0.3)
    plt.show()
    
if plot == 'RES_SOLAR' :
    RES_TOT = RES_TOT.flatten()
    RES_SOLAR = RES_SOLAR.flatten()
    fig,(ax0,ax1,ax2,ax3,ax4) = plt.subplots(5,gridspec_kw = {'height_ratios':[1,4,4,4,4]},sharex = True)

    ax0.plot(100*opt_res[18]/RES_TOT_opt,y_axis[0],'o')
    ax0.set_xlim(-10,110)
    ax0.set_xticks(ticks = [0,50,100])


    ax1.plot(100*np.divide(RES_SOLAR[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1.invert_yaxis()
    ax1.xaxis.set_label_position('top')

    ax2.plot(100*RES_SOLAR[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2.invert_yaxis()
    ax2.xaxis.set_label_position('top')

    ax3.plot(100*RES_SOLAR[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3.invert_yaxis()
    ax3.xaxis.set_label_position('top')

    ax4.plot(100*RES_SOLAR[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4.invert_yaxis()
    ax4.xaxis.set_label_position('top')
    
    if graduations == False :
        ax0.set_yticklabels([])
        ax1.set_yticklabels([])
        ax2.set_yticklabels([])
        ax3.set_yticklabels([])
        ax4.set_yticklabels([])
       
   
    fig.suptitle('RES_SOLAR')
    plt.subplots_adjust(left = 0.46,right = 0.54,hspace = 0.3)
    plt.show()
    
if plot == 'RES_HYDRO' :
    RES_TOT = RES_TOT.flatten()
    RES_HYDRO = RES_HYDRO.flatten()
    fig,(ax0,ax1,ax2,ax3,ax4) = plt.subplots(5,gridspec_kw = {'height_ratios':[1,4,4,4,4]},sharex = True)

    ax0.plot(100*opt_res[19]/RES_TOT_opt,y_axis[0],'o')
    ax0.set_xlim(-10,110)
    ax0.set_xticks(ticks = [0,50,100])


    ax1.plot(100*np.divide(RES_HYDRO[0:4],RES_TOT[0:4]),y_axis[1:5],'o--')
    ax1.invert_yaxis()
    ax1.xaxis.set_label_position('top')

    ax2.plot(100*RES_HYDRO[4:8]/RES_TOT[4:8],y_axis[5:9],'o--')
    ax2.invert_yaxis()
    ax2.xaxis.set_label_position('top')

    ax3.plot(100*RES_HYDRO[8:12]/RES_TOT[8:12],y_axis[9:13],'o--')
    ax3.invert_yaxis()
    ax3.xaxis.set_label_position('top')

    ax4.plot(100*RES_HYDRO[12:16]/RES_TOT[12:16],y_axis[13:17],'o--')
    ax4.invert_yaxis()
    ax4.xaxis.set_label_position('top')
    
    if graduations == False :
        ax0.set_yticklabels([])
        ax1.set_yticklabels([])
        ax2.set_yticklabels([])
        ax3.set_yticklabels([])
        ax4.set_yticklabels([])
       
   
    fig.suptitle('RES_HYDRO')
    plt.subplots_adjust(left = 0.46,right = 0.54,hspace = 0.3)
    plt.show()