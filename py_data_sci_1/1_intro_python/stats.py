import numpy as np

np_baseball = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
					[  65.4, 59.2, 63.6, 88.4, 68.7]])

print(np.mean(np_baseball[0,:]))
print(np.median(np_baseball[1,:]))

#correlation
print(np.corrcoef(np_baseball[0,:], np_baseball[1,:]))

#std deviation
np.std(np_baseball[:,0])

#numpy is much faster, also has sum and sort

#generate normal distributed data
#pass mean, std dev, num samples
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60, 15, 5000), 2)
np_city = np.column_stack((height, weight))

print(np.corrcoef(np_city[:,0], np_city[:,1]))

