#numpy for numeric data, pandas for data frames
import numpy as np
#import pandas

#numpy arrays are the standard for storing numerical data
filename = 'data/num.csv'
data = np.loadtxt(filename, delimiter=',')
print(data)

#if there is text data in first row then skip
data = np.loadtxt(filename, delimiter=',', skiprows=1)
print(data)

#import as strings 
data = np.loadtxt(filename, delimiter=',', dtype=str)
print(type(data))

#np.genfromtxt will allow for multiple data types
data2 = np.genfromtxt('data/seaslug.txt', delimiter='\t', dtype=None)
print(data2)
