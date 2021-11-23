# -*- coding: utf-8 -*-
"""
Heat flow at surface from Paraview

This script requires:
csv HeatFlowSurface.csv from paraview
HF_Lucazeau_SCA_UTM19_onlycoordinates.txt
HF_Lucazeau_SCA_UTM19_petrel.txt (measured HF)


returns:
- plot of heat flow
- ordered file with modelled HF at surface (with correct order of columns and no duplicates)
- Wells of modelled HF
- histogram with HFdiff
- text file with HFdiff
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable
import pandas as pd
import glob as gl  
from scipy.interpolate import griddata
from matplotlib.patches import Polygon
import matplotlib.cm as cm # matplotlib's color map library
from matplotlib import rcParams
from scipy import interpolate
from matplotlib.ticker import PercentFormatter
import matplotlib.gridspec as gridspec

# to export text correctly
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

## location file
directory = r"..\Interpol_topo-to-200km\heatflow" # file location
os.chdir(directory) # file location
list_directory = directory.split('\\') #sepate the directory name to obtain the name of the model
name_model = list_directory[-1] # get the name of the model

# Read file modelled HF from paraview
modHF = pd.read_csv(r'HeatFlowSurface_Paraview.csv', sep=',', skiprows=1, usecols=[0,1,2,3], names=['modHF', 'long', 'lat', 'depth']) # import file

columnsTitles= ['long', 'lat', 'depth','modHF'] # new order of columns 
modHF=modHF.reindex(columns=columnsTitles) # change order of columns

#print(modHF)
#modHF.to_csv(r"Heatflow_python_temp.txt", index = False, sep = ' ') # save ordered file with duplicates

## create mesh for plotting
Z = modHF.pivot_table(index='long', columns='lat', values='modHF').T.values

X_unique = np.sort(modHF.long.unique())
Y_unique = np.sort(modHF.lat.unique())

X, Y = np.meshgrid(X_unique, Y_unique)

# Initialize plot objects
rcParams['figure.figsize'] = 5, 6 # sets plot size
fig,ax=plt.subplots(1,1)

# Define levels of contour mapchange space
levels = np.linspace(30,105,16)

# Generate a color mapping of the levels we've specified
cpf = ax.contourf(X,Y,Z, levels, cmap=cm.inferno)


# Make plot and customize axes
#cp = ax.contour(X, Y, Z, levels, colors='black')
#ax.clabel(cpf, fontsize=10)
cbar = plt.colorbar(cpf)
cbar.set_label('Heat Flow (mW/m2)')
plt.xticks(np.arange(200e3, 900e3, 200e3)) # plot ticks in x (depends on type of coordinates)
#plt.xticks([X_unique.min(),100e3,X_unique.max()])
#plt.yticks([Y_unique.min(),1e5,Y_unique.min()])
ax.set_xlabel('Easting (m)') #set labels x
ax.set_ylabel('Northing (m)') # set labels y
plt.title('Heat flow at surface')

# save figure
plt.savefig('HF_atsurface_utm19.png', bbox_inches='tight', format='png', dpi=200)


### Extract modelled HF at well locations

## filter duplicate values (because the original file comes from a composed vtk file and some locations are duplicated). It takes the max value
modHF = modHF.loc[modHF.groupby(['long','lat']).modHF.idxmax()]
modHF.to_csv(r"HeatflowSurface_noduplicates.txt", index = False, sep = ' ') # save ordered file without duplicates

## Create interpolation
HF=np.array(modHF.modHF).reshape(len(Y_unique), len(X_unique))

xx, yy = np.meshgrid(X_unique, Y_unique)
f = interpolate.interp2d( X_unique, Y_unique, HF, kind='cubic' )

## Read coordinate file
coord = pd.read_csv(r'HF_Lucazeau_SCA_UTM19_onlycoordinates.txt', sep=' ', skiprows=1, usecols=[0,1], names=['long', 'lat']) # import file

## define function that will read the modelled HF at the desired locations
def givemeZ(x,y):
    hfcoord=f(x,y)
    return int(hfcoord)

## extract modelled HF at the desired locations
result = [givemeZ(x, y) for x, y in zip(coord['long'], coord['lat'])]

## add the extracted modelled heat flow to the desired locations
wells_HF=coord.merge(pd.DataFrame(result), left_index=True, right_index=True)

## create header for output file
wells_HF.columns = ['long', 'lat', 'modHF']

## output file
wells_HF.to_csv(r"Heatflow_Wells.txt", index = False, sep = ' ') # save ordered file

### create histogram with differences between modelled and measured HF
## Read coordinate file
df_measHF = pd.read_csv(r'HF_Lucazeau_SCA_UTM19_petrel.txt', sep=' ', skiprows=1, usecols=[0,1,2], names=['long', 'lat', 'measHF']) # import file

# Merge tables w/ measured and modelled heat flow
df_merged = pd.merge(df_measHF, wells_HF)
print(df_merged)

# Calculate difference between measured and modelled heat flow
df_merged['HFdiff']= df_merged['measHF']-df_merged['modHF']

# Create histogram HFdiff

Hdiff_list = df_merged['HFdiff'].tolist() # Convert DataFrame.Column to list

# Initialize plot objects
rcParams['figure.figsize'] = 5, 3 # sets plot size
fig,ax=plt.subplots(1,1)

plt.hist(Hdiff_list, bins=25, range=[-260, 260], weights=np.ones(len(Hdiff_list)) / len(Hdiff_list), linewidth=0.5)

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.title('HF diff ' + name_model)
#plt.xlabel('HF [mW/m2]')
plt.ylabel('Frequency')

plt.savefig('HFdiff.svg')
plt.savefig('HFdiff.pdf')

plt.show()

# save DataFrame as csv
df_merged.to_csv(r"HFdiff.dat", sep=' ', index = None)
