
"""
plot temperature from observations against depth
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# to export text correctly
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

directory = r"..\visualization"
os.chdir(directory) # Change directory

# read file Tmeasured
Tmeasured = pd.read_csv('Tdiff_measuredT.dat', 
                    sep=' ', 
                    usecols= [0,1,2,3], # change depending on which columns of the original file are x, y and depth respectively
                    skiprows=1, #skip comment lines 
                    names=['x', 'y', 'z', 'Tmeasured']) #depth
#create dataframe
df_Tmeasured = pd.DataFrame(Tmeasured)
print(df_Tmeasured)

# read file Tcorrected
Tcorrected = pd.read_csv('Tdiff_correctedT2.dat', 
                    sep=' ', 
                    usecols= [0,1,2,3,4], # change depending on which columns of the original file are x, y and depth respectively
                    skiprows=1, #skip comment lines 
                    names=['x', 'y', 'z', 'Tcorrected','Tmodelled']) #depth
#create dataframe
df_Tcorrected = pd.DataFrame(Tcorrected)
print(df_Tcorrected)


#convert to lists to plot
z_list = df_Tmeasured['z'].tolist() # Convert DataFrame.Column to list
Tmeasured_list = df_Tmeasured['Tmeasured'].tolist() # Convert DataFrame.Column to list
Tcorrected_list = df_Tcorrected['Tcorrected'].tolist()
Tmodelled_list = df_Tcorrected['Tmodelled'].tolist()
z_list2 = df_Tcorrected['z'].tolist() # Convert DataFrame.Column to list

rcParams['figure.figsize'] = 5, 3# sets plot size

# plot measured and corrected T°
fig, ax = plt.subplots() # to plot multiple datasets
#ax.plot(Tmeasured_list, z_list, marker='o', linestyle='None', label = 'Measured T°') #plot measured T°
ax.plot(Tcorrected_list, z_list2, marker='o', color= 'orange', linestyle='None', label = 'Corrected T°') #plot corrected T°
ax.plot(Tmodelled_list, z_list2, marker='o', color= 'black', linestyle='None', label = 'Modelled T°') #plot modelled T°
plt.gca().invert_yaxis() # invert depth axis
ax.legend() # add legend
plt.title('T° wells') #add title
plt.xlabel('T°(°C)') #add label in x axes
plt.ylabel('Depth (m)') #add label in y axes
plt.savefig('Twells.pdf') #save fig always before showing the plot
plt.savefig('Twells.svg') #save fig always before showing the plot
plt.show() #show plot