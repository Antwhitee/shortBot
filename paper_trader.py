open_positions = []


def open_short(symbol, entry):
    position = {
        "symbol": symbol,
        "entry": entry,
        "side": "short"
    }
    open_positions.append(position)
    print("OPEN SHORT:", position)
    return position
