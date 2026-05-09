def detect_market_state(data):

    price = float(data.get("price", 0))
    vwma = float(data.get("vwma", 0))

    volume_spike = data.get("volume_spike", False)

    if price > vwma:

        if volume_spike:
            return "bullish_trend"

        return "bullish"

    if price < vwma:

        if volume_spike:
            return "bearish_trend"

        return "bearish"

    return "range"