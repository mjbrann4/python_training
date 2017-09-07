#use () instead of [] to create generstor object
#like list comprehension, but does not store list in memory
#can be iterated over still
result = (2 * num for num in range(10))
print(result)

#can print out elements in for loop
for num in result:
	print(num)

#also can use list function
result = (2 * num for num in range(10))
print(list(result))

#note once you iterate you are done with it...
print(list(result))

#can use next function - this is called lazy evaluation whereby evaluation of expression
#is delayed until value is needed. Can help with large data
result = (2 * num for num in range(10))
print(next(result))
print(next(result))
print(next(result))

#store very large list in generator- do not do this in normal list!!
x = (num for num in range(10**10))
print(next(x))
print(next(x))

#can do all the same thing in generators as list comprehensions
even_nums = (num for num in range(10) if num % 2 == 0)
print(list(even_nums))

#generator functions produce generator objects
#instead of returning values using return they yield sequences of values using yield

def num_sequence(n):
	"""Generate values from 0 to n."""
	i = 0
	while i < n:
		yield i
		i += 1

result = num_sequence(5)
print(type(result))
for item in result:
	print(item)


