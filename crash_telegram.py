# crash_telegram.py
import time
from telegram import Bot

TOKEN = "8494423217:AAHlpz6aIBq4B-LLV-h-fTpgdYvPnZ0ZB5E"
CHAT_ID = "1765024628"
CHECK_INTERVAL = 30
LOW_THRESHOLD = 1.3
STREAK_ALERT = 5

bot = Bot(token=TOKEN)

import crash_core as core

def get_streak():
    try:
        return core.detect_low_streak(threshold=LOW_THRESHOLD, window=STREAK_ALERT)
    except Exception:
        return 0

def send_start_message():
    bot.send_message(chat_id=CHAT_ID, text="✅ بوت التحليل شغّال الآن.")

def run_alert_loop():
    send_start_message()
    while True:
        streak = get_streak()
        if streak >= STREAK_ALERT:
            bot.send_message(
                chat_id=CHAT_ID,
                text=f"⚠️ تنبيه: سجل {streak} ضربة أقل من {LOW_THRESHOLD} على التوالي!"
            )
        time.sleep(CHECK_INTERVAL)
