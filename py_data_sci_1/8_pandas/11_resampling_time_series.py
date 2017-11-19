import pandas as pd
import numpy as np

df = pd.read_csv('data/weather_data_austin_2010.csv', parse_dates=True, index_col='Date')
print(df.head())

# statistical methods over different time intervals
# downsampling - reduce datetime rows to slower frequency eg daily to weekly
# upsampling - expand slower frequency to faster freq

# Aggregate to daily means
daily_mean = df.resample('D').mean()
print(daily_mean.head())

print(daily_mean.loc['2010-03-21'])

# Aggregate to monthly sum
daily_sum = df.resample('M').sum()
print(daily_sum.head())

# Method chaining - hottest day of the year overall
print(df.resample('D').mean().max())

# Resampling strings - weekly counts
print(df.resample('W').count())

# resampling strings- 'min', 'T', 'H', 'D', 'B', etc

# you can use multiples of these
df.resample('2W').sum()

# Upsampling (interpolation):
two_days = df.loc['2010-04-04': '2010-04-06', 'Temperature'].resample('D').mean()
print(two_days)

# resample every 4 hours and fill in
print(two_days.resample('4H').ffill())

# rolling() method
unsmoothed = df['Temperature']['2010-08-01':'2010-08-15']
smoothed = unsmoothed.rolling(window=24).mean()

print(smoothed)


august = df['Temperature'].loc['2010-08']
# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = august.resample('D').max().rolling(window=7).mean()
print(daily_highs_smoothed)

