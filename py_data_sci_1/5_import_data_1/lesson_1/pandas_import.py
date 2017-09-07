import pandas as pd 

#import a csv
filename = 'data/countries.csv'
data = pd.read_csv(filename, nrows=2)

#print column names
print(data.head())

#can create numPy like array with data.values
data_array = data.values
print(data_array)