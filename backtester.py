import pandas as pd


class Backtester:
    def __init__(self, df, initial_balance=10000):
        self.df = df
        self.balance = initial_balance
        self.initial_balance = initial_balance
        self.trades = []

    def run(self, signal_function):
        position = None

        for i in range(60, len(self.df)):
            window = self.df.iloc[:i].copy()
            row = self.df.iloc[i]

            if position is None:
                if signal_function(window):
                    entry = row["close"]
                    stop = entry * 1.015
                    take_profit = entry * 0.96

                    position = {
                        "entry": entry,
                        "stop": stop,
                        "take_profit": take_profit,
                        "entry_index": i,
                    }

            else:
                price = row["close"]

                exit_reason = None
                exit_price = None

        }
