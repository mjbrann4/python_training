import pandas as pd

#can import data from csvs - can set index column here to a column
df1 = pd.read_csv('data/auto-mpg.csv', index_col=0)

#can create df from dict 
dict1 = {
    'country': ['Brazil', 'Russia'],
    'capital': ['Brasilia', 'Moscow'],
    'area': [8.516, 17.10],
    'population': [200.4, 143.5]
}
df2 = pd.DataFrame(dict1)

#can create dfs from conforming lists
cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
signups = [7, 12, 3, 5]
visitors = [139, 237, 326, 456]
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']

list_labels = ['city', 'signups', 'visitors', 'weekday']

#list of lists
list_cols = [cities, signups, visitors, weekdays]

#list of tuples
zipped = list(zip(list_labels, list_cols))

data = dict(zipped)

users = pd.DataFrame(data)
print(users)

#Broadcasts to create entire column
users['fees'] = 0 
print(users)

#broadcast with a dict
heights = [59.0, 65.2, 61.4, 63.7, 64.1, 67.7]
data = {'height': heights, 'sex': 'M'}
results = pd.DataFrame(data)
print(results)

#can change column and index labels
results.columns = ['height (in)', 'sex']
results.index = ['A', 'B', 'C', 'D', 'E', 'F']
print(results)





