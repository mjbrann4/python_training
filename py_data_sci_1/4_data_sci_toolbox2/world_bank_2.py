#generators for large data limit
#generators work on streaming data-
#read and process the file until all lines are exhausted

#Use generator function to count countries
#-------------------------------------------
# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data
        
# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('data/WDI_csv/WDIData.csv') as file:

    # Iterate over the generator from read_large_file
    for line in read_large_file(file):
    	row = line.split(',')
    	first_col = row[0]

    	if first_col in counts_dict.keys():
    		counts_dict[first_col] += 1
    	else:
    		counts_dict[first_col] = 1

print(counts_dict)


