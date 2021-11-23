# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:15:50 2021

@author: piceda

This script plots shortening rates vs. time
"""


import matplotlib.pyplot as plt
import os #para importar información de otros directorios
import pandas as pd
import matplotlib.cm as cm # matplotlib's color map library
from matplotlib import rcParams
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from brewer2mpl import qualitative
import numpy as np
#bmap = qualitative.Dark2[7]

# to export text correctly
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

os.chdir(r"..\ShorteningRates") # file location

## open file

data = pd.read_csv('ShorteningRates_LG_27S.txt',
                    sep=' ')
data2 = pd.read_csv('ShorteningRates_LG_35S.txt',
                    sep=' ')

#data=data.replace(0,np.NaN)

#data2=data2.replace(0,np.NaN)

column_list=['CC', 'CF', 'Prc', 'SP']
data['total27']=data[column_list].sum(axis=1)

# plot
rcParams['figure.figsize'] = 7, 5 # sets plot size
fig,ax1 =plt.subplots(1,1)
ax1.step(data['time'],data['CC'], color= 'c', label='Coastal Cordillera (27.5°S)')
ax1.step(data['time'],data['CF'], color= 'lightcoral' , label='Frontal Cordillera (27.5°S)')
ax1.step(data['time'],data['Prc'], color = 'purple', label='Precordillera (27.5°S)')
ax1.step(data['time'],data['SP'], color= 'orangered', label='Sierras Pampeanas (27.5°S)')
ax1.step(data2['time'],data2['CP'], color= 'blue', label='Principal Cordillera (35°S)')
ax1.scatter(data['time'],data['CC'], color= 'c')
ax1.scatter(data['time'],data['CF'], color= 'lightcoral')
ax1.scatter(data['time'],data['Prc'], color = 'purple')
ax1.scatter(data['time'],data['SP'], color= 'orangered')
ax1.scatter(data2['time'],data2['CP'], color= 'blue')

ax1.step(data['time'],data['total27'], color= 'black', linestyle='--', label='Total 27°S')
ax1.scatter(data['time'],data['total27'], color= 'black')

ax1.set_ylim(0,14)
ax1.set_ylabel('Shortening rate [mm/yr]')
ax1.set_xlabel('time [Ma]')
ax1.legend(loc='upper right')
ax1.set_title('Shortening rates')
ax1.invert_xaxis()

# Make a plot with major ticks that are multiples of 20 and minor ticks that
# are multiples of 5.  Label major ticks with '.0f' formatting but don't label
# minor ticks.  The string is used directly, the `StrMethodFormatter` is
# created automatically.
ax1.xaxis.set_major_locator(MultipleLocator(5))
ax1.xaxis.set_major_formatter('{x:.0f}')

ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_major_formatter('{x:.0f}')

# For the minor ticks, use no labels; default NullFormatter.
ax1.xaxis.set_minor_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(MultipleLocator(0.5))

fig.savefig('shorteningrates_LG.pdf')

