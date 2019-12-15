"""This document contains the class which registers the commands on /help."""


class HelpCommand():
    """The commandsManager generates a /help command."""

    commands = []

    def registerCommands(self, commands):
        """Register the /commands to help the user understand them."""
        self.cleanCommands()
        for priorityList in commands:
            for item in priorityList:
                self.addValidCommand(item)

    def addValidCommand(self, commandItem):
        """Add valid commands to the list of commands to display with /help"""
        trigger = commandItem.get("trigger")
        if trigger is None:
            return

        isTriggerEmptyOrHelp = (trigger == "/help" or trigger == '')

        isCommandValid = not isTriggerEmptyOrHelp and trigger[0] == '/'
        if isCommandValid:
            self.commands.append(self.parseCommandItem(commandItem))

    def parseCommandItem(self, commandItem):
        """Parse a command item."""
        commandName = commandItem.get('trigger').split('/')[1]
        command = '*' + commandName + '*'
        description = ''
        if 'command_description' in commandItem:
            description = "\n" + commandItem.get('command_description')
        description += "\n\n"
        return command + description

    def cleanCommands(self):
        """Clean the commands variable."""
        self.commands = []

    def getHelpCommand(self):
        """Return the help command's text."""
        result = ""
        for command in self.commands:
            result += command
        return result
