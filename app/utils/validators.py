REQUIRED_FIELDS = [
    "signal",
    "price",
    "symbol"
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