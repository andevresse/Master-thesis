#Write the .run for the MGA for techs

n_design = 4

#change for other reference points with MGA
gwp_limit = '1000000'
model = 'MGA1' #Choose between MGA1 and MGA2
print('gwp_limit : ' + '\t' + gwp_limit + '\n')
print('model :' + '\t' + model)

filename_ref = 'D:\Memoire\Other_Methods\MGA\EnergyScope\ESTD_main_MGA_ref.run'
ref_run = open(filename_ref,'r')
ref_lines = ref_run.readlines()
ref_run.close()

for i in range (0,n_design) :
    filename = r'D:\Memoire\Other_Methods\MGA\EnergyScope\ESTD_main_MGA_'+ str(i)+'.run'
    new_run = open(filename,'w')
    new_run.writelines(ref_lines[0:9])
    new_run.writelines('model ESTD_model_MGA.mod;')
    new_run.writelines(ref_lines[10:13])
    if model == 'MGA1' :
        new_run.writelines('data ESTD_data.dat    # not TDs depending data')
    elif model == 'MGA2' :
        new_run.writelines('data ESTD_data_MGA.dat    # not TDs depending data')
    else :
        print('wrong model')
    new_run.writelines(ref_lines[13:45])
    new_run.writelines(r'param PathName symbolic default "D:\Memoire\Other_Methods\MGA\Output\output'+str(i)+'\"; #place where outputs are print')
    new_run.writelines(ref_lines[46:50])
    new_run.writelines('let gwp_limit := ' + gwp_limit + ';')
    new_run.writelines(ref_lines[50:len(ref_lines)])
    new_run.close()