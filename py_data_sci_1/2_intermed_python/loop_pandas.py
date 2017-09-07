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
df.index = ['BR', 'RU', 'IN', 'CH']

#standard for loop will loop over column names
for val in df:
	print(val)

#iterrows method will select label of row and data in row as series
for lab, row in df.iterrows():
	print(lab)
	print(row)

#can subset within this method
for lab, row in df.iterrows():
	print(lab + ": " + row['capital'])

#create a new column in a data frame- this is inefficient tho
for lab, row in df.iterrows():
	df.loc[lab, 'name_length'] = len(row['country'])

print(df)


#better approach to creating a new column from applying a function on an
#existing column is to use apply
df['name_length2'] = df['country'].apply(len)
print(df)



#create static column in 2 ways:
df['test'] = 'hello'
df.loc[:,'test2'] = 'loc_hello'
print(df)
