import json
import sys

from app.core.rules import (
    evaluate_signal
)

from app.services.alert_service import (
    process_alert
)

from app.utils.logger import logger


def process(payload):

    result = evaluate_signal(payload)

    if not result["allowed"]:

        logger.info(
            f"Rejected: {result['reason']}"
        )

        return

    process_alert(result)

    logger.info("Processing completed")


if __name__ == "__main__":

    try:

        raw_payload = sys.argv[1]

        print(raw_payload)

        try:

            payload = json.loads(raw_payload)

        except json.JSONDecodeError:

            # PowerShell fallback parser
            fixed = (
                raw_payload
                .replace("{", '{"')
                .replace(":", '":"')
                .replace(",", '","')
                .replace("}", '"}')
            )

            fixed = fixed.replace('""', '"')

            payload = json.loads(fixed)

        process(payload)

    except Exception as e:

        logger.error(
            f"Fatal error: {str(e)}"
        )