# -*- coding: utf-8 -*-
"""
plot variation of temperature against depth and vs
"""

import matplotlib.pyplot as plt
import numpy as np
import os 
from mpl_toolkits.axes_grid1 import make_axes_locatable 
import pandas as pd
import glob as gl   # Manejo de archivos externos
from scipy.interpolate import griddata
from matplotlib.patches import Polygon
import matplotlib.cm as cm # matplotlib's color map library
from matplotlib import rcParams
from scipy import interpolate
from matplotlib.colors import LinearSegmentedColormap # to handle colormaps

os.chdir(r"..\Tomography_Feng\VsConversion_Goes\workingfiles_synthetic") # file location

# import file output conversion
df_conversion = pd.read_csv(r'VT_synthetic_AlphaConst_garnetlher.txt', 
                           sep=' ', 
                           skiprows=1, 
                           usecols=[0,1,2,3,4], 
                           names=['long', 'lat', 'depth', 'Vs', 'temp']) 

# filter depths < -200 km (deeper than the base of the model) and remove depth = 75 km (anomalous velocities)
#df_conversion_filtered=df_conversion[(df_conversion['depth']>=-200000) & (df_conversion['depth']!=-75000)]
df_conversion_filtered=df_conversion[(df_conversion['depth']>=-200000) & (df_conversion['depth']!=-75000) & (df_conversion['Vs']>=4200)]

### create mesh for plotting
Z = df_conversion_filtered.pivot_table(index='Vs', columns='depth', values='temp').T.values

X_unique = np.sort(df_conversion_filtered.Vs.unique())
Y_unique = np.sort(df_conversion_filtered.depth.unique())

X, Y = np.meshgrid(X_unique, Y_unique)


### create 1-D Vs profiles of the seismic tomography of Assumpcao et al (2013)

# import file output conversion with tomography
df_tomo = pd.read_csv(r'Rho_feng_AlphaPT_garnetlher.dat', 
                           sep=' ', 
                           skiprows=20, 
                           usecols=[0,1,2,3,4,5], 
                           names=['long', 'lat', 'depth', 'Vs', 'temp', 'rho'])

# filter depths < -200 km (deeper than the base of the model)
df_tomo_filtered=df_tomo[df_tomo['depth']>=-200000]

# filter anomalous vs values at 75 km
df_tomo_filtered=df_tomo_filtered[df_tomo_filtered['depth']!=-75000]


#df_tomo_filtered.to_csv(r"T_synthetic_AlphaConst_garnetlher", index = False, sep = ' ')

## location 1 (flat slab)
# filter velocities at one location
df_tomo_location=df_tomo_filtered[(df_tomo_filtered['lat']== -31.000013) & (df_tomo_filtered['long']== -69.750153)].drop_duplicates()

df_tomo_location=df_tomo_location.iloc[::2, :] # filter every 2 rows of the DataFrame

# convert depth and vs to arrays
depth_location = np.asarray(df_tomo_location['depth'])
vs_location = np.asarray(df_tomo_location['Vs'])

## location 2 (transition zone)
# filter velocities at one location
df_tomo_location2=df_tomo_filtered[(df_tomo_filtered['lat']== -34.249992) & (df_tomo_filtered['long']== -71.25014499999999)].drop_duplicates()

df_tomo_location2=df_tomo_location2.iloc[::2, :] # filter every 2 rows of the DataFrame

# convert depth and vs to arrays
depth_location2 = np.asarray(df_tomo_location2['depth'])
vs_location2 = np.asarray(df_tomo_location2['Vs'])

## location 3 (steep slab)
# filter velocities at one location
df_tomo_location3=df_tomo_filtered[(df_tomo_filtered['lat']== -37.249973) & (df_tomo_filtered['long']== -71.25014499999999)].drop_duplicates()

df_tomo_location3=df_tomo_location3.iloc[::2, :] # filter every 2 rows of the DataFrame

# convert depth and vs to arrays
depth_location3 = np.asarray(df_tomo_location3['depth'])
vs_location3 = np.asarray(df_tomo_location3['Vs'])

### plot

# Initialize plot objects
rcParams['figure.figsize'] = 5,5  # sets plot size
fig,ax=plt.subplots(1,1)

# load colormap
cm_data = np.loadtxt("roma.txt") # load txt with colormap
roma_map = LinearSegmentedColormap.from_list('roma', cm_data).reversed() # create a colormap that can be read by matplotlib


# Define levels of contour mapchange space
#levels = np.linspace(400,1700,14)
levels = np.linspace(400,1500,12)

cpf = ax.contourf(X,Y,Z, levels, cmap=roma_map) # Generate a color mapping of the levels we've specified for the temperature
ax.plot(vs_location, depth_location, linestyle='-', color='black', linewidth=1, marker='o', ms=5, markeredgewidth=1, markerfacecolor="None", markeredgecolor='black') # plot Vs at chosen location
ax.plot(vs_location2, depth_location2, linestyle='-', color='grey', linewidth=1, marker='o', ms=5, markeredgewidth=1, markerfacecolor="None", markeredgecolor='grey') # plot Vs at chosen location
ax.plot(vs_location3, depth_location3, linestyle='-', color='olive', linewidth=1, marker='o', ms=5, markeredgewidth=1, markerfacecolor="None", markeredgecolor='olive') # plot Vs at chosen location
cbar = plt.colorbar(cpf)
cbar.set_label('Temperature (°C)')
#plt.xticks(np.arange(3600, 4800, 200)) # plot ticks in x
plt.xticks(np.arange(4200, 4800, 200)) # plot ticks in x
ax.set_ylim([-200000,-80000]) # set limit in y axis
#plt.yticks(np.arange(-200000, -80000, 10000)) # plot ticks in x
#plt.xticks([X_unique.min(),100e3,X_unique.max()])
#plt.yticks([Y_unique.min(),1e5,Y_unique.min()])
ax.set_xlabel('Vs (m/s)') #set labels x
ax.set_ylabel('Depth (m.b.s.l.)') # set labels y
plt.title('goes alpha constant python')

#plt.savefig('T_synthetic_AlphaConst_garnetlher.svg', bbox_inches='tight', format='svg', dpi=200)
#plt.savefig('T_synthetic_AlphaConst_garnetlher.pdf', bbox_inches='tight', format='pdf', dpi=200)

