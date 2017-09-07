x = str(5)
print(x)
print(type(x))


#function header- value is called parameter here
def square(value):
	new_value = value ** 2
	return new_value 

#pass in value is called argument
num = square(4)
print(num)

#docstrings describe what your function does-serve as documentation
#placed immediately after function header in triple quotes
def cube(value):
	"""Return the cube of a value"""
	new_value = value ** 3
	return new_value


#multiple parameters
def raise_to_value(value1, value2):
	"""Raise value1 to the power of value2"""
	new_value = value1 ** value2
	return new_value 

z = raise_to_value(2, 3)
print(z)









