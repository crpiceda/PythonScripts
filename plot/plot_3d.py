# -*- coding: utf-8 -*-
"""
plot the top surface of the oceanic slab in 3D
"""

import matplotlib.pyplot as plt
import numpy as np
import os 
from mpl_toolkits.axes_grid1 import make_axes_locatable #
import pandas as pd
import glob as gl   
from scipy.interpolate import griddata
from matplotlib.patches import Polygon
import matplotlib.cm as cm # matplotlib's color map library
from matplotlib import rcParams
from scipy import interpolate
from matplotlib.colors import BoundaryNorm
from mpl_toolkits import mplot3d
import matplotlib
from matplotlib import rcParams
import shapefile

os.chdir(r"..\Temperature_TopSlab") # file location

#create data frame with depth and T at top of slab
df_temperature = pd.read_csv('TopSlab-feng_ZT.txt', 
                        sep=' ', 
                        usecols= [0,1,2,3], # change depending on which columns of the original file are x, y and depth respectively
                        skiprows=1, #skip comment lines 
                        names=['long', 'lat', 'depth', 'temp'])


## create mesh for plotting
X_unique = np.sort(df_temperature.long.unique())
Y_unique = np.sort(df_temperature.lat.unique())
X1, Y1 = np.meshgrid(X_unique, Y_unique)

Z2 = df_temperature.pivot_table(index='long', columns='lat', values='depth').T.values

Temp1 = df_temperature.pivot_table(index='long', columns='lat', values='temp').T.values
Z1=Z1.flatten()
X1=X1.flatten()
Y1=Y1.flatten()
Temp1=Temp1.flatten()

Z = np.array([])
Temp = np.array([])
X=np.array([])
Y=np.array([])
for i in range(len(Z1)):
    # print(X1[i])
    if (Z1[i]<=-55000 and Z1[i]>=-195000):
        add_Z=Z1[i]
        add_Temp=Temp1[i]
        add_X1=X1[i]
        add_Y1=Y1[i]
        Z=np.append(Z,add_Z)
        Temp=np.append(Temp,add_Temp)
        X=np.append(X,add_X1)
        Y=np.append(Y,add_Y1)
    # else :
    #     add_Z=0
    #     add_Temp=0
    #     add_X1=0
    #     add_Y1=0
    #     Z=np.append(Z,add_Z)
    #     Temp=np.append(Temp,add_Temp)
    #     X=np.append(X,add_X1)
    #     Y=np.append(Y,add_Y1)
    

Z = np.reshape(Z,(len(X_unique),len(Y_unique)))
X = np.reshape(X,(len(X_unique),len(Y_unique)))
Y = np.reshape(Y,(len(X_unique),len(Y_unique)))
Temp = np.reshape(Temp,(len(X_unique),len(Y_unique)))
# Temp
# nan_array = np.isnan(Temp)
# not_nan_array=~ nan_array
# Temp = Temp[not_nan_array]

# fourth dimention - colormap
# create colormap according to T-value (can use any array with 
color_dimension = Temp # change to desired fourth dimension
minn, maxx = color_dimension.min(), color_dimension.max()
norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='coolwarm')
m.set_array([])
fcolors = m.to_rgba(color_dimension)


# plot
rcParams['figure.figsize'] = 8, 7 # sets plot size
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, facecolors=fcolors, vmin=minn, vmax=maxx, shade=False)
#ax.plot_surface(X,Y,Z, rstride=1, cstride=1, facecolors=fcolors, vmin=np.nanmin(Z), vmax=np.nanmax(Z), shade=False)
plt.xticks(np.arange(200e3, 900e3, 200e3))
plt.yticks(np.arange(57e5, 70e5, 2e5))
#ax.set_zlim3d(-195000, -65000)
ax.tick_params(pad=10)
#ax.set_zlim([-180000,-70000])
cbar=fig.colorbar(m, shrink=0.5)
cbar.set_label('Temperature (°C)')
fig.show()
#fig.savefig('plot3d-TopSlabFeng.pdf', bbox_inches="tight") #save figure

