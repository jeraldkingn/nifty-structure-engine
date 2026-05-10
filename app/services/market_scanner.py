import yfinance as yf
import pandas as pd
import time


def fetch_nifty_data():

    for attempt in range(3):

        try:

            print(f"Fetching market data... Attempt {attempt + 1}")

            df = yf.download(
                "^NSEI",
                interval="5m",
                period="2d",
                progress=False
            )

            if df.empty:

                print("No data received")

                time.sleep(3)

                continue

            if isinstance(df.columns, pd.MultiIndex):

                df.columns = df.columns.get_level_values(0)

            print(f"Rows fetched: {len(df)}")

            return df

        except Exception as e:

            print(f"Fetch attempt failed: {e}")

            time.sleep(3)

    return None


def calculate_indicators(df):

    # VWMA
    df["VWMA"] = (
        (df["Close"] * df["Volume"])
        .rolling(20)
        .sum()
        /
        df["Volume"].rolling(20).sum()
    )

    # Average Volume
    df["AvgVolume"] = (
        df["Volume"]
        .rolling(20)
        .mean()
    )

    # EMA Trend Filters
    df["EMA20"] = (
        df["Close"]
        .ewm(span=20, adjust=False)
        .mean()
    )

    df["EMA50"] = (
        df["Close"]
        .ewm(span=50, adjust=False)
        .mean()
    )

    # ATR Volatility
    df["ATR"] = (
        df["High"] - df["Low"]
    ).rolling(14).mean()

    df = df.dropna()

    return df


def detect_signal(df):

    if len(df) < 2:
        return None

    latest = df.iloc[-1]

    previous = df.iloc[-2]

    today_high = df.iloc[:-1]["High"].max()

    today_low = df.iloc[:-1]["Low"].min()

    breakout = (

        latest["Close"] > today_high and

        latest["Close"] > previous["High"] and

        previous["Close"] < today_high and

        latest["Close"] > latest["VWMA"] and

        latest["EMA20"] > latest["EMA50"] and

        latest["Volume"] > latest["AvgVolume"] * 1.5 and

        (
            latest["Close"] - previous["High"]
        ) > latest["ATR"] * 0.3

    )

    breakdown = (

        latest["Close"] < today_low and

        latest["Close"] < previous["Low"] and

        previous["Close"] > today_low and

        latest["Close"] < latest["VWMA"] and

        latest["EMA20"] < latest["EMA50"] and

        latest["Volume"] > latest["AvgVolume"] * 1.5 and

        (
            previous["Low"] - latest["Close"]
        ) > latest["ATR"] * 0.3

    )

    if breakout:

        stop_loss = float(previous["Low"])

        risk = latest["Close"] - stop_loss

        target = latest["Close"] + (risk * 2)

        return {
            "signal": "BREAKOUT",
            "price": float(latest["Close"]),
            "volume": float(latest["Volume"]),
            "vwma": float(latest["VWMA"]),
            "ema20": float(latest["EMA20"]),
            "ema50": float(latest["EMA50"]),
            "atr": float(latest["ATR"]),
            "stop_loss": round(stop_loss, 2),
            "target": round(target, 2)
        }

    if breakdown:

        stop_loss = float(previous["High"])

        risk = stop_loss - latest["Close"]

        target = latest["Close"] - (risk * 2)

        return {
            "signal": "BREAKDOWN",
            "price": float(latest["Close"]),
            "volume": float(latest["Volume"]),
            "vwma": float(latest["VWMA"]),
            "ema20": float(latest["EMA20"]),
            "ema50": float(latest["EMA50"]),
            "atr": float(latest["ATR"]),
            "stop_loss": round(stop_loss, 2),
            "target": round(target, 2)
        }

    return None