# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:04:48 2021

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt

path_asset = 'Ref\\technologies.txt'
technologies = np.genfromtxt(path_asset,skip_header=2,usecols=0,dtype=str)
technologies = technologies[0:len(technologies)-3]
f_tech = np.genfromtxt(path_asset,skip_header = 2,usecols = 2)
f_tech=f_tech[0:len(f_tech)-3]

#liste des tech installées dans ref
tech_ref = technologies[f_tech!=0].tolist()
f_ref = f_tech[f_tech!=0].tolist()

n_model = 500

#crée un gros tableau qui contient pour chaque model une liste comme suit : 
#[Liste des technologies imposées à la modification, Liste des technologies différentes de la référence,Leurs valeurs]
Master_diff=[]
for n in range(1,n_model+1):

    
    path_result = 'Results_sans_nuk\\Results_max\\output_'+str(int(n))+'\\technologies.txt'
    model_list = np.genfromtxt(path_result,skip_header=2,usecols=0,dtype=str)
    f_inst = np.genfromtxt(path_result,skip_header = 2,usecols = 2)
    
    #Liste des tech installées dans le model
    model_list = model_list[f_inst!=0].tolist()
    f_inst = f_inst[f_inst!=0].tolist()
    
    #modif_list est la liste des technologies modifiées
    model_old = open('models\ESTD_model_'+str(int(n))+'.mod','r')
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
            diff_list.append(x)
            diff_value.append(f_inst[model_list.index(x)]-f_ref[tech_ref.index(x)])
        else:
            diff_list.append(x)
            diff_value.append(f_inst[model_list.index(x)])
    for x in tech_ref:
        if x in model_list:
            pass
        else:
            diff_list.append(x)
            diff_value.append(-f_ref[tech_ref.index(x)])
    # diff_list=diff_list[diff_value!=0]
    # diff_value=diff_value[diff_value!=0]
    
    Master_diff.append([modif_model,diff_list,diff_value])
                   

# #Analyse du bazar
# modif_tab = np.zeros((len(f_tech),len(f_ref)))
# select_num = np.zeros(len(tech_ref))
# vari = np.zeros((n_model,len(f_tech),len(f_ref)))

# for n in range (0,n_model):
#     for i in range (0,len(f_ref)):
#         if tech_ref[i] in Master_diff[n][0]:
#             select_num[i] = select_num[i]+1 
#             for j in range (0,len(f_tech)):
#                 if technologies[j] in Master_diff[n][1]:
                    
#                     if Master_diff[n][2][Master_diff[n][1].index(technologies[j])] != 0:
                        
#                         modif_tab[j][i] = modif_tab[j][i]+1
                        
#                 else:
#                     pass
                        
#         else:
#             pass
                    
# modif_tab_rel = np.divide(modif_tab,select_num)        


# To_plot = []                    
# for i in range (0,len(tech_ref)):
#     to_check = []
#     value_to_plot = []
#     for n in range (0,n_model):
#         if tech_ref[i] in Master_diff[n][0]:
#             to_check.append(Master_diff[n])
#     for j in range (0,len(technologies)):
#         val = []
#         for m in range (0,len(to_check)):
#             if technologies[j] in to_check[m][1]:
#                 val.append(to_check[m][2][to_check[m][1].index(technologies[j])])
#             else:
#                 val.append(0)
#         value_to_plot.append(val)
#     To_plot.append(value_to_plot)


# num_mod = 5
# num_tech = 17
# le_plot = []
# for i in range (0,len(To_plot[num_mod][num_tech])):
#     if To_plot[num_mod][num_tech][i] != 0:
#         le_plot.append(To_plot[num_mod][num_tech][i])

# plt.hist(le_plot, bins=50)


Liste_in = []
Liste_out = [5,6,7]

Gros_tableau = []
for i in Master_diff:
    Gros_tableau.append(i)
    
for i in Liste_in:
    for j in Master_diff:
        if tech_ref[i] not in j[0]:
            try :
                Gros_tableau.remove(j)
            except Exception:
                pass
            
tab = []
for i in Gros_tableau:
    tab.append(i)
    
for i in Liste_out:
    for j in Gros_tableau:
        if tech_ref[i] in j[0]:
            try :
                tab.remove(j)
            except Exception:
                pass
            
modif_tab = np.zeros((len(f_tech),len(f_ref)))
select_num = np.zeros(len(tech_ref))
vari = np.zeros((len(Gros_tableau),len(f_tech),len(f_ref)))

for n in range (0,len(tab)):
    for i in range (0,len(f_ref)):
        if tech_ref[i] in tab[n][0]:
            select_num[i] = select_num[i]+1 
            for j in range (0,len(f_tech)):
                if technologies[j] in tab[n][1]:
                    
                    if tab[n][2][tab[n][1].index(technologies[j])] != 0:
                        
                        modif_tab[j][i] = modif_tab[j][i]+1
                        
                else:
                    pass
                        
        else:
            pass
                    
modif_tab_rel = np.divide(modif_tab,select_num)