
"""
plot countour map of data in geographical coordinates
pip install pyproj==2.6.1.post1

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
import matplotlib.colors as colors

# to export text correctly
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

## directory
os.chdir(r'Z:\piceda\PhD_RodriguezPiceda\Figures\Paper2\SensitivityAnalysis_lbc\Model2Crust_50km-DeeperMoho_5km_test73')

## open file
# data = pd.read_csv('T_25km_geog.txt',
#                     sep=' ', skiprows=1, names=['x','y','z','temp'])
data = pd.read_csv('T_40km_geog.txt',
                    sep=' ', skiprows=1, names=['x','y','z','temp'])
#data.head()


# create columns with transformed coordinates
xx= data["x"]
yy= data["y"]

# plot points to check transformation
rcParams['figure.figsize'] = 4.5, 5 # sets plot size
fig,ax1 =plt.subplots(1,1)
ax1.plot(xx,yy,marker='o')


# define coordinates for grid
xs = np.linspace(-72,-65,100)
ys = np.linspace(-39,-29,100)

# grid the data
xi,yi=np.meshgrid(xs,ys) # create grid
zi = griddata((data["x"], data["y"]), data["temp"] ,(xi,yi) , method='linear') # grid data with cubic method

# since cubic method does not extrapolate outside of the convex hull, we have
# to grid the data with NN and then apply does values to the previous grid  
z_rep = griddata((data["x"], data["y"]), data["temp"] ,(xi,yi) , method='nearest') # grid data with nearest neighbour
mask= np.isnan(zi) # create mask (boolean array where there is nan values)
zi[mask]=z_rep[mask] # replace where is nan values by the values from NN interpolation

## plots
# create plots
fig2,ax2= plt.subplots(1,1)

# make the norm: the center is offset:
divnorm = colors.TwoSlopeNorm(vmin=-460, vcenter=0, vmax=10)
levels=np.linspace(190,440,26)

#cs=ax2.contourf(xi,yi,zi,48,cmap='bwr',norm=divnorm)
#cs=ax2.contourf(xi,yi,zi,26,cmap=cm.roma_r)

cs=ax2.contourf(xi,yi,zi,levels,cmap=cm.roma_r)

#ax2.set_xlabel('Latitude')
#ax2.set_ylabel('Longitude')
cbar = fig2.colorbar(cs, label='Temperature [°C]')
ax2.tick_params(axis='x',which='both',direction='in',right=True)
ax2.tick_params(axis='y',which='both',direction='in',right=True)

# set absolute value in x
ticks_x= ax2.get_xticks() 
ax2.set_xticklabels([int(abs(tick)) for tick in ticks_x])

# set absolute value in y
ticks_y = ax2.get_yticks()
ax2.set_yticklabels([int(abs(tick)) for tick in ticks_y])

# add suffix in labels of x
labels = [item.get_text() for item in ax2.get_xticklabels()]
labels_mod= [label + '°W' for label in labels]
ax2.set_xticklabels(labels_mod)

# add suffix in labels of y
labels = [item.get_text() for item in ax2.get_yticklabels()]
labels_mod= [label + '°S' for label in labels]
ax2.set_yticklabels(labels_mod)

# save figure
fig2.savefig('T_40km_geog.pdf')