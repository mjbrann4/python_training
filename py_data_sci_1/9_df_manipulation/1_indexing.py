import pandas as pd
import numpy as np

df = pd.read_csv('data/sales.csv', index_col='month')
print(df.head())

# simplest indexing uses square brackets
print('Jan Salt Sales: ', df['salt']['Jan'])

# columns may be referred to as attributes of the df if labels are valid
print (df.eggs['Mar'])

# loc (labels) and iloc (index positions) are best practice
# syntax: bracket, row, column, bracket
print(df.loc['May', 'spam'])
print(df.iloc[4,2])

# return df with nested list in square brackets
df_new = df[['salt', 'eggs']]
print(df_new)
