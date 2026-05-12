from config import RISK_PER_TRADE


def calculate_position_size(equity, entry_price, stop_price):
    risk_amount = equity * RISK_PER_TRADE
    stop_distance = abs(entry_price - stop_price)

    if stop_distance == 0:
        return 0

    return risk_amount / stop_distance
