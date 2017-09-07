
#we can loop over objects called iterables-
#lists, strings, dicts, file connectsions, etc
#an object with an associated iter() method is iterable

#applying iter() to an iterable creates an iterator
#iterator produces next value with next()

word = 'Da'
it = iter(word)
print(next(it))
print(next(it))

#print all values in one statement with *
word = 'Data'
it = iter(word)
print(*it)

#iterate over dict
pythonistas = {
	'hugo': 'bowne-anderson',
	'francis': 'castro'
}

for key, value in pythonistas.items():
	print(key, value)

#iterate over file connection
file = open('file.txt')

it = iter(file)
print(next(it))
print(next(it))

file.close()


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
