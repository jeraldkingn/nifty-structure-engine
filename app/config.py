import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    # Supabase
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    # Telegram
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    # App
    APP_ENV = os.getenv("APP_ENV", "development")

    # Trading
    SYMBOL = os.getenv("SYMBOL", "NIFTY")

    # Cooldowns (minutes)
    BREAKOUT_COOLDOWN = int(
        os.getenv("BREAKOUT_COOLDOWN", 15)
    )

    BREAKDOWN_COOLDOWN = int(
        os.getenv("BREAKDOWN_COOLDOWN", 15)
    )

    BOUNCE_COOLDOWN = int(
        os.getenv("BOUNCE_COOLDOWN", 10)
    )

    REJECTION_COOLDOWN = int(
        os.getenv("REJECTION_COOLDOWN", 10)
    )

    # Confidence
    MIN_CONFIDENCE = int(
        os.getenv("MIN_CONFIDENCE", 70)
    )