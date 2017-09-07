import pandas as pd
import numpy as np
import copy

data = {
    'customer': ['jeff', 'jerry', 'mike', 'chris', 'chris'],
    'salary': [np.NaN, 4000, 3500, 2200, 2200],
    'spending': [1000, 3000, 5000, np.NaN, np.NaN]
}
df = pd.DataFrame(data)

#deal with duplicate data
print(df.shape)
df = df.drop_duplicates()
print(df.shape)

###############
#missing data
###############
print(df.info())

#drop all missing values
df_dropped = df.dropna()
print(df_dropped.info())

#fill missing values- user provided value or summary stat
#whole dataset
df_filled = df.fillna(0)
print(df_filled)

#single column
df_test = copy.deepcopy(df)
df_test['salary'] = df_test['salary'].fillna(0)
print(df_test)

#multiple columns
df[['salary', 'spending']] = df[['salary', 'spending']].fillna(999)
print(df)

#fill missing with test statistic 
df = pd.DataFrame(data)
mean_value = df[['salary', 'spending']].mean()
print(mean_value)
df[['salary', 'spending']] = df[['salary','spending']].fillna(mean_value)
print(df)


