import json
import telepot
from base.handler import Handler
from bot_logging.logger import Logger
from base import splitter

class BotManager():
    """Manager class. Mandatory since some parameters must be set."""

    messageHandler = Handler()
    triggers = None
    config = {}
    bot = None
    logger = None

    def init(self, logger, configPath, triggerPath):
        """Initialize the class."""
        messageHandler = Handler()
        messageHandler.setLogger(logger)
        self.logger = logger
        BotManager.loadConfig(self, configPath, triggerPath)

    @staticmethod
    def handle(msg):
        """Handle the message via messageHandler."""
        BotManager.messageHandler.handle(msg, BotManager.bot)

    def loadConfig(self, configPath, triggerPath):
        # notice the user that the process has begun
        self.logger.log("setting up the bot...")

        with open(configPath) as f:
            BotManager.config = json.load(f)
        with open(triggerPath) as f:
            BotManager.triggers = json.load(f)

        botKey = BotManager.config['BOT_KEY']
        BotManager.bot = telepot.Bot(botKey)
        BotManager.splitMessages()
        botName = BotManager.bot.getMe()['username']
        BotManager.messageHandler.setBotname(botName)
        
    @staticmethod
    def splitMessages():
        # split commands in arrays ordered by priority
        configSplitter = splitter.Splitter()
        BotManager.triggers = configSplitter.splitByPriority(BotManager.triggers)
        BotManager.messageHandler.setMessages(BotManager.triggers)

    @staticmethod
    def startLooping():
        botName = BotManager.bot.getMe()['username']
        BotManager.bot.message_loop(BotManager.handle)
        Logger.log(botName + " is listening!")
