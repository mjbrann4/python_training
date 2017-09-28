#visualize in pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas_datareader as pdr # Package and modules for importing data


#aapl = pd.read_csv('aapl.csv', index_col='date', parse_dates=True)

# Examine stock prices over the last year
start = datetime.datetime(2010,1,1)
end = datetime.date.today()

# AAPL stock data
# Args: series, start date, end date
aapl = pdr.get_data_yahoo('aapl', start, end)
print(aapl.head())
print(aapl.shape)

# create numpy array with values attribute
close_arr = aapl['Close'].values
print(type(close_arr))

plt.plot(close_arr)
plt.show()

# plot pandas series directly with date-time index labels
close_series = aapl['Close']
plt.plot(close_series)
plt.show()

# even better way
close_series.plot() #plot series directly
plt.savefig('graphs/aapl.png')
plt.show()

# dataframe has plot method as well
# use log y scale to fix issues
aapl.plot(subplots=True)
#plt.yscale('log') # logarithmic scale on vertical axis
plt.show()









