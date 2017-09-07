#in classification accuracy is commonly used metric
#accuracy=fraction of correct predictions
#which data should be used to compute accuracy
#we want to know how well it will perform on new data
#common practice to split data into training and test set
#fit/train the classifier on the training set
#made predictions on the test set
#compute accuracy of model

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

iris = datasets.load_iris()
x = iris.data
y = iris.target

#pass in feature data, target data, proportion to test, 
#random state sets random seed-so reproducable
#stratify y will distribute labels?
#return 4 numpy arrays, training data, test data, training labels, test labels
x_train, x_test, y_train, y_test = train_test_split(x, y, 
	test_size=0.3, random_state=21, stratify=y)

knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)
print("Test set prediction:\n {}".format(y_pred))

#to test accuracy we use score method of the model
print(knn.score(x_test, y_test))

#note on model complexity-
#larger k = less complex = smoother decision boundry
#smaller k = more complex model = can overfit


#manually compute score
correct = []
for i, item in enumerate(y_test):
	correct.append(y_test[i] == y_pred[i])
print(np.mean(correct))


