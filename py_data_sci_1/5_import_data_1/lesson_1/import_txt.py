filename = 'words.txt'
file = open(filename, mode='r')
text = file.read()

#print(text)

file.close()

#use with as a context manager- best practice
with open('words.txt', 'r') as file:
	#readline prints first line
	print(file.readline(3))
	print(file.readline())
	#print(file.read())