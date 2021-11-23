# -*- coding: utf-8 -*-
"""
create files of depth below topography
"""


import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

## location file
directory = r"..\Diff_DepthSlices" # file location
os.chdir(directory) # file location

topo = pd.read_csv(r'Z_Surface.dat', sep=' ', skiprows=20, usecols=[0,1,2], names=['long', 'lat', 'depth']) # import file


depths = [2000, 5000, 10000, 20000]

for i in depths:
    topo_below = topo.copy()
    
    topo_below['depth'] = topo['depth'] - i
    
    topo_below.to_csv(r'topo_below' + str(int(i/1000)) +'km.txt', index = False, sep = ' ')
    
    topo_const = topo.copy()
    
    topo_const['depth'] =  -i
    
    topo_const.to_csv(r'topo_const' + str(int(i/1000)) +'km.txt', index = False, sep = ' ')