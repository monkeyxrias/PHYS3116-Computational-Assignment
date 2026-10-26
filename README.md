# PHYS3116-Accreted Milky Way Globular Clusters

## Project Overview
This project investigates Accreted Milky Way Globular Clusters by analysing astronomical datasets stored in csv files which contain data about cluster positions and distances, metallicity, brightness and colours, velocities and structural properties, ages and stellar masses. Through analysing and comparing data accreted clusters can be identifed as potential accretion candidates and estimates of the accreted population can be made which helps understand the formation of the Milky Way and whether it is primarily composed of in-situ clusters or accreted clusters.

## Datasets
HarrisPartI:
Contains information regarding positions and distances of globular clusters specifically things like right ascension, declination, longitude etc. The main data column that was used was distance from galactic centre (R_gc) measured in kiloparsecs.
HarrisPartII:
This mostly contains data pertaining to metallicity, brightness and colours specifically it includes data such as metallicity, V-band related quantities and the differences between magnitudes measured in different photometric bands. Metallicity ([Fe/H]) was the main measurement that was used in the metallicity histogram and distance-metallicity plot.
HarrisPartIII:
Contains information mostly about velocities and structural properties such as heliocentric radial velocity, central velocity dispersion, cluster concentration parameter and half-light radius.
vandenBerg:
Contains data regarding ages and metallicities as well as data like absolute V-band magnitude, horizontal-branch morphology parameter and central escape velocity. Age and metallicity were used to investigate the age vs metallicity relation and the R_G column was used to investigate the distance–metallicity relationship.
Krause21:
Contains data regarding ages,metallicities, masses and structure as well as data like stellar mass, object and half-light radius.The Age and FeH columns were used to investigate the age–metallicity relationship.

## Methodology
For exploration.py:
Pandas was used to read the CSV files and analyse their data.
Matplotlib was used to plot a metallicity histogram with 15 bins to show the distribution of cluster metallicities.
pd.read_csv() reads a CSV file and stores its contents in a pandas dataframe.
 These commands print(harris_p2.head()), print(harris_p2.shape) and print(harris_p2.columns) inspect the first five records, the dimensions of the dataset and its column names.
pd.to_numeric() was used to convert the metallicity column into numerical values because pandas read some of them as strings and errors='coerce' replaces values that can't be converted with NaN (missing values).
.min(), .max() and .mean() were used to calculate the minimum, maximum and average metallicities.
Pandas comparisons were used to count number of clusters on each side of the -1.0 threshold for cluster metallicities.
Finally the histogram was created using plt.hist() to create a histogram of metallicity measurements, bins=15 to divide the metallicity range into 15 intervals and rwidth=0.9 to make each bar slightly narrower than its interval leaving small gaps. Additionally the plots were labelled using plt.ylabel and plt.xlabel

For exploration_Age_Metallicity.py:
Pandas was used to read the CSV files and analyse their data using pd.read_csv().
print(vandenberg.columns.tolist()) and print(krause21.columns.tolist()) were used to display the column names for each dataset.
print(vandenberg.head()) and vandenberg['Age'] = pd.to_numeric(vandenberg['Age']) were also used in the same was they were used in exploration.py in order to display the first five rows of each dataset and to also convert the age and metallicity columns into numerical values so that they can be used to plot the data.
plt.scatter(vandenberg['Age'], vandenberg['FeH'], label='Van den Berg')was used to plot the dataset and plt.show was used to show the actual scatter plot for the age-metallicity scatter plot.This was done for both the Krause and vandenBerg dataset.
print(vandenberg['Age'].corr(vandenberg['FeH']))was used to calculate the pearson correlation coefficient and was also done for both datasets.
Pandas filtering was also used to identify Palomar 12 and Terzan7 in their respecitve datasets using print(vandenberg[vandenberg['Name'] == 'Pal12']) and print(krause21[krause21['Object'] == 'Terzan7']).

For Galactic Distance to Metallicity.py:
This script used essentially the same methods that are used in the previous 2 scripts such as pd.read_csv, print(vandenberg.columns.tolist()), print(vandenberg.head()), vandenberg['R_G'] = pd.to_numeric(vandenberg['R_G']).
plt.scatter(vandenberg['R_G'], vandenberg['FeH'], label='Van den Berg') and plt.scatter(Harris1['R_gc'], Harris2['[Fe/H]'], label='Harris 1996') as used to build the scatter plot for Galactocentric distacnes vs Metallicity for both the vandenBerg and Harris datasets.
print(vandenberg['R_G'].corr(vandenberg['FeH'])) and print(Harris1['R_gc'].corr(Harris2['[Fe/H]'])) was used to compute the correlation coefficients for the vandenBerg and Harris1 datatsets.


## Preliminary Results
Total globular cluster records -> 157
Number of columns -> 14
Valid metallicity measurements -> 152
Missing metallicity measurements -> 5
Minimum [Fe/H] -> -2.37
Maximum [Fe/H] -> 0.00
Mean [Fe/H] -> -1.265
The metallicity histogram shows that clusters have a range of metallicities with the highest frequency occurring at around [Fe/H]=-1.4 where approximately 21 clusters are found. 
68.4% of Clusters have a metallicity less than -1.0  and 31.6% of clusters have a metallicity greater than or equal to -1.0
### Age-Metallicity Plots
Both datasets aren't identical, for example. 47 Tuc's reported age differs by 1.05Gyr, but this is kind of expected as measurements may come from different methods or analyses.

From the Van Den Berg dataset:
Most clusters appear from 11-13.5 Gyr old.
There appears to be a generalised tendency for older clusters to have a lower metallicity which aligns with the correlation coefficient of -0.718 however, the relationship is not so clean or uniform. There is notably one outlier, Pal12 that has the same metallicity of globular clusters ~2.5Gyrs older.
Clusters such as M12 have a high metallicity for its age, showing that age alone is not a sole indicator of metallicity. 

From the Krause21 dataset:
Most clusters range from about 7.4 to 14.5 Gyr old with the most clusters concentrated around 11-14 Gyr. Similar to the Van Den Berg dataset there is also a general tendency for older clusters to have lower metallicity however the relation is not as strong with a correlation coefficient equal to -0.398. It is also evident that there is quite a large scatter for example at 13 Gyr clusters have metallicities ranging anywhere from -0.7 to -2.1. This tells us age alone can't explain metallicity for globular clusters and different clusters may have formed in environments with different chemical histories. It is also important to note there is an outlier Terzan 7 at 7.4 Gyr with a metallicity of -0.12.

## Galactocentric Distance-Metallicity Plots

From the Harris dataset:
The data shows most clusters are concentrated within approximately 20 kpc of the galactic centre. These clusters have a wide range of metallicities varying from approximately -2.4 to 0.0. The most distant clusters at over 60 kpc are all relatively metal poor. The overall plot shows considerable scatter with a weak negative correlation of approximately -0.271.

From the Van Den Berg dataset:
The 55 clusters extend from approximately 1.2 to 21.4 kpc from the galactic centre. Clusters with higher metallicities have a general tendency  to be closer to the galactic centre while less metallic clusters spread across a wider range of distances. There is a moderate negative correlation of approximately -0.413.

## Potential Accretion Candidates 
## Limitations
## Conclusion