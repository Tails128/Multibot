import json
from splitter import splitter
from handler import handler

# getting settings.json
with open('config.json') as f:
    config = f;

    # split commands in arrays ordered by priority
    config = splitter.splitByPriority(config)


## TODO: add regular commands to description for [/] function

## TODO: handle message (check if message triggers any command, elaborate, strict matching is assumed to be false)

## TODO: call telepot and start the bot
