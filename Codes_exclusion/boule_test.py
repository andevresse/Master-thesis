# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:42:55 2021

@author: Dédé
"""

import numpy as np
import random as rnd
import os

def print_model (list_tech,var,numb):
    
    path_asset = 'D:\\Documents\\Master_2\\Mémoire\\Energyscope\\Energyscope-2.0-boule2\\STEP_2_Energy_Model\\output_ref\\technologies.txt'
    technologies = np.genfromtxt(path_asset,skip_header=2,usecols=0,dtype=str)
    f_tech = np.genfromtxt(path_asset,skip_header = 2,usecols = 2)
    
    
    model_old = open("ESTD_model.mod","r")
    lignes = model_old.readlines()
    
    model_new = open("ESTD_model_"+str(int(numb))+".mod","w")
    
    model_new.writelines(lignes[0:127])
    model_new.writelines('var Param_minim;\n')
    
    for x in list_tech :
        model_new.writelines('var F_'+x+' binary;\n')
    
    model_new.writelines(lignes[127:234])
    for x in technologies :
        if x=='EFFICIENCY':
            model_new.writelines('subject to size_limit_efficiency: \n')
            model_new.writelines('\tf_min["EFFICIENCY"] <= F["EFFICIENCY"] <= f_max["EFFICIENCY"] ;\n')

        else :
            if x=='GRID':
                model_new.writelines('subject to size_limit_grid: \n')
                model_new.writelines('\tf_min["GRID"] <= F["GRID"] <= f_max["GRID"] ;\n')
            else:
                if x in list_tech :
                    ind = np.where(technologies == x)[0]
                    bm = (1-var)*f_tech[ind][0]
                    bp = (1+var)*f_tech[ind][0]
                    model_new.writelines('subject to size_limit_'+x+'_left : \n')
                    model_new.writelines('\t'+str(bm)+' + (f_max["'+x+'"]-'+str(bm)+')*F_'+x+' >= F ["'+x+'"];\n')
                    model_new.writelines('subject to size_limit_'+x+'_right : \n')
                    model_new.writelines('\tF ["'+x+'"] >= f_min["'+x+'"]+('+str(bp)+'-f_min["'+x+'"])*F_'+x+';\n')
                else :
                        model_new.writelines('subject to size_limit_'+x+' : \n')
                        model_new.writelines('\tf_min ["'+x+'"] <= F ["'+x+'"] <= f_max ["'+x+'"];\n')
                    
    
   
    model_new.writelines(lignes[237:len(lignes)])
   
                    
    model_new.close()

    try:
        os.mkdir('D:\\Documents\\Master_2\\Mémoire\\Energyscope\\Energyscope-2.0-boule_cluster\\STEP_2_Energy_Model\\Results\\output_'+str(int(numb)))
    except:
        pass
    try:
        os.mkdir('D:\\Documents\\Master_2\\Mémoire\\Energyscope\\Energyscope-2.0-boule_cluster\\STEP_2_Energy_Model\\Results\\output_'+str(int(numb))+"\\hourly_data")
    except:
        pass
    try:
        os.mkdir('D:\\Documents\\Master_2\\Mémoire\\Energyscope\\Energyscope-2.0-boule_cluster\\STEP_2_Energy_Model\\Results\\output_'+str(int(numb))+'\\sankey')
    except:
        pass

def used_techs():
    path_asset = 'D:\\Documents\\Master_2\\Mémoire\\Energyscope\\Energyscope-2.0-boule2\\STEP_2_Energy_Model\\output_ref\\technologies.txt'
    technologies = np.genfromtxt(path_asset,skip_header=2,usecols=0,dtype=str)
    f_tech = np.genfromtxt(path_asset,skip_header = 2,usecols = 2)
    returned = np.array([])
    for i in range(0,len(f_tech)):
        if float(f_tech[i]) > 0.0:
            returned = np.append(returned,technologies[i])
    return returned



total_list = used_techs()
total_list = np.resize(total_list,len(total_list)-3)
m=6
n=550
o=1

run_old = open("ESTD_main.run","r")
lignes = run_old.readlines()
run_new = open("ESTD_cluster.run","w")
for i in range (m,n+1):  
    run_new.writelines(lignes[0:9])
    run_new.writelines('model ESTD_model_'+str(int(i))+'.mod;\n')
    run_new.writelines('print "model numero '+str(int(i))+'";')
    run_new.writelines(lignes[10:45])
    run_new.writelines('param PathName symbolic default "Results/output_'+str(int(i))+'";\n')
    run_new.writelines(lignes[46:len(lignes)])   
run_new.close()

# for i in range (1,111):
#     for var in range (10,51,10): 
#         n = rnd.randrange(5,len(total_list)-3)
#         liste = rnd.sample(total_list.tolist(),n)
#         print_model(liste,var/100,(i-1)*5+var/10)