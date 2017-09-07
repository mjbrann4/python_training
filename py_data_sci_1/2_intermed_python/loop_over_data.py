import numpy as np

world = { "afghanistan":30.55,
		  "albania":2.77,
		  "algeria":39.21
}

#you can get a list of keys, values, or items(both) from a dictonary
#prints a list of keys
print(world.keys())

#prints a list of values
print(world.values())

#prints a list of tuples (a key-value pair)
print(world.items())


#need to call items method on world
for key, value in world.items():
	print(key)
	print(value)

#numpy array loops
np_height = np.array([1.7,1.8,1.5,1.6])
np_weight = np.array([80, 70, 40, 65])
bmi = np_weight / np_height ** 2

#basic for loop works
for val in bmi:
	print(val)

#2d numpy array
meas = np.array([np_height, np_weight])

#this won't work, prints out each iteration
for val in meas:
	print(val)

#use np.nditer to loop over numpy array and print in one list
for val in np.nditer(meas) :
	print(val)







