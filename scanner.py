import ccxt

exchange = ccxt.binance({
    "options": {"defaultType": "future"}
})


def get_symbols():
    markets = exchange.load_markets()
    return [
        symbol for symbol in markets
        if symbol.endswith("USDT") and markets[symbol]["active"]
    ]


def fetch_ohlcv(symbol, timeframe="1m", limit=100):
    return exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
