from pyrogram import Client, filters

api_id = 12345678  # api_id-и худа
api_hash = "da423286193d849661ef25b9d9bb1abe"
bot_token = "7840343781:AAHU9eSj-6X5OiRbMBz1UC5aQRm8GNqSgMA"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Салом! Ман зиндаам ва кор мекунам.")

app.run()
