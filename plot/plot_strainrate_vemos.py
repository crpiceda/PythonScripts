# -*- coding: utf-8 -*-
"""
plot histogram and calculate statistics from second invariant of stran rate (Drewes and Sanchez 017)
"""


# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import PercentFormatter
from matplotlib import rcParams
import matplotlib.ticker as ticker

# to export text correctly
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42


os.chdir('..\VMS2017\StrainRates')

points = pd.read_csv(r'strainrate_secondinvariant_UTM19.dat', sep=' ', skiprows=1, usecols=[0,1,2], names=['lat','long','eii'])

## histogram of second invariant of strain rate

# rescale second invariant of the strain rate to 1/s
points['eii/1s'] = points['eii']*3.154*10**(-16)

points.to_csv('strainrate_secondinvariant_1s_UTM19.txt', index = False, sep = ' ')

    
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

ax1.hist(eii_list, bins=25, range=[0, 2.2e-15], weights=np.ones(len(eii_list)) / len(eii_list), linewidth=1)
#ax1.gca().yaxis.set_major_formatter(PercentFormatter(1)) # to use percentage in y axis


# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='white', alpha=0.5)

# place a text box in upper left in axes coords
ax1.text(0.60, 0.85, textstr, transform=ax1.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

ax1.set_title('strain second invariant  VEMOS 2017')
ax1.set_xlabel('Strain second invariant [e-14 1/s]')
ax1.set_ylabel('Frequency %')

# rescale axis
scale_x = 1e-15
ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_x))
ax1.xaxis.set_major_formatter(ticks_x)

scale_y = 100
ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x*scale_y))
ax1.yaxis.set_major_formatter(ticks_y)

fig.tight_layout()
fig.savefig(r'Z:\piceda\PhD_RodriguezPiceda\Figures\Paper3\StrainRate\strainratevemos.pdf')