"""Launch the bot."""
import json
import telepot
import os
import time
from splitter import Splitter
from handler import Handler


bot_name = "botNameHere"

# getting settings.json
with open('config.json') as f:
    config = json.load(f)

# split commands in arrays ordered by priority
splitter = Splitter()
config = splitter.splitByPriority(config)

# define the handler
handler = Handler()
handler.setMessages(config)

# define bot and handle the message loop via handler.handle
bot = telepot.Bot(os.environ['TELEGRAM_MULTIBOT_KEY'])
bot.message_loop(Handler.handle)

# a simple confermation in case the user wants a feedback over the bot starting
print(bot_name + ' successfully started!')

# loop to catch all the messages
while 1:
    time.sleep(10)
