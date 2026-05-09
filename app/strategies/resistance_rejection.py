def evaluate_resistance_rejection(data):

    signal = data.get("signal")

    if signal != "RESISTANCE_REJECTION":
        return None

    price = float(data.get("price", 0))
    vwma = float(data.get("vwma", 0))

    below_vwma = price < vwma

    if not below_vwma:
        return None

    return {
        "strategy": "RESISTANCE_REJECTION",
        "trend": "bearish",
        "volume_spike": False,
        "above_vwma": False,
        "strong_close": True,
        "fakeout_risk": False,
        "weak_volume": False
    }