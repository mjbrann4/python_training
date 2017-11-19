import pandas as pd
import numpy as np


# read_csv can read strings into datetime objects
df = pd.read_csv('data/weather_data_austin_2010.csv', parse_dates=True, index_col='Date')

print(df.info())
print(df.head())


# select records with loc
print(df.loc['2010-03-21 06:00:00', 'Temperature'])

#select whole day
print(df.loc['2010-03-21'])

print(df.loc['March 10, 2010'])

# slicing between dates
print(df.loc['2010-10-10':'2010-10-20'].shape)

# convert strings to datetime
evening_2_11 = pd.to_datetime(['2010-03-11', '2010-03-12'])
print(evening_2_11)

# reindex dataframe
df = df.reindex(evening_2_11)
print(df.head())

# can fill forward or backwards
#df = df.reindex(evening_2_11, method='ffill')
#df = df.reindex(evening_2_11, method='bfill')

# select particular dates
df = pd.read_csv('data/weather_data_austin_2010.csv', parse_dates=['Date'])
print(df.info())


# reindexing can be powerful combining data
#Reindexing is useful in preparation for adding or otherwise
#combining two time series data sets. To reindex the data, we 
#provide a new index and ask pandas to try and match the old data to the new index. 

# Reindex without fill method: ts3
ts3 = ts2.reindex(ts1.index)

# Reindex with fill method, using forward fill: ts4
ts4 = ts2.reindex(ts1.index, method='ffill')

# Combine ts1 + ts2: sum12
sum12 = ts1 + ts2

# Combine ts1 + ts3: sum13
sum13 = ts1 + ts3