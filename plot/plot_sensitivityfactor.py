# -*- coding: utf-8 -*-
"""
plot sensitivity factor of thermal properties
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
from matplotlib.ticker import MaxNLocator

rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

# directories
dir_diff = r'.\ModelsSensitivity'

os.chdir(dir_diff)
df=pd.read_csv(r'Sensitivity_factor.csv')

df['number']=df.index

df.kmin=abs(df.kmin)
df.kmax=abs(df.kmax)
df.smax=abs(df.smax)
df.smin=abs(df.smin)

# Initialize plot objects
rcParams['figure.figsize'] = 5, 3 # sets plot size
fig,ax1 =plt.subplots(1,1)

ax1.plot(df.number, df.kmin, marker='o', label='kmin')
ax1.plot(df.number, df.kmax, marker='o', linestyle='--', color='C0', label='kmax')
ax1.plot(df.number, df.smin, marker='o', label='smin')
ax1.plot(df.number, df.smax, marker='o', linestyle='--', color='orange', label='smax')

ax1.legend()
ax1.set_ylabel('Factor [°C/%]')

fig.savefig('sensitivityfactor.png')
fig.savefig('sensitivityfactor.eps')
fig.savefig('sensitivityfactor.pdf')