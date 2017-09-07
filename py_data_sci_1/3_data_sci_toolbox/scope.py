#scope - part of the program where an object or name may be accessible

#global scope- defined in main body of a script
#local scope - definied within a function
#built-in score - names in the pre-defined built-ins module

new_val = 10

def square(value):
	"""Returns the square of a number."""
	new_val = value ** 2
	return new_val

print(square(3))

#still contains old value
print(new_val)

#function will access global value only if no local value available
def square2(value):
	#new_val = 2
	new_value2 = new_val ** 2
	return new_value2
print(square2(3))


new_val = 10
def square(value):
	"""Returns the square of a number."""
	global new_val
	new_val = new_val ** 2
	return(new_val)

print(square(3))
print(new_val)




