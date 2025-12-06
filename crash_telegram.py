# crash_telegram.py
import time
from telegram import Bot

TOKEN = "PUT_YOUR_TOKEN_HERE"
CHAT_ID = "PUT_YOUR_CHAT_ID_HERE"
CHECK_INTERVAL = 30
LOW_THRESHOLD = 1.3
STREAK_ALERT = 5

bot = Bot(token=TOKEN)

def fallback_detect_low_streak():
    return 0

try:
    import crash_core as core
    has_core = True
except Exception:
    has_core = False
    core = None

def get_streak():
    if has_core:
        try:
            return core.detect_low_streak(threshold=LOW_THRESHOLD, window=STREAK_ALERT)
        except Exception as e:
            print("error:", e)
            return fallback_detect_low_streak()
    return fallback_detect_low_streak()

def send_start_message():
    try:
        bot.send_message(chat_id=CHAT_ID, text="Bot Started")
    except Exception as e:
        print("send_start failed:", e)

def run_alert_loop():
    send_start_message()
    while True:
        try:
            s = get_streak()
            print("streak:", s)
            if s >= STREAK_ALERT:
                bot.send_message(chat_id=CHAT_ID, text=f"ALERT: {s} lows in a row (<{LOW_THRESHOLD})")
            time.sleep(CHECK_INTERVAL)
        except Exception as e:
            print("loop error:", e)
            time.sleep(10)

if __name__ == "__main__":
    run_alert_loop()
