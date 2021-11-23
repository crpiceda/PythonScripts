'''
Calculates the density from P-Waves velocities using the experimentals laws of
Ludwig et al., 1970 and Christensen and Mooney, 1995.
Check Hirsch et al., 2009 for further references

input file should be a plain text file with the folowing columns:
x
y
Vp (should be in km/s)
density
'''
# Import libraries
import pandas as pd
import os

# file location
os.chdir("")

# Opens file and defines DataFrame
# Define the separator depending on the file
df = pd.read_csv('Vp-Ward_SCA_UTM19.dat', sep=' ') #velocities

# Calculation of density from Vp
def density(x):
    if x <= 0:
        density = -9999
        
    if x > 0 and x <= 1.5:
        density = 1.03

    elif x > 1.5 and x <= 3:
        density = (x-1.32)**0.32 + 1.05

    elif x > 3 and x <= 4.5:
        density = (x+9.8)/5.75

    elif x > 4.5  and x <= 6.2:
        density = (x+9.7)/5.71

    elif x > 6.2 and x <= 8.1:
        density = 0.9473 + 0.2966*x

    elif x > 8.1:
        density = 5.141 - 14.539/x

    return density

# Calculates the density for each row and writes the result in the density column
df['density'] = df['Vp'].apply(density)

# optional: replace all of the non-defined values by -9999. The precondition is that all Vs in these cases must be negative
def NaN(x):
    if x < 0:
        x = -9999
    return x

df['density'] = df['density'].apply(NaN)

# save the output file
df.to_csv(r"rho-Ward-CM_SCA_UTM19.dat", sep = ' ', index = False)
	