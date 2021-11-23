# -*- coding: utf-8 -*-
"""
plot countour map of mechanical coupling
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
from cmcrameri import cm
import matplotlib

#%% when exporting, treat every character as text instead of shape
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

#%% paths
os.chdir(r'Z:\piceda\PhD_RodriguezPiceda\Rheology\SRvariable\SCA12_1km_PEIERLS2\output\paraview')
path_model_output=r'Z:\piceda\PhD_RodriguezPiceda\Figures\Paper3\IntegratedStrength\SCA12_PEIERLS2'
#%% open data
coupling = pd.read_csv('SCA_model_20_coupling.txt', sep=' ', usecols=[0,1,2], skiprows=1, names=['x', 'y', 'deltathk'])
model = pd.read_csv('SCA_model_20_mechanicalthickness.txt', sep=' ', usecols=[0,1,2], skiprows=1, names=['x', 'y', 'mechthk'])

#%% prepare data
model['deltathk'] = coupling['deltathk']
model['coupling'] = coupling['deltathk']
model.loc[model['deltathk']<0, 'coupling']=1 # coupled case
model.loc[model['deltathk']>0, 'coupling']=0 # decoupled case

#%% plot results

## create mesh for plotting
Z = model.pivot_table(index='x', columns='y', values='mechthk').T.values
Z2 = model.pivot_table(index='x', columns='y', values='coupling').T.values

X_unique = np.sort(model.x.unique())
Y_unique = np.sort(model.y.unique())

X, Y = np.meshgrid(X_unique, Y_unique)

# Initialize plot objects
rcParams['figure.figsize'] = 9, 5 # sets plot size
fig,(ax1,ax2) =plt.subplots(1,2)

# Make plot mechanical thickness
cont= ax1.contourf(X,Y,Z/1000, cmap=cm.batlowW_r)
ax1.set_title('Mechanical Thickness')
cbar=fig.colorbar(cont, ax=ax1)
cbar.set_label('Mechanical Thickness [km]')

# Make plot coupling
#levels = np.array([-1,0,1])
levels = np.arange(0,5.5,0.1)
cont2= ax2.contourf(X,Y,Z2, levels, cmap='Purples')
#cont2= ax2.contourf(X,Y,Z2, levels, cmap=cm.vik)

ax2.set_title('Coupling')
cbar2=fig.colorbar(cont2, ax=ax2)
cbar2.set_label('Coupling')

fig.tight_layout() # adjust plots so they don't overlap

# save figure
#fig.savefig(path_model_output + r'/' + 'MechanicalThk_Coupling.jpg', bbox_inches="tight") # jpg format
#fig.savefig(path_model_output + r'/' + 'MechanicalThk_Coupling.pdf', bbox_inches="tight") # eps format

