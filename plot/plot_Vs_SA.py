# -*- coding: utf-8 -*-
"""
plot Vs depth slices of seismic tomography
"""
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable
import pandas as pd
import glob as gl
from scipy.interpolate import griddata
from matplotlib.patches import Polygon
import matplotlib.cm as cm 
from matplotlib import rcParams

os.chdir(r"..\Tomography_Feng\VsConversion_Goes\SouthAmerica") # file location
df_Velocity = pd.read_csv(r'Rho_feng_AlphaConst_xenolithCPB_SouthAmerica.dat', sep=' ', skiprows=20, usecols=[0,1,2,3,4,5], names=['long', 'lat', 'depth', 'Vs', 'temp', 'rho']) # import file

valuesdepth = df_Velocity.depth.unique()#array with all depth values

## create ascii files for each depth and plot them
for z in valuesdepth:
    df_Velocity_z = df_Velocity.loc[df_Velocity['depth'] == z]
    #print(df_Velocity_z)
    
    str_z = str(z)
    #df_Velocity_z.to_csv(r"Vs_Assumpcao_" + str_z, index = False, sep = ' ')
    
    ## these steps are necessary to convert the data to a format readable by matplotlib
    Z = df_Velocity_z.pivot_table(index='long', columns='lat', values='Vs').T.values
    
    X_unique = np.sort(df_Velocity_z.long.unique())
    Y_unique = np.sort(df_Velocity_z.lat.unique())
    
    X, Y = np.meshgrid(X_unique, Y_unique)
    
    
    # Initialize plot objects
    #rcParams['figure.figsize'] = 5, 5 # sets plot size
    fig,ax=plt.subplots(1,1)
    
    # Define levels of contour mapchange space
    levels = np.linspace(3600,4900,14)
    
    # Generate a color mapping of the levels we've specified
    cpf = ax.contourf(X,Y,Z, levels, cmap=cm.viridis_r)
    
    # Set all level lines to black
    #line_colors = ['black' for l in cpf.levels]
    
    # Make plot and customize axes
    #ax.clabel(cpf, fontsize=10)
    cbar = plt.colorbar(cpf)
    cbar.set_label('Vs (m/s)')
    plt.xticks(np.arange(-74, -65, 1)) # plot ticks in x
    ax.set_xlim(-74,-65)
    ax.set_ylim(-40,-27)
    #plt.xticks([X_unique.min(),100e3,X_unique.max()])
    #plt.yticks([Y_unique.min(),1e5,Y_unique.min()])
    ax.set_xlabel('long') #set labels x
    ax.set_ylabel('lat') # set labels y
    plt.title('Vs Assumpcao ' + str(z) + ' m')
    
    #plt.savefig('VsFeng' + str_z + 'm' + '.png', bbox_inches='tight', format='png', dpi=200) # uncomment to save vector/high-res version
    #plt.savefig('VsFeng' + str_z + 'm' + '.svg', bbox_inches='tight', format='svg', dpi=200) # uncomment to save vector/high-res version