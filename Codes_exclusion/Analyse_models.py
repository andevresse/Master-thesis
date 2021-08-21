# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:04:48 2021

@author: DD
"""
import numpy as np
import matplotlib.pyplot as plt
from Analyse_funct import get_Master, filter_with, filter_without, get_modif_table, plot_hist,get_to_plot, plot_compare,filter_least_in, results_with, results_least_in,plot_box,get_en_cp,results_without,get_E_produced,get_Elec_layer

path_asset = 'pareto\\CO2emissions40000\\technologies.txt'
technologies = np.genfromtxt(path_asset,skip_header=2,usecols=0,dtype=str)
technologies = technologies[0:len(technologies)-3]
cp = np.genfromtxt(path_asset,skip_header = 2,usecols = 7)
cp=cp[0:len(cp)-3]
f_tech = np.genfromtxt(path_asset,skip_header = 2,usecols = 2)
f_tech=f_tech[0:len(f_tech)-3]


#liste des tech installées dans ref
tech_ref = technologies[f_tech!=0].tolist()
f_ref = f_tech[f_tech!=0].tolist()
tech_unused = technologies
for x in tech_ref:   
    tech_unused = np.delete(tech_unused,np.where(tech_unused==x))

Master_diff=get_Master()  



# Master_diff[0][0].remove('TRAIN_FREIGHT')
# Master_diff[3][0].remove('TRUCK_NG')                     
# Master_diff[2][0].remove('TRUCK_NG')     

Liste_in = []
Liste_out = []
# Gros_tableau = filter_with(Liste_in,Master_diff)
# tab = filter_without(Liste_out,Gros_tableau)
tab = results_with(Liste_in,filter_without([],filter_with([], Master_diff)))
ntab=[]
for j in tab:
    ntab.append(Master_diff.index(j))
print(ntab)
modif_tabs = get_modif_table(tab)
modif_tab = modif_tabs[0]
select_num = modif_tabs[1]
modif_tab_rel = modif_tabs[2]    

rE = get_E_produced(1, 'ref', 40)/get_Elec_layer('ref', 40)

# print(Master_diff.index(tab[6]))
lj=np.array([])
vtp = np.array([])
list_str = np.array([])
toplot = 30

for j in tab:
    if technologies[toplot] in j[1]:
        list_str = np.append(list_str,Master_diff.index(j))
        lj = np.append(lj,j)
        vtp = np.append(vtp,j[2][j[1].index(technologies[toplot])])
toplot = np.zeros(len(list_str))
# i=0
# for n in list_str:
#     En=get_E_produced(1, n, 40)
#     El=get_Elec_layer(n, 40)
#     toplot[i]=En/El
#     i=i+1
# plot_box(toplot, '6')
# # print(len(vtp)/len(tab))

# lj1=np.array([])
# vtp1 = np.array([])
# list_str1 = np.array([])
# toplot = 10

# for j in tab:
#     if technologies[toplot] in j[1]:
#         list_str1 = np.append(list_str1,Master_diff.index(j))
#         lj1 = np.append(lj1,j)
#         vtp1 = np.append(vtp1,j[2][j[1].index(technologies[toplot])])
# print(len(vtp1)/len(tab))


# lj2=np.array([])
# vtp2 = np.array([])
# list_str2 = np.array([])
# toplot = 11

# for j in tab:
#     if technologies[toplot] in j[1]:
#         list_str2 = np.append(list_str2,Master_diff.index(j))
#         lj2 = np.append(lj2,j)
#         vtp2 = np.append(vtp2,j[2][j[1].index(technologies[toplot])])
# print(len(vtp2)/len(tab))

# lj3=np.array([])
# vtp3 = np.array([])
# list_str3 = np.array([])
# toplot = 16

# for j in tab:
#     if technologies[toplot] in j[1]:
#         list_str3 = np.append(list_str3,Master_diff.index(j))
#         lj3 = np.append(lj3,j)
#         vtp3 = np.append(vtp3,j[2][j[1].index(technologies[toplot])])

# print(len(vtp3)/len(tab))  


# lj4=np.array([])      
# vtp4 = np.array([])
# list_str4 = np.array([])
# toplot = 17

# for j in tab:
#     if technologies[toplot] in j[1]:
#         list_str4 = np.append(list_str4,Master_diff.index(j))
#         lj4 = np.append(lj4,j)
#         vtp4 = np.append(vtp4,j[2][j[1].index(technologies[toplot])])
# print(len(vtp4)/len(tab))


# plot_box([vtp,vtp1,vtp3], ['DHN_HP_ELEC','DHN_cogen_gas','DHN_Cogen_Wet'])
# #,vtp2,vtp4
# #,'DEC_THHP_GAS','DEC_HP_ELEC'
# lj=np.array([])
# vtp3 = np.array([])
# list_str = np.array([])
# toplot = 69

# for j in tab:
#     if technologies[toplot] in j[1]:
#         list_str = np.append(list_str,Master_diff.index(j))
#         lj = np.append(lj,j)
#         vtp3 = np.append(vtp3,j[2][j[1].index(technologies[toplot])])

# vtp4 = np.array([])
# list_str = np.array([])
# toplot = 66

# for j in tab:
#     if technologies[toplot] in j[1]:
#         list_str = np.append(list_str,Master_diff.index(j))
#         lj = np.append(lj,j)
#         vtp4 = np.append(vtp4,j[2][j[1].index(technologies[toplot])])
# plot_box([vtp3], ['TS_DHN_Seasonal'])
# #,'TS_DEC_HP_ELEC'
# #,vtp4
# v=np.array([])
# v1=np.array([])
# a_ref = np.genfromtxt(path_asset,skip_header = 2,usecols = 7)[18] * np.genfromtxt(path_asset,skip_header = 2,usecols = 2)[18]
# b_ref = np.genfromtxt(path_asset,skip_header = 2,usecols = 7)[30] * np.genfromtxt(path_asset,skip_header = 2,usecols = 2)[30]
# c_ref = np.genfromtxt(path_asset,skip_header = 2,usecols = 7)[19] * np.genfromtxt(path_asset,skip_header = 2,usecols = 2)[19]
# d_ref = np.genfromtxt(path_asset,skip_header = 2,usecols = 7)[21] * np.genfromtxt(path_asset,skip_header = 2,usecols = 2)[21]
# e_ref = np.genfromtxt(path_asset,skip_header = 2,usecols = 7)[29] * np.genfromtxt(path_asset,skip_header = 2,usecols = 2)[29]
# for j in tab:   
#     a=get_en_cp(Master_diff.index(j), 18)  
#     b=get_en_cp(Master_diff.index(j), 30)    
#     c=get_en_cp(Master_diff.index(j), 19)    
#     d=get_en_cp(Master_diff.index(j), 21)
#     e=get_en_cp(Master_diff.index(j), 29)

#     v=np.append(v,a+b)
#     v1=np.append(v1,c+d+e)
# # v=v[v1!=0]
# # v1=v1[v1!=0]
# v1_0 = v1[v1==0]
# print(len(v1_0)/len(tab))
# plt.plot(v,v1,'.')
# plt.plot([a_ref+b_ref,a_ref+b_ref-14.2],[0,14.2])
# plt.show()





# print(Master_diff.index(tab[37])-550)
# print(Master_diff.index(tab[40])-550)
# print(Master_diff.index(tab[43])-550)
# print(Master_diff.index(tab[46])-550)
# print(Master_diff.index(tab[60])-550)
# print(Master_diff.index(tab[61])-550)
# print(Master_diff.index(tab[79])-550)
# print(Master_diff.index(tab[81])-550)
# print(Master_diff.index(tab[95])-550)
# print(Master_diff.index(tab[98])-550)
# print(Master_diff.index(tab[107])-550)
# print(Master_diff.index(tab[122])-550)
# print(Master_diff.index(tab[125])-550)
# print(Master_diff.index(tab[148])-550)
# print(Master_diff.index(tab[149])-1050)
# print(Master_diff.index(tab[162])-1050)
# print(Master_diff.index(tab[170])-1050)
# print(Master_diff.index(tab[174])-1050)
# print(Master_diff.index(tab[176])-1050)
# print(Master_diff.index(tab[182])-1050)
# print(Master_diff.index(tab[205])-1050)
# print(Master_diff.index(tab[207])-1050)
# print(Master_diff.index(tab[237])-1050)
# print(Master_diff.index(tab[239])-1050)
# print(Master_diff.index(tab[243])-1050)
# print(Master_diff.index(tab[261])-1050)
# print(Master_diff.index(tab[272])-1050)
# print(Master_diff.index(tab[274])-1050)
# print(Master_diff.index(tab[295])-1050)



# plt.boxplot(vtp3,showfliers=False)
# plt.show()

# dec=np.zeros(len(Master_diff))
# dhn=np.zeros(len(Master_diff))
# sumlt = np.zeros(len(Master_diff))
# for n in range (1,len(Master_diff)+1):
#     path_dhn = 'Results_sans_nuk\\Results_max\\output_'+str(int(n))+'\\hourly_data\\layer_HEAT_LOW_T_DHN.txt'
#     path_dec = 'Results_sans_nuk\\Results_max\\output_'+str(int(n))+'\\hourly_data\\layer_HEAT_LOW_T_DECEN.txt'
#     dec[n-1]=np.sum(np.genfromtxt(path_dec,skip_header=1,delimiter = '\t',usecols=151))
#     dhn[n-1]=np.sum(np.genfromtxt(path_dhn,skip_header=1,usecols=151,delimiter = '\t'))
#     sumlt[n-1] = dec[n-1]+dhn[n-1]
# r = np.divide(dhn,np.add(dhn,dec))
# print(np.mean(r))


# plt.boxplot(r)
# plt.show()

