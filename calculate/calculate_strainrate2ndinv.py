# -*- coding: utf-8 -*-
"""
This script takes the global strain rate model and calculates the strain rate second invariant
Then it outputs:
    - ascii file with the calculated second invariant
    - histogram of second invariant with units in 1/s (the figure is not saved)
"""


# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import PercentFormatter
from matplotlib import rcParams
import matplotlib.ticker as ticker

os.chdir('Z:\piceda\PhD_RodriguezPiceda\GNSSData\GlobalStrainRateMap_v2')

points = pd.read_csv(r'GSRM_average_strain_forpython.txt', sep=' ', skiprows=1, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13], names=['lat','long','exx','eyy','exy','sd_exx','sd_eyy','sd_exy','cc_xxyy','cc_xxxy', 'cc_yyxy', 'e1', 'e2', 'azi_e1'])

columnsTitles= ['long','lat','eii','exx','eyy','exy','sd_exx','sd_eyy','sd_exy','cc_xxyy','cc_xxxy', 'cc_yyxy', 'e1', 'e2', 'azi_e1'] # new order of columns 
points=points.reindex(columns=columnsTitles) # change order of columns

# function to calculate second invariant of the strain rate
def calc_eii(exx,eyy,exy):
    eii = (exx**2 + eyy**2 + exy**2)**(1/2)
    return eii

# calculate second invariant of strain rate for each row of the data frame
points['eii'] = points.apply(lambda x: calc_eii(x['exx'], x['eyy'], x['exy']), axis = 1)


points.to_csv('GSRM_average_strain_with_eii.txt', index = False, sep = ' ')    


## histogram of second invariant of strain rate

# rescale second invariant of the strain rate to 1/s
points['eii/1s'] = points['eii']*3.154*10**(-16)

# convert column to list
eii_list = points['eii/1s'].to_list()

# calculate statistics
mean_eii = "{0:.3g}".format(points['eii/1s'].mean())
median_eii = "{0:.3g}".format(points['eii/1s'].median())
sigma_eii = "{0:.3g}".format(points['eii/1s'].std())

# textstr = '\n'.join((
#     r'$\mu=%.2f$' % (mean_eii, ),
#     r'$\mathrm{median}=%.2f$' % (median_eii, ),
#     r'$\sigma=%.2f$' % (sigma_eii, )))

textstr = r'$\mu=%.2f$' + str(mean_eii) + ' 1/s' + '\n' + r'$\mathrm{median}=%.2f$' + str(median_eii) + ' 1/s' + '\n' + r'$\sigma=%.2f$' + str(sigma_eii) + ' 1/s' 


# Initialize plot object size
rcParams['figure.figsize'] = 6, 3 # sets plot size

# Plot histogram
fig, ax1 = plt.subplots()

ax1.hist(eii_list, bins=25, range=[0, 1.4e-13], weights=np.ones(len(eii_list)) / len(eii_list), linewidth=1)
#ax1.gca().yaxis.set_major_formatter(PercentFormatter(1)) # to use percentage in y axis


# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='white', alpha=0.5)

# place a text box in upper left in axes coords
ax1.text(0.60, 0.85, textstr, transform=ax1.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

ax1.set_title('strain second invariant  Global strain rate map')
ax1.set_xlabel('Strain second invariant [e-14 1/s]')
ax1.set_ylabel('Frequency %')

# rescale axis
scale_x = 1e-14
ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_x))
ax1.xaxis.set_major_formatter(ticks_x)

scale_y = 100
ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x*scale_y))
ax1.yaxis.set_major_formatter(ticks_y)

