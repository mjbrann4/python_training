import pandas as pd

df = pd.read_csv('data/MOCK_DATA.csv')

#inspect heads and tails
print(df.head())
print(df.tail())

#this returns index of column names
print(df.columns)

#this returns shape of data
print(df.shape)

#descriptive information
print(df.info())


#frequency functions
#note you can select columns using dot notation instead of bracket notation
print(df.gender.value_counts(dropna=False))

#can chain frequencies with head
print(df['last_name'].value_counts(dropna=False).head())

#summary statistics
print(df.describe())

