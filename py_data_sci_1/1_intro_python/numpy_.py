import numpy as np

#numpy can do mathematical observation over a number of values

height = [1.7,1.8,1.5,1.6]
weight = [80, 70, 40, 65]

#calculation below fails need numpy
#weight/height**2

#numpy array you can do calculations over entire arrays

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print(bmi)

#numpy can do all this easily because they assume arrays only contain one type 
#of values in a the array

#this converts all to strings
x = np.array([1.0, 'is', True])
print(x)
print(type(x))

#numpy array has its own methods, be careful
python_list = [1,2,3]
numpy_array = np.array([1,2,3])

print(python_list + python_list)

#this sums lists
print(python_list + numpy_array)

#can index numpy list
print(bmi[1])

#create an array of booleans
print(bmi>23)
print(bmi)

#can subset with this
sub_bmi = bmi[bmi>23]
print(sub_bmi)













