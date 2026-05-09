from app.services.supabase_service import (
    save_market_snapshot,
    save_market_state
)

from app.models.snapshot import Snapshot

from app.models.market_state import (
    MarketState
)

from app.utils.logger import logger


def create_market_snapshot(payload):

    try:

        snapshot = Snapshot(
            symbol=payload.get("symbol"),
            price=payload.get("price"),
            today_high=payload.get("today_high"),
            today_low=payload.get("today_low"),
            vwma=payload.get("vwma"),
            trend=payload.get("trend"),
            volume_state=payload.get(
                "volume_state"
            )
        )

        save_market_snapshot(
            snapshot.to_dict()
        )

        logger.info(
            "Market snapshot saved"
        )

    except Exception as e:

        logger.error(
            f"Snapshot save failed: {str(e)}"
        )


def create_market_state(payload):

    try:

        market_state = MarketState(
            symbol=payload.get("symbol"),
            trend=payload.get("trend"),
            volatility=payload.get(
                "volatility",
                "normal"
            ),
            bias=payload.get("bias"),
            active_resistance=payload.get(
                "active_resistance"
            ),
            active_support=payload.get(
                "active_support"
            )
        )

        save_market_state(
            market_state.to_dict()
        )

        logger.info(
            "Market state saved"
        )

    except Exception as e:

        logger.error(
            f"Market state save failed: {str(e)}"
        )