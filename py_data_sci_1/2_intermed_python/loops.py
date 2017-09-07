
#while condition:
	#expression

#example
error = 50
while error > 1:
	error = error / 4
	print(error)

#basic for loop- no access to index tho
fam = [1.73, 1.68, 1.71, 1.89]

for height in fam:
	print(height)

#access index with enumerate
for index, height in enumerate(fam):
	print("index " + str(index) + ": " + str(height))

#can loop over string a well
for c in "family":
	print(c.capitalize())


