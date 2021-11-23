# -*- coding: utf-8 -*-
"""
plot yield strength envelope along with lithospheric discontinuities
"""
import matplotlib.pyplot as plt
import numpy as np
import os 
import pandas as pd
import glob
import re # to handle regular expressions
import matplotlib as mpl
import fnmatch

# export text as text
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

# change to where the yse are stored
os.chdir(r'..\Models_LCrheology')
#file= 'SCA_model_20_0000002_constant.dat'
list_files = sorted(glob.glob("*")) # list of files with yse

# initialize plots
fig, ax = plt.subplots(1,1, figsize=(3,5))
ax_temp=ax.twiny() # twin axes to plot ticks of temperature

for file in list_files:
# read file
    if fnmatch.fnmatch(file, '*SCA*'):
        yse = pd.read_csv(file, 
                          sep=' ', 
                          skiprows=1, usecols=[0,1,2,3,4,5,6,7,8,9,10], 
                          names=['z', 'temp', 'dsigma', 'dsigmabrittle','dsigmaductile',
                                  'dsigmapeierls', 'etadiffusion', 'etadislocation',
                                  'etaeffective', 'long', 'lat'])
        
        #file = 'SCA_model_1_0000001.dat'
        file_name = re.sub('\.dat$', '', file.split('_')[-1]) # extract name file with friction
        
        # extract the coordinates
        coord_x = yse['long'][1]
        coord_y = yse ['lat'][1]
        
        # filter depths > 100 km
        yse = yse[yse['z']>-100]
        
        # convert depth and dsgigma values to lists
        z_list = yse['z'].tolist()
        
        dsigma_array =np.array(yse['dsigma'])
        
        # interfaces
        # central orogen
        # z_topbasement=2899.61*1e-3
        # z_icb= -32500.00*1e-3
        # z_moho = -49705.01*1e-3
        
        # northern foreland (WSP)
        z_topbasement=168.80*1e-3
        z_icb= -17000.00*1e-3
        z_moho = -51481.18*1e-3
        
        # temperatures
        temp_array=np.array(yse['temp'])
        
        ##plot
        
        ax_temp.plot(temp_array, z_list, color='red', linewidth=0.5) #plot data
        ax.plot(dsigma_array, z_list, label=file_name) #plot data
        ax.set(xlabel='Differential ' r'$\sigma$'+ ' (Mpa)', ylabel='Depth [kmasl]') #set labels
        ax_temp.set_xlabel('Temperature [°C]')
        ax.axhline(y=z_topbasement, linestyle='dashed', color='grey', linewidth=1)
        ax.axhline(y=z_icb, linestyle='dashed', color='grey', linewidth=1)
        ax.axhline(y=z_moho, linestyle='dashed', color='grey', linewidth=1)
        ax.set_xlim(2000,0) # trick to flip the axes
        ax_temp.set_xlim(900,0) # trick to flip the axes
        
        ax.xaxis.tick_top() # ticks in the top
        ax.xaxis.set_label_position('top') # title in the top
        ax_temp.xaxis.tick_bottom() # ticks in the bottom
        ax_temp.xaxis.set_label_position('bottom') # title in the bottom
        
        ax.set_title('YSE\n' + ' (x_coord =' + str(coord_x) + 'km' + ' -  y_coord =' + str(coord_y) + 'km)' ) #set title
        ax.grid(True) # plot grid
        ax.legend()

fig.savefig('YSE_strainrate.eps', bbox_inches="tight") #save figure
fig.savefig('YSE_strainrate.png', bbox_inches="tight") #save figure