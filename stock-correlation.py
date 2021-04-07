import yfinance as yf
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Get user input
ticker_string = input("> Enter two or more tickers: ")

p = input('> Enter time period: ')

# Get Elements from String
ticker_arr = ticker_string.split()

# Move elements into DataFrame
df = pd.DataFrame()

for t in ticker_arr:
    a = yf.Ticker(t).history(period=p)
    df[t] = a['Open']

# Scale data
scale = StandardScaler()

data = pd.DataFrame(scale.fit_transform(df))

data.columns = ticker_arr

# Print Correlation
print(data.corr())

# Plot data
data.plot(figsize=(8, 4), lw=2)
