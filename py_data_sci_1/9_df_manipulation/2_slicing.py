import pandas as pd

df = pd.read_csv('data/sales.csv', index_col='month')
print(df.head())

# this is a series
print(df['eggs'])

# can use colon syntax when indexing a series
# recall this is half open (non-exclusive on upper bound)
print(df['eggs'][1:4])
print(df['eggs'][4])

# this slices all rows and some columns (note it DOES include right endpoint)
print(df.loc[:, 'eggs':'salt'])

# some rows, all columns
print(df.loc['Jan':'Apr', :])
# or - print(df[:]['Jan':'Apr'])


# some rows, some columns
print(df.loc['Mar':'May', 'salt':'spam'])

# iloc is similar just use positions
print(df.iloc[2:5, 1:])

# can use lists instead of slices
print(df.loc['Jan':'May', ['eggs', 'spam']])

print(df.iloc[[0,4,5], 0:2])

# select series
df['eggs']

# select dataframe
df[['eggs']]


# slicing quiz
#-------------------------------------

election = pd.read_csv('data/penn_2012.csv', index_col='county')

# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election[:]['Perry':'Potter']

# Print the p_counties DataFrame
print(p_counties)

# !!Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev using -1 step!
p_counties_rev = election.loc['Potter':'Perry':-1]

# Print the p_counties_rev DataFrame
print(p_counties_rev)

# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.loc[:,:'Obama']

# Print the output of left_columns.head()
print(left_columns.head())

# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:,'Obama':'winner']

# Print the output of middle_columns.head()
print(middle_columns.head())

# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:,'Romney':]

# Print the output of right_columns.head()
print(right_columns.head())




