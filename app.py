"""Launch the bot."""
import json
import telepot
import time
import os
from base import splitter
from base.handler import Handler
from bot_logging.logger import Logger


class manager():
    """Manager class. Mandatory since some parameters must be set."""

    messageHandler = Handler()
    triggers = None
    config = None
    bot = None

    @staticmethod
    def init(logger):
        """Initialize the class."""
        messageHandler = Handler()
        messageHandler.setLogger(logger)

    @staticmethod
    def handle(msg):
        """Handle the message via messageHandler."""
        manager.messageHandler.handle(msg, manager.bot)


# setup the logger
basePath = os.getcwd()
now = str(time.time())
Logger.setFileName("logs\\log" + now)
Logger.enableFileLog()
Logger.enableConsoleLog()

manager.init(Logger)

# notice the user that the process has begun
Logger.log("setting up the bot...")


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
Logger.log(botName + " is listening!")


# loop to catch all the messages
while 1:
    time.sleep(.3)
