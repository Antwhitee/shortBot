from config import (
    PUMP_THRESHOLD_15M,
    VOLUME_RATIO_THRESHOLD,
    RSI_THRESHOLD,
    VWAP_DISTANCE_THRESHOLD,
)


def detect_signal(df):
    if len(df) < 60:
        return False

    latest = df.iloc[-1]
    prev_15 = df.iloc[-15]

    price_change = (
        latest["close"] - prev_15["close"]
    ) / prev_15["close"]

    volume_ratio = (
        df["volume"].tail(5).mean()
        / df["volume"].tail(60).mean()
    )

    vwap_distance = (
        latest["close"] - latest["vwap"]
    ) / latest["vwap"]

    conditions = [
        price_change > PUMP_THRESHOLD_15M,
        volume_ratio > VOLUME_RATIO_THRESHOLD,
        latest["rsi"] > RSI_THRESHOLD,
        vwap_distance > VWAP_DISTANCE_THRESHOLD,
    ]

    return all(conditions)
