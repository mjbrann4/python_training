#iris dataset

from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

iris = datasets.load_iris()
print(type(iris))
print(iris.keys())

#features and target are numpy arrays
print(type(iris.data), type(iris.target))

#samples are in rows, features in columns.
#150 samples, 4 features
print(iris.data.shape)

#target is coded 0, 1, 2 for each flower type
print(iris.target)
print(iris.target_names)

#exploratory data analysis (EDA)
x = iris.data
y = iris.target

#build dataframe - assign feature names to columns
df = pd.DataFrame(x, columns=iris.feature_names)
print(df.head())

#visual EDA
#c is passed to y so datapoints will be colored by flower species
pd.scatter_matrix(df, c=y, figsize=[8,8], s=150, marker='D')
plt.show()

#flowers are clustered according by species


#code for count plots
#plt.figure()
#sns.countplot(x='education', hue='party', data=df, palette='RdBu')
#plt.xticks([0,1], ['No', 'Yes'])
#plt.show()



