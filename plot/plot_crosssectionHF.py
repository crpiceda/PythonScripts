# -*- coding: utf-8 -*-
"""
plot observed and modelled heat flow along a cross section
"""


## import libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cmcrameri import cm
from matplotlib import rcParams
from pyproj import Transformer
from scipy.interpolate import griddata

# to export text correctly
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

## directory
os.chdir(r'Z:\piceda\PhD_RodriguezPiceda\GOLEM\ModelMerged_tomo_TopSlabtest69\Interpol_topo-to-200km\heatflow')

## open file

data = pd.read_csv('HeatflowSurface_steepslab.txt',
                    sep=' ', skiprows=1, usecols=[0,1,2,3], names=['x','y','z','modHF'])

obs=pd.read_csv('obsHF_steepslab_UTM19.txt',
                    sep=' ', skiprows=1, usecols=[0,1,2], names=['x','y','measHF'])

# plot points to check transformation
rcParams['figure.figsize'] = 7, 3 # sets plot size
fig,ax1 =plt.subplots(1,1)
ax1.plot(data.x, data.modHF, label='Modelled heat flow')
ax1.scatter(obs.x,obs.measHF,marker='o', color='orange', label='Measured heat flow')

ax1.set_ylim(35,250)
ax1.set_ylabel('Heat Flow [mWm--2]')
ax1.legend()
ax1.set_title('steep slab')

fig.savefig('HeatflowSurface_obs-mod_steepslab.pdf')
fig.savefig('HeatflowSurface_obs-mod_steepslab.eps')





