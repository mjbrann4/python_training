import pandas as pd
import numpy as np 
import sys

#create dataframe from dict
dict = {
	'country': ['Brazil', 'Russia', 'India', 'China'],
	'capital': ['Brasilia', 'Moscow', 'New Dehli', 'Beijing'],
	'area': [8.516, 17.10, 3.286, 9.597],
	'population': [200.4, 143.5, 1252, 1357],
}

df = pd.DataFrame(dict)
print(dict)

#set index
df.index = ['BR', 'RU', 'IN', 'CH']
print(df)

#filter to countries with area > 9 million km2

#want to get pandas series not dataframe
is_gt9 = df.loc[:,'area'] > 9
print(is_gt9)

#now can subset by just passing in bracket
df_gt9 = df[is_gt9]
print(df_gt9)
print(type(df_gt9))

#can do this on one line
z = df[df['area'] > 9]
print(z)

#multiple restrictions- between 3 and 9 million
print(df[np.logical_and(df['area'] > 3, df['area'] < 9)])




