import pandas as pd
import ta


def build_features(ohlcv):
    df = pd.DataFrame(
        ohlcv,
        columns=["ts", "open", "high", "low", "close", "volume"]
    )

    df["rsi"] = ta.momentum.RSIIndicator(df["close"], 14).rsi()
    df["ema20"] = df["close"].ewm(span=20).mean()

    df["vwap"] = (
        (df["close"] * df["volume"]).cumsum()
        / df["volume"].cumsum()
    )

    return df
