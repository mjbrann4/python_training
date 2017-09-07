import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/MOCK_DATA.csv')

#histograms
df.wages.plot('hist')
plt.show()

#histogram options
#df['wages'].plot(kind='hist', rot=70, logx=True, logy=True)
#plt.show()

#Box plots
df.boxplot(column='wages', by='gender')
plt.show()

#scatter plots- relationship between 2 numeric variables

