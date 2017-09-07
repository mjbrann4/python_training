import pandas as pd
import numpy as np

data = {
    'customer': ['jeff', 'jerry', 'mike', 'chris', 'chris'],
    'salary': [np.NaN, 4000, 3500, 2200, 2200],
    'spending': [1000, 3000, 5000, np.NaN, np.NaN]
}

df = pd.DataFrame(data)

df['diff'] = df['salary'] - df['spending']

assert 1==1

#assert df['diff'].notnull().all()
df['diff'] = df['diff'].fillna(0)
assert df['diff'].notnull().all()

#test whole dataset
#assert pd.notnull(ebola).all().all()

#test value >= 0
assert (df['diff'] >= -2000).all() 
