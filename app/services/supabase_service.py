from supabase import create_client

from app.config import Config
from app.utils.logger import logger


supabase = create_client(
    Config.SUPABASE_URL,
    Config.SUPABASE_KEY
)


def save_alert(alert_data):

    try:

        response = (
            supabase
            .table("alerts")
            .insert(alert_data)
            .execute()
        )

        logger.info("Alert saved")

        return response

    except Exception as e:

        logger.error(
            f"Save alert failed: {str(e)}"
        )

        return None


def save_market_snapshot(snapshot_data):

    try:

        response = (
            supabase
            .table("market_snapshots")
            .insert(snapshot_data)
            .execute()
        )

        logger.info("Snapshot saved")

        return response

    except Exception as e:

        logger.error(
            f"Save snapshot failed: {str(e)}"
        )

        return None


def save_market_state(state_data):

    try:

        response = (
            supabase
            .table("market_state")
            .insert(state_data)
            .execute()
        )

        logger.info("Market state saved")

        return response

    except Exception as e:

        logger.error(
            f"Save market state failed: {str(e)}"
        )

        return None