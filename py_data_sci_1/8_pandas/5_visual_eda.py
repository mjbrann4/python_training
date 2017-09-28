import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

iris = pd.read_csv('iris.csv', index_col=0)

iris.head()
iris.plot(x='sepal_length', y='sepal_width', kind='scatter')
plt.xlabel('sepal length (cm)')
plt.show()

# box plot
iris.plot(y='sepal_length', kind='box')
plt.ylabel('sepal length (cm)')
plt.show()

# histogram
iris.plot(y='sepal_length', kind='hist')
plt.show()

#cumulative distribution function
iris.plot(y='sepal_length', kind='hist', cumulative=True)
plt.title('Cumulative distribution function (CDF)')
plt.show()
