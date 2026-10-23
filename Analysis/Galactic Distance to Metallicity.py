import pandas as pd
import matplotlib.pyplot as plt # importing relevant libraries

vandenberg = pd.read_csv('data/vandenBerg_table2.csv')
Harris1 = pd.read_csv('data/HarrisPartI.csv')
Harris2 = pd.read_csv('data/HarrisPartII.csv')

print(vandenberg.columns.tolist())
print(Harris1.columns.tolist()) 
print(Harris2.columns.tolist())

print(vandenberg.head())
print(Harris1.head())
print(Harris2.head())

vandenberg['R_G'] = pd.to_numeric(vandenberg['R_G'])
Harris1['R_gc'] = pd.to_numeric(Harris1['R_gc'])

vandenberg['FeH'] = pd.to_numeric(vandenberg['FeH'])
Harris2['[Fe/H]'] = pd.to_numeric(Harris2['[Fe/H]'], errors='coerce') # Was having troubles plotting, had to add errors='coerce' due to string with parseability error

plt.scatter(vandenberg['R_G'], vandenberg['FeH'], label='Van den Berg') # Plots the dataset

plt.xlabel('Galactocentric Distance (kpc)')
plt.ylabel('Cluster Metallicity [Fe/H]')
plt.title("Galactocentric Distance-Metallicity Relation of Milky Way Globular Clusters Van Den Berg Dataset")
plt.show()

plt.figure()
plt.scatter(Harris1['R_gc'], Harris2['[Fe/H]'], label='Harris 1996') # Since the clusters are in the same rows in each dataset, we can pair them by row.
plt.xlabel('Galactocentric Distance (kpc)')
plt.ylabel('Cluster Metallicity [Fe/H]')
plt.title("Galactocentric Distance-Metallicity Relation of Milky Way Globular Clusters Harris Dataset")
plt.show()