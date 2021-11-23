# -*- coding: utf-8 -*-
"""
plot density from PREM model
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
from scipy import interpolate
import scipy.stats as st
import scipy

os.chdir(r"..\VeloDT") # file location

df_prem = pd.read_csv('PREM_1s.csv', 
                        sep=' ', 
                        usecols= [1,2], # change depending on which columns of the original file are x, y and depth respectively
                        names=['z', 'density'])

z_list = df_prem['z'].tolist()
density_list = df_prem['density'].tolist()


depth_goes = np.array([50.14, 200])
density_vs = np.array([3303.95, 3379.28])
density_vp = np.array([3326.18, 3380])

f_vs= interpolate.interp1d(depth_goes,density_vs)
f_vp = interpolate.interp1d(depth_goes,density_vp)

# calculate the density
depth_new=np.arange(51,200, 1) # depth range for the first 20 km
density_vs_new=f_vs(depth_new)/1000 # T° for the first 20 km
density_vp_new=f_vp(depth_new)/1000
print(density_vs_new)

df_prem = pd.read_csv('SL2013rho_AlphaConst.dat', 
                        sep=' ', 
                        usecols= [1,2], # change depending on which columns of the original file are x, y and depth respectively
                        names=['z', 'density'])

fig, ax = plt.subplots() # to plot multiple datasets
ax.plot(density_list, z_list, label = 'density prem')
ax.plot(density_vs_new, depth_new, label = 'density vs (Goes et al. 2000)')
ax.plot(density_vp_new, depth_new, label = 'density vp (Goes et al. 2000)')
plt.legend()
plt.gca().invert_yaxis() # invert depth axis
ax.set_ylim(bottom=660, top =0)
ax.set_xlim(left=3, right=4)
plt.title('Density') #add title
plt.xlabel('Density (g/cm3)') #add label in x axes
plt.ylabel('Depth (km)') #add label in y axes
