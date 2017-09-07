#converting data types
import pandas as pd
import numpy as np

df = pd.read_csv('data/test_usage_data.csv')
print(df.dtypes)

#convert to string
df['score'] = df['score'].astype(str)

#convert to categorical
df['geoid1'] = df['geoid1'].astype('category')

#converting to categorical can make dataframe smaller
#some libraries can utilize categoricals

#use to_numeric with errors='coerce' to convert bad data to numbers
df['kwh'] = pd.to_numeric(df['kwh'], errors='coerce')
print(df.dtypes)

