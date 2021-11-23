"""
Created on Fri Aug 14 16:10:32 2020

@author: piceda

This script calculates the pseudotopography for a given topography and thicknesses of crustal layers

"""
## import libraries
import numpy as np
import os
import pandas as pd

## directory
os.chdir(r'..\pseudotopography')

## import files
topo = pd.read_csv(r'topo_5km_cero_smoothed_petrel.txt', sep=' ', skiprows=20, usecols=[0,1,2], names=['long', 'lat', 'depth'])
thk_sed =  pd.read_csv(r'Thickness_03_ContinentalSediments_5km_smoothed50km.dat', sep=' ', skiprows=20, usecols=[0,1,2], names=['long', 'lat', 'thk'])
thk_uc =  pd.read_csv(r'Thickness_04_UpperContinentalCrust_5km_smoothed50km.dat', sep=' ', skiprows=20, usecols=[0,1,2], names=['long', 'lat', 'thk'])
thk_lc =  pd.read_csv(r'Thickness_05_LowerContinentalCrust_5km_smoothed50km.dat', sep=' ', skiprows=20, usecols=[0,1,2], names=['long', 'lat', 'thk'])

topo.loc[topo.depth< 0, "depth"] = 0 # replace negative depths by 0

## data with densities
rho_t, rho_c, rho_sed, rho_uc, rho_lc = 2670, 2970, 2400, 2800, 3100

## DataFrame with data to calculate pseudotopography
df_calc = pd.DataFrame(columns = ['x', 'y', 'topo', 'thk_sed', 'thk_uc', 'thk_lc', 'pseudotopo']) # create dataframe

# assign coordinates, topography and thickness of the crustal layers
df_calc.x = topo.long  # longitude
df_calc.y = topo.lat # latitude
df_calc.topo = topo.depth # topography
df_calc.thk_sed = thk_sed.thk # thk sediments
df_calc.thk_uc = thk_uc.thk # thk upper crust
df_calc.thk_lc = thk_lc.thk # thk lower crust

#print(df_calc)

## calculate pseudotopography

# define function to calculate pseudotopography
def calc_pseudotopo(h, thk_sed, thk_uc, thk_lc, rho_c, rho_sed, rho_uc, rho_lc, rho_t):
    pseudotopo = h + ((thk_sed*(rho_sed-rho_c))+(thk_uc*(rho_uc-rho_c))+(thk_lc*(rho_lc-rho_c)))/rho_t
    
    return pseudotopo

# calculate pseudotopography for each point
df_calc['pseudotopo'] = np.vectorize(calc_pseudotopo)(df_calc['topo'], df_calc['thk_sed'], df_calc['thk_uc'], df_calc['thk_lc'], rho_c, rho_sed, rho_uc, rho_lc, rho_t)


## create DataFrame with pseudotopography
df_pseudotopo = pd.DataFrame(columns = ['x', 'y', 'z_pseudotopo'])

df_pseudotopo.x = df_calc['x']
df_pseudotopo.y = df_calc['y']
df_pseudotopo.z_pseudotopo = df_calc['pseudotopo']


#print(df_pseudotopo)

df_pseudotopo.to_csv(r"pseudotopo_5km_smoothed50km.txt", index = False, sep = ' ') # save file

 
## create DataFrame with topography
df_topo = pd.DataFrame(columns = ['x', 'y', 'z_topo'])

df_topo.x = df_calc['x']
df_topo.y = df_calc['y']
df_topo.z_topo = df_calc['topo']

#df_topo.to_csv(r"topo.txt", index = False, sep = ' ') # save file
