import pandas as pd

#create dataframe from dict
dict = {
	'Country': ['Brazil', 'Russia', 'India', 'China'],
	'Capital': ['Brasilia', 'Moscow', 'New Dehli', 'Beijing'],
	'area': [8.516, 17.10, 3.286, 9.597],
	'population': [200.4, 143.5, 1252, 1357],
}

df = pd.DataFrame(dict)
print(df)

#set index
df.index = ['BR', 'RU', 'IN', 'CH']
print(df)


#import csv

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)