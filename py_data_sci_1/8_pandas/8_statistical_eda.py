import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/auto-mpg.csv')

#print(df.describe())

#counts count non-missing for whole df or series
print(df['weight'].count())
print(df.count())

# mean calculates mean 
print(df['weight'].mean())

# standard deviation
print(df['weight'].std())

# medians
print(df['weight'].median())

# quantiles for any value
q = 0.8
print(df.quantile(q))

# can use quantile in array
q = [0.25, 0.75]
print(df['mpg'].quantile(q))

# min/max etc
print(df.max())

df['mpg'].plot(kind= 'box')
plt.show()

# can take average accross all columns
means = df.mean(axis='columns')
print(means)