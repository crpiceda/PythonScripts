# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:36:34 2020

@author: piceda

This script calculates the difference between the observed heat flow and the modelled one. It also plots the results
"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import PercentFormatter
from matplotlib import rcParams

directory = r"..\ModelMerged_test54_55"
os.chdir(directory) # file location
list_directory = directory.split('\\') #sepate the directory name to obtain the name of the model

name_model = list_directory[-1] # get the name of the model


# Read file measured heat flow
measHF = pd.read_csv('HF_Lucazeau_SCA_UTM19_petrel.txt', 
                    sep=' ', 
                    skiprows=1,
                    usecols=[0,1,2],
                    names=['x', 'y','measHF'])

# Read file modelled temperatures
modHF = pd.read_csv('Heatflow_Wells.txt', 
                   sep=' ',
                   skiprows=1, 
                   usecols= [0,1,2], 
                   names=['x', 'y', 'modHF'])
#print(modHF)

df_measHF = pd.DataFrame(measHF)
df_modHF = pd.DataFrame(modHF)

# Merge tables w/ measured and modelled heat flow
df_merged = pd.merge(df_measHF, df_modHF)

# Calculate difference between measured and modelled heat flow
df_merged['HFdiff']= df_merged['measHF']-df_merged['modHF']

# Create histogram HFdiff

Hdiff_list = df_merged['HFdiff'].tolist() # Convert DataFrame.Column to list

rcParams['figure.figsize'] = 5, 4 # sets plot size
plt.hist(Hdiff_list,
         bins = 15,
         weights=np.ones(len(Hdiff_list)) / len(Hdiff_list),
         edgecolor='black',
         linewidth = 1.2)

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.title('HF diff ' + name_model)
plt.xlabel('HF [w/m2] ')
plt.ylabel('Frequency')

plt.savefig('HFdiff_Golem.pdf')
plt.show()

# save DataFrame as csv
df_merged.to_csv(r"HFdiff_Golem.dat", sep=' ', index = None)



