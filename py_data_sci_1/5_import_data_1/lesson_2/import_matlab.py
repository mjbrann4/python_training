#use sciPy package
import scipy.io

#read .mat files
scipy.io.loadmat()

#write .mat files
scipy.io.savemat()


filename = 'workspace.mat'
mat = scipy.io.loadmat(filename)

#returns type dict
print(type(mat))

print(type(mat['x']))


