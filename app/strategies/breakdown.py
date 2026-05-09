def evaluate_breakdown(data):

    signal = data.get("signal")

    if signal != "BREAKDOWN":
        return None

    price = float(data.get("price", 0))
    vwma = float(data.get("vwma", 0))

    volume = float(data.get("volume", 0))
    avg_volume = float(data.get("avg_volume", volume))

    volume_spike = volume > (avg_volume * 1.5)

    conditions_met = (
        price < vwma and
        volume_spike
    )

    if not conditions_met:
        return None

    return {
        "strategy": "TODAY_LOW_BREAKDOWN",
        "trend": "bearish",
        "volume_spike": volume_spike,
        "above_vwma": False,
        "strong_close": True,
        "fakeout_risk": False,
        "weak_volume": False
    }