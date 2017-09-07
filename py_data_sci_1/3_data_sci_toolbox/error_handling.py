#main way to handle errors is the try-except clause
#run code following try if it doesnt work then except

def sqrt(x):
	"""Returns the square root of a number."""
	try:
		return x ** (0.5)
	except:
		print('x must be an int or float')

print(sqrt(4))

sqrt('hello')


#can specify type of error
def sqrt(x):
	"""Returns the square root of a number."""
	try:
		return x ** (0.5)
	except TypeError:
		print('x must be an int or float')

sqrt('new')


#can also raise an error if something we don't want to happen occurs
#eg square root of negative number
#can specify type of error
def sqrt(x):
	"""Returns the square root of a number."""
	if x < 0:
		raise ValueError('x must be non-negative')
	try:
		return x ** (0.5)
	except TypeError:
		print('x must be an int or float')

sqrt(-2)