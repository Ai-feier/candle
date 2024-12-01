from binance.spot import Spot
import os

# 从环境变量中读取API密钥和密钥
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')

print(api_key, api_secret)


# 创建Spot客户端实例
client = Spot(api_key=api_key, api_secret=api_secret)


# Get server timestamp
print(client.time())
# Get klines of BTCUSDT at 1m interval
print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(client.klines("BNBUSDT", "1h", limit=10))


# Get account and balance information
print(client.account())

# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 9500
}

response = client.new_order(**params)
print(response)