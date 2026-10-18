import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

harris_p2 = pd.read_csv('data/HarrisPartII.csv')
harris_p3 = pd.read_csv('data/HarrisPartIII.csv')

print(harris_p2.head())  #displays the first 5 rows of the dataframe by default

print(harris_p2.shape)   #returns the total number of rows and columns

print(harris_p2.columns) #returns the names of the columns

harris_p2['[Fe/H]'] = pd.to_numeric(harris_p2['[Fe/H]'], errors='coerce')  #pandas originally interpreted the metallicity measurements as strings, this converts them into numerical values

print(harris_p2['[Fe/H]'].head())  #displays the first five values of the [Fe/H] column

print(harris_p2['[Fe/H]'].isna().sum()) #this returns number of missing/non convertible metallicity values(it returned 5 missing/non convertible values, thus there is 152 usable metallicity values)
print(harris_p2['[Fe/H]'].min())
print(harris_p2['[Fe/H]'].max())
print(harris_p2['[Fe/H]'].mean())

plt.hist(harris_p2['[Fe/H]'], rwidth=0.9, bins=15)
plt.xlabel('[Fe/H]')
plt.ylabel('Number of globular clusters')
plt.title('Metallicity Distribution of Milky Way Globular Clusters')
print((harris_p2['[Fe/H]'] <-1.0).sum())
print((harris_p2['[Fe/H]'] >=-1.0).sum())


plt.show()

