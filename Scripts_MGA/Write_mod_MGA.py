## Writes the weighted sum for MGA method ##
## Author : Anthony Devresse ##

import numpy as np
from numpy import random
from collections import OrderedDict
from write_run_MGA import gwp_limit


def write_mod_func(model,reference_path,choice_MGA,type_weights,ref_run,weights,slack,obj_func,indexes) :
    if model == 'MGA1' :
   
        #Get tech and resources names
        techs = np.genfromtxt(reference_path + '\\technologies.txt',dtype = 'str', delimiter = '\t', skip_header = 2,usecols = 0)
        resources = np.genfromtxt(reference_path + '\\resources.txt',dtype = 'str', delimiter = '\t', skip_header = 1,usecols = 0)
        resources = np.concatenate((resources[:15],resources[17:21]))
        
        #Get non-zero activities indexes
        df_activities = np.genfromtxt(reference_path + '\\technologies.txt',dtype = 'float' , delimiter = '\t', skip_header = 2,usecols = 9)
        myList_activities = list(np.nonzero(df_activities[:40])[0]) #40 does not take mobility into account
        
        #Get non-zero res indexes
        df_res = np.genfromtxt(reference_path + '\\resources.txt',dtype = 'float', delimiter = '\t', skip_header = 1, usecols = 1)
        df_res = np.concatenate((df_res[:15],df_res[17:21]))
        myList_res = list(np.nonzero(df_res)[0]) 
    
        #Weights computation for the weighted sum (can be integer method or normalized)
        if ref_run == True :
            if type_weights == 'Integer' :
                if choice_MGA =='Activities' :
                    pass    
                elif choice_MGA =='Resources' :
                    pass
                
            elif type_weights == 'Normalized' :
                if choice_MGA == 'Activities' :
                    elec_tot = (sum(df_activities[0:9]) + 0.9565 * df_activities[9] + 0.3396 * df_activities[10] + 0.4444 * df_activities[11] + 1.25 * df_activities[19] + 0.3396 * df_activities[20] + 0.826446281 * df_activities[21] + 0.758208955 * df_activities[22] + 0.4444 * df_activities[23] + 0.9565 * df_activities[31] + 0.907 * df_activities[32] + 2.6364*df_activities[33] + 2.6364*df_activities[34])
                    for i in range (0,9) :
                        weights[i] += df_activities[i]/elec_tot
                        
                    for i in range (9,18) :
                        if i==9 :
                            weights[i] += df_activities[i]/sum(df_activities[9:18]) + 0.9565 * df_activities[9]/elec_tot
                        elif i==10 :
                            weights[i] += df_activities[i]/sum(df_activities[9:18]) + 0.3396 * df_activities[10]/elec_tot
                        elif i==11 :
                            weights[i] += df_activities[i]/sum(df_activities[9:18]) + 0.4444 * df_activities[11]/elec_tot
                        else :
                            weights[i] += df_activities[i]/sum(df_activities[9:18])
                            
                    for i in range (18,29) :
                        if i==19 :
                            weights[i] += df_activities[i]/sum(df_activities[18:29]) +  1.25 * df_activities[19]/elec_tot
                        elif i==20 :
                            weights[i] += df_activities[i]/sum(df_activities[18:29]) + 0.3396 * df_activities[20]/elec_tot
                        elif i==21 :
                            weights[i] += df_activities[i]/sum(df_activities[18:29]) + 0.826446281 * df_activities[21]/elec_tot
                        elif i==22 :
                            weights[i] += df_activities[i]/sum(df_activities[18:29]) + 0.758208955 * df_activities[22]/elec_tot
                        elif i==23 :
                            weights[i] += df_activities[i]/sum(df_activities[18:29]) + 0.4444 * df_activities[23]/elec_tot
                        else :   
                            weights[i] += df_activities[i]/sum(df_activities[18:29])
                            
                    for i in range (29,40) :
                        if i==31 :
                            weights[i] += df_activities[i]/sum(df_activities[29:40]) + 0.9565 * df_activities[31]/elec_tot
                        elif i==32 :
                            weights[i] += df_activities[i]/sum(df_activities[29:40]) + 0.907 * df_activities[32]/elec_tot
                        elif i==33 :
                            weights[i] += df_activities[i]/sum(df_activities[29:40]) + 2.6364*df_activities[33]/elec_tot
                        elif i==34 :
                            weights[i] += df_activities[i]/sum(df_activities[29:40]) + 2.6364*df_activities[34]/elec_tot
                        else : 
                            weights[i] += df_activities[i]/sum(df_activities[29:40])
                        
                elif choice_MGA == 'Resources' :
                    for i in range (0,len(df_res)) :
                        weights[i] += df_res[i]/sum(df_res)
                        
                    
                    
                    
        else :
            if choice_MGA =='Activities' :
                if type_weights =='Integer':
                    for i in range(0,len(weights)) :
                        if i in myList_activities :
                            weights[i] +=1
                if type_weights == 'Normalized' :
                    for i in range (0,9) :
                        weights[i] += df_activities[i]/sum(df_activities[0:9])
                    for i in range (9,18) :
                        weights[i] += df_activities[i]/sum(df_activities[9:18])
                    for i in range (18,29) :
                        weights[i] += df_activities[i]/sum(df_activities[18:29])
                    for i in range (29,40) :
                        weights[i] += df_activities[i]/sum(df_activities[29:40])
                    
            if choice_MGA == 'Resources' :
                if type_weights == 'Integer' :
                    for i in range(0,len(weights)) :
                        if i in myList_res :
                            weights[i]+=1
                if type_weights == 'Normalized' :
                    for i in range (0,len(df_res)) :
                        weights[i] += df_res[i]/sum(df_res)
                    
                      


        #Compute the total cost of the reference system
        #Do not forget to change in case the optimum changes
        
        if gwp_limit == '1000000' :
            df_cost = np.genfromtxt(r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_MGA_ref' + '\\cost_breakdown.txt',dtype = 'float',delimiter = '\t', skip_header = 1, usecols = (1,2,3))
        elif gwp_limit == '40000':
            df_cost = np.genfromtxt(r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_MGA_40k' + '\\cost_breakdown.txt',dtype = 'float',delimiter = '\t', skip_header = 1, usecols = (1,2,3))
        elif gwp_limit == '10000' :
            df_cost = np.genfromtxt(r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_MGA_10k' + '\\cost_breakdown.txt',dtype = 'float',delimiter = '\t', skip_header = 1, usecols = (1,2,3))
            
        total_cost = sum(sum(df_cost))



        #Write the.mod
        if choice_MGA == 'Activities' : 
            #Write the .mod for Activities
            filename_ref = 'D:\Memoire\Other_Methods\MGA\EnergyScope\ESTD_model.mod'
            ref_mod = open(filename_ref,'r')
            ref_lines = ref_mod.readlines()
            ref_mod.close()
            filename = r'D:\Memoire\Other_Methods\MGA\EnergyScope\ESTD_model_MGA.mod'
            new_mod = open(filename,'w')

            new_mod.writelines(ref_lines[0:438])
            new_mod.writelines('#########################MGA#####################' + '\n')

            new_mod.writelines('## Variables ##' + '\n')
            new_mod.writelines('var ActivityByTech {TECHNOLOGIES}>=0;' + '\n' + 'var sumA >=0;' + '\n')

            new_mod.writelines('## Parameters##' + '\n')


            new_mod.writelines('## Constraints ##' + '\n')
            new_mod.writelines('subject to ActivityByTech_calc {tech in TECHNOLOGIES} : ' + '\n' + '\t' + 'ActivityByTech[tech] = sum {t in PERIODS, h in HOUR_OF_PERIOD[t], td in TYPICAL_DAY_OF_PERIOD[t]} (F_t [tech, h, td]);' + '\n')
            new_mod.writelines('subject to cost_MGA :' + '\n' + '\t' + 'TotalCost<='+str(slack)+'*' + str(total_cost) + ';' + '\n')
            #new_mod.writelines('subject to sumMGA_Technology :' + '\n' + '\t' + 'sumA =' + str(weights[myList_activities[0]]) + '*' + 'ActivityByTech[\"'+str(techs[myList_activities[0]])+'\"]')
            new_mod.writelines('subject to sumMGA_Technology :' + '\n' + '\t' + 'sumA =')
            for i in range (0,len(myList_activities)) :
                #new_mod.writelines('+' + str(weights[myList_activities[i]]) + '*' + 'ActivityByTech[\"'+str(techs[myList_activities[i]])+'\"]')
                obj_func.append('ActivityByTech[\"'+str(techs[myList_activities[i]])+'\"]')
                indexes.append(myList_activities[i])
                
            obj_func = list(dict.fromkeys(obj_func)) #Get rid of duplicates
            indexes = list(dict.fromkeys(indexes))
            for i in range (0,len(obj_func)-1) :
                new_mod.writelines(str(weights[indexes[i]]) + '*' + obj_func[i] + '+') 
            new_mod.writelines(str(weights[indexes[len(obj_func)-1]]) + '*' + obj_func[len(obj_func)-1])
            
            new_mod.writelines(';' + '\n')
            new_mod.writelines(ref_lines[438:444])
            new_mod.writelines('\n')
            new_mod.writelines('\n' + 'minimize obj: sumA;' )
            new_mod.close()
        
            
        elif choice_MGA == 'Resources' :
            #Write the .mod for Resources
            filename_ref = 'D:\Memoire\Other_Methods\MGA\EnergyScope\ESTD_model.mod'
            ref_mod = open(filename_ref,'r')
            ref_lines = ref_mod.readlines()
            ref_mod.close()
            filename = r'D:\Memoire\Other_Methods\MGA\EnergyScope\ESTD_model_MGA.mod'
            new_mod = open(filename,'w')

            new_mod.writelines(ref_lines[0:438])
            new_mod.writelines('#########################MGA#####################' + '\n')
            
            new_mod.writelines('## Variables ##' + '\n')
            new_mod.writelines('var ActivityByRes {RESOURCES}>=0;' + '\n' + 'var sumR >=0;' + '\n')
            new_mod.writelines('var ActivityByTech {TECHNOLOGIES}>=0;' + '\n')
            
            new_mod.writelines('## Parameters##' + '\n')
            
            new_mod.writelines('## Constraints ##' + '\n')
            new_mod.writelines('subject to ActivityByTech_calc {tech in TECHNOLOGIES} : ' + '\n' + '\t' + 'ActivityByTech[tech] = sum {t in PERIODS, h in HOUR_OF_PERIOD[t], td in TYPICAL_DAY_OF_PERIOD[t]} (F_t [tech, h, td]);' + '\n')
            new_mod.writelines('subject to ActivityByRes_calc {res in RESOURCES} : ' + '\n' + '\t' + 'ActivityByRes[res] = sum {t in PERIODS, h in HOUR_OF_PERIOD[t], td in TYPICAL_DAY_OF_PERIOD[t]} (F_t [res, h, td]);' + '\n')
            new_mod.writelines('subject to cost_MGA :' + '\n' + '\t' + 'TotalCost<='+str(slack)+'*' + str(total_cost) + ';' + '\n')
            #new_mod.writelines('subject to sumMGA_Resource :' + '\n' + '\t' + 'sumR =' + str(weights[myList_res[0]]) + '*' + 'ActivityByRes[\"'+str(resources[myList_res[0]])+'\"]')
            new_mod.writelines('subject to sumMGA_Resource :' + '\n' + '\t' + 'sumR =')
            for i in range (0,len(myList_res)) :
                #new_mod.writelines('+' + str(weights[myList_res[i]]) + '*' + 'ActivityByRes[\"'+str(resources[myList_res[i]])+'\"]')
                obj_func.append('ActivityByRes[\"'+str(resources[myList_res[i]])+'\"]')
                indexes.append(myList_res[i])
                
            obj_func = list(dict.fromkeys(obj_func)) #Get rid of duplicates
            indexes = list(dict.fromkeys(indexes))
            for i in range (0,len(obj_func)-1) :
                new_mod.writelines(str(weights[indexes[i]]) + '*' + obj_func[i] + '+') 
            new_mod.writelines(str(weights[indexes[len(obj_func)-1]]) + '*' + obj_func[len(obj_func)-1])
            
            new_mod.writelines(';' + '\n')
            new_mod.writelines(ref_lines[438:444])
            new_mod.writelines('\n')
            new_mod.writelines('\n' + 'minimize obj: sumR;' )
            new_mod.close()
            
            
        else :
            print('Problème avec choice_MGA')

        return weights   
    
def write_mod_func_bis(count,model,reference_path,slack) :
    if model == 'MGA2' :
        
        output_path = r'D:\Memoire\Other_Methods\MGA\Output'
        #Compute the total cost of the reference system
        #Do not forget to change in case the optimum changes
        if gwp_limit == '1000000' :
            df_cost = np.genfromtxt(r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_MGA_ref' + '\\cost_breakdown.txt',dtype = 'float',delimiter = '\t', skip_header = 1, usecols = (1,2,3))
        elif gwp_limit == '40000':
            df_cost = np.genfromtxt(r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_MGA_40k' + '\\cost_breakdown.txt',dtype = 'float',delimiter = '\t', skip_header = 1, usecols = (1,2,3))
        elif gwp_limit == '10000' :
            df_cost = np.genfromtxt(r'D:\Memoire\Other_Methods\MGA\EnergyScope\output_MGA_10k' + '\\cost_breakdown.txt',dtype = 'float',delimiter = '\t', skip_header = 1, usecols = (1,2,3))
            
        total_cost = sum(sum(df_cost))
        
        #Get resources names
        resources = np.genfromtxt(reference_path + '\\resources.txt',dtype = 'str', delimiter = '\t', skip_header = 1,usecols = 0)
        resources = np.concatenate((resources[:15],resources[17:21]))
        #Get resources values from optimum and previous MGA runs
        
        df_res = np.zeros((count,len(resources)))
        df_ref = np.genfromtxt(reference_path + '\\resources.txt',dtype = 'float', delimiter = '\t', skip_header = 1,usecols = 1)
        df_res[0] = np.concatenate((df_ref[:15],df_ref[17:21]))
        for i in range (1,count) :
            df_ref = np.genfromtxt(output_path + '\\output' + str(i-1) + '\\resources.txt',dtype = 'float', delimiter = '\t', skip_header = 1, usecols = 1)
            df_res[i] = np.concatenate((df_ref[:15],df_ref[17:21]))
        print (df_res)
        
        #Write the .dat for MGA
        
        filename_ref = 'D:\Memoire\Other_Methods\MGA\EnergyScope\ESTD_data.dat'
        ref_dat = open(filename_ref,'r')
        ref_dat_lines = ref_dat.readlines()
        ref_dat.close()
        
        filename = r'D:\Memoire\Other_Methods\MGA\EnergyScope\ESTD_data_MGA.dat'
        new_dat = open(filename,'w')
        
        new_dat.writelines(ref_dat_lines)
        new_dat.writelines('#############MGA2############' + '\n')
        new_dat.writelines('set RESOURCES_MGA :=    ELECTRICITY' + '\t' +   'GASOLINE' + '\t'   + 'DIESEL' + '\t' + 'BIOETHANOL' +'\t'  + 'BIODIESEL'   + '\t' + 'LFO'  + '\t' + 'NG' + '\t' +  'SLF' + '\t' +  'SNG' + '\t' +  'WOOD' + '\t' + 'WET_BIOMASS' + '\t'    + 'COAL'    +'\t' + 'URANIUM' + '\t' +  'WASTE' + '\t' +    'H2'    + '\t' + 'RES_WIND' + '\t' + 'RES_SOLAR' + '\t' + 'RES_HYDRO' + '\t' + 'RES_GEO'    + ';' + '\n')
        
        for i in range (0,count) :
            new_dat.writelines('# A_' + str(i) + '(see MGA2 method)' + '\n')
            new_dat.writelines('param : A_' + str(i) + '\t' + ':=' + '\n')
            for j in range (0,19) :
                new_dat.writelines(resources[j] + '\t' + str(df_res[i,j]) + '\n')           
            new_dat.writelines(';' + '\n' + '\n')
        
        
        #Write the .mod for MGA

        filename_ref = 'D:\Memoire\Other_Methods\MGA\EnergyScope\ESTD_model.mod'
        ref_mod = open(filename_ref,'r')
        ref_mod_lines = ref_mod.readlines()
        ref_mod.close()
        
        filename = r'D:\Memoire\Other_Methods\MGA\EnergyScope\ESTD_model_MGA.mod'
        new_mod = open(filename,'w')
        
        new_mod.writelines(ref_mod_lines[0:438])
        new_mod.writelines('#########################MGA2#####################' + '\n')
        
        new_mod.writelines('\n' + '## Sets ## ' + '\n')
        new_mod.writelines('set RESOURCES_MGA;')
        
        new_mod.writelines('\n' + '## Variables ##' + '\n')
        new_mod.writelines('var ActivityByTech {TECHNOLOGIES}>=0;' + '\n')
        new_mod.writelines('var bin binary;' + '\n')
        for i in range (0,count) :
            new_mod.writelines('var D_'+str(i)+' {RESOURCES_MGA} ;' + '\n')
            new_mod.writelines('var D_new_'+str(i)+' {RESOURCES_MGA} >=0;' + '\n')
            new_mod.writelines('var sumD_'+str(i)+' >=0;' + '\n')
        new_mod.writelines('var alpha_'+str(count-1)+'>=0;' + '\n')
        new_mod.writelines('var sumD >=0;' + '\n')
       
        
        new_mod.writelines('\n' + '## Parameters ## ' + '\n')
        for i in range (0,count) :
            new_mod.writelines('param A_' + str(i) +  '{RESOURCES_MGA} >=0 ;' + '\n')
        
        new_mod.writelines('\n' + '## Constraints ##' + '\n')
        new_mod.writelines('subject to ActivityByTech_calc {tech in TECHNOLOGIES} : ' + '\n' + '\t' + 'ActivityByTech[tech] = sum {t in PERIODS, h in HOUR_OF_PERIOD[t], td in TYPICAL_DAY_OF_PERIOD[t]} (F_t [tech, h, td]);' + '\n')
        for i in range (0,count) :
            new_mod.writelines('subject to D_' + str(i)+ '_calc {res in RESOURCES_MGA} :' + '\n' + '\t')
            new_mod.writelines('D_'+str(i) + '[res] =  sum {t in PERIODS, h in HOUR_OF_PERIOD[t], td in TYPICAL_DAY_OF_PERIOD[t]} (F_t [res, h, td]) - A_' + str(i) + '[res];' + '\n')
            new_mod.writelines('subject to constr_'+str(i)+'_1 {res in RESOURCES_MGA} :' + '\n' + '\t' + 'D_'+str(i)+'[res] + 1000000*bin>=D_new_'+str(i)+'[res];' + '\n')
            new_mod.writelines('subject to constr_'+str(i)+'_2 {res in RESOURCES_MGA} :' + '\n' + '\t' + '-D_'+str(i)+'[res] + 1000000*(1-bin) >= D_new_'+str(i)+'[res];' + '\n')
            new_mod.writelines('subject to constr_'+str(i)+'_3 {res in RESOURCES_MGA} :' + '\n' + '\t' + 'D_'+str(i)+'[res] <= D_new_'+str(i)+'[res] ;' + '\n')
            new_mod.writelines('subject to constr_'+str(i)+'_4 {res in RESOURCES_MGA} :' + '\n' + '\t' + '-D_'+str(i)+'[res] <= D_new_'+str(i)+'[res];' + '\n')
            new_mod.writelines('subject to sumD_calc_'+str(i)+' :' + '\n' + '\t')
            new_mod.writelines('sumD_'+str(i)+' = sum {res in RESOURCES_MGA} (D_new_'+str(i)+'[res]);' + '\n')
            new_mod.writelines('subject to MGA_const_'+str(i)+':' + '\n' + '\t')
            new_mod.writelines('alpha_'+str(count-1)+'<=sumD_'+str(i)+';'+'\n')
#         new_mod.writelines('subject to sumD_calc :' + '\n' + '\t')
#         new_mod.writelines('sumD = ')
#         for i in range (0,count-1) :
#             new_mod.writelines('sumD_'+str(i) + '+')
#         new_mod.writelines('sumD_'+str(count-1)+';' + '\n')
        new_mod.writelines('subject to TotalCost_Slack :' + '\n' + '\t' + 'TotalCost <= ' + str(slack) + '*' + str(total_cost) + ';' + '\n')
        
        new_mod.writelines(ref_mod_lines[438:444])
        new_mod.writelines('\n')
        new_mod.writelines('\n' + 'maximize obj: alpha_'+str(count-1)+';' )
        
        new_mod.close()    
        
    
