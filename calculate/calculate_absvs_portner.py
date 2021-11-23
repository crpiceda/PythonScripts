# -*- coding: utf-8 -*-
"""
calculate absolute velocity from velocity residual
caution: in the calculation no term of the mean velocity is added
"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import interpolate

directory = r"..\OriginalData"
os.chdir(directory) # file location

# Read file dvp
samdvp = pd.read_csv(r'SAM4-P-2017_percent_SCA.txt', 
                    sep=' ', 
                    skiprows=1,
                    usecols=[0,1,2,3],
                    names=['x', 'y','z', 'dvp'])
print(samdvp)

#samdvp.to_csv(r"SAM4-P-2017_percent.txt", sep=' ', index = None)

iasp91 = pd.read_csv('IASP91.csv', 
                    sep=',', 
                    skiprows=1,
                    usecols=[0,2],
                    names=['z', 'vp'])

#create a function to interpolate between the data
x = np.asarray(iasp91['z'].tolist()).squeeze() #convert to numpy array (squeeze used to remove single-dimensional axes)
y = np.asarray(iasp91['vp'].tolist()).squeeze() #convert to numpy array
f= interpolate.interp1d(x,y, fill_value="extrapolate")

# calculate vs for the desired depth interval
z_list=[60, 95, 130, 165, 200, 240, 280, 320, 365, 410, 455, 505, 605, 660, 715, 775, 835, 895, 940, 1010] #depths from dvs
xnew=np.array(z_list)
ynew=f(xnew) 

# Calling DataFrame constructor after zipping 
# both lists, with columns specified 
iasp_red = pd.DataFrame(list(zip(xnew, ynew)), 
                        columns =['z', 'vs']) 

print(iasp_red)

#iasp_red.to_csv(r"iasp91_red.txt", sep=' ', index = None)

samdvp['vp']=''
print(samdvp)

for i in samdvp.index:
    if samdvp['z'][i]==60:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*8.0429
    if samdvp['z'][i]==95:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*8.047049999999999
    if samdvp['z'][i]==130:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*8.0778
    if samdvp['z'][i]==165:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*8.175
    if samdvp['z'][i]==200:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*8.2722
    if samdvp['z'][i]==240:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*8.4095
    if samdvp['z'][i]==280:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*8.5555
    if samdvp['z'][i]==320:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*8.7015
    if samdvp['z'][i]==365:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*8.86575
    if samdvp['z'][i]==410:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*9.03
    if samdvp['z'][i]==455:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*9.5112
    if samdvp['z'][i]==505:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*9.6792
    if samdvp['z'][i]==605:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*10.0152
    if samdvp['z'][i]==660:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*10.2
    if samdvp['z'][i]==715:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*10.9362
    if samdvp['z'][i]==775:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*11.08275
    if samdvp['z'][i]==835:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*11.187575
    if samdvp['z'][i]==895:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*11.291075
    if samdvp['z'][i]==940:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*11.36542
    if samdvp['z'][i]==1010:
       samdvp['vp'][i]=(samdvp['dvp'][i]/100+1)*11.47968

samdvp.to_csv(r"SAM4-P-2017_percent_vp_SCA.txt", sep=' ', index = None)
