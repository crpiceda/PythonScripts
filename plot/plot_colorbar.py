# -*- coding: utf-8 -*-
"""

@author: piceda

script to plot a stand-alone colorbar
"""


import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm # matplotlib's color map library
from cmcrameri import cm as cm_cram
import numpy as np
import os
from matplotlib import rcParams

# to export text correctly
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42


path=r'..\focalmechanisms_intraplate-interplate' # data path
os.chdir(path) # change working directory

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)

#cmap_orig=cm.get_cmap('YlGnBu',256) #color map
#cmap_orig=cm_cram.davos_r
cmap_orig=cm.get_cmap('BuPu_r',200)

bounds=[int(x) for x in np.linspace(0,200,200)] # define list with color interval

norm = mpl.colors.BoundaryNorm(bounds, cmap_orig.N) # define normalization

# plot color bar
cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap_orig,
                                norm=norm,
                                orientation='horizontal')

# plot colorbar with defined ticking
cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap_orig,
                                norm=norm,
                                ticks=[0,20,40,60,80,100,120,140,160,180,200],
                                orientation='horizontal')

cb1.set_label(' depth [km bmsl]')
fig.savefig('colorbar_depthfocalmechanism.pdf')
