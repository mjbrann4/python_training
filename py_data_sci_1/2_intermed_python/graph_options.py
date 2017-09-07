import numpy as np
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010, 2030]
pop = [2.519, 3.692, 5.263, 6.972, 7.8]

#how to plot
plt.plot(year, pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],
			['0', '2B', '4B', '6B', '8B', '10B'])

plt.show()

