from app.services.market_scanner import (
    fetch_nifty_data,
    calculate_indicators,
    detect_signal
)

from app.services.alert_service import (
    process_alert
)


def run_scanner():

    df = fetch_nifty_data()

    df = calculate_indicators(df)

    signal = detect_signal(df)

    if signal:

        process_alert(signal)

        print("Signal sent:", signal)

    else:

        print("No signal detected")


if __name__ == "__main__":

    run_scanner()