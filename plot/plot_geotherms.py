# -*- coding: utf-8 -*-
"""
plot 1D geotherms from thermal model in many locations
"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
from scipy import interpolate
import scipy.stats as st
import scipy

#function to define mean and confidence interval
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='white', alpha=0.5)

os.chdir(r"") # file location
list_files = sorted(glob.glob("Geotherm_*")) # list of files with modelled temperatures

# create data frame with info of depth of the interfaces
df_geotherms_location = pd.read_csv('Geotherms_Petrel.dat', 
                        sep=' ', 
                        usecols= [0,1,3,4,5,6], # change depending on which columns of the original file are x, y and depth respectively
                        skiprows=14, #skip comment lines 
                        names=['x', 'y', 'Z_TopBasement', 'Z_ICB', 'Z_Moho','Z_Base'])

# list with names of the locations
names_location = ['Northern Orogen', 
                  'Central Orogen', 
                  'Southern Orogen', 
                  'Northern Foreland (Sierras Pampeanas)', 
                  'Central Foreland (Cuyo basin)', 
                  'Payenia', 
                  'Southern Foreland (Neuquen basin)',
                  'EasternExtreme']

cont_names = 0 # counter of the for loop

# create emty list where the information of each geotherm will be stored
Tmod_list = []
Z_TopBasementlist =[]
Z_ICBlist = []
Z_Moholist = []
Z_list=[]
geotherm1_list=[]
geotherm2_list=[]
geotherm1_str_list=[]
geotherm2_str_list=[]

for name_file in list_files:
    # create DataFrame with modelled temperatures
    df_modT = pd.read_csv(name_file, 
                   sep=' ',
                   skiprows=3, 
                   usecols= [0,1,2,7], 
                   names=['x', 'y', 'z', 'modT'])

    df_modT = df_modT[df_modT.modT != -1.000000e+20] #delete values outside of the model
    
        
    df_merged = pd.merge(df_modT, df_geotherms_location) # add depth of interfaces as columns

    
    name = names_location[cont_names] # name of the location
    
    # convert columns of depth of the interfaces to lists and store them
    Z_TopBasement = df_merged ['Z_TopBasement'][0].tolist()
    Z_TopBasementlist.append(Z_TopBasement)
    Z_ICB = df_merged ['Z_ICB'][0].tolist()
    Z_ICBlist.append(Z_ICB)
    Z_Moho = df_merged ['Z_Moho'][0].tolist()
    Z_Moholist.append(Z_Moho)
    
    
    # convert depth values of each geotherm to list and store them
    Z_list.append(df_modT['z'].tolist())

    
    # convert temperature values of each geotherm to list and store them
    Tmod_list.append(df_modT['modT'].tolist())
    
    ## calculate the gradient between specific depth values

    #create a geotherm function to interpolate between the data
    x = np.asarray(df_modT['z'].tolist()).squeeze() #convert to numpy array (squeeze used to remove single-dimensional axes)
    y = np.asarray(df_modT['modT'].tolist()).squeeze() #convert to numpy array
    f= interpolate.interp1d(x,y, fill_value="extrapolate")
    
    # calculate the T° between the first 20 km 
    xnew=np.arange(-20000, x.max(), 1000) # depth range for the first 20 km
    ynew=f(xnew) # T° for the first 20 km
    diff_ynew=np.diff(ynew) #difference between each T° value (it is the gradient because the step when defining xnew is km)
    
    #plt.hist(diff_ynew, bins=[-30, -25, -20, -15, -10, -5,0]) #histogram of the differencesc(check that is a gaussian)
    
    #statistics of the geotherm1
    conf_int = mean_confidence_interval(diff_ynew) #confidence interval with mean, max and min
    mean_diff = conf_int[0] #mean of the gradient
    diff_diff = conf_int[0]-conf_int[1] #max value at 95% confidence
    geotherm1 = (mean_diff, diff_diff)
    geotherm1_list.append(geotherm1)
    geotherm1_str= str(-round(mean_diff,2)) + '±' + str(round(diff_diff,2)) + '°C/km'
    geotherm1_str_list.append(geotherm1_str)
    
    # calculate the T° from 40 km to 100 km (base of the model)
    xnew2=np.arange(-100000, -39000, 1000) #from 40 km to 100 km (base of the model)
    ynew2=f(xnew2) # T° for the first 20 km
    diff_ynew2=np.diff(ynew2) #difference between each T° value (it is the gradient because the step when defining xnew is km)
    
    #statistics of the geotherm2
    conf_int2 = mean_confidence_interval(diff_ynew2) #confidence interval with mean, max and min
    mean_diff2 = conf_int2[0] #mean of the gradient
    diff_diff2 = conf_int2[0]-conf_int2[1] #max value at 95% confidence
    geotherm2 = (mean_diff2, diff_diff2)
    geotherm2_list.append(geotherm2)
    geotherm2_str= str(-round(mean_diff2,2)) + '±' + str(round(diff_diff2,2)) + '°C/km' # since the average is negative, I converted to positive value
    geotherm2_str_list.append(geotherm2_str)
    
    cont_names=cont_names + 1 #increase the counter


# create subplot
fig, axs = plt.subplots(3,3, figsize=(15,16)) #set number of columns, rows and size
fig.subplots_adjust(hspace=0.3) #set horizontal spacing
fig.delaxes(axs[2,1]) #delete axes ( in case of odd number of geotherms)
fig.delaxes(axs[2,2]) #delete axes ( in case of odd number of geotherms)

cont_2 = 0 #counter for the second loop

for i, ax in enumerate(axs.flat):
    #in case the counter is bigger than the amount of files, exit the loop
    if i==len(names_location):  
        break
    else:
        y = 1280+ 0.4*(-1e-3*np.asarray(Z_list[cont_2])) #mantle adiabat (important to convert the list to nparray)
        ax.plot(Tmod_list[cont_2], Z_list[cont_2]) #plot data
        ax.plot(y, Z_list[cont_2], linestyle='dashed', label = 'Mantle adiabat') # plot mantle adiabat
        ax.set(xlabel='T (°C)', ylabel='Depth (m)') #set labels
        ax.set_title('Geotherm ' + names_location[cont_2]) #set title
        ax.axhline(y=Z_TopBasementlist[cont_2], linestyle='dashed', color='r', linewidth=0.5, label = 'Top basement') #draw Top basement
        ax.axhline(y=Z_ICBlist[cont_2], linestyle='dashed', color='blue', linewidth=0.5, label = 'Intracrustal Boundary') #draw ICB
        ax.axhline(y=Z_Moholist[cont_2], linestyle='dashed', color='green', linewidth=0.5, label = 'Moho') #draw Moho
        #ax.legend(loc='upper right') #add legend of the interfaces and mantle adiabat
        ax.set_xlim(right=1500) #set maximux value in x axis
        ax.text(700, -10000, geotherm1_str_list[cont_2], bbox=props, fontsize=10)
        ax.text(900, -60000, geotherm2_str_list[cont_2], bbox=props, fontsize=11)
        
        cont_2=cont_2 + 1 #increase the counter
    
   
      
fig.tight_layout(pad=2.0) #set vertical spacing between subplots
#fig.savefig('geotherms_withvalues.pdf', bbox_inches="tight") #save figure
#fig.savefig('geotherms_test_withvalues.svg', bbox_inches="tight")
