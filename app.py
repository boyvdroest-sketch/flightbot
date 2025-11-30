from flask import Flask
import threading
import time

# Import your bot
from bot import bot

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Bot is running on Render!"

def run_bot():
    print("🤖 Starting bot polling...")
    bot.polling(none_stop=True)

# Start bot in a separate thread
bot_thread = threading.Thread(target=run_bot)
bot_thread.daemon = True
bot_thread.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
