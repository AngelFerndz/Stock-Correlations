# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:21:52 2020

@author: angel
"""

import yfinance as yf
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Set features
print('-- Stock Correlation Finder --')

# Get user input
ticker_string = input("> Enter two or more tickers: ")
p = input('> Enter time period [1mo, max] : ')
col = input("> Chose data [Close, Open, High, Low, Volume]: ")

# Get data
ticker_arr = ticker_string.split()
df = pd.DataFrame()
print("------------------------------------------- Correlations")

for t in ticker_arr:
    a = yf.Ticker(t).history(period=p)
    df[t] = a[col]
    
# Scale data
scale = StandardScaler()
data = pd.DataFrame(scale.fit_transform(df))
data.columns = ticker_arr

# Calculate correlation    
corr = data.corr()
print(corr)

# Plot data
plot = input("> Plot data? [y, n]: ")

if plot == 'y':
    data.plot(title='Correlation period {}'.format(p), figsize=(10,5), lw=2)

# Save data
save = input("> Save as csv file? [y, n]: ")

if save == 'y':
    corr.to_csv('Correlation {}.csv'.format(ticker_string))
    print("> File saved")
