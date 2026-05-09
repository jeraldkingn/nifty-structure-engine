from datetime import datetime, timedelta

from app.config import Config


last_alert_times = {}


COOLDOWNS = {
    "BREAKOUT": Config.BREAKOUT_COOLDOWN,
    "BREAKDOWN": Config.BREAKDOWN_COOLDOWN,
    "SUPPORT_BOUNCE": Config.BOUNCE_COOLDOWN,
    "RESISTANCE_REJECTION": Config.REJECTION_COOLDOWN,
    "FAKE_BREAKOUT": 10
}


def can_send_alert(signal):

    now = datetime.utcnow()

    cooldown_minutes = COOLDOWNS.get(signal, 10)

    last_time = last_alert_times.get(signal)

    if last_time is None:
        last_alert_times[signal] = now
        return True

    difference = now - last_time

    if difference > timedelta(minutes=cooldown_minutes):

        last_alert_times[signal] = now
        return True

    return False