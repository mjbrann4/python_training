#HDF5 becoming standard format for storing LARGE data files for python
import h5py

filename = 'H-H1_LOSC.hdf5'
data = h5py.File(filename, 'r')

print(type(data))

#each key is like a directory
for key in data.keys():
	print(key)

print(type(data['meta']))

for key in data['meta'].keys():
	print(key)

print(data['meta']['Description'].value, data['meta']['Detector'].value)

