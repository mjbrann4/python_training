import matplotlib.pyplot as plt 
import numpy as np

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)

plt.hist(height, bins = 20)
plt.show()
plt.clf()

plt.hist(height, bins = 10)
plt.show()
plt.clf()
