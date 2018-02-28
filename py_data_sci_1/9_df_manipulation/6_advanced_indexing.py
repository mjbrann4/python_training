import pandas as pd
import numpy as np 

# key python building blocks:
# index, series, dataframes
# index - sequence of lables, series - 1D array with index, df - 2D array with series as columns

# indexs are immutable, and homogenous in data type

prices = [10.70, 10.86, 10.74, 10.71, 10.79]
shares = pd.Series(prices)
# index is ints
print(shares)

days = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri']
shares = pd.Series(prices, index = days)
# now index is strings
print(shares)

# works basically like lists
print(shares.index)
print(shares.index[2])
print(shares.index[:2])
print(shares.index[-2:])
print(shares.index.name)

# assign an index
shares.index.name = 'weekday'
print(shares)

# indexes are immutable - causes error
# shares.index[2] = 'Wednesday'

# you can overwrite an entire index all at once
shares.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(shares)

# read in election data
election = pd.read_csv('data/penn_2012.csv')
print(election.head())
print(election.info())

election.index = election['county']
print(election.info())

# delete redundant column using del (or preferably drop)
del election['county']
print(election.head())


print(election.index)
print(election.index.name)

# convert index to uppercase with list comprehension
# Create the list of new indexes: new_idx
new_idx = [idx.upper() for idx in election.index]
# Assign new_idx to election.index
election.index = new_idx

# Print the election DataFrame
print(election.head())

# Assign name to columns as well
election.columns.name = 'Election Data'
print(election.head())


