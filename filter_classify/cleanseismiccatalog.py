# -*- coding: utf-8 -*-
"""
remove seismic events with fixed depth and calculate seismic moment from Mb and Ms
"""
import pandas as pd
import os
import numpy as np
import math

## location file
directory = r"" # file location
os.chdir(directory) # file location

hypodata = pd.read_csv(r'seismicity_ISC-EHB_Mb_extended.txt', sep=',', skiprows=2, usecols=[0,1,2,3,4,5,6,7,8,9,10,11], names=['eventid','cat','date','time','lat','long','depth','depfix','depqual','author','type','mag']) # import file


columnsTitles= ['long','lat','depth','date','time','cat','eventid','depfix','depqual','author','type','mag'] # new order of columns 
hypodata=hypodata.reindex(columns=columnsTitles) # change order of columns


hypodata_filtered = hypodata[(hypodata['depqual']== 'L1') & (hypodata['depfix']!= True)]


# calculate seismic moment for Mb

def calc_Mo(Mb):
    Mo = (10**((1.27*(Mb-1.69)/0.66) + 17.23))/1e7 # Chen et al. (2007)
    return Mo


# def calc_Mo(Ms):
#     Mo = (10**((1.27*(Ms+0.53)/1.03) + 17.23))/1e7 # Chen et al. (2007)
#     return Mo


hypodata_filtered['mo'] = hypodata_filtered['mag'].apply(lambda x: calc_Mo(x))   

hypodata_filtered['logmo'] = hypodata_filtered['mo'].apply(lambda x: math.log(x))   

def calc_Mw(Mo):
    Mw = (2/3)*(math.log(Mo)-9.1) # Kanamori (1997)
    return Mw

hypodata_filtered['mw'] = hypodata_filtered['mag'].apply(lambda x: calc_Mw(x))  



hypodata_filtered.to_csv('seismicity_ISC-EHB_ML_extended_filtered.txt', index = False, sep = ' ')

