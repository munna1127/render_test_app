from flask import Flask, request
import telebot
import os

# 🔹 Telegram bot token (replace with your bot token)
BOT_TOKEN = "8396162804:AAFv1RkLd4T8YUKgxbUocoraOYDVHU7ZdBM"

# 🔹 Create Flask app and Telebot instance
app = Flask(__name__)
bot = telebot.TeleBot(BOT_TOKEN)

# 🔹 Webhook route (Render ke liye use hoga)
@app.route(f"/{BOT_TOKEN}", methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

# 🔹 Start command
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello bhai 👋! Bot is working perfectly in Termux & Render.")

# 🔹 Any text message handler
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

# 🔹 Local mode ke liye (Termux me chalane ke liye)
if __name__ == "__main__":
    print("🤖 Bot is running locally...")
    bot.infinity_polling()
