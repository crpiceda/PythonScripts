"""
Sensitivity analysis of thermal parameters
calculate temperature difference between reference and alternative models

structure of the parameter model: 'depthslice_Model13_01sed_kmax-30000.csv'

"""
## import libraries
import os
import pandas as pd
import glob

# directories
dir_reference = r'..\referencemodel' # reference model
dir_param = r'+..\Model13_03lc_smin' # parameter model
dir_diff = r'..\diff_maps' # difference maps

os.chdir(dir_reference) # change to directory reference model

list_reference_model = sorted(glob.glob("*")) # list of depth slices reference model

os.chdir(dir_param) # list of depth slices parameter model

list_param_model = sorted(glob.glob("*")) # list of depth slices parameter model


for i in [0,1,2]:
    os.chdir(dir_reference) # change to directory reference model

    file_ref=list_reference_model[i]
    
    # open depth slices reference model
    t_model_ref = pd.read_csv(file_ref, 
                        sep=',', 
                        skiprows=1, usecols=[0,1,2,3], 
                        names=['long', 'lat', 'depth','temp']) # import file
    
    t_model_ref=t_model_ref.reindex(columns=['long','lat','temp','depth'])
    
       
    # directory parameter model
    
    os.chdir(dir_param) # list of depth slices parameter model
    
    # open depth slices parameter model
    file_param = list_param_model[i]
    
    t_model_param = pd.read_csv(file_param,
                        skiprows=1, usecols=[0,1,2,3], 
                        names=['long', 'lat', 'depth','temp']) # import file
    
    t_model_param = t_model_param.reindex(columns=['long','lat','temp','depth']) # reorder columns
    
    t_diff = t_model_ref.join(t_model_param, lsuffix='_ref', rsuffix='_param') # join df of reference and parameters model
    t_diff['t_diff'] = t_diff['temp_ref'] - t_diff['temp_param'] # calculate delta T°
    
    t_diff_short=t_diff.drop(columns=['long_param','lat_param', 'depth_param', 'temp_ref', 'temp_param']) # delete columns
    
    t_diff_short=t_diff_short.rename(columns={'long_ref':'long','lat_ref':'lat','depth_ref':'depth'}) # rename columns
    
    #t_diff_short.to_csv('')
    
    name_model=file_param[9:].split('_')[-2]+file_param[9:].split('_')[-1]# extract name of the model
    name_model=name_model.split('-')[0]
    depth_model= str(int(file_param[:-4].split('-')[-1])//1000)
    
    # directory difference maps
    
    os.chdir(dir_diff) # # list of depth slices difference maps
    
    t_diff_short.to_csv('Tdiff_' + name_model +'_' + depth_model + '.csv', index=False, sep=',')








