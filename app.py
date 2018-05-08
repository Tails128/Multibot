"""Launch the bot."""
import json
from splitter import Splitter
from handler import Handler

# getting settings.json
with open('config.json') as f:
    config = json.load(f)

# split commands in arrays ordered by priority
splitter = Splitter()
config = splitter.splitByPriority(config)

handler = Handler()
handler.setMessages(config)

# TODO: handle message (check if message triggers any command, elaborate,
# strict matching is assumed to be false)

# TODO: call telepot and start the bot
