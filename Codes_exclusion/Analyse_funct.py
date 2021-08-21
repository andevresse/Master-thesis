# -*- coding: utf-8 -*-
"""
Created on Wed May 26 14:24:13 2021

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt

co2=100
if co2==100:
    path_asset='ref\\technologies.txt'
else:        
    path_asset = 'pareto\\CO2emissions'+str(int(co2))+'000\\technologies.txt'
technologies = np.genfromtxt(path_asset,skip_header=2,usecols=0,dtype=str)
technologies = technologies[0:len(technologies)-3]
f_tech = np.genfromtxt(path_asset,skip_header = 2,usecols = 2)
f_tech=f_tech[0:len(f_tech)-3]

#liste des tech installées dans ref
tech_ref = technologies[f_tech!=0].tolist()
f_ref = f_tech[f_tech!=0].tolist()

n_model = 200
n_devresse = 500
#crée un gros tableau qui contient pour chaque model une liste comme suit : 
#[Liste des technologies imposées à la modification, Liste des technologies différentes de la référence,Leurs valeurs]
def get_Master():
    Master_diff=[]
    for n in range(1,n_model+1):

    
        path_result = 'model40\\Results_f\output_'+str(int(n))+'\\technologies.txt'
        model_list = np.genfromtxt(path_result,skip_header=2,usecols=0,dtype=str)
        f_inst = np.genfromtxt(path_result,skip_header = 2,usecols = 2)
    
        #Liste des tech installées dans le model
        model_list = model_list[f_inst!=0].tolist()
        f_inst = f_inst[f_inst!=0].tolist()
        
        #modif_list est la liste des technologies modifiées
        model_old = open('model40\ESTD_model_'+str(int(n))+'.mod','r')
        lignes_old = model_old.readlines()    
        lignes_inter = lignes_old[128:len(lignes_old)]
        modif_model = []
        while lignes_inter[0][0]!='#':
            modif_model.append(lignes_inter[0][6:len(lignes_inter[0])-9])
            lignes_inter = lignes_inter[1:len(lignes_inter)]
            
        #crée les listes des différences    
        diff_list=[]
        diff_value=[]
        for x in model_list:
            if x in tech_ref:
                if f_inst[model_list.index(x)]-f_ref[tech_ref.index(x)] !=0:
                    diff_list.append(x)
                    diff_value.append(f_inst[model_list.index(x)]-f_ref[tech_ref.index(x)])
            else: 
                if f_inst[model_list.index(x)] != 0:
                    diff_list.append(x)
                    diff_value.append(f_inst[model_list.index(x)])
        for x in tech_ref:
            if x in model_list:
                pass
            else:
                if -f_ref[tech_ref.index(x)] != 0:
                    diff_list.append(x)
                    diff_value.append(-f_ref[tech_ref.index(x)])
                                
        Master_diff.append([modif_model,diff_list,diff_value])
    
    for n in range (0,n_devresse):
        try:
            path_result = 'ResultsA\\gwp40\\output'+str(int(n))+'\\technologies.txt'
            model_list = np.genfromtxt(path_result,skip_header=2,usecols=0,dtype=str)
            f_inst = np.genfromtxt(path_result,skip_header = 2,usecols = 2)
            f_min = np.genfromtxt(path_result,skip_header = 2,usecols = 1)
       
        
            modif_model = model_list[f_min != 0].tolist()
            #Liste des tech installées dans le model
            model_list = model_list[f_inst!=0].tolist()
            f_inst = f_inst[f_inst!=0].tolist()
        
            #crée les listes des différences    
            diff_list=[]
            diff_value=[]
            for x in model_list:
                if x in tech_ref:
                    if f_inst[model_list.index(x)]-f_ref[tech_ref.index(x)] !=0:
                        diff_list.append(x)
                        diff_value.append(f_inst[model_list.index(x)]-f_ref[tech_ref.index(x)])
                else: 
                    if f_inst[model_list.index(x)] != 0:
                        diff_list.append(x)
                        diff_value.append(f_inst[model_list.index(x)])
            for x in tech_ref:
                if x in model_list:
                    pass
                else:
                    if -f_ref[tech_ref.index(x)] != 0:
                        diff_list.append(x)
                        diff_value.append(-f_ref[tech_ref.index(x)])
                                
            Master_diff.append([modif_model,diff_list,diff_value])
        except Exception:
            print(str(n)+' est absent')
            Master_diff.append([[],[],[]])
    # for n in range (0,n_devresse):
    #     try:
    #         path_result = 'ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n))+'\\technologies.txt'
    #         model_list = np.genfromtxt(path_result,skip_header=2,usecols=0,dtype=str)
    #         f_inst = np.genfromtxt(path_result,skip_header = 2,usecols = 2)
    #         f_min = np.genfromtxt(path_result,skip_header = 2,usecols = 1)
       
        
    #         modif_model = model_list[f_min != 0].tolist()
    #         #Liste des tech installées dans le model
    #         model_list = model_list[f_inst!=0].tolist()
    #         f_inst = f_inst[f_inst!=0].tolist()
        
    #         #crée les listes des différences    
    #         diff_list=[]
    #         diff_value=[]
    #         for x in model_list:
    #             if x in tech_ref:
    #                 if f_inst[model_list.index(x)]-f_ref[tech_ref.index(x)] !=0:
    #                     diff_list.append(x)
    #                     diff_value.append(f_inst[model_list.index(x)]-f_ref[tech_ref.index(x)])
    #             else: 
    #                 if f_inst[model_list.index(x)] != 0:
    #                     diff_list.append(x)
    #                     diff_value.append(f_inst[model_list.index(x)])
    #         for x in tech_ref:
    #             if x in model_list:
    #                 pass
    #             else:
    #                 if -f_ref[tech_ref.index(x)] != 0:
    #                     diff_list.append(x)
    #                     diff_value.append(-f_ref[tech_ref.index(x)])
                                
    #         Master_diff.append([modif_model,diff_list,diff_value])
    #     except Exception:
    #         print(str(n)+' est absent') 
            # Master_diff.append([[],[],[]])
    for i in range (0,len(Master_diff)):
        try:
            a=get_en_cp(i, 18)
        except Exception:
            pass
        if a == 0:
            Master_diff[i] = [[],[],[]]
    return Master_diff

#retourne un tableau comme master mais seulement les elements qui modifient les elements de la liste
def filter_with(liste,master):
    tab = []
    for i in master:
        tab.append(i)    
    for i in liste:
        for j in master:
            if tech_ref[i] not in j[0]:
                try :
                    tab.remove(j)
                except Exception:
                    pass
    return tab

def results_with(liste,master):
    tab = []
    for i in master:
        tab.append(i)    
    for i in liste:
        for j in master:
            if technologies[i] not in j[1]:
                try :
                    tab.remove(j)
                except Exception:
                    pass
            elif j[2][j[1].index(technologies[i])]==0:
                try :
                    tab.remove(j)
                except Exception:
                    pass
    return tab

def filter_least_in(liste,master):
    tab = []    
    for i in liste:
        for j in master:
            if tech_ref[i] in j[0]:
                if j not in tab:               
                    try :
                        tab.append(j)
                    except Exception:
                        pass
    return tab

def results_least_in(liste,master):
    tab = []    
    for i in liste:
        for j in master:
            if technologies[i] in j[1]:
                if j not in tab:               
                    try :
                        tab.append(j)
                    except Exception:
                        pass
    return tab

#retourne un tableau comme master mais seulement les elements qui ne modifient pas les elements de la liste
def filter_without(liste,master):
    tab = []
    for i in master:
        tab.append(i)    
    for i in liste:
        for j in master:
            if tech_ref[i] in j[0]:
                try :
                    tab.remove(j)
                except Exception:
                    pass
    return tab

def results_without(liste,master):
    tab = []
    for i in master:
        tab.append(i)    
    for i in liste:
        for j in master:
            if technologies[i] in j[1]:
                try :
                    tab.remove(j)
                except Exception:
                    pass
            
def get_modif_table(master):
    modif_tab = np.zeros((len(f_tech),len(f_ref)))
    select_num = np.zeros(len(tech_ref))
    for n in range (0,len(master)):
        for i in range (0,len(f_ref)):
            if tech_ref[i] in master[n][0]:
                select_num[i] = select_num[i]+1 
                for j in range (0,len(f_tech)):
                    if technologies[j] in master[n][1]:
                    
                        if master[n][2][master[n][1].index(technologies[j])] != 0:
                        
                            modif_tab[j][i] = modif_tab[j][i]+1                    
    modif_tab_rel = np.divide(modif_tab,select_num)
    
    return [modif_tab,select_num,modif_tab_rel]

def plot_hist(num_mod,num_tech,To_plot):
    le_plot = []
    for i in range (0,len(To_plot[num_mod][num_tech])):
        if To_plot[num_mod][num_tech][i] != 0:
            le_plot.append(To_plot[num_mod][num_tech][i])

    plt.hist(le_plot)
    plt.show()
    
def get_to_plot(master):
    To_plot = []
    for i in range (0,len(tech_ref)):
        to_check = []
        value_to_plot = []
        for n in range (0,len(master)):
            if tech_ref[i] in master[n][0]:
                to_check.append(master[n])
        for j in range (0,len(technologies)):
            val = []
            for m in range (0,len(to_check)):
                if technologies[j] in to_check[m][1]:
                    val.append(to_check[m][2][to_check[m][1].index(technologies[j])])
                else:
                    val.append(0)
            value_to_plot.append(val)
        To_plot.append(value_to_plot)
    return To_plot

def plot_compare(master,base,rempl):
    evol_base = np.zeros(len(master))
    evol_rempl = np.zeros(len(master))
    for i in range (0,len(master)):
        for n in range (0,len(base)):
            if tech_ref[base[n]] in master[i][1]:
                evol_base[i] = evol_base[i] + master[i][2][master[i][1].index(tech_ref[base[n]])]
        for n in range (0,len(rempl)):
            if technologies[rempl[n]] in master[i][1]:
                evol_rempl[i] = evol_rempl[i] + master[i][2][master[i][1].index(technologies[rempl[n]])]
    plt.plot(evol_base,evol_rempl,'.')            
    
def plot_HT_ressources():
    fig, ax = plt.subplots()
    left_side = ax.spines["left"]
    left_side.set_visible(False)
    right_side = ax.spines["right"]
    right_side.set_visible(False)

    left_side = ax.spines["top"]
    left_side.set_visible(False)
    right_side = ax.spines["bottom"]
    right_side.set_visible(False)

    av = [23400,33354.99944,7000]
    use = [20063.776211,33354.999440,7000.000000]
    title = ['Wood','Coal','Waste']
    plt.barh([1.35,2.35,3.35],av,0.35)
    plt.barh([1,2,3],use,0.35)
    plt.yticks([1.175,2.175,3.175], title)
    plt.text(7500, 3, 'Used')
    plt.text(7500, 3.35, 'Available')
    plt.xticks([7000,20063,23400,33355])
    plt.show()

def plot_box(val,labs,point,prop):
    fig = plt.figure(figsize=(7.5,1.8*(len(val))),dpi=150)
    fig.subplots_adjust(hspace=0.7)
    ax0=fig.add_subplot()
    ax0.set_yticks([])
    left_side = ax0.spines["left"]
    left_side.set_visible(False)
    right_side = ax0.spines["right"]
    right_side.set_visible(False)
    left_side = ax0.spines["top"]
    left_side.set_visible(False)
    right_side = ax0.spines["bottom"]
    right_side.set_visible(False)
    for i in range(0,len(val)):        
        ax1 = fig.add_subplot(len(val),1,i+1,sharex=ax0)
        left_side = ax1.spines["left"]
        left_side.set_visible(False)
        right_side = ax1.spines["right"]
        right_side.set_visible(False)
        left_side = ax1.spines["top"]
        left_side.set_visible(False)
        right_side = ax1.spines["bottom"]
        right_side.set_visible(False)
        lab=['Total cost dev : 0-1% (r='+str(prop[i][0])+')','Total cost dev : 1-2% (r='+str(prop[i][1])+')','Total cost dev : 2-5% (r='+str(prop[i][2])+')','Total cost dev : 5-10% (r='+str(prop[i][3])+')']
        ax1.plot([point[i],point[i]],[1,4],'-r')
        ax1.boxplot(val[i],showfliers=True,labels=lab,vert=False,meanline=True)
        ax1.set_title(labs[i])
        # for tick in ax1.xaxis.get_major_ticks():
        #     tick.label.set_fontsize(7) 
    # left_side = ax2.spines["left"]
    # left_side.set_visible(False)
    # right_side = ax2.spines["right"]
    # right_side.set_visible(False)
    # left_side = ax2.spines["top"]
    # left_side.set_visible(False)
    # right_side = ax2.spines["bottom"]
    # right_side.set_visible(False)
    # left_side = ax3.spines["left"]
    # left_side.set_visible(False)
    # right_side = ax3.spines["right"]
    # right_side.set_visible(False)
    # left_side = ax3.spines["top"]
    # left_side.set_visible(False)
    # right_side = ax3.spines["bottom"]
    # right_side.set_visible(False)
    # left_side = ax4.spines["left"]
    # left_side.set_visible(False)
    # right_side = ax4.spines["right"]
    # right_side.set_visible(False)
    # left_side = ax4.spines["top"]
    # left_side.set_visible(False)
    # right_side = ax4.spines["bottom"]
    # right_side.set_visible(False)
    # if point != -1:
    #     y = np.linspace(1,len(point),len(point))
    #     ax1.scatter(point,y,c='r',marker='.')
    #     ax2.scatter(point,y,c='r',marker='.')
    #     ax3.scatter(point,y,c='r',marker='.')
    #     ax4.scatter(point,y,c='r',marker='.')
    # val1=[]
    # val2=[]
    # val3=[]
    # val4=[]
    # lab2=[]
    # for i in range (0,len(val)):
    #     val1.append(val[i][0])
    #     val2.append(val[i][1])
    #     val3.append(val[i][2])
    #     val4.append(val[i][3])
    # for i in range (0,len(lab)):
    #     lab2.append(' ')
    # ax1.boxplot(val1,showfliers=True,vert=False,labels=lab,meanline=True)
    # ax1.set_title('max 1% \nprice dev')
    # ax2.boxplot(val2,showfliers=True,vert=False,labels=lab2,meanline=True)
    # ax2.set_title('1% to 2% \nprice dev')
    # ax3.boxplot(val3,showfliers=True,vert=False,labels=lab2,meanline=True)
    # ax3.set_title('2% to 5% \nprice dev')
    # ax4.boxplot(val4,showfliers=True,vert=False,labels=lab2,meanline=True)
    # ax4.set_title('5% to 10% \nprice dev.')
    # plt.show()
    
def get_en_cp(n,tech):
    if n in range (0,550):
        path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))+'\\technologies.txt'
    elif n in range (550,1050):
        path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))+'\\technologies.txt'
    else:
        path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))+'\\technologies.txt'
    
    cp=np.genfromtxt(path,skip_header = 2,usecols = 7)[tech]
    f=np.genfromtxt(path,skip_header = 2,usecols = 2)[tech]
    return f*cp

def plot_intro():
    fig, ax = plt.subplots()
    left_side = ax.spines["left"]
    left_side.set_visible(False)
    right_side = ax.spines["right"]
    right_side.set_visible(False)

    left_side = ax.spines["top"]
    left_side.set_visible(False)
    right_side = ax.spines["bottom"]
    right_side.set_visible(False)

    n = [3,4,9,18]
    title = ['',]
    plt.barh([2],[100],0.7)
    plt.barh([1],[34],0.7)

    plt.yticks([1,2], ['Systematic\nUncertainty\nAnalysis\nApproaches','Small\nensemble\nof scenario\nanalysis'])
    plt.text(100, 2, '100')
    plt.text(34, 1, '34')

    # plt.text(7500, 3.35, 'Available')
    plt.xticks([])
    plt.show()
    
    fig, ax = plt.subplots()
    left_side = ax.spines["left"]
    left_side.set_visible(False)
    right_side = ax.spines["right"]
    right_side.set_visible(False)

    left_side = ax.spines["top"]
    left_side.set_visible(False)
    right_side = ax.spines["bottom"]
    right_side.set_visible(False)

    n = [3,4,9,18]
    title = ['Robust\noptimization','Modeling\nto generate\nalternatives','Monte Carlo\nAnalysis (MCA)','Stochastic\nProgramming']
    plt.barh([4],[18],0.7,color='green')
    plt.barh([3],[9],0.7,color='red')
    plt.barh([2],[4],0.7,color='purple')
    plt.barh([1],[3],0.7,color='brown')
    plt.yticks([1,2,3,4], title)
    plt.text(18, 4, '18')
    plt.text(9, 3, '9')
    plt.text(4, 2, '4')
    plt.text(3, 1, '3')



    # plt.text(7500, 3.35, 'Available')
    plt.xticks([])
    plt.show()
    
def plot_elec40():
    fig, ax = plt.subplots()
    left_side = ax.spines["left"]
    left_side.set_visible(False)
    right_side = ax.spines["right"]
    right_side.set_visible(False)

    left_side = ax.spines["top"]
    left_side.set_visible(False)
    right_side = ax.spines["bottom"]
    right_side.set_visible(False)

    v100 = [77,22.7,33.6,9,0,1.6]
    v40 = [21.6,61.5,33.5,27.6,28.2,1.6]
    title = ['CCGT','Solar','Wind','Imported Elec','CHP','hydro']
    plt.barh([6.35,5.35,4.35,3.35,2.35,1.35],v100,0.35)
    plt.barh([6,5,4,3,2,1],v40,0.35)
    plt.yticks([6.175,5.175,4.175,3.175,2.175,1.175], title)
    plt.text(35, 4, 'GWP limit at 40 Mt-eq CO2')
    plt.text(35, 4.35, 'Without constraint')
    plt.xticks([77,21.6,33.6,9,1.6,61.5,28.2])
    plt.show()

def plot_elec10():
    fig, ax = plt.subplots()
    left_side = ax.spines["left"]
    left_side.set_visible(False)
    right_side = ax.spines["right"]
    right_side.set_visible(False)

    left_side = ax.spines["top"]
    left_side.set_visible(False)
    right_side = ax.spines["bottom"]
    right_side.set_visible(False)

    v100 = [77,22.7,33.6,9,0,1.6]
    v40 = [21.6,61.5,33.5,27.6,28.2,1.6]
    v10 = [0,61.5,33.5,27.6,31.9,1.6]
    title = ['CCGT','Solar','Wind','Imported Elec','CHP','hydro']
    plt.barh([6.6,5.6,4.6,3.6,2.6,1.6],v100,0.3)
    plt.barh([6.3,5.3,4.3,3.3,2.3,1.3],v40,0.3)    
    plt.barh([6,5,4,3,2,1],v10,0.3)
    plt.yticks([6.3,5.3,4.3,3.3,2.3,1.3], title)
    plt.text(35, 3.9, 'GWP limit at 10 Mt-eq CO2')
    plt.text(35, 4.2, 'GWP limit at 40 Mt-eq CO2')
    plt.text(35, 4.5, 'Without constraint')
    plt.xticks([77,21.6,33.6,9,1.6,61.5,28.2])
    plt.show()

def get_co2():
    nDD = 550
    nAntho = 500
    gwp = np.zeros(nDD + nAntho*2)
    for i in range (1,nDD+1):
        path = 'Results_sans_nuk\\Results_max\\output_'+str(int(i))+'\\gwp_breakdown.txt'
        gwp[i-1] = np.sum(np.genfromtxt(path,skip_header = 1,usecols = 1))
    for i in range (0,nAntho):
        try:
            path = 'ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(i))+'\\gwp_breakdown.txt'
            gwp[i+nDD] = np.sum(np.genfromtxt(path,skip_header = 1,usecols = 1))
        except Exception:
            print(str(i)+' est absent')
    for i in range (0,nAntho):
        try:
            path = 'ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(i))+'\\gwp_breakdown.txt'
            gwp[i+nAntho+nDD] = np.sum(np.genfromtxt(path,skip_header = 1,usecols = 1))   
        except Exception:
            print(str(i)+' est absent')
    return gwp

def get_E_produced(tech,n,co2):
    if co2 == 100:
        if n=='ref':
            path2='ref\\technologies.txt'
        elif n<550:
            path2='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))+'\\technologies.txt'
        elif n<1050:
            path2='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))+'\\technologies.txt'
        else:
            path2='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))+'\\technologies.txt'    
    else:   
        if n=='ref':
            path2='pareto\\CO2emissions'+str(int(co2))+'000\\technologies.txt'
        elif n > 199:
            n=n-200
            path2 = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))+'\\technologies.txt'
        else:
            path2 = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))+'\\technologies.txt'
    
    P=np.genfromtxt(path2,skip_header = 2,usecols = 2)[tech]
    Pmax = np.genfromtxt(path_asset,skip_header = 2,usecols = 3)[tech]
    if P>Pmax:
        P=Pmax
    Cp = np.genfromtxt(path2,skip_header = 2,usecols = 7)[tech]
    E=P*Cp*8760
    return E
    
def get_Elec_layer(n,co2):
    if co2 == 100:
        if n=='ref':
            path='ref'
        elif n<550:
            path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
        elif n<1050:
            path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
        else:
            path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
    else:   
        if n=='ref':
            path='pareto\\CO2emissions'+str(int(co2))+'000'
        elif n > 199:
            n=n-200
            path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
        else:
            path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
    Total = 0
    Fs = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
    Cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
    for i in range(0,9):
        Total = Total + Fs[i]*Cp[i]*8760
    Total = Total + Fs[9]*Cp[9]*8760*0.9565
    Total = Total + Fs[10]*Cp[10]*8760*0.3396
    Total = Total + Fs[11]*Cp[11]*8760*0.4444
    Total = Total + Fs[19]*Cp[19]*8760*1.25
    Total = Total + Fs[20]*Cp[20]*8760*0.3396
    Total = Total + Fs[21]*Cp[21]*8760*0.4444
    Total = Total + Fs[22]*Cp[22]*8760*0.8264
    Total = Total + Fs[23]*Cp[23]*8760*0.7582
    Total = Total + Fs[31]*Cp[31]*8760*0.9565
    Total = Total + Fs[32]*Cp[32]*8760*0.907
    Total = Total + Fs[33]*Cp[33]*8760*2.6364
    Total = Total + Fs[34]*Cp[34]*8760*2.6364
    Total = Total + np.genfromtxt(path+'\\resources.txt',skip_header = 1,usecols = 1)[0]
    return Total

def get_HT_layer(n,co2):
    if co2 == 100:
        if n=='ref':
            path='ref'
        elif n<550:
            path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
        elif n<1050:
            path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
        else:
            path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
    else:   
        if n=='ref':
            path='pareto\\CO2emissions'+str(int(co2))+'000'
        elif n > 199:
            n=n-200
            path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
        else:
            path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
    Total = 0
    Fs = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
    Cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
    for i in range(9,18):
        Total = Total + Fs[i]*Cp[i]*8760
    return Total

def get_LT_layer(n,co2):
    if co2 == 100:
        if n=='ref':
            path='ref'
        elif n<550:
            path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
        elif n<1050:
            path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
        else:
            path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
    else:   
        if n=='ref':
            path='pareto\\CO2emissions'+str(int(co2))+'000'
        elif n > 199:
            n=n-200
            path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
        else:
            path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
    Total = 0
    Fs = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
    Cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
    for i in range(18,40):
        Total = Total + Fs[i]*Cp[i]*8760
    return Total

def get_MobPub_layer(n,co2):
    if co2 == 100:
        if n=='ref':
            path='ref'
        elif n<550:
            path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
        elif n<1050:
            path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
        else:
            path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
    else:   
        if n=='ref':
            path='pareto\\CO2emissions'+str(int(co2))+'000'
        elif n > 199:
            n=n-200
            path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
        else:
            path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
    Total = 0
    Fs = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
    Cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
    for i in range(40,46):
        Total = Total + Fs[i]*Cp[i]*8760
    return Total

def get_MobPriv_layer(n,co2):
    if co2 == 100:
        if n=='ref':
            path='ref'
        elif n<550:
            path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
        elif n<1050:
            path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
        else:
            path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
    else:   
        if n=='ref':
            path='pareto\\CO2emissions'+str(int(co2))+'000'
        elif n > 199:
            n=n-200
            path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
        else:
            path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
    Total = 0
    Fs = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
    Cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
    for i in range(46,53):
        Total = Total + Fs[i]*Cp[i]*8760
    return Total

def get_fRoad_layer(n,co2):
    if co2 == 100:
        if n=='ref':
            path='ref'
        elif n<550:
            path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
        elif n<1050:
            path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
        else:
            path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
    else:   
        if n=='ref':
            path='pareto\\CO2emissions'+str(int(co2))+'000'
        elif n > 199:
            n=n-200
            path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
        else:
            path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
    Total = 0
    Fs = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
    Cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
    for i in range(56,60):
        Total = Total + Fs[i]*Cp[i]*8760
    return Total
    
def get_fRail_layer(n,co2):
    if co2 == 100:
        if n=='ref':
            path='ref'
        elif n<550:
            path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
        elif n<1050:
            path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
        else:
            path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
    else:   
        if n=='ref':
            path='pareto\\CO2emissions'+str(int(co2))+'000'
        elif n > 199:
            n=n-200
            path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
        else:
            path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
    Total = 0
    Fs = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
    Cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
    for i in range(53,54):
        Total = Total + Fs[i]*Cp[i]*8760
    return Total
    
def get_fBoat_layer(n,co2):
    if co2 == 100:
        if n=='ref':
            path='ref'
        elif n<550:
            path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
        elif n<1050:
            path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
        else:
            path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
    else:   
        if n=='ref':
            path='pareto\\CO2emissions'+str(int(co2))+'000'
        elif n > 199:
            n=n-200
            path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n))
        else:
            path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
    Total = 0
    Fs = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)
    Cp = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 7)
    for i in range(54,56):
        Total = Total + Fs[i]*Cp[i]*8760
    return Total

def list_installed(tech,co2,select):
    liste=[]
    if co2==100:
        copt = copt = np.sum(np.sum(np.genfromtxt('ref\\cost_breakdown.txt',skip_header=1,usecols=[1,2,3])))
        nmax=1550
    elif co2 ==40:
        copt = np.sum(np.sum(np.genfromtxt('pareto\\CO2emissions40000\\cost_breakdown.txt',skip_header=1,usecols=[1,2,3])))
        nmax=700
    elif co2 ==10:
        copt = np.sum(np.sum(np.genfromtxt('pareto\\CO2emissions10000\\cost_breakdown.txt',skip_header=1,usecols=[1,2,3])))
        nmax=700             
    if select == 1:
        cmin = copt
        cmax = copt*1.01
    elif select == 2:
        cmin = copt*1.01
        cmax = copt*1.02
    elif select == 5:
        cmin = copt*1.02
        cmax = copt*1.05
    elif select == 10:
        cmin = copt*1.05
        cmax = copt*1.10
    for n in range(0,nmax):
        if co2 == 100:
            if n=='ref':
                path='ref'
            elif n<550:
                path='Results_sans_nuk\\Results_max\\output_'+str(int(n+1))
            elif n<1050:
                path='ResultsA\\New_LHS_Random9_90\\1st\\New_LHS_1\\output'+str(int(n-550))
            else:
                path='ResultsA\\New_LHS_Random9_90\\2nd\\New_LHS_2\\output'+str(int(n-1050))
        else:   
            if n=='ref':
                path='pareto\\CO2emissions'+str(int(co2))+'000'
            elif n > 199:
                path = 'ResultsA\\gwp'+str(int(co2))+'\\output'+str(int(n-200))
            else:
                path = 'model'+str(int(co2))+'\\Results_f\\output_'+str(int(n+1))
        try:
            Fs = np.genfromtxt(path+'\\technologies.txt',skip_header = 2,usecols = 2)[tech]
            cost = np.sum(np.sum(np.genfromtxt(path+'\\cost_breakdown.txt',skip_header=1,usecols=[1,2,3])))

            if ((Fs !=0 and cost<cmax) and cost > cmin):
                liste.append(n)
        except:
            pass        
    return liste


       
# liste = get_Elec_layer(1, 100)