import pandas as pd

dict1 = {
	'country': ['Brazil', 'Russia'],
	'capital': ['Brasilia', 'Moscow'],
	'area': [8.516, 17.10],
}

dict2 = {
	'c_name': ['Brazil', 'Russia'],
	'heat_level': [3.286, 9.597],
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

pd_merged = pd.merge(left=df1, right=df2, left_on='country', right_on='c_name')
print(pd_merged)


#note - if spelled same you can use on
dict1 = {
	'country': ['Brazil', 'Russia'],
	'capital': ['Brasilia', 'Moscow'],
	'area': [8.516, 17.10],
}

dict2 = {
	'country': ['Brazil', 'Russia'],
	'heat_level': [3.286, 9.597],
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

pd_merged = pd.merge(left=df1, right=df2, on = 'country')
print(pd_merged)


