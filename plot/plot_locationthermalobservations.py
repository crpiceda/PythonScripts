
"""
plot location of thermal observations (temperature and heat flow)
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
import matplotlib.colors as colors

# to export text correctly
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42


## directory
os.chdir(r'..\Model2Crust_50km-DeeperMoho_5km_test73\visualization')

## open file
data = pd.read_csv('Tdiff_corrected_geog.txt',
                    sep=' ', skiprows=1, names=['x','y', 'z', 'measT', 'modT','Tdiff'])
# data = pd.read_csv('Tdiff_correctedT2_geog.txt',
#                     sep=' ', skiprows=1, names=['x','y', 'measT', 'z', 'modT','Tdiff'])

## plots
# create plots
fig,ax2 = plt.subplots()
ax2.set_aspect('equal')

# make the norm: the center is offset:
divnorm = colors.TwoSlopeNorm(vmin=-10, vcenter=0, vmax=80)

cs=ax2.scatter(data.x,data.y,c=data.Tdiff,marker="D", cmap='bwr', norm=divnorm)
#cs=ax2.scatter(data.x,data.y,c=data.modT,marker="D", cmap=cm_cram.roma_r)
ax2.set_xlabel('Latitude', fontsize=10)
ax2.set_ylabel('Longitude', fontsize=10)
ax2.set_xlim(left=-72, right=-66)
ax2.set_ylim(bottom=-39,top=-29)

# color bar
divider = make_axes_locatable(ax2)
cax = divider.append_axes("right", size="8%", pad=0.1)
cbar = plt.gcf().colorbar(cs, cax=cax) # colorbar
cbar.ax.tick_params(labelsize=10)
cbar.set_label(label='Observed Temperature [°C]', fontsize=10)

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

fig.savefig('Tdiff_points_geog.pdf')