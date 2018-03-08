import pandas as pd

in_dict = {
    'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
    'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
    'bread': [139, 237, 326, 456],
    'butter': [20, 45, 70, 98],
}

sales = pd.DataFrame(in_dict)
print(sales.head())

# can use boolean filtering
print(sales.loc[sales['weekday'] == 'Sun'].count())

# groupby uses split-apply-combine
# 1. split rows by weekday
# 2. apply count() function on each group
# 3. combine counts per group
z = sales.groupby('weekday').count()
print(z)

z = sales.groupby('weekday')['bread','butter'].sum()
print(z)

# multi-level groupby
z = sales.groupby(['city', 'weekday']).mean()
print(z)

# can use any pandas series as group by
customers = pd.Series(['Dave', 'Alice', 'Bob', 'Alice'])
z = sales.groupby(customers)['bread'].sum()
print(z)

uniq = sales['weekday'].unique()
print(uniq)

# categorical data is more efficient for operations like groupby, 
# also uses less memory
sales['weekday'] = sales['weekday'].astype('category')
print(sales['weekday'])

