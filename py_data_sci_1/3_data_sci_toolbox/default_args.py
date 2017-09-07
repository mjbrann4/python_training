import numpy as np

#assign default argument by using equals
def power(number, pow=1):
	"""Raise number to the power of pow."""
	new_value = number ** pow
	return new_value

print(power(9,2))
print(power(9)) # <- uses defualt arg

#flexible number of arguments
def add_all(*args):
	"""Sum all values in *args together."""

	#passed in as tuple
	print(type(args))

	#Initialize sum
	sum_all = 0

	#Accumulate the sum
	for num in args:
		sum_all += num

	#or
	sum_all = np.sum(args)

	return sum_all

print(add_all(1,2,3,4,5))

#**kwargs for arguments preceded by identifiers
def print_all(**kwargs):
	"""Print out key-value pairs in **kwargs."""

	#kwargs is a dict
	print(type(kwargs))

	#Print out the key-value pairs
	for key, value in kwargs.items():
		print(key + ": " + value)

print_all(name="dumbledore", job="headmaster")





