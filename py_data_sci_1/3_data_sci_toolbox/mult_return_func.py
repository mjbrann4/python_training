#return multiple values from a function with tuples
#tuples are immutable

even_nums = (2, 4, 6)
print(type(even_nums))

#can unpack a tuple into several variables
a, b, c = even_nums
print(a)
print(b)

#access tuple elements like lists
print(even_nums[1])

def raise_both(value1, value2):
	"""Raise value1 to power of value2 and vice versa."""
	new_value1 = value1 ** value2
	new_value2 = value2 ** value1

	new_tuple = (new_value1, new_value2)
	return new_tuple

powers = raise_both(4,3)
print(powers)


# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Return both arguments- automatically puts into tuple
    return shout1, shout2

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations','you')

# Print yell1 and yell2
print(yell1)
print(yell2)


