REQUIRED_FIELDS = [
    "signal",
    "price",
    "volume",
    "avg_volume",
    "vwma",
    "ema20",
    "ema50",
    "atr",
    "stop_loss",
    "target"
]


def validate_payload(payload):

    missing = []

    for field in REQUIRED_FIELDS:
        if field not in payload:
            missing.append(field)

    return {
        "valid": len(missing) == 0,
        "missing": missing
    }