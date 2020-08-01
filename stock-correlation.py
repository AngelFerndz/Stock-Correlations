# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:21:52 2020

@author: angel
"""

import yfinance as yf
import pandas as pd
from sklearn.preprocessing import StandardScaler

# set features
print('- Stock Correlation Finder -')
tickers = input("> Enter ticker to find correlation : ").split()
p = input('> Enter time period [1mo, 1day, max] : ')

print("------------------------------------------- Correlations")

df = pd.DataFrame()

# gather data
for t in tickers:
    a = yf.Ticker(t).history(period=p)
    df[t] = a['Close']
    
# scale data
scale = StandardScaler()
data = pd.DataFrame(scale.fit_transform(df))
data.columns = tickers

# plot data
data.plot(title='Correlation Period {}'.format(p), figsize=(10,5), lw=2)
corr = data.corr()

print(corr)
