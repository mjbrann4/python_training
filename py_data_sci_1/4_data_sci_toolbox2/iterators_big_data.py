#pulling data from a database or API and there is too much to hold in memory
#solution- load data in chunks and then use it and discard and get next chunk
#use chunksize argument in read_csv()

import pandas as pd
result = []
#object created by read csv is an iterable
for chunk in pd.read_csv('data/OD_data.csv', chunksize=100):
	result.append(sum(chunk['rate']))

print(result)
total = sum(result)
print(total)

#alternatively
total = 0
for chunk in pd.read_csv('data/OD_data.csv', chunksize=100):
	total += sum(chunk['rate'])

print(total)


#reusable iterator function!

# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)




