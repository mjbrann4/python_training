import pandas as pd 
file = 'data/ed_data.xlsx'

data = pd.ExcelFile(file)

#access sheet names in list
print(data.sheet_names)

#access data frame as sheet name
df1 = data.parse('EDU01A')

#access data frame as sheet index
df2 = data.parse(1)

print(df1.head())
print(df2.head())

