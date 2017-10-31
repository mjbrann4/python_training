import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/auto-mpg.csv')
print(df.head())

print(df['origin'].value_counts(dropna=False))
print(df['cyl'].value_counts(dropna=False))

#can find categorical variable
print(df['origin'].describe())

# unique will return all unique values in a list
uniq = df['origin'].unique()
print(uniq)

# filtering by origin and extract dataframe
indices = df['origin'] == uniq[0]
us_cars = df.loc[indices,:]
print(type(us_cars))

indices = df['origin'] == uniq[1]
asia_cars = df.loc[indices,:]

indices = df['origin'] == uniq[2]
euro_cars = df.loc[indices,:]

print(us_cars['origin'].unique())

us_cars.plot(kind='hist', bins=50, range=(0,8), alpha=0.3)
plt.show()

# better to do descriptive stats separately
describe_all = df.describe()
describe_us = us_cars.describe()
describe_asia = asia_cars.describe()
describe_euro = euro_cars.describe()

print(describe_euro)

# computing errors etc...
error_us = 100 * np.abs(describe_us - describe_all)



