import pandas as pd

#create dataframe from dict
dict = {
	'country': ['Brazil', 'Russia', 'India', 'China'],
	'capital': ['Brasilia', 'Moscow', 'New Dehli', 'Beijing'],
	'area': [8.516, 17.10, 3.286, 9.597],
	'population': [200.4, 143.5, 1252, 1357],
}

df = pd.DataFrame(dict)
print(df)

#set index
df.index = ['BR', 'RU', 'IN', 'CH']
print(df)


#column access in series
print(df['country'])


#a series is essentially a 1-d array that can be labeled
print(type(df['country']))

#to select a column but keep in a data frame
print(df[['country']])
print(type(df[['country']]))

#subset dataframe
print(df[['country', 'capital']])

#can also access rows using slices
print(df[1:4])

#square brackets have limited functionality
#ideally use somethng like 2d Numpy arrays
#my_array[rows, columns]

#pandas - loc (label-based)
#iloc - (integer position-based)

#this produces series again, on different lines
print(df.loc['RU'])

#use two brackets to get a dataframe
print(df.loc[['RU']])

#subset dataset rows
df2 = df.loc[['RU', 'IN', 'CH']]
print(df2)

#subset rows and columns
df_row_col_subset = df.loc[['RU', 'IN', 'CH'], ['country', 'capital']]
print(df_row_col_subset)

#subset columns only
print(df.loc[:, ['country', 'capital']])

#loc is very similar to numpy subsetting

#iloc rows
print(df.iloc[[1,2,3]])

#iloc rows and cols
print(df.iloc[[1,2,3], [0,1]])

#iloc cols
print(df.iloc[:, [0,1]])


