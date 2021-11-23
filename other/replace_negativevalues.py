"""
Created on Fri Aug 14 16:10:32 2020

@author: piceda

This script replaces negative values of a column by zeros

"""

import numpy as np
from scipy.interpolate import griddata
import os
import pandas as pd


## directory
os.chdir('')

## import file
topo_data = pd.read_csv(r'Z_06_ContinentalMantle.dat', sep=' ', skiprows=20, usecols=[0,1,2], names=['long', 'lat', 'depth']) 

print(topo_data)

#topo_data.loc[topo_data.depth< 0, "depth"] = 0 # replace negative depths by 0


topo_data.to_csv(r"moho_5km_cero.txt", index = False, sep = ' ') # save file

#len(topo_data.lat.unique())