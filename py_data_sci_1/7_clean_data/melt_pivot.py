#tidy data principles
#1. Columns represent separate variables
#2. Rows represent individual observations
#3. Observational units form tables

import pandas as pd
import numpy as np

df = pd.read_csv('data/treatment.csv')

print(df.head())

#pandas function melt will restructure columns into rows
#if you don't specify value_vars melt uses all columns not specified in ID vars
df_melt = pd.melt(frame=df, id_vars=['first_name', 'gender'], value_vars=['treatmentA', 'treatmentB'], var_name='treatment', value_name='result')
print(df_melt.head())
print(df_melt['treatment'].value_counts(dropna=False))

#un-melting data is called pivot
#pivot turns unique values into separate columns
#pivot_table can deal with multiple values - can use aggregation functions as well
df_pivot = df_melt.pivot_table(index=['first_name','gender'], columns='treatment', values='result')

#note this is not the original dataframe, the index must be reset
print(df_pivot.head())
print(df_pivot.index)

df_pivot = df_pivot.reset_index()
print(df_pivot.head())
print(df_pivot.index)

#note on column creation/parsing
df_pivot['sex'] = df_pivot.gender.str[0]
print(df_pivot.head())



