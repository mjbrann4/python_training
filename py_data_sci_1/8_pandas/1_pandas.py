import pandas as pd

df = pd.read_csv('data/auto-mpg.csv')

#first 5 rows, first 2 columns
print(df.iloc[:5, :2])

print(df.head())

#extracting a single column returns a series
mpg = df['mpg']
print(type(mpg))
print(mpg.head())

#to extract numerical values use .values attribute 
#- this extracts a numpy array
mpg_val = mpg.values
print(type(mpg_val))

#pandas series is 1 diminsional labeled numpy array
#pandas df is 2 diminsional labeled numpy array whose columns are series



