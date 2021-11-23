'''
Convert Vp to Vs using a defined Vp/Vs ratio

input file with the following heading columns:
x
y
depth
Vp
'''
import pandas as pd
import os
os.chdir("") # file location

df = pd.read_csv('Vs-Ward_SCA_UTM19.dat', sep=' ') #velocities

# optional: if the depths are in km, set in m
df['depth'] = df['depth'].multiply(1000)

# convert Vs to Vp taking into account the Vp/Vs ratio. In my case, it's 1.75
df['Vp'] = df['Vs'].multiply(1.75)

# optional: replace all of the non-defined values by -9999. The precondition is that all Vs in these cases must be negative
def NaN(x):
    if x < 0:
        x = -9999
    return x

df['Vp'] = df['Vp'].apply(NaN)

# save in csv format
df.to_csv(r"Vp-Ward_SCA_UTM19.dat", index = False)