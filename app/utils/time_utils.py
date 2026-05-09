from datetime import datetime
import pytz


IST = pytz.timezone("Asia/Kolkata")


def now_ist():
    return datetime.now(IST)


def current_time_string():
    return now_ist().strftime("%I:%M %p")


def current_date_string():
    return now_ist().strftime("%Y-%m-%d")