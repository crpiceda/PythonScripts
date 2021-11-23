# -*- coding: utf-8 -*-
"""
plot variation of thermal expansitivty with temperature for different minerals
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

os.chdir(r"..\VelocityConversion") # file location

temp = np.linspace(673,1573,10)

alpha_ol = 2.01e-5 + 1.39e-8*temp + 0.001627/temp + (-0.338)/(temp*temp)

alpha_opx = 4.4135e-5 + 6.61e-9*temp + (-0.00575625)/temp + (-0.08385)/(temp*temp)

alpha_cpx = 0.000053 + 0.00000000592*temp + (-0.0122)/temp + (0.672)/(temp*temp)

alpha_gnt = 9.91e-6 + 1.17e-8*temp + 1.06e-2/temp + (-2.5)/(temp*temp)

alpha_spinel = 0.00006969 - 1.08e-9*temp - 0.030799/temp + 5.0395/(temp*temp)


# Initialize plot objects
rcParams['figure.figsize'] = 4,3  # sets plot size
fig,ax=plt.subplots(1,1)

ax.plot(temp, alpha_ol, linestyle='-', color='black', linewidth=1, marker='o', ms=5, markeredgewidth=1, markerfacecolor="black", label='olivine') # plot Vs at chosen location
ax.plot(temp, alpha_opx, linestyle='-', color='purple', linewidth=1, marker='^', ms=5, markeredgewidth=1, markerfacecolor="purple", label='orthopiroxene') # plot Vs at chosen location
ax.plot(temp, alpha_cpx, linestyle='-', color='lightcoral', linewidth=1, marker='s', ms=5, markeredgewidth=1, markerfacecolor="lightcoral", label = "clinopiroxene") # plot Vs at chosen location
ax.plot(temp, alpha_gnt, linestyle='-', color='darkcyan', linewidth=1, marker='D', ms=5, markeredgewidth=1, markerfacecolor="darkcyan", label = "garnet") # plot Vs at chosen location
ax.plot(temp, alpha_spinel, linestyle='-', color='orange', linewidth=1, marker='x', ms=5, markeredgewidth=1, markerfacecolor="orange", label = "spinel") # plot Vs at chosen location
ax.legend(loc='upper left', fontsize = 'xx-small') # plot legend

plt.xticks(np.arange(600, 1700, 200)) # plot ticks in x
ax.set_xlabel('Temperature (K)') #set labels x
ax.set_ylabel('α (K-1)') # set labels y
plt.title('AlphaT')

#plt.savefig('Plot_AlphaT.svg', bbox_inches='tight', format='svg', dpi=200)
