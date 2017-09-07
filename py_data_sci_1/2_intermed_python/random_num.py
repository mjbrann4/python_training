import numpy as np
import matplotlib.pyplot as plt
#random num generator
print(np.random.rand())

#can set seed
np.random.seed(123)
print(np.random.rand())

#0/1 random int
#coin = np.random.randint(0,2)


#a random walk of tails
tails = [0]
for x in range(10):
	coin = np.random.randint(0,2)
	tails.append(tails[x] + coin)

#print(tails)


#multiple random walks
final_tails = []
for x in range(10000):
	tails = [0]
	for x in range(10):
		coin = np.random.randint(0,2)
		tails.append(tails[x] + coin)
	final_tails.append(tails[-1])

#this is a distribution
#print(final_tails)

plt.hist(final_tails, bins=10)
plt.show()

print(np.mean(final_tails))
print(np.median(final_tails))



