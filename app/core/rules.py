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
    vwma_state
):

    return f"""
⚠️ {signal}

Strategy: {strategy}

Price: {price}

VWMA: {vwma_state}

Volume: {volume_state}

Market State: {market_state}

Confidence: {confidence}%
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
        if "bullish" in market_state
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
        vwma_state=vwma_state
    )

    result = {
        "allowed": True,
        "signal": signal,
        "price": payload.get("price"),
        "confidence": confidence,
        "market_bias": market_bias,
        "message": message,
        "market_state": market_state,
        "strategy": classified["strategy"]
    }

    return result

    logger.info(
        f"Received payload: {payload}"
    )

    # Validate payload
    validation = validate_payload(payload)

    if not validation["valid"]:

        logger.error(
            f"Invalid payload: {validation}"
        )

        return {
            "allowed": False,
            "reason": "invalid_payload"
        }

    # Classify strategy
    classified = classify_strategy(payload)

    if not classified:

        logger.info(
            "No valid strategy detected"
        )

        return {
            "allowed": False,
            "reason": "no_strategy"
        }

    signal = payload.get("signal")

    # Cooldown
    if not can_send_alert(signal):

        logger.info(
            f"Cooldown active for {signal}"
        )

        return {
            "allowed": False,
            "reason": "cooldown_active"
        }

    # Market state
    payload["volume_spike"] = (
        classified["volume_spike"]
    )

    market_state = detect_market_state(
        payload
    )

    # Confidence
    classified["trend"] = market_state

    confidence = calculate_confidence(
        classified
    )

    # Confidence filter
    if confidence < Config.MIN_CONFIDENCE:

        logger.info(
            f"Low confidence: {confidence}"
        )

        return {
            "allowed": False,
            "reason": "low_confidence"
        }

    # Market bias
    market_bias = (
        "Bullish"
        if "bullish" in market_state
        else "Bearish"
    )

    # Volume state
    volume_state = (
        "Strong"
        if classified["volume_spike"]
        else "Moderate"
    )

    # VWMA state
    vwma_state = (
        "Above"
        if classified["above_vwma"]
        else "Below"
    )

    # Telegram message
    message = build_message(
        signal=signal,
        strategy=classified["strategy"],
        price=payload.get("price"),
        confidence=confidence,
        market_state=market_state,
        volume_state=volume_state,
        vwma_state=vwma_state
    )

    logger.info(
        f"Signal approved: {signal}"
    )

    return {
        "allowed": True,
        "signal": signal,
        "price": payload.get("price"),
        "confidence": confidence,
        "market_bias": market_bias,
        "message": message,
        "market_state": market_state,
        "strategy": classified["strategy"]
    }