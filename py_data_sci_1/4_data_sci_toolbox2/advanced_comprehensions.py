#can use conditionals in a list comprehension
x = [num ** 2 for num in range(10) if num % 2 == 0]
print(x)

#conditionals on output
x = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print(x)

#dict comprehensions- key and value are separated by a colon
pos_neg = {num: -num for num in range(9)}
print(pos_neg)

