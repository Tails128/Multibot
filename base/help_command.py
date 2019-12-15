"""This document contains the class which registers the commands on /help."""


class HelpCommand():
    """The commandsManager generates a /help command."""

    commands = []

    def register_commands(self, commands):
        """Register the /commands to help the user understand them."""
        self.clean_commands()
        for priority_list in commands:
            for item in priority_list:
                self.add_valid_command(item)

    def add_valid_command(self, command_item):
        """Add valid commands to the list of commands to display with /help"""
        trigger = command_item.get("trigger")
        if trigger is None:
            return

        is_trigger_empty_or_help = (trigger in ("/help", ''))

        is_command_valid = not is_trigger_empty_or_help and trigger[0] == '/'
        if is_command_valid:
            self.commands.append(self.parse_command_item(command_item))

    @staticmethod
    def parse_command_item(command_item):
        """Parse a command item."""
        command_name = command_item.get('trigger').split('/')[1]
        command = '*' + command_name + '*'
        description = ''
        if 'command_description' in command_item:
            description = "\n" + command_item.get('command_description')
        description += "\n\n"
        return command + description

    def clean_commands(self):
        """Clean the commands variable."""
        self.commands = []

    def get_help_command(self):
        """Return the help command's text."""
        return "".join(self.commands)