import numpy as np 

file = 'data/seaslug.txt'

data = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)
print(data)

