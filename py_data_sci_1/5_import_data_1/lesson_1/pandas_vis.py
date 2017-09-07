import pandas as pd 
import matplotlib.pyplot as plt 

file = 'data/countries.csv'
df = pd.read_csv(file)
print(df.head())

#print(df['country'])

pd.DataFrame.hist(df[['population']])
plt.xlabel('Population')
plt.ylabel('count')
plt.show()
