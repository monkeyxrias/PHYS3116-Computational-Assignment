import pandas as pd
import matplotlib.pyplot as plt # importing relevant libraries

vandenberg = pd.read_csv('data/vandenBerg_table2.csv')
krause21 = pd.read_csv('data/krause21.csv')

print(vandenberg.columns.tolist())
print(krause21.columns.tolist()) # Displays the column names in each dataset

print(vandenberg.head())
print(krause21.head()) # Displays the first five rows of each dataset

vandenberg['Age'] = pd.to_numeric(vandenberg['Age'])
vandenberg['FeH'] = pd.to_numeric(vandenberg['FeH']) # Converts the age and metallicity columns into numerical values so that they can be used to plot the data

krause21['Age'] = pd.to_numeric(krause21['Age'])
krause21['FeH'] = pd.to_numeric(krause21['FeH'])

plt.scatter(vandenberg['Age'], vandenberg['FeH'], label='Van den Berg') # Plots the dataset
plt.xlabel('Cluster Age (Gyr)')
plt.ylabel('Cluster Metallicity [Fe/H]')
plt.title("Age-Metallicity Relation of Milky Way Globular Clusters") # Labels the axes, adds the titles.
plt.show() # Displays the scatter plot

plt.scatter(krause21['Age'], krause21['FeH'], label='Krause 2021') # Same for the Krause, plots the dataset, Labels and adds titles, and then displays.
plt.xlabel('Cluster Age (Gyr)') 
plt.ylabel('Cluster Metallicity [Fe/H]')
plt.title("Age-Metallicity Relation of Milky Way Globular Clusters")
plt.show()