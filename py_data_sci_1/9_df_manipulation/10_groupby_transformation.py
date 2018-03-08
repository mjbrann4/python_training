import pandas as pd

# apply distinct transformations to distinct groups
# changes dataframes in place

def zscore(series):
    return (series - series.mean()) / series.std()

auto = pd.read_csv('data/auto-mpg.csv')
print(auto.head())

# apply to one series
z = zscore(auto['mpg'])
print(z.head())

# we can calculate z scores grouped by year
z_year = auto.groupby('yr')['mpg'].transform(zscore).head()
print(z_year.head)

# we use apply when we don't need full aggregation or transformation
def zscore_with_year_and_name(group):
    df = pd.DataFrame(
        {'mpg': zscore(group['mpg']),
         'year': group['yr'],
         'name': group['name']})
    return df

# note this function is called 13 times, once for each year b/w 1970-82 
z2 = auto.groupby('yr').apply(zscore_with_year_and_name)
print(z2.head())
print(z2.shape)

