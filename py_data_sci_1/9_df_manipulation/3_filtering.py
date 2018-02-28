import pandas as pd 

df = pd.read_csv('data/sales.csv', index_col='month')
print(df.head())

# create a boolean series
print(df.salt>60)

# filtering with boolean series
print(df[df.salt > 60])

enough_salt = df.salt > 60
print(df[enough_salt])

# filters can be combined with and/or/not
a = df[ (df.salt >= 50) & (df.eggs < 200) ]
b = df[ (df.salt >= 50) | (df.eggs < 200) ]
print(a,b)

# Zeroes and NaNs
#------------------

df2 = df.copy()
df2['bacon'] = [0,0,50,60,70,80]
print(df2)

# select columns with all nonzeros
print(df2.loc[:, df2.all()])

# select columns with any nonzeros
print(df2.loc[:, df2.any()])

# select columns with any NaNs
print( df.loc[:, df2.isnull().any()] )

# select columns without any NaNs
print( df.loc[:, df2.notnull().all()] )

# drop rows with any NaNs
df_drops = df.dropna(how='any').copy()
print(df_drops)


# Filtering columns based on others
#----------------------

#extract egg sales in months were sale sales were high
print(df.eggs[df.salt > 55])

# modify a column based on another
new = df.eggs[df.salt > 55] + 5
print(new)


# Quiz
#------------------------

# Import numpy
import numpy as np

election = pd.read_csv('data/penn_2012.csv', index_col='county')


# Create the boolean array: too_close
too_close = election['margin'] < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election['winner'][too_close] = np.nan

# Print the output of election.info()
print(election.info())




