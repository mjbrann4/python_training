import numpy as np
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

#how to plot
plt.plot(year, pop)

#actually displays the plot
#plt.show()

#scatter plot
plt.scatter(year, pop)
plt.show()
