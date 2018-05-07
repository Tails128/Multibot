"""Test HelpCommand class."""
from helpCommand import HelpCommand


def test_registerCommands():
    """Test the registerCommands function."""
    commands = [[{"trigger": "/test",
                 "command_description": "the test works!"}]]
    testHelpCommand = HelpCommand()
    testHelpCommand.registerCommands(commands)
    assert testHelpCommand.commands == ["*test*\nthe test works!\n\n"]


def test_cleanCommands():
    """Test the cleanCommands function."""
    """Test the registerCommands function."""
    commands = [[{"trigger": "/test",
                 "command_description": "the test works!"}]]
    testHelpCommand = HelpCommand()
    testHelpCommand.registerCommands(commands)
    testHelpCommand.cleanCommands()
    assert testHelpCommand.commands == []
