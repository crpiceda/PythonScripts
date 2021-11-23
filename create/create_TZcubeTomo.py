# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:30:10 2021

@author: piceda
"""
import os
import numpy as np
import pandas as pd

path=r'Z:\piceda\PhD_RodriguezPiceda\Seismic\S-Assumpcao_etal_2013\Tomography_Feng\VsConversion_Goes\garnetlher-xenolith_AlphaConst\T_xenolith+garnetlher'
os.chdir(path)
temp_list=os.listdir(path)
temp_list = sorted(temp_list) # list of depth slices reference model

df_cube=pd.DataFrame(columns=['x','y','temperature','z'])
                     
for name_file in temp_list:
    temp=pd.read_csv(name_file,skiprows=20, usecols=[0,1,2], names=['x','y','temperature'], sep=' ')
    
    depth=int(name_file.split('_')[-2].split('-')[-1])
    
    temp['z']=-depth
    print(name_file,depth)
    df_cube=pd.concat([df_cube,temp])

df_cube=df_cube.sort_values(by=['z','y','x'],ascending=[False,True,True])

df_cube.to_csv('TZ_Cube_xenolith_garnetlher.txt',columns=['x','y','z','temperature'],index=None,sep=' ')

