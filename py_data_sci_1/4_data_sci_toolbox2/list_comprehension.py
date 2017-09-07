#can do operations on lists in one line of code instead of a for loop
#Components:
#	Iterable
#	Iterator variable (represent members of iterable)
#	Output expression

nums = [12, 8, 21, 3, 16]
new_nums = [num + 1 for num in nums]
print(new_nums)

#can do list comprehension over any iterable
result = [num for num in range(11)]
print(result)

#in place of nexted loops eg below
pairs_1 = []
for num1 in range(0, 2):
	for num2 in range(6, 8):
		t = (num1, num2)
		pairs_1.append(t)

print(pairs_1)

pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
print(pairs_2)

# Create a 5 x 5 matrix using a list of lists: matrix
#pass output into next list
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)
