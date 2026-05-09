import requests

from app.config import Config
from app.utils.logger import logger


BASE_URL = (
    f"https://api.telegram.org/bot"
    f"{Config.TELEGRAM_TOKEN}"
)


def send_telegram(message):

    try:

        url = f"{BASE_URL}/sendMessage"

        payload = {
            "chat_id": Config.TELEGRAM_CHAT_ID,
            "text": message
        }

        response = requests.post(
            url,
            json=payload,
            timeout=10
        )

        logger.info(
            f"Telegram sent: {response.status_code}"
        )

        return response.json()

    except Exception as e:

        logger.error(
            f"Telegram send failed: {str(e)}"
        )

        return None