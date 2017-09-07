#enumerate() takes an iterable as an argument and returns enumerate object
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
e = enumerate(avengers)
print(type(e))

#will enumerate object into list of tuples
e_list = list(e)
print(e_list)

#can unpack in a loop
for index, value in enumerate(avengers):
	print(index, value)

for index, value in enumerate(avengers, start=10):
	print(index, value)


#using zip will create a zip object (an iterator of tuples)
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']

z = zip(avengers, names)
print(type(z))

z_list = list(z)
print(z_list)

#or use a for loop to unpack the zip object and print tuples
for z1, z2 in zip(avengers, names):
	print(z1, z2)

#can also use splat to unpack
print(*z)

#note these still iterate and you reach end EG
z = zip(avengers, names)
print(*z)
print(*z)

