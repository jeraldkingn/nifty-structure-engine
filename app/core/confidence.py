def calculate_confidence(data):

    score = 50

    # VWMA alignment
    if data.get("above_vwma"):
        score += 15

    # Volume confirmation
    if data.get("volume_spike"):
        score += 20

    # Trend confirmation
    if data.get("trend") == "bullish":
        score += 10

    if data.get("trend") == "bearish":
        score += 10

    # Strong candle body
    if data.get("strong_close"):
        score += 10

    # Fakeout penalty
    if data.get("fakeout_risk"):
        score -= 15

    # Weak volume penalty
    if data.get("weak_volume"):
        score -= 10

    # Clamp
    score = max(score, 0)
    score = min(score, 100)

    return score