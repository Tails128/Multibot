"""Launch the bot."""
import json
import telepot
import os
import time
from base import splitter
from base import handler


bot_name = "botNameHere"

# getting settings.json
with open('config.json') as f:
    config = json.load(f)

# split commands in arrays ordered by priority
configSplitter = splitter.Splitter()
config = configSplitter.splitByPriority(config)

# define the handler
messageHandler = handler.Handler()
messageHandler.setMessages(config)

# define bot and handle the message loop via handler.handle
bot = telepot.Bot(os.environ['TELEGRAM_MULTIBOT_KEY'])
bot.message_loop(messageHandler.handle)

# a simple confermation in case the user wants a feedback over the bot starting
print(bot_name + ' successfully started!')

# loop to catch all the messages
while 1:
    time.sleep(10)
