# -*- coding: utf-8 -*-
"""
calculate difference maps between reference and alternative model
plot temperature against depth and vs
"""


import matplotlib.pyplot as plt
import numpy as np
import datetime as dt # Manejo de fechas
import os #para importar información de otros directorios
from mpl_toolkits.axes_grid1 import make_axes_locatable # para el manejo del tamano del colorbar
import pandas as pd
import glob as gl   # Manejo de archivos externos
from scipy.interpolate import griddata
from matplotlib.patches import Polygon
import matplotlib.cm as cm # matplotlib's color map library
from matplotlib import rcParams
from scipy import interpolate

os.chdir(r"..\Tomography_Feng\VsConversion_Goes\workingfiles_synthetic") # file location

# import file output conversion
df_conversion = pd.read_csv(r'VT_synthetic_AlphaConst_garnetlher.txt', 
                           sep=' ', 
                           skiprows=1, 
                           usecols=[0,1,2,3,4], 
                           names=['long', 'lat', 'depth', 'Vs', 'temp']) 

# filter depths > -80 km and < -200 km (limits of the model) and remove depth = 75 km (anomalous velocities)
df_conversion_filtered=df_conversion[(df_conversion['depth']>=-200000) & (df_conversion['depth']!=-75000) & (df_conversion['Vs']>=4200)]


# import file output conversion 2
df_conversion2 = pd.read_csv(r'VT_synthetic_AlphaPT_python.txt', 
                           sep=' ', 
                           skiprows=1, 
                           usecols=[0,1,2,3,4], 
                           names=['long', 'lat', 'depth', 'Vs', 'temp']) 

# filter depths > -80 km and < -200 km (limits of the model) and remove depth = 75 km (anomalous velocities)
df_conversion_filtered2=df_conversion2[(df_conversion2['depth']>=-200000) & (df_conversion2['depth']!=-75000) & (df_conversion['Vs']>=4200)]

## create DF with difference of T
df_diff = pd.DataFrame(columns=['long', 'lat', 'depth', 'Vs', 'diffT'])

df_diff.long = df_conversion_filtered.long
df_diff.lat = df_conversion_filtered.lat
df_diff.depth = df_conversion_filtered.depth
df_diff.Vs = df_conversion_filtered.Vs
df_diff.diffT = df_conversion_filtered['temp'] - df_conversion_filtered2['temp']

## create mesh for plotting
Z = df_diff.pivot_table(index='Vs', columns='depth', values='diffT').T.values

X_unique = np.sort(df_diff.Vs.unique())
Y_unique = np.sort(df_diff.depth.unique())

X, Y = np.meshgrid(X_unique, Y_unique)


### to plot 1-D velocity profiles of the seismic tomography of Assumpcao et al (2013)

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


### build plot

# Initialize plot objects
rcParams['figure.figsize'] = 5,5  # sets plot size
fig,ax=plt.subplots(1,1)

# Define levels of contour mapchange space
#levels = np.linspace(-500,500,21)
levels = np.linspace(-200,200,21)

# plot
cpf = ax.contourf(X,Y,Z, levels, cmap=cm.seismic) # Generate a color mapping of the levels we've specified for the temperature
ax.plot(vs_location, depth_location, linestyle='-', color='black', linewidth=1, marker='o', ms=5, markeredgewidth=1, markerfacecolor="None", markeredgecolor='black') # plot Vs at chosen location
ax.plot(vs_location2, depth_location2, linestyle='-', color='grey', linewidth=1, marker='o', ms=5, markeredgewidth=1, markerfacecolor="None", markeredgecolor='grey') # plot Vs at chosen location
ax.plot(vs_location3, depth_location3, linestyle='-', color='olive', linewidth=1, marker='o', ms=5, markeredgewidth=1, markerfacecolor="None", markeredgecolor='olive') # plot Vs at chosen location
cbar = plt.colorbar(cpf)
cbar.set_label('Difference Temperature (°C)')
plt.xticks(np.arange(4200, 4800, 200)) # plot ticks in x
ax.set_ylim([-200000,-80000]) # set limit in y axis
#plt.xticks([X_unique.min(),100e3,X_unique.max()])
#plt.yticks([Y_unique.min(),1e5,Y_unique.min()])
ax.set_xlabel('Vs (m/s)') #set labels x
ax.set_ylabel('Depth (m.b.s.l.)') # set labels y
plt.title('AlphaConst-AlphaPT')

#save files
#plt.savefig("T_synthetic_AlphaConst_XenolithAP_v2" + '.pdf')
#plt.savefig("T_synthetic_AlphaConst_XenolithAP_v2" + '.svg')

#df_diff.to_csv(r"Tdiff_synthetic_Goes-PM.txt", index = False, sep = ' ')