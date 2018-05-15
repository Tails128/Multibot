"""Launch the bot."""
import json
import telepot
import time
from base import splitter
from base import handler
import sys


class manager():
    """Manager class. Mandatory since some parameters must be set."""

    messageHandler = handler.Handler()
    triggers = None
    config = None
    bot = None

    @staticmethod
    def handle(msg):
        """Handle the message via messageHandler."""
        manager.messageHandler.handle(msg, manager.bot)


# handle notice the user that the process has begun
print("setting up the bot...")
sys.stdout.flush()


with open('triggers.json') as f:
    manager.triggers = json.load(f)
with open('config.json') as f:
    manager.config = json.load(f)

botKey = manager.config['BOT_KEY']

# define the bot and the botname
manager.bot = telepot.Bot(botKey)
botName = manager.bot.getMe()['username']

# split commands in arrays ordered by priority
configSplitter = splitter.Splitter()
manager.triggers = configSplitter.splitByPriority(manager.triggers)

# define the handler
manager.messageHandler.setBotname(botName)
manager.messageHandler.setMessages(manager.triggers)

manager.bot.message_loop(manager.handle)
print(botName + " is listening!")
sys.stdout.flush()


# loop to catch all the messages
while 1:
    time.sleep(.3)
