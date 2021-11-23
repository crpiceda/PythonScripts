"""
merge files with seismic events with Mb and Mw. Filter events according to completeness
"""


import pandas as pd
import os
import numpy as np
import math

os.chdir(r'..\SCA')


data_mw = pd.read_csv('seismicity_ISC_reviewedcat_Mw_SCA_clean.txt', sep=' ') # open data mw
data_mb = pd.read_csv('seismicity_ISC_reviewedcat_Mb_SCA_clean.txt',  sep=' ') # open data mb

# scale mB to Mw
data_mb['mag_mw']= 1.22*data_mb['mag']-1.45

data_mw['mag_mw']= data_mb['mag']

data_all=data_mb.append(data_mw) # append data set

data_all_clean=data_all.drop_duplicates(subset=['date', 'time'], keep='last') # check if there are duplicates events based on date and time

h_mag_year = ['long','lat','depth','depth_error','mag_mw','year']

data_all_clean.to_csv('seismicity_ISC_reviewedcat_MWall_mag-year_clean.txt', columns = h_mag_year , index = False, sep = ' ')

data_all_clean_short = data_all_clean.drop(columns=['mag'])
data_all_clean_short.to_csv('seismicity_ISC_reviewedcat_MWall_clean.txt', index = False, sep = ' ')

data_completeness=data_all_clean_short[data_all_clean_short['mag_mw']>=4.8] # filter according to completeness magnitude

data_completeness.to_csv('seismicity_ISC_reviewedcat_Mwall_completeness.txt',index = False, sep = ' ')