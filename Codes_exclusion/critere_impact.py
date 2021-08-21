# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:31:22 2021

@author: User
"""
from Analyse_funct import get_E_produced,get_Elec_layer,get_HT_layer,get_LT_layer,get_MobPriv_layer,get_MobPub_layer,get_fBoat_layer,get_fRail_layer,get_fRoad_layer,get_Master,list_installed,plot_box,path_asset,co2
import numpy as np
from math import log10, floor
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection

# Master = get_Master()

technologies = np.genfromtxt(path_asset,skip_header=2,usecols=0,dtype=str)
technologies = technologies[0:len(technologies)-3]
f_tech = np.genfromtxt(path_asset,skip_header = 2,usecols = 2)
f_tech=f_tech[0:len(f_tech)-3]
cp = np.genfromtxt(path_asset,skip_header = 2,usecols = 7)
cp=cp[0:len(cp)-3]


def get_to_plot(tech,co2,sector,select):
    if co2==100:
        nmax=1550
    else:
        nmax=700  
    toplot = []
    liste=list_installed(tech, co2, select)
    lmax = list_installed(6, co2,select)
    for n in liste:
        mult = 1
        if sector =='HT':
            Layer=get_HT_layer(n, co2)
        elif sector =='Elec':
            Layer=get_Elec_layer(n, co2)
            if tech == 9:
                mult = 0.9565
            elif tech == 10:
                mult = 0.3396
            elif tech == 11:
                mult = 0.4444
            elif tech == 19:
                mult = 1.25
            elif tech == 20:
                mult = 0.3396
            elif tech == 21:
                mult = 0.4444
            elif tech == 22:
                mult = 0.8264
            elif tech == 23:
                mult = 0.7582
            elif tech == 31:
                mult = 0.9565
            elif tech == 32:
                mult = 0.907
            elif tech == 33:
                mult = 2.6364
            elif tech == 34:
                mult = 2.6364
        elif sector =='LT':
            Layer=get_LT_layer(n, co2)
        elif sector =='MobPub':
            Layer=get_MobPub_layer(n, co2)
        elif sector =='MobPriv':
            Layer=get_MobPriv_layer(n, co2)
        elif sector =='MobfRail':
            Layer=get_fRail_layer(n, co2)
        elif sector =='MobfRoad':
            Layer=get_fRoad_layer(n, co2)
        elif sector =='MobfBoat':
            Layer=get_fBoat_layer(n, co2)

        Ener = get_E_produced(tech, n, co2)
        if Layer !=0:
            toplot.append(mult*Ener/Layer)
    x=len(liste)/len(lmax)
    x=round(x, 3)
    return [x,toplot]

def to_plot_cogen(co2,select):
    liste = []
    cogen = [34,33,32,31,23,22,21,20,19,11,10,9]
    l=[]
    for tech in cogen:
        liste_1 = list_installed(tech,co2,select)
        to_add1 = set(liste_1)-set(l)
        l = l + list(to_add1)
    prop = len(l)/len(list_installed(4, co2, select))
    for num in l:
        if co2 == 100:
            if num<550:
                path='Results_sans_nuk\\Results_max\\output_'+str(int(num+1))
            elif num<1050:
                path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(num-550))
            else:
                path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(num-1050))
        else:   
            if num=='ref':
                path='pareto\\CO2emissions'+str(int(co2))+'000'
            elif num > 199:
                n=num-200
                path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
            else:
                path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(num+1))
        try:
            f = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
            fmax=np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 3)
            cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
            somme = 0
            for i in cogen:
                mult=1
                if i == 9:
                    mult = 0.9565
                elif i == 10:
                    mult = 0.3396
                elif i == 11:
                    mult = 0.4444
                elif i == 19:
                    mult = 1.25
                elif i == 20:
                    mult = 0.3396
                elif i == 21:
                    mult = 0.4444
                elif i == 22:
                    mult = 0.8264
                elif i == 23:
                    mult = 0.7582
                elif i == 31:
                    mult = 0.9565
                elif i == 32:
                    mult = 0.907
                elif i == 33:
                    mult = 2.6364
                elif i == 34:
                    mult = 2.6364
                somme = somme + f[i]*cp[i]*8760*mult
            Layer = get_Elec_layer(num, co2)
            if Layer!=0:
                liste.append(somme/Layer)
        except:
            pass
    return [liste,prop]

def to_plot_sum(co2,select,techs,layer):
    liste=[]
    cogen = techs
    l=[]
    for tech in cogen:
        liste_1 = list_installed(tech,co2,select)
        to_add1 = set(liste_1)-set(l)
        l = l + list(to_add1)
    prop = len(l)/len(list_installed(4, co2, select))
    for num in l:
        if co2 == 100:
            if num<550:
                path='Results_sans_nuk\\Results_max\\output_'+str(int(num+1))
            elif num<1050:
                path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(num-550))
            else:
                path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(num-1050))
        else:   
            if num=='ref':
                path='pareto\\CO2emissions'+str(int(co2))+'000'
            elif num > 199:
                n=num-200
                path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
            else:
                path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(num+1))
        try:
            f = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
            fmax=np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 3)
            cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
            somme = 0
            for i in cogen:
                somme = somme + f[i]*cp[i]*8760
            if layer == 'Elec':
                Layer = get_Elec_layer(num, co2)
            elif layer == 'LT':
                Layer = get_LT_layer(num, co2)
            if Layer!=0:
                liste.append(somme/Layer)
        except:
            pass
    return [liste,prop]
def to_plot_wind(co2,select):
    liste = []
    cogen = [6,5]
    l=list_installed(6, co2,select)  
    for num in l:
        if co2 == 100:
            if num<550:
                path='Results_sans_nuk\\Results_max\\output_'+str(int(num+1))
            elif num<1050:
                path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(num-550))
            else:
                path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(num-1050))
        else:   
            if num=='ref':
                path='pareto\\CO2emissions'+str(int(co2))+'000'
            elif num > 199:
                n=num-200
                path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
            else:
                path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(num+1))
        try:
            f = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
            fmax=np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 3)
            cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
            somme = 0
            for i in cogen:
                mult=1
                somme = somme + f[i]*cp[i]*8760*mult
            Layer = get_Elec_layer(num, co2)
            if Layer!=0:
                liste.append(somme/Layer)
        except:
            pass
    return liste

def cogen_opti(co2):
    cogen = [34,33,32,31,23,22,21,20,19,11,10,9]
    
    if co2==100:
        path = 'ref\\technologies.txt'
    else:
        path = 'pareto\\CO2emissions'+str(int(co2))+'000\\technologies.txt'
    f = np.genfromtxt(path,skip_header = 2,usecols = 2)
    cp = np.genfromtxt(path,skip_header = 2,usecols = 7)
    somme = 0
    for i in cogen:
        mult=1
        if i == 9:
            mult = 0.9565
        elif i == 10:
            mult = 0.3396
        elif i == 11:
            mult = 0.4444
        elif i == 19:
            mult = 1.25
        elif i == 20:
            mult = 0.3396
        elif i == 21:
            mult = 0.4444
        elif i == 22:
            mult = 0.8264
        elif i == 23:
            mult = 0.7582
        elif i == 31:
            mult = 0.9565
        elif i == 32:
            mult = 0.907
        elif i == 33:
            mult = 2.6364
        elif i == 34:
            mult = 2.6364
        somme = somme + f[i]*cp[i]*8760*mult
    return somme/get_Elec_layer('ref',co2)

def wind_opti(co2):
    cogen = [6,5]
    if co2==100:
        path = 'ref\\technologies.txt'
    else:
        path = 'pareto\\CO2emissions'+str(int(co2))+'000\\technologies.txt'
    f = np.genfromtxt(path,skip_header = 2,usecols = 2)
    cp = np.genfromtxt(path,skip_header = 2,usecols = 7)
    somme = 0
    for i in cogen:
        somme = somme + f[i]*cp[i]*8760
    return somme/get_Elec_layer('ref',co2)

def sum_opti(co2,techs):
    if co2==100:
        path = 'ref\\technologies.txt'
    else:
        path = 'pareto\\CO2emissions'+str(int(co2))+'000\\technologies.txt'
    f = np.genfromtxt(path,skip_header = 2,usecols = 2)
    cp = np.genfromtxt(path,skip_header = 2,usecols = 7)
    somme = 0
    for i in techs:
        somme = somme + f[i]*cp[i]*8760
    return somme/get_Elec_layer('ref',co2)

def res_plot(techs,co2,sector):
    techs.reverse()
    if sector =='HT':
        Layer=get_HT_layer('ref', co2)
    elif sector =='Elec':
        Layer=get_Elec_layer('ref', co2)
    elif sector =='LT':
        Layer=get_LT_layer('ref', co2)
    elif sector =='MobPub':
        Layer=get_MobPub_layer('ref', co2)
    elif sector =='MobPriv':
        Layer=get_MobPriv_layer('ref', co2)
    elif sector =='MobfRail':
        Layer=get_fRail_layer('ref', co2)
    elif sector =='MobfRoad':
        Layer=get_fRoad_layer('ref', co2)
    elif sector =='MobfBoat':
        Layer=get_fBoat_layer('ref', co2)
    opts = []
    plts = []
    labs = []
    prop = []
    for tech in techs:
        if tech == 999:
            opts.append(cogen_opti(co2))
            plts.append([to_plot_cogen(co2,1)[0],to_plot_cogen(co2,2)[0],to_plot_cogen(co2,5)[0],to_plot_cogen(co2,10)[0]])
            labs.append('CHP')
            prop.append([round(to_plot_cogen(co2,1)[1],3),round(to_plot_cogen(co2,2)[1],3),round(to_plot_cogen(co2,5)[1],3),round(to_plot_cogen(co2,10)[1],3)])
        elif tech == 998:
            opts.append(wind_opti(co2))
            plts.append([to_plot_wind(co2,1),to_plot_wind(co2,2),to_plot_wind(co2,5),to_plot_wind(co2,10)])
            labs.append('Wind')
            prop.append([1.0,1.0,1.0,1.0])
        elif tech == 997:
            l=[18,29,30]
            opts.append(sum_opti(co2,l))
            plts.append([to_plot_sum(co2,1,l,'LT')[0],to_plot_sum(co2,2,l,'LT')[0],to_plot_sum(co2,5,l,'LT')[0],to_plot_sum(co2,10,l,'LT')[0]])
            labs.append('HP')
            prop.append([round(to_plot_cogen(co2,1)[1],3),round(to_plot_cogen(co2,2)[1],3),round(to_plot_cogen(co2,5)[1],3),round(to_plot_cogen(co2,10)[1],3)])
        elif tech == 996:
            l=[19,20,21,22,23,31,32,33,34]
            opts.append(sum_opti(co2,l))
            plts.append([to_plot_sum(co2,1,l,'LT')[0],to_plot_sum(co2,2,l,'LT')[0],to_plot_sum(co2,5,l,'LT')[0],to_plot_sum(co2,10,l,'LT')[0]])
            labs.append('CHP')
            prop.append([round(to_plot_cogen(co2,1)[1],3),round(to_plot_cogen(co2,2)[1],3),round(to_plot_cogen(co2,5)[1],3),round(to_plot_cogen(co2,10)[1],3)])
        elif tech == 995:
            l=[24,25,26,35,36,37]
            opts.append(sum_opti(co2,l))
            plts.append([to_plot_sum(co2,1,l,'LT')[0],to_plot_sum(co2,2,l,'LT')[0],to_plot_sum(co2,5,l,'LT')[0],to_plot_sum(co2,10,l,'LT')[0]])
            labs.append('Boilers')
            prop.append([round(to_plot_cogen(co2,1)[1],3),round(to_plot_cogen(co2,2)[1],3),round(to_plot_cogen(co2,5)[1],3),round(to_plot_cogen(co2,10)[1],3)])

        else:
                
            mult=1
            if sector =='Elec':
                if tech == 9:
                    mult = 0.9565
                elif tech == 10:
                    mult = 0.3396
                elif tech == 11:
                    mult = 0.4444
                elif tech == 19:
                    mult = 1.25
                elif tech == 20:
                    mult = 0.3396
                elif tech == 21:
                    mult = 0.4444
                elif tech == 22:
                    mult = 0.8264
                elif tech == 23:
                    mult = 0.7582
                elif tech == 31:
                    mult = 0.9565
                elif tech == 32:
                    mult = 0.907
                elif tech == 33:
                    mult = 2.6364
                elif tech == 34:
                    mult = 2.6364
            opts.append(mult*f_tech[tech]*8760*cp[tech]/Layer)
            tp1 = get_to_plot(tech, co2, sector,1)
            tp2 = get_to_plot(tech, co2, sector,2)
            tp5 = get_to_plot(tech, co2, sector,5)
            tp10 = get_to_plot(tech, co2, sector,10)
            plts.append([tp1[1],tp2[1],tp5[1],tp10[1]])
            prop.append([tp1[0],tp2[0],tp5[0],tp10[0]])
            labs.append(technologies[tech])
    plot_box(plts,labs,opts,prop)

def mat_corr(techs,co2):
    liste_f = []
    names = []
    for tech in techs:
        if tech == 999:
            liste_1 = list_installed(6,co2,1)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            liste_1 = list_installed(6,co2,2)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            liste_1 = list_installed(6,co2,5)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            liste_1 = list_installed(6,co2,10)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            names.append('CHP')
        elif tech ==998:
            liste_1 = list_installed(6,co2,1)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            liste_1 = list_installed(6,co2,2)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            liste_1 = list_installed(6,co2,5)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            liste_1 = list_installed(6,co2,10)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            names.append('Wind')
        else:    
            liste_1 = list_installed(tech,co2,1)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            liste_1 = list_installed(tech,co2,2)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            liste_1 = list_installed(tech,co2,5)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            liste_1 = list_installed(tech,co2,10)
            to_add1 = set(liste_1)-set(liste_f)
            liste_f = liste_f + list(to_add1)
            names.append(technologies[tech])
        
    Master_list = []
    for n in liste_f:
        to_append = []
        if co2 == 100:
            if n<550:
                path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
            elif n<1050:
                path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
            else:
                path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
        else:   
            if n=='ref':
                path='pareto\\CO2emissions'+str(int(co2))+'000'
            elif n > 199:
                num=n-200
                path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(num))
            else:
                path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
        for tech in techs:
            if tech == 999:
                cogen = [34,33,32,31,23,22,21,20,19,11,10,9]                
                try:
                    f = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
                    cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
                    somme = 0
                    for i in cogen:
                        mult=1
                        if i == 9:
                            mult = 0.9565
                        elif i == 10:
                            mult = 0.3396
                        elif i == 11:
                            mult = 0.4444
                        elif i == 19:
                            mult = 1.25
                        elif i == 20:
                            mult = 0.3396
                        elif i == 21:
                            mult = 0.4444
                        elif i == 22:
                            mult = 0.8264
                        elif i == 23:
                            mult = 0.7582
                        elif i == 31:
                            mult = 0.9565
                        elif i == 32:
                            mult = 0.907
                        elif i == 33:
                            mult = 2.6364
                        elif i == 34:
                            mult = 2.6364
                        somme = somme + f[i]*cp[i]*8760*mult
                        # print(somme)
                    to_append.append(somme)
                    # print(to_append)
                except:
                    pass
            elif tech ==998:
                to_append.append(get_E_produced(5, n, co2)+get_E_produced(6, n, co2))
            else:
                to_append.append(get_E_produced(tech, n, co2))
        # to_append.append(np.sum(np.genfromtxt(path+'\\gwp_breakdown.txt',skip_header = 1,usecols = 1)))
        to_append.append(np.sum(np.sum(np.genfromtxt(path+'\\cost_breakdown.txt',skip_header = 1,usecols = [1,2,3]))))
        Master_list.append(to_append)
    print(Master_list)
    ar = np.array([np.array(xi) for xi in Master_list])
    print(ar)
    # names.append('Emissions')
    names.append('Total Cost')
    names[1]='Bus_Diesel'
    names[2]='Bus_CNG'
    names[0]='Tram'
    # names[4]='HT_Elec'
    names[3]='Train'
    df=pd.DataFrame(ar,columns=names)
    print(df,"\n")  
    co = df.corr()
    print(co)
    cor = co.to_numpy()
    print(cor)
    
    
    N = len(names)
    M = len(names)
    ylabels = names
    xlabels = names
    x, y = np.meshgrid(np.arange(M), np.arange(N))
    s = cor   
    fig, ax = plt.subplots()
    R = s/s.max()
    circles = [plt.Circle((i,j), radius=r*0.4) for r, i, j in zip(R.flat, x.flat, y.flat)]
    col = PatchCollection(circles, array=R.flatten(), cmap="RdBu")
    ax.add_collection(col)    
    ax.set(xticks=np.arange(M), yticks=np.arange(N),
           xticklabels=xlabels, yticklabels=ylabels)
    ax.set_xticklabels(xlabels,rotation = 30)
    ax.set_xticks(np.arange(M+1)-0.5, minor=True)
    ax.set_yticks(np.arange(N+1)-0.5, minor=True)
    ax.grid(which='minor')

    fig.colorbar(col)
    plt.show()

## N = 998 : somme wind
## N = 999 : somme CHP elec
    
mat_corr([40,41,43,45],100)
# mat_corr([18,19,22,29,30],40)

# mat_corr([9,10,11,12,13,16,17],40)

# if co2 == 100:
#     # res_plot([999,998,4,2,1],co2,'Elec')
#     res_plot([30,29,18,996,995],co2,'LT')
    # res_plot([17,16,15,13,12,9],co2,'HT')
#     # res_plot([52,49], co2, 'MobPriv')
    # res_plot([45,43,41,40], co2, 'MobPub')
#     # res_plot([58,57,56], co2, 'MobfRoad')
#     # res_plot([55,54], co2, 'MobfBoat')
# elif co2 == 40:
#     res_plot([999,998,4,1],co2,'Elec')
#     res_plot([30,29,22,19,18],co2,'LT')
#     # res_plot([22,19,18],co2,'LT')
    # res_plot([17,16,13,9],co2,'HT')
#     res_plot([52,49], co2, 'MobPriv')
#     res_plot([45,43,42,40], co2, 'MobPub')
#     res_plot([58,57,56], co2, 'MobfRoad')
#     res_plot([55,54], co2, 'MobfBoat')
# elif co2 == 10:
#     res_plot([999,998,4,1],co2,'Elec')
#     res_plot([30,29,28,22,19,18],co2,'LT')
#     res_plot([17,16,13,12,9],co2,'HT')
#     res_plot([52,49], co2, 'MobPriv')
#     res_plot([45,44,43,42,40], co2, 'MobPub')
# #     res_plot([57,56], co2, 'MobfRoad')
#     res_plot([55,54], co2, 'MobfBoat')