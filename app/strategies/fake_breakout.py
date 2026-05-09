def evaluate_fake_breakout(data):

    signal = data.get("signal")

    if signal != "FAKE_BREAKOUT":
        return None

    return {
        "strategy": "FAKE_BREAKOUT",
        "trend": "range",
        "volume_spike": False,
        "above_vwma": False,
        "strong_close": False,
        "fakeout_risk": True,
        "weak_volume": True
    }