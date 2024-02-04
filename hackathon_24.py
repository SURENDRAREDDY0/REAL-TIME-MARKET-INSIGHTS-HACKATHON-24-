# -*- coding: utf-8 -*-
"""Hackathon 24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZaLa6cadJxxFKZ729mYg-2gS0NPAxERe
"""

import yfinance as yf
import datetime

def fetch_real_time_data(ticker, interval='1m', period='1d'):
    """
    Fetches real-time stock data from Yahoo Finance.

    Args:
    - ticker: str, the ticker symbol of the stock (e.g., 'AAPL' for Apple Inc.).
    - interval: str, the frequency of data (e.g., '1m' for 1 minute interval).
    - period: str, the time period to fetch data (e.g., '1d' for 1 day).

    Returns:
    - DataFrame, containing real-time stock data.
    """
    stock_data = yf.download(ticker, interval=interval, period=period)
    return stock_data

def analyze_market_insights(data):
    """
    Analyzes real-time stock data to provide insights.

    Args:
    - data: DataFrame, containing real-time stock data.

    Returns:
    - dict, containing market insights.
    """
    insights = {}

    # Example analysis: calculate moving average
    data['Moving_Average_5'] = data['Close'].rolling(window=5).mean()
    data['Moving_Average_20'] = data['Close'].rolling(window=20).mean()

    # Example insight: check if the latest close price is above the moving averages
    latest_close_price = data['Close'].iloc[-1]
    ma_5 = data['Moving_Average_5'].iloc[-1]
    ma_20 = data['Moving_Average_20'].iloc[-1]

    if latest_close_price > ma_5 and latest_close_price > ma_20:
        insights['Trend'] = 'Bullish'
    elif latest_close_price < ma_5 and latest_close_price < ma_20:
        insights['Trend'] = 'Bearish'
    else:
        insights['Trend'] = 'Neutral'

    return insights

# Example usage:
ticker_symbol = 'AAPL'
real_time_data = fetch_real_time_data(ticker_symbol)
market_insights = analyze_market_insights(real_time_data)
print("Real-time Market Insights for", ticker_symbol)
print(market_insights)