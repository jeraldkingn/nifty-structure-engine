def evaluate_support_bounce(data):

    signal = data.get("signal")

    if signal != "SUPPORT_BOUNCE":
        return None

    price = float(data.get("price", 0))
    vwma = float(data.get("vwma", 0))

    reclaimed_vwma = price > vwma

    if not reclaimed_vwma:
        return None

    return {
        "strategy": "SUPPORT_BOUNCE",
        "trend": "bullish",
        "volume_spike": False,
        "above_vwma": True,
        "strong_close": True,
        "fakeout_risk": False,
        "weak_volume": False
    }