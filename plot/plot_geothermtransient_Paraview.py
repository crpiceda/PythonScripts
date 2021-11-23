
"""
script to plot geotherms over time from paraview
geotherm file must have the form : time temp x y z

"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42


## directory
path =r'..\Model_50km-DeeperMoho_5km_hc1050\extract' 
os.chdir(path)

geotherm_list= [f for f in os.listdir(path) if os.path.isfile(f) & f.endswith('.csv')] # list of only files
geotherm_list_sorted = sorted(geotherm_list)[2::3] # list of geotherms
geotherm_list_sorted.append(sorted(geotherm_list)[-1])


# Initialize plot objects
rcParams['figure.figsize'] = 7,5  # sets plot size
fig,ax=plt.subplots(1,1)

for file in geotherm_list_sorted:
    geotherm = pd.read_csv(file, names= ['time','temp','x','y','z'], skiprows=1)
    
    time_ma = geotherm.time.values[0]/1e6 # time in Ma
    x_coord= geotherm.x[0]
    y_coord= geotherm.y[0] 
    
    
    temp=geotherm.temp.values
    z=geotherm.z.values
    
    ax.plot(temp,z/1000, label=str(time_ma))

    
ax.set_xlabel('Temperature[°C]')
ax.set_ylabel('Depth [km amsl]')
ax.set_title('hc=1050' + '\n' + 'easting:' + str(x_coord) + ' - northing:' + str(y_coord))
ax.legend(title='Time [Ma]', bbox_to_anchor=(1, 1.0), loc='upper left')
fig.tight_layout()
plt.savefig('geotherms_transient_hc1050.png')
plt.savefig('geotherm_transient_hc1050.eps')