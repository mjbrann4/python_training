import pandas as pd
import numpy as np

df = pd.read_csv('data/weather_data_austin_2010.csv', parse_dates=True, index_col='Date')
print(df.head())


# Filtering time series data

