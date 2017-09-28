# y = a1x1 + a2x2 + b
# y - target
# x1, x2 - features
# a1,a2,b - parameters of model
# define error function for any given line, chose line
# that minmized error function (or loss function)

# !!When you call fit on regression model in scikit learn it
# calculates this under the hood

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

boston = datasets.load_boston()
print(boston.keys())
print(boston['feature_names'])

X = boston.data
y = boston.target

# fit linear regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42) 
reg_all = linear_model.LinearRegression()

reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test)

print("Test set prediction:\n {}".format(y_pred))

print("R^2: {}".format(reg_all.score(X_test, y_test)))

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: {}".format(rmse))

