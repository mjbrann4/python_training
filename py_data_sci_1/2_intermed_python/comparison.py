import numpy as np

#can compare strings alphabetically
print("carl" < "chris")

#can return array of booleans- numpy creates an array of 23s and compares
bmi = np.array([22, 24, 21.2, 19.5, 23.5, 21.7])
print(bmi>23)

#in python and, or, not are useable
print(not True)

#does not work!
#print(bmi > 21 and bmi < 22)


#for numpy you can use logical_and, logical_or, and logical_not
print(np.logical_and(bmi > 21, bmi < 22))
print(np.logical_or(bmi > 23, bmi < 20))

#can subset a np array using this
x = bmi[np.logical_and(bmi > 21, bmi <22)]
print(x)