# -*- coding: utf-8 -*-
# author: Constanza Rodriguez Piceda

"""
Script to prepare lower boundary condition files to run advective-conductive transient simulation in GOLEM.
Input files are:
- comma-separated files (.csv) output from advective LYNX model with the following column format: id,temperature,x,y,z
Output files are: 
- a time wrapper with the timesteps and file paths (wrapper_bc.csv)
- files with lower boundary condition at each timestep with the following column format: x y temperature
"""
## import libraries
import os
import numpy as np
import pandas as pd

## define paths
path = r'..\out\out_csv' # path of input data (.csv files with temperature field at each timestep from LYNX simulation)
path_out = r'..\out\out_csv\reference' # path of output data 

## change working directory
os.chdir(path)

bc_list= [f for f in os.listdir(path) if os.path.isfile(f) & f.endswith('.csv')] # list of only files
bc_list_sorted = sorted(bc_list) # sorted list

##generate name
new_bc_name = [x.replace('transient_advection_csv_sample_nodes','bc') for x in bc_list_sorted] # rename the files
new_bc_name_path = ['data_bc/reference/'+ x for x in new_bc_name] # create path of files

## create wrapper file

time_list = [] # create empty list where all the timesteps will be stored


for i in range(len(bc_list_sorted)):
    time_int = int(bc_list_sorted[i][:-4].split('_')[-1])*10000 # extract the year from the file name and scale from Kyr to yr
    time_sa = f'{time_int/1e3:.0f}e3' # formatting time
    time_list.append(time_sa) # save in list
    
#print(time_list)

## create time wrapper
wrapper = [time_list, new_bc_name_path]

## save time wrapper
np.savetxt(path_out+'/wrapper_bc.csv', wrapper, delimiter=',', fmt='%s')


# create boundary condition files from input

cont=0 # counter for the name of the files 

for file in bc_list_sorted:
    df_bc = pd.read_csv(file) # read file
    
    # write header
    name_df_bc=new_bc_name[cont] # name of the file
    path_out_file= path_out + '/' + name_df_bc
    
    with open(path_out_file, 'w') as f:
        f.write('# x y temperature\n')    
    
    # write the rest
    df_bc.to_csv(path_out_file, columns=['x','y','temperature'], sep=' ', index=None, header=None, mode='a') # save only x y coordinates and temperature and change separator

    cont=cont+1

    