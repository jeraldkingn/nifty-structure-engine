import yfinance as yf
import pandas as pd


def fetch_nifty_data():

    df = yf.download(
        "^NSEI",
        interval="5m",
        period="2d",
        progress=False
    )

    df.dropna(inplace=True)

    return df

def calculate_indicators(df):

    df["VWMA"] = (
        (df["Close"] * df["Volume"])
        .rolling(20)
        .sum()
        /
        df["Volume"].rolling(20).sum()
    )

    df["AvgVolume"] = (
        df["Volume"]
        .rolling(20)
        .mean()
    )

    return df

def detect_signal(df):

    latest = df.iloc[-1]

    today_high = df["High"].max()
    today_low = df["Low"].min()

    breakout = (
        latest["Close"] > today_high and
        latest["Close"] > latest["VWMA"] and
        latest["Volume"] > latest["AvgVolume"] * 1.5
    )

    breakdown = (
        latest["Close"] < today_low and
        latest["Close"] < latest["VWMA"] and
        latest["Volume"] > latest["AvgVolume"] * 1.5
    )

    if breakout:

        return {
            "signal": "BREAKOUT",
            "price": float(latest["Close"]),
            "volume": float(latest["Volume"]),
            "vwma": float(latest["VWMA"]),
            "confidence": 75,
            "market_bias": "BULLISH",
            "message": "NIFTY breakout above intraday resistance with strong volume"
        }

    if breakdown:

        return {
            "signal": "BREAKDOWN",
            "price": float(latest["Close"]),
            "volume": float(latest["Volume"]),
            "vwma": float(latest["VWMA"]),
            "confidence": 75,
            "market_bias": "BEARISH",
            "message": "NIFTY breakdown below intraday support with strong volume"
        }

    return None