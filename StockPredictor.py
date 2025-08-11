import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import datetime

# Download stock data
ticker = "AAPL"
data = yf.download(ticker, start="2020-01-01", end=datetime.datetime.today().strftime('%Y-%m-%d'))

# Prepare data
data['Date'] = data.index
data['Days'] = np.arange(len(data))

X = np.array(data['Days']).reshape(-1, 1)
y = np.array(data['Close'])

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next day
next_day = np.array([[len(data) + 1]])
predicted_price = model.predict(next_day)

print(f"Predicted next day closing price for {ticker}: ${predicted_price[0]:.2f}")
