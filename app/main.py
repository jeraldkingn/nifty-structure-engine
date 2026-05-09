import json
import sys

from app.core.rules import (
    evaluate_signal
)

from app.services.telegram_service import (
    send_telegram
)

from app.services.supabase_service import (
    save_alert
)

from app.utils.logger import logger


def process(payload):

    result = evaluate_signal(payload)

    if not result["allowed"]:

        logger.info(
            f"Rejected: {result['reason']}"
        )

        return

    

    from app.services.alert_service import (
    process_alert
    )

    process_alert(payload)
    logger.info("Processing completed")


if __name__ == "__main__":

    try:

        raw_payload = sys.argv[1]

        payload = json.loads(raw_payload)

        process(payload)

    except Exception as e:

        logger.error(
            f"Fatal error: {str(e)}"
        )