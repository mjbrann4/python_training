# cross-validation motivation
# model performance is dependent on way the data is split
# not representative of model's ability to generalize

# split dataset into 5 groups or folds
# we hold out first set, fit model on remaining 4 folds, predict on test set, compute metric of interest
# repeat on the second set, etc.

# we get 5 values of r squared, from which we can compute means, medians, confidence, etc.
# k folds = k-fold CV
# using more folds is more computationally expensive

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

boston = datasets.load_boston()
print(boston.keys())
print(boston['feature_names'])

X = boston.data
y = boston.target

# fit linear regression
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42) 

reg = linear_model.LinearRegression()
cv_results = cross_val_score(reg, X, y, cv=5)

print(cv_results)
print(np.mean(cv_results))
