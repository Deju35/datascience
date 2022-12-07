import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)
# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

import pandas as pd

df = pd.read_csv('pal.csv')
print(df)

cars = pd.read_csv('pal.csv', index_col=0)
print(cars)

print(cars[['country','drives_right']])
print(cars[0:3])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

#loc and iloc (3)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
import pandas as pd
import numpy as np
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
bs = cars.loc[:,'cars_per_cap']
isHuge = bs>500

cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 600)
medium = cars[between]

# Print medium
print(medium)


import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

for lab, row in cars.iterrows():
  print(lab) 
  print(row)

for lab,row in cars.iterrows():
  print(lab + ":" +str(row['cars_per_cap']))

#Add column (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
    
# Print cars
print(cars)

#Add column (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
