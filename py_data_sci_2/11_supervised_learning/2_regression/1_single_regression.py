# in regression target is continuous variable such as home price

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

boston = datasets.load_boston()
print(boston.keys())
print(boston['feature_names'])

x = boston.data
y = boston.target

# lets try taking only rooms
x_rooms = x[:,5]
print('x_rooms is: ', boston['feature_names'][5])

print(type(x_rooms), type(y))

# reshape
y = y.reshape(-1, 1)
x_rooms = x_rooms.reshape(-1, 1)

print(len(x_rooms))
print(len(y))

plt.scatter(x_rooms, y)
plt.ylabel('Value of house/1000 ($)')
plt.xlabel('Number of rooms')
plt.show()

#fit linear regression
reg = linear_model.LinearRegression()
reg.fit(x_rooms, y)

prediction_space = np.linspace(min(x_rooms), max(x_rooms)).reshape(-1, 1)

plt.scatter(x_rooms, y, color = 'blue')
plt.plot(prediction_space, reg.predict(prediction_space), 
    color='black', linewidth=3)

plt.show()


