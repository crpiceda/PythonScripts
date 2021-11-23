# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:03:37 2021

@author: piceda

This script classifies the slab earthquakes into interplate and intraslab taking into account the strike and the dip of the nodal planes

"""
## import libraries
import os
import pandas as pd
import numpy as np


## directory
os.chdir(r'..\GMT\SCA_76W64W40S27S_1976-2021')

# open file of slab focal mechanisms
# these include interplate and intraplate
fm_slab = pd.read_csv('SlabMechanisms_GMT_76W64W40S27S_UTM19.txt',
                    sep=' ', 
                    skiprows=1, 
                    usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13], 
                    names=['x', 'y', 'z', 'str1', 'dip1', 'rake1', 'str2', 'dip2', 'rake2', 'sc', 'iexp', 'name', 'slab_dip', 'slab_dipazimuth'])


# open file of candidates to interplate focal mechanisms
# these are the events only filtered by depth
fm_can = pd.read_csv('InterplateCandidatesMechanisms_GMT_76W64W40S27S_UTM19.txt',
                    sep=' ', 
                    skiprows=1, 
                    usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13], 
                    names=['x', 'y', 'z', 'str1', 'dip1', 'rake1', 'str2', 'dip2', 'rake2', 'sc', 'iexp', 'name', 'slab_dip', 'slab_dipazimuth'])

# calculate slab strike for interplate candidates
fm_can['slab_strike'] = fm_can['slab_dipazimuth'] + 90
fm_can.loc[fm_can['slab_strike'] >=360, 'slab_strike'] = fm_can['slab_strike'] - 360 # for the cases the slab strike surpasses 360°

# calculate slab strike for intraslab
fm_slab['slab_strike'] = fm_slab['slab_dipazimuth'] + 90
fm_slab.loc[fm_slab['slab_strike'] >=360, 'slab_strike'] = fm_slab['slab_strike'] - 360 # for the cases the slab strike surpasses 360°

# calculate acceptable bounds of slab strike
lim_str = 15
fm_can['slab_strike_max']= fm_can['slab_strike'] + lim_str
fm_can.loc[fm_can['slab_strike_max'] >=360, 'slab_strike_max'] = fm_can['slab_strike_max'] - 360
fm_can['slab_strike_min']= fm_can['slab_strike'] - lim_str
fm_can.loc[fm_can['slab_strike_min'] <0, 'slab_strike_min'] = fm_can['slab_strike_min'] + 360

## define acceptable bounds for the dip angle of the fault plane
# we consider that the FM has the same dip angle than the subduction interface with +-10° acceptable bounds
lim_dip = 35

# calculate acceptable bounds of dip angle of the plane
fm_can['dip_max']= fm_can['slab_dip'] + lim_dip


## filter all interplate events
# first approach: this filter considers the strike and the dip of the top surface of the slab as condition
#fm_interplate = fm_can[((fm_can['str1']>=fm_can['slab_strike_min']) & (fm_can['str1']<=fm_can['slab_strike_max']) & (fm_can['dip1']>=fm_can['slab_dip']-lim_dip) & (fm_can['dip1']<=fm_can['slab_dip']+lim_dip)) | ((fm_can['str2']>=fm_can['slab_strike_min']) & (fm_can['str2']<=fm_can['slab_strike_max']) & (fm_can['dip2']>=fm_can['slab_dip']-lim_dip) & (fm_can['dip2']<=fm_can['slab_dip']+lim_dip))]

## filter all interplate events
# second approach: this filter considers the strike of the top surface of the slab and dip angle < 35 as condition
#fm_interplate = fm_can[((fm_can['str1']>=fm_can['slab_strike_min']) & (fm_can['str1']<=fm_can['slab_strike_max']) & (fm_can['dip1']<=35)) | ((fm_can['str2']>=fm_can['slab_strike_min']) & (fm_can['str2']<=fm_can['slab_strike_max']) & (fm_can['dip2']<=35))]

## filter all interplate events
# third approach: this filter considers the strike of the top surface of the slab and dip angle < 35 from the top of the slab as condition
fm_interplate = fm_can[((fm_can['str1']>=fm_can['slab_strike_min']) & (fm_can['str1']<=fm_can['slab_strike_max']) & (fm_can['dip1']<=fm_can['dip_max'])) | ((fm_can['str2']>=fm_can['slab_strike_min']) & (fm_can['str2']<=fm_can['slab_strike_max']) & (fm_can['dip2']<=fm_can['dip_max']))]


## filter intraslab events using the name of events
i_intraslab = ~fm_slab['name'].isin(fm_interplate['name']) # series with boolean (all lines that are interplate are false)
fm_intraslab = fm_slab[i_intraslab] # filter intraslab events

# save files
fm_interplate.to_csv('InterplateMechanisms_GMT_76W64W40S27S_UTM19.txt', columns=['x', 'y', 'z', 'str1', 'dip1', 'rake1', 'str2', 'dip2', 'rake2', 'sc', 'iexp', 'name', 'slab_dip', 'slab_dipazimuth', 'slab_strike'], index=None, sep= ' ')
fm_intraslab.to_csv('IntraslabMechanisms_GMT_76W64W40S27S_UTM19.txt', columns=['x', 'y', 'z', 'str1', 'dip1', 'rake1', 'str2', 'dip2', 'rake2', 'sc', 'iexp', 'name', 'slab_dip', 'slab_dipazimuth', 'slab_strike'], index=None, sep= ' ')


