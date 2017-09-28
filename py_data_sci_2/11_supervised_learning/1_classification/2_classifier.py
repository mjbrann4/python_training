#first choice is picking the classifier that takes unlabeled data as input and outputs a label

#k-Nearest neighbors (k-NN)
#Basic idea is predict the label of any data point by
#looking at 'k' closest labeled data point
#taking a majority vote

#k-NN: creates intuition boundries

#Scikit-learn fit and predict
#all machine learning models implemented as Python classes
#implement the algorithms for learning and predicting
#store the information learned from the data

#training a model on the data = 'fitting' a model to the data 
#use .fit() method
#to predict the labels of new data: .predict() method

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

iris = datasets.load_iris()
x = iris.data
y = iris.target

#set up k-neighbors classifier and fit to training data
knn = KNeighborsClassifier(n_neighbors=6)

#data must be numpy array or pandas dataframe
#features must be continuous, no missing values allowed
#sklearn api requires features are in array where column is feature
#target must be column with same # of obs in feature data
print(x.shape, y.shape)

print(knn.fit(iris['data'], iris['target']))
knn.fit(x, y)

#can predict on same dataset you trainined on, though not practical
y_pred = knn.predict(x)
print(y_pred)


