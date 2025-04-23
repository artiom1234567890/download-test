from flask import Flask
from pyrogram import Client, filters
import threading
import os

api_id = int(os.environ.get("21110543"))
api_hash = os.environ.get("da423286193d849661ef25b9d9bb1abe")
bot_token = os.environ.get("7840343781:AAHU9eSj-6X5OiRbMBz1UC5aQRm8GNqSgMA")

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Бот фаъол аст!")

def run_bot():
    app.run()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    flask_app.run(host="0.0.0.0", port=8000)
