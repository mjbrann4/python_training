#LEGB Rule- searches scope in this order
#Local scope
#Enclosing functions
#Global
#Built-in


#def outer():
	#x = ..

	#def inner():
		#y = x ** 2  <- python searches inner first then outer for value x

#nested functions can process something multiple times
def mod2plus5(x1, x2, x3):
	"""Returns the remainder plus 5 of 3 values"""

	def inner(x):
		"""returns remainder of 5 plus a value"""
		return x % 2 + 5

	return (inner(x1), inner(x2), inner(x3))

print(mod2plus5(1,2,3))

#raise_val will return a FUNCTION that will raise numbers to the nth power
def raise_val(n):
	"""Return the inner function"""

	def inner(x):
		"""Raise x to the power of n"""
		raised = x ** n
		return raised

	return inner

square = raise_val(2)
cube = raise_val(3)
print(square(2), cube(4))


#use nonlocal function to create and change names in enclosing scope
def outer():
	"""Prints the value of n."""
	n = 1

	def inner():
		nonlocal n
		n = 2
		print(n)

	inner()
	print(n)


outer()




