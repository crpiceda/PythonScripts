# -*- coding: utf-8 -*-
"""
This script plots the variation of the thermal expansion coefficient as a 
function of P and T from the Hacker and Abers (2004) worksheet

input: mineral data base from the velocity conversion
output: plot of alpha as a function of P and T for one mineral

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
import matplotlib.ticker # for cientific anotation of the colorbar

# class for scientific anotation in the colorbar
class OOMFormatter(matplotlib.ticker.ScalarFormatter):
    def __init__(self, order=0, fformat="%1.1f", offset=True, mathText=True):
        self.oom = order
        self.fformat = fformat
        matplotlib.ticker.ScalarFormatter.__init__(self,useOffset=offset,useMathText=mathText)
    def _set_order_of_magnitude(self):
        self.orderOfMagnitude = self.oom
    def _set_format(self, vmin=None, vmax=None):
        self.format = self.fformat
        if self._useMathText:
             self.format = r'$\mathdefault{%s}$' % self.format
             
        
os.chdir(r".\VelocityConversion") # file location

# import file output conversion
df_alpha = pd.read_csv(r'AlphaDB.csv', 
                           sep=';', 
                           skiprows=3, 
                           usecols=[0,1,2,4,6,11,12], 
                           names=['P', 'temp', 'alpha_cpx', 'alpha_opx', 'alpha_ol','alpha_gnt', 'alpha_spinel']) # these are the minerals I chose to plot

## create mesh for plotting
Z = df_alpha.pivot_table(index='temp', columns='P', values='alpha_cpx').T.values # change values according to the mineral

X_unique = np.sort(df_alpha.temp.unique())
Y_unique = np.sort(df_alpha.P.unique())

X, Y = np.meshgrid(X_unique, Y_unique)

# Initialize plot objects
rcParams['figure.figsize'] = 5,5  # sets plot size
fig,ax=plt.subplots(1,1)

# Define levels of contour mapchange space
levels = np.linspace(1e-5,5e-5,11)

# plot
cpf = ax.contourf(X,Y,Z, levels, cmap=cm.plasma) # Generate a color mapping of the levels we've specified for the temperature
cbar = plt.colorbar(cpf, format=OOMFormatter(-5, mathText=False))
cbar.set_label('Alpha (1/K)')
ax.set_ylim(10, 0.5)  # decreasing pressure in y axis
#plt.xticks(np.arange(3600, 4800, 200)) # plot ticks in x
#plt.xticks([X_unique.min(),100e3,X_unique.max()])
#plt.yticks([Y_unique.min(),1e5,Y_unique.min()])
ax.axhline(y=6.4, linestyle='dashed', color='black', linewidth=0.5) #draw pressure at the base of the model
ax.axvline(x=1300, linestyle='dashed', color='black', linewidth=0.5) #draw temperature at the base of the lithosphere
ax.set_xlabel('T (K)') #set labels x
ax.set_ylabel('P (GPa)') # set labels y
plt.title('Alpha cpx')
fig.savefig('Alpha_cpx_withPTlines.svg', bbox_inches="tight")