import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas_datareader as pdr # Package and modules for importing data


start = datetime.datetime(2010,1,1)
end = datetime.date.today()

# Create a list of y-axis column names: y_columns
y_columns = ['AAPL', 'IBM']

# Generate a line plot
df.plot(x='Month', y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()