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

        # notice the user that the process has begun
        logger.log("setting up the bot...")

        BotManager.__setup_logger(self, logger)
        BotManager.__setup_message_handler(logger)
        BotManager.__read_config_files(config_path, trigger_path)
        BotManager.__setup_bot_key()
        BotManager.__setup_bot_name()
        BotManager.__setup_bot_messages()

    @staticmethod
    def handle(msg):
        """Handle the message via messageHandler."""
        BotManager.messageHandler.handle(msg, BotManager.bot)

    @staticmethod
    def __read_config_files(config_path, trigger_path):
        with open(config_path) as file:
            BotManager.config = json.load(file)
        with open(trigger_path) as file:
            BotManager.triggers = json.load(file)

    @staticmethod
    def __setup_message_handler(logger):
        """Setup the message hander."""
        message_handler = Handler()
        message_handler.set_logger(logger)

    def __setup_logger(self, logger):
        """Setup the message handler and the logger."""
        self.logger = logger

    @staticmethod
    def __setup_bot_key():
        bot_key = BotManager.config['BOT_KEY']
        BotManager.bot = telepot.Bot(bot_key)

    @staticmethod
    def __setup_bot_name():
        bot_name = BotManager.bot.getMe()['username']
        BotManager.messageHandler.set_botname(bot_name)

    @staticmethod
    def __setup_bot_messages():
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
