import requests
import time
import telegram
from datetime import datetime

TOKEN = "7697706108:AAF9DiBS6kaOMccog9_x7CFeIhJrZdFkXE0"
CHAT_ID = "7928410277"
bot = telegram.Bot(token=TOKEN)

FOREX_PAIRS = [
    "EUR/USD", "USD/JPY", "GBP/USD", "USD/CHF",
    "AUD/USD", "USD/CAD", "NZD/USD", "EUR/GBP",
    "EUR/JPY", "GBP/JPY"
]

def get_trend(pair):
    # Simulated logic — Replace with real API later
    # Randomly assign trends
    import random
    trend = random.choice(["UP", "DOWN", "NEUTRAL"])
    strength = random.choice(["Strong", "Medium", "Weak"])
    return trend, strength

def send_alert(pair, trend, strength):
    now = datetime.utcnow().strftime("%H:%M GMT")
    message = f"📢 TREND ALERT: {pair}\n"
    emoji = "🟢" if trend == "UP" else "🔴" if trend == "DOWN" else "⚪"
    message += f"{emoji} Trend: {trend} ✅\n"
    message += f"💪 Strength: {strength}\n"
    message += f"🕒 Time: {now}"
    bot.send_message(chat_id=CHAT_ID, text=message)

while True:
    for pair in FOREX_PAIRS:
        trend, strength = get_trend(pair)
        send_alert(pair, trend, strength)
        time.sleep(2)  # small delay between pairs
    time.sleep(900)  # wait 15 minutes before next full scan
