from scanner import get_symbols, fetch_ohlcv
from features import build_features
from signals import detect_signal
from paper_trader import open_short
from database import init_db, save_trade
from backtester import Backtester


def run_live_scan():
    init_db()
    symbols = get_symbols()

    for symbol in symbols:
        try:
            data = fetch_ohlcv(symbol)
            df = build_features(data)

            if detect_signal(df):
                price = df.iloc[-1]["close"]
                open_short(symbol, price)
                save_trade(symbol, price, "short")

        except Exception as e:
            print(symbol, e)


def run_backtest(symbol="BTC/USDT"):
    data = fetch_ohlcv(symbol, limit=500)
    df = build_features(data)

    bt = Backtester(df)
    bt.run(detect_signal)

    print(bt.stats())


    run_backtest()
