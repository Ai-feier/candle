from xmlrpc.server import list_public_methods

from binance.spot import Spot
import os

from behave.model import Candles

"""
[
  [
    1499040000000,      // Kline open time
    "0.01634790",       // Open price
    "0.80000000",       // High price
    "0.01575800",       // Low price
    "0.01577100",       // Close price
    "148976.11427815",  // Volume
    1499644799999,      // Kline close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    "0"                 // Unused field. Ignore.
  ]
]"""



if __name__ == "__main__":
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    # 创建Spot客户端实例
    client = Spot(api_key=api_key, api_secret=api_secret)

    data = client.klines("BTCUSDT", "5m", limit=10)
    candles = Candles(data)
    print(candles.convert_to_3_line().convert_to_3_line())