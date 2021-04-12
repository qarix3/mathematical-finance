import numpy as np
import pandas as pd
import matplotlib as plt
import yfinance as yf

tickers = []
expected_growth_rate = -1
margin_safety = .10
growth_decline_rate = .05
discount_rate = .09
DCF_year_projection = 5
long_term_growth_rate = .03

# Get financial statement data of the ticker for the past 4 years
ticker = yf.Ticker('aapl')