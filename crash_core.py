# crash_core.py
import random

current_streak = 0

def detect_low_streak(threshold=1.3, window=5):
    global current_streak
    value = round(random.uniform(1.0, 3.0), 2)
    print("test value:", value)
    if value < threshold:
        current_streak += 1
    else:
        current_streak = 0
    return current_streak
