from app.config import Config

from app.utils.validators import (
    validate_payload
)

from app.utils.logger import logger

from app.core.classifiers import (
    classify_strategy
)

from app.core.confidence import (
    calculate_confidence
)

from app.core.market_state import (
    detect_market_state
)

from app.core.cooldown import (
    can_send_alert
)


def build_message(
    signal,
    strategy,
    price,
    confidence,
    market_state,
    volume_state,
    vwma_state,
    stop_loss,
    target
):

    return f"""
⚠️ {signal}

Strategy: {strategy}

Price: {round(price, 2)}

VWMA: {vwma_state}

Volume: {volume_state}

Market State: {market_state}

Confidence: {confidence}%

SL: {round(stop_loss, 2)}

Target: {round(target, 2)}
"""


def evaluate_signal(payload):

    logger.info(
        f"Received payload: {payload}"
    )

    validation = validate_payload(payload)

    if not validation["valid"]:

        return {
            "allowed": False,
            "reason": "invalid_payload"
        }

    classified = classify_strategy(payload)

    if not classified:

        return {
            "allowed": False,
            "reason": "no_strategy"
        }

    signal = payload.get("signal")

    if not can_send_alert(signal):

        return {
            "allowed": False,
            "reason": "cooldown_active"
        }

    payload["volume_spike"] = (
        classified["volume_spike"]
    )

    market_state = detect_market_state(
        payload
    )

    classified["trend"] = market_state

    confidence = calculate_confidence(
        classified
    )

    if confidence < Config.MIN_CONFIDENCE:

        return {
            "allowed": False,
            "reason": "low_confidence"
        }

    market_bias = (
        "Bullish"
        if "bullish" in market_state.lower()
        else "Bearish"
    )

    volume_state = (
        "Strong"
        if classified["volume_spike"]
        else "Moderate"
    )

    vwma_state = (
        "Above"
        if classified["above_vwma"]
        else "Below"
    )

    message = build_message(
        signal=signal,
        strategy=classified["strategy"],
        price=payload.get("price"),
        confidence=confidence,
        market_state=market_state,
        volume_state=volume_state,
        vwma_state=vwma_state,
        stop_loss=payload.get("stop_loss", 0),
        target=payload.get("target", 0)
    )

    result = {
        "allowed": True,
        "signal": signal,
        "price": payload.get("price"),
        "confidence": confidence,
        "market_bias": market_bias,
        "message": message,
        "market_state": market_state,
        "strategy": classified["strategy"],
        "stop_loss": payload.get("stop_loss", 0),
        "target": payload.get("target", 0)
    }

    return result