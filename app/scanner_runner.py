from datetime import datetime
import pytz

from app.core.rules import evaluate_signal
from app.services.market_scanner import (
    fetch_nifty_data,
    calculate_indicators,
    detect_signal
)

from app.services.alert_service import (
    process_alert
)


def is_market_hours():

    ist = pytz.timezone("Asia/Kolkata")

    now = datetime.now(ist)

    current_minutes = now.hour * 60 + now.minute

    market_open = (9 * 60) + 15
    market_close = (15 * 60) + 30

    return market_open <= current_minutes <= market_close


def run_scanner():

    # if not is_market_hours():

    #     print("Outside market hours")

    #     return

    try:

        df = fetch_nifty_data()

        if df is None or df.empty:

            print("No market data fetched")

            return

        df = calculate_indicators(df)

        # signal = detect_signal(df)
        signal = {
            "signal": "BREAKOUT",
            "price": 24220,
            "volume": 150000,
            "avg_volume": 90000,
            "vwma": 24190,
            "ema20": 24200,
            "ema50": 24150,
            "atr": 40,
            "stop_loss": 24150,
            "target": 24360
        }

        if signal:

            result = evaluate_signal(signal)

            if result["allowed"]:

                process_alert(result)

                print("Signal sent:", result)

            else:

                print("Signal rejected:", result["reason"])

        else:

            print("No signal detected")

    except Exception as e:

        print(f"Scanner error: {e}")


if __name__ == "__main__":

    run_scanner()