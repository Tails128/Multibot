"""The manager which configures the bot and is able to launch it."""
import json
import telepot
from base.handler import Handler
from base import splitter
from bot_logging.logger import Logger

class BotManager():
    """Manager class. Mandatory since some parameters must be set."""

    messageHandler = Handler()
    triggers = None
    config = {}
    bot = None
    logger = None

    def init(self, logger, config_path, trigger_path):
        """Initialize the class."""
        message_handler = Handler()
        message_handler.set_logger(logger)
        self.logger = logger
        BotManager.load_config(self, config_path, trigger_path)

    @staticmethod
    def handle(msg):
        """Handle the message via messageHandler."""
        BotManager.messageHandler.handle(msg, BotManager.bot)

    def load_config(self, config_path, trigger_path):
        """Load the configuration from the json files."""

        # notice the user that the process has begun
        self.logger.log("setting up the bot...")

        with open(config_path) as file:
            BotManager.config = json.load(file)
        with open(trigger_path) as file:
            BotManager.triggers = json.load(file)

        bot_key = BotManager.config['BOT_KEY']
        BotManager.bot = telepot.Bot(bot_key)
        BotManager.split_messages()
        bot_name = BotManager.bot.getMe()['username']
        BotManager.messageHandler.set_botname(bot_name)

    @staticmethod
    def split_messages():
        """Split commands in arrays ordered by priority."""
        config_splitter = splitter.Splitter()
        BotManager.triggers = config_splitter.split_by_priority(BotManager.triggers)
        BotManager.messageHandler.set_messages(BotManager.triggers)

    @staticmethod
    def start_looping():
        """Start to listen for messages on telegram."""
        bot_name = BotManager.bot.getMe()['username']
        BotManager.bot.message_loop(BotManager.handle)
        Logger.log(bot_name + " is listening!")
