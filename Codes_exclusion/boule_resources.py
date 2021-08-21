# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:58:34 2021

@author: User
"""
import numpy as np
import os
import random as rnd

def print_model (list_tech,var,numb):
    
    path_asset = 'ref\\resources.txt'
    resources = np.genfromtxt(path_asset,skip_header=2,usecols=0,dtype=str)
    f_tech = np.genfromtxt(path_asset,skip_header = 2,usecols = 2)
    
    
    model_old = open("resources\\ESTD_model.mod","r")
    lignes = model_old.readlines()
    
    model_new = open("resources\\ESTD_model_"+str(int(numb))+".mod","w")
    
    model_new.writelines(lignes[0:127])
    
    for x in list_tech :
        model_new.writelines('var F_'+x+' binary;\n')
            
        
    model_new.writelines(lignes[127:250])
        
    for x in resources :
        
        if x in list_tech :
            ind = np.where(resources == x)[0]
            bm = (1-var)*f_tech[ind][0]
            bp = (1+var)*f_tech[ind][0]
            model_new.writelines('subject to availability_'+x+'_left : \n')
            model_new.writelines('\t'+str(bm)+' + (availablity["'+x+'"]-'+str(bm)+')*F_'+x+' >= sum {t in PERIODS, h in HOUR_OF_PERIOD[t], td in TYPICAL_DAY_OF_PERIOD[t]} (F_t ["'+x+'", h, td] * t_op [h, td]);\n')
            model_new.writelines('subject to availability_'+x+'_right : \n')
            model_new.writelines('\tsum {t in PERIODS, h in HOUR_OF_PERIOD[t], td in TYPICAL_DAY_OF_PERIOD[t]} (F_t ["'+x+'", h, td] * t_op [h, td]) >= '+str(bp)+'*F_'+x+';\n')
        else :
            model_new.writelines('subject to availability_'+x+' : \n')
            model_new.writelines('\tsum {t in PERIODS, h in HOUR_OF_PERIOD[t], td in TYPICAL_DAY_OF_PERIOD[t]} (F_t ["'+x+'", h, td] * t_op [h, td]) <= avail ["'+x+'"];\n')
                    
    model_new.writelines(lignes[253:len(lignes)])
                    
    model_new.close()

    # run_old = open("ESTD_main.run","r")
    # lignes = run_old.readlines()
    
    # run_new = open("model40\\ESTD_boule"+str(int(numb))+".run","w")
    # run_new.writelines(lignes[0:9])
    
    # run_new.writelines('model ESTD_model_'+str(int(numb))+'.mod;\n')
    
    # run_new.writelines(lignes[10:45])
    
    # run_new.writelines('\nparam PathName symbolic default "output_'+str(int(numb))+'/";\n')
    
    # run_new.writelines(lignes[46:len(lignes)])
    # run_new.close()
    
    try:
        os.mkdir('model10\\output\\output_'+str(int(numb))+'\\')
        os.mkdir('model10\\output\\output_'+str(int(numb))+'\\hourly_data\\')
        os.mkdir('model10\\output\\output_'+str(int(numb))+'\\sankey\\')
    except:
        pass
    
    # stream = os.popen('ampl ESTD_main_boule.run','r',-1)
    # stream.read()

variation = 0.05
list_tech_val = ['CCGT','PV','WIND'] #à modifier
emission = 50000
path_tech = 'pareto\\CO2emissions10000\\technologies.txt'
tech_list = np.genfromtxt(path_tech,skip_header=2,usecols=0,dtype=str)
elec_list = np.genfromtxt(path_tech,skip_header=2,skip_footer=95,usecols=0,dtype=str)
heat_list = np.genfromtxt(path_tech,skip_header=11,skip_footer=64,usecols=0,dtype=str)
mob_list = np.genfromtxt(path_tech,skip_header=42,skip_footer=44,usecols=0,dtype=str)
stor_list = np.genfromtxt(path_tech,skip_header=64,skip_footer=21,usecols=0,dtype=str)

def used_techs():
    path_asset = 'pareto\\CO2emissions10000\\technologies.txt'
    technologies = np.genfromtxt(path_asset,skip_header=2,usecols=0,dtype=str)
    f_tech = np.genfromtxt(path_asset,skip_header = 2,usecols = 2)
    returned = np.array([])
    for i in range(0,len(f_tech)):
        if float(f_tech[i]) > 0.0:
            returned = np.append(returned,technologies[i])
    return returned


num = 0
total_list = used_techs()

for i in range (0,200):
    n = rnd.randrange(5,len(total_list))
    liste = rnd.sample(total_list.tolist(),n)
    num = num+1
    k=rnd.randrange(0,100)/2000
    print_model(liste,k,num)
    print(num)

run_old = open("ESTD_main.run","r")
lignes = run_old.readlines()
run_new = open("model10\\ESTD_cluster1.run","w")
for i in range (1,201):  
    run_new.writelines(lignes[0:9])
    run_new.writelines('model ESTD_model_'+str(int(i))+'.mod;\n')
    run_new.writelines('print "model numero '+str(int(i))+'";')
    run_new.writelines(lignes[10:45])
    run_new.writelines('param PathName symbolic default "Results_1/output_'+str(int(i))+'";\n')
    run_new.writelines(lignes[46:len(lignes)])   
run_new.close()

run_old = open("ESTD_main.run","r")
lignes = run_old.readlines()
run_new = open("model10\\ESTD_cluster2.run","w")
for i in range (1,201):  
    run_new.writelines(lignes[0:9])
    run_new.writelines('model ESTD_model_'+str(int(i))+'.mod;\n')
    run_new.writelines('print "model numero '+str(int(i))+'";')
    run_new.writelines(lignes[10:45])
    run_new.writelines('param PathName symbolic default "Results_2/output_'+str(int(i))+'";\n')
    run_new.writelines('let gwp_limit := 40000;\n')
    run_new.writelines(lignes[46:len(lignes)])   
run_new.close()

run_old = open("ESTD_main.run","r")
lignes = run_old.readlines()
run_new = open("model10\\ESTD_cluster3.run","w")
for i in range (1,201):  
    run_new.writelines(lignes[0:9])
    run_new.writelines('model ESTD_model_'+str(int(i))+'.mod;\n')
    run_new.writelines('print "model numero '+str(int(i))+'";')
    run_new.writelines(lignes[10:45])
    run_new.writelines('param PathName symbolic default "Results_3/output_'+str(int(i))+'";\n')
    run_new.writelines('let gwp_limit := 10000;\n')
    run_new.writelines(lignes[46:len(lignes)])   
run_new.close()