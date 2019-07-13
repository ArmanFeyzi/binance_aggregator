# Binance historical data aggregator OHLCV
## Get dynamic all data in diffrent candles time-frame
Save historical ticker price in different time-frame from Binance exchange to MongoDB database

### How to use:
1. Save All Binance Market Symbol

`python getAllTicker.py`

2. Run Agregator by parameter

`python save_historical_data.py 1d 50`

Parameters help:
The first parameter is candel size, in this example `1d` equal to "1 Day" candlestick size
Valid type for first parameter is: ['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M']

The Second parameter is count of candlesticks do you want to save
