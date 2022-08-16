import os
from dotenv import load_dotenv
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import urllib.request, json
import numpy as np
import tensorflow as tf # This code has been tested with TensorFlow 1.6
from sklearn.preprocessing import MinMaxScaler

load_dotenv()
api_key = os.getenv('API_KEY')

ticker = 'TSLA' #Tesla

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s"%(ticker,api_key)
file_save = 'stock_market_data-%s.csv'%ticker
