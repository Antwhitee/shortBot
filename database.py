import sqlite3


def init_db():
    conn = sqlite3.connect("trades.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            entry REAL,
            side TEXT
        )
    ''')

    conn.commit()
    conn.close()


def save_trade(symbol, entry, side):
    conn = sqlite3.connect("trades.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO trades (symbol, entry, side) VALUES (?, ?, ?)",
        (symbol, entry, side)
    )

    conn.commit()
    conn.close()
