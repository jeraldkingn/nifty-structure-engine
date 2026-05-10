from app.services.supabase_service import (
    save_alert
)

from app.services.telegram_service import (
    send_telegram
)

from app.utils.logger import logger


def process_alert(result):

    try:

        alert_data = {
            "signal": result["signal"],
            "price": result["price"],
            "confidence": result["confidence"],
            "market_bias": result["market_bias"],
            "message": result["message"],
            "stop_loss": result["stop_loss"],
            "target": result["target"]
        }

        save_alert(alert_data)

        send_telegram(result["message"])

        logger.info(
            "Alert processed successfully"
        )

    except Exception as e:

        logger.error(
            f"Alert processing failed: {str(e)}"
        )