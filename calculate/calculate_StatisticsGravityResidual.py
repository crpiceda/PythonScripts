# -*- coding: utf-8 -*-
"""
calculate statistics from gravity residual
"""
import pandas as pd
#import numpy as np
import os


os.chdir("..\GravityResidual\Original_GR") # file location

## function to calculate RMS
def qmean(num):
    from math import sqrt
    return sqrt(sum(n*n for n in num)/len(num))

df_statistics = pd.DataFrame(columns = ['meanGR', 'SDGR', 'maxGR', 'minGR', 'RMS']) # df of statistics

for filename in os.listdir('Z:\piceda\PhD_RodriguezPiceda\Figures\Paper1\SensitivityAnalysis\Model13\GravityResidual\Original_GR'):
    df_res = pd.read_csv(filename, sep=' ', usecols= [0,1,5], names=['x', 'y', 'GravityResidual']) # read with original file
    
    # calculate statistics
    mean_GR  = df_res.GravityResidual.mean()
    SD_GR = df_res.GravityResidual.std()
    max_GR = df_res.GravityResidual.max()
    min_GR = df_res.GravityResidual.min()
    RMS_GR= qmean(df_res.GravityResidual)
    statistics = [mean_GR, SD_GR, max_GR, min_GR, RMS_GR]
    
    df_statistics_file = pd.DataFrame([statistics], index = [filename], columns = ['meanGR', 'SDGR', 'maxGR', 'minGR', 'RMS']) # save statistics in a new df
    df_statistics = pd.concat([df_statistics_file, df_statistics]) #append statistics to df

df_statistics.to_csv(r"statistics_gravityresidual.dat", sep=' ') # export