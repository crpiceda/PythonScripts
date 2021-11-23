# -*- coding: utf-8 -*-
"""
plot slab2 contour
"""

## import libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cmcrameri import cm as cm_cram
import matplotlib.cm as cm # matplotlib's color map library
from matplotlib import rcParams
from pyproj import Transformer
from scipy.interpolate import griddata
import glob
import fnmatch
from mpl_toolkits.axes_grid1 import make_axes_locatable


## directory
path =r'..\Slab2' 
os.chdir(path)

slab= pd.read_csv('sam_slab2_dep_mod.xyz', sep = ' ', names=['x','y','z'])

# define coordinates for grid
xs = np.linspace(-72,-65,100)
ys = np.linspace(-39,-29,100)

# grid the data
xi,yi=np.meshgrid(xs,ys) # create grid
zi = griddata((slab["x"], slab["y"]), slab["z"] ,(xi,yi) , method='cubic') # grid data    

## plots
# create plots
fig,ax2 = plt.subplots()
ax2.set_aspect('equal')



cs=ax2.contour(xi,yi,zi,15,cmap=cm.inferno)
ax2.set_xlabel('Latitude', fontsize=10)
ax2.set_ylabel('Longitude', fontsize=10)

# color bar
divider = make_axes_locatable(ax2)
cax = divider.append_axes("right", size="5%", pad=0.1)
cbar = plt.gcf().colorbar(cs, cax=cax) # colorbar
cbar.ax.tick_params(labelsize=10)
cbar.set_label(label='depth (kmasl)', fontsize=10)

# set absolute value in x
ticks_x= ax2.get_xticks() 
ax2.set_xticklabels([int(abs(tick)) for tick in ticks_x])

# set absolute value in y
ticks_y = ax2.get_yticks()
ax2.set_yticklabels([int(abs(tick)) for tick in ticks_y])

# add suffix in labels of x
labels = [item.get_text() for item in ax2.get_xticklabels()]
labels_mod= [label + '°S' for label in labels]
ax2.set_xticklabels(labels_mod, fontsize=10)

# add suffix in labels of y
labels = [item.get_text() for item in ax2.get_yticklabels()]
labels_mod= [label + '°W' for label in labels]
ax2.set_yticklabels(labels_mod, fontsize=10)

plt.gcf().subplots_adjust(wspace=1)

fig.savefig('contoursdepth_slab2_SCA.eps')