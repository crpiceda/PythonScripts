# -*- coding: utf-8 -*-
"""
Calculate shear stress from normal stress in brittle and ductile domains
"""
import os
import fnmatch
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import math

#%% functions

# function to calculate shear stress in brittle domain

def shear_stress_brittle(diff_sigma, byerlee_friction):
    
    phi= 0
    
    if byerlee_friction == 2:
        phi = 0.58
    if byerlee_friction == 0.35:
        phi = 0.15
    if byerlee_friction == 2.45:
        phi = 0.66
    if byerlee_friction == 0.1:
        phi = 0.05
    if byerlee_friction == 0.03:
        phi = 0.015
    
    tau_brittle = 1/2*diff_sigma*math.sin(phi+1/2)
    
    return tau_brittle

# function to calculate shear stress in brittle domain
def shear_stress_ductile(strain_rate, eta_effective):
    tau_ductile = eta_effective*strain_rate*1e-6
    
    return tau_ductile # in MPa

#%%

## set directory
directory = r''
directory_input = directory + '\input'
directory_output = directory + '\output'

#%%

os.chdir(directory_input)

# extract Byerlee friction and strain rate form rheology file
for file in os.listdir('.'):
    # work with rheology file
    if fnmatch.fnmatch(file, '*rheology.ini*'):
        rheology = pd.read_csv(file, sep = '\t')
        byerlee_friction_topOC = float(rheology['friction'][79]) # extract byerlee friction
        strain_rate_topOC = float(rheology['strain_rate_value'][79]) # extract strain rate

os.chdir(directory_output)

for file in os.listdir('.'):
    # work with info3d file
    if fnmatch.fnmatch(file, '*info3D.csv*'):
        points = pd.read_csv(file)
        points_topOC = points[points['layer_name[]']=='08_OC_Basalt'] # extract info top oceanic crust
        
        points_topOC['eta_effective[Pa*s]'] = 10**(points_topOC['log_eta_effective[Pa*s]']) # create column with eta_effective
        
        tau_brittle = points_topOC['dsigma[MPa]'].apply(lambda x: shear_stress_brittle(x, byerlee_friction_topOC))
        tau_ductile = points_topOC['eta_effective[Pa*s]'].apply(lambda x: shear_stress_ductile(strain_rate_topOC, x))
        
        is_brittle = (points_topOC['bdt[]']==0)
        is_ductile = (points_topOC['bdt[]']==1)
                                   
        points_topOC.loc[is_brittle, 'shear_stress[Mpa]'] = tau_brittle
        points_topOC.loc[is_ductile, 'shear_stress[Mpa]'] = tau_ductile
        
        y_list_all = [6700, 6650, 6600, 6550, 6500, 6450, 6400, 6350, 6300, 6250, 6200, 6150, 6100, 6050, 6000, 5950, 5900, 5850, 5800, 5750] # latitudes flat slab
        
        # initialize plots
        fig, (ax1,ax2) = plt.subplots(1,2, figsize=(9,11))
        
        #fig=plt.figure(figsize=(9,11))
        
        for y_cs in y_list_all:
            points_cs = points_topOC[points_topOC['y[km]']==y_cs]
            
            # convert depth dsgigma  and temperatures values to lists
            z_list = (points_cs['z[km]']*1000).tolist()
            
            dsigma_list = points_cs['dsigma[MPa]'].tolist()
            
            tau_list = points_cs['shear_stress[Mpa]'].tolist()
            
            ax1.plot(tau_list, z_list, label = y_cs) #plot data
            ax1.set_xlabel('tau '+ ' [Mpa]')
            ax1.set_ylabel('Depth [masl]')
            ax1.set_ylim(-120000,0) # set limits for the y axis
            ax1.xaxis.tick_top() # ticks in the top
            ax1.xaxis.set_label_position('top') # title in the top
            ax1.legend(loc="lower right", title="Easting (m)") # set legend
            ax1.set_title('YSE ' + 'subduction interface' ) #set title
            ax1.grid(zorder=0,linewidth=0.5) # plot grid
            
            ax2.plot(dsigma_list, z_list, label = y_cs) #plot data
            ax2.set_xlabel('Differential ' r'$\sigma$'+ ' [Mpa]')
            ax2.set_ylabel('Depth [masl]')
            ax2.set_ylim(-120000,0) # set limits for the y axis
            ax2.xaxis.tick_top() # ticks in the top
            ax2.xaxis.set_label_position('top') # title in the top
            ax2.legend(loc="lower right", title="Easting (m)") # set legend
            ax2.set_title('YSE ' + 'subduction interface' ) #set title
            ax2.grid(zorder=0,linewidth=0.5) # plot grid
            
            
