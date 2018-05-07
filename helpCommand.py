"""This document contains the class which registers the commands on /help."""


class HelpCommand():
    """The commandsManager generates a /help command."""

    commands = []

    def registerCommands(self, commands):
        """Register the /commands to help the user understand them."""
        for priorityList in commands:
            for item in priorityList:
                if item.get('trigger') == "/help":
                    continue
                if item.get('trigger')[0] == '/':
                    tempCommand = item.get('trigger').split('/')[1]
                    command = '*' + tempCommand + '*'
                    description = ''
                    if 'command_description' in item:
                        description = "\n" + item.get('command_description')
                    description += "\n\n"
                    self.commands.append(command + description)

    def cleanCommands(self):
        """Clean the commands variable."""
        self.commands = []
