"""Launch the bot."""
import time
import os
from bot_logging.logger import Logger
from base.bot_manager import BotManager

# get base infos
BASE_PATH = os.getcwd()
NOW = str(time.time())

# create the logger
Logger.set_file_name("logs\\log" + NOW)
Logger.enable_file_log()
Logger.enable_console_log()

# start the bot
BOT_MANAGER = BotManager()
BOT_MANAGER.init(Logger, 'config.json', 'triggers.json')
BotManager.start_looping()

# loop to catch all the messages
while 1:
    time.sleep(.3)
