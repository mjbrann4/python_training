import pandas as pd
import numpy as np

# Note! apply() and map() can be very slow and should be avoided when performance is desired
# NumPy, SciPy and pandas come with a variety of vectorized functions that are much faster

# these strategies use vectorized (elementwise) computation to perform on entire structure with no loops

df = pd.read_csv('data/sales.csv', index_col='month')
print(df.head())

# convert to dozens units (no loops works for whole df)
print(df.floordiv(12))

# numpy floor_divide function
print(np.floor_divide(df,12))

def dozens(n):
    return n//12

# apply this function to entire dataframe
doz_df = df.apply(dozens)
print(doz_df)

# can use lambda functions
print( df.apply(lambda n: n//12))

# storing a transformation
df['dozens_of_eggs'] = df.eggs.floordiv(12)
print(df)

# note apply and vectorized methods work on series as well as dataframes

# df index is special attribute
print(df.index)

# dfs, series, and index objects come with a str attribute as accesor to vectorized string transformations
df.index = df.index.str.upper()
print(df)

# index has NO apply method, it uses map
df.index = df.index.map(str.lower)
print(df)

# can use arithmatic operators
df['salty_eggs'] = df['salt'] + df['dozens_of_eggs']
print(df)


# can use maps and dictionaries together
election = pd.read_csv('data/penn_2012.csv', index_col='county')
print(election.head())

# Create the dictionary: red_vs_blue
red_vs_blue = {
    'Obama': 'blue',
    'Romney': 'red'
}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election['winner'].map(red_vs_blue)

# Print the output of election.head()
print(election.head())


# Vectorized functions are much faster

from scipy.stats import zscore

# Call zscore with election['turnout'] as input: turnout_zscore
turnout_zscore = zscore(election['turnout'])

# Print the type of turnout_zscore
print(type(turnout_zscore))

# Assign turnout_zscore to a new column: election['turnout_zscore']
election['turnout_zscore'] = turnout_zscore

# Print the output of election.head()
print(election.head())






