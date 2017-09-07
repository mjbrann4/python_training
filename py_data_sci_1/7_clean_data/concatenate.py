#concatenate dataframe
import pandas as pd

dict1 = {
	'country': ['Brazil', 'Russia'],
	'capital': ['Brasilia', 'Moscow'],
	'area': [8.516, 17.10],
	'population': [200.4, 143.5]
}

dict2 = {
	'country': ['India', 'China'],
	'capital': ['New Dehli', 'Beijing'],
	'area': [3.286, 9.597],
	'population': [1252, 1357]
}


df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

df_concat = pd.concat([df1, df2])
print(df_concat)

#index labels are original, eg this returns two
print(df_concat.loc[0,:])

#to ignore index set ignote_index = True
df_concat = pd.concat([df1, df2], ignore_index=True)
print(df_concat)
