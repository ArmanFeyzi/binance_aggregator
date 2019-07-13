import time
import datetime
import json
from requests import get
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.Binance1
collection = db.Binance1

ip = get('http://ip-api.com/json')
ip = ip.json()

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

if(ip['countryCode'] == 'IR'):
    print("Turn on your VPN!")
else:
    tickers = get('https://api.binance.com/api/v3/ticker/price')
    tickers = tickers.json()
    for ticker in tickers:
        # print(st)
        pair = {"ticker": ticker['symbol'],
                "price": float(ticker['price']),
                "updatetime": st,
                }
        
        allTicker = db.allTicker
        allTicker_id = allTicker.insert_one(pair).inserted_id
