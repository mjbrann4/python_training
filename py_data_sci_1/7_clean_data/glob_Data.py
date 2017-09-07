#globbing is pattern matching for file names
#use wildcards to match file names
# * is wildcard for all eg *.csv
# ? is wildcard for single character eg file_?.csv

#returns a list of filenames, which we can loop through

import glob
import pandas as pd

pattern = 'data/*.csv'
csv_files = glob.glob(pattern)
print(csv_files)

#create list of dataframe
list_data = []
for filename in csv_files:
	data = pd.read_csv(filename)
	list_data.append(data)

z = pd.concat(list_data)
