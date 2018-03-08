import pandas as pd

in_dict = {
    'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
    'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
    'bread': [139, 237, 326, 456],
    'butter': [20, 45, 70, 98],
}

sales = pd.DataFrame(in_dict)
print(sales.head())

customers = pd.Series(['Dave', 'Alice', 'Bob', 'Alice'])

# can pass relevent strings into agg
grouped = sales.groupby('city')[['bread', 'butter']].agg(['max', 'sum'])
print(grouped)

# can also do custom aggregations
# return range of data in each category
def data_range(series):
    return series.max() - series.min()

cust_grouped = sales.groupby('city')[['bread', 'butter']].agg(data_range)
print(cust_grouped)

# use dictionaries with custom aggs
cust_grouped = sales.groupby(customers)[['bread', 'butter']].agg({'bread':'sum', 'butter':data_range})
print(cust_grouped)