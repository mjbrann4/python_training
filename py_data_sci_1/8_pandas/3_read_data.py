
filepath = 'data/sunspot.csv'

# set col names
col_names = ['year', 'month', 'day', 'dec_date', 'sunspots', 'definite']

# header=None will read data without a header
# names=col_names will assign column names
# na_values=-1 will assign -1 as null
sunspots = pd.read_csv(filepath, header=None, names=col_names, na_values='-1')

# rows 10-20
sunspots.iloc[10:20, :]

# can pass list or dict for null values
# parse dates option for date cols will concat dates
sunspots = pd.read_csv(filepath, header=None, 
    names=col_names, 
    na_values={'sunspots': ['-1']},
    parse_dates=[[0,1,2]])

# using dates as an index
sunspots.index = sunspots['year_month_day']

# change label of index
sunspots.index.name = 'date'

# trim redundant cols
cols = ['sunspots', 'definite']
sunspots = sunspots[cols]

# write csv
out_csv = 'sunspots.csv'
sunspots.to_csv(out_csv)

# write xlsx
sunspots.to_excel('sunspots.xlsx')