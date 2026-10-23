# PHYS3116-Accreted Milky Way Globular Clusters

## Project Overview
This project investigates Accreted Milky Way Globular Clusters by analysing astronomical datasets stored in csv files which contain data about cluster positions and distances, metallicity, brightness and colours, velocities and structural properties, ages and stellar masses. Through analysing and comparing data accreted clusters can be identifed as potential accretion candidates and estimates of the accreted population can be made which helps understand the formation of the Milky Way and whether it is primarily composed of in-situ clusters or accreted clusters.

## Datasets

## Methodology
Matplotlib was used to plot a metallicity histogram with 15 bins to show the distribution of cluster metallicities.
Pandas comparisons were used to count number of clusters on each side of the -1.0 threshold for cluster metallicities
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
### Age-Metallicity plot
both datasets aren't identical, for example. 47 Tuc's reported age differs by a factor of 1.05 GYr, but this is kind of expected as measurements may come from different methods or analyses.

From the Van Den Verg dataset:
Most clusters appear from 11-13.5 Gyr old.
There appears to have a generalised tendency for older clusters to have a lower metallicity, however, the relationship is not so clean or uniform. There is notably one outlier, Pal12 that has the same metalicity of Globular Clusters ~2.5Gyrs older.
Clusters such as M12 has a high metallicity for it's age, showing that age alone is not a sole indicator of metallicity. <!-- Incomplete, will work on tmr -->
