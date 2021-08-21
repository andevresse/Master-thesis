## Clustering function for suboptimums around one optimum ##
## Author : Anthony Devresse ##

import numpy as np
import pandas as pd


def clustering(file_ref,file_sub) :
    
    ## Resources clustering ##
    try :
        res_ref = np.genfromtxt(file_ref + '\\resources.txt' ,dtype = 'float', delimiter = '\t', skip_header = 1, usecols = (1))
        res_sub = np.genfromtxt(file_sub + '\\resources.txt' ,dtype = 'float', delimiter = '\t', skip_header = 1, usecols = (1))
        
        tot_res_ref = sum(res_ref)
        tot_res_sub = sum(res_sub)
        res_ref_rel = 100*np.divide(res_ref,tot_res_ref)
        res_sub_rel = 100*np.divide(res_sub,tot_res_sub)
        return (res_sub_rel[0])
    except Exception as x :
        print(x)
    
    
    ## Technologies clustering ##
    try :
        tech_ref = np.genfromtxt(file_ref + '\\technologies.txt' ,dtype = 'float', delimiter = '\t', skip_header = 2, usecols = (2))
        tech_sub = np.genfromtxt(file_sub + '\\technologies.txt' ,dtype = 'float', delimiter = '\t', skip_header = 2, usecols = (2))
        
        elec_ref_tot = sum(tech_ref[0:9])
        elec_ref_rel = 100*np.divide(tech_ref[0:9],elec_ref_tot)
        elec_sub_tot = sum(tech_sub[0:9])
        elec_sub_rel = 100*np.divide(tech_sub[0:9],elec_sub_tot)
        
        heat_HT_ref_tot = sum(tech_ref[9:18])
        heat_HT_ref_rel = 100*np.divide(tech_ref[9:18],heat_HT_ref_tot)
        heat_HT_sub_tot = sum(tech_sub[9:18])
        heat_HT_sub_rel = 100*np.divide(tech_sub[9:18],heat_HT_sub_tot)
        
        heat_LT_DHN_ref_tot = sum(tech_ref[18:29])
        heat_LT_DHN_ref_ref = 100*np.divide(tech_ref[18:29],heat_LT_DHN_ref_tot)
        heat_LT_DHN_sub_tot = sum(tech_sub[18:29])
        heat_LT_DHN_sub_ref = 100*np.divide(tech_sub[18:29],heat_LT_DHN_sub_tot)
        
        heat_LT_DEC_ref_tot = sum(tech_ref[29:40])
        heat_LT_DEC_ref_ref = 100*np.divide(tech_ref[29:40],heat_LT_DEC_ref_tot)
        heat_LT_DEC_sub_tot = sum(tech_sub[29:40])
        heat_LT_DEC_sub_ref = 100*np.divide(tech_sub[29:40],heat_LT_DEC_sub_tot)
        
        pub_mobility_ref_tot = sum(tech_ref[40:46])
        pub_mobility_ref_rel = 100*np.divide(tech_ref[40:46],pub_mobility_ref_tot)
        pub_mobility_sub_tot = sum(tech_sub[40:46])
        pub_mobility_sub_rel = 100*np.divide(tech_sub[40:46],pub_mobility_sub_tot)
        
        priv_mobility_ref_tot = sum(tech_ref[46:53])
        priv_mobility_ref_rel = 100*np.divide(tech_ref[46:53],priv_mobility_ref_tot)
        priv_mobility_sub_tot = sum(tech_sub[46:53])
        priv_mobility_sub_rel = 100*np.divide(tech_sub[46:53],priv_mobility_sub_tot)
        
        freight_ref_tot = sum(tech_ref[53:60])
        freight_ref_rel = 100*np.divide(tech_ref[53:60],freight_ref_tot)
        freight_sub_tot = sum(tech_sub[53:60])
        freight_sub_rel = 100*np.divide(tech_sub[53:60],freight_sub_tot)
        
        storage_ref_tot = sum(tech_ref[62:83])
        storage_ref_rel = 100*np.divide(tech_ref[62:83],storage_ref_tot)
        storage_sub_tot = sum(tech_sub[62:83])
        storage_sub_rel = 100*np.divide(tech_sub[62:83],storage_sub_tot)
    except Exception as x :
        print (x)
    