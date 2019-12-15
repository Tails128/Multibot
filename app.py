"""Launch the bot."""
import time
import os
from bot_logging.logger import Logger
from base.BotManager import BotManager

# get base infos
basePath = os.getcwd()
now = str(time.time())

# create the logger
Logger.setFileName("logs\\log" + now)
Logger.enableFileLog()
Logger.enableConsoleLog()

# start the bot
botManager = BotManager()
botManager.init(Logger, 'config.json', 'triggers.json')
BotManager.startLooping()

# loop to catch all the messages
while 1:
    time.sleep(.3)
